###################################################################################
#  ======== Rules.make ========
#  This file specified variables used by the makefiles. After editing this file
#  you should not have to modify any of Makefiles to build this product.
#
#  The DVSDK_INSTALL_DIR variable is a local support variable only used in
#  this file and does not need to be set if individual components are used.
###################################################################################
#=========================================================
# If C6Accel package is found under DVSDK Root Directory
# Set only the DVSDK INSTALL Directory below
#=========================================================
DVSDK_INSTALL_DIR=/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09
-include $(DVSDK_INSTALL_DIR)/Rules.make
EXEC_DIR = /home/anol/targetfs/opt/test
EXEC_DIR_C6ACCEL = $(EXEC_DIR)/opencv_dsp

C6ACCEL_INSTALL_DIR= ${PWD}/c6accel
# RTSC platform
PLATFORM_XDC = ti.platforms.evm3530

# ARM Instruction set
ARM_ISA = armv7-a

# DSP Instruction set
DSP_ISA = 64P

