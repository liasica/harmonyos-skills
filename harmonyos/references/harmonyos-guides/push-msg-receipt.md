---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-msg-receipt
title: （可选）开发消息回执
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > （可选）开发消息回执
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a57f0a2772132e27d367c312fb6916fc69348f9c202ab83ad182c5a213f0c4b
---

## 场景介绍

消息回执是指Push Kit服务端将消息推送到用户终端之后，端侧会给Push服务端反馈送达结果，与此同时，Push服务端会将消息送达状态以回执消息形式发送给您的应用回执服务端，方便您获取消息下达端侧后的状态，定位问题等。

受网络环境以及消息量的影响，消息回执在Push服务端收到端侧响应后发送，会存在一些延迟现象，如果较长时间无法收到回执，可能是设备处于离线状态。

## 回执服务开发

请参见[消息回执API](../harmonyos-references/push-api-msg-receipt.md)开发您的回执服务器代码，服务接口地址将作为[配置回执参数](push-msg-receipt.md#配置回执参数)中的回调地址。

## 开通回执权益

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/vK3Usdl0SZiyF_RctAs9UQ/zh-cn_image_0000002583439179.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=38ED96CB33D7B0628DF6D54CECA8BDED7A3128E2E072162BF5F4E9251EBAC4C6)
2. 在项目列表中找到您的项目，通过“增长 > 推送服务 > 配置”导航到“配置”页签。在该页面可以选择配置项目级回执或者应用级回执，需要注意的是项目级回执消息接收URL地址，对该项目下所有应用生效。如果您同时配置了项目级回执和应用级回执地址，则优先获取应用级回执地址信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/0wWpy-1GRaSHoW98OnGD3g/zh-cn_image_0000002552959134.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=E12F0A8B1B276152289879251564C7C02932F343F2D890E21A0E09865DA15F00)
3. 这里以应用级回执举例，选择需要配置回执的应用，点击“开通”应用回执状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/RqJXacHcRh2tMnAkGm5MkQ/zh-cn_image_0000002583479135.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=1FA513E4465BB258D17910221684D7204417F571B9922220DB9200783BAF39D6)
4. 进入回执参数配置，可以选择已有回执或者新建回执。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/_RsJr615TrWjQp7rjgM8ag/zh-cn_image_0000002552799486.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=8DC234622B4F70962DF8364F58E25C9FD109CC6E40266B3EDE2B5833FB2C7D38)

## 配置回执参数

点击“新建回执”后，需要配置如下参数：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/w8HVyYRZQNOpEcl8ofJ0Lw/zh-cn_image_0000002583439181.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=85456C589355093C4CA497DCD2F9058EB55C89082D5D2918912FC7CD8FE61383)

1. 配置消息回执的名称和回调地址。

   回调地址配置完成后，Push Kit服务器会校验回执服务器（接收回执消息的应用服务器）提供的证书是否为商用CA签发证书。

   * 商用CA提示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/9smUk2TmQVuvrICJ8DbsZg/zh-cn_image_0000002552959136.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=C2F1731B49760E1C21B88E9BC04825C775F54C2BBB428DD771058686DAEA77AB)
   * 自签CA提示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/bhzKzDmGTvCaABicVQkR_A/zh-cn_image_0000002583479137.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=E9B436C39ACAEC58EBDB28B1C6978B3470F3767C7CC035BE25D9EB322760E4BE)

   说明

   证书过期将导致您无法接收消息回执，请及时更换回执服务器证书。
2. 配置回调用户名（可选，下文描述为userName）和回调密钥（可选，下文描述为secret）进行身份验证。回调密钥支持自动生成。

   1. 从回执消息的请求Header中获取X-HUAWEI-CALLBACK-ID，举例如下：

      ```
      1. X-HUAWEI-CALLBACK-ID:
      2. timestamp=1563*****1261;nonce=a07bfa17-6d82-4b53-a9a2-07c*****eef1;value=E4YeO*********************QXF+c=
      ```

      其中timestamp为回执消息的时间戳（毫秒级时间戳），nonce为UUID随机数，value为签名信息，签名方法为：Base64(HMAC-SHA256(secret, timestamp+nonce+userName))。
   2. 开发者可以根据timestamp、nonce、userName、secret参考示例生成签名，与value的值比较进行签名验证。开发者也可点击网页提供的“生成密钥”自动生成回调密钥。

      生成签名示例（以下为java代码）：

      ```
      1. StringBuilder buf = new StringBuilder();
      2. buf.append(timestamp);
      3. buf.append(nonce);
      4. // 在回执配置中的回调用户名
      5. buf.append(userName);
      6. // 在回执配置中的回调密钥
      7. String secret = "your secret";
      8. String signature = "";
      9. try {
      10. Mac mac = Mac.getInstance("HmacSHA256");
      11. // 老旧版本的回执配置密钥使用secret.getBytes(UTF_8)，新的回执配置密钥使用base64编码
      12. SecretKeySpec key = new SecretKeySpec(Base64.getDecoder().decode(secret), "HmacSHA256");
      13. mac.init(key);
      14. byte[] encodeV = mac.doFinal(buf.toString().getBytes(UTF_8));
      15. signature = Base64.getEncoder().encodeToString(encodeV);
      16. } catch (NoSuchAlgorithmException | InvalidKeyException e) {
      17. // 打印错误日志
      18. // ...
      19. }
      ```
