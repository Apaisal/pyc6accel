#
#  Do not edit this file.  This file is generated from 
#  package.bld.  Any modifications to this file will be 
#  overwritten whenever makefiles are re-generated.
#

unexport MAKEFILE_LIST
override PKGDIR = ti/c6accel_unitservers/omap3530
XDCINCS = -I. -I$(strip $(subst ;, -I,$(subst $(space),\$(space),$(XPKGPATH))))
XDCPKGS = $(call pkgsearch,ti/bios/include )
XDCINCS += $(if $(XDCPKGS),-I$(subst $(space), -I,$(XDCPKGS)))
IMPORTPATH += $(if $(XDCPKGS),;$(subst $(space),;,$(XDCPKGS)))
XDCCFGDIR = package/cfg/

#
# The following dependencies ensure package.mak is rebuilt
# in the event that some included BOM script changes.
#
ifneq (clean,$(MAKECMDGOALS))
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/bld.js:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/bld.js
package.mak: package.bld
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/template.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/template.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Executable.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Executable.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/ITargetFilter.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/ITargetFilter.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/arm/GCArmv6.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/arm/GCArmv6.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Library.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Library.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Manifest.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Manifest.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/xmlgen2.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/xmlgen2.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/IPackage.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/IPackage.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/MVArm9.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/MVArm9.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/BuildEnvironment.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/BuildEnvironment.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Repository.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Repository.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/services/global/Clock.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/services/global/Clock.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/ITarget.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/ITarget.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/xdc.tci:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/xdc.tci
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/services/global/Trace.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/services/global/Trace.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/ti/targets/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/ti/targets/package.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/ITarget.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/ITarget.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/arm/GCArmv7A.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/arm/GCArmv7A.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/_gen.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/_gen.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Utils.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Utils.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/Linux86.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/Linux86.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/PackageContents.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/PackageContents.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/c6accel_1_01_00_02/config.bld:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/c6accel_1_01_00_02/config.bld
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/Mingw.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/Mingw.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/xmlgen.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/xmlgen.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/om2.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/om2.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/ti/targets/ITarget.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/ti/targets/ITarget.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Script.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/xdc/bld/Script.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/UCArm9.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/UCArm9.xs
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/include/utils.tci:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/include/utils.tci
/home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/package.xs:
package.mak: /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/gnu/targets/package.xs
endif

ti.targets.C64P.rootDir ?= /home/anol/TI/TI_CGT_C6000_7.0.4
ti.targets.packageBase ?= /home/anol/dvsdk/dvsdk_3_01_00_10/xdctools_3_20_04_68/packages/ti/targets/
.PRECIOUS: $(XDCCFGDIR)/%.o64P
.PHONY: all,64P .dlls,64P .executables,64P test,64P
all,64P: .executables,64P
.executables,64P: .libraries,64P
.executables,64P: .dlls,64P
.dlls,64P: .libraries,64P
.libraries,64P: .interfaces
	@$(RM) $@
	@$(TOUCH) "$@"

.help::
	@$(ECHO) xdc test,64P
	@$(ECHO) xdc .executables,64P
	@$(ECHO) xdc .libraries,64P
	@$(ECHO) xdc .dlls,64P


all: .executables 
.executables: .libraries .dlls
.libraries: .interfaces

PKGCFGS := $(wildcard package.xs) package/build.cfg
.interfaces: package/package.xdc.inc package/package.defs.h package.xdc $(PKGCFGS)

-include package/package.xdc.dep
package/%.xdc.inc package/%_ti.c6accel_unitservers.omap3530.c package/%.defs.h: %.xdc $(PKGCFGS)
	@$(MSG) generating interfaces for package ti.c6accel_unitservers.omap3530" (because $@ is older than $(firstword $?))" ...
	$(XSRUN) -f xdc/services/intern/cmd/build.xs $(MK_IDLOPTS) -m package/package.xdc.dep -i package/package.xdc.inc package.xdc

