# PIXNET AI智慧影像生成

**PIXNET** 旗下「痞客邦」網站累積了豐富的美食紀錄，包含各式各樣的影像及文字資料，早餐、午餐、晚餐外加宵夜，每一天，上千萬的使用者來這裡找尋下一餐的靈感。「影像生成」是 AI 人工智慧領域中新興的應用，機器能否擁有跟美食部落客一樣的專業和理解能力？ AI 能夠計算出好吃的牛排該長什麼樣子嗎？ 又或者麻辣火鍋裡該加什麼料呢？

**PIXNET** 首創以「AI 智慧影像生成」為題舉辦企業黑客松，第五屆 PIXNET HACKATHON 提供站上美食圖庫及文章資料，歡迎各界高手前來挑戰！

<img src="./static/example.png" width="500" align="middle">

參賽者將利用**影像檢索**與**深度學習**的相關技術，想辦法**從影像中找回遺失的食材，還原食物的美味。**


參賽者拿到的題目範例將如下所示：

```
這顆草莓瑞士捲，草莓沾著奶油吃起來香濃滑口，酸酸甜甜，搭配巧克力蛋糕，滋味絕妙。
```
<img src="./static/strawberrycake-missing.jpg" width="500" align="middle">

### 題目內容包含：

1. 一段圖片中食物的文字描述。
2. 一張局部挖空的食物圖片，並附上挖空位置的 **bounding box** 資訊(示意圖，非顯示在原始圖片中)。
3. 比賽圖片尺寸統一為 **`256 x 256`**，格式為 `BMP`。[註1](#how-to-resize)
4. 挖空 **bounding box** 最大邊長不會超過 `128`。
5. 挖空幾何形狀可為不規則，但不會超出 **bounding box** 範圍，背景顏色固定為**綠色**(色碼: `#00ff00`)。

<a name="how-to-resize"></a>
ℹ️ [註1] **題目影像前處理**: 題目的原始來源圖片會先以 `等比例` 縮放到接近(大於) `256` 的大小，再裁切出 **`256 x 256`** 的區域作為題目，實際比賽參賽者無需處理這段前處理。

### 比賽答題流程示意：

<img src="./static/battle-flow.png" width="500" align="middle">

1. 參賽者透過 API 向主辦方索取題目。
2. 參賽者設計算法預測並還原影像。
3. 參賽者將還原之影像透過 API 上傳主辦方。
詳細的比賽流程請參考[比賽方式](#how-to-battle)

### 範例實作
PIXNET 參考了 [Globally and Locally Consistent Image Completion](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/en/) 這篇論文，提供了基本的實作範例，可參考 [pixchef](../demos/pixchef/)


## 題庫


### 痞客邦美食資料集：PIXFOOD20

<img src="./static/pixfood20.png" width="500" align="middle">

**`PIXFOOD20`** 是痞客邦精選 **20+2** 個種類的美食圖庫，分類包含：

```
火鍋、牛排、咖啡、丼飯、滷肉飯、
生魚片、鬆餅、麵包、蛋糕、義大利麵、
牛肉麵、小籠包、生菜沙拉、拉麵、串燒、
壽司、漢堡、薯條、冰淇淋、手搖飲料
```

**`PIXFOOD20`** 將被切分為**訓練集**(Training set)與**測試集**(Testing set)，訓練集開放給所有參賽者下載，用來訓練深度學習的模型，**實際比賽題目將由測試集抽出**。

詳見 [**PIXFOOD20** 資料集說明](../opendata/pixfood20.md)


## 輔助資料集

### 痞客邦文章資料集：

含有原始 html 的熱門文章資料，參賽者可以透過此資料集了解圖文間的上下文關係，詳細說明請參考 [PIXNET熱門文章集說明文件](../opendata/pixnet.md)

### 外部資料集：
參賽者可以使用額外的資料集輔助模型訓練，範例如下：

* [Food-101 Dataset](https://www.vision.ee.ethz.ch/datasets_extra/food-101/)
* [UECFOOD-100 Dataset](http://foodcam.mobi/dataset100.html)


## 競賽平台: 痞客邦神廚鬥味場
* 競賽平台預計於 **`7/30`** 對外開放給參賽者測試使用，請參賽者密切注意。

* 每組通過報名審核之參賽隊伍，將在 telegram 發送一組 API Token(預計 **`7/30`** 發放)，作為接收題目與上傳答案的身份驗證，請妥善保管好自己的 API Token。



<a name="how-to-battle"></a>
### 比賽方式

#### 🥊 [HACKAHTON競賽平台](https://pixnethackathon2018-competition.events.pixnet.net/)

<img src="./static/competition-web.png" width="500" align="middle">


1. 比賽以 **回合制** 進行，無分初、決賽，一共 `10` 個回合，總計 `10` 張圖片。
2. 每一回合競賽平台會更新一組題目，並呈現在頁面上。
3. 題目由一段`文字描述`與`缺空的食物圖片`組成，圖片尺寸固定為 **`256 x 256`** [註1](#how-to-resize)，並被包裝成`JSON`格式如下：

	```
	{
            question_id: 2,
		desc: "今天想吃中式的早餐。煎得酥酥的餅皮加上滑順的蛋汁，最後林上甜甜鹹鹹的醬油，就決定這樣的早餐當作今天的開始了！",
            image_b64: "/9j/4AAQSkZJRgABAQAASABIAAD...(略)"
		bounding_area: {
			"x": 160,
			"y": 120,
			"w": 80,
			"h": 40
		}
	}
	```

* **bouding box** 符號定義:
<img src="./static/boundingbox.png" width="300" align="middle">

* API 欄位說明：
	* `question_id`: 題目編號(uuid)
	* `bounding_area`: 見上圖定義
	* `desc`: 圖片中食物的文字描述
	* `image_b64`: 圖片的 base64 編碼

* 詳細 API 說明請參考[ API 文件說明](../opendata/food.competition.api.md)

* ⚠️NOTE：目前 API 尚在開發階段，仍可能調整，請參賽者密切注意。


4. 當題目公布，參賽隊伍須 **主動** 透過平台 API，下載題目進行分析並生成完整影像。
5. 自題目公布開始，參賽隊有 **1分鐘** 的時間，將生成之影像，透過 API 傳送回競賽平台，成品將即時呈現於畫面上。
6. 所有上傳之影像，開放給現場觀眾投票，每回合觀眾將有 **3分鐘** 進行投票，詳細說請參考 [投票機制](#how-to-poll)。
7. 進行下一回合出題。


### 獎項與評分機制
本競賽將提供兩個獎項：

#### 🏆評審獎
評選標準：

* 演算法設計 40%
	* 使用何種模型架構
	* 如何處理資料 pipeline
	* 如何評估算法 performance

* 影像成果 40%
	* 生成之影像能夠產生多少細節。
	* 生成之內容符合原始圖片的場景。

* 簡報說明 20%
	* 論述應掌握重點，表達清晰，條理分明。

#### 🏆票選獎
由現場觀眾進行投票，總計最高票之隊伍獲得。

<a name="how-to-poll"></a>
投票機制：

1. 參與投票的觀眾必須在 **PIXNET** 平台註冊一組帳號，驗證通過後即可使用此帳號登入本平台。
2. 每張由參賽者產生的圖片上會有三個可點選的按鈕，👍、🤤、💩，觀眾可任意點選。
3. 平台將統計每隊所得 👍 總數，作為得獎依據，其他按鈕不予計分。

* ⚠️NOTE：此處圖示僅為示意，正確投票圖示以競賽平台顯示為準。


### API說明
請參考[ API 文件說明](../opendata/food.competition.api.md)


## 參考閱讀
* [Globally and Locally Consistent Image Completion](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/en/)
* [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/abs/1804.07723)
