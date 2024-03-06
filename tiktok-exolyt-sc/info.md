TikTok ハッシュタグ データ取得手順
①Chrome のタブを全て閉じ、その状態で login.py を"python3 login.py"で行い、途中手動でログインする過程があるので 30 秒以内に行う
② ログイン状態になったので、もう一度 Chrome が全て閉じていることを確認し、live-sc.py を"python3 live-sc.py"で実行

参考:https://prtn-life.com/blog/selenium-chrome-login

注意!!!：
Chrome drive の ver が更新されるたびに、以下のエラーが出る
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 120
Current browser version is 122.0.6261.94

その場合手動で chromedriver を入れ直す必要あり(上のエラーの場合、Chrome ver122 に対応する chrome driver を入れる必要あり)
また初回起動時は該当 chromedrive を許可しないといけない(参考 2 を拝見)
参考：https://yuki.world/python-chrome-driver-version-error/
参考 2：https://qiita.com/kurokoya/items/ac9951da61fa4fff3dde
