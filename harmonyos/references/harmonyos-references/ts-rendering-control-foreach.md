---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach
title: ForEach
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > ForEach
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:29519c9c7f4d37779da4a633a4cce8cd85e859d024d82e22a21df22abb59dac9
---

ForEach接口基于数组类型数据进行循环渲染，可基于数组数据快速生成结构相同、内容不同的子组件，适用于动态列表、批量数据展示等场景，需与容器组件配合使用。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[ForEach开发者指南](../harmonyos-guides/arkts-rendering-control-foreach.md)。

## 接口

ForEach(arr: Array<any>, itemGenerator: (item: any, index: number) => void, keyGenerator?: (item: any, index: number) => string)

该接口需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，[ListItem](ts-container-listitem.md)组件要求ForEach的父容器组件必须为[List](ts-container-list.md)组件或[ListItemGroup](ts-container-listitemgroup.md)组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array<any> | 是 | 数据源，为Array类型。  设置为undefined时ForEach接口不生效。  **说明：**  - 可以设置为空数组，此时不会创建子组件。  - 可以设置返回值为数组类型的函数，例如arr.slice(1, 3)，但设置的函数不应改变包括数组本身在内的任何状态变量，例如不应使用Array.splice()、Array.sort()或Array.reverse()这些会改变原数组的函数。 |
| itemGenerator | (item: any, index: number) => void | 是 | 组件生成函数。  - 为数组中的每个数据项创建对应的组件。  - item参数（可选）：arr数组中的数据项。  - index参数（可选）：arr数组中的数据项索引。  - 建议item的数据类型与arr的数据类型保持一致，否则，当itemGenerator中存在与数据类型强相关的操作时，会导致子组件无法正常渲染，甚至运行时崩溃。  **说明：**  - 组件的类型必须是ForEach的父容器所允许的。例如，ListItem组件要求ForEach的父容器组件必须为List组件或ListItemGroup组件。  - 组件生成函数不应改变任何组件状态。 |
| keyGenerator | (item: any, index: number) => string | 否 | 键值生成函数。  - 为数据源arr的每个数据项生成唯一且稳定的键值。开发者可以通过该函数自定义键值生成规则，例如当数据项包含唯一标识符时，可使用该标识符作为键值以提升渲染性能；当数据项可能被增删或重排序时，自定义稳定键值可保证组件正确复用。若键值不唯一或不持久，可能导致组件复用错误或渲染异常。  - item参数（可选）：arr数组中的数据项。建议item的数据类型与arr的数据类型保持一致，否则，当keyGenerator中存在与数据类型强相关的操作时，会导致子组件无法正常渲染，甚至运行时崩溃。  - index参数（可选）：arr数组中的数据项索引。  **说明：**  - 如果函数缺省，框架默认的键值生成函数为(item: any, index: number) => { return index + '\_\_' + JSON.stringify(item); }  - 键值生成函数不应改变任何组件状态。 |

**说明** 

* ForEach的itemGenerator函数可以包含[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)条件渲染逻辑。另外，也可以在if/else条件渲染语句中使用ForEach组件。
* 在初始化渲染时，ForEach会加载数据源的所有数据，并为每个数据项创建对应的组件，然后将其挂载到渲染树上。当数据源中的数据项数量较多（例如达到数百项以上）或出现列表首次加载卡顿等性能问题时，建议使用[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)组件。最佳实践请参考[使用懒加载优化性能](../best-practices/bpta-lazyforeach-optimization.md)。

由于数据源的数据项类型为any，缺少类型一致性校验，建议在使用ForEach时保持类型声明一致（详见如下代码片段），不规范写法可能会导致子组件无法正常渲染。

```ts
// 不规范写法
arr: Array<Type1 | Type2> = [];

ForEach(this.arr, (item: Type1) => {...}, (item: Type2) => item.toString()); // item类型和数据项类型不一致

// 正确写法
arr: Array<Type1 | Type2> = [];

ForEach(this.arr, (item: Type1 | Type2) => {...}, (item: Type1 | Type2) => item.toString()); // item类型和数据项类型保持一致
```

## 属性

支持[拖拽排序](ts-universal-attributes-drag-sorting.md)属性。
