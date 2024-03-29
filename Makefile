all:
	@true

install-common:
	install -m 644 -D xfce4-panel-qubes-default.xml $(DESTDIR)/etc/xdg/xfce4/panel/default.xml.qubes
	install -m 644 -D xsettings.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml.qubes
	install -m 644 -D xfwm4.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml
	install -m 644 -D xfce4-desktop.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
	install -m 644 -D xfce4-session.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml.qubes
	install -m 644 -D xfce4-power-manager.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml.qubes
	install -m 644 -D xfce4-keyboard-shortcuts.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml.qubes
	install -m 644 -D xfce4-xss-lock.desktop $(DESTDIR)/etc/xdg/autostart/xfce4-xss-lock.desktop
	install -m 644 -D xscreensaver-xfce.desktop $(DESTDIR)/etc/xdg/autostart/xscreensaver-xfce.desktop
	install -m 644 -D qubes-update-xfce-config.desktop $(DESTDIR)/etc/xdg/autostart/qubes-update-xfce-config.desktop
	install -m 755 -D update-xfce-config $(DESTDIR)/usr/lib/qubes/update-xfce-config

	ln -s ../../panel/default.xml $(DESTDIR)/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml

install: install-common
	install -D etc/X11/xinit/xinitrc.d/55xfce-qubes.sh $(DESTDIR)/etc/X11/xinit/xinitrc.d/55xfce-qubes.sh

install-debian: install-common
	install -D etc/X11/Xsession.d/55xfce-qubes $(DESTDIR)/etc/X11/Xsession.d/55xfce-qubes

clean:
	rm -rf debian/changelog.*
	rm -rf pkgs
