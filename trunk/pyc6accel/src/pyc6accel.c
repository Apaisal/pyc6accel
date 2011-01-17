/*
 * pyc6accel.c
 *
 *  Created on: Nov 4, 2010
 *      Author: anol
 */

/* Standard includes */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <strings.h>

/* system time include*/
#include <sys/time.h>

/* Python includes */
#include <Python.h>
#include <structmember.h>

/* PyC6Accel include*/
#include "pyc6accel.h"

/* Codec Engine and xdc includes */
#include <xdc/std.h>
#include <ti/sdo/ce/Engine.h>
#include <ti/sdo/ce/CERuntime.h>
#include <ti/sdo/ce/osal/Memory.h>

/* This object is used in MACRO in benchmark.h */
static Time_Object sTime;
static UInt32 dtime;

/*Define a C6Accel Handle to call the abstracted wrapper APIs*/
#include "../c6accelw/c6accelw.h"

#define START_BENCHMARK()                                     \
		Time_reset(&sTime);						\
		Time_delta(&sTime,&dtime);
#define END_BENCHMARK()                             \
		Time_delta(&sTime,&dtime);                                \
		printf("%f\n",(unsigned int)dtime / 1000.);

static C6accel_Handle hC6 = NULL;
static Memory_AllocParams memParams;

static String algName = ALGNAME;
static String engineName = ENGINENAME;

static PyObject *py6accel_error;

static int failmsg(const char *fmt, ...) {
	char str[1000];

	va_list ap;
	va_start(ap, fmt);
	vsnprintf(str, sizeof(str), fmt, ap);
	va_end(ap);

	PyErr_SetString(PyExc_TypeError, str);
	return 0;
}

static void Time_reset(Time_Object *sTime) {
	struct timeval tv;

	if (gettimeofday(&tv, NULL) == -1) {
		return;
	}

	sTime->original = tv;
	sTime->previous = tv;

	return;
}

static void Time_delta(Time_Object* sTime, UInt32 *deltaPtr) {
	struct timeval tv;
	time_t s;
	suseconds_t us;

	if (gettimeofday(&tv, NULL) == -1) {
		return;
	}

	s = tv.tv_sec - sTime->previous.tv_sec;
	us = tv.tv_usec - sTime->previous.tv_usec;

	*deltaPtr = s * 1000000l + us;

	sTime->previous = tv;

	return;
}

static PyObject *
pyc6accel_img_adds(PyObject *self, PyObject *args)
{
	PyObject *src, *dst;
	IplImage *img, *adds;
	int value;

	if (!PyArg_ParseTuple(args, "OiO", &src, &value, &dst))
		return NULL;

	img = ((iplimage_t *) src)->a;
	adds = ((iplimage_t *) dst)->a;

	START_BENCHMARK();
	C6accel_IMG_addS_8(hC6, img, adds, (char) value, img->imageSize);

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();

	return Py_None;
}

static PyObject *
pyc6accel_img_add(PyObject *self, PyObject *args)
{
	PyObject *src1, *src2, *dst;
	IplImage *img1, *img2, *adds;
	int value;

	if (!PyArg_ParseTuple(args, "OOO", &src1, &src2, &dst))
		return NULL;

	img1 = ((iplimage_t *) src1)->a;
	img2 = ((iplimage_t *) src2)->a;
	adds = ((iplimage_t *) dst)->a;

	START_BENCHMARK();
	C6accel_IMG_add_16s(hC6, (short*) img1->imageData,
	        (short*) img2->imageData, (short*) adds->imageData, adds->height
	                * adds->widthStep);

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();

	return Py_None;
}

static PyObject *
pyc6accel_img_subs(PyObject *self, PyObject *args)
{
	PyObject *src, *dst;
	IplImage *img, *subs;
	int value;

	if (!PyArg_ParseTuple(args, "OiO", &src, &value, &dst))
		return NULL;

	img = ((iplimage_t *) src)->a;
	subs = ((iplimage_t *) dst)->a;

	printf("Start AddS\n");

	START_BENCHMARK();
	C6accel_IMG_subS_8(hC6, img, subs, (char) value, img->imageSize);

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();

	return Py_None;
}

static PyObject *
pyc6accel_img_cvtcolor(PyObject *self, PyObject *args)
{
	PyObject *src, *dst;
	IplImage *color, *gray;
	int code;

	if (!PyArg_ParseTuple(args, "OOi", &src, &dst, &code))
		return NULL;

	color = ((iplimage_t *) src)->a;
	gray = ((iplimage_t *) dst)->a;

	START_BENCHMARK();
	switch (code) {
		case CV_RGB2GRAY:
			C6accel_IMG_rgb_to_y(hC6, color, gray, gray->imageSize);
			break;
		default:
			failmsg("This convert code can not support @ version %s", VERSION);
			goto END;
			//			break;
	}

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();
	END: return Py_None;
}

