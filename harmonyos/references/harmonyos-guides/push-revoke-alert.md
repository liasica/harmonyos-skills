---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-revoke-alert
title: 撤回通知消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送通知消息 > 撤回通知消息
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:93cfe180a4389d2769608aab4ce8f4ee5304a1c67e216c47e79a218b7457eca3
---

当推送的通知消息内容有误或者存在违规情况时，可能会引起用户投诉或监管部门处罚等不良后果。Push Kit为您提供消息撤回功能，降低此类推送可能造成的影响。

说明

* 消息撤回仅支持使用token和notifyId撤回。
* 若要使用消息撤回功能，请确保您在推送消息时设置了notifyId字段。
* 消息撤回仅支持以下类型：

  还未下发到端侧的消息。

  已在终端展示但用户还未点击的消息。
* 消息撤回不会影响应用的通知角标。

## 约束与限制

撤回通知消息能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

1. 参考[开发步骤](push-send-alert.md#开发步骤)章节进行消息推送，确保应用可正常收到通知消息。
2. 应用服务端调用REST API撤回通知消息，消息详情可参见[消息撤回](../harmonyos-references/push-msg-revoke.md)，请求示例如下：

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v1/[clientId]/messages:revoke"

   4. // Request Header
   5. Content-Type:application/json
   6. Authorization:Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 0

   9. // Request Body
   10. {
   11. "notifyId": 1234567,
   12. "token": [
   13. "pushToken1",
   14. "pushToken2",
   15. "pushToken3"
   16. ]
   17. }
   ```

   * [clientId]：请替换为您应用的Client ID，可参见[指导](../app/agc-help-view-app-info-0000002282674569.md)获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-msg-revoke.md#request-header)获取。
   * push-type：0表示通知消息场景。
   * notifyId：消息ID，消息的唯一标识，详情请参见[notifyId](../harmonyos-references/push-msg-revoke.md#request-body)。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
