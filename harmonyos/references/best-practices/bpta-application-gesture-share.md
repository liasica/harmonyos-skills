---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-gesture-share
title: 隔空传送快速分享
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 隔空传送快速分享
category: best-practices
scraped_at: 2026-04-29T14:12:54+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:5d05723a7a9738451611b04b73ee19cc67def4212f354038874adc748071b7a6
---

## 概述

[Share Kit（分享服务）](../harmonyos-guides/share-kit-guide.md)提供隔空传送分享，支持用户通过“一抓一放”手势实现跨设备文件分享（图片、视频、文档等）以及跨设备链接分享。

|  |  |
| --- | --- |
| 隔空传送分享文件 | 通过隔空传送手势触发文件分享，接收端为phone、tablet设备会将媒体文件存储至图库，非媒体文件存储至文件管理器，接收端为PC/2in1设备则会将媒体以及非媒体文件存储至文件管理器。 |
| 隔空传送分享链接 | 通过隔空传送手势触发分享App Linking链接，接收端已安装应用可直接打开应用查看内容。 |

## 实现原理

### 关键技术

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/r-cNet0WT4STuu1MawqxnA/zh-cn_image_0000002464125198.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061244Z&HW-CC-Expire=86400&HW-CC-Sign=2FBD4FF3CBA233896BC2E1ECD2AF8E49BBDBE4E73B2F7D79D60C32FD69578B5B "点击放大")

隔空传送基于分享服务，允许用户通过简单的“一抓一放”手势实现跨设备分享，当前支持手机、平板、PC，使用体验无差异，应用接入只需监听harmonyShare.on('gesturesShare')方法。

当用户做出手势进行隔空传送分享时，系统触发回调，应用可以在回调中实现数据分享。

接收端的处理由系统统一管理：

* 媒体文件（如图片、视频）将存储到图库。
* 非媒体文件将存储到文件管理。
* App Linking链接将自动打开目标应用，并由应用处理链接传递的参数，实现内容的快速访问。

### 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/9-doG1tXTOWdf5BIC3LDng/zh-cn_image_0000002497324205.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061244Z&HW-CC-Expire=86400&HW-CC-Sign=C5659BB9CBB3A404DA12DA5E4B1E4745487E11D1CC69AD13D1858CEF1C65F057 "点击放大")

