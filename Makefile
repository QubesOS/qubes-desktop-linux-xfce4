RPMS_DIR=rpm/
help:
	@echo "make rpms        -- generate binary rpm packages"

RPM_DEFINES := --define "_rpmdir $(RPMS_DIR)" \
			   --define "_sourcedir $(PWD)/xfwm4"
SPECFILE := xfwm4/xfwm4.spec

VER_REL := $(shell rpm $(RPM_DEFINES) -q --qf "%{VERSION}-%{RELEASE}\n" --specfile $(SPECFILE)| head -1|sed -e 's/fc../fc13/')

rpms: rpms-dom0

rpms-vm:

rpms-dom0:
	rpmbuild $(RPM_DEFINES) -bb $(SPECFILE)
	rpm --addsign $(RPMS_DIR)/x86_64/*$(VER_REL)*.rpm

srpms:
	rpmbuild $(RPM_DEFINES) -bs $(SPECFILE)
	rpm --addsign $(SRPMS_DIR)/*$(VER_REL)*.rpm

update-repo:
	ln -f rpm/x86_64/*$(VER_REL)*.rpm ../yum/current-release/current/dom0/rpm/

update-repo-testing:
	ln -f rpm/x86_64/*$(VER_REL)*.rpm ../yum/current-release/current-testing/dom0/rpm/

update-repo-unstable:
	ln -f rpm/x86_64/*$(VER_REL)*.rpm ../yum/current-release/unstable/dom0/rpm/

clean:

