Name:		xfce4-settings-qubes
Version:	1.0
Release:	1%{?dist}
Summary:	Default Xfce4 panel settings for Qubes

Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://www.qubes-os.org/
Source0:	xfce4-panel-qubes-default.xml
Source1:	inhibit-systemd-power-handling.desktop
Source2:	xsettings.xml
Source3:	xfce4-power-manager.xml

Requires:	xfce4-panel
Requires(post):	xfce4-panel

%description
%{summary}

%prep

%build


%install
install -m 644 -D %{SOURCE0} %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/qubes-default.xml
install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/inhibit-systemd-power-handling.desktop
install -m 644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/qubes-xsettings.xml
install -m 644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml

%post
REPLACEFILE="${REPLACEFILE} %{_sysconfdir}/xdg/xfce4/panel/qubes-default.xml"
REPLACEFILE="${REPLACEFILE} %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/qubes-xsettings.xml"
for file in ${REPLACEFILE}; do
	origfile="`echo $file | sed s/qubes-//`"
	backupfile="`echo $file | sed s/qubes-/xfce4-/`"
	if [ -r "$origfile" -a ! -r "$backupfile" ]; then
		mv -f "$origfile" "$backupfile"
	fi
	cp -f "$file" "$origfile"
done

%triggerin -- xfce4-panel
if [ -r /etc/xdg/xfce4/panel/default.xml ! -r /etc/xdg/xfce4/panel/xfce4-default.xml ]; then
	mv -f /etc/xdg/xfce4/panel/default.xml /etc/xdg/xfce4/panel/xfce4-default.xml
fi
cp -f /etc/xdg/xfce4/panel/qubes-default.xml /etc/xdg/xfce4/panel/default.xml

%triggerin -- xfce4-settings
file="%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/qubes-xsettings.xml"
origfile="`echo $file | sed s/qubes-//`"
backupfile="`echo $file | sed s/qubes-/xfce4-/`"
if [ -r "$origfile" -a ! -r "$backupfile" ]; then
	mv -f "$origfile" "$backupfile"
fi
cp -f "$file" "$origfile"


%files
%{_sysconfdir}/xdg/autostart/inhibit-systemd-power-handling.desktop
%{_sysconfdir}/xdg/xfce4/panel/qubes-default.xml
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/qubes-xsettings.xml
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml


%changelog

