# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['libs/forge.py', 'libs/Launcher.py', 'libs/check_libs.py', 'libs/clean.py', 'libs/utils.py', 'libs/FileUtils.py', 'libs/selection.py', 'libs/download.py', 'main.py'],
             pathex=['/home/ctozer/Desktop/Development/Python/mcpy/cli'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='forge.exec',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='forge')
