---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-intro
title: 功能介绍
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息推送 > 功能介绍
category: harmonyos-references
scraped_at: 2026-09-02T14:53:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e75afcf8e19eb4d7fec52c7c33a456c8ecc50a88665112fe51183e1a708629c8
---

对典型推送场景按类型进行拆分，并为不同场景定义独立的**push-type**，提供基于场景的消息发送、治理及差异化能力，有效提升消息触达效果与用户使用体验。

## 场景介绍

| push-type | 名称 | 场景介绍 | 备注 |
| --- | --- | --- | --- |
| 0 | Alert消息 | 通知消息。  角标刷新消息：仅更新角标，无消息提醒。 | 需[申请通知消息自分类权益](../harmonyos-guides/push-apply-right.md#申请通知消息自分类权益)。 |
| 1 | 卡片刷新 | 卡片刷新。 | - |
| 2 | 语音播报消息 | Push Kit拉起通知扩展子进程，您可以在通知扩展子进程中处理语音播报业务。 | 需申请[推送语音播报消息权益](../harmonyos-guides/push-apply-right.md#申请推送语音播报消息权益) |
| 6 | 后台消息 | 如果应用进程在前台则将消息内容传给应用；如果应用进程不在前台则缓存消息，等待应用启动后再传给应用。 | - |
| 7 | 实况窗消息 | 实况窗创建、更新或结束。 | 需[申请实况窗权益](../harmonyos-guides/liveview-rights.md) |
| 10 | 应用内通话消息 | 应用内通话消息。 | 需[申请推送应用内通话消息权益](../harmonyos-guides/push-apply-right.md#申请推送应用内通话消息权益) |

## 使用约束

* 消息体最大不能超过4096Bytes（不包括Push Token），若超过请求会返回错误码[80300008](push-scenariozed-api-response.md#section80300008-消息体大小超过4096bytes不包括push-token)。
* 每个项目每日全网最多可推送1000条测试消息，正式消息区分场景有不同的配额，参考[消息频控](push-msg-freq-control.md)说明。
