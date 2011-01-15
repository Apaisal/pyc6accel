#
_XDCBUILDCOUNT = 0
ifneq (,$(findstring path,$(_USEXDCENV_)))
override XDCPATH = /home/anol/workspace/pyc6accel/c6accel/soc;packages;/home/anol/dvsdk/dvsdk_3_01_00_10/xdais_6_25_02_11/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/framework_components_2_25_01_05/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/framework_components_2_25_01_05/fctools/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/bios_5_41_00_06/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/biosutils_1_02_02/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/linuxutils_2_25_02_08/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_02/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_02;/home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_25_02_11/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_25_02_11/cetools/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/edma3_lld_01_11_00_03/packages;/packages
override XDCROOT = /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27
override XDCBUILDCFG = /home/anol/workspace/pyc6accel/c6accel/config.bld
endif
ifneq (,$(findstring args,$(_USEXDCENV_)))
override XDCARGS = "prod"
override XDCTARGETS = ti.targets.C64P
endif
#
ifeq (0,1)
PKGPATH = /home/anol/workspace/pyc6accel/c6accel/soc;packages;/home/anol/dvsdk/dvsdk_3_01_00_10/xdais_6_25_02_11/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/framework_components_2_25_01_05/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/framework_components_2_25_01_05/fctools/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/bios_5_41_00_06/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/biosutils_1_02_02/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/linuxutils_2_25_02_08/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_02/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_02;/home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_25_02_11/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_25_02_11/cetools/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/edma3_lld_01_11_00_03/packages;/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages;../../..
HOSTOS = Linux
endif
