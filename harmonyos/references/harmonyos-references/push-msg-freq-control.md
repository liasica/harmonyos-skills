---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-msg-freq-control
title: 消息频控
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息 > 消息频控
category: harmonyos-references
scraped_at: 2026-04-28T08:18:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:15f6b328f589da8d622b79ec5d841e166610b57fce84c1cc5c2c4091c3183455
---

Push Kit消息频控包括场景化消息频控、设备消息频控、测试消息频控和消息推送速率管控，当超过了某个频控规则限制会返回对应的[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

说明

消息频控的数量是指应用发起消息推送请求的数量，无论设备是否成功展示消息都会增加计数，如果消息未按预期展示，建议不要频繁发起消息推送请求，请先进行[问题排查](../harmonyos-guides/push-faq-2.md)。

## 场景化消息频控

为了给用户提供更好的体验，营造清朗网络空间，华为推送服务根据不同的[推送场景](../harmonyos-guides/push-scenes-send.md)，设置了多条频控规则。

若场景化消息超出对应的频控规则限制，推送服务将向您的回执服务器返回**256结果码**，详情请参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

具体频控规则见下表：

| 场景 | 频控规则 |
| --- | --- |
| 通知消息 | 1.应用违规处罚时，按照处罚频次限制，参考[通知违规处罚标准](../harmonyos-guides/push-punishment-standards.md)。  2.消息为资讯营销类（[category](push-scenariozed-api-request-param.md#notification)取值为MARKETING）时，按照应用营销消息频次限制，参考[通知消息推送数量管理规则](../harmonyos-guides/push-apply-right.md#通知消息推送数量管理规则)（若未[开通消息自分类权益](../harmonyos-guides/push-send-alert.md#开通权益)，则推送的通知消息**默认为资讯营销类消息**）。 |
| 卡片刷新消息 | 按照应用下单个卡片限制刷新频次。  默认频次：应用每个设备单个卡片已上架为2条/天，未上架为5条/天。 |
| 实况窗消息 | 单个实况窗消息每个设备每5分钟最多更新10次，每小时最多更新60次。  出行打车与赛事比分场景，5分钟最多更新30次，每小时最多更新180次。 |

## 设备消息频控

除了单个场景的次数限制外，推送服务还对单个设备下的单个应用一天内所能接收的所有消息总量进行了限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控，并且推送服务将向您的回执服务器返回**102结果码**，详情请参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

## 测试消息频控

为了方便开发者测试消息，您可以设置pushOptions.[testMessage](push-scenariozed-api-request-param.md#pushoptions)为true，发送测试消息。

每个项目每日可推送总共1000条测试消息（非设备级，所有设备共用1000条）且不受[场景化消息频控](push-msg-freq-control.md#场景化消息频控)。若项目当天已推送超过1000条测试消息，则会进行消息限流（限流直到次日后恢复），并且推送服务将向您的回执服务器返回**256结果码**，详情请参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

## 消息推送速率管控

消息推送速率是指应用QPS（每秒推送的设备个数），当应用QPS超过阈值时请求会返回[HTTP响应码](push-scenariozed-api-response.md#http响应码) 503。应用QPS与应用类型相关，并且随着应用在华为终端上的月活跃用户人数增加而增长，您可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)查询到应用QPS阈值，查询路径：“开发与服务 > 推送服务 > 配置 > 选择应用”，选择需要查看的应用，下方即可查到对应的QPS阈值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Dv_4fbvdQuC2fppnlRJ_hg/zh-cn_image_0000002552801260.png?HW-CC-KV=V1&HW-CC-Date=20260428T001831Z&HW-CC-Expire=86400&HW-CC-Sign=1845E61C26C14DD9CD707927B3C1A2109CEA18A8F516AC31DAE76A1F8850EB29)

说明

全网流量较高时，会出现系统级流控，请求也会返回[HTTP响应码](push-scenariozed-api-response.md#http响应码) 503。
