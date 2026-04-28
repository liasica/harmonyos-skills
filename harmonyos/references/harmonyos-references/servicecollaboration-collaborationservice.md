---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationservice
title: CollaborationService (跨设备互通组件)
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS 组件 > CollaborationService (跨设备互通组件)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:14+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:72ba9fc5ae25c7bfde00d61d094deb857afe0ca13915399b653c1cfde0dfdd87
---

该模块提供了组件[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)和[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)，两者需要配合使用，完成分布式跨端能力，如在2in1端跨端调用手机端拍照。

通过[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)组件，可以获取组网内具有对应能力的设备列表。用户选择对应的设备后，拉起应用。调用[CollaborationServiceStateDialog](servicecollaboration-collaborationservice.md#collaborationservicestatedialog)，应用将弹出提示框，提示对端应用状态。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { CollaborationServiceStateDialog, createCollaborationServiceMenuItems, CollaborationServiceFilter} from '@kit.ServiceCollaborationKit';
```

## createCollaborationServiceMenuItems

PhonePC/2in1TabletTV

createCollaborationServiceMenuItems(businessFilter?: Array<CollaborationServiceFilter>): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Service

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)> | 否 | 传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。  对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。 |

**示例：**

```
1. @Builder
2. MyTestMenu() {
3. Menu() {
4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL])
5. }
6. }
```

## createCollaborationServiceMenuItems

PhonePC/2in1TabletTV

createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveNumber: number): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表，此接口支持自定义对端图库能力图片选择的数量。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Service

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)> | 是 | 传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。  对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。 |
| canReceiveNumber | number | 是 | 传入照片最大张数，数量1到50，小于等于0时不会拉起被调用设备的能力，大于50默认为50。 |

**示例：**

```
1. @Builder
2. MyTestMenu() {
3. Menu() {
4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30)
5. }
6. }
```

## createCollaborationServiceMenuItems

PhonePC/2in1TabletTV

createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveMaxCount: number, deviceTypeFilter: Array<CollaborationDeviceFilterType> ): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表，此接口支持自定义对端图库能力图片选择的数量和支持自定义选择对端的设备类型手机、平板和2in1设备。

具体调用策略：2in1设备可以调用平板和手机，平板可以调用手机，并且在6.1.0(23)及以上版本支持手机、平板或2in1设备调用支持拍照、扫描、选择图库能力的手机，支持拍照、扫描、选择图库能力的平板，以及支持选择图库能力的2in1设备

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)> | 是 | 传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。  对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。 |
| canReceiveMaxCount | number | 是 | 传入照片最大张数，数量1到50，小于等于0时不会拉起被调用设备的能力，大于50默认为50。 |
| deviceTypeFilter | Array<[CollaborationDeviceFilterType](servicecollaboration-collaborationservice.md#collaborationdevicefiltertype)> | 是 | 传入调用的设备类型，传入为空或传入非法值时不会调用设备。 |

**示例：**

```
1. @Builder
2. MyTestMenu() {
3. Menu() {
4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30, [CollaborationDeviceFilterType.PHONE, CollaborationDeviceFilterType.TABLET])
5. }
6. }
```

## CollaborationServiceFilter

PhonePC/2in1TabletTV

能力类型枚举值。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 匹配跨端拍照、文档扫描和图库选择器。 |
| TAKE\_PHOTO | 1 | 匹配跨端拍照。 |
| SCAN\_DOCUMENT | 2 | 匹配文档扫描。 |
| IMAGE\_PICKER | 3 | 匹配图库选择器。 |
| VIDEO\_PICKER | 5 | 匹配视频选择器。  **起始版本：** 6.0.0(20) |
| IMAGE\_VIDEO\_PICKER | 6 | 匹配图片和视频选择器。  **起始版本：** 6.0.0(20) |

**示例：**

```
1. @Builder
2. MyTestMenu() {
3. Menu() {
4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30)
5. }
6. }
```

## CollaborationDeviceFilterType

PhonePC/2in1TabletTV

设备类型枚举值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHONE | 1 | 手机。 |
| TABLET | 2 | 平板。 |
| PC\_2IN1 | 3 | PC/2in1。 |

**示例：**

```
1. @Builder
2. MyTestMenu() {
3. Menu() {
4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30, [CollaborationDeviceFilterType.PHONE, CollaborationDeviceFilterType.TABLET])
5. }
6. }
```

## CollaborationServiceStateDialog

PhonePC/2in1TabletTV

弹窗组件，用于提示对端应用状态。

您需要实现[onState](servicecollaboration-collaborationservice.md#onstate)方法，并且在页面中定义这个组件，在业务开始后，此方法将被协同框架调用。

该组件为自定义组件，开发者在使用前需要先了解[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)。

**装饰器类型：** @Component

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

### onState

PhonePC/2in1TabletTV

onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer) => void

接收数据的回调函数，其中传入的stateCode是完成状态，bufferType是回传的数据类型，buffer是回传的数据内容，开发者可通过状态和数据结合自身的业务逻辑实现onState方法。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateCode | number | 是 | 标识业务完成状态，含义详见下面状态码。 |
| bufferType | string | 是 | 标识回传数据类型。  "general.image"：图片类型。  "general.fileName"：文件名称。  "general.video"：视频，从6.1.0(23)开始支持此类型。 |
| buffer | ArrayBuffer | 是 | 当bufferType为"general.image"，成功则返回对应数据，失败则返回空。  当bufferType为"general.video"，成功则返回对应存在应用沙箱视频uri路径，失败则返回空。 |

**状态码：**

以下部分错误状态的详细介绍请参见[ArkTS 错误码](servicecollaboration-error-code.md)。

| 状态码ID | 错误信息 |
| --- | --- |
| 0 | 成功。 |
| 1001202001 | 对端取消。 |
| 1001202002 | 协同框架内部出现错误。 |
| 1001202003 | 本端取消。 |
| 1001202004 | 跨设备互通能力开始。 |
| 1001202005 | 图片全部回传结束。 |
| 1001202006 | 回传文件名称。 |
| 1001202007 | 当[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems-1)传入自定义图片张数canReceiveNumber小于等于0时，不会拉起被调用设备的能力。 |
| 1001202015 | 视频全部回传成功。 |
| 1001202016 | 正在回传多个视频。 |

### build

PhonePC/2in1TabletTV

build(): void

struct的默认构造函数，开发者无法直接调用此方法。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**示例1：**

6.1.0(23)之前的版本，参考以下示例，可以完成一次调用对端应用的获取图片操作。

跨设备互通详细介绍可参考[跨设备互通特性简介](../harmonyos-guides/servicecollaboration-service-overview.md)。

```
1. import {
2. createCollaborationServiceMenuItems,
3. CollaborationServiceStateDialog,
4. CollaborationServiceFilter
5. } from '@kit.ServiceCollaborationKit';
6. import { image } from '@kit.ImageKit';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. @Entry
10. @Component
11. struct Index {
12. @State picture: PixelMap | undefined = undefined;

14. @Builder
15. MyTestMenu() {
16. Menu() {
17. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30)
18. }
19. }