.executables,64P .executables: c6accel_omap3530.x64P

package/cfg/c6accel_omap3530_x64Pcfg_c.c package/cfg/c6accel_omap3530_x64Pcfg.s62 package/cfg/c6accel_omap3530_x64Pcfg.cmd: override _PROG_NAME := c6accel_omap3530.x64P
package/cfg/c6accel_omap3530_x64Pcfg_c.c package/cfg/c6accel_omap3530_x64Pcfg.s62 package/cfg/c6accel_omap3530_x64Pcfg.cmd: override _PROG_XSOPTS =  -Dxdc.cfg.check.fatal=false
-include package/cfg/c6accel_omap3530_x64P.mak
ifneq (clean,$(MAKECMDGOALS))
-include package/cfg/c6accel_omap3530_x64P.dep
endif
package/cfg/c6accel_omap3530_x64Pcfg.o64P package/cfg/c6accel_omap3530/main.o64P package/cfg/c6accel_omap3530_x64Pcfg_c.o64P package/cfg/c6accel_omap3530_x64P.o64P : | package/cfg/c6accel_omap3530_x64P.xdl
c6accel_omap3530.x64P: package/cfg/c6accel_omap3530_x64Pcfg.cmd
c6accel_omap3530.x64P:
	$(RM) $@
	@$(MSG) lnk64P $@ ...
	$(RM) $(XDCCFGDIR)/$@.map
	$(ti.targets.C64P.rootDir)/bin/lnk6x -w -q -u _c_int00 -l link.cmd -q -o $@ package/cfg/c6accel_omap3530_x64Pcfg.o64P package/cfg/c6accel_omap3530/main.o64P package/cfg/c6accel_omap3530_x64Pcfg_c.o64P package/cfg/c6accel_omap3530_x64P.o64P  package/cfg/c6accel_omap3530_x64P.xdl  -c -m $(XDCCFGDIR)/$@.map -l $(ti.targets.C64P.rootDir)/lib/rts64plus.lib
	
c6accel_omap3530.x64P:C_DIR=
c6accel_omap3530.x64P: PATH:=$(ti.targets.C64P.rootDir)/bin/:$(PATH)


ifeq (,$(wildcard .libraries,64P))
c6accel_omap3530.x64P package/cfg/c6accel_omap3530_x64P.c: .libraries,64P
endif

package/cfg/c6accel_omap3530_x64P.c package/cfg/c6accel_omap3530_x64P.h package/cfg/c6accel_omap3530_x64P.xdl: override _PROG_NAME := c6accel_omap3530.x64P
package/cfg/c6accel_omap3530_x64P.c package/cfg/c6accel_omap3530_x64P.xdl: override _PROG_XSOPTS =  -Dxdc.cfg.check.fatal=false
package/cfg/c6accel_omap3530_x64P.c: package/cfg/c6accel_omap3530_x64P.cfg
c6accel_omap3530.test test,64P test: c6accel_omap3530.x64P.test

c6accel_omap3530.x64P.test:: c6accel_omap3530.x64P
ifeq (,$(_TESTLEVEL))
	@$(MAKE) -R -r --no-print-directory -f $(XDCROOT)/packages/xdc/bld/xdc.mak _TESTLEVEL=1 c6accel_omap3530.x64P.test
else
	@$(MSG) running $<  ...
	$(call EXEC.c6accel_omap3530.x64P, ) 
endif


clean:: clean,64P
	-$(RM) package/cfg/c6accel_omap3530_x64P.cfg
	-$(RM) package/cfg/c6accel_omap3530_x64P.dep
	-$(RM) package/cfg/c6accel_omap3530_x64P.c
	-$(RM) package/cfg/c6accel_omap3530_x64P.xdc.inc

clean,64P::
	-$(RM) c6accel_omap3530.x64P
	-$(RM) .tmp,c6accel_omap3530.x64P,*

