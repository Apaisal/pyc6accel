#!/usr/bin/env python
# -=- encoding: utf-8 -=-
import pygtk
pygtk.require('2.0')
import sys, os
import gobject
gobject.threads_init()
import pygst
pygst.require("0.10")
#import glib
import gst
import gst.interfaces
import gtk
gtk.gdk.threads_init()
import cv

class VideoWidget(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.imagesink = None
        self.unset_flags(gtk.DOUBLE_BUFFERED)

    def do_expose_event(self, event):
        if self.imagesink:
            self.imagesink.expose()
            return False
        else:
            return True

    def set_sink(self, sink):
        assert self.window.xid
        self.imagesink = sink
        self.imagesink.set_xwindow_id(self.window.xid)


class Main:
    def __init__(self):
        self.HEIGHT = 480
        self.WIDTH = 640
        self.REMOTE_HOST = 'rtsp://158.108.47.75:554/h264.sdp?res=full&x0=0&y0=0&x1=%d&y1=%d' % (self.WIDTH, self.HEIGHT)
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("H.264 Player")
        window.set_default_size(640, 480)
        window.connect("destroy", gtk.main_quit, "WM destroy")
        vbox = gtk.VBox()
        vbox.show()
        window.add(vbox)
        self.video_widget = VideoWidget()
        self.video_widget.show()
        vbox.pack_start(self.video_widget, True, True, 0)
        hbox = gtk.HBox()
        hbox.set_border_width(10)
        self.capture_btn = gtk.Button("Capture")
        self.capture_btn.connect("clicked", self.capture_btn_clicked)
        self.debug = gtk.CheckButton()
        self.debug.set_label("Debug")
        self.debug.set_active(True)
        self.entry = gtk.Entry()
        self.entry.set_text(self.REMOTE_HOST)
        self.button = gtk.Button("Start")
        self.button.connect("clicked", self.on_start_stop_btn_clicked)
        hbox.pack_start(self.debug)
        vbox.pack_start(hbox, False)
        vbox.pack_start(self.entry, False)
        hbox.pack_end(self.capture_btn, False)
        hbox.pack_end(self.button, False)
        window.show_all()

        #/* Create gstreamer elements */
        self.pipeline = gst.Pipeline('player')

        source = gst.element_factory_make('rtspsrc', 'source')
        source.set_property('location', self.REMOTE_HOST)
        source.connect("pad-added", self.source_pad_added)
#        source.connect("no-more-pads", self.source_no_more_pads)
#        source.connect("pad-removed", self.source_pad_removed)
        self.pipeline.add(source)

        depayload = gst.element_factory_make('rtph264depay', 'depayload')
        self.pipeline.add(depayload)

        decoder = gst.element_factory_make('ffdec_h264', 'decoder')
        self.pipeline.add(decoder)

#        textoverlay = gst.element_factory_make('textoverlay')
#        textoverlay.set_property("text", "H264 Real Streaming")
#        textoverlay.set_property("font-desc", "normal 14")
#        textoverlay.set_property("halign", "right")
#        textoverlay.set_property("valign", "top")

        conv1 = gst.element_factory_make('ffmpegcolorspace', 'conv1')
        self.pipeline.add(conv1)
        conv2 = gst.element_factory_make('ffmpegcolorspace', 'conv2')
        self.pipeline.add(conv2)
        #/* Tee that copies the stream to multiple outputs */
        tee = gst.element_factory_make("tee", "tee")
        self.pipeline.add(tee)

        screen_queue = gst.element_factory_make("queue", "screen_queue");
        self.pipeline.add(screen_queue)

#        /* Creates separate thread for the stream from which the image
#         * is captured */
        image_queue = gst.element_factory_make("queue", "image_queue");
        self.pipeline.add(image_queue)

        try :
            screen_sink = gst.element_factory_make ("xvimagesink", "screen_sink");
        except:
            try :
                screen_sink = gst.element_factory_make ("ximagesink", "screen_sink");
            except:
                gst.error("Could not create neither 'xvimagesink' nor 'ximagesink' element");

        image_sink = gst.element_factory_make('fakesink', 'image_sink')
        image_sink.set_property("signal-handoffs", True)
        image_sink.connect('handoff', self.fsink_handoff_handle)

        screen_sink.set_property('sync', 'true')
        image_sink.set_property('sync', 'true')
        self.pipeline.add(screen_sink)
        self.pipeline.add(image_sink)

        caps_yuv = gst.caps_from_string("video/x-raw-yuv,width=%d,height=%d" % (self.WIDTH, self.HEIGHT))
        caps_rgb = gst.caps_from_string("video/x-raw-rgb,width=%d,height=%d" % (self.WIDTH, self.HEIGHT))

        #/* Set up the pipeline */
        gst.element_link_many(depayload, decoder)
#        gst.element_link_many(screen_queue, screen_sink)
#        gst.element_link_many(image_queue, image_sink)

        decoder.link(conv1, caps_yuv)
        conv1.link(tee, caps_rgb)
        tee.link(screen_queue)
        screen_queue.link(conv2)
        conv2.link(screen_sink)

        tee.link(image_queue)
        image_queue.link(image_sink)

        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("sync-message::element", self.on_sync_message)
        bus.connect("message", self.on_message)

    def fsink_handoff_handle(self, element, buff, pad):
        ''''''
        self.buffer = buff.copy_on_write()
#        print pad

    def source_pad_added(self, element, pad):
        ''''''
        depay = self.pipeline.get_by_name('depayload').get_pad("sink")
        pad.link(depay)

    def capture_btn_clicked(self, events):
        success, state, pending = self.pipeline.get_state(1)
        if not pending:
            if state == gst.STATE_PLAYING:
                if len(self.buffer) > 0:
                    print len(self.buffer)
                    cv_im = cv.CreateImageHeader((self.WIDTH, self.HEIGHT), cv.IPL_DEPTH_8U, 3)
                    cv.SetData(cv_im, self.buffer)

                    cv.ShowImage("Image captured", cv_im)
                    cv.WaitKey()
                else:
                    print "Image failed"
    def on_start_stop_btn_clicked(self, event):
        if self.button.get_label() == "Start":
            self.REMOTE_HOST = self.entry.get_text()
            debug = self.debug.state
            self.pipeline.get_by_name("source").set_property("location", self.REMOTE_HOST)
            if debug :
                 self.pipeline.get_by_name("source").set_property("debug", debug)
#                 self.pipeline.get_by_name('decoder').set_property("debug_mv", debug)
            self.button.set_label("Stop")
            self.pipeline.set_state(gst.STATE_PLAYING)
        else:
            self.button.set_label("Start")
            self.pipeline.set_state(gst.STATE_NULL)


    def on_message(self, bus, message):
        if message.type == gst.MESSAGE_EOS:
            self.pipeline.set_state(gst.STATE_NULL)
            self.button.set_label("Start")
        elif message.type == gst.MESSAGE_ERROR:
            self.pipeline.set_state(gst.STATE_NULL)
            self.button.set_label("Start")
            err, debug = message.parse_error()
            print "Error: %s" % err, debug

    def on_sync_message(self, bus, message):
        print 'Sync Message'
        if message.structure is None:
            return
        if message.structure.get_name() == "prepare-xwindow-id":
            # Assign the viewport
            gtk.gdk.threads_enter()
            gtk.gdk.display_get_default().sync()
            self.video_widget.set_sink(message.src)
            message.src.set_property("force-aspect-ratio", True)
            message.src.set_property("synchronous", True)
            gtk.gdk.threads_leave()

def main():
    # Need to register our derived widget types for implicit event
    # handlers to get called.
#    gobject.type_register(Main)
    gobject.type_register(VideoWidget)

    main = Main()
    gtk.main()

if __name__ == '__main__':
    sys.exit(main())
