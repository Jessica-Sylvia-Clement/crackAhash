# crackAhash Makefile
# Install or uninstall the tool system-wide

DESTDIR ?= /usr/local/bin
TARGET  = crackAhash
PYTHON  = python3

install:
	@# Check if venv is installed
	@if ! $(PYTHON) -m venv --help >/dev/null 2>&1; then \
		echo "❌ python3-venv is not installed."; \
		echo "👉 Install it with: sudo apt install python3-venv"; \
		exit 1; \
	fi
	@echo "🥚 Setting up virtual environment..."
	$(PYTHON) -m venv venv
	@echo "🥚 Activating venv and installing dependencies..."
	. venv/bin/activate && pip install -r requirements.txt
	@sudo cp crackAhash.py $(DESTDIR)/$(TARGET)
	@sudo chmod +x $(DESTDIR)/$(TARGET)
	@echo "✅ crackAhash installed successfully! Run it anywhere with '$(TARGET)'"

uninstall:
	@sudo rm -f $(DESTDIR)/$(TARGET)
	@echo "🥚 crackAhash has been removed... kitchen closed!"

