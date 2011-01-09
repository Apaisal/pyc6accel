#
_XDCBUILDCOUNT = 
ifneq (,$(findstring path,$(_USEXDCENV_)))
override XDCPATH = /home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_26_01_09/examples;/home/anol/workspace/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_26_01_09/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/framework_components_2_25_01_05/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_03/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_03;/home/anol/dvsdk/dvsdk_3_01_00_10/xdais_6_26_01_03/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/linuxutils_2_25_05_11/packages;/home/anol/workspace/pyc6accel/c6accel/soc/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/local_power_manager_linux_1_24_02_09/packages;/packages
override XDCROOT = /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68
override XDCBUILDCFG = ./config.bld
endif
ifneq (,$(findstring args,$(_USEXDCENV_)))
override XDCARGS = 
override XDCTARGETS = 
endif
#
ifeq (0,1)
PKGPATH = /home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_26_01_09/examples;/home/anol/workspace/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/codec_engine_2_26_01_09/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/framework_components_2_25_01_05/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_03/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/dsplink_linux_1_65_00_03;/home/anol/dvsdk/dvsdk_3_01_00_10/xdais_6_26_01_03/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/linuxutils_2_25_05_11/packages;/home/anol/workspace/pyc6accel/c6accel/soc/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/local_power_manager_linux_1_24_02_09/packages;/packages;/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages;..
HOSTOS = Linux
endif
