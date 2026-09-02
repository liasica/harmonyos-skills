---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management
title: 应用级变量的状态管理
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 应用级变量的状态管理
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:256e610b2eb0afd67fd023f2d99741a8f2f78e14f922014c4ac47a7b386eb39a
---

状态管理模块提供了应用的数据存储能力、持久化数据管理能力、UIAbility数据存储能力和环境状态查询能力。[AppStorage](ts-state-management.md#appstorage)是与应用进程绑定的全局UI状态存储中心，[LocalStorage](ts-state-management.md#localstorage9)提供了页面级的UI状态存储能力，[PersistentStorage](ts-state-management.md#persistentstorage)提供了状态变量持久化的能力，[Environment](ts-state-management.md#environment)提供了读取系统环境变量并将其值写入AppStorage的能力。

开发指南参考：[AppStorage：应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md)、[LocalStorage：页面级UI状态存储](../harmonyos-guides/arkts-localstorage.md)、[PersistentStorage：持久化存储UI状态](../harmonyos-guides/arkts-persiststorage.md)和[Environment：设备环境查询](../harmonyos-guides/arkts-environment.md)。

**说明** 

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

本文中T和S的含义如下：

| 类型 | 说明 |
| --- | --- |
| T | Class、number、boolean、string及这些类型的数组形式。 |
| S | number、boolean、string。 |

## AppStorage

AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。具体UI使用说明，详见[AppStorage：应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md)。

**说明** 

从API version 12开始，AppStorage支持[Map](../harmonyos-guides/arkts-appstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-appstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-appstorage.md#appstorage支持联合类型)。

### ref12+

static ref<T>(propName: string): AbstractProperty<T> | undefined

如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回AppStorage中propName对应属性的引用。否则，返回undefined。

与[link](ts-state-management.md#link10)的功能基本一致，区别在于不需要手动释放返回的[AbstractProperty<T>](ts-state-management.md#abstractpropertyt12)类型的变量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbstractProperty<T>](ts-state-management.md#abstractpropertyt12) | undefined | 返回AppStorage中propName对应属性的引用，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let refToPropA1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
let refToPropA2: AbstractProperty<number> | undefined = AppStorage.ref('PropA'); // refToPropA2.get() == 47
refToPropA1?.set(48); // 同步修改AppStorage：refToPropA1.get() == refToPropA2.get() == 48
```

### setAndRef12+

static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>

与[ref](ts-state-management.md#ref12)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回AppStorage中propName对应属性的引用。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，并返回其引用。

与[setAndLink](ts-state-management.md#setandlink10)的功能基本一致，区别在于不需要手动释放返回的[AbstractProperty<T>](ts-state-management.md#abstractpropertyt12)类型的变量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbstractProperty<T>](ts-state-management.md#abstractpropertyt12) | AbstractProperty<T>的实例，为AppStorage中propName对应属性的引用。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> = AppStorage.setAndRef('PropB', 49); // 用默认值49创建PropB
let ref2: AbstractProperty<number> = AppStorage.setAndRef('PropA', 50); // PropA已存在，值为47
```

### link10+

static link<T>(propName: string): SubscribedAbstractProperty<T>

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立双向数据绑定。如果给定的propName在AppStorage中存在，返回AppStorage中propName对应属性的双向绑定数据。与[prop](ts-state-management.md#prop10)的单向数据绑定不同，link的修改会同步回AppStorage，AppStorage会将变化同步到所有绑定该propName的数据和自定义组件中。

如果AppStorage中不存在propName，则返回undefined。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | 返回双向绑定的数据，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let linkToPropA1: SubscribedAbstractProperty<number> = AppStorage.link('PropA');
let linkToPropA2: SubscribedAbstractProperty<number> = AppStorage.link('PropA'); // linkToPropA2.get() == 47
linkToPropA1.set(48); // 双向同步：linkToPropA1.get() == linkToPropA2.get() == 48
```

### setAndLink10+

static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[link](ts-state-management.md#link10)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值。从API version 12开始，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<T>的实例，为AppStorage中propName对应属性的双向绑定的数据。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let link1: SubscribedAbstractProperty<number> = AppStorage.setAndLink('PropB', 49); // 用默认值49创建PropB
let link2: SubscribedAbstractProperty<number> = AppStorage.setAndLink('PropA', 50); // PropA已存在，值为47
```

### prop10+

static prop<T>(propName: string): SubscribedAbstractProperty<T>

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立单向数据绑定。如果给定的propName在AppStorage中存在，则返回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回undefined。单向绑定数据的修改不会同步回AppStorage中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | 返回单向绑定的数据，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
let prop2: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.set(1); // 单向同步：prop1.get()的值为1，prop2.get()的值为47
```

### setAndProp10+

static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[prop](ts-state-management.md#prop10)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值。从API version 12开始，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<T>的实例，为AppStorage中propName对应属性的单向绑定的数据。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let prop: SubscribedAbstractProperty<number> = AppStorage.setAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

### has10+

static has(propName: string): boolean

判断propName对应的属性是否在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果propName对应的属性在AppStorage中存在，则返回true。不存在则返回false。 |

**示例：**

```ts
AppStorage.has('simpleProp');
```

### get10+

static get<T>(propName: string): T | undefined

获取propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的属性值。如果不存在则返回undefined。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | AppStorage中propName对应的属性值，如果不存在则返回undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let value: number = AppStorage.get('PropA') as number; // 47
```

### set10+

static set<T>(propName: string, newValue: T): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中设置propName对应属性的值。如果newValue与propName对应属性的值相同，则不做赋值操作，状态变量不会通知UI刷新propName对应属性的值。与[setOrCreate](ts-state-management.md#setorcreate10)不同，set仅在propName已存在时生效，propName不存在时返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | propName对应属性的新值，从API version 12开始可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中不存在propName对应的属性，或设值失败，则返回false。设置成功则返回true。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 48);
let res: boolean = AppStorage.set('PropA', 47); // true
let res1: boolean = AppStorage.set('PropB', 47); // false
```

### setOrCreate10+

static setOrCreate<T>(propName: string, newValue: T): void

如果propName已经在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。

如果propName不存在，则创建propName属性，值为newValue。setOrCreate仅可创建单个AppStorage的键值对，如需创建多个AppStorage键值对，可多次调用此方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | propName对应属性的新值，从API version 12开始可以为null或undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('simpleProp', 121);
```

### delete10+

static delete(propName: string): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中删除propName对应的属性。

仅当AppStorage中该属性没有任何订阅者时可删除成功并返回true；如果有订阅者，则返回false。

属性的订阅者为：

1. [@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)、[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)装饰的变量。
2. 通过[link](ts-state-management.md#link10)、[prop](ts-state-management.md#prop10)、[setAndLink](ts-state-management.md#setandlink10)、[setAndProp](ts-state-management.md#setandprop10)接口返回的[SubscribedAbstractProperty](ts-state-management.md#subscribedabstractpropertyt9)的实例。

如需删除这些订阅者，可通过以下方式：

1. 删除@StorageLink、@StorageProp所在的自定义组件。删除自定义组件请参考[自定义组件的删除](../harmonyos-guides/arkts-page-custom-components-lifecycle.md#自定义组件的删除)。
2. 对link、prop、setAndLink、setAndProp接口返回的SubscribedAbstractProperty的实例调用[aboutToBeDeleted](ts-state-management.md#abouttobedeleted10)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中有对应的属性，且该属性已经没有订阅者，则删除成功，返回true。如果属性不存在，或者该属性还存在订阅者，则返回false。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
AppStorage.link<number>('PropA');
let res: boolean = AppStorage.delete('PropA'); // false，PropA 还存在订阅者

AppStorage.setOrCreate('PropB', 48);
let res1: boolean = AppStorage.delete('PropB'); // true，PropB 已从AppStorage成功删除
```

### keys10+

static keys(): IterableIterator<string>

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有的属性名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | AppStorage中所有的属性名。 |

**示例：**

```ts
AppStorage.setOrCreate('PropB', 48);
let keys: IterableIterator<string> = AppStorage.keys();
```

### clear10+

static clear(): boolean

删除[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有属性。仅当AppStorage没有任何订阅者时可删除成功并返回true；如果有订阅者，clear不会生效并返回false。

订阅者的含义参考[delete](ts-state-management.md#delete10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中的属性已经没有订阅者则删除成功，返回true；如果当前仍有订阅者，返回false。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let res: boolean = AppStorage.clear(); // true，已经没有订阅者
```

### size10+

static size(): number

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中的属性数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | AppStorage中属性的数量。 |

**示例：**

```ts
AppStorage.setOrCreate('PropB', 48);
let res: number = AppStorage.size(); // 1
```

### Link(deprecated)

static Link(propName: string): any

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立双向数据绑定。如果给定的propName在AppStorage中存在，返回与AppStorage中propName对应属性的双向绑定数据。

双向绑定数据的修改会同步回AppStorage中，AppStorage会将变化同步到所有绑定该propName的数据和自定义组件中。

如果AppStorage中不存在propName，则返回undefined。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[link](ts-state-management.md#link10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 返回双向绑定的数据，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
let linkToPropA1: SubscribedAbstractProperty<number> = AppStorage.Link('PropA');
let linkToPropA2: SubscribedAbstractProperty<number> = AppStorage.Link('PropA'); // linkToPropA2.get() == 47
linkToPropA1.set(48); // 双向同步：linkToPropA1.get() == linkToPropA2.get() == 48
```

### SetAndLink(deprecated)

static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[Link](ts-state-management.md#linkdeprecated)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，并返回其双向绑定数据。defaultValue必须为T类型，且不能为null或undefined。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[setAndLink](ts-state-management.md#setandlink10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值，defaultValue不能为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<T>的实例，为AppStorage中propName对应属性的双向绑定的数据。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
let link1: SubscribedAbstractProperty<number> = AppStorage.SetAndLink('PropB', 49); // 用默认值49创建PropB
let link2: SubscribedAbstractProperty<number> = AppStorage.SetAndLink('PropA', 50); // PropA已存在，值为47
```

### Prop(deprecated)

static Prop(propName: string): any

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立单向数据绑定。如果给定的propName在AppStorage中存在，则返回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回undefined。单向绑定数据的修改不会同步回AppStorage中。

**说明** 

Prop仅支持S类型（number、boolean、string）。

从API version 7开始支持，从API version 10开始废弃，建议使用[prop](ts-state-management.md#prop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 返回单向绑定的数据，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA');
let prop2: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA');
prop1.set(1); // 单向同步：prop1.get()的值为1，prop2.get()的值为47
```

### SetAndProp(deprecated)

static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>

与[Prop](ts-state-management.md#propdeprecated)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。defaultValue必须为S类型，且不能为null或undefined。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[setAndProp](ts-state-management.md#setandprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | S | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值，defaultValue不能为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<S>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<S>的实例，为AppStorage中propName对应属性的单向绑定的数据。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
let prop: SubscribedAbstractProperty<number> = AppStorage.SetAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

### Has(deprecated)

static Has(propName: string): boolean

判断propName对应的属性是否在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[has](ts-state-management.md#has10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果propName对应的属性在AppStorage中存在，则返回true。不存在则返回false。 |

**示例：**

```ts
AppStorage.Has('simpleProp');
```

### Get(deprecated)

static Get<T>(propName: string): T | undefined

获取propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的属性值。如果不存在则返回undefined。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[get](ts-state-management.md#get10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | AppStorage中propName对应的属性值，如果不存在则返回undefined。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
let value: number = AppStorage.Get('PropA') as number; // 47
```

### Set(deprecated)

static Set<T>(propName: string, newValue: T): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中设置propName对应属性的值。如果newValue与propName对应属性的值相同，则不做赋值操作，状态变量不会通知UI刷新propName对应属性的值。与[SetOrCreate](ts-state-management.md#setorcreatedeprecated)不同，Set仅在propName已存在时生效，propName不存在时返回false。从API version 12开始，newValue可以为null或undefined。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[set](ts-state-management.md#set10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | propName对应属性的新值，从API version 12开始可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中不存在propName对应的属性，返回false。设置成功则返回true。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 48);
let res: boolean = AppStorage.Set('PropA', 47); // true
let res1: boolean = AppStorage.Set('PropB', 47); // false
```

### SetOrCreate(deprecated)

static SetOrCreate<T>(propName: string, newValue: T): void

如果propName已经在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。如果不存在，则创建propName属性，值为newValue。从API version 12开始，newValue可以为null或undefined。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[setOrCreate](ts-state-management.md#setorcreate10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | propName对应属性的新值，从API version 12开始可以为null或undefined。 |

**示例：**

```ts
AppStorage.SetOrCreate('simpleProp', 121);
```

### Delete(deprecated)

static Delete(propName: string): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中删除propName对应的属性。

仅当AppStorage中该属性没有任何订阅者时可删除成功并返回true；如果有订阅者，则返回false。

属性的订阅者为[Link](ts-state-management.md#linkdeprecated)、[Prop](ts-state-management.md#propdeprecated)等接口返回的实例，以及[@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)和[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)装饰的变量。如果@StorageLink('propName')、@StorageProp('propName')装饰的变量或SubscribedAbstractProperty实例依旧对propName有同步关系，则该属性不能从AppStorage中删除。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[delete](ts-state-management.md#delete10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中有对应的属性，且该属性已经没有订阅者，则删除成功，返回true。如果属性不存在，或者该属性还存在订阅者，则返回false。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
AppStorage.Link('PropA');
let res: boolean = AppStorage.Delete('PropA'); // false，PropA 还存在订阅者

AppStorage.SetOrCreate('PropB', 48);
let res1: boolean = AppStorage.Delete('PropB'); // true，PropB 已从AppStorage成功删除
```

### Keys(deprecated)

static Keys(): IterableIterator<string>

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有的属性名。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[keys](ts-state-management.md#keys10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | AppStorage中所有的属性名。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropB', 48);
let keys: IterableIterator<string> = AppStorage.Keys();
```

### staticClear(deprecated)

static staticClear(): boolean

删除[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有属性。仅当AppStorage没有任何订阅者时可删除成功并返回true；如果有订阅者，staticClear不会生效并返回false。订阅者的含义参考[delete](ts-state-management.md#delete10)。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[clear](ts-state-management.md#clear10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除AppStorage中所有的属性。仅当没有任何订阅者时删除成功，返回true；如果仍有订阅者，返回false。 |

**示例：**

```ts
let clearResult = AppStorage.staticClear();
```

### Clear(deprecated)

static Clear(): boolean

删除[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有属性。前提是AppStorage已经没有任何订阅者。如果有订阅者，Clear将不会生效并返回false。如果没有订阅者且删除成功则返回true。

订阅者的含义参考[delete](ts-state-management.md#delete10)。

**说明** 

从API version 9开始支持，从API version 10开始废弃，建议使用[clear](ts-state-management.md#clear10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中的属性已经没有订阅者则删除成功，返回true。否则返回false。 |

**示例：**

```typescript
AppStorage.SetOrCreate('PropA', 47);
let res: boolean = AppStorage.Clear(); // true，已经没有订阅者
```

### IsMutable(deprecated)

static IsMutable(propName: string): boolean

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中propName对应的属性是否是可变的。

**说明** 

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回AppStorage中propName对应的属性是否是可变的。当前该返回值恒为true。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropA', 47);
let res: boolean = AppStorage.IsMutable('PropA');
```

### Size(deprecated)

static Size(): number

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中的属性数量。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[size](ts-state-management.md#size10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | AppStorage中属性的数量。 |

**示例：**

```ts
AppStorage.SetOrCreate('PropB', 48);
let res: number = AppStorage.Size(); // 1
```

## LocalStorage9+

LocalStorage是页面级的UI状态存储，通过[@Entry](ts-universal-entry.md#entry)装饰器接收的参数可以在页面内共享同一个LocalStorage实例。具体UI使用说明，详见[LocalStorage：页面级UI状态存储](../harmonyos-guides/arkts-localstorage.md)。

**说明** 

从API version 12开始，LocalStorage支持[Map](../harmonyos-guides/arkts-localstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-localstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-localstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-localstorage.md#localstorage支持联合类型)。

### constructor9+

constructor(initializingProperties?: Object)

创建一个新的[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。使用Object.keys(initializingProperties)返回的属性名及其值，初始化LocalStorage实例。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initializingProperties | Object | 否 | 用于初始化LocalStorage，当需要在创建时预置属性数据时传入此参数。其键作为LocalStorage中的属性名，值为对应属性的初始值。initializingProperties不能为undefined。不传入时默认值为空对象，LocalStorage中不包含任何预置属性。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
```

### getShared(deprecated)

static getShared(): LocalStorage

获取当前Stage共享的[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。

**说明** 

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getSharedLocalStorage](arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)替代。

从API version 12开始，可使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getSharedLocalStorage](arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)明确UI执行上下文中的LocalStorage实例。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalStorage](ts-state-management.md#localstorage9) | 返回当前Stage共享的LocalStorage实例。 |

### has9+

has(propName: string): boolean

判断propName对应的属性是否在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果propName对应的属性在LocalStorage中存在，则返回true。不存在则返回false。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
storage.has('PropA'); // true
```

### get9+

get<T>(propName: string): T | undefined

获取propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中对应的属性值。如果不存在则返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | LocalStorage中propName对应的属性值，如果不存在则返回undefined。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let value: number = storage.get('PropA') as number; // 47
```

### set9+

set<T>(propName: string, newValue: T): boolean

在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中设置propName对应属性的值。如果newValue与propName对应属性的值相同，则不做赋值操作，状态变量不会通知UI刷新propName对应属性的值。与[setOrCreate](ts-state-management.md#setorcreate9)不同，set仅在propName已存在时生效，propName不存在时返回false。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| newValue | T | 是 | propName对应属性的新值，从API version 12开始可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中不存在propName对应的属性，返回false。设置成功返回true。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let res: boolean = storage.set('PropA', 47); // true
let res1: boolean = storage.set('PropB', 47); // false
```

### setOrCreate9+

setOrCreate<T>(propName: string, newValue: T): boolean

如果propName已经在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。

如果propName不存在，则创建propName属性，值为newValue。setOrCreate仅可创建单个LocalStorage的键值对，如需创建多个LocalStorage键值对，可多次调用此方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| newValue | T | 是 | propName对应属性的新值，从API version 12开始可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中存在propName，则更新其值为newValue，返回true。  如果LocalStorage中不存在propName，则创建propName，并初始化其值为newValue，返回true。  API version 12之前，当newValue为null或undefined时返回false。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let res: boolean = storage.setOrCreate('PropA', 121); // true
let res1: boolean = storage.setOrCreate('PropB', 111); // true
let res2: boolean = storage.setOrCreate('PropB', null); // true（API version 12及之后返回true，API version 11及之前返回false）
```

### ref12+

ref<T>(propName: string): AbstractProperty<T> | undefined

如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回LocalStorage中propName对应属性的引用。否则，返回undefined。

与[link](ts-state-management.md#link9)的功能基本一致，区别在于不需要手动释放返回的[AbstractProperty<T>](ts-state-management.md#abstractpropertyt12)类型的变量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbstractProperty<T>](ts-state-management.md#abstractpropertyt12) | undefined | 返回LocalStorage中propName对应属性的引用，如果LocalStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let refToPropA1: AbstractProperty<number> | undefined = storage.ref('PropA');
let refToPropA2: AbstractProperty<number> | undefined = storage.ref('PropA'); // refToPropA2.get() == 47
refToPropA1?.set(48); // refToPropA1.get() == refToPropA2.get() == 48
```

### setAndRef12+

setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>

与[ref](ts-state-management.md#ref12-1)接口类似，如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回LocalStorage中propName对应属性的引用。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，并返回其引用。

与[setAndLink](ts-state-management.md#setandlink9)的功能基本一致，区别在于不需要手动释放返回的[AbstractProperty<T>](ts-state-management.md#abstractpropertyt12)类型的变量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在LocalStorage中不存在时，使用defaultValue在LocalStorage中初始化propName对应属性的值，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbstractProperty<T>](ts-state-management.md#abstractpropertyt12) | AbstractProperty<T>的实例，为LocalStorage中propName对应属性的引用。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let ref1: AbstractProperty<number> = storage.setAndRef('PropB', 49); // 用默认值49创建PropB
let ref2: AbstractProperty<number> = storage.setAndRef('PropA', 50); // PropA已存在，值为47
```

### link9+

link<T>(propName: string): SubscribedAbstractProperty<T>

如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例中存在，则返回与LocalStorage中propName对应属性的双向绑定数据。与[prop](ts-state-management.md#prop9)的单向数据绑定不同，link建立双向数据绑定，修改会同步回LocalStorage，LocalStorage会将变化同步到所有绑定该propName的数据和自定义组件中。

如果LocalStorage中不存在propName，则返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<T>的实例，与LocalStorage中propName对应属性的双向绑定的数据，如果LocalStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let linkToPropA1: SubscribedAbstractProperty<number> = storage.link('PropA');
let linkToPropA2: SubscribedAbstractProperty<number> = storage.link('PropA'); // linkToPropA2.get() == 47
linkToPropA1.set(48); // 双向同步：linkToPropA1.get() == linkToPropA2.get() == 48
```

### setAndLink9+

setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[link](ts-state-management.md#link9)接口类似，如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在LocalStorage中不存在时，使用defaultValue在LocalStorage中初始化propName对应属性的值。从API version 12开始，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<T>的实例，与LocalStorage中propName对应属性的双向绑定的数据。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let link1: SubscribedAbstractProperty<number> = storage.setAndLink('PropB', 49); // 用默认值49创建PropB
let link2: SubscribedAbstractProperty<number> = storage.setAndLink('PropA', 50); // PropA已存在，值为47
```

### prop9+

prop<S>(propName: string): SubscribedAbstractProperty<S>

如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回与LocalStorage中propName对应属性的单向绑定数据。如果LocalStorage中不存在propName，则返回undefined。单向绑定数据的修改不会同步回LocalStorage中。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<S>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<S>的实例，为LocalStorage中propName对应属性的单向绑定的数据。如果LocalStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let prop1: SubscribedAbstractProperty<number> = storage.prop('PropA');
let prop2: SubscribedAbstractProperty<number> = storage.prop('PropA');
prop1.set(1); // 单向同步：prop1.get()的值为1，prop2.get()的值为47
```

### setAndProp9+

setAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>

与[prop](ts-state-management.md#prop9)接口类似，如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| defaultValue | S | 是 | 当propName在LocalStorage中不存在时，使用defaultValue在LocalStorage中初始化propName对应属性的值。从API version 12开始，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<S>](ts-state-management.md#subscribedabstractpropertyt9) | SubscribedAbstractProperty<S>的实例，为LocalStorage中propName对应属性的单向绑定的数据。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let prop: SubscribedAbstractProperty<number> = storage.setAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

### delete9+

delete(propName: string): boolean

在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中删除propName对应的属性。仅当LocalStorage中该属性没有任何订阅者时可删除成功并返回true；如果有订阅者，则返回false。

属性的订阅者为：

1. [@LocalStorageLink](../harmonyos-guides/arkts-localstorage.md#localstoragelink)、[@LocalStorageProp](../harmonyos-guides/arkts-localstorage.md#localstorageprop)装饰的变量。
2. 通过[link](ts-state-management.md#link9)、[prop](ts-state-management.md#prop9)、[setAndLink](ts-state-management.md#setandlink9)、[setAndProp](ts-state-management.md#setandprop9)接口返回的[SubscribedAbstractProperty](ts-state-management.md#subscribedabstractpropertyt9)的实例。

如需删除这些订阅者，可通过以下方式：

1. 删除@LocalStorageLink、@LocalStorageProp所在的自定义组件。删除自定义组件请参考[自定义组件的删除](../harmonyos-guides/arkts-page-custom-components-lifecycle.md#自定义组件的删除)。
2. 对link、prop、setAndLink、setAndProp接口返回的SubscribedAbstractProperty的实例调用[aboutToBeDeleted](ts-state-management.md#abouttobedeleted10)接口。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中有对应的属性，且该属性已经没有订阅者，则删除成功，返回true。如果属性不存在，或者该属性还存在订阅者，则返回false。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
storage.link<number>('PropA');
let res: boolean = storage.delete('PropA'); // false，PropA 还存在订阅者
let res1: boolean = storage.delete('PropB'); // false，PropB 不存在于storage中
storage.setOrCreate('PropB', 48);
let res2: boolean = storage.delete('PropB'); // true，PropB 已从storage成功删除
```

### keys9+

keys(): IterableIterator<string>

返回[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所有的属性名。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | LocalStorage中所有的属性名。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let keys: IterableIterator<string> = storage.keys();
```

### size9+

size(): number

返回[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中的属性数量。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | LocalStorage中属性的数量。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let res: number = storage.size(); // 1
```

### clear9+

clear(): boolean

删除[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所有的属性。仅当LocalStorage中的属性没有任何订阅者时可删除成功并返回true；如果有订阅者，clear不会生效并返回false。

订阅者的含义参考[delete](ts-state-management.md#delete9)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中的属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。 |

**示例：**

```ts
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let res: boolean = storage.clear(); // true，已经没有订阅者
```

### GetShared(deprecated)

static GetShared(): LocalStorage

获取当前Stage共享的[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。

**说明** 

从API version 9开始支持，从API version 10开始废弃，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getSharedLocalStorage](arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalStorage](ts-state-management.md#localstorage9) | 返回当前Stage共享的LocalStorage实例。 |

**示例：**

```ts
let storage: LocalStorage = LocalStorage.GetShared();
```

## AbstractProperty<T>12+

AbstractProperty是AppStorage/LocalStorage中属性的引用，提供读取、修改所引用属性数据及查询属性名的能力。与SubscribedAbstractProperty不同，AbstractProperty实例无需手动释放。

**说明** 

从API version 12开始，AppStorage/LocalStorage支持Map、Set、Date类型，支持null、undefined以及联合类型。

### get12+

get(): T

读取[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所引用属性的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | AppStorage/LocalStorage中所引用属性的数据。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.get(); // ref1.get()=47
```

### set12+

set(newValue: T): void

更新[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所引用属性的数据，newValue必须是T类型，可以为null或undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | AppStorage/LocalStorage中所引用属性的新值，可以为null或undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.set(1); // ref1.get()=1
let mapValue: Map<string, number> = new Map([['1', 0]]);
let ref2 = AppStorage.setAndRef('MapA', mapValue);
ref2.set(mapValue);
let setValue: Set<string> = new Set(['1']);
let ref3 = AppStorage.setAndRef('SetB', setValue);
ref3.set(setValue);
let dateValue: Date = new Date('2024');
let ref4 = AppStorage.setAndRef('DateC', dateValue);
ref4.set(dateValue);
ref2.set(null);
ref3.set(undefined);
```

### info12+

info(): string

读取[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所引用属性的属性名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | AppStorage/LocalStorage中所引用属性的属性名。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.info(); // ref1.info()='PropA'
```

## SubscribedAbstractProperty<T>9+

SubscribedAbstractProperty是[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中属性的单/双向同步绑定对象，用于与AppStorage/LocalStorage中的属性建立数据同步关系。SubscribedAbstractProperty实例需要通过[aboutToBeDeleted](ts-state-management.md#abouttobedeleted10)接口手动释放，以取消同步关系并无效化实例。

**说明** 

从API version 12开始，AppStorage/LocalStorage支持Map、Set、Date类型，支持null、undefined以及联合类型。

### get9+

abstract get(): T

读取[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所同步属性的数据。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | AppStorage/LocalStorage同步属性的数据。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.get(); // prop1.get()=47
```

### set9+

abstract set(newValue: T): void

设置[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所同步属性的数据，newValue必须是T类型，从API version 12开始可以为null或undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | AppStorage/LocalStorage中所同步属性的新值，从API version 12开始可以为null或undefined。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.set(1); // prop1.get()=1
// 从API version 12开始支持Map、Set、Date类型，支持null、undefined以及联合类型。
let mapValue: Map<string, number> = new Map([['1', 0]]);
let prop2 = AppStorage.setAndProp('MapA', mapValue);
prop2.set(mapValue);
let setValue: Set<string> = new Set(['1']);
let prop3 = AppStorage.setAndProp('SetB', setValue);
prop3.set(setValue);
let dateValue: Date = new Date('2024');
let prop4 = AppStorage.setAndProp('DateC', dateValue);
prop4.set(dateValue);
prop2.set(null);
prop3.set(undefined);
```

### aboutToBeDeleted10+

abstract aboutToBeDeleted(): void

取消[SubscribedAbstractProperty](ts-state-management.md#subscribedabstractpropertyt9)实例对[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)的单向或双向同步关系，并无效化SubscribedAbstractProperty实例。即调用aboutToBeDeleted方法之后，不能再使用SubscribedAbstractProperty实例调用[set](ts-state-management.md#set9-1)或[get](ts-state-management.md#get9-1)方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let link = AppStorage.setAndLink('PropB', 49); // PropA -> 47, PropB -> 49
link.aboutToBeDeleted();
```

### info10+

info(): string

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所同步属性的属性名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | AppStorage/LocalStorage中所同步属性的属性名。 |

**示例：**

```ts
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.info(); // prop1.info() = 'PropA'
```

## PersistPropsOptions10+

用于指定持久化属性及其默认值的键值对对象，作为[persistProps](ts-state-management.md#persistprops10)参数传入。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 要持久化的属性名。 |
| defaultValue | number | string | boolean | Object | 否 | 否 | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。从API version 12开始，defaultValue可以为null或undefined。 |

## PersistentStorage

PersistentStorage提供了UI状态的持久化存储能力，将选定的AppStorage属性持久化到文件中，在应用重启时从文件中恢复这些属性值并写入到AppStorage。具体UI使用说明，详见[PersistentStorage：持久化存储UI状态](../harmonyos-guides/arkts-persiststorage.md)。

**说明** 

从API version 12开始，PersistentStorage支持null、undefined。

### persistProp10+

static persistProp<T>(key: string, defaultValue: T): void

将[AppStorage](../harmonyos-guides/arkts-appstorage.md)中key对应的属性持久化到文件中。该接口通常在访问AppStorage之前调用。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)文件中存在key对应的属性，在AppStorage中创建对应的key，并用在PersistentStorage中找到的key的属性初始化。
2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。
3. 如果AppStorage中也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值覆盖PersistentStorage文件中的值。由于AppStorage是内存中的数据，这种操作会使持久化文件中的数据被内存数据覆盖，导致持久化数据失去意义。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要持久化的属性名。 |
| defaultValue | T | 是 | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。从API version 12开始可以为null或undefined。 |

**示例：**

persistProp具体用法详见[从AppStorage中访问PersistentStorage初始化的属性](../harmonyos-guides/arkts-persiststorage.md#从appstorage中访问persistentstorage初始化的属性)。

### deleteProp10+

static deleteProp(key: string): void

是[persistProp](ts-state-management.md#persistprop10)的逆向操作。将key对应的属性从[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)中删除，后续[AppStorage](../harmonyos-guides/arkts-appstorage.md)的操作对PersistentStorage不会再有影响。如需再次持久化，可再次调用[persistProp](ts-state-management.md#persistprop10)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | PersistentStorage中的属性名。 |

**示例：**

```ts
PersistentStorage.deleteProp('highScore');
```

### persistProps10+

static persistProps(props: PersistPropsOptions[]): void

行为与[persistProp](ts-state-management.md#persistprop10)类似，不同在于可以一次性持久化多个数据。该接口通常在访问AppStorage之前调用，适合在应用启动时初始化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| props | [PersistPropsOptions](ts-state-management.md#persistpropsoptions10)[] | 是 | 持久化数组，每项包含属性名和默认值。 |

**示例：**

```ts
PersistentStorage.persistProps([{ key: 'highScore', defaultValue: '0' }, { key: 'weightScore', defaultValue: '1' }]);
```

### keys10+

static keys(): Array<string>

返回所有持久化属性的属性名的数组。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回所有持久化属性的属性名的数组。 |

**示例：**

```ts
let keys: Array<string> = PersistentStorage.keys();
```

### PersistProp(deprecated)

static PersistProp<T>(key: string, defaultValue: T): void

将[AppStorage](../harmonyos-guides/arkts-appstorage.md)中key对应的属性持久化到文件中。该接口应在访问AppStorage之前调用。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)文件中存在key对应的属性，在AppStorage中创建对应的key，并用在PersistentStorage中找到的key的属性初始化。
2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。
3. 如果AppStorage也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值覆盖PersistentStorage文件中的值。由于AppStorage是内存中的数据，这种操作会使持久化文件中的数据被内存数据覆盖，导致持久化数据失去意义。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[persistProp](ts-state-management.md#persistprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要持久化的属性名。 |
| defaultValue | T | 是 | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。默认值不允许为null或undefined。 |

**示例：**

```ts
PersistentStorage.PersistProp('highScore', '0');
```

### DeleteProp(deprecated)

static DeleteProp(key: string): void

是[PersistProp](ts-state-management.md#persistpropdeprecated)的逆向操作。将key对应的属性从[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)中删除，后续[AppStorage](../harmonyos-guides/arkts-appstorage.md)的操作对PersistentStorage不会再有影响。如需再次持久化，可再次调用[PersistProp](ts-state-management.md#persistpropdeprecated)接口。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[deleteProp](ts-state-management.md#deleteprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | PersistentStorage中的属性名。 |

**示例：**

```ts
PersistentStorage.DeleteProp('highScore');
```

### PersistProps(deprecated)

static PersistProps(properties: {key: string; defaultValue: any;}[]): void

行为与[PersistProp](ts-state-management.md#persistpropdeprecated)类似，不同在于可以一次性持久化多个数据。该接口应在访问AppStorage之前调用，适合在应用启动时初始化。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[persistProps](ts-state-management.md#persistprops10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | {key: string; defaultValue: any}[] | 是 | 持久化数组，其中key为属性名，defaultValue为默认值。规则同PersistProp。 |

**示例：**

```ts
PersistentStorage.PersistProps([{ key: 'highScore', defaultValue: '0' }, { key: 'weightScore', defaultValue: '1' }]);
```

### Keys(deprecated)

static Keys(): Array<string>

返回所有持久化属性的属性名的数组。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[keys](ts-state-management.md#keys10-1)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回所有持久化属性的属性名的数组。 |

**示例：**

```ts
let keys: Array<string> = PersistentStorage.Keys();
```

## EnvPropsOptions10+

用于指定环境变量名称及其默认值的键值对对象，作为[envProps](ts-state-management.md#envprops10)参数传入。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 环境变量名称，支持的范围详见[内置环境变量说明](ts-state-management.md#内置环境变量说明)。 |
| defaultValue | number | string | boolean | 否 | 否 | 查询不到环境变量key，则使用defaultValue作为默认值存入AppStorage中。 |

## Environment

Environment提供设备环境状态的查询能力，可将系统环境变量（如深浅色模式、语言、字体缩放、布局方向等）注入AppStorage，使应用能够感知和响应设备环境变化。具体UI使用说明，详见[Environment：设备环境查询](../harmonyos-guides/arkts-environment.md)。

### envProp10+

static envProp<S>(key: string, value: S): boolean

将[Environment](../harmonyos-guides/arkts-environment.md)的内置环境变量key存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。如果系统中未查询到Environment环境变量key的值，则使用默认值value存入AppStorage并返回true。如果AppStorage中已经有对应的key，则返回false。

在没有调用envProp的情况下，直接使用AppStorage读取环境变量，将无法获取到对应的环境变量值。建议在应用启动时调用该接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 环境变量名称，支持的范围详见[内置环境变量说明](ts-state-management.md#内置环境变量说明)。 |
| value | S | 是 | 查询不到环境变量key时，则使用value作为默认值存入AppStorage中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果key对应的属性在AppStorage中存在，则返回false。不存在则在AppStorage中用value作为默认值创建key对应的属性，返回true。 |

**示例：**

envProp具体使用，详见[从UI中访问Environment参数](../harmonyos-guides/arkts-environment.md#从ui中访问environment参数)。

### envProps10+

static envProps(props: EnvPropsOptions[]): void

和[envProp](ts-state-management.md#envprop10)功能类似，不同点在于参数为数组，可以一次性初始化多个数据。在没有调用envProps的情况下，直接使用AppStorage读取环境变量，将无法获取到对应的环境变量值。建议在应用启动时调用，将系统环境变量批量存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| props | [EnvPropsOptions](ts-state-management.md#envpropsoptions10)[] | 是 | 系统环境变量和默认值的键值对的数组。 |

**示例：**

```ts
Environment.envProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
  key: 'languageCode',
  defaultValue: 'en'
}, { key: 'prop', defaultValue: 'hhhh' }]);
```

### keys10+

static keys(): Array<string>

返回环境变量的属性key的数组。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回环境变量的属性key的数组。 |

**示例：**

```ts
Environment.envProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
  key: 'languageCode',
  defaultValue: 'en'
}, { key: 'prop', defaultValue: 'hhhh' }]);

let keys: Array<string> = Environment.keys(); // keys 包含 accessibilityEnabled、languageCode、prop
```

### EnvProp(deprecated)

static EnvProp<S>(key: string, value: S): boolean

将[Environment](../harmonyos-guides/arkts-environment.md)的内置环境变量key存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。如果系统中未查询到Environment环境变量key的值，则使用默认值value存入AppStorage并返回true。如果AppStorage中已经有对应的key，则返回false。

在没有调用EnvProp的情况下，直接使用AppStorage读取环境变量，将无法获取到对应的环境变量值。建议在应用启动时调用该接口。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[envProp](ts-state-management.md#envprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 环境变量名称，支持的范围详见[内置环境变量说明](ts-state-management.md#内置环境变量说明)。 |
| value | S | 是 | 查询不到环境变量key时，则使用value作为默认值存入AppStorage中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果key对应的属性在AppStorage中存在，则返回false。不存在则在AppStorage中用value作为默认值创建key对应的属性，返回true。 |

**示例：**

```ts
Environment.EnvProp('accessibilityEnabled', 'default');
```

### EnvProps(deprecated)

static EnvProps(props: {key: string; defaultValue: any;}[]): void

和[EnvProp](ts-state-management.md#envpropdeprecated)功能类似，不同点在于参数为数组，可以一次性初始化多个数据。在没有调用EnvProps的情况下，直接使用AppStorage读取环境变量，将无法获取到对应的环境变量值。建议在应用启动时调用，将系统环境变量批量存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[envProps](ts-state-management.md#envprops10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| props | {key: string; defaultValue: any}[] | 是 | 系统环境变量和默认值的键值对的数组。 |

**示例：**

```ts
Environment.EnvProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
  key: 'languageCode',
  defaultValue: 'en'
}, { key: 'prop', defaultValue: 'hhhh' }]);
```

### Keys(deprecated)

static Keys(): Array<string>

返回环境变量的属性key的数组。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[keys](ts-state-management.md#keys10-2)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回环境变量的属性key的数组。 |

**示例：**

```ts
Environment.EnvProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
  key: 'languageCode',
  defaultValue: 'en'
}, { key: 'prop', defaultValue: 'hhhh' }]);

let keys: Array<string> = Environment.Keys(); // keys 包含 accessibilityEnabled、languageCode、prop
```

## 内置环境变量说明

| key | 类型 | 说明 |
| --- | --- | --- |
| accessibilityEnabled | string | 无障碍屏幕朗读是否启用。当无法获取环境变量中的accessibilityEnabled的值时，将通过envProp、envProps等接口传入的开发者指定的默认值添加到AppStorage中。 |
| colorMode | [ColorMode](ts-state-management-environment-variables.md#colormode) | 深浅色模式，可选值为：  - ColorMode.LIGHT：浅色模式；  - ColorMode.DARK：深色模式。 |
| fontScale | number | 字体大小比例。 |
| fontWeightScale | number | 字重比例。 |
| layoutDirection | [LayoutDirection](ts-state-management-environment-variables.md#layoutdirection) | 布局方向类型，可选值为：  - LayoutDirection.LTR：从左到右；  - LayoutDirection.RTL：从右到左；  - LayoutDirection.Auto：跟随系统。 |
| languageCode | string | 当前系统语言，小写字母，例如zh。 |