1. **分享注册监听与取消监听**：在分享页面的生命周期函数（如aboutToAppear或onPageShow）中，注册 harmonyShare.on('gesturesShare') 事件监听，以监听隔空传送事件。当页面即将隐藏或应用退至后台时，通过harmonyShare.off('gesturesShare')取消该监听。
2. **构建分享数据**：定义需要分享的数据[SharedData](../harmonyos-references/share-system-share.md#section816451553012)。
3. **分享数据**：在监听回调中调用[sharableTarget.share](../harmonyos-references/share-harmony-share.md#section1862171812120)方法来分享数据。
4. **文件接收策略与对端跳转处理**：
   1. **文件分享**：隔空传送文件分享的接收由对端系统自行接收，见[文件接收策略](bpta-application-gesture-share.md#section177815256291)。
   2. **链接分享**：隔空传送链接分享需[配置App Linking](bpta-application-gesture-share.md#section1685558173015)并在接收端进行数据处理参考[对端跳转处理](bpta-application-gesture-share.md#section20788652163113)。

说明

* **超时控制**：从触发事件到调用sharableTarget.share需在3秒内完成，否则可能导致失败。
* **页面生命周期管理**：确保页面隐藏或退至后台时取消监听。
* **数据分享**：可分享链接或文件（图片、视频、文档等），但每次分享内容只能是链接或文件中的一种，不支持混合分享。

## 分享文件

### 分享注册监听与取消监听

[harmonyShare（华为分享）](../harmonyos-references/share-harmony-share.md)模块提供了隔空传送分享事件的监听方法[on('gesturesShare')](../harmonyos-references/share-harmony-share.md#section199317814132)及取消监听的方法[off('gesturesShare')](../harmonyos-references/share-harmony-share.md#section1699538101317)。

说明

隔空传送监听方法：

on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

该方法需传入capability参数，类型为[SendCapabilityRegistry](../harmonyos-references/share-harmony-share.md#section7361949172719)，继承自[BaseCapabilityRegistry](../harmonyos-references/share-harmony-share.md#section7252115555417)。其包含windowId属性，需要传入当前应用的窗口ID。在PC/2in1或平板自由窗口模式中，系统会根据窗口ID判断当前应用是否获取了窗口焦点。只有在获取焦点后，当用户触发隔空传送事件时，才会触发应用注册的隔空传送方法。

该方法支持phone、tablet和PC/2in1设备类型，在多设备开发时建议使用该接口。

定义ShareModel类，用于封装分享相关方法，也便于分享页面调用相关方法，首先需要导入相关模块，其中harmonyShare、systemShare为分享服务相关模块。

```
1. import { harmonyShare, systemShare } from '@kit.ShareKit';
2. import { uniformTypeDescriptor } from '@kit.ArkData';
3. import { fileUri } from '@kit.CoreFileKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { common } from '@kit.AbilityKit';
6. import { window } from '@kit.ArkUI';
7. import { hilog } from '@kit.PerformanceAnalysisKit';
8. import { FileData, ShareType, VIDEO_SOURCES } from './FileData';
```

[ShareModel.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/model/ShareModel.ets#L17-L24)

将隔空传送监听方法[on('gesturesShare')](../harmonyos-references/share-harmony-share.md#section199317814132)封装为immersiveListening()，取消监听的方法[off('gesturesShare')](../harmonyos-references/share-harmony-share.md#section1699538101317)封装为immersiveDisableListening()。在分享页面可通过初始化ShareModel类并调用immersiveListening()方法来启动监听，调用immersiveDisableListening()方法取消监听。

```
1. /**
2. *  Add gesturesShare listening.
3. */
4. public immersiveListening(shareType: ShareType) {
5. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
6. window.getLastWindow(this.context).then((data) => {
7. try {
8. let mainWindowID: number = data.getWindowProperties().id;
9. harmonyShare.on('gesturesShare', { windowId: mainWindowID }, (target: harmonyShare.SharableTarget) => {
10. this.immersiveCallback(target, shareType);
11. });
12. } catch (err) {
13. let error = err as BusinessError;
14. hilog.error(0x0000, 'GesturesShare', `getWindowProperties error ${error.code} ${error.message}`);
15. }
16. }).catch((error: BusinessError) => {
17. hilog.error(0x0000, 'GesturesShare', `immersiveListening error ${error.code} ${error.message}`);
18. })
19. }
20. }

22. /**
23. *  Remove gesturesShare listening.
24. */
25. public immersiveDisableListening() {
26. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
27. window.getLastWindow(this.context).then((data) => {
28. try {
29. let mainWindowID: number = data.getWindowProperties().id;
30. harmonyShare.off('gesturesShare', { windowId: mainWindowID });
31. } catch (error) {
32. let err = error as BusinessError;
33. hilog.error(0x0000, 'GesturesShare', `getWindowProperties error ${err.code} ${err.message}`);
34. }
35. }).catch((error: BusinessError) => {
36. hilog.error(0x0000, 'GesturesShare', `immersiveDisableListening error ${error.code} ${error.message}`);
37. })
38. }
39. }
```

[ShareModel.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/model/ShareModel.ets#L55-L93)

开发者应在用户进入隔空传送分享页面时调用隔空传送分享接口。当应用不再需要隔空传送分享文件或离开页面（包括退至后台等情况）时，应及时调用取消监听的方法。ShareModel模块自定义封装了分享相关方法，可以通过调用this.shareModel.immersiveListening()方法并传入ShareType.FILE\_SHARE来注册文件分享事件监听，调用this.shareModel.immersiveDisableListening()来取消监听。

当用户在文件分享页面勾选或取消勾选文件时，会触发onChange()方法，在该方法中，调用setFileShare()方法将要分享的文件索引数据存储到shareModel实例中，以便在生成分享数据时使用。

```
1. import { common } from '@kit.AbilityKit';
2. import { filePreview } from '@kit.PreviewKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { FileData, FILE_SOURCES, ShareType } from '../model/FileData';
5. import { ShareModel } from '../model/ShareModel';
6. import { FileUtil, BreakpointConstants, BreakpointType } from '@ohos/common';

8. @Component
9. export struct FileSharePageComponent {
10. // ...
11. // Pending shared data index.
12. @State fileShare: number[] = [];
13. // All file data collection.
14. @State dataList: FileData[] = FILE_SOURCES;

16. build() {
17. NavDestination() {
18. List({ space: 16 }) {
19. ForEach(this.dataList, (item: FileData, index: number) => {
20. ListItem() {
21. Stack() {
22. // ...
23. Column() {
24. Checkbox({ name: index + '', group: 'checkboxGroup'})
25. // ...
26. .onChange((value: boolean) => {
27. if (value) {
28. this.fileShare.push(index);
29. } else {
30. this.fileShare.splice(this.fileShare.indexOf(index), 1);
31. }
32. this.shareModel = ShareModel.getInstance(this.context);
33. this.shareModel.setFileShare(this.fileShare);
34. this.shareModel.setVideoDataList(this.dataList);
35. })
36. // ...
37. }
38. // ...
39. .onShown(() => {
40. // ...
41. this.shareModel = ShareModel.getInstance(this.context);
42. this.shareModel.immersiveListening(ShareType.FILE_SHARE);
43. })
44. .onHidden(() => {
45. this.shareModel = ShareModel.getInstance(this.context);
46. this.shareModel.immersiveDisableListening();
47. })
48. }
49. }
```

[FileSharePageComponent.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/view/FileSharePageComponent.ets#L17-L153)

### 构建分享数据

在分享数据时，分享发起方需要构建[SharedRecord](../harmonyos-references/share-system-share.md#section20696483813)对象。在文件分享场景中，发起方在构造此参数时，必须传入uri和utd这两个属性。

说明

* uri是指要分享的文件URI，而非文件路径，例如沙箱路径content.fileDir，应通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)获取其URI。
* utd则是当前文件的[标准化数据类型](../harmonyos-guides/uniform-data-type-list.md)，需要传入与分享的数据匹配的类型，以便系统匹配精确的目标应用，推荐使用[uniformTypeDescriptor.getUniformDataTypeByFilenameExtension](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgetuniformdatatypebyfilenameextension11)方法，通过给定的文件后缀名查询标准化数据类型的ID。

在ShareModel模块中定义getShareRecord()方法，用于根据当前的文件类型构建分享数据。定义getFileShareData()方法，当需要分享多个文件时，该方法会通过循环处理来获取分享数据。

```
1. /**
2. * Get file Share data.
3. * @returns systemShare.SharedData.
4. */
5. private getFileShareData(): systemShare.SharedData {
6. let shareData: systemShare.SharedData =
7. new systemShare.SharedData(this.getShareRecord(this.videoDataList[this.fileShare[0]]));
8. try {
9. for (let i = 1; i < this.fileShare.length; i++) {
10. shareData.addRecord(this.getShareRecord(this.videoDataList[this.fileShare[i]]));
11. }
12. } catch (err) {
13. let error = err as BusinessError;
14. hilog.error(0x0000, 'GesturesShare', `shareData.addRecord error ${error.code} ${error.message}`);
15. }
16. return shareData;
17. }

19. /**
20. * Get shared data.
21. *
22. * @param data File data to be shared.
23. * @returns systemShare.SharedRecord.
24. */
25. private getShareRecord(data: FileData): systemShare.SharedRecord {
26. let suffix = '.' + data.url.split('.').pop();
27. // Obtain the UTD through the file extension.
28. let utd = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(suffix);
29. hilog.info(0x0000, 'GesturesShare', `getShareRecord utd ${utd}`);
30. return {
31. utd: utd,
32. uri: data.url,
33. thumbnailUri: data.thumbnail,
34. title: data.name,
35. description: data.description
36. };
37. }
```

[ShareModel.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/model/ShareModel.ets#L118-L154)

### 分享数据

在隔空传送事件回调中，调用this.immersiveCallback()方法，通过传入的ShareType类型来判断当前是文件分享还是链接分享，文件分享调用getFileShareData()方法构造分享数据，并通过sharableTarget.share()方法分享数据，完成隔空传送文件分享流程。

```
1. public immersiveCallback(target: harmonyShare.SharableTarget, shareType: ShareType) {
2. if (shareType === ShareType.FILE_SHARE) {
3. if (!this.fileShare || this.fileShare.length === 0) {
4. return;
5. }
6. let shareData: systemShare.SharedData = this.getFileShareData();
7. target.share(shareData);
8. } else {
9. let shareData: systemShare.SharedData = this.getLinkShareData();
10. target.share(shareData);
11. }
12. }
```

[ShareModel.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/model/ShareModel.ets#L103-L114)

### 文件接收策略

分享接收端接收数据时遵循统一规则，详情请参考[目标设备接收分享数据一步直达体验](../harmonyos-guides/share-access-one-step.md)。当传入的分享参数utd为uniformTypeDescriptor.UniformDataType.IMAGE且文件确认为图片文件时，接收端为phone、tablet设备时默认将其存储在图库中。当传入的utd为uniformTypeDescriptor.UniformDataType.FILE时，文件会默认存储到文件管理中。接收端为PC/2in1设备类型时则会将媒体以及非媒体文件存储至文件管理器。系统预置了常用类型，详情可参考[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)。

## 分享链接

开发者可以通过分享 AppLinking 链接实现应用间的无缝跳转和内容精准直达。当用户通过隔空传送分享链接时，接收端接收链接后：

* 如果目标应用已安装，将直接启动目标应用。
* 如果目标应用未安装，将直接跳转到应用市场或启动浏览器打开网页查看内容。

详情请参考碰一碰视频分享[典型场景](bpta-application-knock-video-share.md#section95975396464)章节。

### 分享注册监听及取消监听

分享链接再注册监听以及取消监听与分享文件章节下的[分享注册监听与取消监听](bpta-application-gesture-share.md#section18279162912273)处理过程一致，开发者可参考分享文件这一章节的内容，在调用immersiveListening()方法需传入ShareType.LINK\_SHARE来注册链接分享事件监听，调用this.shareModel.immersiveDisableListening()来取消监听。

在分享链接页面，当用户点击不同的视频集数时，会触发onClick()方法。在该方法中，调用setVideoIndex()方法将当前集数存储到shareModel实例中，以便在生成分享链接时使用。

```
1. import { common } from '@kit.AbilityKit';
2. import { JSON } from '@kit.ArkTS';
3. import { FileData, ShareType, VIDEO_SOURCES } from '../model/FileData';
4. import { ShareModel } from '../model/ShareModel';
5. import { BreakpointConstants } from '@ohos/common';

7. @Component
8. export struct LinkSharePageComponent {
9. // ...
10. // Current playing video index.
11. @State currentVideoIndex: number = 0;
12. @State url: ResourceStr = $rawfile(this.dataList[this.currentVideoIndex].url);

14. build() {
15. NavDestination() {
16. Scroll() {
17. Column() {
18. // ...
19. Column() {
20. // ...
21. Scroll() {
22. Row({ space: 10 }) {
23. ForEach(this.dataList, (item: FileData, index) => {
24. RelativeContainer() {
25. // ...
26. }
27. // ...
28. .onClick(() => {
29. this.currentVideoIndex = index;
30. this.shareModel = ShareModel.getInstance(this.context);
31. this.shareModel.setVideoIndex(this.currentVideoIndex);
32. this.videoController.reset();
33. this.url = $rawfile(item.url);
34. })
35. // ...
36. }
37. // ...
38. .onShown(() => {
39. // ...
40. this.shareModel = ShareModel.getInstance(this.context);
41. this.shareModel?.immersiveListening(ShareType.LINK_SHARE);
42. })
43. .onHidden(() => {
44. this.shareModel = ShareModel.getInstance(this.context);
45. this.shareModel?.immersiveDisableListening();
46. })
47. }

49. // ...
50. }
```

[LinkSharePageComponent.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/view/LinkSharePageComponent.ets#L17-L159)

### 构建分享数据并分享数据

在隔空传送事件回调中调用this.immersiveLinkCallback()方法，实现分享数据构建，在链接分享场景中，发起方在构造[SharedRecord](../harmonyos-references/share-system-share.md#section20696483813)参数时，必须传入content和utd这两个属性，并通过sharableTarget.share()方法传输数据，完成隔空传送链接分享流程。

说明

* utd需设置为utd.UniformDataType.HYPERLINK，表示分享内容为链接；content设置为[配置App Linking](bpta-application-gesture-share.md#section1685558173015)章节中配置的链接，链接中拼接视频唯一标识符videoIndex。
* 为提升分享预览模板缩略图的清晰度和整体用户体验，建议开发者优先使用thumbnailUri参数设置缩略图。尽管thumbnailUri和thumbnail两个参数均可实现缩略图效果，但thumbnail参数因大小限制为32KB，实际应用中可能导致图片模糊，影响用户体验。因此，采用thumbnailUri指定高质量缩略图更为推荐。

```
1. getLinkShareData(): systemShare.SharedData {
2. // share app linking.
3. let videoData: FileData = VIDEO_SOURCES[this.videoIndex];
4. // Video thumbnail image sandbox path.
5. let filePath: string = this.context?.filesDir + `/${videoData.thumbnail}`;
6. // Get video thumbnail URI path.
7. let coverUri: string = fileUri.getUriFromPath(filePath);
8. let shareData: systemShare.SharedData = new systemShare.SharedData({
9. // Set the shared data type to Link.
10. utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
11. // The shared App Linking link is replaced with the real address here.
12. content: `https://www.example.com?videoIndex=${this.videoIndex}`,
13. thumbnailUri: coverUri,
14. title: videoData.name,
15. description: videoData.description
16. });
17. return shareData;
18. }
```

[ShareModel.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/feature/share/src/main/ets/model/ShareModel.ets#L162-L179)

### 配置App Linking

开发者可参考[使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)进行配置和使用。例如，此处配置的App Linking的链接为：www.example.com，开发者需在entry模块的module.json5中进行如下配置：

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. "name": "EntryAbility",
7. // ...
8. "exported": true,
9. "skills": [
10. {
11. "entities": [
12. "entity.system.home",
13. // entities must contain "entity.system.browsable"
14. "entity.system.browsable"
15. ],
16. "actions": [
17. "ohos.want.action.home",
18. // Actions must contain "ohos.want.action.viewData"
19. "ohos.want.action.viewData"
20. ],
21. "uris": [
22. {
23. // The scheme must be configured as https
24. "scheme": "https",
25. // The host must be configured as the associated domain name
26. "host": "www.example.com",
27. "path": ""
28. }
29. ],
30. // domainVerify must be set to true
31. "domainVerify": true
32. }
33. ]
34. }
35. ],
36. // ...
37. }
38. }
```

[module.json5](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/product/entry/src/main/module.json5#L2-L74)

### 对端跳转处理

当对端设备已安装应用并收到分享的 App Linking 链接后，系统会拉起应用。根据应用是否已在运行，有以下两种情况需处理：

应用未运行：此时跳转应用，应在onCreate()方法中获取链接中的视频唯一标识符videoIndex并存储到AppStorage中，同时存储GesturesShare\_isShareLink为true，表示当前应用通过分享系统启动，以便于跳转到隔空传送链接分享页面播放视频。

```
1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
2. // ...
3. let videoIndex = this.getVideoIndex(want);
4. if (videoIndex !== '') {
5. AppStorage.setOrCreate('GesturesShare_shareVideoIndex', Number.parseInt(videoIndex));
6. AppStorage.setOrCreate('GesturesShare_isShareLink', true);
7. }
8. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/product/entry/src/main/ets/entryability/EntryAbility.ets#L28-L43)

应用已运行：此时跳转应用，需在onNewWant()方法中获取链接中的视频唯一标识符videoIndex并存储到AppStorage中，并存储GesturesShare\_isShareLink为true，表示当前应用通过分享系统启动，以便于跳转到隔空传送链接分享页面播放视频。

```
1. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
2. let videoIndex = this.getVideoIndex(want);
3. if (videoIndex !== '') {
4. AppStorage.setOrCreate('GesturesShare_shareVideoIndex', Number.parseInt(videoIndex));
5. AppStorage.setOrCreate('GesturesShare_isShareLink', true);
6. }
7. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/product/entry/src/main/ets/entryability/EntryAbility.ets#L47-L53)

getVideoIndex()通过want参数获取分享链接中的参数。

```
1. private getVideoIndex(want: Want): string {
2. try {
3. let uri = want?.uri;
4. let videoIndex: string = '';
5. // Parse the parameters to obtain the app linking
6. if (uri) {
7. let urlObject = url.URL.parseURL(want?.uri);
8. videoIndex = urlObject.params.get('videoIndex') as string;
9. hilog.info(0x0000, 'GesturesShare', `getAid aid:${videoIndex}`);
10. }
11. return videoIndex;
12. } catch (err) {
13. let error = err as BusinessError;
14. hilog.error(0x0000, 'GesturesShare', `Failed to getVideoIndex, error: ${error.code} ${error.message}`);
15. }
16. return '';
17. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/product/entry/src/main/ets/entryability/EntryAbility.ets#L57-L73)

在应用首页判断GesturesShare\_isShareLink是否为true，若为true则跳转至隔空传送链接分享页面。

```
1. onPageShow(): void {
2. if (this.isShareLink) {
3. this.pageInfos.pushPathByName('LinkSharePage', null, true);
4. }
5. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/GesturesShare/blob/master/product/entry/src/main/ets/pages/Index.ets#L37-L41)

## 常见问题

### 数据在分享过程中被丢弃或者提示无效的数据类型

分享服务支持链接分享和文件分享两种场景，但不支持两者混合分享。在混合分享时，数据可能会在分享过程中丢失或提示无效的数据类型。详情可参考[分享数据类型不支持](../harmonyos-guides/share-faq-2.md)。

## 示例代码

* [基于Share Kit实现隔空传送分享文件和链接](https://gitcode.com/harmonyos_samples/GesturesShare)
