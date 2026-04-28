---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-knock-video-share
title: 碰一碰链接分享
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 碰一碰链接分享
category: best-practices
scraped_at: 2026-04-28T08:21:44+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:83e15b1d11dac9944eab479b2221fd03929ee0c0c507f997c443815236119f52
---

## 概述

随着全场景智慧生活的不断演进，跨设备内容分享已成为用户的核心需求之一。传统分享方式普遍存在操作繁琐（需手动选择设备或应用）、依赖特定网络环境、传输效率低等问题，影响用户体验。HarmonyOS提供了[Share Kit（分享服务）](../harmonyos-guides/share-kit-guide.md)，并结合[App Linking](../harmonyos-guides/applinking-introduction.md)技术，可实现内容的快速跨设备分享，直达目标应用，无需依赖第三方应用中转，提供高效、便捷、无缝的分享体验。

本文以视频分享场景为例，详细介绍碰一碰快速分享视频的原理与开发步骤。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/2a/v3/17x10pf-QrOuHaEmV4VDGw/zh-cn_media_0000002306538056.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=0A1220919DA52DF21C8DDF6DDA7C6A30F1F72E12905676756F3B70DA2AF876C2)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 4.19%

0:00

Duration 0:09

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

## 典型场景

当用户在源端（发起碰一碰操作的设备）上使用视频应用播放视频时，可通过“碰一碰”功能将该视频分享至对端（接收分享的目标设备）。根据对端是否安装视频应用以及是否配置了直达应用市场，对端收到分享的视频之后，有如下三种场景：

### 场景一：目标应用已安装

系统直接拉起目标应用视频播放页面播放视频，无需经过浏览器中转，实现一键直达，极大提高便捷度和转化率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/LzbrStyzTuqfSN1_2j9bDg/zh-cn_image_0000002307668620.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=3AADB341E74EF577D544B7CEB9C1609F00B810A370241F076C3DB7A22F2CF048 "点击放大")

### 场景二：目标应用未安装，已配置直达应用市场

当对端未安装目标应用且开发者配置了[直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)功能时，将直接跳转到应用市场的应用详情页。安装完成后，首次打开应用将通过[延迟链接](../harmonyos-guides/applinking-deferredlink.md)功能自动跳转到视频播放页面，无需用户重新搜索或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/RoejT1FcRRa6_mf5JN_iMQ/zh-cn_image_0000002340377337.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=9BA3F294AD3A3BAC8901EDF55B85ECA0A41C9A1AADC740E0692CD342A058E6C6 "点击放大")

### 场景三：目标应用未安装，未配置直达应用市场（有Web页面）

对端收到分享的视频链接之后，系统通过浏览器打开Web页面，用户可直接查看内容。在Web页面可提供“下载”按钮，引导用户安装应用获取更佳体验，安装后仍可通过[延迟链接](../harmonyos-guides/applinking-deferredlink.md)直达原内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/r6k7ReNYSUy8s6VR4F2fGg/zh-cn_image_0000002341667937.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=B1363F5C14BA3AA1FEAE9E6A658D81F974BFE8FCA88440F1E9428B3B8E9FACFA "点击放大")

说明

对于不提供Web页面的应用，建议开启[直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)功能，避免因无法访问内容而造成体验断裂。

## 实现原理

碰一碰视频分享功能主要依赖于Share Kit与App Linking实现，确保用户能够通过简单的设备接触快速分享内容并直达应用。首先，应用需要集成App Linking来保证从分享到打开的端到端体验流畅无阻，具体可参考：[使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)。

碰一碰视频分享后对端跳转目标应用的流程图如下，对端无论是否安装视频应用，用户都能获得连贯流畅的体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/3fCRh4iFT0mU0NoLrK6M0w/zh-cn_image_0000002306538072.png?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=09EED77941F74BEC72085DBD2EF66E74FBB6D22DFD6C587B7E02102690D3F082 "点击放大")

碰一碰视频分享时序图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/N0w0DP5xRlK3x9rxeIPhsw/zh-cn_image_0000002306378348.png?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=662B0209DAA68BEDE4BA5A28FFD4602599EAC31E9FD0597E2CEF67F60D5B1A81 "点击放大")

