---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode
title: FrameNode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > FrameNode
category: harmonyos-references
scraped_at: 2026-09-05T06:16:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bff46fbf89ea3b8081865555c6d198c8f3ca8a6ac404b9a0066a7e7803562dcf
---

FrameNode表示组件树的实体节点，支持节点树操作、自定义绘制与布局、位置查询、动画等能力。[NodeController](js-apis-arkui-nodecontroller.md)可通过[BuilderNode](js-apis-arkui-buildernode.md)持有的FrameNode将其挂载到[NodeContainer](ts-basic-components-nodecontainer.md)上，也可通过FrameNode获取[RenderNode](js-apis-arkui-rendernode.md)，挂载到其他FrameNode上。适用于需要通过代码动态创建和管理组件节点树的场景，可实现声明式组件无法直接满足的灵活UI组合与自定义渲染需求。最佳实践请参考[组件动态创建](../harmonyos-guides/arkts-ui-component-dynamic-creation.md)。

**说明** 

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当前不支持在预览器中使用FrameNode节点。
* FrameNode节点暂不支持拖拽。
* FrameNode对象不支持使用JSON序列化。
* 在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的场景中调用[FrameNode](js-apis-arkui-framenode.md#framenode-1)对象的接口时，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口明确UI上下文，参考[执行绑定UI实例的闭包](../harmonyos-guides/arkts-global-interface.md#执行绑定ui实例的闭包)示例。
* FrameNode的接口中，仅[Optional](ts-universal-attributes-custom-property.md#optionalt)类型的必选参数支持传入null或undefined。

## 导入模块

```ts
import { FrameNode, LayoutConstraint, ExpandMode, ChildrenCountMode, typeNode, NodeAdapter } from '@kit.ArkUI';
```

## LayoutConstraint12+

描述组件的布局约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxSize | [Size](js-apis-arkui-graphics.md#size) | 否 | 否 | 最大尺寸。 |
| minSize | [Size](js-apis-arkui-graphics.md#size) | 否 | 否 | 最小尺寸。 |
| percentReference | [Size](js-apis-arkui-graphics.md#size) | 否 | 否 | 子节点计算百分比时的尺寸基准。 |

## CrossLanguageOptions15+

该接口用于配置或查询FrameNode的跨语言访问权限。例如，针对ArkTS语言创建的节点，可通过该接口控制是否允许通过非ArkTS语言进行属性访问或修改。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attributeSetting | boolean | 否 | 是 | FrameNode是否支持跨ArkTS语言进行属性设置。  true表示支持跨ArkTS语言进行属性设置，false表示不支持跨ArkTS语言进行属性设置。  默认值为false。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| treeOperating | boolean | 否 | 是 | FrameNode是否支持跨ArkTS语言进行组件树操作。  true表示支持跨ArkTS语言进行组件树操作，false表示不支持跨ArkTS语言进行组件树操作。  默认值为false。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **说明：** 当FrameNode启用了跨ArkTS语言进行组件树操作的选项后，支持该FrameNode跨ArkTS语言调用[addChild](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addchild)、[insertChildAfter](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#insertchildafter)、[insertChildAt](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#insertchildat)、[insertChildBefore](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#insertchildbefore)和[removeChild](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removechild)。 |

## ExpandMode15+

子节点展开模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_EXPAND | 0 | 表示不展开当前FrameNode的子节点。如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，获取在主节点树上的子节点时，不展开当前FrameNode的子节点。子节点序列号按在主节点树上的子节点计算。  使用场景：仅需获取主节点树上已展开子节点且不触发展开操作的场景。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| EXPAND | 1 | 表示展开当前FrameNode的子节点。如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，获取所有子节点时，展开当前FrameNode的子节点。子节点序列号按所有子节点计算。  使用场景：需要获取包含懒加载在内的所有子节点的场景。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| LAZY\_EXPAND | 2 | 表示按需展开当前FrameNode的子节点。如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，获取在主节点树上的子节点时，不展开当前FrameNode的子节点；获取不在主节点树上的子节点时，展开当前FrameNode的子节点。子节点序列号按所有子节点计算。  使用场景：需要兼顾主节点树与非主节点树子节点按需获取的场景。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| LAZY\_NOT\_EXPAND | 3 | 表示不展开当前FrameNode的子节点，如果FrameNode包含[LazyForEach](ts-rendering-control-lazyforeach.md)子节点，对于已经展开的子节点，可以直接返回，获取未展开的子节点时，仅创建对应位置的节点，而不展开所有子节点。子节点序列号按所有子节点计算。  使用场景：需要按位置精确获取子节点但不批量展开懒加载子节点的场景。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## ChildrenCountMode

子节点计数模式枚举。用于指定获取子节点数量时的计数方式。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL\_EXPAND | 0 | 计数展开模式。当遇到懒加载节点（如[LazyForEach](ts-rendering-control-lazyforeach.md)）时，展开节点并返回所有子节点数量。  是否展开懒加载节点：是  使用场景：需要展开并返回所有子节点数量的场景。 |
| ONLY\_EXPANDED | 1 | 计数已展开模式。不展开懒加载节点，只返回当前已展开的子节点数量。未展开的懒加载节点不包含在计数中。  是否展开懒加载节点：否  使用场景：仅查询已展开子节点数量的场景。 |
| ALL\_NOT\_EXPAND | 2 | 计数所有模式。不展开懒加载节点，但返回包含所有潜在子节点的数量（包括已展开和未展开的懒加载节点）。此模式提供潜在子节点总数而不触发展开操作。  是否展开懒加载节点：否  使用场景：需要获取所有子节点数量的场景，与ALL\_EXPAND相比，该模式不会展开子节点。 |

## InteractionEventBindingInfo19+

组件的交互事件绑定状态信息。如果当前节点上绑定了所要查询的交互事件，调用查询接口时返回一个InteractionEventBindingInfo对象，指示事件绑定详细信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseEventRegistered | boolean | 否 | 否 | 是否以声明方式绑定事件。  true表示以声明方式绑定事件，false表示没有以声明方式绑定事件。 |
| nodeEventRegistered | boolean | 否 | 否 | 是否以自定义组件节点的方式绑定事件，请参考[基础事件示例](js-apis-arkui-framenode.md#基础事件示例)。  true表示以自定义组件节点的方式绑定事件，false表示没有以自定义组件节点的方式绑定事件。 |
| nativeEventRegistered | boolean | 否 | 否 | 是否以注册节点事件（[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)）的方式绑定事件。  true表示以注册节点事件的方式绑定事件，false表示没有以注册节点事件的方式绑定事件。 |
| builtInEventRegistered | boolean | 否 | 否 | 组件是否绑定内置事件（组件内部定义的事件，无需开发者手动绑定）。  true表示组件绑定内置事件，false表示组件没有绑定内置事件。 |

## UIState20+

多态样式状态枚举，用于处理多态样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 正常状态。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| PRESSED | 1 << 0 | 按下状态。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| FOCUSED | 1 << 1 | 获焦状态。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DISABLED | 1 << 2 | 禁用状态。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| SELECTED | 1 << 3 | 选中状态。  仅特定的组件支持此状态：Checkbox、Radio、Toggle、List、Grid、MenuItem。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| HOVERED | 1 << 4 | 悬浮状态。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## UIStatesChangeHandler20+

type UIStatesChangeHandler = (node: FrameNode, currentUIStates: number) => void

当UI状态发生变化时触发的回调。接收回调触发时的[UIState](js-apis-arkui-framenode.md#uistate20)状态，该参数的取值为UIState状态枚举值或其运算结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 触发UI状态变化的节点。 |
| currentUIStates | number | 是 | 回调触发时当前的UI状态。  可以通过位与运算判断当前包含哪些[UIState](js-apis-arkui-framenode.md#uistate20)状态。  位与运算方法：if ((currentUIStates & UIState.PRESSED) == UIState.PRESSED)。  当仅需判断当前是否仅处于单个状态时，可以直接判断：if (currentUIStates == UIState.PRESSED)。注意，此方式仅在当前仅有一个状态激活时有效，若需判断多个状态中是否包含某个状态，请使用位与运算。 |

## FrameNode

FrameNode表示组件树的实体节点，支持节点树操作、自定义绘制与布局、位置查询、动画等能力。[NodeController](js-apis-arkui-nodecontroller.md)可通过[BuilderNode](js-apis-arkui-buildernode.md)持有的FrameNode将其挂载到[NodeContainer](ts-basic-components-nodecontainer.md)上，也可通过FrameNode获取[RenderNode](js-apis-arkui-rendernode.md)，挂载到其他FrameNode上。适用于需要通过代码动态创建和管理组件节点树的场景，可实现声明式组件无法直接满足的灵活UI组合与自定义渲染需求。[getInspectorInfo返回结果$attrs映射表.xlsx](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-arkui/figures/getInspectorInfo返回结果$attrs映射表.xlsx)。

**说明** 

* 当前不支持在预览器中使用FrameNode节点。
* FrameNode节点暂不支持拖拽。
* FrameNode对象不支持使用JSON序列化。
* 在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的场景中调用[FrameNode](js-apis-arkui-framenode.md#framenode-1)对象的接口时，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口明确UI上下文，参考[执行绑定UI实例的闭包](../harmonyos-guides/arkts-global-interface.md#执行绑定ui实例的闭包)示例。
* FrameNode的接口中，仅[Optional](ts-universal-attributes-custom-property.md#optionalt)类型的必选参数支持传入null或undefined。

### constructor

constructor(uiContext: UIContext)

FrameNode的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |

### getRenderNode

getRenderNode(): RenderNode | null

获取FrameNode中持有的[RenderNode](js-apis-arkui-rendernode.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderNode](js-apis-arkui-rendernode.md) | null | 一个RenderNode对象。若该FrameNode不包含RenderNode，则返回空对象null。如果当前FrameNode为声明式组件创建的节点，则返回null。 |

**示例：**

```ts
import { NodeController, FrameNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 获取rootNode持有的RenderNode
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode !== null) {
      renderNode.size = { width: 100, height: 100 };
      renderNode.backgroundColor = 0XFFFF0000;
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

### isModifiable12+

isModifiable(): boolean

判断当前节点是否可修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 判断当前节点是否可修改。  true表示当前节点可修改，false表示当前节点不可修改。  当节点为[自定义组件节点](../harmonyos-guides/arkts-user-defined-node.md#自定义组件节点-framenode)中的系统组件代理节点或节点已经[dispose](js-apis-arkui-framenode.md#dispose12)时返回false。  当返回false时，当前FrameNode不支持[appendChild](js-apis-arkui-framenode.md#appendchild12)、[insertChildAfter](js-apis-arkui-framenode.md#insertchildafter12)、[removeChild](js-apis-arkui-framenode.md#removechild12)、[clearChildren](js-apis-arkui-framenode.md#clearchildren12)、[createAnimation](js-apis-arkui-framenode.md#createanimation20)、[cancelAnimations](js-apis-arkui-framenode.md#cancelanimations20)、[moveTo](js-apis-arkui-framenode.md#moveto18)、[addComponentContent](js-apis-arkui-framenode.md#addcomponentcontent12)、[adoptChild](js-apis-arkui-framenode.md#adoptchild22)、[removeAdoptedChild](js-apis-arkui-framenode.md#removeadoptedchild22)的操作。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### appendChild12+

appendChild(node: FrameNode): void

在FrameNode最后一个子节点后添加新的子节点。当前FrameNode如果不可修改，抛出异常信息。[typeNode](js-apis-arkui-framenode.md#typenode12)在appendChild时会校验子组件类型或个数，不满足时抛出异常信息，限制情况请查看[typeNode](js-apis-arkui-framenode.md#typenode12)描述。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 需要添加的FrameNode。  node节点不可以为不可修改的FrameNode（例如通过getFrameNodeById等接口获取的声明式组件节点）。仅[BuilderNode](js-apis-arkui-buildernode.md)通过getFrameNode接口获取的FrameNode可作为声明式子节点添加。若子节点不符合规格，则抛出异常信息。  node节点不可以拥有父节点，否则抛出异常信息。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted."  适用版本：22+ |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### insertChildAfter12+

insertChildAfter(child: FrameNode, sibling: FrameNode | null): void

在FrameNode指定子节点之后添加新的子节点。当前FrameNode如果不可修改，抛出异常信息。[typeNode](js-apis-arkui-framenode.md#typenode12)在insertChildAfter时会校验子组件类型或个数，不满足时抛出异常信息，限制情况请查看[typeNode](js-apis-arkui-framenode.md#typenode12)描述。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 需要添加的子节点。  child节点不可以为不可修改的FrameNode（例如通过getFrameNodeById等接口获取的声明式组件节点）。仅[BuilderNode](js-apis-arkui-buildernode.md)通过getFrameNode接口获取的FrameNode可作为声明式子节点添加。若子节点不符合规格，则抛出异常信息。  child节点不可以拥有父节点，否则抛出异常信息。 |
| sibling | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 是 | 新节点将插入到该节点之后。若该参数设置为空，则新节点将插入到首个子节点之前。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be adopted."  适用版本：22+ |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### removeChild12+

removeChild(node: FrameNode): void

从FrameNode中删除指定的子节点。当前FrameNode如果不可修改，抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

clearChildren(): void

清除当前FrameNode的所有子节点。当前FrameNode如果不可修改，抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getChild12+

getChild(index: number): FrameNode | null

获取当前节点指定位置的子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getChild(index: number, expandMode?: ExpandMode): FrameNode | null

获取当前节点指定位置的子节点，支持指定子节点展开模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getFirstChildIndexWithoutExpand(): number

获取当前节点第一个在主节点树上的子节点的序列号。子节点序列号按所有子节点计算。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前节点第一个在主节点树上的子节点的序列号。 |

**示例：**

请参考[LazyForEach场景节点操作示例](js-apis-arkui-framenode.md#lazyforeach场景节点操作示例)。

### getLastChildIndexWithoutExpand15+

getLastChildIndexWithoutExpand(): number

获取当前节点最后一个在主节点树上的子节点的序列号。子节点序列号按所有子节点计算。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前节点最后一个在主节点树上的子节点的序列号。 |

**示例：**

请参考[LazyForEach场景节点操作示例](js-apis-arkui-framenode.md#lazyforeach场景节点操作示例)。

### getFirstChild12+

getFirstChild(): FrameNode | null

获取当前FrameNode的第一个子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 首个子节点。若该FrameNode不包含子节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getNextSibling12+

getNextSibling(): FrameNode | null

获取当前FrameNode的下一个同级节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 当前FrameNode的下一个同级节点。若该FrameNode不包含下一个同级节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPreviousSibling12+

getPreviousSibling(): FrameNode | null

获取当前FrameNode的上一个同级节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 当前FrameNode的上一个同级节点。若该FrameNode不包含上一个同级节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getParent12+

getParent(): FrameNode | null

获取当前FrameNode的父节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 当前FrameNode的父节点。若该FrameNode不包含父节点，则返回空对象null。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)和[获取根节点示例](js-apis-arkui-framenode.md#获取根节点示例)。

### getChildrenCount12+

getChildrenCount(): number

获取当前FrameNode的子节点数量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前FrameNode的子节点数量。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getChildrenCount

getChildrenCount(countMode?: ChildrenCountMode): number

根据指定的计数模式获取当前FrameNode的子节点数量。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| countMode | [ChildrenCountMode](js-apis-arkui-framenode.md#childrencountmode) | 否 | 子节点计数模式。默认值为ChildrenCountMode.ALL\_EXPAND。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 根据计数模式返回的当前FrameNode的子节点数量。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext, BuilderNode, ChildrenCountMode, LengthUnit } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): string {
    return this.originDataArray[index];
  }

  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    })
  }
}

// 自定义数据管理类管理string数组
class MyDataSource extends BasicDataSource {
  private dataArray: string[] = []

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string {
    return this.dataArray[index];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

class Params {
  data: MyDataSource | null = null;
  scroller: Scroller | null = null;

  constructor(data: MyDataSource, scroller: Scroller) {
    this.data = data;
    this.scroller = scroller;
  }
}

@Builder
function buildData(params: Params) {
  List({ scroller: params.scroller }) {
    LazyForEach(params.data, (item: string) => {
      ListItem() {
        Column() {
          Text(item)
            .fontSize(20)
            .onAppear(() => {
              console.info(`${TEST_TAG} node appear: ${item}`)
            })
            .backgroundColor(Color.Pink)
            .margin({
              top: 30,
              bottom: 30,
              left: 10,
              right: 10
            })
        }
      }
      .id(item)
    }, (item: string) => item)
  }
  .cachedCount(5)
  .listDirection(Axis.Horizontal)
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private uiContext: UIContext | null = null;
  private data: MyDataSource = new MyDataSource();
  private scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    for (let i = 0; i <= 20; i++) {
      this.data.pushData(`N${i}`);
    }
    const params: Params = new Params(this.data, this.scroller);
    const dataNode: BuilderNode<[Params]> = new BuilderNode(uiContext);
    dataNode.build(wrapBuilder<[Params]>(buildData), params);
    this.rootNode = dataNode.getFrameNode();
    const scrollToIndexOptions: ScrollToIndexOptions = {
      extraOffset: {
        value: 20, unit: LengthUnit.VP
      }
    };
    this.scroller.scrollToIndex(6, true, ScrollAlign.START, scrollToIndexOptions);
    return this.rootNode;
  }

  getChildCountAllExpand() {
    const childCount = this.rootNode?.getChildrenCount(ChildrenCountMode.ALL_EXPAND);
    console.info(TEST_TAG + 'ALL_EXPAND, childCount=' + childCount);
  }

  getChildCountOnlyExpanded() {
    const childCount = this.rootNode?.getChildrenCount(ChildrenCountMode.ONLY_EXPANDED);
    console.info(TEST_TAG + 'ONLY_EXPANDED, childCount=' + childCount);
  }
  
  getChildCountAllNotExpand() {
    const childCount = this.rootNode?.getChildrenCount(ChildrenCountMode.ALL_NOT_EXPAND);
    console.info(TEST_TAG + 'ALL_NOT_EXPAND, childCount=' + childCount);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getChildCount(ALL_EXPAND)')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildCountAllExpand();
          })
        Button('getChildCount(ONLY_EXPANDED)')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildCountOnlyExpanded();
          })
        Button('getChildCount(ALL_NOT_EXPAND)')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildCountAllNotExpand();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

### moveTo18+

moveTo(targetParent: FrameNode, index?: number): void

将当前FrameNode移动到目标FrameNode的指定位置。当前FrameNode如果不可修改，抛出异常信息。targetParent为[typeNode](js-apis-arkui-framenode.md#typenode12)时会校验子组件类型或个数，不满足时抛出异常信息，限制情况请查看[typeNode](js-apis-arkui-framenode.md#typenode12)描述。

**说明** 

当前仅支持以下类型的[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)进行移动操作：[Stack](js-apis-arkui-framenode.md#stack12)、[XComponent](js-apis-arkui-framenode.md#xcomponent12)。对于其他类型的节点，移动操作不会生效。

当前仅支持根节点为以下类型组件的[BuilderNode](js-apis-arkui-buildernode.md#buildernode-1)进行移动操作：[Stack](ts-container-stack.md)、[XComponent](ts-basic-components-xcomponent.md)、[EmbeddedComponent](ts-container-embedded-component.md)。对于其他类型的组件，移动操作不会生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 100027 | The current node has been adopted.  适用版本：22+ |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToWindow12+

getPositionToWindow(): Position

获取FrameNode相对于窗口的位置偏移，单位为VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于窗口的位置偏移，单位为VP。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.rootNode.appendChild(this.frameNode);
    return this.rootNode;
  }

  getPositionToWindow() {
    // 获取FrameNode相对于窗口的位置偏移
    let positionToWindow = this.rootNode?.getPositionToWindow();
    console.info(`${TEST_TAG}${JSON.stringify(positionToWindow)}`);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getPositionToWindow')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToWindow();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToParent12+

getPositionToParent(): Position

获取FrameNode相对于父组件的位置偏移，单位为VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于父组件的位置偏移，单位为VP。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.rootNode.appendChild(this.frameNode);
    return this.rootNode;
  }

  getPositionToParent() {
    // 获取FrameNode相对于父组件的位置偏移
    let positionToParent = this.rootNode?.getPositionToParent();
    console.info(`${TEST_TAG}${JSON.stringify(positionToParent)}`);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getPositionToParent')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToParent();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToScreen12+

getPositionToScreen(): Position

获取FrameNode相对于屏幕的位置偏移，单位为VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于屏幕的位置偏移，单位为VP。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.rootNode.appendChild(this.frameNode);
    return this.rootNode;
  }

  getPositionToScreen() {
    // 获取FrameNode相对于屏幕的位置偏移
    let positionToScreen = this.rootNode?.getPositionToScreen();
    console.info(`${TEST_TAG}${JSON.stringify(positionToScreen)}`);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getPositionToScreen')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToScreen();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getGlobalPositionOnDisplay20+

getGlobalPositionOnDisplay(): Position

获取FrameNode相对于全局屏幕的位置偏移，单位为VP。与[getPositionToScreen](js-apis-arkui-framenode.md#getpositiontoscreen12)的坐标系参考不同，请根据实际场景选择使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于全局屏幕的位置偏移，单位为VP。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToParentWithTransform12+

getPositionToParentWithTransform(): Position

获取FrameNode相对于父组件带有绘制属性的位置偏移，单位为VP，绘制属性比如[transform](ts-universal-attributes-transformation.md#transform)、[translate](ts-universal-attributes-transformation.md#translate)等，返回的坐标是组件布局时左上角变换后的坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于父组件的位置偏移，单位为VP。当设置了其他（比如：transform、translate等）绘制属性，由于浮点数精度的影响，返回值会有微小偏差。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.rootNode.appendChild(this.frameNode);
    return this.rootNode;
  }

  getPositionToParentWithTransform() {
    // 获取FrameNode相对于父组件带有绘制属性的位置偏移
    let positionToParentWithTransform = this.rootNode?.getPositionToParentWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToParentWithTransform)}`);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getPositionToParentWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToParentWithTransform();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToWindowWithTransform12+

getPositionToWindowWithTransform(): Position

获取FrameNode相对于窗口带有绘制属性的位置偏移，单位为VP，绘制属性比如[transform](ts-universal-attributes-transformation.md#transform)、[translate](ts-universal-attributes-transformation.md#translate)等，返回的坐标是组件布局时左上角变换后的坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于窗口的位置偏移，单位为VP。当设置了其他（比如：transform、translate等）绘制属性，由于浮点数精度的影响，返回值会有微小偏差。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.rootNode.appendChild(this.frameNode);
    return this.rootNode;
  }

  getPositionToWindowWithTransform() {
    // 获取FrameNode相对于窗口带有绘制属性的位置偏移
    let positionToWindowWithTransform = this.rootNode?.getPositionToWindowWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToWindowWithTransform)}`);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }
        Button('getPositionToWindowWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToWindowWithTransform();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getPositionToScreenWithTransform12+

getPositionToScreenWithTransform(): Position

获取FrameNode相对于屏幕带有绘制属性的位置偏移，单位为VP，绘制属性比如[transform](ts-universal-attributes-transformation.md#transform)、[translate](ts-universal-attributes-transformation.md#translate)等，返回的坐标是组件布局时左上角变换后的坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点相对于屏幕的位置偏移，单位为VP。当设置了其他（比如：transform、translate等）绘制属性，由于浮点数精度的影响，返回值会有微小偏差。 |

**示例：**

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.rootNode.appendChild(this.frameNode);
    return this.rootNode;
  }

  getPositionToScreenWithTransform() {
    // 获取FrameNode相对于屏幕带有绘制属性的位置偏移
    let positionToScreenWithTransform = this.rootNode?.getPositionToScreenWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToScreenWithTransform)}`);
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getPositionToScreenWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToScreenWithTransform();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getMeasuredSize12+

getMeasuredSize(): Size

获取FrameNode测量后的大小，单位为PX。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Size](js-apis-arkui-graphics.md#size) | 节点测量后的大小，单位为PX。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getLayoutPosition12+

getLayoutPosition(): Position

获取FrameNode布局后相对于父组件的位置偏移，单位为PX。该偏移是父容器对该节点进行布局之后的结果，因此布局之后生效的offset属性和不参与布局的position属性不影响该偏移值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 节点布局后相对于父组件的位置偏移，单位为PX。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigBorderWidth12+

getUserConfigBorderWidth(): Edges<LengthMetrics>

获取用户设置的边框宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的边框宽度。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigPadding12+

getUserConfigPadding(): Edges<LengthMetrics>

获取用户设置的内边距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的内边距。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigMargin12+

getUserConfigMargin(): Edges<LengthMetrics>

获取用户设置的外边距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的外边距。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUserConfigSize12+

getUserConfigSize(): SizeT<LengthMetrics>

获取用户设置的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeT](js-apis-arkui-graphics.md#sizett12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 用户设置的宽高。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getId12+

getId(): string

获取用户设置的节点ID（通用属性设置的[组件标识](ts-universal-attributes-component-id.md)）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用户设置的节点ID（通用属性设置的[组件标识](ts-universal-attributes-component-id.md)）。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getUniqueId12+

getUniqueId(): number

获取系统分配的节点唯一标识（UniqueID）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 系统分配的节点唯一标识（UniqueID）。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getNodeType12+

getNodeType(): string

获取节点的类型。系统组件类型为组件名称，例如，按钮组件[Button](ts-basic-components-button.md)的类型为Button。而对于自定义组件，若其有渲染内容，则其类型为\_\_Common\_\_。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 节点的类型。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getOpacity12+

getOpacity(): number

获取节点的不透明度，最小值为0，最大值为1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 节点的不透明度。范围是[0, 1]，值越大透明度越低。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isVisible12+

isVisible(): boolean

获取节点是否可见。

**说明** 

根据组件设置的visibility属性值判断该节点是否可见。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否可见。  true表示节点可见，false表示节点不可见。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isClipToFrame12+

isClipToFrame(): boolean

获取节点是否剪裁到组件区域。当调用[dispose](js-apis-arkui-framenode.md#dispose12)解除对实体FrameNode节点的引用关系之后，返回值为true。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否剪裁到组件区域。  true表示节点剪裁到组件区域，false表示节点未剪裁到组件区域。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isAttached12+

isAttached(): boolean

获取节点是否被挂载到主节点树上。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否被挂载到主节点树上。  true表示节点被挂载到主节点树上，false表示节点不是被挂载到主节点树上。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### isDisposed20+

isDisposed(): boolean

查询当前FrameNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用该节点的其他接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

请参考[检验FrameNode是否有效示例](js-apis-arkui-framenode.md#检验framenode是否有效示例)。

### getInspectorInfo12+

getInspectorInfo(): Object

获取节点的结构信息，该信息和DevEco Studio内置[ArkUI Inspector](../harmonyos-guides/ide-arkui-inspector.md)工具里面的一致。

**说明** 

getInspectorInfo接口用于获取所有节点的信息，作为调试接口使用，频繁调用会导致性能下降。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 节点的结构信息。 |

以查询[Button](ts-basic-components-button.md)组件节点为例获取到的Object结果部分值如下。

```json5
{
    "$type": "Button",
    "$ID": 44,
    "type": "build-in",
    "$rect": "[498.00, 468.00],[718.00,598.00]",
    "$debugLine": "",
    "$attrs": {
        "borderStyle": "BorderStyle.Solid",
        "borderColor": "#FF000000",
        "borderWidth": "0.00vp",
        "borderRadius": {
            "topLeft": "65.00px",
            "topRight": "65.00px",
            "bottomLeft": "65.00px",
            "bottomRight": "65.00px"
        },
        "border": "{\"style\":\"BorderStyle.Solid\",\"color\":\"#FF000000\",\"width\":\"0.00vp\",\"radius\":{\"topLeft\":\"65.00px\",\"topRight\":\"65.00px\",\"bottomLeft\":\"65.00px\",\"bottomRight\":\"65.00px\"},\"dashGap\":\"0.00vp\",\"dashWidth\":\"0.00vp\"}",
        "outlineStyle": "OutlineStyle.SOLID",
        "outlineColor": "#FF000000"
    }
}
```

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getCustomProperty12+

getCustomProperty(name: string): Object | undefined

通过名称获取组件的自定义属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

dispose(): void

立即解除当前FrameNode对象对实体FrameNode节点的引用关系。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**说明** 

* FrameNode对象调用dispose后，由于不对应任何实体FrameNode节点，在调用部分查询接口([getMeasuredSize](js-apis-arkui-framenode.md#getmeasuredsize12)、[getLayoutPosition](js-apis-arkui-framenode.md#getlayoutposition12))的时候会导致应用出现jscrash。
* 通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)可以判断当前FrameNode是否对应一个实体FrameNode节点。当UniqueID大于0时表示该对象对应一个实体FrameNode节点。

**示例：**

```ts
import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';

@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: BuilderNode<[]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(new WrappedBuilder(buildComponent));

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 200, height: 200 };
      rootRenderNode.backgroundColor = 0xffd5d5d5;
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  disposeFrameNode() {
    if (this.rootNode !== null && this.builderNode !== null) {
      // 解除rootNode对实体FrameNode节点的引用关系前，移除rootNode的所有子节点
      this.rootNode.removeChild(this.builderNode.getFrameNode());
      // 解除builderNode对实体FrameNode节点的引用关系
      this.builderNode.dispose();
      // 解除rootNode对实体FrameNode节点的引用关系
      this.rootNode.dispose();
    }
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('FrameNode dispose')
        .onClick(() => {
          this.myNodeController.disposeFrameNode();
        })
        .width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/mUeLYLOEQAW57Xr8QTBh-g/zh-cn_image_0000002712405780.gif)

### commonAttribute12+

get commonAttribute(): CommonAttribute

获取FrameNode中持有的CommonAttribute接口，用于设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)。

仅可以修改自定义节点的属性。

**说明** 

FrameNode的效果参考对齐方式为顶部起始端的[Stack](ts-container-stack.md)容器组件。

FrameNode的属性支持情况参考[属性或事件对attributemodifier的支持情况](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#属性或事件对attributemodifier的支持情况)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CommonAttribute | 获取FrameNode中持有的CommonAttribute接口，用于设置通用属性和通用事件。 |

**示例：**

请参考[基础事件示例](js-apis-arkui-framenode.md#基础事件示例)。

### commonEvent12+

get commonEvent(): UICommonEvent

获取FrameNode中持有的UICommonEvent对象，用于设置基础事件。设置的基础事件与声明式定义的事件平行，参与事件竞争；设置的基础事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

LazyForEach场景下，由于存在节点的销毁重建，对于重建的节点需要重新设置事件回调才能保证监听事件正常响应。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UICommonEvent](ts-uicommonevent.md#uicommonevent) | UICommonEvent对象，用于设置基础事件。 |

**示例：**

请参考[基础事件示例](js-apis-arkui-framenode.md#基础事件示例)和[LazyForEach场景基础事件使用示例](js-apis-arkui-framenode.md#lazyforeach场景基础事件使用示例)。

### gestureEvent14+

get gestureEvent(): UIGestureEvent

获取FrameNode中持有的UIGestureEvent对象，用于设置组件绑定的手势事件。通过gestureEvent接口设置的手势不会覆盖通过[绑定手势事件](ts-gesture-settings.md)绑定的手势，两者同时设置了手势时，优先回调绑定手势事件设置的手势事件。

LazyForEach场景下，由于存在节点的销毁重建，对于重建的节点需要重新设置手势事件回调才能保证监听事件正常响应。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIGestureEvent](ts-uigestureevent.md#uigestureevent) | UIGestureEvent对象，用于设置组件绑定的手势。 |

**示例：**

请参考[手势事件示例](js-apis-arkui-framenode.md#手势事件示例)。

### onDraw12+

onDraw?(context: DrawContext): void

FrameNode的自绘制方法，该方法会重写默认绘制方法，在FrameNode进行内容绘制时被调用。

该接口的[DrawContext](js-apis-arkui-graphics.md#drawcontext)中的Canvas是用于记录指令的临时Canvas，并非节点的真实Canvas。使用请参见[调整自定义绘制Canvas的变换矩阵](../harmonyos-guides/arkts-user-defined-arktsnode-framenode.md#调整自定义绘制canvas的变换矩阵)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [DrawContext](js-apis-arkui-graphics.md#drawcontext) | 是 | 图形绘制上下文。自绘制区域无法超出组件自身大小。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### onMeasure12+

onMeasure(constraint: LayoutConstraint): void

FrameNode的自定义测量方法，该方法会重写默认测量方法，在FrameNode进行测量时被调用，测量FrameNode及其内容的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | [LayoutConstraint](js-apis-arkui-framenode.md#layoutconstraint12) | 是 | 组件进行测量时使用的布局约束。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### onLayout12+

onLayout(position: Position): void

FrameNode的自定义布局方法，该方法会重写默认布局方法，在FrameNode进行布局时被调用，为FrameNode及其子节点指定位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 组件进行布局时使用的位置信息。单位为PX。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### setMeasuredSize12+

setMeasuredSize(size: Size): void

设置FrameNode的测量后的尺寸，默认单位PX。若设置的宽高为负数，自动取零。建议在[onMeasure](js-apis-arkui-framenode.md#onmeasure12)方法中调用，用于设置自定义测量的结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Size](js-apis-arkui-graphics.md#size) | 是 | FrameNode的测量后的尺寸，单位为PX。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### setLayoutPosition12+

setLayoutPosition(position: Position): void

设置FrameNode的布局后的位置，默认单位PX。建议在[onLayout](js-apis-arkui-framenode.md#onlayout12)方法中调用，用于设置自定义布局的结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | FrameNode的布局后的位置，单位为PX。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### measure12+

measure(constraint: LayoutConstraint): void

调用FrameNode的测量方法，根据父容器的布局约束，对FrameNode进行测量，计算出尺寸，如果测量方法被重写，则调用重写的方法。建议在[onMeasure](js-apis-arkui-framenode.md#onmeasure12)方法中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | [LayoutConstraint](js-apis-arkui-framenode.md#layoutconstraint12) | 是 | 组件进行测量时使用的父容器布局约束。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### layout12+

layout(position: Position): void

调用FrameNode的布局方法，为FrameNode及其子节点指定布局位置，如果布局方法被重写，则调用重写的方法。建议在[onLayout](js-apis-arkui-framenode.md#onlayout12)方法中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 组件进行布局时使用的位置信息。单位为PX。 |

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### setNeedsLayout12+

setNeedsLayout(): void

该方法会将FrameNode标记为需要布局的状态，下一帧将会进行重新布局，触发[onMeasure](js-apis-arkui-framenode.md#onmeasure12)和[onLayout](js-apis-arkui-framenode.md#onlayout12)方法的调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[节点自定义示例](js-apis-arkui-framenode.md#节点自定义示例)。

### invalidate12+

invalidate(): void

该方法会触发FrameNode自绘制内容的重新渲染，即重新调用[onDraw](js-apis-arkui-framenode.md#ondraw12)方法进行自绘制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### addComponentContent12+

addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void

支持添加ComponentContent类型的组件内容。要求当前节点是一个可修改的节点，即[isModifiable](js-apis-arkui-framenode.md#ismodifiable12)的返回值为true，否则抛出异常信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, ComponentContent, typeNode } from '@kit.ArkUI';

@Builder
function buildText() {
  Column() {
    Text('hello')
      .width(50)
      .height(50)
      .backgroundColor(Color.Yellow)
  }
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute.width(300).height(300).backgroundColor(Color.Red)
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 10 })
    node.appendChild(col)
    let row = typeNode.createNode(uiContext, 'Row')
    row.attribute.width(200)
      .height(200)
      .borderWidth(1)
      .borderColor(Color.Black)
      .backgroundColor(Color.Green)
    // 创建组件内容
    let component = new ComponentContent<Object>(uiContext, wrapBuilder(buildText))
    if (row.isModifiable()) {
      // 添加新创建的builderText至row中
      row.addComponentContent(component)
      col.appendChild(row)
    }
    return node
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController);
    }
  }
}
```

### disposeTree12+

disposeTree(): void

下树并递归释放当前节点为根的子树。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

// 自定义挂载事件的自定义组件，作为自定义组件树的入口
@Component
struct TestComponent {
  private myNodeController: MyNodeController = new MyNodeController(wrapBuilder(buildComponent2));

  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
      NodeContainer(this.myNodeController)
    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('BuilderNode aboutToAppear');
  }

  aboutToDisappear() {
    console.info('BuilderNode aboutToDisappear');
  }
}

// 自定义挂载事件的自定义组件，作为TestComponent1的子组件与TestComponent3、TestComponent4的父组件
@Component
struct TestComponent2 {
  private myNodeController: MyNodeController = new MyNodeController(wrapBuilder(buildComponent3));
  private myNodeController2: MyNodeController = new MyNodeController(wrapBuilder(buildComponent4));

  build() {
    Column() {
      Text('This is a BuilderNode 2.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
      NodeContainer(this.myNodeController)
      NodeContainer(this.myNodeController2)
    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('BuilderNode 2 aboutToAppear');
  }

  aboutToDisappear() {
    console.info('BuilderNode 2 aboutToDisappear');
  }
}

// 自定义挂载事件的自定义组件，作为buildComponent2的子组件
@Component
struct TestComponent3 {
  build() {
    Column() {
      Text('This is a BuilderNode 3.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)

    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('BuilderNode 3 aboutToAppear');
  }

  aboutToDisappear() {
    console.info('BuilderNode 3 aboutToDisappear');
  }
}

// 自定义挂载事件的自定义组件，作为buildComponent2的子组件
@Component
struct TestComponent4 {
  build() {
    Column() {
      Text('This is a BuilderNode 4.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)

    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('BuilderNode 4 aboutToAppear');
  }

  aboutToDisappear() {
    console.info('BuilderNode 4 aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

@Builder
function buildComponent2() {
  TestComponent2()
}

@Builder
function buildComponent3() {
  TestComponent3()
}

@Builder
function buildComponent4() {
  TestComponent4()
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: BuilderNode<[]> | null = null;
  private wrappedBuilder: WrappedBuilder<[]>;

  constructor(builder: WrappedBuilder<[]>) {
    super();
    this.wrappedBuilder = builder;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(this.wrappedBuilder);

    return this.builderNode.getFrameNode();
  }

  dispose() {
    if (this.builderNode !== null) {
      // 下树并递归释放当前节点为根的子树
      this.builderNode.getFrameNode()?.disposeTree()
    }
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController(wrapBuilder(buildComponent));

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('BuilderNode dispose')
        .onClick(() => {
          this.myNodeController.dispose();
        })
        .width('100%')
      Button('BuilderNode rebuild')
        .onClick(() => {
          this.myNodeController.rebuild();
        })
        .width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/R2WEiZUVSV-7-K7ZCWXTBA/zh-cn_image_0000002742124729.gif)

### setCrossLanguageOptions15+

setCrossLanguageOptions(options: CrossLanguageOptions): void

设置当前FrameNode的跨ArkTS语言访问选项。例如ArkTS语言创建的节点，设置该节点是否可通过非ArkTS语言进行属性设置，从API版本26.0.0开始支持设置是否可通过非ArkTS语言进行组件树操作。当前FrameNode如果不可修改或不可设置跨ArkTS语言访问选项，抛出异常信息。

**说明** 

当前仅支持[Scroll](js-apis-arkui-framenode.md#scroll12)、[Swiper](js-apis-arkui-framenode.md#swiper12)、[List](js-apis-arkui-framenode.md#list12)、[ListItem](js-apis-arkui-framenode.md#listitem12)、[ListItemGroup](js-apis-arkui-framenode.md#listitemgroup12)、[WaterFlow](js-apis-arkui-framenode.md#waterflow12)、[FlowItem](js-apis-arkui-framenode.md#flowitem12)、[Grid](js-apis-arkui-framenode.md#grid14)、[GridItem](js-apis-arkui-framenode.md#griditem14)、[TextInput](js-apis-arkui-framenode.md#textinput12)、[TextArea](js-apis-arkui-framenode.md#textarea14)、[Column](js-apis-arkui-framenode.md#column12)、[Row](js-apis-arkui-framenode.md#row12)、[Stack](js-apis-arkui-framenode.md#stack12)、[Flex](js-apis-arkui-framenode.md#flex12)、[RelativeContainer](js-apis-arkui-framenode.md#relativecontainer12)、[Progress](js-apis-arkui-framenode.md#progress12)、[LoadingProgress](js-apis-arkui-framenode.md#loadingprogress12)、[Image](js-apis-arkui-framenode.md#image12)、[Button](js-apis-arkui-framenode.md#button12)、[Checkbox](js-apis-arkui-framenode.md#checkbox18)、[Radio](js-apis-arkui-framenode.md#radio18)、[Slider](js-apis-arkui-framenode.md#slider18)、[Toggle](js-apis-arkui-framenode.md#toggle18)、[XComponent](js-apis-arkui-framenode.md#xcomponent12)类型的[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)设置跨ArkTS语言访问选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getCrossLanguageOptions(): CrossLanguageOptions

获取当前FrameNode的跨ArkTS语言访问选项。例如ArkTS语言创建的节点，返回该节点是否可通过非ArkTS语言进行属性设置和跨语言组件树操作，从API版本26.0.0开始支持获取是否可通过非ArkTS语言进行组件树操作。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CrossLanguageOptions](js-apis-arkui-framenode.md#crosslanguageoptions15) | 跨ArkTS语言访问选项。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### getInteractionEventBindingInfo19+

getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined

获取目标节点的事件绑定信息，如果该组件节点上没有绑定要查询的交互事件类型时，返回 undefined。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | [EventQueryType](ts-appendix-enums.md#eventquerytype19) | 是 | 要查询的交互事件类型。例如EventQueryType.ON\_CLICK表示查询点击事件的绑定信息，各枚举值的具体含义请参考[EventQueryType](ts-appendix-enums.md#eventquerytype19)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InteractionEventBindingInfo](js-apis-arkui-framenode.md#interactioneventbindinginfo19) | undefined | 如果当前节点上绑定了所查询类型的交互事件，则返回一个InteractionEventBindingInfo对象，指示事件绑定详细信息，如果没有绑定所查询类型的交互事件则返回undefined。 |

**示例：**

请参考[节点操作示例](js-apis-arkui-framenode.md#节点操作示例)。

### recycle18+

recycle(): void

全局复用场景下，触发子组件回收，彻底释放FrameNode后端资源，以便于通过[reuse](js-apis-arkui-framenode.md#reuse18)方法实现资源的重新复用，确保后端资源能够被有效回收并再次使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[节点复用回收使用示例](js-apis-arkui-framenode.md#节点复用回收使用示例)。

### reuse18+

reuse(): void

全局复用场景下，触发子组件复用，实现FrameNode后端资源的复用，提升资源利用效率。为保证资源充足，可以在recycle之后使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[节点复用回收使用示例](js-apis-arkui-framenode.md#节点复用回收使用示例)。

### addSupportedUIStates20+

addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void

设置组件支持的多态样式状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiStates | number | 是 | 需要处理目标节点的UI状态。  可以通过位或计算同时指定多个状态，如：targetUIStates = UIState.PRESSED | UIState.FOCUSED。 |
| statesChangeHandler | [UIStatesChangeHandler](js-apis-arkui-framenode.md#uistateschangehandler20) | 是 | 状态变化时的回调函数。 |
| excludeInner | boolean | 否 | 禁止内部默认状态样式处理的标志，默认值为false。内部默认状态样式处理指组件自身内置的状态样式响应（如Button按下时的默认视觉反馈）。  true表示禁止内部默认状态样式处理，false不禁止内部默认状态样式处理。 |

**示例：**

请参考[组件设置和删除多态样式状态示例](js-apis-arkui-framenode.md#组件设置和删除多态样式状态示例)。

### removeSupportedUIStates20+

removeSupportedUIStates(uiStates: number): void

删除组件当前注册的状态处理。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiStates | number | 是 | 需要删除的UI状态。  可以通过位或计算同时指定删除多个状态，如：removeUIStates = UIState.PRESSED | UIState.FOCUSED。 |

**示例：**

请参考[组件设置和删除多态样式状态示例](js-apis-arkui-framenode.md#组件设置和删除多态样式状态示例)。

### createAnimation20+

createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean

创建FrameNode上属性的动画。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [AnimationPropertyType](ts-appendix-enums.md#animationpropertytype20) | 是 | 动画属性枚举。 |
| startValue | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number[]> | 是 | 动画属性的起始值。取值为undefined或数组，取值为数组时数组长度需要和属性枚举匹配。如果为undefined则表示不显式指定动画初值，节点上一次设置的属性终值为此次动画的起点值。如果取值为数组，  - 对于AnimationPropertyType.ROTATION，取值格式为[rotationX, rotationY, rotationZ]，单位为度（°），表示绕x、y、z轴的旋转角。  - 对于AnimationPropertyType.TRANSLATION，取值格式为[translateX, translateY]，单位为px，表示沿x、y轴的平移量。  - 对于AnimationPropertyType.SCALE，取值格式为[scaleX, scaleY]，表示x、y方向的缩放比例。  - 对于AnimationPropertyType.OPACITY，取值格式为[opacity]，表示不透明度。opacity的取值范围为[0, 1]，超出范围的值会被钳位到[0, 1]，动画正常创建。  当节点上从未设置过该属性时，需要显式指定startValue才能正常创建动画。当节点上已经设置过属性（如第二次及之后创建动画），则推荐不显式指定startValue或者显式指定startValue为上一次的终值，表示使用上一次的终值作为新的动画起点，避免起始值跳变。 |
| endValue | number[] | 是 | 动画属性的终止值。取值为数组，数组长度需要和属性枚举匹配。  - 对于AnimationPropertyType.ROTATION，取值格式为[rotationX, rotationY, rotationZ]，单位为度（°），表示绕x、y、z轴的旋转角。  - 对于AnimationPropertyType.TRANSLATION，取值格式为[translateX, translateY]，单位为px，表示沿x、y轴的平移量。  - 对于AnimationPropertyType.SCALE，取值格式为[scaleX, scaleY]，表示x、y方向的缩放比例。  - 对于AnimationPropertyType.OPACITY，取值格式为[opacity]，表示不透明度。opacity的取值范围为[0, 1]，超出范围的值会被钳位到[0, 1]，动画正常创建。 |
| param | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 动画参数。包含时长、动画曲线、结束回调等参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示动画是否创建成功。  返回值为true：动画创建成功，如果动画参数中设置结束回调，动画结束后会调用结束回调。  返回值为false：动画创建失败，即使动画参数中设置结束回调，结束回调也不会被调用。  可能导致动画创建失败的原因：  1. 节点已经释放，调用过[dispose](js-apis-arkui-framenode.md#dispose12)方法。  2. 对于系统组件的代理节点，即对于[isModifiable](js-apis-arkui-framenode.md#ismodifiable12)为false的节点，调用该接口会失败。  3. 属性枚举非法，或属性枚举需要的长度与startValue或endValue的长度不匹配。  4. 该属性在第一次创建动画时没有显式指定startValue导致没有动画起点值，或设置的动画终值和动画起始值（当startValue为undefined时动画起始值为上一次的终值）相同，此时无动画产生。 |

**示例：**

请参考[动画创建与取消示例](js-apis-arkui-framenode.md#动画创建与取消示例)。

### cancelAnimations20+

cancelAnimations(properties: AnimationPropertyType[]): boolean

请求取消FrameNode上指定属性上的所有动画，该方法需在节点所处线程中调用，会阻塞当前线程以等待取消结果。如果动画成功取消，节点上的属性值会被恢复为取消时的显示值（即当前状态）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | [AnimationPropertyType](ts-appendix-enums.md#animationpropertytype20)[] | 是 | 待取消的动画属性枚举数组。可以一次取消一个节点上的多个属性的动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示动画是否取消成功。  返回值为true：动画取消成功。  返回值为false：动画取消失败。  可能导致动画取消失败的原因：  1. 节点已经释放，调用过[dispose](js-apis-arkui-framenode.md#dispose12)方法。  2. 对于系统组件的代理节点，即对于[isModifiable](js-apis-arkui-framenode.md#ismodifiable12)为false的节点，调用该接口会失败。  3. 属性枚举数组存在非法枚举值。  4. 系统异常。如发生ipc异常导致动画取消失败。  补充说明：  1. 即使属性上没有动画，尝试取消该属性的动画，在无系统异常情况下调用取消接口也会返回true。  2. 如果开发者保证传入参数合法且节点正常，返回false时表明发生了系统异常。此时开发者可隔一段时间后再次尝试取消，或通过调用duration为0的[createAnimation](js-apis-arkui-framenode.md#createanimation20)接口停止属性上的动画。 |

**示例：**

请参考[动画创建与取消示例](js-apis-arkui-framenode.md#动画创建与取消示例)。

### getNodePropertyValue20+

getNodePropertyValue(property: AnimationPropertyType): number[]

获取FrameNode上的属性值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [AnimationPropertyType](ts-appendix-enums.md#animationpropertytype20) | 是 | 动画属性枚举。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 表示FrameNode上的属性值，返回的数组长度与属性枚举相关，异常时返回空数组。  对不同属性枚举的返回值格式：  - 当节点已经释放，调用过[dispose](js-apis-arkui-framenode.md#dispose12)方法，或者属性枚举非法时，返回长度为0的空数组。  - 对于AnimationPropertyType.ROTATION，返回值为[rotationX, rotationY, rotationZ]，单位为度（°），表示绕x、y、z轴的旋转角。  - 对于AnimationPropertyType.TRANSLATION，返回值为[translateX, translateY]，单位为px，表示沿x、y轴的平移量。  - 对于AnimationPropertyType.SCALE，返回值为[scaleX, scaleY]，表示x、y方向的缩放比例。  - 对于AnimationPropertyType.OPACITY，返回值为[opacity]，表示不透明度。  1. 动画正常取消后，节点上的属性值被恢复为取消时的值，通过该接口可以获取取消后的显示值。  2. 动画期间该接口的返回值为该属性的终值，而不是动画过程的实时值。 |

**示例：**

请参考[动画创建与取消示例](js-apis-arkui-framenode.md#动画创建与取消示例)。

### invalidateAttributes21+

invalidateAttributes(): void

在当前帧触发节点属性更新。

当前节点的属性在构建阶段后被修改，这些改动不会立即生效，而是延迟到下一帧统一处理。

此功能强制当前帧内即时节点更新，确保同步应用渲染效果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

从API version 21开始，通过if else动态切换两个节点，并且在节点创建时调用invalidateAttributes即时触发节点属性更新，避免组件切换过程中出现闪烁。

```ts
// index.ets
import { FrameNode, NodeController, typeNode, NodeContent } from '@kit.ArkUI';

// 继承NodeController实现自定义NodeAdapter控制器
class MyNodeAdapterController extends NodeController {
  rootNode: FrameNode | null = null;
  imageUrl: string = '';

  constructor(imageUrl: string) {
    super();
    this.imageUrl = imageUrl;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode.initialize($r(this.imageUrl))
    imageNode.attribute.syncLoad(true).width(100).height(100);
    // 强制当前帧内即时节点更新，避免出现切换闪烁
    imageNode.invalidateAttributes();
    return imageNode;
  }
}

// 自定义挂载事件的自定义组件，挂载前加载样例图片
@Component
struct NodeComponent3 {
  private rootSlot: NodeContent = new NodeContent();

  aboutToAppear(): void {
    const uiContext = this.getUIContext();
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode.initialize($r('app.media.startIcon'))
    imageNode.attribute.syncLoad(true).width(100).height(100);
    imageNode.invalidateAttributes();
    this.rootSlot.addFrameNode(imageNode);
  }

  build() {
    ContentSlot(this.rootSlot)
  }
}

// 自定义挂载事件的自定义组件，挂载前加载样例图片
@Component
struct NodeComponent4 {
  private rootSlot: NodeContent = new NodeContent();

  aboutToAppear(): void {
    const uiContext = this.getUIContext();
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode.initialize($r('app.media.startIcon'))
    imageNode.attribute.syncLoad(true).width(100).height(100);
    imageNode.invalidateAttributes();
    this.rootSlot.addFrameNode(imageNode);
  }

  build() {
    ContentSlot(this.rootSlot)
  }
}

@Entry
@Component
struct ListNodeTest {
  @State flag: boolean = true;
  adapterController: MyNodeAdapterController = new MyNodeAdapterController('app.media.startIcon');

  build() {
    Column() {
      Text('ListNode Adapter');
      if (this.flag) {
        NodeComponent3()
      } else {
        NodeComponent4()
      }
      if (this.flag) {
        NodeContainer(this.adapterController)
          .width(300).height(300)
          .borderWidth(1).borderColor(Color.Black)
      } else {
        NodeContainer(this.adapterController)
          .width(300).height(300)
          .borderWidth(1).borderColor(Color.Black)
      }
      if (this.flag) {
        Image($r('app.media.startIcon')).width(100).height(100).syncLoad(true)
      } else {
        Image($r('app.media.startIcon')).width(100).height(100).syncLoad(true)
      }
      Button('change').onClick(() => {
        this.flag = !this.flag;
      })
    }
    .borderWidth(1)
    .width('100%')
  }
}
```

### adoptChild22+

adoptChild(child: FrameNode): void

当前节点接纳目标节点为附属节点。当前FrameNode如果不可修改，抛出异常信息。被接纳的附属节点不能已有父节点。调用该接口实际上不会将目标节点添加为子节点，而是仅允许当前节点接收该附属节点的生命周期回调。使用场景：当需要监听某个节点的生命周期回调但不希望改变其父子关系或组件树结构时，可通过该接口接纳其为附属节点。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 指定待被接纳的节点。child节点不可以拥有父节点，否则抛出异常信息。 |

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

removeAdoptedChild(child: FrameNode): void

移除被接纳的目标附属节点。当前FrameNode如果不可修改，抛出异常信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 已被接纳的目标附属节点。 |

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

convertPosition(position: Position, targetNode: FrameNode): Position

将点的坐标从当前节点的坐标系转换为目标节点的坐标系。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 当前节点坐标系中的相对坐标。单位为VP。 |
| targetNode | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 本次坐标转换的目标节点，转换得到的点坐标就是该节点坐标系中的相对坐标。targetNode节点不可以为已释放的节点，且需与当前节点存在共同祖先节点，否则抛出异常信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 目标节点局部坐标系中的转换坐标，单位为VP。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100024 | The current FrameNode and the target FrameNode do not have a common ancestor node. |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'targetNode' is invalid: it cannot be disposed." |

**示例：**

```ts
@Entry
@Component
struct ConvertPositionTestOnly {
  private uiContext: UIContext = this.getUIContext();
  @State message: string = 'Hello World';
  @State nodeAOk: boolean = false;
  @State nodeBOk: boolean = false;

  build() {
    Column() {
      Text(this.message)
        .id('testNodeA')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .onAppear(() => {
          this.nodeAOk = true
        })
      Column() {
        Text('testNodeB')
          .id('testNodeB')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onAppear(() => {
            this.nodeBOk = true
          })

      }

      Button('运行convertPosition测试')
        .onClick(() => {
          this.runBasicTest();
        })
        .margin(20)

    }
    .width('100%')
    .height('100%')
  }

  private runBasicTest() {
    if (!this.nodeAOk || !this.nodeBOk) {
      return
    }

    // 等待UI渲染完成
    if (!this.uiContext) {
      return
    }
    const nodeA = this.uiContext.getAttachedFrameNodeById('testNodeA');
    const nodeB = this.uiContext.getAttachedFrameNodeById('testNodeB');

    if (!nodeA || !nodeB) {
      console.info('无法获取测试节点');
      return;
    }

    const result: Position | undefined = nodeA.convertPosition({ x: 30, y: 10 }, nodeB); // 显式声明可能返回undefined
    if (result === undefined) {
      console.info('convertPosition 转换失败，返回 undefined');
      return;
    }
    console.info(`输出: (${result.x}, ${result.y})`);

  }
}
```

### isInRenderState23+

isInRenderState(): boolean

获取节点是否处于渲染状态，如果一个节点的对应RenderNode在渲染树上，则处于渲染状态。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 节点是否处于渲染状态。  true：处于渲染状态；false：不处于渲染状态。 |

**示例：**

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'is on render tree';
  @State @Watch('change') isShow: boolean = true;
  data: Array<string> = ['hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7', 'hello8'];

  // 监听状态变化后打印是否处于渲染状态
  change() {
    let buttonNode = this.getUIContext().getFrameNodeById('testButton');
    if (buttonNode == null) {
      return;
    }
    let isOnRenderTree = buttonNode!.isInRenderState();
    if (isOnRenderTree) {
      hilog.info(1, 'frameNode', 'is on render tree');
    } else {
      hilog.info(1, 'frameNode', 'is not on render tree');
    }
  }

  build() {
    Column() {
      Button('change button visibility').onClick(() => {
        // 修改button的visibility状态
        this.isShow = !this.isShow;
      })
        .margin({ top: 20 })
      Button('test button')
        .visibility(this.isShow ? Visibility.Visible : Visibility.Hidden)
        .margin(20).id('testButton')

      List() {
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item).id(item)
          }.alignSelf(ItemAlign.Center).width('100%')
        })
      }
      .width('30%')
      .alignSelf(ItemAlign.Center)
      .height('10%')
      .onReachEnd(() => {
        let textNode8 = this.getUIContext().getFrameNodeById('hello8');
        if (textNode8 != null) {
          let isOnRenderTree = textNode8!.isInRenderState();
          hilog.info(1, 'frameNode', 'is hello8 on RenderTree: %{public}s', isOnRenderTree);
        }
        let textNode1 = this.getUIContext().getFrameNodeById('hello1');
        if (textNode1 != null) {
          let isOnRenderTree = textNode1!.isInRenderState();
          if (isOnRenderTree) { this.message = 'is on render tree'; }
          hilog.info(1, 'frameNode', 'is hello1 on RenderTree: %{public}s', isOnRenderTree);
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

### isOnMainTree23+

isOnMainTree(): boolean

查询节点是否被挂载到主节点树上。与[isAttached](js-apis-arkui-framenode.md#isattached12)均用于判断节点是否挂载到主节点树上，区别在于本接口在节点已调用[dispose](js-apis-arkui-framenode.md#dispose12)解除引用时会抛出错误码100026，开发者可根据是否需要节点dispose时的错误码校验（即抛出错误码100026）来选择使用本接口或[isAttached](js-apis-arkui-framenode.md#isattached12)接口。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, UIContext, typeNode } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

const TEST_TAG: string = 'FrameNode ';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  public childList: Array<FrameNode> = new Array<FrameNode>();
  private rootNode: FrameNode | null = null;
  private uiContext: UIContext | null = null;
  private childrenCount: number = 0;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.uiContext = uiContext;

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.addCommonEvent(this.frameNode)
    this.rootNode.appendChild(this.frameNode);
    this.childrenCount = this.childrenCount + 1;
    for (let i = 0; i < 10; i++) {
      let childNode = new FrameNode(uiContext);
      this.childList.push(childNode);
      this.frameNode.appendChild(childNode);
    }
    let stackNode = typeNode.createNode(uiContext, 'Stack');
    this.frameNode.appendChild(stackNode);
    return this.rootNode;
  }

  addCommonEvent(frameNode: FrameNode) {
    frameNode.commonEvent.setOnClick((event: ClickEvent) => {
      console.info(`Click FrameNode: ${JSON.stringify(event)}`)
    })
  }

  createFrameNode() {
    let frameNode = new FrameNode(this.uiContext!);
    frameNode.commonAttribute.backgroundColor(Color.Pink);
    frameNode.commonAttribute.size({ width: 100, height: 100 });
    frameNode.commonAttribute.position({ x: this.childrenCount * 120, y: 0 });

    return frameNode;
  }

  appendChild() {
    const childNode = this.createFrameNode();
    this.rootNode!.appendChild(childNode);
    this.childrenCount = this.childrenCount + 1;
  }

  insertChildAfter(index: number) {
    let insertNode = this.createFrameNode();
    let childNode = this.rootNode!.getChild(index);
    this.rootNode!.insertChildAfter(insertNode, childNode);
    this.childrenCount = this.childrenCount + 1;
  }

  removeChild(index: number) {
    let childNode = this.rootNode!.getChild(index);
    if (childNode == null) {
      console.info(`${TEST_TAG} getchild at index {${index}} : fail`);
      return;
    }
    this.rootNode!.removeChild(childNode);
    this.childrenCount = this.childrenCount - 1;
  }

  getChildNumber() {
    console.info(`${TEST_TAG} getChildNumber ${this.rootNode!.getChildrenCount()}`)
    console.info(`${TEST_TAG} children count is ${this.childrenCount}`);
  }

  clearChildren() {
    this.rootNode!.clearChildren();
  }

  searchFrameNode() {
    if (this.rootNode!.getFirstChild() === null) {
      console.info(`${TEST_TAG} the rootNode does not have child node.`)
    }
    if (this.rootNode!.getFirstChild() === this.frameNode) {
      console.info(`${TEST_TAG} getFirstChild result: success. The first child of the rootNode is equals to frameNode.`);
    } else {
      console.info(`${TEST_TAG} getFirstChild result: fail. The first child of the rootNode is not equals to frameNode.`);
    }
    if (this.frameNode!.getChild(5) === this.frameNode!.getChild(4)!.getNextSibling()) {
      console.info(`${TEST_TAG} getNextSibling result: success.`);
    } else {
      console.info(`${TEST_TAG} getNextSibling result: fail.`);
    }
    if (this.frameNode!.getChild(3) === this.frameNode!.getChild(4)!.getPreviousSibling()) {
      console.info(`${TEST_TAG} getPreviousSibling result: success.`);
    } else {
      console.info(`${TEST_TAG} getPreviousSibling result: fail.`);
    }
    if (this.rootNode!.getFirstChild() !== null && this.rootNode!.getFirstChild()!.getParent() === this.rootNode) {
      console.info(`${TEST_TAG} getParent result: success.`);
    } else {
      console.info(`${TEST_TAG} getParent result: fail.`);
    }
    if (this.rootNode!.getParent() !== null) {
      console.info(`${TEST_TAG} get ArkTsNode success.`)
      console.info(`${TEST_TAG} check rootNode whether is modifiable ${this.rootNode!.isModifiable()}`)
      console.info(`${TEST_TAG} check getParent whether is modifiable ${this.rootNode!.getParent()!.isModifiable()}`)
    } else {
      console.info(`${TEST_TAG} get ArkTsNode fail.`);
    }
  }

  moveFrameNode() {
    const currentNode = this.frameNode!.getChild(10);
    try {
      currentNode!.moveTo(this.rootNode, 0);
      if (this.rootNode!.getChild(0) === currentNode) {
        console.info(`${TEST_TAG} moveTo result: success.`);
      } else {
        console.info(`${TEST_TAG} moveTo result: fail.`);
      }
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
      console.error(`${TEST_TAG} moveTo result: fail.`);
    }
  }

  getPositionToWindow() {
    let positionToWindow = this.rootNode?.getPositionToWindow();
    console.info(`${TEST_TAG}${JSON.stringify(positionToWindow)}`);
  }

  getPositionToParent() {
    let positionToParent = this.rootNode?.getPositionToParent();
    console.info(`${TEST_TAG}${JSON.stringify(positionToParent)}`);
  }

  getPositionToScreen() {
    let positionToScreen = this.rootNode?.getPositionToScreen();
    console.info(`${TEST_TAG}${JSON.stringify(positionToScreen)}`);
  }

  getGlobalPositionOnDisplay() {
    let positionOnGlobalDisplay = this.rootNode?.getGlobalPositionOnDisplay();
    console.info(`${TEST_TAG}${JSON.stringify(positionOnGlobalDisplay)}`);
  }

  getPositionToWindowWithTransform() {
    let positionToWindowWithTransform = this.rootNode?.getPositionToWindowWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToWindowWithTransform)}`);
  }

  getPositionToParentWithTransform() {
    let positionToParentWithTransform = this.rootNode?.getPositionToParentWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToParentWithTransform)}`);
  }

  getPositionToScreenWithTransform() {
    let positionToScreenWithTransform = this.rootNode?.getPositionToScreenWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToScreenWithTransform)}`);
  }

  getMeasuredSize() {
    let measuredSize = this.frameNode?.getMeasuredSize();
    console.info(`${TEST_TAG}${JSON.stringify(measuredSize)}`);
  }

  getLayoutPosition() {
    let layoutPosition = this.frameNode?.getLayoutPosition();
    console.info(`${TEST_TAG}${JSON.stringify(layoutPosition)}`);
  }

  getUserConfigBorderWidth() {
    let userConfigBorderWidth = this.frameNode?.getUserConfigBorderWidth();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigBorderWidth)}`);
  }

  getUserConfigPadding() {
    let userConfigPadding = this.frameNode?.getUserConfigPadding();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigPadding)}`);
  }

  getUserConfigMargin() {
    let userConfigMargin = this.frameNode?.getUserConfigMargin();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigMargin)}`);
  }

  getUserConfigSize() {
    let userConfigSize = this.frameNode?.getUserConfigSize();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigSize)}`);
  }

  getId() {
    let id = this.frameNode?.getId();
    console.info(`${TEST_TAG}${id}`);
  }

  getUniqueId() {
    let uniqueId = this.frameNode?.getUniqueId();
    console.info(`${TEST_TAG}${uniqueId}`);
  }

  getNodeType() {
    let nodeType = this.frameNode?.getNodeType();
    console.info(`${TEST_TAG}${nodeType}`);
  }

  getOpacity() {
    let opacity = this.frameNode?.getOpacity();
    console.info(`${TEST_TAG}${JSON.stringify(opacity)}`);
  }

  isVisible() {
    let visible = this.frameNode?.isVisible();
    console.info(`${TEST_TAG}${JSON.stringify(visible)}`);
  }

  isClipToFrame() {
    let clipToFrame = this.frameNode?.isClipToFrame();
    console.info(`${TEST_TAG}${JSON.stringify(clipToFrame)}`);
  }

  isAttached() {
    let attached = this.frameNode?.isAttached();
    console.info(`${TEST_TAG}${JSON.stringify(attached)}`);
  }

  isOnMainTree() {
    let attached = this.frameNode?.isOnMainTree();
    console.info(`${TEST_TAG}${JSON.stringify(attached)}`);
  }

  getInspectorInfo() {
    let inspectorInfo = this.frameNode?.getInspectorInfo();
    console.info(`${TEST_TAG}${JSON.stringify(inspectorInfo)}`);
  }

  setCrossLanguageOptions() {
    console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions())}`);
    try {
      this.frameNode?.setCrossLanguageOptions({
        attributeSetting: true
      });
      console.info(`${TEST_TAG} setCrossLanguageOptions success.`);
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
      console.error(`${TEST_TAG} setCrossLanguageOptions fail.`);
    }
    console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions())}`);
  }

  getInteractionEventBindingInfo() {
    let bindingInfo = this.frameNode?.getInteractionEventBindingInfo(EventQueryType.ON_CLICK);
    console.info(`${TEST_TAG}${bindingInfo?.baseEventRegistered}`);
    console.info(`${TEST_TAG}${bindingInfo?.nodeEventRegistered}`);
    console.info(`${TEST_TAG}${bindingInfo?.nativeEventRegistered}`);
    console.info(`${TEST_TAG}${bindingInfo?.builtInEventRegistered}`);
    console.info(`${TEST_TAG}${JSON.stringify(bindingInfo)}`);
  }

  throwError() {
    try {
      this.rootNode!.getParent()!.clearChildren();
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
    }
    try {
      this.rootNode!.getParent()!.appendChild(new FrameNode(this.uiContext));
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
    }
    try {
      this.rootNode!.getParent()!.removeChild(this.rootNode!.getParent()!.getChild(0));
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();
  @State index: number = 0;

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Row() {
            Button('ADD')
              .onClick(() => {
                this.index++;
              })
            Button('DEC')
              .onClick(() => {
                this.index--;
              })
          }

          Text('Current index is ' + this.index)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
        }

        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('appendChild')
          .width(300)
          .onClick(() => {
            this.myNodeController.appendChild();
          })
        Button('insertChildAfter')
          .width(300)
          .onClick(() => {
            this.myNodeController.insertChildAfter(this.index);
          })
        Button('removeChild')
          .width(300)
          .onClick(() => {
            this.myNodeController.removeChild(this.index);
          })
        Button('clearChildren')
          .width(300)
          .onClick(() => {
            this.myNodeController.clearChildren();
          })
        Button('getChildNumber')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildNumber();
          })
        Button('searchFrameNode')
          .width(300)
          .onClick(() => {
            this.myNodeController.searchFrameNode();
          })
        Button('moveFrameNode')
          .width(300)
          .onClick(() => {
            this.myNodeController.moveFrameNode();
          })
        Button('getPositionToWindow')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToWindow();
          })
        Button('getPositionToParent')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToParent();
          })
        Button('getPositionToScreen')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToScreen();
          })
        Button('getGlobalPositionOnDisplay')
          .width(300)
          .onClick(() => {
            this.myNodeController.getGlobalPositionOnDisplay();
          })
        Button('getPositionToParentWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToParentWithTransform();
          })
        Button('getPositionToWindowWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToWindowWithTransform();
          })
        Button('getPositionToScreenWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToScreenWithTransform();
          })
        Button('getMeasuredSize')
          .width(300)
          .onClick(() => {
            this.myNodeController.getMeasuredSize();
          })
        Button('getLayoutPosition')
          .width(300)
          .onClick(() => {
            this.myNodeController.getLayoutPosition();
          })
        Button('getUserConfigBorderWidth')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigBorderWidth();
          })
        Button('getUserConfigPadding')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigPadding();
          })
        Button('getUserConfigMargin')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigMargin();
          })
        Button('getUserConfigSize')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigSize();
          })
        Button('getId')
          .width(300)
          .onClick(() => {
            this.myNodeController.getId();
          })
        Button('getUniqueId')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUniqueId();
          })
        Button('getNodeType')
          .width(300)
          .onClick(() => {
            this.myNodeController.getNodeType();
          })
        Button('getOpacity')
          .width(300)
          .onClick(() => {
            this.myNodeController.getOpacity();
          })
        Button('isVisible')
          .width(300)
          .onClick(() => {
            this.myNodeController.isVisible();
          })
        Button('isClipToFrame')
          .width(300)
          .onClick(() => {
            this.myNodeController.isClipToFrame();
          })
        Button('isAttached')
          .width(300)
          .onClick(() => {
            this.myNodeController.isAttached();
          })
        Button('isOnMainTree')
          .width(300)
          .onClick(() => {
            this.myNodeController.isOnMainTree();
          })
        Button('getInspectorInfo')
          .width(300)
          .onClick(() => {
            this.myNodeController.getInspectorInfo();
          })
        Button('getCustomProperty')
          .width(300)
          .onClick(() => {
            const uiContext: UIContext = this.getUIContext();
            if (uiContext) {
              const node: FrameNode | null = uiContext.getFrameNodeById('Test_Button') || null;
              if (node) {
                for (let i = 1; i < 4; i++) {
                  const key = 'customProperty' + i;
                  const property = node.getCustomProperty(key);
                  console.info(`${TEST_TAG}${key}`, JSON.stringify(property));
                }
              }
            }
          })
          .id('Test_Button')
          .customProperty('customProperty1', {
            'number': 10,
            'string': 'this is a string',
            'bool': true,
            'object': {
              'name': 'name',
              'value': 100
            }
          })
          .customProperty('customProperty2', {})
          .customProperty('customProperty2', undefined)
        Button('setCrossLanguageOptions')
          .width(300)
          .onClick(() => {
            this.myNodeController.setCrossLanguageOptions();
          })
        Button('getInteractionEventBindingInfo')
          .width(300)
          .onClick(() => {
            this.myNodeController.getInteractionEventBindingInfo();
          })
        Button('throwError')
          .width(300)
          .onClick(() => {
            this.myNodeController.throwError();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向为纵向
  }
}
```

### convertPositionToWindow23+

convertPositionToWindow(positionByLocal: Position): Position

将点的坐标从当前节点的坐标系转换为当前节点所在窗口的坐标系。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionByLocal | [Position](js-apis-arkui-graphics.md#position) | 是 | 当前节点坐标系中的相对坐标。单位为VP。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 当前节点所在窗口的坐标系中的转换坐标，单位为VP。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100026 | The current FrameNode has been disposed. |
| 100028 | The current FrameNode is not on the main tree. |

**示例：**

请参考[局部与窗口坐标转换示例](js-apis-arkui-framenode.md#局部与窗口坐标转换示例)。

### convertPositionFromWindow23+

convertPositionFromWindow(positionByWindow: Position): Position

将点的坐标从当前节点所在窗口的坐标系转换为当前节点的坐标系。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionByWindow | [Position](js-apis-arkui-graphics.md#position) | 是 | 当前节点所在窗口的坐标系中的相对坐标。单位为VP。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 当前节点坐标系中的转换坐标，单位为VP。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100026 | The current FrameNode has been disposed. |
| 100028 | The current FrameNode is not on the main tree. |

**示例：**

请参考[局部与窗口坐标转换示例](js-apis-arkui-framenode.md#局部与窗口坐标转换示例)。

### createFrameNodes

static createFrameNodes(uiContext: UIContext, count: number): FrameNode[]

批量创建指定数量的FrameNode，返回FrameNode数组。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| count | number | 是 | 指定创建节点的数量，取值范围为大于零的整型。若给定值小于等于0或不是整数，则返回空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1)[] | 创建的FrameNode数组。 |

**示例：**

```ts
import { NodeController, FrameNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    // 创建20个FrameNode添加到根节点中。
    const children: FrameNode[] = FrameNode.createFrameNodes(uiContext, 20);
    for (let i = 0; i < children.length; i++) {
      this.rootNode.appendChild(children[i]);
    }
    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(300)
        .height(300)
    }.width('100%')
  }
}
```

### getFrameNodeById

getFrameNodeById(id: string): FrameNode | null

以当前节点为根节点，逐层查找所有子节点，返回第一个匹配指定id的节点。查找顺序为：先查找直接子节点，再查找二级子节点，依此类推，找到后立即返回。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 查询的子节点id，为通用属性设置的[组件标识](ts-universal-attributes-component-id.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 以当前节点为根节点，逐层查找所有子节点，返回第一个匹配指定id的节点。若当前节点所有的子节点中都不存在匹配该id的节点，则返回空对象null。 |

**示例：**

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;
  private id: string = 'text';

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    // 创建Column。
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    this.rootNode.appendChild(col);

    // 创建Text组件添加到Column中。
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello').id(this.id);
    col.appendChild(text);

    // 再次创建相同ID的Text组件添加到Column中。
    let text1 = typeNode.createNode(uiContext, 'Text');
    text1.initialize('World').id(this.id);
    col.appendChild(text1);
    this.update();
    return this.rootNode;
  }

  update() {
    if (this.rootNode) {
      // 查询并返回首个ID为“text”的组件，并设置backgroundColor属性。
      let node = this.rootNode.getFrameNodeById(this.id);
      node?.commonAttribute.backgroundColor('rgb(39,135,217)');
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(300)
        .height(300)
    }.width('100%')
  }
}
```

### getFrameNodeByUniqueId

getFrameNodeByUniqueId(id: number): FrameNode | null

以当前节点为根节点，查找并返回指定UniqueID（系统分配的节点唯一标识，该标识可通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)接口获取）的子节点。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 查询的子节点的唯一标识UniqueID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | null | 以当前节点为根节点，查找到指定UniqueID的子节点。若当前节点无法查找到该UniqueID的子节点，则返回空对象null。 |

**示例：**

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;
  private uniqueId: number = 0;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    // 创建Column。
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    this.rootNode.appendChild(col);

    // 创建Text组件添加到Column中。
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello');
    col.appendChild(text);

    // 再次创建Text组件添加到Column中。
    let text1 = typeNode.createNode(uiContext, 'Text');
    text1.initialize('World');
    this.uniqueId = text1.getUniqueId();
    col.appendChild(text1);
    this.update();
    return this.rootNode;
  }

  update() {
    if (this.rootNode) {
      // 查询并返回指定UniqueID的组件，并设置backgroundColor属性。
      let node = this.rootNode.getFrameNodeByUniqueId(this.uniqueId);
      node?.commonAttribute.backgroundColor('rgb(39,135,217)');
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(300)
        .height(300)
    }.width('100%')
  }
}
```

## TypedFrameNode12+

TypedFrameNode继承自[FrameNode](js-apis-arkui-framenode.md#framenode-1)，用于声明具体类型的FrameNode，支持Text、Image、Button、Column等多种组件类型，适用于通过代码动态创建具体类型组件节点的场景。

### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialize | C | 否 | 否 | 该接口用于传入对应组件的构造参数，以设置/更新组件的初始值。 |
| attribute | T | 是 | 否 | 该接口用于获取对应组件的属性设置对象，以设置/更新组件的通用、私有属性。 |

**说明** 

[commonAttribute](js-apis-arkui-framenode.md#commonattribute12)仅在FrameNode上生效，TypedFrameNode上commonAttribute行为未定义。建议使用[attribute](js-apis-arkui-framenode.md#属性)接口而非[commonAttribute](js-apis-arkui-framenode.md#commonattribute12)接口进行通用属性设置，如node.attribute.backgroundColor(Color.Pink)。

## typeNode12+

typeNode提供创建具体类型的FrameNode能力，可通过FrameNode的基础接口进行自定义的挂载，使用占位容器进行显示。适用于需要通过代码动态创建具体类型组件节点并进行自定义挂载的场景。

使用typeNode创建[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)、[Select](ts-basic-components-select.md)、[Toggle](ts-basic-components-toggle.md)节点时，当传入的[UIContext](arkts-apis-uicontext-uicontext.md)对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**示例：**

请参考[自定义具体类型节点示例](js-apis-arkui-framenode.md#自定义具体类型节点示例)。

### Text12+

type Text = TypedFrameNode<TextInterface, TextAttribute>

Text类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<TextInterface, TextAttribute> | 提供Text类型FrameNode节点。  TextInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Text组件的构造函数类型。  TextAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Text组件的属性设置对象。  TextInterface表示Text的[接口](ts-basic-components-text.md#接口)，TextAttribute表示Text的[属性](ts-basic-components-text.md#属性)。 |

### createNode('Text')12+

createNode(context: UIContext, nodeType: 'Text'): Text

创建Text类型的FrameNode节点。使用typeNode创建Text节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Text
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello').fontColor(Color.Blue).fontSize(14);
    typeNode.getAttribute(text, 'Text')?.fontWeight(FontWeight.Bold);
    col.appendChild(text);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Text sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### getAttribute('Text')20+

getAttribute(node: FrameNode, nodeType: 'Text'): TextAttribute | undefined

获取Text节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Text
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello');
    // 获取Text的属性
    typeNode.getAttribute(text, 'Text')?.fontColor(Color.Red)
    col.appendChild(text);
    // 创建另一个Text用于对比
    let text2 = typeNode.createNode(uiContext, 'Text');
    text2.initialize('world');
    col.appendChild(text2);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Text sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### bindController('Text')20+

bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void

将文本控制器[TextController](ts-basic-components-text.md#textcontroller11)绑定到[Text](js-apis-arkui-framenode.md#text12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 绑定文本控制器的目标节点。 |
| controller | [TextController](ts-basic-components-text.md#textcontroller11) | 是 | 文本控制器。 |
| nodeType | 'Text' | 是 | 绑定文本控制器的目标节点的节点类型为Text。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| 100021 | The FrameNode is not modifiable. |

**示例：**

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  // 设置TextController，可以在外部获取
  controller: TextController = new TextController()

  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Text
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello').fontColor(Color.Blue).fontSize(14);
    typeNode.getAttribute(text, 'Text')?.fontWeight(FontWeight.Bold)
    // 绑定TextController
    typeNode.bindController(text, this.controller, 'Text');
    col.appendChild(text);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  @State line: number = 0
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Text bindController Sample')
      NodeContainer(this.myNodeController)
      Text(`Text的行数, ${this.line}`)
      Button(`点击获取行数`)
        .onClick(() => {
          this.line = this.myNodeController.controller.getLayoutManager().getLineCount()
        })
    }
  }
}
```

### Column12+

type Column = TypedFrameNode<ColumnInterface, ColumnAttribute>

Column类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ColumnInterface, ColumnAttribute> | 提供Column类型FrameNode节点。  ColumnInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Column组件的构造函数类型。  ColumnAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Column组件的属性设置对象。  ColumnInterface表示Column的[接口](ts-container-column.md#接口)，ColumnAttribute表示Column的[属性](ts-container-column.md#属性)。 |

### createNode('Column')12+

createNode(context: UIContext, nodeType: 'Column'): Column

创建Column类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Column控制器
class MyColumnController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute
    // 创建Column
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(col)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myColumnController: MyColumnController = new MyColumnController();

  build() {
    Column({ space: 5 }) {
      Text('ColumnSample')
      NodeContainer(this.myColumnController);
    }.width('100%')
  }
}
```

### getAttribute('Column')20+

getAttribute(node: FrameNode, nodeType: 'Column'): ColumnAttribute | undefined

获取Column节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Column
    let col1 = typeNode.createNode(uiContext, 'Column');
    col1.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    // 获取Column的属性
    typeNode.getAttribute(col1, 'Column')?.backgroundColor(Color.Blue).width('100%');
    col.appendChild(col1);
    // 创建另一个Column用于对比
    let col2 = typeNode.createNode(uiContext, 'Column');
    col2.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    col.appendChild(col2);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Column sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Row12+

type Row = TypedFrameNode<RowInterface, RowAttribute>

Row类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<RowInterface, RowAttribute> | 提供Row类型FrameNode节点。  RowInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Row组件的构造函数类型。  RowAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Row组件的属性设置对象。  RowInterface表示Row的[接口](ts-container-row.md#接口)，RowAttribute表示Row的[属性](ts-container-row.md#属性)。 |

### createNode('Row')12+

createNode(context: UIContext, nodeType: 'Row'): Row

创建Row类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Row控制器
class MyRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建row
    let row = typeNode.createNode(uiContext, 'Row')
    row.initialize({ space: 5 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(row)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRowController: MyRowController = new MyRowController();

  build() {
    Column({ space: 5 }) {
      Text('RowSample')
      NodeContainer(this.myRowController);
    }.width('100%')
  }
}
```

### getAttribute('Row')20+

getAttribute(node: FrameNode, nodeType: 'Row'): RowAttribute | undefined

获取Row节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Row
    let row1 = typeNode.createNode(uiContext, 'Row');
    row1.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    // 获取Row的属性
    typeNode.getAttribute(row1, 'Row')?.backgroundColor(Color.Blue).width('100%');
    col.appendChild(row1);
    // 创建另一个Row用于对比
    let row2 = typeNode.createNode(uiContext, 'Row');
    row2.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    col.appendChild(row2);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Row sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Stack12+

type Stack = TypedFrameNode<StackInterface, StackAttribute>

Stack类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<StackInterface, StackAttribute> | 提供Stack类型FrameNode节点。  StackInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Stack组件的构造函数类型。  StackAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Stack组件的属性设置对象。  StackInterface表示Stack的[接口](ts-container-stack.md#接口)，StackAttribute表示Stack的[属性](ts-container-stack.md#属性)。 |

### createNode('Stack')12+

createNode(context: UIContext, nodeType: 'Stack'): Stack

创建Stack类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Stack控制器
class MyStackController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建Stack
    let stack = typeNode.createNode(uiContext, 'Stack')
    stack.initialize({ alignContent: Alignment.Top })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(stack)
    let text = typeNode.createNode(uiContext, 'Text')
    text.initialize('This is Text')
    // 向stack添加text
    stack.appendChild(text)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myStackController: MyStackController = new MyStackController();

  build() {
    Column({ space: 5 }) {
      Text('StackSample')
      NodeContainer(this.myStackController);
    }.width('100%')
  }
}
```

### getAttribute('Stack')20+

getAttribute(node: FrameNode, nodeType: 'Stack'): StackAttribute | undefined

获取Stack节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Stack
    let stack1 = typeNode.createNode(uiContext, 'Stack');
    stack1.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    // 获取Stack的属性
    typeNode.getAttribute(stack1, 'Stack')?.backgroundColor(Color.Blue).width('100%')
    col.appendChild(stack1);
    // 创建另一个Stack用于对比
    let stack2 = typeNode.createNode(uiContext, 'Stack');
    stack2.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    col.appendChild(stack2);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Row sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### GridRow12+

type GridRow = TypedFrameNode<GridRowInterface, GridRowAttribute>

GridRow类型的FrameNode节点类型。只允许添加GridCol类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<GridRowInterface, GridRowAttribute> | 提供GridRow类型FrameNode节点。  GridRowInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为GridRow组件的构造函数类型。  GridRowAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回GridRow组件的属性设置对象。  GridRowInterface表示GridRow的[接口](ts-container-gridrow.md#接口)，GridRowAttribute表示GridRow的[属性](ts-container-gridrow.md#属性)。 |

### createNode('GridRow')12+

createNode(context: UIContext, nodeType: 'GridRow'): GridRow

创建GridRow类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义GridRow控制器
class MyGridRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建GridRow
    let gridRow = typeNode.createNode(uiContext, 'GridRow')
    gridRow.initialize({ columns: 12 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(gridRow)
    // 创建GridCol
    let gridCol = typeNode.createNode(uiContext, 'GridCol')
    gridCol.initialize({ span: 2, offset: 4 })
      .height('100%')
      .backgroundColor(Color.Red)
    // 向gridRow添加gridCol
    gridRow.appendChild(gridCol)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myGridRowController: MyGridRowController = new MyGridRowController();

  build() {
    Column({ space: 5 }) {
      Text('GridRowSample')
      NodeContainer(this.myGridRowController);
    }.width('100%')
  }
}
```

### GridCol12+

type GridCol = TypedFrameNode<GridColInterface, GridColAttribute>

GridCol类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<GridColInterface, GridColAttribute> | 提供GridCol类型FrameNode节点。  GridColInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为GridCol组件的构造函数类型。  GridColAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回GridCol组件的属性设置对象。  GridColInterface表示GridCol的[接口](ts-container-gridcol.md#接口)，GridColAttribute表示GridCol的[属性](ts-container-gridcol.md#属性)。 |

### createNode('GridCol')12+

createNode(context: UIContext, nodeType: 'GridCol'): GridCol

创建GridCol类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义GridRow控制器
class MyGridRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建GridRow
    let gridRow = typeNode.createNode(uiContext, 'GridRow')
    gridRow.initialize({ columns: 12 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(gridRow)
    // 创建GridCol
    let gridCol = typeNode.createNode(uiContext, 'GridCol')
    gridCol.initialize({ span: 2, offset: 4 })
      .height('100%')
      .backgroundColor(Color.Red)
    // 向gridRow添加gridCol
    gridRow.appendChild(gridCol)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myGridRowController: MyGridRowController = new MyGridRowController();

  build() {
    Column({ space: 5 }) {
      Text('GridColSample')
      NodeContainer(this.myGridRowController);
    }.width('100%')
  }
}
```

### Flex12+

type Flex = TypedFrameNode<FlexInterface, FlexAttribute>

Flex类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<FlexInterface, FlexAttribute> | 提供Flex类型FrameNode节点。  FlexInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Flex组件的构造函数类型。  FlexAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Flex组件的属性设置对象。  FlexInterface表示Flex的[接口](ts-container-flex.md#接口)，FlexAttribute表示Flex的[属性](ts-container-flex.md#属性)。 |

### createNode('Flex')12+

createNode(context: UIContext, nodeType: 'Flex'): Flex

创建Flex类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Flex控制器
class MyFlexController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建Flex
    let flex = typeNode.createNode(uiContext, 'Flex')
    flex.initialize()
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(flex)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myFlexController: MyFlexController = new MyFlexController();

  build() {
    Column({ space: 5 }) {
      Text('FlexSample')
      NodeContainer(this.myFlexController);
    }.width('100%')
  }
}
```

### getAttribute('Flex')20+

getAttribute(node: FrameNode, nodeType: 'Flex'): FlexAttribute | undefined

获取Flex节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Flex
    let flex1 = typeNode.createNode(uiContext, 'Flex');
    flex1.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    // 获取Flex的属性
    typeNode.getAttribute(flex1, 'Flex')?.backgroundColor(Color.Blue).width('100%')
    col.appendChild(flex1);
    // 创建另一个Flex用于对比
    let flex2 = typeNode.createNode(uiContext, 'Flex');
    flex2.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    col.appendChild(flex2);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Flex sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Swiper12+

type Swiper = TypedFrameNode<SwiperInterface, SwiperAttribute>

Swiper类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<SwiperInterface, SwiperAttribute> | 提供Swiper类型FrameNode节点。  SwiperInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Swiper组件的构造函数类型。  SwiperAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Swiper组件的属性设置对象。  SwiperInterface表示Swiper的[接口](ts-container-swiper.md#接口)，SwiperAttribute表示Swiper的[属性](ts-container-swiper.md#属性)。 |

### createNode('Swiper')12+

createNode(context: UIContext, nodeType: 'Swiper'): Swiper

创建Swiper类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Swiper控制器
class MySwiperController extends NodeController {
  swiperController: SwiperController = new SwiperController()

  makeNode(uiContext: UIContext): FrameNode | null {
    // 创建Swiper
    let swiperNode = typeNode.createNode(uiContext, 'Swiper')

    // 创建Text
    let text0 = typeNode.createNode(uiContext, 'Text')
    text0.initialize('0')
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
    // 向swiper添加text0
    swiperNode.appendChild(text0)
    // 创建另一个Text用于切换
    let text1 = typeNode.createNode(uiContext, 'Text')
    text1.initialize('1')
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
    // 向swiper添加text1
    swiperNode.appendChild(text1)
    swiperNode.commonAttribute.width('100%')
      .height('20%')
      .backgroundColor(0xAFEEEE)
    // 向swiper绑定控制器
    typeNode.bindController(swiperNode, this.swiperController, 'Swiper')
    typeNode.getAttribute(swiperNode, 'Swiper')?.loop(false)
    return swiperNode;

  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySwiperController: MySwiperController = new MySwiperController();

  build() {
    Column({ space: 5 }) {
      Text('SwiperSample')
      NodeContainer(this.mySwiperController);
    }.width('100%')
  }
}
```

### getAttribute('Swiper')20+

getAttribute(node: FrameNode, nodeType: 'Swiper'): SwiperAttribute | undefined

获取Swiper节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void

将控制器[SwiperController](ts-container-swiper.md#swipercontroller)绑定到[Swiper](js-apis-arkui-framenode.md#swiper12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

type Progress = TypedFrameNode<ProgressInterface, ProgressAttribute>

Progress类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ProgressInterface, ProgressAttribute> | 提供Progress类型FrameNode节点。  ProgressInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Progress组件的构造函数类型。  ProgressAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Progress组件的属性设置对象。  ProgressInterface表示Progress的[接口](ts-basic-components-progress.md#接口)，ProgressAttribute表示Progress的[属性](ts-basic-components-progress.md#属性)。 |

### createNode('Progress')12+

createNode(context: UIContext, nodeType: 'Progress'): Progress

创建Progress类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Progress控制器
class MyProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // 创建Progress
    let node = typeNode.createNode(uiContext, 'Progress');
    node.initialize({
      value: 15,
      total: 200,
      type: ProgressType.ScaleRing
    }).width(100)
      .height(100)
    this!.rootNode!.appendChild(node);
    return this.rootNode;
  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyProgressNodeController()).margin(5)
    }.width('100%').height('100%')

  }
}
```

### getAttribute('Progress')20+

getAttribute(node: FrameNode, nodeType: 'Progress'): ProgressAttribute | undefined

获取Progress节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Progress控制器
class MyProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    let node = typeNode.createNode(uiContext, 'Progress');
    node.initialize({
      value: 15,
      total: 200,
      type: ProgressType.ScaleRing
    }).width(100)
      .height(100)
    // 获取Progress的属性
    typeNode.getAttribute(node, 'Progress');
    this!.rootNode!.appendChild(node);
    return this.rootNode;
  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyProgressNodeController()).margin(5)
    }.width('100%').height('100%')

  }
}
```

### Scroll12+

type Scroll = TypedFrameNode<ScrollInterface, ScrollAttribute>

Scroll类型的FrameNode节点类型。允许添加一个子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ScrollInterface, ScrollAttribute> | 提供Scroll类型FrameNode节点。  ScrollInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Scroll组件的构造函数类型。  ScrollAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Scroll组件的属性设置对象。  ScrollInterface表示Scroll的[接口](ts-container-scroll.md#接口)，ScrollAttribute表示Scroll的[属性](ts-container-scroll.md#属性)。 |

### createNode('Scroll')12+

createNode(context: UIContext, nodeType: 'Scroll'): Scroll

创建Scroll类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Scroll控制器
class MyScrollController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 创建Scroll
    let scroller: Scroller = new Scroller();
    // 创建Scroll并设置属性
    let scrollNode = typeNode.createNode(uiContext, 'Scroll');
    scrollNode.initialize(scroller).size({ width: '100%', height: 500 });
    typeNode.getAttribute(scrollNode, 'Scroll')?.friction(0.6);

    let colNode = typeNode.createNode(uiContext, 'Column');
    // 向scroll添加column
    scrollNode.appendChild(colNode);

    for (let i = 0; i < 10; i++) {
      let text = typeNode.createNode(uiContext, 'Text');
      text.initialize('item' + i)
        .size({ width: '90%', height: 100 })
        .textAlign(TextAlign.Center)
        .backgroundColor(0xF9CF93);
      colNode.appendChild(text);
    }

    this!.rootNode!.appendChild(scrollNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myScrollController: MyScrollController = new MyScrollController();

  build() {
    Column({ space: 5 }) {
      Text('ScrollSample')
      NodeContainer(this.myScrollController)

    }.width('100%')
  }
}
```

### getAttribute('Scroll')15+

getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined

获取Scroll节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined

获取Scroll节点中持有的UIScrollEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[Scroll](js-apis-arkui-framenode.md#scroll12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 100021 | The FrameNode is not modifiable. Introduced in API version 15 and will not be threw above API version 24.  适用版本：15-24 |

**示例：**

```ts
typeNode.bindController(node, scroller, 'Scroll');
```

### RelativeContainer12+

type RelativeContainer = TypedFrameNode<RelativeContainerInterface, RelativeContainerAttribute>

RelativeContainer类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<RelativeContainerInterface, RelativeContainerAttribute> | 提供RelativeContainer类型FrameNode节点。  RelativeContainerInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为RelativeContainer组件的构造函数类型。  RelativeContainerAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回RelativeContainer组件的属性设置对象。  RelativeContainerInterface表示RelativeContainer的[接口](ts-container-relativecontainer.md#接口)，RelativeContainerAttribute表示RelativeContainer的[属性](ts-container-relativecontainer.md#属性)。 |

### createNode('RelativeContainer')12+

createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer

创建RelativeContainer类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Relative控制器
class MyRelativeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建RelativeContainer
    let relative = typeNode.createNode(uiContext, 'RelativeContainer')
    relative.initialize()
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(relative)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRelativeController: MyRelativeController = new MyRelativeController();

  build() {
    Column({ space: 5 }) {
      Text('RelativeContainerSample')
      NodeContainer(this.myRelativeController);
    }.width('100%')
  }
}
```

### getAttribute('RelativeContainer')20+

getAttribute(node: FrameNode, nodeType: 'RelativeContainer'): RelativeContainerAttribute | undefined

获取RelativeContainer节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建RelativeContainer
    let relative1 = typeNode.createNode(uiContext, 'RelativeContainer');
    relative1.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    // 获取RelativeContainer的属性
    typeNode.getAttribute(relative1, 'RelativeContainer')?.backgroundColor(Color.Blue).width('100%')
    col.appendChild(relative1);
    // 创建另一个RelativeContainer用于对比
    let relative2 = typeNode.createNode(uiContext, 'RelativeContainer');
    relative2.initialize().width('50%').height('20%').backgroundColor(Color.Pink);
    col.appendChild(relative2);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('RelativeContainer sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Divider12+

type Divider = TypedFrameNode<DividerInterface, DividerAttribute>

Divider类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<DividerInterface, DividerAttribute> | 提供Divider类型FrameNode节点。  DividerInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Divider组件的构造函数类型。  DividerAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Divider组件的属性设置对象。  DividerInterface表示Divider的[接口](ts-basic-components-divider.md#接口)，DividerAttribute表示Divider的[属性](ts-basic-components-divider.md#属性)。 |

### createNode('Divider')12+

createNode(context: UIContext, nodeType: 'Divider'): Divider

创建Divider类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Divider控制器
class MyDividerController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建divider
    let divider = typeNode.createNode(uiContext, 'Divider')
    divider.initialize()
      .strokeWidth(1)
    // 向col添加divider
    col.appendChild(divider)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myDividerController: MyDividerController = new MyDividerController();

  build() {
    Column({ space: 5 }) {
      Text('DividerSample')
      NodeContainer(this.myDividerController);

    }.width('100%')
  }
}
```

### LoadingProgress12+

type LoadingProgress = TypedFrameNode<LoadingProgressInterface, LoadingProgressAttribute>

LoadingProgress类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<LoadingProgressInterface, LoadingProgressAttribute> | 提供LoadingProgress类型FrameNode节点。  LoadingProgressInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为LoadingProgress组件的构造函数类型。  LoadingProgressAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回LoadingProgress组件的属性设置对象。  LoadingProgressInterface表示LoadingProgress的[接口](ts-basic-components-loadingprogress.md#接口)，LoadingProgressAttribute表示LoadingProgress的[属性](ts-basic-components-loadingprogress.md#属性)。 |

### createNode('LoadingProgress')12+

createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress

创建LoadingProgress类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义LoadingProgress控制器
class MyLoadingProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // 创建LoadingProgress
    let node = typeNode.createNode(uiContext, 'LoadingProgress');
    node.initialize()
      .width(100)
      .height(100)
      .color(Color.Red)
      .enableLoading(true)
    this!.rootNode!.appendChild(node);
    return this.rootNode;
  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyLoadingProgressNodeController()).margin(5)
    }.width('100%').height('100%')
  }
}
```

### getAttribute('LoadingProgress')20+

getAttribute(node: FrameNode, nodeType: 'LoadingProgress'): LoadingProgressAttribute | undefined

获取[LoadingProgress](ts-basic-components-loadingprogress.md)节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义LoadingProgress控制器
class MyLoadingProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    let node = typeNode.createNode(uiContext, 'LoadingProgress');
    node.initialize()
      .width(100)
      .height(100)
      .color(Color.Red)
      .enableLoading(true)
    // 获取LoadingProgress的属性
    typeNode.getAttribute(node, 'LoadingProgress');
    this!.rootNode!.appendChild(node);
    return this.rootNode;
  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyLoadingProgressNodeController()).margin(5)
    }.width('100%').height('100%')
  }
}
```

### Search12+

type Search = TypedFrameNode<SearchInterface, SearchAttribute>

Search类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<SearchInterface, SearchAttribute> | 提供Search类型FrameNode节点。  SearchInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Search组件的构造函数类型。  SearchAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Search组件的属性设置对象。  SearchInterface表示Search的[接口](ts-basic-components-search.md#接口)，SearchAttribute表示Search的[属性](ts-basic-components-search.md#属性)。 |

### createNode('Search')12+

createNode(context: UIContext, nodeType: 'Search'): Search

创建Search类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Search
    let search = typeNode.createNode(uiContext, 'Search');
    search.initialize({ value: 'Search' })
      .searchButton('SEARCH')
      .textFont({ size: 14, weight: 400 })
    col.appendChild(search);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Search sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Blank12+

type Blank = TypedFrameNode<BlankInterface, BlankAttribute>

Blank类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<BlankInterface, BlankAttribute> | 提供Blank类型FrameNode节点。  BlankInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Blank组件的构造函数类型。  BlankAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Blank组件的属性设置对象。  BlankInterface表示Blank的[接口](ts-basic-components-blank.md#接口)，BlankAttribute表示Blank的[属性](ts-basic-components-blank.md#属性)。 |

### createNode('Blank')12+

createNode(context: UIContext, nodeType: 'Blank'): Blank

创建Blank类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Blank控制器
class MyBlankController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Blank
    let blank = typeNode.createNode(uiContext, 'Blank')
    blank.initialize()
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Blue)
    col.appendChild(blank)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myBlankController: MyBlankController = new MyBlankController();

  build() {
    Column({ space: 5 }) {
      Text('BlankSample')
      NodeContainer(this.myBlankController);

    }.width('100%')
  }
}
```

### Image12+

type Image = TypedFrameNode<ImageInterface, ImageAttribute>

Image类型的FrameNode节点类型。不允许添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ImageInterface, ImageAttribute> | 提供Image类型FrameNode节点。  ImageInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Image组件的构造函数类型。  ImageAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Image组件的属性设置对象。  ImageInterface表示Image的[接口](ts-basic-components-image.md#接口)，ImageAttribute表示Image的[属性](ts-basic-components-image.md#属性)。 |

### createNode('Image')12+

createNode(context: UIContext, nodeType: 'Image'): Image

创建Image类型的FrameNode节点。使用typeNode创建Image节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Image控制器
class MyImageController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // 创建Image
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode
      // $r('app.media.img')需要替换为开发者所需的图像资源文件
      .initialize($r('app.media.img'))
      .width(100)
      .height(100)
      .fillColor(Color.Red)
      .objectFit(ImageFit.Contain)
      .renderMode(ImageRenderMode.Template)
      .fitOriginalSize(true)
      .matchTextDirection(true)
      .objectRepeat(ImageRepeat.X)
      .autoResize(true)

    this!.rootNode!.appendChild(imageNode);
    return this.rootNode;

  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyImageController()).margin(5)
    }.width('100%').height('100%')

  }
}
```

### getAttribute('Image')20+

getAttribute(node: FrameNode, nodeType: 'Image'): ImageAttribute | undefined

获取Image节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Image控制器
class MyImageController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode
      // $r('app.media.img')需要替换为开发者所需的图像资源文件
      .initialize($r('app.media.img'))
      .width(100)
      .height(100)
      .fillColor(Color.Red)
      .objectFit(ImageFit.Contain)
      .renderMode(ImageRenderMode.Template)
      .fitOriginalSize(true)
      .matchTextDirection(true)
      .objectRepeat(ImageRepeat.X)
      .autoResize(true)
    // 获取Image的属性
    typeNode.getAttribute(imageNode, 'Image');
    this!.rootNode!.appendChild(imageNode);
    return this.rootNode;

  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyImageController()).margin(5)
    }.width('100%').height('100%')

  }
}
```

### List12+

type List = TypedFrameNode<ListInterface, ListAttribute>

List类型的FrameNode节点类型。只允许添加[ListItem](js-apis-arkui-framenode.md#listitem12)、[ListItemGroup](js-apis-arkui-framenode.md#listitemgroup12)类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ListInterface, ListAttribute> | 提供List类型FrameNode节点。  ListInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为List组件的构造函数类型。  ListAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回List组件的属性设置对象。  ListInterface表示List的[接口](ts-container-list.md#接口)，ListAttribute表示List的[属性](ts-container-list.md#属性)。 |

### createNode('List')12+

createNode(context: UIContext, nodeType: 'List'): List

创建List类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义List控制器
class MyListController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    // 创建list节点
    this.rootNode = new FrameNode(uiContext);
    // 创建List
    let listNode = typeNode.createNode(uiContext, 'List');
    listNode.initialize({ space: 3 }).size({ width: '100%', height: '100%' });
    typeNode.getAttribute(listNode, 'List')?.friction(0.6);

    // 在list下创建ListItemGroup节点
    let listItemGroupNode = typeNode.createNode(uiContext, 'ListItemGroup');
    listItemGroupNode.initialize({ space: 3 });
    listNode.appendChild(listItemGroupNode);

    // 在ListItemGroup中放入ListItem节点
    let listItemNode1 = typeNode.createNode(uiContext, 'ListItem');
    listItemNode1.initialize({ style: ListItemStyle.NONE }).height(100).borderWidth(1).backgroundColor('#FF00FF');
    let text1 = typeNode.createNode(uiContext, 'Text');
    text1.initialize('ListItem1');
    listItemNode1.appendChild(text1);
    listItemGroupNode.appendChild(listItemNode1);

    // 创建ListItem，添加Text至ListItem，添加至listItemGroup
    let listItemNode2 = typeNode.createNode(uiContext, 'ListItem');
    listItemNode2.initialize({ style: ListItemStyle.CARD }).borderWidth(1).backgroundColor('#FF00FF');
    typeNode.getAttribute(listItemNode2, 'ListItem')?.height(100);
    let text2 = typeNode.createNode(uiContext, 'Text');
    text2.initialize('ListItem2');
    listItemNode2.appendChild(text2);
    listItemGroupNode.appendChild(listItemNode2);

    this!.rootNode!.appendChild(listNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myListController: MyListController = new MyListController();

  build() {
    Column({ space: 5 }) {
      Text('ListSample')
      NodeContainer(this.myListController)

    }.width('100%')
  }
}
```

### getEvent('List')19+

getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined

获取List节点中持有的UIListEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'List'): ListAttribute | undefined

获取List节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[List](js-apis-arkui-framenode.md#list12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 100021 | The FrameNode is not modifiable. Introduced in API version 20 and will not be threw above API version 24.  适用版本：20-24 |

**示例：**

```ts
typeNode.bindController(node, scroller, 'List');
```

### ListItem12+

type ListItem = TypedFrameNode<ListItemInterface, ListItemAttribute>

ListItem类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ListItemInterface, ListItemAttribute> | 提供ListItem类型FrameNode节点。  ListItemInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为ListItem组件的构造函数类型。  ListItemAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回ListItem组件的属性设置对象。  ListItemInterface表示ListItem的[接口](ts-container-listitem.md#接口)，ListItemAttribute表示ListItem的[属性](ts-container-listitem.md#属性)。 |

### createNode('ListItem')12+

createNode(context: UIContext, nodeType: 'ListItem'): ListItem

创建ListItem类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'ListItem'): ListItemAttribute | undefined

获取ListItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

type TextInput = TypedFrameNode<TextInputInterface, TextInputAttribute>

TextInput类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<TextInputInterface, TextInputAttribute> | 提供TextInput类型FrameNode节点。  TextInputInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextInput组件的构造函数类型。  TextInputAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextInput组件的属性设置对象。  TextInputInterface表示TextInput的[接口](ts-basic-components-textinput.md#接口)，TextInputAttribute表示TextInput的[属性](ts-basic-components-textinput.md#属性)。 |

### createNode('TextInput')12+

createNode(context: UIContext, nodeType: 'TextInput'): TextInput

创建TextInput类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建TextInput
    let textInput = typeNode.createNode(uiContext, 'TextInput');
    textInput.initialize({ text: 'TextInput' });
    col.appendChild(textInput);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextInput sample')
      NodeContainer(this.myNodeController);
    }
  }
}
```

### getAttribute('TextInput')20+

getAttribute(node: FrameNode, nodeType: 'TextInput'): TextInputAttribute | undefined

获取TextInput节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建TextInput
    let textInput = typeNode.createNode(uiContext, 'TextInput');
    textInput.initialize({ placeholder: 'TextInput placeholderColor' });
    // 获取TextInput的属性
    typeNode.getAttribute(textInput, 'TextInput')?.placeholderColor(Color.Red);
    col.appendChild(textInput);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextInput getAttribute sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### bindController('TextInput')20+

bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void

将输入框控制器[TextInputController](ts-basic-components-textinput.md#textinputcontroller8)绑定到[TextInput](js-apis-arkui-framenode.md#textinput12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API版本26.0.0开始，该接口支持声明式方式创建的节点，API版本26.0.0以下版本不支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建、初始化TextInput，默认获焦
    let textInput = typeNode.createNode(uiContext, 'TextInput');
    textInput.initialize({ text: 'TextInput' })
      .defaultFocus(true)
    col.appendChild(textInput);
    // 绑定TextInputController，设置光标位置
    let controller: TextInputController = new TextInputController();
    typeNode.bindController(textInput, controller, 'TextInput');
    controller.caretPosition(3);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextInput bindController sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Button12+

type Button = TypedFrameNode<ButtonInterface, ButtonAttribute>

Button类型的FrameNode节点类型。以子组件模式创建允许添加一个子组件。以label模式创建不可以添加子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ButtonInterface, ButtonAttribute> | 提供Button类型FrameNode节点。  ButtonInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Button组件的构造函数类型。  ButtonAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Button组件的属性设置对象。  接口入参label不为空时，以label模式创建Button组件，以此模式创建时无法包含子组件，并且不允许再设置子组件，否则会抛出异常。且label模式和子组件模式在第一次initialize创建之后无法在后续的initialize进行动态修改，如需要包含子组件，第一次initialize时不要设置label参数。  以子组件模式创建时，只能包含一个子组件，不能设置多个子组件，否则会抛出异常。  ButtonInterface表示Button的[接口](ts-basic-components-button.md#接口)，ButtonAttribute表示Button的[属性](ts-basic-components-button.md#属性)。 |

### createNode('Button')12+

createNode(context: UIContext, nodeType: 'Button'): Button

创建Button类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Button控制器
class MyButtonController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Button
    let button = typeNode.createNode(uiContext, 'Button')
    button.initialize('This is Button')
      .onClick(() => {
        uiContext.getPromptAction().showToast({ message: 'Button clicked' })
      })
    col.appendChild(button)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myButtonController: MyButtonController = new MyButtonController();

  build() {
    Column({ space: 5 }) {
      Text('ButtonSample')
      NodeContainer(this.myButtonController);

    }.width('100%')
  }
}
```

### getAttribute('Button')20+

getAttribute(node: FrameNode, nodeType: 'Button'): ButtonAttribute | undefined

获取Button节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Button控制器
class MyButtonController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    let button = typeNode.createNode(uiContext, 'Button')
    button.initialize('This is Button')
      .onClick(() => {
        uiContext.getPromptAction().showToast({ message: 'Button clicked' })
      })
    // 获取Button属性
    typeNode.getAttribute(button, 'Button')?.buttonStyle(ButtonStyleMode.TEXTUAL);
    col.appendChild(button)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myButtonController: MyButtonController = new MyButtonController();

  build() {
    Column({ space: 5 }) {
      Text('ButtonSample')
      NodeContainer(this.myButtonController);

    }.width('100%')
  }
}
```

### ListItemGroup12+

type ListItemGroup = TypedFrameNode<ListItemGroupInterface, ListItemGroupAttribute>

ListItemGroup类型的FrameNode节点类型。只允许添加[ListItem](ts-container-listitem.md)类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ListItemGroupInterface, ListItemGroupAttribute> | 提供ListItemGroup类型FrameNode节点。  ListItemGroupInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为ListItemGroup组件的构造函数类型。  ListItemGroupAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回ListItemGroup组件的属性设置对象。  ListItemGroupInterface表示ListItemGroup的[接口](ts-container-listitem.md#接口)，ListItemGroupAttribute表示ListItemGroup的[属性](ts-container-listitem.md#属性)。 |

### createNode('ListItemGroup')12+

createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup

创建ListItemGroup类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'ListItemGroup'): ListItemGroupAttribute | undefined

获取ListItemGroup节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
typeNode.getAttribute(node, 'ListItemGroup');
```

### WaterFlow12+

type WaterFlow = TypedFrameNode<WaterFlowInterface, WaterFlowAttribute>

WaterFlow类型的FrameNode节点类型。只允许添加[FlowItem](ts-container-flowitem.md)类型子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<WaterFlowInterface, WaterFlowAttribute> | 提供[WaterFlow](js-apis-arkui-framenode.md#waterflow12)类型FrameNode节点。  WaterFlowInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为WaterFlow组件的构造函数类型。  WaterFlowAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回WaterFlow组件的属性设置对象。  WaterFlowInterface表示WaterFlow的[接口](ts-container-waterflow.md#接口)，WaterFlowAttribute表示WaterFlow的[属性](ts-container-waterflow.md#属性)。 |

### createNode('WaterFlow')12+

createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow

创建WaterFlow类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义WaterFlow控制器
class MyWaterFlowController extends NodeController {
  public rootNode: FrameNode | null = null;
  private minHeight: number = 80;
  private maxHeight: number = 180;

  // 计算FlowItem高
  private getHeight() {
    let randomHeight = Math.floor(Math.random() * this.maxHeight);
    return (randomHeight > this.minHeight ? randomHeight : this.minHeight);
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 创建WaterFlow并设置属性
    let waterFlowNode = typeNode.createNode(uiContext, 'WaterFlow');
    waterFlowNode.attribute.size({ width: '100%', height: '100%' })
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5);
    typeNode.getAttribute(waterFlowNode, 'WaterFlow')?.friction(0.6);

    // 创建FlowItem并设置属性
    for (let i = 0; i < 20; i++) {
      let flowItemNode = typeNode.createNode(uiContext, 'FlowItem');
      flowItemNode.attribute.size({ height: this.getHeight() });
      typeNode.getAttribute(flowItemNode, 'FlowItem')?.width('100%');
      waterFlowNode.appendChild(flowItemNode);

      let text = typeNode.createNode(uiContext, 'Text');
      text.initialize('N' + i)
        .size({ width: '100%', height: '100%' })
        .textAlign(TextAlign.Center)
        .backgroundColor(0xF9CF93);
      flowItemNode.appendChild(text);
    }

    this!.rootNode!.appendChild(waterFlowNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myWaterFlowController: MyWaterFlowController = new MyWaterFlowController();

  build() {
    Column({ space: 5 }) {
      Text('WaterFlowSample')
      NodeContainer(this.myWaterFlowController);

    }.width('100%')
  }
}
```

### getEvent('WaterFlow')19+

getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined

获取[WaterFlow](js-apis-arkui-framenode.md#waterflow12)节点中持有的UIWaterFlowEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'WaterFlow'): WaterFlowAttribute | undefined

获取WaterFlow节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[WaterFlow](js-apis-arkui-framenode.md#waterflow12)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 100021 | The FrameNode is not modifiable. Introduced in API version 20 and will not be threw above API version 24.  适用版本：20-24 |

**示例：**

```ts
typeNode.bindController(node, scroller, 'WaterFlow');
```

### FlowItem12+

type FlowItem = TypedFrameNode<FlowItemInterface, FlowItemAttribute>

FlowItem类型的FrameNode节点类型。允许添加一个子组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<FlowItemInterface, FlowItemAttribute> | 提供FlowItem类型FrameNode节点。  FlowItemInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为FlowItem组件的构造函数类型。  FlowItemAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回FlowItem组件的属性设置对象。  FlowItemInterface表示FlowItem的[接口](ts-container-flowitem.md#接口)，FlowItemAttribute表示FlowItem的[属性](ts-container-flowitem.md#属性)。 |

### createNode('FlowItem')12+

createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem

创建FlowItem类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'FlowItem'): FlowItemAttribute | undefined

获取FlowItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

type XComponent = TypedFrameNode<XComponentInterface, XComponentAttribute>

XComponent类型的FrameNode节点类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<XComponentInterface, XComponentAttribute> | 提供XComponent类型FrameNode节点。  XComponentInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为XComponent组件的构造函数类型。  XComponentAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回XComponent组件的属性设置对象。  XComponentInterface表示XComponent的[接口](ts-basic-components-xcomponent.md#接口)，XComponentAttribute表示XComponent的[属性](ts-basic-components-xcomponent.md#属性)。 |

### createNode('XComponent')12+

createNode(context: UIContext, nodeType: 'XComponent'): XComponent

创建XComponent类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    // 创建XComponent
    let xcomponent = typeNode.createNode(uiContext, 'XComponent');
    xcomponent.attribute.backgroundColor(Color.Red);
    col.appendChild(xcomponent);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('XComponentSample')
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```

### createNode('XComponent')12+

createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent

按照options中的配置参数创建XComponent类型的FrameNode节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  controller: XComponentController = new XComponentController();
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    // 设置XComponent参数对象
    let options: XComponentOptions = {
      type: XComponentType.SURFACE,
      controller: this.controller
    };
    // 创建XComponent
    let xcomponent = typeNode.createNode(uiContext, 'XComponent', options);
    xcomponent.attribute.backgroundColor(Color.Red);
    col.appendChild(xcomponent);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('XComponentSample')
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```

### createNode('XComponent')19+

createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent

按照parameters中的配置参数创建XComponent类型的FrameNode节点。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  controller: XComponentController = new XComponentController();
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    let parameters: NativeXComponentParameters = {
      type: XComponentType.SURFACE
    };
    // 创建XComponent
    let xcomponent = typeNode.createNode(uiContext, 'XComponent', parameters);
    xcomponent.attribute.backgroundColor(Color.Red);
    col.appendChild(xcomponent);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('XComponentSample')
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```

### getAttribute('XComponent')20+

getAttribute(node: FrameNode, nodeType: 'XComponent'): XComponentAttribute | undefined

获取XComponent节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
typeNode.getAttribute(node, 'XComponent');
```

### QRCode14+

type QRCode = TypedFrameNode<QRCodeInterface, QRCodeAttribute>

QRCode类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<QRCodeInterface, QRCodeAttribute> | 提供QRCode类型FrameNode节点。  QRCodeInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为QRCode组件的构造函数类型。  QRCodeAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回QRCode组件的属性设置对象。  QRCodeInterface表示QRCode的[接口](ts-basic-components-qrcode.md#接口)，QRCodeAttribute表示QRCode的[属性](ts-basic-components-qrcode.md#属性)。 |

### createNode('QRCode')14+

createNode(context: UIContext, nodeType: 'QRCode'): QRCode

创建QRCode类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
typeNode.createNode(uiContext, 'QRCode');
```

### Badge14+

type Badge = TypedFrameNode<BadgeInterface, BadgeAttribute>

Badge类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<BadgeInterface, BadgeAttribute> | 提供Badge类型FrameNode节点。  BadgeInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Badge组件的构造函数类型。  BadgeAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Badge组件的属性设置对象。  BadgeInterface表示Badge的[接口](ts-container-badge.md#接口)，BadgeAttribute表示Badge的[属性](ts-container-badge.md#属性)。 |

### createNode('Badge')14+

createNode(context: UIContext, nodeType: 'Badge'): Badge

创建Badge类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
typeNode.createNode(uiContext, 'Badge');
```

### Grid14+

type Grid = TypedFrameNode<GridInterface, GridAttribute>

Grid类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<GridInterface, GridAttribute> | 提供Grid类型FrameNode节点。  GridInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Grid组件的构造函数类型。  GridAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Grid组件的属性设置对象。  GridInterface表示Grid的[接口](ts-container-grid.md#接口)，GridAttribute表示Grid的[属性](ts-container-grid.md#属性)。 |

### createNode('Grid')14+

createNode(context: UIContext, nodeType: 'Grid'): Grid

创建Grid类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Grid控制器
class MyGridController extends NodeController {
  public rootNode: FrameNode | null = null;
  private scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 创建Grid设置属性
    let gridNode = typeNode.createNode(uiContext, 'Grid');
    gridNode.initialize(this.scroller, { regularSize: [1, 1] })
      .size({ width: '90%', height: 300 })
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10);
    typeNode.getAttribute(gridNode, 'Grid')?.friction(0.6);

    // 创建GridItem并设置属性
    for (let i = 0; i < 25; i++) {
      let gridItemNode = typeNode.createNode(uiContext, 'GridItem');
      gridItemNode.initialize({ style: GridItemStyle.NONE }).size({ height: '100%' });
      typeNode.getAttribute(gridItemNode, 'GridItem')?.width('100%');

      let text = typeNode.createNode(uiContext, 'Text');
      text.initialize((i % 5).toString())
        .size({ width: '100%', height: '100%' })
        .textAlign(TextAlign.Center)
        .backgroundColor(0xF9CF93);
      gridItemNode.appendChild(text);
      gridNode.appendChild(gridItemNode);
    }

    this!.rootNode!.appendChild(gridNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myGridController: MyGridController = new MyGridController();

  build() {
    Column({ space: 5 }) {
      Text('GridSample')
      NodeContainer(this.myGridController)

    }.width('100%')
  }
}
```

### getEvent('Grid')19+

getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined

获取Grid节点中持有的UIGridEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'Grid'): GridAttribute | undefined

获取Grid节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void

将滚动控制器[Scroller](ts-container-scroll.md#scroller)绑定到[Grid](js-apis-arkui-framenode.md#grid14)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 100021 | The FrameNode is not modifiable. Introduced in API version 20 and will not be threw above API version 24.  适用版本：20-24 |

**示例：**

```ts
typeNode.bindController(node, scroller, 'Grid');
```

### GridItem14+

type GridItem = TypedFrameNode<GridItemInterface, GridItemAttribute>

GridItem类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<GridItemInterface, GridItemAttribute> | 提供GridItem类型FrameNode节点。  GridItemInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为GridItem组件的构造函数类型。  GridItemAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回GridItem组件的属性设置对象。  GridItemInterface表示GridItem的[接口](ts-container-griditem.md#接口)，GridItemAttribute表示GridItem的[属性](ts-container-griditem.md#属性)。 |

### createNode('GridItem')14+

createNode(context: UIContext, nodeType: 'GridItem'): GridItem

创建GridItem类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getAttribute(node: FrameNode, nodeType: 'GridItem'): GridItemAttribute | undefined

获取GridItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

type TextClock = TypedFrameNode<TextClockInterface, TextClockAttribute>

TextClock类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<TextClockInterface, TextClockAttribute> | 提供TextClock类型FrameNode节点。  TextClockInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextClock组件的构造函数类型。  TextClockAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextClock组件的属性设置对象。  TextClockInterface表示TextClock的[接口](ts-basic-components-textclock.md#接口)，TextClockAttribute表示TextClock的[属性](ts-basic-components-textclock.md#属性)。 |

### createNode('TextClock')14+

createNode(context: UIContext, nodeType: 'TextClock'): TextClock

创建TextClock类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
typeNode.createNode(uiContext, 'TextClock');
```

### TextTimer14+

type TextTimer = TypedFrameNode<TextTimerInterface, TextTimerAttribute>

TextTimer类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<TextTimerInterface, TextTimerAttribute> | 提供TextTimer类型FrameNode节点。  TextTimerInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextTimer组件的构造函数类型。  TextTimerAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextTimer组件的属性设置对象。  TextTimerInterface表示TextTimer的[接口](ts-basic-components-texttimer.md#接口)，TextTimerAttribute表示TextTimer的[属性](ts-basic-components-texttimer.md#属性)。 |

### createNode('TextTimer')14+

createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer

创建TextTimer类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
typeNode.createNode(uiContext, 'TextTimer');
```

### Marquee14+

type Marquee = TypedFrameNode<MarqueeInterface, MarqueeAttribute>

Marquee类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<MarqueeInterface, MarqueeAttribute> | 提供Marquee类型FrameNode节点。  MarqueeInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Marquee组件的构造函数类型。  MarqueeAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Marquee组件的属性设置对象。  MarqueeInterface表示Marquee的[接口](ts-basic-components-marquee.md#接口)，MarqueeAttribute表示Marquee的[属性](ts-basic-components-marquee.md#属性)。 |

### createNode('Marquee')14+

createNode(context: UIContext, nodeType: 'Marquee'): Marquee

创建Marquee类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
    node.appendChild(col);
    // 创建marquee
    let marquee = typeNode.createNode(uiContext, 'Marquee');
    marquee.initialize({ start: true, src: 'Marquee, if need display, src shall be long' })
      .width(100);
    col.appendChild(marquee);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Marquee createNode sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### TextArea14+

type TextArea = TypedFrameNode<TextAreaInterface, TextAreaAttribute>

TextArea类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<TextAreaInterface, TextAreaAttribute> | 提供TextArea类型FrameNode节点。  TextAreaInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为TextArea组件的构造函数类型。  TextAreaAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回TextArea组件的属性设置对象。  TextAreaInterface表示TextArea的[接口](ts-basic-components-textarea.md#接口)，TextAreaAttribute表示TextArea的[属性](ts-basic-components-textarea.md#属性)。 |

### createNode('TextArea')14+

createNode(context: UIContext, nodeType: 'TextArea'): TextArea

创建TextArea类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
    node.appendChild(col);
    // 创建textArea
    let textArea = typeNode.createNode(uiContext, 'TextArea');
    textArea.initialize({ text: 'TextArea' });
    col.appendChild(textArea);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextArea create sample')
      NodeContainer(this.myNodeController);
    }
  }
}
```

### getAttribute('TextArea')20+

getAttribute(node: FrameNode, nodeType: 'TextArea'): TextAreaAttribute | undefined

获取TextArea节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建TextArea
    let textArea = typeNode.createNode(uiContext, 'TextArea');
    textArea.initialize({ placeholder: 'TextArea placeholderColor' });
    col.appendChild(textArea);
    // 获取TextArea节点的属性
    typeNode.getAttribute(textArea, 'TextArea')?.placeholderColor(Color.Red);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextArea getAttribute sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### bindController('TextArea')20+

bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void

将输入框控制器[TextAreaController](ts-basic-components-textarea.md#textareacontroller8)绑定到[TextArea](js-apis-arkui-framenode.md#textarea14)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API版本26.0.0开始，该接口支持声明式方式创建的节点，API版本26.0.0以下版本不支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建、初始化TextArea，默认获焦
    let textArea = typeNode.createNode(uiContext, 'TextArea');
    textArea.initialize({ text: 'TextArea' })
      .defaultFocus(true)
    col.appendChild(textArea);
    // 绑定TextAreaController，设置光标位置
    let controller: TextAreaController = new TextAreaController()
    typeNode.bindController(textArea, controller, 'TextArea');
    controller.caretPosition(3);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextArea bindController sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### SymbolGlyph14+

type SymbolGlyph = TypedFrameNode<SymbolGlyphInterface, SymbolGlyphAttribute>

SymbolGlyph类型的FrameNode节点类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<SymbolGlyphInterface, SymbolGlyphAttribute> | 提供SymbolGlyph类型FrameNode节点。  SymbolGlyphInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为SymbolGlyph组件的构造函数类型。  SymbolGlyphAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回SymbolGlyph组件的属性设置对象。  SymbolGlyphInterface表示SymbolGlyph的[接口](ts-basic-components-symbolglyph.md#接口)，SymbolGlyphAttribute表示SymbolGlyph的[属性](ts-basic-components-symbolglyph.md#属性)。 |

### createNode('SymbolGlyph')14+

createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph

创建SymbolGlyph类型的FrameNode节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建SymbolGlyph
    let symbolGlyph = typeNode.createNode(uiContext, 'SymbolGlyph');
    symbolGlyph.initialize($r('sys.symbol.ohos_trash'));
    col.appendChild(symbolGlyph);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('SymbolGlyph sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```

### Checkbox18+

type Checkbox = TypedFrameNode<CheckboxInterface, CheckboxAttribute>

Checkbox类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<CheckboxInterface, CheckboxAttribute> | 提供Checkbox类型FrameNode节点。  CheckboxInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Checkbox组件的构造函数类型。  CheckboxAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Checkbox组件的属性设置对象。  CheckboxInterface表示Checkbox的[接口](ts-basic-components-checkbox.md#接口)，CheckboxAttribute表示Checkbox的[属性](ts-basic-components-checkbox.md#属性)。 |

### createNode('Checkbox')18+

createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox

创建Checkbox类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Checkbox控制器
class MyCheckboxController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Checkbox
    let checkbox = typeNode.createNode(uiContext, 'Checkbox')
    checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

    // 创建另一个Checkbox
    let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
    checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

    // 将两个checkbox添加至col进行比较
    col.appendChild(checkbox)
    col.appendChild(checkbox1)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myCheckboxController: MyCheckboxController = new MyCheckboxController();

  build() {
    Column({ space: 5 }) {
      Text('CheckboxSample')
      NodeContainer(this.myCheckboxController);
    }.width('100%')
  }
}
```

### getAttribute('Checkbox')20+

getAttribute(node: FrameNode, nodeType: 'Checkbox'): CheckboxAttribute | undefined

获取Checkbox节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Checkbox控制器
class MyCheckboxController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Checkbox
    let checkbox = typeNode.createNode(uiContext, 'Checkbox')
    checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

    // 创建另一个Checkbox
    let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
    checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })
    // 给另一个Checkbox设置形状属性
    typeNode.getAttribute(checkbox1,'Checkbox')?.shape(CheckBoxShape.ROUNDED_SQUARE)
    // 将两个checkbox添加至col进行比较
    col.appendChild(checkbox)
    col.appendChild(checkbox1)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myCheckboxController: MyCheckboxController = new MyCheckboxController();

  build() {
    Column({ space: 5 }) {
      Text('CheckboxSample')
      NodeContainer(this.myCheckboxController);
    }.width('100%')
  }
}
```

### CheckboxGroup18+

type CheckboxGroup = TypedFrameNode<CheckboxGroupInterface, CheckboxGroupAttribute>

CheckboxGroup类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<CheckboxGroupInterface, CheckboxGroupAttribute> | 提供CheckboxGroup类型FrameNode节点。  CheckboxGroupInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为CheckboxGroup组件的构造函数类型。  CheckboxGroupAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回CheckboxGroup组件的属性设置对象。  CheckboxGroupInterface表示CheckboxGroup的[接口](ts-basic-components-checkboxgroup.md#接口)，CheckboxGroupAttribute表示CheckboxGroup的[属性](ts-basic-components-checkboxgroup.md#属性)。 |

### createNode('CheckboxGroup')18+

createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup

创建CheckboxGroup类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义CheckboxGroup控制器
class MyCheckboxGroupController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    let checkbox = typeNode.createNode(uiContext, 'Checkbox')
    checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

    let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
    checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

    // 创建checkboxGroup
    let checkboxGroup = typeNode.createNode(uiContext, 'CheckboxGroup')
    checkboxGroup.initialize({ group: 'checkboxGroup1' })

    col.appendChild(checkbox)
    col.appendChild(checkbox1)
    col.appendChild(checkboxGroup)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myCheckboxGroupController: MyCheckboxGroupController = new MyCheckboxGroupController();

  build() {
    Column({ space: 5 }) {
      Text('CheckboxGroupSample')
      NodeContainer(this.myCheckboxGroupController);
    }.width('100%')
  }
}
```

### Rating18+

type Rating = TypedFrameNode<RatingInterface, RatingAttribute>

Rating类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<RatingInterface, RatingAttribute> | 提供Rating类型FrameNode节点。  RatingInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Rating组件的构造函数类型。  RatingAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Rating组件的属性设置对象。  RatingInterface表示Rating的[接口](ts-basic-components-rating.md#接口)，RatingAttribute表示Rating的[属性](ts-basic-components-rating.md#属性)。 |

### createNode('Rating')18+

createNode(context: UIContext, nodeType: 'Rating'): Rating

创建Rating类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Rating控制器
class MyRatingController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建rating
    let rating = typeNode.createNode(uiContext, 'Rating')
    rating.initialize({ rating: 0 })
    col.appendChild(rating)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRatingController: MyRatingController = new MyRatingController();

  build() {
    Column({ space: 5 }) {
      Text('RatingSample')

      NodeContainer(this.myRatingController);

    }.width('100%')
  }
}
```

### Radio18+

type Radio = TypedFrameNode<RadioInterface, RadioAttribute>

Radio类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<RadioInterface, RadioAttribute> | 提供Radio类型FrameNode节点。  RadioInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Radio组件的构造函数类型。  RadioAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Radio组件的属性设置对象。  RadioInterface表示Radio的[接口](ts-basic-components-radio.md#接口)，RadioAttribute表示Radio的[属性](ts-basic-components-radio.md#属性)。 |

### createNode('Radio')18+

createNode(context: UIContext, nodeType: 'Radio'): Radio

创建Radio类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Radio控制器
class MyRadioController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Radio
    let radio1 = typeNode.createNode(uiContext, 'Radio')
    radio1.initialize({ value: 'radio1', group: 'radioGroup' })

    // 创建另一个Radio用于对比
    let radio2 = typeNode.createNode(uiContext, 'Radio')
    radio2.initialize({ value: 'radio2', group: 'radioGroup' })

    col.appendChild(radio1)
    col.appendChild(radio2)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRadioController: MyRadioController = new MyRadioController();

  build() {
    Column({ space: 5 }) {
      Text('RadioSample')
      NodeContainer(this.myRadioController);
    }.width('100%')
  }
}
```

### getAttribute('Radio')20+

getAttribute(node: FrameNode, nodeType: 'Radio'): RadioAttribute | undefined

获取Radio节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Radio控制器
class MyRadioController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建radio
    let radio1 = typeNode.createNode(uiContext, 'Radio')
    radio1.initialize({ value: 'radio1', group: 'radioGroup' })
    typeNode.getAttribute(radio1,'Radio')?.checked(true)
    // 创建另一个radio用于对比
    let radio2 = typeNode.createNode(uiContext, 'Radio')
    radio2.initialize({ value: 'radio2', group: 'radioGroup' })

    col.appendChild(radio1)
    col.appendChild(radio2)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRadioController: MyRadioController = new MyRadioController();

  build() {
    Column({ space: 5 }) {
      Text('RadioSample')
      NodeContainer(this.myRadioController);
    }.width('100%')
  }
}
```

### Slider18+

type Slider = TypedFrameNode<SliderInterface, SliderAttribute>

Slider类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<SliderInterface, SliderAttribute> | 提供Slider类型FrameNode节点。  SliderInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Slider组件的构造函数类型。  SliderAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Slider组件的属性设置对象。  SliderInterface表示Slider的[接口](ts-basic-components-slider.md#接口)，SliderAttribute表示Slider的[属性](ts-basic-components-slider.md#属性)。 |

### createNode('Slider')18+

createNode(context: UIContext, nodeType: 'Slider'): Slider

创建Slider类型的FrameNode节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Slider控制器
class MySliderController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Slider
    let slider = typeNode.createNode(uiContext, 'Slider')
    slider.initialize({value:50})
    col.appendChild(slider)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySliderController: MySliderController = new MySliderController();

  build() {
    Column({ space: 5 }) {
      Text('SliderSample')
      NodeContainer(this.mySliderController);

    }.width('100%')
  }
}
```

### getAttribute('Slider')20+

getAttribute(node: FrameNode, nodeType: 'Slider'): SliderAttribute | undefined

获取Slider节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Slider控制器
class MySliderController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Slider
    let slider = typeNode.createNode(uiContext, 'Slider')
    slider.initialize({value:50})
    typeNode.getAttribute(slider,'Slider')?.selectedColor(Color.Pink)
    col.appendChild(slider)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySliderController: MySliderController = new MySliderController();

  build() {
    Column({ space: 5 }) {
      Text('SliderSample')
      NodeContainer(this.mySliderController);

    }.width('100%')
  }
}
```

### Select18+

type Select = TypedFrameNode<SelectInterface, SelectAttribute>

Select类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<SelectInterface, SelectAttribute> | 提供Select类型FrameNode节点。  SelectInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Select组件的构造函数类型。  SelectAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Select组件的属性设置对象。  SelectInterface表示Select的[接口](ts-basic-components-select.md#接口)，SelectAttribute表示Select的[属性](ts-basic-components-select.md#属性)。 |

### createNode('Select')18+

createNode(context: UIContext, nodeType: 'Select'): Select

创建Select类型的FrameNode节点。使用typeNode创建Select节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Select控制器
class MySelectController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Select并设置选项
    let select = typeNode.createNode(uiContext, 'Select')
    select.initialize([{ value: 'option one' }, { value: 'option two' }, { value: 'option three' }])
    col.appendChild(select)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySelectController: MySelectController = new MySelectController();

  build() {
    Column({ space: 5 }) {
      Text('SelectSample')
      NodeContainer(this.mySelectController);
    }.width('100%')
  }
}
```

### Toggle18+

type Toggle = TypedFrameNode<ToggleInterface, ToggleAttribute>

[Toggle](ts-basic-components-toggle.md)类型的FrameNode节点类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| TypedFrameNode<ToggleInterface, ToggleAttribute> | 提供Toggle类型FrameNode节点。  ToggleInterface用于[TypedFrameNode](js-apis-arkui-framenode.md#typedframenode12)的[initialize](js-apis-arkui-framenode.md#属性)接口的入参，入参为Toggle组件的构造函数类型。  ToggleAttribute用于TypedFrameNode的[attribute](js-apis-arkui-framenode.md#属性)接口的返回值，返回Toggle组件的属性设置对象。  ToggleInterface表示Toggle的[接口](ts-basic-components-toggle.md#接口)，ToggleAttribute表示Toggle的[属性](ts-basic-components-toggle.md#属性)。 |

### createNode('Toggle')18+

createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle

创建Toggle类型的FrameNode节点。使用typeNode创建Toggle节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Toggle' | 是 | 创建Toggle类型的节点。 |
| options | [ToggleOptions](ts-basic-components-toggle.md#toggleoptions18对象说明) | 否 | 创建Toggle节点的接口参数，仅可通过ToggleOptions中的type属性设置开关样式。不传入该参数时，需通过initialize接口设置Toggle的type属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Toggle](js-apis-arkui-framenode.md#toggle18) | Toggle类型的FrameNode节点。 |

**示例：**

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Toggle控制器
class MyToggleController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Toggle
    let toggleSwitch = typeNode.createNode(uiContext, 'Toggle')
    toggleSwitch.initialize({ type: ToggleType.Switch })
    col.appendChild(toggleSwitch)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myToggleController: MyToggleController = new MyToggleController();

  build() {
    Column({ space: 5 }) {
      Text('ToggleSample')
      NodeContainer(this.myToggleController);

    }.width('100%')
  }
}
```

### getAttribute('Toggle')20+

getAttribute(node: FrameNode, nodeType: 'Toggle'): ToggleAttribute | undefined

获取Toggle节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Toggle控制器
class MyToggleController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Toggle
    let toggleSwitch = typeNode.createNode(uiContext, 'Toggle')
    toggleSwitch.initialize({ type: ToggleType.Switch })
    typeNode.getAttribute(toggleSwitch,'Toggle')?.selectedColor(Color.Orange)
    col.appendChild(toggleSwitch)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myToggleController: MyToggleController = new MyToggleController();

  build() {
    Column({ space: 5 }) {
      Text('ToggleSample')
      NodeContainer(this.myToggleController);

    }.width('100%')
  }
}
```

## NodeAdapter12+

NodeAdapter提供FrameNode的数据懒加载能力，通过[LazyForEach](ts-rendering-control-lazyforeach.md)实现接口功能。适用于长列表等需要按需加载节点数据的场景，可提升渲染性能并降低内存占用。

**说明** 

NodeAdapter各方法中的数值入参（如start、count、from、to）不能为负数，入参为负数时不做处理。

**示例：**

请参考[NodeAdapter使用示例](js-apis-arkui-framenode.md#nodeadapter使用示例)。

### constructor12+

constructor()

NodeAdapter的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### dispose12+

dispose(): void

立即释放当前的NodeAdapter。如果是已绑定的状态，会先进行解绑操作，再释放当前的NodeAdapter。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### totalNodeCount12+

set totalNodeCount(count: number)

设置数据节点总数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 数据节点总数。  取值范围：[0, +∞) |

get totalNodeCount(): number

获取数据节点总数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 数据节点总数。  取值范围：[0, +∞) |

### reloadAllItems12+

reloadAllItems(): void

重新加载全部数据操作。实际调用了LazyForEach中的[onDataReloaded](ts-rendering-control-lazyforeach.md#ondatareloaded)接口通知组件重新加载所有数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### reloadItem12+

reloadItem(start: number, count: number): void

从索引值开始重新加载指定数量的节点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 重新加载的节点开始索引值。  取值范围：[0, +∞) |
| count | number | 是 | 重新加载数据节点的数量。  取值范围：[0, +∞) |

### removeItem12+

removeItem(start: number, count: number): void

从索引值开始删除指定数量的节点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 删除的节点开始索引值。  取值范围：[0, +∞) |
| count | number | 是 | 删除数据节点的数量。  取值范围：[0, +∞) |

### insertItem12+

insertItem(start: number, count: number): void

从索引值开始新增指定数量的节点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 新增的节点开始索引值。  取值范围：[0, +∞) |
| count | number | 是 | 新增数据节点的数量。  取值范围：[0, +∞) |

### moveItem12+

moveItem(from: number, to: number): void

将数据从原始索引移动到目的索引。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 | 数据移动的原始索引值。  取值范围：[0, +∞) |
| to | number | 是 | 数据移动的目的索引值。  取值范围：[0, +∞) |

### getAllAvailableItems12+

getAllAvailableItems(): Array<FrameNode>

获取所有有效数据。有效节点数据包括显示在屏幕上的节点以及预加载的节点。其中预加载节点的数量可依照LazyForEach的[使用限制](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#使用限制)，调整父容器的cachedCount属性进行设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[FrameNode](js-apis-arkui-framenode.md#framenode-1)> | FrameNode数据节点集合。 |

### onAttachToNode12+

onAttachToNode?(target: FrameNode): void

FrameNode绑定NodeAdapter时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 绑定NodeAdapter的FrameNode节点。 |

### onDetachFromNode12+

onDetachFromNode?(): void

解除绑定时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### onGetChildId12+

onGetChildId?(index: number): number

节点首次加载或新节点滑入时回调。传入的index参数用于自定义生成Id，需要开发者自行保证根据不同index生成Id的唯一性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

onCreateChild?(index: number): FrameNode

节点首次加载或新节点滑入时回调。建议开发者在添加子组件时，遵循声明式组件中子组件的约束。例如，WaterFlow支持添加FlowItem子节点。父节点根据子节点的索引与key值判断是否触发了节点首次加载或新节点滑入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 加载节点索引值。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 返回开发者创建的FrameNode节点。 |

### onDisposeChild12+

onDisposeChild?(id: number, node: FrameNode): void

子节点即将销毁时回调。既不显示在屏幕上，也不处于预加载范围内的节点都属于即将销毁的节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 即将销毁的子节点id。 |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 即将销毁的FrameNode节点。 |

### onUpdateChild12+

onUpdateChild?(id: number, node: FrameNode): void

重新加载的数据节点被复用时回调。已缓存节点的key值与被复用节点一致时进行节点复用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 复用节点的id。 |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 被复用的FrameNode节点。 |

### attachNodeAdapter12+

static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean

给FrameNode绑定一个NodeAdapter。一个节点只能绑定一个NodeAdapter。已经绑定NodeAdapter的再次绑定会失败并返回false。

**说明** 

支持绑定的组件：Column、Row、Stack、GridRow、Flex、Swiper、RelativeContainer、List、ListItemGroup、WaterFlow、Grid。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adapter | [NodeAdapter](js-apis-arkui-framenode.md#nodeadapter12) | 是 | 定义懒加载的NodeAdapter类。 |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 绑定的FrameNode节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 绑定结果，返回true绑定成功，false绑定失败。 |

### detachNodeAdapter12+

static detachNodeAdapter(node: FrameNode): void

解除绑定操作，解除FrameNode节点绑定的NodeAdapter。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 要解除绑定的FrameNode节点。 |

### isDisposed20+

isDisposed(): boolean

查询当前NodeAdapter对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用该节点的其他接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

请参考[检验NodeAdapter是否有效示例](js-apis-arkui-framenode.md#检验nodeadapter是否有效示例)。

## 自定义具体类型节点示例

以Text节点为例，创建Text类型节点。

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute.width(100)
      .height(50)
      .borderColor(Color.Gray)
      .borderWidth(1)
      .margin({ left: 10 });
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%').height('100%').margin({ top: 5 });
    node.appendChild(col);
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello').fontColor(Color.Blue).fontSize(14);
    col.appendChild(text);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController);
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/20i1BtrnT6yv7tISUUdzYQ/zh-cn_image_0000002712245822.png)

## 节点操作示例

```ts
import { NodeController, FrameNode, UIContext, typeNode } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

const TEST_TAG: string = 'FrameNode '

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  public childList: Array<FrameNode> = new Array<FrameNode>();
  private rootNode: FrameNode | null = null;
  private uiContext: UIContext | null = null;
  private childrenCount: number = 0;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.uiContext = uiContext;

    this.frameNode = new FrameNode(uiContext);
    this.frameNode.commonAttribute.backgroundColor(Color.Pink);
    this.frameNode.commonAttribute.size({ width: 100, height: 100 });
    this.addCommonEvent(this.frameNode)
    this.rootNode.appendChild(this.frameNode);
    this.childrenCount = this.childrenCount + 1;

    // 批量创建10个子节点并挂载到主节点
    for (let i = 0; i < 10; i++) {
      let childNode = new FrameNode(uiContext);
      this.childList.push(childNode);
      this.frameNode.appendChild(childNode);
    }

    // 创建Stack容器节点
    let stackNode = typeNode.createNode(uiContext, 'Stack');
    this.frameNode.appendChild(stackNode);
    return this.rootNode;
  }

  // 为节点添加点击事件
  addCommonEvent(frameNode: FrameNode) {
    frameNode.commonEvent.setOnClick((event: ClickEvent) => {
      console.info(`Click FrameNode: ${JSON.stringify(event)}`)
    })
  }

  createFrameNode() {
    let frameNode = new FrameNode(this.uiContext!);
    frameNode.commonAttribute.backgroundColor(Color.Pink);
    frameNode.commonAttribute.size({ width: 100, height: 100 });
    frameNode.commonAttribute.position({ x: this.childrenCount * 120, y: 0 });

    return frameNode;
  }

  // 追加子节点到根节点的末尾
  appendChild() {
    const childNode = this.createFrameNode();
    this.rootNode!.appendChild(childNode);
    this.childrenCount = this.childrenCount + 1;
  }

  // 在指定索引节点后插入新节点
  insertChildAfter(index: number) {
    let insertNode = this.createFrameNode();
    let childNode = this.rootNode!.getChild(index);
    this.rootNode!.insertChildAfter(insertNode, childNode);
    this.childrenCount = this.childrenCount + 1;
  }

  // 移除指定索引的子节点
  removeChild(index: number) {
    let childNode = this.rootNode!.getChild(index);
    if (childNode == null) {
      console.info(`${TEST_TAG} getchild at index {${index}} : fail`);
      return;
    }
    this.rootNode!.removeChild(childNode);
    this.childrenCount = this.childrenCount - 1;
  }

  // 打印节点计数
  getChildNumber() {
    console.info(`${TEST_TAG} getChildNumber ${this.rootNode!.getChildrenCount()}`)
    console.info(`${TEST_TAG} children count is ${this.childrenCount}`);
  }

  // 清空所有子节点
  clearChildren() {
    this.rootNode!.clearChildren();
  }

  // 节点关系校验
  searchFrameNode() {
    if (this.rootNode!.getFirstChild() === null) {
      console.info(`${TEST_TAG} the rootNode does not have child node.`)
    }
    if (this.rootNode!.getFirstChild() === this.frameNode) {
      console.info(`${TEST_TAG} getFirstChild result: success. The first child of the rootNode is equals to frameNode.`);
    } else {
      console.info(`${TEST_TAG} getFirstChild result: fail. The first child of the rootNode is not equals to frameNode.`);
    }
    if (this.frameNode!.getChild(5) === this.frameNode!.getChild(4)!.getNextSibling()) {
      console.info(`${TEST_TAG} getNextSibling result: success.`);
    } else {
      console.info(`${TEST_TAG} getNextSibling result: fail.`);
    }
    if (this.frameNode!.getChild(3) === this.frameNode!.getChild(4)!.getPreviousSibling()) {
      console.info(`${TEST_TAG} getPreviousSibling result: success.`);
    } else {
      console.info(`${TEST_TAG} getPreviousSibling result: fail.`);
    }
    if (this.rootNode!.getFirstChild() !== null && this.rootNode!.getFirstChild()!.getParent() === this.rootNode) {
      console.info(`${TEST_TAG} getParent result: success.`);
    } else {
      console.info(`${TEST_TAG} getParent result: fail.`);
    }
    if (this.rootNode!.getParent() !== null) {
      console.info(`${TEST_TAG} get ArkTsNode success.`)
      console.info(`${TEST_TAG} check rootNode whether is modifiable ${this.rootNode!.isModifiable()}`)
      console.info(`${TEST_TAG} check getParent whether is modifiable ${this.rootNode!.getParent()!.isModifiable()}`)
    } else {
      console.info(`${TEST_TAG} get ArkTsNode fail.`);
    }
  }

  // 将指定节点移动到根节点的第一个位置
  moveFrameNode() {
    const currentNode = this.frameNode!.getChild(10);
    try {
      currentNode!.moveTo(this.rootNode, 0);
      if (this.rootNode!.getChild(0) === currentNode) {
        console.info(`${TEST_TAG} moveTo result: success.`);
      } else {
        console.info(`${TEST_TAG} moveTo result: fail.`);
      }
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
      console.error(`${TEST_TAG} moveTo result: fail.`);
    }
  }

  getPositionToWindow() {
    let positionToWindow = this.rootNode?.getPositionToWindow();
    console.info(`${TEST_TAG}${JSON.stringify(positionToWindow)}`);
  }

  getPositionToParent() {
    let positionToParent = this.rootNode?.getPositionToParent();
    console.info(`${TEST_TAG}${JSON.stringify(positionToParent)}`);
  }

  getPositionToScreen() {
    let positionToScreen = this.rootNode?.getPositionToScreen();
    console.info(`${TEST_TAG}${JSON.stringify(positionToScreen)}`);
  }

  getGlobalPositionOnDisplay() {
    let positionOnGlobalDisplay = this.rootNode?.getGlobalPositionOnDisplay();
    console.info(`${TEST_TAG}${JSON.stringify(positionOnGlobalDisplay)}`);
  }

  getPositionToWindowWithTransform() {
    let positionToWindowWithTransform = this.rootNode?.getPositionToWindowWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToWindowWithTransform)}`);
  }

  getPositionToParentWithTransform() {
    let positionToParentWithTransform = this.rootNode?.getPositionToParentWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToParentWithTransform)}`);
  }

  getPositionToScreenWithTransform() {
    let positionToScreenWithTransform = this.rootNode?.getPositionToScreenWithTransform();
    console.info(`${TEST_TAG}${JSON.stringify(positionToScreenWithTransform)}`);
  }

  getMeasuredSize() {
    let measuredSize = this.frameNode?.getMeasuredSize();
    console.info(`${TEST_TAG}${JSON.stringify(measuredSize)}`);
  }

  getLayoutPosition() {
    let layoutPosition = this.frameNode?.getLayoutPosition();
    console.info(`${TEST_TAG}${JSON.stringify(layoutPosition)}`);
  }

  getUserConfigBorderWidth() {
    let userConfigBorderWidth = this.frameNode?.getUserConfigBorderWidth();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigBorderWidth)}`);
  }

  getUserConfigPadding() {
    let userConfigPadding = this.frameNode?.getUserConfigPadding();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigPadding)}`);
  }

  getUserConfigMargin() {
    let userConfigMargin = this.frameNode?.getUserConfigMargin();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigMargin)}`);
  }

  getUserConfigSize() {
    let userConfigSize = this.frameNode?.getUserConfigSize();
    console.info(`${TEST_TAG}${JSON.stringify(userConfigSize)}`);
  }

  getId() {
    let id = this.frameNode?.getId();
    console.info(`${TEST_TAG}${id}`);
  }

  getUniqueId() {
    let uniqueId = this.frameNode?.getUniqueId();
    console.info(`${TEST_TAG}${uniqueId}`);
  }

  getNodeType() {
    let nodeType = this.frameNode?.getNodeType();
    console.info(`${TEST_TAG}${nodeType}`);
  }

  getOpacity() {
    let opacity = this.frameNode?.getOpacity();
    console.info(`${TEST_TAG}${JSON.stringify(opacity)}`);
  }

  isVisible() {
    let visible = this.frameNode?.isVisible();
    console.info(`${TEST_TAG}${JSON.stringify(visible)}`);
  }

  isClipToFrame() {
    let clipToFrame = this.frameNode?.isClipToFrame();
    console.info(`${TEST_TAG}${JSON.stringify(clipToFrame)}`);
  }

  isAttached() {
    let attached = this.frameNode?.isAttached();
    console.info(`${TEST_TAG}${JSON.stringify(attached)}`);
  }

  getInspectorInfo() {
    let inspectorInfo = this.frameNode?.getInspectorInfo();
    console.info(`${TEST_TAG}${JSON.stringify(inspectorInfo)}`);
  }

  // 设置跨语言交互选项
  setCrossLanguageOptions() {
    console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions())}`);
    try {
      this.frameNode?.setCrossLanguageOptions({
        attributeSetting: true
      });
      console.info(`${TEST_TAG} setCrossLanguageOptions success.`);
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
      console.error(`${TEST_TAG} setCrossLanguageOptions fail.`);
    }
    console.info(`${TEST_TAG} getCrossLanguageOptions ${JSON.stringify(this.frameNode?.getCrossLanguageOptions())}`);
  }

  getInteractionEventBindingInfo() {
    let bindingInfo = this.frameNode?.getInteractionEventBindingInfo(EventQueryType.ON_CLICK);
    console.info(`${TEST_TAG}${bindingInfo?.baseEventRegistered}`);
    console.info(`${TEST_TAG}${bindingInfo?.nodeEventRegistered}`);
    console.info(`${TEST_TAG}${bindingInfo?.nativeEventRegistered}`);
    console.info(`${TEST_TAG}${bindingInfo?.builtInEventRegistered}`);
    console.info(`${TEST_TAG}${JSON.stringify(bindingInfo)}`);
  }

  throwError() {
    try {
      this.rootNode!.getParent()!.clearChildren();
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
    }
    try {
      this.rootNode!.getParent()!.appendChild(new FrameNode(this.uiContext));
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
    }
    try {
      this.rootNode!.getParent()!.removeChild(this.rootNode!.getParent()!.getChild(0));
    } catch (err) {
      console.error(`${TEST_TAG} ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();
  @State index: number = 0;

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Row() {
            Button('ADD')
              .onClick(() => {
                this.index++;
              })
            Button('DEC')
              .onClick(() => {
                this.index--;
              })
          }

          // 显示当前索引值
          Text('Current index is ' + this.index)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
        }

        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)

          // 自定义节点容器
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('appendChild')
          .width(300)
          .onClick(() => {
            this.myNodeController.appendChild();
          })
        Button('insertChildAfter')
          .width(300)
          .onClick(() => {
            this.myNodeController.insertChildAfter(this.index);
          })
        Button('removeChild')
          .width(300)
          .onClick(() => {
            this.myNodeController.removeChild(this.index);
          })
        Button('clearChildren')
          .width(300)
          .onClick(() => {
            this.myNodeController.clearChildren();
          })
        Button('getChildNumber')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildNumber();
          })
        Button('searchFrameNode')
          .width(300)
          .onClick(() => {
            this.myNodeController.searchFrameNode();
          })
        Button('moveFrameNode')
          .width(300)
          .onClick(() => {
            this.myNodeController.moveFrameNode();
          })
        Button('getPositionToWindow')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToWindow();
          })
        Button('getPositionToParent')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToParent();
          })
        Button('getPositionToScreen')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToScreen();
          })
        Button('getGlobalPositionOnDisplay')
          .width(300)
          .onClick(() => {
            this.myNodeController.getGlobalPositionOnDisplay();
          })
        Button('getPositionToParentWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToParentWithTransform();
          })
        Button('getPositionToWindowWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToWindowWithTransform();
          })
        Button('getPositionToScreenWithTransform')
          .width(300)
          .onClick(() => {
            this.myNodeController.getPositionToScreenWithTransform();
          })
        Button('getMeasuredSize')
          .width(300)
          .onClick(() => {
            this.myNodeController.getMeasuredSize();
          })
        Button('getLayoutPosition')
          .width(300)
          .onClick(() => {
            this.myNodeController.getLayoutPosition();
          })
        Button('getUserConfigBorderWidth')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigBorderWidth();
          })
        Button('getUserConfigPadding')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigPadding();
          })
        Button('getUserConfigMargin')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigMargin();
          })
        Button('getUserConfigSize')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUserConfigSize();
          })
        Button('getId')
          .width(300)
          .onClick(() => {
            this.myNodeController.getId();
          })
        Button('getUniqueId')
          .width(300)
          .onClick(() => {
            this.myNodeController.getUniqueId();
          })
        Button('getNodeType')
          .width(300)
          .onClick(() => {
            this.myNodeController.getNodeType();
          })
        Button('getOpacity')
          .width(300)
          .onClick(() => {
            this.myNodeController.getOpacity();
          })
        Button('isVisible')
          .width(300)
          .onClick(() => {
            this.myNodeController.isVisible();
          })
        Button('isClipToFrame')
          .width(300)
          .onClick(() => {
            this.myNodeController.isClipToFrame();
          })
        Button('isAttached')
          .width(300)
          .onClick(() => {
            this.myNodeController.isAttached();
          })
        Button('getInspectorInfo')
          .width(300)
          .onClick(() => {
            this.myNodeController.getInspectorInfo();
          })
        Button('getCustomProperty')
          .width(300)
          .onClick(() => {
            const uiContext: UIContext = this.getUIContext();
            if (uiContext) {
              // 通过组件ID获取对应的FrameNode节点
              const node: FrameNode | null = uiContext.getFrameNodeById('Test_Button') || null;
              if (node) {
                for (let i = 1; i < 4; i++) {
                  const key = 'customProperty' + i;
                  const property = node.getCustomProperty(key);
                  console.info(`${TEST_TAG}${key}`, JSON.stringify(property));
                }
              }
            }
          })
          .id('Test_Button')
          .customProperty('customProperty1', {
            'number': 10,
            'string': 'this is a string',
            'bool': true,
            'object': {
              'name': 'name',
              'value': 100
            }
          })
          .customProperty('customProperty2', {})
          .customProperty('customProperty2', undefined)
        Button('setCrossLanguageOptions')
          .width(300)
          .onClick(() => {
            this.myNodeController.setCrossLanguageOptions();
          })
        Button('getInteractionEventBindingInfo')
          .width(300)
          .onClick(() => {
            this.myNodeController.getInteractionEventBindingInfo();
          })
        Button('throwError')
          .width(300)
          .onClick(() => {
            this.myNodeController.throwError();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

## LazyForEach场景节点操作示例

```ts
import { NodeController, FrameNode, UIContext, BuilderNode, ExpandMode, LengthUnit } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode '

// BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): string {
    return this.originDataArray[index];
  }

  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
    })
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
    })
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
    })
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
    })
  }

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    })
  }
}

// 自定义数据管理类管理string数组
class MyDataSource extends BasicDataSource {
  private dataArray: string[] = []

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string {
    return this.dataArray[index];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

class Params {
  data: MyDataSource | null = null;
  scroller: Scroller | null = null;

  constructor(data: MyDataSource, scroller: Scroller) {
    this.data = data;
    this.scroller = scroller;
  }
}

@Builder
function buildData(params: Params) {
  List({ scroller: params.scroller }) {
    LazyForEach(params.data, (item: string) => {
      ListItem() {
        Column() {
          Text(item)
            .fontSize(20)
            .onAppear(() => {
              console.info(`${TEST_TAG} node appear: ${item}`)
            })
            .backgroundColor(Color.Pink)
            .margin({
              top: 30,
              bottom: 30,
              left: 10,
              right: 10
            })
        }
      }
      .id(item)
    }, (item: string) => item)
  }
  .cachedCount(5)
  .listDirection(Axis.Horizontal)
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private uiContext: UIContext | null = null;
  private data: MyDataSource = new MyDataSource();
  private scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    for (let i = 0; i <= 20; i++) {
      this.data.pushData(`N${i}`);
    }
    const params: Params = new Params(this.data, this.scroller);
    const dataNode: BuilderNode<[Params]> = new BuilderNode(uiContext);
    dataNode.build(wrapBuilder<[Params]>(buildData), params);
    this.rootNode = dataNode.getFrameNode();
    const scrollToIndexOptions: ScrollToIndexOptions = {
      extraOffset: {
        value: 20, unit: LengthUnit.VP
      }
    };
    this.scroller.scrollToIndex(6, true, ScrollAlign.START, scrollToIndexOptions);
    return this.rootNode;
  }

  getFirstChildIndexWithoutExpand() {
    console.info(`${TEST_TAG} getFirstChildIndexWithoutExpand: ${this.rootNode!.getFirstChildIndexWithoutExpand()}`);
  }

  getLastChildIndexWithoutExpand() {
    console.info(`${TEST_TAG} getLastChildIndexWithoutExpand: ${this.rootNode!.getLastChildIndexWithoutExpand()}`);
  }

  getChildWithNotExpand() {
    const childNode = this.rootNode!.getChild(3, ExpandMode.NOT_EXPAND);
    console.info(`${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND): ${childNode!.getId()}`);
    if (childNode!.getId() === 'N9') {
      console.info(`${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND) result: success.`);
    } else {
      console.info(`${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND) result: fail.`);
    }
  }

  getChildWithExpand() {
    const childNode = this.rootNode!.getChild(3, ExpandMode.EXPAND);
    console.info(`${TEST_TAG} getChild(3, ExpandMode.EXPAND): ${childNode!.getId()}`);
    if (childNode!.getId() === 'N3') {
      console.info(`${TEST_TAG} getChild(3, ExpandMode.EXPAND) result: success.`);
    } else {
      console.info(`${TEST_TAG} getChild(3, ExpandMode.EXPAND) result: fail.`);
    }
  }

  getChildWithLazyExpand() {
    const childNode = this.rootNode!.getChild(3, ExpandMode.LAZY_EXPAND);
    console.info(`${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND): ${childNode!.getId()}`);
    if (childNode!.getId() === 'N3') {
      console.info(`${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND) result: success.`);
    } else {
      console.info(`${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND) result: fail.`);
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  private scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Column() {
          Text('This is a NodeContainer.')
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .fontSize(16)
          NodeContainer(this.myNodeController)
            .borderWidth(1)
            .width(300)
            .height(100)
        }

        Button('getFirstChildIndexWithoutExpand')
          .width(300)
          .onClick(() => {
            this.myNodeController.getFirstChildIndexWithoutExpand();
          })
        Button('getLastChildIndexWithoutExpand')
          .width(300)
          .onClick(() => {
            this.myNodeController.getLastChildIndexWithoutExpand();
          })
        Button('getChildWithNotExpand')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildWithNotExpand();
          })
        Button('getChildWithExpand')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildWithExpand();
          })
        Button('getChildWithLazyExpand')
          .width(300)
          .onClick(() => {
            this.myNodeController.getChildWithLazyExpand();
          })
      }
      .width('100%')
    }
    .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
  }
}
```

## 基础事件示例

```ts
import { NodeController, FrameNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width(100)
      .height(100)
      .backgroundColor(Color.Pink);
    this.addCommonEvent(this.rootNode);
    return this.rootNode;
  }

  // 为FrameNode绑定交互事件
  addCommonEvent(frameNode: FrameNode) {

    // 悬浮事件
    frameNode.commonEvent.setOnHover(((isHover: boolean, event: HoverEvent): void => {
      console.info(`isHover FrameNode: ${isHover}`);
      console.info(`isHover FrameNode: ${JSON.stringify(event)}`);
      event.stopPropagation();
    }))

    // 点击事件
    frameNode.commonEvent.setOnClick((event: ClickEvent) => {
      console.info(`Click FrameNode: ${JSON.stringify(event)}`)
    })

    // 触摸事件
    frameNode.commonEvent.setOnTouch((event: TouchEvent) => {
      console.info(`touch FrameNode: ${JSON.stringify(event)}`)
    })

    // 显示事件
    frameNode.commonEvent.setOnAppear(() => {
      console.info(`on Appear FrameNode`)
    })

    // 消失事件
    frameNode.commonEvent.setOnDisappear(() => {
      console.info(`onDisAppear FrameNode`)
    })

    // 获焦事件
    frameNode.commonEvent.setOnFocus(() => {
      console.info(`onFocus FrameNode`)
    })

    // 失焦事件
    frameNode.commonEvent.setOnBlur(() => {
      console.info(`onBlur FrameNode`)
    })

    // 键盘事件
    frameNode.commonEvent.setOnKeyEvent((event: KeyEvent) => {
      console.info(`Key FrameNode: ${JSON.stringify(event)}`)
    })

    // 鼠标事件
    frameNode.commonEvent.setOnMouse((event: MouseEvent) => {
      console.info(`Mouse FrameNode: ${JSON.stringify(event)}`)
    })

    // 组件区域变化事件
    frameNode.commonEvent.setOnSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
      console.info(`onSizeChange FrameNode: oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`)
    })
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      Button('add CommonEvent to Text')
        .onClick(() => {
          this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling() !)
        })
      Text('this is a Text')
        .fontSize(16)
        .borderWidth(1)
        .onHover(((isHover: boolean, event: HoverEvent): void => {
          console.info(`isHover Text: ${isHover}`);
          console.info(`isHover Text: ${JSON.stringify(event)}`);
          event.stopPropagation();  // 阻止事件冒泡
        }))
        .onClick((event: ClickEvent) => {
          console.info(`Click Text    : ${JSON.stringify(event)}`)
        })
        .onTouch((event: TouchEvent) => {
          console.info(`touch Text    : ${JSON.stringify(event)}`)
        })
        .onAppear(() => {
          console.info(`on Appear Text`)
        })
        .onDisAppear(() => {
          console.info(`onDisAppear Text`)
        })
        .onFocus(() => {
          console.info(`onFocus Text`)
        })
        .onBlur(() => {
          console.info(`onBlur Text`)
        })
        .onKeyEvent((event: KeyEvent) => {
          console.info(`Key Text    : ${JSON.stringify(event)}`)
        })
        .onMouse((event: MouseEvent) => {
          console.info(`Mouse Text : ${JSON.stringify(event)}`)
        })
        .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
          console.info(`onSizeChange Text: oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`)
        })
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(300)
        .height(100)
    }.width('100%')
  }
}
```

## LazyForEach场景基础事件使用示例

```ts
// index.ets
import {Track, TrackManager, TrackNode} from './track'

@Builder
function page1() {
  Column() {
    Text('Page1')
    PageList().height('90%')
    Button('DumpMessage')
      .onClick(() => {
        TrackManager.get().dump()
      })

  }.width('100%').height('100%')
}

class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): string {
    return this.originDataArray[index];
  }

  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }
}

