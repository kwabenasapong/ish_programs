# Makefile for ping pong game

# The name of the game
GAME = ping_pong

# The main file for the game
MAIN = $(GAME).py

# The dependencies for the game
DEPS = pygame

# The default target
all: install run

# Install the dependencies
install:
	pip3 install $(DEPS)

# Run the game
run:
	python3 $(MAIN)

# Clean up
clean:
	rm -f *.pyc
	rm -f *.pyo
	rm -f *~
