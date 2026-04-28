---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-20
title: 如何将PixelMap保存到相册
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将PixelMap保存到相册
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cfdc29863557148142b107a8c39a3141f76957ab8c1e3c76f275991d2eaa00f1
---

PixelMap使用[imagePacker.packToFile()](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)的方法将ImageSource图片源编码后直接打包进文件。

**参考代码**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { image } from '@kit.ImageKit';
5. import { fileIo } from '@kit.CoreFileKit';

7. @Entry
8. @Component
9. struct SavePixelMapToAlbum {
10. @State saveButtonOptions: SaveButtonOptions = {
11. icon: SaveIconStyle.FULL_FILLED,
12. text: SaveDescription.SAVE,
13. buttonType: ButtonType.Capsule
14. };
15. @State pixel: image.PixelMap | undefined = undefined;
16. @State albumPath: string = '';
17. @State photoSize: number = 0;
18. private context: Context = this.getUIContext().getHostContext()!;

20. async aboutToAppear() {
21. const resourceMgr: resourceManager.ResourceManager = this.context.resourceManager;
22. // "beer.jpeg" is the name of the image file under the rawfile directory, which can be modified and used according to your own needs
23. const fileData: Uint8Array = await resourceMgr.getRawFileContent('beer.jpeg');
24. let buffer = new Uint8Array(fileData).buffer as object as ArrayBuffer;
25. let imageResource = image.createImageSource(buffer);
26. let opts: image.DecodingOptions = { editable: true };
27. this.pixel = await imageResource.createPixelMap(opts);
28. }

30. async savePixelMapToAlbum() {
31. // Obtain the save path of the album
32. let helper = photoAccessHelper.getPhotoAccessHelper(this.context);
33. let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpeg');
34. let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
35. let imagePackerApi = image.createImagePacker();
36. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };

38. imagePackerApi.packToFile(this.pixel, file.fd, packOpts, (err: BusinessError) => {
39. if (err) {
40. console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
41. } else {
42. console.info('Succeeded in packing the image to file.');
43. imagePackerApi.release((err: BusinessError) => {
44. if (err) {
45. console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
46. } else {
47. console.info('Succeeded in releasing the image source instance.');
48. fileIo.close(file.fd);
49. }
50. })
51. this.getUIContext().getPromptAction().showToast({ message: '已保存至相册！' });
52. }
53. })
54. }

56. build() {
57. Row() {
58. Column() {
59. Image(this.pixel)
60. .objectFit(ImageFit.None)
61. .height('30%')

63. SaveButton(this.saveButtonOptions)
64. .onClick(async (event, result: SaveButtonOnClickResult) => {
65. if (result === SaveButtonOnClickResult.SUCCESS) {
66. this.savePixelMapToAlbum();
67. }
68. })
69. }
70. .width('100%')
71. }
72. .height('100%')
73. }
74. }
```

[PixelMapSaveToAlbum.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/PixelMapSaveToAlbum.ets#L21-L94)
