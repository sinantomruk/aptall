PREFIX?=	/usr
BINDIR=		${PREFIX}/bin

all:
	@echo Run \'make install\' to install aptall on your device

install:
	@mkdir -p $(DESTDIR)$(BINDIR)
	@cp aptall.py $(DESTDIR)$(BINDIR)/aptall
	@chmod 755 $(DESTDIR)$(BINDIR)/aptall
	@echo aptall has been installed on your device

uninstall:
	@rm -rf $(DESTDIR)$(BINDIR)/aptall
	@rmdir -p --ignore-fail-on-non-empty $(DESTDIR)$(BINDIR)
	@echo aptall has been removed from your device
