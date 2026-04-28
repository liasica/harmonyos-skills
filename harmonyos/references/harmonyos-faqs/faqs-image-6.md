---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-6
title: 如何将相册选择的图片生成PixelMap
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将相册选择的图片生成PixelMap
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:30+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:9cda345eac02b61317498188ccfc0c8ae5f85bc3cb7580d9cb201fb56cf84e99
---

方法一：

1. 创建图库选择器实例，调用select()接口拉起photoPicker界面选择图片。选择成功后，返回PhotoSelectResult结果集。
2. 通过photoAccessHelper模块的getAssets接口获取媒体文件的URI。
3. 调用getThumbnail获取缩略图。

参考代码如下：

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { dataSharePredicates } from '@kit.ArkData';
4. import { common } from '@kit.AbilityKit';

6. const context = AppStorage.get("context") as common.UIAbilityContext;
7. @Entry
8. @Component
9. struct WebComponent {
10. build() {
11. Column() {
12. Button('选择图片').onClick(() => {
13. try {
14. let uris: Array<string> = [];
15. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
16. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
17. PhotoSelectOptions.maxSelectNumber = 1;
18. let photoPicker = new photoAccessHelper.PhotoViewPicker();
19. photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
20. console.info('photoPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
21. uris = PhotoSelectResult.photoUris;
22. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
23. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
24. // Configure query conditions, use PhotoViewPicker to select the URI of the image to be queried
25. predicates.equalTo('uri', uris[0]);
26. let fetchOptions: photoAccessHelper.FetchOptions = {
27. fetchColumns: [],
28. predicates: predicates
29. };
30. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
31. if (fetchResult !== undefined) {
32. console.info('fetchResult success');
33. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
34. if (photoAsset !== undefined) {
35. // Get Thumbnail
36. photoAsset.getThumbnail((err, pixelMap) => {
37. if (err == undefined) {
38. console.info('getThumbnail successful ' + JSON.stringify(pixelMap));
39. } else {
40. console.error('getThumbnail fail', err);
41. }
42. });
43. console.info('photoAsset.displayName : ' + photoAsset.displayName);
44. }
45. } else {
46. console.error(`fetchResult fail with error: ${err.code}, ${err.message}`);
47. }
48. });
49. }).catch((err: BusinessError) => {
50. console.error('photoPicker.select failed with err: ' + JSON.stringify(err));
51. });
52. } catch (error) {
53. let err: BusinessError = error as BusinessError;
54. console.error('photoPicker failed with err: ' + JSON.stringify(err));
55. }
56. })
57. }
58. }
59. }
```

[SelectedAlbumPictureGeneratePixelMap\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/SelectedAlbumPictureGeneratePixelMap_One.ets#L21-L79)

方法二：

1. 创建图库选择器实例，调用select()接口拉起photoPicker界面进行图片选择。图片选择成功后，返回PhotoSelectResult结果集。

1. 待界面从图库返回后，使用 fileIo.openSync 接口通过 URI 打开文件并获取文件描述符（fd）。注意，接口的权限参数应设置为 fileIo.OpenMode.READ\_ONLY。
2. 通过 image 使用 image.createImageSource 接口创建图片源实例。
3. 根据 imageSource 创建 pixelMap。

参考代码如下：

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';
4. import { fileIo } from '@kit.CoreFileKit';

6. @Entry
7. @Component
8. struct WebComponent {
9. build() {
10. Column() {
11. Button('Select Picture').onClick(() => {
12. try {
13. let uris: Array<string> = [];
14. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
15. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
16. PhotoSelectOptions.maxSelectNumber = 1;
17. let photoPicker = new photoAccessHelper.PhotoViewPicker();
18. photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
19. uris = PhotoSelectResult.photoUris;
20. let file = fileIo.openSync(uris[0], fileIo.OpenMode.READ_ONLY);
21. console.info('file fd: ' + file.fd);
22. let buffer = new ArrayBuffer(4096);
23. let readLen = fileIo.readSync(file.fd, buffer);
24. console.info('readSync data to file succeed and buffer size is:' + readLen);
25. const imageSource: image.ImageSource = image.createImageSource(file.fd);
26. let decodingOptions: image.DecodingOptions = {
27. editable: true,
28. desiredPixelFormat: 3,
29. }
30. imageSource.createPixelMap(decodingOptions, (err: BusinessError, pixelMap: image.PixelMap) => {
31. if (err !== undefined) {
32. console.error(`Failed to create pixelMap.code is ${err.code},message is ${err.message}`);
33. } else {
34. console.info('Succeeded in creating pixelMap object.');
35. }
36. })
37. }).catch((err: BusinessError) => {
38. console.error(`Invoke photoPicker.select failed, code is ${err.code}, message is ${err.message}`);
39. })
40. } catch (error) {
41. let err: BusinessError = error as BusinessError;
42. console.error('photoPicker failed with err: ' + JSON.stringify(err));
43. }
44. })
45. }
46. }
47. }
```

[SelectedAlbumPictureGeneratePixelMap\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/SelectedAlbumPictureGeneratePixelMap_Two.ets#L21-L67)
