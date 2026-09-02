---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-129
title: UI布局默认是多少vp为基准，以达到不同机器自适应
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > UI布局默认是多少vp为基准，以达到不同机器自适应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a3b37c9bff9a3ecf807dbe3441c44944f93e4438bbf5b0152ed3beff656ad8c1
---

无论屏幕分辨率或密度如何，组件的视觉效果保持一致。

vp具体计算公式为：vp= px/(DPI/160)

px 是屏幕的真实物理像素值，densityDPI 通常指系统屏幕密度，densityPixels是屏幕密度与标准DPI的比率，常见取值有 0.75、1.0、1.5、2.0、3.0 等。在HarmonyOS中，标准DPI为160。以华为Mate 40 Pro为例，densityDPI为 560，densityPixels为3.5。要查看真机的DPI，可以调用屏幕属性中的display接口查询。

```typescript
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
} catch (exception) {
  console.error('Failed to obtain the default display object. Code: ' + JSON.stringify(exception));
}
```

如果原型图没有提供vp单位的布局，开发者可以根据densityPixels把px转为vp，HarmonyOS也封装了现成的接口[px2vp()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)和[vp2px()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)供开发者直接调用。

**参考链接**

[像素单位](../harmonyos-references/ts-pixel-units.md)，[@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)
