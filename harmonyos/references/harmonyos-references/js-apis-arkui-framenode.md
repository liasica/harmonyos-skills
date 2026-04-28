---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode
title: FrameNode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > FrameNode
category: harmonyos-references
scraped_at: 2026-04-28T08:00:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dceace0de0a3b5255ac46c729fcaf6fe5f2abce91eea276685141987386a4880
---

FrameNode表示组件树的实体节点。[NodeController](js-apis-arkui-nodecontroller.md)可通过[BuilderNode](js-apis-arkui-buildernode.md)持有的FrameNode将其挂载到[NodeContainer](ts-basic-components-nodecontainer.md)上，也可通过FrameNode获取[RenderNode](js-apis-arkui-rendernode.md)，挂载到其他FrameNode上。最佳实践请参考[组件动态创建-组件动态添加、更新和删除](../best-practices/bpta-ui-dynamic-operations.md#section153921947151012)。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当前不支持在预览器中使用FrameNode节点。
* FrameNode节点暂不支持拖拽。
* FrameNode对象不支持使用JSON序列化。
* 在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的场景中调用[FrameNode](js-apis-arkui-framenode.md#framenode-1)对象的接口时，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口明确UI上下文，参考[执行绑定UI实例的闭包](../harmonyos-guides/arkts-global-interface.md#执行绑定ui实例的闭包)示例。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FrameNode, LayoutConstraint, ExpandMode, typeNode, NodeAdapter } from "@kit.ArkUI";
```

## LayoutConstraint12+

PhonePC/2in1TabletTVWearable

描述组件的布局约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxSize | [Size](js-apis-arkui-graphics.md#size) | 否 | 否 | 最大尺寸。 |
| minSize | [Size](js-apis-arkui-graphics.md#size) | 否 | 否 | 最小尺寸。 |
| percentReference | [Size](js-apis-arkui-graphics.md#size) | 否 | 否 | 子节点计算百分比时的尺寸基准。 |

## CrossLanguageOptions15+

PhonePC/2in1TabletTVWearable

该接口用于配置或查询FrameNode的跨语言访问权限。例如，针对ArkTS语言创建的节点，可通过该接口控制是否允许通过非ArkTS语言进行属性访问或修改。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attributeSetting | boolean | 否 | 是 | FrameNode是否支持跨ArkTS语言进行属性设置。  true表示支持跨ArkTS语言进行属性设置，false表示不支持跨ArkTS语言进行属性设置。  默认为false。 |

## ExpandMode15+

PhonePC/2in1TabletTVWearable

子节点展开模式枚举。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_EXPAND | 0 | 表示不展开当前FrameNode的子节点。如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，获取在主节点树上的子节点时，不展开当前FrameNode的子节点。子节点序列号按在主节点树上的子节点计算。 |
| EXPAND | 1 | 表示展开当前FrameNode的子节点。如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，获取所有子节点时，展开当前FrameNode的子节点。子节点序列号按所有子节点计算。 |
| LAZY\_EXPAND | 2 | 表示按需展开当前FrameNode的子节点。如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，获取在主树上的子节点时，不展开当前FrameNode的子节点；获取不在主树上的子节点时，展开当前FrameNode的子节点。子节点序列号按所有子节点计算。 |

## InteractionEventBindingInfo19+

PhonePC/2in1TabletTVWearable

组件的交互事件绑定状态信息。如果当前节点上绑定了所要查询的交互事件，调用查询接口时返回一个InteractionEventBindingInfo对象，指示事件绑定详细信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseEventRegistered | boolean | 否 | 否 | 是否以声明方式绑定事件。  true表示以声明方式绑定事件，false表示没有以声明方式绑定事件。 |
| nodeEventRegistered | boolean | 否 | 否 | 是否以自定义组件节点的方式绑定事件，请参考[基础事件示例](js-apis-arkui-framenode.md#基础事件示例)  true表示以自定义组件节点的方式绑定事件，false表示没有以自定义组件节点的方式绑定事件。 |
| nativeEventRegistered | boolean | 否 | 否 | 是否以注册节点事件（[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)）的方式绑定事件。  true表示以注册节点事件的方式绑定事件，false表示没有以注册节点事件的方式绑定事件。 |
| builtInEventRegistered | boolean | 否 | 否 | 组件是否绑定内置事件(组件内部定义的事件, 无需开发者手动绑定)。  true表示组件绑定内置事件，false表示组件没有绑定内置事件。 |

## UIState20+

PhonePC/2in1TabletTVWearable

多态样式状态枚举，用于处理多态样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 正常状态。 |
| PRESSED | 1 << 0 | 按下状态。 |
| FOCUSED | 1 << 1 | 获焦状态。 |
| DISABLED | 1 << 2 | 禁用状态。 |
| SELECTED | 1 << 3 | 选中状态。  仅特定的组件支持此状态：Checkbox、Radio、Toggle、List、Grid、MenuItem。 |

## UIStatesChangeHandler20+

PhonePC/2in1TabletTVWearable

type UIStatesChangeHandler = (node: FrameNode, currentUIStates: number) => void

当UI状态发生变化时触发的回调。接收回调触发时的[UIState](js-apis-arkui-framenode.md#uistate20)状态，该参数的取值为UIState状态枚举值或其运算结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 触发UI状态变化的节点。 |
| currentUIStates | number | 是 | 回调触发时当前的UI状态。  可以通过位与运算判断当前包含哪些[UIState](js-apis-arkui-framenode.md#uistate20)状态。  位与运算方法：if (currentState & UIState.PRESSED == UIState.PRESSED)。  一般的UIState状态检查可以直接判断：if (currentState == UIState.PRESSED)。 |

## FrameNode

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext)

FrameNode的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |

### getRenderNode

PhonePC/2in1TabletTVWearable

getRenderNode(): RenderNode | null

获取FrameNode中持有的[RenderNode](js-apis-arkui-rendernode.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderNode](js-apis-arkui-rendernode.md) | null | 一个RenderNode对象。若该FrameNode不包含RenderNode，则返回空对象null。如果当前FrameNode为声明式组件创建的节点，则返回null。 |

**示例：**

```
1. import { NodeController, FrameNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. private rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);

10. // 获取rootNode持有的RenderNode
11. const renderNode = this.rootNode.getRenderNode();
12. if (renderNode !== null) {
13. renderNode.size = { width: 100, height: 100 };
14. renderNode.backgroundColor = 0XFFFF0000;
15. }

17. return this.rootNode;
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. private myNodeController: MyNodeController = new MyNodeController();

26. build() {
27. Row() {
28. NodeContainer(this.myNodeController)
29. }
30. }
31. }
```

### isModifiable12+

PhonePC/2in1TabletTVWearable

isModifiable(): boolean

判断当前节点是否可修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 判断当前节点是否可修改。  true表示当前节点可修改，false表示当前节点不可修改。  当节点为[自定义组件节点](../harmonyos-guides/arkts-user-defined-node.md#自定义组件节点-framenode)中的系统组件代理节点或节点已经[dispose](js-apis-arkui-framenode.md#dispose12)时返回false。  当返回false时，当前FrameNode不支持[appendChild](js-apis-arkui-framenode.md#appendchild12)、[insertChildAfter](js-apis-arkui-framenode.md#insertchildafter12)、[removeChild](js-apis-arkui-framenode.md#removechild12)、[clearChildren](js-apis-arkui-framenode.md#clearchildren12)、[createAnimation](js-apis-arkui-framenode.md#createanimation20)、[cancelAnimations](js-apis-arkui-framenode.md#cancelanimations20)的操作。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### appendChild12+

PhonePC/2in1TabletTVWearable

appendChild(node: FrameNode): void

在FrameNode最后一个子节点后添加新的子节点。当前FrameNode如果不可修改，抛出异常信息。[typeNode](js-apis-arkui-framenode.md#typenode12)在appendChild时会校验子组件类型或个数，不满足时抛出异常信息，限制情况请查看[typeNode](js-apis-arkui-framenode.md#typenode12)描述。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 需要添加的FrameNode。  node节点不可以为声明式创建的节点，即不可修改的FrameNode。仅有从BuilderNode中获取的声明式节点可以作为子节点。若子节点不符合规格，则抛出异常信息。  node节点不可以拥有父节点，否则抛出异常信息。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted." |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### insertChildAfter12+

PhonePC/2in1TabletTVWearable

insertChildAfter(child: FrameNode, sibling: FrameNode | null): void

在FrameNode指定子节点之后添加新的子节点。当前FrameNode如果不可修改，抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 需要添加的子节点。  child节点不可以为声明式创建的节点，即不可修改的FrameNode。仅有从BuilderNode中获取的声明式节点可以作为子节点。若子节点不符合规格，则抛出异常信息。  child节点不可以拥有父节点，否则抛出异常信息。 |
| sibling | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 是 | 新节点将插入到该节点之后。若该参数设置为空，则新节点将插入到首个子节点之前。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be adopted." |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### removeChild12+

PhonePC/2in1TabletTVWearable

removeChild(node: FrameNode): void

从FrameNode中删除指定的子节点。当前FrameNode如果不可修改，抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 需要删除的子节点。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### clearChildren12+

PhonePC/2in1TabletTVWearable

clearChildren(): void

清除当前FrameNode的所有子节点。当前FrameNode如果不可修改，抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getChild12+

PhonePC/2in1TabletTVWearable

getChild(index: number): FrameNode | null

获取当前节点指定位置的子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 需要查询的子节点的序列号。  index取值范围为[0, +∞)，若当前节点有n个子节点，index取值有效范围为[0, n-1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 子节点。若该FrameNode不包含所查询的子节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getChild15+

PhonePC/2in1TabletTVWearable

getChild(index: number, expandMode?: ExpandMode): FrameNode | null

获取当前节点指定位置的子节点，支持指定子节点展开模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 需要查询的子节点的序列号。  index取值范围为[0, +∞)，若当前节点有n个子节点，index取值有效范围为[0, n-1]。 |
| expandMode | [ExpandMode](js-apis-arkui-framenode.md#expandmode15) | 否 | 指定子节点展开模式。  默认值：ExpandMode.EXPAND |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 子节点。若该FrameNode不包含所查询的子节点，则返回空对象null。 |

**示例：**

请参考[LazyForEach场景节点操作示例](js-apis-arkui-framenode.md#lazyforeach场景节点操作示例)。

### getFirstChildIndexWithoutExpand15+

PhonePC/2in1TabletTVWearable

getFirstChildIndexWithoutExpand(): number

获取当前节点第一个在主节点树上的子节点的序列号。子节点序列号按所有子节点计算。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前节点第一个在主节点树上的子节点的序列号。 |

**示例：**

请参考[LazyForEach场景节点操作示例](js-apis-arkui-framenode.md#lazyforeach场景节点操作示例)。

### getLastChildIndexWithoutExpand15+

PhonePC/2in1TabletTVWearable

getLastChildIndexWithoutExpand(): number

获取当前节点最后一个在主节点树上的子节点的序列号。子节点序列号按所有子节点计算。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前节点最后一个在主节点树上的子节点的序列号。 |

**示例：**

请参考[LazyForEach场景节点操作示例](js-apis-arkui-framenode.md#lazyforeach场景节点操作示例)。

### getFirstChild12+

PhonePC/2in1TabletTVWearable

getFirstChild(): FrameNode | null

获取当前FrameNode的第一个子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 首个子节点。若该FrameNode不包含子节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getNextSibling12+

PhonePC/2in1TabletTVWearable

getNextSibling(): FrameNode | null

获取当前FrameNode的下一个同级节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 当前FrameNode的下一个同级节点。若该FrameNode不包含下一个同级节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPreviousSibling12+

PhonePC/2in1TabletTVWearable

getPreviousSibling(): FrameNode | null

获取当前FrameNode的上一个同级节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 当前FrameNode的上一个同级节点。若该FrameNode不包含上一个同级节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getParent12+

PhonePC/2in1TabletTVWearable

getParent(): FrameNode | null

获取当前FrameNode的父节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 当前FrameNode的父节点。若该FrameNode不包含父节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)和[获取根节点示例](js-apis-arkui-framenode.md#获取根节点示例)。

### getChildrenCount12+

PhonePC/2in1TabletTVWearable

getChildrenCount(): number

获取当前FrameNode的子节点数量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前FrameNode的子节点数量。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### moveTo18+

PhonePC/2in1TabletTVWearable

moveTo(targetParent: FrameNode, index?: number): void

将当前FrameNode移动到目标FrameNode的指定位置。当前FrameNode如果不可修改，抛出异常信息。targetParent为[typeNode](js-apis-arkui-framenode.md#typenode12)时会校验子组件类型或个数，不满足时抛出异常信息，限制情况请查看[typeNode](js-apis-arkui-framenode.md#typenode12)描述。

说明

当前仅支持以下类型的[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)进行移动操作：[Stack](js-apis-arkui-framenode.md#stack12)、[XComponent](js-apis-arkui-framenode.md#xcomponent12)。对于其他类型的节点，移动操作不会生效。

当前仅支持根节点为以下类型组件的[BuilderNode](js-apis-arkui-buildernode.md#buildernode-1)进行移动操作：[Stack](ts-container-stack.md)、[XComponent](ts-basic-components-xcomponent.md)、[EmbeddedComponent](ts-container-embedded-component.md)。对于其他类型的组件，移动操作不会生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetParent | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 目标父节点。  targetParent节点不可以为声明式创建的节点，即不可修改的FrameNode。若目标父节点不符合规格，则抛出异常信息。 |
| index | number | 否 | 子节点序列号。当前FrameNode将被添加到目标FrameNode对应序列号的子节点之前，若目标FrameNode有n个节点，index取值范围为[0, n-1]。  若参数无效或不指定，则添加到目标FrameNode的最后。  默认值：-1 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |
| 100027 | The current node has been adopted. |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToWindow12+

PhonePC/2in1TabletTVWearable

getPositionToWindow(): Position

获取FrameNode相对于窗口的位置偏移，单位为VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于窗口的位置偏移，单位为VP。 |

**示例：**

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode ";

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);
12. this.frameNode = new FrameNode(uiContext);
13. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
14. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
15. this.rootNode.appendChild(this.frameNode);
16. return this.rootNode;
17. }

19. getPositionToWindow() {
20. // 获取FrameNode相对于窗口的位置偏移
21. let positionToWindow = this.rootNode?.getPositionToWindow();
22. console.info(`${TEST_TAG}${JSON.stringify(positionToWindow)}`);
23. }
24. }

26. @Entry
27. @Component
28. struct Index {
29. private myNodeController: MyNodeController = new MyNodeController();
30. private scroller: Scroller = new Scroller();
31. @State index: number = 0;

33. build() {
34. Scroll(this.scroller) {
35. Column({ space: 8 }) {
36. Column() {
37. Text("This is a NodeContainer.")
38. .textAlign(TextAlign.Center)
39. .borderRadius(10)
40. .backgroundColor(0xFFFFFF)
41. .width('100%')
42. .fontSize(16)
43. NodeContainer(this.myNodeController)
44. .borderWidth(1)
45. .width(300)
46. .height(100)
47. }

49. Button("getPositionToWindow")
50. .width(300)
51. .onClick(() => {
52. this.myNodeController.getPositionToWindow();
53. })
54. }
55. .width("100%")
56. }
57. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
58. }
59. }
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToParent12+

PhonePC/2in1TabletTVWearable

getPositionToParent(): Position

获取FrameNode相对于父组件的位置偏移，单位为VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于父组件的位置偏移，单位为VP。 |

**示例：**

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode ";

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);

13. this.frameNode = new FrameNode(uiContext);
14. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
15. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
16. this.rootNode.appendChild(this.frameNode);
17. return this.rootNode;
18. }

20. getPositionToParent() {
21. // 获取FrameNode相对于父组件的位置偏移
22. let positionToParent = this.rootNode?.getPositionToParent();
23. console.info(`${TEST_TAG}${JSON.stringify(positionToParent)}`);
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();
31. private scroller: Scroller = new Scroller();
32. @State index: number = 0;

34. build() {
35. Scroll(this.scroller) {
36. Column({ space: 8 }) {
37. Column() {
38. Text("This is a NodeContainer.")
39. .textAlign(TextAlign.Center)
40. .borderRadius(10)
41. .backgroundColor(0xFFFFFF)
42. .width('100%')
43. .fontSize(16)
44. NodeContainer(this.myNodeController)
45. .borderWidth(1)
46. .width(300)
47. .height(100)
48. }

50. Button("getPositionToParent")
51. .width(300)
52. .onClick(() => {
53. this.myNodeController.getPositionToParent();
54. })
55. }
56. .width("100%")
57. }
58. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
59. }
60. }
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToScreen12+

PhonePC/2in1TabletTVWearable

getPositionToScreen(): Position

获取FrameNode相对于屏幕的位置偏移，单位为VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于屏幕的位置偏移，单位为VP。 |

**示例：**

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode ";

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);

13. this.frameNode = new FrameNode(uiContext);
14. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
15. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
16. this.rootNode.appendChild(this.frameNode);
17. return this.rootNode;
18. }

20. getPositionToScreen() {
21. // 获取FrameNode相对于屏幕的位置偏移
22. let positionToScreen = this.rootNode?.getPositionToScreen();
23. console.info(`${TEST_TAG}${JSON.stringify(positionToScreen)}`);
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();
31. private scroller: Scroller = new Scroller();
32. @State index: number = 0;

34. build() {
35. Scroll(this.scroller) {
36. Column({ space: 8 }) {
37. Column() {
38. Text("This is a NodeContainer.")
39. .textAlign(TextAlign.Center)
40. .borderRadius(10)
41. .backgroundColor(0xFFFFFF)
42. .width('100%')
43. .fontSize(16)
44. NodeContainer(this.myNodeController)
45. .borderWidth(1)
46. .width(300)
47. .height(100)
48. }

50. Button("getPositionToScreen")
51. .width(300)
52. .onClick(() => {
53. this.myNodeController.getPositionToScreen();
54. })
55. }
56. .width("100%")
57. }
58. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
59. }
60. }
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getGlobalPositionOnDisplay20+

PhonePC/2in1TabletTVWearable

getGlobalPositionOnDisplay(): Position

获取FrameNode相对于全局屏幕的位置偏移，单位为VP。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于全局屏幕的位置偏移，单位为VP。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToParentWithTransform12+

PhonePC/2in1TabletTVWearable

getPositionToParentWithTransform(): Position

获取FrameNode相对于父组件带有绘制属性的位置偏移，单位为VP，绘制属性比如[transform](ts-universal-attributes-transformation.md#transform), [translate](ts-universal-attributes-transformation.md#translate)等，返回的坐标是组件布局时左上角变换后的坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于父组件的位置偏移，单位为VP。 当设置了其他（比如：transform, translate等）绘制属性，由于浮点数精度的影响，返回值会有微小偏差。 |

**示例：**

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode ";

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);

13. this.frameNode = new FrameNode(uiContext);
14. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
15. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
16. this.rootNode.appendChild(this.frameNode);
17. return this.rootNode;
18. }

20. getPositionToParentWithTransform() {
21. // 获取FrameNode相对于父组件带有绘制属性的位置偏移
22. let positionToParentWithTransform = this.rootNode?.getPositionToParentWithTransform();
23. console.info(`${TEST_TAG}${JSON.stringify(positionToParentWithTransform)}`);
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();
31. private scroller: Scroller = new Scroller();
32. @State index: number = 0;

34. build() {
35. Scroll(this.scroller) {
36. Column({ space: 8 }) {
37. Column() {
38. Text("This is a NodeContainer.")
39. .textAlign(TextAlign.Center)
40. .borderRadius(10)
41. .backgroundColor(0xFFFFFF)
42. .width('100%')
43. .fontSize(16)
44. NodeContainer(this.myNodeController)
45. .borderWidth(1)
46. .width(300)
47. .height(100)
48. }

50. Button("getPositionToParentWithTransform")
51. .width(300)
52. .onClick(() => {
53. this.myNodeController.getPositionToParentWithTransform();
54. })
55. }
56. .width("100%")
57. }
58. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
59. }
60. }
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToWindowWithTransform12+

PhonePC/2in1TabletTVWearable

getPositionToWindowWithTransform(): Position

获取FrameNode相对于窗口带有绘制属性的位置偏移，单位为VP，绘制属性比如[transform](ts-universal-attributes-transformation.md#transform), [translate](ts-universal-attributes-transformation.md#translate)等，返回的坐标是组件布局时左上角变换后的坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于窗口的位置偏移，单位为VP。 当设置了其他（比如：transform, translate等）绘制属性，由于浮点数精度的影响，返回值会有微小偏差。 |

**示例：**

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode ";

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);

13. this.frameNode = new FrameNode(uiContext);
14. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
15. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
16. this.rootNode.appendChild(this.frameNode);
17. return this.rootNode;
18. }

20. getPositionToWindowWithTransform() {
21. // 获取FrameNode相对于窗口带有绘制属性的位置偏移
22. let positionToWindowWithTransform = this.rootNode?.getPositionToWindowWithTransform();
23. console.info(`${TEST_TAG}${JSON.stringify(positionToWindowWithTransform)}`);
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();
31. private scroller: Scroller = new Scroller();
32. @State index: number = 0;

34. build() {
35. Scroll(this.scroller) {
36. Column({ space: 8 }) {
37. Column() {
38. Text("This is a NodeContainer.")
39. .textAlign(TextAlign.Center)
40. .borderRadius(10)
41. .backgroundColor(0xFFFFFF)
42. .width('100%')
43. .fontSize(16)
44. NodeContainer(this.myNodeController)
45. .borderWidth(1)
46. .width(300)
47. .height(100)
48. }
49. Button("getPositionToWindowWithTransform")
50. .width(300)
51. .onClick(() => {
52. this.myNodeController.getPositionToWindowWithTransform();
53. })
54. }
55. .width("100%")
56. }
57. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
58. }
59. }
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToScreenWithTransform12+

PhonePC/2in1TabletTVWearable

getPositionToScreenWithTransform(): Position

获取FrameNode相对于屏幕带有绘制属性的位置偏移，单位为VP，绘制属性比如[transform](ts-universal-attributes-transformation.md#transform), [translate](ts-universal-attributes-transformation.md#translate)等，返回的坐标是组件布局时左上角变换后的坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于屏幕的位置偏移，单位为VP。 当设置了其他（比如：transform, translate等）绘制属性，由于浮点数精度的影响，返回值会有微小偏差。 |

**示例：**

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode ";

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);

13. this.frameNode = new FrameNode(uiContext);
14. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
15. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
16. this.rootNode.appendChild(this.frameNode);
17. return this.rootNode;
18. }

20. getPositionToScreenWithTransform() {
21. // 获取FrameNode相对于屏幕带有绘制属性的位置偏移
22. let positionToScreenWithTransform = this.rootNode?.getPositionToScreenWithTransform();
23. console.info(`${TEST_TAG}${JSON.stringify(positionToScreenWithTransform)}`);
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();
31. private scroller: Scroller = new Scroller();
32. @State index: number = 0;

34. build() {
35. Scroll(this.scroller) {
36. Column({ space: 8 }) {
37. Column() {
38. Text("This is a NodeContainer.")
39. .textAlign(TextAlign.Center)
40. .borderRadius(10)
41. .backgroundColor(0xFFFFFF)
42. .width('100%')
43. .fontSize(16)
44. NodeContainer(this.myNodeController)
45. .borderWidth(1)
46. .width(300)
47. .height(100)
48. }

50. Button("getPositionToScreenWithTransform")
51. .width(300)
52. .onClick(() => {
53. this.myNodeController.getPositionToScreenWithTransform();
54. })
55. }
56. .width("100%")
57. }
58. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
59. }
60. }
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getMeasuredSize12+

PhonePC/2in1TabletTVWearable

getMeasuredSize(): Size

获取FrameNode测量后的大小，单位为PX。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Size](js-apis-arkui-graphics.md#size) | 节点测量后的大小，单位为PX。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getLayoutPosition12+

PhonePC/2in1TabletTVWearable

getLayoutPosition(): Position

获取FrameNode布局后相对于父组件的位置偏移，单位为PX。该偏移是父容器对该节点进行布局之后的结果，因此布局之后生效的offset属性和不参与布局的position属性不影响该偏移值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点布局后相对于父组件的位置偏移，单位为PX。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigBorderWidth12+

PhonePC/2in1TabletTVWearable

getUserConfigBorderWidth(): Edges<LengthMetrics>

获取用户设置的边框宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的边框宽度。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigPadding12+

PhonePC/2in1TabletTVWearable

getUserConfigPadding(): Edges<LengthMetrics>

获取用户设置的内边距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的内边距。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigMargin12+

PhonePC/2in1TabletTVWearable

getUserConfigMargin(): Edges<LengthMetrics>

获取用户设置的外边距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的外边距。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigSize12+

PhonePC/2in1TabletTVWearable

getUserConfigSize(): SizeT<LengthMetrics>

获取用户设置的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeT](js-apis-arkui-graphics.md#sizett12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的宽高。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getId12+

PhonePC/2in1TabletTVWearable

getId(): string

获取用户设置的节点ID（通用属性设置的[组件标识](ts-universal-attributes-component-id.md)）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用户设置的节点ID（通用属性设置的[组件标识](ts-universal-attributes-component-id.md)）。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUniqueId12+

PhonePC/2in1TabletTVWearable

getUniqueId(): number

获取系统分配的唯一标识的节点UniqueID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 系统分配的唯一标识的节点UniqueID。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getNodeType12+

PhonePC/2in1TabletTVWearable

getNodeType(): string

获取节点的类型。系统组件类型为组件名称，例如，按钮组件[Button](ts-basic-components-button.md)的类型为Button。而对于自定义组件，若其有渲染内容，则其类型为\_\_Common\_\_。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 节点的类型。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getOpacity12+

PhonePC/2in1TabletTVWearable

getOpacity(): number

获取节点的不透明度，最小值为0，最大值为1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 节点的不透明度。范围是[0, 1]，值越大透明度越低。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isVisible12+

PhonePC/2in1TabletTVWearable

isVisible(): boolean

获取节点是否可见。

说明

根据组件设置的visibility属性值判断该节点是否可见。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否可见。  true表示节点可见，false表示节点不可见。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isClipToFrame12+

PhonePC/2in1TabletTVWearable

isClipToFrame(): boolean

获取节点是否是剪裁到组件区域。当调用[dispose](js-apis-arkui-framenode.md#dispose12)解除对实体FrameNode节点的引用关系之后，返回值为true。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否是剪裁到组件区域。  true表示节点剪裁到组件区域，false表示节点不是剪裁到组件区域。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isAttached12+

PhonePC/2in1TabletTVWearable

isAttached(): boolean

获取节点是否被挂载到主节点树上。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否被挂载到主节点树上。  true表示节点被挂载到主节点树上，false表示节点不是被挂载到主节点树上。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isDisposed20+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前FrameNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

请参考[检验FrameNode是否有效示例](js-apis-arkui-framenode.md#检验framenode是否有效示例)。

### getInspectorInfo12+

PhonePC/2in1TabletTVWearable

getInspectorInfo(): Object

获取节点的结构信息，该信息和DevEco Studio内置[ArkUI Inspector](../harmonyos-guides/ide-arkui-inspector.md)工具里面的一致。

说明

getInspectorInfo接口用于获取所有节点的信息，作为调试接口使用，频繁调用会导致性能下降。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 节点的结构信息。 |

以查询[Button](ts-basic-components-button.md)组件节点为例获取到的Object结果部分值如下。

```
1. {
2. "$type": "Button",
3. "$ID": 44,
4. "type": "build-in",
5. "$rect": "[498.00, 468.00],[718.00,598.00]",
6. "$debugLine": "",
7. "$attrs": {
8. "borderStyle": "BorderStyle.Solid",
9. "borderColor": "#FF000000",
10. "borderWidth": "0.00vp",
11. "borderRadius": {
12. "topLeft": "65.00px",
13. "topRight": "65.00px",
14. "bottomLeft": "65.00px",
15. "bottomRight": "65.00px"
16. },
17. "border": "{\"style\":\"BorderStyle.Solid\",\"color\":\"#FF000000\",\"width\":\"0.00vp\",\"radius\":{\"topLeft\":\"65.00px\",\"topRight\":\"65.00px\",\"bottomLeft\":\"65.00px\",\"bottomRight\":\"65.00px\"},\"dashGap\":\"0.00vp\",\"dashWidth\":\"0.00vp\"}",
18. "outlineStyle": "OutlineStyle.SOLID",
19. "outlineColor": "#FF000000"
20. }
21. }
```

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getCustomProperty12+

PhonePC/2in1TabletTVWearable

getCustomProperty(name: string): Object | undefined

通过名称获取组件的自定义属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 自定义属性的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | undefined | 自定义属性的值。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### dispose12+

PhonePC/2in1TabletTVWearable

dispose(): void

立即解除当前FrameNode对象对实体FrameNode节点的引用关系。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

* FrameNode对象调用dispose后，由于不对应任何实体FrameNode节点，在调用部分查询接口([getMeasuredSize](js-apis-arkui-framenode.md#getmeasuredsize12)、[getLayoutPosition](js-apis-arkui-framenode.md#getlayoutposition12))的时候会导致应用出现jscrash。
* 通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)可以判断当前FrameNode是否对应一个实体FrameNode节点。当UniqueId大于0时表示该对象对应一个实体FrameNode节点。

**示例：**

```
1. import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';

3. @Component
4. struct TestComponent {
5. build() {
6. Column() {
7. Text('This is a BuilderNode.')
8. .fontSize(16)
9. .fontWeight(FontWeight.Bold)
10. }
11. .width('100%')
12. .backgroundColor(Color.Gray)
13. }

15. aboutToAppear() {
16. console.info('aboutToAppear');
17. }

19. aboutToDisappear() {
20. console.info('aboutToDisappear');
21. }
22. }

24. @Builder
25. function buildComponent() {
26. TestComponent()
27. }

29. // 继承NodeController实现自定义UI控制器
30. class MyNodeController extends NodeController {
31. private rootNode: FrameNode | null = null;
32. private builderNode: BuilderNode<[]> | null = null;

34. makeNode(uiContext: UIContext): FrameNode | null {
35. this.rootNode = new FrameNode(uiContext);
36. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
37. this.builderNode.build(new WrappedBuilder(buildComponent));

39. const rootRenderNode = this.rootNode.getRenderNode();
40. if (rootRenderNode !== null) {
41. rootRenderNode.size = { width: 200, height: 200 };
42. rootRenderNode.backgroundColor = 0xffd5d5d5;
43. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
44. }

46. return this.rootNode;
47. }

49. disposeFrameNode() {
50. if (this.rootNode !== null && this.builderNode !== null) {
51. // 解除rootNode对实体FrameNode节点的引用关系前，移除rootNode的所有子节点
52. this.rootNode.removeChild(this.builderNode.getFrameNode());
53. // 解除builderNode对实体FrameNode节点的引用关系
54. this.builderNode.dispose();
55. // 解除rootNode对实体FrameNode节点的引用关系
56. this.rootNode.dispose();
57. }
58. }

60. removeBuilderNode() {
61. const rootRenderNode = this.rootNode!.getRenderNode();
62. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
63. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
64. }
65. }
66. }

