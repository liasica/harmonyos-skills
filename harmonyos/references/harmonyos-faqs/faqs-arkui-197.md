---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-197
title: 如何监听窗口大小的变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听窗口大小的变化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b2e3c6461600aed94d5730ee540a5af58905bf5b98149de78ea3ff765d7d453e
---

**问题现象**

监听窗口大小的变化。

**解决措施**

获取窗口实例对象后，可以通过[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口尺寸大小变化的监听。

需要注意的是，在window侧如果窗口大小没发生变化，此监听不会被触发。如直接旋转180度的情况下，窗口大小并没有改变，此时不会通知回调。在这种情况下，应用可以通过监听display.on('change')事件，在callback中通过display接口来获取窗口尺寸大小。

```
1. try {
2. windowClass.on('windowSizeChange', (data) => {
3. console.info('Succeeded in enabling the listener for window size changes. Data: ' + JSON.stringify(data));
4. });
5. } catch (exception) {
6. console.error('Failed to enable the listener for window size changes. Cause: ' + JSON.stringify(exception));
7. }
```

[EntryAbilityMonitorChangesWindowSize.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityMonitorChangesWindowSize.ets#L40-L46)

**参考链接**

[display.on('add'|'remove'|'change')](../harmonyos-references/js-apis-display.md#displayonaddremovechange)
