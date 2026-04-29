---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-continue
title: 内容编辑多设备协同
breadcrumb: 最佳实践 > 自由流转 > 典型全场景协同开发案例 > 内容编辑多设备协同
category: best-practices
scraped_at: 2026-04-29T14:12:54+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:bf1fef42896056dda64dbac0cdc9b2a5b9420b6e8ec466906f9c134210563967
---

## 概述

在办公、创作和社区交友等应用中，内容发布是用户互动与交流的核心，它允许用户创作并分享包含图片、文字等多媒体信息，从而增强用户间的连接与互动。随着手机、平板、PC/2in1等多设备的普及，用户对在不同设备间无缝切换、跨设备处理图片和文字及接续编辑内容的需求日益增长。本文介绍如何通过应用接续功能（实现不同设备间的快速切换）和跨设备互通功能，提升内容发布的便利性。

本文主要包含以下几个方面内容：

* [跨设备互通](bpta-continue.md#section81333710289)：基于分布式协同框架，面向跨设备拍照等业务场景，提供[createCollaborationServiceMenuItems()](../harmonyos-references/servicecollaboration-collaborationservice.md#section1633482912443)（相机设备列表组件）和[CollaborationServiceStateDialog()](../harmonyos-references/servicecollaboration-collaborationservice.md#section158671330145417)（远端相机状态弹窗组件）两个组件。应用只需要调用这两个组件，即可实现跨设备调用相机、拍照、扫描及访问图库的功能。
* [跨设备拖拽图片/文字](bpta-continue.md#section103557271407)：支持跨设备拖拽场景，系统自动完成键鼠穿越和跨设备的数据传递，应用可根据实际需求，使用[拖拽控制](../harmonyos-references/ts-universal-attributes-drag-drop.md)和[拖拽事件](../harmonyos-references/ts-universal-events-drag-drop.md)能力，实现在平板或PC/2in1类型的任意两台设备间拖拽文件和文本的功能。
* [跨设备剪贴图片/文字](bpta-continue.md#section1838716271127)：基于[剪贴板](../harmonyos-references/js-apis-pasteboard.md)能力，支持系统复制、粘贴功能，实现本地剪贴板和跨设备剪贴板的业务场景。本地剪贴板提供设备内的内容复制粘贴，跨设备剪贴板提供跨设备的内容复制粘贴。
* [跨设备应用接续](bpta-continue.md#section181890343316)：基于UIAbility应用组件，通过在本端使用[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)接口保存迁移数据，在目的端使用[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)接口恢复迁移数据，实现应用接续的场景。即当用户在一个设备上操作某个应用时，可以在另一个设备的同一个应用中快速切换，并无缝衔接上一个设备的应用体验。

## 用户体验

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/f4/v3/yCqhMop2TDuQZMiTtfc7rQ/zh-cn_media_0000002311815932.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=0F608C3C49FFE927F0A361E2B7AFB1FE168B1C27E631979C473255E4B495158D)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 1.00%

0:00

Duration 1:04

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

### 使用限制

| 限制\场景 | 跨设备互通 | 跨设备拖拽 | 跨设备剪贴 | 跨设备应用接续 |
| --- | --- | --- | --- | --- |
| HarmonyOS NEXT及以上版本的设备 | √ | √ | √ | √ |
| 登录同一个华为账号 | √ | √ | √ | √ |
| 打开Wi-Fi和蓝牙开关 | √ | √ | √ | √ |
| 打开键鼠穿越开关 | NA | √ | NA | NA |
| 设备需解锁、亮屏 | NA | NA | √ | NA |
| 非同类型设备操作 | √（调用策略：PC/2in1设备可以调用平板和手机，平板可以调用手机，不可反向调用） | NA | NA | NA |
| 只能在同应用（UIAbility）之间触发 | NA | NA | NA | √ |
| 开启“多设备协同 > 接续”功能 | NA | NA | NA | √ |
| 应用在安装前的HAP包中已经存在的资源文件不能跨端 | NA | √ | NA | NA |

## 跨设备互通

### 场景描述

当用户在平板或PC/2in1设备上使用文本编辑应用（如备忘录、邮件、笔记等）时，若需拍摄照片作为素材，当设备操作不便时，可利用跨设备互通功能解决。用户可在当前设备的应用中选择平板或手机，启动其相机拍摄所需素材，或从图库中选取所需图片。使用手机或平板拍摄具备更高的灵活性和取景便利性，以及更强大的相机功能。所选照片将迅速传输至平板或PC/2in1设备的应用中，助力用户高效完成图文编辑任务。

说明

该功能的使用需满足设备限制和使用限制，具体约束与限制可参考：跨设备互通开发指导中的[约束与限制](../harmonyos-guides/servicecollaboration-dev-guides.md#section17575828642)章节。

**实现效果**

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/fa/v3/qyQZk3ksQ5KjAAgDpNdaSQ/zh-cn_media_0000002345894753.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=91887D2A2AC31AECC0A902F6E1FFE7AD2CC172B290C3C5E870B1D90E7B6EFE81)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 2.61%

0:00

Duration 0:21

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

### 实现原理

**场景分析**

1. 用户在本端（平板或PC/2in1）应用界面操作，选择使用远端设备的拍照、扫描或图库功能，向远端发起请求。
2. 系统将自动唤醒远端设备上的相机、图库或扫描功能，进入相应的界面。
3. 使用远端设备完成拍照或选择图片并确认，远端拍摄状态信息实时回传到本端，并将数据插入到本端设备的应用中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/IKDm136aST6HeiKqU_8qDg/zh-cn_image_0000002345774957.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=DE5AE2ACF8E59B7E16AA032667566E8A89E710607A6989920729C0A7A7E1E109 "点击放大")

**关键技术**

在分布式协同框架下，针对跨设备互通图片信息的业务场景，应用只需要调用[createCollaborationServiceMenuItems()](../harmonyos-references/servicecollaboration-collaborationservice.md#section1633482912443)（相机设备列表组件）和[CollaborationServiceStateDialog()](../harmonyos-references/servicecollaboration-collaborationservice.md#section158671330145417)（远端相机状态弹窗组件）两个组件，即可完成跨端拍照、扫描、图库访问能力，开发者无需关注分布式场景下的数据传输和指令控制等细节，具体运作机制可参考：跨设备互通特性简介中的[运作机制](../harmonyos-guides/servicecollaboration-service-overview.md#section7984237153619)章节。

### 实现方案

* 拉取远端菜单，选择远端设备

  通过[createCollaborationServiceMenuItems()](../harmonyos-references/servicecollaboration-collaborationservice.md#section1633482912443)组件，获取组网内具有对应能力的设备列表。当用户选择特定的设备功能后，系统将自动激活远端设备的相机或图库，并使设备屏幕自动点亮。可设置传输照片的最大数量，范围为1至50张；若设置数量小于或等于0，则不会触发设备的相应功能；若设置数量超过50，则默认为50张。

  ```
  1. // Remote menu.
  2. @Builder
  3. MyTestMenu() {
  4. Menu() {
  5. MenuItem({
  6. symbolStartIcon: new SymbolGlyphModifier($r('sys.symbol.picture_2')),
  7. content: $r('app.string.local_device')
  8. })
  9. .onClick(() => {
  10. if (this.imageUriArray.length < CommonConstants.MAX_ADD_PIC) {
  11. this.selectImage();
  12. } else {
  13. try {
  14. this.getUIContext().getPromptAction().showToast({ message: $r('app.string.add_picture_prompt') });
  15. } catch (err) {
  16. hilog.error(DOMAIN, TAG, FORMAT, `ShowToast failed. Cause code: ${err.code}, message: ${err.message}`);
  17. }
  18. }
  19. })
  20. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 9)
  21. }
  22. }
  ```

  [AddPic.ets](https://gitcode.com/HarmonyOS_Samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L454-L476)
* 将远端拍摄状态信息实时回传

  应用将弹出提示框，实时回传远端拍摄状态信息到组件[CollaborationServiceStateDialog()](../harmonyos-references/servicecollaboration-collaborationservice.md#section158671330145417)（远端相机状态弹窗组件），为弹窗组件绑定和实现[onState()](../harmonyos-references/servicecollaboration-collaborationservice.md#section33027582114)方法，在业务开始后，此方法将被协同框架调用，用于接收和处理数据。该回调函数接收的数据中，stateCode表示完成状态，bufferType表示回传的数据类型，buffer则是回传的图片数据。

  ```
  1. build() {
  2. Column() {
  3. CollaborationServiceStateDialog({
  4. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode,
  5. bufferType, buffer)
  6. })
  7. // ...
  8. }
  9. // ...
  10. }
  ```

  [AddPic.ets](https://gitcode.com/HarmonyOS_Samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L268-L339)
* 将回传数据写入页面

  用户使用远端设备完成拍照或选择图库照片后，通过自定义方法将返回的图片数据写入本端设备的页面。远端设备将自动退出相机或图库界面，恢复到初始状态。

  ```
  1. // Remote images fall into.
  2. doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
  3. if (stateCode != 0) {
  4. return;
  5. }
  6. if (bufferType === 'general.image') {
  7. let imageSource = image.createImageSource(buffer);
  8. imageSource.createPixelMap().then((pixelMap) => {
  9. if (this.imageUriArray.length < CommonConstants.MAX_ADD_PIC) {
  10. let uuid = util.generateRandomUUID();
  11. this.PixelMapToBuffer(pixelMap, uuid);
  12. this.imageUriArray.push({ imagePixelMap: pixelMap, imageName: uuid });
  13. }
  14. })
  15. }
  16. }
  ```

  [AddPic.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L163-L179)

## 跨设备拖拽图片/文字

### 场景描述

当用户拥有多台设备时，开启键鼠共享功能，可以实现键鼠在不同设备间的自由移动。通过跨设备拖拽，用户可以轻松地将本端上的素材拖拽到远端，快速完成内容创作，享受高效的跨设备协同工作体验。

说明

该功能的使用需满足设备限制和使用限制，具体约束与限制可参考：[跨设备拖拽约束与限制](../harmonyos-guides/distributed-drag-guide.md#section17575828642)。

**实现效果**

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/0f/v3/QGEBWJdDRbyVkYClriYWqA/zh-cn_media_0000002311975752.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=3B19516E3BCFF9E89D9E9C4AE5AE9D073967534AB6BF60BAA6AFA0988A784B18)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 9.40%

0:00

Duration 0:17

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

### 实现原理

**场景分析**

1. 用户通过长按鼠标触发拖拽事件，可以从本端编辑页面将图片或文字拖拽到远端的编辑页面。
2. 在此过程中，系统自动处理跨设备的数据传输，开发者无需介入。
3. 当用户释放鼠标时，触发拖拽松手事件，远端应用处理接收到的拖拽数据，并将其写入远端编辑页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/265rxrkSQL2KPQj2jj20wg/zh-cn_image_0000002311815960.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=C3194948E4194935395A926D8D9709D3F7812A1EDF438E6EBA46D265EB06FB28 "点击放大")

**关键技术**

在开发跨设备拖拽功能时，系统会自动处理鼠标和键盘的跨设备操作及数据传递。应用可以根据实际需求，实现组件的拖入或拖出，完成拖拽事件的开发。具体运作机制可参考：[跨设备拖拽运作机制](../harmonyos-guides/distributed-drag-overview.md#section159119429237)。

### 实现方案

* 设置组件允许拖拽

  将需要触发拖拽事件和松手事件的Image组件、TextInput组件及TextArea组件设置[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)为true，以允许拖拽。
* 设置组件允许落入的类型

  使用[allowDrop()](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)方法设置组件允许拖入的数据类型，包括PLAIN\_TEXT、IMAGE、OPENHARMONY\_PIXEL\_MAP等。
* 定义[拖拽事件](../harmonyos-references/ts-universal-events-drag-drop.md)

  将允许拖入的组件绑定[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)事件作为释放目标。当在该组件范围内停止拖拽操作时，将触发回调函数，实现图片的拖出和写入页面的功能。

  ```
  1. build() {
  2. Column() {
  3. // ...
  4. }
  5. .draggable(true)
  6. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE,
  7. uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP])
  8. .onDrop((dragEvent?: DragEvent) => {
  9. // The logic behind the image falling in, achieving image writing.
  10. // ...
  11. })
  12. })

  14. }

  17. // ...

  19. /*
  20. *  Adding an image.
  21. */
  22. @Builder
  23. addPic() {
  24. Row() {
  25. List({ space: CommonConstants.LIST_COMM_SPACE }) {
  26. ForEach(this.imageUriArray, (item: ImageInfo) => {
  27. ListItem() {
  28. Image(item.imagePixelMap)// ...
  29. .draggable(true)
  30. .onDragEnd((event) => {
  31. // The logic after dragging and dropping is completed.
  32. // ...
  33. })// ...
  34. }
  35. }, (item: ImageInfo, index: number) => JSON.stringify(item) + index)
  36. // ...
  37. }
  38. // ...
  39. }
  40. // ...
  41. }
  ```

  [AddPic.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L267-L450)

  当在TextInput()和TextArea()组件范围内停止拖放行为时，将触发回调，实现文字拖出和写入页面的效果。

  ```
  1. build() {
  2. Flex({ direction: FlexDirection.Column }) {
  3. TextInput({ text: this.mainTitle, placeholder: $r('app.string.text_input_placeholder') })// ...
  4. .draggable(true)
  5. .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
  6. .onDrop((dragEvent?: DragEvent) => {
  7. // The logic after the text falls in, realizing the writing of text.
  8. // ...
  9. })

  11. TextArea({ text: this.textContent, placeholder: $r('app.string.richEditor_placeholder') })// ...
  12. .draggable(true)
  13. .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
  14. .onDrop((dragEvent?: DragEvent) => {
  15. // The logic after the text falls in, realizing the writing of text.
  16. // ...
  17. })
  18. }
  19. .backgroundColor($r('sys.color.background_primary'))
  20. // ...
  21. }
  ```

  [EditorComponent.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/view/EditorComponent.ets#L65-L155)

## 跨设备剪贴图片/文字

### 场景描述

当用户拥有多台设备时，可以利用跨设备剪贴板的功能，在本端的应用中复制文本或图片，并在远端的应用中粘贴，实现高效的内容共享。

说明

该功能的使用需满足设备限制和使用限制，具体约束与限制可参考：[跨设备剪贴板约束与限制](../harmonyos-guides/distributed-pasteboard-guide.md#section17575828642)。

**实现效果**

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/a9/v3/hspMydF5S2uTvIAtZCwyog/zh-cn_media_0000002345894765.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=AF5997CC8D70C62048C014C74AD928B098A99658B93BD19E6BA073FF87E0A875)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 100.00%

0:00

Duration 0:19

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

### 实现原理

**场景分析**

1. 用户在本端复制数据，写入到系统剪贴板服务。

2. 系统剪贴板服务处理数据并完成同步，此过程开发者不感知。

3. 用户在远端读取系统剪贴板内容，粘贴来自本端的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/t9X9ior0RUmHO-SLQwPQcA/zh-cn_image_0000002345774965.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=91E990F1CA762CC2E4F7D90EC8AF281C4EE4C82CB0959516B8B72CA29146FE6D "点击放大")

**关键技术**

在开发跨设备剪贴板功能时，系统会自动处理设备间的数据传输，应用程序可根据实际需求接入跨设备剪贴板，实现跨设备间的数据共享。具体运作机制可参考：[跨设备剪贴板运作机制](../harmonyos-guides/distributed-pasteboard-overview.md#section1047015015477)。

### 实现方案

* 本端复制数据，写入到剪贴板服务

  使用[SystemPasteboard](../harmonyos-references/js-apis-pasteboard.md#systempasteboard)(系统剪贴板对象)的[setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法将本端复制的数据写入剪贴板服务。

  ```
  1. // Copy picture.
  2. async setPasteDataTest(pixelMap: image.PixelMap): Promise<void> {
  3. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
  4. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
  5. await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
  6. hilog.error(DOMAIN, TAG, FORMAT, `Failed to set pastedata. Code: ${err.code}, message: ${err.message}`);
  7. });
  8. }
  ```

  [AddPic.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L222-L230)
* 远端粘贴数据，读取剪贴板内容

  在远端设备上粘贴数据时，使用[SystemPasteboard](../harmonyos-references/js-apis-pasteboard.md#systempasteboard)（系统剪贴板对象）的[getData()](../harmonyos-references/js-apis-pasteboard.md#getdata9)方法读取剪贴板中的内容，并将数据展示在页面上。

  ```
  1. // Paste picture.
  2. async getPasteDataTest(): Promise<void> {
  3. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
  4. systemPasteBoard.getData((err: BusinessError, data: pasteboard.PasteData) => {
  5. if (err) {
  6. hilog.error(DOMAIN, TAG, FORMAT, `Failed to get pastedata. Code: ${err.code}, message: ${err.message}`);
  7. return;
  8. }
  9. // Process pasteData, obtain type, number, etc
  10. // Retrieve the number of records in the clipboard.
  11. let recordCount: number = data.getRecordCount();
  12. // Retrieve the type of data from the clipboard.
  13. let types: string = data.getPrimaryMimeType();
  14. hilog.info(DOMAIN, TAG, FORMAT, `recordCount: ${recordCount}, types: ${types}`);
  15. // Retrieve the content of data from the clipboard.
  16. if (types === 'pixelMap') {
  17. let primaryPixelMap: image.PixelMap = data.getPrimaryPixelMap();
  18. if (this.imageUriArray.length < CommonConstants.MAX_ADD_PIC) {
  19. let uuid = util.generateRandomUUID();
  20. this.PixelMapToBuffer(primaryPixelMap, uuid);
  21. this.imageUriArray.push({ imagePixelMap: primaryPixelMap, imageName: uuid });
  22. } else {
  23. this.toastShow = true;
  24. }
  25. } else if (types === 'text/uri') {
  26. this.uri2pixelMap(data.getPrimaryUri());
  27. }
  28. });
  29. }
  ```

  [AddPic.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L234-L263)

## 跨设备应用接续

### 场景描述

在用户使用过程中，使用场景发生了变化，之前使用的设备不再适合继续当前任务，或者周围有更合适的设备，此时用户可以选择使用新的设备来继续当前的任务。接续完成后，之前设备的应用可退出或保留，用户可以将注意力集中在被拉起的设备上，继续执行任务。

说明

该功能的使用需满足设备限制和使用限制，具体约束与限制可参考：[应用接续约束与限制](../harmonyos-guides/app-continuation-guide.md#section17575828642)。

**实现效果**

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/27/v3/wOJ_1Z7XR2i9mqctKKD_1A/zh-cn_media_0000002311975768.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=06553C444D66674DC9BF30DF7E337976FA1689135EFEA416D66C2A631BBFC72C)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 100.00%

0:00

Duration 0:02

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

### 实现原理

**场景分析**

1. 输入数据：用户在本端设备的编辑页面上选择照片、输入标题和正文等文字信息。
2. 用户点击远端设备Dock栏图标后，本端设备发起接续，数据进行传输。
3. 远端设备接收接续数据并显示。

场景核心在于应用接续的过程中如何传递数据。对于文字信息可使用分布式数据对象保存，对于图片可以拷贝到分布式文件目录下，使用分布式数据资产作为分布式数据对象的根属性保存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/z4VZL0bXT5-ACjxRjUlIww/zh-cn_image_0000002311815980.png?HW-CC-KV=V1&HW-CC-Date=20260429T061247Z&HW-CC-Expire=86400&HW-CC-Sign=E6100D5985EA6FAFA7474CDD11EBC4812E12007CAB193A6ECB79AACD2401AFB1 "点击放大")

**关键技术**

将发起接续的设备称为本端设备，接收数据的设备称为远端设备，运作机制如图，接续过程底层依赖分布式框架和软总线，开发者只需要启用接续、保存数据和恢复数据，具体运作机制可参考：[应用接续运作机制](../harmonyos-guides/app-continuation-overview.md#section13558148125311)。

### 实现方案

* 启用应用接续能力

  在module.json5文件的abilities中，将continuable标签配置为“true”，表示该UIAbility可被迁移。配置为false的UIAbility将被系统识别为无法迁移且该配置默认值为false。

  ```
  1. {
  2. "module": {
  3. // ...
  4. "abilities": [
  5. {
  6. // ...
  7. "continuable": true,
  8. // ...
  9. }
  10. ],
  11. // ...
  12. }
  13. }
  ```

  [module.json5](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/module.json5#L2-L111)
* 基础数据&文件资产迁移

  对于图片、文档等文件类数据，可以转化成ArrayBuffer类型，保存在分布式文件目录下。

  ```
  1. writeDistributedFile(buf: ArrayBuffer, displayName: string): void {
  2. // The asset is written to the distributed file directory.
  3. // Obtain the distributed file directory path.
  4. let distributedDir: string = this.context.distributedFilesDir;
  5. let fileName: string = '/' + displayName;
  6. let filePath: string = distributedDir + fileName;
  7. try {
  8. // Create a file in a distributed directory.
  9. let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  10. hilog.info(DOMAIN, TAG, FORMAT, 'Create file success.');
  11. // Write content to a file (if the asset is a picture, the picture can be converted to a buffer to write)
  12. fs.writeSync(file.fd, buf);
  13. // closed file.
  14. fs.closeSync(file.fd);
  15. } catch (error) {
  16. let err: BusinessError = error as BusinessError;
  17. hilog.info(DOMAIN, TAG, FORMAT,
  18. `Failed to openSync / writeSync / closeSync. Code: ${err.code}, message: ${err.message}`);
  19. }
  20. }
  ```

  [AddPic.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/view/AddPic.ets#L109-L130)

  使用分布式数据对象时，需要在本端onContinue()接口中进行数据保存。在本端UIAbility的[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)接口中，创建分布式数据对象并保存数据，执行流程如下：

  1. 在onContinue()接口中使用create()接口创建分布式数据对象，将所要迁移的数据填充到分布式数据对象数据中。
  2. 如果有图片、文档等文件类数据要迁移，需要先将其转换为资产commonType.Asset类型，再封装到分布式数据对象中进行迁移。
  3. 调用genSessionId()接口生成数据对象组网id，并使用该id调用setSessionId()加入组网，激活分布式数据对象。
  4. 使用save()接口将已激活的分布式数据对象持久化，确保本端退出后远端依然可以获取到数据。
  5. 将生成的sessionId通过want传递到远端，供远端激活同步使用。

  ```
  1. async onContinue(wantParam: Record<string, Object | undefined>): Promise<AbilityConstant.OnContinueResult> {
  2. wantParam.imageUriArray = JSON.stringify(AppStorage.get<Array<PixelMap>>('imageUriArray'));
  3. try {
  4. // Generate the session ID of the distributed data object.
  5. let sessionId: string = distributedDataObject.genSessionId();
  6. wantParam.distributedSessionId = sessionId;

  8. let imageUriArray = AppStorage.get<Array<ImageInfo>>('imageUriArray');
  9. let assets: commonType.Assets = [];
  10. if (imageUriArray) {
  11. for (let i = 0; i < imageUriArray.length; i++) {
  12. let append = imageUriArray[i];
  13. let attachment: commonType.Asset = this.getAssetInfo(append);
  14. assets.push(attachment);
  15. }
  16. }

  18. let contentInfo: ContentInfo = new ContentInfo(
  19. AppStorage.get('mainTitle'),
  20. AppStorage.get('textContent'),
  21. AppStorage.get('imageUriArray'),
  22. AppStorage.get('isShowLocalInfo'),
  23. AppStorage.get('isAddLocalInfo'),
  24. AppStorage.get('selectLocalInfo'),
  25. assets
  26. );
  27. let source = contentInfo.flatAssets();
  28. this.distributedObject = distributedDataObject.create(this.context, source);
  29. this.distributedObject.setSessionId(sessionId).catch((err: BusinessError) => {
  30. hilog.info(DOMAIN, TAG, FORMAT, `SetSessionId failed. Cause code: ${err.code}, message: ${err.message}`);
  31. });
  32. await this.distributedObject.save(wantParam.targetDevice as string).catch((err: BusinessError) => {
  33. hilog.info(DOMAIN, TAG, FORMAT, `Failed to save. Code: ${err.code}, message: ${err.message}`);
  34. });
  35. } catch (error) {
  36. hilog.error(DOMAIN, TAG, FORMAT, 'distributedDataObject failed', `code ${(error as BusinessError).code}`);
  37. }
  38. return AbilityConstant.OnContinueResult.AGREE;
  39. }
  ```

  [EntryAbility.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L131-L172)
* 基础数据&文件资产恢复

  在远端设备UIAbility的onCreate()/onNewWant()中调用restoreDistributedObject()方法，通过加入与本端一致的分布式数据对象组网进行数据恢复，执行流程如下：

  1. 在restoreDistributedObject()方法中创建空的分布式数据对象，用于接收恢复的数据。
  2. 从want中读取分布式数据对象组网id。
  3. 注册on()接口监听数据变更。在收到status为restore的事件的回调中，实现数据恢复完毕时需要进行的业务操作。由于恢复的数据中有图片文件，调用fileCopy()方法从分布式文件中读取ArrayBuffer，然后把ArrayBuffer转化成图片类型数据进行存储。
  4. 调用setSessionId()加入组网，激活分布式数据对象。
  5. 打开远端设备，点击接续图标，应用打开，页面数据恢复。

  ```
  1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  2. hilog.info(DOMAIN, TAG, FORMAT, 'Ability onCreate');
  3. this.restoreDistributedObject(want, launchParam);
  4. AppStorage.setOrCreate('systemColorMode', this.context.config.colorMode);
  5. try {
  6. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
  7. } catch (err) {
  8. hilog.error(DOMAIN, TAG, FORMAT, `SetColorMode failed. Cause code: ${err.code}, message: ${err.message}`);
  9. }
  10. // ...
  11. }

  13. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  14. hilog.info(DOMAIN, TAG, FORMAT, 'Ability onNewWant');
  15. this.restoreDistributedObject(want, launchParam);
  16. }

  18. /*
  19. * The peer device receives data.
  20. * @param want
  21. * @param launchParam
  22. * @returns
  23. */
  24. async restoreDistributedObject(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
  25. if (launchParam.launchReason !== AbilityConstant.LaunchReason.CONTINUATION) {
  26. return;
  27. }

  29. let mailInfo: ContentInfo = new ContentInfo(undefined, undefined, [], undefined, undefined, undefined, undefined);
  30. this.distributedObject = distributedDataObject.create(this.context, mailInfo);
  31. // Add a data restored listener.
  32. try {
  33. this.distributedObject.on('status',
  34. (sessionId: string, networkId: string, status: 'online' | 'offline' | 'restored') => {
  35. hilog.info(DOMAIN, TAG, FORMAT, `status changed, sessionId: ${sessionId}`);
  36. hilog.info(DOMAIN, TAG, FORMAT, `status changed, status: ${status}`);
  37. hilog.info(DOMAIN, TAG, FORMAT, `status changed, networkId: ${networkId}`);
  38. if (status === 'restored') {
  39. if (!this.distributedObject) {
  40. return;
  41. }
  42. AppStorage.setOrCreate('mainTitle', this.distributedObject['mainTitle']);
  43. AppStorage.setOrCreate('textContent', this.distributedObject['textContent']);
  44. AppStorage.setOrCreate('isShowLocalInfo', this.distributedObject['isShowLocalInfo']);
  45. AppStorage.setOrCreate('isAddLocalInfo', this.distributedObject['isAddLocalInfo']);
  46. AppStorage.setOrCreate('selectLocalInfo', this.distributedObject['selectLocalInfo']);
  47. AppStorage.setOrCreate('attachments', this.distributedObject['attachments']);
  48. let attachments = this.distributedObject['attachments'] as commonType.Assets;
  49. hilog.info(DOMAIN, TAG, FORMAT,
  50. `attachments: ${JSON.stringify(this.distributedObject['attachments'])}`);
  51. for (const attachment of attachments) {
  52. this.fileCopy(attachment);
  53. }
  54. AppStorage.setOrCreate<Array<ImageInfo>>('imageUriArray', this.imageUriArray);
  55. }
  56. });
  57. } catch (err) {
  58. hilog.error(DOMAIN, TAG, FORMAT, `On status failed. Cause code: ${err.code}, message: ${err.message}`);
  59. }
  60. let sessionId: string = want.parameters?.distributedSessionId as string;
  61. this.distributedObject.setSessionId(sessionId).catch((err: BusinessError) => {
  62. hilog.info(DOMAIN, TAG, FORMAT, `SetSessionId failed. Cause code: ${err.code}, message: ${err.message}`);
  63. });
  64. try {
  65. this.context.restoreWindowStage(new LocalStorage());
  66. } catch (err) {
  67. hilog.error(DOMAIN, TAG, FORMAT, `RestoreWindowStage failed. Cause code: ${err.code}, message: ${err.message}`);
  68. }
  69. }
  ```

  [EntryAbility.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L40-L127)

  接续过来的图片，需要从分布式文件目录路径下读取所需的文件，经处理后，转化成需要的数据类型。

  ```
  1. /*
  2. * Copy distributed files.
  3. * @param attachmentRecord
  4. * @param key
  5. */
  6. private fileCopy(attachment: commonType.Asset): void {
  7. if (canIUse('SystemCapability.DistributedDataManager.CommonType')) {
  8. let filePath: string = this.context.distributedFilesDir + '/' + attachment.name;
  9. let savePath: string = this.context.filesDir + '/' + attachment.name;
  10. try {
  11. if (fs.accessSync(filePath)) {
  12. let saveFile = fs.openSync(savePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  13. let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  14. let buf: ArrayBuffer = new ArrayBuffer(Number(attachment.size));
  15. let readSize = 0;
  16. let readLen = fs.readSync(file.fd, buf, {
  17. offset: readSize
  18. });
  19. let sourceOptions: image.SourceOptions = {
  20. sourceDensity: 120
  21. };
  22. let imageSourceApi: image.ImageSource = image.createImageSource(buf, sourceOptions);
  23. this.imageUriArray.push({
  24. imagePixelMap: imageSourceApi.createPixelMapSync(),
  25. imageName: attachment.name
  26. });
  27. while (readLen > 0) {
  28. readSize += readLen;
  29. fs.writeSync(saveFile.fd, buf);
  30. readLen = fs.readSync(file.fd, buf, {
  31. offset: readSize
  32. });
  33. }
  34. fs.closeSync(file);
  35. fs.closeSync(saveFile);
  36. hilog.info(DOMAIN, TAG, FORMAT, attachment.name + 'synchronized successfully.');
  37. }
  38. } catch (error) {
  39. let err: BusinessError = error as BusinessError;
  40. hilog.error(DOMAIN, TAG, FORMAT, `DocumentViewPicker failed with err: ${JSON.stringify(err)}`);
  41. }
  42. }
  43. }
  ```

  [EntryAbility.ets](https://gitcode.com/harmonyos_samples/ContinuePublish/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L176-L221)

## 示例代码

* [基于应用接续及跨设备互通功能实现内容发布功能](https://gitcode.com/harmonyos_samples/ContinuePublish)
