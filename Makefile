RPMS_DIR=rpm/
SRPMS_DIR=srpm/
help:
	@echo "make rpms        -- generate binary rpm packages"
	@echo "make srpms       -- generate source rpm packages"

rpms:   
	rpmbuild --define "_rpmdir $(RPMS_DIR)" --define "_sourcedir $(PWD)/xfwm4" -bb xfwm4/xfwm4.spec
	rpm --addsign $(RPMS_DIR)/x86_64/*.rpm

srpms:
	rpmbuild --define "_srcrpmdir $(SRPMS_DIR)" --define "_sourcedir $(PWD)/xfwm4" -bs xfwm4/xfwm4.spec
	rpm --addsign $(SRPMS_DIR)/*.rpm
