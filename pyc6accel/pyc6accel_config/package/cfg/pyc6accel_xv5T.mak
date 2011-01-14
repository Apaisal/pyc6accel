#
#  Do not edit this file.  This file is generated from 
#  package.bld.  Any modifications to this file will be 
#  overwritten whenever makefiles are re-generated.
#
#  target compatibility key = gnu.targets.arm.GCArmv5T{1,0,4.5,1
#
ifneq (clean,$(MAKECMDGOALS))
-include package/cfg/pyc6accel_xv5T.ov5T.dep
endif

package/cfg/pyc6accel_xv5T.ov5T: | .interfaces
package/cfg/pyc6accel_xv5T.ov5T: package/cfg/pyc6accel_xv5T.c package/cfg/pyc6accel_xv5T.mak
	@$(RM) $@.dep
	$(RM) $@
	@$(MSG) clv5T $< ...
	$(gnu.targets.arm.GCArmv5T.rootDir)/bin/arm-none-linux-gnueabi-gcc -c -MD -MF $@.dep -x c  -fPIC -Wunused -march=armv5t -Dfar=   -Dxdc_cfg__header__='pyc6accel_config/package/cfg/pyc6accel_xv5T.h'  -Dxdc_target_name__=GCArmv5T -Dxdc_target_types__=gnu/targets/arm/std.h -Dxdc_bld__profile_release -Dxdc_bld__vers_1_0_4_5_1 -O2 -ffunction-sections -fdata-sections  $(XDCINCS)  -o $@ $<
	-@$(FIXDEP) $@.dep $@.dep
	
package/cfg/pyc6accel_xv5T.ov5T:LD_LIBRARY_PATH=

package/cfg/pyc6accel_xv5T.sv5T: | .interfaces
package/cfg/pyc6accel_xv5T.sv5T: package/cfg/pyc6accel_xv5T.c package/cfg/pyc6accel_xv5T.mak
	@$(RM) $@.dep
	$(RM) $@
	@$(MSG) clv5T -S $< ...
	$(gnu.targets.arm.GCArmv5T.rootDir)/bin/arm-none-linux-gnueabi-gcc -c -MD -MF $@.dep -x c -S -fPIC -Wunused -march=armv5t -Dfar=   -Dxdc_cfg__header__='pyc6accel_config/package/cfg/pyc6accel_xv5T.h'  -Dxdc_target_name__=GCArmv5T -Dxdc_target_types__=gnu/targets/arm/std.h -Dxdc_bld__profile_release -Dxdc_bld__vers_1_0_4_5_1 -O2 -ffunction-sections -fdata-sections  $(XDCINCS)  -o $@ $<
	-@$(FIXDEP) $@.dep $@.dep
	
package/cfg/pyc6accel_xv5T.sv5T:LD_LIBRARY_PATH=

clean,v5T ::
	-$(RM) package/cfg/pyc6accel_xv5T.ov5T
	-$(RM) package/cfg/pyc6accel_xv5T.sv5T

pyc6accel.xv5T: package/cfg/pyc6accel_xv5T.ov5T package/cfg/pyc6accel_xv5T.mak

clean::
	-$(RM) package/cfg/pyc6accel_xv5T.mak