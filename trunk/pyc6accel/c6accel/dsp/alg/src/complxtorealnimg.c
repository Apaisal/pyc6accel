/*==================================================================== */
/*  Copyright (c) 2010, Texas Instruments Incorporated                 */
/*  All rights reserved.                                               */
/*                                                                     */
/*                                                                     */
/* ======== complxtorealnimg.c ========                                */
/* This file contains a function to seperate the real and imaginary    */
/*   parts of a complex number                                         */
/* This function is also used in the documentation to describe how a   */
/* custom DSP kernel can be added to the C6Accel algorithm             */
/*                                                                     */
/*  Version: 0.0.1                                                     */
/*==================================================================== */

void complxtorealnimg 
(
    float * complex_src,    
    float * real_dst, 
    float * img_dst,
    int n_elements 
)
{
    unsigned int j;
    double r3_r2_r1_r0_i3_i2_i1_i0;
          
        /* for each sample... */
        for (j = 0; j <n_elements; j++) {
            r3_r2_r1_r0_i3_i2_i1_i0 = _amemd8 (complex_src+2*j);
 
            _amem4(real_dst+j)     = _lo (r3_r2_r1_r0_i3_i2_i1_i0);
            _amem4(img_dst+j)      = _hi (r3_r2_r1_r0_i3_i2_i1_i0);
       }
    
}
/*=====================================================================*/
/*     ==== complxtorealnimg.c ====                                    */
/*                                     */
/*          Version: 0.0.1                                             */
/*==================================================================== */
