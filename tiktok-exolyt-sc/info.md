# TikTok ハッシュタグ データ取得手順

1. Tiktok 分析ツール Exolyt を新規登録(登録してない人のみ)

- URL: https://exolyt.com/ja

2. このフォルダ直下に.env ファイルを作成しそこに Exolyt でログインするのに必要なメールアドレスとパスワードを記入

- USER*EMAIL=*ログインに必要なメルア\_
- PASS=_ログインに必要なパスワード_

3. live-sc.py で import しているライブラリを全てインストール

- 参考：https://gammasoft.jp/python/python-library-install/

4. Chrome のタブを全て閉じ、その状態で login.py を"python3 login.py"で行い、閉じるまで待つ

5. ログイン状態になったので、もう一度 Chrome が全て閉じていることを確認し、live-sc.py を"python3 live-sc.py"で実行

6. 上の CMD を打ったあと、CMD を打ったターミナルに*「流行を調べたいハッシュタグを複数記入してください(間は半角空白で区切る)」*という文字が出てくるので、調査したいハッシュタグを間を半角空白にしながら複数記入していく

- 記入例：ボクシング 剣道 日本 免許

7. data フォルダに csv データが作成される

参考:https://prtn-life.com/blog/selenium-chrome-login

## 注意!!!：

### Chrome のバージョン が更新されるたびに、以下のエラーが出る

selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 120
Current browser version is 122.0.6261.94

- その場合手動で chromedriver を入れ直す必要あり(上のエラーの場合、Chrome ver122 に対応する chrome driver を入れる必要あり)
- また初回起動時は該当 chromedrive を許可しないといけない(参考 2 を拝見)

参考：https://yuki.world/python-chrome-driver-version-error/
参考 2：https://qiita.com/kurokoya/items/ac9951da61fa4fff3dde
