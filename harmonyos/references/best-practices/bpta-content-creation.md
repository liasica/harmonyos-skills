---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-content-creation
title: AI辅助图文内容编创
breadcrumb: 最佳实践 > 行业场景解决方案 > 社交通讯 > AI辅助图文内容编创
category: best-practices
scraped_at: 2026-04-29T14:13:15+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:cc27c712a6ade950f6f77c06a7253521dc6d0764b0abd19caa1b4be8dbf45ccc
---

## 概述

本场景实现社交通讯类应用的图文内容编创流程，接入自由流转、服务互动等HarmonyOS特性能力。

## 整体场景介绍

图文编创流程主要通过Photo Picker选取本地图片，然后对图片进行智能处理，同时也可使用自定义相机拍摄动图，最后进行文字编创时可进行自由流转接续编辑和跨端获取相册或相机拍摄内容。

### 演示效果

图文编创操作流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/j5VY_nBKT8KuVY-1hoXPyg/zh-cn_image_0000002229451385.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061310Z&HW-CC-Expire=86400&HW-CC-Sign=2B8229663B2AC40C4780B5B8CCAA8CFE70F9284CE719A10894B1E54BFAF4759E)

## 场景适用说明

### 适用范围

本场景适用于社交通讯类应用，图文内容编辑过程中接入HarmonyOS特性能力，提供详细技术实现方案，降低开发者学习成本，提高接入速度。

## 场景优势

本场景结合HarmonyOS的跨设备互通、智能处理、自由流转等能力，提升用户内容发布体验。具体优势如下：

（1）跨设备互通能力使多设备用户可以灵活选择存储在不同设备上的媒体资源，并使用不同设备的拍摄能力获取新图像，简化了不同设备间的数据传输流程，提升了用户体验。

（2）HarmonyOS智能的使用，为用户提供了强大的编创能力支持。用户可以从图中提取有效信息进行文字编辑，可以从候选图中提取目标去除背景，进行二次创作。这些技术的应用，为用户提供了更丰富的编创选择。

（3）自由流转能力的接入，可无缝切换至其他设备，并同步最新编辑状态至新设备，用户可以灵活选择合适设备，实现接续编辑。

## 场景分析

### 典型场景分析

|  |  |  |
| --- | --- | --- |
| 子场景名称 | 描述 | 实现方案 |
| 图片视图选择 | 发布首页资源文件类型选择 | 使用Photo Picker能力实现图片选择 |
| 相机拍摄 | 自定义相机页面，可拍摄和预览Moving Photo图片 | 使用Camera相机组件能力自定义相机 |
| 图片文字识别、抠取与HDR Vivid图片的展示 | 图片浏览页支持选定图片的目标抠取、复制图上文字信息获取，参与创作编辑，自动识别HDR模式并展示高亮 | 使用Image组件的智能识别能力，实现OCR文字识别与抠图 |
| 跨端相册选取 | 从其他设备的相册中选取图片，回传到本端设备 | 基于CollaborationService跨设备互通组件 |
| 编辑页流转接续 | 编创内容支持在多设备之间接续编辑。开发者可以在不同设备上继续编辑内容 | 基于Ability的自由流转能力，使用ArkData数据管理和分布式文件管理实现本地创作内容的多设备之间接续编辑 |

## 场景实现

## Photo Picker的使用

### 子场景描述

用户在首页点击进入发布流程时，将直接跳转到半模态窗口的Picker页面。该页面支持自定义，为开发者提供更多选择。

### 关键点说明

使用系统Picker能力，可以免申请权限读写权限'READ\_IMAGEVIDEO'和'WRITE\_IMAGEVIDEO'，给开发者提供了极大的便利。

### 关键代码

首先在使用前，需要先创建PhotoViewPicker实例。

```
1. const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
```

