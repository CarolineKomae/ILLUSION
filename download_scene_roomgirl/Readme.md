# About this tool - このツールについて
ILLUSION様のROOMガールの公式アップローダーにアップされているシーンデータをダウンロードするツールです。<br>
2023/08/07 23:24 時点でアップロードされているシーンを全てダウンロードします。<br>
http://uproom.illusion.jp/scenes

# How to use - 使い方
* download_scene_roomgirl.py, roomgirl_scene.html の2ファイルをダウンロードする。
* pythonをインストールする https://www.python.org/downloads/ ※ 既にインストール済の方は不要です。
* コマンドプロンプトを開き、pipコマンドで必要なライブラリをinstallする。 ※ 既にインストール済の方は不要です。
  ```python
  pip install beautifulsoup4
  pip install requests
  ```
* コマンドプロンプトから download_scene_roomgirl.py のあるフォルダに移動し、download_scene_roomgirl.py を実行する。
  ```python
  cd フォルダ名
  python download_scene_roomgirl.py
  ```
* ダウンロードが開始されるので、終了まで待つ (20分程度、約1.2 GB)
* 「シーンのダウンロードが全て完了しました。」が出たら完了。
* 取得したシーンは scene\作者名\タイトル.png の名前で保存される。

# Notes - 注意事項
* このツールはWindows環境での動作を前提としています。
* このツールは個人で作成したものであり、全ての環境での動作は保証しておりません。
* このツールを使用した場合に発生した損害等の補償は致しかねます。
