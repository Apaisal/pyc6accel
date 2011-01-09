## THIS IS A GENERATED FILE -- DO NOT EDIT
.configuro: .libraries,v5T linker.cmd \
  package/cfg/pyc6accel_xv5T.ov5T \

linker.cmd: package/cfg/pyc6accel_xv5T.xdl
	$(SED) 's"^\"\(package/cfg/pyc6accel_xv5Tcfg.cmd\)\"$""\"/home/anol/workspace/pyc6accel/pyc6accel_config/\1\""' package/cfg/pyc6accel_xv5T.xdl > $@
