---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-introduction
title: AppGallery Kit简介
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ce7ad9f11f70d371cffa7a3c099651c1e60c5977c8e34fa4abe8e62616d852f
---

AppGallery Kit（应用市场服务）提供应用市场业务的对外开放能力，可以更好地支持应用的下载、推荐和分发等场景以提高在应用市场上的曝光度，以及为开发者提供便捷高效的数字商品服务的接入流程和交互体验，助力开发者商业变现。

使用AppGallery Kit为您的应用和应用内数字商品提供以下功能和服务：

**[数字商品服务](store-iap-introduction.md)**：指华为为开发者的数字商品的管理、交易、售后提供的平台能力和服务，助力您实现数字商品交易和结算。

**[应用市场推荐](store-productview.md)**：用户可直达您的应用市场详情页或卡片加桌页面，有效提高您的应用曝光率。

**[产品特性按需分发](store-moduleinstall_arkts.md)**：实现应用多子业务独立演进，能够提供动态分发和资源拆分，帮助提高分发效率。

**[生态查询服务](store-erms.md)**：您可查询您的元服务/应用是通过何种场景被打开的，您还可基于场景值，做更多的业务设计和拓展。

**[应用市场更新功能](store-update.md)**：您可以通过本服务查询应用是否有可更新的版本。当存在可更新版本时，可为用户在应用内显示更新提醒。

**[应用归因服务](store-attribution-introduction.md)**：您可通过本服务判断用户下载应用和使用应用的原因，借助归因数据分析营销效果，评估多渠道商业价值和优化商业策略。

**[隐私管理服务](store-privacy.md)**：为用户提供统一隐私弹框，您可通过本服务查询隐私链接、隐私签署状态、撤销用户已同意签署的隐私协议记录。

**[图标管理服务](appgallery-appinfo-manage.md)**：您可以通过本服务管理动态图标，包括查询可选动态图标、切换动态图标、恢复默认图标。

**[应用评论服务](appgallery-comment.md)**：您可以通过本服务对应用进行评论，在应用内拉起应用评分弹窗。

## 约束和限制

### 支持的设备

| 能力 | 支持设备 |
| --- | --- |
| 数字商品服务 | [支持的设备](iap-introduction.md#支持的设备)。 |
| 应用市场推荐 | 支持Phone、PC/2in1、Tablet、TV。 |
| 产品特性按需分发 | 支持Phone、PC/2in1、Tablet、TV。 |
| 生态查询服务 | 支持Phone、PC/2in1、Tablet、TV。 |
| 应用市场更新功能 | 支持Phone、PC/2in1、Tablet、Wearable、TV。 |
| 应用归因服务 | 支持Phone、PC/2in1、Tablet、TV。 |
| 隐私管理服务 | 支持Phone、PC/2in1、Tablet、TV。 |
| 图标管理服务 | 支持Phone、PC/2in1、Tablet、Wearable、TV。 |
| 应用评论服务 | 支持Phone、PC/2in1、Tablet。 |

### 支持的国家/地区

| 能力 | 支持的国家/地区 |
| --- | --- |
| 数字商品服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 应用市场推荐 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 产品特性按需分发 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 生态查询服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 应用归因服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 隐私管理服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 应用评论服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 应用市场更新功能 | 请参见[支持的国家/地区](appgallery-support-regions.md)。 |
| 图标管理服务 | 请参见[支持的国家/地区](appgallery-support-regions.md)。 |

## 模拟器支持情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下：

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 不支持数字商品服务、应用市场推荐、生态查询服务、应用市场更新功能、应用评论服务、图标管理服务，不支持端云交互。

## 示例代码

该指南涉及到的示例代码均为片段，全量示例代码请参考：[Samplecode](https://gitcode.com/HarmonyOS_Samples/appgallerykit-samplecode-clientdemo-arkts)。
