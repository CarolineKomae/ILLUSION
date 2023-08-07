#
# ROOMガール シーンデータ一括ダウンロードツール
# 取得したシーンは scene\作者名\タイトル.png の名前で保存されます。
# 実行方法: python download_scene_roomgirl.py
#
import os
import re
import time
import requests
import string
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    # シーン投稿ページのHTMLファイルを読み込んでシーン取得
    # シーンが追加された場合は、別途以下のHTMLファイルの編集が必要
    file_path = 'roomgirl_scene.html'
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read()
    
    # HTMLデータを解析
    soup = BeautifulSoup(content, 'html.parser')

    # Scene_scene__W5yGuを含むすべてのdiv要素を取得
    items = soup.find_all('div', class_='Scene_scene__W5yGu')

    # 1シーンずつダウンロード
    if items:
        for i, item in enumerate(items):
            download_scene(item)
            time.sleep(0.2)  # サーバに負荷をかけ過ぎないよう、スリープ処理を入れる
    
    print('シーンのダウンロードが全て完了しました。')

# Windowsでファイル名に使用できない文字を全角に置き換え
def replace_invalid_chars_with_fullwidth(text):

    # 改行をスペースに変換
    text = text.replace('\n', ' ')

    invalid_chars = {
        ord('<'): '＜',
        ord('>'): '＞',
        ord(':'): '：',
        ord('"'): '”',
        ord('/'): '／',
        ord('\\'): '＼',
        ord('|'): '｜',
        ord('?'): '？',
        ord('*'): '＊'
    }
    
    return text.translate(invalid_chars)

# タイトルが空だった場合に無題を返す
def get_title_or_default(title):
    if title.strip():
        return title
    else:
        return '無題'

# 複数のスペースを１つのスペースに変換
def replace_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text)

# ファイルをダウンロードし、指定したパスに保存
def download_file(file_url, file_path):
    response = requests.get(file_url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

# ファイルのアクセス時刻と変更時刻を設定
def set_file_time(file_path, file_time):
    file_timestamp = file_time.timestamp()
    os.utime(file_path, (file_timestamp, file_timestamp))

# シーンデータをダウンロードする
def download_scene(item):

    # ダウンロードリンクのURLを取得
    download_link = item.find('div', class_='Scene_image__lPyqk').find('a')
    file_url = download_link['href']
    
    # タイトルを取得(ファイル名として使用)
    scene_name = item.find('div', class_='Scene_title__5ZcFi')
    file_name = scene_name.get_text().strip()
    file_name = replace_invalid_chars_with_fullwidth(file_name)
    file_name = replace_multiple_spaces(file_name)
    file_name = get_title_or_default(file_name) + '.png'
    
    # 作者名を取得（フォルダ名として使用）
    handle_name = item.find('div', class_='Scene_author__YEGPR').find('div', class_='Scene_text__nEs3g')
    folder_name = handle_name.get_text().strip()
    folder_name = replace_invalid_chars_with_fullwidth(folder_name)
    folder_name = os.path.join('scene', folder_name)
    
    # フォルダが無い場合に作成する
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # 投稿時刻を取得（ファイルの時刻として設定）
    scene_time = item.find('div', class_='Scene_created__Ngr_V')['title']
    file_time = datetime.strptime(scene_time.strip(), '%Y/%m/%d - %H:%M:%S')
    
    # ファイルをダウンロードして保存
    file_path = os.path.join(folder_name, file_name)
    download_file(file_url, file_path)
    set_file_time(file_path, file_time)
    print("ファイルがダウンロードされ、保存されました。" + file_path)

if __name__ == "__main__":
    main()
