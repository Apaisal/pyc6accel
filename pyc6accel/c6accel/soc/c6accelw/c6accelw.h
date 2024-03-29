/*==================================================================*/
/*  Copyright (c) 2010, Texas Instruments Incorporated              */
/*  All rights reserved.                                            */
/*                                                                  */
/*                                                                  */
/* ========c6accelw.h ========                                      */
/*This file declares the ARM wrapper functions for DSP kernels      */
/*  in C6ACCEL                                                      */
/*                                                                  */
/*                                                                  */
/*  Version: 0.0.1                                                  */
/*==================================================================*/

#ifndef WRAPPER_C6ACCEL_DSP_H
#define WRAPPER_C6ACCEL_DSP_H

#ifdef __cplusplus
extern "C" {
#endif

#include <ti/sdo/ce/Engine.h>
#include <ti/sdo/ce/universal/universal.h>

///*	Video Decode */
//#include <ti/sdo/ce/video/viddec.h>

/*OpenCV*/
//#include <cv.h>
//#include <cxcore.h>
/* Include the header for C6ACCEL codec support*/
#include "ti/c6accel/iC6Accel_ti.h"
/* Data type to set synchronous and asynchronous calls in C6Accel */
typedef enum _E_CALL_TYPE {
	SYNC, ASYNC
} E_CALL_TYPE;

/* Structure to hold the params between async process and wait call.
 Aim is to hide from the app these params so that on wait call app just returns output buffers */
typedef struct {
	int asyncCallCount;
	XDM1_BufDesc inBufs;
	XDM1_BufDesc outBufs;
	XDM1_BufDesc inOutBufs;
	IUNIVERSAL_InArgs inArgs;
	IUNIVERSAL_OutArgs outArgs;


	// Memory structure to handle freeing of buffer
	XDAS_Int8 *pBuf;
	XDAS_Int32 pBufSize;

} T_ASYNC_CALL_PARAMS;

extern E_CALL_TYPE callType;

typedef struct C6accel_Object *C6accel_Handle;

/* Function to open and initialise codec engine */
C6accel_Handle C6accel_create(String engName, Engine_Handle hEngine,
        String algName, UNIVERSAL_Handle hUni);

int C6Accel_setSync(C6accel_Handle hC6accel);

E_CALL_TYPE C6Accel_readCallType(C6accel_Handle hC6accel);

int C6Accel_setAsync(C6accel_Handle hC6accel);

/* Function to delete algorithm and codec engine */
int C6accel_delete(C6accel_Handle hC6accel);

/* Function to wait for an async call return */
int C6accel_waitAsyncCall(C6accel_Handle hC6accel);

int C6accel_DSP_fft16x16(C6accel_Handle hC6accel, const short * restrict ptr_w, /* Input twiddle factors */
int npoints, /* number of points      */
short * restrict ptr_x, /* transformed data reversed */
short * restrict ptr_y /* linear transformed data */
);

int C6accel_DSP_gen_twiddle_fft16x16(C6accel_Handle hC6accel,
        short * restrict ptr_w, /* Output array */
        int n); /* Number of elements */

int C6accel_DSP_gen_twiddle_fft32x32(C6accel_Handle hC6accel,
        int * restrict ptr_w, /* Output array */
        int n, double scale); /* Number of elements */

int C6accel_DSP_ifft16x16(C6accel_Handle hC6accel,
        const short * restrict ptr_w, /* Input twiddle factors */
        int npoints, /* number of points      */
        short * restrict ptr_x, /* transformed data reversed */
        short * restrict ptr_y /* linear transformed data */
);

int C6accel_DSP_fft32x32(C6accel_Handle hC6accel, const int * restrict ptr_w, /* Input twiddle factors */
int npoints, /* number of points      */
int * restrict ptr_x, /* transformed data reversed */
int * restrict ptr_y /* linear transformed data */
);

int C6accel_DSP_ifft32x32(C6accel_Handle hC6accel, const int * restrict ptr_w, /* Input twiddle factors */
int npoints, /* number of points      */
int * restrict ptr_x, /* transformed data reversed */
int * restrict ptr_y /* linear transformed data */
);

int C6accel_DSP_autocor(C6accel_Handle hC6accel, short * restrict ptr_r, /* Output array */
short * restrict ptr_x, /*Input array. Must be double-word aligned */
int nx, /*Length of autocorrelation.*/
int nr); /* Number of lags */

int C6accel_DSP_dotprod(C6accel_Handle hC6accel, short * restrict ptr_x, /* Output array */
short * restrict ptr_y, /*Input array. Must be double-word aligned */
int * restrict ptr_r, /* Result of the dot prod */
int nx); /* Number of elements */

int C6accel_DSP_dotp_sqr(C6accel_Handle hC6accel, int Gin,
        short * restrict ptr_x, /* Output array */
        short * restrict ptr_y, /*Input array. Must be double-word aligned */
        int * restrict ptr_r, /* Result of the dot prod */
        int * restrict ptr_Gout,/* Result Gout */
        int nx); /* Number of elements */

int C6accel_DSP_mat_mul(C6accel_Handle hC6accel, short * restrict ptr_x, /* Input array */
int r1, /* # Row 1st array */
int c1, /* # Columan of 1st array */
short * restrict ptr_y, /*Input array. Must be double-word aligned */
int c2, /* #Columen of 2nd Array */
short * restrict ptr_r, /*Output Array */
int qs); /* Number of elements */

int C6accel_DSP_fir_gen(C6accel_Handle hC6accel, short * restrict ptr_x,
        short * restrict ptr_h, short * restrict ptr_r, int nh, int nr);

int C6accel_DSP_fir_r4(C6accel_Handle hC6accel, short * restrict ptr_x,
        short * restrict ptr_h, short * restrict ptr_r, int nh, int nr);

int C6accel_DSP_fir_r8(C6accel_Handle hC6accel, short * restrict ptr_x,
        short * restrict ptr_h, short * restrict ptr_r, int nh, int nr);

int C6accel_DSP_iir(C6accel_Handle hC6accel, short * restrict ptr_x,
        short * restrict ptr_h, int nh, short * restrict ptr_b,
        short * restrict ptr_r, int npoints);

int C6accel_IMG_histogram_8(C6accel_Handle hC6accel,
        const unsigned char *restrict in, /* Input image data */
        int n, /* Number of pixels in image */
        short accumulate, /* accumulate +1, or subtract -1 from hist[] */
        unsigned short *restrict t_hist, unsigned short *restrict hist /* Output histogram data */
);

int C6accel_IMG_histogram_16(C6accel_Handle hC6accel,
        unsigned short *restrict in, /* input image data  */
        int n, /* number of input image pixels    */
        int accumulate, /* define add/sum for histogtram   */
        short *restrict t_hist, /* temporary histogram bins        */
        short *restrict hist, /* running histogram bins          */
        int img_bits /* number of data bits in a pixel  */
);

int C6accel_IMG_median_3x3_8(C6accel_Handle hC6accel,
        const unsigned char *restrict in, /* Input image data, pointer to a line of image   */
        int cols, /* Number of pixels in image */
        unsigned char *restrict out /* Output image line         */
);

int C6accel_IMG_median_3x3_16s(C6accel_Handle hC6accel,
        const short *restrict in, /* Input image data, pointer to a line of image   */
        int cols, /* Number of pixels in image                      */
        short *restrict out /* Output image line                              */
);

int C6accel_IMG_median_3x3_16(C6accel_Handle hC6accel,
        const short *restrict in, /* Input image data, pointer to a line of image   */
        int cols, /* Number of pixels in image */
        short *restrict out /* Output image line */
);

int C6accel_IMG_median_3x3_8_Frame(C6accel_Handle hC6accel,
        const unsigned char *restrict in, /* Input image data, pointer to a line of image   */
        int rows, /* Number of rows in image */
        int cols, /* Number of cols in image */
        unsigned char *restrict out /* Output image line */
);

int C6accel_IMG_median_3x3_16_Frame(C6accel_Handle hC6accel,
        const short *restrict in, /* Input image data, pointer to a line of image   */
        int rows, /* Number of rows in image */
        int cols, /* Number of cols in image */
        short *restrict out /* Output image line       */
);

int C6accel_IMG_median_3x3_16s_Frame(C6accel_Handle hC6accel,
        const short *restrict in, /* Input image data, pointer to a line of image   */
        int rows, /* Number of rows in image     */
        int cols, /* Number of cols in image     */
        short *restrict out /* Output image line           */
);

int C6accel_IMG_conv_3x3_i8_c8s(C6accel_Handle hC6accel,
        const unsigned char *restrict inptr, unsigned char *restrict outptr,
        int x_dim, const char *restrict mask, int shift);

int C6accel_IMG_conv_3x3_i16s_c16s(C6accel_Handle hC6accel,
        const short *restrict imgin_ptr, short *restrict imgout_ptr,
        short width, short pitch, const short *restrict mask_ptr, short shift);

int C6accel_IMG_conv_3x3_i8_c8s_Frame(C6accel_Handle hC6accel,
        const unsigned char *restrict inptr, unsigned char *restrict outptr,
        int rows, int x_dim, const char *restrict mask, int shift);

int C6accel_IMG_conv_3x3_i16s_c16s_Frame(C6accel_Handle hC6accel,
        const short *restrict imgin_ptr, short *restrict imgout_ptr,
        short rows, short width, short pitch, const short *restrict mask_ptr,
        short shift);
int C6accel_IMG_conv_5x5_i8_c8s(C6accel_Handle hC6accel,
        const unsigned char *restrict imgin_ptr,
        unsigned char *restrict imgout_ptr, short width, short pitch,
        const char *restrict mask_ptr, short shift);

int C6accel_IMG_corr_3x3_i8_c8(C6accel_Handle hC6accel,
        const unsigned char *restrict inptr, int *restrict outptr, int n_out,
        int x_dim, const unsigned char *restrict mask, short shift, int round);

int C6accel_IMG_corr_3x3_i16s_c16s(C6accel_Handle hC6accel,
        const short *restrict imgin_ptr, int *restrict imgout_ptr, short width,
        short pitch, const short *restrict mask_ptr, short shift, int round);

int C6accel_IMG_corr_3x3_i8_c8_Frame(C6accel_Handle hC6accel,
        const unsigned char *restrict inptr, int *restrict outptr, int rows,
        int n_out, int x_dim, const unsigned char *restrict mask, short shift,
        int round);

int C6accel_IMG_corr_3x3_i16s_c16s_Frame(C6accel_Handle hC6accel,
        const short *restrict imgin_ptr, int *restrict imgout_ptr, short rows,
        short width, short pitch, const short *restrict mask_ptr, short shift,
        int round);

int C6accel_IMG_sobel_3x3_8(C6accel_Handle hC6accel,
        const IplImage *restrict in, IplImage *restrict out, short cols,
        short rows);

int C6accel_IMG_sobel_3x3_16(C6accel_Handle hC6accel,
        const unsigned short *restrict in, /* Input image data   */
        unsigned short *restrict out, /* Output image data  */
        short cols, short rows /* Image dimensions   */
);

int C6accel_IMG_mulS_8(C6accel_Handle hC6accel, const IplImage *restrict imgR, /* Input image data 16 bits/pixel  */
IplImage *restrict imgW, /* Output image data 32 bits/pixel */
char constData, /* 16 bit constant to multiply by  */
int count /* Number of pixels in image       */
);

int C6accel_IMG_mulS_16s(C6accel_Handle hC6accel, const short *restrict imgR, /* Input image data 16 bits/pixel   */
int *restrict imgW, /* Output image data 32 bits/pixel  */
short constData, /* 16 bit constant to multiply by   */
int count /* Number of pixels in image        */
);

int C6accel_IMG_addS_8(C6accel_Handle hC6accel, const IplImage *restrict imgR, /* Input image data 8 bits/pixel  */
IplImage *restrict imgW, /* Output image data 8 bits/pixel */
char constData, /* 8 bit constant to add          */
int count /* Number of pixels in image      */
);

int C6accel_IMG_addS_16s(C6accel_Handle hC6accel, const short *restrict imgR, /* Input image data 16 bits/pixel  */
short *restrict imgW, /* Output image data 16 bits/pixel */
short constData, /* 16 bit constant to multiply by  */
int count /* Number of pixels in image       */
);

int C6accel_IMG_add_16s(C6accel_Handle hC6accel,
        const IplImage * restrict imgR1, /* Input image 1 data 16 bits/pixel  */
        const IplImage * restrict imgR2, /* Input image 2 data 16 bits/pixel  */
        IplImage * restrict imgW, /* Output image data 16 bits/pixel */
        int count /* Number of pixels in image       */
);

int C6accel_IMG_subS_8(C6accel_Handle hC6accel, const IplImage *restrict imgR, /* Input image data 8 bits/pixel  */
IplImage *restrict imgW, /* Output image data 8 bits/pixel */
char constData, /* 8 bit constant to sub          */
int count /* Number of pixels in image      */
);

int C6accel_IMG_subS_16s(C6accel_Handle hC6accel, const short *restrict imgR, /* Input image data 16 bits/pixel   */
short *restrict imgW, /* Output image data 16 bits/pixel  */
short constData, /* 16 bit constant to sub           */
int count /* Number of pixels in image        */
);

int C6accel_IMG_yc_demux_le8_8(C6accel_Handle hC6accel, int n, /* Number of luma points           */
unsigned char *restrict yc, /* Packed YUYV image               */
unsigned char *restrict y, /* Unpacked luma frame             */
unsigned char *restrict cr, /* Unpacked red chroma frame       */
unsigned char *restrict cb /* Unpacked green chroma frame     */
);

int C6accel_IMG_yc_demux_le16_16(C6accel_Handle hC6accel, int n, /* Number of luma points           */
unsigned short *restrict yc, /* Packed YUYV image               */
short *restrict y, /* Unpacked luma frame             */
short *restrict cr, /* Unpacked red chroma frame       */
short *restrict cb /* Unpacked green chroma frame     */
);

int C6accel_IMG_yuv420pl_to_rgb565(C6accel_Handle hC6accel, const short *coeff, /* YUV to RGB transformation matrix*/
short height, short width, unsigned char *restrict y, /* Unpacked luma frame             */
unsigned char *restrict cb, /* Unpacked blue chroma frame      */
unsigned char *restrict cr, /* Unpacked red chroma frame       */
unsigned short *restrict rgb /* output RGB565 frame             */
);

int C6accel_IMG_yuv420pl16_to_rgb565(C6accel_Handle hC6accel,
        const short *coeff, /* YUV to RGB transformation matrix*/
        short height, short width, short *restrict y, /* Unpacked luma frame             */
        short *restrict cb, /* Unpacked blue chroma frame      */
        short *restrict cr, /* Unpacked red chroma frame       */
        unsigned short *restrict rgb /* output RGB565 frame             */
);

int C6accel_IMG_ycbcr422pl_to_rgb565(C6accel_Handle hC6accel,
        const short *coeff, /* YUV to RGB transformation matrix*/
        unsigned char *restrict y, /* Unpacked luma frame             */
        unsigned char *restrict cb, /* Unpacked blue chroma frame      */
        unsigned char *restrict cr, /* Unpacked red chroma frame       */
        unsigned short *restrict rgb, /* output RGB565 frame             */
        unsigned int num_pixels);

int C6accel_IMG_ycbcr422pl16_to_rgb565(C6accel_Handle hC6accel,
        const short *coeff, /* YUV to RGB transformation matrix*/
        short *restrict y, /* Unpacked luma frame             */
        short *restrict cb, /* Unpacked blue chroma frame      */
        short *restrict cr, /* Unpacked red chroma frame       */
        unsigned short *restrict rgb, /* output RGB565 frame             */
        unsigned int num_pixels);

int C6accel_IMG_ycbcr422sp_to_ycbcr420pl(C6accel_Handle hC6accel,
        const unsigned char * y_src, const unsigned char * cbcr_src,
        unsigned char * restrict y_dst, unsigned char * restrict cb_dst,
        unsigned char * restrict cr_dst, unsigned int num_lines,
        unsigned int width, unsigned int src_pitch, unsigned int dst_y_pitch,
        unsigned int dst_cbcr_pitch);

int C6accel_IMG_ycbcr422sp_to_ycbcr422ile(C6accel_Handle hC6accel,
        const unsigned char * y_src, const unsigned char * cbcr_src,
        unsigned char * restrict ycbcr_dst, unsigned int num_lines,
        unsigned int width, unsigned int src_pitch,
        unsigned int dst_ycbcr_pitch);

int C6accel_IMG_ycbcr422pl_to_ycbcr422sp(C6accel_Handle hC6accel,
        const unsigned char * y_dst, const unsigned char * cbcr_dst,
        unsigned char * restrict y_src, unsigned char * restrict cb_src,
        unsigned char * restrict cr_src, unsigned int num_lines,
        unsigned int width, unsigned int dst_pitch, unsigned int src_y_pitch,
        unsigned int src_cbcr_pitch);

/* Converts VYUY to Y,U,V format */
int C6accel_IMG_yc_demux_be8_8(C6accel_Handle hC6accel, int n, /* Number of luma points           */
unsigned char *restrict yc, /* Packed YUYV image               */
unsigned char *restrict y, /* Unpacked luma frame             */
unsigned char *restrict cr, /* Unpacked red chroma frame       */
unsigned char *restrict cb /* Unpacked green chroma frame     */
);

int C6accel_IMG_rgb_to_y(C6accel_Handle hC6accel, const IplImage *restrict src,
        IplImage * restrict dst, unsigned int count);

int C6accel_IMG_addweight(C6accel_Handle hC6, const IplImage * restrict src1,
        const IplImage * restrict src2, IplImage * restrict addw, float a,
        float b, float c);

int cC6accel_IMG_thr_binary(C6accel_Handle hC6accel, const IplImage * in_data, /*  Input image data    */
IplImage * restrict out_data, /*  Output image data   */
short cols, short rows, /*  Image dimensions    */
unsigned char threshold /*  Threshold value     */
);

// image threshold greater than to maximum 8 bits
int C6accel_IMG_thr_gt2max_8(C6accel_Handle hC6accel, const IplImage * in_data, /*  Input image data    */
IplImage * restrict out_data, /*  Output image data   */
short cols, short rows, /*  Image dimensions    */
unsigned char threshold /*  Threshold value     */
);

int C6accel_IMG_thr_gt2thr_8(C6accel_Handle hC6accel, const IplImage * in_data, /*  Input image data    */
IplImage * restrict out_data, /*  Output image data   */
short cols, short rows, /*  Image dimensions    */
unsigned char threshold /*  Threshold value     */
);

int C6accel_IMG_thr_le2min_8(C6accel_Handle hC6accel, const IplImage * in_data, /*  Input image data    */
IplImage * restrict out_data, /*  Output image data   */
short cols, short rows, /*  Image dimensions    */
unsigned char threshold /*  Threshold value     */
);

int C6accel_IMG_thr_le2thr_8(C6accel_Handle hC6accel, const IplImage * in_data, /*  Input image data    */
IplImage * restrict out_data, /*  Output image data   */
short cols, short rows, /*  Image dimensions    */
unsigned char threshold /*  Threshold value     */
);

//int C6accel_IMG_canny(C6accel_Handle hC6, const unsigned char * in_dat,
//        unsigned char * restrict out_dat, const unsigned char * mask, int rows,
//        int cols, double l_thr, double h_thr, int aperture_size);

int C6accel_MATH_f2d(C6accel_Handle hC6accel, double *ptr_d, /* Output double array */
float *ptr_f, int n);

int C6accel_MATH_addsp_i(C6accel_Handle hC6accel, float *ptr_x, float *ptr_y,
        float *ptr_r, int npoints);

int C6accel_MATH_subsp_i(C6accel_Handle hC6accel, float *ptr_x, float *ptr_y,
        float *ptr_r, int npoints);

int C6accel_MATH_mpysp_i(C6accel_Handle hC6accel, float *ptr_x, float *ptr_y,
        float *ptr_r, int npoints);

int C6accel_MATH_divsp_i(C6accel_Handle hC6accel, float *ptr_x, float *ptr_y,
        float *ptr_r, int npoints);

int C6accel_MATH_recipsp_i(C6accel_Handle hC6accel, float *ptr_x, float *ptr_r,
        int npoints);

int C6accel_MATH_sqrtsp_i(C6accel_Handle hC6accel, float *ptr_x, float *ptr_r,
        int npoints);

int C6accel_MATH_intsp_i(C6accel_Handle hC6accel, int *ptr_x, float *ptr_r,
        int npoints);

int C6accel_MATH_uintsp_i(C6accel_Handle hC6accel, unsigned int *ptr_x,
        float *ptr_r, int npoints);

int C6accel_MATH_spint_i(C6accel_Handle hC6accel, float *ptr_x, int *ptr_r,
        int npoints);

int C6accel_MATH_spuint_i(C6accel_Handle hC6accel, float *ptr_x,
        unsigned int *ptr_r, int npoints);

int C6accel_MATH_FTOIQN(C6accel_Handle hC6accel, float *ptr_x,
        unsigned int qfmt, int *ptr_r, int npoints);

int C6accel_MATH_IQN(C6accel_Handle hC6accel, int *ptr_x, unsigned int qfmt,
        int *ptr_r, int npoints);

int C6accel_MATH_IQXtoIQY(C6accel_Handle hC6accel, int *ptr_x,
        unsigned int qfmt1, unsigned int qfmt2, int *ptr_r, int npoints);

int C6accel_MATH_IQNtoF(C6accel_Handle hC6accel, int *ptr_x, unsigned int qfmt,
        float *ptr_r, int npoints);

int C6accel_MATH_IQNint(C6accel_Handle hC6accel, int *ptr_x, unsigned int qfmt,
        int *ptr_r, int npoints);

int C6accel_MATH_IQNfrac(C6accel_Handle hC6accel, int *ptr_x,
        unsigned int qfmt, int *ptr_r, int npoints);

int C6accel_MATH_IQNabs(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNlog(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNsqrt(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNisqrt(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNexp(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNpow(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNmag(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNmpy(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNmpyI32int(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNmpyI32frac(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNmpyIQx(C6accel_Handle hC6accel, int *ptr_x,
        unsigned int qfmt1, int *ptr_y, unsigned int qfmt2, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNrmpy(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNrsmpy(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNdiv(C6accel_Handle hC6accel, int *ptr_x, int *ptr_y,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNsin(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNasin(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNcos(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNacos(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNcosPU(C6accel_Handle hC6accel, int *ptr_x, int *ptr_r,
        unsigned int qfmt, int npoints);

int C6accel_MATH_IQNsinPU(C6accel_Handle hC6accel, int *ptr_x,

int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNatan2(C6accel_Handle hC6accel, int *ptr_y, int *ptr_x,
        int *ptr_r, unsigned int qfmt, int npoints);

int C6accel_MATH_IQNatan2PU(C6accel_Handle hC6accel, int *ptr_y, int *ptr_x,
        int *ptr_r, unsigned int qfmt, int npoints);

/* Floating point kernels APIs */
int C6accel_DSPF_sp_fftSPxSP(C6accel_Handle hC6accel, int npoints, /* number of points      */
float * restrict ptr_x, /* transformed data reversed */
float * restrict ptr_w, /* Input twiddle factors */
float * restrict ptr_y, /* linear transformed data */
unsigned char * ptr_brev, int n_min, int offset, int n_max);

int C6accel_DSPF_tw_gen(C6accel_Handle hC6accel, float * restrict ptr_w, /* Output array */
int n);

int C6accel_DSPF_sp_ifftSPxSP(C6accel_Handle hC6accel, int npoints, /* number of points      */
float * restrict ptr_x, /* transformed data reversed */
float * restrict ptr_w, /* Input twiddle factors */
float * restrict ptr_y, /* linear transformed data */
unsigned char * ptr_brev, int n_min, int offset, int n_max);

int C6accel_DSPF_sp_autocor(C6accel_Handle hC6accel, float * restrict ptr_r, /* Output array */
float * restrict ptr_x, /*Input array. Must be double-word aligned */
int nx, /*Length of autocorrelation.*/
int nr);

int C6accel_DSPF_sp_dotprod(C6accel_Handle hC6accel,
        const float * restrict ptr_x, /* Output array */
        const float * restrict ptr_y, /*Input array. Must be double-word aligned */
        const float * ptr_r, const int nx); /* Number of elements */

int C6accel_DSPF_sp_mat_mul(C6accel_Handle hC6accel, float *restrict ptr_x1, /* Input matrix 1 */
int r1, /* Number of rows in matrix 1 */
int c1, /* Number of cols in matrix 1 */
float *restrict ptr_x2, /* Input array. Must be double-word aligned */
int c2, /* Number of cols for matrix 2 */
float *restrict ptr_y /* Output matrix */
);

int C6accel_DSPF_sp_mat_mul_cplx(C6accel_Handle hC6accel,
        float *restrict ptr_x1, /* Input matrix 1 */
        int r1, /* Number of rows in matrix 1 */
        int c1, /* Number of cols in matrix 1 */
        float *restrict ptr_x2, /* Input array. Must be double-word aligned */
        int c2, /* Number of cols for matrix 2 */
        float *restrict ptr_y); /* Output matrix */

int C6accel_DSPF_sp_mat_trans(C6accel_Handle hC6accel, float *restrict ptr_x, /* Input matrix 1 */
int row, /* Number of rows in matrix 1 */
int col, /* Number of cols in matrix 1 */
float *restrict ptr_r /* Output matrix */
);

int C6accel_DSPF_sp_vecmul(C6accel_Handle hC6accel, float *restrict ptr_x1, /* Input matrix 1 */
float *restrict ptr_x2, /* Input array. Must be double-word aligned */
float *restrict ptr_y, /* Output matrix */
const int n /* Number of elements*/
);

int C6accel_DSPF_sp_vecrecip(C6accel_Handle hC6accel,
        const float *restrict ptr_x, /* Input matrix 1 */
        float *restrict ptr_y, /* Output matrix */
        const int n /* Number of elements*/
);

int C6accel_DSPF_sp_vecsum_sq(C6accel_Handle hC6accel,
        const float *restrict ptr_x, /* Input matrix 1 */
        float *restrict ptr_OutRet, /* Output matrix */
        const int n /* Number of elements*/
);

int C6accel_DSPF_sp_w_vec(C6accel_Handle hC6accel, float *restrict ptr_x1, /* Input matrix 1 */
float *restrict ptr_x2, /* Input array. Must be double-word aligned */
const float m, float *restrict ptr_y, /* Output matrix */
const int n /* Number of elements*/
);

int C6accel_DSPF_sp_fir_gen(C6accel_Handle hC6accel, float * restrict ptr_x,
        float * restrict ptr_h, float * restrict ptr_y, int nh, int ny);

int C6accel_DSPF_sp_fir_cplx(C6accel_Handle hC6accel, float * restrict ptr_x,
        float * restrict ptr_h, float * restrict ptr_y, int nh, int ny);

int C6accel_DSPF_sp_iir(C6accel_Handle hC6accel, float * restrict ptr_y1,
        float * restrict ptr_x, float * restrict ptr_y2,
        float * restrict ptr_hb, float * restrict ptr_ha, int n);

int C6accel_DSPF_sp_convol(C6accel_Handle hC6accel, float * restrict ptr_x,
        float * restrict ptr_h, float * restrict ptr_y, const short nh,
        const short ny);

int C6accel_DSPF_sp_biquad(C6accel_Handle hC6accel, float * restrict ptr_x,
        float * restrict ptr_b, float * restrict ptr_a,
        float * restrict ptr_delay, float * restrict ptr_y, const int n);

int C6accel_MATH_sqrtsp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_sqrtdp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_rsqrtsp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_rsqrtdp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_logsp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_logdp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_expsp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_expdp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_exp2sp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_exp2dp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_exp10sp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_exp10dp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_sinsp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_sindp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_cossp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_cosdp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_atansp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_atandp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_recipsp(C6accel_Handle hC6accel, float *ptr_z, float *ptr_r,
        int npoints);

int C6accel_MATH_recipdp(C6accel_Handle hC6accel, double *ptr_z, double *ptr_r,
        int npoints);

int C6accel_MATH_atan2sp(C6accel_Handle hC6accel, float *ptr_y, float *ptr_x,
        float *ptr_r, int npoints);

int C6accel_MATH_atan2dp(C6accel_Handle hC6accel, double *ptr_y, double *ptr_x,
        double *ptr_r, int npoints);

int C6accel_MATH_powsp(C6accel_Handle hC6accel, float *ptr_x, float *ptr_y,
        float *ptr_r, int npoints);

int C6accel_MATH_powdp(C6accel_Handle hC6accel, double *ptr_x, double *ptr_y,
        double *ptr_r, int npoints);

int C6accel_DSPF_complextorealnimg(C6accel_Handle hC6accel, float *ptr_cplx,
        float *ptr_real, float *ptr_img, int npoints);

int C6accel_IMG_ycbcr420pl_to_ycbcr422sp(C6accel_Handle hC6accel,
        const unsigned char * y_dst, const unsigned char * cbcr_dst,
        unsigned char * restrict y_src, unsigned char * restrict cb_src,
        unsigned char * restrict cr_src, unsigned int num_lines,
        unsigned int width, unsigned int dst_pitch, unsigned int src_y_pitch,
        unsigned int src_cbcr_pitch);

int C6accel_IMG_erode_bin(C6accel_Handle hC6accel,
        const IplImage *restrict in_data, IplImage *restrict out_data,
        const IplConvKernel *restrict mask, int cols);

int C6accel_IMG_dilate_bin(C6accel_Handle hC6accel,
        const IplImage *restrict in_data, IplImage *restrict out_data,
        const IplConvKernel *restrict mask, int cols);

int C6accel_IMG_jpegdec(C6accel_Handle hC6accel, const char *restrict inBuf,
        char * restrict outBuf);

#ifdef __cplusplus
}
#endif

#endif
