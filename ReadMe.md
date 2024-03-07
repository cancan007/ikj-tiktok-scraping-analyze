# IKJ tiktok アナライザー

### 主な機能

- IKJ アカウントの Tiktok ライブデータの自動取得(tiktok-scraping フォルダ)と相関図の作成(tiktok-analyze フォルダ)
- Tiktok 分析サイト exolyt から　ハッシュタグごとの流行度データ取得(tiktok-exolyt-sc フォルダ)

各機能の使い方は各フォルダ直下の _info.md_ ファイルを拝見

### はじめ方(環境構築)

1. Python のインストール

- windows の場合
- 参考：https://prog-8.com/docs/python-env-win
- mac の場合
- 参考：https://prog-8.com/docs/python-env

2. ChromDriver をこのフォルダ直下に入れる

- この URL から自分の PC にあった ChromeDriver を入れる
- https://chromedriver.chromium.org/downloads

3. 各機能ごとの使い方は各フォルダの _info.md_ を参照(_それぞれの機能は各フォルダ直下で行う_)

- Tiktok ライブデータの自動取得
- フォルダ：tiktok-scraping
- Tiktok ライブデータの相関図作成
- フォルダ：tiktok-analyze
- 調査したいハッシュタグごとの流行度データ取得(事前に tiktok-analyze でデータ取得する必要あり)
- フォルダ：tiktok-exolyt-sc
