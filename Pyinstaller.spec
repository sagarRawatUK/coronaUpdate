# -*- mode: python -*-

block_cipher = None


a = Analysis(['State_wise_data.py'],
             pathex=['C:\\Users\\shree ju\\Documents\\Python\\Corona Update'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('icon.png','C:\\Users\\shree ju\\Documents\\Python\\Corona Update\\icon.png', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='State_wise_data',
          debug=False,
          strip=False,
          upx=True,
          console=False)