68. @Entry
69. @Component
70. struct Index {
71. private myNodeController: MyNodeController = new MyNodeController();

73. build() {
74. Column({ space: 4 }) {
75. NodeContainer(this.myNodeController)
76. Button('FrameNode dispose')
77. .onClick(() => {
78. this.myNodeController.disposeFrameNode();
79. })
80. .width('100%')
81. }
82. }
83. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Sx7YUr_UTc6upUwGYf9Ztg/zh-cn_image_0000002583439491.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=2BFC020FC26D3B2CCFA6642D37149D131016DE2B4E887ABEB5CAC2C6C4478B65)

### commonAttribute12+

PhonePC/2in1TabletTVWearable

get commonAttribute(): CommonAttribute

获取FrameNode中持有的CommonAttribute接口，用于设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)。

仅可以修改自定义节点的属性。

说明

FrameNode的效果参考对齐方式为顶部起始端的[Stack](ts-container-stack.md)容器组件。

FrameNode的属性支持情况参考[属性或事件对attributemodifier的支持情况](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#属性或事件对attributemodifier的支持情况)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CommonAttribute | 获取FrameNode中持有的CommonAttribute接口，用于设置通用属性和通用事件。 |

**示例：**

请参考[基础事件示例](js-apis-arkui-framenode.md#基础事件示例)。

### commonEvent12+

PhonePC/2in1TabletTVWearable

get commonEvent(): UICommonEvent

获取FrameNode中持有的UICommonEvent对象，用于设置基础事件。设置的基础事件与声明式定义的事件平行，参与事件竞争；设置的基础事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

LazyForEach场景下，由于存在节点的销毁重建，对于重建的节点需要重新设置事件回调才能保证监听事件正常响应。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UICommonEvent](ts-uicommonevent.md#uicommonevent) | UICommonEvent对象，用于设置基础事件。 |

**示例：**

请参考[基础事件示例](js-apis-arkui-framenode.md#基础事件示例)和[LazyForEach场景基础事件使用示例](js-apis-arkui-framenode.md#lazyforeach场景基础事件使用示例)。

### gestureEvent14+

PhonePC/2in1TabletTVWearable

get gestureEvent(): UIGestureEvent

获取FrameNode中持有的UIGestureEvent对象，用于设置组件绑定的手势事件。通过gestureEvent接口设置的手势不会覆盖通过[声明式手势接口](ts-gesture-settings.md)绑定的手势，两者同时设置了手势时，优先回调声明式接口设置的手势事件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIGestureEvent](ts-uigestureevent.md#uigestureevent) | UIGestureEvent对象，用于设置组件绑定的手势。 |

**示例：**

请参考[手势事件示例](js-apis-arkui-framenode.md#手势事件示例)。

### onDraw12+

PhonePC/2in1TabletTVWearable

onDraw?(context: DrawContext): void

FrameNode的自绘制方法，该方法会重写默认绘制方法，在FrameNode进行内容绘制时被调用。

该接口的[DrawContext](js-apis-arkui-graphics.md#drawcontext)中的Canvas是用于记录指令的临时Canvas，并非节点的真实Canvas。使用请参见[调整自定义绘制Canvas的变换矩阵](../harmonyos-guides/arkts-user-defined-arktsnode-framenode.md#调整自定义绘制canvas的变换矩阵)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [DrawContext](js-apis-arkui-graphics.md#drawcontext) | 是 | 图形绘制上下文。自绘制区域无法超出组件自身大小。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### onMeasure12+

PhonePC/2in1TabletTVWearable

onMeasure(constraint: LayoutConstraint): void

FrameNode的自定义测量方法，该方法会重写默认测量方法，在FrameNode进行测量时被调用，测量FrameNode及其内容的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | [LayoutConstraint](js-apis-arkui-framenode.md#layoutconstraint12) | 是 | 组件进行测量时使用的布局约束。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### onLayout12+

PhonePC/2in1TabletTVWearable

onLayout(position: Position): void

FrameNode的自定义布局方法，该方法会重写默认布局方法，在FrameNode进行布局时被调用，为FrameNode及其子节点指定位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 组件进行布局时使用的位置信息。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### setMeasuredSize12+

PhonePC/2in1TabletTVWearable

setMeasuredSize(size: Size): void

设置FrameNode的测量后的尺寸，默认单位PX。若设置的宽高为负数，自动取零。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Size](js-apis-arkui-graphics.md#size) | 是 | FrameNode的测量后的尺寸。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### setLayoutPosition12+

PhonePC/2in1TabletTVWearable

setLayoutPosition(position: Position): void

设置FrameNode的布局后的位置，默认单位PX。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | FrameNode的布局后的位置。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### measure12+

PhonePC/2in1TabletTVWearable

measure(constraint: LayoutConstraint): void

调用FrameNode的测量方法，根据父容器的布局约束，对FrameNode进行测量，计算出尺寸，如果测量方法被重写，则调用重写的方法。建议在[onMeasure](js-apis-arkui-framenode.md#onmeasure12)方法中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | [LayoutConstraint](js-apis-arkui-framenode.md#layoutconstraint12) | 是 | 组件进行测量时使用的父容器布局约束。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### layout12+

PhonePC/2in1TabletTVWearable

layout(position: Position): void

调用FrameNode的布局方法，为FrameNode及其子节点指定布局位置，如果布局方法被重写，则调用重写的方法。建议在[onLayout](js-apis-arkui-framenode.md#onlayout12)方法中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 组件进行布局时使用的位置信息。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### setNeedsLayout12+

PhonePC/2in1TabletTVWearable

setNeedsLayout(): void

该方法会将FrameNode标记为需要布局的状态，下一帧将会进行重新布局。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### invalidate12+

PhonePC/2in1TabletTVWearable

invalidate(): void

该方法会触发FrameNode自绘制内容的重新渲染。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### addComponentContent12+

PhonePC/2in1TabletTVWearable

addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void

支持添加ComponentContent类型的组件内容。要求当前节点是一个可修改的节点，即[isModifiable](js-apis-arkui-framenode.md#ismodifiable12)的返回值为true，否则抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md)<T> | [ReactiveComponentContent](js-apis-arkui-componentcontent.md#reactivecomponentcontent22)<T>22+ | 是 | FrameNode节点中显示的组件内容。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |

```
1. import { NodeController, FrameNode, ComponentContent, typeNode } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. Column() {
6. Text('hello')
7. .width(50)
8. .height(50)
9. .backgroundColor(Color.Yellow)
10. }
11. }

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. makeNode(uiContext: UIContext): FrameNode | null {
16. let node = new FrameNode(uiContext)
17. node.commonAttribute.width(300).height(300).backgroundColor(Color.Red)
18. let col = typeNode.createNode(uiContext, "Column")
19. col.initialize({ space: 10 })
20. node.appendChild(col)
21. let row4 = typeNode.createNode(uiContext, "Row")
22. row4.attribute.width(200)
23. .height(200)
24. .borderWidth(1)
25. .borderColor(Color.Black)
26. .backgroundColor(Color.Green)
27. // 创建组件内容
28. let component = new ComponentContent<Object>(uiContext, wrapBuilder(buildText))
29. if (row4.isModifiable()) {
30. // 添加新创建的builderText至row4中
31. row4.addComponentContent(component)
32. col.appendChild(row4)
33. }
34. return node
35. }
36. }

38. @Entry
39. @Component
40. struct FrameNodeTypeTest {
41. private myNodeController: MyNodeController = new MyNodeController();

43. build() {
44. Row() {
45. NodeContainer(this.myNodeController);
46. }
47. }
48. }
```

### disposeTree12+

PhonePC/2in1TabletTVWearable

disposeTree(): void

下树并递归释放当前节点为根的子树。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

3. // 自定义挂载事件的自定义组件，作为自定义组件树的入口
4. @Component
5. struct TestComponent {
6. private myNodeController: MyNodeController = new MyNodeController(wrapBuilder(buildComponent2));

8. build() {
9. Column() {
10. Text('This is a BuilderNode.')
11. .fontSize(16)
12. .fontWeight(FontWeight.Bold)
13. NodeContainer(this.myNodeController)
14. }
15. .width('100%')
16. .backgroundColor(Color.Gray)
17. }

19. aboutToAppear() {
20. console.info('BuilderNode aboutToAppear');
21. }

23. aboutToDisappear() {
24. console.info('BuilderNode aboutToDisappear');
25. }
26. }

28. // 自定义挂载事件的自定义组件，作为TestComponent1的子组件与TestComponent3、TestComponent4的父组件
29. @Component
30. struct TestComponent2 {
31. private myNodeController: MyNodeController = new MyNodeController(wrapBuilder(buildComponent3));
32. private myNodeController2: MyNodeController = new MyNodeController(wrapBuilder(buildComponent4));

34. build() {
35. Column() {
36. Text('This is a BuilderNode 2.')
37. .fontSize(16)
38. .fontWeight(FontWeight.Bold)
39. NodeContainer(this.myNodeController)
40. NodeContainer(this.myNodeController2)
41. }
42. .width('100%')
43. .backgroundColor(Color.Gray)
44. }

46. aboutToAppear() {
47. console.info('BuilderNode 2 aboutToAppear');
48. }

50. aboutToDisappear() {
51. console.info('BuilderNode 2 aboutToDisappear');
52. }
53. }

55. // 自定义挂载事件的自定义组件，作为buildComponent2的子组件
56. @Component
57. struct TestComponent3 {
58. build() {
59. Column() {
60. Text('This is a BuilderNode 3.')
61. .fontSize(16)
62. .fontWeight(FontWeight.Bold)

64. }
65. .width('100%')
66. .backgroundColor(Color.Gray)
67. }

69. aboutToAppear() {
70. console.info('BuilderNode 3 aboutToAppear');
71. }

73. aboutToDisappear() {
74. console.info('BuilderNode 3 aboutToDisappear');
75. }
76. }

78. // 自定义挂载事件的自定义组件，作为buildComponent2的子组件
79. @Component
80. struct TestComponent4 {
81. build() {
82. Column() {
83. Text('This is a BuilderNode 4.')
84. .fontSize(16)
85. .fontWeight(FontWeight.Bold)

87. }
88. .width('100%')
89. .backgroundColor(Color.Gray)
90. }

92. aboutToAppear() {
93. console.info('BuilderNode 4 aboutToAppear');
94. }

96. aboutToDisappear() {
97. console.info('BuilderNode 4 aboutToDisappear');
98. }
99. }

101. @Builder
102. function buildComponent() {
103. TestComponent()
104. }

106. @Builder
107. function buildComponent2() {
108. TestComponent2()
109. }

111. @Builder
112. function buildComponent3() {
113. TestComponent3()
114. }

116. @Builder
117. function buildComponent4() {
118. TestComponent4()
119. }

121. // 继承NodeController实现自定义UI控制器
122. class MyNodeController extends NodeController {
123. private rootNode: FrameNode | null = null;
124. private builderNode: BuilderNode<[]> | null = null;
125. private wrappedBuilder: WrappedBuilder<[]>;

127. constructor(builder: WrappedBuilder<[]>) {
128. super();
129. this.wrappedBuilder = builder;
130. }

132. makeNode(uiContext: UIContext): FrameNode | null {
133. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
134. this.builderNode.build(this.wrappedBuilder);

136. return this.builderNode.getFrameNode();
137. }

139. dispose() {
140. if (this.builderNode !== null) {
141. // 下树并递归释放当前节点为根的子树
142. this.builderNode.getFrameNode()?.disposeTree()
143. }
144. }

146. removeBuilderNode() {
147. const rootRenderNode = this.rootNode!.getRenderNode();
148. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
149. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
150. }
151. }
152. }

154. @Entry
155. @Component
156. struct Index {
157. private myNodeController: MyNodeController = new MyNodeController(wrapBuilder(buildComponent));

159. build() {
160. Column({ space: 4 }) {
161. NodeContainer(this.myNodeController)
162. Button('BuilderNode dispose')
163. .onClick(() => {
164. this.myNodeController.dispose();
165. })
166. .width('100%')
167. Button('BuilderNode rebuild')
168. .onClick(() => {
169. this.myNodeController.rebuild();
170. })
171. .width('100%')
172. }
173. }
174. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/hh9L0SK7SN2nQJNgIB1DoQ/zh-cn_image_0000002552959446.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=44CA5C7842933D0F578148F0ECB1C3A71DEA48B079839569096052C0D9C8D5F1)

### setCrossLanguageOptions15+

PhonePC/2in1TabletTVWearable

setCrossLanguageOptions(options: CrossLanguageOptions): void

设置当前FrameNode的跨ArkTS语言访问选项。例如ArkTS语言创建的节点，设置该节点是否可通过非ArkTS语言进行属性设置。当前FrameNode如果不可修改或不可设置跨ArkTS语言访问选项，抛出异常信息。

说明

当前仅支持[Scroll](js-apis-arkui-framenode.md#scroll12), [Swiper](js-apis-arkui-framenode.md#swiper12)，[List](js-apis-arkui-framenode.md#list12)，[ListItem](js-apis-arkui-framenode.md#listitem12)，[ListItemGroup](js-apis-arkui-framenode.md#listitemgroup12)，[WaterFlow](js-apis-arkui-framenode.md#waterflow12)，[FlowItem](js-apis-arkui-framenode.md#flowitem12)，[Grid](js-apis-arkui-framenode.md#grid14)，[GridItem](js-apis-arkui-framenode.md#griditem14)，[TextInput](js-apis-arkui-framenode.md#textinput12)，[TextArea](js-apis-arkui-framenode.md#textarea14)，[Column](js-apis-arkui-framenode.md#column12)，[Row](js-apis-arkui-framenode.md#row12)，[Stack](js-apis-arkui-framenode.md#stack12)，[Flex](js-apis-arkui-framenode.md#flex12)，[RelativeContainer](js-apis-arkui-framenode.md#relativecontainer12)，[Progress](js-apis-arkui-framenode.md#progress12)，[LoadingProgress](js-apis-arkui-framenode.md#loadingprogress12)，[Image](js-apis-arkui-framenode.md#image12)，[Button](js-apis-arkui-framenode.md#button12)，[CheckBox](js-apis-arkui-framenode.md#checkbox18)，[Radio](js-apis-arkui-framenode.md#radio18)，[Slider](js-apis-arkui-framenode.md#slider18)，[Toggle](js-apis-arkui-framenode.md#toggle18)，[XComponent](js-apis-arkui-framenode.md#xcomponent12)类型的[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)设置跨ArkTS语言访问选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CrossLanguageOptions](js-apis-arkui-framenode.md#crosslanguageoptions15) | 是 | 跨ArkTS语言访问选项。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100022 | The FrameNode cannot be set whether to support cross-language common attribute setting. |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getCrossLanguageOptions15+

PhonePC/2in1TabletTVWearable

getCrossLanguageOptions(): CrossLanguageOptions

获取当前FrameNode的跨ArkTS语言访问选项。例如ArkTS语言创建的节点，返回该节点是否可通过非ArkTS语言进行属性设置。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CrossLanguageOptions](js-apis-arkui-framenode.md#crosslanguageoptions15) | 跨ArkTS语言访问选项。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getInteractionEventBindingInfo19+

PhonePC/2in1TabletTVWearable

getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined

获取目标节点的事件绑定信息，如果该组件节点上没有绑定要查询的交互事件类型时，返回 undefined。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | [EventQueryType](ts-appendix-enums.md#eventquerytype19) | 是 | 要查询的交互事件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InteractionEventBindingInfo](js-apis-arkui-framenode.md#interactioneventbindinginfo19) | undefined | 如果当前节点上绑定了任意交互事件，则返回一个InteractionEventBindingInfo对象，指示事件绑定详细信息，如果没有绑定任何交互事件则返回undefined。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### recycle18+

PhonePC/2in1TabletTVWearable

recycle(): void

全局复用场景下，触发子组件回收，彻底释放FrameNode后端资源，以便于资源的重新复用，确保后端资源能够被有效回收并再次使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[节点复用回收使用示例](js-apis-arkui-framenode.md#节点复用回收使用示例)。

### reuse18+

PhonePC/2in1TabletTVWearable

reuse(): void

全局复用场景下，触发子组件复用，实现FrameNode后端资源的复用，提升资源利用效率。为保证资源充足，可以在recycle之后使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[节点复用回收使用示例](js-apis-arkui-framenode.md#节点复用回收使用示例)。

### addSupportedUIStates20+

PhonePC/2in1TabletTVWearable

addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void

设置组件支持的多态样式状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiStates | number | 是 | 需要处理目标节点的UI状态。  可以通过位或计算同时指定设置多个状态，如：targetUIStates = UIState.PRESSED | UIState.FOCUSED。 |
| statesChangeHandler | [UIStatesChangeHandler](js-apis-arkui-framenode.md#uistateschangehandler20) | 是 | 状态变化时的回调函数。 |
| excludeInner | boolean | 否 | 禁止内部默认状态样式处理的标志，默认值为false。  true表示禁止内部默认状态样式处理，false不禁止内部默认状态样式处理。 |

**示例：**

请参考[组件设置和删除多态样式状态示例](js-apis-arkui-framenode.md#组件设置和删除多态样式状态示例)。

### removeSupportedUIStates20+

PhonePC/2in1TabletTVWearable

removeSupportedUIStates(uiStates: number): void

删除组件当前注册的状态处理。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiStates | number | 是 | 需要删除的UI状态。  可以通过位或计算同时指定删除多个状态，如：removeUIStates = UIState.PRESSED | UIState.FOCUSED。 |

**示例：**

请参考[组件设置和删除多态样式状态示例](js-apis-arkui-framenode.md#组件设置和删除多态样式状态示例)。

### createAnimation20+

PhonePC/2in1TabletTVWearable

createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean

创建FrameNode上属性的动画。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [AnimationPropertyType](ts-appendix-enums.md#animationpropertytype20) | 是 | 动画属性枚举。 |
| startValue | Optional<number[]> | 是 | 动画属性的起始值。取值为undefined或数组，取值为数组时数组长度需要和属性枚举匹配。如果为undefined则表示不显式指定动画初值，节点上一次设置的属性终值为此次动画的起点值。如果取值为数组，  - 对于AnimationPropertyType.ROTATION，取值格式为[rotationX, rotationY, rotationZ]，单位为度（°），表示绕x、y、z轴的旋转角。  - 对于AnimationPropertyType.TRANSLATION，取值格式为[translateX, translateY]，单位为px，表示沿x、y轴的平移量。  - 对于AnimationPropertyType.SCALE，取值格式为[scaleX, scaleY]，表示x、y方向的缩放比例。  - 对于AnimationPropertyType.OPACITY，取值格式为[opacity]，表示不透明度。opacity的取值范围为[0, 1]。  当节点上从未设置过该属性时，需要显式指定startValue才能正常创建动画。当节点上已经设置过属性（如第二次及之后创建动画），则推荐不显式指定startValue或者显式指定startValue为上一次的终值，表示使用上一次的终值作为新的动画起点，避免起始值跳变。 |
| endValue | number[] | 是 | 动画属性的终止值。取值为数组，数组长度需要和属性枚举匹配。  - 对于AnimationPropertyType.ROTATION，取值格式为[rotationX, rotationY, rotationZ]，单位为度（°），表示绕x、y、z轴的旋转角。  - 对于AnimationPropertyType.TRANSLATION，取值格式为[translateX, translateY]，单位为px，表示沿x、y轴的平移量。  - 对于AnimationPropertyType.SCALE，取值格式为[scaleX, scaleY]，表示x、y方向的缩放比例。  - 对于AnimationPropertyType.OPACITY，取值格式为[opacity]，表示不透明度。opacity的取值范围为[0, 1]。 |
| param | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 动画参数。包含时长、动画曲线、结束回调等参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示动画是否创建成功。  返回值为true：动画创建成功，如果动画参数中设置结束回调，动画结束后会调用结束回调。  返回值为false：动画创建失败，即使动画参数中设置结束回调，结束回调也不会被调用。  可能导致动画创建失败的原因：  1. 节点已经释放，调用过[dispose](js-apis-arkui-framenode.md#dispose12)方法。  2. 对于系统组件的代理节点，即对于[isModifiable](js-apis-arkui-framenode.md#ismodifiable12)为false的节点，调用该接口会失败。  3. 属性枚举非法，或属性枚举需要的长度与startValue或endValue的长度不匹配。  4. 该属性在第一次创建动画时没有显式指定startValue导致没有动画起点值，或设置的动画终值和动画起始值（当startValue为undefined时动画起始值为上一次的终值）相同，此时无动画产生。 |

**示例：**

请参考[动画创建与取消示例](js-apis-arkui-framenode.md#动画创建与取消示例)。

### cancelAnimations20+

PhonePC/2in1TabletTVWearable

cancelAnimations(properties: AnimationPropertyType[]): boolean

请求取消FrameNode上指定属性上的所有动画，该方法需在节点所处线程中调用，会阻塞当前线程以等待取消结果。如果动画成功取消，节点上的属性值会被恢复为取消时的显示值（即当前状态）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | [AnimationPropertyType](ts-appendix-enums.md#animationpropertytype20)[] | 是 | 待取消的动画属性枚举数组。可以一次取消一个节点上的多个属性的动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示动画是否取消成功。  返回值为true：动画取消成功。  返回值为false：动画取消失败。  可能导致动画取消失败的原因：  1. 节点已经释放，调用过[dispose](js-apis-arkui-framenode.md#dispose12)方法。  2. 对于系统组件的代理节点，即对于[isModifiable](js-apis-arkui-framenode.md#ismodifiable12)为false的节点，调用该接口会失败。  3. 属性枚举数组存在非法枚举值。  4. 系统异常。如发生ipc异常导致动画取消失败。  1. 即使属性上没有动画，尝试取消该属性的动画，在无系统异常情况下调用取消接口也会返回true。  2. 如果开发者保证传入参数合法且节点正常，返回false时表明发生了系统异常。此时开发者可隔一段时间后再次尝试取消，或通过调用duration为0的[createAnimation](js-apis-arkui-framenode.md#createanimation20)接口停止属性上的动画。 |

**示例：**

请参考[动画创建与取消示例](js-apis-arkui-framenode.md#动画创建与取消示例)。

### getNodePropertyValue20+

PhonePC/2in1TabletTVWearable

getNodePropertyValue(property: AnimationPropertyType): number[]

获取FrameNode上的属性值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [AnimationPropertyType](ts-appendix-enums.md#animationpropertytype20) | 是 | 动画属性枚举。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 表示渲染节点上的属性值，返回的数组长度与属性枚举相关，异常时返回空数组。  对不同属性枚举的返回值格式：  - 当节点已经释放，调用过[dispose](js-apis-arkui-framenode.md#dispose12)方法，或者属性枚举非法时，返回长度为0的空数组。  - 对于AnimationPropertyType.ROTATION，返回值为[rotationX, rotationY, rotationZ]，单位为度（°），表示绕x、y、z轴的旋转角。  - 对于AnimationPropertyType.TRANSLATION，返回值为[translateX, translateY]，单位为px，表示沿x、y轴的平移量。  - 对于AnimationPropertyType.SCALE，返回值为[scaleX, scaleY]，表示x、y方向的缩放比例。  - 对于AnimationPropertyType.OPACITY，返回值为[opacity]，表示不透明度。  1. 动画正常取消后，节点上的属性值被恢复为取消时的值，通过该接口可以获取取消后的显示值。  2. 动画期间该接口的返回值为该属性的终值，而不是动画过程的实时值。 |

**示例：**

请参考[动画创建与取消示例](js-apis-arkui-framenode.md#动画创建与取消示例)。

### invalidateAttributes21+

PhonePC/2in1TabletTVWearable

invalidateAttributes(): void

在当前帧触发节点属性更新。

当前节点的属性在构建阶段后被修改，这些改动不会立即生效，而是延迟到下一帧统一处理。

此功能强制当前帧内即时节点更新，确保同步应用渲染效果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

从API version 21开始，通过if else动态切换两个节点，并且在节点创建时调用invalidateAttributes即时触发节点属性更新，避免组件切换过程中出现闪烁。

```
1. // index.ets
2. import { FrameNode, NodeController, typeNode, NodeContent } from '@kit.ArkUI';

4. // 继承NodeController实现自定义NodeAdapter控制器
5. class MyNodeAdapterController extends NodeController {
6. rootNode: FrameNode | null = null;
7. imageUrl: string = "";

9. constructor(imageUrl: string) {
10. super();
11. this.imageUrl = imageUrl;
12. }

14. makeNode(uiContext: UIContext): FrameNode | null {
15. let imageNode = typeNode.createNode(uiContext, "Image");
16. imageNode.initialize($r(this.imageUrl))
17. imageNode.attribute.syncLoad(true).width(100).height(100);
18. // 强制当前帧内即时节点更新，避免出现切换闪烁
19. imageNode.invalidateAttributes();
20. return imageNode;
21. }
22. }

24. // 自定义挂载事件的自定义组件，挂载前加载样例图片
25. @Component
26. struct NodeComponent3 {
27. private rootSlot: NodeContent = new NodeContent();

29. aboutToAppear(): void {
30. const uiContext = this.getUIContext();
31. let imageNode = typeNode.createNode(uiContext, "Image");
32. imageNode.initialize($r('app.media.startIcon'))
33. imageNode.attribute.syncLoad(true).width(100).height(100);
34. imageNode.invalidateAttributes();
35. this.rootSlot.addFrameNode(imageNode);
36. }

38. build() {
39. ContentSlot(this.rootSlot)
40. }
41. }

43. // 自定义挂载事件的自定义组件，挂载前加载样例图片
44. @Component
45. struct NodeComponent4 {
46. private rootSlot: NodeContent = new NodeContent();

48. aboutToAppear(): void {
49. const uiContext = this.getUIContext();
50. let imageNode = typeNode.createNode(uiContext, "Image");
51. imageNode.initialize($r('app.media.startIcon'))
52. imageNode.attribute.syncLoad(true).width(100).height(100);
53. imageNode.invalidateAttributes();
54. this.rootSlot.addFrameNode(imageNode);
55. }

57. build() {
58. ContentSlot(this.rootSlot)
59. }
60. }

62. @Entry
63. @Component
64. struct ListNodeTest {
65. @State flag: boolean = true;
66. adapterController: MyNodeAdapterController = new MyNodeAdapterController('app.media.startIcon');

68. build() {
69. Column() {
70. Text("ListNode Adapter");
71. if (this.flag) {
72. NodeComponent3()
73. } else {
74. NodeComponent4()
75. }
76. if (this.flag) {
77. NodeContainer(this.adapterController)
78. .width(300).height(300)
79. .borderWidth(1).borderColor(Color.Black)
80. } else {
81. NodeContainer(this.adapterController)
82. .width(300).height(300)
83. .borderWidth(1).borderColor(Color.Black)
84. }
85. if (this.flag) {
86. Image($r('app.media.startIcon')).width(100).height(100).syncLoad(true)
87. } else {
88. Image($r('app.media.startIcon')).width(100).height(100).syncLoad(true)
89. }
90. Button('change').onClick(() => {
91. this.flag = !this.flag;
92. })
93. }
94. .borderWidth(1)
95. .width("100%")
96. }
97. }
```

### adoptChild22+

PhonePC/2in1TabletTVWearable

adoptChild(child: FrameNode): void

当前节点接纳目标节点为附属节点。被接纳的附属节点不能已有父节点。调用该接口实际上不会将其添加为子节点，而是仅允许其接收对应子节点的生命周期回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 指定待被接纳的节点。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The current FrameNode is not modifiable. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be disposed." |
| 100026 | The current FrameNode has been disposed. |

**示例：**

完整示例请参考[接纳为附属节点示例](js-apis-arkui-framenode.md#接纳为附属节点示例)。

### removeAdoptedChild22+

PhonePC/2in1TabletTVWearable

removeAdoptedChild(child: FrameNode): void

移除被接纳的目标附属节点。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 正在被接纳的节点。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The current FrameNode is not modifiable. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be null." |
| 100026 | The current FrameNode has been disposed. |

**示例：**

完整示例请参考[接纳为附属节点示例](js-apis-arkui-framenode.md#接纳为附属节点示例)。

### convertPosition22+

PhonePC/2in1TabletTVWearable

convertPosition(position: Position, targetNode: FrameNode): Position

将点的坐标从当前节点的坐标系转换为目标节点的坐标系。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 当前节点坐标系中的相对坐标。 |
| targetNode | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 本次坐标转换的目标节点，转换得到的点坐标就是该节点坐标系中的相对坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 目标节点局部坐标系中的转换坐标。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100024 | The current FrameNode and the target FrameNode do not have a common ancestor node. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'targetNode' is invalid: it cannot be disposed." |

**示例：**

```
1. @Entry
2. @Component
3. struct ConvertPositionTestOnly {
4. private uiContext: UIContext = this.getUIContext();
5. @State message: string = 'Hello World';
6. @State nodeAOk: boolean = false;
7. @State nodeBOK: boolean = false;

9. build() {
10. Column() {
11. Text(this.message)
12. .id('testNodeA')
13. .fontSize($r('app.float.page_text_font_size'))
14. .fontWeight(FontWeight.Bold)
15. .onAppear(() => {
16. this.nodeAOk = true
17. })
18. Column() {
19. Text('testNodeB')
20. .id('testNodeB')
21. .fontSize($r('app.float.page_text_font_size'))
22. .fontWeight(FontWeight.Bold)
23. .onAppear(() => {
24. this.nodeBOK = true
25. })

27. }

29. Button('运行convertPosition测试')
30. .onClick(() => {
31. this.runBasicTest();
32. })
33. .margin(20)

35. }
36. .width('100%')
37. .height('100%')
38. }

40. private runBasicTest() {
41. if (!this.nodeAOk || !this.nodeBOK) {
42. return
43. }

45. // 等待UI渲染完成
46. if (!this.uiContext) {
47. return
48. }
49. const nodeA = this.uiContext.getAttachedFrameNodeById('testNodeA');
50. const nodeB = this.uiContext.getAttachedFrameNodeById('testNodeB');

52. if (!nodeA || !nodeB) {
53. console.info('无法获取测试节点');
54. return;
55. }

57. const testPoint: Position = { x: 10, y: 10 };
58. const result: Position | undefined = nodeA.convertPosition({ x: 30, y: 10 }, nodeB); // 显式声明可能返回undefined
59. if (result === undefined) {
60. console.info("convertPosition 转换失败，返回 undefined");
61. return;
62. }
63. console.info(`输出: (${result.x}, ${result.y})`);

65. }
66. }
```

### isInRenderState23+

PhonePC/2in1TabletTVWearable

isInRenderState(): boolean

获取节点是否处于渲染状态，如果一个节点的对应RenderNode在渲染树上，则处于渲染状态。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否处于渲染状态。  true：处于渲染状态；false：不处于渲染状态。 |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'is on render tree';
7. @State @Watch('change') isShow: boolean = true;
8. data: Array<string> = ['hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7', 'hello8'];

10. // 监听状态变化后打印是否处于渲染状态
11. change() {
12. let buttonNode = this.getUIContext().getFrameNodeById("testButton");
13. if (buttonNode == null) {
14. return;
15. }
16. let isOnRenderTree = buttonNode!.isInRenderState();
17. if (isOnRenderTree) {
18. hilog.info(1, 'frameNode', 'is on render tree');
19. } else {
20. hilog.info(1, 'frameNode', 'is not on render tree');
21. }
22. }

24. build() {
25. Column() {
26. Button('change button visibility').onClick(() => {
27. // 修改button的visibility状态
28. this.isShow = !this.isShow;
29. })
30. .margin({ top: 20 })
31. Button('test button')
32. .visibility(this.isShow ? Visibility.Visible : Visibility.Hidden)
33. .margin(20).id('testButton')

35. List() {
36. ForEach(this.data, (item: string, index: number) => {
37. ListItem() {
38. Text(item).id(item)
39. }.alignSelf(ItemAlign.Center).width('100%')
40. })
41. }
42. .width('30%')
43. .alignSelf(ItemAlign.Center)
44. .height("10%")
45. .onReachEnd(() => {
46. let textNode8 = this.getUIContext().getFrameNodeById("hello8");
47. if (textNode8 != null) {
48. let isOnRenderTree = textNode8!.isInRenderState();
49. hilog.info(1, 'frameNode', 'is hello8 on RenderTree: %{public}s', isOnRenderTree);
50. }
51. let textNode1 = this.getUIContext().getFrameNodeById("hello1");
52. if (textNode1 != null) {
53. let isOnRenderTree = textNode1!.isInRenderState();
54. isOnRenderTree ? this.message = 'is on render tree' : 'is not on render tree'
55. hilog.info(1, 'frameNode', 'is hello1 on RenderTree: %{public}s', isOnRenderTree);
56. }
57. })
58. }
59. .height('100%')
60. .width('100%')
61. }
62. }
```

### isOnMainTree23+

PhonePC/2in1TabletTVWearable

isOnMainTree(): boolean

查询节点是否被挂载到主节点树上。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否被挂载到主节点树上。  true表示节点被挂载到主节点树上，false表示节点没有被挂载到主节点树上。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100026 | The current FrameNode has been disposed. |

**示例：**

```
1. import { NodeController, FrameNode, UIContext, typeNode } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TEST_TAG: string = 'FrameNode '

6. // 继承NodeController实现自定义UI控制器
7. class MyNodeController extends NodeController {
8. public frameNode: FrameNode | null = null;
9. public childList: Array<FrameNode> = new Array<FrameNode>();
10. private rootNode: FrameNode | null = null;
11. private uiContext: UIContext | null = null;
12. private childrenCount: number = 0;

14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext);
16. this.uiContext = uiContext;

18. this.frameNode = new FrameNode(uiContext);
19. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
20. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
21. this.addCommonEvent(this.frameNode)
22. this.rootNode.appendChild(this.frameNode);
23. this.childrenCount = this.childrenCount + 1;
24. for (let i = 0; i < 10; i++) {
25. let childNode = new FrameNode(uiContext);
26. this.childList.push(childNode);
27. this.frameNode.appendChild(childNode);
28. }
29. let stackNode = typeNode.createNode(uiContext, 'Stack');
30. this.frameNode.appendChild(stackNode);
31. return this.rootNode;
32. }

34. addCommonEvent(frameNode: FrameNode) {
35. frameNode.commonEvent.setOnClick((event: ClickEvent) => {
36. console.info(`Click FrameNode: ${JSON.stringify(event)}`)
37. })
38. }

40. createFrameNode() {
41. let frameNode = new FrameNode(this.uiContext!);
42. frameNode.commonAttribute.backgroundColor(Color.Pink);
43. frameNode.commonAttribute.size({ width: 100, height: 100 });
44. frameNode.commonAttribute.position({ x: this.childrenCount * 120, y: 0 });

46. return frameNode;
47. }

49. appendChild() {
50. const childNode = this.createFrameNode();
51. this.rootNode!.appendChild(childNode);
52. this.childrenCount = this.childrenCount + 1;
53. }

55. insertChildAfter(index: number) {
56. let insertNode = this.createFrameNode();
57. let childNode = this.rootNode!.getChild(index);
58. this.rootNode!.insertChildAfter(insertNode, childNode);
59. this.childrenCount = this.childrenCount + 1;
60. }

62. removeChild(index: number) {
63. let childNode = this.rootNode!.getChild(index);
64. if (childNode == null) {
65. console.info(`${TEST_TAG} getchild at index {${index}} : fail`);
66. return;
67. }
68. this.rootNode!.removeChild(childNode);
69. this.childrenCount = this.childrenCount - 1;
70. }

72. getChildNumber() {
73. console.info(`${TEST_TAG} getChildNumber ${this.rootNode!.getChildrenCount()}`)
74. console.info(`${TEST_TAG} children count is ${this.childrenCount}`);
75. }

77. clearChildren() {
78. this.rootNode!.clearChildren();
79. }

81. searchFrameNode() {
82. if (this.rootNode!.getFirstChild() === null) {
83. console.info(`${TEST_TAG} the rootNode does not have child node.`)
84. }
85. if (this.rootNode!.getFirstChild() === this.frameNode) {
86. console.info(`${TEST_TAG} getFirstChild  result: success. The first child of the rootNode is equals to frameNode.`);
87. } else {
88. console.info(`${TEST_TAG} getFirstChild  result: fail. The first child of the rootNode is not equals to frameNode.`);
89. }
90. if (this.frameNode!.getChild(5) === this.frameNode!.getChild(4)!.getNextSibling()) {
91. console.info(`${TEST_TAG} getNextSibling  result: success.`);
92. } else {
93. console.info(`${TEST_TAG} getNextSibling  result: fail.`);
94. }
95. if (this.frameNode!.getChild(3) === this.frameNode!.getChild(4)!.getPreviousSibling()) {
96. console.info(`${TEST_TAG} getPreviousSibling  result: success.`);
97. } else {
98. console.info(`${TEST_TAG} getPreviousSibling  result: fail.`);
99. }
100. if (this.rootNode!.getFirstChild() !== null && this.rootNode!.getFirstChild()!.getParent() === this.rootNode) {
101. console.info(`${TEST_TAG} getParent  result: success.`);
102. } else {
103. console.info(`${TEST_TAG} getParent  result: fail.`);
104. }
105. if (this.rootNode!.getParent() !== undefined || this.rootNode!.getParent() !== null) {
106. console.info(`${TEST_TAG} get ArkTsNode success.`)
107. console.info(`${TEST_TAG} check rootNode whether is modifiable ${this.rootNode!.isModifiable()}`)
108. console.info(`${TEST_TAG} check getParent whether is modifiable ${this.rootNode!.getParent()!.isModifiable()}`)
109. } else {
110. console.info(`${TEST_TAG} get ArkTsNode fail.`);
111. }
112. }

114. moveFrameNode() {
115. const currentNode = this.frameNode!.getChild(10);
116. try {
117. currentNode!.moveTo(this.rootNode, 0);
118. if (this.rootNode!.getChild(0) === currentNode) {
119. console.info(`${TEST_TAG} moveTo  result: success.`);
120. } else {
121. console.info(`${TEST_TAG} moveTo  result: fail.`);
122. }
123. } catch (err) {
124. console.info(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
125. console.info(`${TEST_TAG} moveTo  result: fail.`);
126. }
127. }

129. getPositionToWindow() {
130. let positionToWindow = this.rootNode?.getPositionToWindow();
131. console.info(`${TEST_TAG}${JSON.stringify(positionToWindow)}`);
132. }

134. getPositionToParent() {
135. let positionToParent = this.rootNode?.getPositionToParent();
136. console.info(`${TEST_TAG}${JSON.stringify(positionToParent)}`);
137. }

139. getPositionToScreen() {
140. let positionToScreen = this.rootNode?.getPositionToScreen();
141. console.info(`${TEST_TAG}${JSON.stringify(positionToScreen)}`);
142. }

144. getGlobalPositionOnDisplay() {
145. let positionOnGlobalDisplay = this.rootNode?.getGlobalPositionOnDisplay();
146. console.info(`${TEST_TAG}${JSON.stringify(positionOnGlobalDisplay)}`);
147. }

149. getPositionToWindowWithTransform() {
150. let positionToWindowWithTransform = this.rootNode?.getPositionToWindowWithTransform();
151. console.info(`${TEST_TAG}${JSON.stringify(positionToWindowWithTransform)}`);
152. }

154. getPositionToParentWithTransform() {
155. let positionToParentWithTransform = this.rootNode?.getPositionToParentWithTransform();
156. console.info(`${TEST_TAG}${JSON.stringify(positionToParentWithTransform)}`);
157. }

159. getPositionToScreenWithTransform() {
160. let positionToScreenWithTransform = this.rootNode?.getPositionToScreenWithTransform();
161. console.info(`${TEST_TAG}${JSON.stringify(positionToScreenWithTransform)}`);
162. }

164. getMeasuredSize() {
165. let measuredSize = this.frameNode?.getMeasuredSize();
166. console.info(`${TEST_TAG}${JSON.stringify(measuredSize)}`);
167. }

169. getLayoutPosition() {
170. let layoutPosition = this.frameNode?.getLayoutPosition();
171. console.info(`${TEST_TAG}${JSON.stringify(layoutPosition)}`);
172. }

174. getUserConfigBorderWidth() {
175. let userConfigBorderWidth = this.frameNode?.getUserConfigBorderWidth();
176. console.info(`${TEST_TAG}${JSON.stringify(userConfigBorderWidth)}`);
177. }

179. getUserConfigPadding() {
180. let userConfigPadding = this.frameNode?.getUserConfigPadding();
181. console.info(`${TEST_TAG}${JSON.stringify(userConfigPadding)}`);
182. }

184. getUserConfigMargin() {
185. let userConfigMargin = this.frameNode?.getUserConfigMargin();
186. console.info(`${TEST_TAG}${JSON.stringify(userConfigMargin)}`);
187. }

189. getUserConfigSize() {
190. let userConfigSize = this.frameNode?.getUserConfigSize();
191. console.info(`${TEST_TAG}${JSON.stringify(userConfigSize)}`);
192. }

194. getId() {
195. let id = this.frameNode?.getId();
196. console.info(`${TEST_TAG}${id}`);
197. }

199. getUniqueId() {
200. let uniqueId = this.frameNode?.getUniqueId();
201. console.info(`${TEST_TAG}${uniqueId}`);
202. }

204. getNodeType() {
205. let nodeType = this.frameNode?.getNodeType();
206. console.info(`${TEST_TAG}${nodeType}`);
207. }

209. getOpacity() {
210. let opacity = this.frameNode?.getOpacity();
211. console.info(`${TEST_TAG}${JSON.stringify(opacity)}`);
212. }

214. isVisible() {
215. let visible = this.frameNode?.isVisible();
216. console.info(`${TEST_TAG}${JSON.stringify(visible)}`);
217. }

219. isClipToFrame() {
220. let clipToFrame = this.frameNode?.isClipToFrame();
221. console.info(`${TEST_TAG}${JSON.stringify(clipToFrame)}`);
222. }

224. isAttached() {
225. let attached = this.frameNode?.isAttached();
226. console.info(`${TEST_TAG}${JSON.stringify(attached)}`);
227. }

229. isOnMainTree() {
230. let attached = this.frameNode?.isOnMainTree();
231. console.info(`${TEST_TAG}${JSON.stringify(attached)}`);
232. }

234. getInspectorInfo() {
235. let inspectorInfo = this.frameNode?.getInspectorInfo();
236. console.info(`${TEST_TAG}${JSON.stringify(inspectorInfo)}`);
237. }

239. setCrossLanguageOptions() {
240. console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions())}`);
241. try {
242. this.frameNode?.setCrossLanguageOptions({
243. attributeSetting: true
244. });
245. console.info(`${TEST_TAG} setCrossLanguageOptions success.`);
246. } catch (err) {
247. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
248. console.error(`${TEST_TAG} setCrossLanguageOptions fail.`);
249. }
250. console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions())}`);
251. }

253. getInteractionEventBindingInfo() {
254. let bindingInfo = this.frameNode?.getInteractionEventBindingInfo(EventQueryType.ON_CLICK);
255. console.info(`${TEST_TAG}${bindingInfo?.baseEventRegistered}`);
256. console.info(`${TEST_TAG}${bindingInfo?.nodeEventRegistered}`);
257. console.info(`${TEST_TAG}${bindingInfo?.nativeEventRegistered}`);
258. console.info(`${TEST_TAG}${bindingInfo?.builtInEventRegistered}`);
259. console.info(`${TEST_TAG}${JSON.stringify(bindingInfo)}`);
260. }

262. throwError() {
263. try {
264. this.rootNode!.getParent()!.clearChildren();
265. } catch (err) {
266. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
267. }
268. try {
269. this.rootNode!.getParent()!.appendChild(new FrameNode(this.uiContext));
270. } catch (err) {
271. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
272. }
273. try {
274. this.rootNode!.getParent()!.removeChild(this.rootNode!.getParent()!.getChild(0));
275. } catch (err) {
276. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
277. }
278. }
279. }

281. @Entry
282. @Component
283. struct Index {
284. private myNodeController: MyNodeController = new MyNodeController();
285. private scroller: Scroller = new Scroller();
286. @State index: number = 0;

288. build() {
289. Scroll(this.scroller) {
290. Column({ space: 8 }) {
291. Column() {
292. Row() {
293. Button('ADD')
294. .onClick(() => {
295. this.index++;
296. })
297. Button('DEC')
298. .onClick(() => {
299. this.index--;
300. })
301. }

303. Text('Current index is ' + this.index)
304. .textAlign(TextAlign.Center)
305. .borderRadius(10)
306. .backgroundColor(0xFFFFFF)
307. .width('100%')
308. .fontSize(16)
309. }

311. Column() {
312. Text('This is a NodeContainer.')
313. .textAlign(TextAlign.Center)
314. .borderRadius(10)
315. .backgroundColor(0xFFFFFF)
316. .width('100%')
317. .fontSize(16)
318. NodeContainer(this.myNodeController)
319. .borderWidth(1)
320. .width(300)
321. .height(100)
322. }

324. Button('appendChild')
325. .width(300)
326. .onClick(() => {
327. this.myNodeController.appendChild();
328. })
329. Button('insertChildAfter')
330. .width(300)
331. .onClick(() => {
332. this.myNodeController.insertChildAfter(this.index);
333. })
334. Button('removeChild')
335. .width(300)
336. .onClick(() => {
337. this.myNodeController.removeChild(this.index);
338. })
339. Button('clearChildren')
340. .width(300)
341. .onClick(() => {
342. this.myNodeController.clearChildren();
343. })
344. Button('getChildNumber')
345. .width(300)
346. .onClick(() => {
347. this.myNodeController.getChildNumber();
348. })
349. Button('searchFrameNode')
350. .width(300)
351. .onClick(() => {
352. this.myNodeController.searchFrameNode();
353. })
354. Button('moveFrameNode')
355. .width(300)
356. .onClick(() => {
357. this.myNodeController.moveFrameNode();
358. })
359. Button('getPositionToWindow')
360. .width(300)
361. .onClick(() => {
362. this.myNodeController.getPositionToWindow();
363. })
364. Button('getPositionToParent')
365. .width(300)
366. .onClick(() => {
367. this.myNodeController.getPositionToParent();
368. })
369. Button('getPositionToScreen')
370. .width(300)
371. .onClick(() => {
372. this.myNodeController.getPositionToScreen();
373. })
374. Button('getGlobalPositionOnDisplay')
375. .width(300)
376. .onClick(() => {
377. this.myNodeController.getGlobalPositionOnDisplay();
378. })
379. Button('getPositionToParentWithTransform')
380. .width(300)
381. .onClick(() => {
382. this.myNodeController.getPositionToParentWithTransform();
383. })
384. Button('getPositionToWindowWithTransform')
385. .width(300)
386. .onClick(() => {
387. this.myNodeController.getPositionToWindowWithTransform();
388. })
389. Button('getPositionToScreenWithTransform')
390. .width(300)
391. .onClick(() => {
392. this.myNodeController.getPositionToScreenWithTransform();
393. })
394. Button('getMeasuredSize')
395. .width(300)
396. .onClick(() => {
397. this.myNodeController.getMeasuredSize();
398. })
399. Button('getLayoutPosition')
400. .width(300)
401. .onClick(() => {
402. this.myNodeController.getLayoutPosition();
403. })
404. Button('getUserConfigBorderWidth')
405. .width(300)
406. .onClick(() => {
407. this.myNodeController.getUserConfigBorderWidth();
408. })
409. Button('getUserConfigPadding')
410. .width(300)
411. .onClick(() => {
412. this.myNodeController.getUserConfigPadding();
413. })
414. Button('getUserConfigMargin')
415. .width(300)
416. .onClick(() => {
417. this.myNodeController.getUserConfigMargin();
418. })
419. Button('getUserConfigSize')
420. .width(300)
421. .onClick(() => {
422. this.myNodeController.getUserConfigSize();
423. })
424. Button('getId')
425. .width(300)
426. .onClick(() => {
427. this.myNodeController.getId();
428. })
429. Button('getUniqueId')
430. .width(300)
431. .onClick(() => {
432. this.myNodeController.getUniqueId();
433. })
434. Button('getNodeType')
435. .width(300)
436. .onClick(() => {
437. this.myNodeController.getNodeType();
438. })
439. Button('getOpacity')
440. .width(300)
441. .onClick(() => {
442. this.myNodeController.getOpacity();
443. })
444. Button('isVisible')
445. .width(300)
446. .onClick(() => {
447. this.myNodeController.isVisible();
448. })
449. Button('isClipToFrame')
450. .width(300)
451. .onClick(() => {
452. this.myNodeController.isClipToFrame();
453. })
454. Button('isAttached')
455. .width(300)
456. .onClick(() => {
457. this.myNodeController.isAttached();
458. })
459. Button('isOnMainTree')
460. .width(300)
461. .onClick(() => {
462. this.myNodeController.isOnMainTree();
463. })
464. Button('getInspectorInfo')
465. .width(300)
466. .onClick(() => {
467. this.myNodeController.getInspectorInfo();
468. })
469. Button('getCustomProperty')
470. .width(300)
471. .onClick(() => {
472. const uiContext: UIContext = this.getUIContext();
473. if (uiContext) {
474. const node: FrameNode | null = uiContext.getFrameNodeById('Test_Button') || null;
475. if (node) {
476. for (let i = 1; i < 4; i++) {
477. const key = 'customProperty' + i;
478. const property = node.getCustomProperty(key);
479. console.info(`${TEST_TAG}${key}`, JSON.stringify(property));
480. }
481. }
482. }
483. })
484. .id('Test_Button')
485. .customProperty('customProperty1', {
486. 'number': 10,
487. 'string': 'this is a string',
488. 'bool': true,
489. 'object': {
490. 'name': 'name',
491. 'value': 100
492. }
493. })
494. .customProperty('customProperty2', {})
495. .customProperty('customProperty2', undefined)
496. Button('setCrossLanguageOptions')
497. .width(300)
498. .onClick(() => {
499. this.myNodeController.setCrossLanguageOptions();
500. })
501. Button('getInteractionEventBindingInfo')
502. .width(300)
503. .onClick(() => {
504. this.myNodeController.getInteractionEventBindingInfo();
505. })
506. Button('throwError')
507. .width(300)
508. .onClick(() => {
509. this.myNodeController.throwError();
510. })
511. }
512. .width('100%')
513. }
514. .scrollable(ScrollDirection.Vertical) // 滚动方向为纵向
515. }
516. }
```

### convertPositionToWindow23+

PhonePC/2in1TabletTVWearable

convertPositionToWindow(positionByLocal: Position): Position

将点的坐标从当前节点的坐标系转换为当前节点所在窗口的坐标系。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionByLocal | [Position](js-apis-arkui-graphics.md#position) | 是 | 当前节点坐标系中的相对坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 当前节点所在窗口的坐标系中的转换坐标。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100026 | The current FrameNode has been disposed. |
| 100028 | The current FrameNode is not on the main tree. |

**示例：**

请参考[局部与窗口坐标转化示例](js-apis-arkui-framenode.md#局部与窗口坐标转化示例)。

### convertPositionFromWindow23+

PhonePC/2in1TabletTVWearable

convertPositionFromWindow(positionByWindow: Position): Position

将点的坐标从当前节点所在窗口的坐标系转换为当前节点的坐标系。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionByWindow | [Position](js-apis-arkui-graphics.md#position) | 是 | 当前节点所在窗口的坐标系中的相对坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 当前节点坐标系中的转换坐标。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100026 | The current FrameNode has been disposed. |
| 100028 | The current FrameNode is not on the main tree. |

**示例：**

请参考[局部与窗口坐标转化示例](js-apis-arkui-framenode.md#局部与窗口坐标转化示例)。

## TypedFrameNode12+

PhonePC/2in1TabletTVWearable

TypedFrameNode继承自[FrameNode](js-apis-arkui-framenode.md#framenode-1)，用于声明具体类型的FrameNode。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialize | C | 否 | 否 | 该接口用于创建对应组件的构造参数，用于设置/更新组件的初始值。 |
| attribute | T | 是 | 否 | 该接口用于获取对应组件的属性设置对象，用于设置/更新组件的通用、私有属性。 |

说明

[commonAttribute](js-apis-arkui-framenode.md#commonattribute12)仅在CustomFrameNode上生效，TypedFrameNode上commonAttribute行为未定义。建议使用[attribute](js-apis-arkui-framenode.md#属性)接口而非[commonAttribute](js-apis-arkui-framenode.md#commonattribute12)接口进行通用属性设置，如node.attribute.backgroundColor(Color.Pink)。

## typeNode12+

PhonePC/2in1TabletTVWearable

typeNode提供创建具体类型的FrameNode能力，可通过FrameNode的基础接口进行自定义的挂载，使用占位容器进行显示。

使用typeNode创建[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)、[Select](ts-basic-components-select.md)、[Toggle](ts-basic-components-toggle.md)节点时，当传入的[UIContext](arkts-apis-uicontext-uicontext.md)对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**示例：**

请参考[自定义具体类型节点示例](js-apis-arkui-framenode.md#自定义具体类型节点示例)。

### Text12+

PhonePC/2in1TabletTVWearable

type Text = TypedFrameNode<TextInterface, TextAttribute>

Text类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[TextInterface](ts-basic-components-text.md#接口), [TextAttribute](ts-basic-components-text.md#属性)> | 提供Text类型FrameNode节点。  TextInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Text组件的构造函数类型。  TextAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Text组件的属性设置对象。 |

### createNode('Text')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Text'): Text

创建Text类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Text' | 是 | 创建Text类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Text](js-apis-arkui-framenode.md#text12) | Text类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建Text
12. let text = typeNode.createNode(uiContext, 'Text');
13. text.initialize("Hello").fontColor(Color.Blue).fontSize(14);
14. typeNode.getAttribute(text, 'Text')?.fontWeight(FontWeight.Bold);
15. col.appendChild(text);
16. return node;
17. }
18. }

20. @Entry
21. @Component
22. struct FrameNodeTypeTest {
23. private myNodeController: MyNodeController = new MyNodeController();

25. build() {
26. Column({ space: 5 }) {
27. Text('Text sample');
28. NodeContainer(this.myNodeController);
29. }
30. }
31. }
```

### getAttribute('Text')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Text'): TextAttribute | undefined

获取Text节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Text' | 是 | 获取Text节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TextAttribute | undefined | Text节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建Text
12. let text = typeNode.createNode(uiContext, 'Text');
13. text.initialize("Hello");
14. // 获取Text的属性
15. typeNode.getAttribute(text, 'Text')?.fontColor(Color.Red)
16. col.appendChild(text);
17. // 创建另一个Text用于对比
18. let text2 = typeNode.createNode(uiContext, 'Text');
19. text2.initialize("world");
20. col.appendChild(text2);
21. return node;
22. }
23. }

25. @Entry
26. @Component
27. struct FrameNodeTypeTest {
28. private myNodeController: MyNodeController = new MyNodeController();

30. build() {
31. Column({ space: 5 }) {
32. Text('Text sample');
33. NodeContainer(this.myNodeController);
34. }
35. }
36. }
```

### bindController('Text')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void

将文本控制器[TextController](ts-basic-components-text.md#textcontroller11)绑定到[Text](js-apis-arkui-framenode.md#text12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定文本控制器的目标节点。 |
| controller | [TextController](ts-basic-components-text.md#textcontroller11) | 是 | 文本控制器。 |
| nodeType | 'Text' | 是 | 绑定输入框控制器的目标节点的节点类型为Text。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. // 设置TextController，可以在外部获取
6. controller: TextController = new TextController()

8. makeNode(uiContext: UIContext): FrameNode | null {
9. let node = new FrameNode(uiContext);
10. node.commonAttribute;
11. let col = typeNode.createNode(uiContext, 'Column');
12. col.initialize({ space: 5 });
13. node.appendChild(col);
14. // 创建Text
15. let text = typeNode.createNode(uiContext, 'Text');
16. text.initialize("Hello").fontColor(Color.Blue).fontSize(14);
17. typeNode.getAttribute(text, 'Text')?.fontWeight(FontWeight.Bold)
18. // 绑定TextController
19. typeNode.bindController(text, this.controller, 'Text');
20. col.appendChild(text);
21. return node;
22. }
23. }

25. @Entry
26. @Component
27. struct FrameNodeTypeTest {
28. @State line: number = 0
29. private myNodeController: MyNodeController = new MyNodeController();

31. build() {
32. Column({ space: 5 }) {
33. Text('Text bindController Sample')
34. NodeContainer(this.myNodeController)
35. Text(`Text的行数, ${this.line}`)
36. Button(`点击获取行数`)
37. .onClick(() => {
38. this.line = this.myNodeController.controller.getLayoutManager().getLineCount()
39. })
40. }
41. }
42. }
```

### Column12+

PhonePC/2in1TabletTVWearable

type Column = TypedFrameNode<ColumnInterface, ColumnAttribute>

Column类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ColumnInterface](ts-container-column.md#接口), [ColumnAttribute](ts-container-column.md#属性)> | 提供Column类型FrameNode节点。  ColumnInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Column组件的构造函数类型。  ColumnAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Column组件的属性设置对象。 |

### createNode('Column')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Column'): Column

创建Column类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Column' | 是 | 创建Column类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Column](js-apis-arkui-framenode.md#column12) | Column类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Column控制器
4. class MyColumnController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建Column
9. let col = typeNode.createNode(uiContext, 'Column')
10. col.initialize({ space: 5 })
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(col)
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myColumnController: MyColumnController = new MyColumnController();

24. build() {
25. Column({ space: 5 }) {
26. Text('ColumnSample')
27. NodeContainer(this.myColumnController);
28. }.width('100%')
29. }
30. }
```

### getAttribute('Column')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Column'): ColumnAttribute | undefined

获取Column节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Column' | 是 | 获取Column节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ColumnAttribute | undefined | Column节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. makeNode(uiContext: UIContext): FrameNode | null {
5. let node = new FrameNode(uiContext);
6. node.commonAttribute;
7. let col = typeNode.createNode(uiContext, 'Column');
8. col.initialize({ space: 5 });
9. node.appendChild(col);
10. // 创建Column
11. let col1 = typeNode.createNode(uiContext, 'Column');
12. col1.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
13. // 获取Column的属性
14. typeNode.getAttribute(col1, 'Column')?.backgroundColor(Color.Blue).width("100%")
15. col.appendChild(col1);
16. // 创建另一个Column用于对比
17. let col2 = typeNode.createNode(uiContext, 'Column');
18. col2.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
19. col.appendChild(col2);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('Column sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### Row12+

PhonePC/2in1TabletTVWearable

type Row = TypedFrameNode<RowInterface, RowAttribute>

Row类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[RowInterface](ts-container-row.md#接口), [RowAttribute](ts-container-row.md#属性)> | 提供Row类型FrameNode节点。  RowInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Row组件的构造函数类型。  RowAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Row组件的属性设置对象。 |

### createNode('Row')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Row'): Row

创建Row类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Row' | 是 | 创建Row类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Row](js-apis-arkui-framenode.md#row12) | Row类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Row控制器
4. class MyRowController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建row
9. let row = typeNode.createNode(uiContext, 'Row')
10. row.initialize({ space: 5 })
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(row)
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myRowController: MyRowController = new MyRowController();

24. build() {
25. Column({ space: 5 }) {
26. Text('RowSample')
27. NodeContainer(this.myRowController);
28. }.width('100%')
29. }
30. }
```

### getAttribute('Row')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Row'): RowAttribute | undefined

获取Row节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Row' | 是 | 获取Row节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RowAttribute | undefined | Row节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. makeNode(uiContext: UIContext): FrameNode | null {
5. let node = new FrameNode(uiContext);
6. node.commonAttribute;
7. let col = typeNode.createNode(uiContext, 'Column');
8. col.initialize({ space: 5 });
9. node.appendChild(col);
10. // 创建Row
11. let row1 = typeNode.createNode(uiContext, 'Row');
12. row1.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
13. // 获取Row的属性
14. typeNode.getAttribute(row1, 'Row')?.backgroundColor(Color.Blue).width("100%")
15. col.appendChild(row1);
16. // 创建另一个Row用于对比
17. let row2 = typeNode.createNode(uiContext, 'Row');
18. row2.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
19. col.appendChild(row2);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('Row sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### Stack12+

PhonePC/2in1TabletTVWearable

type Stack = TypedFrameNode<StackInterface, StackAttribute>

Stack类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[StackInterface](ts-container-stack.md#接口), [StackAttribute](ts-container-stack.md#属性)> | 提供Stack类型FrameNode节点。  StackInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Stack组件的构造函数类型。  StackAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Stack组件的属性设置对象。 |

### createNode('Stack')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Stack'): Stack

创建Stack类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Stack' | 是 | 创建Stack类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stack](js-apis-arkui-framenode.md#stack12) | Stack类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Stack控制器
4. class MyStackController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建Stack
9. let stack = typeNode.createNode(uiContext, 'Stack')
10. stack.initialize({ alignContent: Alignment.Top })
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(stack)
15. let text = typeNode.createNode(uiContext, 'Text')
16. text.initialize("This is Text")
17. // 向stack添加text
18. stack.appendChild(text)
19. return node;
20. }
21. }

23. @Entry
24. @Component
25. struct FrameNodeTypeTest {
26. private myStackController: MyStackController = new MyStackController();

28. build() {
29. Column({ space: 5 }) {
30. Text('StackSample')
31. NodeContainer(this.myStackController);
32. }.width('100%')
33. }
34. }
```

### getAttribute('Stack')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Stack'): StackAttribute | undefined

获取Stack节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Stack' | 是 | 获取Stack节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| StackAttribute | undefined | Stack节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. makeNode(uiContext: UIContext): FrameNode | null {
5. let node = new FrameNode(uiContext);
6. node.commonAttribute;
7. let col = typeNode.createNode(uiContext, 'Column');
8. col.initialize({ space: 5 });
9. node.appendChild(col);
10. // 创建Stack
11. let stack1 = typeNode.createNode(uiContext, 'Stack');
12. stack1.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
13. // 获取Stack的属性
14. typeNode.getAttribute(stack1, 'Stack')?.backgroundColor(Color.Blue).width("100%")
15. col.appendChild(stack1);
16. // 创建另一个Stack用于对比
17. let stack2 = typeNode.createNode(uiContext, 'Stack');
18. stack2.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
19. col.appendChild(stack2);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('Row sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### GridRow12+

PhonePC/2in1TabletTVWearable

type GridRow = TypedFrameNode<GridRowInterface, GridRowAttribute>

GridRow类型的FrameNode节点类型。只允许添加GridCol类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[GridRowInterface](ts-container-gridrow.md#接口), [GridRowAttribute](ts-container-gridrow.md#属性)> | 提供GridRow类型FrameNode节点。  GridRowInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为GridRow组件的构造函数类型。  GridRowAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回GridRow组件的属性设置对象。 |

### createNode('GridRow')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'GridRow'): GridRow

创建GridRow类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'GridRow' | 是 | 创建GridRow类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridRow](js-apis-arkui-framenode.md#gridrow12) | GridRow类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义GridRow控制器
4. class MyGridRowController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建GridRow
9. let gridRow = typeNode.createNode(uiContext, 'GridRow')
10. gridRow.initialize({ columns: 12 })
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(gridRow)
15. // 创建GridCol
16. let gridCol = typeNode.createNode(uiContext, 'GridCol')
17. gridCol.initialize({ span: 2, offset: 4 })
18. .height("100%")
19. .backgroundColor(Color.Red)
20. // 向gridRow添加gridCol
21. gridRow.appendChild(gridCol)
22. return node;
23. }
24. }

26. @Entry
27. @Component
28. struct FrameNodeTypeTest {
29. private myGridRowController: MyGridRowController = new MyGridRowController();

31. build() {
32. Column({ space: 5 }) {
33. Text('GridRowSample')
34. NodeContainer(this.myGridRowController);
35. }.width('100%')
36. }
37. }
```

### GridCol12+

PhonePC/2in1TabletTVWearable

type GridCol = TypedFrameNode<GridColInterface, GridColAttribute>

GridCol类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[GridColInterface](ts-container-gridcol.md#接口), [GridColAttribute](ts-container-gridcol.md#属性)> | 提供GridCol类型FrameNode节点。  GridColInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为GridCol组件的构造函数类型。  GridColAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回GridCol组件的属性设置对象。 |

### createNode('GridCol')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'GridCol'): GridCol

创建GridCol类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'GridCol' | 是 | 创建GridCol类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridCol](js-apis-arkui-framenode.md#gridcol12) | GridCol类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义GridRow控制器
4. class MyGridRowController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建GridRow
9. let gridRow = typeNode.createNode(uiContext, 'GridRow')
10. gridRow.initialize({ columns: 12 })
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(gridRow)
15. // 创建GridCol
16. let gridCol = typeNode.createNode(uiContext, 'GridCol')
17. gridCol.initialize({ span: 2, offset: 4 })
18. .height("100%")
19. .backgroundColor(Color.Red)
20. // 向gridRow添加gridCol
21. gridRow.appendChild(gridCol)
22. return node;
23. }
24. }

26. @Entry
27. @Component
28. struct FrameNodeTypeTest {
29. private myGridRowController: MyGridRowController = new MyGridRowController();

31. build() {
32. Column({ space: 5 }) {
33. Text('GridColSample')
34. NodeContainer(this.myGridRowController);
35. }.width('100%')
36. }
37. }
```

### Flex12+

PhonePC/2in1TabletTVWearable

type Flex = TypedFrameNode<FlexInterface, FlexAttribute>

Flex类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[FlexInterface](ts-container-flex.md#接口), [FlexAttribute](ts-container-flex.md#属性)> | 提供Flex类型FrameNode节点。  FlexInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Flex组件的构造函数类型。  FlexAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Flex组件的属性设置对象。 |

### createNode('Flex')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Flex'): Flex

创建Flex类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Flex' | 是 | 创建Flex类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Flex](js-apis-arkui-framenode.md#flex12) | Flex类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Flex控制器
4. class MyFlexController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建Flex
9. let flex = typeNode.createNode(uiContext, 'Flex')
10. flex.initialize()
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(flex)
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myFlexController: MyFlexController = new MyFlexController();

24. build() {
25. Column({ space: 5 }) {
26. Text('FlexSample')
27. NodeContainer(this.myFlexController);
28. }.width('100%')
29. }
30. }
```

### getAttribute('Flex')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Flex'): FlexAttribute | undefined

获取Flex节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Flex' | 是 | 获取Flex节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FlexAttribute | undefined | Flex节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. makeNode(uiContext: UIContext): FrameNode | null {
5. let node = new FrameNode(uiContext);
6. node.commonAttribute;
7. let col = typeNode.createNode(uiContext, 'Column');
8. col.initialize({ space: 5 });
9. node.appendChild(col);
10. // 创建Flex
11. let flex1 = typeNode.createNode(uiContext, 'Flex');
12. flex1.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
13. // 获取Flex的属性
14. typeNode.getAttribute(flex1, 'Flex')?.backgroundColor(Color.Blue).width("100%")
15. col.appendChild(flex1);
16. // 创建另一个Flex用于对比
17. let flex2 = typeNode.createNode(uiContext, 'Flex');
18. flex2.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
19. col.appendChild(flex2);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('Flex sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### Swiper12+

PhonePC/2in1TabletTVWearable

type Swiper = TypedFrameNode<SwiperInterface, SwiperAttribute>

Swiper类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[SwiperInterface](ts-container-swiper.md#接口), [SwiperAttribute](ts-container-swiper.md#属性)> | 提供Swiper类型FrameNode节点。  SwiperInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Swiper组件的构造函数类型。  SwiperAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Swiper组件的属性设置对象。 |

### createNode('Swiper')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Swiper'): Swiper

创建Swiper类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Swiper' | 是 | 创建Swiper类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Swiper](js-apis-arkui-framenode.md#swiper12) | Swiper类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Swiper控制器
4. class MySwiperController extends NodeController {
5. swiperController: SwiperController = new SwiperController()

7. makeNode(uiContext: UIContext): FrameNode | null {
8. // 创建Swiper
9. let swiperNode = typeNode.createNode(uiContext, 'Swiper')

11. // 创建Text
12. let text0 = typeNode.createNode(uiContext, 'Text')
13. text0.initialize("0")
14. .width('100%')
15. .height('100%')
16. .textAlign(TextAlign.Center)
17. // 向swiper添加text0
18. swiperNode.appendChild(text0)
19. // 创建另一个Text用于切换
20. let text1 = typeNode.createNode(uiContext, 'Text')
21. text1.initialize("1")
22. .width('100%')
23. .height('100%')
24. .textAlign(TextAlign.Center)
25. // 向swiper添加text1
26. swiperNode.appendChild(text1)
27. swiperNode.commonAttribute.width('100%')
28. .height('20%')
29. .backgroundColor(0xAFEEEE)
30. // 向swiper绑定控制器
31. typeNode.bindController(swiperNode, this.swiperController, 'Swiper')
32. typeNode.getAttribute(swiperNode, 'Swiper')?.loop(false)
33. return swiperNode;

35. }
36. }

38. @Entry
39. @Component
40. struct FrameNodeTypeTest {
41. private mySwiperController: MySwiperController = new MySwiperController();

43. build() {
44. Column({ space: 5 }) {
45. Text('SwiperSample')
46. NodeContainer(this.mySwiperController);
47. }.width('100%')
48. }
49. }
```

### getAttribute('Swiper')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Swiper'): SwiperAttribute | undefined

获取Swiper节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Swiper' | 是 | 获取Swiper节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SwiperAttribute | undefined | Swiper节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

请参考[createNode('Swiper')12+示例](js-apis-arkui-framenode.md#createnodeswiper12)。

### bindController('Swiper')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void

将控制器[SwiperController](ts-container-swiper.md#swipercontroller)绑定到[Swiper](js-apis-arkui-framenode.md#swiper12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定控制器的目标节点。 |
| controller | [SwiperController](ts-container-swiper.md#swipercontroller) | 是 | Swiper容器组件的控制器。 |
| nodeType | 'Swiper' | 是 | 绑定控制器的目标节点的节点类型为Swiper。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

请参考[createNode('Swiper')12+示例](js-apis-arkui-framenode.md#createnodeswiper12)。

### Progress12+

PhonePC/2in1TabletTVWearable

type Progress = TypedFrameNode<ProgressInterface, ProgressAttribute>

Progress类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ProgressInterface](ts-basic-components-progress.md#接口), [ProgressAttribute](ts-basic-components-progress.md#属性)> | 提供Progress类型FrameNode节点。  ProgressInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Progress组件的构造函数类型。  ProgressAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Progress组件的属性设置对象。 |

### createNode('Progress')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Progress'): Progress

创建Progress类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Progress' | 是 | 创建Progress类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Progress](js-apis-arkui-framenode.md#progress12) | Progress类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Progress控制器
4. class MyProgressNodeController extends NodeController {
5. public uiContext: UIContext | null = null;
6. public rootNode: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.uiContext = uiContext;
10. this.rootNode = new FrameNode(uiContext);
11. // 创建Progress
12. let node = typeNode.createNode(uiContext, 'Progress');
13. node.initialize({
14. value: 15,
15. total: 200,
16. type: ProgressType.ScaleRing
17. }).width(100)
18. .height(100)
19. this!.rootNode!.appendChild(node);
20. return this.rootNode;
21. }
22. }

24. @Entry
25. @Component
26. struct Sample {
27. build() {
28. Column({ space: 10 }) {
29. NodeContainer(new MyProgressNodeController()).margin(5)
30. }.width('100%').height('100%')

32. }
33. }
```

### getAttribute('Progress')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Progress'): ProgressAttribute | undefined

获取Progress节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Progress' | 是 | 获取Progress节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ProgressAttribute | undefined | Progress节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Progress控制器
4. class MyProgressNodeController extends NodeController {
5. public uiContext: UIContext | null = null;
6. public rootNode: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.uiContext = uiContext;
10. this.rootNode = new FrameNode(uiContext);
11. let node = typeNode.createNode(uiContext, 'Progress');
12. node.initialize({
13. value: 15,
14. total: 200,
15. type: ProgressType.ScaleRing
16. }).width(100)
17. .height(100)
18. // 获取Progress的属性
19. typeNode.getAttribute(node, 'Progress');
20. this!.rootNode!.appendChild(node);
21. return this.rootNode;
22. }
23. }

25. @Entry
26. @Component
27. struct Sample {
28. build() {
29. Column({ space: 10 }) {
30. NodeContainer(new MyProgressNodeController()).margin(5)
31. }.width('100%').height('100%')

33. }
34. }
```

### Scroll12+

PhonePC/2in1TabletTVWearable

type Scroll = TypedFrameNode<ScrollInterface, ScrollAttribute>

Scroll类型的FrameNode节点类型。允许添加一个子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ScrollInterface](ts-container-scroll.md#接口), [ScrollAttribute](ts-container-scroll.md#属性)> | 提供Scroll类型FrameNode节点。  ScrollInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Scroll组件的构造函数类型。  ScrollAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Scroll组件的属性设置对象。 |

### createNode('Scroll')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Scroll'): Scroll

创建Scroll类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Scroll' | 是 | 创建Scroll类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scroll](js-apis-arkui-framenode.md#scroll12) | Scroll类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Scroll控制器
4. class MyScrollController extends NodeController {
5. public rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);

10. // 创建Scroll
11. let scroller: Scroller = new Scroller();
12. // 创建Scroll并设置属性
13. let scrollNode = typeNode.createNode(uiContext, 'Scroll');
14. scrollNode.initialize(scroller).size({ width: '100%', height: 500 });
15. typeNode.getAttribute(scrollNode, "Scroll")?.friction(0.6);

17. let colNode = typeNode.createNode(uiContext, 'Column');
18. // 向scroll添加column
19. scrollNode.appendChild(colNode);

21. for (let i = 0; i < 10; i++) {
22. let text = typeNode.createNode(uiContext, 'Text');
23. text.initialize('item' + i)
24. .size({ width: '90%', height: 100 })
25. .textAlign(TextAlign.Center)
26. .backgroundColor(0xF9CF93);
27. colNode.appendChild(text);
28. }

30. this!.rootNode!.appendChild(scrollNode);
31. return this.rootNode;
32. }
33. }

35. @Entry
36. @Component
37. struct FrameNodeTypeTest {
38. private myScrollController: MyScrollController = new MyScrollController();

40. build() {
41. Column({ space: 5 }) {
42. Text('ScrollSample')
43. NodeContainer(this.myScrollController)

45. }.width('100%')
46. }
47. }
```

### getAttribute('Scroll')15+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined

获取Scroll节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Scroll' | 是 | 获取Scroll节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ScrollAttribute | undefined | Scroll节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('Scroll')](js-apis-arkui-framenode.md#createnodescroll12)的示例。

### getEvent('Scroll')19+

PhonePC/2in1TabletTVWearable

getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined

获取Scroll节点中持有的UIScrollEvent对象，用于设置滚动事件。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取事件时所需的目标节点。 |
| nodeType | 'Scroll' | 是 | 获取Scroll节点类型的滚动事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIScrollEvent](ts-container-scroll.md#uiscrollevent19) | undefined | Scroll节点类型的滚动事件，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[滚动事件示例](js-apis-arkui-framenode.md#滚动事件示例)。

### bindController('Scroll')15+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[Scroll](js-apis-arkui-framenode.md#scroll12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定滚动控制器的目标节点。 |
| controller | [Scroller](ts-container-scroll.md#scroller) | 是 | 滚动控制器。 |
| nodeType | 'Scroll' | 是 | 绑定滚动控制器的目标节点的节点类型为Scroll。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. the type of the node is error. 2. the node is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. typeNode.bindController(node, scroller, 'Scroll');
```

### RelativeContainer12+

PhonePC/2in1TabletTVWearable

type RelativeContainer = TypedFrameNode<RelativeContainerInterface, RelativeContainerAttribute>

RelativeContainer类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[RelativeContainerInterface](ts-container-relativecontainer.md#接口), [RelativeContainerAttribute](ts-container-relativecontainer.md#属性)> | 提供RelativeContainer类型FrameNode节点。  RelativeContainerInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为RelativeContainer组件的构造函数类型。  RelativeContainerAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回RelativeContainer组件的属性设置对象。 |

### createNode('RelativeContainer')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer

创建RelativeContainer类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'RelativeContainer' | 是 | 创建RelativeContainer类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RelativeContainer](js-apis-arkui-framenode.md#relativecontainer12) | RelativeContainer类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Relative控制器
4. class MyRelativeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. // 创建RelativeContainer
9. let relative = typeNode.createNode(uiContext, 'RelativeContainer')
10. relative.initialize()
11. .width('50%')
12. .height('50%')
13. .backgroundColor(Color.Gray)
14. node.appendChild(relative)
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myRelativeController: MyRelativeController = new MyRelativeController();

24. build() {
25. Column({ space: 5 }) {
26. Text('RelativeContainerSample')
27. NodeContainer(this.myRelativeController);
28. }.width('100%')
29. }
30. }
```

### getAttribute('RelativeContainer')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'RelativeContainer'): RelativeContainerAttribute | undefined

获取RelativeContainer节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'RelativeContainer' | 是 | 获取RelativeContainer节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RelativeContainerAttribute | undefined | RelativeContainer节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. makeNode(uiContext: UIContext): FrameNode | null {
5. let node = new FrameNode(uiContext);
6. node.commonAttribute;
7. let col = typeNode.createNode(uiContext, 'Column');
8. col.initialize({ space: 5 });
9. node.appendChild(col);
10. // 创建RelativeContainer
11. let relative1 = typeNode.createNode(uiContext, 'RelativeContainer');
12. relative1.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
13. // 获取RelativeContainer的属性
14. typeNode.getAttribute(relative1, 'RelativeContainer')?.backgroundColor(Color.Blue).width("100%")
15. col.appendChild(relative1);
16. // 创建另一个RelativeContainer用于对比
17. let relative2 = typeNode.createNode(uiContext, 'RelativeContainer');
18. relative2.initialize().width("50%").height("20%").backgroundColor(Color.Pink);
19. col.appendChild(relative2);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('RelativeContainer sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### Divider12+

PhonePC/2in1TabletTVWearable

type Divider = TypedFrameNode<DividerInterface, DividerAttribute>

Divider类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[DividerInterface](ts-basic-components-divider.md#接口), [DividerAttribute](ts-basic-components-divider.md#属性)> | 提供Divider类型FrameNode节点。  DividerInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为RelativeContainer组件的构造函数类型。  DividerAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Divider组件的属性设置对象。 |

### createNode('Divider')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Divider'): Divider

创建Divider类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Divider' | 是 | 创建Divider类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Divider](js-apis-arkui-framenode.md#divider12) | Divider类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Divider控制器
4. class MyDividerController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建divider
14. let divider = typeNode.createNode(uiContext, 'Divider')
15. divider.initialize()
16. .strokeWidth(1)
17. // 向col添加divider
18. col.appendChild(divider)

20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myDividerController: MyDividerController = new MyDividerController();

29. build() {
30. Column({ space: 5 }) {
31. Text('DividerSample')
32. NodeContainer(this.myDividerController);

34. }.width('100%')
35. }
36. }
```

### LoadingProgress12+

PhonePC/2in1TabletTVWearable

type LoadingProgress = TypedFrameNode<LoadingProgressInterface, LoadingProgressAttribute>

LoadingProgress类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[LoadingProgressInterface](ts-basic-components-loadingprogress.md#接口), [LoadingProgressAttribute](ts-basic-components-loadingprogress.md#属性)> | 提供LoadingProgress类型FrameNode节点。  LoadingProgressInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为LoadingProgress组件的构造函数类型。  LoadingProgressAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回LoadingProgress组件的属性设置对象。 |

### createNode('LoadingProgress')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress

创建LoadingProgress类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'LoadingProgress' | 是 | 创建LoadingProgress类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoadingProgress](js-apis-arkui-framenode.md#loadingprogress12) | LoadingProgress类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义LoadingProgress控制器
4. class MyLoadingProgressNodeController extends NodeController {
5. public uiContext: UIContext | null = null;
6. public rootNode: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.uiContext = uiContext;
10. this.rootNode = new FrameNode(uiContext);
11. // 创建LoadingProgress
12. let node = typeNode.createNode(uiContext, 'LoadingProgress');
13. node.initialize()
14. .width(100)
15. .height(100)
16. .color(Color.Red)
17. .enableLoading(true)
18. this!.rootNode!.appendChild(node);
19. return this.rootNode;
20. }
21. }

23. @Entry
24. @Component
25. struct Sample {
26. build() {
27. Column({ space: 10 }) {
28. NodeContainer(new MyLoadingProgressNodeController()).margin(5)
29. }.width('100%').height('100%')
30. }
31. }
```

### getAttribute('LoadingProgress')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'LoadingProgress'): LoadingProgressAttribute | undefined

获取[LoadingProgress](ts-basic-components-loadingprogress.md)节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'LoadingProgress' | 是 | 获取LoadingProgress节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| LoadingProgressAttribute | undefined | LoadingProgress节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义LoadingProgress控制器
4. class MyLoadingProgressNodeController extends NodeController {
5. public uiContext: UIContext | null = null;
6. public rootNode: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.uiContext = uiContext;
10. this.rootNode = new FrameNode(uiContext);
11. let node = typeNode.createNode(uiContext, 'LoadingProgress');
12. node.initialize()
13. .width(100)
14. .height(100)
15. .color(Color.Red)
16. .enableLoading(true)
17. // 获取LoadingProgress的属性
18. typeNode.getAttribute(node, 'LoadingProgress');
19. this!.rootNode!.appendChild(node);
20. return this.rootNode;
21. }
22. }

24. @Entry
25. @Component
26. struct Sample {
27. build() {
28. Column({ space: 10 }) {
29. NodeContainer(new MyLoadingProgressNodeController()).margin(5)
30. }.width('100%').height('100%')
31. }
32. }
```

### Search12+

PhonePC/2in1TabletTVWearable

type Search = TypedFrameNode<SearchInterface, SearchAttribute>

Search类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[SearchInterface](ts-basic-components-search.md#接口), [SearchAttribute](ts-basic-components-search.md#属性)> | 提供Search类型FrameNode节点。  SearchInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Search组件的构造函数类型。  SearchAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Search组件的属性设置对象。 |

### createNode('Search')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Search'): Search

创建Search类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Search' | 是 | 创建Search类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Search](js-apis-arkui-framenode.md#search12) | Search类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建Search
12. let search = typeNode.createNode(uiContext, 'Search');
13. search.initialize({ value: "Search" })
14. .searchButton('SEARCH')
15. .textFont({ size: 14, weight: 400 })
16. col.appendChild(search);
17. return node;
18. }
19. }

21. @Entry
22. @Component
23. struct FrameNodeTypeTest {
24. private myNodeController: MyNodeController = new MyNodeController();

26. build() {
27. Column({ space: 5 }) {
28. Text('Search sample');
29. NodeContainer(this.myNodeController);
30. }
31. }
32. }
```

### Blank12+

PhonePC/2in1TabletTVWearable

type Blank = TypedFrameNode<BlankInterface, BlankAttribute>

Blank类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[BlankInterface](ts-basic-components-blank.md#接口), [BlankAttribute](ts-basic-components-blank.md#属性)> | 提供Blank类型FrameNode节点。  BlankInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Blank组件的构造函数类型。  BlankAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Blank组件的属性设置对象。 |

### createNode('Blank')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Blank'): Blank

创建Blank类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Blank' | 是 | 创建Blank类型的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Blank](js-apis-arkui-framenode.md#blank12) | Blank类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Blank控制器
4. class MyBlankController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Blank
14. let blank = typeNode.createNode(uiContext, 'Blank')
15. blank.initialize()
16. .width('50%')
17. .height('50%')
18. .backgroundColor(Color.Blue)
19. col.appendChild(blank)

21. return node;
22. }
23. }

25. @Entry
26. @Component
27. struct FrameNodeTypeTest {
28. private myBlankController: MyBlankController = new MyBlankController();

30. build() {
31. Column({ space: 5 }) {
32. Text('BlankSample')
33. NodeContainer(this.myBlankController);

35. }.width('100%')
36. }
37. }
```

### Image12+

PhonePC/2in1TabletTVWearable

type Image = TypedFrameNode<ImageInterface, ImageAttribute>

Image类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ImageInterface](ts-basic-components-image.md#接口), [ImageAttribute](ts-basic-components-image.md#属性)> | 提供Image类型FrameNode节点。  ImageInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Image组件的构造函数类型。  ImageAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Image组件的属性设置对象。 |

### createNode('Image')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Image'): Image

创建Image类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Image' | 是 | 创建Image类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Image](js-apis-arkui-framenode.md#image12) | Image类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Image控制器
4. class MyImageController extends NodeController {
5. public uiContext: UIContext | null = null;
6. public rootNode: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.uiContext = uiContext;
10. this.rootNode = new FrameNode(uiContext);
11. // 创建Image
12. let imageNode = typeNode.createNode(uiContext, 'Image');
13. imageNode
14. // $r('app.media.img')需要替换为开发者所需的图像资源文件
15. .initialize($r('app.media.img'))
16. .width(100)
17. .height(100)
18. .fillColor(Color.Red)
19. .objectFit(ImageFit.Contain)
20. .renderMode(ImageRenderMode.Template)
21. .fitOriginalSize(true)
22. .matchTextDirection(true)
23. .objectRepeat(ImageRepeat.X)
24. .autoResize(true)

26. this!.rootNode!.appendChild(imageNode);
27. return this.rootNode;

29. }
30. }

32. @Entry
33. @Component
34. struct Sample {
35. build() {
36. Column({ space: 10 }) {
37. NodeContainer(new MyImageController()).margin(5)
38. }.width('100%').height('100%')

40. }
41. }
```

### getAttribute('Image')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Image'): ImageAttribute | undefined

获取Image节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Image' | 是 | 获取Image节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ImageAttribute | undefined | Image节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Image控制器
4. class MyImageController extends NodeController {
5. public uiContext: UIContext | null = null;
6. public rootNode: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.uiContext = uiContext;
10. this.rootNode = new FrameNode(uiContext);
11. let imageNode = typeNode.createNode(uiContext, 'Image');
12. imageNode
13. // $r('app.media.img')需要替换为开发者所需的图像资源文件
14. .initialize($r('app.media.img'))
15. .width(100)
16. .height(100)
17. .fillColor(Color.Red)
18. .objectFit(ImageFit.Contain)
19. .renderMode(ImageRenderMode.Template)
20. .fitOriginalSize(true)
21. .matchTextDirection(true)
22. .objectRepeat(ImageRepeat.X)
23. .autoResize(true)
24. // 获取Image的属性
25. typeNode.getAttribute(imageNode, 'Image');
26. this!.rootNode!.appendChild(imageNode);
27. return this.rootNode;

29. }
30. }

32. @Entry
33. @Component
34. struct Sample {
35. build() {
36. Column({ space: 10 }) {
37. NodeContainer(new MyImageController()).margin(5)
38. }.width('100%').height('100%')

40. }
41. }
```

### List12+

PhonePC/2in1TabletTVWearable

type List = TypedFrameNode<ListInterface, ListAttribute>

List类型的FrameNode节点类型。只允许添加[ListItem](js-apis-arkui-framenode.md#listitem12)、[ListItemGroup](js-apis-arkui-framenode.md#listitemgroup12)类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ListInterface](ts-container-list.md#接口), [ListAttribute](ts-container-list.md#属性)> | 提供List类型FrameNode节点。  ListInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为List组件的构造函数类型。  ListAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回List组件的属性设置对象。 |

### createNode('List')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'List'): List

创建List类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'List' | 是 | 创建List类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [List](js-apis-arkui-framenode.md#list12) | List类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义List控制器
4. class MyListController extends NodeController {
5. public rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. // 创建list节点
9. this.rootNode = new FrameNode(uiContext);
10. // 创建List
11. let listNode = typeNode.createNode(uiContext, 'List');
12. listNode.initialize({ space: 3 }).size({ width: '100%', height: '100%' });
13. typeNode.getAttribute(listNode, "List")?.friction(0.6);

15. // 在list下创建ListItemGroup节点
16. let listItemGroupNode = typeNode.createNode(uiContext, 'ListItemGroup');
17. listItemGroupNode.initialize({ space: 3 });
18. listNode.appendChild(listItemGroupNode);

20. // 在ListItemGroup中放入ListItem节点
21. let listItemNode1 = typeNode.createNode(uiContext, 'ListItem');
22. listItemNode1.initialize({ style: ListItemStyle.NONE }).height(100).borderWidth(1).backgroundColor('#FF00FF');
23. let text1 = typeNode.createNode(uiContext, 'Text');
24. text1.initialize('ListItem1');
25. listItemNode1.appendChild(text1);
26. listItemGroupNode.appendChild(listItemNode1);

28. // 创建ListItem，添加Text至ListItem，添加至listItemGroup
29. let listItemNode2 = typeNode.createNode(uiContext, 'ListItem');
30. listItemNode2.initialize({ style: ListItemStyle.CARD }).borderWidth(1).backgroundColor('#FF00FF');
31. typeNode.getAttribute(listItemNode2, "ListItem")?.height(100);
32. let text2 = typeNode.createNode(uiContext, 'Text');
33. text2.initialize('ListItem2');
34. listItemNode2.appendChild(text2);
35. listItemGroupNode.appendChild(listItemNode2);

37. this!.rootNode!.appendChild(listNode);
38. return this.rootNode;
39. }
40. }

42. @Entry
43. @Component
44. struct FrameNodeTypeTest {
45. private myListController: MyListController = new MyListController();

47. build() {
48. Column({ space: 5 }) {
49. Text('ListSample')
50. NodeContainer(this.myListController)

52. }.width('100%')
53. }
54. }
```

### getEvent('List')19+

PhonePC/2in1TabletTVWearable

getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined

获取List节点中持有的UIListEvent对象，用于设置滚动事件。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取事件时所需的目标节点。 |
| nodeType | 'List' | 是 | 获取List节点类型的滚动事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIListEvent](ts-container-list.md#uilistevent19) | undefined | List节点类型的滚动事件，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[滚动事件示例](js-apis-arkui-framenode.md#滚动事件示例)。

### getAttribute('List')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'List'): ListAttribute | undefined

获取List节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'List' | 是 | 获取List节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ListAttribute | undefined | List节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('List')](js-apis-arkui-framenode.md#createnodelist12)的示例。

### bindController('List')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[List](js-apis-arkui-framenode.md#list12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定滚动控制器的目标节点。 |
| controller | [Scroller](ts-container-scroll.md#scroller) | 是 | 滚动控制器。 |
| nodeType | 'List' | 是 | 绑定滚动控制器的目标节点的节点类型为List。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. typeNode.bindController(node, scroller, 'List');
```

### ListItem12+

PhonePC/2in1TabletTVWearable

type ListItem = TypedFrameNode<ListItemInterface, ListItemAttribute>

ListItem类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ListItemInterface](ts-container-listitem.md#接口), [ListItemAttribute](ts-container-listitem.md#属性)> | 提供ListItem类型FrameNode节点。  ListItemInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为ListItem组件的构造函数类型。  ListItemAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回ListItem组件的属性设置对象。 |

### createNode('ListItem')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'ListItem'): ListItem

创建ListItem类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'ListItem' | 是 | 创建ListItem类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ListItem](js-apis-arkui-framenode.md#listitem12) | ListItem类型的FrameNode节点。 |

**示例：**

参考[createNode('List')](js-apis-arkui-framenode.md#createnodelist12)示例。

### getAttribute('ListItem')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'ListItem'): ListItemAttribute | undefined

获取ListItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'ListItem' | 是 | 获取ListItem节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ListItemAttribute | undefined | ListItem节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('List')](js-apis-arkui-framenode.md#createnodelist12)的示例。

### TextInput12+

PhonePC/2in1TabletTVWearable

type TextInput = TypedFrameNode<TextInputInterface, TextInputAttribute>

TextInput类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[TextInputInterface](ts-basic-components-textinput.md#接口), [TextInputAttribute](ts-basic-components-textinput.md#属性)> | 提供TextInput类型FrameNode节点。  TextInputInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextInput组件的构造函数类型。  TextInputAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextInput组件的属性设置对象。 |

### createNode('TextInput')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'TextInput'): TextInput

创建TextInput类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextInput' | 是 | 创建TextInput类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextInput](js-apis-arkui-framenode.md#textinput12) | TextInput类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建TextInput
12. let textInput = typeNode.createNode(uiContext, 'TextInput');
13. textInput.initialize({ text: "TextInput" });
14. col.appendChild(textInput);
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myNodeController: MyNodeController = new MyNodeController();

24. build() {
25. Column({ space: 5 }) {
26. Text('TextInput sample')
27. NodeContainer(this.myNodeController);
28. }
29. }
30. }
```

### getAttribute('TextInput')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'TextInput'): TextInputAttribute | undefined

获取TextInput节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'TextInput' | 是 | 获取TextInput节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TextInputAttribute | undefined | TextInput节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建TextInput
12. let textInput = typeNode.createNode(uiContext, 'TextInput');
13. textInput.initialize({ placeholder: 'TextInput placeholderColor' });
14. // 获取TextInput的属性
15. typeNode.getAttribute(textInput, 'TextInput')?.placeholderColor(Color.Red);
16. col.appendChild(textInput);
17. return node;
18. }
19. }

21. @Entry
22. @Component
23. struct FrameNodeTypeTest {
24. private myNodeController: MyNodeController = new MyNodeController();

26. build() {
27. Column({ space: 5 }) {
28. Text('TextInput getAttribute sample');
29. NodeContainer(this.myNodeController);
30. }
31. }
32. }
```

### bindController('TextInput')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void

将输入框控制器[TextInputController](ts-basic-components-textinput.md#textinputcontroller8)绑定到[TextInput](js-apis-arkui-framenode.md#textinput12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定输入框控制器的目标节点。 |
| controller | [TextInputController](ts-basic-components-textinput.md#textinputcontroller8) | 是 | 输入框控制器。 |
| nodeType | 'TextInput' | 是 | 绑定输入框控制器的目标节点的节点类型为TextInput。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建、初始化TextInput，默认获焦
12. let textInput = typeNode.createNode(uiContext, 'TextInput');
13. textInput.initialize({ text: "TextInput" })
14. .defaultFocus(true)
15. col.appendChild(textInput);
16. // 绑定TextInputController，设置光标位置
17. let controller: TextInputController = new TextInputController();
18. typeNode.bindController(textInput, controller, 'TextInput');
19. controller.caretPosition(3);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('TextInput bindController sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### Button12+

PhonePC/2in1TabletTVWearable

type Button = TypedFrameNode<ButtonInterface, ButtonAttribute>

Button类型的FrameNode节点类型。以子组件模式创建允许添加一个子组件。以label模式创建不可以添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ButtonInterface](ts-basic-components-button.md#接口), [ButtonAttribute](ts-basic-components-button.md#属性)> | 提供Button类型FrameNode节点。  ButtonInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Button组件的构造函数类型。  ButtonAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Button组件的属性设置对象。  接口入参label不为空时，以label模式创建Button组件，以此模式创建无法包含子组件，并且不允许再设置子组件，否则会抛出异常。且label模式和子组件模式在第一次initialize创建之后无法在后续的initialize进行动态修改，如需要包含子组件，第一次initialize时不要设置label参数。  以子组件模式创建时，只能包含一个子组件，不能设置多个子组件，否则会抛出异常。 |

### createNode('Button')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Button'): Button

创建Button类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Button' | 是 | 创建Button类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Button](js-apis-arkui-framenode.md#button12) | Button类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Button控制器
4. class MyButtonController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Button
14. let button = typeNode.createNode(uiContext, 'Button')
15. button.initialize("This is Button")
16. .onClick(() => {
17. uiContext.getPromptAction().showToast({ message: "Button clicked" })
18. })
19. col.appendChild(button)

21. return node;
22. }
23. }

25. @Entry
26. @Component
27. struct FrameNodeTypeTest {
28. private myButtonController: MyButtonController = new MyButtonController();

30. build() {
31. Column({ space: 5 }) {
32. Text('ButtonSample')
33. NodeContainer(this.myButtonController);

35. }.width('100%')
36. }
37. }
```

### getAttribute('Button')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Button'): ButtonAttribute | undefined

获取Button节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Button' | 是 | 获取Button节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonAttribute | undefined | Button节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Button控制器
4. class MyButtonController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. let button = typeNode.createNode(uiContext, 'Button')
14. button.initialize("This is Button")
15. .onClick(() => {
16. uiContext.getPromptAction().showToast({ message: "Button clicked" })
17. })
18. // 获取Button属性
19. typeNode.getAttribute(button,'Button')?.buttonStyle(ButtonStyleMode.TEXTUAL)
20. col.appendChild(button)

22. return node;
23. }
24. }

26. @Entry
27. @Component
28. struct FrameNodeTypeTest {
29. private myButtonController: MyButtonController = new MyButtonController();

31. build() {
32. Column({ space: 5 }) {
33. Text('ButtonSample')
34. NodeContainer(this.myButtonController);

36. }.width('100%')
37. }
38. }
```

### ListItemGroup12+

PhonePC/2in1TabletTVWearable

type ListItemGroup = TypedFrameNode<ListItemGroupInterface, ListItemGroupAttribute>

ListItemGroup类型的FrameNode节点类型。只允许添加[ListItem](ts-container-listitem.md)类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ListItemGroupInterface](ts-container-listitem.md#接口), [ListItemGroupAttribute](ts-container-listitem.md#属性)> | 提供ListItemGroup类型FrameNode节点。  ListItemGroupInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为ListItemGroup组件的构造函数类型。  ListItemGroupAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回ListItemGroup组件的属性设置对象。 |

### createNode('ListItemGroup')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup

创建ListItemGroup类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'ListItemGroup' | 是 | 创建ListItemGroup类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ListItemGroup](js-apis-arkui-framenode.md#listitemgroup12) | ListItemGroup类型的FrameNode节点。 |

**示例：**

参考[createNode('List')](js-apis-arkui-framenode.md#createnodelist12)示例。

### getAttribute('ListItemGroup')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'ListItemGroup'): ListItemGroupAttribute | undefined

获取ListItemGroup节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'ListItemGroup' | 是 | 获取ListItemGroup节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ListItemGroupAttribute | undefined | ListItemGroup节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. typeNode.getAttribute(node, 'ListItemGroup');
```

### WaterFlow12+

PhonePC/2in1TabletTVWearable

type WaterFlow = TypedFrameNode<WaterFlowInterface, WaterFlowAttribute>

WaterFlow类型的FrameNode节点类型。只允许添加[FlowItem](ts-container-flowitem.md)类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[WaterFlowInterface](ts-container-waterflow.md#接口), [WaterFlowAttribute](ts-container-waterflow.md#属性)> | 提供[WaterFlow](js-apis-arkui-framenode.md#waterflow12)类型FrameNode节点。  WaterFlowInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为WaterFlow组件的构造函数类型。  WaterFlowAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回WaterFlow组件的属性设置对象。 |

### createNode('WaterFlow')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow

创建WaterFlow类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'WaterFlow' | 是 | 创建WaterFlow类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WaterFlow](js-apis-arkui-framenode.md#waterflow12) | WaterFlow类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义WaterFlow控制器
4. class MyWaterFlowController extends NodeController {
5. public rootNode: FrameNode | null = null;
6. private minHeight: number = 80;
7. private maxHeight: number = 180;

9. // 计算FlowItem高
10. private getHeight() {
11. let ret = Math.floor(Math.random() * this.maxHeight);
12. return (ret > this.minHeight ? ret : this.minHeight);
13. }

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);

18. // 创建WaterFlow并设置属性
19. let waterFlowNode = typeNode.createNode(uiContext, 'WaterFlow');
20. waterFlowNode.attribute.size({ width: '100%', height: '100%' })
21. .columnsTemplate('1fr 1fr')
22. .columnsGap(10)
23. .rowsGap(5);
24. typeNode.getAttribute(waterFlowNode, "WaterFlow")?.friction(0.6);

26. // 创建FlowItem并设置属性
27. for (let i = 0; i < 20; i++) {
28. let flowItemNode = typeNode.createNode(uiContext, 'FlowItem');
29. flowItemNode.attribute.size({ height: this.getHeight() });
30. typeNode.getAttribute(flowItemNode, "FlowItem")?.width('100%');
31. waterFlowNode.appendChild(flowItemNode);

33. let text = typeNode.createNode(uiContext, 'Text');
34. text.initialize('N' + i)
35. .size({ width: '100%', height: '100%' })
36. .textAlign(TextAlign.Center)
37. .backgroundColor(0xF9CF93);
38. flowItemNode.appendChild(text);
39. }

41. this!.rootNode!.appendChild(waterFlowNode);
42. return this.rootNode;
43. }
44. }

46. @Entry
47. @Component
48. struct FrameNodeTypeTest {
49. private myWaterFlowController: MyWaterFlowController = new MyWaterFlowController();

51. build() {
52. Column({ space: 5 }) {
53. Text('WaterFlowSample')
54. NodeContainer(this.myWaterFlowController);

56. }.width('100%')
57. }
58. }
```

### getEvent('WaterFlow')19+

PhonePC/2in1TabletTVWearable

getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined

获取[WaterFlow](js-apis-arkui-framenode.md#waterflow12)节点中持有的UIWaterFlowEvent对象，用于设置滚动事件。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取事件时所需的目标节点。 |
| nodeType | 'WaterFlow' | 是 | 获取WaterFlow节点类型的滚动事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIWaterFlowEvent](ts-container-waterflow.md#uiwaterflowevent19) | undefined | WaterFlow节点类型的滚动事件，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[滚动事件示例](js-apis-arkui-framenode.md#滚动事件示例)。

### getAttribute('WaterFlow')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'WaterFlow'): WaterFlowAttribute | undefined

获取WaterFlow节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'WaterFlow' | 是 | 获取WaterFlow节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WaterFlowAttribute | undefined | WaterFlow节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('WaterFlow')](js-apis-arkui-framenode.md#createnodewaterflow12)的示例。

### bindController('WaterFlow')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[WaterFlow](js-apis-arkui-framenode.md#waterflow12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定滚动控制器的目标节点。 |
| controller | [Scroller](ts-container-scroll.md#scroller) | 是 | 滚动控制器。 |
| nodeType | 'WaterFlow' | 是 | 绑定滚动控制器的目标节点的节点类型为WaterFlow。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. typeNode.bindController(node, scroller, 'WaterFlow');
```

### FlowItem12+

PhonePC/2in1TabletTVWearable

type FlowItem = TypedFrameNode<FlowItemInterface, FlowItemAttribute>

FlowItem类型的FrameNode节点类型。允许添加一个子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[FlowItemInterface](ts-container-flowitem.md#接口), [FlowItemAttribute](ts-container-flowitem.md#属性)> | 提供FlowItem类型FrameNode节点。  FlowItemInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为FlowItem组件的构造函数类型。  FlowItemAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回FlowItem组件的属性设置对象。 |

### createNode('FlowItem')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem

创建FlowItem类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'FlowItem' | 是 | 创建FlowItem类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FlowItem](js-apis-arkui-framenode.md#flowitem12) | FlowItem类型的FrameNode节点。 |

**示例：**

参考[createNode('WaterFlow')](js-apis-arkui-framenode.md#createnodewaterflow12)示例。

### getAttribute('FlowItem')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'FlowItem'): FlowItemAttribute | undefined

获取FlowItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'FlowItem' | 是 | 获取FlowItem节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FlowItemAttribute | undefined | FlowItem节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('WaterFlow')](js-apis-arkui-framenode.md#createnodewaterflow12)的示例。

### XComponent12+

PhonePC/2in1TabletTVWearable

type XComponent = TypedFrameNode<XComponentInterface, XComponentAttribute>

XComponent类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[XComponentInterface](ts-basic-components-xcomponent.md#接口), [XComponentAttribute](ts-basic-components-xcomponent.md#属性)> | 提供XComponent类型FrameNode节点。  XComponentInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为XComponent组件的构造函数类型。  XComponentAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回XComponent组件的属性设置对象。 |

### createNode('XComponent')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'XComponent'): XComponent

创建XComponent类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'XComponent' | 是 | 创建XComponent类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [XComponent](js-apis-arkui-framenode.md#xcomponent12) | XComponent类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. let col = typeNode.createNode(uiContext, 'Column');
8. col.initialize({ space: 5 })
9. .width('100%')
10. .height('100%')
11. node.appendChild(col);
12. // 创建XComponent
13. let xcomponent = typeNode.createNode(uiContext, 'XComponent');
14. xcomponent.attribute.backgroundColor(Color.Red);
15. col.appendChild(xcomponent);
16. return node;
17. }
18. }

20. @Entry
21. @Component
22. struct FrameNodeTypeTest {
23. private myNodeController: MyNodeController = new MyNodeController();

25. build() {
26. Column({ space: 5 }) {
27. Text('XComponentSample')
28. NodeContainer(this.myNodeController)
29. }.width('100%')
30. }
31. }
```

### createNode('XComponent')12+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent

按照options中的配置参数创建XComponent类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'XComponent' | 是 | 创建XComponent类型的节点。 |
| options | [XComponentOptions](ts-basic-components-xcomponent.md#xcomponentoptions12) | 是 | 定义XComponent的具体配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [XComponent](js-apis-arkui-framenode.md#xcomponent12) | XComponent类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. controller: XComponentController = new XComponentController();
6. makeNode(uiContext: UIContext): FrameNode | null {
7. let node = new FrameNode(uiContext);
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col);
13. // 设置XComponent参数对象
14. let options: XComponentOptions = {
15. type: XComponentType.SURFACE,
16. controller: this.controller
17. };
18. // 创建XComponent
19. let xcomponent = typeNode.createNode(uiContext, 'XComponent', options);
20. xcomponent.attribute.backgroundColor(Color.Red);
21. col.appendChild(xcomponent);
22. return node;
23. }
24. }

26. @Entry
27. @Component
28. struct FrameNodeTypeTest {
29. private myNodeController: MyNodeController = new MyNodeController();

31. build() {
32. Column({ space: 5 }) {
33. Text('XComponentSample')
34. NodeContainer(this.myNodeController)
35. }.width('100%')
36. }
37. }
```

### createNode('XComponent')19+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent

按照parameters中的配置参数创建XComponent类型的FrameNode节点。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'XComponent' | 是 | 创建XComponent类型的节点。 |
| parameters | [NativeXComponentParameters](ts-basic-components-xcomponent.md#nativexcomponentparameters19) | 是 | 定义XComponent的具体配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [XComponent](js-apis-arkui-framenode.md#xcomponent12) | XComponent类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. controller: XComponentController = new XComponentController();
6. makeNode(uiContext: UIContext): FrameNode | null {
7. let node = new FrameNode(uiContext);
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col);
13. let parameters: NativeXComponentParameters = {
14. type: XComponentType.SURFACE
15. };
16. // 创建XComponent
17. let xcomponent = typeNode.createNode(uiContext, 'XComponent', parameters);
18. xcomponent.attribute.backgroundColor(Color.Red);
19. col.appendChild(xcomponent);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('XComponentSample')
32. NodeContainer(this.myNodeController)
33. }.width('100%')
34. }
35. }
```

### getAttribute('XComponent')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'XComponent'): XComponentAttribute | undefined

获取XComponent节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'XComponent' | 是 | 获取XComponent节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| XComponentAttribute | undefined | XComponent节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. typeNode.getAttribute(node, 'XComponent');
```

### QRCode14+

PhonePC/2in1TabletTVWearable

type QRCode = TypedFrameNode<QRCodeInterface, QRCodeAttribute>

QRCode类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[QRCodeInterface](ts-basic-components-qrcode.md#接口), [QRCodeAttribute](ts-basic-components-qrcode.md#属性)> | 提供QRCode类型FrameNode节点。  QRCodeInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为QRCode组件的构造函数类型。  QRCodeAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回QRCode组件的属性设置对象。 |

### createNode('QRCode')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'QRCode'): QRCode

创建QRCode类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'QRCode' | 是 | 创建QRCode类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [QRCode](js-apis-arkui-framenode.md#qrcode14) | QRCode类型的FrameNode节点。 |

**示例：**

```
1. typeNode.createNode(uiContext, 'QRCode');
```

### Badge14+

PhonePC/2in1TabletTVWearable

type Badge = TypedFrameNode<BadgeInterface, BadgeAttribute>

Badge类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[BadgeInterface](ts-container-badge.md#接口), [BadgeAttribute](ts-container-badge.md#属性)> | 提供Badge类型FrameNode节点。  BadgeInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Badge组件的构造函数类型。  BadgeAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Badge组件的属性设置对象。 |

### createNode('Badge')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Badge'): Badge

创建Badge类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Badge' | 是 | 创建Badge类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Badge](js-apis-arkui-framenode.md#badge14) | Badge类型的FrameNode节点。 |

**示例：**

```
1. typeNode.createNode(uiContext, 'Badge');
```

### Grid14+

PhonePC/2in1TabletTVWearable

type Grid = TypedFrameNode<GridInterface, GridAttribute>

Grid类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[GridInterface](ts-container-grid.md#接口), [GridAttribute](ts-container-grid.md#属性)> | 提供Grid类型FrameNode节点。  GridInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Grid组件的构造函数类型。  GridAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Grid组件的属性设置对象。 |

### createNode('Grid')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Grid'): Grid

创建Grid类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Grid' | 是 | 创建Grid类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Grid](js-apis-arkui-framenode.md#grid14) | Grid类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Grid控制器
4. class MyGridController extends NodeController {
5. public rootNode: FrameNode | null = null;
6. private scroller: Scroller = new Scroller();

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.rootNode = new FrameNode(uiContext);

11. // 创建Grid设置属性
12. let gridNode = typeNode.createNode(uiContext, 'Grid');
13. gridNode.initialize(this.scroller, { regularSize: [1, 1] })
14. .size({ width: '90%', height: 300 })
15. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
16. .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
17. .columnsGap(10)
18. .rowsGap(10);
19. typeNode.getAttribute(gridNode, "Grid")?.friction(0.6);

21. // 创建GridItem并设置属性
22. for (let i = 0; i < 25; i++) {
23. let gridItemNode = typeNode.createNode(uiContext, 'GridItem');
24. gridItemNode.initialize({ style: GridItemStyle.NONE }).size({ height: '100%' });
25. typeNode.getAttribute(gridItemNode, "GridItem")?.width('100%');

27. let text = typeNode.createNode(uiContext, 'Text');
28. text.initialize((i % 5).toString())
29. .size({ width: '100%', height: '100%' })
30. .textAlign(TextAlign.Center)
31. .backgroundColor(0xF9CF93);
32. gridItemNode.appendChild(text);
33. gridNode.appendChild(gridItemNode);
34. }

36. this!.rootNode!.appendChild(gridNode);
37. return this.rootNode;
38. }
39. }

41. @Entry
42. @Component
43. struct FrameNodeTypeTest {
44. private myGridController: MyGridController = new MyGridController();

46. build() {
47. Column({ space: 5 }) {
48. Text('GridSample')
49. NodeContainer(this.myGridController)

51. }.width('100%')
52. }
53. }
```

### getEvent('Grid')19+

PhonePC/2in1TabletTVWearable

getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined

获取Grid节点中持有的UIGridEvent对象，用于设置滚动事件。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取事件时所需的目标节点。 |
| nodeType | 'Grid' | 是 | 获取Grid节点类型的滚动事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIGridEvent](ts-container-grid.md#uigridevent19) | undefined | Grid节点类型的滚动事件，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[滚动事件示例](js-apis-arkui-framenode.md#滚动事件示例)。

### getAttribute('Grid')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Grid'): GridAttribute | undefined

获取Grid节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Grid' | 是 | 获取Grid节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| GridAttribute | undefined | Grid节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('Grid')](js-apis-arkui-framenode.md#createnodegrid14)的示例。

### bindController('Grid')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[Grid](js-apis-arkui-framenode.md#grid14)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定滚动控制器的目标节点。 |
| controller | [Scroller](ts-container-scroll.md#scroller) | 是 | 滚动控制器。 |
| nodeType | 'Grid' | 是 | 绑定滚动控制器的目标节点的节点类型为Grid。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. typeNode.bindController(node, scroller, 'Grid');
```

### GridItem14+

PhonePC/2in1TabletTVWearable

type GridItem = TypedFrameNode<GridItemInterface, GridItemAttribute>

GridItem类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[GridItemInterface](ts-container-griditem.md#接口), [GridItemAttribute](ts-container-griditem.md#属性)> | 提供GridItem类型FrameNode节点。  GridItemInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为GridItem组件的构造函数类型。  GridItemAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回GridItem组件的属性设置对象。 |

### createNode('GridItem')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'GridItem'): GridItem

创建GridItem类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'GridItem' | 是 | 创建GridItem类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridItem](js-apis-arkui-framenode.md#griditem14) | GridItem类型的FrameNode节点。 |

**示例：**

参考[createNode('Grid')](js-apis-arkui-framenode.md#createnodegrid14)示例。

### getAttribute('GridItem')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'GridItem'): GridItemAttribute | undefined

获取GridItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'GridItem' | 是 | 获取GridItem节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| GridItemAttribute | undefined | GridItem节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

完整示例请参考[createNode('Grid')](js-apis-arkui-framenode.md#createnodegrid14)的示例。

### TextClock14+

PhonePC/2in1TabletTVWearable

type TextClock = TypedFrameNode<TextClockInterface, TextClockAttribute>

TextClock类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[TextClockInterface](ts-basic-components-textclock.md#接口), [TextClockAttribute](ts-basic-components-textclock.md#属性)> | 提供TextClock类型FrameNode节点。  TextClockInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextClock组件的构造函数类型。  TextClockAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextClock组件的属性设置对象。 |

### createNode('TextClock')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'TextClock'): TextClock

创建TextClock类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextClock' | 是 | 创建TextClock类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextClock](js-apis-arkui-framenode.md#textclock14) | TextClock类型的FrameNode节点。 |

**示例：**

```
1. typeNode.createNode(uiContext, 'TextClock');
```

### TextTimer14+

PhonePC/2in1TabletTVWearable

type TextTimer = TypedFrameNode<TextTimerInterface, TextTimerAttribute>

TextTimer类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[TextTimerInterface](ts-basic-components-texttimer.md#接口), [TextTimerAttribute](ts-basic-components-texttimer.md#属性)> | 提供TextTimer类型FrameNode节点。  TextTimerInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextTimer组件的构造函数类型。  TextTimerAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextTimer组件的属性设置对象。 |

### createNode('TextTimer')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer

创建TextTimer类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextTimer' | 是 | 创建TextTimer类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextTimer](js-apis-arkui-framenode.md#texttimer14) | TextTimer类型的FrameNode节点。 |

**示例：**

```
1. typeNode.createNode(uiContext, 'TextTimer');
```

### Marquee14+

PhonePC/2in1TabletTVWearable

type Marquee = TypedFrameNode<MarqueeInterface, MarqueeAttribute>

Marquee类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[MarqueeInterface](ts-basic-components-marquee.md#接口), [MarqueeAttribute](ts-basic-components-marquee.md#属性)> | 提供Marquee类型FrameNode节点。  MarqueeInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Marquee组件的构造函数类型。  MarqueeAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Marquee组件的属性设置对象。 |

### createNode('Marquee')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Marquee'): Marquee

创建Marquee类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Marquee' | 是 | 创建Marquee类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Marquee](js-apis-arkui-framenode.md#marquee14) | Marquee类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 })
10. node.appendChild(col);
11. // 创建marquee
12. let marquee = typeNode.createNode(uiContext, 'Marquee');
13. marquee.initialize({start:true,src:'Marquee, if need display, src shall be long'})
14. .width(100);
15. col.appendChild(marquee);
16. return node;
17. }
18. }

20. @Entry
21. @Component
22. struct FrameNodeTypeTest {
23. private myNodeController: MyNodeController = new MyNodeController();

25. build() {
26. Column({ space: 5 }) {
27. Text('Marquee createNode sample');
28. NodeContainer(this.myNodeController);
29. }
30. }
31. }
```

### TextArea14+

PhonePC/2in1TabletTVWearable

type TextArea = TypedFrameNode<TextAreaInterface, TextAreaAttribute>

TextArea类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[TextAreaInterface](ts-basic-components-textarea.md#接口), [TextAreaAttribute](ts-basic-components-textarea.md#属性)> | 提供TextArea类型FrameNode节点。  TextAreaInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextArea组件的构造函数类型。  TextAreaAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextArea组件的属性设置对象。 |

### createNode('TextArea')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'TextArea'): TextArea

创建TextArea类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextArea' | 是 | 创建TextArea类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextArea](js-apis-arkui-framenode.md#textarea14) | TextArea类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 })
10. node.appendChild(col);
11. // 创建textArea
12. let textArea = typeNode.createNode(uiContext, 'TextArea');
13. textArea.initialize({ text: "TextArea" });
14. col.appendChild(textArea);
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myNodeController: MyNodeController = new MyNodeController();

24. build() {
25. Column({ space: 5 }) {
26. Text('TextArea create sample')
27. NodeContainer(this.myNodeController);
28. }
29. }
30. }
```

### getAttribute('TextArea')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'TextArea'): TextAreaAttribute | undefined

获取TextArea节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'TextArea' | 是 | 获取TextArea节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TextAreaAttribute | undefined | TextArea节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建TextArea
12. let textArea = typeNode.createNode(uiContext, 'TextArea');
13. textArea.initialize({ placeholder: 'TextArea placeholderColor' });
14. col.appendChild(textArea);
15. // 获取TextArea节点的属性
16. typeNode.getAttribute(textArea, 'TextArea')?.placeholderColor(Color.Red);
17. return node;
18. }
19. }

21. @Entry
22. @Component
23. struct FrameNodeTypeTest {
24. private myNodeController: MyNodeController = new MyNodeController();

26. build() {
27. Column({ space: 5 }) {
28. Text('TextArea getAttribute sample');
29. NodeContainer(this.myNodeController);
30. }
31. }
32. }
```

### bindController('TextArea')20+

PhonePC/2in1TabletTVWearable

bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void

将输入框控制器[TextAreaController](ts-basic-components-textarea.md#textareacontroller8)绑定到[TextArea](js-apis-arkui-framenode.md#textarea14)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定输入框控制器的目标节点。 |
| controller | [TextAreaController](ts-basic-components-textarea.md#textareacontroller8) | 是 | 输入框控制器。 |
| nodeType | 'TextArea' | 是 | 绑定输入框控制器的目标节点的节点类型为TextArea。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建、初始化TextArea，默认获焦
12. let textArea = typeNode.createNode(uiContext, 'TextArea');
13. textArea.initialize({ text: "TextArea" })
14. .defaultFocus(true)
15. col.appendChild(textArea);
16. // 绑定TextAreaController，设置光标位置
17. let controller: TextAreaController = new TextAreaController()
18. typeNode.bindController(textArea, controller, 'TextArea');
19. controller.caretPosition(3);
20. return node;
21. }
22. }

24. @Entry
25. @Component
26. struct FrameNodeTypeTest {
27. private myNodeController: MyNodeController = new MyNodeController();

29. build() {
30. Column({ space: 5 }) {
31. Text('TextArea bindController sample');
32. NodeContainer(this.myNodeController);
33. }
34. }
35. }
```

### SymbolGlyph14+

PhonePC/2in1TabletTVWearable

type SymbolGlyph = TypedFrameNode<SymbolGlyphInterface, SymbolGlyphAttribute>

SymbolGlyph类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[SymbolGlyphInterface](ts-basic-components-symbolglyph.md#接口), [SymbolGlyphAttribute](ts-basic-components-symbolglyph.md#属性)> | 提供SymbolGlyph类型FrameNode节点。  SymbolGlyphInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为SymbolGlyph组件的构造函数类型。  SymbolGlyphAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回SymbolGlyph组件的属性设置对象。 |

### createNode('SymbolGlyph')14+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph

创建SymbolGlyph类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'SymbolGlyph' | 是 | 创建SymbolGlyph类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SymbolGlyph](js-apis-arkui-framenode.md#symbolglyph14) | SymbolGlyph类型的FrameNode节点。 |

**示例：**

```
1. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute;
8. let col = typeNode.createNode(uiContext, 'Column');
9. col.initialize({ space: 5 });
10. node.appendChild(col);
11. // 创建SymbolGlyph
12. let symbolGlyph = typeNode.createNode(uiContext, 'SymbolGlyph');
13. symbolGlyph.initialize($r('sys.symbol.ohos_trash'));
14. col.appendChild(symbolGlyph);
15. return node;
16. }
17. }

19. @Entry
20. @Component
21. struct FrameNodeTypeTest {
22. private myNodeController: MyNodeController = new MyNodeController();

24. build() {
25. Column({ space: 5 }) {
26. Text('SymbolGlyph sample');
27. NodeContainer(this.myNodeController);
28. }
29. }
30. }
```

### Checkbox18+

PhonePC/2in1TabletTVWearable

type Checkbox = TypedFrameNode<CheckboxInterface, CheckboxAttribute>

Checkbox类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[CheckboxInterface](ts-basic-components-checkbox.md#接口), [CheckboxAttribute](ts-basic-components-checkbox.md#属性)> | 提供Checkbox类型FrameNode节点。  CheckboxInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Checkbox组件的构造函数类型。  CheckboxAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Checkbox组件的属性设置对象。 |

### createNode('Checkbox')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox

创建Checkbox类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Checkbox' | 是 | 创建Checkbox类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Checkbox](js-apis-arkui-framenode.md#checkbox18) | Checkbox类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Checkbox控制器
4. class MyCheckboxController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Checkbox
14. let checkbox = typeNode.createNode(uiContext, 'Checkbox')
15. checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

17. // 创建另一个Checkbox
18. let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
19. checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

21. // 将两个checkbox添加至col进行比较
22. col.appendChild(checkbox)
23. col.appendChild(checkbox1)
24. return node;
25. }
26. }

28. @Entry
29. @Component
30. struct FrameNodeTypeTest {
31. private myCheckboxController: MyCheckboxController = new MyCheckboxController();

33. build() {
34. Column({ space: 5 }) {
35. Text('CheckboxSample')
36. NodeContainer(this.myCheckboxController);
37. }.width('100%')
38. }
39. }
```

### getAttribute('Checkbox')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Checkbox'): CheckboxAttribute | undefined

获取Checkbox节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Checkbox' | 是 | 获取Checkbox节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CheckboxAttribute | undefined | Checkbox节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Checkbox控制器
4. class MyCheckboxController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Checkbox
14. let checkbox = typeNode.createNode(uiContext, 'Checkbox')
15. checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

17. // 创建另一个Checkbox
18. let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
19. checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })
20. // 给首个Checkbox设置形状属性
21. typeNode.getAttribute(checkbox1,'Checkbox')?.shape(CheckBoxShape.ROUNDED_SQUARE)
22. // 将两个checkbox添加至col进行比较
23. col.appendChild(checkbox)
24. col.appendChild(checkbox1)
25. return node;
26. }
27. }

29. @Entry
30. @Component
31. struct FrameNodeTypeTest {
32. private myCheckboxController: MyCheckboxController = new MyCheckboxController();

34. build() {
35. Column({ space: 5 }) {
36. Text('CheckboxSample')
37. NodeContainer(this.myCheckboxController);
38. }.width('100%')
39. }
40. }
```

### CheckboxGroup18+

PhonePC/2in1TabletTVWearable

type CheckboxGroup = TypedFrameNode<CheckboxGroupInterface, CheckboxGroupAttribute>

CheckboxGroup类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[CheckboxGroupInterface](ts-basic-components-checkboxgroup.md#接口), [CheckboxGroupAttribute](ts-basic-components-checkboxgroup.md#属性)> | 提供CheckboxGroup类型FrameNode节点。  CheckboxGroupInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为CheckboxGroup组件的构造函数类型。  CheckboxGroupAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回CheckboxGroup组件的属性设置对象。 |

### createNode('CheckboxGroup')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup

创建CheckboxGroup类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'CheckboxGroup' | 是 | 创建CheckboxGroup类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CheckboxGroup](js-apis-arkui-framenode.md#checkboxgroup18) | CheckboxGroup类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义CheckboxGroup控制器
4. class MyCheckboxGroupController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. let checkbox = typeNode.createNode(uiContext, 'Checkbox')
14. checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

16. let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
17. checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

19. // 创建checkboxGroup
20. let checkboxGroup = typeNode.createNode(uiContext, 'CheckboxGroup')
21. checkboxGroup.initialize({ group: 'checkboxGroup1' })

23. col.appendChild(checkbox)
24. col.appendChild(checkbox1)
25. col.appendChild(checkboxGroup)
26. return node;
27. }
28. }

30. @Entry
31. @Component
32. struct FrameNodeTypeTest {
33. private myCheckboxGroupController: MyCheckboxGroupController = new MyCheckboxGroupController();

35. build() {
36. Column({ space: 5 }) {
37. Text('CheckboxGroupSample')
38. NodeContainer(this.myCheckboxGroupController);
39. }.width('100%')
40. }
41. }
```

### Rating18+

PhonePC/2in1TabletTVWearable

type Rating = TypedFrameNode<RatingInterface, RatingAttribute>

Rating类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[RatingInterface](ts-basic-components-rating.md#接口), [RatingAttribute](ts-basic-components-rating.md#属性)> | 提供Rating类型FrameNode节点。  RatingInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Rating组件的构造函数类型。  RatingAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Rating组件的属性设置对象。 |

### createNode('Rating')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Rating'): Rating

创建Rating类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Rating' | 是 | 创建Rating类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Rating](js-apis-arkui-framenode.md#rating18) | Rating类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Rating控制器
4. class MyRatingController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建rating
14. let rating = typeNode.createNode(uiContext, 'Rating')
15. rating.initialize({ rating: 0 })
16. col.appendChild(rating)
17. return node;
18. }
19. }

21. @Entry
22. @Component
23. struct FrameNodeTypeTest {
24. private myRatingController: MyRatingController = new MyRatingController();

26. build() {
27. Column({ space: 5 }) {
28. Text('RatingSample')

30. NodeContainer(this.myRatingController);

32. }.width('100%')
33. }
34. }
```

### Radio18+

PhonePC/2in1TabletTVWearable

type Radio = TypedFrameNode<RadioInterface, RadioAttribute>

Radio类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[RadioInterface](ts-basic-components-radio.md#接口), [RadioAttribute](ts-basic-components-radio.md#属性)> | 提供Radio类型FrameNode节点。  RadioInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Radio组件的构造函数类型。  RadioAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Radio组件的属性设置对象。 |

### createNode('Radio')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Radio'): Radio

创建Radio类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Radio' | 是 | 创建Radio类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Radio](js-apis-arkui-framenode.md#radio18) | Radio类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Radio控制器
4. class MyRadioController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Radio
14. let radio1 = typeNode.createNode(uiContext, 'Radio')
15. radio1.initialize({ value: 'radio1', group: 'radioGroup' })

17. // 创建另一个Radio用于对比
18. let radio2 = typeNode.createNode(uiContext, 'Radio')
19. radio2.initialize({ value: 'radio2', group: 'radioGroup' })

21. col.appendChild(radio1)
22. col.appendChild(radio2)
23. return node;
24. }
25. }

27. @Entry
28. @Component
29. struct FrameNodeTypeTest {
30. private myRadioController: MyRadioController = new MyRadioController();

32. build() {
33. Column({ space: 5 }) {
34. Text('RadioSample')
35. NodeContainer(this.myRadioController);
36. }.width('100%')
37. }
38. }
```

### getAttribute('Radio')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Radio'): RadioAttribute | undefined

获取Radio节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Radio' | 是 | 获取Radio节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RadioAttribute | undefined | Radio节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Radio控制器
4. class MyRadioController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建radio
14. let radio1 = typeNode.createNode(uiContext, 'Radio')
15. radio1.initialize({ value: 'radio1', group: 'radioGroup' })
16. typeNode.getAttribute(radio1,'Radio')?.checked(true)
17. // 创建另一个radio用于对比
18. let radio2 = typeNode.createNode(uiContext, 'Radio')
19. radio2.initialize({ value: 'radio2', group: 'radioGroup' })

22. col.appendChild(radio1)
23. col.appendChild(radio2)
24. return node;
25. }
26. }

28. @Entry
29. @Component
30. struct FrameNodeTypeTest {
31. private myRadioController: MyRadioController = new MyRadioController();

33. build() {
34. Column({ space: 5 }) {
35. Text('RadioSample')
36. NodeContainer(this.myRadioController);
37. }.width('100%')
38. }
39. }
```

### Slider18+

PhonePC/2in1TabletTVWearable

type Slider = TypedFrameNode<SliderInterface, SliderAttribute>

Slider类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[SliderInterface](ts-basic-components-slider.md#接口), [SliderAttribute](ts-basic-components-slider.md#属性)> | 提供Slider类型FrameNode节点。  SliderInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Slider组件的构造函数类型。  SliderAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Slider组件的属性设置对象。 |

### createNode('Slider')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Slider'): Slider

创建Slider类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Slider' | 是 | 创建Slider类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Slider](js-apis-arkui-framenode.md#slider18) | Slider类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Slider控制器
4. class MySliderController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Slider
14. let slider = typeNode.createNode(uiContext, 'Slider')
15. slider.initialize({value:50})
16. col.appendChild(slider)
17. return node;
18. }
19. }

21. @Entry
22. @Component
23. struct FrameNodeTypeTest {
24. private mySliderController: MySliderController = new MySliderController();

26. build() {
27. Column({ space: 5 }) {
28. Text('SliderSample')
29. NodeContainer(this.mySliderController);

31. }.width('100%')
32. }
33. }
```

### getAttribute('Slider')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Slider'): SliderAttribute | undefined

获取Slider节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Slider' | 是 | 获取Slider节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SliderAttribute | undefined | Slider节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Slider控制器
4. class MySliderController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Slider
14. let slider = typeNode.createNode(uiContext, 'Slider')
15. slider.initialize({value:50})
16. typeNode.getAttribute(slider,'Slider')?.selectedColor(Color.Pink)
17. col.appendChild(slider)
18. return node;
19. }
20. }

22. @Entry
23. @Component
24. struct FrameNodeTypeTest {
25. private mySliderController: MySliderController = new MySliderController();

27. build() {
28. Column({ space: 5 }) {
29. Text('SliderSample')
30. NodeContainer(this.mySliderController);

32. }.width('100%')
33. }
34. }
```

### Select18+

PhonePC/2in1TabletTVWearable

type Select = TypedFrameNode<SelectInterface, SelectAttribute>

Select类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[SelectInterface](ts-basic-components-select.md#接口), [SelectAttribute](ts-basic-components-select.md#属性)> | 提供Select类型FrameNode节点。  SelectInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Select组件的构造函数类型。  SelectAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Select组件的属性设置对象。 |

### createNode('Select')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Select'): Select

创建Select类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Select' | 是 | 创建Select类型的节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Select](js-apis-arkui-framenode.md#select18) | Select类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Select控制器
4. class MySelectController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Select并设置选项
14. let select = typeNode.createNode(uiContext, 'Select')
15. select.initialize([{ value: "option one" }, { value: "option two" }, { value: "option three" }])
16. col.appendChild(select)
17. return node;
18. }
19. }

21. @Entry
22. @Component
23. struct FrameNodeTypeTest {
24. private mySelectController: MySelectController = new MySelectController();

26. build() {
27. Column({ space: 5 }) {
28. Text('SelectSample')
29. NodeContainer(this.mySelectController);
30. }.width('100%')
31. }
32. }
```

### Toggle18+

PhonePC/2in1TabletTVWearable

type Toggle = TypedFrameNode<[ToggleInterface](ts-basic-components-toggle.md#接口), [ToggleAttribute](ts-basic-components-toggle.md#属性)>

[Toggle](ts-basic-components-toggle.md)类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<[ToggleInterface](ts-basic-components-toggle.md#接口), [ToggleAttribute](ts-basic-components-toggle.md#属性)> | 提供Toggle类型FrameNode节点。  ToggleInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Toggle组件的构造函数类型。  ToggleAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Toggle组件的属性设置对象。 |

### createNode('Toggle')18+

PhonePC/2in1TabletTVWearable

createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle

创建Toggle类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Toggle' | 是 | 创建Toggle类型的节点。 |
| options | [ToggleOptions](ts-basic-components-toggle.md#toggleoptions18对象说明) | 否 | 创建Toggle节点的接口参数，仅可通过ToggleOptions中的type属性设置开关样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Toggle](js-apis-arkui-framenode.md#toggle18) | Toggle类型的FrameNode节点。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Toggle控制器
4. class MyToggleController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Toggle
14. let toggleSwitch = typeNode.createNode(uiContext, 'Toggle')
15. toggleSwitch.initialize({ type: ToggleType.Switch })
16. col.appendChild(toggleSwitch)

18. return node;
19. }
20. }

22. @Entry
23. @Component
24. struct FrameNodeTypeTest {
25. private myToggleController: MyToggleController = new MyToggleController();

27. build() {
28. Column({ space: 5 }) {
29. Text('ToggleSample')
30. NodeContainer(this.myToggleController);

32. }.width('100%')
33. }
34. }
```

### getAttribute('Toggle')20+

PhonePC/2in1TabletTVWearable

getAttribute(node: FrameNode, nodeType: 'Toggle'): ToggleAttribute | undefined

获取Toggle节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 获取属性时所需的目标节点。 |
| nodeType | 'Toggle' | 是 | 获取Toggle节点类型的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToggleAttribute | undefined | Toggle节点类型的属性，若获取失败，则返回undefined。 |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义Toggle控制器
4. class MyToggleController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext)
7. node.commonAttribute
8. let col = typeNode.createNode(uiContext, 'Column')
9. col.initialize({ space: 5 })
10. .width('100%')
11. .height('100%')
12. node.appendChild(col)
13. // 创建Toggle
14. let toggleSwitch = typeNode.createNode(uiContext, 'Toggle')
15. toggleSwitch.initialize({ type: ToggleType.Switch })
16. typeNode.getAttribute(toggleSwitch,'Toggle')?.selectedColor(Color.Orange)
17. col.appendChild(toggleSwitch)
18. return node;
19. }
20. }

22. @Entry
23. @Component
24. struct FrameNodeTypeTest {
25. private myToggleController: MyToggleController = new MyToggleController();

27. build() {
28. Column({ space: 5 }) {
29. Text('ToggleSample')
30. NodeContainer(this.myToggleController);

32. }.width('100%')
33. }
34. }
```

## NodeAdapter12+

PhonePC/2in1TabletTVWearable

NodeAdapter提供FrameNode的数据懒加载能力，通过[LazyForEach](ts-rendering-control-lazyforeach.md)实现接口功能。

说明

入参不能为负数，入参为负数时不做处理。

**示例：**

请参考[NodeAdapter使用示例](js-apis-arkui-framenode.md#nodeadapter使用示例)。

### constructor12+

PhonePC/2in1TabletTVWearable

constructor()

NodeAdapter的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### dispose12+

PhonePC/2in1TabletTVWearable

dispose(): void

立即释放当前的NodeAdapter。如果是已绑定的状态，会先进行解绑操作，再释放当前的NodeAdapter。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### totalNodeCount12+

PhonePC/2in1TabletTVWearable

set totalNodeCount(count: number)

设置数据节点总数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 数据节点总数。  取值范围：[0, +∞) |

get totalNodeCount(): number

获取数据节点总数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 数据节点总数。  取值范围：[0, +∞) |

### reloadAllItems12+

PhonePC/2in1TabletTVWearable

reloadAllItems(): void

重新加载全部数据操作。实际调用了LazyForEach中的[OnDataReloaded](ts-rendering-control-lazyforeach.md#ondatareloaded)接口通知组件重新加载所有数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### reloadItem12+

PhonePC/2in1TabletTVWearable

reloadItem(start: number, count: number): void

从索引值开始重新加载指定数量的节点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 重新加载的节点开始索引值。  取值范围：[0, +∞) |
| count | number | 是 | 重新加载数据节点的数量。  取值范围：[0, +∞) |

### removeItem12+

PhonePC/2in1TabletTVWearable

removeItem(start: number, count: number): void

从索引值开始删除指定数量的节点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 删除的节点开始索引值。  取值范围：[0, +∞) |
| count | number | 是 | 删除数据节点的数量。  取值范围：[0, +∞) |

### insertItem12+

PhonePC/2in1TabletTVWearable

insertItem(start: number, count: number): void

从索引值开始新增指定数量的节点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 新增的节点开始索引值。  取值范围：[0, +∞) |
| count | number | 是 | 新增数据节点的数量。  取值范围：[0, +∞) |

### moveItem12+

PhonePC/2in1TabletTVWearable

moveItem(from: number, to: number): void

将数据从原始索引移动到目的索引。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 | 数据移动的原始索引值。  取值范围：[0, +∞) |
| to | number | 是 | 数据移动的目的索引值。  取值范围：[0, +∞) |

### getAllAvailableItems12+

PhonePC/2in1TabletTVWearable

getAllAvailableItems(): Array<FrameNode>

获取所有有效数据。有效节点数据包括显示在屏幕上的节点以及预加载的节点。其中预加载节点的数量可依照LazyForEach的[使用限制](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#使用限制)，调整父容器的cachedCount属性进行设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<FrameNode> | FrameNode数据节点集合。 |

### onAttachToNode12+

PhonePC/2in1TabletTVWearable

onAttachToNode?(target: FrameNode): void

FrameNode绑定NodeAdapter时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | FrameNode | 是 | 绑定NodeAdapter的FrameNode节点。 |

### onDetachFromNode12+

PhonePC/2in1TabletTVWearable

onDetachFromNode?(): void

解除绑定时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### onGetChildId12+

PhonePC/2in1TabletTVWearable

onGetChildId?(index: number): number

节点首次加载或新节点滑入时回调。传入的index参数用于自定义生成Id，需要开发者自行保证根据不同index生成Id的唯一性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 加载节点索引值。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回开发者自定义生成的Id，需要开发者自行保证Id的唯一性。 |

### onCreateChild12+

PhonePC/2in1TabletTVWearable

onCreateChild?(index: number): FrameNode

节点首次加载或新节点滑入时回调。建议开发者在添加子组件时，遵循声明式组件中子组件的约束。例如，WaterFlow支持添加FlowItem子节点。父节点根据子节点的索引与key值判断是否触发了节点首次加载或新节点滑入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 加载节点索引值。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FrameNode | 返回开发者创建的FrameNode节点。 |

### onDisposeChild12+

PhonePC/2in1TabletTVWearable

onDisposeChild?(id: number, node: FrameNode): void

子节点即将销毁时回调。既不显示在屏幕上，也不处于预加载范围内的节点都属于即将销毁的节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 即将销毁的子节点id。 |
| node | FrameNode | 是 | 即将销毁的FrameNode节点。 |

### onUpdateChild12+

PhonePC/2in1TabletTVWearable

onUpdateChild?(id: number, node: FrameNode): void

重新加载的数据节点被复用时回调。已缓存节点的key值与被复用节点一致时进行节点复用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 复用节点的id。 |
| node | FrameNode | 是 | 被复用的FrameNode节点。 |

### attachNodeAdapter12+

PhonePC/2in1TabletTVWearable

static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean

给FrameNode绑定一个NodeAdapter。一个节点只能绑定一个NodeAdapter。已经绑定NodeAdapter的再次绑定会失败并返回false。

说明

支持绑定的组件：Column、Row、Stack、GridRow、Flex、Swiper、RelativeContainer、List、ListItemGroup、WaterFlow、Grid。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adapter | [NodeAdapter](js-apis-arkui-framenode.md#nodeadapter12) | 是 | 定义懒加载的NodeAdapter类。 |
| node | FrameNode | 是 | 绑定的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 绑定结果，返回true绑定成功，false绑定失败。 |

### detachNodeAdapter12+

PhonePC/2in1TabletTVWearable

static detachNodeAdapter(node: FrameNode): void

解除绑定操作，解除FrameNode节点绑定的NodeAdapter。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | FrameNode | 是 | 要解除绑定的FrameNode节点。 |

### isDisposed20+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前NodeAdapter对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

请参考[检验NodeAdapter是否有效示例](js-apis-arkui-framenode.md#检验nodeadapter是否有效示例)。

## 自定义具体类型节点示例

PhonePC/2in1TabletTVWearable

以Text节点为例，创建Text类型节点。

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.commonAttribute.width(100)
8. .height(50)
9. .borderColor(Color.Gray)
10. .borderWidth(1)
11. .margin({ left: 10 });
12. let col = typeNode.createNode(uiContext, 'Column');
13. col.initialize({ space: 5 })
14. .width('100%').height('100%').margin({ top: 5 });
15. node.appendChild(col);
16. let text = typeNode.createNode(uiContext, 'Text');
17. text.initialize("Hello").fontColor(Color.Blue).fontSize(14);
18. col.appendChild(text);
19. return node;
20. }
21. }

23. @Entry
24. @Component
25. struct FrameNodeTypeTest {
26. private myNodeController: MyNodeController = new MyNodeController();

28. build() {
29. Row() {
30. NodeContainer(this.myNodeController);
31. }
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/yJ7zHyVER96DlOTbEK2tgw/zh-cn_image_0000002583479447.png?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=55B23FD42802C08A5BACD55DB271AF819825422E44C624C954B52E78111C2295)

## 节点操作示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode, UIContext, typeNode } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TEST_TAG: string = "FrameNode "

6. // 继承NodeController实现自定义UI控制器
7. class MyNodeController extends NodeController {
8. public frameNode: FrameNode | null = null;
9. public childList: Array<FrameNode> = new Array<FrameNode>();
10. private rootNode: FrameNode | null = null;
11. private uiContext: UIContext | null = null;
12. private childrenCount: number = 0;

14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext);
16. this.uiContext = uiContext;

18. this.frameNode = new FrameNode(uiContext);
19. this.frameNode.commonAttribute.backgroundColor(Color.Pink);
20. this.frameNode.commonAttribute.size({ width: 100, height: 100 });
21. this.addCommonEvent(this.frameNode)
22. this.rootNode.appendChild(this.frameNode);
23. this.childrenCount = this.childrenCount + 1;

25. // 批量创建10个子节点并挂载到主节点
26. for (let i = 0; i < 10; i++) {
27. let childNode = new FrameNode(uiContext);
28. this.childList.push(childNode);
29. this.frameNode.appendChild(childNode);
30. }

32. // 创建Stack容器节点
33. let stackNode = typeNode.createNode(uiContext, "Stack");
34. this.frameNode.appendChild(stackNode);
35. return this.rootNode;
36. }

38. // 为节点添加点击事件
39. addCommonEvent(frameNode: FrameNode) {
40. frameNode.commonEvent.setOnClick((event: ClickEvent) => {
41. console.info(`Click FrameNode: ${JSON.stringify(event)}`)
42. })
43. }

45. createFrameNode() {
46. let frameNode = new FrameNode(this.uiContext!);
47. frameNode.commonAttribute.backgroundColor(Color.Pink);
48. frameNode.commonAttribute.size({ width: 100, height: 100 });
49. frameNode.commonAttribute.position({ x: this.childrenCount * 120, y: 0 });

51. return frameNode;
52. }

54. // 追加子节点到根节点的末尾
55. appendChild() {
56. const childNode = this.createFrameNode();
57. this.rootNode!.appendChild(childNode);
58. this.childrenCount = this.childrenCount + 1;
59. }

61. // 在指定索引节点后插入新节点
62. insertChildAfter(index: number) {
63. let insertNode = this.createFrameNode();
64. let childNode = this.rootNode!.getChild(index);
65. this.rootNode!.insertChildAfter(insertNode, childNode);
66. this.childrenCount = this.childrenCount + 1;
67. }

69. // 移除指定索引的子节点
70. removeChild(index: number) {
71. let childNode = this.rootNode!.getChild(index);
72. if (childNode == null) {
73. console.info(`${TEST_TAG} getchild at index {${index}} : fail`);
74. return;
75. }
76. this.rootNode!.removeChild(childNode);
77. this.childrenCount = this.childrenCount - 1;
78. }

80. // 打印节点计数
81. getChildNumber() {
82. console.info(`${TEST_TAG} getChildNumber ${this.rootNode!.getChildrenCount()}`)
83. console.info(`${TEST_TAG} children count is ${this.childrenCount}`);
84. }

86. // 清空所有子节点
87. clearChildren() {
88. this.rootNode!.clearChildren();
89. }

91. // 节点关系校验
92. searchFrameNode() {
93. if (this.rootNode!.getFirstChild() === null) {
94. console.info(`${TEST_TAG} the rootNode does not have child node.`)
95. }
96. if (this.rootNode!.getFirstChild() === this.frameNode) {
97. console.info(`${TEST_TAG} getFirstChild  result: success. The first child of the rootNode is equals to frameNode.`);
98. } else {
99. console.info(`${TEST_TAG} getFirstChild  result: fail. The first child of the rootNode is not equals to frameNode.`);
100. }
101. if (this.frameNode!.getChild(5) === this.frameNode!.getChild(4)!.getNextSibling()) {
102. console.info(`${TEST_TAG} getNextSibling  result: success.`);
103. } else {
104. console.info(`${TEST_TAG} getNextSibling  result: fail.`);
105. }
106. if (this.frameNode!.getChild(3) === this.frameNode!.getChild(4)!.getPreviousSibling()) {
107. console.info(`${TEST_TAG} getPreviousSibling  result: success.`);
108. } else {
109. console.info(`${TEST_TAG} getPreviousSibling  result: fail.`);
110. }
111. if (this.rootNode!.getFirstChild() !== null && this.rootNode!.getFirstChild()!.getParent() === this.rootNode) {
112. console.info(`${TEST_TAG} getParent  result: success.`);
113. } else {
114. console.info(`${TEST_TAG} getParent  result: fail.`);
115. }
116. if (this.rootNode!.getParent() !== undefined || this.rootNode!.getParent() !== null) {
117. console.info(`${TEST_TAG} get ArkTsNode success.`)
118. console.info(`${TEST_TAG} check rootNode whether is modifiable ${this.rootNode!.isModifiable()}`)
119. console.info(`${TEST_TAG} check getParent whether is modifiable ${this.rootNode!.getParent()!.isModifiable()}`)
120. } else {
121. console.info(`${TEST_TAG} get ArkTsNode fail.`);
122. }
123. }

125. // 将指定节点移动到根节点的第一个位置
126. moveFrameNode() {
127. const currentNode = this.frameNode!.getChild(10);
128. try {
129. currentNode!.moveTo(this.rootNode, 0);
130. if (this.rootNode!.getChild(0) === currentNode) {
131. console.info(`${TEST_TAG} moveTo  result: success.`);
132. } else {
133. console.info(`${TEST_TAG} moveTo  result: fail.`);
134. }
135. } catch (err) {
136. console.info(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
137. console.info(`${TEST_TAG} moveTo  result: fail.`);
138. }
139. }

141. getPositionToWindow() {
142. let positionToWindow = this.rootNode?.getPositionToWindow();
143. console.info(`${TEST_TAG}${JSON.stringify(positionToWindow)}`);
144. }

146. getPositionToParent() {
147. let positionToParent = this.rootNode?.getPositionToParent();
148. console.info(`${TEST_TAG}${JSON.stringify(positionToParent)}`);
149. }

151. getPositionToScreen() {
152. let positionToScreen = this.rootNode?.getPositionToScreen();
153. console.info(`${TEST_TAG}${JSON.stringify(positionToScreen)}`);
154. }

156. getGlobalPositionOnDisplay() {
157. let positionOnGlobalDisplay = this.rootNode?.getGlobalPositionOnDisplay();
158. console.info(`${TEST_TAG}${JSON.stringify(positionOnGlobalDisplay)}`);
159. }

161. getPositionToWindowWithTransform() {
162. let positionToWindowWithTransform = this.rootNode?.getPositionToWindowWithTransform();
163. console.info(`${TEST_TAG}${JSON.stringify(positionToWindowWithTransform)}`);
164. }

166. getPositionToParentWithTransform() {
167. let positionToParentWithTransform = this.rootNode?.getPositionToParentWithTransform();
168. console.info(`${TEST_TAG}${JSON.stringify(positionToParentWithTransform)}`);
169. }

171. getPositionToScreenWithTransform() {
172. let positionToScreenWithTransform = this.rootNode?.getPositionToScreenWithTransform();
173. console.info(`${TEST_TAG}${JSON.stringify(positionToScreenWithTransform)}`);
174. }

176. getMeasuredSize() {
177. let measuredSize = this.frameNode?.getMeasuredSize();
178. console.info(`${TEST_TAG}${JSON.stringify(measuredSize)}`);
179. }

181. getLayoutPosition() {
182. let layoutPosition = this.frameNode?.getLayoutPosition();
183. console.info(`${TEST_TAG}${JSON.stringify(layoutPosition)}`);
184. }

186. getUserConfigBorderWidth() {
187. let userConfigBorderWidth = this.frameNode?.getUserConfigBorderWidth();
188. console.info(`${TEST_TAG}${JSON.stringify(userConfigBorderWidth)}`);
189. }

191. getUserConfigPadding() {
192. let userConfigPadding = this.frameNode?.getUserConfigPadding();
193. console.info(`${TEST_TAG}${JSON.stringify(userConfigPadding)}`);
194. }

196. getUserConfigMargin() {
197. let userConfigMargin = this.frameNode?.getUserConfigMargin();
198. console.info(`${TEST_TAG}${JSON.stringify(userConfigMargin)}`);
199. }

201. getUserConfigSize() {
202. let userConfigSize = this.frameNode?.getUserConfigSize();
203. console.info(`${TEST_TAG}${JSON.stringify(userConfigSize)}`);
204. }

206. getId() {
207. let id = this.frameNode?.getId();
208. console.info(`${TEST_TAG}${id}`);
209. }

211. getUniqueId() {
212. let uniqueId = this.frameNode?.getUniqueId();
213. console.info(`${TEST_TAG}${uniqueId}`);
214. }

216. getNodeType() {
217. let nodeType = this.frameNode?.getNodeType();
218. console.info(`${TEST_TAG}${nodeType}`);
219. }

221. getOpacity() {
222. let opacity = this.frameNode?.getOpacity();
223. console.info(`${TEST_TAG}${JSON.stringify(opacity)}`);
224. }

226. isVisible() {
227. let visible = this.frameNode?.isVisible();
228. console.info(`${TEST_TAG}${JSON.stringify(visible)}`);
229. }

231. isClipToFrame() {
232. let clipToFrame = this.frameNode?.isClipToFrame();
233. console.info(`${TEST_TAG}${JSON.stringify(clipToFrame)}`);
234. }

236. isAttached() {
237. let attached = this.frameNode?.isAttached();
238. console.info(`${TEST_TAG}${JSON.stringify(attached)}`);
239. }

241. getInspectorInfo() {
242. let inspectorInfo = this.frameNode?.getInspectorInfo();
243. console.info(`${TEST_TAG}${JSON.stringify(inspectorInfo)}`);
244. }

246. // 设置跨语言交互选项
247. setCrossLanguageOptions() {
248. console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions)}`);
249. try {
250. this.frameNode?.setCrossLanguageOptions({
251. attributeSetting: true
252. });
253. console.info(`${TEST_TAG} setCrossLanguageOptions success.`);
254. } catch (err) {
255. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
256. console.error(`${TEST_TAG} setCrossLanguageOptions fail.`);
257. }
258. console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions)}`);
259. }

261. getInteractionEventBindingInfo() {
262. let bindingInfo = this.frameNode?.getInteractionEventBindingInfo(EventQueryType.ON_CLICK);
263. console.info(`${TEST_TAG}${bindingInfo?.baseEventRegistered}`);
264. console.info(`${TEST_TAG}${bindingInfo?.nodeEventRegistered}`);
265. console.info(`${TEST_TAG}${bindingInfo?.nativeEventRegistered}`);
266. console.info(`${TEST_TAG}${bindingInfo?.builtInEventRegistered}`);
267. console.info(`${TEST_TAG}${JSON.stringify(bindingInfo)}`);
268. }

270. throwError() {
271. try {
272. this.rootNode!.getParent()!.clearChildren();
273. } catch (err) {
274. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
275. }
276. try {
277. this.rootNode!.getParent()!.appendChild(new FrameNode(this.uiContext));
278. } catch (err) {
279. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
280. }
281. try {
282. this.rootNode!.getParent()!.removeChild(this.rootNode!.getParent()!.getChild(0));
283. } catch (err) {
284. console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
285. }
286. }
287. }

289. @Entry
290. @Component
291. struct Index {
292. private myNodeController: MyNodeController = new MyNodeController();
293. private scroller: Scroller = new Scroller();
294. @State index: number = 0;

296. build() {
297. Scroll(this.scroller) {
298. Column({ space: 8 }) {
299. Column() {
300. Row() {
301. Button("ADD")
302. .onClick(() => {
303. this.index++;
304. })
305. Button("DEC")
306. .onClick(() => {
307. this.index--;
308. })
309. }

311. // 显示当前索引值
312. Text("Current index is " + this.index)
313. .textAlign(TextAlign.Center)
314. .borderRadius(10)
315. .backgroundColor(0xFFFFFF)
316. .width('100%')
317. .fontSize(16)
318. }

320. Column() {
321. Text("This is a NodeContainer.")
322. .textAlign(TextAlign.Center)
323. .borderRadius(10)
324. .backgroundColor(0xFFFFFF)
325. .width('100%')
326. .fontSize(16)

328. // 自定义节点容器
329. NodeContainer(this.myNodeController)
330. .borderWidth(1)
331. .width(300)
332. .height(100)
333. }

335. Button("appendChild")
336. .width(300)
337. .onClick(() => {
338. this.myNodeController.appendChild();
339. })
340. Button("insertChildAfter")
341. .width(300)
342. .onClick(() => {
343. this.myNodeController.insertChildAfter(this.index);
344. })
345. Button("removeChild")
346. .width(300)
347. .onClick(() => {
348. this.myNodeController.removeChild(this.index);
349. })
350. Button("clearChildren")
351. .width(300)
352. .onClick(() => {
353. this.myNodeController.clearChildren();
354. })
355. Button("getChildNumber")
356. .width(300)
357. .onClick(() => {
358. this.myNodeController.getChildNumber();
359. })
360. Button("searchFrameNode")
361. .width(300)
362. .onClick(() => {
363. this.myNodeController.searchFrameNode();
364. })
365. Button("moveFrameNode")
366. .width(300)
367. .onClick(() => {
368. this.myNodeController.moveFrameNode();
369. })
370. Button("getPositionToWindow")
371. .width(300)
372. .onClick(() => {
373. this.myNodeController.getPositionToWindow();
374. })
375. Button("getPositionToParent")
376. .width(300)
377. .onClick(() => {
378. this.myNodeController.getPositionToParent();
379. })
380. Button("getPositionToScreen")
381. .width(300)
382. .onClick(() => {
383. this.myNodeController.getPositionToScreen();
384. })
385. Button("getGlobalPositionOnDisplay")
386. .width(300)
387. .onClick(() => {
388. this.myNodeController.getGlobalPositionOnDisplay();
389. })
390. Button("getPositionToParentWithTransform")
391. .width(300)
392. .onClick(() => {
393. this.myNodeController.getPositionToParentWithTransform();
394. })
395. Button("getPositionToWindowWithTransform")
396. .width(300)
397. .onClick(() => {
398. this.myNodeController.getPositionToWindowWithTransform();
399. })
400. Button("getPositionToScreenWithTransform")
401. .width(300)
402. .onClick(() => {
403. this.myNodeController.getPositionToScreenWithTransform();
404. })
405. Button("getMeasuredSize")
406. .width(300)
407. .onClick(() => {
408. this.myNodeController.getMeasuredSize();
409. })
410. Button("getLayoutPosition")
411. .width(300)
412. .onClick(() => {
413. this.myNodeController.getLayoutPosition();
414. })
415. Button("getUserConfigBorderWidth")
416. .width(300)
417. .onClick(() => {
418. this.myNodeController.getUserConfigBorderWidth();
419. })
420. Button("getUserConfigPadding")
421. .width(300)
422. .onClick(() => {
423. this.myNodeController.getUserConfigPadding();
424. })
425. Button("getUserConfigMargin")
426. .width(300)
427. .onClick(() => {
428. this.myNodeController.getUserConfigMargin();
429. })
430. Button("getUserConfigSize")
431. .width(300)
432. .onClick(() => {
433. this.myNodeController.getUserConfigSize();
434. })
435. Button("getId")
436. .width(300)
437. .onClick(() => {
438. this.myNodeController.getId();
439. })
440. Button("getUniqueId")
441. .width(300)
442. .onClick(() => {
443. this.myNodeController.getUniqueId();
444. })
445. Button("getNodeType")
446. .width(300)
447. .onClick(() => {
448. this.myNodeController.getNodeType();
449. })
450. Button("getOpacity")
451. .width(300)
452. .onClick(() => {
453. this.myNodeController.getOpacity();
454. })
455. Button("isVisible")
456. .width(300)
457. .onClick(() => {
458. this.myNodeController.isVisible();
459. })
460. Button("isClipToFrame")
461. .width(300)
462. .onClick(() => {
463. this.myNodeController.isClipToFrame();
464. })
465. Button("isAttached")
466. .width(300)
467. .onClick(() => {
468. this.myNodeController.isAttached();
469. })
470. Button("getInspectorInfo")
471. .width(300)
472. .onClick(() => {
473. this.myNodeController.getInspectorInfo();
474. })
475. Button("getCustomProperty")
476. .width(300)
477. .onClick(() => {
478. const uiContext: UIContext = this.getUIContext();
479. if (uiContext) {
480. // 通过组件ID获取对应的FrameNode节点
481. const node: FrameNode | null = uiContext.getFrameNodeById("Test_Button") || null;
482. if (node) {
483. for (let i = 1; i < 4; i++) {
484. const key = 'customProperty' + i;
485. const property = node.getCustomProperty(key);
486. console.info(`${TEST_TAG}${key}`, JSON.stringify(property));
487. }
488. }
489. }
490. })
491. .id('Test_Button')
492. .customProperty('customProperty1', {
493. 'number': 10,
494. 'string': 'this is a string',
495. 'bool': true,
496. 'object': {
497. 'name': 'name',
498. 'value': 100
499. }
500. })
501. .customProperty('customProperty2', {})
502. .customProperty('customProperty2', undefined)
503. Button("setCrossLanguageOptions")
504. .width(300)
505. .onClick(() => {
506. this.myNodeController.setCrossLanguageOptions();
507. })
508. Button("getInteractionEventBindingInfo")
509. .width(300)
510. .onClick(() => {
511. this.myNodeController.getInteractionEventBindingInfo();
512. })
513. Button("throwError")
514. .width(300)
515. .onClick(() => {
516. this.myNodeController.throwError();
517. })
518. }
519. .width("100%")
520. }
521. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
522. }
523. }
```

## LazyForEach场景节点操作示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode, UIContext, BuilderNode, ExpandMode, LengthUnit } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode "

5. // BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: string[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): string {
15. return this.originDataArray[index];
16. }

18. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
19. registerDataChangeListener(listener: DataChangeListener): void {
20. if (this.listeners.indexOf(listener) < 0) {
21. console.info('add listener');
22. this.listeners.push(listener);
23. }
24. }

26. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
27. unregisterDataChangeListener(listener: DataChangeListener): void {
28. const pos = this.listeners.indexOf(listener);
29. if (pos >= 0) {
30. console.info('remove listener');
31. this.listeners.splice(pos, 1);
32. }
33. }

35. // 通知LazyForEach组件需要重载所有子组件
36. notifyDataReload(): void {
37. this.listeners.forEach(listener => {
38. listener.onDataReloaded();
39. })
40. }

42. // 通知LazyForEach组件需要在index对应索引处添加子组件
43. notifyDataAdd(index: number): void {
44. this.listeners.forEach(listener => {
45. listener.onDataAdd(index);
46. // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
47. })
48. }

50. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
51. notifyDataChange(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataChange(index);
54. // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
55. })
56. }

58. // 通知LazyForEach组件需要在index对应索引处删除该子组件
59. notifyDataDelete(index: number): void {
60. this.listeners.forEach(listener => {
61. listener.onDataDelete(index);
62. // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
63. })
64. }

66. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
67. notifyDataMove(from: number, to: number): void {
68. this.listeners.forEach(listener => {
69. listener.onDataMove(from, to);
70. // 写法2：listener.onDatasetChange([{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
71. })
72. }

74. notifyDatasetChange(operations: DataOperation[]): void {
75. this.listeners.forEach(listener => {
76. listener.onDatasetChange(operations);
77. })
78. }
79. }

81. // 自定义数据管理类管理string数组
82. class MyDataSource extends BasicDataSource {
83. private dataArray: string[] = []

85. public totalCount(): number {
86. return this.dataArray.length;
87. }

89. public getData(index: number): string {
90. return this.dataArray[index];
91. }

93. public addData(index: number, data: string): void {
94. this.dataArray.splice(index, 0, data);
95. this.notifyDataAdd(index);
96. }

98. public pushData(data: string): void {
99. this.dataArray.push(data);
100. this.notifyDataAdd(this.dataArray.length - 1);
101. }
102. }

104. class Params {
105. data: MyDataSource | null = null;
106. scroller: Scroller | null = null;

108. constructor(data: MyDataSource, scroller: Scroller) {
109. this.data = data;
110. this.scroller = scroller;
111. }
112. }

114. @Builder
115. function buildData(params: Params) {
116. List({ scroller: params.scroller }) {
117. LazyForEach(params.data, (item: string) => {
118. ListItem() {
119. Column() {
120. Text(item)
121. .fontSize(20)
122. .onAppear(() => {
123. console.info(`${TEST_TAG} node appear: ${item}`)
124. })
125. .backgroundColor(Color.Pink)
126. .margin({
127. top: 30,
128. bottom: 30,
129. left: 10,
130. right: 10
131. })
132. }
133. }
134. .id(item)
135. }, (item: string) => item)
136. }
137. .cachedCount(5)
138. .listDirection(Axis.Horizontal)
139. }

141. // 继承NodeController实现自定义UI控制器
142. class MyNodeController extends NodeController {
143. private rootNode: FrameNode | null = null;
144. private uiContext: UIContext | null = null;
145. private data: MyDataSource = new MyDataSource();
146. private scroller: Scroller = new Scroller();

148. makeNode(uiContext: UIContext): FrameNode | null {
149. this.uiContext = uiContext;
150. for (let i = 0; i <= 20; i++) {
151. this.data.pushData(`N${i}`);
152. }
153. const params: Params = new Params(this.data, this.scroller);
154. const dataNode: BuilderNode<[Params]> = new BuilderNode(uiContext);
155. dataNode.build(wrapBuilder<[Params]>(buildData), params);
156. this.rootNode = dataNode.getFrameNode();
157. const scrollToIndexOptions: ScrollToIndexOptions = {
158. extraOffset: {
159. value: 20, unit: LengthUnit.VP
160. }
161. };
162. this.scroller.scrollToIndex(6, true, ScrollAlign.START, scrollToIndexOptions);
163. return this.rootNode;
164. }

166. getFirstChildIndexWithoutExpand() {
167. console.info(`${TEST_TAG} getFirstChildIndexWithoutExpand: ${this.rootNode!.getFirstChildIndexWithoutExpand()}`);
168. }

170. getLastChildIndexWithoutExpand() {
171. console.info(`${TEST_TAG} getLastChildIndexWithoutExpand: ${this.rootNode!.getLastChildIndexWithoutExpand()}`);
172. }

174. getChildWithNotExpand() {
175. const childNode = this.rootNode!.getChild(3, ExpandMode.NOT_EXPAND);
176. console.info(`${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND): ${childNode!.getId()}`);
177. if (childNode!.getId() === "N9") {
178. console.info(`${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND)  result: success.`);
179. } else {
180. console.info(`${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND)  result: fail.`);
181. }
182. }

184. getChildWithExpand() {
185. const childNode = this.rootNode!.getChild(3, ExpandMode.EXPAND);
186. console.info(`${TEST_TAG} getChild(3, ExpandMode.EXPAND): ${childNode!.getId()}`);
187. if (childNode!.getId() === "N3") {
188. console.info(`${TEST_TAG} getChild(3, ExpandMode.EXPAND)  result: success.`);
189. } else {
190. console.info(`${TEST_TAG} getChild(3, ExpandMode.EXPAND)  result: fail.`);
191. }
192. }

194. getChildWithLazyExpand() {
195. const childNode = this.rootNode!.getChild(3, ExpandMode.LAZY_EXPAND);
196. console.info(`${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND): ${childNode!.getId()}`);
197. if (childNode!.getId() === "N3") {
198. console.info(`${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND)  result: success.`);
199. } else {
200. console.info(`${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND)  result: fail.`);
201. }
202. }
203. }

205. @Entry
206. @Component
207. struct Index {
208. private myNodeController: MyNodeController = new MyNodeController();
209. private scroller: Scroller = new Scroller();

211. build() {
212. Scroll(this.scroller) {
213. Column({ space: 8 }) {
214. Column() {
215. Text("This is a NodeContainer.")
216. .textAlign(TextAlign.Center)
217. .borderRadius(10)
218. .backgroundColor(0xFFFFFF)
219. .width('100%')
220. .fontSize(16)
221. NodeContainer(this.myNodeController)
222. .borderWidth(1)
223. .width(300)
224. .height(100)
225. }

227. Button("getFirstChildIndexWithoutExpand")
228. .width(300)
229. .onClick(() => {
230. this.myNodeController.getFirstChildIndexWithoutExpand();
231. })
232. Button("getLastChildIndexWithoutExpand")
233. .width(300)
234. .onClick(() => {
235. this.myNodeController.getLastChildIndexWithoutExpand();
236. })
237. Button("getChildWithNotExpand")
238. .width(300)
239. .onClick(() => {
240. this.myNodeController.getChildWithNotExpand();
241. })
242. Button("getChildWithExpand")
243. .width(300)
244. .onClick(() => {
245. this.myNodeController.getChildWithExpand();
246. })
247. Button("getChildWithLazyExpand")
248. .width(300)
249. .onClick(() => {
250. this.myNodeController.getChildWithLazyExpand();
251. })
252. }
253. .width("100%")
254. }
255. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
256. }
257. }
```

## 基础事件示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. public rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);
9. this.rootNode.commonAttribute.width(100)
10. .height(100)
11. .backgroundColor(Color.Pink);
12. this.addCommonEvent(this.rootNode);
13. return this.rootNode;
14. }

16. // 为FrameNode绑定交互事件
17. addCommonEvent(frameNode: FrameNode) {

19. // 悬浮事件
20. frameNode.commonEvent.setOnHover(((isHover: boolean, event: HoverEvent): void => {
21. console.info(`isHover FrameNode: ${isHover}`);
22. console.info(`isHover FrameNode: ${JSON.stringify(event)}`);
23. event.stopPropagation();
24. }))

26. // 点击事件
27. frameNode.commonEvent.setOnClick((event: ClickEvent) => {
28. console.info(`Click FrameNode: ${JSON.stringify(event)}`)
29. })

31. // 触摸事件
32. frameNode.commonEvent.setOnTouch((event: TouchEvent) => {
33. console.info(`touch FrameNode: ${JSON.stringify(event)}`)
34. })

36. // 显示事件
37. frameNode.commonEvent.setOnAppear(() => {
38. console.info(`on Appear FrameNode`)
39. })

41. // 消失事件
42. frameNode.commonEvent.setOnDisappear(() => {
43. console.info(`onDisAppear FrameNode`)
44. })

46. // 获焦事件
47. frameNode.commonEvent.setOnFocus(() => {
48. console.info(`onFocus FrameNode`)
49. })

51. // 失焦事件
52. frameNode.commonEvent.setOnBlur(() => {
53. console.info(`onBlur FrameNode`)
54. })

56. // 键盘事件
57. frameNode.commonEvent.setOnKeyEvent((event: KeyEvent) => {
58. console.info(`Key FrameNode: ${JSON.stringify(event)}`)
59. })

61. // 鼠标事件
62. frameNode.commonEvent.setOnMouse((event: MouseEvent) => {
63. console.info(`Mouse FrameNode: ${JSON.stringify(event)}`)
64. })

66. // 组件区域变化事件
67. frameNode.commonEvent.setOnSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
68. console.info(`onSizeChange FrameNode: oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`)
69. })
70. }
71. }

73. @Entry
74. @Component
75. struct Index {
76. private myNodeController: MyNodeController = new MyNodeController();

78. build() {
79. Column() {
80. Button("add CommonEvent to Text")
81. .onClick(() => {
82. this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling() !)
83. })
84. Text("this is a Text")
85. .fontSize(16)
86. .borderWidth(1)
87. .onHover(((isHover: boolean, event: HoverEvent): void => {
88. console.info(`isHover Text: ${isHover}`);
89. console.info(`isHover Text: ${JSON.stringify(event)}`);
90. event.stopPropagation();  // 阻止事件冒泡
91. }))
92. .onClick((event: ClickEvent) => {
93. console.info(`Click Text    : ${JSON.stringify(event)}`)
94. })
95. .onTouch((event: TouchEvent) => {
96. console.info(`touch Text    : ${JSON.stringify(event)}`)
97. })
98. .onAppear(() => {
99. console.info(`on Appear Text`)
100. })
101. .onDisAppear(() => {
102. console.info(`onDisAppear Text`)
103. })
104. .onFocus(() => {
105. console.info(`onFocus Text`)
106. })
107. .onBlur(() => {
108. console.info(`onBlur Text`)
109. })
110. .onKeyEvent((event: KeyEvent) => {
111. console.info(`Key Text    : ${JSON.stringify(event)}`)
112. })
113. .onMouse((event: MouseEvent) => {
114. console.info(`Mouse Text : ${JSON.stringify(event)}`)
115. })
116. .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
117. console.info(`onSizeChange Text: oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`)
118. })
119. NodeContainer(this.myNodeController)
120. .borderWidth(1)
121. .width(300)
122. .height(100)
123. }.width("100%")
124. }
125. }
```

## LazyForEach场景基础事件使用示例

PhonePC/2in1TabletTVWearable

```
1. // index.ets
2. import {Track, TrackManager, TrackNode} from "./track"

4. @Builder
5. function page1() {
6. Column() {
7. Text("Page1")
8. PageList().height("90%")
9. Button("DumpMessage")
10. .onClick(() => {
11. TrackManager.get().dump()
12. })

14. }.width("100%").height("100%")
15. }

17. class BasicDataSource implements IDataSource {
18. private listeners: DataChangeListener[] = [];
19. private originDataArray: string[] = [];

21. public totalCount(): number {
22. return 0;
23. }

25. public getData(index: number): string {
26. return this.originDataArray[index];
27. }

29. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
30. registerDataChangeListener(listener: DataChangeListener): void {
31. if (this.listeners.indexOf(listener) < 0) {
32. console.info('add listener');
33. this.listeners.push(listener);
34. }
35. }

37. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
38. unregisterDataChangeListener(listener: DataChangeListener): void {
39. const pos = this.listeners.indexOf(listener);
40. if (pos >= 0) {
41. console.info('remove listener');
42. this.listeners.splice(pos, 1);
43. }
44. }

46. // 通知LazyForEach组件需要重载所有子组件
47. notifyDataReload(): void {
48. this.listeners.forEach(listener => {
49. listener.onDataReloaded();
50. })
51. }

53. // 通知LazyForEach组件需要在index对应索引处添加子组件
54. notifyDataAdd(index: number): void {
55. this.listeners.forEach(listener => {
56. listener.onDataAdd(index);
57. })
58. }

60. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
61. notifyDataChange(index: number): void {
62. this.listeners.forEach(listener => {
63. listener.onDataChange(index);
64. })
65. }

67. // 通知LazyForEach组件需要在index对应索引处删除该子组件
68. notifyDataDelete(index: number): void {
69. this.listeners.forEach(listener => {
70. listener.onDataDelete(index);
71. })
72. }

74. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
75. notifyDataMove(from: number, to: number): void {
76. this.listeners.forEach(listener => {
77. listener.onDataMove(from, to);
78. })
79. }
80. }

82. // 自定义数据管理类管理string数组
83. class MyDataSource extends BasicDataSource {
84. private dataArray: string[] = [];

86. public totalCount(): number {
87. return this.dataArray.length;
88. }

90. public getData(index: number): string {
91. return this.dataArray[index];
92. }

94. public addData(index: number, data: string): void {
95. this.dataArray.splice(index, 0, data);
96. this.notifyDataAdd(index);
97. }

99. public pushData(data: string): void {
100. this.dataArray.push(data);
101. this.notifyDataAdd(this.dataArray.length - 1);
102. }
103. }

105. @Component
106. struct PageList {
107. private data: MyDataSource = new MyDataSource();

109. aboutToAppear() {
110. for (let i = 0; i <= 100; i++) {
111. this.data.pushData(`Hello ${i}`)
112. }
113. }

115. build() {
116. List({ space: 3 }) {
117. LazyForEach(this.data, (item: string, index: number) => {
118. ListItem() {
119. // 通过TrackNode对组件进行封装埋点
120. TrackNode({track: new Track().tag("xxx"+ item).id(index + 30000)}) {
121. Row() {
122. Text(item).fontSize(30)
123. .onClick(() => {
124. })
125. }.margin({ left: 10, right: 10 })
126. }
127. }
128. }, (item: string) => item)
129. }.cachedCount(5)
130. }
131. }

134. @Entry
135. @Component
136. struct TrackTest {
137. pageInfos: NavPathStack = new NavPathStack()
138. build() {
139. Row() {
140. TrackNode({ track: new Track().tag("root").id(10000)}) {
141. page1()
142. }
143. }
144. }

146. aboutToAppear(): void {
147. TrackManager.get().startListenClick(this.getUIContext())
148. }
149. }
```

```
1. // ./track.ets
2. import { FrameNode, Rect } from '@kit.ArkUI';

4. @Component
5. export struct TrackNode {
6. @BuilderParam closer: VoidCallback = this.defaultBuilder
7. track: Track | null = null
8. trackShadow: TrackShadow = new TrackShadow()

10. @Builder defaultBuilder() {
11. }

13. build() {
14. this.closer()
15. }

17. aboutToAppear(): void {
18. // 稍后使用onDidBuild
19. }

21. aboutToDisappear(): void {
22. TrackManager.get().removeTrack(this.trackShadow.id)
23. console.info(`Track disappear:${this.trackShadow.id}`)
24. }

26. onDidBuild(): void {
27. // 构建埋点的虚拟树，获取的node为当前页面的根节点（用例中为Row）
28. let uid = this.getUniqueId()
29. let node: FrameNode | null = this.getUIContext().getFrameNodeByUniqueId(uid);
30. console.info(`Track onDidBuild node:${node?.getNodeType()}`);
31. if (node === null) {
32. return
33. }
34. this.trackShadow.node = node
35. this.trackShadow.id = node?.getUniqueId()
36. this.trackShadow.track = this.track;
37. TrackManager.get().addTrack(this.trackShadow.id, this.trackShadow)
38. // 通过setOnVisibleAreaApproximateChange监听记录埋点组件的可视区域
39. node?.commonEvent.setOnVisibleAreaApproximateChange(
40. { ratios: [0, 0.1, 0.2, 0.5, 0.8, 1], expectedUpdateInterval: 500 },
41. (ratioInc: boolean, ratio: number) => {
42. console.info(`Node ${node?.getUniqueId()}:${node?.getNodeType()} is visibleRatio is ${ratio}`);
43. this.trackShadow.visibleRatio = ratio
44. })

46. let parent: FrameNode | null = node?.getParent()

48. let attachTrackToParent: (parent: FrameNode | null) => boolean =
49. (parent: FrameNode | null) => {
50. while (parent !== null) {
51. let parentTrack = TrackManager.get().getTrackById(parent.getUniqueId())
52. if (parentTrack !== undefined) {
53. parentTrack.childIds.add(this.trackShadow.id)
54. this.trackShadow.parentId = parentTrack.id
55. return true;
56. }
57. parent = parent.getParent()
58. }
59. return false;
60. }
61. let attached = attachTrackToParent(parent);

63. if (!attached) {
64. node?.commonEvent.setOnAppear(() => {
65. let attached = attachTrackToParent(parent);
66. if (attached) {
67. console.info(`Track lazy attached:${this.trackShadow.id}`)
68. }
69. })
70. }
71. }
72. }

74. export class Track {
75. public areaPercent: number = 0
76. private trackTag: string = ""
77. private trackId: number = 0

79. constructor() {
80. }

82. tag(newTag: string): Track {
83. this.trackTag = newTag;
84. return this;
85. }

87. id(newId: number): Track {
88. this.trackId = newId;
89. return this;
90. }
91. }

93. export class TrackShadow {
94. public node: FrameNode | null = null
95. public id: number = -1
96. public track: Track | null = null
97. public childIds: Set<number> = new Set()
98. public parentId: number = -1
99. public visibleRect: Rect = { left: 0, top: 0, right: 0, bottom: 0 }
100. public area: number = 0
101. public visibleRatio: number = 0

103. // 通过全局dump输出埋点树的信息
104. dump(depth: number = 0): void {
105. console.info(`Track DP:${depth} id:${this.id} areaPer:${this.track?.areaPercent} visibleRatio:${this.visibleRatio}`)
106. this.childIds.forEach((value: number) => {
107. TrackManager.get().getTrackById(value)?.dump(depth + 1)
108. })
109. }
110. }

112. export class TrackManager {
113. static instance: TrackManager
114. private trackMap: Map<number, TrackShadow> = new Map()
115. private rootTrack: TrackShadow | null = null

117. static get(): TrackManager {
118. if (TrackManager.instance !== undefined) {
119. return TrackManager.instance
120. }
121. TrackManager.instance = new TrackManager()
122. return TrackManager.instance
123. }

125. addTrack(id: number, track: TrackShadow) {
126. if (this.trackMap.size == 0) {
127. this.rootTrack = track
128. }
129. console.info(`Track add id:${id}`)
130. this.trackMap.set(id, track)
131. }

133. removeTrack(id: number) {
134. let current = this.getTrackById(id)
135. if (current !== undefined) {
136. this.trackMap.delete(id)
137. let parent = this.getTrackById(current?.parentId)
138. parent?.childIds.delete(id)
139. }
140. }

142. getTrackById(id: number): TrackShadow | undefined {
143. return this.trackMap.get(id)
144. }

146. startListenClick(context: UIContext) {
147. // 通过无感监听获取FrameNode查找埋点信息
148. context.getUIObserver().on("willClick", (event: ClickEvent, node?: FrameNode) => {
149. console.info(`Track clicked:${node}`)
150. if (node == undefined) {
151. return
152. }
153. let track = this.getTrackById(node.getUniqueId())
154. track?.dump(0);
155. })
156. }

158. updateVisibleInfo(track: TrackShadow): void {
159. // 更新埋点信息
160. }

162. dump(): void {
163. this.rootTrack?.dump(0)
164. }
165. }
```

## 手势事件示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. public rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);
9. this.rootNode.commonAttribute.width(100)
10. .overlay('This is a FrameNode')
11. .backgroundColor(Color.Pink)
12. .width('100%')
13. .height('100%');
14. this.addGestureEvent(this.rootNode);
15. return this.rootNode;
16. }

18. addGestureEvent(frameNode: FrameNode) {
19. frameNode.gestureEvent.addGesture(new PanGestureHandler()
20. .onActionStart((event: GestureEvent) => {
21. console.info(`Pan start: ${JSON.stringify(event)}`);
22. })
23. .onActionUpdate((event: GestureEvent) => {
24. console.info(`Pan update: ${JSON.stringify(event)}`);
25. })
26. .onActionEnd((event: GestureEvent) => {
27. console.info(`Pan end: ${JSON.stringify(event)}`);
28. })
29. .onActionCancel(() => {
30. console.info('Pan cancel');
31. })
32. )
33. frameNode.gestureEvent.addGesture(new LongPressGestureHandler()
34. .onAction((event: GestureEvent) => {
35. console.info(`Long press action: ${JSON.stringify(event)}`);
36. })
37. .onActionEnd((event: GestureEvent) => {
38. console.info(`Long press action end: ${JSON.stringify(event)}`);
39. })
40. .onActionCancel(() => {
41. console.info('Long press cancel');
42. })
43. )
44. frameNode.gestureEvent.addGesture(new TapGestureHandler()
45. .onAction((event: GestureEvent) => {
46. console.info(`Tap action: ${JSON.stringify(event)}`);
47. })
48. )
49. }
50. }

52. @Entry
53. @Component
54. struct Index {
55. private myNodeController: MyNodeController = new MyNodeController();

57. build() {
58. Column() {
59. NodeContainer(this.myNodeController)
60. .borderWidth(1)
61. .width(300)
62. .height(300)
63. }.width("100%")
64. }
65. }
```

## 节点自定义示例

PhonePC/2in1TabletTVWearable

```
1. import { UIContext, DrawContext, FrameNode, NodeController, LayoutConstraint, Size, Position } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. function GetChildLayoutConstraint(constraint: LayoutConstraint, child: FrameNode): LayoutConstraint {
5. const size = child.getUserConfigSize();
6. const width = Math.max(
7. Math.min(constraint.maxSize.width, size.width.value),
8. constraint.minSize.width
9. );
10. const height = Math.max(
11. Math.min(constraint.maxSize.height, size.height.value),
12. constraint.minSize.height
13. );
14. const finalSize: Size = { width, height };
15. const res: LayoutConstraint = {
16. maxSize: finalSize,
17. minSize: finalSize,
18. percentReference: finalSize
19. };

21. return res;
22. }

24. // 自定义FrameNode实现自定义布局函数
25. class MyFrameNode extends FrameNode {
26. public width: number = 10;
27. private space: number = 1;

29. onMeasure(constraint: LayoutConstraint): void {
30. let sizeRes: Size = { width: 100, height: 100 };
31. for (let i = 0; i < this.getChildrenCount(); i++) {
32. let child = this.getChild(i);
33. if (child) {
34. let childConstraint = GetChildLayoutConstraint(constraint, child);
35. child.measure(childConstraint);
36. let size = child.getMeasuredSize();
37. sizeRes.height += size.height + this.space;
38. sizeRes.width = Math.max(sizeRes.width, size.width);
39. }
40. }
41. this.setMeasuredSize(sizeRes);
42. }

44. onLayout(position: Position): void {
45. let y = 0;
46. for (let i = 0; i < this.getChildrenCount(); i++) {
47. let child = this.getChild(i);
48. if (child) {
49. child.layout({
50. x: 20,
51. y: y
52. });
53. y += child.getMeasuredSize().height + this.space;
54. }
55. }
56. this.setLayoutPosition(position);
57. }

59. onDraw(context: DrawContext) {
60. const canvas = context.canvas;
61. const pen = new drawing.Pen();
62. pen.setStrokeWidth(5);
63. pen.setColor({
64. alpha: 255,
65. red: 255,
66. green: 0,
67. blue: 0
68. });
69. canvas.attachPen(pen);
70. canvas.drawRect({
71. left: 0,
72. right: this.width,
73. top: 0,
74. bottom: this.width
75. });
76. canvas.detachPen();
77. }

79. addWidth() {
80. this.width += 10;
81. }
82. }

84. // 继承NodeController实现自定义UI控制器
85. class MyNodeController extends NodeController {
86. public rootNode: MyFrameNode | null = null;

88. makeNode(context: UIContext): FrameNode | null {
89. this.rootNode = new MyFrameNode(context);
90. this.rootNode?.commonAttribute?.size({ width: 100, height: 100 }).backgroundColor(Color.Green);
91. return this.rootNode;
92. }
93. }

95. @Entry
96. @Component
97. struct Index {
98. private nodeController: MyNodeController = new MyNodeController();

100. build() {
101. Row() {
102. Column() {
103. NodeContainer(this.nodeController)
104. .width('100%')
105. .height(100)
106. .backgroundColor('#FFF0F0F0')
107. Button('Invalidate')
108. .onClick(() => {
109. this.nodeController?.rootNode?.addWidth();
110. this.nodeController?.rootNode?.invalidate();
111. })
112. Button('UpdateLayout')
113. .onClick(() => {
114. this.nodeController?.rootNode?.setNeedsLayout();
115. })
116. }
117. .width('100%')
118. .height('100%')
119. }
120. .height('100%')
121. }
122. }
```

## NodeAdapter使用示例

PhonePC/2in1TabletTVWearable

```
1. import { FrameNode, NodeController, NodeAdapter, typeNode } from '@kit.ArkUI';

3. // 自定义NodeAdapter管理数据
4. class MyNodeAdapter extends NodeAdapter {
5. uiContext: UIContext
6. cachePool: Array<FrameNode> = new Array();
7. changed: boolean = false
8. reloadTimes: number = 0;
9. data: Array<string> = new Array();
10. hostNode?: FrameNode

12. constructor(uiContext: UIContext, count: number) {
13. super();
14. this.uiContext = uiContext;
15. this.totalNodeCount = count;
16. this.loadData();
17. }

19. reloadData(count: number): void {
20. this.reloadTimes++;
21. NodeAdapter.attachNodeAdapter(this, this.hostNode);
22. this.totalNodeCount = count;
23. this.loadData();
24. this.reloadAllItems();
25. }

27. refreshData(): void {
28. let items = this.getAllAvailableItems()
29. console.info(`UINodeAdapter get All items:${items.length}`);
30. this.reloadAllItems();
31. }

33. detachData(): void {
34. NodeAdapter.detachNodeAdapter(this.hostNode);
35. this.reloadTimes = 0;
36. }

38. loadData(): void {
39. for (let i = 0; i < this.totalNodeCount; i++) {
40. this.data[i] = "Adapter ListItem " + i + " r:" + this.reloadTimes;
41. }
42. }

44. changeData(from: number, count: number): void {
45. this.changed = !this.changed;
46. for (let i = 0; i < count; i++) {
47. let index = i + from;
48. this.data[index] = "Adapter ListItem " + (this.changed ? "changed:" : "") + index + " r:" + this.reloadTimes;
49. }
50. this.reloadItem(from, count);
51. }

53. insertData(from: number, count: number): void {
54. for (let i = 0; i < count; i++) {
55. let index = i + from;
56. this.data.splice(index, 0, "Adapter ListItem " + from + "-" + i);
57. }
58. this.insertItem(from, count);
59. this.totalNodeCount += count;
60. console.info(`UINodeAdapter after insert count:${this.totalNodeCount}`);
61. }

63. removeData(from: number, count: number): void {
64. let arr = this.data.splice(from, count);
65. this.removeItem(from, count);
66. this.totalNodeCount -= arr.length;
67. console.info(`UINodeAdapter after remove count:${this.totalNodeCount}`);
68. }

70. moveData(from: number, to: number): void {
71. let tmp = this.data.splice(from, 1);
72. this.data.splice(to, 0, tmp[0]);
73. this.moveItem(from, to);
74. }

76. onAttachToNode(target: FrameNode): void {
77. console.info(`UINodeAdapter onAttachToNode id:${target.getUniqueId()}`);
78. this.hostNode = target;
79. }

81. onDetachFromNode(): void {
82. console.info("UINodeAdapter onDetachFromNode");
83. }

85. onGetChildId(index: number): number {
86. console.info(`UINodeAdapter onGetChildId:${index}`);
87. return index;
88. }

90. onCreateChild(index: number): FrameNode {
91. console.info(`UINodeAdapter onCreateChild:${index}`);
92. if (this.cachePool.length > 0) {
93. let cacheNode = this.cachePool.pop();
94. if (cacheNode !== undefined) {
95. console.info(`UINodeAdapter onCreateChild reused id:${cacheNode.getUniqueId()}`);
96. let text = cacheNode?.getFirstChild();
97. let textNode = text as typeNode.Text;
98. textNode?.initialize(this.data[index]).fontSize(20);
99. return cacheNode;
100. }
101. }
102. console.info("UINodeAdapter onCreateChild createNew");
103. let itemNode = typeNode.createNode(this.uiContext, "ListItem");
104. let textNode = typeNode.createNode(this.uiContext, "Text");
105. textNode.initialize(this.data[index]).fontSize(20);
106. itemNode.appendChild(textNode);
107. return itemNode;
108. }

110. onDisposeChild(id: number, node: FrameNode): void {
111. console.info(`UINodeAdapter onDisposeChild:${id}`);
112. if (this.cachePool.length < 10) {
113. if (!this.cachePool.includes(node)) {
114. console.info(`UINodeAdapter caching node id:${node.getUniqueId()}`);
115. this.cachePool.push(node);
116. }
117. } else {
118. node.dispose();
119. }
120. }

122. onUpdateChild(id: number, node: FrameNode): void {
123. let index = id;
124. let text = node.getFirstChild();
125. let textNode = text as typeNode.Text;
126. textNode?.initialize(this.data[index]).fontSize(20);
127. }
128. }

130. // 继承NodeController实现自定义NodeAdapter控制器
131. class MyNodeAdapterController extends NodeController {
132. rootNode: FrameNode | null = null;
133. nodeAdapter: MyNodeAdapter | null = null;

135. makeNode(uiContext: UIContext): FrameNode | null {
136. this.rootNode = new FrameNode(uiContext);
137. let listNode = typeNode.createNode(uiContext, "List");
138. listNode.initialize({ space: 3 }).borderWidth(2).borderColor(Color.Black);
139. this.rootNode.appendChild(listNode);
140. this.nodeAdapter = new MyNodeAdapter(uiContext, 100);
141. NodeAdapter.attachNodeAdapter(this.nodeAdapter, listNode);
142. return this.rootNode;
143. }
144. }

146. @Entry
147. @Component
148. struct ListNodeTest {
149. adapterController: MyNodeAdapterController = new MyNodeAdapterController();

151. build() {
152. Column() {
153. Text("ListNode Adapter");
154. NodeContainer(this.adapterController)
155. .width(300).height(300)
156. .borderWidth(1).borderColor(Color.Black);
157. Row() {
158. Button("Reload")
159. .onClick(() => {
160. this.adapterController.nodeAdapter?.reloadData(50);
161. })
162. Button("Change")
163. .onClick(() => {
164. this.adapterController.nodeAdapter?.changeData(5, 10)
165. })
166. Button("Insert")
167. .onClick(() => {
168. this.adapterController.nodeAdapter?.insertData(10, 10);
169. })
170. }

172. Row() {
173. Button("Remove")
174. .onClick(() => {
175. this.adapterController.nodeAdapter?.removeData(10, 10);
176. })
177. Button("Move")
178. .onClick(() => {
179. this.adapterController.nodeAdapter?.moveData(2, 5);
180. })
181. Button("Refresh")
182. .onClick(() => {
183. this.adapterController.nodeAdapter?.refreshData();
184. })
185. Button("Detach")
186. .onClick(() => {
187. this.adapterController.nodeAdapter?.detachData();
188. })
189. }
190. }.borderWidth(1)
191. .width("100%")
192. }
193. }
```

## 节点复用回收使用示例

PhonePC/2in1TabletTVWearable

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

18. // 继承NodeController实现自定义UI控制器
19. class MyNodeController extends NodeController {
20. private buttonNode: BuilderNode<[Params]> | null = null;
21. private rootNode: FrameNode | null = null;
22. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

24. makeNode(uiContext: UIContext): FrameNode {
25. if (this.rootNode == null) {
26. this.rootNode = new FrameNode(uiContext);
27. this.buttonNode = new BuilderNode(uiContext);
28. this.buttonNode.build(this.wrapBuilder, { text: "This is a Button" });
29. this.rootNode.appendChild(this.buttonNode.getFrameNode());
30. }
31. return this.rootNode;
32. }

34. onAttach(): void {
35. console.info("myButton on attach");
36. }

38. onDetach(): void {
39. console.info("myButton on detach");
40. }

42. // onBind时，子节点已经重新上树，此时调用reuse，保证子组件的能重新被复用
43. onBind(containerId: number): void {
44. // 该方法触发子组件复用，全局复用场景下，复用FrameNode后端资源
45. this.rootNode?.reuse();
46. console.info("myButton reuse");
47. }

49. // onUnbind时，子节点已经完全下树，此时调用recycle，保证子组件的能完全被回收
50. onUnbind(containerId: number): void {
51. // 该方法触发子组件的回收，全局复用场景下，回收FrameNode后端资源用于重新利用
52. this.rootNode?.recycle();
53. console.info("myButton recycle");
54. }

56. getButtonNode(): BuilderNode<[Params]> | null {
57. return this.buttonNode;
58. }

60. getFrameNode(): FrameNode | null {
61. return this.rootNode;
62. }
63. }

65. @Entry
66. @Component
67. struct Index {
68. @State buttonShow: boolean = true
69. @State buttonIndex: number = 0
70. public buttonController: MyNodeController = new MyNodeController();
71. private buttonNull: null = null;
72. private buttonControllerArray: Array<MyNodeController | null> = [this.buttonController, this.buttonNull]

74. build() {
75. Column() {
76. Row() {
77. Button("Bind/Unbind")
78. .onClick(() => {
79. this.buttonIndex++;
80. }).margin(5)
81. Button("onAttach/onDetach")
82. .onClick(() => {
83. this.buttonShow = !this.buttonShow
84. }).margin(5)
85. }

87. if (this.buttonShow) {
88. NodeContainer(this.buttonControllerArray[this.buttonIndex % this.buttonControllerArray.length])
89. }
90. }
91. .padding({ left: 35, right: 35 })
92. .width("100%")
93. .height("100%")
94. }
95. }
```

## 组件设置和删除多态样式状态示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode, typeNode, UIState } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. private isEnable: boolean = true;
6. private theStatesToBeSupported =
7. UIState.NORMAL | UIState.PRESSED | UIState.FOCUSED | UIState.DISABLED | UIState.SELECTED;

9. makeNode(uiContext: UIContext): FrameNode | null {
10. // 创建并组织节点关系
11. let node = new FrameNode(uiContext);
12. node.commonAttribute.width('100%')
13. .height('100%')
14. .borderColor(Color.Gray)
15. .borderWidth(1)
16. .margin({ left: 10 })

18. let column = typeNode.createNode(uiContext, 'Column');
19. column.initialize({ space: 20 })
20. .width('100%')
21. .height('100%')
22. node.appendChild(column);

24. let styleText = typeNode.createNode(uiContext, 'Text');
25. styleText.initialize("StyleTarget")
26. .width('50%')
27. .height('5%')
28. .margin({ top: 5, bottom: 5 })
29. .fontSize(14)
30. .fontColor(Color.White)
31. .textAlign(TextAlign.Center)
32. .backgroundColor(Color.Green)
33. .borderWidth(2)
34. .borderColor(Color.Black)
35. .focusable(true)

37. // 为Text组件添加多态样式处理能力
38. styleText.addSupportedUIStates(this.theStatesToBeSupported, (node: FrameNode, currentState: number) => {
39. if (currentState == UIState.NORMAL) { // 判断是否normal要使用等于
40. // normal状态，刷normal的UI效果
41. console.info('Callback UIState.NORMAL')
42. node.commonAttribute.backgroundColor(Color.Green)
43. node.commonAttribute.borderWidth(2)
44. node.commonAttribute.borderColor(Color.Black)
45. }
46. if ((currentState & UIState.PRESSED) == UIState.PRESSED) {
47. // press状态，刷press的UI效果
48. console.info('Callback UIState.PRESSED')
49. node.commonAttribute.backgroundColor(Color.Brown)
50. }
51. if ((currentState & UIState.FOCUSED) == UIState.FOCUSED) {
52. // focused状态，刷focused的UI效果
53. console.info('Callback UIState.FOCUSED')
54. node.commonAttribute.borderWidth(5)
55. node.commonAttribute.borderColor(Color.Yellow)
56. }
57. if ((currentState & UIState.DISABLED) == UIState.DISABLED) {
58. // disabled状态，刷disabled的UI效果
59. console.info('Callback UIState.DISABLED')
60. node.commonAttribute.backgroundColor(Color.Gray)
61. node.commonAttribute.borderWidth(0)
62. }
63. if ((currentState & UIState.SELECTED) == UIState.SELECTED) {
64. // selected状态，刷selected的UI效果
65. console.info('Callback UIState.SELECTED')
66. node.commonAttribute.backgroundColor(Color.Pink)
67. }
68. }, false)

70. column.appendChild(styleText);

72. // 为Text组件删除多态样式处理能力
73. let buttonRemove = typeNode.createNode(uiContext, 'Button');
74. buttonRemove.initialize("RemoveUIStatus")
75. .width('50%')
76. .height('5%')
77. .fontSize(14)
78. .margin({ top: 5, bottom: 5 })
79. .onClick(() => {
80. styleText.removeSupportedUIStates(this.theStatesToBeSupported);
81. });
82. column.appendChild(buttonRemove);

84. // 改变多态样式目标节点的使能状态
85. let buttonEnable = typeNode.createNode(uiContext, 'Button');
86. buttonEnable.initialize("DisableText")
87. .width('50%')
88. .height('5%')
89. .fontSize(14)
90. .margin({ top: 5, bottom: 5 })
91. .onClick(() => {
92. this.isEnable = !this.isEnable;
93. buttonEnable.initialize(this.isEnable ? 'DisableText' : 'EnableText');
94. styleText.attribute.enabled(this.isEnable)
95. });
96. column.appendChild(buttonEnable);
97. return node;
98. }
99. }

