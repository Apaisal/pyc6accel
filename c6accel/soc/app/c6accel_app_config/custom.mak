## THIS IS A GENERATED FILE -- DO NOT EDIT
.configuro: .libraries,v5T linker.cmd \
  package/cfg/c6accel_app_xv5T.ov5T \

linker.cmd: package/cfg/c6accel_app_xv5T.xdl
	$(SED) 's"^\"\(package/cfg/c6accel_app_xv5Tcfg.cmd\)\"$""\"/home/anol/dvsdk/dvsdk_3_01_00_10/c6accel_1_01_00_02/soc/app/c6accel_app_config/\1\""' package/cfg/c6accel_app_xv5T.xdl > $@
