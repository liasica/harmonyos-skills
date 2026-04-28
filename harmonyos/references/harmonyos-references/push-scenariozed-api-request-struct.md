---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-struct
title: 请求体结构说明
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息 > 请求体结构说明
category: harmonyos-references
scraped_at: 2026-04-28T08:18:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c0b513dfc327be2ad148e7755d7b1c8ca43878f23225253beda14756608cbb4
---

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为Push服务器
* **接口URL：** https://push-api.cloud.huawei.com/v3/**[projectId]**/messages:send
* **数据格式：** Content-Type: application/json

说明

**[projectId]** ：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面中获取。

## Request Header

| 参数 | 取值描述 | 样例 |
| --- | --- | --- |
| Authorization | 鉴权方式：**JWT方式**。  **说明：**  HarmonyOS 5及以上系统版本推送不再支持OAuth 2.0开放鉴权方式。  详情参见[基于服务账号生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)。  **说明：**  建议JWT令牌过期时间设置为3600秒，有效期内可以复用。  Bearer后面拼接空格，再拼接获取的鉴权信息。 | Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\* |
| push-type | 消息类型，取值如下：  0：Alert消息（通知消息）  1：卡片刷新消息  2：语音播报消息  6：后台消息  7：实况窗消息  10：应用内通话消息 | 0 |

## Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| payload | 是 | Object | 推送消息结构体，不同的push-type场景拥有不同的payload定义：  0：[AlertPayload](push-scenariozed-api-request-param.md#alertpayload-通知消息) 通知消息  1：[FormUpdatePayload](push-scenariozed-api-request-param.md#formupdatepayload-卡片刷新消息) 卡片刷新消息  2：[ExtensionPayload](push-scenariozed-api-request-param.md#extensionpayload-语音播报消息) 语音播报消息  6：[BackgroundPayload](push-scenariozed-api-request-param.md#backgroundpayload-后台消息) 后台消息  7：[LiveViewPayload](push-scenariozed-api-request-param.md#liveviewpayload-实况窗消息) 实况窗消息  10：[VoIPCallPayload](push-scenariozed-api-request-param.md#voipcallpayload-应用内通话消息) 应用内通话消息 |
| pushOptions | 否 | Object | 发送控制参数，详情请参见[pushOptions](push-scenariozed-api-request-param.md#pushoptions)的定义。 |
| target | 是 | Object | 发送目标，详情请参见[target](push-scenariozed-api-request-param.md#target)的定义。 |
