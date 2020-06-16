# -*- mode: python -*-

import sys
sys.setrecursionlimit(5000)

import os

block_cipher = None


a = Analysis(['Hausdorff95'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[],
             hiddenimports=['numpy.core._dtype_ctypes', 'nibabel'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Hausdorff95',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )