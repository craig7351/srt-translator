# -*- mode: python ; coding: utf-8 -*-
from os.path import exists

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pysrt', 'deep_translator', 'tqdm', 'chardet', 'certifi', 'charset_normalizer', 'idna', 'urllib3'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='srt_translator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name='SRT Translator.app',
    icon=None,
    bundle_identifier='com.srt.translator',
    info_plist={
        'CFBundleName': 'SRT Translator',
        'CFBundleDisplayName': 'SRT Translator',
        'CFBundleExecutable': 'srt_translator',
        'CFBundlePackageType': 'APPL',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
    },
) 