21. build() {
22. Column({ space: 20 }) {
23. CollaborationServiceStateDialog({
24. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode, bufferType, buffer)
25. })
26. Button('使用远端设备进行拍照')
27. .type(ButtonType.Normal)
28. .borderRadius(10)
29. .bindMenu(this.MyTestMenu)

31. if (this.picture) {
32. Image(this.picture)
33. .borderStyle(BorderStyle.Dotted)
34. .borderWidth(1)
35. .objectFit(ImageFit.Contain)
36. .height('80%')
37. .onComplete((event) => {
38. if (event != undefined) {
39. hilog.info(0, "MEMOMOCK", "onComplete " + event.loadingStatus)
40. }
41. })
42. }
43. }
44. .padding(20)
45. .width('100%')
46. .alignItems(HorizontalAlign.Center)
47. }

49. doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
50. if (stateCode != 0) {
51. return
52. }
53. if (bufferType == "general.image") {
54. let imageSource = image.createImageSource(buffer)
55. imageSource.createPixelMap().then((pixelMap) => {
56. this.picture = pixelMap;
57. })
58. }
59. }
60. }
```

**示例2：**

6.1.0(23)及之后的版本，参考以下示例，可以完成一次调用对端应用的获取图片和视频操作。

跨设备互通详细介绍可参考[跨设备互通特性简介](../harmonyos-guides/servicecollaboration-service-overview.md)。

```
1. import {
2. createCollaborationServiceMenuItems, CollaborationServiceStateDialog
3. } from '@kit.ServiceCollaborationKit';
4. import { image } from '@kit.ImageKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';
6. import { util } from '@kit.ArkTS';

