---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-knock-file-share
title: 碰一碰文件分享
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 碰一碰文件分享
category: best-practices
scraped_at: 2026-04-28T08:21:46+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:361a92f01acf4c0df017432f73fe17ce7933d692d3b54c3ba4b2c16948670b28
---

## 概述

随着消费者终端设备不断增加，不同设备间进行文本分享（链接、文本等）和文件分享（图片、视频、文档等）已成为用户日常生活中不可或缺的需求。HarmonyOS通过[Share Kit（分享服务）](../harmonyos-guides/share-introduction.md)提供便捷的分享功能，其中“碰一碰”分享功能使用户能够轻松实现跨设备分享。本文将重点介绍应用如何实现碰一碰文件分享。

## 特性体验

目前HarmonyOS 6.0.0 Beta1及以上版本的手机和PC支持两种触碰形式：手机碰手机和手机碰PC。由于设备形态和操作系统的限制，这两种形式具有不同的特性和体验。

说明

手机与手机碰一碰对华为账号无要求，而手机与PC/2in1碰一碰则需登录同一华为账号方可进行分享。

|  | 手机碰手机 | 手机碰PC |
| --- | --- | --- |
| 手机发送 | 通过手机顶部的相碰触发，文件被设备接收，接收端将媒体文件存储到图库中，非媒体文件存储到文件管理器中。 | 通过手机顶部与PC窗口的相碰触发，使用约束详见手机与PC/2in1碰一碰分享[概述](../harmonyos-guides/knock-share-pc-phones-overview.md)使用约束章节，文件应被窗口所属的应用接收，统一存储入沙箱文件中。 |
| 手机接收 | 通过手机顶部与PC窗口的相碰触发，使用约束详见手机与PC/2in1碰一碰分享[概述](../harmonyos-guides/knock-share-pc-phones-overview.md)使用约束章节，文件被手机设备接收，接收端将媒体文件存储到图库中，非媒体文件存储到文件管理器中。 |

## 实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/f1QxA89nSFueu_uWPggTTw/zh-cn_image_0000002447912893.png?HW-CC-KV=V1&HW-CC-Date=20260428T002138Z&HW-CC-Expire=86400&HW-CC-Sign=AEB36090716F07E0399810D790495F54C432E285DD90DC67319673C26865458F "点击放大")