// 自定义数据管理类管理string数组
class MyDataSource extends BasicDataSource {
  private dataArray: string[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string {
    return this.dataArray[index];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

@Component
struct PageList {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i <= 100; i++) {
      this.data.pushData(`Hello ${i}`)
    }
  }

  build() {
    List({ space: 3 }) {
      LazyForEach(this.data, (item: string, index: number) => {
        ListItem() {
          // 通过TrackNode对组件进行封装埋点
          TrackNode({track: new Track().tag('xxx'+ item).id(index + 30000)}) {
            Row() {
              Text(item).fontSize(30)
                .onClick(() => {
                })
            }.margin({ left: 10, right: 10 })
          }
        }
      }, (item: string) => item)
    }.cachedCount(5)
  }
}

@Entry
@Component
struct TrackTest {
  pageInfos: NavPathStack = new NavPathStack()
  build() {
    Row() {
      TrackNode({ track: new Track().tag('root').id(10000)}) {
        page1()
      }
    }
  }

  aboutToAppear(): void {
    TrackManager.get().startListenClick(this.getUIContext())
  }
}
```

```ts
// ./track.ets
import { FrameNode, Rect } from '@kit.ArkUI';

@Component
export struct TrackNode {
  @BuilderParam closer: VoidCallback = this.defaultBuilder
  track: Track | null = null
  trackShadow: TrackShadow = new TrackShadow()

