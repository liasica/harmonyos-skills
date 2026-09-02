---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-msg-freq-control
title: 消息频控
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息推送 > 消息频控
category: harmonyos-references
scraped_at: 2026-09-02T15:03:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e90134a540c50771ec184471f93c22c5efd114b74fd44a4c1b27b386e41f98fb
---

Push Kit消息频控包括场景化消息频控、设备消息频控、测试消息频控和消息推送速率管控，当超过了某个频控规则限制会返回对应的[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

**说明** 

消息频控的数量是指应用发起消息推送请求的数量，无论设备是否成功展示消息都会增加计数，如果消息未按预期展示，建议不要频繁发起消息推送请求，请先进行[问题排查](../harmonyos-guides/push-faq-2.md)。

## 场景化消息频控

为了给用户提供更好的体验，营造清朗网络空间，华为Push Kit根据不同的[推送场景](../harmonyos-guides/push-scenes-send.md)，设置了多条频控规则。

若场景化消息超出对应的频控规则限制，Push Kit将向您的回执服务器返回**256结果码**，详情请参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

具体频控规则见下表：

| 场景 | 频控规则 |
| --- | --- |
| 通知消息 | 1.应用违规处罚时，按照处罚频次限制，参考[通知违规处罚标准](../harmonyos-guides/push-punishment-standards.md)。  2.消息为资讯营销类（[category](push-scenariozed-api-request-param.md#notification)取值为MARKETING）时，按照应用营销消息频次限制，参考[通知消息推送数量管理规则](../harmonyos-guides/push-apply-right.md#通知消息推送数量管理规则)（若未[开通消息自分类权益](../harmonyos-guides/push-send-alert.md#开通权益)，则推送的通知消息**默认为资讯营销类消息**）。 |
| 卡片刷新消息 | 按照应用下单个卡片限制刷新频次。  单张服务卡片刷新消息数量按[华为应用市场应用分类示例](../app/classify-1.md)划分，具体频控规则请参考[ArkTS卡片Push刷新](../harmonyos-guides/arkts-ui-widget-update-by-push.md)。 |
| 实况窗消息 | 单个实况窗消息每个设备每5分钟最多更新10次，每小时最多更新60次。  出行打车与赛事比分场景，5分钟最多更新30次，每小时最多更新180次。 |

## 设备消息频控

除了单个场景的次数限制外，Push Kit还对单个设备下的单个应用一天内所能接收的所有消息总量进行了限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控，并且Push Kit将向您的回执服务器返回**102结果码**，详情请参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

## 测试消息频控

为了方便开发者测试消息，您可以设置pushOptions.[testMessage](push-scenariozed-api-request-param.md#pushoptions)为true，发送测试消息。

每个项目每日可推送总共1000条测试消息（非设备级，所有设备共用1000条）且不受[场景化消息频控](push-msg-freq-control.md#场景化消息频控)。若项目当天已推送超过1000条测试消息，则会进行消息限流（限流直到次日后恢复），并且Push Kit将向您的回执服务器返回**256结果码**，详情请参考[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。

## 消息推送速率管控

消息推送速率是指应用QPS（每秒推送的设备个数），当应用QPS超过阈值时请求会返回[HTTP响应码](push-scenariozed-api-response.md#http响应码) 503。应用QPS与应用类型相关，并且随着应用在华为终端上的月活跃用户人数增加而增长，您可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)查询到应用QPS阈值，查询路径：“开发与服务 > 推送服务 > 配置 > 选择应用”，选择需要查看的应用，下方即可查到对应的QPS阈值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NiN-6YVpTnWgFkknWWnKig/zh-cn_image_0000002736436275.png)

**说明** 

全网流量较高时，会出现系统级流控，请求也会返回[HTTP响应码](push-scenariozed-api-response.md#http响应码) 503。
