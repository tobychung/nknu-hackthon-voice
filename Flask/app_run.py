from flask import *
import json
import requests
from bs4 import BeautifulSoup
import pandas

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    result = req.get("result")
    parameters = result.get("parameters")

    if req.get("result").get("action") == "askweather":
        speech = weather()
    elif req.get("result").get("action") == "guide":
        zone = str(parameters.get("guide"))
        speech = getWiki(zone)
    elif req.get("result").get("action") == "bike":
        zone = str(parameters.get("bike"))
        speech = bike_stop(zone)
    else:
        return {}

    print("Response:")
    print(speech)
    # 回傳
    return {
        "speech": speech,
        "displayText": speech,
        # "data": {},
        # "contextOut": [],
        "source": "agent"
    }

def getWiki(location):
    try:
        res = requests.get('https://zh.wikipedia.org/wiki/{}'.format(location))
        soup = BeautifulSoup(res.text)
        article = soup.select_one('.mw-parser-output p').text
        return str(article)
    except AttributeError:
        print ("維基百科無'{}'這個詞彙".format(term))

def weather():
    try:
        df = pandas.read_html('https://www.cwb.gov.tw/V7/observe/24real/Data/46692.htm')
        df2 = str(df[0][1][1])
        return "現在溫度為"+df2+"度"
    except AttributeError:
        print ("抱歉氣象局資料異常")

def bike_stop(bike_stop):
    url = "http://data.taipei/youbike"
    data = requests.get(url).json()

    sno = []
    tot = []
    sbi = []
    bemp = []
    act = []
    lat = []
    lng = []
    sna = []
    act = []

    for key, value in data["retVal"].items():
        sno.append(value["sno"])  # 站點代號
        tot.append(int(value["tot"]))  # 總停車格
        sbi.append(int(value["sbi"]))  # 目前停放車輛數
        bemp.append(int(value["bemp"]))  # 空位數量
        act.append(value["act"])  # 全站禁用數量
        lat.append(float(value["lat"]))  # 緯度
        lng.append(float(value["lng"]))  # 經度
        sna.append(value["sna"])  # 站名
        act.append(int(value["act"]))
    x=1
    while (str(sna[x])!=bike_stop):
        x+=1
    return ("目前空位數"+str(bemp[x])+"個")

if __name__ == '__main__':
    app.run(debug=True)
