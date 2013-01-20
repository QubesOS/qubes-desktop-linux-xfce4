%global xfceversion 4.10

Name:           xfwm4
Version:        4.10.0
Release:        5%{?dist}
Summary:        Next generation window manager for Xfce

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfwm4
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# Fix window grabbing with gtk3 windows (#845272=
# Upstream bug: https://bugzilla.xfce.org/show_bug.cgi?id=8949
# Upstream fix: http://git.xfce.org/xfce/xfwm4/commit/?id=0b39bbe0
Patch0:         xfwm4-4.10.0-gtk3-windows.patch
# Fix potential crash in xfce4-settings-manager through wrong xfwm4 settings
# Upstream bug: https://bugzilla.xfce.org/show_bug.cgi?id=9108
# Upstream fix: http://git.xfce.org/xfce/xfwm4/commit/?id=f09ea920
Patch1:         xfwm4-4.10.0-wrong-title-alignment.patch
# Delete active workspace instead of last workspace
# Upstream bug: https://bugzilla.xfce.org/show_bug.cgi?id=8827
# Upstream fix: http://git.xfce.org/xfce/xfwm4/commit/?id=0003144f
Patch2:         xfwm4-4.10.0-workspace-deletion.patch
## Downstream patches:
# Fix desktop categories
Patch10:        xfwm4-4.9.0-desktop-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libXext-devel
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  startup-notification-devel >= 0.5
BuildRequires:  libglade2-devel
BuildRequires:  libwnck-devel >= 2.22
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils
Provides:       firstboot(windowmanager) = xfwm4

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%setup -q
%patch0 -p1 -b .gtk3
%patch1 -p1 -b .title-alignment
%patch2 -p1 -b .workspace-deletion
%patch10 -p1 -b .categories


%build
%configure  --disable-static

make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

%find_lang %{name}

