---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-inspector
title: @ohos.arkui.inspector (布局回调)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.inspector (布局回调)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:463e6b907536d75b2639d601bb72ab5e5e9e4043132e820ffe562a331c07ce3e
---

提供注册组件布局和组件绘制送显完成回调通知的能力。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { inspector } from '@kit.ArkUI';
```

## inspector.createComponentObserver(deprecated)

PhonePC/2in1TabletTVWearable

createComponentObserver(id: string): ComponentObserver

绑定指定组件，返回对应的监听句柄。

说明

* 从API version 18开始废弃，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getUIInspector](arkts-apis-uicontext-uicontext.md#getuiinspector)方法获取[UIInspector](arkts-apis-uicontext-uiinspector.md)实例，再通过此实例调用替代方法[createComponentObserver](arkts-apis-uicontext-uiinspector.md#createcomponentobserver)。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getUIInspector](arkts-apis-uicontext-uicontext.md#getuiinspector)方法获取当前UI上下文关联的[UIInspector](arkts-apis-uicontext-uiinspector.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定组件id，该id通过通用属性[id](ts-universal-attributes-component-id.md#id)或者[key](ts-universal-attributes-component-id.md#key12)设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ComponentObserver](js-apis-arkui-inspector.md#componentobserver) | 组件回调事件监听句柄，用于注册和取消注册监听回调。 |

**示例：**

```
1. let listener:inspector.ComponentObserver = inspector.createComponentObserver('COMPONENT_ID'); // 监听id为COMPONENT_ID的组件回调事件
```

## ComponentObserver

PhonePC/2in1TabletTVWearable

组件布局和组件绘制送显完成回调的句柄，包含了申请句柄时的首次查询结果。

### on('layout')

PhonePC/2in1TabletTVWearable

on(type: 'layout', callback: () => void): void

通过句柄向对应的查询条件注册回调，当组件布局完成时会触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'layout'。  layout: 组件布局完成。 |
| callback | () => void | 是 | 监听layout的回调。 |

### off('layout')

PhonePC/2in1TabletTVWearable

off(type: 'layout', callback?: () => void): void

通过句柄向对应的查询条件取消注册回调，当组件布局完成时不再触发指定的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'layout'。  layout: 组件布局完成。 |
| callback | () => void | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和[on('layout')](js-apis-arkui-inspector.md#onlayout)方法中的callback为相同对象时才能取消回调成功。 |

### on('draw')

PhonePC/2in1TabletTVWearable

on(type: 'draw', callback: () => void): void

通过句柄向对应的查询条件注册回调，当组件绘制送显完成时会触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'draw'。  draw: 组件绘制送显完成。 |
| callback | () => void | 是 | 监听draw的回调。 |

### off('draw')

PhonePC/2in1TabletTVWearable

off(type: 'draw', callback?: () => void): void

通过句柄向对应的查询条件取消注册回调，当组件绘制送显完成时不再触发指定的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'draw'。  draw: 组件绘制送显完成。 |
| callback | () => void | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和[on('draw')](js-apis-arkui-inspector.md#ondraw)方法中的callback为相同对象时才能取消回调成功。 |

### on('drawChildren')20+

PhonePC/2in1TabletTVWearable

on(type: 'drawChildren', callback: Callback<void>): void

通过[ComponentObserver](js-apis-arkui-inspector.md#componentobserver)注册drawChildren事件回调方法，当组件的子组件绘制送显完成时会触发该回调方法。如果组件树中存在多个drawChildren事件回调，只会触发在最顶层的drawChildren事件回调。取消最顶层的回调后，其余drawChildren事件回调也无法生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'drawChildren'。  drawChildren: 子组件绘制送显完成。 |
| callback | Callback<void> | 是 | 监听drawChildren的回调。 |

### off('drawChildren')20+

PhonePC/2in1TabletTVWearable

off(type: 'drawChildren', callback?: Callback<void>): void

通过句柄向对应的查询条件取消注册回调，当组件的子组件绘制送显完成时不再触发指定的回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'drawChildren'。  drawChildren: 子组件绘制送显完成。 |
| callback | Callback<void> | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和[on('drawChildren')20+](js-apis-arkui-inspector.md#ondrawchildren20)方法中的callback为相同对象时才能取消回调成功。 |

### onLayoutChildren23+

PhonePC/2in1TabletTVWearable

onLayoutChildren(callback: Callback<void>): void

通过[ComponentObserver](js-apis-arkui-inspector.md#componentobserver)注册layoutChildren事件回调。使用callback异步回调。

把当前注册监听的节点作为根节点，子树中的节点完成布局时，会触发该回调。如果组件树中存在多个layoutChildren事件回调，只会触发在最顶层的layoutChildren事件回调。取消最顶层的回调后，其余layoutChildren事件回调也无法生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 监听layoutChildren的回调。 |

### offLayoutChildren23+

PhonePC/2in1TabletTVWearable

offLayoutChildren(callback?: Callback<void>): void

取消注册layoutChildren事件回调。使用callback异步回调。

要实现在子组件布局完成后停止触发特定回调，只需通过其句柄，在对应的查询条件上取消注册该回调即可。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和[onLayoutChildren23+](js-apis-arkui-inspector.md#onlayoutchildren23)方法中的callback为相同对象时才能取消回调成功。 |

## 示例

PhonePC/2in1TabletTVWearable

以下示例展示了inspector注册组件布局和组件绘制送显完成回调通知能力的基本用法。同时，从API version 23开始新增[onLayoutChildren](js-apis-arkui-inspector.md#onlayoutchildren23)接口，用于监听子树中的节点完成布局时的回调事件。

```
1. import { inspector } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ImageExample {
6. build() {
7. Column() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
9. Row({ space: 5 }) {
10. Image($r('app.media.startIcon'))
11. .width(110)
12. .height(110)
13. .border({ width: 1 })
14. .id('IMAGE_ID')
15. }
16. .id('ROW_ID')
17. }
18. }.height(320).width(360).padding({ right: 10, top: 10 })
19. }