[UIUtils.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/utils/UIUtils.ets#L74-L74)

根据业务逻辑需要进行图片选择环节的属性设置，如设置可选择的媒体资源类型、资源数量上限。

```
1. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
2. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
3. photoSelectOptions.maxSelectNumber = CommonConstants.LIMIT_PICKER_NUM - selectedNum;
```

[UIUtils.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/utils/UIUtils.ets#L69-L71)

发起调用，获取图片。

```
1. photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
2. let uriArr = photoSelectResult.photoUris;
3. callback(uriArr);
4. }).catch((err: BusinessError) => {
5. Logger.error(UIUtils.tag,
6. `Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
7. });
```

[UIUtils.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/utils/UIUtils.ets#L77-L83)

## OCR文字识别、智能抠图与HDR vivid的使用

### 子场景描述

选取图片后，可以浏览图片并长按物体实现目标抠取，同时可以识别图片中的文字以供后续文本编辑使用。如果图片采用HDR Vivid模式拍摄，将展示其效果。

### 演示效果

长按图片可识别文字并实现物体抠图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Yys908CxRbGB4LuPNGVw1g/zh-cn_image_0000002229336901.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061310Z&HW-CC-Expire=86400&HW-CC-Sign=97C4F3438A383BAA127EE5CFCC288519F8629A12592EF94713E75593A7DDA388)

### 关键点说明

（1）在Image组件中，设置enableAnalyzer属性可实现OCR文字识别和抠图；设置dynamicRangeMode属性可展示HDR高亮，需配合image.DecodingOptions配置动态范围模式。

（2）图片可OCR文字识别时，点击图片内出现的识别按钮或长按文字，会出现复制文本菜单和文字框选区域。

（3）抠图：长按图片中的物体，出现抠图效果，菜单中可复制与分享。

### 关键代码

开启图片智能分析属性并设置图像的动态模式。

```
1. Image(item)
2. .objectFit(ImageFit.Contain)
3. .enableAnalyzer(true)
4. .dynamicRangeMode(DynamicRangeMode.HIGH)
```

[SelectedEditeView.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/view/SelectedEditeView.ets#L88-L91)

设置图片解码选项，配合动态模式。

```
1. public static options: image.DecodingOptions = {
2. index: 0,
3. editable: false,
4. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
5. };

7. static createPixelMap(uri: string): ImageInfo | undefined {
8. let imageInfo: ImageInfo | undefined;
9. try {
10. let file = fs.openSync(uri, fs.OpenMode.READ_ONLY);
11. let displayName = file.name;
12. let imageResource = image.createImageSource(file.fd);
13. let pixelMap = imageResource.createPixelMapSync(FileUtils.options);
14. imageInfo = { imagePixelMap: pixelMap, imageName: displayName };
15. fs.closeSync(file);
16. } catch (error) {
17. Logger.error(FileUtils.tag, `createPixelMap error: ${JSON.stringify(error)}`);
18. }
19. return imageInfo;
20. }
```

[FileUtils.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/utils/FileUtils.ets#L27-L85)

## Moving Photo的拍摄与展示

## 子场景描述

在编辑图片页，增加一个自定义相机tab项，开发者可以根据自身需求，设置并拍摄多种模式的照片，用于内容展示。

### 关键点说明

（1）相机初始化后，可设置Moving Photo属性，默认关闭。当前场景中，若设置为开启，可点击Moving Photo按钮切换状态。

（2）获取拍摄的最新图片，需要在拍摄完成后等待30秒，然后才能获取到最新图片。

（3）使用MovingPhotoView视图预览Moving Photo图片，长按可播放。

（4）申请对应权限，同意后初始化相机。

### 关键代码

申请对应权限。

```
1. private permissions: Array<Permissions> = [
2. 'ohos.permission.CAMERA',
3. 'ohos.permission.MICROPHONE',
4. 'ohos.permission.MEDIA_LOCATION',
5. 'ohos.permission.READ_IMAGEVIDEO',
6. 'ohos.permission.WRITE_IMAGEVIDEO',
7. ];
8. abilityAccessCtrl.createAtManager().requestPermissionsFromUser(DataUtils.context, this.permissions).then(() => {
9. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
10. this.initCamera();
11. this.getThumbnail();
12. })
```

[CameraView.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/view/CameraView.ets#L35-L187)

相机设置Moving Photo属性。

```
1. setEnableLivePhoto(isMovingPhoto: boolean) {
2. try {
3. if (this.photoOutput?.isMovingPhotoSupported()) {
4. this.photoOutput?.enableMovingPhoto(isMovingPhoto);
5. }
6. } catch (error) {
7. Logger.error(this.tag, `The setEnableLivePhoto call failed. error: ${JSON.stringify(error)}`);
8. }
9. }
```

[CameraService.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/model/CameraService.ets#L222-L231)

获取媒体库中最新图片地址与缩略图。

```
1. async getThumbnail(): Promise<void> {
2. try {
3. let photoAsset: photoAccessHelper.PhotoAsset =
4. AppStorage.get(CommonConstants.KEY_PHOTO_ASSET) as photoAccessHelper.PhotoAsset;
5. if (photoAsset === undefined) {
6. return;
7. }
8. this.currentImg = await photoAsset.getThumbnail();
9. } catch (error) {
10. Logger.error(this.tag, `getThumbnail error: ${JSON.stringify(error)}`);
11. }
12. }
```

[CameraView.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/view/CameraView.ets#L289-L301)

引入Moving Photo相关库。

```
1. import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@ohos.multimedia.movingphotoview';
```

[PreviewMovingPhotoPage.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/pages/PreviewMovingPhotoPage.ets#L17-L17)

通过拍摄后获取的photoAccessHelper.PhotoAsset请求Moving Photo。

```
1. @StorageLink(CommonConstants.KEY_MOVING_DATA) src: photoAccessHelper.MovingPhoto | undefined = undefined;
2. @StorageLink(CommonConstants.KEY_IMAGE_INFO) imageInfoArr: Array<ImageInfo> = [];
3. @State isMuted: boolean = false;
4. async aboutToAppear(): Promise<void> {
5. // ...
6. this.requestMovingPhoto();
7. }