static PyObject *
pyc6accel_img_sobel(PyObject *self, PyObject *args)
{
	PyObject *src, *dst;
	IplImage *org, *sobel;
	int kernel;

	if (!PyArg_ParseTuple(args, "OOi", &src, &dst, &kernel))
		return NULL;

	org = ((iplimage_t *) src)->a;
	sobel = ((iplimage_t *) dst)->a;

	START_BENCHMARK();
	switch (kernel) {
		case 3:
			C6accel_IMG_sobel_3x3_8(hC6, org, sobel,
			        (short int) sobel->widthStep, (short int) sobel->height);
			break;
		case 5:
		case 7:
		default:
			failmsg("This kernel can not support @ version %s", VERSION);
			goto END;
			//			break;
	}

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();
	END: return Py_None;
}

static PyObject *
pyc6accel_img_threshold(PyObject *self, PyObject *args)
{
	PyObject *src, *dst;
	IplImage *input, *output;
	int threshold;
	int thresholdType;

	if (!PyArg_ParseTuple(args, "OOii", &src, &dst, &threshold, &thresholdType))
		return NULL;

	input = ((iplimage_t *) src)->a;
	output = ((iplimage_t *) dst)->a;

	START_BENCHMARK();
	switch (thresholdType) {
		//				case CV_THRESH_BINARY:
		case THRESH_GREATER2MAX:
			C6accel_IMG_thr_gt2max_8(hC6, (unsigned char*) input->imageData,
			        (unsigned char*) output->imageData,
			        (short) output->widthStep, (short) output->height,
			        (unsigned char) threshold);
			break;
			//				case CV_THRESH_BINARY:
		case THRESH_GREATER2THRES:
			C6accel_IMG_thr_gt2thr_8(hC6, (unsigned char*) input->imageData,
			        (unsigned char*) output->imageData,
			        (short) output->widthStep, (short) output->height,
			        (unsigned char) threshold);
			break;
		case THRESH_LESS2MIN:
			C6accel_IMG_thr_le2min_8(hC6, (unsigned char*) input->imageData,
			        (unsigned char*) output->imageData,
			        (short) output->widthStep, (short) output->height,
			        (unsigned char) threshold);
			break;
		case THRESH_LESS2THRES:
			C6accel_IMG_thr_le2thr_8(hC6, (unsigned char*) input->imageData,
			        (unsigned char*) output->imageData,
			        (short) output->widthStep, (short) output->height,
			        (unsigned char) threshold);
			break;
		default:
			failmsg("This kernel can not support @ version %s", VERSION);
			goto END;
			//			break;
	}

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();
	END: return Py_None;
}

static PyObject*
pyc6accel_img_erode(PyObject *self, PyObject *args)
{
	PyObject *src, *mask, *dst;
	IplImage *img, *out;
	IplConvKernel * element;
	int iterations;

	if (!PyArg_ParseTuple(args, "OOOi", &src, &dst, &mask, &iterations))
		return NULL;

	img = ((iplimage_t *) src)->a;
	out = ((iplimage_t *) dst)->a;
	element = ((iplconvkernel_t *) mask)->a;

	START_BENCHMARK();
	C6accel_IMG_erode_bin(hC6, img, out, element, iterations);

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();

	return Py_None;
}

static PyObject*
pyc6accel_img_dilate(PyObject *self, PyObject *args)
{
	PyObject *src, *mask, *dst;
	IplImage *img, *out;
	IplConvKernel * element;
	int iterations;

	if (!PyArg_ParseTuple(args, "OOOi", &src, &dst, &mask, &iterations))
		return NULL;

	img = ((iplimage_t *) src)->a;
	out = ((iplimage_t *) dst)->a;
	element = ((iplconvkernel_t *) mask)->a;

	START_BENCHMARK();
	C6accel_IMG_dilate_bin(hC6, img, out, element, iterations);

	if (C6Accel_readCallType(hC6) == ASYNC)
		C6accel_waitAsyncCall(hC6);
	END_BENCHMARK();

	return Py_None;
}

int getGaussianKernel(unsigned char * out_dat, int ksize) {
	int i, j;
	float *rows;
	float alpha = 1;
	float sigma = 1.4;
	if (!(ksize > 0 && ksize % 2 == 1)) {
		return -1;
	}

	if (sigma < 0) {
		sigma = 0.3 * ((ksize / 2) - 1) + 0.8;
	}
	alpha = 1.0 / (sqrt(2 * M_PI) * sigma);
	rows = alloca(ksize * SIZEOF_FLOAT);
	for (i = 0; i < ksize; ++i) {
		rows[i] = alpha * exp(-pow(i - (ksize - 1) / 2, 2) / pow(2 * sigma, 2));
	}
	printf("Gaussian mask.\n");
	for (i = 0; i < ksize; ++i) {
		for (j = 0; j < ksize; ++j) {
			*out_dat = rows[j] * rows[i] * 255;
#ifdef DEBUG
			printf("|%2d|", *out_dat);
#endif
			out_dat++;
		}
		printf("\n");
	}
	return 0;
}