for file in $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc example.gtkrc-2.0 README TODO COPYING AUTHORS COMPOSITOR
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfwm4
%{_datadir}/themes/*
%dir %{_libdir}/xfce4/xfwm4/
%{_libdir}/xfce4/xfwm4/helper-dialog


%changelog
* Sun Oct 07 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-5
- Delete active workspace instead of last workspace (bugzilla.xfce.org #8827)

* Sat Oct 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-4
- Fix potential crash in xfce4-settings-manager (bugzilla.xfce.org #9108)

* Sat Aug 11 2012 Kevin Fenzi <kevin@scrye.com> - 4.10.0-3
- Add patch to fix grabbing on gtk3 apps. Fixes bug #845272

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final
- Drop Nodoka patch
- Make build verbose
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.1-1
- Update to 4.9.1 (Xfce 4.10pre1)

* Mon Apr 02 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.0-1
- Update to 4.9.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Kevin Fenzi <kevin@scrye.com> - 4.8.3-1
- Update to 4.8.3

* Tue Nov 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.2-1
- Update to 4.8.2
- Remove all upstreamed patches
- Apply Nodoka theme only in Fedora

* Tue Nov 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-5
- Provide window manager for firstboot (#750397)

* Sat Oct 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-4
- Another patch to fix resizing (#670173)

* Mon Sep 19 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-3
- Be less strict on size changes (#670173)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.1-1
- Update to 4.8.1

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4
- Update icon-cache scriptlets

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Mon Nov 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1

* Wed Sep 29 2010 Jesse Keating <jkeating@fedoraproject.org> - 4.6.2-3
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.2-2
- Provide firstboot(windowmanager)

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.2-1
- Update to 4.6.2

* Sat Feb 13 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.1-7
- Add patch to fix DSO linking issue. Fixes bug #564730

* Sun Dec 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-6
- Add patch for multi monitor issue (xfce bug #5795)

* Sun Sep 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-5
- Validate *.desktop files

* Sun Sep 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-4
- Make Nodoka default (fixes bug #491092)

* Tue Jul 28 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-3
- Add patch for focus issue (fixes bug #514206)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-1
- Update to 4.6.1

* Sat Feb 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.0-2
- Fix directory ownership problems
- Require xfce4-doc

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-1
- Update to 4.6.0
- Remove unneeded BuildRequires

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.99.1-1
- Update to 4.5.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.93-1
- Update to 4.5.93

* Sat Dec 27 2008 Kevin Fenzi <kevin@tummy.com> - 4.5.92-1
- Update to 4.5.92

* Mon Oct 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3
- Update gtk-update-icon-cache scriptlets

* Sun Jul 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.2-4
- Really switch to Nodoka theme

* Wed Apr 23 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.2-3
- Switch to Nodoka theme by default
- disable-static instead of removing *.a files

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-2
- Rebuild for gcc43

* Sun Nov 18 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.2-1
- Update to 4.4.2

* Mon Aug 27 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-3
- Update License tag

* Mon Jul  9 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-2
- Add patch for gtk2 hang issue (fixes #243735) 

* Wed Apr 11 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Update to 4.4.1

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-1
- Update to 4.4.0

* Fri Nov 10 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-1
- Update to 4.3.99.2

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-6
- Fix defattr
- Add gtk-update-icon-cache

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-5
- Bump release for devel checkin

* Mon Oct  2 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-4
- Own the datadir/xfce4 directory

* Mon Oct  2 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-3
- Add libXcomposite-devel and libXdamage-devel BuildRequires
- Add startup-notification-devel BuildRequires

* Sun Sep 24 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-2
- Don't own the xfce4 docdir. (xfdesktop does)

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-1
- Upgrade to 4.3.99.1
- Fix macro in changelog

* Wed Jul 12 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.2-1
- Upgrade to 4.3.90.2

* Mon May  8 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.1-1
- Upgrade 4.3.90.1

* Thu Nov 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3.2-3.fc5
- Added libXpm-devel and libXext-devel BuildRequires

* Thu Nov 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3.2-2.fc5
- Add imake and libXt-devel BuildRequires

* Wed Nov 16 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3.2-1.fc5
- Update to 4.2.3.2

* Mon Nov  7 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3.1-1.fc5
- Update to 4.2.3.1
- Added dist tag
- Rediffed bluecurve-prep patch

* Tue May 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.2-1.fc4
- Update to 4.2.2
- Rediffed bluecurve-prep patch
- Removed focus patch (applied upstream)

* Sun Mar 27 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-5.fc4
- Add patch for focus issue (bug #152299)

* Fri Mar 25 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-4.fc4
- lowercase Release

* Wed Mar 23 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-3.FC4
- Removed unneeded a/la files

* Sun Mar 20 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-2
- Readded changelogs
- Split old fedora patch into a bluecurve-prep and bluecurve patch and applied

* Tue Mar 15 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-1
- Updated to version 4.2.1

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-2
- Removed generic INSTALL from %%doc
- Fixed case of Xfce

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-1
- Inital Fedora Extras version

* Thu Jan 27 2005 Than Ngo <than@redhat.com> 4.2.0-1
- 4.2.0

* Mon Jul 19 2004 Than Ngo <than@redhat.com> 4.0.6-1
- update to 4.0.6
- use %%find_lang macros

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 20 2004 Than Ngo <than@redhat.com> 4.0.5-2
- Add a patch for stacking request with sibling, thanks to Olivier Fourdan <fourdan@xfce.org>
- Change defaults for fedora, thanks to Olivier Fourdan <fourdan@xfce.org>

* Thu Apr 15 2004 Than Ngo <than@redhat.com> 4.0.5-1
- update to 4.0.5

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Than Ngo <than@redhat.com> 4.0.3.1-2
- fixed dependant libraries check on x86_64

* Tue Jan 13 2004 Than Ngo <than@redhat.com> 4.0.3.1-1
- 4.0.3.1 release

* Mon Jan 12 2004 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3 release

* Thu Dec 25 2003 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2 release

* Tue Dec 16 2003 Than Ngo <than@redhat.com> 4.0.1-1
- initial build
