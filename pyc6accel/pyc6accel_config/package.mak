#
#  Do not edit this file.  This file is generated from 
#  package.bld.  Any modifications to this file will be 
#  overwritten whenever makefiles are re-generated.
#

unexport MAKEFILE_LIST
override PKGDIR = pyc6accel_config
XDCINCS = -I. -I$(strip $(subst ;, -I,$(subst $(space),\$(space),$(XPKGPATH))))
XDCCFGDIR = package/cfg/

#
# The following dependencies ensure package.mak is rebuilt
# in the event that some included BOM script changes.
#
ifneq (clean,$(MAKECMDGOALS))
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/global/Clock.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/global/Clock.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Library.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Library.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/xmlgen2.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/xmlgen2.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/xdc.tci:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/xdc.tci
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/ITargetFilter.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/ITargetFilter.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/UCArm9.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/UCArm9.xs
package.mak: package.bld
/opt/ti/ccsv5/xdctools_3_20_06_81/include/utils.tci:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/include/utils.tci
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/ITarget.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/ITarget.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/package.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/package.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/Linux86.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/Linux86.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Repository.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Repository.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/arm/GCArmv7A.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/arm/GCArmv7A.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/arm/GCArmv6.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/arm/GCArmv6.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/om2.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/om2.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/tools/configuro/template/package.xs.xdt:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/tools/configuro/template/package.xs.xdt
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/_gen.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/_gen.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/tools/configuro/template/custom.mak.exe.xdt:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/tools/configuro/template/custom.mak.exe.xdt
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Script.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Script.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/global/Trace.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/global/Trace.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Manifest.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Manifest.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/ITarget.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/ITarget.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/io/package.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/io/package.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/BuildEnvironment.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/BuildEnvironment.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/package.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/package.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/PackageContents.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/PackageContents.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/Mingw.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/Mingw.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/IPackage.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/IPackage.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/bld.js:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/bld.js
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/package.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/package.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/xmlgen.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/xmlgen.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Utils.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Utils.xs
/home/anol/workspace/pyc6accel/config.bld:
package.mak: /home/anol/workspace/pyc6accel/config.bld
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/template.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/template.xs
package.mak: config.bld
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/tools/configuro/template/compiler.opt.xdt:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/tools/configuro/template/compiler.opt.xdt
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/ti/targets/ITarget.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/ti/targets/ITarget.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/io/File.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/services/io/File.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/ti/targets/package.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/ti/targets/package.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/MVArm9.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/MVArm9.xs
/opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Executable.xs:
package.mak: /opt/ti/ccsv5/xdctools_3_20_06_81/packages/xdc/bld/Executable.xs
endif

gnu.targets.arm.GCArmv5T.rootDir ?= /home/anol/CodeSourcery/Sourcery_G++_Lite/
gnu.targets.arm.packageBase ?= /opt/ti/ccsv5/xdctools_3_20_06_81/packages/gnu/targets/arm/
.PRECIOUS: $(XDCCFGDIR)/%.ov5T
.PHONY: all,v5T .dlls,v5T .executables,v5T test,v5T
all,v5T: .executables,v5T
.executables,v5T: .libraries,v5T
.executables,v5T: .dlls,v5T
.dlls,v5T: .libraries,v5T
.libraries,v5T: .interfaces
	@$(RM) $@
	@$(TOUCH) "$@"

.help::
	@$(ECHO) xdc test,v5T
	@$(ECHO) xdc .executables,v5T
	@$(ECHO) xdc .libraries,v5T
	@$(ECHO) xdc .dlls,v5T


all: .executables 
.executables: .libraries .dlls
.libraries: .interfaces

PKGCFGS := $(wildcard package.xs) package/build.cfg
.interfaces: package/package.xdc.inc package/package.defs.h package.xdc $(PKGCFGS)

-include package/package.xdc.dep
package/%.xdc.inc package/%_pyc6accel_config.c package/%.defs.h: %.xdc $(PKGCFGS)
	@$(MSG) generating interfaces for package pyc6accel_config" (because $@ is older than $(firstword $?))" ...
	$(XSRUN) -f xdc/services/intern/cmd/build.xs $(MK_IDLOPTS) -m package/package.xdc.dep -i package/package.xdc.inc package.xdc

.executables,v5T .executables: pyc6accel.xv5T

-include package/cfg/pyc6accel_xv5T.mak
ifneq (clean,$(MAKECMDGOALS))
-include package/cfg/pyc6accel_xv5T.dep
endif
package/cfg/pyc6accel_xv5T.ov5T : | package/cfg/pyc6accel_xv5T.xdl
pyc6accel.xv5T:
	$(RM) $@
	@$(MSG) lnkv5T $@ ...
	$(gnu.targets.arm.GCArmv5T.rootDir)/bin/arm-none-linux-gnueabi-gcc    -o $@ package/cfg/pyc6accel_xv5T.ov5T  package/cfg/pyc6accel_xv5T.xdl  -Wl,-Map=$(XDCCFGDIR)/$@.map -lstdc++ -L$(gnu.targets.arm.GCArmv5T.rootDir)/arm-none-linux-gnueabi/lib
	
