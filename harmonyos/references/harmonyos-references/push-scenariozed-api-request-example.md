---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-example
title: 请求示例
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息 > 请求示例
category: harmonyos-references
scraped_at: 2026-04-28T08:18:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccd3081effb1d6ef0e599c461ac30b40da110aa4cf6fdfc056175affeac83c88
---

## 通知消息

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:0

9. // Request Body
10. {
11. "payload": {
12. "notification": {
13. "category": "xxxxxx", // category替换为实际通知消息类型
14. "title": "普通标题",
15. "body": "普通内容",
16. "clickAction": {
17. "actionType": 0
18. },
19. "style": 0,
20. "image":"https://lf*******246.png"
21. }
22. },
23. "target": {
24. "token": ["MAAALgE4G98BAAAAst*******jg"]
25. }
26. }
```

### 应用在前台时接收通知消息

应用只在后台展示通知消息；应用在前台时，通知消息将不会展示，但可以接收通知消息后自行完成业务处理，详情请参见[应用在前台时处理通知消息](../harmonyos-guides/push-send-alert.md#应用在前台时处理通知消息)。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type: 0

9. // Request Body
10. {
11. "payload": {
12. "notification": {
13. "category": "MARKETING",
14. "title": "普通通知标题",
15. "body": "普通通知内容",
16. "clickAction": {
17. "actionType": 0
18. },
19. "foregroundShow": false  // 设置为false则应用在前台时不会展示通知消息，默认为true表示前后台都展示
20. }
21. },
22. "target": {
23. "token": ["MAMzLg**********lPW"]
24. },
25. "pushOptions": {
26. "testMessage": true,
27. "ttl": 86400
28. }
29. }
```

## 卡片刷新消息

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:1

9. // Request Body
10. {
11. "payload": {
12. "formData": {
13. "123": 96,
14. "class": "123"
15. },
16. "version": 922337203,
17. "images": [
18. {
19. "keyName": "hello",
20. "url": "https://xxx.png",
21. "require": 1
22. }
23. ],
24. "formId": 0,
25. "moduleName": "testName",
26. "formName": "testFormName",
27. "abilityName": "testAbilityName"
28. },
29. "pushOptions": {
30. "biTag": "this is bi",
31. "ttl": 666
32. },
33. "target": {
34. "token": [
35. "MAAALgE4G98BAAAAst************ttQd4Tw"
36. ]
37. }
38. }
```

## 语音播报消息

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:2

9. // Request Body
10. {
11. "payload": {
12. "extraData": "Extension extra data",
13. "notification": {
14. "category": "PLAY_VOICE",
15. "title": "普通标题",
16. "body": "普通内容",
17. "clickAction": {
18. "actionType": 0
19. },
20. "style": 0,
21. "image":"https://lf*******246.png"
22. }
23. },
24. "target": {
25. "token": ["MAAALgE4G98BAAAAst*******jg"]
26. }
27. }
```

## 后台消息

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:6

9. // Request Body
10. {
11. "payload": {
12. "extraData": "携带的数据"
13. },
14. "target": {
15. "token": ["MAAALgE4G98BAAAAst************jq"]
16. }
17. }
```

## 创建实况窗消息

### 航班场景（event为FLIGHT）

计划出发，使用左右文本模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 1,
17. "operation": 0,
18. "event": "FLIGHT",
19. "status": "DEPART", // 计划出发
20. "activityData": {
21. "notificationData": {
22. "keywords": {
23. "flightNo": "MU1471"
24. },
25. "type": 5,
26. "contentTitle": "航班{{status}}", // 航班计划出发
27. "contentText": [
28. {
29. "text": "航班号："
30. },
31. {
32. "text": "{{flightNo}}", // MU1471
33. "foregroundColor": "#FF317AF7"
34. }
35. ],
36. "clickAction": {
37. "actionType": 0
38. },
39. "firstTextBlock": {
40. "firstLine": "12:00",
41. "secondLine": "上海虹桥"
42. },
43. "lastTextBlock": {
44. "firstLine": "14:20",
45. "secondLine": "成都天府"
46. },
47. "displayHorizontalLine": true,
48. "spaceIcon": "space.png", // 取值为“/resources/rawfile”路径下的文件名
49. "extend": {
50. "type": 3,
51. "pic": "flight.png", // 取值为“/resources/rawfile”路径下的文件名
52. "clickAction": {
53. "actionType": 1,
54. "action": "xxxxxxx"
55. }
56. }
57. },
58. "capsuleData": {
59. "type": 1,
60. "status": 1,
61. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
62. "bgColor": "#FF317AF7",
63. "remind": "EXPAND",
64. "title": "即将出发",
65. "content": "请尽快前往机场"
66. }
67. }
68. },
69. "target": {
70. "token": [
71. "MAAALgE4G98BAAAAst************jq"
72. ]
73. }
74. }
```

