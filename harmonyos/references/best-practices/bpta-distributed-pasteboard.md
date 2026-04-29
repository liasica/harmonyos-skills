---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-distributed-pasteboard
title: 跨设备剪贴板常见场景
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 跨设备剪贴板常见场景
category: best-practices
scraped_at: 2026-04-29T14:12:41+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:0226fd0650d1edb65e0f4b3d7b0ac1878d9e3ceb9255cfccf755b46b2edeb31e
---

## 概述

剪贴板分为本地剪贴板和跨设备剪贴板，本地剪贴板提供设备内的内容复制粘贴，跨设备剪贴板提供跨设备的内容复制粘贴。跨设备剪贴板通过全场景协同能力同步剪贴板内容，实现手机、PC/2in1、平板等设备间的无缝数据互通。

当用户拥有多台设备时，可以通过跨设备剪贴板的功能，在A设备的应用上复制一段内容，粘贴到B设备的应用中，高效地完成多设备间的内容共享，其核心价值在于提升多设备协作效率。

## 实现原理

**场景分析**

1. 用户在设备A复制数据，写入到系统剪贴板服务。

2. 系统剪贴板服务将处理相关数据，并完成数据同步，此过程开发者不感知。

3. 用户在设备B读取系统剪贴板内容，粘贴来自设备A的数据。

