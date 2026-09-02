---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-146
title: 如何获取图片的宽高
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取图片的宽高
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:347a8c8745aa5b4aabff1b281e280ff730c676bf62d4f3dd7fc013846f227a6e
---

通过Image组件的[onComplete](../harmonyos-references/ts-basic-components-image.md#oncomplete)事件，图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。参考代码如下：

```screen
Image($r('app.media.startIcon'))
  .width(200)
  .height(200)
  .objectFit(ImageFit.Contain)
  .onComplete((event) => {
    let imageWidth = event?.width;
    let imageHeight = event?.height;
    console.info('imageWidth:'+imageWidth,'imageHeight:'+imageHeight);
  })
```

**参考链接**

[Image](../harmonyos-references/ts-basic-components-image.md)