  @Builder defaultBuilder() {
  }

  build() {
    this.closer()
  }

  aboutToAppear(): void {
    // 稍后使用onDidBuild
  }

  aboutToDisappear(): void {
    TrackManager.get().removeTrack(this.trackShadow.id)
    console.info(`Track disappear:${this.trackShadow.id}`)
  }

  onDidBuild(): void {
    // 构建埋点的虚拟树，获取的node为当前页面的根节点（用例中为Row）
    let uid = this.getUniqueId()
    let node: FrameNode | null = this.getUIContext().getFrameNodeByUniqueId(uid);
    console.info(`Track onDidBuild node:${node?.getNodeType()}`);
    if (node === null) {
      return
    }
    this.trackShadow.node = node
    this.trackShadow.id = node?.getUniqueId()
    this.trackShadow.track = this.track;
    TrackManager.get().addTrack(this.trackShadow.id, this.trackShadow)
    // 通过setOnVisibleAreaApproximateChange监听记录埋点组件的可视区域
    node?.commonEvent.setOnVisibleAreaApproximateChange(
      { ratios: [0, 0.1, 0.2, 0.5, 0.8, 1], expectedUpdateInterval: 500 },
      (ratioInc: boolean, ratio: number) => {
        console.info(`Node ${node?.getUniqueId()}:${node?.getNodeType()} is visibleRatio is ${ratio}`);
        this.trackShadow.visibleRatio = ratio
      })

    let parent: FrameNode | null = node?.getParent()

    let attachTrackToParent: (parent: FrameNode | null) => boolean =
      (parent: FrameNode | null) => {
        while (parent !== null) {
          let parentTrack = TrackManager.get().getTrackById(parent.getUniqueId())
          if (parentTrack !== undefined) {
            parentTrack.childIds.add(this.trackShadow.id)
            this.trackShadow.parentId = parentTrack.id
            return true;
          }
          parent = parent.getParent()
        }
        return false;
      }
    let attached = attachTrackToParent(parent);

    if (!attached) {
      node?.commonEvent.setOnAppear(() => {
        let attached = attachTrackToParent(parent);
        if (attached) {
          console.info(`Track lazy attached:${this.trackShadow.id}`)
        }
      })
    }
  }
}

export class Track {
  public areaPercent: number = 0
  private trackTag: string = ''
  private trackId: number = 0

