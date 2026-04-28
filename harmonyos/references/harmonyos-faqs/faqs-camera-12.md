---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-12
title: 如何避免预览流产生畸变
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何避免预览流产生畸变
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e76b8651135c38c9ef0c5276f2b1a46992af00e48c2df48aeaea8b477761da00
---

使用下列代码获取设备支持的宽和高，然后根据手机屏幕的宽高设置最合适的预览流分辨率，并使surface和XComponent的宽高一致。

```
1. //The aspect ratio of the preview stream and the video output stream resolution should be consistent
2. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;

4. let position: number = 0;
5. if (previewProfilesArray != null) {
6. previewProfilesArray.forEach((value: camera.Profile,index: number) => {
7. // View supported preview sizes
8. console.info(TAG,
9. `支持的预览尺寸: [${value.size.width},${value.size.height},${value.size.width / value.size.height}]`);
10. if (value.size.width === 2592 && value.size.height === 1200) {
11. position = index;
12. }
13. })
14. } else {
15. console.error(TAG,"createOutput photoProfilesArray == null || undefined");
16. }

18. let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
19. if (!photoProfilesArray) {
20. console.error(TAG,"createOutput photoProfilesArray == null || undefined");
21. }

23. this.xComponentWidth = previewProfilesArray[position].size.width;
24. this.xComponentHeight = previewProfilesArray[position].size.height;

26. this.mXComponentController.setXComponentSurfaceSize({
27. surfaceWidth: this.xComponentWidth,
28. surfaceHeight: this.xComponentHeight
29. });
30. // Create a preview output stream, where the parameter surfaceId refers to the XComponent component mentioned earlier,
31. // and the preview stream is the surface provided by the XComponent component
32. try {
33. previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[position],surfaceId);
34. } catch (error) {
35. let err = error as BusinessError;
36. console.error(TAG,`Failed to create the PreviewOutput instance. error code: ${err.code}`);
37. }
38. if (previewOutput === undefined) {
39. return;
40. }

42. // Monitor preview output error message
43. previewOutput.on('error',(error: BusinessError) => {
44. console.error(TAG,`Preview output error code: ${error.code}`);
45. });

47. // Create an ImageReceiver object and set photo parameters:
48. // The resolution size is set based on the current device's supported photo resolution size obtained from the previous photoProfilesArray
49. let size: image.Size = {
50. height: 1200,
51. width: 2592
52. }
53. let imageReceiver: image.ImageReceiver = image.createImageReceiver(size,4,8);
```

[AvoidDistortion.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/AvoidDistortion.ets#L41-L93)
