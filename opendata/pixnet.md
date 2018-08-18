# PIXNET 熱門文章集


### 基本資訊

項目           | 值
---------------|-------
資料筆數        | 208,743 筆
資料格式        | jsonline
壓縮檔大小      | 1.2 G
檔案實際大小     | 5.8 G
下載連結        | [這裡](https://drive.google.com/open?id=1nRqyFQkg2fGyqv3PZgc3ocmSGmXUvAAe) (1.2 G)
樣本資料(100筆) | [這裡](https://drive.google.com/file/d/1DqQzfIb8u7SybvhK8izZ3NUgb07EBsFL/view) (3 M)

### 資料範例
```json
{
  "url": "http://phina66.pixnet.net/blog/post/55377582",
  "site_category": "美味食記",
  "custom_category": "美式餐廳",
  "title": "(3)台北中山區。GAUCHO(高卓人)~阿根廷炭烤餐廳，大口吃肉吃到怕!",
  "tags": [
    "烤肉",
    "majimaji",
  ],
  "body": "<table id=\"table1\" style=\"margin: 0 ...略... </small>&nbsp;</p>",
  "comments": [
    {
      "body": "阿根廷主厨有工作證嗎？",
      "reply": "我不會西班牙語沒跟他聊到天耶~~~~還是下次我換工作到徵信社時幫你查一下(其實當記者也可以歐??)"
    }
  ],
  "images": [
    "http://pic.pimg.tw/phina66/1388908473-3616148299_l.jpg",
    "http://pic.pimg.tw/phina66/1388908582-2565883661_l.jpg",
    "http://pic.pimg.tw/phina66/1389535107-1865653827.jpg?v=1389535242"
  ],
  "keywords": [
    "阿根廷烤肉台北"
  ]
}

```

### 欄位說明
欄位名稱        |說明                                 |資料型態
---------------|------------------------------------|---------
url            |該文章原始連結                        |String
site_category  |文章作者選取的 PIXNET定義之文章分類，其值為 國內旅遊, 國外旅遊, 食譜分享, 美味食記, 美食情報, 美容彩妝, 時尚流行 之一。        |String
custom_category|使用者自行定義的文章分類                |String
title          |文章標題                             |String
tags           |使用者定義的所有標籤                   |List[String]
body           |文章原始 `html` 格式內文              |String
comments       |文章的回覆討論串，詳見 Comment 說明     |List[Comment]
images         |文章中出現的所有圖片連結                |List[String]
keywords       |與文章關聯的 google 搜尋關鍵字 (已抽樣) |List[String]

### Comment 欄位說明
欄位名稱        |說明                                 |資料型態
---------------|------------------------------------|---------
body           |一般使用者對該篇文章的留言              |String
reply          |文章作者對留言的回答(可能為空值: `null`) |String


## 資料使用授權
若您下載下方連結所提供的資料集 (Dataset)，表示您同意以下的資料使用授權：

您可以：

* 自由應用提供的資料集，產生新的程式、文件、圖表等著作。
* 自由修改提供的資料集，產生衍生的資料集。

您必須：

* 在您的著作或衍生資料集明確標示資料來源與此份說明文件的連結。

您不可以：

* 使用可能混淆或困擾的商標或名稱。
* 造成痞客邦會員產生違反痞客邦會員條款之行為。
* 違反中華民國法令或造成第三人發生違反中華民國法令的行為。
* 另為提供他人資料集下載。亦即，您不可以複製一份資料集到您自己的網路服務上供他人下載，但您可以提供他人此份說明文件的連結。
* 如您利用提供的資料集，開發任何妨礙善良風俗之違法服務或程式工具，PIXNET 並不為此負任何法律連帶責任。