static PyObject * loadiplimage(PyObject *self, PyObject *args) {
	PyObject *src;
	if (!PyArg_ParseTuple(args, "O", &src))
		return NULL;
	IplImage* ipl = ((iplimage_t *) src)->a;
	//	PyTypeObject *obj = src->ob_type;
	printf("iplimage pyobject i = %i\n", ipl->imageSize);
	printf("iplimage pyobject s = %s\n", ipl->imageData);
	ipl->imageData[0] = 255;
	ipl->imageData[1] = 255;
	ipl->imageData[2] = 255;
	return src;
}

static PyMethodDef pyc6accel_methods[] =
	{
	        //		        {
	        //		                "canny", (PyCFunction) pyc6accel_canny, METH_VARARGS,
	        //		                "Canny Edge Filter" },
		        {
		                "Add", (PyCFunction) pyc6accel_img_add, METH_VARARGS,
		                "Add -> None" },
		        {
		                "AddS", (PyCFunction) pyc6accel_img_adds, METH_VARARGS,
		                "AddS -> None" },
		        {
		                "SubS", (PyCFunction) pyc6accel_img_subs, METH_VARARGS,
		                "SubS -> None" },
		        {
		                "Erode", (PyCFunction) pyc6accel_img_erode,
		                METH_VARARGS, "Erode -> None" },
		        {
		                "Dilate", (PyCFunction) pyc6accel_img_dilate,
		                METH_VARARGS, "Dilate -> None" },
	        //		        {
	        //		                "MulS", (PyCFunction) pyc6accel_img_muls, METH_VARARGS,
	        //		                "MulS -> None" },
	        //		        {
	        //		                "DivS", (PyCFunction) pyc6accel_img_divs, METH_VARARGS,
	        //		                "DivS -> None" },
		        {
		                "CvtColor", (PyCFunction) pyc6accel_img_cvtcolor,
		                METH_VARARGS, "CvtColor -> None" },
		        {
		                "Threshold", (PyCFunction) pyc6accel_img_threshold,
		                METH_VARARGS, "Threshold -> None" },
		        {
		                "Sobel", (PyCFunction) pyc6accel_img_sobel,
		                METH_VARARGS, "Sobel -> None" },
	        //		        {
	        //		                "AbsDiff", (PyCFunction) pyc6accel_math_absdiff,
	        //		                METH_VARARGS, "AbsDiff -> None" },
	        //	        //		        {
	        //		                "setAsync", (PyCFunction) pyc6accel_setAsync,
	        //		                METH_NOARGS, "Asynchronous mode." },
	        //		        {
	        //		                "setSync", (PyCFunction) pyc6accel_setSync,
	        //		                METH_NOARGS, "Synchronous mode." },
	        //		        {
	        //		                "histogram_8", (PyCFunction) pyc6accel_img_histogram_8,
	        //		                METH_VARARGS, "" },
	        //		        {
	        //		                "histogram_16",
	        //		                (PyCFunction) pyc6accel_img_histogram_16, METH_VARARGS,
	        //		                "" },
	        //		        {
	        //		                "median_3x3_8",
	        //		                (PyCFunction) pyc6accel_img_median_3x3_8, METH_VARARGS,
	        //		                "" },
		        {
		                "load", (PyCFunction) loadiplimage, METH_VARARGS,
		                "test load iplimage" },

	        //		        {
	        //		                "gt2max_8", (PyCFunction) pyc6accel_img_thr_gt2max_8,
	        //		                METH_VARARGS, "" },
		        {
		                NULL, NULL, 0, NULL } };

PyMODINIT_FUNC initpyc6accel(void) {
	PyObject *m, *d;
	char *version = VERSION;

	m = Py_InitModule3(MODULESTR"", pyc6accel_methods,"");
	if (m == NULL)
		return;

	d = PyModule_GetDict(m);
	PyDict_SetItemString(d, "__version__", PyString_FromString(version));


#define PUBLISH(I) PyDict_SetItemString(d, #I, PyInt_FromLong(I));

	PUBLISH(THRESH_GREATER2MAX);
	PUBLISH(THRESH_GREATER2THRES);
	PUBLISH(THRESH_LESS2MIN);
	PUBLISH(THRESH_LESS2THRES);
	PUBLISH(CV_RGB2GRAY);

	py6accel_error = PyErr_NewException((char*) MODULESTR".error", NULL, NULL);
	PyDict_SetItemString(d, "error", py6accel_error);


	/* Codec Engine Initialize & Setting*/
	CERuntime_init();
	memParams = Memory_DEFAULTPARAMS;
	memParams.flags = Memory_CACHED;
	memParams.type = Memory_CONTIGHEAP;
	hC6 = (C6accel_Handle) C6accel_create(engineName, NULL, algName, NULL);
	if (hC6 == NULL) {
		PyErr_SetString(PyExc_RuntimeError, "Can not created c6accel object!");
	}

	Py_INCREF(hC6);
	//	Py_INCREF(memParams);

	/* Synchronous */
	C6Accel_setSync(hC6);
}