101. @Entry
102. @Component
103. struct FrameNodeTypeTest {
104. private myNodeController: MyNodeController = new MyNodeController();

106. build() {
107. Row() {
108. NodeContainer(this.myNodeController);
109. }
110. }
111. }
```

## 动画创建与取消示例

PhonePC/2in1TabletTVWearable

该示例说明在FrameNode上[createAnimation](js-apis-arkui-framenode.md#createanimation20)、[cancelAnimations](js-apis-arkui-framenode.md#cancelanimations20)、[getNodePropertyValue](js-apis-arkui-framenode.md#getnodepropertyvalue20)接口的用法。

```
1. import { FrameNode, NodeController, UIContext } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. private rootNode: FrameNode | null = null;
6. private isRunning: boolean = false; // 表示节点上动画是否在运行

8. private startInitAnimation() {
9. if (this.rootNode) {
10. let result: boolean = this.rootNode.createAnimation(AnimationPropertyType.ROTATION, [0, 0, 0], [0, 0, 360],
11. { duration: 3000, curve: Curve.Linear, iterations: -1 }); // 创建动画，第一次创建时显式指定初值，旋转角从[0,0,0]变成[0,0,360]，无限循环
12. if (result) {
13. this.isRunning = true;
14. } else {
15. console.warn('create rotation animation failed');
16. }
17. }
18. }

