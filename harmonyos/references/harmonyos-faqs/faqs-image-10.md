---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-10
title: 如何读取相册中的图片
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何读取相册中的图片
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e7b830c58f16496bbe282b85624601f3b8fd9832cd397badefbf385fba7d49ca
---

使用photoAccessHelper.PhotoSelectOptions接口读取相册中的图片

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { image } from '@kit.ImageKit';
3. import { fileIo as fs } from '@kit.CoreFileKit';

5. @Entry
6. @Component
7. struct Index {
8. @State getAlbum: string = '显示相册中的图片';
9. @State pixel: image.PixelMap | undefined = undefined;
10. @State albumPath: string = '';
11. @State photoSize: number = 0;

13. async getPictureFromAlbum() {
14. // Pull up the album and select the pictures
15. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
16. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
17. PhotoSelectOptions.maxSelectNumber = 1;
18. let photoPicker = new photoAccessHelper.PhotoViewPicker();
19. let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
20. this.albumPath = photoSelectResult.photoUris[0];

22. // Read the image as a buffer
23. const file = fs.openSync(this.albumPath, fs.OpenMode.READ_ONLY);
24. this.photoSize = fs.statSync(file.fd).size;
25. console.info('Photo Size: ' + this.photoSize);
26. let buffer = new ArrayBuffer(this.photoSize);
27. fs.readSync(file.fd, buffer);
28. fs.closeSync(file);

30. // Decoding into PixelMap
31. const imageSource = image.createImageSource(buffer);
32. console.log('imageSource: ' + JSON.stringify(imageSource));
33. this.pixel = await imageSource.createPixelMap({});
34. }

36. build() {
37. Row() {
38. Column() {
39. Image(this.pixel)
40. .width('100%')
41. .aspectRatio(1)
42. Button('显示照片')
43. .onClick(() => {
44. this.getPictureFromAlbum();
45. })
46. }
47. .width('100%')
48. }
49. .height('100%')
50. }
51. }
```

[GetPhoto.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/GetPhoto.ets#L21-L71)
