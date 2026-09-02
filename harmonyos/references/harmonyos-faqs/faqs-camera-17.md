---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-17
title: 视频预览分辨率设置
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 视频预览分辨率设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:446301b5e528683bc247b7f129395a7f55c223a4208fe5190f4dfcc80ef0f924
---

## 问题现象

旋转手机，预览画面中物品高度变化明显，画面畸变。代码中的预览分辨率：previewProfile {"format":1003,"size":{"width":3200,"height":2400}}，XComponent的surfaceWidth: 3200, surfaceHeight: 2400。

```ts
XComponent({
  id: 'componentId',
  type: 'surface',
  controller: this.mXComponentController,
}).onLoad(async () => {
  this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
  let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
  await this.initCamera(baseContext, this.surfaceId)
}).width('100%')
  .height('100%')
```

## 可能原因

XComponent宽高比设置不当。

## 解决措施

请确保.width('100%').height('100%')的值不都设置为100%，并保持width和height的比例与previewProfile的height与width比例一致。
