# 雙北綠色運具應用開放資料

## 雙北市政府交通局
台北市與新北市交通局一同合作，提供參賽隊伍107年上半年度的大台北地區交通資料，包含公車路線定點與定時資訊、各路段每五分鐘車流量及車速相關資訊、YouBike自行車各借還站每分鐘空位數、捷運車站出入口座標及票價說明、臺灣中油各種類油品價格等，期待參賽隊伍整合旅行時間與旅運成本，設計更多元的綠色運具應用情境。

<a name="taipei"></a>

1. [⏬臺北市政府交通局開放資料集](https://drive.google.com/open?id=1Wwn4dpPABgXibmWBTZ737OoyFY6LqnpG)

項目      |內容介紹   |更新頻率    |資料時間起日    |資料時間迄日
---------|:---------|:----------|:-------------|:-------
臺北市各雨量站過去24小時時雨量資料| |每日|2018年1月1日|2018年6月15日
每日雨量-過去9年局屬地面測站每日雨量資料|中央氣象局全國地面測站每日雨量資料(日雨量統計)|每年|2018年1月1日|2018年6月15日
汽、柴油零售|臺灣中油各種類油品價格|每週|2018年1月1日|2018年6月15日
YouBike臺北市自行車即時欄位|YouBike臺北市自行車各借還站空位數|每一分鐘|2018年1月1日|2018年6月15日
YouBike臺北市自行車場站資訊|YouBike臺北市自行車各借還站座標及總車位數|每日|2018年1月1日|2018年6月15日
路段靜態資訊資料|臺北市各路段起訖點及道路等級相關資訊|不定期|2017年10月1日|2017年10月1日
路段動態資訊資料|臺北市各路段車流量及車速相關資訊|每五分鐘|2018年1月1日|2018年6月15日
大臺北地區捷運車站出入口座標||||
捷運票價說明||||
臺北捷運車站免費接駁車路線說明||||
臺北市公車票價說明|http://www.5284.com.tw/1.html


<a name="new-taipei"></a>

2. [⏬新北市政府交通局開放資料集](https://drive.google.com/open?id=17whcbw49bJzwARRxPc6bz7tKM1YFCzBM)

項目      |內容介紹   |更新頻率    |資料時間起日    |資料時間迄日
---------|:---------|:----------|:-------------|:-------
YouBike新北市自行車場站資訊|YouBike新北市自行車場站資訊|||

<a name="big-taipei-bus"></a>

3. 雙北市公車靜/動態資料集

項目|內容介紹|更新頻率|資料時間起日|資料時間迄日
---------|:---------|:----------|:-------------|:-------
[⏬北市公車靜態基本資料](https://drive.google.com/open?id=1KlATr-iCdHgCv-jGILICPAWBoVWJL_fl)|[資料說明文件](https://drive.google.com/a/pixnet.tw/file/d/1NG97Ih4U_XQ8gnkD1vUccuIVjPiDkUDN/view?usp=sharing)||2018年1月1日|2018年6月15日
雙北公車動態歷史資料|[資料格式說明](https://drive.google.com/open?id=1qGzXNQsKBcjnqmvlpi2ptybKYLsv5ytX)|每日|2018年1月1日|2018年6月15日
[⏬新北公車靜態基本資料](https://drive.google.com/open?id=1vhqPHJFGpP2QMCyc0SRnBaYkA83nmcqW)|[資料說明文件](https://drive.google.com/open?id=1f404sVnh7649NflK2BjRD_0tIXkBv6Na)||2018年1月1日|2018年6月15日

* ℹ️雙北公車動態歷史資料內容龐大(解壓前: 180G, 解壓後超過 1T)，雲端下載連結將 email 給報名錄取的參賽者
* ℹ️樣本資料: [ADPServerLog.2018-01-01.tar.xz](https://drive.google.com/open?id=1VG2Ad89XRgI_IOQeKjaZm8pHVdw3AoXd) 811MB

	解壓縮方式參考：
	```
	$ mkdir -p ADPServerLog/2018-01-01
	$ tar Jxvf ADPServerLog.2018-01-01.tar.xz -C ADPServerLog/2018-01-01
	```

	若遇到檔案亂碼問題，可嘗試以下方式處理：
	```
	$ iconv -f BIG -t UTF-8 {內容亂碼之檔案路徑} > {重新編碼之存檔路徑}
	```

## 亞旭電腦股份有限公司
臺北市政府交通局與亞旭電腦合作推動改造台北車站為智慧車站，推出「台北車站通」室內導航App，亞旭電腦並開放台北車站室內圖資API及該場域內導航功能SDK，提供有意進行加值應用之開發者介接。 開發工具中所使用到的 API token/key 會在 telegram上 發送給報名錄取的參賽者。

[⏬下載連結](https://drive.google.com/open?id=1Oy82PwNfHylHb6O0aAsSyI8pLI-Ycf7H)
