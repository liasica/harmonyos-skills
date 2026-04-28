---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoeditorextensionability
title: 拉起图片编辑类应用（startAbilityByType）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起图片编辑类应用（startAbilityByType）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6639ca5392708beab7f7c2cb03a88890f6ed45df3a38948be24c2f876ec8b71f
---

## 使用场景

当应用自身不具备图片编辑能力、但存在图片编辑的场景时，可以通过startAbilityByType拉起图片编辑类应用扩展面板，由对应的应用完成图片编辑操作。图片编辑类应用可以通过PhotoEditorExtensionAbility实现图片编辑页面，并将该页面注册到图片编辑面板，从而将图片编辑能力开放给其他应用。

流程示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/WUYlW7LSQgm_K6IOtXtoEw/zh-cn_image_0000002583477509.png?HW-CC-KV=V1&HW-CC-Date=20260427T233751Z&HW-CC-Expire=86400&HW-CC-Sign=01172C2D275615CEE39BC0F3A83A4B09B727915248334424F247DFCCEB749F4B)

例如：用户在图库App中选择编辑图片时，图库App可以通过startAbilityByType拉起图片编辑类应用扩展面板。用户可以从已实现PhotoEditorExtensionAbility应用中选择一款，并进行图片编辑。

## 接口说明

接口详情参见[PhotoEditorExtensionAbility](../harmonyos-references/js-apis-app-ability-photoeditorextensionability.md)和[PhotoEditorExtensionContext](../harmonyos-references/js-apis-app-ability-photoeditorextensioncontext.md)。

| **接口名** | **描述** |
| --- | --- |
| onStartContentEditing(uri: string, want:Want, session: UIExtensionContentSession):void | 可以执行读取原始图片、加载页面等操作。 |
| saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult> | 传入编辑过的图片的PixelMap对象并保存。 |

## 图片编辑类应用实现图片编辑页面

1. 在DevEco Studio工程中手动新建一个PhotoEditorExtensionAbility。

   1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，如PhotoEditorExtensionAbility。
   2. 在PhotoEditorExtensionAbility目录中，右键选择“New > File”，新建一个.ets文件，如ExamplePhotoEditorAbility.ets。
2. 在ExamplePhotoEditorAbility.ets中重写onCreate、onForeground、onBackground、onDestroy和onStartContentEditing的生命周期回调。

   其中，需要在onStartContentEditing中加载入口页面文件pages/Index.ets，并将session、uri、实例对象等保存在LocalStorage中传递给页面。

   ```
   1. import { PhotoEditorExtensionAbility,UIExtensionContentSession,Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const TAG = '[ExamplePhotoEditorAbility]';
   5. export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
   6. onCreate() {
   7. hilog.info(0x0000, TAG, 'onCreate');
   8. }

   10. // 获取图片，加载页面并将需要的参数传递给页面
   11. onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void {
   12. hilog.info(0x0000, TAG, `onStartContentEditing want: ${JSON.stringify(want)}, uri: ${uri}`);

   14. const storage: LocalStorage = new LocalStorage({
   15. "session": session,
   16. "uri": uri
   17. } as Record<string, Object>);

   19. session.loadContent('pages/Index', storage);
   20. }

   22. onForeground() {
   23. hilog.info(0x0000, TAG, 'onForeground');
   24. }

   26. onBackground() {
   27. hilog.info(0x0000, TAG, 'onBackground');
   28. }

   30. onDestroy() {
   31. hilog.info(0x0000, TAG, 'onDestroy');
   32. }
   33. }
   ```