### 出行打车场景（event为TAXI）

司机正在赶来，使用进度可视化模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 2,
17. "operation": 0,
18. "event": "TAXI",
19. "status": "DRIVER_ON_THE_WAY", // 司机正在赶来
20. "activityData": {
21. "notificationData": {
22. "type": 3,
23. "contentTitle": "{{status}}", // 司机正在赶来
24. "contentText": [
25. {
26. "text": "距您"
27. },
28. {
29. "text": "1.2公里",
30. "foregroundColor": "#FF317AF7"
31. },
32. {
33. "text": " | "
34. },
35. {
36. "text": "5分钟",
37. "foregroundColor": "#FF317AF7"
38. }
39. ],
40. "clickAction": {
41. "actionType": 1, // 打开应用自定义页面
42. "action": "xxxxxx" // 应用内置页面ability对应的action
43. },
44. "richProgress": {
45. "type": 0,
46. "nodeIcons": ["icon1.png", "icon2.png", "icon3.png"], // 取值为“/resources/rawfile”路径下的文件名
47. "indicatorIcon": "taxi.png", // 取值为“/resources/rawfile”路径下的文件名
48. "progress": 40,
49. "indicatorType": 1,
50. "color": "#FF317AF7",
51. "bgColor": "#19000000"
52. },
53. "extend": {
54. "type": 3,
55. "pic": "phone.png", // 取值为“/resources/rawfile”路径下的文件名
56. "clickAction": {
57. "actionType": 5, // 打开拨号界面
58. "data": {
59. "tel": "138xxxxxxxx" // 通过tel字段携带电话号码
60. }
61. }
62. }
63. },
64. "capsuleData": {
65. "type": 1,
66. "status": 1,
67. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
68. "bgColor": "#FF317AF7",
69. "remind": "EXPAND",
70. "title": "接驾中",
71. "content": "预计5分钟"
72. }
73. }
74. },
75. "target": {
76. "token": [
77. "MAAALgE4G98BAAAAst************jq"
78. ]
79. }
80. }
```

### 高铁/火车场景（event为TRAIN）

计划出发，使用左右文本模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 3,
17. "operation": 0,
18. "event": "TRAIN",
19. "status": "DEPART", // 计划出发
20. "title": "列车即将出发",
21. "content": "请尽快去高铁站",
22. "activityData": {
23. "notificationData": {
24. "keywords": {
25. "trainNo": "G1406"
26. },
27. "type": 5,
28. "contentTitle": "列车{{status}}", // 列车计划出发
29. "contentText": [
30. {
31. "text": "车次："
32. },
33. {
34. "text": "{{trainNo}}", // G1406
35. "foregroundColor": "#FF317AF7"
36. }
37. ],
38. "clickAction": {
39. "actionType": 0
40. },
41. "firstTextBlock": {
42. "firstLine": "13:00",
43. "secondLine": "上海虹桥"
44. },
45. "lastTextBlock": {
46. "firstLine": "14:20",
47. "secondLine": "南京南"
48. },
49. "displayHorizontalLine": true,
50. "spaceIcon": "space.png", // 取值为“/resources/rawfile”路径下的文件名
51. "extend": {
52. "type": 3,
53. "pic": "train.png", // 取值为“/resources/rawfile”路径下的文件名
54. "clickAction": {
55. "actionType": 1,
56. "action": "xxxxxxx"
57. }
58. }
59. },
60. "capsuleData": {
61. "type": 1,
62. "status": 1,
63. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
64. "bgColor": "#FF317AF7",
65. "remind": "EXPAND",
66. "title": "即将出发",
67. "content": "请尽快去高铁站"
68. }
69. }
70. },
71. "target": {
72. "token": [
73. "MAAALgE4G98BAAAAst************jq"
74. ]
75. }
76. }
```

## 更新实况窗消息

