#
#  Do not edit this file.  This file is generated from 
#  package.bld.  Any modifications to this file will be 
#  overwritten whenever makefiles are re-generated.
#

unexport MAKEFILE_LIST
override PKGDIR = ti/c6accel/ce
XDCINCS = -I. -I$(strip $(subst ;, -I,$(subst $(space),\$(space),$(XPKGPATH))))
XDCCFGDIR = package/cfg/

#
# The following dependencies ensure package.mak is rebuilt
# in the event that some included BOM script changes.
#
ifneq (clean,$(MAKECMDGOALS))
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/xmlgen.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/xmlgen.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/MSP430_large_code.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/MSP430_large_code.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/ITarget.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/ITarget.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Executable.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Executable.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Script.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Script.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/MVArm9.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/MVArm9.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/services/global/Clock.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/services/global/Clock.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/_gen.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/_gen.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/Linux86.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/Linux86.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/UCArm9.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/UCArm9.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/arm/GCArmv7A.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/arm/GCArmv7A.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/om2.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/om2.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/MSP430_large_data.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/MSP430_large_data.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Repository.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Repository.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/IPackage.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/IPackage.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/BuildEnvironment.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/BuildEnvironment.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/ITarget.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/ITarget.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/services/global/Trace.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/services/global/Trace.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/include/utils.tci:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/include/utils.tci
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/xdc.tci:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/xdc.tci
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/arm/GCArmv6.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/arm/GCArmv6.xs
package.mak: package.bld
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/template.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/template.xs
/home/anol/workspace/pyc6accel/c6accel/config.bld:
package.mak: /home/anol/workspace/pyc6accel/c6accel/config.bld
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Utils.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Utils.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/xmlgen2.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/xmlgen2.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Library.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/Library.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/PackageContents.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/PackageContents.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/ITarget.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/ITarget.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/Mingw.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/gnu/targets/Mingw.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/MSP430.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/ti/targets/MSP430.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/ITargetFilter.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_16_01_27/packages/xdc/bld/ITargetFilter.xs
endif

all,64P .libraries,64P .dlls,64P .executables,64P test,64P:;

all: .executables 
.executables: .libraries .dlls
.libraries: .interfaces

PKGCFGS := $(wildcard package.xs) package/build.cfg
.interfaces: package/package.xdc.inc package/package.defs.h package.xdc $(PKGCFGS)

-include package/package.xdc.dep
package/%.xdc.inc package/%_ti.c6accel.ce.c package/%.defs.h: %.xdc $(PKGCFGS)
	@$(MSG) generating interfaces for package ti.c6accel.ce" (because $@ is older than $(firstword $?))" ...
	$(XSRUN) -f xdc/services/intern/cmd/build.xs $(MK_IDLOPTS) -m package/package.xdc.dep -i package/package.xdc.inc package.xdc

ifneq (clean,$(MAKECMDGOALS))
-include package/package.cfg.dep
endif

package/package.ext.xml: package/package.cfg.xdc.inc
package/package.cfg.xdc.inc: $(XDCROOT)/packages/xdc/cfg/cfginc.js package.xdc
	@$(MSG) generating schema include file list ...
	$(CONFIG) -f $(XDCROOT)/packages/xdc/cfg/cfginc.js ti.c6accel.ce $@

test:;
%,copy:
	@$(if $<,,$(MSG) don\'t know how to build $*; exit 1)
	@$(MSG) cp $< $@
	$(RM) $@
	$(CP) $< $@

$(XDCCFGDIR)%.c $(XDCCFGDIR)%.h $(XDCCFGDIR)%.xdl: $(XDCCFGDIR)%.cfg .interfaces $(XDCROOT)/packages/xdc/cfg/Main.xs
	@$(MSG) "configuring $(_PROG_NAME) from $< ..."
	$(CONFIG) $(_PROG_XSOPTS) xdc.cfg $(_PROG_NAME) $(XDCCFGDIR)$*.cfg $(XDCCFGDIR)$*

.PHONY: release,ti_c6accel_ce
ti_c6accel_ce.tar: package/build.cfg
ti_c6accel_ce.tar: package/package.cfg.xdc.inc
ti_c6accel_ce.tar: package/package.ext.xml
ti_c6accel_ce.tar: package/package.xdc.inc
ti_c6accel_ce.tar: package/package.bld.xml
ti_c6accel_ce.tar: package/package.rel.dot
ifneq (clean,$(MAKECMDGOALS))
-include package/rel/ti_c6accel_ce.tar.dep
endif
package/rel/ti_c6accel_ce/ti/c6accel/ce/package/package.rel.xml:

ti_c6accel_ce.tar: package/rel/ti_c6accel_ce.xdc.inc package/rel/ti_c6accel_ce/ti/c6accel/ce/package/package.rel.xml
	@$(MSG) making release file $@ "(because of $(firstword $?))" ...
	-$(RM) $@
	$(call MKRELTAR,package/rel/ti_c6accel_ce.xdc.inc,package/rel/ti_c6accel_ce.tar.dep)


release release,ti_c6accel_ce: all ti_c6accel_ce.tar
clean:: .clean
	-$(RM) ti_c6accel_ce.tar
	-$(RM) package/rel/ti_c6accel_ce.xdc.inc
	-$(RM) package/rel/ti_c6accel_ce.tar.dep

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
ifeq (,$(wildcard package/rel))
    $(shell $(MKDIR) package/rel)
endif
ifeq (,$(wildcard package/cfg))
    $(shell $(MKDIR) package/cfg)
endif
ifeq (,$(wildcard package/internal))
    $(shell $(MKDIR) package/internal)
endif
endif
clean::
	-$(RMDIR) package


