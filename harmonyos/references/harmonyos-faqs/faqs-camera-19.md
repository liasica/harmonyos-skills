---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-19
title: 如何实现拍照预览onPreviewFrame回调
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现拍照预览onPreviewFrame回调
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cf212595b91326c60be70ce53a2cf2cd950255c8ff3b8fae6dcc184923e2065b
---

使用双路预览实现onPreviewFrame回调，设置previewOutput2接收连续数据，示例代码如下，在示例代码中保存接收到的前三帧数据，也可以通过业务需要调整：

```
1. this.previewOutput = this.cameraManager!.createPreviewOutput(previewProfilesArray[5], surfaceId);
2. let size: image.Size = {
3. width: 640,
4. height: 480
5. }
6. let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
7. receiver.on('imageArrival', () => {
8. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
9. if (err || nextImage === undefined) {
10. console.error('readNextImage failed');
11. return;
12. }
13. nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
14. if (err || imgComponent === undefined) {
15. console.error('getComponent failed');
16. }
17. if (imgComponent && imgComponent.byteBuffer as ArrayBuffer && this.count<3) {
18. this.count = this.count + 1
19. let path: string = context.filesDir + "/image.yuv";
20. let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
21. let opt: WriteOptions = {
22. // 2048 extra bytes of data
23. length: imgComponent.byteBuffer.byteLength - 2048
24. }
25. fileIo.write(file.fd, imgComponent.byteBuffer, opt).then((writeLen) => {
26. console.info("write data to file succeed and size is:" + writeLen);
27. fileIo.closeSync(file);
28. }).catch((err: BusinessError) => {
29. console.info("write data to file failed with error message: " + err.message + ", error code: " + err.code);
30. });
31. }
32. nextImage.release();
33. })
34. })
35. })
36. let ImageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
37. this.previewOutput2 = this.cameraManager!.createPreviewOutput(previewProfilesArray[5], ImageReceiverSurfaceId);
```

[RealizePhotoPreview.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/RealizePhotoPreview.ets#L35-L71)