8. class VideoItem {
9. id: string;
10. src: string;

12. constructor(id: string, src: string) {
13. this.id = id;
14. this.src = src;
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. @State picture: PixelMap | undefined = undefined;
22. controller: RichEditorController = new RichEditorController();
23. options: RichEditorOptions = { controller: this.controller };
24. @State videoSrc: string = ''
25. @State videoItems: VideoItem[] = [];
26. refreshId: number = 0;

28. @Builder
29. MyToolBarMenu() {
30. Menu() {
31. // create collaboration camera menuItems to show camera devices.
32. createCollaborationServiceMenuItems([0, 5
33. ], 50)
34. }
35. }

37. aboutToAppear(): void {
38. hilog.info(0, 'MEMOMOCK', 'aboutToAppear ');
39. }

41. aboutToDisappear(): void {
42. hilog.info(0, 'MEMOMOCK', 'aboutToDisappear ');
43. }

45. build() {
46. Column({ space: 20 }) {
47. CollaborationServiceStateDialog({
48. onState: (stateCode: number, dataType?: string, buffer?: ArrayBuffer): void =>
49. this.doInsertPicture(stateCode, dataType, buffer)
50. })
51. Button('使用远端设备进行拍照')
52. .type(ButtonType.Normal)
53. .borderRadius(10)
54. .bindMenu(this.MyToolBarMenu)
55. RichEditor(this.options)
56. .onReady(() => {
57. hilog.info(0x0000, 'MEMOMOCK', 'RichEditor');
58. }
59. )
60. Column() {
61. List() {
62. ForEach(this.videoItems, (item: VideoItem, index: number) => {
63. ListItem() {
64. Video({
65. src: item.src,
66. controller: new VideoController()
67. })
68. .objectFit(ImageFit.Auto)
69. .width('20%')
70. .height('20%')
71. .margin({ top: 10, right: 10 })
72. .onError((err) => {
73. hilog.error(0, 'MEMOMOCK', `code is ${err.code}, message is ${err.message}`);
74. })
75. }
76. }, (item: VideoItem) => {
77. hilog.info(0, 'MEMOMOCK', 'item id ' + item.id);
78. hilog.info(0, 'MEMOMOCK', 'item src' + item.src);
79. return item.id;
80. });
81. }
82. }.padding({ bottom: '120vp' })
83. }
84. .width('100%')
85. .alignItems(HorizontalAlign.Center);
86. }

88. doInsertPicture(stateCode: number, dataType?: string, buffer?: ArrayBuffer): void {
89. hilog.info(0, 'MEMOMOCK', 'doInsertPicture is ' + stateCode)
90. if (dataType == 'general.video') {
91. let decoder = util.TextDecoder.create('utf-8');
92. let uriStr = decoder.decodeToString(new Uint8Array(buffer));
93. hilog.info(0, 'MEMOMOCK', 'Received URI: ' + uriStr);
94. const newId = String(++this.refreshId);
95. this.videoItems.push(new VideoItem(newId, uriStr));
96. } else if (dataType == 'general.image') {
97. let imageSource = image.createImageSource(buffer)
98. imageSource && imageSource.createPixelMap().then((pixelMap) => {
99. this.picture = pixelMap;
100. if (this.controller) {
101. this.controller.addImageSpan(pixelMap,
102. {
103. imageStyle:
104. {
105. size: ["200px", "200px"]
106. }
107. });
108. }
109. })
110. }
111. }
112. }
```