3. 配置回执支持版本

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/pJsYyGZvSueIVGrfqchfLg/zh-cn_image_0000002552799488.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=ABA88BFBA5F74FB05DFDF70ADB8CAB2F4C370842D73458ED32772E42D6629BDB)

   V1回执不支持场景化消息发送，请使用V2回执。
4. “测试回执”可以对回执地址进行功能测试，点击“提交”完成回执的创建。

   说明

   * 华为Push服务器和接收回执消息的应用服务器之间使用HTTPS协议，华为Push服务器会校验应用服务器提供证书的合法性，请使用商用CA签发的HTTPS证书。
   * 如果您的回执配置正确，点击“测试回执”后，您的回执服务器将收到由华为Push服务器发送的测试消息，同一回执版本该消息内容固定，仅供测试使用。

   **示例报文：**

   消息到达回执：

   说明

   除卡片刷新场景外的其他场景化消息均支持消息到达回执。

   ```
   1. {
   2. "statuses": [
   3. {
   4. "biTag": "bi**62",
   5. "pushType": 0,
   6. "token": "MsDZmCSyuS+Gd***********ZLs8Es",
   7. "requestId": "169802**1701",
   8. "appPackageName": "com.**.**",
   9. "deliveryStatus": {
   10. "result": 0,
   11. "timestamp": 1697741455082
   12. }
   13. }
   14. ]
   15. }
   ```

   卡片刷新回执：

   ```
   1. {
   2. "statuses": [
   3. {
   4. "biTag": "bi**62",
   5. "pushType": 1,
   6. "token": "MsDZmCSyuS+Gd***********ZLs8Es",
   7. "requestId": "169802**1701",
   8. "appPackageName": "com.**.**",
   9. "formStatus": {
   10. "formId": 10086,
   11. "result": 0,
   12. "timestamp": 1698027152082
   13. }
   14. }
   15. ]
   16. }
   ```

   您的回执服务器必须返回成功的响应，才能测试通过，再点击“提交”完成回执的创建。

   成功响应：

   ```
   1. {
   2. "code": "0",
   3. "message": "success"
   4. }
   ```

## 回执状态码

说明

通过回执状态码定位问题之前，请优先检查[消息推送接口](../harmonyos-references/push-scenariozed-api-request-struct.md)URL（https://push-api.cloud.huawei.com/**v3**/**[projectId]**/messages:send）是否正确：

* 请使用v3版本的推送接口URL，不要使用v1或v2版本的推送接口URL，详情请参见[场景化消息中的请求URL版本问题](push-faq-8.md)。
* 请检查推送接口地址中的projectId，确保与您当前应用所属的项目保持一致，若不一致请更新推送接口URL中的projectId，并重新[生成鉴权令牌](push-jwt-token.md)，应用重新[获取Push Token](push-get-token.md)，再进行消息推送。

您可以基于接收到的消息回执码进行数据统计和分析，回执状态码如下表所示：

