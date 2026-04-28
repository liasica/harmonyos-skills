---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecomponent
title: HandwriteComponent（手写套件组件）
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS组件 > HandwriteComponent（手写套件组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:90f8d7c8f0ac8fc535dbb07b70e7c778ad90b834c51685967a0d94d81cbf27e6
---

本模块提供手写套件组件，组件包含画布和手写工具栏，集成之后可快速实现手写能力。

需要提供手写画布功能入口和回调，画布将在初始化、加载和保存动作完成时触发回调，可以在回调中自定义应用的行为。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { HandwriteController,HandwriteComponent, PenHspInfo, PenType } from '@kit.Penkit';
```

## HandwriteComponent

PhonePC/2in1Tablet

**模型约束：** 此接口仅可在Stage模型下使用。

**装饰器类型**：@Component

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数**：

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| handwriteController | [HandwriteController](pen-handwritecontroller.md) | 否 | 否 | 手写套件功能类实例。 |
| onInit | [InitCallback](pen-handwritecomponent.md#initcallback) | 否 | 是 | InitCallback：() => void，套件初始化的回调。 |
| onScale | [ScaleCallback](pen-handwritecomponent.md#scalecallback) | 否 | 是 | ScaleCallback：(scale: number) => void，画布缩放的回调。回调方法的参数是当前画布的缩放值。 |
| defaultPenType | [PenType](pen-handwritecomponent.md#pentype) | 否 | 是 | 设置默认笔刷特性。5.1.0(18)版本仅支持通过number类型传参。支持的笔刷有  - 钢笔 - 1  - 圆珠笔 - 2  - 铅笔 - 3  - 马克笔 - 4  - 荧光笔 - 5  - 马赛克笔 - 7  - 橡皮擦 - 8  - 套索 - 9  - 激光笔 - 10  **起始版本**：5.1.0(18) |
| defaultPenInfo | [PenHspInfo](pen-handwritecomponent.md#penhspinfo)[] | 否 | 是 | 设置各笔刷的默认宽度。  **起始版本**：5.1.0(18) |
| widthRatio | number | 否 | 是 | 画布宽度占比。取值范围：0 ~ 1。  **起始版本**：6.0.0(20) |
| heightRatio | number | 否 | 是 | 画布高度占比。取值范围：0 ~ 1。  **起始版本**：6.0.0(20) |
| maxCanvasHeight | number | 否 | 是 | 长画布最大高度。单位vp。取值范围：大于0。  **起始版本**：6.1.0(23) |
| scaleDisabled | boolean | 否 | 是 | 是否禁用画布缩放。true代表禁用缩放，false代表不禁用缩放。默认为false。  **起始版本**：6.1.0(23) |
| onDidScroll | [DidScrollCallback](pen-handwritecomponent.md#didscrollcallback) | 否 | 是 | 画布滚动时的回调。  **起始版本**：6.1.0(23) |

## build

PhonePC/2in1Tablet

build(): void

struct的默认构造函数，无法直接调用此方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

## InitCallback

PhonePC/2in1Tablet

type InitCallback = () => void

套件初始化的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

## ScaleCallback

PhonePC/2in1Tablet

type ScaleCallback = (scale: number) => void

画布缩放的回调。回调方法的参数是当前画布的缩放值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 当前画布的缩放值。 |

## DidScrollCallback

PhonePC/2in1Tablet

type DidScrollCallback = (yOffset: number) => void

画布滚动的回调。回调方法的参数是当前画布的偏移量。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.1.0(23)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| yOffset | number | 是 | 当前画布的偏移量。单位vp。 |

## PenType

PhonePC/2in1Tablet

笔刷枚举类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEN | 1 | 钢笔。 |
| BALLPOINT\_PEN | 2 | 圆珠笔。 |
| PENCIL | 3 | 铅笔。 |
| MARKER | 4 | 马克笔。 |
| HIGHLIGHTER\_BRUSH | 5 | 荧光笔。 |
| MOSAIC | 7 | 马赛克笔。 |
| RUBBER | 8 | 橡皮擦。 |
| LASSO | 9 | 套索。 |
| LASER | 10 | 激光笔。 |

## PenHspInfo

PhonePC/2in1Tablet

笔刷类型及笔宽。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| penType | [PenType](pen-handwritecomponent.md#pentype) | 否 | 否 | 笔刷类型。5.1.0(18)版本仅支持通过number类型传参。 |
| penWidth | number | 否 | 否 | 笔宽。各笔刷默认笔宽和取值范围如下：  - 钢笔 4(2-10)  - 圆珠笔 4(2-10)  - 铅笔 8(4-20)  - 马克笔 32(16-80)  - 荧光笔 32(16-80)  - 马赛克笔 40(8-40)  - 橡皮擦 50(10-120)  - 激光笔 20(8-48) |

**示例**:

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
30. { penType: PenType.BALLPOINT_PEN, penWidth: this.ballpointPenWidth }] as PenHspInfo[], // 可选属性，各笔刷的默认宽度
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
53. console.error("save err：" + error.message);
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
