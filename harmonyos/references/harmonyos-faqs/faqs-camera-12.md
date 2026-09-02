---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-12
title: 如何避免预览流产生畸变
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何避免预览流产生畸变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cc029a026331286b7f4ef4e8b96bcc145bcd2301dcff79342a5ad9c1d614c81c
---

使用下列代码获取设备支持的宽和高，然后根据手机屏幕的宽高设置最合适的预览流分辨率，并使surface和XComponent的宽高一致。

```ts
//The aspect ratio of the preview stream and the video output stream resolution should be consistent
let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;

let position: number = 0;
if (previewProfilesArray != null) {
  previewProfilesArray.forEach((value: camera.Profile,index: number) => {
    // View supported preview sizes
    console.info(TAG,
      `支持的预览尺寸: [${value.size.width},${value.size.height},${value.size.width / value.size.height}]`);
    if (value.size.width === 2592 && value.size.height === 1200) {
      position = index;
    }
  })
} else {
  console.error(TAG,"createOutput photoProfilesArray == null || undefined");
}

let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
if (!photoProfilesArray) {
  console.error(TAG,"createOutput photoProfilesArray == null || undefined");
}

this.xComponentWidth = previewProfilesArray[position].size.width;
this.xComponentHeight = previewProfilesArray[position].size.height;

this.mXComponentController.setXComponentSurfaceSize({
  surfaceWidth: this.xComponentWidth,
  surfaceHeight: this.xComponentHeight
});
// Create a preview output stream, where the parameter surfaceId refers to the XComponent component mentioned earlier,
// and the preview stream is the surface provided by the XComponent component
try {
  previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[position],surfaceId);
} catch (error) {
  let err = error as BusinessError;
  console.error(TAG,`Failed to create the PreviewOutput instance. error code: ${err.code}`);
}
if (previewOutput === undefined) {
  return;
}

// Monitor preview output error message
previewOutput.on('error',(error: BusinessError) => {
  console.error(TAG,`Preview output error code: ${error.code}`);
});

// Create an ImageReceiver object and set photo parameters:
// The resolution size is set based on the current device's supported photo resolution size obtained from the previous photoProfilesArray
let size: image.Size = {
  height: 1200,
  width: 2592
}
let imageReceiver: image.ImageReceiver = image.createImageReceiver(size,4,8);
```
