#!/usr/bin/env python3

#KIVY Installer

import pip,os

pip.main(['install', 'setuptools', 'virtualenv'])
os.system('python3 -m virtualenv ~/kivy_env')
os.system('~/kivy_venv/bin/activiate')
pip.main(['install', 'kivy', 'kivy_examples', 'ffpyplayer'])