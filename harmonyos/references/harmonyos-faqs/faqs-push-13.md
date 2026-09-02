---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-13
title: 发送无效消息是否会消耗频控额度
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 发送无效消息是否会消耗频控额度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aeb7e028a1f685ea38828822a5ae9895096d1afa92e3512efb7fd15f98e3acee
---

## 问题现象

通过AGC自助查询推送消息，结果显示频控。但设备当天从未收到通知，为何显示被频控？

## 解决方案

无效推送会占用消耗频控额度，导致消息到达率低。建议[开发消息回执](../harmonyos-guides/push-msg-receipt.md)，针对下列状态做过滤处理，减少对这些用户的无效推送，详情参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

| 回执状态码 | 状态码描述 | 说明 |
| --- | --- | --- |
| 2 | Token无效，应用卸载。 | 成功发送到设备后发现应用不存在，通常表示应用已卸载。 |
| 5 | Token无效，Token不匹配。 | 终端收到应用的Push消息，但Push消息带的Token与本地应用的Token不一致。 |
| 6 | 通知消息不展示。 | 请排查以下三种原因： 1、用户关闭了设备上的系统通知总开关。2、用户关闭了本应用的通知渠道开关。3、用户开启了未成年模式。 |
| 10 | 非活跃设备。 | 设备为非活跃设备（终端设备未接入网络达30天），消息不进行下发。 |
