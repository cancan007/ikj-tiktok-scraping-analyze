# IKJ tiktok アナライザー

### 主な機能

- IKJ アカウントの Tiktok ライブデータの自動取得(tiktok-scraping フォルダ)と相関図の作成(tiktok-analyze フォルダ)
- Tiktok 分析サイト exolyt から　ハッシュタグごとの流行度データ取得(tiktok-exolyt-sc フォルダ)

各機能の使い方は各 info.md ファイルを拝見

### はじめ方(環境構築)

1. Python のインストール

- windows の場合
- 参考：https://prog-8.com/docs/python-env-win
- mac の場合
- 参考：https://prog-8.com/docs/python-env

2. ChromDriver をこのフォルダ直下に入れる

- この URL から自分の PC にあった ChromeDriver を入れる
- https://chromedriver.chromium.org/downloads

3. 各機能ごとの使い方は各フォルダの info.md を参照

- Tiktok ライブデータの自動取得
- フォルダ：tiktok-scraping
- Tiktok ライブデータの相関図作成
- フォルダ：tiktok-analyze
- 調査したいハッシュタグごとの流行度データ取得
- フォルダ：tiktok-exolyt-sc
