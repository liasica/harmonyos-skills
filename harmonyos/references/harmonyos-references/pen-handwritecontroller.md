---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecontroller
title: HandwriteController (手写套件功能)
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > HandwriteController (手写套件功能)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:536bdcbc393deee326b6fa35b5591c0892262a438f182e2924077687a35b19ce
---

手写套件的主要功能入口类，包含手写能力的主要方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { HandwriteController } from '@kit.Penkit';
```

本模块提供以下方法，完成手写内容的加载和保存等功能。

| 方法名称 | 说明 |
| --- | --- |
| [load](pen-handwritecontroller.md#load) | 从指定路径加载笔记文件。 |
| [save](pen-handwritecontroller.md#save) | 保存手写内容。 |
| [onLoad](pen-handwritecontroller.md#onload) | 加载完成时的回调接口。 |
| [getContentRange](pen-handwritecontroller.md#getcontentrange) | 获取笔迹范围。 |
| [getThumbnail](pen-handwritecontroller.md#getthumbnail) | 获取缩略图数据。 |

## load

PhonePC/2in1Tablet

load(path: string): void

从指定路径加载笔记文件，调用时机：手写套件初始化之后。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 加载文件的路径。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010400001 | load failed. |

**示例**：

具体代码示例见[示例](pen-handwritecontroller.md#示例)。

## save

PhonePC/2in1Tablet

save(path: string): Promise<void>

保存笔记到指定路径，使用Promise异步回调。调用时机：手写套件加载完之后。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 保存文件的路径。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010400002 | save failed. |

**示例**：

具体代码示例见[示例](pen-handwritecontroller.md#示例)。

## onLoad

PhonePC/2in1Tablet

onLoad(callback: AsyncCallback<string>): void

注册回调，加载完成后将会触发此回调，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当加载成功时，err的message为load success；加载失败时，err的message为load failed；string为加载的路径。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010400001 | load failed. |

## getContentRange

PhonePC/2in1Tablet

getContentRange(): Rect

获取笔迹范围。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [Rect](pen-handwritecontroller.md#rect) | Rect信息参数，表示内容涵盖的矩形区域。 |

## getThumbnail

PhonePC/2in1Tablet

getThumbnail(rect: Rect): Promise<PixelMap>

获取缩略图数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [Rect](pen-handwritecontroller.md#rect) | 是 | Rect信息参数，表示缩略图包含的矩形区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | 缩略图的数据。 |

## Rect

PhonePC/2in1Tablet

Rect信息参数，表示矩形区域。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 矩形左侧的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |
| top | number | 矩形顶部的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |
| right | number | 矩形右侧的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |
| bottom | number | 矩形底部的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |

## scrollTo

PhonePC/2in1Tablet

scrollTo(yOffset: number): void

设置长画布的滚动位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| yOffset | number | 是 | 滚动位置的纵坐标绝对值。单位vp。当前可滚动最大距离为[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)(1000000)减去list组件高度。 |

**示例**：

具体代码示例见[示例](pen-handwritecontroller.md#示例)。

## **示例**

PhonePC/2in1Tablet

```
1. import { HandwriteController, HandwriteComponent, PenType, PenHspInfo } from '@kit.Penkit';

3. @Entry
4. @Component
5. struct HandWriteDemoComp {
6. controller: HandwriteController = new HandwriteController();
7. // 根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考
8. initPath: string = this.getUIContext().getHostContext()?.filesDir + '/aa';
9. penWidth: number = 5;
10. ballpointPenWidth: number = 6;
11. @State yOffset: number = 0;

13. aboutToAppear() {
14. // 加载时设置保存动作完成后的回调。
15. this.controller.onLoad(this.callback);
16. }

18. // 手写文件内容加载完毕渲染上屏后的回调,通知接入用户,可在此处进行自定义行为
19. callback = () => {
20. // 自定义行为,例如文件加载完毕后展示用户操作指导
21. }

23. build() {
24. Row() {
25. Stack({ alignContent: Alignment.TopStart }) {
26. HandwriteComponent({
27. handwriteController: this.controller,
28. defaultPenType: PenType.PEN, // 可选属性，默认笔刷
29. defaultPenInfo: [{ penType: PenType.PEN, penWidth: this.penWidth },
30. { penType: PenType.BALLPOINT_PEN, penWidth: this.ballpointPenWidth }] as PenHspInfo[], //可选属性，各笔刷的默认宽度
31. widthRatio: 1, // 可选属性，自定义画布大小，宽度占比（0-1）。
32. heightRatio: 1, // 可选属性，自定义画布大小，高度占比（0-1）。
33. maxCanvasHeight: 5000, // 可选属性，自定义画布最大高度
34. scaleDisabled: false, // 可选属性，是否禁止缩放
35. onInit: () => {
36. // 画布初始化完成时的回调。此时可以调用接口加载和显示笔记内容
37. this.controller?.load(this.initPath);
38. },
39. onScale: (scale: number) => {
40. // 画布缩放时的回调方法，将返回当前手写控件的缩放比例，可在此处进行自定义行为。
41. },
42. onDidScroll: (yOffset: number) => {
43. // 画布滚动时的回调方法，将返回当前滚动位置的纵坐标，可在此处进行自定义行为。
44. this.yOffset = yOffset
45. }
46. })
47. // 保存及获取缩略图。非必要组件，用户可自行调整或删除。
48. Button("save")
49. .onClick(async () => {
50. // 需根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考
51. const path = this.getUIContext().getHostContext()?.filesDir + '/aa';
52. await this.controller?.save(path).then().catch((error: Error) => {
53. console.info("err：" + error);
54. })
55. // 获取缩略图
56. this.controller.getThumbnail(this.controller?.getContentRange())?.then((pixelMap: PixelMap) => {
57. if (pixelMap) {
58. pixelMap.release()
59. console.info('getThumbnail success')
60. }
61. })
62. })
63. // 设置长画布的滚动位置。当前可滚动最大距离为px2vp(1000000)减去list组件高度。
64. Search()
65. .searchButton('scrollTo').onSubmit((value: string) => {
66. if (!Number.isNaN(Number(value))) {
67. this.controller.scrollTo(Number(value))
68. }
69. }).margin({ top: 100 }).width(220)
70. // 当前画布的偏移量。
71. Text("onDidScroll：" + this.yOffset)
72. .margin({ top: 150 }).width(220)
73. }
74. .width('100%')
75. }
76. .height('100%')
77. }
78. }
```

说明

HandwriteController中的方法需要放在上述示例的画布控件初始化的回调中运行或自定义的方法中运行。

使用前需要先[设置context信息](../harmonyos-guides/pen-suite.md#开发步骤)。

完整示例代码可参考[手写笔服务（ArkTS）](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy)。
