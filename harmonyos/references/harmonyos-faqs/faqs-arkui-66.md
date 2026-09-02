---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-66
title: 如何监听屏幕旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何监听屏幕旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:414681a0d2d0d75f0149a37be8fe5b43f493a4f55a7f2ad487f51831fa620698
---

可以使用媒体查询接口监听屏幕旋转。参考代码如下：

```ts
import { mediaquery, UIContext } from '@kit.ArkUI';
const context = AppStorage.get("context") as UIContext;
let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen for landscape screen events
function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // Register callback
listener.off('change', onPortrait) // Unregister callback
```

**参考链接**

[@ohos.mediaquery (媒体查询)](../harmonyos-references/js-apis-mediaquery.md)
