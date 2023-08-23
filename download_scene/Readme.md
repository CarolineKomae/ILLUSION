# About this tool - このツールについて
ILLUSION様のコイカツサンシャインの公式アップローダーにアップされているシーンデータをダウンロードするツールです。<br>
http://upks.illusion.jp/list/scene

## File viewer - ファイルビューア (2023/08/23 追加)
ダウンロードしたSDをブラウザで表示するための簡易ツールです。sceneフォルダがある場所に配置して、以下のhtmlファイルをブラウザで表示して下さい。<br>
一度にすべてのSDを表示させるため、メモリをかなり消費（5GB程度）するので注意して下さい。
* scene_info_kks.html
* scene_info_kks_org.html (オリジナルのファイル名で取得した人用 - sceneフォルダ直下に取得したSDを入れて下さい)

# How to use - 使い方
* download_scene.py をダウンロードする。
* pythonをインストールする https://www.python.org/downloads/
* コマンドプロンプトを開き、pipコマンドで必要なライブラリをinstallする。
  ```python
  pip install beautifulsoup4
  pip install requests
  ```
* コマンドプロンプトから download_scene.py のあるフォルダに移動し、download_scene.py を実行する。
  ```python
  cd フォルダ名
  python download_scene.py
  ```
* ダウンロードが開始されるので、終了まで待つ (1時間程度、約4.3 GBあるのでディスク残量には注意)
* 「シーンのダウンロードが全て完了しました。」が出たら完了。
* 取得したシーンは scene\作者名\タイトル.png の名前で保存される。

## How to resume from the middle of the process - 途中から再開したい場合
* download_scene.py の 16行目にある "start=1" の番号を変更し、download_scene.py を再実行する。
* 指定したページ番号から取得が開始される。

# Notes - 注意事項
* このツールはWindows環境での動作を前提としています。
* このツールは個人で作成したものであり、全ての環境での動作は保証しておりません。
* このツールを使用した場合に発生した損害等の補償は致しかねます。
