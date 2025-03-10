# SRT 字幕翻譯工具 | SRT Subtitle Translator

> 這個專案是使用 Cursor AI 輔助開發的開源工具。
> This project is an open-source tool developed with the assistance of Cursor AI.

[English](#english) | [中文](#中文)

# 中文

這是一個將英文 SRT 字幕檔翻譯成中文的工具。支援批次處理多個字幕檔，並提供多種翻譯服務選擇。

## macOS 用戶使用方法

### 方法一：直接使用（無需安裝 Python）

1. 前往 [Releases](https://github.com/craig7351/srt-translator/releases) 頁面
2. 下載最新版本的 `SRT_Translator-1.0.dmg` 檔案
3. 雙擊打開 DMG 檔案
4. 將 `SRT Translator` 拖曳到 Applications 資料夾
5. 從 Applications 資料夾開啟程式
   - 首次開啟時可能會出現安全性警告，需要在「系統偏好設定」→「安全性與隱私」中允許執行

### 使用方式

#### 命令列介面
打開終端機（Terminal），執行：
```bash
# 翻譯單個檔案
/Applications/SRT\ Translator.app/Contents/MacOS/srt_translator input.srt

# 翻譯整個資料夾中的所有 .srt 檔案
/Applications/SRT\ Translator.app/Contents/MacOS/srt_translator -f ./字幕資料夾
```

## Windows 用戶使用方法

### 使用方法

1. 前往 [Releases](https://github.com/craig7351/srt-translator/releases) 頁面
2. 下載最新版本的 `SRT_Translator-1.0.exe` 檔案
3. 將下載的檔案放在您選擇的資料夾中
4. 打開命令提示符（CMD）或 PowerShell
5. 導航到包含 `SRT_Translator-1.0.exe` 的資料夾。例如：

   ```bash
   cd C:\path\to\your\directory
   ```

6. 執行可執行文件，使用以下命令格式：

   ```bash
   SRT_Translator-1.0.exe <input_file.srt> <output_file.srt>
   ```

   - `<input_file.srt>`: 要翻譯的輸入 SRT 檔案。
   - `<output_file.srt>`: 翻譯後生成的輸出 SRT 檔案。

### 翻譯整個資料夾

如果您想要翻譯整個資料夾中的所有 SRT 檔案，可以使用 `-f` 參數。以下是具體步驟：

1. 確保您的資料夾中只包含需要翻譯的 `.srt` 檔案。
2. 使用以下命令格式執行：

   ```bash
   SRT_Translator-1.0.exe -f <folder_path>
   ```

   - `<folder_path>`: 包含要翻譯的 SRT 檔案的資料夾路徑。

### 翻譯完成後的檔案位置

翻譯完成後，所有生成的 SRT 檔案將自動保存在當前目錄的 `result` 資料夾中。

### 示例

```bash
# 翻譯單個檔案
SRT_Translator-1.0.exe example.srt translated_example.srt

# 翻譯整個資料夾
SRT_Translator-1.0.exe -f C:\path\to\your\subtitles_folder
```

## Python 用戶使用方法

如果您已安裝 Python，可以直接使用原始碼執行：

### 1. 安裝必要套件
```bash
# 下載專案
git clone https://github.com/craig7351/srt-translator.git
cd srt-translator

# 安裝依賴
pip install -r requirements.txt
```

### 2. 執行程式
```bash
# 翻譯單個檔案
python main.py input.srt

# 翻譯整個資料夾
python main.py -f ./字幕資料夾
```

## 功能特點

- 支援批次處理多個字幕檔
- 自動保存翻譯進度，意外中斷可續翻
- 多種翻譯服務可選：
  - MyMemory（免費，每小時 1000 字）
  - Google 翻譯（免費，較穩定）
- 智能錯誤處理和重試機制
- 翻譯結果自動保存為新檔案

## 使用提示

1. 翻譯後的檔案會自動保存在 `result` 資料夾中
2. 程式會自動處理特殊字元和格式
3. 如果翻譯中斷，重新執行即可從上次進度繼續
4. 建議先用小檔案測試再處理大量字幕

## 常見問題

Q: 為什麼第一次執行時會被系統阻擋？  
A: 這是 macOS 的安全機制，需要在「系統偏好設定」→「安全性與隱私」中允許執行。

Q: 翻譯速度似乎很慢？  
A: 為了避免被翻譯服務封鎖，程式設有間隔時間限制。建議使用 Google 翻譯服務，相對較快且穩定。

# English

This is a tool for translating English SRT subtitle files to Chinese. It supports batch processing of multiple subtitle files and offers various translation services.

## macOS User Guide

### Method 1: Direct Use (No Python Required)

1. Go to the [Releases](https://github.com/craig7351/srt-translator/releases) page
2. Download the latest `SRT_Translator-1.0.dmg` file
3. Double-click to open the DMG file
4. Drag `SRT Translator` to the Applications folder
5. Launch from the Applications folder
   - First-time launch may require approval in "System Preferences" → "Security & Privacy"

### Usage

#### Command Line Interface
Open Terminal and run:
```bash
# Translate a single file
/Applications/SRT\ Translator.app/Contents/MacOS/srt_translator input.srt

# Translate all .srt files in a directory
/Applications/SRT\ Translator.app/Contents/MacOS/srt_translator -f ./subtitles_folder
```

## Windows User Guide

### Usage

1. Go to the [Releases](https://github.com/craig7351/srt-translator/releases) page
2. Download the latest `SRT_Translator-1.0.exe` file
3. Place the downloaded file in your chosen directory
4. Open Command Prompt (CMD) or PowerShell
5. Navigate to the directory containing `SRT_Translator-1.0.exe`. For example:

   ```bash
   cd C:\path\to\your\directory
   ```

6. Run the executable using the following command format:

   ```bash
   SRT_Translator-1.0.exe <input_file.srt> <output_file.srt>
   ```

   - `<input_file.srt>`: The input SRT file to be translated.
   - `<output_file.srt>`: The output SRT file generated after translation.

### Translating an Entire Folder

If you want to translate all SRT files in a folder, you can use the `-f` parameter. Here are the steps:

1. Ensure that your folder contains only the `.srt` files you want to translate.
2. Run the following command format:

   ```bash
   SRT_Translator-1.0.exe -f <folder_path>
   ```

   - `<folder_path>`: The path to the folder containing the SRT files.

### Output Location

After the translation is complete, all generated SRT files will be automatically saved in the `result` folder within the current directory.

### Example

```bash
# Translate a single file
SRT_Translator-1.0.exe example.srt translated_example.srt

# Translate an entire folder
SRT_Translator-1.0.exe -f C:\path\to\your\subtitles_folder
```

## Python User Guide

If you have Python installed, you can run from source:

### 1. Install Required Packages
```bash
# Clone the project
git clone https://github.com/craig7351/srt-translator.git
cd srt-translator

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Program
```bash
# Translate a single file
python main.py input.srt

# Translate a directory
python main.py -f ./subtitles_folder
```

## Features

- Batch processing of multiple subtitle files
- Auto-save translation progress, resume from interruption
- Multiple translation services:
  - MyMemory (Free, 1000 words per hour)
  - Google Translate (Free, more stable)
- Smart error handling and retry mechanism
- Automatic saving of translation results

## Usage Tips

1. Translated files are saved in the `result` folder
2. Special characters and formatting are handled automatically
3. If interrupted, resume from the last progress point
4. Test with small files before processing large batches

## FAQ

Q: Why is the app blocked on first launch?  
A: This is a macOS security feature. Approve the app in "System Preferences" → "Security & Privacy".

Q: Why is the translation slow?  
A: To avoid service blocks, there are rate limits. Google Translate is recommended for better speed and stability.

## Issue Reporting

If you encounter any issues, please report them on the [Issues](https://github.com/craig7351/srt-translator/issues) page. 