20. cancelAnimation(cnt: number) {
21. if (this.rootNode && this.isRunning) {
22. let result: boolean = this.rootNode.cancelAnimations([AnimationPropertyType.ROTATION]);
23. if (result) {
24. this.isRunning = false;
25. } else {
26. console.warn('cancel rotation animation failed');
27. if (cnt < 2) { // cnt为尝试取消的次数
28. // 如果取消失败，500ms后再次尝试取消
29. setTimeout(() => {
30. this.cancelAnimation(cnt + 1);
31. }, 500);
32. }
33. }
34. }
35. }

37. continueAnimation() {
38. if (this.rootNode && !this.isRunning) {
39. let currentProperty: number[] =
40. this.rootNode.getNodePropertyValue(AnimationPropertyType.ROTATION); // 获取当前节点上的旋转属性终值
41. if (currentProperty.length == 3) { // 获取属性正常，旋转属性对应的数组长度为3，分别是x、y、z方向的旋转角
42. let endValue: number[];
43. let startValue: number[] | undefined = undefined;
44. if (currentProperty[2] >= 360) {
45. startValue = [currentProperty[0], currentProperty[1],
46. currentProperty[2] - 360]; // 当旋转属性过大时使z方向少转360度，避免z方向角度由于多次启停动画一直增加
47. endValue = [currentProperty[0], currentProperty[1], currentProperty[2]];
48. } else {
49. endValue = [currentProperty[0], currentProperty[1], currentProperty[2] + 360]; // 此时旋转属性小于360度，可以从上次旋转角再多旋转一圈
50. }
51. let result: boolean = this.rootNode.createAnimation(AnimationPropertyType.ROTATION, startValue, endValue,
52. { duration: 3000, curve: Curve.Linear, iterations: -1 });
53. console.info(`create rotation animation from ${startValue ? String(startValue[2]) :
54. "undefined"} to ${endValue[2]}`);
55. if (result) {
56. this.isRunning = true;
57. } else {
58. console.warn('create rotation animation failed when continue');
59. }
60. }
61. }
62. }

