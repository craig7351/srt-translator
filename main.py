import pysrt
from deep_translator import (
    MyMemoryTranslator,
    GoogleTranslator,
    LingueeTranslator,
    PonsTranslator,
    QcriTranslator
)
from tqdm import tqdm
import argparse
import os
import time
import glob
import json
import random
import requests
from dotenv import load_dotenv

# 載入 .env 文件
load_dotenv()

class DeepSeekTranslator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def translate(self, text):
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一個專業的翻譯助手。請將英文翻譯成繁體中文，保持原意的同時使翻譯更加通順自然。只需要返回翻譯結果，不需要任何解釋。"},
                {"role": "user", "content": f"請翻譯：{text}"}
            ],
            "temperature": 0.3
        }
        
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            raise Exception(f"API錯誤: {response.status_code} - {response.text}")

class TranslatorService:
    def __init__(self, source='en-US', target='zh-TW'):
        self.source = source
        self.target = target
        self._last_translate_time = 0
        self._min_interval = 1.0  # 最小間隔時間（秒）
        
    def get_translator(self, service_name):
        if service_name == "mymemory":
            return MyMemoryTranslator(source=self.source, target=self.target)
        elif service_name == "google":
            return GoogleTranslator(source='en', target='zh-TW')
        elif service_name == "linguee":
            return LingueeTranslator(source='english', target='chinese')
        elif service_name == "pons":
            return PonsTranslator(source='en', target='zh')
        elif service_name == "qcri":
            return QcriTranslator(source='en', target='zh')
        else:
            raise ValueError(f"不支持的翻譯服務: {service_name}")
            
    def wait_if_needed(self):
        """確保兩次翻譯之間有足夠的間隔"""
        now = time.time()
        elapsed = now - self._last_translate_time
        if elapsed < self._min_interval:
            time.sleep(self._min_interval - elapsed + random.uniform(0.1, 0.5))
        self._last_translate_time = time.time()

def select_translator():
    services = {
        "1": ("mymemory", "MyMemory翻譯 (繁體中文，免費，每小時1000字)"),
        "2": ("google", "Google翻譯 (繁體中文，免費，較穩定)")
    }
    
    print("\n請選擇翻譯服務：")
    for key, (_, desc) in services.items():
        print(f"{key}. {desc}")
    
    while True:
        choice = input("\n請輸入選項編號 (1-2): ").strip()
        if choice in services:
            return services[choice][0]
        print("無效的選擇，請重試")

def load_progress(progress_file):
    if os.path.exists(progress_file):
        with open(progress_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_progress(progress_file, translations):
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)

def translate_with_retry(translator_service, translator, text, max_retries=3):
    if not text or text.isspace():  # 處理空文本
        return text
        
    # 清理文本中的特殊字符
    text = text.replace('&#9472;', '-').strip()
    
    # 基礎延遲時間（秒）
    base_delay = 5
    
    for attempt in range(max_retries):
        try:
            # 確保翻譯請求之間有足夠的間隔
            translator_service.wait_if_needed()
            
            translated = translator.translate(text)
            if not translated:  # 檢查空結果
                raise Exception("翻譯結果為空")
            return translated
            
        except Exception as e:
            if attempt == max_retries - 1:  # 最後一次嘗試
                return text  # 如果所有重試都失敗，返回原文
                
            # 計算下一次重試的延遲時間
            delay = base_delay * (2 ** attempt) + random.uniform(1, 3)
            print(f"\n遇到錯誤: {str(e)}")
            print(f"等待 {delay:.1f} 秒後重試... (第 {attempt + 1} 次重試)")
            time.sleep(delay)
    
    return text  # 如果執行到這裡，返回原文

def translate_subtitle(input_file, output_file, service_name):
    # 讀取字幕文件
    subs = pysrt.open(input_file)
    # 創建翻譯服務
    translator_service = TranslatorService()
    translator = translator_service.get_translator(service_name)
    
    # 進度文件路徑
    progress_file = f"{input_file}.progress.json"
    # 載入已有的翻譯進度
    translations = load_progress(progress_file)
    
    print(f"開始翻譯字幕文件: {input_file}")
    print(f"使用翻譯服務: {service_name}")
    print(f"總共 {len(subs)} 條字幕需要翻譯")
    
    # 遍歷每一條字幕並翻譯
    for i, sub in enumerate(tqdm(subs)):
        # 檢查是否已經翻譯過
        if str(i) in translations:
            sub.text = translations[str(i)]
            continue
            
        try:
            # 翻譯文本
            translated = translate_with_retry(translator_service, translator, sub.text)
            # 更新字幕文本
            sub.text = translated
            # 保存翻譯結果
            translations[str(i)] = translated
            # 每10條保存一次進度
            if i % 10 == 0:
                save_progress(progress_file, translations)
                
        except Exception as e:
            print(f"\n翻譯出錯: {str(e)}")
            print(f"原文: {sub.text}")
            # 保存當前進度
            save_progress(progress_file, translations)
            # 保存原文
            translations[str(i)] = sub.text
            continue
    
    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # 保存翻譯後的字幕
    subs.save(output_file, encoding='utf-8')
    print(f"\n翻譯完成！已保存至: {output_file}")
    
    # 翻譯完成後刪除進度文件
    if os.path.exists(progress_file):
        os.remove(progress_file)

def process_directory(input_dir, service_name):
    # 確保輸出目錄存在
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)
    
    # 獲取所有srt文件
    srt_files = glob.glob(os.path.join(input_dir, "*.srt"))
    
    if not srt_files:
        print(f"在目錄 {input_dir} 中沒有找到任何SRT文件")
        return
    
    print(f"在目錄 {input_dir} 中找到 {len(srt_files)} 個SRT文件")
    
    # 處理每個文件
    for srt_file in srt_files:
        # 獲取文件名
        file_name = os.path.basename(srt_file)
        # 構建輸出文件路徑
        output_file = os.path.join(output_dir, file_name)
        # 翻譯文件
        translate_subtitle(srt_file, output_file, service_name)

def main():
    parser = argparse.ArgumentParser(description='將英文SRT字幕翻譯成中文')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('input', nargs='?', help='輸入的SRT文件路徑')
    group.add_argument('-f', '--folder', help='包含SRT文件的目錄路徑')
    parser.add_argument('-o', '--output', help='輸出的SRT文件路徑（可選，僅在處理單個文件時有效）')
    
    args = parser.parse_args()
    
    # 選擇翻譯服務
    service_name = select_translator()
    
    if args.folder:
        # 處理整個目錄
        process_directory(args.folder, service_name)
    else:
        # 處理單個文件
        if not args.output:
            file_name, file_ext = os.path.splitext(args.input)
            args.output = f"{file_name}_zh{file_ext}"
        translate_subtitle(args.input, args.output, service_name)

if __name__ == '__main__':
    main() 