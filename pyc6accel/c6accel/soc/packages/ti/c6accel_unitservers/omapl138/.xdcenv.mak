#
_XDCBUILDCOUNT = 1
ifneq (,$(findstring path,$(_USEXDCENV_)))
override XDCPATH = /home/anol/workspace/pyc6accel/c6accel/soc;packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/xdais_6_26_00_02/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/framework-components_2_25_03_07/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/framework-components_2_25_03_07/fctools/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/dspbios_5_41_03_17/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/biosutils_1_02_02/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/linuxutils_2_25_05_11/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/dsplink_1_65_00_02/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/dsplink_1_65_00_02;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/codec-engine_2_26_01_09/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/codec-engine_2_26_01_09/cetools/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/edma3lld_01_11_00_03/packages;/packages
override XDCROOT = /home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/xdctools_3_16_03_36
override XDCBUILDCFG = /home/anol/workspace/pyc6accel/c6accel/config.bld
endif
ifneq (,$(findstring args,$(_USEXDCENV_)))
override XDCARGS = "prod"
override XDCTARGETS = ti.targets.C64P
endif
#
ifeq (0,1)
PKGPATH = /home/anol/workspace/pyc6accel/c6accel/soc;packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/xdais_6_26_00_02/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/framework-components_2_25_03_07/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/framework-components_2_25_03_07/fctools/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/dspbios_5_41_03_17/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/biosutils_1_02_02/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/linuxutils_2_25_05_11/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/dsplink_1_65_00_02/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/dsplink_1_65_00_02;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/codec-engine_2_26_01_09/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/codec-engine_2_26_01_09/cetools/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/edma3lld_01_11_00_03/packages;/packages;/home/anol/ti-dvsdk_dm3730-evm_4_01_00_09/xdctools_3_16_03_36/packages;../../..
HOSTOS = Linux
endif