9. private requestMovingPhoto() {
10. let photoAsset: photoAccessHelper.PhotoAsset =
11. AppStorage.get(CommonConstants.KEY_PHOTO_ASSET) as photoAccessHelper.PhotoAsset;
12. if (photoAsset === undefined) {
13. return;
14. }
15. let requestOptions: photoAccessHelper.RequestOptions = {
16. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
17. }
18. photoAccessHelper.MediaAssetManager.requestMovingPhoto(DataUtils.context, photoAsset, requestOptions,
19. new MediaDataHandlerMovingPhoto()).catch(() => {
20. Logger.error(this.tag, `requestMovingPhoto fail!`);
21. });
22. }

24. class MediaDataHandlerMovingPhoto implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
25. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto): Promise<void> {
26. AppStorage.setOrCreate(CommonConstants.KEY_MOVING_DATA, movingPhoto);
27. }
28. }
```

[PreviewMovingPhotoPage.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/pages/PreviewMovingPhotoPage.ets#L35-L218)

添加Moving Photo展示图。

```
1. build() {
2. Flex({
3. direction: new BreakpointType(
4. {
5. sm: FlexDirection.Column,
6. md: FlexDirection.Column,
7. lg: FlexDirection.Row,
8. }
9. ).getValue(this.currentBreakpoint),
10. wrap: FlexWrap.NoWrap,
11. justifyContent: FlexAlign.Start,
12. alignItems: ItemAlign.Start,
13. alignContent: FlexAlign.Start
14. }) {
15. this.setActions();
16. MovingPhotoView({
17. movingPhoto: this.src,
18. controller: this.controller
19. })
20. .width($r('app.string.full_screen'))
21. .objectFit(ImageFit.Contain)
22. .muted(this.isMuted)
23. .margin(new BreakpointType(
24. {
25. sm: { bottom: $r('app.float.margin_190') } as Padding,
26. md: { bottom: $r('app.float.margin_190') } as Padding,
27. lg: { right: $r('app.float.margin_24') } as Padding,
28. }
29. ).getValue(this.currentBreakpoint))
30. }
31. .backgroundColor(Color.Black)
32. .width($r('app.string.full_screen'))
33. .height($r('app.string.full_screen'))
34. }
```

[PreviewMovingPhotoPage.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/pages/PreviewMovingPhotoPage.ets#L64-L103)

说明

本章节只介绍主干流程的关键代码，要实现自定义相机还需要其他配置，可详细关注封装模块CameraService文件，Moving Photo的使用可查看相关Api使用：[动图照片](../harmonyos-references/ohos-multimedia-movingphotoview.md)。

## 跨设备互通组件的使用

### 演示效果

跨端相册获取新的图片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VRnucn6XTB6gjnTeb32VSg/zh-cn_image_0000002229336897.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061310Z&HW-CC-Expire=86400&HW-CC-Sign=91D9A1FEB9BB5A6F6568848F0E98A33A72CF4929B32E35F518DE3C81B766A737 "点击放大")

### 子场景描述

通过跨设备互通组件，实现跨端相册访问和跨端相机拍照，从其他设备获取新的图像内容，提高设备间图像传输的快捷性和便利性。

### 关键点说明

（1）使用跨设备互通组件需要连接网络并登录相同账号。

注意

当前跨设备互通能力仅支持“重”设备调用“轻”设备，其中“重”设备指重量较大、便携性较差的设备，“轻”设备指重量较轻、便携性较好的设备。设备间可跨端调用关系如下说明：

（1）平板可调用手机，但无法调用其他平板。

（2）手机无法调用平板，也无法调用其他手机。

### 关键代码

跨端拍照与跨端相册访问

使用createCollaborationServiceMenuItems定义设备列表选择器，显示组网内具有相机能力的设备列表。

```
1. import {
2. CollaborationServiceFilter,
3. CollaborationServiceStateDialog,
4. createCollaborationServiceMenuItems
5. } from '@kit.ServiceCollaborationKit';
6. @Builder
7. CollaborationMenu() {
8. Menu() {
9. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL]);
10. }
11. }
```

[GraphicCreationPage.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/pages/GraphicCreationPage.ets#L16-L359)

使用CollaborationCameraStateDialog弹窗组件提示对端相机拍摄状态。

该组件在build()函数内直接调用，实现onState方法。拍摄完成后，通过onState方法回传内容。

onState方法的回调函数包含两个参数：stateCode表示业务完成状态，buffer表示成功返回的数据。

```
1. @Builder
2. setCollaborationDialog() {
3. CollaborationServiceStateDialog({
4. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode,
5. bufferType, buffer)
6. });
7. }

