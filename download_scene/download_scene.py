#
# コイカツサンシャイン シーンデータ一括ダウンロードツール
# 取得したシーンは scene\作者名\タイトル.png の名前で保存されます。
# 実行方法: python download_scene.py
#
import os
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    # 投稿順の古い順からページ単位でファイルを取得する
    # ページ番号の終わりと始まりを指定
    # 2023/07/29 時点でのsceneのページ数はMAX 286 (1ページあたりの表示を12シーンとした場合)
    start=1
    stop=286
    
    # ダウンロード開始
    for i in range(start, stop + 1):
        download_scene_by_number(i)
    
    print('シーンのダウンロードが全て完了しました。')

# Windowsでファイル名に使用できない文字を全角に置き換え
def replace_invalid_chars_with_fullwidth(text):
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

# サイトからHTMLソースを取得
def get_source(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"HTMLソースの取得に失敗しました: {e}")
        return

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
    download_link = item.find('a', class_='download-link')
    file_url = "http://upks.illusion.jp/list/scene" + download_link['href']
    
    # タイトルを取得(ファイル名として使用)
    scene_name = item.find('div', class_='card-scene__name')
    file_name = scene_name.get_text().strip()
    file_name = replace_invalid_chars_with_fullwidth(file_name)
    file_name = file_name + '.png'
    
    # 作者名を取得（フォルダ名として使用）
    handle_name = item.find('a', class_='card-scene__handle-name')
    folder_name = handle_name.get_text().strip().replace('by ', '')
    folder_name = replace_invalid_chars_with_fullwidth(folder_name)
    folder_name = os.path.join('scene', folder_name)
    
    # フォルダが無い場合に作成する
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # 投稿時刻を取得（ファイルの時刻として設定）
    scene_time = item.find('div', class_='card-scene__time')
    file_time = datetime.strptime(scene_time.get_text().strip(), '%Y/%m/%d - %H:%M')
    
    # ファイルをダウンロードして保存
    file_path = os.path.join(folder_name, file_name)
    download_file(file_url, file_path)
    set_file_time(file_path, file_time)
    print("ファイルがダウンロードされ、保存されました。" + file_path)

# ページ番号を指定してシーンデータダウンロード
def download_scene_by_number(num):
    print(f'{num}ページ目を取得中')
    
    url = f'http://upks.illusion.jp/list/scene?&page={num}&order_by=createtime%2Casc'
    
    # ページのソースを取得
    html_source = get_source(url)
    soup = BeautifulSoup(html_source, 'html.parser')
    
    # uploader__card-sceneを含むすべてのdiv要素を取得
    items = soup.find_all('div', class_='uploader__card-scene')
    
    # 1シーンずつダウンロード
    if items:
        for i, item in enumerate(items):
            download_scene(item)
            time.sleep(0.2)  # サーバに負荷をかけ過ぎないよう、スリープ処理を入れる
    
    print(f'{num}ページ目を取得完了')

if __name__ == "__main__":
    main()