3. 在page中实现图片编辑功能。

   图片编辑完成后调用saveEditedContentWithImage保存图片，并将回调结果通过terminateSelfWithResult返回给调用方。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { image } from '@kit.ImageKit';

   7. const TAG = '[ExamplePhotoEditorAbility]';

   9. @Entry
   10. @Component
   11. struct Index {
   12. @State message: string = 'editImg';
   13. @State originalImage: PixelMap | null = null;
   14. @State editedImage: PixelMap | null = null;
   15. private newWant ?: Want;
   16. private storage = this.getUIContext().getSharedLocalStorage();

   18. aboutToAppear(): void {
   19. let originalImageUri = this.storage?.get<string>("uri") ?? "";
   20. hilog.info(0x0000, TAG, `OriginalImageUri: ${originalImageUri}.`);

   22. this.readImageByUri(originalImageUri).then(imagePixMap => {
   23. this.originalImage = imagePixMap;
   24. })
   25. }

   27. // 根据uri读取图片内容
   28. async readImageByUri(uri: string): Promise < PixelMap | null > {
   29. hilog.info(0x0000, TAG, "uri: " + uri);
   30. let file: fileIo.File | undefined;
   31. try {
   32. file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
   33. hilog.info(0x0000, TAG, "Original image file id: " + file.fd);

   35. let imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
   36. if(!imageSourceApi) {
   37. hilog.info(0x0000, TAG, "ImageSourceApi failed");
   38. return null;
   39. }
   40. let pixmap: image.PixelMap = await imageSourceApi.createPixelMap();
   41. if(!pixmap) {
   42. hilog.info(0x0000, TAG, "createPixelMap failed");
   43. return null;
   44. }
   45. this.originalImage = pixmap;
   46. return pixmap;
   47. } catch(e) {
   48. hilog.error(0x0000, TAG, `ReadImage failed:${e}`);
   49. } finally {
   50. fileIo.close(file);
   51. }
   52. return null;
   53. }

   55. build() {
   56. Row() {
   57. Column() {
   58. Text(this.message)
   59. .fontSize(50)
   60. .fontWeight(FontWeight.Bold)

   62. Button("RotateAndSaveImg").onClick(event => {
   63. hilog.info(0x0000, TAG, `Start to edit image and save.`);
   64. // 编辑图片功能实现
   65. this.originalImage?.rotate(90).then(() => {
   66. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
   67. try {
   68. // 调用saveEditedContentWithImage保存图片
   69. (this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext).saveEditedContentWithImage(this.originalImage as image.PixelMap,
   70. packOpts).then(data => {
   71. if (data.resultCode == 0) {
   72. hilog.info(0x0000, TAG, `Save succeed.`);
   73. }
   74. hilog.info(0x0000, TAG,
   75. `saveContentEditingWithImage result: ${JSON.stringify(data)}`);
   76. this.newWant = data.want;
   77. // data.want.uri存有编辑过图片的uri
   78. this.readImageByUri(this.newWant?.uri ?? "").then(imagePixMap => {
   79. this.editedImage = imagePixMap;
   80. })
   81. })
   82. } catch (e) {
   83. hilog.error(0x0000, TAG, `saveContentEditingWithImage failed:${e}`);
   84. return;
   85. }
   86. })
   87. }).margin({ top: 10 })

   89. Button("terminateSelfWithResult").onClick((event => {
   90. hilog.info(0x0000, TAG, `Finish the current editing.`);

   92. let session = this.storage?.get('session') as UIExtensionContentSession;
   93. // 关闭并回传修改结果给调用方
   94. session?.terminateSelfWithResult({ resultCode: 0, want: this.newWant });

   96. })).margin({ top: 10 })

   98. Image(this.originalImage).width("100%").height(200).margin({ top: 10 }).objectFit(ImageFit.Contain)

   100. Image(this.editedImage).width("100%").height(200).margin({ top: 10 }).objectFit(ImageFit.Contain)
   101. }
   102. .width('100%')
   103. }
   104. .height('100%')
   105. .backgroundColor(Color.Pink)
   106. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
   107. }
   108. }
   ```
4. 在工程Module对应的module.json5配置文件中注册PhotoEditorExtensionAbility。

   type标签需要配置为"photoEditor"，srcEntry需要配置为PhotoEditorExtensionAbility组件所对应的代码路径。

   ```
   1. {
   2. "module": {
   3. "extensionAbilities": [
   4. {
   5. "name": "ExamplePhotoEditorAbility",
   6. "icon": "$media:icon",
   7. "description": "ExamplePhotoEditorAbility",
   8. "type": "photoEditor",
   9. "exported": true,
   10. "srcEntry": "./ets/PhotoEditorExtensionAbility/ExamplePhotoEditorAbility.ets",
   11. "label": "$string:EntryAbility_label",
   12. "extensionProcessMode": "bundle"
   13. },
   14. ]
   15. }
   16. }
   ```

## 调用方拉起图片编辑类应用编辑图片

开发者可以在UIAbility或者UIExtensionAbility的页面中通过接口startAbilityByType拉起图片编辑类应用扩展面板，系统将自动查找并在面板上展示基于[PhotoEditorExtensionAbility](../harmonyos-references/js-apis-app-ability-photoeditorextensionability.md)实现的图片编辑应用，由用户选择某个应用来完成图片编辑的功能，最终将编辑的结果返回给到调用方，具体步骤如下：

1. 导入模块。

   ```
   1. import { common, wantConstant } from '@kit.AbilityKit';
   2. import { fileUri, picker } from '@kit.CoreFileKit';
   ```
2. （可选）实现从图库中选取图片。

   ```
   1. async photoPickerGetUri(): Promise < string > {
   2. try {
   3. let PhotoSelectOptions = new picker.PhotoSelectOptions();
   4. PhotoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
   5. PhotoSelectOptions.maxSelectNumber = 1;
   6. let photoPicker = new picker.PhotoViewPicker();
   7. let photoSelectResult: picker.PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
   8. return photoSelectResult.photoUris[0];
   9. } catch(error) {
   10. let err: BusinessError = error as BusinessError;
   11. hilog.error(0x0000, TAG, 'PhotoViewPicker failed with err: ' + JSON.stringify(err));
   12. }
   13. return "";
   14. }
   ```
3. 将图片拷贝到本地沙箱路径。

   ```
   1. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. let file: fileIo.File | undefined;
   3. try {
   4. file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
   5. hilog.info(0x0000, TAG, "file: " + file.fd);

   7. let timeStamp = Date.now();
   8. // 将用户图片拷贝到应用沙箱路径
   9. fileIo.copyFileSync(file.fd, context.filesDir + `/original-${timeStamp}.jpg`);

   11. this.filePath = context.filesDir + `/original-${timeStamp}.jpg`;
   12. this.originalImage = fileUri.getUriFromPath(this.filePath);
   13. } catch (e) {
   14. hilog.error(0x0000, TAG, `readImage failed:${e}`);
   15. } finally {
   16. fileIo.close(file);
   17. }
   ```
4. 在startAbilityByType回调函数中，通过want.uri获取编辑后的图片uri，并做对应的处理。

   ```
   1. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. let abilityStartCallback: common.AbilityStartCallback = {
   3. onError: (code, name, message) => {
   4. const tip: string = `code:` + code + ` name:` + name + ` message:` + message;
   5. hilog.error(0x0000, TAG, "startAbilityByType:", tip);
   6. },
   7. onResult: (result) => {
   8. // 获取到回调结果中编辑后的图片uri并做对应的处理
   9. let uri = result.want?.uri ?? "";
   10. hilog.info(0x0000, TAG, "PhotoEditorCaller result: " + JSON.stringify(result));
   11. this.readImage(uri).then(imagePixMap => {
   12. this.editedImage = imagePixMap;
   13. });
   14. }
   15. }
   ```
5. 将图片转换为图片uri，并调用startAbilityByType拉起图片编辑应用面板。

   ```
   1. let uri = fileUri.getUriFromPath(this.filePath);
   2. context.startAbilityByType("photoEditor", {
   3. "ability.params.stream": [uri], // 原始图片的uri,只支持传入一个uri
   4. "ability.want.params.uriPermissionFlag": wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION // 至少需要分享读权限给到图片编辑面板
   5. } as Record<string, Object>, abilityStartCallback, (err) => {
   6. let tip: string;
   7. if (err) {
   8. tip = `Start error: ${JSON.stringify(err)}`;
   9. hilog.error(0x0000, TAG, `startAbilityByType: fail, err: ${JSON.stringify(err)}`);
   10. } else {
   11. tip = `Start success`;
   12. hilog.info(0x0000, TAG, "startAbilityByType: ", `success`);
   13. }
   14. });
   ```

示例：

```
1. import { common, wantConstant } from '@kit.AbilityKit';
2. import { fileUri, picker } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { image } from '@kit.ImageKit';
6. import { BusinessError } from '@kit.BasicServicesKit';
7. import { JSON } from '@kit.ArkTS';
8. import { photoAccessHelper } from '@kit.MediaLibraryKit';