9. private doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
10. if (stateCode !== 0) {
11. Logger.error(this.tag, `doInsertPicture stateCode: ${stateCode}}`);
12. return;
13. }
14. Logger.info(this.tag, `doInsertPicture bufferType: ${bufferType}}`);
15. if (bufferType === CommonConstants.BUFFER_TYPE) {
16. if (this.imageInfoArr.length === CommonConstants.LIMIT_PICKER_NUM) {
17. try {
18. this.getUIContext().getPromptAction().showToast({
19. message: $r('app.string.toast_picker_limit'),
20. duration: DataUtils.fromResToNumber($r('app.float.show_DELAY_TIME')),
21. });
22. } catch (error) {
23. Logger.error(this.tag, `showToast error: ${JSON.stringify(error)}}`);
24. }
25. return;
26. }
27. let saveUri: string = FileUtils.saveFile(DataUtils.context, buffer);
28. let imageInfo: ImageInfo | undefined = FileUtils.createPixelMap(saveUri);
29. if (imageInfo) {
30. this.imageInfoArr.unshift(imageInfo);
31. this.selectedData.unshiftData(imageInfo.imagePixelMap);
32. // copy file to distributedFilesDir
33. FileUtils.copyFileToDestination(saveUri, DataUtils.context.distributedFilesDir);
34. }
35. }
36. }
```

[GraphicCreationPage.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/pages/GraphicCreationPage.ets#L122-L158)

## 应用接续的实现

### 子场景描述

使用Ability的自由流转能力，编辑内容可以流转到其他设备上进行接续编辑，方便用户在不同设备上编辑。

### 演示效果

自由流转，接续编辑图文内容的功能已启用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/-WbgL0ARR1OftHTmR8kBsA/zh-cn_image_0000002229336905.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061310Z&HW-CC-Expire=86400&HW-CC-Sign=FA2F659502BEC07796831EFD464770450D9A7059E0D3C8A9AF8FE3A8465C0934 "点击放大")

### 关键点说明

接续使用条件

（1）两端设备登录同一华为账号。

（2）两端设备打开Wi-Fi和蓝牙开关，连接同一局域网，可提升数据传输速度。

（3）应用接续只能在同应用（UIAbility）之间触发，双端设备都需要该应用。

（4）在onContinue回调中使用wantParam传输的数据应控制在100KB以内。对于大于100KB的数据，建议使用分布式数据对象或分布式文件系统，例如图片文件。

申请权限需要在module.json5文件中的module对象的requestPermissions属性中进行。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.DISTRIBUTED_DATASYNC",
4. "reason": "$string:distributed_desc",
5. "usedScene": {
6. "abilities": [
7. "EntryAbility"
8. ],
9. "when": "always"
10. }
11. }
12. // ...
13. ]
```

