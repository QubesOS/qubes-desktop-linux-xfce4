Name:		xfce4-settings-qubes
Version:	1.1
Release:	1%{?dist}
Summary:	Default Xfce4 panel settings for Qubes

Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://www.qubes-os.org/
Source0:	xfce4-panel-qubes-default.xml
Source1:	inhibit-systemd-power-handling.desktop
Source2:	xsettings.xml
Source3:	xfce4-power-manager.xml
Source4:	xfwm4.xml

Requires:	xfce4-panel
Requires(post):	xfce4-panel

%description
%{summary}

%prep

%build


%install
install -m 644 -D %{SOURCE0} %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/default.xml.qubes
install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/inhibit-systemd-power-handling.desktop
install -m 644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml.qubes
install -m 644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
install -m 644 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml

%define settings_replace() \
origfile="`echo %{1} | sed 's/\.qubes$//'`"\
backupfile="`echo %{1} | sed s/\.qubes$/\.xfce4/`"\
if [ -r "$origfile" -a ! -r "$backupfile" ]; then\
	mv -f "$origfile" "$backupfile"\
fi\
cp -f "%{1}" "$origfile"\
%{nil}

%triggerin -- xfce4-panel
%settings_replace %{_sysconfdir}/xdg/xfce4/panel/default.xml.qubes

%triggerin -- xfce4-settings
%settings_replace %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml.qubes

%postun
REPLACEFILE="${REPLACEFILE} %{_sysconfdir}/xdg/xfce4/panel/default.xml.qubes"
REPLACEFILE="${REPLACEFILE} %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml.qubes"
if [ $1 -lt 1 ]; then
	for file in ${REPLACEFILE}; do
		origfile="`echo $file | sed 's/\.qubes$//'`"
		backupfile="`echo $file | sed 's/\.qubes$/\.xfce4/'`"
		mv -f "$backupfile" "$origfile"
	done
fi

%files
%{_sysconfdir}/xdg/autostart/inhibit-systemd-power-handling.desktop
%{_sysconfdir}/xdg/xfce4/panel/default.xml.qubes
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml.qubes
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml


%changelog

