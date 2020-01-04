#!/usr/bin/env bash

file_name=$(find -name "forge.exec")

x-terminal-emulator -e $file_name 1>&2> /dev/null