### 航班场景（event为FLIGHT）

已值机，使用左右文本模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 1,
17. "operation": 1,
18. "event": "FLIGHT",
19. "status": "CHECKED_IN", // 已值机
20. "version": 1,
21. "activityData": {
22. "notificationData": {
23. "keywords": {
24. "flightNo": "MU1471"
25. },
26. "type": 5,
27. "contentTitle": "登机口88",
28. "contentText": [
29. {
30. "text": "{{status}} | " // 已值机
31. },
32. {
33. "text": "{{flightNo}}", // MU1471
34. "foregroundColor": "#FF317AF7"
35. }
36. ],
37. "clickAction": {
38. "actionType": 0
39. },
40. "firstTextBlock": {
41. "firstLine": "12:00",
42. "secondLine": "上海虹桥"
43. },
44. "lastTextBlock": {
45. "firstLine": "14:20",
46. "secondLine": "成都天府"
47. },
48. "displayHorizontalLine": true,
49. "spaceIcon": "space.png", // 取值为“/resources/rawfile”路径下的文件名
50. "extend": {
51. "type": 3,
52. "pic": "flight.png", // 取值为“/resources/rawfile”路径下的文件名
53. "clickAction": {
54. "actionType": 1,
55. "action": "xxxxxxx"
56. }
57. }
58. },
59. "capsuleData": {
60. "type": 1,
61. "status": 1,
62. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
63. "bgColor": "#FF317AF7",
64. "remind": "EXPAND",
65. "title": "登机口88",
66. "content": "请尽快完成安检"
67. }
68. }
69. },
70. "target": {
71. "token": [
72. "MAAALgE4G98BAAAAst************jq"
73. ]
74. }
75. }
```

### 出行打车场景（event为TAXI）

正在去往目的地，使用进度可视化模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 2,
17. "operation": 1,
18. "event": "TAXI",
19. "status": "HEADING_TO_DESTINATION", // 正在去往目的地
20. "version": 1,
21. "activityData": {
22. "notificationData": {
23. "type": 3,
24. "contentTitle": "{{status}}", // 正在去往目的地
25. "contentText": [
26. {
27. "text": "距目的地"
28. },
29. {
30. "text": "7.2公里",
31. "foregroundColor": "#FF317AF7"
32. },
33. {
34. "text": " | 预计"
35. },
36. {
37. "text": "27分钟",
38. "foregroundColor": "#FF317AF7"
39. }
40. ],
41. "clickAction": {
42. "actionType": 1,
43. "action": "xxxxxx"
44. },
45. "richProgress": {
46. "type": 0,
47. "nodeIcons": ["icon1.png", "icon2.png", "icon3.png"], // 取值为“/resources/rawfile”路径下的文件名
48. "indicatorIcon": "taxi.png", // 取值为“/resources/rawfile”路径下的文件名
49. "progress": 60,
50. "indicatorType": 1,
51. "color": "#FF317AF7",
52. "bgColor": "#19000000"
53. },
54. "extend": {
55. "type": 0
56. }
57. },
58. "capsuleData": {
59. "type": 1,
60. "status": 1,
61. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
62. "bgColor": "#FF317AF7",
63. "title": "27分钟",
64. "content": "距目的地7.2公里"
65. }
66. }
67. },
68. "target": {
69. "token": [
70. "MAAALgE4G98BAAAAst************jq"
71. ]
72. }
73. }
```

