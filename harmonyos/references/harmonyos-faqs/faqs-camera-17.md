---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-17
title: 视频预览分辨率设置
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 视频预览分辨率设置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee0d168c52513d3621499dbdd555cd50404dbf6d49d57b19cb9d7880cc0ddd5f
---

**问题现象**

旋转手机，预览画面中物品高度变化明显，画面畸变。代码中的预览分辨率：previewProfile {"format":1003,"size":{"width":3200,"height":2400}}，XComponent的surfaceWidth: 3200, surfaceHeight: 2400。

```
1. XComponent({
2. id: 'componentId',
3. type: 'surface',
4. controller: this.mXComponentController,
5. }).onLoad(async () => {
6. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
7. let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
8. await this.initCamera(baseContext, this.surfaceId)
9. }).width('100%')
10. .height('100%')
```

[SetVideoPreviewResolution.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/SetVideoPreviewResolution.ets#L32-L41)

**可能原因**

XComponent宽高比设置不当。

**解决措施**

请确保.width('100%').height('100%')的值不都设置为100%，并保持width和height的比例与previewProfile的height与width比例一致。
