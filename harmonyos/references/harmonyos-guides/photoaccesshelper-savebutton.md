---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-savebutton
title: 保存媒体库资源
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 保存媒体库资源
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:403dacf429c00a5427eea702b6919af675469e62f4b47d961d176f99863141e3
---

保存图片、视频等用户文件到图库时，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，应用可以通过[安全控件](photoaccesshelper-savebutton.md#使用安全控件保存媒体库资源)或[授权弹窗](photoaccesshelper-savebutton.md#使用弹窗授权保存媒体库资源)的方式，将用户指定的媒体资源保存到图库中。

注意

Media Library Kit提供图片和视频的管理能力，当需要读取和保存音频文件时，请使用[AudioViewPicker（音频选择器对象）](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)。

## 获取支持保存的资源格式

下面以获取支持保存的图片类型资源格式为例。

**开发步骤**

调用[phAccessHelper.getSupportedPhotoFormats](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getsupportedphotoformats18)接口获取支持保存的图片类型资源格式。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry({ routeName : 'Scene1' })
5. @Component
6. export struct Scene1 {
7. @State outputText: string = 'Supported formats:\n';

9. build() {
10. NavDestination() {
11. Column({ space: 20 }) {
12. // ...

14. Button('example')
15. .width('80%')
16. .height(50)
17. .fontSize(16)
18. .onClick(async () => {
19. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
20. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
21. this.outputText = await example(phAccessHelper);
22. })

24. // ...
25. }
26. .width('100%')
27. .height('100%')
28. }
29. .title('Supported Formats')
30. }
31. }

33. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<string> {
34. try {
35. let outputText = 'Supported formats:\n';
36. // The value 1 means the supported image formats, and 2 means the supported video formats.
37. let imageFormat = await phAccessHelper.getSupportedPhotoFormats(1);
38. let result = '';
39. for (let i = 0; i < imageFormat.length; i++) {
40. result += imageFormat[i];
41. if (i !== imageFormat.length - 1) {
42. result += ', ';
43. }
44. }
45. outputText += result;
46. console.info('getSupportedPhotoFormats success, data is ' + outputText);
47. return 'getSupportedPhotoFormats success, data is\n' + outputText;
48. } catch (error) {
49. console.error('getSupportedPhotoFormats failed, errCode is', error);
50. return 'getSupportedPhotoFormats failed, errCode is\n' + JSON.stringify(error);
51. }
52. }
```

[Scene1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SaveButtonSample/entry/src/main/ets/pages/Scene1.ets#L16-L93)

## 使用安全控件保存媒体库资源

安全控件的介绍可参考[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)。保存前可以通过调用[registerChange](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#registerchange)接口注册对默认URI（[DEFAULT\_PHOTO\_URI](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#defaultchangeuri)）的监听。资源保存成功后，根据接收到该资源的[NOTIFY\_ADD](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#notifytype)通知完成后续业务。

下面以使用安全控件创建一张图片资源为例。

**开发步骤**

1. 设置安全控件按钮属性。
2. 创建安全控件按钮。
3. 调用[registerChange](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#registerchange)接口注册对默认URI（[DEFAULT\_PHOTO\_URI](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#defaultchangeuri)）的监听。
4. 调用[MediaAssetChangeRequest.createImageAssetRequest](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#createimageassetrequest11)和[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口创建图片资源。
5. 调用[getAsset](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#getasset11)接口获取保存的资产，并获取资产URI。在接收到资产URI的[NOTIFY\_ADD](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#notifytype)通知后，完成后续业务。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';
3. import { dataSharePredicates } from '@kit.ArkData';
4. // ...
5. @Entry({ routeName : 'Scene2' })
6. @Component
7. export struct Scene2 {
8. @State statusMessage: string = '';
9. @State imageSource: string = '';
10. uriString: string = '';

12. saveButtonOptions: SaveButtonOptions = {
13. icon: SaveIconStyle.FULL_FILLED,
14. text: SaveDescription.SAVE_IMAGE,
15. buttonType: ButtonType.Capsule
16. }// Set properties of SaveButton.

18. // ...

20. onCallback = (changeData: photoAccessHelper.ChangeData) => {
21. for (let i = 0; i < changeData.uris.length; i++) {
22. // 保存媒体库资源成功后，会监听到类型为NOTIFY_ADD的资产URI。
23. if (changeData.uris[i] === this.uriString && changeData.type === photoAccessHelper.NotifyType.NOTIFY_ADD) {
24. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
25. predicates.equalTo(photoAccessHelper.PhotoKeys.URI, changeData.uris[i]);
26. let fetchOptions: photoAccessHelper.FetchOptions = {
27. fetchColumns: [],
28. predicates: predicates
29. };

31. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
32. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
33. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
34. if (fetchResult !== undefined) {
35. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
36. if (photoAsset !== undefined) {
37. console.info('getAssets successfully');
38. }
39. }
40. phAccessHelper.unRegisterChange(photoAccessHelper.DefaultChangeUri.DEFAULT_PHOTO_URI);
41. });
42. }
43. }
44. }

46. build() {
47. NavDestination() {
48. Column({ space: 20 }) {
49. // ...

51. SaveButton(this.saveButtonOptions) // Create a button with SaveButton.
52. .onClick(async (event, result: SaveButtonOnClickResult) => {
53. if (result == SaveButtonOnClickResult.SUCCESS) {
54. try {
55. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
56. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

58. // 注册默认监听
59. phAccessHelper.registerChange(
60. photoAccessHelper.DefaultChangeUri.DEFAULT_PHOTO_URI, true, this.onCallback);

62. // 需要确保fileUri对应的资源存在。
63. let fileUri = 'file://' + context.filesDir + '/test.jpg';
64. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
65. photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, fileUri);

67. await phAccessHelper.applyChanges(assetChangeRequest);

69. this.uriString = assetChangeRequest.getAsset().uri;
70. this.statusMessage = 'createAsset successfully, uri: ' + this.uriString;
71. console.info('createAsset successfully, uri: ' + this.uriString);
72. } catch (err) {
73. this.statusMessage = `create asset failed with error: ${err.code}, ${err.message}`;
74. console.error(`create asset failed with error: ${err.code}, ${err.message}`);
75. }
76. } else {
77. this.statusMessage = 'SaveButtonOnClickResult create asset failed';
78. console.error('SaveButtonOnClickResult create asset failed');
79. }
80. })

82. // ...
83. }
84. .width('100%')
85. .height('100%')
86. }
87. .title('SaveButton Example')
88. }
89. }
```

[Scene2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SaveButtonSample/entry/src/main/ets/pages/Scene2.ets#L16-L168)

除了上述通过fileUri从应用沙箱指定资源内容的方式，开发者还可以通过ArrayBuffer的方式添加资源内容，详情请参考[addResource](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#addresource11-1)接口。

## 使用弹窗授权保存媒体库资源

下面以弹窗授权的方式保存一张图片资源为例。

**开发步骤**

1. 指定待保存到媒体库的[应用文件](app-file-access.md)uri（需为应用沙箱路径）。
2. 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
3. 调用[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)，基于弹窗授权的方式获取的目标[媒体文件](user-file-uri-intro.md#媒体文件uri)uri。

   弹框需要显示应用名称，无法直接获取应用名称，依赖于配置项的label和icon，因此调用此接口时请确保module.json5文件中的abilities标签中配置了label和icon项。当传入uri为沙箱路径时，可正常保存图片/视频，但无界面预览。
4. 将应用沙箱的照片内容写入媒体库的目标URI。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';
3. import { fileIo } from '@kit.CoreFileKit';

5. // ...

7. async function example(
8. phAccessHelper: photoAccessHelper.PhotoAccessHelper,
9. context: common.UIAbilityContext
10. ): Promise<string> {
11. try {
12. // 指定要保存到应用程序沙盒目录中的图片的URI。
13. let srcFileUri = context.filesDir + '/test.jpg';
14. let srcFileUris: string[] = [
15. srcFileUri
16. ];
17. // 设置要保存的图片的参数：文件扩展名、图片类型、标题和子类型（后两者为可选）。
18. let photoCreationConfigs: photoAccessHelper.PhotoCreationConfig[] = [
19. {
20. title: 'test', // This parameter is optional.
21. fileNameExtension: 'jpg',
22. photoType: photoAccessHelper.PhotoType.IMAGE,
23. subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
24. }
25. ];

27. console.info('Source URI: ' + srcFileUri);
28. // 基于弹窗授权获取媒体库中的目标URI。
29. let desFileUris: string[] =
30. await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
31. console.info('Destination URIs: ' + JSON.stringify(desFileUris));
32. // 将图片从沙盒目录写入媒体库中的目标URI。
33. let desFile: fileIo.File = await fileIo.open(desFileUris[0], fileIo.OpenMode.WRITE_ONLY);
34. let srcFile: fileIo.File = await fileIo.open(srcFileUri, fileIo.OpenMode.READ_ONLY);
35. await fileIo.copyFile(srcFile.fd, desFile.fd);
36. fileIo.closeSync(srcFile);
37. fileIo.closeSync(desFile);
38. console.info('create asset by dialog successfully');
39. return 'create asset by dialog successfully';
40. } catch (err) {
41. console.error(`failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}`);
42. return `failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}`;
43. }
44. }
```

[Scene3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SaveButtonSample/entry/src/main/ets/pages/Scene3.ets#L16-L141)
