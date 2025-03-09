#!/bin/bash

# 設置變數
APP_NAME="SRT Translator"
DMG_NAME="SRT_Translator"
VERSION="1.0"

# 創建臨時目錄
TMP_DIR="tmp_dmg"
rm -rf "$TMP_DIR"
mkdir "$TMP_DIR"

# 複製應用程式到臨時目錄
cp -r dist/srt_translator "$TMP_DIR/$APP_NAME.app"

# 創建 Applications 軟連結
ln -s /Applications "$TMP_DIR/Applications"

# 創建 DMG
rm -f "$DMG_NAME-$VERSION.dmg"
hdiutil create -volname "$APP_NAME" -srcfolder "$TMP_DIR" -ov -format UDZO "$DMG_NAME-$VERSION.dmg"

# 清理臨時文件
rm -rf "$TMP_DIR"

echo "DMG 文件已創建: $DMG_NAME-$VERSION.dmg" 