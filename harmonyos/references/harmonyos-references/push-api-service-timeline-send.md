---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-service-timeline-send
title: 服务动态推送接口
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 服务动态 > 服务动态推送接口
category: harmonyos-references
scraped_at: 2026-04-28T08:18:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30e653feaad31b1961addbbe6d25a9de7b224197b070f69efa7d4782b8a1cc70
---

说明

为了更安全的网络访问，华为服务动态仅支持TLS1.2及以上版本，应用使用TLS1.2以下协议或使用规定外的加密套件将无法正常发送消息。

## 功能介绍

元服务调用服务动态发送API，完成服务动态消息下发。

## 使用约束

* 服务动态能力支持Phone、Tablet设备。
* 消息体最大不能超过4096Bytes，若超过请求会返回错误码[82600005](push-api-service-timeline-send.md#section82600005-服务动态下发异常)。

## 请求体结构说明

### 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为Push服务器
* **接口URL：** https://push-api.cloud.huawei.com/v1/**[projectId]**/service\_timeline/send
* **数据格式：** Content-Type: application/json

说明

**[projectId]** ：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。

### Request Header

| 参数 | 取值描述 | 样例 |
| --- | --- | --- |
| Authorization | 鉴权方式：  **JWT方式**  详情参见[基于服务账号生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)。  **说明：**  · 调用服务动态API接口必须使用**PS256**算法。  · 建议JWT令牌过期时间设置为3600秒，有效期内可以复用。  Bearer后面拼接空格，再拼接获取的鉴权信息。 | Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\* |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| toOpenId | 是 | String | 接收者（用户）账号登录的openID。使用从端侧上报的openID，或请求华为账号服务器[获取用户信息](account-api-get-user-info-overview.md)。可参考元服务[账号使用规范](../design-guides/accounts-0000001967444380.md)进行华为账号登录的设计和接入。 |
| appId | 是 | String | 元服务的APP ID。长度范围[1, 64]。  **说明：**  **[appId]** ：登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“APP与元服务”，在列表中选择对应的元服务，左侧导航栏选择“应用信息”，在应用信息页面下的基本信息中获取**APP ID**的值。 |
| sceneId | 是 | String | 场景标识，详细参见[服务动态发送场景说明](push-api-service-timeline-param.md#服务动态发送场景说明)。长度范围[1, 32]。 |
| subSceneId | 是 | String | 子场景标识，详细参见[服务动态发送场景说明](push-api-service-timeline-param.md#服务动态发送场景说明)。长度范围[1, 32]。 |
| code | 是 | String | · 当用户在元服务内调用华为支付收银台进行支付时，开发者可获得华为支付订单号[sysTransOrderNo](payment-sys-query-order.md)，可直接作为code。  · 当用户通过前端场景化button获取code时，开发者可以使用[服务动态授权码Button](../atomic-guides/scenario-fusion-button-atomic-getservicecode.md)获取code。 |
| content | 是 | [TimelineStatusContent](push-api-service-timeline-param.md#timelinestatuscontent全量参数定义) Object | 服务动态指定状态参数。  若您是外卖自取场景，请参考[外卖自取结构体说明](push-api-service-timeline-param.md#外卖自取结构体说明)。  若您是外卖配送场景，请参考[外卖配送结构体说明](push-api-service-timeline-param.md#外卖配送结构体说明)。 |

## 请求示例

说明

根据不同状态必传参数、选填参数发送请求。以外卖自取场景为例。

**请求示例：制作中**

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v1/[projectId]/service_timeline/send"

4. // Request Header
5. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****

7. // Request Body
8. {
9. "appId": "5**********7",
10. "toOpenId": "A**********O",
11. "sceneId": "10001",
12. "subSceneId": "100010001",
13. "code": "3**********7",
14. "content": {
15. "status": 3,
16. "orderTime": 1716191520,
17. "amount": "¥ 18.00",
18. "productCount": 1,
19. "productName": "霸气芒果",
20. "productImg": "image_test_1",
21. "merchantName": "威**********店",
22. "pickupNumber": "1668",
23. "pickupTime": "16:08",
24. "remainOrders": "5单/共5杯",
25. "waitTime": "10-20分钟",
26. "button": {
27. "type": 0,
28. "text": "取餐码",
29. "data": {
30. "testKey": "testValue"
31. }
32. },
33. "clickAction": {
34. "type": 0,
35. "data": {
36. "testKey": "testValue"
37. }

39. },
40. "appendButtons": [
41. {
42. "type": 0,
43. "text": "取餐码",
44. "data": {
45. "testKey": "testValue"
46. }
47. }
48. ]
49. }
50. }
```

**请求示例：待支付**

```
1. // Request URL
2. POST "https://push-api.cloud.huawei.com/v1/[projectId]/service_timeline/send"

4. // Request Header
5. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****

7. // Request Body
8. {
9. "appId": "6**********3",
10. "toOpenId": "A**********F",
11. "sceneId": "10001",
12. "subSceneId": "100010001",
13. "code": "1**********6",
14. "content": {
15. "status": 1,
16. "orderTime": 1715236319,
17. "amount": "¥ 5.00",
18. "productCount": 1,
19. "productName": "霸气芒果",
20. "productImg": "image_test_1",
21. "paymentEndTime": "5分钟内支付",
22. "merchantName": "**********园店",
23. "button": {
24. "type": 0,
25. "text": "立即支付",
26. "action": "https://***"
27. },
28. "clickAction": {
29. "type": 0,
30. "action": "https://***"
31. },
32. "appendButtons": [
33. {
34. "type": 0,
35. "text": "立即支付",
36. "action": "https://***"
37. }
38. ]
39. }
40. }
```

## 响应参数

### Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| code | 是 | String | 响应码。 |
| msg | 是 | String | 响应码描述。 |
| requestId | 是 | String | 请求标识。 |

## 响应示例

**响应成功示例：**

```
1. {
2. "code": "80000000",
3. "msg": "Success",
4. "requestId": "157*******006"
5. }
```

**响应失败示例：**

```
1. {
2. "code": "82600010",
3. "msg": "status content missing required field",
4. "requestId": "157*******006"
5. }
```

## HTTP响应码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 400 | 参数错误。 | 请检查业务响应码并根据业务响应码进一步排查问题。 |
| 401 | 鉴权失败。 | 请检查HTTP头中Authorization参数。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 流量控制。 | · 平均分配发送速度。  · 平均分布推送时间段，不要集中发送。 |
| 504 | 网关超时。 | 建议稍后重试，或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 业务响应码

### 80000000 成功

**错误信息**

Success.

**错误描述**

发送成功。

**可能原因**

发送成功。

**处理步骤**

不涉及。

### 82600001 系统内部错误

**错误信息**

system error.

**错误描述**

系统内部错误。

**可能原因**

其他未知错误。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

### 82600002 参数错误

**错误信息**

invalid parameter {errorTips}.

**错误描述**

参数错误。

**可能原因**

携带的参数不合法。

**处理步骤**

请按照响应消息中的提示，检查并修改请求参数。

### 82600003 拒绝服务

**错误信息**

access deny.

**错误描述**

拒绝服务。

**可能原因**

未开通服务动态消息发送权益。

**处理步骤**

请开通[服务动态消息发送权益](../atomic-guides/push-as-timeline.md#section20387153745216)。

### 82600004 风控异常

**错误信息**

status content blocked.

**错误描述**

风控异常。

**可能原因**

场景参数中存在违禁参数。

**处理步骤**

请按照响应消息中的提示，检查场景参数是否携带违禁参数。

### 82600005 服务动态下发异常

**错误信息**

send message failed{errorTips}.

**错误描述**

服务动态下发异常。

**可能原因**

1. 接收端没有在线设备。
2. 请求消息体超过默认大小（4096Bytes）。

**处理步骤**

按照响应消息中的提示，检查消息下发异常情况：

1. 检查接收端是否有在线设备。
2. 检查请求消息体是否超过默认大小（4096Bytes），并减小请求体后重新推送。

### 82600006 openID校验异常

**错误信息**

invalid openId.

**错误描述**

openID校验异常。

**可能原因**

携带不正确接收者openID。

**处理步骤**

请使用从端侧上报的openID，或请求华为账号服务器[获取用户信息](account-api-get-user-info-overview.md)中的openID。

### 82600007 场景及子场景标识错误

**错误信息**

invalid sceneId or subSceneId.

**错误描述**

场景及子场景标识错误。

**可能原因**

场景及子场景未开通权益。

**处理步骤**

请按照已开通权益的场景及子场景标识发送。

### 82600008 授权码错误

**错误信息**

invalid code.

**错误描述**

授权码错误。

**可能原因**

1. 交易订单号非法。
2. 交易订单号超期未激活（有效期1小时）。

**处理步骤**

请检查交易订单号：

1. 确保交易订单号合法。
2. 请重新生成code进行推送。

使用华为支付订单号[sysTransOrderNo](payment-sys-query-order.md)作为授权码，重新推送消息。

### 82600009 场景状态错误

**错误信息**

invalid scene status.

**错误描述**

场景状态错误。

**可能原因**

请求体参数错误。

**处理步骤**

请按照响应消息中的提示，请按照[服务动态发送场景说明](push-api-service-timeline-param.md#服务动态发送场景说明)检查并修改请求体参数。

### 82600010 状态必填参数缺失

**错误信息**

status content missing required field {errorTips}.

**错误描述**

状态必填参数缺失。

**可能原因**

状态必填参数缺失。

**处理步骤**

请按照响应消息中的提示，请按照[服务动态发送场景说明](push-api-service-timeline-param.md#服务动态发送场景说明)检查并修改请求体参数。

### 82600011 状态参数格式不合法

**错误信息**

status content has invalid field {errorTips}.

**错误描述**

状态参数格式不合法。

**可能原因**

状态参数格式不合法。

**处理步骤**

请按照响应消息中的提示，检查并修改[请求体参数](push-api-service-timeline-send.md#request-body)。

### 82600012 状态跳转非法

**错误信息**

invalid status transition.

**错误描述**

状态跳转非法。

**可能原因**

状态跳转非法。

**处理步骤**

* 若您是外卖自取场景，请按照[自取场景服务动态参数要求](push-api-service-timeline-param.md#指定状态下发送服务动态参数要求)检查并修改请求体参数。
* 若您是外卖配送场景，请按照[配送场景服务动态参数要求](push-api-service-timeline-param.md#指定状态下发送服务动态参数要求-1)检查并修改请求体参数。

### 82600013 用户关闭服务动态推送

**错误信息**

user close service.

**错误描述**

用户关闭服务动态推送。

**可能原因**

用户关闭该场景服务动态推送。

**处理步骤**

请按照响应消息中的提示，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上开通服务动态推送权益，请参考[申请权益](../atomic-guides/push-as-timeline.md#section20387153745216)。

### 82600014 非法的图片资源ID

**错误信息**

invalid image id.

**错误描述**

非法的图片资源ID。

**可能原因**

资源ID对应的图片资源不存在。

**处理步骤**

请检查资源ID对应的图片资源是否存在，不存在则需要通过[申请图片资源托管](../atomic-guides/push-as-timeline.md#section19921168203013)提供图片重新获取资源ID。

### 82600015 状态刷新次数超过限制

**错误信息**

status refresh frequency reached upper limit.

**错误描述**

状态刷新次数超过限制。

**可能原因**

状态刷新次数超过限制。

**处理步骤**

状态刷新次数超过限制，请减少无效状态刷新。

### 82600016 服务动态超期

**错误信息**

event expired.

**错误描述**

服务动态超期。

**可能原因**

服务动态超期，超过expireTime后将禁止刷新该服务动态消息。

**处理步骤**

合理设置expireTime并重新推送消息。

### 82600017 用户无授权设备

**错误信息**

no authorization device.

**错误描述**

用户无授权设备。

**可能原因**

用户该场景无授权设备。

**处理步骤**

用户该场景无授权设备，请添加授权设备再重新推送消息。

### 82600018 服务动态事件已结束

**错误信息**

event already closed.

**错误描述**

服务动态事件已结束。

**可能原因**

该事件已关闭，不允许继续发送。

**处理步骤**

该事件已关闭，不允许继续发送，请重新创建服务动态事件下发消息。

### 82600019 激活授权码超出阈值

**错误信息**

code reached upper limit.

**错误描述**

激活授权码超出阈值。

**可能原因**

向同一用户推送的授权码超过20个。

**处理步骤**

默认向同一用户推送的授权码不能超过20个，请减少授权码个数。
