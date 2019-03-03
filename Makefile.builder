ifeq ($(PACKAGE_SET),dom0)
RPM_SPEC_FILES := garcon/garcon.spec \
                  xfce4-settings-qubes/xfce4-settings-qubes.spec \
                  xfwm4/xfwm4.spec
endif

SOURCE_COPY_IN := copy-sources

copy-sources: sources = $(foreach spec,$(RPM_SPEC_FILES),$(addprefix $(dir $(spec)),$(notdir $(shell spectool -lf $(ORIG_SRC)/$(spec)|cut -f 2 -d ' '))))
copy-sources:
	cd "$(ORIG_SRC)"; cp $(sources) "$(CHROOT_DIR)/$(DIST_SRC)/"
