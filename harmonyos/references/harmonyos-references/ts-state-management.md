---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management
title: 应用级变量的状态管理
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 应用级变量的状态管理
category: harmonyos-references
scraped_at: 2026-04-28T08:02:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7e877972efbd171bad50a49eb66dacb848ccf0cfa6ef115a7b9c6ea9b8c0bd32
---

状态管理模块提供了应用程序的数据存储能力、持久化数据管理能力、UIAbility数据存储能力和应用程序需要的环境状态。

说明

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

本文中T和S的含义如下：

| 类型 | 说明 |
| --- | --- |
| T | Class，number，boolean，string和这些类型的数组形式。 |
| S | number，boolean，string。 |

## AppStorage

PhonePC/2in1TabletTVWearable

AppStorage具体UI使用说明，详见[AppStorage(应用全局的UI状态存储)](../harmonyos-guides/arkts-appstorage.md)

### ref12+

PhonePC/2in1TabletTVWearable

static ref<T>(propName: string): AbstractProperty<T> | undefined

如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回AppStorage中propName对应属性的引用。否则，返回undefined。

与[link](ts-state-management.md#link10)的功能基本一致，但不需要手动释放返回的[AbstractProperty](ts-state-management.md#abstractproperty12)类型的变量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbstractProperty<T>](ts-state-management.md#abstractproperty12) | undefined | AppStorage中propName对应属性的引用，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let refToPropA1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
3. let refToPropA2: AbstractProperty<number> | undefined = AppStorage.ref('PropA'); // refToPropA2.get() == 47
4. refToPropA1?.set(48); // 同步修改AppStorage: refToPropA1.get() == refToPropA2.get() == 48
```

### setAndRef12+

PhonePC/2in1TabletTVWearable

static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>

与[ref](ts-state-management.md#ref12)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回AppStorage中propName对应属性的引用。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，并返回其引用。

与[setAndLink](ts-state-management.md#setandlink10)的功能基本一致，但不需要手动释放返回的[AbstractProperty](ts-state-management.md#abstractproperty12)类型的变量。

说明

从API version 12开始，AppStorage支持[Map](../harmonyos-guides/arkts-appstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-appstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-appstorage.md#appstorage支持联合类型)。

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
| [AbstractProperty<T>](ts-state-management.md#abstractproperty12) | AbstractProperty<T>的实例，为AppStorage中propName对应属性的引用。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let ref1: AbstractProperty<number> = AppStorage.setAndRef('PropB', 49); // 用默认值49创建PropB
3. let ref2: AbstractProperty<number> = AppStorage.setAndRef('PropA', 50); // PropA已存在，值为47
```

### link10+

PhonePC/2in1TabletTVWearable

static link<T>(propName: string): SubscribedAbstractProperty<T>

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立双向数据绑定。如果给定的propName在AppStorage中存在，返回AppStorage中propName对应属性的双向绑定数据。

双向绑定数据的修改会同步回AppStorage中，AppStorage会将变化同步到所有绑定该propName的数据和自定义组件中。

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
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | 返回双向绑定的数据，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let linkToPropA1: SubscribedAbstractProperty<number> = AppStorage.link('PropA');
3. let linkToPropA2: SubscribedAbstractProperty<number> = AppStorage.link('PropA'); // linkToPropA2.get() == 47
4. linkToPropA1.set(48); // 双向同步: linkToPropA1.get() == linkToPropA2.get() == 48
```

### setAndLink10+

PhonePC/2in1TabletTVWearable

static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[link](ts-state-management.md#link10)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

说明

从API version 12开始，AppStorage支持[Map](../harmonyos-guides/arkts-appstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-appstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-appstorage.md#appstorage支持联合类型)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值，从API version 12开始，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<T>的实例，为AppStorage中propName对应属性的双向绑定的数据。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let link1: SubscribedAbstractProperty<number> = AppStorage.setAndLink('PropB', 49); // 用默认值49创建PropB
3. let link2: SubscribedAbstractProperty<number> = AppStorage.setAndLink('PropA', 50); // PropA已存在，值为47
```

### prop10+

PhonePC/2in1TabletTVWearable

static prop<T>(propName: string): SubscribedAbstractProperty<T>

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立单向属性绑定。如果给定的propName在AppStorage中存在，则返回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回undefined。单向绑定数据的修改不会被同步回AppStorage中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | 返回单向绑定的数据，如果AppStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
3. let prop2: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
4. prop1.set(1); // 单向同步：prop1.get()的值为1，prop2.get()的值为47
```

### setAndProp10+

PhonePC/2in1TabletTVWearable

static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[prop](ts-state-management.md#prop10)接口类似。如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

说明

从API version 12开始，AppStorage支持[Map](../harmonyos-guides/arkts-appstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-appstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-appstorage.md#appstorage支持联合类型)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在时，使用defaultValue在AppStorage中初始化propName对应属性的值，从API version 12开始，defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<T>的实例。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let prop: SubscribedAbstractProperty<number> = AppStorage.setAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

### has10+

PhonePC/2in1TabletTVWearable

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

```
1. AppStorage.has('simpleProp');
```

### get10+

PhonePC/2in1TabletTVWearable

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
| T | undefined | AppStorage中propName对应的属性，如果不存在则返回undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let value: number = AppStorage.get('PropA') as number; // 47
```

### set10+

PhonePC/2in1TabletTVWearable

static set<T>(propName: string, newValue: T): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中设置propName对应属性的值。如果newValue的值和propName对应属性的值相同，即不需要做赋值操作，状态变量不会通知UI刷新propName对应属性的值。

说明

从API version 12开始，AppStorage支持[Map](../harmonyos-guides/arkts-appstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-appstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-appstorage.md#appstorage支持联合类型)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | 属性值，从API version 12开始可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中不存在propName对应的属性，或设值失败，则返回false。设置成功则返回true。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 48);
2. let res: boolean = AppStorage.set('PropA', 47) // true
3. let res1: boolean = AppStorage.set('PropB', 47) // false
```

### setOrCreate10+

PhonePC/2in1TabletTVWearable

static setOrCreate<T>(propName: string, newValue: T): void

如果propName已经在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。

如果propName不存在，则创建propName属性，值为newValue。setOrCreate只可以创建单个AppStorage的键值对，如果想创建多个AppStorage键值对，可以多次调用此方法。

说明

从API version 12开始，AppStorage支持[Map](../harmonyos-guides/arkts-appstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-appstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-appstorage.md#appstorage支持联合类型)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | 属性值，从API version 12开始可以为null或undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('simpleProp', 121);
```

### delete10+

PhonePC/2in1TabletTVWearable

static delete(propName: string): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中删除propName对应的属性。

在AppStorage中删除该属性的前提是必须保证该属性没有订阅者。如果有订阅者，则返回false。如果没有订阅者，则删除成功并返回true。

属性的订阅者为：

1. [@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)、[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)装饰的变量。
2. 通过[link](ts-state-management.md#link10)、[prop](ts-state-management.md#prop10)、[setAndLink](ts-state-management.md#setandlink10)、[setAndProp](ts-state-management.md#setandprop10)接口返回的[SubscribedAbstractProperty](ts-state-management.md#subscribedabstractproperty)的实例。

如果想要删除这些订阅者，可以通过以下方式：

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

```
1. AppStorage.setOrCreate('PropA', 47);
2. AppStorage.link<number>('PropA');
3. let res: boolean = AppStorage.delete('PropA'); // false，PropA 还存在订阅者

5. AppStorage.setOrCreate('PropB', 48);
6. let res1: boolean = AppStorage.delete('PropB'); // true，PropB 已从AppStorage成功删除
```

### keys10+

PhonePC/2in1TabletTVWearable

static keys(): IterableIterator<string>

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有的属性名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | AppStorage中所有的属性名。 |

**示例：**

```
1. AppStorage.setOrCreate('PropB', 48);
2. let keys: IterableIterator<string> = AppStorage.keys();
```

### clear10+

PhonePC/2in1TabletTVWearable

static clear(): boolean

删除[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有属性。删除所有属性的前提是，AppStorage已经没有任何订阅者。如果有订阅者，clear将不会生效并返回false。如果没有订阅者，则删除成功，并返回true。

订阅者的含义参考[delete](ts-state-management.md#delete10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中的属性已经没有订阅者则删除成功，返回true；如果当前仍有订阅者，返回false。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let res: boolean = AppStorage.clear(); // true，已经没有订阅者
```

### size10+

PhonePC/2in1TabletTVWearable

static size(): number

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中的属性数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回AppStorage中属性的数量。 |

**示例：**

```
1. AppStorage.setOrCreate('PropB', 48);
2. let res: number = AppStorage.size(); // 1
```

### Link(deprecated)

PhonePC/2in1TabletTVWearable

static Link(propName: string): any

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立双向数据绑定。如果给定的propName在AppStorage中存在，返回与AppStorage中propName对应属性的双向绑定数据。

双向绑定数据的修改会同步回AppStorage中，AppStorage会将变化同步到所有绑定该propName的数据和自定义组件中。

如果AppStorage中不存在propName，则返回undefined。

说明

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

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let linkToPropA1: SubscribedAbstractProperty<number> = AppStorage.Link('PropA');
3. let linkToPropA2: SubscribedAbstractProperty<number> = AppStorage.Link('PropA'); // linkToPropA2.get() == 47
4. linkToPropA1.set(48); // 双向同步: linkToPropA1.get() == linkToPropA2.get() == 48
```

### SetAndLink(deprecated)

PhonePC/2in1TabletTVWearable

static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[Link](ts-state-management.md#linkdeprecated)接口类似，如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，并返回其双向绑定数据。defaultValue必须为T类型，且不能为null或undefined。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[setAndLink](ts-state-management.md#setandlink10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在AppStorage中不存在，使用defaultValue在AppStorage中初始化propName对应属性的值，defaultValue不能为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<T>的实例，和AppStorage中propName对应属性的双向绑定的数据。 |

**示例：**

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let link1: SubscribedAbstractProperty<number> = AppStorage.SetAndLink('PropB', 49); // 用默认值49创建PropB
3. let link2: SubscribedAbstractProperty<number> = AppStorage.SetAndLink('PropA', 50); // PropA已存在，值为47
```

### Prop(deprecated)

PhonePC/2in1TabletTVWearable

static Prop(propName: string): any

与[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的propName建立单向属性绑定。如果给定的propName在AppStorage中存在，则返回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回undefined。单向绑定数据的修改不会被同步回AppStorage中。

说明

Prop仅支持简单类型。

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

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let prop1: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA');
3. let prop2: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA');
4. prop1.set(1); // 单向同步：prop1.get()的值为1，prop2.get()的值为47
```

### SetAndProp(deprecated)

PhonePC/2in1TabletTVWearable

static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>

与[Prop](ts-state-management.md#propdeprecated)接口类似。如果给定的propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。defaultValue必须为S类型，且不能为null或undefined。

说明

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
| [SubscribedAbstractProperty<S>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<S>的实例。 |

**示例：**

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let prop: SubscribedAbstractProperty<number> = AppStorage.SetAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

### Has(deprecated)

PhonePC/2in1TabletTVWearable

static Has(propName: string): boolean

判断propName对应的属性是否在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在。

说明

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

```
1. AppStorage.Has('simpleProp');
```

### Get(deprecated)

PhonePC/2in1TabletTVWearable

static Get<T>(propName: string): T | undefined

获取propName在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中对应的属性值。如果不存在则返回undefined。

说明

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

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let value: number = AppStorage.Get('PropA') as number; // 47
```

### Set(deprecated)

PhonePC/2in1TabletTVWearable

static Set<T>(propName: string, newValue: T): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中设置propName对应属性的值，如果newValue的值和propName对应属性的值相同，即不需要做赋值操作，状态变量不会通知UI刷新propName对应属性的值，从API version 12开始，newValue可以为null或undefined。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[set](ts-state-management.md#set10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | 属性值，从API version 12开始可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中不存在propName对应的属性，返回false。设置成功则返回true。 |

**示例：**

```
1. AppStorage.SetOrCreate('PropA', 48);
2. let res: boolean = AppStorage.Set('PropA', 47) // true
3. let res1: boolean = AppStorage.Set('PropB', 47) // false
```

### SetOrCreate(deprecated)

PhonePC/2in1TabletTVWearable

static SetOrCreate<T>(propName: string, newValue: T): void

如果propName已经在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中存在，则设置propName对应的属性值为newValue。如果不存在，则创建propName属性，值为newValue。

newValue不能为null或undefined。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[setOrCreate](ts-state-management.md#setorcreate10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | AppStorage中的属性名。 |
| newValue | T | 是 | 属性值，不能为null或undefined。 |

**示例：**

```
1. AppStorage.SetOrCreate('simpleProp', 121);
```

### Delete(deprecated)

PhonePC/2in1TabletTVWearable

static Delete(propName: string): boolean

在[AppStorage](../harmonyos-guides/arkts-appstorage.md)中删除propName对应的属性。

在AppStorage中删除该属性的前提是必须保证该属性没有订阅者。如果有订阅者，则返回false。如果没有订阅者则删除成功并返回true。

属性的订阅者为[Link](ts-state-management.md#linkdeprecated)、[Prop](ts-state-management.md#propdeprecated)等接口绑定的propName，以及[@StorageLink('propName')](../harmonyos-guides/arkts-appstorage.md#storagelink)和[@StorageProp('propName')](../harmonyos-guides/arkts-appstorage.md#storageprop)。如果自定义组件中使用@StorageLink('propName')和@StorageProp('propName')或者SubscribedAbstractProperty实例依旧对propName有同步关系，则该属性不能从AppStorage中删除。

说明

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

```
1. AppStorage.SetOrCreate('PropA', 47);
2. AppStorage.Link('PropA');
3. let res: boolean = AppStorage.Delete('PropA'); // false，PropA 还存在订阅者

5. AppStorage.SetOrCreate('PropB', 48);
6. let res1: boolean = AppStorage.Delete('PropB'); // true，PropB 已从AppStorage成功删除
```

### Keys(deprecated)

PhonePC/2in1TabletTVWearable

static Keys(): IterableIterator<string>

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有的属性名。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[keys](ts-state-management.md#keys10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | AppStorage中所有的属性名。 |

**示例：**

```
1. AppStorage.SetOrCreate('PropB', 48);
2. let keys: IterableIterator<string> = AppStorage.Keys();
```

### staticClear(deprecated)

PhonePC/2in1TabletTVWearable

static staticClear(): boolean

删除所有的属性。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[clear](ts-state-management.md#clear10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除所有的属性。如果删除成功，返回true；如果当前有状态变量依旧引用此属性，返回false。 |

**示例：**

```
1. let simple = AppStorage.staticClear();
```

### Clear(deprecated)

PhonePC/2in1TabletTVWearable

static Clear(): boolean

删除[AppStorage](../harmonyos-guides/arkts-appstorage.md)中所有属性。删除所有属性的前提是，AppStorage已经没有任何订阅者。如果有订阅者，Clear将不会生效并返回false。如果没有订阅者且删除成功则返回true。

订阅者的含义参考[delete](ts-state-management.md#delete10)。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[clear](ts-state-management.md#clear10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果AppStorage中的属性已经没有订阅者则删除成功，返回true。否则返回false。 |

**示例：**

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let res: boolean = AppStorage.Clear(); // true，已经没有订阅者
```

### IsMutable(deprecated)

PhonePC/2in1TabletTVWearable

static IsMutable(propName: string): boolean

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中propName对应的属性是否是可变的。

说明

从API version 7开始支持，从API version 10开始废弃。

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

```
1. AppStorage.SetOrCreate('PropA', 47);
2. let res: boolean = AppStorage.IsMutable('PropA');
```

### Size(deprecated)

PhonePC/2in1TabletTVWearable

static Size(): number

返回[AppStorage](../harmonyos-guides/arkts-appstorage.md)中的属性数量。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[size](ts-state-management.md#size10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回AppStorage中属性的数量。 |

**示例：**

```
1. AppStorage.SetOrCreate('PropB', 48);
2. let res: number = AppStorage.Size(); // 1
```

## LocalStorage9+

PhonePC/2in1TabletTVWearable

LocalStorage具体UI使用说明，详见[LocalStorage(页面级UI状态存储)](../harmonyos-guides/arkts-localstorage.md)

### constructor9+

PhonePC/2in1TabletTVWearable

constructor(initializingProperties?: Object)

创建一个新的[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。使用Object.keys(initializingProperties)返回的属性和其数值，初始化LocalStorage实例。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initializingProperties | Object | 否 | 用initializingProperties包含的属性和数值初始化LocalStorage。initializingProperties不能为undefined。默认值为空对象，即初始化时不在LocalStorage中新增属性。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
```

### getShared(deprecated)

PhonePC/2in1TabletTVWearable

static getShared(): LocalStorage

获取当前stage共享的[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。

说明

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getSharedLocalStorage](arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)替代。

从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getSharedLocalStorage](arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)来明确UI的执行上下文。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalStorage](ts-state-management.md#localstorage9) | 返回LocalStorage实例。 |

### has9+

PhonePC/2in1TabletTVWearable

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

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. storage.has('PropA'); // true
```

### get9+

PhonePC/2in1TabletTVWearable

get<T>(propName: string): T | undefined

获取propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中对应的属性值。

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

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let value: number = storage.get('PropA') as number; // 47
```

### set9+

PhonePC/2in1TabletTVWearable

set<T>(propName: string, newValue: T): boolean

在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中设置propName对应属性的值。如果newValue的值和propName对应属性的值相同，即不需要做赋值操作，状态变量不会通知UI刷新propName对应属性的值。

说明

从API version 12开始，LocalStorage支持[Map](../harmonyos-guides/arkts-localstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-localstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-localstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-localstorage.md#localstorage支持联合类型)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| newValue | T | 是 | 属性值，从API version 12开始可以为undefined或者null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中不存在propName对应的属性，返回false。设置成功返回true。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let res: boolean = storage.set('PropA', 47); // true
4. let res1: boolean = storage.set('PropB', 47); // false
```

### setOrCreate9+

PhonePC/2in1TabletTVWearable

setOrCreate<T>(propName: string, newValue: T): boolean

如果propName已经在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。

如果propName不存在，则创建propName属性，值为newValue。setOrCreate只可以创建单个LocalStorage的键值对，如果想创建多个LocalStorage键值对，可以多次调用此方法。

说明

从API version 12开始，LocalStorage支持[Map](../harmonyos-guides/arkts-localstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-localstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-localstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-localstorage.md#localstorage支持联合类型)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| newValue | T | 是 | 属性值，从API version 12开始可以为undefined或者null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中存在propName，则更新其值为newValue，返回true。  如果LocalStorage中不存在propName，则创建propName，并初始化其值为newValue，返回true。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let res: boolean = storage.setOrCreate('PropA', 121); // true
4. let res1: boolean = storage.setOrCreate('PropB', 111); // true
5. let res2: boolean = storage.setOrCreate('PropB', null); // true (API12及之后返回true，API11及之前返回false)
```

### ref12+

PhonePC/2in1TabletTVWearable

ref<T>(propName: string): AbstractProperty<T> | undefined

如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回LocalStorage中propName对应属性的引用。否则，返回undefined。

与[link](ts-state-management.md#link9)的功能基本一致，但不需要手动释放返回的[AbstractProperty](ts-state-management.md#abstractproperty12)类型的变量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbstractProperty<T>](ts-state-management.md#abstractproperty12) | undefined | LocalStorage中propName对应属性的引用，如果LocalStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let refToPropA1: AbstractProperty<number> | undefined = storage.ref('PropA');
4. let refToPropA2: AbstractProperty<number> | undefined = storage.ref('PropA'); // refToPropA2.get() == 47
5. refToPropA1?.set(48); // refToPropA1.get() == refToPropA2.get() == 48
```

### setAndRef12+

PhonePC/2in1TabletTVWearable

setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>

与[ref](ts-state-management.md#ref12-1)接口类似，如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回LocalStorage中propName对应属性的引用。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，并返回其引用。

与[setAndLink](ts-state-management.md#setandlink9)的功能基本一致，但不需要手动释放返回的[AbstractProperty](ts-state-management.md#abstractproperty12)类型的变量。

说明

从API version 12开始，LocalStorage支持[Map](../harmonyos-guides/arkts-localstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-localstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-localstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-localstorage.md#localstorage支持联合类型)。

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
| [AbstractProperty<T>](ts-state-management.md#abstractproperty12) | AbstractProperty<T>的实例，为LocalStorage中propName对应属性的引用。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let ref1: AbstractProperty<number> = storage.setAndRef('PropB', 49); // 用默认值49创建PropB
4. let ref2: AbstractProperty<number> = storage.setAndRef('PropA', 50); // PropA已存在，值为47
```

### link9+

PhonePC/2in1TabletTVWearable

link<T>(propName: string): SubscribedAbstractProperty<T>

如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例中存在，则返回与LocalStorage中propName对应属性的双向绑定数据。

双向绑定数据的修改会被同步回LocalStorage中，LocalStorage会将变化同步到所有绑定该propName的数据和Component中。

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
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<T>的实例，与LocalStorage中propName对应属性的双向绑定的数据，如果LocalStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let linkToPropA1: SubscribedAbstractProperty<number> = storage.link('PropA');
4. let linkToPropA2: SubscribedAbstractProperty<number> = storage.link('PropA'); // linkToPropA2.get() == 47
5. linkToPropA1.set(48); // 双向同步: linkToPropA1.get() == linkToPropA2.get() == 48
```

### setAndLink9+

PhonePC/2in1TabletTVWearable

setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>

与[link](ts-state-management.md#link9)接口类似，如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

说明

从API version 12开始，LocalStorage支持[Map](../harmonyos-guides/arkts-localstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-localstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-localstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-localstorage.md#localstorage支持联合类型)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| defaultValue | T | 是 | 当propName在LocalStorage中不存在时，使用defaultValue在LocalStorage中初始化propName对应属性的值，从API version 12开始defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<T>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<T>的实例，与LocalStorage中propName对应属性的双向绑定的数据。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let link1: SubscribedAbstractProperty<number> = storage.setAndLink('PropB', 49); // 用默认值49创建PropB
4. let link2: SubscribedAbstractProperty<number> = storage.setAndLink('PropA', 50); // PropA已存在，值为47
```

### prop9+

PhonePC/2in1TabletTVWearable

prop<S>(propName: string): SubscribedAbstractProperty<S>

如果给定的propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回与LocalStorage中propName对应属性的单向绑定数据。如果LocalStorage中不存在propName，则返回undefined。单向绑定数据的修改不会被同步回LocalStorage中。

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
| [SubscribedAbstractProperty<S>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<S>的实例，和LocalStorage中propName对应属性的单向绑定的数据。如果LocalStorage中不存在对应的propName，则返回undefined。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let prop1: SubscribedAbstractProperty<number> = storage.prop('PropA');
4. let prop2: SubscribedAbstractProperty<number> = storage.prop('PropA');
5. prop1.set(1); // 单向同步：prop1.get()的值为1，prop2.get()的值为47
```

### setAndProp9+

PhonePC/2in1TabletTVWearable

setAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>

与[prop](ts-state-management.md#prop9)接口类似。如果propName在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中存在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在LocalStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

说明

从API version 12开始，LocalStorage支持[Map](../harmonyos-guides/arkts-localstorage.md#装饰map类型变量)、[Set](../harmonyos-guides/arkts-localstorage.md#装饰set类型变量)、[Date类型](../harmonyos-guides/arkts-localstorage.md#装饰date类型变量)，支持null、undefined以及[联合类型](../harmonyos-guides/arkts-localstorage.md#localstorage支持联合类型)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propName | string | 是 | LocalStorage中的属性名。 |
| defaultValue | S | 是 | 当propName在LocalStorage中不存在，使用defaultValue在LocalStorage中初始化propName对应属性的值，从API version 12开始defaultValue可以为null或undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SubscribedAbstractProperty<S>](ts-state-management.md#subscribedabstractproperty) | SubscribedAbstractProperty<S>的实例，和LocalStorage中propName对应属性的单向绑定的数据。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let prop: SubscribedAbstractProperty<number> = storage.setAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

### delete9+

PhonePC/2in1TabletTVWearable

delete(propName: string): boolean

在[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中删除propName对应的属性。在LocalStorage中删除属性的前提是该属性已经没有订阅者，如果有订阅者，则返回false。如果没有订阅者则删除成功并返回true。

属性的订阅者为：

1. [@LocalStorageLink](../harmonyos-guides/arkts-localstorage.md#localstoragelink)、[@LocalStorageProp](../harmonyos-guides/arkts-localstorage.md#localstorageprop)装饰的变量。
2. 通过[link](ts-state-management.md#link9)、[prop](ts-state-management.md#prop9)、[setAndLink](ts-state-management.md#setandlink9)、[setAndProp](ts-state-management.md#setandprop9)接口返回的[SubscribedAbstractProperty](ts-state-management.md#subscribedabstractproperty)的实例。

如果想要删除这些订阅者，可以通过以下方式：

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

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. storage.link<number>('PropA');
4. let res: boolean = storage.delete('PropA'); // false，PropA 还存在订阅者
5. let res1: boolean = storage.delete('PropB'); // false，PropB 不存在于storage中
6. storage.setOrCreate('PropB', 48);
7. let res2: boolean = storage.delete('PropB'); // true，PropB 已从storage成功删除
```

### keys9+

PhonePC/2in1TabletTVWearable

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

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let keys: IterableIterator<string> = storage.keys();
```

### size9+

PhonePC/2in1TabletTVWearable

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

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let res: number = storage.size(); // 1
```

### clear9+

PhonePC/2in1TabletTVWearable

clear(): boolean

删除[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所有的属性。删除所有属性的前提是已经没有任何订阅者。如果有订阅者，clear不会生效并返回false。如果没有订阅者则删除成功并返回true。

订阅者的含义参考[delete](ts-state-management.md#delete9)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果LocalStorage中的属性已经没有任何订阅者，则删除成功，并返回true。否则返回false。 |

**示例：**

```
1. let para: Record<string, number> = { 'PropA': 47 };
2. let storage: LocalStorage = new LocalStorage(para);
3. let res: boolean = storage.clear(); // true，已经没有订阅者
```

### GetShared(deprecated)

PhonePC/2in1TabletTVWearable

static GetShared(): LocalStorage

获取当前stage共享的[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getSharedLocalStorage](arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalStorage](ts-state-management.md#localstorage9) | 返回LocalStorage实例。 |

**示例：**

```
1. let storage: LocalStorage = LocalStorage.GetShared();
```

## AbstractProperty12+

PhonePC/2in1TabletTVWearable

AbstractProperty是[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中属性的引用。

### get12+

PhonePC/2in1TabletTVWearable

get(): T

读取[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所引用属性的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | AppStorage/LocalStorage中所引用属性的数据。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
3. ref1?.get(); //  ref1.get()=47
```

### set12+

PhonePC/2in1TabletTVWearable

set(newValue: T): void

更新[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所引用属性的数据，newValue必须是T类型，可以为null或undefined。

说明

从API version 12开始，AppStorage/LocalStorage支持Map、Set、Date类型，支持null、undefined以及联合类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | 要更新的数据，可以为null或undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
3. ref1?.set(1); //  ref1.get()=1
4. let a: Map<string, number> = new Map([['1', 0]]);
5. let ref2 = AppStorage.setAndRef('MapA', a);
6. ref2.set(a);
7. let b: Set<string> = new Set('1');
8. let ref3 = AppStorage.setAndRef('SetB', b);
9. ref3.set(b);
10. let c: Date = new Date('2024');
11. let ref4 = AppStorage.setAndRef('DateC', c);
12. ref4.set(c);
13. ref2.set(null);
14. ref3.set(undefined);
```

### info12+

PhonePC/2in1TabletTVWearable

info(): string

读取[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中所引用属性的属性名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | AppStorage/LocalStorage中所引用属性的属性名。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
3. ref1?.info(); //  ref1.info()='PropA'
```

## SubscribedAbstractProperty

PhonePC/2in1TabletTVWearable

SubscribedAbstractProperty是[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)中同步的属性。

### get9+

PhonePC/2in1TabletTVWearable

abstract get(): T

读取从[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)同步属性的数据。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | AppStorage/LocalStorage同步属性的数据。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
3. prop1.get(); //  prop1.get()=47
```

### set9+

PhonePC/2in1TabletTVWearable

abstract set(newValue: T): void

设置[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)同步属性的数据，newValue必须是T类型，从API version 12开始可以为null或undefined。

说明

从API version 12开始，AppStorage/LocalStorage支持Map、Set、Date类型，支持null、undefined以及联合类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | 要设置的数据，从API version 12开始可以为null或undefined。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
3. prop1.set(1); //  prop1.get()=1
4. // 从API12开始支持Map、Set、Date类型，支持null、undefined以及联合类型。
5. let a: Map<string, number> = new Map([['1', 0]]);
6. let prop2 = AppStorage.setAndProp('MapA', a);
7. prop2.set(a);
8. let b: Set<string> = new Set('1');
9. let prop3 = AppStorage.setAndProp('SetB', b);
10. prop3.set(b);
11. let c: Date = new Date('2024');
12. let prop4 = AppStorage.setAndProp('DateC', c);
13. prop4.set(c);
14. prop2.set(null);
15. prop3.set(undefined);
```

### aboutToBeDeleted10+

PhonePC/2in1TabletTVWearable

abstract aboutToBeDeleted(): void

取消[SubscribedAbstractProperty](ts-state-management.md#subscribedabstractproperty)实例对[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[LocalStorage](../harmonyos-guides/arkts-localstorage.md)的单/双向同步关系，并无效化SubscribedAbstractProperty实例，即当调用aboutToBeDeleted方法之后不能再使用SubscribedAbstractProperty实例调用[set](ts-state-management.md#set9-1)或[get](ts-state-management.md#get9-1)方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let link = AppStorage.setAndLink('PropB', 49); // PropA -> 47, PropB -> 49
3. link.aboutToBeDeleted();
```

### info10+

PhonePC/2in1TabletTVWearable

info(): string

返回属性名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 属性名称。 |

**示例：**

```
1. AppStorage.setOrCreate('PropA', 47);
2. let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
3. prop1.info(); // prop1.info() = 'PropA'
```

## PersistPropsOptions10+

PhonePC/2in1TabletTVWearable

用于指定持久化属性及其默认值的键值对对象，作为[persistProps](ts-state-management.md#persistprops10)参数传入。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 属性名。 |
| defaultValue | number | string | boolean | Object | 否 | 否 | 在PersistentStorage和AppStorage未查询到时，则使用默认值初始化它。从API version 12开始，defaultValue允许为null或undefined。 |

## PersistentStorage

PhonePC/2in1TabletTVWearable

PersistentStorage具体UI使用说明，详见[PersistentStorage(持久化存储UI状态)](../harmonyos-guides/arkts-persiststorage.md)

说明

从API version 12开始，PersistentStorage支持null、undefined。

### persistProp10+

PhonePC/2in1TabletTVWearable

static persistProp<T>(key: string, defaultValue: T): void

将[AppStorage](../harmonyos-guides/arkts-appstorage.md)中key对应的属性持久化到文件中。该接口的调用通常在访问AppStorage之前。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)文件中存在key对应的属性，在AppStorage中创建对应的propName，并用在PersistentStorage中找到的key的属性初始化。
2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。
3. 如果AppStorage中也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值，覆盖掉PersistentStorage文件中的值。由于AppStorage是内存内数据，该行为会导致数据丧失持久化能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 属性名。 |
| defaultValue | T | 是 | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。从API version 12开始允许为null或undefined。 |

**示例：**

persistProp具体使用，见[从AppStorage中访问PersistentStorage初始化的属性](../harmonyos-guides/arkts-persiststorage.md#从appstorage中访问persistentstorage初始化的属性)

### deleteProp10+

PhonePC/2in1TabletTVWearable

static deleteProp(key: string): void

[persistProp](ts-state-management.md#persistprop10)的逆向操作。将key对应的属性从PersistentStorage中删除，后续[AppStorage](../harmonyos-guides/arkts-appstorage.md)的操作，对[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)不会再有影响。该操作会将对应的key从持久化文件中删除，如果希望再次持久化，可以再次调用[persistProp](ts-state-management.md#persistprop10)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | PersistentStorage中的属性名。 |

**示例：**

```
1. PersistentStorage.deleteProp('highScore');
```

### persistProps10+

PhonePC/2in1TabletTVWearable

static persistProps(props: PersistPropsOptions[]): void

行为和[persistProp](ts-state-management.md#persistprop10)类似，不同在于可以一次性持久化多个数据，适合在应用启动的时候初始化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| props | [PersistPropsOptions](ts-state-management.md#persistpropsoptions10)[] | 是 | 持久化数组。 |

**示例：**

```
1. PersistentStorage.persistProps([{ key: 'highScore', defaultValue: '0' }, { key: 'wightScore', defaultValue: '1' }]);
```

### keys10+

PhonePC/2in1TabletTVWearable

static keys(): Array<string>

返回所有持久化属性的属性名的数组。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回所有持久化属性的属性名的数组。 |

**示例：**

```
1. let keys: Array<string> = PersistentStorage.keys();
```

### PersistProp(deprecated)

PhonePC/2in1TabletTVWearable

static PersistProp<T>(key: string, defaultValue: T): void

将[AppStorage](../harmonyos-guides/arkts-appstorage.md)中key对应的属性持久化到文件中。该接口的调用通常在访问AppStorage之前。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)文件中存在key对应的属性，在AppStorage中创建对应的propName，并用在PersistentStorage中找到的key的属性初始化。
2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。
3. 如果AppStorage也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值，覆盖掉PersistentStorage文件中的值。由于AppStorage是内存内数据，该行为会导致数据丧失持久化能力。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[persistProp](ts-state-management.md#persistprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 属性名。 |
| defaultValue | T | 是 | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。不允许为null或undefined。 |

**示例：**

```
1. PersistentStorage.PersistProp('highScore', '0');
```

### DeleteProp(deprecated)

PhonePC/2in1TabletTVWearable

static DeleteProp(key: string): void

[PersistProp](ts-state-management.md#persistpropdeprecated)的逆向操作。将key对应的属性从[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)中删除，后续[AppStorage](../harmonyos-guides/arkts-appstorage.md)的操作，对PersistentStorage不会再有影响。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[deleteProp](ts-state-management.md#deleteprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | PersistentStorage中的属性名。 |

**示例：**

```
1. PersistentStorage.DeleteProp('highScore');
```

### PersistProps(deprecated)

PhonePC/2in1TabletTVWearable

static PersistProps(properties: {key: string; defaultValue: any;}[]): void

行为和[PersistProp](ts-state-management.md#persistpropdeprecated)类似，不同在于可以一次性持久化多个数据，适合在应用启动的时候初始化。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[persistProps](ts-state-management.md#persistprops10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | {key: string; defaultValue: any}[] | 是 | 持久化数组，启动key为属性名，defaultValue为默认值。规则同PersistProp。 |

**示例：**

```
1. PersistentStorage.PersistProps([{ key: 'highScore', defaultValue: '0' }, { key: 'wightScore', defaultValue: '1' }]);
```

### Keys(deprecated)

PhonePC/2in1TabletTVWearable

static Keys(): Array<string>

返回所有持久化属性的属性名的数组。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[keys](ts-state-management.md#keys10-1)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回所有持久化属性的属性名的数组。 |

**示例：**

```
1. let keys: Array<string> = PersistentStorage.Keys();
```

## EnvPropsOptions10+

PhonePC/2in1TabletTVWearable

用于指定环境变量名称及其默认值的键值对对象，作为[envProps](ts-state-management.md#envprops10)参数传入。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 环境变量名称，支持的范围详见[内置环境变量说明](ts-state-management.md#内置环境变量说明)。 |
| defaultValue | number | string | boolean | 否 | 否 | 查询不到环境变量key，则使用defaultValue作为默认值存入AppStorage中。 |

## Environment

PhonePC/2in1TabletTVWearable

Environment具体使用说明，详见[Environment(设备环境查询)](../harmonyos-guides/arkts-environment.md)

### envProp10+

PhonePC/2in1TabletTVWearable

static envProp<S>(key: string, value: S): boolean

将[Environment](../harmonyos-guides/arkts-environment.md)的内置环境变量key存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。如果系统中未查询到Environment环境变量key的值，则使用默认值value，存入成功，返回true。如果AppStorage中已经有对应的key，则返回false。

所以建议在程序启动的时候调用该接口。

在没有调用envProp的情况下，就使用AppStorage读取环境变量是错误的。

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

PhonePC/2in1TabletTVWearable

static envProps(props: EnvPropsOptions[]): void

和[envProp](ts-state-management.md#envprop10)类似，不同点在于参数为数组，可以一次性初始化多个数据。建议在应用启动时调用，将系统环境变量批量存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| props | [EnvPropsOptions](ts-state-management.md#envpropsoptions10)[] | 是 | 系统环境变量和默认值的键值对的数组。 |

**示例：**

```
1. Environment.envProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
2. key: 'languageCode',
3. defaultValue: 'en'
4. }, { key: 'prop', defaultValue: 'hhhh' }]);
```

### keys10+

PhonePC/2in1TabletTVWearable

static keys(): Array<string>

返回环境变量的属性key的数组。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回关联的系统项数组。 |

**示例：**

```
1. Environment.envProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
2. key: 'languageCode',
3. defaultValue: 'en'
4. }, { key: 'prop', defaultValue: 'hhhh' }]);

6. let keys: Array<string> = Environment.keys(); // keys 包含 accessibilityEnabled，languageCode，prop
```

### EnvProp(deprecated)

PhonePC/2in1TabletTVWearable

static EnvProp<S>(key: string, value: S): boolean

将[Environment](../harmonyos-guides/arkts-environment.md)的内置环境变量key存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。如果系统中未查询到Environment环境变量key的值，则使用默认值value，存入成功，返回true。如果AppStorage中已经有对应的key，则返回false。

所以建议在程序启动的时候调用该接口。

在没有调用EnvProp的情况下，就使用AppStorage读取环境变量是错误的。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[envProp](ts-state-management.md#envprop10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 环境变量名称，支持的范围详见[内置环境变量说明](ts-state-management.md#内置环境变量说明)。 |
| value | S | 是 | 查询不到环境变量key，则使用value作为默认值存入AppStorage中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果key对应的属性在AppStorage中存在，则返回false。不存在则在AppStorage中用value作为默认值创建key对应的属性，返回true。 |

**示例：**

```
1. Environment.EnvProp('accessibilityEnabled', 'default');
```

### EnvProps(deprecated)

PhonePC/2in1TabletTVWearable

static EnvProps(props: {key: string; defaultValue: any;}[]): void

和[EnvProp](ts-state-management.md#envpropdeprecated)类似，不同点在于参数为数组，可以一次性初始化多个数据。建议在应用启动时调用，将系统环境变量批量存入[AppStorage](../harmonyos-guides/arkts-appstorage.md)中。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[envProps](ts-state-management.md#envprops10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| props | {key: string; defaultValue: any}[] | 是 | 系统环境变量和默认值的键值对的数组。 |

**示例：**

```
1. Environment.EnvProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
2. key: 'languageCode',
3. defaultValue: 'en'
4. }, { key: 'prop', defaultValue: 'hhhh' }]);
```

### Keys(deprecated)

PhonePC/2in1TabletTVWearable

static Keys(): Array<string>

返回环境变量的属性key的数组。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[keys](ts-state-management.md#keys10-2)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回关联的系统项数组。 |

**示例：**

```
1. Environment.EnvProps([{ key: 'accessibilityEnabled', defaultValue: 'default' }, {
2. key: 'languageCode',
3. defaultValue: 'en'
4. }, { key: 'prop', defaultValue: 'hhhh' }]);

6. let keys: Array<string> = Environment.Keys(); // keys 包含 accessibilityEnabled，languageCode，prop
```

## 内置环境变量说明

PhonePC/2in1TabletTVWearable

| key | 类型 | 说明 |
| --- | --- | --- |
| accessibilityEnabled | string | 无障碍屏幕朗读是否启用。当无法获取环境变量中的accessibilityEnabled的值时，将通过envProp、envProps等接口传入的开发者指定的默认值添加到AppStorage中。 |
| colorMode | [ColorMode](ts-state-management-environment-variables.md#colormode) | 深浅色模式，可选值为：  - ColorMode.LIGHT：浅色模式；  - ColorMode.DARK：深色模式。 |
| fontScale | number | 字体大小比例。 |
| fontWeightScale | number | 字重比例。 |
| layoutDirection | [LayoutDirection](ts-state-management-environment-variables.md#layoutdirection) | 布局方向类型，可选值为：  - LayoutDirection.LTR：从左到右；  - LayoutDirection.RTL：从右到左。  - Auto：跟随系统。 |
| languageCode | string | 当前系统语言，小写字母，例如zh。 |