[module.json5](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/module.json5#L15-L109)

打开应用接续开关，在module.json5文件里的module对象的abilities字段内设置"continuable"的值为true。

```
1. "abilities": [
2. {
3. // ...
4. "continuable": true,
5. // ...
6. }
7. ]
```

[module.json5](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/module.json5#L113-L139)

### 关键代码

应用接续可以按需迁移路由栈，也可选择动态配置，仅对特定页面开启接续，此处仅设置最后的图文编辑页面GraphicCreationPage开启接续能力。按需迁移路由栈的方法具体可参考[应用接续开发指导：按需迁移页面栈](../harmonyos-guides/app-continuation-guide.md#section34254151518)。

```
1. onPageShow(): void {
2. DataUtils.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
3. Logger.info('setMissionContinueState ACTIVE result: ', `${result.code}`);
4. });
5. }

7. aboutToDisappear(): void {
8. this.title = '';
9. this.description = '';
10. DataUtils.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result) => {
11. Logger.info('setMissionContinueState INACTIVE result: ', `${result.code}`);
12. });
13. }
```

[GraphicCreationPage.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/pages/GraphicCreationPage.ets#L62-L75)

设置迁移加载指定页面。

```
1. onWindowStageRestore(windowStage: window.WindowStage) {
2. windowStage.loadContent('pages/GraphicCreationPage', (err, data) => {
3. // ...
4. });
5. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L179-L190)

迁移端实现onContinue接口，多图片自由流转，使用资产卡片数组的方式传递，与其他文本数据分装成一个数据对象。

```
1. async onContinue(wantParam: Record<string, Object | undefined>): Promise<AbilityConstant.OnContinueResult> {
2. try {
3. // get distribute id
4. let sessionId: string = distributedDataObject.genSessionId();
5. wantParam.distributedSessionId = sessionId;
6. // set images assets info
7. let imageInfoArray = AppStorage.get<Array<ImageInfo>>(CommonConstants.KEY_IMAGE_INFO);
8. let assets: commonType.Assets = [];
9. if (imageInfoArray) {
10. for (let i = 0; i < imageInfoArray.length; i++) {
11. let append = imageInfoArray[i];
12. let attachment: commonType.Asset | undefined = this.getAssetInfo(append);
13. if (attachment === undefined) {
14. continue;
15. }
16. assets.push(attachment);
17. }
18. }
19. // set distribute data object
20. let contentInfo: ContentInfo = new ContentInfo(
21. AppStorage.get(CommonConstants.KEY_TITLE),
22. AppStorage.get(CommonConstants.KEY_DESCRIPTION),
23. AppStorage.get(CommonConstants.KEY_IMAGE_INFO),
24. assets
25. );
26. let source = contentInfo.flatAssets();
27. // save data to distribute
28. this.distributedObject = distributedDataObject.create(this.context, source);
29. Logger.info(this.tag, `onContinue source: ${JSON.stringify(source)}`);
30. this.distributedObject.setSessionId(sessionId);
31. await this.distributedObject.save(wantParam.targetDevice as string).catch((err: BusinessError) => {
32. Logger.error(this.tag, `Failed to save. Code: ${err.code}, message: ${err.message}`);
33. });
34. } catch (error) {
35. Logger.error(this.tag, 'distributedDataObject failed', `code ${(error as BusinessError).code}`);
36. }
37. return AbilityConstant.OnContinueResult.AGREE;
38. }

40. private getAssetInfo(append: ImageInfo): commonType.Asset | undefined {
41. let filePath = this.context.distributedFilesDir + '/' + append.imageName;
42. try {
43. fs.statSync(filePath);
44. let uri: string = fileUri.getUriFromPath(filePath);
45. let stat = fs.statSync(filePath);
46. let attachment: commonType.Asset = {
47. name: append.imageName,
48. uri: uri,
49. path: filePath,
50. createTime: stat.ctime.toString(),
51. modifyTime: stat.ctime.toString(),
52. size: stat.size.toString()
53. };
54. Logger.info(this.tag, `getAssetInfo attachment = ${JSON.stringify(attachment)}`);
55. return attachment;
56. } catch (error) {
57. Logger.error(this.tag, `getAssetInfo error: ${JSON.stringify(error)}`);
58. return undefined;
59. }
60. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L96-L156)

说明

这部分代码写在EntryAbility中，而不是Page页中。使用AppStorage进行数据的持续保存和双向绑定，当数据变化时更新视图。

接收端实现onCreate接口和onNewWant接口，onCreate接口用于冷启动或多实例热启动，onNewWant接口用于单实例热启动。仅在应用接续状态下，注册数据监听，恢复页面流转的数据。

```
1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
2. DataUtils.context = this.context;
3. // set circulation status INACTIVE
4. this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result) => {
5. Logger.info(`restoreDistributedObject setMissionContinueState code: ${result.code}`);
6. });
7. this.restoreDistributedObject(want, launchParam);
8. Logger.info(this.tag, '%{public}s', 'Ability onCreate');
9. }

11. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
12. this.restoreDistributedObject(want, launchParam);
13. }

15. private restoreDistributedObject(want: Want, launchParam: AbilityConstant.LaunchParam): void {
16. if (launchParam.launchReason !== AbilityConstant.LaunchReason.CONTINUATION) {
17. return;
18. }
19. try {
20. // File copying takes a long time, resulting in the page lifecycle aboutToAppear being executed first.
21. let imageInfoArr: ImageInfo[] = [];
22. AppStorage.setOrCreate(CommonConstants.KEY_IMAGE_INFO, imageInfoArr);
23. let contentInfo: ContentInfo = new ContentInfo(undefined, undefined, undefined, undefined);
24. // 创建分布式数据对象
25. this.distributedObject = distributedDataObject.create(this.context, contentInfo);
26. // Add a data restored listener.
27. this.distributedObject.on('status',
28. (_sessionId: string, _networkId: string, status: 'online' | 'offline' | 'restored') => {
29. if (status === 'restored') {
30. if (!this.distributedObject) {
31. return;
32. }
33. AppStorage.setOrCreate(CommonConstants.KEY_TITLE, this.distributedObject['title']);
34. AppStorage.setOrCreate(CommonConstants.KEY_DESCRIPTION, this.distributedObject['description']);
35. let attachments = this.distributedObject['attachments'] as commonType.Assets;
36. if (attachments) {
37. for (const attachment of attachments) {
38. let sourceUri: string =
39. fileUri.getUriFromPath(`${this.context.distributedFilesDir}/${attachment.name}`);
40. let destination: string = this.context.filesDir;
41. FileUtils.copyFileToDestination(sourceUri, destination);
42. let uri: string = `${this.context.filesDir}/${attachment.name}`;
43. let imageInfo = FileUtils.createPixelMap(uri);
44. if (imageInfo) {
45. imageInfoArr.push(imageInfo);
46. }
47. }
48. }
49. AppStorage.set(CommonConstants.KEY_IMAGE_INFO, imageInfoArr);
50. AppStorage.setOrCreate(CommonConstants.KEY_RESTORE_IMAGE_INFO, imageInfoArr);
51. }
52. });
53. let sessionId: string = want.parameters?.distributedSessionId as string;
54. this.distributedObject.setSessionId(sessionId);
55. this.context.restoreWindowStage(new LocalStorage());
56. } catch (error) {
57. Logger.info(`restoreDistributedObject error: ${JSON.stringify(error)}`);
58. }
59. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L32-L91)

图片的流转需要借助分布式文件系统，发送侧需将文件拷贝到分布式目录下，接受侧再从分布式目录拷贝到本地沙箱使用。

```
1. static copyFileToDestination(sourceUri: string, destination: string) {
2. try {
3. let buf = new ArrayBuffer(CommonConstants.FILE_BUFFER_SIZE);
4. let readSize = 0;
5. let file = fs.openSync(sourceUri, fs.OpenMode.READ_ONLY);
6. let readLen = fs.readSync(file.fd, buf, { offset: readSize });
7. let destinationDistribute =
8. fs.openSync(`${destination}/${file.name}`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
9. while (readLen > 0) {
10. readSize += readLen;
11. fs.writeSync(destinationDistribute.fd, buf);
12. readLen = fs.readSync(file.fd, buf, { offset: readSize });
13. }
14. Logger.info(FileUtils.tag, 'copyFileToDestination success');
15. fs.closeSync(file);
16. fs.closeSync(destinationDistribute);
17. } catch (err) {
18. Logger.error(FileUtils.tag, `copyFileToDestination failed. Code: ${err.code}, message: ${err.message}`);
19. }
20. }
```

[FileUtils.ets](https://gitcode.com/harmonyos_samples/graphic-creation/blob/master/entry/src/main/ets/utils/FileUtils.ets#L41-L61)

## 示例代码

* [基于AI能力实现图文内容高效编创](https://gitcode.com/HarmonyOS_Samples/graphic-creation)