clean:: 
	-$(RM) package/cfg/c6accel_omap3530_x64P.pjt
%,copy:
	@$(if $<,,$(MSG) don\'t know how to build $*; exit 1)
	@$(MSG) cp $< $@
	$(RM) $@
	$(CP) $< $@
c6accel_omap3530_x64P.o64P,copy : package/cfg/c6accel_omap3530_x64P.o64P
c6accel_omap3530_x64P.s64P,copy : package/cfg/c6accel_omap3530_x64P.s64P
c6accel_omap3530_x64Pcfg.o64P,copy : package/cfg/c6accel_omap3530_x64Pcfg.o64P
main.o64P,copy : package/cfg/c6accel_omap3530/main.o64P
main.s64P,copy : package/cfg/c6accel_omap3530/main.s64P
c6accel_omap3530_x64Pcfg_c.o64P,copy : package/cfg/c6accel_omap3530_x64Pcfg_c.o64P
c6accel_omap3530_x64Pcfg_c.s64P,copy : package/cfg/c6accel_omap3530_x64Pcfg_c.s64P

$(XDCCFGDIR)%cfg.s62 $(XDCCFGDIR)%cfg_c.c $(XDCCFGDIR)%cfg.cmd $(XDCCFGDIR)%.c $(XDCCFGDIR)%.h $(XDCCFGDIR)%.xdl: $(XDCCFGDIR)%.cfg .interfaces $(XDCROOT)/packages/xdc/cfg/Main.xs
	@$(MSG) "configuring $(_PROG_NAME) from $< ..."
	$(CONFIG) $(_PROG_XSOPTS) xdc.cfg $(_PROG_NAME) $(XDCCFGDIR)$*.cfg $(XDCCFGDIR)$*

.PHONY: release,ti_c6accel_unitservers_omap3530
ti_c6accel_unitservers_omap3530.tar: package/build.cfg
ti_c6accel_unitservers_omap3530.tar: package/info
ti_c6accel_unitservers_omap3530.tar: package/package.ext.xml
ti_c6accel_unitservers_omap3530.tar: package/package.xdc.inc
ti_c6accel_unitservers_omap3530.tar: package/package.bld.xml
ti_c6accel_unitservers_omap3530.tar: c6accel_omap3530.x64P
ti_c6accel_unitservers_omap3530.tar: package/package.rel.dot
ifneq (clean,$(MAKECMDGOALS))
-include package/rel/ti_c6accel_unitservers_omap3530.tar.dep
endif
package/rel/ti_c6accel_unitservers_omap3530/ti/c6accel_unitservers/omap3530/package/package.rel.xml:

ti_c6accel_unitservers_omap3530.tar: package/rel/ti_c6accel_unitservers_omap3530.xdc.inc package/rel/ti_c6accel_unitservers_omap3530/ti/c6accel_unitservers/omap3530/package/package.rel.xml
	@$(MSG) making release file $@ "(because of $(firstword $?))" ...
	-$(RM) $@
	$(call MKRELTAR,package/rel/ti_c6accel_unitservers_omap3530.xdc.inc,package/rel/ti_c6accel_unitservers_omap3530.tar.dep)


release release,ti_c6accel_unitservers_omap3530: all ti_c6accel_unitservers_omap3530.tar
clean:: .clean
	-$(RM) ti_c6accel_unitservers_omap3530.tar
	-$(RM) package/rel/ti_c6accel_unitservers_omap3530.xdc.inc
	-$(RM) package/rel/ti_c6accel_unitservers_omap3530.tar.dep

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
ifeq (,$(wildcard package/cfg/c6accel_omap3530))
    $(shell $(MKDIR) package/cfg/c6accel_omap3530)
endif
ifeq (,$(wildcard package/internal))
    $(shell $(MKDIR) package/internal)
endif
endif
clean::
	-$(RMDIR) package


clean:: 
	-$(RM) package/ti.c6accel_unitservers.omap3530.pjt