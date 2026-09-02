---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ads-2
title: 激励广告回调中无法弹出Toast弹窗
breadcrumb: FAQ > 应用服务开发 > 广告变现服务（Ads Kit） > 激励广告回调中无法弹出Toast弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c97973a8eafa2411c43fe21444570b9e56af034274350facbb00773d3cba24aa
---

## 问题现象

激励广告的回调中无法弹出Toast窗口。关键代码如下：

```ts
case AdStatus.VIDEO_PLAY_END:
  hilog.info(0x0000, TAG, 'Status is onVideoPlayEnd');
  this.promptAction.showToast({
    message: 'reward ad end',
    duration: 2000,
    showMode:1
  });
  break;
```

## 背景知识

* [事件订阅](../harmonyos-guides/ads-publisher-service-reward.md#事件订阅)：开发者需要在App中订阅com.huawei.hms.pps.action.PPS\_REWARD\_STATUS\_CHANGED事件来监听激励广告页面变化并接收奖励信息，需要在每次展示广告前调用。
* [advertising.showAd](../harmonyos-references/js-apis-advertising.md#advertisingshowad)：展示全屏广告。
* 不安全窗口：包括非系统全局悬浮窗、宿主创建的非系统子窗口、宿主创建的非系统Dialog窗口。
* [模态UIExtension创建默认行为变更](../harmonyos-releases/changelogs-ux-b071.md#模态uiextension创建默认行为变更)：通过各个应用或者kit提供的开放能力创建出来的模态UIExtension，可能被三方应用组件或窗口遮挡，造成安全风险。

## 问题定位

1. 根据日志排查是否成功监听到了广告各状态：

   ```shell
   A00000/com.hua...StatusHandler  com.huawe...ientdemo  I     Status is onVideoPlayBegin
   A00000/com.hua...StatusHandler  com.huawe...ientdemo  I     Status is onVideoPlayEnd
   ```

   从以上日志中可以看到成功监听到广告。
2. 排查Toast弹窗是否符合UX要求。

## 分析结论

Toast弹窗为宿主创建的非系统子窗口，属于不安全窗口。advertising.showAd创建出来的是模态UIExtension，模态UIExtension不允许被不安全窗口遮挡。API 11之后拉起模态UIExtension时，会隐藏三方应用已创建的不安全窗口和组件，并阻止三方应用创建新的不安全窗口。

## 修改建议

可以在看完广告后，将广告弹窗移除，在原来的页面中弹出Toast弹窗。
