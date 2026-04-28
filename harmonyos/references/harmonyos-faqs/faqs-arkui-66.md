---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-66
title: 如何监听屏幕旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听屏幕旋转
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dd202404e59d2ceb01f2b51f198cb7c19aaf57409eb00c96d4115a58505a6bfa
---

可以使用媒体查询接口监听屏幕旋转。参考代码如下：

```
1. import { mediaquery, UIContext } from '@kit.ArkUI';
2. const context = AppStorage.get("context") as UIContext;
3. let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen for landscape screen events
4. function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
5. if (mediaQueryResult.matches) {
6. // do something here
7. } else {
8. // do something here
9. }
10. }
11. listener.on('change', onPortrait) // Register callback
12. listener.off('change', onPortrait) // Unregister callback
```

[ListenForScreenRotation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListenForScreenRotation.ets#L21-L32)

**参考链接**

[@ohos.mediaquery (媒体查询)](../harmonyos-references/js-apis-mediaquery.md)