64. makeNode(uiContext: UIContext): FrameNode | null {
65. if (this.rootNode) {
66. return this.rootNode;
67. }
68. this.rootNode = new FrameNode(uiContext);
69. this.rootNode.commonAttribute.width(100)
70. .height(100)
71. .backgroundColor(Color.Blue); // 设置节点属性
72. this.startInitAnimation();
73. this.rootNode.commonEvent.setOnClick(() => {
74. if (this.isRunning) {
75. this.cancelAnimation(1);
76. } else {
77. this.continueAnimation();
78. }
79. });
80. return this.rootNode;
81. }
82. }

84. @Entry
85. @Component
86. struct CreateAnimationExample {
87. private myNodeController: MyNodeController = new MyNodeController();

89. build() {
90. Column() {
91. NodeContainer(this.myNodeController)
92. }.width('100%').padding({ top: 50 })
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/8hErB7SOTaaLLZxIgmpjJQ/zh-cn_image_0000002552799798.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=CF9A64323F9A3CB202133EFAF6931EDE55F6A33E1BB72F79CBFB002958464FA5)

## 滚动事件示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. public rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);
9. this.rootNode.commonAttribute.width(100)
10. return this.rootNode;
11. }

13. addCommonEvent(frameNode: FrameNode) {
14. let gridEvent: UIGridEvent | undefined = typeNode.getEvent(frameNode, "Grid");
15. gridEvent?.setOnWillScroll((scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
16. console.info(`onWillScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}`)
17. })
18. gridEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
19. console.info(`onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}`)
20. })
21. gridEvent?.setOnReachStart(() => {
22. console.info(`onReachStart`)
23. })
24. gridEvent?.setOnReachEnd(() => {
25. console.info(`onReachEnd`)
26. })
27. gridEvent?.setOnScrollStart(() => {
28. console.info(`onScrollStart`)
29. })
30. gridEvent?.setOnScrollStop(() => {
31. console.info(`onScrollStop`)
32. })
33. gridEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
34. console.info(`onScrollFrameBegin offset = ${offset}, state = ${state}`)
35. return undefined;
36. })
37. gridEvent?.setOnScrollIndex((first: number, last: number) => {
38. console.info(`onScrollIndex start = ${first}, end = ${last}`)
39. })
40. }
41. }

