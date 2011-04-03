RPMS_DIR=rpm/
help:
	@echo "make rpms        -- generate binary rpm packages"

rpms:   
	rpmbuild --define "_rpmdir $(RPMS_DIR)" --define "_sourcedir $(PWD)/xfwm4" -bb xfwm4/xfwm4.spec
	rpm --addsign $(RPMS_DIR)/x86_64/*.rpm
