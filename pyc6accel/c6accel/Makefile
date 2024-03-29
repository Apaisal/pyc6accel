#############################################################################
# Makefile                                                                  #
#                                                                           #
# Top-level make for C6Accel project                                        #
#############################################################################
#
#
#############################################################################
#                                                                           #
#   Copyright (C) 2010 Texas Instruments Incorporated                       #
#     http://www.ti.com/                                                    #
#                                                                           #
#############################################################################

include Rules.make

COMPONENTS:=$(LPM_INSTALL_DIR) $(LINK_INSTALL_DIR) $(XDAIS_INSTALL_DIR) $(CMEM_INSTALL_DIR) $(FC_INSTALL_DIR) $(CE_INSTALL_DIR) $(XDC_INSTALL_DIR) $(BIOSUTILS_INSTALL_DIR) $(BIOS_INSTALL_DIR) $(DMAI_INSTALL_DIR)

REPOSITORIES:=$(addsuffix /packages, $(COMPONENTS))

CHECKLIST:=$(REPOSITORIES) $(CODEGEN_INSTALL_DIR)/bin/cl6x $(MVTOOL_PREFIX)gcc 

.PHONY:	all clean dmai c6accel app app_clean packages servers c6accelw c6accel_clean install

#==============================================================================
# The default build target.
#==============================================================================
all:	c6accel dmai

#==============================================================================
# Clean up the targets built by 'make all'.
#==============================================================================
clean:	c6accel_clean dmai_clean
#==============================================================================
# Build everything rebuildable.
#==============================================================================
everything: all

#==============================================================================
# Clean up all targets.
#==============================================================================
clobber:    clean

#==============================================================================
# A help message target.
#==============================================================================
help:
	@echo
	@echo "Available build targets are:"
	@echo
	@echo "    all             : Build the components below"
	@echo "    clean           : Remove files generated by the 'all' target"
	@echo
	@echo "    servers         : Build c6accel unit servers for $(PLATFORM)"
	@echo "    packages        : Build c6accel packages	"
	@echo "    clean_packages  : Remove generated files in c6accel packages	"
	@echo
	@echo "    c6accelw        : Build c6accel ARM side library"
	@echo "    c6accelw_clean  : Remove generated c6accel ARM side library" 
	@echo
	@echo "    app             : Build c6accel sample application"
	@echo "    app_clean       : Remove generated c6accel sample application files" 
	@echo
	@echo "    install         : Install binaries to $(EXEC_DIR)"
	@echo

#==============================================================================
# Target for listing information about the DVSDK components.
#==============================================================================
info:	check
	@LINUXKERNEL_INSTALL_DIR="$(LINUXKERNEL_INSTALL_DIR)" CODEGEN_INSTALL_DIR="$(CODEGEN_INSTALL_DIR)" GCC_PREFIX="$(MVTOOL_PREFIX)" XDC_INSTALL_DIR="$(XDC_INSTALL_DIR)" REPOSITORIES="$(REPOSITORIES)" $(DVSDK_INSTALL_DIR)/bin/info.sh 

#==============================================================================
# Target for checking that the Rules.make file is set up properly.
#==============================================================================
check:
	@CHECKLIST="$(CHECKLIST)" $(DVSDK_INSTALL_DIR)/bin/check.sh


#==============================================================================
# Build the codec servers for the configured platform. Also, an
# explicit cleanup target is defined.
#==============================================================================
c6accel:
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/dsp DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\"
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/soc DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\"

c6accel_clean:
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/dsp DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\" clean
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/soc DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\" clean

server: .check-BIOS
	$(XDC) -P $(C6ACCEL_INSTALL_DIR)/soc/packages/ti/c6accel_unitservers/$(PLATFORM)

packages: .check-BIOS
	$(XDC) -P $(C6ACCEL_INSTALL_DIR)/soc/packages/ti/c6accel
	$(XDC) -P $(C6ACCEL_INSTALL_DIR)/soc/packages/ti/c6accel/ce
	$(XDC) -P $(C6ACCEL_INSTALL_DIR)/soc/packages/ti/c6accel_unitservers/$(PLATFORM)

clean_packages:
	$(XDC) clean -PR $(C6ACCEL_INSTALL_DIR)/soc/packages

c6accelw:
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/soc/c6accelw DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\"

c6accelw_clean:
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/soc/c6accelw DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\" clean

app:
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/soc/app DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\"