43. @Entry
44. @Component
45. struct Index {
46. @State index: number = 0;
47. private myNodeController: MyNodeController = new MyNodeController();
48. @State numbers: string[] = []

50. aboutToAppear() {
51. for (let i = 0; i < 5; i++) {
52. for (let j = 0; j < 5; j++) {
53. this.numbers.push(j.toString());
54. }
55. }
56. }

58. build() {
59. Column() {
60. Button("add CommonEvent to Grid")
61. .onClick(() => {
62. this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
63. })
64. Grid() {
65. ForEach(this.numbers, (day: string, index: number) => {
66. GridItem() {
67. Text(day)
68. .fontSize(16)
69. .backgroundColor(0xF9CF93)
70. .width('100%')
71. .height(80)
72. .textAlign(TextAlign.Center)
73. }
74. }, (day: string, index: number) => index.toString() + day)
75. }
76. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
77. .columnsGap(10)
78. .rowsGap(10)
79. .enableScrollInteraction(true)
80. .width('90%')
81. .backgroundColor(0xFAEEE0)
82. .height(300)

84. NodeContainer(this.myNodeController)
85. }.width("100%")
86. }
87. }
```

## 检验FrameNode是否有效示例

PhonePC/2in1TabletTVWearable

该示例演示了FrameNode释放节点前后分别使用[isDisposed](js-apis-arkui-framenode.md#isdisposed20)接口验证节点的状态，释放节点前节点调用isDisposed接口返回true，释放节点后节点调用isDisposed接口返回false。

```
1. import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';

