---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-movingphoto
title: 访问和管理动态照片资源
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 动态照片 > 访问和管理动态照片资源
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:40c1707c8dd28b7832c11741592b82d3bb445baa6ac1bf0c53b349f30cd5a83f
---

动态照片是一种结合了图片和视频的照片形式，可以显示一小段时间的动态画面和声音。可以帮助用户捕捉精彩的动态瞬间，提升创作空间，同时令拍照的容错率更高。

媒体库提供访问和管理动态照片资源的能力，包括：

* [使用安全控件保存动态照片资源](photoaccesshelper-movingphoto.md#保存动态照片资源)
* [获取动态照片对象（MovingPhoto）](photoaccesshelper-movingphoto.md#获取动态照片对象)
* [使用MovingPhotoView播放动态照片](movingphotoview-guidelines.md)
* [读取动态照片资源](photoaccesshelper-movingphoto.md#读取动态照片资源)

拍摄动态照片的能力由Camera Kit提供，可参考[动态照片拍摄(ArkTS)](camera-moving-photo.md)。

## 保存动态照片资源

使用安全控件保存动态照片资源后，可用于获取MovingPhoto对象，从而完成播放动态照片等操作。

使用安全控件保存动态照片资源，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，允许用户通过点击按钮临时获取存储权限，并将资源直接保存到指定的媒体库路径，使得操作更为便捷。

详情请参考[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)。

**开发步骤**

1. 设置安全控件按钮属性。
2. 创建安全控件按钮。
3. 调用[MediaAssetChangeRequest.createAssetRequest](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#createassetrequest11)接口新建一个创建资产的变更请求，指定待创建资产的子类型为动态照片。
4. 调用[MediaAssetChangeRequest.addResource](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#addresource11)接口指定动态照片的图片和视频内容，动态照片的视频时长不能超过10s。

   以下示例以从应用沙箱的[应用文件](app-file-access.md)fileUri指定动态照片的图片和视频内容为例。

   开发者可根据实际情况，通过ArrayBuffer的方式指定资源内容，参考[MediaAssetChangeRequest.addResource(type: ResourceType, data: ArrayBuffer)](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#addresource11-1)。
5. 调用[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口提交创建资产的变更请求。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';
3. // ...

5. @Entry({ routeName : 'Scene1' })
6. @Component
7. export struct Scene1 {
8. @State statusMessage: string = '';
9. @State imageSource: string = '';

11. saveButtonOptions: SaveButtonOptions = {
12. icon: SaveIconStyle.FULL_FILLED,
13. text: SaveDescription.SAVE_IMAGE,
14. buttonType: ButtonType.Capsule
15. }// Set properties of SaveButton.

17. // ...

19. build() {
20. NavDestination() {
21. Column({ space: 20 }) {
22. // ...

24. SaveButton(this.saveButtonOptions) // Create a button with SaveButton.
25. .onClick(async (event, result: SaveButtonOnClickResult) => {
26. if (result == SaveButtonOnClickResult.SUCCESS) {
27. try {
28. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
29. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
30. // Ensure that the assets specified by imageFileUri and videoFileUri exist.
31. let imageFileUri = 'file://' + context.filesDir + '/create_moving_photo.jpg';
32. let videoFileUri = 'file://' + context.filesDir + '/create_moving_photo.mp4';

34. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
35. photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context,
36. photoAccessHelper.PhotoType.IMAGE, 'jpg', {
37. title: 'moving_photo',
38. subtype: photoAccessHelper.PhotoSubtype.MOVING_PHOTO
39. });

41. assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, imageFileUri);
42. assetChangeRequest.addResource(photoAccessHelper.ResourceType.VIDEO_RESOURCE, videoFileUri);

44. await phAccessHelper.applyChanges(assetChangeRequest);

46. this.statusMessage = 'create moving photo successfully, uri: ' + assetChangeRequest.getAsset().uri;
47. console.info('create moving photo successfully, uri: ' + assetChangeRequest.getAsset().uri);
48. } catch (err) {
49. this.statusMessage = `create moving photo failed with error: ${err.code}, ${err.message}`;
50. console.error(`create moving photo failed with error: ${err.code}, ${err.message}`);
51. }
52. } else {
53. this.statusMessage = 'SaveButtonOnClickResult create moving photo failed';
54. console.error('SaveButtonOnClickResult create moving photo failed');
55. }
56. })

58. // ...

60. }
61. .width('100%')
62. .height('100%')
63. }
64. .title('Save Moving Photo')
65. }
66. }
```

[Scene1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MovingPhotoSample/entry/src/main/ets/pages/Scene1.ets#L16-L156)

## 获取动态照片对象

* 应用可以通过Picker的方式获取用户媒体库里的动态照片对象，后续可用于在应用内播放动态照片，或是读取动态照片资源进行其他操作（如上传到应用共享给他人浏览等）。
* 应用也可以通过传入应用沙箱的[应用文件](app-file-access.md)图片和视频fileUri的方式构造应用本地的动态照片对象。

获取到动态照片对象后，如需播放动态照片请参考[使用MovingPhotoView播放动态照片](movingphotoview-guidelines.md)。

### 获取媒体库动态照片对象

1. 通过Picker选择动态照片的[媒体文件URI](user-file-uri-intro.md#媒体文件uri)。
2. 调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)和[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取URI对应的PhotoAsset资产。
3. 调用[MediaAssetManager.requestMovingPhoto](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#requestmovingphoto12)获取PhotoAsset对应的动态照片对象（MovingPhoto）。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { dataSharePredicates } from '@kit.ArkData';
3. import { common } from '@kit.AbilityKit';

6. @Entry({ routeName : 'Scene2' })
7. @Component
8. export struct Scene2 {

10. @State statusMessage: string = '';

12. build() {
13. NavDestination() {
14. Column({ space: 20 }) {

16. Button('example')
17. .width('80%')
18. .height(50)
19. .fontSize(16)
20. .onClick(async () => {
21. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
22. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
23. this.statusMessage = await example(phAccessHelper, context);
24. })

26. // ...
27. }
28. .width('100%')
29. .height('100%')
30. }
31. .title('Get from Media Library')
32. }
33. }
34. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context): Promise<string> {
35. try {
36. // Use Picker to select the URI of the moving photo.
37. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
38. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.MOVING_PHOTO_IMAGE_TYPE;
39. photoSelectOptions.maxSelectNumber = 9;
40. let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
41. let photoSelectResult = await photoViewPicker.select(photoSelectOptions);
42. let uris = photoSelectResult.photoUris;

44. let resultMessage = 'Selected ' + uris.length + ' moving photo(s)\n\n';

46. for (let i = 0; i < uris.length; i++) {
47. // Obtain the photo asset corresponding to the URI.
48. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
49. predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uris[i]);
50. let fetchOption: photoAccessHelper.FetchOptions = {
51. fetchColumns: [],
52. predicates: predicates
53. };
54. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
55. await phAccessHelper.getAssets(fetchOption);
56. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

58. let movingPhotoUri = await new Promise<string>((resolve) => {
59. // Obtain the moving photo object corresponding to the photo asset.
60. photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, photoAsset, {
61. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE
62. }, {
63. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
64. if (movingPhoto !== undefined) {
65. // Customize the logic for processing the moving photo.
66. console.info('request moving photo successfully, uri: ' + movingPhoto.getUri());
67. resolve(movingPhoto.getUri());
68. }
69. }
70. })
71. });

73. resultMessage += (i + 1) + '. request moving photo successfully, uri: ' + movingPhotoUri + '\n';
74. }

76. return resultMessage;
77. } catch (err) {
78. console.error(`request moving photo failed with error: ${err.code}, ${err.message}`);
79. return `request moving photo failed with error: ${err.code}, ${err.message}`;
80. }
81. }
```

[Scene2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MovingPhotoSample/entry/src/main/ets/pages/Scene2.ets#L1-L99)

### 获取应用沙箱动态照片对象

调用[MediaAssetManager.loadMovingPhoto](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#loadmovingphoto12)加载应用沙箱的动态照片对象（MovingPhoto）。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';
3. // ...
4. @Entry({ routeName : 'Scene3' })
5. @Component
6. export struct Scene3 {
7. @State statusMessage: string = '';
8. @State imageSource: string = '';

10. // ...
11. build() {
12. NavDestination() {
13. Column({ space: 20 }) {
14. // ...

16. Button('example')
17. .width('80%')
18. .height(50)
19. .fontSize(16)
20. .onClick(async () => {
21. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
22. this.statusMessage = await example(context);
23. })

25. // ...

27. }
28. .width('100%')
29. .height('100%')
30. }
31. .title('Load from Sandbox')
32. }
33. }

35. async function example(context: Context): Promise<string> {
36. try {
37. let imageFileUri = 'file://' + context.filesDir + '/local_moving_photo.jpg';
38. let videoFileUri = 'file://' + context.filesDir + '/local_moving_photo.mp4';
39. let movingPhoto = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
40. console.info('load moving photo successfully');
41. return 'load moving photo successfully';
42. } catch (err) {
43. console.error(`load moving photo failed with error: ${err.code}, ${err.message}`);
44. return `load moving photo failed with error: ${err.code}, ${err.message}`;
45. }
46. }
```

[Scene3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MovingPhotoSample/entry/src/main/ets/pages/Scene3.ets#L16-L137)

## 读取动态照片资源

对于一个动态照片对象，应用可以通过[MovingPhoto.requestContent](../harmonyos-references/arkts-apis-photoaccesshelper-movingphoto.md#requestcontent12)导出图片和视频到应用沙箱，或者读取图片或视频的ArrayBuffer内容。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';
3. // ...
4. @Entry({ routeName : 'Scene4' })
5. @Component
6. export struct Scene4 {
7. @State movingPhotoObj: photoAccessHelper.MovingPhoto | null = null;
8. @State statusMessage: string = '';
9. // ...

11. build() {
12. NavDestination() {
13. Column({ space: 20 }) {
14. // ...
15. Button('example')
16. .width('80%')
17. .height(50)
18. .fontSize(16)
19. .onClick(async () => {
20. if (this.movingPhotoObj) {
21. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
22. this.statusMessage = await example(this.movingPhotoObj, context);
23. } else {
24. this.statusMessage = 'Please prepare and load moving photo first!';
25. }
26. })
27. // ...
28. }
29. .width('100%')
30. .height('100%')
31. }
32. // ...
33. }
34. }

36. async function example(movingPhoto: photoAccessHelper.MovingPhoto, context: Context): Promise<string> {
37. try {
38. let imageFileUri = context.filesDir + '/request_moving_photo.jpg';
39. let videoFileUri = context.filesDir + '/request_moving_photo.mp4';
40. await movingPhoto.requestContent(imageFileUri, videoFileUri);
41. let imageData = await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE_RESOURCE);
42. let videoData = await movingPhoto.requestContent(photoAccessHelper.ResourceType.VIDEO_RESOURCE);

44. return 'Exported to:\n' + imageFileUri + '\n' + videoFileUri + '\n\nImage data size: ' + imageData.byteLength + ' bytes\nVideo data size: ' + videoData.byteLength + ' bytes';
45. } catch (err) {
46. console.error(`request content of moving photo failed with error: ${err.code}, ${err.message}`);
47. return `request content of moving photo failed with error: ${err.code}, ${err.message}`;
48. }
49. }
```

[Scene4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MovingPhotoSample/entry/src/main/ets/pages/Scene4.ets#L17-L148)