21. listenerForImage: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID')
22. listenerForRow: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('ROW_ID')

24. aboutToAppear() {
25. let onLayoutComplete: () => void = (): void => {
26. // 根据需要补充实现代码
27. }
28. let onDrawComplete: () => void = (): void => {
29. // 根据需要补充实现代码
30. }
31. let onDrawChildrenComplete: () => void = (): void => {
32. // 根据需要补充实现代码
33. }
34. // 绑定当前js实例
35. let FuncLayout = onLayoutComplete
36. let FuncDraw = onDrawComplete
37. let FuncDrawChildren = onDrawChildrenComplete
38. let OffFuncLayout = onLayoutComplete
39. let OffFuncDraw = onDrawComplete
40. let OffFuncDrawChildren = onDrawChildrenComplete

42. this.listenerForImage.on('layout', FuncLayout)
43. this.listenerForImage.on('draw', FuncDraw)
44. this.listenerForRow.on('drawChildren', FuncDrawChildren)

46. // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
47. // this.listenerForImage.off('layout', OffFuncLayout)
48. // this.listenerForImage.off('draw', OffFuncDraw)
49. // this.listenerForRow.off('drawChildren', OffFuncDrawChildren)

51. let onLayoutChildrenComplete: () => void = (): void => {
52. // 监听到LayoutChildren事件后，用户可以自定义实现逻辑。
53. }
54. let uniqueId: number = this.getUniqueId();
55. let listenerForUniqueId: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver(uniqueId)
56. listenerForUniqueId.onLayoutChildren(onLayoutChildrenComplete)
57. // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
58. // listenerForUniqueId.offLayoutChildren(onLayoutChildrenComplete)
59. }
60. }
```