3. @Component
4. struct TestComponent {
5. build() {
6. Column() {
7. Text('This is a BuilderNode.')
8. .fontSize(25)
9. .fontWeight(FontWeight.Bold)
10. }
11. .width('100%')
12. .height(30)
13. .backgroundColor(Color.Gray)
14. }

16. aboutToAppear() {
17. console.info('aboutToAppear');
18. }

20. aboutToDisappear() {
21. console.info('aboutToDisappear');
22. }
23. }

25. @Builder
26. function buildComponent() {
27. TestComponent()
28. }

30. // 继承NodeController实现自定义UI控制器
31. class MyNodeController extends NodeController {
32. private rootNode: FrameNode | null = null;
33. private builderNode: BuilderNode<[]> | null = null;

35. makeNode(uiContext: UIContext): FrameNode | null {
36. this.rootNode = new FrameNode(uiContext);
37. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
38. this.builderNode.build(new WrappedBuilder(buildComponent));

40. const rootRenderNode = this.rootNode.getRenderNode();
41. if (rootRenderNode !== null) {
42. rootRenderNode.size = { width: 300, height: 300 };
43. rootRenderNode.backgroundColor = 0xffd5d5d5;
44. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
45. }

47. return this.rootNode;
48. }

50. disposeFrameNode() {
51. if (this.rootNode !== null && this.builderNode !== null) {
52. this.rootNode.removeChild(this.builderNode.getFrameNode());
53. this.builderNode.dispose();

55. this.rootNode.dispose();
56. }
57. }

59. isDisposed(): string {
60. if (this.rootNode !== null) {
61. if (this.rootNode.isDisposed()) {
62. return 'frameNode isDisposed is true';
63. } else {
64. return 'frameNode isDisposed is false';
65. }
66. }
67. return 'frameNode is null';
68. }

70. removeBuilderNode() {
71. const rootRenderNode = this.rootNode!.getRenderNode();
72. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
73. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
74. }
75. }
76. }

