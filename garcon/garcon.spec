# Review at https://bugzilla.redhat.com/show_bug.cgi?id=554603

%if 0%{?qubes_builder}
%define _sourcedir %(pwd)/garcon
%endif
%global minorversion 0.6

Name:           garcon
Epoch:		1000
Version:        0.6.1
Release:        1%{?dist}
Summary:        Implementation of the freedesktop.org menu specification

Group:          System Environment/Libraries
# garcon's source code is licensed under the LGPLv2+,
# while its documentation is licensed under the GFDL 1.1
License:        LGPLv2+ and GFDL
URL:            http://xfce.org/
#VCS git:git://git.xfce.org/xfce/garcon
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
Source1:        xfce-documentation.directory
Patch0:         garcon-0.4.0-qubes-menus.patch
Patch1:         fix_large_icons.patch

BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.10.0
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.10.0
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.11.1
BuildRequires:	pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.30.0
BuildRequires:	pkgconfig(gthread-2.0) >= 2.30.0
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.14.0

BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  gettext
BuildRequires:  intltool

Obsoletes:      libxfce4menu < 4.6.3
# because of %%{_datadir}/desktop-directories/xfce-*
Conflicts:      xfdesktop <= 4.6.2

Requires:	qubes-menus

%description
Garcon is an implementation of the freedesktop.org menu specification replacing
the former Xfce menu library libxfce4menu. It is based on GLib/GIO only and 
aims at covering the entire specification except for legacy menus.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       pkgconfig
Obsoletes:      libxfce4menu-devel < 4.6.2

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b.redhat-menus
%patch1 -p1

%build
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags} V=1

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

# fix permissions for libraries
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*.so

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/desktop-directories

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_libdir}/*.so.*
%{_datadir}/desktop-directories/*.directory

%files devel
%doc HACKING STATUS TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/

%changelog
* Fri Jul 29 2016 Kevin Fenzi <kevin@scrye.com> - 0.5.0-1
- Update to 0.5.0. Fixes bug #1361565

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-2
- Fix permissions for installed libraries

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-1
- Update to version 0.4.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Kevin Fenzi <kevin@scrye.com> 0.2.1-3
- Fix obsoletes. Fixes bug #1002131

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 0.2.1-1
- Update to 0.2.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-2
- Don't use redhat-menus, otherwiese we need gnome-menus, too (#750380)

* Sat Apr 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0 (Xfce 4.10 final)
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 0.1.12-1
- Update to 0.1.12 (Xfce 4.10pre1)

* Mon Apr 02 2012 Kevin Fenzi <kevin@scrye.com> - 0.1.11-1
- Update to 0.1.11

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for glibc bug#747377

* Sat Oct 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9
- BR libxfce4util-devel

* Sun Jun 19 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Thu May 05 2011 Christoph Wickert <wickert@kolabsys.com> - 0.1.7-1
- Update to 0.1.7
- Fix redhat-menus.patch to include all icons

* Wed Apr 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6
- Remove Provides: for libxfce4menu since we not really provide it

* Sat Apr 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-5
- Remove internet-mail icons again (moved to exo)
- Update redhat-menus.patch for F15

* Tue Mar 29 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-4
- Add internet-mail icon for exo-mail-reader (#678706)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-2
- Include rebased redhat-menus.patch

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 0.1.5-1
- Update to 0.1.5

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Dec 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-2
- Add patch to use redhat-menus

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.2

* Wed Nov 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Oct 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-2
- Drop dependency on gtk-doc (#604352)

* Fri Feb 26 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Tue Jan 12 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-2
- Build gtk-doc

* Tue Jan 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Initial spec file
