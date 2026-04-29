---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-intro
title: 功能介绍
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息 > 功能介绍
category: harmonyos-references
scraped_at: 2026-04-29T14:09:09+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0600e69ebf093c7232825677186238179ae44311c8d11699b52cb32358e70e5c
---

说明

为了更安全的网络访问，华为Push Kit于2022年11月30日关闭Push相关域名的TLS1.0、TLS1.1协议及规定之外的加密套件，当前应用使用TLS1.2以下协议或使用规定外的加密套件将无法正常推送消息。

若您的应用访问Push相关域名使用协议是TLS1.0或TLS1.1，可能无法正常发送消息，请您务必升级到TLS1.2及以上版本。

V3场景化接口将典型的推送场景按照类型拆分为多种场景，不同场景定义为不同**push-type**，提供基于场景的消息发送，治理和差异化能力，实现更好的消息触达和用户使用体验。

## 场景介绍

| push-type | 名称 | 场景介绍 | 备注 |
| --- | --- | --- | --- |
| 0 | Alert消息 | 通知消息。 | 需[申请通知消息自分类权益](../harmonyos-guides/push-apply-right.md#申请通知消息自分类权益)。 |
| 1 | 卡片刷新 | 卡片刷新。 | - |
| 2 | 语音播报消息 | Push Kit拉起通知扩展子进程，您可以在通知扩展子进程中处理语音播报业务。 | 需申请[推送语音播报消息权益](../harmonyos-guides/push-apply-right.md#申请通知消息自分类权益)。 |
| 6 | 后台消息 | Push Kit检测应用是否启动，应用如果启动消息传递到目标应用。应用如果未启动，则缓存。 | - |
| 7 | 实况窗消息 | 实况窗创建、更新或结束。 | 需[申请实况窗权益](../harmonyos-guides/liveview-rights.md)。 |
| 10 | 应用内通话消息 | 应用内通话消息。 | 需[申请推送应用内通话消息权益](../harmonyos-guides/push-apply-right.md#申请推送应用内通话消息权益)。 |

## 使用约束

* 消息体最大不能超过4096Bytes（不包括Push Token），若超过请求会返回错误码[80300008](push-scenariozed-api-response.md#section80300008-消息体大小超过4096bytes不包括push-token)。
* 每个项目每日全网最多可推送1000条测试消息，正式消息区分场景有不同的配额，参考[消息频控](push-msg-freq-control.md)说明。
