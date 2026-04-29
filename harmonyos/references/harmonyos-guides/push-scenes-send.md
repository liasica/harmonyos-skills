---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-scenes-send
title: 推送场景化消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > 推送场景化消息
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a165de81b107005d6be375934a7b25875731852998180e4dd86680f8cecbccc2
---

## 场景介绍

Push Kit支持您使用HTTPS协议接入云侧，使用场景化V3接口发送场景化消息，并将不同场景定义为不同push-type。

您可发送的场景化消息类型如下表：

| push-type | 名称 |
| --- | --- |
| 0 | Alert消息（通知消息） |
| 1 | 卡片刷新消息 |
| 2 | 语音播报消息 |
| 6 | 后台消息 |
| 7 | 实况窗消息（Wearable、TV、PC/2in1不支持） |
| 10 | 应用内通话消息（Wearable、TV、PC/2in1不支持） |

有关场景化消息的更详细说明，请参见REST API-[场景化消息API接口](../harmonyos-references/push-scenariozed-api-intro.md#场景介绍)。

## 开发步骤

1. 您的服务端获取鉴权令牌，详情请参见[基于服务账号生成鉴权令牌](push-jwt-token.md)。
2. 您的服务端调用API发送Push场景化消息，更多消息内容请参见REST API-[场景化消息API接口](../harmonyos-references/push-scenariozed-api-intro.md#场景介绍)。

   **HTTPS POST URL：**

   ```
   1. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"
   ```

   “[projectId]”请替换为您应用的项目ID。登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取“项目ID”。

   **请求消息头示例：**

   ```
   1. Content-Type: application/json
   2. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   3. push-type: 0
   ```

   * 请求消息头中的Authorization参数为"Bearer "拼接上您在上一步[在线生成服务账号鉴权令牌](push-jwt-token.md)中获取的鉴权令牌。
   * 请求消息头中的push-type参数为场景化消息类型，0代表Alert消息（通知消息）。

   **通知消息体示例：**

   ```
   1. {
   2. "payload": {
   3. "notification": {
   4. "category": "MARKETING",
   5. "title": "普通通知标题",
   6. "body": "普通通知内容",
   7. "clickAction": {
   8. "actionType": 0
   9. },
   10. "notifyId": 12345
   11. }
   12. },
   13. "target": {
   14. "token": ["MAMzLg**********lPW"]
   15. },
   16. "pushOptions": {
   17. "testMessage": true
   18. }
   19. }
   ```

   * 更多场景化消息示例可参见[请求示例](../harmonyos-references/push-scenariozed-api-request-example.md)。
   * 建议您在开发代码前先使用Postman等调试工具发送消息，测试功能。
3. （可选）您的应用服务器接收Push Kit的消息回执，详情请参见[消息回执](push-msg-receipt.md)。

说明

Push Kit提供了基于Java语言的服务端示例代码（包括申请鉴权令牌、发送通知消息、卡片刷新消息等功能），方便您参考使用，详情请参见[示例代码](https://gitcode.com/HarmonyOS_Samples/push-kit_-sample-code_-server-demo_-java)。

## AppGallery Connect在线推送通知消息

说明

**当前仅支持配置Alert消息**。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，点击“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/DjKbzZLfTce0PPDgmprNAw/zh-cn_image_0000002589245439.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=3170A649A6C6754A7D058F185A7570F8C1D267A5DCFC6AAF0E7F871220F93337)
2. 在项目列表中找到您的项目，通过“增长 > 推送服务 > 推送通知（V3 Beta）”导航到“推送通知（V3 Beta）”页签。在该页签下点击“添加推送通知”新建推送任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/YPOY-kb-RR6adSQy0LolKQ/zh-cn_image_0000002558765632.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=9EB6B594A4BD1836AEC51A4DF1B613632E03396F454CD85C29F75F2CB97DF4D6)
3. 这里以Alert消息举例，配置参数如下。

   * **配置推送任务**

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/l4cXeOrdQoifi50CSaARyQ/zh-cn_image_0000002558605976.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=F0AAD0B7703301B73D1DD4CC34C51A9432EAF18483CC0BD74900C7BFE2F436C1)

     | 字段值 | 说明 |
     | --- | --- |
     | 选择应用 | 消息发送的目标应用，此字段为必填字段。 |
     | 名称 | 用于在管理台中标识通知，此名称不会给用户显示，此字段为必填字段。 |
     | 场景化类型 | 场景化消息类型，**当前仅支持Alert消息**。 |
   * **配置推送内容-通用参数**

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/NmJSi6T9To-dUpTmdJVtzg/zh-cn_image_0000002589325503.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=A85C992D25456E8541BAA8DF9FA670D903ED243BBD99AF607733FC96B9E6DF3D)

     | 字段值 | 说明 |
     | --- | --- |
     | 是否测试消息 (testMessage) | 测试消息标识，对应场景化接口中的testMessage参数，此字段为必填字段。  测试消息标识：  false：正式消息  true：测试消息 **（默认值）** |
     | 离线消息缓存机制 (collapseKey) | 离线消息缓存控制方式，，对应场景化接口中的collapseKey参数，此字段为可选字段。  离线消息缓存控制方式，取值范围-1~100。  -1：对所有离线消息都缓存（**默认值）** ；  0~100：离线消息缓存分组标识，对离线消息进行分组缓存，每个应用每一组只缓存一条最新的离线消息。 |
     | 消息缓存时间 (ttl) | 对应场景化接口中的ttl参数，此字段为可选字段。  消息缓存时间，单位是秒。在用户设备离线时，消息在Push服务器进行缓存，在消息缓存时间内用户设备上线，消息会下发，超过缓存时间后消息会丢弃，**默认值为86400秒（1天）** ，最大值为15天。 |
     | 批量任务消息标识 (biTag) | 对应场景化接口中的biTag参数，此字段为可选字段。  批量任务消息标识，[消息回执](push-msg-receipt.md)时会返回给应用服务器，长度最大64字节。 |
     | 回执ID (receiptId) | 对应场景化接口中的receiptId参数，此字段为可选字段。  回执ID指定本次下行消息的回执地址及配置。该回执ID可以在[配置回执参数](push-msg-receipt.md#配置回执参数)中查看。 |
   * **配置推送内容-发送目标设备**

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/dBT_d7sZTSSOhwxSGYRu3g/zh-cn_image_0000002589245441.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=0F81A26346E7A192DEA1F39168F3D7DF440AC3487F37805C80333FEE07077478)

     | 字段值 | 说明 |
     | --- | --- |
     | 设备Token (token) | 对应场景化接口中的token参数，此字段为必填字段。  按照Token向目标用户推送消息。  **样例：MAMzL\*\*\*\*\*\*\*** |
   * **配置推送内容-消息内容**

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/eXuBaVe6SCOLer5Ul_hv-g/zh-cn_image_0000002558765634.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=AA0E3AD6BF0E09EE65686EF40BDB12AC90D13F1A1671CFD430B8DEB9BEC382CA)

     | 字段值 | 说明 |
     | --- | --- |
     | 消息类别 (category) | 对应场景化接口中的category参数，此字段为必填字段。  通知消息类别。完成[申请通知消息自分类权益](push-apply-right.md#申请通知消息自分类权益)后，用于标识消息类型，不同的通知消息类型影响消息展示和提醒方式。取值如下：  · 即时聊天：IM  · 音视频通话：VOIP  · 订阅：SUBSCRIPTION  · 出行：TRAVEL  · 健康：HEALTH  · 工作事项提醒：WORK  · 账号动态：ACCOUNT  · 订单&物流：EXPRESS  · 财务：FINANCE  · 设备提醒：DEVICE\_REMINDER  · 邮件：MAIL  · 新闻、内容推荐、社交动态、产品促销、财经动态、生活资讯、调研、功能推荐、运营活动（仅对内容进行标识，不会加快消息发送），统称为资讯营销类消息：MARKETING  · PLAY\_VOICE：语音播报 |
     | 消息标题 (title) | 对应场景化接口中的title参数，此字段为必填字段。  通知消息标题。 |
     | 消息内容 (body) | 对应场景化接口中的body参数，此字段为必填字段。  通知消息内容。 |
     | 点击通知动作 (actionType) | 对应场景化接口中的clickAction中actionType参数，此字段为必填字段。  点击消息后触发的动作，可选择打开应用首页、自定义action页面或自定义intentUri页面。 |
4. 当您完成上述步骤后，点击右上方“提交”按钮即可推送消息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/3TizupuUS-SxYNPF9isp1g/zh-cn_image_0000002558605978.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=B818EC38AD56C79A18AA16AB036F0A33DF361473A0CCA0BEECD6D6E4F70D21C6)

   说明

   预览效果仅供参考，请以客户端实际效果为准。
