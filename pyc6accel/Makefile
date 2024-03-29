#############################################################################
# Makefile                                                                  #
#                                                                           #
# Make to build C6Accel test application                                    #
#############################################################################
#
#
#############################################################################
#                                                                           #
#   Copyright (C) 2010 Texas Instruments Incorporated                       #
#     http://www.ti.com/                                                    #
#                                                                           #
#############################################################################

TARGET = pyc6accel

include Rules.make

# Comment this out if you want to see full compiler and linker output.
VERBOSE = 

# Which compiler flags should be used?
BUILD_TYPE=debug

# Package path for the XDC tools
XDCPATH = $(USER_XDC_PATH);../packages;$(CE_INSTALL_DIR)/packages;$(FC_INSTALL_DIR)/packages;$(LINK_INSTALL_DIR)/packages;$(LINK_INSTALL_DIR);$(XDAIS_INSTALL_DIR)/packages;$(CMEM_INSTALL_DIR)/packages;$(C6ACCEL_INSTALL_DIR)/soc/packages;$(LPM_INSTALL_DIR)/packages;$(SERVER_INSTALL_DIR)/packages;$(DMAI_INSTALL_DIR)/packages;

# Where to output configuration files
XDC_CFG		= $(TARGET)_config

# Output compiler options
XDC_CFLAGS	= $(XDC_CFG)/compiler.opt

# Output linker file
XDC_LFILE	= $(XDC_CFG)/linker.cmd

# Input configuration file
XDC_CFGFILE	= $(TARGET).cfg

# Target tools
XDC_TARGET	= gnu.targets.arm.GCArmv5T

CROSS_COMPILE	= $(CSTOOL_PREFIX)

export CROSS_COMPILE
export CODEGEN_INSTALL_DIR
export XDCPATH
export PLATFORM_XDC

# The XDC configuration tool command line
CONFIGURO = $(XDC_INSTALL_DIR)/xs xdc.tools.configuro
CONFIG_BLD = ./config.bld

ifeq ($(BUILD_TYPE), release)
ifeq ($(ARM_ISA),armv7-a)
    C_FLAGS	+= -O3 -march=armv7-a -mtune=cortex-a8 -mfpu=neon -ftree-vectorize -mfloat-abi=softfp
endif
ifeq ($(ARM_ISA),armv5t)
    C_FLAGS	+= -mlittle-endian -march=armv5t -mtune=arm9tdmi -mabi=aapcs-linux -O
endif
else
    CPP_FLAGS	+= -DNDEBUG
    C_FLAGS	+= -Wall -g
endif

ifeq ($(PLATFORM),dm3730)
    C_FLAGS	+= -DPLATFORM=3530
endif
ifeq ($(PLATFORM),omap3530)
    C_FLAGS	+= -DPLATFORM=3530
endif
ifeq ($(PLATFORM),omapl138)
    C_FLAGS	+= -DPLATFORM=138
endif

#C_FLAGS += -I/home/anol/CodeSourcery/Sourcery_G++_Lite/arm-none-linux-gnueabi/libc/usr/include/python2.6 #-I/home/anol/CodeSourcery/Sourcery_G++_Lite/arm-none-linux-gnueabi/libc/usr/local/include
LD_FLAGS += -L$(LINUXLIBS_INSTALL_DIR)/lib -lm -lpthread -L${PWD}/python/lib -lpython2.6
C6ACCEL_LIB += $(C6ACCEL_INSTALL_DIR)/soc/c6accelw/lib/c6accelw_omap3530.a470MV
DMAI_C_FLAG += -I$(DMAI_INSTALL_DIR)/packages
DMAI_LIB += $(DMAI_INSTALL_DIR)/packages/ti/sdo/dmai/lib/dmai_linux_omap3530.a470MV
CE_C_FLAG += -I$(CE_INSTALL_DIR)/packages
CE_LIB += $(CE_INSTALL_DIR)/packages/ti/sdo/ce/lib/debug/ce.av5T
OPENCV_C_FLAGS = -I${PWD}/opencv/include -I${PWD}/python/include
OPENCV_LD_FLAGS = -L${PWD}/opencv/lib -lml -lcxcore -lcv -lcvaux -lhighgui

COMPILE.c = $(VERBOSE) $(CSTOOL_PREFIX)gcc  $(CPP_FLAGS) $(C_FLAGS) $(OPENCV_C_FLAGS) $(OPENCV_PYTHON_FLAGS) $(DMAI_C_FLAG) $(CE_C_FLAG) -c
LINK.c = $(VERBOSE) $(CSTOOL_PREFIX)gcc $(LD_FLAGS) $(OPENCV_LD_FLAGS) $(DMAI_LIB) $(CE_LIB)

SOURCES = $(wildcard ./src/*.c)
HEADERS = $(wildcard ./src/*.h)
OBJFILES = $(SOURCES:%.c=%.o)

.PHONY: clean install 

all:	$(TARGET)

install:	$(if $(wildcard $(TARGET).so), install_$(TARGET))

install_$(TARGET):
	@install -d $(EXEC_DIR_C6ACCEL)
	@install $(TARGET).so $(EXEC_DIR_C6ACCEL)
	@cp c6accel/soc/packages/ti/c6accel_unitservers/omap3530/c6accel_omap3530.x64P $(EXEC_DIR_C6ACCEL)
	@cp -fR app/* $(EXEC_DIR_C6ACCEL)
	@cp scripts/run.sh $(EXEC_DIR_C6ACCEL)
	@install -d $(EXEC_DIR_C6ACCEL)/test_files/
	@cp -R test_files/* $(EXEC_DIR_C6ACCEL)/test_files/
	@echo Installed $(TARGET) binaries to $(EXEC_DIR_C6ACCEL)..

$(TARGET):	$(OBJFILES) $(C6ACCEL_LIB) $(DMAI_LIB) $(XDC_LFILE)
	@echo
	@echo Linking $@ from $^..
	$(LINK.c) -shared -o $@".so" $^
	@echo Completed.
	
$(OBJFILES):	%.o: %.c $(HEADERS) $(XDC_CFLAGS)
	@echo Compiling $@ from $<..
	$(COMPILE.c) $(shell cat $(XDC_CFLAGS)) -o $@ $<

$(XDC_LFILE) $(XDC_CFLAGS):	$(XDC_CFGFILE)
	@echo
	@echo ======== Building $(TARGET) ========
	@echo Configuring application using $<
	@echo
	$(VERBOSE) $(CONFIGURO) -o $(XDC_CFG) -t $(XDC_TARGET) -p $(PLATFORM_XDC) -b $(CONFIG_BLD) $(XDC_CFGFILE)

clean:
	@echo Removing generated files..
	$(VERBOSE) -$(RM) -rf $(XDC_CFG) $(OBJFILES) $(TARGET) *~ *.d .dep
	$(VERBOSE) -$(RM) -rf *.o *.so
