Summary: Next generation window manager for Xfce
Name: xfwm4
Version: 4.6.1
Release: 7%{?dist}
License: GPLv2+
URL: http://www.xfce.org/
Source0: http://www.xfce.org/archive/xfce-%{version}/src/xfwm4-%{version}.tar.bz2
Patch0: xfwm4-4.6.1-nodoka.patch
Patch1: xfwm4-4.6.1-focus.patch
Patch2: xfwm4-4.6.1-multi-monitor.patch
# Upstream bug: http://bugzilla.xfce.org/show_bug.cgi?id=6231
Patch3: xfwm4-4.6.1-dsofix.patch

Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: libxfcegui4 >= %{version}
Requires: xfce4-doc
BuildRequires: libxfcegui4-devel >= %{version}
BuildRequires: libXext-devel
BuildRequires: gettext intltool
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: startup-notification-devel
BuildRequires: libglade2-devel
BuildRequires: libwnck-devel
BuildRequires: xfconf-devel
BuildRequires: desktop-file-utils

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%setup -q
# use Nodoka Theme
%patch0 -p1 -b .nodoka
%patch1 -p1 -b .focus
%patch2 -p1 -b .multiwindow
%patch3 -p1 -b .dsofix

%build
%configure  --disable-static

make %{?_smp_mflags}

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
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc example.gtkrc-2.0 README TODO COPYING AUTHORS COMPOSITOR
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%doc %{_datadir}/xfce4/doc/*/images/*
%doc %{_datadir}/xfce4/doc/*/*.html
%{_datadir}/xfwm4
%{_datadir}/themes/*
%{_libexecdir}/xfce4/xfwm4

%changelog
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