10. const TAG = 'PhotoEditorCaller';

12. @Entry
13. @Component
14. struct Index {
15. @State message: string = 'selectImg';
16. @State originalImage: ResourceStr = "";
17. @State editedImage: PixelMap | null = null;
18. private filePath: string = "";

20. // 根据uri读取图片内容
21. async readImage(uri: string): Promise < PixelMap | null > {
22. hilog.info(0x0000, TAG, "image uri: " + uri);
23. let file: fileIo.File | undefined;
24. try {
25. file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
26. hilog.info(0x0000, TAG, "file: " + file.fd);

28. let imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
29. if(!imageSourceApi) {
30. hilog.info(0x0000, TAG, "imageSourceApi failed");
31. return null;
32. }
33. let pixmap: image.PixelMap = await imageSourceApi.createPixelMap();
34. if(!pixmap) {
35. hilog.info(0x0000, TAG, "createPixelMap failed");
36. return null;
37. }
38. this.editedImage = pixmap;
39. return pixmap;
40. } catch(e) {
41. hilog.error(0x0000, TAG, `readImage failed:${e}`);
42. } finally {
43. fileIo.close(file);
44. }
45. return null;
46. }

48. // 图库中选取图片
49. async photoPickerGetUri(): Promise<string> {
50. try {
51. let textInfo: photoAccessHelper.TextContextInfo = {
52. text: 'photo'
53. }
54. let recommendOptions: photoAccessHelper.RecommendationOptions = {
55. textContextInfo: textInfo
56. }
57. let options: photoAccessHelper.PhotoSelectOptions = {
58. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
59. maxSelectNumber: 1,
60. recommendationOptions: recommendOptions
61. }
62. let photoPicker = new photoAccessHelper.PhotoViewPicker();
63. let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(options);
64. return photoSelectResult.photoUris[0];
65. } catch (error) {
66. let err: BusinessError = error as BusinessError;
67. hilog.error(0x0000, TAG, 'PhotoViewPicker failed with err: ' + JSON.stringify(err));
68. }
69. return "";
70. }

72. build() {
73. Row() {
74. Column() {
75. Text(this.message)
76. .fontSize(50)
77. .fontWeight(FontWeight.Bold)

79. Button("selectImg").onClick(event => {
80. // 图库中选取图片
81. this.photoPickerGetUri().then(uri => {
82. hilog.info(0x0000, TAG, "uri: " + uri);

84. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
85. let file: fileIo.File | undefined;
86. try {
87. file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
88. hilog.info(0x0000, TAG, "file: " + file.fd);

90. let timeStamp = Date.now();
91. // 将用户图片拷贝到应用沙箱路径
92. fileIo.copyFileSync(file.fd, context.filesDir + `/original-${timeStamp}.jpg`);

94. this.filePath = context.filesDir + `/original-${timeStamp}.jpg`;
95. this.originalImage = fileUri.getUriFromPath(this.filePath);
96. } catch (e) {
97. hilog.info(0x0000, TAG, `readImage failed:${e}`);
98. } finally {
99. fileIo.close(file);
100. }
101. })

103. }).width('200').margin({ top: 20 })

105. Button("editImg").onClick(event => {
106. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
107. let abilityStartCallback: common.AbilityStartCallback = {
108. onError: (code, name, message) => {
109. const tip: string = `code:` + code + ` name:` + name + ` message:` + message;
110. hilog.error(0x0000, TAG, "startAbilityByType:", tip);
111. },
112. onResult: (result) => {
113. // 获取到回调结果中编辑后的图片uri并做对应的处理
114. let uri = result.want?.uri ?? "";
115. hilog.info(0x0000, TAG, "PhotoEditorCaller result: " + JSON.stringify(result));
116. this.readImage(uri).then(imagePixMap => {
117. this.editedImage = imagePixMap;
118. });
119. }
120. }
121. // 将图片转换为图片uri，并调用startAbilityByType拉起图片编辑应用面板
122. let uri = fileUri.getUriFromPath(this.filePath);
123. context.startAbilityByType("photoEditor", {
124. "ability.params.stream": [uri], // 原始图片的uri,只支持传入一个uri
125. "ability.want.params.uriPermissionFlag": wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION // 至少需要分享读权限给到图片编辑面板
126. } as Record<string, Object>, abilityStartCallback, (err) => {
127. let tip: string;
128. if (err) {
129. tip = `Start error: ${JSON.stringify(err)}`;
130. hilog.error(0x0000, TAG, `startAbilityByType: fail, err: ${JSON.stringify(err)}`);
131. } else {
132. tip = `Start success`;
133. hilog.info(0x0000, TAG, "startAbilityByType: ", `success`);
134. }
135. });

137. }).width('200').margin({ top: 20 })

139. Image(this.originalImage).width("100%").height(200).margin({ top: 20 }).objectFit(ImageFit.Contain)

141. Image(this.editedImage).width("100%").height(200).margin({ top: 20 }).objectFit(ImageFit.Contain)
142. }
143. .width('100%')
144. }
145. .height('100%')
146. .backgroundColor(Color.Orange)
147. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
148. }
149. }
```