  constructor() {
  }

  tag(newTag: string): Track {
    this.trackTag = newTag;
    return this;
  }

  id(newId: number): Track {
    this.trackId = newId;
    return this;
  }
}

export class TrackShadow {
  public node: FrameNode | null = null
  public id: number = -1
  public track: Track | null = null
  public childIds: Set<number> = new Set()
  public parentId: number = -1
  public visibleRect: Rect = { left: 0, top: 0, right: 0, bottom: 0 }
  public area: number = 0
  public visibleRatio: number = 0

  // 通过全局dump输出埋点树的信息
  dump(depth: number = 0): void {
    console.info(`Track DP:${depth} id:${this.id} areaPer:${this.track?.areaPercent} visibleRatio:${this.visibleRatio}`)
    this.childIds.forEach((value: number) => {
      TrackManager.get().getTrackById(value)?.dump(depth + 1)
    })
  }
}

export class TrackManager {
  static instance: TrackManager
  private trackMap: Map<number, TrackShadow> = new Map()
  private rootTrack: TrackShadow | null = null

  static get(): TrackManager {
    if (TrackManager.instance !== undefined) {
      return TrackManager.instance
    }
    TrackManager.instance = new TrackManager()
    return TrackManager.instance
  }

  addTrack(id: number, track: TrackShadow) {
    if (this.trackMap.size == 0) {
      this.rootTrack = track
    }
    console.info(`Track add id:${id}`)
    this.trackMap.set(id, track)
  }

