---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-introduction
title: IAP Kit简介
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:84b659aaac257eb42286bc534c5e208c1c1dd6cd22f667fc1a39612b724fbe4f
---

IAP Kit（应用内支付服务）为开发者提供便捷的应用内支付体验和简便的接入流程，让开发者聚焦应用本身的业务能力，助力开发者商业变现。开发者应用可通过使用IAP Kit提供的系统级支付API快速启动IAP收银台，即可实现应用内支付。

通过IAP Kit，用户可以在应用内购买各种类型的**数字商品（虚拟商品）** ，包括消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。

| 商品类型 | 定义 | 用户权益时间 | 开发者权益处理 | 场景举例 |
| --- | --- | --- | --- | --- |
| 消耗型商品 | 使用一次后即消耗掉，随使用减少，需要再次购买的商品 | 无限制 | 开发者发放权益后，后续不再进行管理 | 游戏货币，游戏道具等 |
| 非消耗型商品 | 一次性购买，永久拥有，无需消耗 | 永久 | 开发者永久维护用户权益 | 游戏中额外的游戏关卡、应用中无时限的高级会员等 |
| 自动续期订阅商品 | 用户购买后在一段时间内允许访问增值功能或内容，周期结束前自动续期购买下一期的服务 | 连续性周期 | 开发者周期性维护用户权益 | 应用中有时限的自动续期高级会员，如：视频连续包月会员 |
| 非续期订阅商品 | 用户购买后在一段时间内允许访问增值功能或内容，周期结束后禁止访问，除非再次购买自动续期订阅或非续期订阅商品 | 一个周期 | 开发者在一个周期内要进行权益维护 | 应用中有时限的高级会员，如：视频一个月会员 |

## 约束与限制

### 支持的设备

说明

[华为IAP范围覆盖](iap-appendix-coverage.md)中的国家/地区（不包括中国境内（香港特别行政区、澳门特别行政区、中国台湾除外））仅支持Wearable设备。

中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）：

| 商品类型 | 支持设备 |
| --- | --- |
| 消耗型商品 | Phone、PC/2in1、Tablet、Wearable、TV |
| 非消耗型商品 | Phone、PC/2in1、Tablet、Wearable、TV |
| 自动续期订阅商品 | Phone、PC/2in1、Tablet、TV |
| 非续期订阅商品 | Phone、PC/2in1、Tablet、TV |

从6.1.0（23）开始，提供了IAP嵌入式收银台组件。

| IAP Kit提供的能力 | 支持设备 |
| --- | --- |
| [IAP嵌入式收银台组件](../harmonyos-references/iap-cashier-component.md) | TV |

在TV设备拉起支付收银台页面为扫码支付页，参考示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Q3H-hw3UTICVXEnAQZLQag/zh-cn_image_0000002583478921.png?HW-CC-KV=V1&HW-CC-Date=20260427T234922Z&HW-CC-Expire=86400&HW-CC-Sign=0ADEC29F60CDA3DD92967DB1322A82F2F94CB9F1CD1255AB2D59EA176A662C3D)

### 支持的国家/地区

由于IAP Kit支持的国家/地区和设备类型相关，具体请参见[支持的设备](iap-introduction.md#支持的设备)。

## 模拟器支持情况

本Kit暂不支持模拟器。