说明

碰一碰分享环境要求请参见[环境要求](../harmonyos-guides/knock-share-between-phones-overview.md#section124151731174519)。

## 开发步骤

本章将详细介绍视频应用使用碰一碰分享App Linking实现直达应用，主要开发步骤如下：

* [配置App Linking服务](bpta-application-knock-video-share.md#section97421941152319)

* [碰一碰分享事件监听/取消](bpta-application-knock-video-share.md#section1261410588212)
* [加载预览图和发起分享](bpta-application-knock-video-share.md#section89721840192313)
* [对端跳转处理](bpta-application-knock-video-share.md#section3655631162511)

### 配置App Linking服务

为了通过碰一碰分享实现直达应用的功能，应用需集成App Linking，以确保端到端体验的完整性。当碰一碰分享成功，对端收到源端分享的App Linking链接后，系统将根据链接配置自动拉起对应应用或浏览器，从而继续播放视频。

App Linking的配置和使用开发者可以参考[使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)。例如这里配置的App Linking的链接为：https://www.example.com，开发者需要在entry模块的module.json5进行如下配置：

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

[module.json5](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/module.json5#L2-L73)

### 碰一碰分享事件监听/取消

在视频播放页面中添加碰一碰分享事件的监听与取消功能前，需先使用[canIUse()](../harmonyos-references/js-apis-syscap.md#caniuse)接口判断设备是否支持该能力。下面将碰一碰分享的相关逻辑代码封装至KnockController类文件中，使碰一碰逻辑与UI界面分离，便于代码维护。

KnockController用于管理碰一碰事件监听的添加与取消，以及分享功能，支持手机和PC端碰一碰分享。它封装了[harmonyShare（华为分享）](../harmonyos-references/share-harmony-share.md)模块的相关方法，将碰一碰分享事件的监听[on('knockShare')](../harmonyos-references/share-harmony-share.md#section1215414133214)、取消监听[off('knockShare')](../harmonyos-references/share-harmony-share.md#section18498201183311)以及分享功能[share()](../harmonyos-references/share-harmony-share.md#section1862171812120)分别进行了封装。需要注意的是PC端碰一碰事件的监听和取消监听需要传入窗口的ID，如immersiveListeningPC()和immersiveDisableListeningPC()方法所示。

```
1. import { harmonyShare, systemShare } from '@kit.ShareKit';
2. import { fileUri } from '@kit.CoreFileKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { uniformTypeDescriptor } from '@kit.ArkData';
5. import { common } from '@kit.AbilityKit';
6. // ...
7. export class KnockController {
8. private static controller: KnockController;
9. private context: common.UIAbilityContext | undefined = undefined;
10. // Knock listening status
11. private isKnockListening: boolean = false;

13. public static getInstance(context: common.UIAbilityContext): KnockController {
14. if (!KnockController.controller) {
15. KnockController.controller = new KnockController(context);
16. }
17. return KnockController.controller;
18. }

20. constructor(context: common.UIAbilityContext) {
21. this.context = context;
22. }

24. /**
25. * knock listening callback
26. * @param target After the Huawei Share event is triggered,
27. * you can call back the parameters and share them across devices.
28. */
29. public immersiveCallback(target: harmonyShare.SharableTarget) {
30. // ...
31. }

33. /**
34. *  Add knock listening
35. */
36. public immersiveListening() {
37. if (canIUse('SystemCapability.Collaboration.HarmonyShare') && !this.isKnockListening) {
38. harmonyShare.on('knockShare', (target: harmonyShare.SharableTarget) => {
39. this.immersiveCallback(target);
40. });
41. this.isKnockListening = true;
42. }
43. }

45. /**
46. *  remove knock listening
47. */
48. public immersiveDisableListening() {
49. if (canIUse('SystemCapability.Collaboration.HarmonyShare') && this.isKnockListening) {
50. harmonyShare.off('knockShare');
51. this.isKnockListening = false;
52. }
53. }

55. /**
56. *  Add knock listening in 2in1 device type.
57. */
58. public immersiveListeningPC() {
59. try {
60. if (canIUse('SystemCapability.Collaboration.HarmonyShare') && !this.isKnockListening) {
61. window.getLastWindow(this.context).then((data) => {
62. let mainWindowID: number = data.getWindowProperties().id;
63. harmonyShare.on('knockShare', { windowId: mainWindowID }, (target: harmonyShare.SharableTarget) => {
64. this.immersiveCallback(target);
65. });
66. })

68. this.isKnockListening = true;
69. }
70. } catch (err) {
71. let error = err as BusinessError;
72. Logger.error(TAG, `getWindowProperties err, errCode: ${error.code}, error mesage: ${error.message}`);
73. }
74. }

76. /**
77. *  Remove knock listening in 2in1 device type.
78. */
79. public immersiveDisableListeningPC() {
80. try {
81. if (canIUse('SystemCapability.Collaboration.HarmonyShare') && this.isKnockListening) {
82. window.getLastWindow(this.context).then((data) => {
83. let mainWindowID: number = data.getWindowProperties().id;
84. harmonyShare.off('knockShare', { windowId: mainWindowID });
85. })

87. this.isKnockListening = false;
88. }
89. } catch (err) {
90. let error = err as BusinessError;
91. Logger.error(TAG, `getWindowProperties err, errCode: ${error.code}, error mesage: ${error.message}`);
92. }
93. }
94. }
```

[KnockController.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/controller/KnockController.ets#L17-L145)

根据前文所述场景，碰一碰分享功能主要用于视频播放页面，因此需在VideoPlay.ets中添加相应的事件监听与取消操作。进入页面时，在aboutToAppear()和onPageShow()回调中注册监听；离开页面（包括应用退至后台等情况）时，比如在onPageHide()方法中及时调用immersiveDisableListening()方法取消监听，避免资源浪费和异常触发。

```
1. import { common } from '@kit.AbilityKit';
2. import { KnockController } from '../controller/KnockController';
3. // ...
4. @Entry
5. @Component
6. struct VideoPlay {
7. // ...
8. aboutToAppear(): void {
9. // ...
10. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
11. this.knockController = KnockController.getInstance(context);
12. if (deviceInfo.deviceType === '2in1') {
13. this.knockController?.immersiveListeningPC();
14. } else {
15. this.knockController?.immersiveListening();
16. }
17. }
18. // ...
19. onPageShow(): void {
20. if (deviceInfo.deviceType === '2in1') {
21. this.knockController?.immersiveListeningPC();
22. } else {
23. this.knockController?.immersiveListening();
24. }
25. }

27. onPageHide(): void {
28. if (deviceInfo.deviceType === '2in1') {
29. this.knockController?.immersiveDisableListeningPC();
30. } else {
31. this.knockController?.immersiveDisableListening();
32. }
33. }

35. aboutToDisappear(): void {
36. if (deviceInfo.deviceType === '2in1') {
37. this.knockController?.immersiveDisableListeningPC();
38. } else {
39. this.knockController?.immersiveDisableListening();
40. }
41. this.videoIndex=0;
42. // ...
43. }
44. // ...
45. }
```

[VideoPlay.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/pages/VideoPlay.ets#L19-L143)

说明

收到碰一碰分享事件回调后，需尽快调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#section1862171812120)方法发起分享，超过3秒可能会失败。

### 加载预览图和发起分享

收到碰一碰事件分享回调后，调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#section1862171812120)方法发起分享，并设置分享卡片的信息，包括标题（title）、描述（description）和缩略图URI（thumbnailUri）。这些参数将用于生成特定的卡片模板，详情可参考[通过分享面板发起分享](../harmonyos-guides/share-mobilephone-app-share.md)。

utd需要设置为utd.UniformDataType.HYPERLINK，表示分享的内容为链接；content设置为[配置App Linking服务](bpta-application-knock-video-share.md#section97421941152319)章节中配置的链接，链接中拼接视频的唯一标识符videoIndex。

```
1. /**
2. * knock listening callback
3. * @param target After the Huawei Share event is triggered,
4. * you can call back the parameters and share them across devices.
5. */
6. public immersiveCallback(target: harmonyShare.SharableTarget) {
7. // share app linking
8. try {
9. let videoIndex: number = AppStorage.get('videoIndex') as number;
10. let videoData: VideoData = VIDEO_SOURCES[videoIndex];
11. // Video thumbnail image sandbox path
12. let filePath: string = this.context?.filesDir + `/${videoData.head}`;
13. // Get video thumbnail URI path
14. let coverUri: string = fileUri.getUriFromPath(filePath);
15. let shareData: systemShare.SharedData = new systemShare.SharedData({
16. // Set the shared data type to Link
17. utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
18. // The shared App Linking link is replaced with the real address here
19. content: `https://www.example.com?videoIndex=${videoIndex}`,
20. thumbnailUri: coverUri,
21. title: videoData.name,
22. description: videoData.description
23. });
24. // Initiate a share
25. target.share(shareData).then(() => {
26. Logger.info(TAG, 'Share link success');
27. }).catch((error: BusinessError) => {
28. Logger.error(TAG, `Share link  error. code: ${error.code}, message: ${error.message}`);
29. });
30. } catch (err) {
31. Logger.error(TAG, `Share link exception. code: ${err.code}, message: ${err.message}`);
32. }
33. }
```

[KnockController.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/controller/KnockController.ets#L47-L81)

说明

为了提升分享预览模板缩略图的清晰度和整体用户体验，建议开发者优先使用thumbnailUri参数来设置缩略图。虽然thumbnailUri和thumbnail两个参数均可用于实现缩略图效果，但是thumbnail参数由于大小限制为32KB，在实际应用中可能会导致图片模糊不清，从而影响用户体验。因此，采用thumbnailUri来指定高质量的缩略图是更为推荐的做法。

thumbnailUri仅支持沙箱文件URI或用户文件URI。若需将网络图片作为缩略图，请先将其下载并保存至应用沙箱内。下面的代码示例展示了如何将media目录下的图片保存到应用沙箱路径中，以便于后续图片分享操作。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import { Logger } from './Logger';
4. import { fileIo } from '@kit.CoreFileKit';

6. const TAG = 'ImageUtil';

8. export class ImageUtil {
9. /**
10. * Save image to sandbox.
11. * @param context UIAbility Context.
12. */
13. public static saveImage(context: common.UIAbilityContext) {
14. try {
15. [
16. [context.resourceManager.getMediaContentSync($r('app.media.video_cover_0').id), '/video_cover_0.png'],
17. [context.resourceManager.getMediaContentSync($r('app.media.video_cover_1').id), '/video_cover_1.png'],
18. [context.resourceManager.getMediaContentSync($r('app.media.video_cover_2').id), '/video_cover_2.png'],
19. [context.resourceManager.getMediaContentSync($r('app.media.video_cover_3').id), '/video_cover_3.png']
20. ].forEach(item => {
21. let file: fileIo.File | undefined = undefined;
22. try {
23. file = fileIo.openSync(context.filesDir + item[1], fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
24. let writeLen = fileIo.writeSync(file.fd, (item[0] as Uint8Array).buffer);
25. Logger.info(TAG, `write data to file succeed and size is: ${writeLen}`);
26. } catch (err) {
27. Logger.error(TAG, `Failed to save image. code: ${err.code}, message: ${err.message}`);
28. } finally {
29. fileIo.closeSync(file);
30. }
31. })
32. } catch (err) {
33. let error = err as BusinessError;
34. Logger.error(TAG, `saveImage err, errCode: ${error.code}, error mesage: ${error.message}`);
35. }
36. }
37. }
```

[ImageUtil.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/utils/ImageUtil.ets#L17-L53)

卡片效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/D9cWbqHZRA-jhQX3E0ZO9w/zh-cn_image_0000002340377341.png?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=70BD3C0B9E94E1A1A436072965370ECEB97A445B9E6727387EFB7150D5C9A9EF "点击放大")

### 对端跳转处理

1. 拉起应用

   对端收到分享的App Linking之后，系统拉起应用时有以下两种情况：

   1. 应用未在后台运行：此时跳转应用，应在onCreate()方法中获取链接中的视频唯一标识符videoIndex。

      ```
      1. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
      2. import { BusinessError } from '@kit.BasicServicesKit';
      3. import { window } from '@kit.ArkUI';
      4. import { url } from '@kit.ArkTS';
      5. import { Logger } from '../utils/Logger';

      7. const TAG = 'EntryAbility';
      8. export default class EntryAbility extends UIAbility {
      9. private uiContext: UIContext | undefined = undefined;
      10. private mVideoIndex: string = '';

      12. private getVideoIndex(want: Want): string {
      13. let uri = want?.uri;
      14. let videoIndex: string = '';
      15. // Parse the parameters to obtain the app linking
      16. if (uri) {
      17. try {
      18. let urlObject = url.URL.parseURL(want?.uri);
      19. videoIndex = urlObject.params.get('videoIndex') as string;
      20. } catch (err) {
      21. let error = err as BusinessError;
      22. Logger.error(TAG, `parseURL err, errCode: ${error.code}, error mesage: ${error.message}`);
      23. }
      24. Logger.info(TAG, `getAid aid:${videoIndex}`);
      25. }
      26. return videoIndex;
      27. }
      28. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      29. // ...
      30. this.mVideoIndex = this.getVideoIndex(want);
      31. }
      32. // ...
      33. }
      ```

      [EntryAbility.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L16-L127)

      在onWindowStageCreate()回调中使用windowStage.loadContent()方法加载详情页的URL为“pages/VideoPlay”。

      ```
      1. onWindowStageCreate(windowStage: window.WindowStage): void {
      2. // ...
      3. let pageUrl: string = 'pages/Index';
      4. if (this.mVideoIndex && this.mVideoIndex !== '') {
      5. AppStorage.setOrCreate('videoIndex', Number.parseInt(this.mVideoIndex));
      6. pageUrl = 'pages/VideoPlay';
      7. }

      9. windowStage.loadContent(pageUrl, (err) => {
      10. // ...
      11. try {
      12. let windowObj = windowStage.getMainWindowSync();
      13. this.uiContext = windowObj.getUIContext();
      14. } catch (err) {
      15. let error = err as BusinessError;
      16. Logger.error(TAG, `getMainWindowSync err, errCode: ${error.code}, error mesage: ${error.message}`);
      17. }
      18. });
      19. }
      ```

      [EntryAbility.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L61-L88)
   2. 应用已在后台运行：此时跳转应用，需在onNewWant()方法中获取链接中的视频唯一标识符 videoIndex，并通过 UIContext.getRouter().pushUrl() 实现页面跳转。

      ```
      1. export default class EntryAbility extends UIAbility {
      2. private uiContext: UIContext | undefined = undefined;
      3. private mVideoIndex: string = '';

      5. private getVideoIndex(want: Want): string {
      6. // ...
      7. }
      8. // ...
      9. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      10. let videoIndex: string = this.getVideoIndex(want);
      11. if (videoIndex && videoIndex !== '') {
      12. let page = this.uiContext?.getRouter().getState();
      13. if (page?.name === 'VideoPlay') {
      14. AppStorage.setOrCreate('videoIndex', Number.parseInt(videoIndex));
      15. } else {
      16. this.uiContext?.getRouter().pushUrl({
      17. url: 'pages/VideoPlay',
      18. params: {
      19. videoIndex: videoIndex
      20. }
      21. }).catch((error: BusinessError) => {
      22. Logger.error(TAG, `pushUrl err, errCode: ${error.code}, error mesage: ${error.message}`);
      23. });
      24. }
      25. }
      26. }
      27. // ...
      28. }
      ```

      [EntryAbility.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L24-L128)
   3. 获取视频的唯一标识符videoIndex后，在视频播放页面根据该videoIndex并播放相应的视频内容。

      ```
      1. @Entry
      2. @Component
      3. struct VideoPlay {
      4. // ...
      5. @StorageLink('videoIndex') videoIndex: number = 0;
      6. // ...
      7. aboutToAppear(): void {
      8. let params = this.getUIContext().getRouter().getParams() as Record<string, string>;
      9. if (params && params.videoIndex) {
      10. this.videoIndex = Number.parseInt(params.videoIndex);
      11. }
      12. // ...
      13. }
      14. // ...
      15. build() {
      16. Column() {
      17. VideoPlayingView({
      18. videoList: VIDEO_SOURCES,
      19. videoIndex: this.videoIndex
      20. })
      21. // ...
      22. }
      23. .width('100%')
      24. }
      25. }
      ```

      [VideoPlay.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/pages/VideoPlay.ets#L32-L142)
2. 配置直达应用市场与延迟链接

   为提升用户未安装应用时的体验，可配置[直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)功能，引导用户下载安装应用。配置完成后，当对端收到源端分享的App Linking链接时，若设备未安装目标应用，系统将直接跳转至应用市场的应用详情页，支持一键下载安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/BpkkL53dSTSYMUmELxOr7Q/zh-cn_image_0000002340497529.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=39A6E3B7691AFD7EAEE7AA3588CCACFD4D8E133A17789E626C223ED2188229B6 "点击放大")

   同时，需要实现[延迟链接](../harmonyos-guides/applinking-deferredlink.md)功能，确保安装后首次启动可直达内容。安装完应用之后，开发者可以在用户首次打开应用时，使用延迟链接，直接跳转到视频播放页面，这一流程不仅优化了用户体验，还有助于提升链接的转化率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/WfMoeo_VTli_VK4xI1_pgQ/zh-cn_image_0000002306538076.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=E2049FB9BBB921CDC77A6731D1C709E5AC05F16B2DF55D43F993559343699E28 "点击放大")

   通过[deferredLink.popDeferredLink()](../harmonyos-references/applinking-deferredlink-api.md#section15555111210233)接口获取原始App Linking链接，并根据解析该链接直接跳转至视频播放页面。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // ...
   5. aboutToAppear(): void {
   6. // ...
   7. //Get the deferred link parameter and go to video play page
   8. deferredLink.popDeferredLink()
   9. .then((link: string) => {
   10. Logger.info(TAG, `Succeeded in getting deferred link, result: ${link}`);
   11. const videoIndex = url.URL.parseURL(link)?.params?.get('videoIndex') as string;
   12. if (videoIndex) {
   13. this.getUIContext().getRouter().pushUrl({
   14. url: 'pages/VideoPlay',
   15. params: { videoIndex }
   16. });
   17. }
   18. }).catch((error: BusinessError) => {
   19. Logger.error(TAG, `Failed to get deferred link. code: ${error.code}, message: ${error.message}`);
   20. });
   21. }
   22. // ...
   23. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/knock-share/blob/master/entry/src/main/ets/pages/Index.ets#L27-L116)
3. Web页面开发与部署

   当应用未安装且未配置直达应用市场时，系统会打开浏览器加载视频播放Web页面来播放视频，保证应用在未安装的情况下也能体验播放视频功能，特别是与[延迟链接](../harmonyos-guides/applinking-deferredlink.md)结合使用，详细请参见[Web页面开发与部署（可选）](bpta-social-share.md#section157709544229)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/bDlYdkZ1TQe0KA-Fbm55Ow/zh-cn_image_0000002306378360.png?HW-CC-KV=V1&HW-CC-Date=20260428T002137Z&HW-CC-Expire=86400&HW-CC-Sign=1C25EB90F56E84F0B6D0EDED3F962C140650509BB73632808838DC4E5A3E6C27 "点击放大")

## 常见问题

### 碰一碰分享后，目标应用无法拉起、Web视频播放页面无法跳转异常等

对端成功接收到源端分享的App Linking链接，但是未拉起目标应用，具体请查看[AGC上显示了配置成功，但是配置到目标方后无法拉起如何解决](bpta-social-share.md#section1057235918212)。Web视频播放页面跳转异常请参考[Web页面跳转应用异常](bpta-social-share.md#section129769325414)。

更多关于碰一碰分享之后对端跳转问题请参考[社交分享跳转：常见问题](bpta-social-share.md#section1181324774617)。

### 碰一碰分享预览图模糊

碰一碰预览图模糊不清，可能是因为图片本身画质低或者使用了thumbnail参数来设置预览图，这种情况需要更换更高质量的图片，优先使用thumbnailUri参数来设置缩略图。因为thumbnail仅支持32KB以下大小的图片，无法保证预览图的高清。

## 示例代码

* [基于Share Kit实现碰一碰视频快速分享](https://gitcode.com/harmonyos_samples/knock-share)