78. @Entry
79. @Component
80. struct Index {
81. @State text: string = ''
82. private myNodeController: MyNodeController = new MyNodeController();

84. build() {
85. Column({ space: 4 }) {
86. NodeContainer(this.myNodeController)
87. Button('FrameNode dispose')
88. .onClick(() => {
89. this.myNodeController.disposeFrameNode();
90. this.text = '';
91. })
92. .width(200)
93. .height(50)
94. Button('FrameNode isDisposed')
95. .onClick(() => {
96. this.text = this.myNodeController.isDisposed();
97. })
98. .width(200)
99. .height(50)
100. Text(this.text)
101. .fontSize(25)
102. }
103. .width('100%')
104. .height('100%')
105. }
106. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/AKCPWBwzS9eTyM4IZkJgvQ/zh-cn_image_0000002583439493.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=E724AF6A342B9D5FC3A6A4E2ABC8F58E3688FDA4FB8694CBC50C93EE81F00A59)

## 检验NodeAdapter是否有效示例

PhonePC/2in1TabletTVWearable

该示例演示了[NodeAdapter](js-apis-arkui-framenode.md#nodeadapter12)释放节点前后分别使用[isDisposed](js-apis-arkui-framenode.md#isdisposed20)接口验证节点的状态，释放节点前节点调用isDisposed接口返回true，释放节点后节点调用isDisposed接口返回false。

```
1. import { FrameNode, NodeController, NodeAdapter, typeNode } from '@kit.ArkUI';

3. // 自定义NodeAdapter管理数据
4. class MyNodeAdapter extends NodeAdapter {
5. uiContext: UIContext
6. cachePool: Array<FrameNode> = new Array();
7. changed: boolean = false
8. reloadTimes: number = 0;
9. data: Array<string> = new Array();
10. hostNode?: FrameNode

12. constructor(uiContext: UIContext, count: number) {
13. super();
14. this.uiContext = uiContext;
15. this.totalNodeCount = count;
16. this.loadData();
17. }

19. loadData(): void {
20. for (let i = 0; i < this.totalNodeCount; i++) {
21. this.data[i] = "Adapter ListItem " + i + " r:" + this.reloadTimes;
22. }
23. }

25. onCreateChild(index: number): FrameNode {
26. console.info(`UINodeAdapter onCreateChild:${index}`);
27. if (this.cachePool.length > 0) {
28. let cacheNode = this.cachePool.pop();
29. if (cacheNode !== undefined) {
30. console.info(`UINodeAdapter onCreateChild reused id:${cacheNode.getUniqueId()}`);
31. let text = cacheNode?.getFirstChild();
32. let textNode = text as typeNode.Text;
33. textNode?.initialize(this.data[index]).fontSize(20);
34. return cacheNode;
35. }
36. }
37. console.info("UINodeAdapter onCreateChild createNew");
38. let itemNode = typeNode.createNode(this.uiContext, "ListItem");
39. let textNode = typeNode.createNode(this.uiContext, "Text");
40. textNode.initialize(this.data[index]).fontSize(20);
41. itemNode.appendChild(textNode);
42. return itemNode;
43. }
44. }

46. // 继承NodeController实现自定义NodeAdapter控制器
47. class MyNodeAdapterController extends NodeController {
48. rootNode: FrameNode | null = null;
49. nodeAdapter: MyNodeAdapter | null = null;

51. makeNode(uiContext: UIContext): FrameNode | null {
52. this.rootNode = new FrameNode(uiContext);
53. let listNode = typeNode.createNode(uiContext, "List");
54. listNode.initialize({ space: 3 }).borderColor(Color.Black);
55. this.rootNode.appendChild(listNode);
56. this.nodeAdapter = new MyNodeAdapter(uiContext, 20);
57. NodeAdapter.attachNodeAdapter(this.nodeAdapter, listNode);
58. return this.rootNode;
59. }

61. dispose() {
62. if (this.nodeAdapter !== null) {
63. this.nodeAdapter.dispose();
64. }
65. }

67. isDisposed(): string {
68. if (this.nodeAdapter !== null) {
69. if (this.nodeAdapter.isDisposed()) {
70. return 'nodeAdapter isDisposed is true';
71. } else {
72. return 'nodeAdapter isDisposed is false';
73. }
74. }
75. return 'nodeAdapter is null';
76. }
77. }

79. @Entry
80. @Component
81. struct ListNodeTest {
82. @State text: string = ''
83. adapterController: MyNodeAdapterController = new MyNodeAdapterController();

85. build() {
86. Column() {
87. Text("ListNode Adapter");
88. NodeContainer(this.adapterController)
89. .width(300).height(300)
90. .borderWidth(1).borderColor(Color.Black);
91. Button("NodeAdapter dispose")
92. .onClick(() => {
93. this.adapterController.dispose();
94. this.text = '';
95. })
96. .width(200)
97. .height(50)
98. .margin({ top: 10, bottom: 10 })
99. Button("NodeAdapter isDisposed")
100. .onClick(() => {
101. this.text = this.adapterController.isDisposed();
102. })
103. .width(200)
104. .height(50)
105. Text(this.text)
106. .fontSize(25)
107. }
108. .width("100%")
109. }
110. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/-XZDPYWgR4yOTe3ILvbTtw/zh-cn_image_0000002552959448.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=4E687A5848127392AF1B249C97B183A37109C514198CC4534D055324E22C1560)

## 获取根节点示例

PhonePC/2in1TabletTVWearable

该示例演示了如何通过FrameNode的[getParent](js-apis-arkui-framenode.md#getparent12)接口获取当前页面根节点。

```
1. @Component
2. struct ChildView {
3. @State message: string = 'Hello World';

5. build() {
6. RelativeContainer() {
7. Text(this.message)
8. .id('HelloWorld')
9. .fontSize($r('app.float.page_text_font_size'))
10. .fontWeight(FontWeight.Bold)
11. .alignRules({
12. center: { anchor: '__container__', align: VerticalAlign.Center },
13. middle: { anchor: '__container__', align: HorizontalAlign.Center }
14. })
15. .onClick(() => {
16. // 通过id查询获得Text节点的FrameNode对象。不建议设置多个相同的id的节点
17. let node = this.getUIContext().getFrameNodeById("HelloWorld");
18. console.info(`Find HelloWorld Tag:${node!.getNodeType()} id:${node!.getUniqueId()}`);
19. // 通过while循环遍历查询页面的根节点。如果当前节点为自定义组件，则会继续遍历其父节点
20. while (node && node.getParent() && node.getParent()!.getUniqueId() > 0) {
21. node = node.getParent();
22. console.info(`Find FrameNode Tag:${node!.getNodeType()} id:${node!.getUniqueId()}`);
23. }
24. })
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. @State message: string = 'Hello World';

36. build() {
37. RelativeContainer() {
38. ChildView({ message: this.message })
39. .height('100%')
40. .width('100%')
41. }
42. .height('100%')
43. .width('100%')
44. }
45. }
```

## 接纳为附属节点示例

PhonePC/2in1TabletTVWearable

从API version 22开始，该示例演示了如何通过FrameNode的[adoptChild](js-apis-arkui-framenode.md#adoptchild22)和[removeAdoptedChild](js-apis-arkui-framenode.md#removeadoptedchild22)接口进行接纳为附属节点的相关操作。

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = "FrameNode "

5. // 继承NodeController实现自定义UI控制器
6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. public rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);
12. this.frameNode = new FrameNode(uiContext);
13. this.addCommonEvent(this.frameNode);
14. return this.rootNode;
15. }

17. addCommonEvent(frameNode: FrameNode) {
18. frameNode.commonEvent.setOnClick((event: ClickEvent) => {
19. console.info(`${TEST_TAG} Click FrameNode: ${JSON.stringify(event)}`);
20. })
21. }

23. adoptChild() {
24. try {
25. this.rootNode?.adoptChild(this.frameNode);
26. console.info(`${TEST_TAG} adoptChild success`);
27. } catch (e) {
28. console.info(`${TEST_TAG} adoptChild fail: ${JSON.stringify(e)}`);
29. }
30. }

32. removeAdoptedChild() {
33. try {
34. this.rootNode?.removeAdoptedChild(this.frameNode);
35. console.info(`${TEST_TAG} removeAdoptedChild success`);
36. } catch (e) {
37. console.info(`${TEST_TAG} removeAdoptedChild fail: ${JSON.stringify(e)}`);
38. }
39. }
40. }

42. @Entry
43. @Component
44. struct Index {
45. private myNodeController: MyNodeController = new MyNodeController();

47. build() {
48. Column({ space: 8 }) {
49. Column() {
50. Text(`This is a NodeContainer.`)
51. .textAlign(TextAlign.Center)
52. .borderRadius(10)
53. .backgroundColor(0xFFFFFF)
54. .width(`100%`)
55. .fontSize(16)
56. NodeContainer(this.myNodeController)
57. .borderWidth(1)
58. .width(300)
59. .height(100)
60. }

62. Button(`adoptChild`)
63. .width(300)
64. .onClick(() => {
65. this.myNodeController.adoptChild();
66. })
67. Button(`removeAdoptedChild`)
68. .width(300)
69. .onClick(() => {
70. this.myNodeController.removeAdoptedChild();
71. })
72. }
73. }
74. }
```

## 局部与窗口坐标转化示例

PhonePC/2in1TabletTVWearable

该示例演示了如何通过FrameNode的[convertPositionToWindow](js-apis-arkui-framenode.md#convertpositiontowindow23)和[convertPositionFromWindow](js-apis-arkui-framenode.md#convertpositionfromwindow23)接口进行局部与窗口坐标转化。

从API version 23开始，新增convertPositionToWindow和convertPositionFromWindow接口。

```
1. import { Position } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ConvertPositionWithWindow {
6. private uiContext: UIContext = this.getUIContext();
7. @State message: string = 'Hello World';

9. build() {
10. Column() {
11. Text(this.message)
12. .id('testNodeA')
13. .fontSize($r('app.float.page_text_font_size')) // 请开发者替换为实际的资源文件
14. .fontWeight(FontWeight.Bold)
15. Button('运行convertPositionToWindow和convertPositionFromWindow测试')
16. .onClick(() => {
17. this.runBasicTest();
18. })
19. .margin(20)
20. }
21. .width('100%')
22. .height('100%')
23. }

25. private runBasicTest() {
26. // 等待UI渲染完成
27. if (!this.uiContext) {
28. return;
29. }
30. const nodeA = this.uiContext.getAttachedFrameNodeById('testNodeA');

32. if (!nodeA) {
33. console.info('无法获取测试节点');
34. return;
35. }

37. const testPoint: Position = { x: 10, y: 10 };
38. try {
39. const result: Position = nodeA.convertPositionToWindow(testPoint); // 显式声明可能返回undefined
40. console.info(`相对于节点的(10, 10)坐标转换到相对于窗口的坐标为(${result.x}, ${result.y})`);
41. } catch (e) {
42. const exception = e as BusinessError<void>;
43. console.error(`convertPositionToWindow throw error! code: ${exception.code}, message: ${exception.message}`);
44. }

46. try {
47. const result: Position = nodeA.convertPositionFromWindow(testPoint); // 显式声明可能返回undefined
48. console.info(`相对于窗口的(10, 10)坐标转换到相对于该节点的坐标为(${result.x}, ${result.y})`);
49. } catch (e) {
50. const exception = e as BusinessError<void>;
51. console.error(`convertPositionFromWindow throw error! code: ${exception.code}, message: ${exception.message}`);
52. }
53. }
54. }
```
