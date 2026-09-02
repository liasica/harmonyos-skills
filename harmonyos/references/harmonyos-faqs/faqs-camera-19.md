---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-19
title: 如何实现拍照预览onPreviewFrame回调
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现拍照预览onPreviewFrame回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:183a67a2df4924aea62455348cbaf75f1488cf9635ff282c0342da87a54dc4d2
---

使用双路预览实现onPreviewFrame回调，设置previewOutput2接收连续数据，示例代码如下，在示例代码中保存接收到的前三帧数据，也可以通过业务需要调整：

```ts
this.previewOutput = this.cameraManager!.createPreviewOutput(previewProfilesArray[5], surfaceId);
let size: image.Size = {
  width: 640,
  height: 480
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
receiver.on('imageArrival', () => {
  receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
    if (err || nextImage === undefined) {
      console.error('readNextImage failed');
      return;
    }
    nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error('getComponent failed');
      }
      if (imgComponent && imgComponent.byteBuffer as ArrayBuffer && this.count<3) {
        this.count = this.count + 1
        let path: string = context.filesDir + "/image.yuv";
        let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
        let opt: WriteOptions = {
          // 2048 extra bytes of data
          length: imgComponent.byteBuffer.byteLength - 2048
        }
        fileIo.write(file.fd, imgComponent.byteBuffer, opt).then((writeLen) => {
          console.info("write data to file succeed and size is:" + writeLen);
          fileIo.closeSync(file);
        }).catch((err: BusinessError) => {
          console.info("write data to file failed with error message: " + err.message + ", error code: " + err.code);
        });
      }
      nextImage.release();
    })
  })
})
let ImageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
this.previewOutput2 = this.cameraManager!.createPreviewOutput(previewProfilesArray[5], ImageReceiverSurfaceId);
```
