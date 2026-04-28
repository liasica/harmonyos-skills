---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontroller
title: NodeController
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > NodeController
category: harmonyos-references
scraped_at: 2026-04-28T08:00:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0be8a8d577efe7b88575cc740c55535ba618f101fd69cdce903af083934b1f4d
---

NodeController用于实现自定义节点的创建、显示、更新等操作的管理，并负责将自定义节点挂载到[NodeContainer](ts-basic-components-nodecontainer.md)上。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* NodeController对象不支持使用JSON序列化。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {  NodeController  } from '@kit.ArkUI';
```

## NodeController

PhonePC/2in1TabletTVWearable

通常搭配[NodeContainer](ts-basic-components-nodecontainer.md)进行使用。用于创建控制器管理绑定的[NodeContainer](ts-basic-components-nodecontainer.md)组件。一个NodeController只允许与一个[NodeContainer](ts-basic-components-nodecontainer.md)进行绑定。最佳实践请参考[组件动态创建-组件动态添加、更新和删除](../best-practices/bpta-ui-dynamic-operations.md#section153921947151012)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### makeNode

PhonePC/2in1TabletTVWearable

abstract makeNode(uiContext : UIContext): FrameNode | null

当实例绑定的[NodeContainer](ts-basic-components-nodecontainer.md)创建的时候进行回调。回调方法将返回一个节点，将该节点挂载至[NodeContainer](ts-basic-components-nodecontainer.md)。

或者可以通过NodeController的rebuild()方法进行回调的触发。

说明

[NodeContainer](ts-basic-components-nodecontainer.md)不支持跨实例复用。如果出现跨实例复用[NodeContainer](ts-basic-components-nodecontainer.md)，传入[NodeContainer](ts-basic-components-nodecontainer.md)的[NodeController](js-apis-arkui-nodecontroller.md#nodecontroller-1)触发[makeNode](js-apis-arkui-nodecontroller.md#makenode)回调方法时，入参中的[UIContext](arkts-apis-uicontext-uicontext.md)对象可能为undefined，此时需要开发者判断入参中的[UIContext](arkts-apis-uicontext-uicontext.md)对象是否为undefined，防止后续使用此入参时出现[UIContext无效的JS异常](../harmonyos-guides/arkts-wrong-uicontext-debug.md#定位uicontext错误问题)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 回调该方法的时候，绑定[NodeContainer](ts-basic-components-nodecontainer.md)的UI上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md)| null | 一个FrameNode对象，返回的节点将被挂载至[NodeContainer](ts-basic-components-nodecontainer.md)的占位节点上。若返回null对象，将清空对应[NodeContainer](ts-basic-components-nodecontainer.md)的子节点。 |

### aboutToAppear

PhonePC/2in1TabletTVWearable

aboutToAppear?(): void

当NodeController绑定的[NodeContainer](ts-basic-components-nodecontainer.md)挂载显示后触发此回调。

说明

回调时机参考[onAppear](ts-universal-events-show-hide.md#onappear)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### aboutToDisappear

PhonePC/2in1TabletTVWearable

aboutToDisappear?(): void

当NodeController绑定的[NodeContainer](ts-basic-components-nodecontainer.md)销毁时触发此回调。

说明

回调时机参考[onDisAppear](ts-universal-events-show-hide.md#ondisappear)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### onAttach18+

PhonePC/2in1TabletTVWearable

onAttach?(): void

当NodeController绑定的[NodeContainer](ts-basic-components-nodecontainer.md)挂载至主节点树时触发此回调。

说明

回调时机参考[onAttach](ts-universal-events-show-hide.md#onattach12)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### onDetach18+

PhonePC/2in1TabletTVWearable

onDetach?(): void

当NodeController绑定的[NodeContainer](ts-basic-components-nodecontainer.md)从主节点树卸载时触发此回调。

说明

回调时机参考[onDetach](ts-universal-events-show-hide.md#ondetach12)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### onWillBind18+

PhonePC/2in1TabletTVWearable

onWillBind?(containerId: number): void

当NodeController与[NodeContainer](ts-basic-components-nodecontainer.md)即将绑定前触发此回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](ts-basic-components-nodecontainer.md)即将绑定。 |

### onWillUnbind18+

PhonePC/2in1TabletTVWearable

onWillUnbind?(containerId: number): void

当NodeController与[NodeContainer](ts-basic-components-nodecontainer.md)即将解绑前触发此回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](ts-basic-components-nodecontainer.md)即将解绑。 |

### onBind18+

PhonePC/2in1TabletTVWearable

onBind?(containerId: number): void

当NodeController与[NodeContainer](ts-basic-components-nodecontainer.md)绑定后触发此回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](ts-basic-components-nodecontainer.md)绑定完成。 |

### onUnbind18+

PhonePC/2in1TabletTVWearable

onUnbind?(containerId: number): void

当NodeController与[NodeContainer](ts-basic-components-nodecontainer.md)解绑后触发此回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](ts-basic-components-nodecontainer.md)解绑完成。 |

### aboutToResize

PhonePC/2in1TabletTVWearable

aboutToResize?(size: Size): void

当NodeController绑定的[NodeContainer](ts-basic-components-nodecontainer.md)布局的时候触发此回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Size](js-apis-arkui-graphics.md#size) | 是 | 用于返回组件布局大小的宽和高，单位为vp。 |

### onTouchEvent

PhonePC/2in1TabletTVWearable

onTouchEvent?(event: TouchEvent): void

当NodeController绑定的[NodeContainer](ts-basic-components-nodecontainer.md)收到Touch事件时触发此回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 触摸事件。 |

### rebuild

PhonePC/2in1TabletTVWearable

rebuild(): void

调用此接口通知[NodeContainer](ts-basic-components-nodecontainer.md)组件重新回调[makeNode](js-apis-arkui-nodecontroller.md#makenode)方法，更改子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

由于rebuild方法为应用主动调用的方法，且该操作与UI相关。需要开发者自行保证调用该接口时UI上下文有效，即与绑定的NodeContainer保持UI上下文一致。

监听回调等[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)时，可以通过[UIContext](arkts-apis-uicontext-uicontext.md)的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)方法明确调用时的UI上下文。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（添加节点布局、Touch、挂载和卸载时的生命周期回调）

该示例通过aboutToResize、onTouchEvent，实现了NodeContainer节点布局、收到Touch事件时的生命周期回调功能。

并通过aboutToAppear、aboutToDisappear接口，实现了NodeContainer节点挂载、卸载时的生命周期回调功能。

通过NodeController挂载BuilderNode节点。

```
1. import { NodeController, BuilderNode, Size, FrameNode, UIContext } from '@kit.ArkUI';

