#!/usr/bin/env python
# -=- encoding: utf-8 -=-

import gobject, pygst
import gst
import sys
import os
import readline
import glib
import gtk



class Main:
    def __init__(self):
        self.REMOTE_HOST = 'rtsp://158.108.47.75:554/h264.sdp?res=half'
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("H264-Player")
        window.set_default_size(640, 480)
        window.connect("destroy", gtk.main_quit, "WM destroy")
        vbox = gtk.VBox()
        window.add(vbox)
        self.movie_window = gtk.DrawingArea()
        vbox.add(self.movie_window)
        hbox = gtk.HBox()
        hbox.set_border_width(10)

        self.debug = gtk.CheckButton()
        self.debug.set_label("Debug")
        self.debug.set_active(True)
        self.entry = gtk.Entry()
        self.entry.set_text(self.REMOTE_HOST)
        self.button = gtk.Button("Start")
        self.button.connect("clicked", self.start_stop)
        hbox.pack_start(self.debug)
        vbox.pack_start(hbox, False)
        vbox.pack_start(self.entry, False)
        hbox.pack_end(self.button, False)

        window.show_all()

        #/* Create gstreamer elements */
        self.player = gst.Pipeline('player')

        source = gst.element_factory_make('rtspsrc', 'rtspsource')
        source.connect("pad-added", self.source_pad_added)
#        source.connect("no-more-pads", self.source_no_more_pads)
#        source.connect("pad-removed", self.source_pad_removed)
        source.set_property('location', self.REMOTE_HOST)

        self.depayload = gst.element_factory_make('rtph264depay', 'depayload')

        decoder = gst.element_factory_make('ffdec_h264', 'decoder')

        caps = gst.Caps("video/x-raw-yuv, width=1280, height=720")
        filter = gst.element_factory_make("capsfilter", "filter")
        filter.set_property("caps", caps)

        textoverlay = gst.element_factory_make('textoverlay')
        textoverlay.set_property("text", "H264 Real Streaming")
        textoverlay.set_property("font-desc", "normal 14")
        textoverlay.set_property("halign", "right")
        textoverlay.set_property("valign", "top")


        conv = gst.element_factory_make ("ffmpegcolorspace", "conv")

#        sink = gst.element_factory_make('filesink', 'sink')
        sink = gst.element_factory_make("xvimagesink", "video-output")

#        sink = gst.element_factory_make('ximagesink', 'sink')
#        sink = gst.element_factory_make('fakesink', 'sink')
        sink.set_property('location', 'test.264')
        sink.set_property('sync', 'true')


        #/* Set up the pipeline */
        self.player.add(source, self.depayload, decoder, filter, sink)
        gst.element_link_many(self.depayload, decoder, filter, sink)

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.on_message)
        bus.connect("sync-message::element", self.on_sync_message)

    def source_pad_removed(self, obj, pad):
        '''
        
        @param params:
        '''
        print 'pad_removed'

    def source_no_more_pads(self, obj):
        ''''''
        print obj

    def source_pad_added(self, obj, pad):
        ''''''
        depay = self.depayload.get_pad("sink")
        pad.link(depay)


    def start_stop(self, w):
        if self.button.get_label() == "Start":
            self.REMOTE_HOST = self.entry.get_text()
            debug = self.debug.get_state()
            self.button.set_label("Stop")
            self.player.get_by_name("rtspsource").set_property("location", self.REMOTE_HOST)

            if debug :
                 self.player.get_by_name("rtspsource").set_property("debug", debug)

            self.player.set_state(gst.STATE_PLAYING)
        else:
            self.player.set_state(gst.STATE_NULL)
            self.button.set_label("Start")


    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.button.set_label("Start")

        elif t == gst.MESSAGE_ERROR:
            self.button.set_label("Start")
            self.player.set_state(gst.STATE_NULL)
            err, debug = message.parse_error()
            print "Error: %s" % err, debug

    def on_sync_message(self, bus, message):
        if message.structure is None:
            return
        message_name = message.structure.get_name()
        print message_name
        if message_name == "prepare-xwindow-id":
            # Assign the viewport
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(self.movie_window.window.xid)


main = Main()
gtk.gdk.threads_init()
gtk.main()

