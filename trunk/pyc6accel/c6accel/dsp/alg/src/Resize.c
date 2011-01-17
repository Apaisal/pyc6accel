/*
 Resize.c

 Created on: Jan 16, 2011
 Author: anol
 */

#include <xdc/std.h>
#include <ti/sdo/dmai/Dmai.h>
#include <ti/sdo/dmai/Resize.h>
#include <ti/sdo/dmai/BufferGfx.h>

void IMG_Resize() {
//	BufferGfx_Attrs gfxAttrs = BufferGfx_Attrs_DEFAULT;
//	Resize_Attrs rszAttrs = Resize_Attrs_DEFAULT;
//	Buffer_Handle inBuf, outBuf;
//	Capture_Handle hCap;
//	Resize_Handle hResize;
//	Int32 bufSize;
//
//	Dmai_init();
//	bufSize = BufferGfx_calcSize(VideoStd_D1_NTSC, ColorSpace_420P);
//	BufferGfx_calcDimensions(VideoStd_D1_NTSC, ColorSpace_420P, &gfxAttrs.dim);
//	gfxAttrs.colorSpace = ColorSpace_420P;
//	outBuf = Buffer_create(bufSize, Buffer_getBufferAttrs(&gfxAttrs));
//
//	bufSize = BufferGfx_calcSize(VideoStd_720P, ColorSpace_420P);
//	BufferGfx_calcDimensions(VideoStd_720P, ColorSpace_420P, &gfxAttrs.dim);
//	gfxAttrs.colorSpace = ColorSpace_420P;
//	inBuf = Buffer_create(bufSize, Buffer_getBufferAttrs(&gfxAttrs));
//
//	Resize_create(&rszAttrs);
//	Resize_config(hInBuf, hOutBuf);
//	// Fill hInBuf with video data
//	Resize_execute(hResize, inBuf, outBuf);
//
//	Buffer_delete(inBuf);
//	Buffer_delete(outBuf);
//	Resize_delete(hResize);
}