行程结束，使用强调文本模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 2,
17. "operation": 1,
18. "event": "TAXI",
19. "status": "COMPLETED", // 行程结束
20. "version": 2,
21. "activityData": {
22. "notificationData": {
23. "type": 4,
24. "contentTitle": "{{status}}，请支付", // 行程结束，请支付
25. "contentText": [
26. {
27. "text": "全程"
28. },
29. {
30. "text": "10公里",
31. "foregroundColor": "#FF317AF7"
32. },
33. {
34. "text": " | 耗时"
35. },
36. {
37. "text": "30分钟",
38. "foregroundColor": "#FF317AF7"
39. }
40. ],
41. "clickAction": {
42. "actionType": 1,
43. "action": "xxxxxx"
44. },
45. "singleTextBlock": {
46. "firstLine": "全程费用",
47. "secondLine": "35.2元",
48. "underlineColor": "#FF317AF7"
49. },
50. "descPic": "payment.png", // 取值为“/resources/rawfile”路径下的文件名
51. "extend": {
52. "type": 0
53. }
54. },
55. "capsuleData": {
56. "type": 1,
57. "status": 1,
58. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
59. "bgColor": "#FF317AF7",
60. "title": "待支付",
61. "content": "费用35.2元"
62. }
63. }
64. },
65. "target": {
66. "token": [
67. "MAAALgE4G98BAAAAst************jq"
68. ]
69. }
70. }
```

### 高铁/火车场景（event为TRAIN）

列车运行中，使用左右文本模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 3,
17. "operation": 1,
18. "event": "TRAIN",
19. "status": "HEADING_TO_DESTINATION", // 列车运行中
20. "version": 1,
21. "activityData": {
22. "notificationData": {
23. "keywords": {
24. "trainNo": "G1406"
25. },
26. "type": 5,
27. "contentTitle": "{{status}}", // 列车运行中
28. "contentText": [
29. {
30. "text": "车次："
31. },
32. {
33. "text": "{{trainNo}}", // G1406
34. "foregroundColor": "#FF317AF7"
35. }
36. ],
37. "clickAction": {
38. "actionType": 0
39. },
40. "firstTextBlock": {
41. "firstLine": "13:00",
42. "secondLine": "上海虹桥"
43. },
44. "lastTextBlock": {
45. "firstLine": "14:20",
46. "secondLine": "南京南"
47. },
48. "displayHorizontalLine": true,
49. "spaceIcon": "space.png", // 取值为“/resources/rawfile”路径下的文件名
50. "extend": {
51. "type": 3,
52. "pic": "train.png", // 取值为“/resources/rawfile”路径下的文件名
53. "clickAction": {
54. "actionType": 1,
55. "action": "xxxxxxx"
56. }
57. }
58. },
59. "capsuleData": {
60. "type": 1,
61. "status": 1,
62. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
63. "bgColor": "#FF317AF7",
64. "title": "运行中",
65. "content": "预计14:20到达"
66. }
67. }
68. },
69. "target": {
70. "token": [
71. "MAAALgE4G98BAAAAst************jq"
72. ]
73. }
74. }
```

### 赛事比分场景（event为SCORE）

推送赛事最新比分，使用赛事比分模板。

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:7

9. // Request Body
10. {
11. "pushOptions": {
12. "ttl": 1000,
13. "biTag": "biTag"
14. },
15. "payload": {
16. "activityId": 4,
17. "operation": 1,
18. "event": "SCORE",
19. "activityData": {
20. "notificationData": {
21. "type": 7,
22. "contentTitle": "第四节比赛中",
23. "contentText": [
24. {
25. "text": "XX",
26. "foregroundColor": "#FF317AF7"
27. },
28. {
29. "text": " VS "
30. },
31. {
32. "text": "XX",
33. "foregroundColor": "#FF317AF7"
34. },
35. {
36. "text": " | 小组赛第五场"
37. }
38. ],
39. "game": {
40. "host": {
41. "icon":"host.png", // 取值为“/resources/rawfile”路径下的文件名
42. "name": "队名A",
43. "score": "110"
44. },
45. "guest": {
46. "icon":"guest.png", // 取值为“/resources/rawfile”路径下的文件名
47. "name": "队名B",
48. "score": "102"
49. },
50. "competition": {
51. "desc": "Q4",
52. "time":"02:16"
53. }
54. },
55. "displayHorizontalLine": true,
56. "clickAction": {
57. "actionType": 1,
58. "action": "xxxxxxx"
59. }
60. },
61. "capsuleData": {
62. "type": 1,
63. "status": 1,
64. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
65. "bgColor": "#FF317AF7",
66. "title": "110:102",
67. "content": "第四节比赛中"
68. }
69. }
70. },
71. "target": {
72. "token": ["MAAALgE4G98BAAAAst************jq"]
73. }
74. }
```

## 应用内通话消息

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"

4. // Request Header
5. Content-Type: application/json
6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
7. push-type:10

9. // Request Body
10. {
11. "pushOptions": {
12. "biTag": "biTag",
13. "ttl": 30
14. },
15. "payload": {
16. "extraData": "传递给应用的数据"
17. },
18. "target": {
19. "token": [
20. "MAAALgE4G98BAAAAst************jq"
21. ]
22. }
23. }
```