app_clean:
	$(MAKE) -C $(C6ACCEL_INSTALL_DIR)/soc/app DVSDK_INSTALL_DIR=$(DVSDK_INSTALL_DIR) BIOS_INSTALL_DIR=$(BIOS_INSTALL_DIR) XDC_INSTALL_DIR=$(XDC_INSTALL_DIR) CE_INSTALL_DIR=$(CE_INSTALL_DIR) FC_INSTALL_DIR=$(FC_INSTALL_DIR) CMEM_INSTALL_DIR=$(CMEM_INSTALL_DIR) CODEC_INSTALL_DIR=$(CODEC_INSTALL_DIR) BIOSUTILS_INSTALL_DIR=$(BIOSUTILS_INSTALL_DIR) XDAIS_INSTALL_DIR=$(XDAIS_INSTALL_DIR) LINK_INSTALL_DIR=$(LINK_INSTALL_DIR) PLATFORM_XDC=$(PLATFORM_XDC) XDCARGS=\"prod\" clean

#==============================================================================
# Install the built binaries to the target file system.
#==============================================================================
install:
	@echo Creating $(EXEC_DIR_C6ACCEL)
	@mkdir -p $(EXEC_DIR_C6ACCEL)
	@mkdir -p $(EXEC_DIR_C6ACCEL)/test_files

ifeq ($(PLATFORM),omap3530)
	@echo Copying kernel modules to target file system: $(EXEC_DIR_C6ACCEL)/
	@echo Copying cmemk.ko
	@install -m 755 $(CMEM_INSTALL_DIR)/packages/ti/sdo/linuxutils/cmem/src/module/cmemk.ko $(EXEC_DIR_C6ACCEL)/
	@echo Copying dsplinkk.ko
	@install -m 755 $(LINK_INSTALL_DIR)/packages/dsplink/gpp/export/BIN/Linux/OMAP3530/RELEASE/dsplinkk.ko $(EXEC_DIR_C6ACCEL)/
	@echo Copying lpm_omap3530.ko
	@install -m 755 $(LPM_INSTALL_DIR)/packages/ti/bios/power/modules/omap3530/lpm/lpm_omap3530.ko $(EXEC_DIR_C6ACCEL)/
	@echo Copying sdmak.ko
	@install -m 755 $(CMEM_INSTALL_DIR)/packages/ti/sdo/linuxutils/sdma/src/module/sdmak.ko $(EXEC_DIR_C6ACCEL)/
	@echo Copying c6accel codec servers from $(C6ACCEL_INSTALL_DIR)
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/packages/ti/c6accel_unitservers/omap3530/c6accel_omap3530.x64P $(EXEC_DIR_C6ACCEL)/
	@echo Copying c6accel test app from $(C6ACCEL_INSTALL_DIR)
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/app/c6accel_app $(EXEC_DIR_C6ACCEL)/
	@echo Copying testfile from $(C6ACCEL_INSTALL_DIR)
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/app/test_files/* $(EXEC_DIR_C6ACCEL)/test_files
	@chmod -x $(EXEC_DIR_C6ACCEL)/*.x64P $(EXEC_DIR_C6ACCEL)/*.ko 
	@chmod +x $(EXEC_DIR_C6ACCEL)/c6accel_app
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/app/omap3530/loadmodules_omap3530_c6accel.sh $(EXEC_DIR_C6ACCEL)
	@chmod +x $(EXEC_DIR_C6ACCEL)/loadmodules_omap3530_c6accel.sh
endif
ifeq ($(PLATFORM),omapl138)
	@echo Copying kernel modules to target file system: $(EXEC_DIR_C6ACCEL)/
	@echo Copying cmemk.ko
	@install -m 755 $(CMEM_INSTALL_DIR)/packages/ti/sdo/linuxutils/cmem/src/module/cmemk.ko $(EXEC_DIR_C6ACCEL)/
	@echo Copying dsplinkk.ko
	@install -m 755 $(LINK_INSTALL_DIR)/dsplink/gpp/export/BIN/Linux/OMAPL138/RELEASE/dsplinkk.ko $(EXEC_DIR_C6ACCEL)/
	@echo Copying c6accel codec servers from $(C6ACCEL_INSTALL_DIR)
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/packages/ti/c6accel_unitservers/omapl138/c6accel_omapl138.x674 $(EXEC_DIR_C6ACCEL)/
	@echo Copying c6accel test app from $(C6ACCEL_INSTALL_DIR)
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/app/c6accel_app $(EXEC_DIR_C6ACCEL)/
	@echo Copying testfile from $(C6ACCEL_INSTALL_DIR)
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/app/test_files/* $(EXEC_DIR_C6ACCEL)/test_files
	@chmod -x $(EXEC_DIR_C6ACCEL)/*.x674 $(EXEC_DIR_C6ACCEL)/*.ko 
	@chmod +x $(EXEC_DIR_C6ACCEL)/c6accel_app
	@install -m 755 $(C6ACCEL_INSTALL_DIR)/soc/app/omapl138/loadmodules_omapl138_c6accel.sh $(EXEC_DIR_C6ACCEL)
	@chmod +x $(EXEC_DIR_C6ACCEL)/loadmodules_omapl138_c6accel.sh
endif

