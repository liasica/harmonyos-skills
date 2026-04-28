---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-146
title: 如何获取图片的宽高
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取图片的宽高
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:41b56bd5f60e32603ad9a8928ed2179848b082ec9cd8c580aef7b09434c3764e
---

通过Image组件的[onComplete](../harmonyos-references/ts-basic-components-image.md#oncomplete)事件，图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。参考代码如下：

```
1. Image($r('app.media.startIcon'))
2. .width(200)
3. .height(200)
4. .objectFit(ImageFit.Contain)
5. .onComplete((event) => {
6. let imageWidth = event?.width;
7. let imageHeight = event?.height;
8. console.info('imageWidth:'+imageWidth,'imageHeight:'+imageHeight);
9. })
```

[ObtainTheWidthAndHeightOfTheImage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ObtainTheWidthAndHeightOfTheImage.ets#L24-L32)

**参考链接**

[Image](../harmonyos-references/ts-basic-components-image.md)
