# 痞客神廚鬥味場開放 API 說明 (持續調整中)

## 題目取得

* Method: GET
* EndPoint: /api/question
* request params
    * question_id: (int) 題號, default: newest
    * img_header: (bool) 是否顯示圖片 header 資訊 1-不顯示, 0-顯示, default: 0
* return value
    * question_id: 題號
    * desc: 題目敘述
    * image(base64): 純 base64
    * bounding_area: 圖片挖空的區塊會在哪邊，包含四個點座標
    * expire_at: 何時截止取得題目
* sample request

    ```
    curl -X GET "https://pixnethackathon2018-competition.events.pixnet.net/api/question?question_id=1"
    ```
* sample respose

    ```
    {
       "error":false,
       "status":200,
       "data":{
          "question_id":1,
          "desc":"今天想吃中式的早餐。煎得酥酥的餅皮加上滑順的蛋汁，最後林上甜甜鹹鹹的醬油，就決定這樣的早餐當作今天的開始了！",
          "image":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAEAAElEQVR4nET9SbMkW5IeiH2f6jlm5u53ihvTm1++HF5mZWGqQjXYEKLRh...(後略)",
          "bounding_area": {
             "x": 160,
             "y": 120,
             "w": 80,
             "h": 40
          },
          "expire_at":60
       }
    }
    ```

* example


## 答題

* Method: POST
* EndPoint: /api/answer
* request params
    * question_id: (int) 題號
    * key: (string) 各組認證 key
    * image: （string）圖片 base64格式，須帶 header
* return value
    * expired_at: (int) 回答截止時間
    * remain_quota: (int) 所剩答題次數
* sample request

    ```
    curl -X POST -d '{"question_id": 1, "key": YOUR_API_KEY, "image": "data:image/png;base64,iVBORw0KCSV...(後略)"}' "https://pixnethackathon2018-competition.events.pixnet.net/api/answer"
    ```
* sample response

    ```
    {
        "error": false,
        "status": 200,
        "data": {
            "expired_at": 1600000060,
            "remain_quota": 2
        }
    }
    ```
* example