3. class Params {
4. text: string = "this is a text"
5. }

7. @Builder
8. function buttonBuilder(params: Params) {
9. Column() {
10. Button(params.text)
11. .fontSize(12)
12. .borderRadius(8)
13. .borderWidth(2)
14. .backgroundColor(Color.Orange)
15. }
16. }

18. class MyNodeController extends NodeController {
19. private buttonNode: BuilderNode<[Params]> | null = null;
20. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

22. makeNode(uiContext: UIContext): FrameNode {
23. if (this.buttonNode == null) {
24. this.buttonNode = new BuilderNode(uiContext);
25. this.buttonNode.build(this.wrapBuilder, { text: "This is a Button" })
26. }
27. return this.buttonNode!.getFrameNode()!;
28. }

30. aboutToResize(size: Size) {
31. console.info(`aboutToResize width : ${size.width} height : ${size.height}`)
32. }

34. aboutToAppear() {
35. console.info("aboutToAppear")
36. }

38. aboutToDisappear() {
39. console.info("aboutToDisappear");
40. }

42. onTouchEvent(event: TouchEvent) {
43. console.info("onTouchEvent");
44. }
45. }

47. @Entry
48. @Component
49. struct Index {
50. private myNodeController: MyNodeController = new MyNodeController();

52. build() {
53. Column() {
54. NodeContainer(this.myNodeController)
55. }
56. .padding({ left: 35, right: 35, top: 35 })
57. .width("100%")
58. .height("100%")
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/imyjv8RuTKaAA2StlVCg-A/zh-cn_image_0000002552799806.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=6DE4BFA14A57D096C3794B31B424D4D3559A3EBB5B53CE1748AEB4AE5EE908F5)

### 示例2（添加节点上下树和绑定解绑前后的生命周期回调）

该示例通过onAttach、onDetach接口，实现了NodeContainer节点上下主节点树的生命周期回调功能。

并通过onWillBind、onWillUnbind、onBind、onUnbind接口，实现了NodeContainer节点绑定和解绑前后的生命周期回调功能。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. class Params {
4. text: string = "this is a text"
5. }

7. @Builder
8. function buttonBuilder(params: Params) {
9. Column() {
10. Button(params.text)
11. .fontSize(20)
12. .borderRadius(8)
13. .borderWidth(2)
14. .backgroundColor(Color.Grey)
15. }
16. }

18. class MyNodeController extends NodeController {
19. private buttonNode: BuilderNode<[Params]> | null = null;
20. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

22. makeNode(uiContext: UIContext): FrameNode {
23. if (this.buttonNode == null) {
24. this.buttonNode = new BuilderNode(uiContext);
25. this.buttonNode.build(this.wrapBuilder, { text: "This is a Button" })
26. }
27. return this.buttonNode!.getFrameNode()!;
28. }

30. onAttach(): void {
31. console.info("myButton on attach");
32. }

34. onDetach(): void {
35. console.info("myButton on detach");
36. }

38. onWillBind(containerId: number): void {
39. console.info(`myButton on WillBind${containerId}`);
40. }

42. onWillUnbind(containerId: number): void {
43. console.info(`myButton on WillUnbind${containerId}`);
44. }

46. onBind(containerId: number): void {
47. console.info(`myButton on bind: ${containerId}`);
48. }

50. onUnbind(containerId: number): void {
51. console.info(`myButton on unbind: ${containerId}`);
52. }
53. }

55. @Entry
56. @Component
57. struct Index {
58. @State buttonShow: boolean = true
59. @State buttonIndex: number = 0
60. private buttonController: MyNodeController = new MyNodeController();
61. private buttonNull: null = null;
62. private buttonControllerArray: Array<MyNodeController | null> = [this.buttonController, this.buttonNull]

64. build() {
65. Column() {
66. Row() {
67. Button("Bind/Unbind")
68. .onClick(() => {
69. this.buttonIndex++;
70. }).margin(5)
71. Button("onAttach/onDetach")
72. .onClick(() => {
73. this.buttonShow = !this.buttonShow
74. }).margin(5)
75. }

77. if (this.buttonShow) {
78. NodeContainer(this.buttonControllerArray[this.buttonIndex % this.buttonControllerArray.length])
79. }
80. }
81. .padding({ left: 35, right: 35 })
82. .width("100%")
83. .height("100%")
84. }
85. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/WOybGZkITdWeF3Yqbe_XAg/zh-cn_image_0000002583439501.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=BD47D7F1FB917A3E9C7A159DA692BE23F33D72F6419338A73CCA936D86DCB6F5)