  removeTrack(id: number) {
    let current = this.getTrackById(id)
    if (current !== undefined) {
      this.trackMap.delete(id)
      let parent = this.getTrackById(current?.parentId)
      parent?.childIds.delete(id)
    }
  }

  getTrackById(id: number): TrackShadow | undefined {
    return this.trackMap.get(id)
  }

  startListenClick(context: UIContext) {
    // 通过无感监听获取FrameNode查找埋点信息
    context.getUIObserver().on('willClick', (event: ClickEvent, node?: FrameNode) => {
      console.info(`Track clicked:${node}`)
      if (node == undefined) {
        return
      }
      let track = this.getTrackById(node.getUniqueId())
      track?.dump(0);
    })
  }

  updateVisibleInfo(track: TrackShadow): void {
    // 更新埋点信息
  }

  dump(): void {
    this.rootTrack?.dump(0)
  }
}
```

## 手势事件示例

```ts
import { NodeController, FrameNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute
      .overlay('This is a FrameNode')
      .backgroundColor(Color.Pink)
      .width('100%')
      .height('100%');
    this.addGestureEvent(this.rootNode);
    return this.rootNode;
  }

  addGestureEvent(frameNode: FrameNode) {
    frameNode.gestureEvent.addGesture(new PanGestureHandler()
        .onActionStart((event: GestureEvent) => {
            console.info(`Pan start: ${JSON.stringify(event)}`);
        })
        .onActionUpdate((event: GestureEvent) => {
            console.info(`Pan update: ${JSON.stringify(event)}`);
        })
        .onActionEnd((event: GestureEvent) => {
            console.info(`Pan end: ${JSON.stringify(event)}`);
        })
        .onActionCancel(() => {
            console.info('Pan cancel');
        })
    )
    frameNode.gestureEvent.addGesture(new LongPressGestureHandler()
        .onAction((event: GestureEvent) => {
            console.info(`Long press action: ${JSON.stringify(event)}`);
        })
        .onActionEnd((event: GestureEvent) => {
            console.info(`Long press action end: ${JSON.stringify(event)}`);
        })
        .onActionCancel(() => {
            console.info('Long press cancel');
        })
    )
    frameNode.gestureEvent.addGesture(new TapGestureHandler()
        .onAction((event: GestureEvent) => {
            console.info(`Tap action: ${JSON.stringify(event)}`);
        })
    )
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(300)
        .height(300)
    }.width('100%')
  }
}
```

## 节点自定义示例

```ts
import { UIContext, DrawContext, FrameNode, NodeController, LayoutConstraint, Size, Position } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

