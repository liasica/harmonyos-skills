---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ads-4
title: 如何解决开屏广告未生效
breadcrumb: FAQ > 应用服务开发 > 广告变现服务（Ads Kit） > 如何解决开屏广告未生效
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ec1d03a31df0382f317de92a3290cd5d8ef9f352641aff801e63d1f70a5c11ec
---

## 问题现象

应用上架成功后，开屏广告未生效。

## 背景知识

[开屏广告](../harmonyos-guides/ads-publisher-service-splash.md)是一种在应用启动时且在应用主界面显示之前需要被展示的广告。需要预先为App设计一张开屏默认的Slogan图片，确保在未获得开屏广告之前展示默认的Slogan，提供良好的用户体验。开屏广告分为全屏开屏广告、半屏开屏广告，其中全屏开屏广告展示形式为广告铺满整个页面；半屏开屏广告展示形式会根据媒体页面自定义布局渲染广告、icon和版权信息，一般情况下建议将icon和版权信息展示在广告下方。

## 解决方案

如果应用在HarmonyOS系统上架并且已经通过审核，但是开屏广告并未生效，有以下几个原因：

1. 如果媒体状态显示为“未启用”，需要确保在后台管理系统中激活了相关的广告设置。
2. 用户协议未同意：[鲸鸿动能平台](../promotion/ads_toufang01-0000001057732432.md)提示用户需要同意用户协议后，广告才会开始推送。确保开发者在用户首次启动应用时引导完成了这一步骤。可参考案例设置：[广告服务demo。](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_AdsKit-Splash-ArkTS)
3. 开屏广告已启用但未进行测试验收。开屏广告正式ID开发者在后台置为已启用状态，但仍然无法请求展示广告的，需要在互动中心联系广告支持人员进行验收，需要广告侧使用测试ID验收通过后，联系广告运营进行配置+加入版位，此时广告正式ID才能正常请求返回并展示广告。详情可以看参考：[测试验证及上线。](../monetize/ceshiyanzhengjishangxian-0000001085219714.md#section1252511599306)

   **说明** 

   测试开屏广告时，需要使用专门的**测试广告位ID**来获取测试广告，以避免在测试过程中产生无效的广告点击量。测试广告位ID仅作为功能调试使用，不可用于广告变现。另外，如果排查完毕并非广告接入问题，而是正常的广告未填充，则可以先提供具体原因到互动中心，进行申诉，若申诉通过，那么可以重新提交上架，并备注中注明情况和互动中心工单号；若未申诉通过，则需要进行修改。
