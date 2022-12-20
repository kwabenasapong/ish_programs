# Makefile for the chat application

# This Makefile includes targets for building, installing, uninstalling, cleaning, and creating a distribution archive of the chat application. To use it, you will need to place your client and server scripts in the client and server directories, respectively, and update the CLIENT_SCRIPT and SERVER_SCRIPT variables to point to the correct scripts. You will also need to update the INSTALL_DIR variable to specify the desired install directory for the chat application, and the MAN_PAGE variable to point to the man page for the chat application.

# The name of the chat application
APP_NAME=chat

# The directories for the client and server scripts
CLIENT_DIR=client
SERVER_DIR=server

# The client and server scripts
CLIENT_SCRIPT=$(CLIENT_DIR)/chat_client.sh
SERVER_SCRIPT=$(SERVER_DIR)/chat_server.sh

# The install directory for the chat application
INSTALL_DIR=/usr/local/bin

# The man page for the chat application
MAN_PAGE=chat.1

# The target for building the chat application
build:
	# Build the chat application

# The target for installing the chat application
install: build
	# Install the chat application
	install -m 755 $(CLIENT_SCRIPT) $(INSTALL_DIR)/$(APP_NAME)
	install -m 755 $(SERVER_SCRIPT) $(INSTALL_DIR)/$(APP_NAME)-server
	install -m 644 $(MAN_PAGE) /usr/local/share/man/man1

# The target for uninstalling the chat application
uninstall:
	# Uninstall the chat application
	rm $(INSTALL_DIR)/$(APP_NAME)
	rm $(INSTALL_DIR)/$(APP_NAME)-server
	rm /usr/local/share/man/man1/$(MAN_PAGE)

# The target for cleaning the chat application
clean:
	# Clean the chat application

# The target for creating a distribution archive of the chat application
dist: clean
	# Create a distribution archive of the chat application
	tar -czvf $(APP_NAME).tar.gz $(CLIENT_DIR) $(SERVER_DIR) $(MAN_PAGE) Makefile