function getChildLayoutConstraint(constraint: LayoutConstraint, child: FrameNode): LayoutConstraint {
  const size = child.getUserConfigSize();
  const width = Math.max(
    Math.min(constraint.maxSize.width, size.width.value),
    constraint.minSize.width
  );
  const height = Math.max(
    Math.min(constraint.maxSize.height, size.height.value),
    constraint.minSize.height
  );
  const finalSize: Size = { width, height };
  const res: LayoutConstraint = {
    maxSize: finalSize,
    minSize: finalSize,
    percentReference: finalSize
  };

  return res;
}

// 自定义FrameNode实现自定义布局函数
class MyFrameNode extends FrameNode {
  public width: number = 10;
  private space: number = 1;

  onMeasure(constraint: LayoutConstraint): void {
    let sizeRes: Size = { width: 100, height: 100 };
    for (let i = 0; i < this.getChildrenCount(); i++) {
      let child = this.getChild(i);
      if (child) {
        let childConstraint = getChildLayoutConstraint(constraint, child);
        child.measure(childConstraint);
        let size = child.getMeasuredSize();
        sizeRes.height += size.height + this.space;
        sizeRes.width = Math.max(sizeRes.width, size.width);
      }
    }
    this.setMeasuredSize(sizeRes);
  }

  onLayout(position: Position): void {
    let y = 0;
    for (let i = 0; i < this.getChildrenCount(); i++) {
      let child = this.getChild(i);
      if (child) {
        child.layout({
          x: 20,
          y: y
        });
        y += child.getMeasuredSize().height + this.space;
      }
    }
    this.setLayoutPosition(position);
  }

