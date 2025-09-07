# crackAhash Makefile
# Install or uninstall the tool system-wide

DESTDIR ?= /usr/local/bin
TARGET  = crackAhash

install:
	@sudo cp crackAhash.py $(DESTDIR)/$(TARGET)
	@sudo chmod +x $(DESTDIR)/$(TARGET)
	@echo "crackAhash installed successfully! Run it anywhere with '$(TARGET)'"

uninstall:
	@sudo rm -f $(DESTDIR)/$(TARGET)
	@echo "crackAhash has been removed from the kitchen!"

