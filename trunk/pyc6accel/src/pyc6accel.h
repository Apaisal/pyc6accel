/*
 * pyc6accel.h
 *
 *  Created on: Nov 4, 2010
 *      Author: anol
 */

#ifndef PYC6ACCEL_H_
#define PYC6ACCEL_H_

/*OpenCV*/
#include <cv.h>
#include <cxcore.h>
#include <cvaux.h>
#include <highgui.h>

#define VERSION	"0.1"
#define MODULESTR "pyc6accel"
#define ENGINENAME "omap3530"
#define ALGNAME "c6accel"
#define APPNAME MODULESTR
#define DEFAULT_ENGINE_NAME	"decode"

#define MAX_CODEC_NAME_SIZE     30
#define MAX_ENGINE_NAME_SIZE    30

/* Types of thresholding */
#define THRESH_GREATER2MAX      10  /* value = value > threshold ? max_value : value       */
#define THRESH_GREATER2THRES  11  /* value = value > threshold ? threshold : value       */
#define THRESH_LESS2MIN       12  /* value = value > threshold ? threshold : min_value   */
#define THRESH_LESS2THRES      13  /* value = value > threshold ? value : threshold           */

#define BUFFSIZE 1024

// Define a structure to allow benchmarking using gettimeofday()
//typedef struct Time_Object {
//    struct timeval original;
//    struct timeval previous;
//} Time_Object;

typedef struct {
	PyObject_HEAD
	IplImage *a;
	PyObject *data;
	size_t offset;
} iplimage_t;

typedef struct {
	PyObject_HEAD
	CvMat *a;
	PyObject *data;
	size_t offset;
} cvmat_t;

typedef struct {
	PyObject_HEAD
	CvMatND *a;
	PyObject *data;
	size_t offset;
} cvmatnd_t;

typedef struct {
	PyObject_HEAD
	IplConvKernel *a;
	PyObject *data;
	size_t offset;
} iplconvkernel_t;

int getGaussianKernel(unsigned char * out_dat, int ksize);

#endif /* PYC6ACCEL_H_ */
