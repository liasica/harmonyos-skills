---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-update-liveview
title: 推送实况窗消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送实况窗消息
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:629aa3fdd7b85495b14981552a7f8aaf19ec99c9e380b0091e5ced52e06904f0
---

## 场景介绍

实况窗是一种帮助用户聚焦正在进行的任务，方便快速查看和即时处理的通知形态。有关实况窗简介、权限申请、开放场景、设计规范等说明，请参见[Live View Kit简介](liveview-introduction.md)。

通过Push Kit发送的实况窗消息支持三种操作类型，分别是：

| 实况窗消息操作类型 | 支持操作的场景类型 | 说明 |
| --- | --- | --- |
| 创建实况窗 | FLIGHT、TAXI、TRAIN | 仅航班、出行打车、高铁/火车场景支持通过Push Kit创建实况窗，其他场景请通过Live View Kit本地创建。 |
| 更新实况窗 | 所有场景 | 所有场景皆支持通过Push Kit更新实况窗。 |
| 结束实况窗 | 所有场景 | 所有场景皆支持通过Push Kit结束实况窗。 |

说明

推送实况窗消息仅支持Phone、Tablet设备。

有关场景类型的详细说明请参见[支持的范围与场景](liveview-introduction.md#支持的范围与场景)。

根据创建实况窗的方式不同，通过Push Kit发送实况窗消息的流程有所区别。

**通过Live View Kit创建实况窗，Push Kit更新与结束实况窗**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ZXNKu5J6S-q_nXoNBlROOw/zh-cn_image_0000002583439171.png?HW-CC-KV=V1&HW-CC-Date=20260427T235030Z&HW-CC-Expire=86400&HW-CC-Sign=5C2BB5D804C253BCCEA4B457CE6C6B9B08A1BF1F89E7B0BC5E6F635275A22B2F)

1. 使用Push Kit，获取Push Token。
2. 使用Live View Kit创建实况窗成功后，开发者需要将实况窗id、pushToken、实况窗场景event以及业务服务的相关的状态属性保存到业务服务端。
3. 当业务服务的用户订单状态发生变化时，通过Push Kit通道推送更新消息，更新/结束实况窗。

**通过Push Kit创建、更新、结束实况窗**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/SeoJhipsSIeVIivFBdxReA/zh-cn_image_0000002552959126.png?HW-CC-KV=V1&HW-CC-Date=20260427T235030Z&HW-CC-Expire=86400&HW-CC-Sign=8C892EF8A10C2BCB65BC8D4BF3013470F2E7BAD5C5A0EAFE5A6FAAE0DC3B7A0E)

1. 使用Push Kit，获取Push Token。
2. 将Push Token保存到业务的服务端。
3. 通过Push Kit推送创建/更新/结束实况窗消息。

**实况窗更新效果示例图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/fMFc1uOQTD-mBVfPM-YJgg/zh-cn_image_0000002583479127.png?HW-CC-KV=V1&HW-CC-Date=20260427T235030Z&HW-CC-Expire=86400&HW-CC-Sign=A8F2E6BC0956189CBE360300D95885BCACE6C3E9776A48B731FC6910132135C3)

说明

* 单个实况窗的生命周期最长不超过8小时，超过8小时后，系统会认为通知结束。
* 为了确保用户看到内容的时效性，请您确保对实况窗内容进行及时更新。系统将在实况窗超过2小时未更新时，隐藏实况窗在状态栏胶囊和锁屏的展示，保留通知中心展示；超过4小时未更新，系统会认为实况窗结束，并从各个展示入口清除该实况窗。

## 开通权益

推送实况窗消息前您需要开通对应的场景权益，可参见[开通实况窗权益](liveview-formal-authority.md)完成权益的申请。

说明

必须要开通实况窗权益才可以通过Push Kit推送实况窗消息，无法通过添加白名单设备的方式进行调试。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。