  onDraw(context: DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    canvas.attachPen(pen);
    canvas.drawRect({
      left: 0,
      right: this.width,
      top: 0,
      bottom: this.width
    });
    canvas.detachPen();
  }

  addWidth() {
    this.width += 10;
  }
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: MyFrameNode | null = null;

  makeNode(context: UIContext): FrameNode | null {
    this.rootNode = new MyFrameNode(context);
    this.rootNode?.commonAttribute?.size({ width: 100, height: 100 }).backgroundColor(Color.Green);
    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      Column() {
        NodeContainer(this.nodeController)
          .width('100%')
          .height(100)
          .backgroundColor('#FFF0F0F0')
        Button('Invalidate')
          .onClick(() => {
            this.nodeController?.rootNode?.addWidth();
            this.nodeController?.rootNode?.invalidate();
          })
        Button('UpdateLayout')
          .onClick(() => {
            this.nodeController?.rootNode?.setNeedsLayout();
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

## NodeAdapter使用示例

```ts
import { FrameNode, NodeController, NodeAdapter, typeNode } from '@kit.ArkUI';

// 自定义NodeAdapter管理数据
class MyNodeAdapter extends NodeAdapter {
  uiContext: UIContext
  cachePool: Array<FrameNode> = new Array();
  changed: boolean = false
  reloadTimes: number = 0;
  data: Array<string> = new Array();
  hostNode?: FrameNode

  constructor(uiContext: UIContext, count: number) {
    super();
    this.uiContext = uiContext;
    this.totalNodeCount = count;
    this.loadData();
  }

  reloadData(count: number): void {
    this.reloadTimes++;
    NodeAdapter.attachNodeAdapter(this, this.hostNode);
    this.totalNodeCount = count;
    this.loadData();
    this.reloadAllItems();
  }

  refreshData(): void {
    let items = this.getAllAvailableItems()
    console.info(`UINodeAdapter get All items:${items.length}`);
    this.reloadAllItems();
  }

  detachData(): void {
    NodeAdapter.detachNodeAdapter(this.hostNode);
    this.reloadTimes = 0;
  }

  loadData(): void {
    for (let i = 0; i < this.totalNodeCount; i++) {
      this.data[i] = 'Adapter ListItem ' + i + ' r:' + this.reloadTimes;
    }
  }

  changeData(from: number, count: number): void {
    this.changed = !this.changed;
    for (let i = 0; i < count; i++) {
      let index = i + from;
      this.data[index] = 'Adapter ListItem ' + (this.changed ? 'changed:' : '') + index + ' r:' + this.reloadTimes;
    }
    this.reloadItem(from, count);
  }

  insertData(from: number, count: number): void {
    for (let i = 0; i < count; i++) {
      let index = i + from;
      this.data.splice(index, 0, 'Adapter ListItem ' + from + '-' + i);
    }
    this.insertItem(from, count);
    this.totalNodeCount += count;
    console.info(`UINodeAdapter after insert count:${this.totalNodeCount}`);
  }

  removeData(from: number, count: number): void {
    let arr = this.data.splice(from, count);
    this.removeItem(from, count);
    this.totalNodeCount -= arr.length;
    console.info(`UINodeAdapter after remove count:${this.totalNodeCount}`);
  }

  moveData(from: number, to: number): void {
    let movedItem = this.data.splice(from, 1);
    this.data.splice(to, 0, movedItem[0]);
    this.moveItem(from, to);
  }

  onAttachToNode(target: FrameNode): void {
    console.info(`UINodeAdapter onAttachToNode id:${target.getUniqueId()}`);
    this.hostNode = target;
  }

  onDetachFromNode(): void {
    console.info('UINodeAdapter onDetachFromNode');
  }

  onGetChildId(index: number): number {
    console.info(`UINodeAdapter onGetChildId:${index}`);
    return index;
  }

  onCreateChild(index: number): FrameNode {
    console.info(`UINodeAdapter onCreateChild:${index}`);
    if (this.cachePool.length > 0) {
      let cacheNode = this.cachePool.pop();
      if (cacheNode !== undefined) {
        console.info(`UINodeAdapter onCreateChild reused id:${cacheNode.getUniqueId()}`);
        let text = cacheNode?.getFirstChild();
        let textNode = text as typeNode.Text;
        textNode?.initialize(this.data[index]).fontSize(20);
        return cacheNode;
      }
    }
    console.info('UINodeAdapter onCreateChild createNew');
    let itemNode = typeNode.createNode(this.uiContext, 'ListItem');
    let textNode = typeNode.createNode(this.uiContext, 'Text');
    textNode.initialize(this.data[index]).fontSize(20);
    itemNode.appendChild(textNode);
    return itemNode;
  }

  onDisposeChild(id: number, node: FrameNode): void {
    console.info(`UINodeAdapter onDisposeChild:${id}`);
    if (this.cachePool.length < 10) {
      if (!this.cachePool.includes(node)) {
        console.info(`UINodeAdapter caching node id:${node.getUniqueId()}`);
        this.cachePool.push(node);
      }
    } else {
      node.dispose();
    }
  }

  onUpdateChild(id: number, node: FrameNode): void {
    let index = id;
    let text = node.getFirstChild();
    let textNode = text as typeNode.Text;
    textNode?.initialize(this.data[index]).fontSize(20);
  }
}

// 继承NodeController实现自定义NodeAdapter控制器
class MyNodeAdapterController extends NodeController {
  rootNode: FrameNode | null = null;
  nodeAdapter: MyNodeAdapter | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    let listNode = typeNode.createNode(uiContext, 'List');
    listNode.initialize({ space: 3 }).borderWidth(2).borderColor(Color.Black);
    this.rootNode.appendChild(listNode);
    this.nodeAdapter = new MyNodeAdapter(uiContext, 100);
    NodeAdapter.attachNodeAdapter(this.nodeAdapter, listNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct ListNodeTest {
  adapterController: MyNodeAdapterController = new MyNodeAdapterController();

  build() {
    Column() {
      Text('ListNode Adapter');
      NodeContainer(this.adapterController)
        .width(300).height(300)
        .borderWidth(1).borderColor(Color.Black);
      Row() {
        Button('Reload')
          .onClick(() => {
            this.adapterController.nodeAdapter?.reloadData(50);
          })
        Button('Change')
          .onClick(() => {
            this.adapterController.nodeAdapter?.changeData(5, 10)
          })
        Button('Insert')
          .onClick(() => {
            this.adapterController.nodeAdapter?.insertData(10, 10);
          })
      }

      Row() {
        Button('Remove')
          .onClick(() => {
            this.adapterController.nodeAdapter?.removeData(10, 10);
          })
        Button('Move')
          .onClick(() => {
            this.adapterController.nodeAdapter?.moveData(2, 5);
          })
        Button('Refresh')
          .onClick(() => {
            this.adapterController.nodeAdapter?.refreshData();
          })
        Button('Detach')
          .onClick(() => {
            this.adapterController.nodeAdapter?.detachData();
          })
      }
    }.borderWidth(1)
    .width('100%')
  }
}
```

## 节点复用回收使用示例

```ts
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = 'this is a text'
}

@Builder
function buttonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .fontSize(20)
      .borderRadius(8)
      .borderWidth(2)
      .backgroundColor(Color.Grey)
  }
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private buttonNode: BuilderNode<[Params]> | null = null;
  private rootNode: FrameNode | null = null;
  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode {
    if (this.rootNode == null) {
      this.rootNode = new FrameNode(uiContext);
      this.buttonNode = new BuilderNode(uiContext);
      this.buttonNode.build(this.wrapBuilder, { text: 'This is a Button' });
      this.rootNode.appendChild(this.buttonNode.getFrameNode());
    }
    return this.rootNode;
  }

  onAttach(): void {
    console.info('myButton on attach');
  }

  onDetach(): void {
    console.info('myButton on detach');
  }

  // onBind时，子节点已经重新上树，此时调用reuse，保证子组件能重新被复用
  onBind(containerId: number): void {
    // 该方法触发子组件复用，全局复用场景下，复用FrameNode后端资源
    this.rootNode?.reuse();
    console.info('myButton reuse');
  }

  // onUnbind时，子节点已经完全下树，此时调用recycle，保证子组件能完全被回收
  onUnbind(containerId: number): void {
    // 该方法触发子组件的回收，全局复用场景下，回收FrameNode后端资源用于重新利用
    this.rootNode?.recycle();
    console.info('myButton recycle');
  }

  getButtonNode(): BuilderNode<[Params]> | null {
    return this.buttonNode;
  }

  getFrameNode(): FrameNode | null {
    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  @State buttonShow: boolean = true
  @State buttonIndex: number = 0
  public buttonController: MyNodeController = new MyNodeController();
  private buttonNull: null = null;
  private buttonControllerArray: Array<MyNodeController | null> = [this.buttonController, this.buttonNull]

  build() {
    Column() {
      Row() {
        Button('Bind/Unbind')
          .onClick(() => {
            this.buttonIndex++;
          }).margin(5)
        Button('onAttach/onDetach')
          .onClick(() => {
            this.buttonShow = !this.buttonShow
          }).margin(5)
      }

      if (this.buttonShow) {
        NodeContainer(this.buttonControllerArray[this.buttonIndex % this.buttonControllerArray.length])
      }
    }
    .padding({ left: 35, right: 35 })
    .width('100%')
    .height('100%')
  }
}
```

## 组件设置和删除多态样式状态示例

从API版本26.0.0开始，[UIState](js-apis-arkui-framenode.md#uistate20)新增HOVERED枚举。

```ts
import { NodeController, FrameNode, typeNode, UIState } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private isEnable: boolean = true;
  private theStatesToBeSupported =
    UIState.NORMAL | UIState.PRESSED | UIState.FOCUSED | UIState.DISABLED | UIState.SELECTED | UIState.HOVERED;

  makeNode(uiContext: UIContext): FrameNode | null {
    // 创建并组织节点关系
    let node = new FrameNode(uiContext);
    node.commonAttribute.width('100%')
      .height('100%')
      .borderColor(Color.Gray)
      .borderWidth(1)
      .margin({ left: 10 })

    let column = typeNode.createNode(uiContext, 'Column');
    column.initialize({ space: 20 })
      .width('100%')
      .height('100%')
    node.appendChild(column);

    let styleText = typeNode.createNode(uiContext, 'Text');
    styleText.initialize('StyleTarget')
      .width('50%')
      .height('5%')
      .margin({ top: 5, bottom: 5 })
      .fontSize(14)
      .fontColor(Color.White)
      .textAlign(TextAlign.Center)
      .backgroundColor(Color.Green)
      .borderWidth(2)
      .borderColor(Color.Black)
      .focusable(true)

    // 为Text组件添加多态样式处理能力
    styleText.addSupportedUIStates(this.theStatesToBeSupported, (node: FrameNode, currentState: number) => {
      if (currentState == UIState.NORMAL) { // 判断是否normal要使用等于
        // normal状态，刷新普通状态的UI效果
        console.info('Callback UIState.NORMAL')
        node.commonAttribute.backgroundColor(Color.Green)
        node.commonAttribute.borderWidth(2)
        node.commonAttribute.borderColor(Color.Black)
      }
      if ((currentState & UIState.HOVERED) == UIState.HOVERED) {
        // hovered状态，刷新悬浮状态的UI效果
        console.info('Callback UIState.HOVERED')
        node.commonAttribute.backgroundColor(Color.Blue)
      }
      if ((currentState & UIState.PRESSED) == UIState.PRESSED) {
        // pressed状态，刷新按压状态的UI效果
        console.info('Callback UIState.PRESSED')
        node.commonAttribute.backgroundColor(Color.Brown)
      }
      if ((currentState & UIState.FOCUSED) == UIState.FOCUSED) {
        // focused状态，刷新获焦状态的UI效果
        console.info('Callback UIState.FOCUSED')
        node.commonAttribute.borderWidth(5)
        node.commonAttribute.borderColor(Color.Yellow)
      }
      if ((currentState & UIState.DISABLED) == UIState.DISABLED) {
        // disabled状态，刷新禁用状态的UI效果
        console.info('Callback UIState.DISABLED')
        node.commonAttribute.backgroundColor(Color.Gray)
        node.commonAttribute.borderWidth(0)
      }
      if ((currentState & UIState.SELECTED) == UIState.SELECTED) {
        // selected状态，刷新选中状态的UI效果
        console.info('Callback UIState.SELECTED')
        node.commonAttribute.backgroundColor(Color.Pink)
      }
    }, false)

    column.appendChild(styleText);

    // 为Text组件删除多态样式处理能力
    let buttonRemove = typeNode.createNode(uiContext, 'Button');
    buttonRemove.initialize('RemoveUIStatus')
      .width('50%')
      .height('5%')
      .fontSize(14)
      .margin({ top: 5, bottom: 5 })
      .onClick(() => {
        styleText.removeSupportedUIStates(this.theStatesToBeSupported);
      });
    column.appendChild(buttonRemove);

    // 改变多态样式目标节点的使能状态
    let buttonEnable = typeNode.createNode(uiContext, 'Button');
    buttonEnable.initialize('DisableText')
      .width('50%')
      .height('5%')
      .fontSize(14)
      .margin({ top: 5, bottom: 5 })
      .onClick(() => {
        this.isEnable = !this.isEnable;
        buttonEnable.initialize(this.isEnable ? 'DisableText' : 'EnableText');
        styleText.attribute.enabled(this.isEnable)
      });
    column.appendChild(buttonEnable);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController);
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/BjbQP2jLQlahVSOA-0OiEg/zh-cn_image_0000002742004771.gif)

## 动画创建与取消示例

该示例说明在FrameNode上[createAnimation](js-apis-arkui-framenode.md#createanimation20)、[cancelAnimations](js-apis-arkui-framenode.md#cancelanimations20)、[getNodePropertyValue](js-apis-arkui-framenode.md#getnodepropertyvalue20)接口的用法。

```ts
import { FrameNode, NodeController, UIContext } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private isRunning: boolean = false; // 表示节点上动画是否在运行

  private startInitAnimation() {
    if (this.rootNode) {
      let result: boolean = this.rootNode.createAnimation(AnimationPropertyType.ROTATION, [0, 0, 0], [0, 0, 360],
        { duration: 3000, curve: Curve.Linear, iterations: -1 }); // 创建动画，第一次创建时显式指定初值，旋转角从[0,0,0]变成[0,0,360]，无限循环
      if (result) {
        this.isRunning = true;
      } else {
        console.warn('create rotation animation failed');
      }
    }
  }

  cancelAnimation(cnt: number) {
    if (this.rootNode && this.isRunning) {
      let result: boolean = this.rootNode.cancelAnimations([AnimationPropertyType.ROTATION]);
      if (result) {
        this.isRunning = false;
      } else {
        console.warn('cancel rotation animation failed');
        if (cnt < 2) { // cnt为尝试取消的次数
          // 如果取消失败，500ms后再次尝试取消
          setTimeout(() => {
            this.cancelAnimation(cnt + 1);
          }, 500);
        }
      }
    }
  }

  continueAnimation() {
    if (this.rootNode && !this.isRunning) {
      let currentProperty: number[] =
        this.rootNode.getNodePropertyValue(AnimationPropertyType.ROTATION); // 获取当前节点上的旋转属性终值
      if (currentProperty.length == 3) { // 获取属性正常，旋转属性对应的数组长度为3，分别是x、y、z方向的旋转角
        let endValue: number[];
        let startValue: number[] | undefined = undefined;
        if (currentProperty[2] >= 360) {
          startValue = [currentProperty[0], currentProperty[1],
            currentProperty[2] - 360]; // 当旋转属性过大时使z方向少转360度，避免z方向角度由于多次启停动画一直增加
          endValue = [currentProperty[0], currentProperty[1], currentProperty[2]];
        } else {
          endValue = [currentProperty[0], currentProperty[1], currentProperty[2] + 360]; // 此时旋转属性小于360度，可以从上次旋转角再多旋转一圈
        }
        let result: boolean = this.rootNode.createAnimation(AnimationPropertyType.ROTATION, startValue, endValue,
          { duration: 3000, curve: Curve.Linear, iterations: -1 });
        console.info(`create rotation animation from ${startValue ? String(startValue[2]) :
          'undefined'} to ${endValue[2]}`);
        if (result) {
          this.isRunning = true;
        } else {
          console.warn('create rotation animation failed when continue');
        }
      }
    }
  }
  
  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.rootNode) {
      return this.rootNode;
    }
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width(100)
      .height(100)
      .backgroundColor(Color.Blue); // 设置节点属性
    this.startInitAnimation();
    this.rootNode.commonEvent.setOnClick(() => {
      if (this.isRunning) {
        this.cancelAnimation(1);
      } else {
        this.continueAnimation();
      }
    });
    return this.rootNode;
  }
}

@Entry
@Component
struct CreateAnimationExample {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
    }.width('100%').padding({ top: 50 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/OVOl_4HWS9us0geJeKgshw/zh-cn_image_0000002712405782.gif)

## 滚动事件示例

```ts
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width(100)
    return this.rootNode;
  }

  addCommonEvent(frameNode: FrameNode) {
    let gridEvent: UIGridEvent | undefined = typeNode.getEvent(frameNode, 'Grid');
    gridEvent?.setOnWillScroll((scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
      console.info(`onWillScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}`)
    })
    gridEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
      console.info(`onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}`)
    })
    gridEvent?.setOnReachStart(() => {
      console.info(`onReachStart`)
    })
    gridEvent?.setOnReachEnd(() => {
      console.info(`onReachEnd`)
    })
    gridEvent?.setOnScrollStart(() => {
      console.info(`onScrollStart`)
    })
    gridEvent?.setOnScrollStop(() => {
      console.info(`onScrollStop`)
    })
    gridEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info(`onScrollFrameBegin offset = ${offset}, state = ${state}`)
      return undefined;
    })
    gridEvent?.setOnScrollIndex((first: number, last: number) => {
      console.info(`onScrollIndex start = ${first}, end = ${last}`)
    })
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  @State numbers: string[] = []

  aboutToAppear() {
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        this.numbers.push(j.toString());
      }
    }
  }

  build() {
    Column() {
      Button('add CommonEvent to Grid')
        .onClick(() => {
          this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
        })
      Grid() {
        ForEach(this.numbers, (day: string, index: number) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (day: string, index: number) => index.toString() + day)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .enableScrollInteraction(true)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)

      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```

## 检验FrameNode是否有效示例

该示例演示了FrameNode释放节点前后分别使用[isDisposed](js-apis-arkui-framenode.md#isdisposed20)接口验证节点的状态，释放节点前节点调用isDisposed接口返回false，释放节点后节点调用isDisposed接口返回true。

```ts
import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';

@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(25)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height(30)
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: BuilderNode<[]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(new WrappedBuilder(buildComponent));

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 300, height: 300 };
      rootRenderNode.backgroundColor = 0xffd5d5d5;
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  disposeFrameNode() {
    if (this.rootNode !== null && this.builderNode !== null) {
      this.rootNode.removeChild(this.builderNode.getFrameNode());
      this.builderNode.dispose();

      this.rootNode.dispose();
    }
  }

  isDisposed(): string {
    if (this.rootNode !== null) {
      if (this.rootNode.isDisposed()) {
        return 'frameNode isDisposed is true';
      } else {
        return 'frameNode isDisposed is false';
      }
    }
    return 'frameNode is null';
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  @State text: string = ''
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('FrameNode dispose')
        .onClick(() => {
          this.myNodeController.disposeFrameNode();
          this.text = '';
        })
        .width(200)
        .height(50)
      Button('FrameNode isDisposed')
        .onClick(() => {
          this.text = this.myNodeController.isDisposed();
        })
        .width(200)
        .height(50)
      Text(this.text)
        .fontSize(25)
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/8H8HB8CyQ2uvNzXqUOSaBg/zh-cn_image_0000002742124731.gif)

## 检验NodeAdapter是否有效示例

该示例演示了[NodeAdapter](js-apis-arkui-framenode.md#nodeadapter12)释放节点前后分别使用[isDisposed](js-apis-arkui-framenode.md#isdisposed20)接口验证节点的状态，释放节点前节点调用isDisposed接口返回false，释放节点后节点调用isDisposed接口返回true。

```ts
import { FrameNode, NodeController, NodeAdapter, typeNode } from '@kit.ArkUI';

// 自定义NodeAdapter管理数据
class MyNodeAdapter extends NodeAdapter {
  uiContext: UIContext
  cachePool: Array<FrameNode> = new Array();
  changed: boolean = false
  reloadTimes: number = 0;
  data: Array<string> = new Array();
  hostNode?: FrameNode

  constructor(uiContext: UIContext, count: number) {
    super();
    this.uiContext = uiContext;
    this.totalNodeCount = count;
    this.loadData();
  }

  loadData(): void {
    for (let i = 0; i < this.totalNodeCount; i++) {
      this.data[i] = 'Adapter ListItem ' + i + ' r:' + this.reloadTimes;
    }
  }

  onCreateChild(index: number): FrameNode {
    console.info(`UINodeAdapter onCreateChild:${index}`);
    if (this.cachePool.length > 0) {
      let cacheNode = this.cachePool.pop();
      if (cacheNode !== undefined) {
        console.info(`UINodeAdapter onCreateChild reused id:${cacheNode.getUniqueId()}`);
        let text = cacheNode?.getFirstChild();
        let textNode = text as typeNode.Text;
        textNode?.initialize(this.data[index]).fontSize(20);
        return cacheNode;
      }
    }
    console.info('UINodeAdapter onCreateChild createNew');
    let itemNode = typeNode.createNode(this.uiContext, 'ListItem');
    let textNode = typeNode.createNode(this.uiContext, 'Text');
    textNode.initialize(this.data[index]).fontSize(20);
    itemNode.appendChild(textNode);
    return itemNode;
  }
}

// 继承NodeController实现自定义NodeAdapter控制器
class MyNodeAdapterController extends NodeController {
  rootNode: FrameNode | null = null;
  nodeAdapter: MyNodeAdapter | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    let listNode = typeNode.createNode(uiContext, 'List');
    listNode.initialize({ space: 3 }).borderColor(Color.Black);
    this.rootNode.appendChild(listNode);
    this.nodeAdapter = new MyNodeAdapter(uiContext, 20);
    NodeAdapter.attachNodeAdapter(this.nodeAdapter, listNode);
    return this.rootNode;
  }

  dispose() {
    if (this.nodeAdapter !== null) {
      this.nodeAdapter.dispose();
    }
  }

  isDisposed(): string {
    if (this.nodeAdapter !== null) {
      if (this.nodeAdapter.isDisposed()) {
        return 'nodeAdapter isDisposed is true';
      } else {
        return 'nodeAdapter isDisposed is false';
      }
    }
    return 'nodeAdapter is null';
  }
}

@Entry
@Component
struct ListNodeTest {
  @State text: string = ''
  adapterController: MyNodeAdapterController = new MyNodeAdapterController();

  build() {
    Column() {
      Text('ListNode Adapter');
      NodeContainer(this.adapterController)
        .width(300).height(300)
        .borderWidth(1).borderColor(Color.Black);
      Button('NodeAdapter dispose')
        .onClick(() => {
          this.adapterController.dispose();
          this.text = '';
        })
        .width(200)
        .height(50)
        .margin({ top: 10, bottom: 10 })
      Button('NodeAdapter isDisposed')
        .onClick(() => {
          this.text = this.adapterController.isDisposed();
        })
        .width(200)
        .height(50)
      Text(this.text)
        .fontSize(25)
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/YUYw6LiOSxy9sWoRuLyFCA/zh-cn_image_0000002712245824.gif)

## 获取根节点示例

该示例演示了如何通过FrameNode的[getParent](js-apis-arkui-framenode.md#getparent12)接口获取当前页面根节点。

```ts
@Component
struct ChildView {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 通过id查询获得Text节点的FrameNode对象。不建议设置多个相同的id的节点
          let node = this.getUIContext().getFrameNodeById('HelloWorld');
          console.info(`Find HelloWorld Tag:${node!.getNodeType()} id:${node!.getUniqueId()}`);
          // 通过while循环遍历查询页面的根节点。如果当前节点为自定义组件，则会继续遍历其父节点
          while (node && node.getParent() && node.getParent()!.getUniqueId() > 0) {
            node = node.getParent();
            console.info(`Find FrameNode Tag:${node!.getNodeType()} id:${node!.getUniqueId()}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      ChildView({ message: this.message })
        .height('100%')
        .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 接纳为附属节点示例

从API version 22开始，该示例演示了如何通过FrameNode的[adoptChild](js-apis-arkui-framenode.md#adoptchild22)和[removeAdoptedChild](js-apis-arkui-framenode.md#removeadoptedchild22)接口进行接纳为附属节点的相关操作。

```ts
import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';

const TEST_TAG: string = 'FrameNode '

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  public frameNode: FrameNode | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.frameNode = new FrameNode(uiContext);
    this.addCommonEvent(this.frameNode);
    return this.rootNode;
  }

  addCommonEvent(frameNode: FrameNode) {
    frameNode.commonEvent.setOnClick((event: ClickEvent) => {
      console.info(`${TEST_TAG} Click FrameNode: ${JSON.stringify(event)}`);
    })
  }

  adoptChild() {
    try {
      this.rootNode?.adoptChild(this.frameNode);
      console.info(`${TEST_TAG} adoptChild success`);
    } catch (e) {
      console.error(`${TEST_TAG} adoptChild fail. Code: ${(e as BusinessError).code}, message: ${(e as BusinessError).message}`);
    }
  }

  removeAdoptedChild() {
    try {
      this.rootNode?.removeAdoptedChild(this.frameNode);
      console.info(`${TEST_TAG} removeAdoptedChild success`);
    } catch (e) {
      console.error(`${TEST_TAG} removeAdoptedChild fail. Code: ${(e as BusinessError).code}, message: ${(e as BusinessError).message}`);
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 8 }) {
      Column() {
        Text(`This is a NodeContainer.`)
          .textAlign(TextAlign.Center)
          .borderRadius(10)
          .backgroundColor(0xFFFFFF)
          .width(`100%`)
          .fontSize(16)
        NodeContainer(this.myNodeController)
          .borderWidth(1)
          .width(300)
          .height(100)
      }

      Button(`adoptChild`)
        .width(300)
        .onClick(() => {
          this.myNodeController.adoptChild();
        })
      Button(`removeAdoptedChild`)
        .width(300)
        .onClick(() => {
          this.myNodeController.removeAdoptedChild();
        })
    }
  }
}
```

## 局部与窗口坐标转换示例

该示例演示了如何通过FrameNode的[convertPositionToWindow](js-apis-arkui-framenode.md#convertpositiontowindow23)和[convertPositionFromWindow](js-apis-arkui-framenode.md#convertpositionfromwindow23)接口进行局部与窗口坐标转换。

从API version 23开始，新增convertPositionToWindow和convertPositionFromWindow接口。

```ts
import { Position } from '@kit.ArkUI';

@Entry
@Component
struct ConvertPositionWithWindow {
  private uiContext: UIContext = this.getUIContext();
  @State message: string = 'Hello World';

  build() {
    Column() {
      Text(this.message)
        .id('testNodeA')
        .fontSize($r('app.float.page_text_font_size')) // 请开发者替换为实际的资源文件
        .fontWeight(FontWeight.Bold)
      Button('运行convertPositionToWindow和convertPositionFromWindow测试')
        .onClick(() => {
          this.runBasicTest();
        })
        .margin(20)
    }
    .width('100%')
    .height('100%')
  }

  private runBasicTest() {
    // 等待UI渲染完成
    if (!this.uiContext) {
      return;
    }
    const nodeA = this.uiContext.getAttachedFrameNodeById('testNodeA');

    if (!nodeA) {
      console.info('无法获取测试节点');
      return;
    }

    const testPoint: Position = { x: 10, y: 10 };
    try {
      const result: Position = nodeA.convertPositionToWindow(testPoint);
      console.info(`相对于节点的(10, 10)坐标转换到相对于窗口的坐标为(${result.x}, ${result.y})`);
    } catch (e) {
      const exception = e as BusinessError<void>;
      console.error(`convertPositionToWindow throw error! code: ${exception.code}, message: ${exception.message}`);
    }

    try {
      const result: Position = nodeA.convertPositionFromWindow(testPoint);
      console.info(`相对于窗口的(10, 10)坐标转换到相对于该节点的坐标为(${result.x}, ${result.y})`);
    } catch (e) {
      const exception = e as BusinessError<void>;
      console.error(`convertPositionFromWindow throw error! code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```
