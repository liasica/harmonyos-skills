---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-badge
title: 推送角标刷新消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送角标刷新消息
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:00+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:519c6c3fbb51428ab403aa5d7915b3fe77e6c060c3fb5a5eb60f8cd0181945ab
---

## 场景介绍

角标刷新消息仅适用于即时通讯类应用的多端角标同步场景。该功能主要用于设置应用角标上的数字，终端仅展示应用桌面的角标，从而提醒用户查看应用内的消息更新。

## 约束与限制

推送角标刷新消息能力支持Phone、Tablet、PC/2in1设备。

## 开通权益

推送角标刷新消息需要应用开通即时聊天通知消息自分类权益。请参见[申请通知消息自分类权益](push-apply-right.md#申请通知消息自分类权益)。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 应用服务端调用REST API推送角标刷新消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)。

   **说明** 

   * 发送角标刷新消息时，[payload.notification](../harmonyos-references/push-scenariozed-api-request-param.md#notification)中不可携带title和body字段。
   * 应用开通即时聊天通知消息自分类权益即可发送角标刷新消息，发消息时无需携带category参数，未申请即时聊天通知消息自分类权益的应用不可以发送角标刷新消息。
   * 请使用V3版本的请求URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）进行消息推送。

   请求示例如下：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0

   // Request Body
   {
     "payload": {
       "notification": {
         "badge" :
         {
           "setNum" : 99
         }
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：0表示角标刷新消息场景。
   * setNum：表示应用要显示的角标数量，取值为大于等于0小于100的整数。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送可发送Token数不超过10个。详情请参见[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
3. 通过观察应用的角标数字是否更新为预期值，以验证设备是否收到角标刷新消息。