详细的使用限制可参考[跨设备剪贴板开发指导](../harmonyos-guides/distributed-pasteboard-guide.md#section17575828642)。

**关键技术**

在开发跨设备剪贴板的功能时，系统将自动完成跨设备的数据传递，应用可根据实际需求，接入跨设备剪贴板，完成跨设备剪贴板的开发，具体运作机制可参考：[跨设备剪贴板特性简介](../harmonyos-guides/distributed-pasteboard-overview.md#section1047015015477)。

## 开发流程

跨设备剪贴板的开发流程主要包括以下两个步骤：

1. 设备A复制数据，写入剪贴板服务：将需要存入系统剪贴板的数据转换为系统剪贴板可接受的通用格式，调用[SystemPasteboard.setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法，将数据写入系统剪贴板。
2. 设备B粘贴数据，读取剪贴板内容：可以[使用粘贴控件](../harmonyos-guides/pastebutton.md)获得临时授权直接读取剪贴板数据。或申请系统剪贴板权限[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)后，使用[@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md#systempasteboard)接口读取剪贴板数据。具体开发步骤请参考[访问剪贴板内容](../harmonyos-guides/get-pastedata-permission-guidelines.md#访问剪贴板内容)。

下文将通过[粘贴分享直达](bpta-distributed-pasteboard.md#section1146419501282)场景、[多样式复制粘贴](bpta-distributed-pasteboard.md#section91711442235)场景、[进度条接入](bpta-distributed-pasteboard.md#section58295561239)场景，详细介绍跨设备剪贴板开发过程中常见场景的开发实现流程。

## 分享直达

用户在任意应用（如短信、浏览器等）中复制包含特定标识的文本（如活动口令、订单号或链接等），随后打开目标应用（如商城应用、服务应用），应用能自动识别复制文本中预设的关键字或编码。应用在校验关键字格式、时效性或用户权限通过后，弹窗或直接跳转至关联的活动页面、订单详情页或其他特定功能模块。例如用户复制短信中的活动链接，打开商城应用后自动跳转至促销活动页，无需手动搜索或点击多级菜单。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/29/v3/ZipMcLnaQz2U9rF5Sb7IuA/zh-cn_media_0000002429043485.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061240Z&HW-CC-Expire=86400&HW-CC-Sign=A37BFA3E92E6CCE353CEE8DA4DA8ED7E729E5FACBE910D072A4A8FEEEA5D3510)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 7.56%

0:00

Duration 0:10

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

**构建****数据存入剪贴板**

使用createData()创建一个包含单URI类型的pasteData数据。使用[setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法将pasteData数据写入系统剪贴板。

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'PageABuilder');
2. let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
3. await systemPasteboard.setData(pasteData);
```

[PageA.ets](https://gitcode.com/harmonyos_samples/pasteboard/blob/master/entry/src/main/ets/pages/PageA.ets#L39-L41)

**读取剪贴板数据实现跳转**

由于应用读取系统剪贴板的权限[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)是受限访问的，因此需要先通过AGC平台申请此权限，才能获取系统剪贴板内的数据。具体申请权限的流程可参考[使用ACL的签名配置指导](../harmonyos-guides/ide-signing.md#section89479413571)。

首先，应用在启动时或从后台进入前台时，在[onPageShow()](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)生命周期中检查系统剪贴板中是否包含URI类型数据。URI类型数据存在时检查权限ohos.permission.READ\_PASTEBOARD是否已授权。确认权限授权后，使用[getData()](../harmonyos-references/js-apis-pasteboard.md#getdata9)方法获取系统剪贴板内的数据，并使用[getPrimaryUri()](../harmonyos-references/js-apis-pasteboard.md#getprimaryuri7)方法获取单URI类型的数据。校验数据格式正确后，拉起弹窗询问用户是否需要执行跳转。

```
1. onPageShow(): void {
2. let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
3. try {
4. let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_URI);
5. if (result) {
6. this.checkPermissionGrant();
7. }
8. } catch (error) {
9. const err: BusinessError = error as BusinessError;
10. hilog.error(0x0000, '[Home]',
11. `Check data type failed. Code is ${err.code}, message is ${err.message}`);
12. }
13. }

15. checkPermissionGrant(): void {
16. let hasPermission = false;
17. let tokenId: number = 0;
18. try {
19. let bundleInfo: bundleManager.BundleInfo =
20. bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
21. let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
22. tokenId = appInfo.accessTokenId;
23. } catch (error) {
24. const err: BusinessError = error as BusinessError;
25. hilog.error(0x0000, '[Home]',
26. `Failed to get bundle info for self. Code is ${err.code}, message is ${err.message}`);
27. }

29. try {
30. let atManager = abilityAccessCtrl.createAtManager();
31. let approximatelyLocation = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.READ_PASTEBOARD');
32. hasPermission = approximatelyLocation === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
33. } catch (error) {
34. const err: BusinessError = error as BusinessError;
35. hilog.error(0x0000, '[Home]', `Failed to check access token. Code is ${err.code}, message is ${err.message}`);
36. }
37. if (hasPermission) {
38. let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
39. systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
40. this.uri = pasteData.getPrimaryUri();
41. if (this.uri === 'PageABuilder' || this.uri === 'PageBBuilder') {
42. this.dialogControllerImage.open();
43. }
44. }).catch((err: BusinessError) => {
45. hilog.error(0x0000, '[Home]', 'Failed to get PasteData. Cause: ' + err.message);
46. })
47. } else {
48. hilog.error(0x0000, '[Home]', 'The app is not authorized.');
49. this.requestPermissionsFn();
50. }
51. }
```

[Home.ets](https://gitcode.com/harmonyos_samples/pasteboard/blob/master/entry/src/main/ets/pages/Home.ets#L34-L84)

## 多样式复制粘贴

随着富文本数据接入不同设备，为了使复制的数据能够被更多的设备B识别，设备A需要将同一份数据的多种样式存入剪贴板中。如设备A图文混排的富文本数据可以按[纯文本类型（'text/plain'）](../harmonyos-references/js-apis-pasteboard.md#常量)、包含文字样式及图片的[HTML类型（'text/html'）](../harmonyos-references/js-apis-pasteboard.md#常量)、[纯图片类型（'pixelMap'）](../harmonyos-references/js-apis-pasteboard.md#常量)等多种类型存入剪贴板。设备B选择需要的类型读取对应类型的数据，然后实现粘贴操作。剪贴板支持的数据类型请参考[@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md#常量)。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/e4/v3/Z0feEUAmRlaijgzVxJe8tg/zh-cn_media_0000002429163385.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061240Z&HW-CC-Expire=86400&HW-CC-Sign=76DC6B3DA8CE406904A9939E8FDC0F6F813BAA752A58C50526540FB7CF3C9525)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 10.87%

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

**构建数据存入剪贴板**

创建[PasteData](../harmonyos-references/js-apis-pasteboard.md#pastedata)类型对象pasteData，通过[PasteData.getRecord()](../harmonyos-references/js-apis-pasteboard.md#getrecord9)方法获取数据条目[PasteDataRecord](../harmonyos-references/js-apis-pasteboard.md#pastedatarecord7)。本示例中使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件实现富文本数据的初始化，开发者可以选择其他富文本实现方案读取粘贴富文本数据。使用初始化RichEditor组件[RichEditorStyledStringController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringcontroller12)控制器的[getStyledString()](../harmonyos-references/ts-basic-components-richeditor.md#getstyledstring12)方法获取富文本框内的数据。根据需要的数据类型，使用[PasteDataRecord.addEntry()](../harmonyos-references/js-apis-pasteboard.md#addentry14)方法向条目中添加多种类型的数据。最后，调用[setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法将包含多样式数据的对象pasteData存入系统剪贴板。需要注意，PasteDataRecord 仅支持单个PixelMap数据传输，如需传输多个PixelMap，需要向PasteData中存入多个PasteDataRecord分别保存PixelMap。

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, '');
2. let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);

4. let styledString: StyledString = this.editController.getStyledString();
5. let html: string = StyledString.toHtml(styledString);

7. record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
8. record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, styledString.getString());
9. const htmlSpans = this.pastePixelMapController.fromStyledString(styledString);
10. if (!htmlSpans || htmlSpans.length < 1) {
11. return;
12. }
13. for (let i = 0; i < htmlSpans.length; i++) {
14. const span = htmlSpans[i];
15. if (!!(span as RichEditorImageSpanResult)?.valuePixelMap) {
16. const pixelMap = (span as RichEditorImageSpanResult)?.valuePixelMap;
17. record.addEntry(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
18. break;
19. }
20. }

22. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
23. await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
24. hilog.error(0x0000, '[PasteBoard]',
25. `Failed to set pastedata. Code: ${err.code}, message: ${err.message}`);
26. });
```

[PasteBoard.ets](https://gitcode.com/HarmonyOS_Samples/pasteboard/blob/master/entry/src/main/ets/pages/PasteBoard.ets#L212-L237)

**实现多样式数据读取**

1. 数据写入系统剪贴板后，通过[粘贴控件](../harmonyos-guides/pastebutton.md)获得临时授权读取剪贴板数据。直接点击粘贴按钮，使用[getData()](../harmonyos-references/js-apis-pasteboard.md#getdata9)方法，即可直接读取系统剪贴板的内容。

   ```
   1. PasteButton()
   2. // ...
   3. .onClick(async (_event: ClickEvent, result: PasteButtonOnClickResult) => {
   4. if (result === PasteButtonOnClickResult.SUCCESS) {
   5. try {
   6. // ...
   7. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
   8. let gettedData = await systemPasteBoard.getData();
   9. // ...
   10. } catch {
   11. (err: BusinessError) => {
   12. hilog.error(0x0000, '[PasteBoard]', `getData error.code: ${err.code}, message: ${err.message}`);
   13. }
   14. }
   15. }
   16. })
   ```

   [PasteBoard.ets](https://gitcode.com/harmonyos_samples/pasteboard/blob/master/entry/src/main/ets/pages/PasteBoard.ets#L116-L200)
2. 对于存储在系统剪贴板中的多样式数据，使用[PasteDataRecord.getValidTypes()](../harmonyos-references/js-apis-pasteboard.md#getvalidtypes14)方法获取剪贴板中数据类型与传入参数类型的交集的数据类型数组，交集结果表示请求的类型在剪贴板中存在。遍历数据类型数组，使用[PasteDataRecord.getData()](../harmonyos-references/js-apis-pasteboard.md#getdata14)方法获取对应类型的数据，通过不同RichEditor组件的控制器，实现不同类型数据的粘贴。请注意若剪贴板中不存在请求的数据类型，则对应类型的粘贴操作无法执行，对应RichEditor组件中内容不做更新。

   ```
   1. PasteButton()
   2. // ...
   3. .onClick(async (_event: ClickEvent, result: PasteButtonOnClickResult) => {
   4. if (result === PasteButtonOnClickResult.SUCCESS) {
   5. try {
   6. // ...
   7. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
   8. let gettedData = await systemPasteBoard.getData();
   9. if (gettedData.getRecordCount() <= 0) {
   10. return;
   11. }

   13. let isPastedSuccess: boolean = false;
   14. for (let i = 0; i < gettedData.getRecordCount(); i++) {
   15. let record = gettedData.getRecord(i);
   16. let targetTypes: string[] = [
   17. pasteboard.MIMETYPE_TEXT_HTML,
   18. pasteboard.MIMETYPE_TEXT_PLAIN,
   19. pasteboard.MIMETYPE_PIXELMAP
   20. ];
   21. let tmpTypes: string[] = record.getValidTypes(targetTypes);
   22. for (let j = 0; j < tmpTypes.length; j++) {
   23. switch (tmpTypes[j]) {
   24. case pasteboard.MIMETYPE_TEXT_HTML: {
   25. let htmlRecord = await record.getData(pasteboard.MIMETYPE_TEXT_HTML);
   26. htmlRecord = htmlRecord as string;
   27. this.handlerPasteHtmlData(htmlRecord);
   28. isPastedSuccess = true;
   29. break;
   30. }
   31. case pasteboard.MIMETYPE_TEXT_PLAIN: {
   32. let textRecord = await record.getData(pasteboard.MIMETYPE_TEXT_PLAIN);
   33. textRecord = textRecord as string;
   34. let styledString = new StyledString(textRecord);
   35. this.pasteTextController.setStyledString(styledString);
   36. isPastedSuccess = true;
   37. break;
   38. }
   39. case pasteboard.MIMETYPE_PIXELMAP: {
   40. let pixelMapRecord = await record.getData(pasteboard.MIMETYPE_PIXELMAP);
   41. pixelMapRecord = pixelMapRecord as PixelMap;
   42. this.pastePixelMapController.deleteSpans();
   43. this.pastePixelMapController.addImageSpan(pixelMapRecord, {
   44. imageStyle: {
   45. size: ['57px', '57px']
   46. }
   47. });
   48. isPastedSuccess = true;
   49. break;
   50. }
   51. default:
   52. break;
   53. }
   54. }
   55. }
   56. // ...
   57. } catch {
   58. (err: BusinessError) => {
   59. hilog.error(0x0000, '[PasteBoard]', `getData error.code: ${err.code}, message: ${err.message}`);
   60. }
   61. }
   62. }
   63. })
   ```

   [PasteBoard.ets](https://gitcode.com/harmonyos_samples/pasteboard/blob/master/entry/src/main/ets/pages/PasteBoard.ets#L117-L201)

## 进度条接入

允许文件粘贴时，通常需要使用进度条将抽象进程转化为可视化的动态变化，帮助用户快速理解了解当前进展。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/f1/v3/tpDeT9fWReukKsKTZhBCRg/zh-cn_media_0000002395443772.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061240Z&HW-CC-Expire=86400&HW-CC-Sign=299D698F52C7F25497D84ED883E1CCFBB81E6AB29A5476EB0BDA2720068580D9)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 11.09%

0:00

Duration 0:10

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

**构建****数据存入剪贴板**

创建一个包含单样式的pasteData数据。创建一个文本文件存入剪贴板。

```
1. let filesDir = uiContext?.getHostContext()!.filesDir;
2. let fileFullName = filesDir + '/test1.txt';
3. hilog.info(0x0000, '[ProgressBar]', 'The fileFullName of str is:' + fileFullName);
4. let file = fs.openSync(fileFullName, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
5. let writeLen = fs.writeSync(file.fd, VALUE_TEST_STRING_ELEMENT);
6. hilog.info(0x0000, '[ProgressBar]', 'The size of str is: ' + writeLen);
7. fs.closeSync(file);
8. let pasteData =
9. pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, fileUri.getUriFromPath(fileFullName));

11. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
12. await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
13. hilog.error(0x0000, '[ProgressBar]',
14. `Failed to set pastedata. Code: ${err.code}, message: ${err.message}`);
15. });
```

[ProgressBar.ets](https://gitcode.com/harmonyos_samples/pasteboard/blob/master/entry/src/main/ets/pages/ProgressBar.ets#L143-L157)

**获取剪贴板的内容和进度**

[使用粘贴控件](../harmonyos-guides/pastebutton.md)获取临时授权后，调用[getDataWithProgress()](../harmonyos-references/js-apis-pasteboard.md#getdatawithprogress15)方法获取剪贴板的内容及进度。params参数用于在应用使用剪贴板提供的文件拷贝功能时提供必要的信息，包括目标路径、文件冲突处理选项、进度条类型等。[ProgressListener](../harmonyos-references/js-apis-pasteboard.md#progresslistener15)是用于订阅进度数据变化的函数，可以当前获取数据的进度信息。进度数据状态变量更新后，刷新进度条Progress组件显示。

```
1. PasteButton()
2. // ...
3. .onClick(async (event: ClickEvent, result: PasteButtonOnClickResult) => {
4. if (result === PasteButtonOnClickResult.SUCCESS) {
5. let systemPasteboard = pasteboard.getSystemPasteboard();
6. let ProgressListener = (progress: pasteboard.ProgressInfo) => {
7. this.progressInfo = progress.progress;
8. hilog.info(0x0000, '[ProgressBar]', 'progressListener success, progress:' + progress.progress);
9. // ...
10. }
11. let dstUri: string = fileUri.getUriFromPath(dstDir);
12. hilog.info(0x0000, '[ProgressBar]', 'progressBar' + 'dstUri: ' + dstUri + ' length: ' + dstUri.length);
13. let params: pasteboard.GetDataParams = {
14. destUri: dstUri,
15. progressIndicator: pasteboard.ProgressIndicator.NONE,
16. progressListener: ProgressListener
17. };
18. try {
19. await systemPasteboard.getDataWithProgress(params).then((data) => {
20. hilog.info(0x0000, '[ProgressBar]', 'getDataWithProgress success');
21. fs.unlink(dstUri);
22. }).catch((error: BusinessError) => {
23. hilog.error(0x0000, '[ProgressBar]', 'getDataWithProgress failed,error: ' + JSON.stringify(error));
24. })
25. } catch (err) {
26. hilog.error(0x0000, '[ProgressBar]',
27. 'getDataWithProgress fail,err：' + err.code + ',message: ' + err.message);
28. }
29. }
30. })
```

[ProgressBar.ets](https://gitcode.com/harmonyos_samples/pasteboard/blob/master/entry/src/main/ets/pages/ProgressBar.ets#L88-L132)

## 示例代码

* [实现剪贴板复制粘贴的功能](https://gitcode.com/harmonyos_samples/pasteboard)