碰一碰文件分享基于华为分享服务，通过手机与手机碰一碰或手机与PC/2in1屏幕碰一碰实现文件的跨端传输。应用需实现监听方法[harmonyShare.on('knockShare')](../harmonyos-references/share-harmony-share.md#section1215414133214)，用户触发碰一碰后即可分享文件至对方设备。文件接收则由分享服务按照[规则](../harmonyos-guides/share-access-one-step.md)处理，存储于图库或文件管理中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/8uUvf1TJQcOHjzvc3mqpnA/zh-cn_image_0000002414273862.png?HW-CC-KV=V1&HW-CC-Date=20260428T002138Z&HW-CC-Expire=86400&HW-CC-Sign=F4F42B2AC3A8DF1C7864A570EB6DB9244376F45D3C4AFFFAFA42306E9AC0D169 "点击放大")

PC/2in1设备除了可以默认碰一碰将文件保存到文件管理中，应用还可以注册监听文件接收接口[harmonyShare.on('dataReceive')](../harmonyos-references/share-harmony-share.md#section1365282783615)方法，手机分享的文件将存储于应用沙箱目录下。详情可参考[手机与手机碰一碰分享](../harmonyos-guides/knock-share-between-phones.md)、[手机与PC/2in1碰一碰分享](../harmonyos-guides/knock-share-pc-phones.md)。

## 开发步骤

### 发起分享

1. 分享数据构建

   在分享数据时，分享发起方需要构建[SharedRecord](../harmonyos-references/share-system-share.md#section20696483813)。在文件分享的场景中，发起方在构造此参数时，必须传入uri和utd这两个属性。其中，uri属性仅在文件分享场景中为必填项，而在内容分享场景下content属性则为必填项，uri属性不需要传值。

   说明

   * uri是指要分享的文件URI，而非文件路径，例如沙箱路径content.fileDir，应通过[fileUri.getUriFromPath()](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)获取其URI。
   * utd则是当前文件的[标准化数据类型](../harmonyos-guides/uniform-data-type-list.md)，需要传入准确的值，以便系统匹配精确的目标应用，推荐使用[uniformTypeDescriptor.getUniformDataTypeByFilenameExtension()](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgetuniformdatatypebyfilenameextension11)方法，通过给定的文件后缀名查询标准化数据类型的ID，详情可见[不同类型分享数据构建](bpta-application-knock-file-share.md#section131364139197)。

   ```
   1. /**
   2. * Knock listening callback.
   3. *
   4. * @param target After the Huawei Share event is triggered,
   5. * you can call back the parameters and share them across devices.
   6. */
   7. public immersiveCallback(target: harmonyShare.SharableTarget) {
   8. let fileShare = AppStorage.get('KnockFileShare_fileShare') as number[];
   9. let videoDataList = AppStorage.get('KnockFileShare_videoDataList') as FileData[];
   10. if (!fileShare || fileShare.length === 0) {
   11. return;
   12. }
   13. let shareData: systemShare.SharedData = new systemShare.SharedData(this.getShareRecord(videoDataList[fileShare[0]]));
   14. for (let i = 1; i < fileShare.length; i++) {
   15. try {
   16. shareData.addRecord(this.getShareRecord(videoDataList[fileShare[i]]));
   17. } catch (e) {
   18. hilog.error(0x0000, 'KnockFileShare', `addRecord failed ${JSON.stringify(e)}`);
   19. }
   20. }
   21. target.share(shareData);
   22. }

   24. /**
   25. * Get shared data.
   26. *
   27. * @param data File data to be shared.
   28. * @returns systemShare.SharedRecord.
   29. */
   30. getShareRecord(data: FileData): systemShare.SharedRecord {
   31. let suffix = '.' + data.url.split('.').pop();
   32. // Obtain the UTD through the file extension.
   33. let utd = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(suffix);
   34. hilog.info(0x0000, 'KnockFileShare', `getShareRecord utd ${utd}`)
   35. return {
   36. utd: utd,
   37. uri: data.url,
   38. thumbnailUri: data.thumbnail,
   39. title: data.name,
   40. description: data.description
   41. };
   42. }
   ```

   [KnockController.ets](https://gitcode.com/harmonyos_samples/KnockFileShare/blob/master/entry/src/main/ets/controller/KnockController.ets#L48-L89)
2. 分享注册

   [华为分享](../harmonyos-references/share-harmony-share.md)模块提供了碰一碰分享事件的监听方法[on('knockShare')](../harmonyos-references/share-harmony-share.md#section1215414133214)。在回调中调用this.immersiveCallback()方法，实现分享数据的构建，并通过sharableTarget.share()方法传输文件数据，完成碰一碰文件分享流程。

   分享模块也同样提供了取消监听的方法[off('knockShare')](../harmonyos-references/share-harmony-share.md#section18498201183311)，当应用不需要碰一碰分享文件或离开页面（包括应用退至后台等情况）时，应及时调用取消监听的方法，以避免资源浪费和异常触发。

   需要注意的是，PC端的碰一碰事件监听和取消监听需要传入窗口的ID，如immersiveListeningPC()和immersiveDisableListeningPC()方法所示。

   ```
   1. /**
   2. *  Add knock listening.
   3. */
   4. public immersiveListening() {
   5. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   6. harmonyShare.on('knockShare', (target: harmonyShare.SharableTarget) => {
   7. this.immersiveCallback(target);
   8. });
   9. }
   10. }

   12. /**
   13. *  Add knock listening in 2in1 device type.
   14. */
   15. public immersiveListeningPC() {
   16. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   17. window.getLastWindow(this.context).then((data) => {
   18. let mainWindowID: number = data.getWindowProperties().id;
   19. harmonyShare.on('knockShare', { windowId: mainWindowID }, (target: harmonyShare.SharableTarget) => {
   20. this.immersiveCallback(target);
   21. });
   22. }).catch((error: BusinessError) => {
   23. hilog.error(0x0000, 'KnockFileShare', `getLastWindow failed ${JSON.stringify(error)}`);
   24. });
   25. }
   26. }

   28. /**
   29. *  remove knock listening.
   30. */
   31. public immersiveDisableListening() {
   32. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   33. harmonyShare.off('knockShare');
   34. }
   35. }

   37. /**
   38. *  remove knock listening.
   39. */
   40. public immersiveDisableListeningPC() {
   41. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   42. window.getLastWindow(this.context).then((data) => {
   43. let mainWindowID: number = data.getWindowProperties().id;
   44. harmonyShare.off('knockShare', { windowId: mainWindowID });
   45. }).catch((error: BusinessError) => {
   46. hilog.error(0x0000, 'KnockFileShare', `getLastWindow failed ${JSON.stringify(error)}`);
   47. });
   48. }
   49. }
   ```

   [KnockController.ets](https://gitcode.com/harmonyos_samples/KnockFileShare/blob/master/entry/src/main/ets/controller/KnockController.ets#L93-L141)

### 接收文件

[华为分享](../harmonyos-references/share-harmony-share.md)模块提供了[harmonyShare.on('dataReceive')](../harmonyos-references/share-harmony-share.md#section1365282783615)方法，用于实现应用沙箱接收文件的事件监听。请注意当前接口仅在2in1设备类型可以正常调用，其他设备类型会返回801错误码。

PC/2in1应用可以通过监听harmonyShare.on('dataReceive')方法来实现应用沙箱接收文件。该方法需要传入当前应用的窗口ID，并且需要传入capabilities属性，以表示当前应用支持接收的文件标准化数据类型及其最大接收数量，该属性不能传入空数组。

在dataReceive回调方法中，通过receiveTarget.receive()传入应用接收文件的沙箱路径。当应用接收到碰一碰分享的文件后，会触发onDataReceived回调，开发者可以通过回调参数shareData.getRecords()获取分享的数据，当碰一碰接收事件结束后，将响应onResult回调，通过参数resultCode判断分享接收事件是否成功。

```
1. /**
2. * Add dataReceive listening in 2in1 device type.
3. */
4. public dataReceiveListeningPC() {
5. if (!canIUse('SystemCapability.Collaboration.HarmonyShare')) {
6. return;
7. }
8. window.getLastWindow(this.context).then(((data) => {
9. let mainWindowID: number = data.getWindowProperties().id;
10. harmonyShare.on('dataReceive', { windowId: mainWindowID, capabilities: [
11. {
12. 'utd': uniformTypeDescriptor.UniformDataType.MEDIA,
13. 'maxSupportedCount': 5
14. },
15. {
16. 'utd': uniformTypeDescriptor.UniformDataType.FILE,
17. 'maxSupportedCount': 5
18. }
19. ] },
20. (receiveTarget: harmonyShare.ReceivableTarget) => {
21. if (!this.context) {
22. return;
23. }
24. // Process the received file data.
25. receiveTarget.receive(fileUri.getUriFromPath(this.context.filesDir), {
26. onDataReceived: (shareData: systemShare.SharedData) => {
27. let shareRecords = shareData.getRecords();
28. let videoDataList = AppStorage.get('KnockFileShare_videoDataList') as FileData[];
29. shareRecords.forEach(async (record: systemShare.SharedRecord) => {
30. if (!record.uri) {
31. return;
32. }
33. // Get video thumbnails.
34. let fileName = record.uri.split('/').pop()?.split('.')[0];
35. let thumbPath: string = videoDataList[0].thumbnail;
36. if (record.uri.endsWith('mp4') || record.uri.endsWith('mkv')) {
37. thumbPath = record.uri.slice(0, record.uri.lastIndexOf('.')) + 'thumb.png';
38. let result = await new FileUtil().getVideoThumbnail(record.uri, thumbPath);
39. if (!result) {
40. thumbPath = videoDataList[0].thumbnail;
41. }
42. } else if (record.uri.endsWith('png') || record.uri.endsWith('jpg') || record.uri.endsWith('jpeg')) {
43. thumbPath = record.uri;
44. } else {
45. thumbPath = videoDataList[0].thumbnail;
46. }

48. videoDataList.push({
49. url: record.uri,
50. name: fileName,
51. description: record.description,
52. thumbnail: thumbPath,
53. index: videoDataList.length
54. });
55. });
56. },
57. onResult(resultCode: harmonyShare.ShareResultCode) {
58. if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
59. hilog.info(0x0000, 'KnockFileShare', 'receive file success');
60. } else {
61. hilog.error(0x0000, 'KnockFileShare', 'receive failed ' + resultCode);
62. }
63. }
64. });
65. });
66. })).catch((error: BusinessError) => {
67. hilog.error(0x0000, 'KnockFileShare', `failed to obtain the window. cause ${error.code} ${error.message}`);
68. });
69. }
```

[KnockController.ets](https://gitcode.com/harmonyos_samples/KnockFileShare/blob/master/entry/src/main/ets/controller/KnockController.ets#L145-L213)

## 系统拦截策略

碰一碰分享接收端接收数据时遵循统一规则，详情请参考[目标设备接收分享数据一步直达体验](../harmonyos-guides/share-access-one-step.md)。

## 不同类型分享数据构建

碰一碰文件分享需要关注文件分享类型，在[发起分享](bpta-application-knock-file-share.md#section0997243321)时作为参数传入，系统提供标准化数据类型解决跨设备传输中的数据类型模糊问题，通过统一的数据格式标识，接收端可精准识别文件属性。例如图片自动匹配图库应用接收，文档类文件定向唤起文件管理器，实现数据与处理程序的自动绑定。当传入的分享参数的utd为uniformTypeDescriptor.UniformDataType.IMAGE时，且文件确认为图片文件，接收端会默认将其存储在图库中。当传入的utd为uniformTypeDescriptor.UniformDataType.FILE时，文件会默认存储到文件管理中。系统中预置了一部分常用类型，更多类型可参考[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)。

| **后缀名** | **UTD-ID** | **MIMEType类型** | **说明** |
| --- | --- | --- | --- |
| .png | general.png | image/png | PNG图片类型。 |
| .jpg，.jpeg，.jpe | general.jpeg | image/jpeg | JPEG图片类型。 |
| .mp4，.mp4v，.mpeg4 | general.mpeg-4 | video/mp4，video/mp4v | MPEG-4视频类型。 |
| .avi，.vfw | general.avi | video/avi，video/msvideo，video/x-msvideo | AVI视频类型。 |
| .txt，.text | general.plain-text | text/plain | 未指定编码的文本类型，无修饰的文本。 |
| .doc | com.microsoft.word.doc | application/msword | Microsoft Word数据类型。 |
| .xls | com.microsoft.excel.xls | application/vnd.ms-excel | Microsoft Excel数据类型。 |
| .ppt | com.microsoft.powerpoint.ppt | application/vnd.ms-powerpoint | Microsoft PowerPoint演示文稿类型。 |
| ... | ... | ... | ... |

## 常见问题

### 数据在分享过程中被丢弃或者提示无效的数据类型

分享服务支持内容分享和文件分享两种场景，但不支持两者混合分享。在混合分享时，数据可能会在分享过程中丢失或提示无效的数据类型。详情可参考[分享数据类型不支持](../harmonyos-guides/share-faq-2.md)。

## 示例代码

* [基于Share Kit实现碰一碰文件分享](https://gitcode.com/harmonyos_samples/KnockFileShare)