pyc6accel.xv5T:LD_LIBRARY_PATH=


ifeq (,$(wildcard .libraries,v5T))
pyc6accel.xv5T package/cfg/pyc6accel_xv5T.c: .libraries,v5T
endif

package/cfg/pyc6accel_xv5T.c package/cfg/pyc6accel_xv5T.h package/cfg/pyc6accel_xv5T.xdl: override _PROG_NAME := pyc6accel.xv5T
package/cfg/pyc6accel_xv5T.c: package/cfg/pyc6accel_xv5T.cfg
pyc6accel.test test,v5T test: pyc6accel.xv5T.test

pyc6accel.xv5T.test:: pyc6accel.xv5T
ifeq (,$(_TESTLEVEL))
	@$(MAKE) -R -r --no-print-directory -f $(XDCROOT)/packages/xdc/bld/xdc.mak _TESTLEVEL=1 pyc6accel.xv5T.test
else
	@$(MSG) running $<  ...
	$(call EXEC.pyc6accel.xv5T, ) 
endif


clean:: clean,v5T
	-$(RM) package/cfg/pyc6accel_xv5T.cfg
	-$(RM) package/cfg/pyc6accel_xv5T.dep
	-$(RM) package/cfg/pyc6accel_xv5T.c
	-$(RM) package/cfg/pyc6accel_xv5T.xdc.inc

clean,v5T::
	-$(RM) pyc6accel.xv5T
	-$(RM) .tmp,pyc6accel.xv5T,*

%,copy:
	@$(if $<,,$(MSG) don\'t know how to build $*; exit 1)
	@$(MSG) cp $< $@
	$(RM) $@
	$(CP) $< $@
pyc6accel_xv5T.sv5T,copy : package/cfg/pyc6accel_xv5T.sv5T
pyc6accel_xv5T.ov5T,copy : package/cfg/pyc6accel_xv5T.ov5T

$(XDCCFGDIR)%.c $(XDCCFGDIR)%.h $(XDCCFGDIR)%.xdl: $(XDCCFGDIR)%.cfg .interfaces $(XDCROOT)/packages/xdc/cfg/Main.xs
	@$(MSG) "configuring $(_PROG_NAME) from $< ..."
	$(CONFIG) $(_PROG_XSOPTS) xdc.cfg $(_PROG_NAME) $(XDCCFGDIR)$*.cfg $(XDCCFGDIR)$*

.PHONY: release,pyc6accel_config
pyc6accel_config.tar: package/build.cfg
pyc6accel_config.tar: package/package.ext.xml
pyc6accel_config.tar: package/package.xdc.inc
pyc6accel_config.tar: package/package.bld.xml
pyc6accel_config.tar: package/package.rel.dot
ifneq (clean,$(MAKECMDGOALS))
-include package/rel/pyc6accel_config.tar.dep
endif
package/rel/pyc6accel_config/pyc6accel_config/package/package.rel.xml:

pyc6accel_config.tar: package/rel/pyc6accel_config.xdc.inc package/rel/pyc6accel_config/pyc6accel_config/package/package.rel.xml
	@$(MSG) making release file $@ "(because of $(firstword $?))" ...
	-$(RM) $@
	$(call MKRELTAR,package/rel/pyc6accel_config.xdc.inc,package/rel/pyc6accel_config.tar.dep)


release release,pyc6accel_config: all pyc6accel_config.tar
clean:: .clean
	-$(RM) pyc6accel_config.tar
	-$(RM) package/rel/pyc6accel_config.xdc.inc
	-$(RM) package/rel/pyc6accel_config.tar.dep

clean:: .clean
	-$(RM) .libraries .libraries,*
clean:: 
	-$(RM) .dlls .dlls,*
#
# The following clean rule removes user specified
# generated files or directories.
#

ifneq (clean,$(MAKECMDGOALS))
ifeq (,$(wildcard package))
    $(shell $(MKDIR) package)
endif
ifeq (,$(wildcard package/external))
    $(shell $(MKDIR) package/external)
endif
ifeq (,$(wildcard package/lib))
    $(shell $(MKDIR) package/lib)
endif
ifeq (,$(wildcard package/cfg))
    $(shell $(MKDIR) package/cfg)
endif
ifeq (,$(wildcard package/rel))
    $(shell $(MKDIR) package/rel)
endif
ifeq (,$(wildcard package/internal))
    $(shell $(MKDIR) package/internal)
endif
endif
clean::
	-$(RMDIR) package

include custom.mak