单个实况窗消息，出行打车与赛事比分场景每个设备每5分钟最多更新30次，每小时最多更新180次。其余场景每个设备每5分钟最多更新10次，每小时最多更新60次。超过频次部分将丢弃不下发。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 根据应用情况选择创建实况窗的方式：

   * 通过Live View Kit创建本地实况窗，详细内容请参见[构建本地实况窗](liveview-create-locally.md)。
   * 通过Push Kit远程创建实况窗，需满足[创建实况窗约束](../harmonyos-references/push-scenariozed-api-request-param.md#创建实况窗约束)。以出行打车场景为例，消息示例如下：

     ```
     1. // Request URL
     2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

     4. // Request Header
     5. Content-Type: application/json
     6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
     7. push-type: 7

     9. // Request Body
     10. {
     11. "payload": {
     12. "activityId": 1,
     13. "operation": 0,
     14. "event": "TAXI",
     15. "status": "DRIVER_ON_THE_WAY", // 司机正在赶来
     16. "activityData": {
     17. "notificationData": {
     18. "type": 3,
     19. "contentTitle": "{{status}}", // 司机正在赶来
     20. "contentText": [
     21. {
     22. "text": "距您"
     23. },
     24. {
     25. "text": "1.2公里",
     26. "foregroundColor": "#FF317AF7"
     27. },
     28. {
     29. "text": " | "
     30. },
     31. {
     32. "text": "5分钟",
     33. "foregroundColor": "#FF317AF7"
     34. }
     35. ],
     36. "clickAction": {
     37. "actionType": 1, // 打开应用自定义页面
     38. "action": "xxxxxx" // 应用内置页面ability对应的action
     39. },
     40. "richProgress": {
     41. "type": 0,
     42. "nodeIcons": ["icon1.png", "icon2.png", "icon3.png"], // 取值为“/resources/rawfile”路径下的文件名
     43. "indicatorIcon": "taxi.png", // 取值为“/resources/rawfile”路径下的文件名
     44. "progress": 40,
     45. "indicatorType": 1,
     46. "color": "#FF317AF7",
     47. "bgColor": "#19000000"
     48. },
     49. "extend": {
     50. "type": 3,
     51. "pic": "phone.png", // 取值为“/resources/rawfile”路径下的文件名
     52. "clickAction": {
     53. "actionType": 0 // 点击辅助区打开应用首页
     54. }
     55. }
     56. },
     57. "capsuleData": {
     58. "type": 1,
     59. "status": 1,
     60. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
     61. "bgColor": "#FF317AF7",
     62. "remind": "EXPAND",
     63. "title": "接驾中",
     64. "content": "预计5分钟"
     65. }
     66. }
     67. },
     68. "pushOptions": {
     69. "ttl": 1000,
     70. "biTag": "biTag"
     71. },
     72. "target": {
     73. "token": [
     74. "MAAALgE4G98BAAAAst************jq"
     75. ]
     76. }
     77. }
     ```

     + [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
     + Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
     + push-type：7表示实况窗消息场景。
     + activityId：实况活动ID。详情请参见[activityId](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)。
     + operation：实况窗通知操作类型，0表示创建实况窗。详情请参见[operation](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)。
     + event：实况窗消息具体场景类型，需要与应用实际申请通过的场景一致。例如：TAXI（出行打车）、FLIGHT（航班）等。通过Push Kit创建实况窗仅支持TAXI、FLIGHT、TRAIN三种场景。详情请参见[创建实况窗约束](../harmonyos-references/push-scenariozed-api-request-param.md#创建实况窗约束)。
     + status：表示实况窗消息状态。operation为0时必填，取值范围根据场景类型而定，详情见[Status取值范围](../harmonyos-references/push-scenariozed-api-request-param.md#status取值范围)，并且需要在[支持携带占位符的字段](../harmonyos-references/push-scenariozed-api-request-param.md#支持携带占位符的字段)填入至少一次status的占位符{{status}}，Push Kit将替换占位符{{status}}为[Status取值范围](../harmonyos-references/push-scenariozed-api-request-param.md#status取值范围)中对应的值。
     + activityData：填写您项目中的实况窗数据。详情请参见[activityData](../harmonyos-references/push-scenariozed-api-request-param.md#activitydata)。
     + type：实况窗布局类型，有进度可视化类、强调文本类等。创建实况窗时每种event仅可使用特定的布局类型，详情请参见[创建实况窗约束](../harmonyos-references/push-scenariozed-api-request-param.md#创建实况窗约束)。
     + token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
3. 当用户的服务订单状态发生变化时，开发者可以调用Push Kit服务端开放的REST API服务接口，更新或者结束实况窗。

   消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)。（若开发者更新的实况窗为通过Push Kit远程创建的实况窗，更新时请遵守[创建实况窗约束](../harmonyos-references/push-scenariozed-api-request-param.md#创建实况窗约束)）

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   4. // Request Header
   5. Content-Type: application/json
   6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 7

   9. // Request Body
   10. {
   11. "payload": {
   12. "activityId": 1,
   13. "operation": 1,
   14. "event": "TAXI",
   15. "status": "HEADING_TO_DESTINATION", // 正在去往目的地
   16. "version": 1,
   17. "activityData": {
   18. "notificationData": {
   19. "type": 3,
   20. "contentTitle": "{{status}}", // 正在去往目的地
   21. "contentText": [
   22. {
   23. "text": "距目的地"
   24. },
   25. {
   26. "text": "7.2公里",
   27. "foregroundColor": "#FF317AF7"
   28. },
   29. {
   30. "text": " | 预计"
   31. },
   32. {
   33. "text": "27分钟",
   34. "foregroundColor": "#FF317AF7"
   35. }
   36. ],
   37. "clickAction": {
   38. "actionType": 1, // 打开应用自定义页面
   39. "action": "xxxxxx" // 应用内置页面ability对应的action
   40. },
   41. "richProgress": {
   42. "type": 0,
   43. "nodeIcons": ["icon1.png", "icon2.png", "icon3.png"], // 取值为“/resources/rawfile”路径下的文件名
   44. "indicatorIcon": "taxi.png", // 取值为“/resources/rawfile”路径下的文件名
   45. "progress": 70,
   46. "indicatorType": 1,
   47. "color": "#FF317AF7",
   48. "bgColor": "#19000000"
   49. },
   50. "extend": {
   51. "type": 0
   52. }
   53. },
   54. "capsuleData": {
   55. "type": 1,
   56. "status": 1,
   57. "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
   58. "bgColor": "#FF317AF7",
   59. "title": "27分钟",
   60. "content": "距目的地7.2公里"
   61. }
   62. }
   63. },
   64. "pushOptions": {
   65. "ttl": 1000,
   66. "biTag": "biTag"
   67. },
   68. "target": {
   69. "token": [
   70. "MAMzLg**********lPW"
   71. ]
   72. }
   73. }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：7表示实况窗消息场景。
   * activityId：实况活动ID。详情请参见[activityId](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)。
   * operation：实况窗通知操作类型，0表示创建实况窗，1表示更新实况窗，2表示结束实况窗。详情请参见[operation](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)。
   * event：实况窗通知具体场景类型，需要与应用实际申请通过的场景一致。例如：TAXI（出行打车）、FLIGHT（航班）等。详情请参见[event](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)。
   * status：表示实况窗消息状态。operation为1且更新的实况窗为通过Push Kit远程创建的实况窗时必填，取值范围根据场景类型而定，详情见[Status取值范围](../harmonyos-references/push-scenariozed-api-request-param.md#status取值范围)，并且需要在[支持携带占位符的字段](../harmonyos-references/push-scenariozed-api-request-param.md#支持携带占位符的字段)填入至少一次status的占位符{{status}}，Push Kit将替换占位符{{status}}为[Status取值范围](../harmonyos-references/push-scenariozed-api-request-param.md#status取值范围)中对应的值。
   * version：更新实况窗通知的版本号。详情请参见[version](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)。
   * activityData：填写您项目中的实况窗数据。详情请参见[activityData](../harmonyos-references/push-scenariozed-api-request-param.md#activitydata)。
   * type：实况窗布局类型，有进度可视化类、强调文本类等。详情请参见[type](../harmonyos-references/push-scenariozed-api-request-param.md#notificationdata)。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。

     说明

     若发送的activityId对应的实况窗不存在（更新或结束实况窗的场景中），将限制使用该activityId发送实况窗消息24小时。
