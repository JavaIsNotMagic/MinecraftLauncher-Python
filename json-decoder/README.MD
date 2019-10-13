Folder Structure

json-decoder - ROOT
|-> cli - Command Line Version
|-> cli/downloads - Data directory for the cli version
|-> cli/libs - Modules that we wrote for the cli version
|-> cli/testing - Modules that are being worked on / code that isn't ready to go
|-> gui - Graphical User Interface
|-> gui/libs - Modules that I wrote for the GUI
|-> gui/libs/cli - Modules that we wrote for the CLI that I am using again to make life easy
|-> gui/data - All of the files that are used by the GUI go here. Sorted by type
|-> gui/data/unec - Raw data, unencrypted
|-> gui/data/unec/nacl - NaCl data that isn't encrypted
|-> gui/data/1 - User store, this is encrypted
|-> gui/testing - Modules that I'm working on for the GUI, mostly aren't ready for production use
|-> release - All the files here will be used to make the apllication files
