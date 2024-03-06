# Tiktok ライブデータの自動取得

1. このフォルダ直下に.env ファイルを作成しそこに Tiktok でログインするのに必要なメールアドレスとパスワードを記入

- USER*EMAIL=*ログインに必要なメルア\_
- PASS=_ログインに必要なパスワード_

2. live-sc.py で import しているライブラリを全てインストール

- 参考：https://gammasoft.jp/python/python-library-install/

3. Chrome のタブを全て閉じ、その状態で login.py を"python3 login.py"で行い、途中手動でログインする過程があるので 30 秒以内に行う
4. ログイン状態になったので、もう一度 Chrome が全て閉じていることを確認し、live-sc.py を"python3 live-sc.py"で実行
5. data フォルダ内に*tiktok-live-data.csv*としてデータが保存される

参考:https://prtn-life.com/blog/selenium-chrome-login
