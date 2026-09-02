---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ads-1
title: 如何解决华为开屏广告闪屏问题
breadcrumb: FAQ > 应用服务开发 > 广告变现服务（Ads Kit） > 如何解决华为开屏广告闪屏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b85eda74e939e80569559fe2e6da8f309cf328daccf6e4984f91a747fe805bf1
---

## 问题现象

展示华为开屏广告时出现闪屏问题，应该如何解决？

## 背景知识

* [开屏广告](../harmonyos-guides/ads-publisher-service-splash.md)是一种在应用启动时且在应用主界面显示之前需要被展示的广告。您需要预先为App设计一张开屏默认的Slogan图片，确保在未获得到开屏广告之前展示默认的Slogan，提供良好的用户体验。具体可参考：[广告服务代码示例](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_AdsKit-Splash-ArkTS)。
* [transition](../harmonyos-references/ts-transition-animation-component.md)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。可以通过[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)对象的组合使用，定义出各式效果。

## 解决方案

闪屏原因，是因为展示开屏广告前有一帧白色底，是广告加载前的加载过程。可以预先为App设计一张开屏默认的Slogan图片，确保在未获得到开屏广告之前展示默认的Slogan。

## 常见FAQ

Q：开屏广告功能，能自己实现吗？还是必须使用AdComponent？

A：可以自己实现。比如预置一个视频或开屏图片，再或者接入其他广告SDK，不是只能用AdComponent。

Q：开屏广告可以只请求全屏广告，不请求半屏广告吗？

A：全屏广告与半屏广告的类型区分，是由返回的[onAdLoadSuccess](../harmonyos-references/js-apis-advertising.md#onadloadsuccess)请求成功后回调中的isFullScreen参数决定的（true为全屏广告，false为半屏广告。）请求方无法事先知道是全屏类型还是半屏类型，不过可以在回调成功之后判断如果是半屏广告就不展示。