| 回执状态码 | 状态码描述 | 原因及处理 |
| --- | --- | --- |
| 0 | 成功送达 | 不涉及。 |
| 2 | Token无效，应用卸载 | 成功发送到设备后发现应用不存在，通常表示应用已卸载。 |
| 5 | Token无效，Token不匹配 | 终端收到应用的Push消息，但Push消息带的Token与本地应用的Token不一致。请排查以下几种原因：  · 终端用户清除了本地应用数据。  · 终端用户通过卸载再安装的方式更新了本地应用。  · 您在应用中调用pushService.[deleteToken](../harmonyos-references/push-pushservice.md#pushservicedeletetoken)()方法删除了本地应用的Token。  · 您在应用中调用了[deleteAAID](../harmonyos-references/push-aaid-api.md#aaiddeleteaaid)()，该方法删除AAID的同时也会删除本地应用的Token。  · 终端设备恢复出厂设置后终端用户重新进入预安装应用或者重新安装并进入应用。  终端收到应用的Push消息，但检查本地数据存储中并没有应用的Token。请排查以下原因：  · 应用未激活。  若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 6 | 通知消息不展示 | 请排查以下三种原因：  · 用户关闭了设备上的系统通知总开关。  · 用户关闭了本应用的通知渠道开关。  · 用户开启了未成年模式。 |
| 10 | 非活跃设备 | 设备为非活跃设备（终端设备未接入网络达30天），消息不进行下发。 |
| 14 | 其它错误 | 系统内部网络异常。 |
| 15 | 离线用户消息管控 | 1. 设置了离线用户消息覆盖（服务端API中的collapseKey）功能，消息被覆盖掉了，未下发到设备。  2. 离线消息最多缓存120条，超过后旧消息被新消息覆盖。 |
| 22 | 目标用户不匹配 | 下发消息时Push Token归属的用户与当前终端设备上的本地用户不匹配。请排查Push Token是否是当前本地用户下申请的。  **说明：**  如您在进入隐私空间前的本地用户为用户A，点击进入隐私空间后，系统会将本地用户切换为用户B，如果此刻您使用归属用户A下的Push Token推送消息，则会返回该回执状态码。 |
| 27 | 应用进程不在，后台消息被缓存 | 在终端设备上目标应用进程不存在导致后台消息被缓存。 |
| 31 | 目标应用中不存在指向的页面 | 请参见[点击消息动作](push-send-alert.md#点击消息动作)检查应用skills标签配置和消息请求体中的clickAction字段。 |
| 51 | 终端设备处于开机未解锁状态 | 用户重启终端设备后，点亮屏幕未解锁。 |
| 102 | 消息频控丢弃 | 系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。 |
| 144 | profileId不存在 | 发送下行消息时请检查场景化消息payload中的[profileId](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段。 |
| 151 | 推送消息未展示或卡片formId不存在 | 1. 请检查卡片是否已经添加到终端设备桌面。  2. 请检查卡片刷新消息中指定的[formId](../harmonyos-references/push-scenariozed-api-request-param.md#formupdatepayload-卡片刷新消息)是否存在。 |
| 155 | 实况窗通知更新失败 | 请检查您的通知是否未创建或已经过期。 |
| 156 | 实况窗通知消息乱序更新 | 实况窗通知消息携带[version](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)小于当前版本，更新失败。 |
| 158 | 创建的实况窗已存在 | 在设备中已存在通过Live View Kit创建的[activityId](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)相同的实况窗。 |
| 188 | 拉起应用失败 | 请稍后重试。 |
| 191 | 角标更新失败 | 系统内部设置角标异常。 |
| 256 | 消息频次限制 | 频次限制请参考消息发送[频次限制](../harmonyos-references/push-msg-freq-control.md#场景化消息频控)。 |
| 259 | 消息被拒绝 | 1. 发送消息中存在违规内容。  2. 存在不安全的url。  请更换消息体内容或url。 |
| 261 | 卡片不存在 | 卡片刷新消息被Push服务端管控不下发（管控周期30天），建议做过滤处理减少无效推送。原因：不存在卡片刷新消息中指定[formId](../harmonyos-references/push-scenariozed-api-request-param.md#formupdatepayload-卡片刷新消息)的卡片。  建议填写已分配过的formId，避免后续formId分配后，对应的卡片刷新消息被管控导致管控周期内无法下发。 |
| 262 | 卡片刷新次数达上限 | 卡片刷新消息被Push服务端管控不下发（管控周期1天），建议做过滤处理减少无效推送。原因：终端设备上对应的卡片刷新次数达到上限（未被Push服务端频次限制）。 |
| 264 | 消息未订阅 | 发送的订阅消息，但实际未订阅。 |
| 265 | 实况窗通知更新被管控 | 发送的[activityId](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)对应的实况窗通知不存在，限制发送该activityId的实况窗通知消息24小时。 |
| 268 | 未携带status字段 | 通过Push Kit创建的实况窗，在对该实况窗更新时未携带[status](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)字段。 |
| 269 | 重复创建实况窗 | 通过Push Kit创建的实况窗重复（[activityId](../harmonyos-references/push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息)相同）。 |

说明

您需要对上述状态中的2、5、6、10做过滤处理，减少对这些用户的无效推送。
