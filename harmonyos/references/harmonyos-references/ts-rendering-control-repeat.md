---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat
title: Repeat
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > Repeat
category: harmonyos-references
scraped_at: 2026-04-28T08:02:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d595cad7cda6c0ad7b17cc0ca18b652474adf99ad235582242ebb7d58ef92a41
---

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

Repeat基于数组类型数据来进行循环渲染，一般与滚动容器组件配合使用。

本文档仅为API参数说明。组件描述和使用说明见[Repeat开发者指南](../harmonyos-guides/arkts-new-rendering-control-repeat.md)。

## 接口

PhonePC/2in1TabletTVWearable

### Repeat: <T>(arr: Array<T>)

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array<T> | 是 | 数据源，为Array<T>类型的数组，由开发者决定数据类型。 |

**示例：**

```
1. // arr是Array<string>类型的数组，以arr为数据源创建Repeat组件
2. Repeat<string>(this.arr)
```

### Repeat: <T>(arr: RepeatArray<T>)18+

PhonePC/2in1TabletTVWearable

说明

从API version 18开始，Repeat数据源支持RepeatArray类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [RepeatArray<T>](ts-rendering-control-repeat.md#repeatarrayt18) | 是 | 数据源，为RepeatArray<T>类型的数组，由开发者决定数据类型。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[拖拽排序](ts-universal-attributes-drag-sorting.md)属性外，还支持以下属性。

### each

PhonePC/2in1TabletTVWearable

each(itemGenerator: (repeatItem: RepeatItem<T>) => void)

组件生成函数。当所有[.template()](ts-rendering-control-repeat.md#template)的type和[.templateId()](ts-rendering-control-repeat.md#templateid)返回值不匹配（即当前item不适用任何template定义的样式）时，将使用.each()处理数据项。

说明

* each属性必须有，否则运行时会报错。
* itemGenerator的参数为RepeatItem，该参数将item和index结合到了一起，请勿将RepeatItem参数拆开使用。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemGenerator | (repeatItem: [RepeatItem<T>](ts-rendering-control-repeat.md#repeatitemt)) => void | 是 | 组件生成函数。 |

**示例：**

```
1. // arr是Array<string>类型的数组，为每个数据创建一个Text组件
2. Repeat<string>(this.arr)
3. .each((obj: RepeatItem<string>) => { Text(obj.item) })
```

### key

PhonePC/2in1TabletTVWearable

key(keyGenerator: (item: T, index: number) => string)

键值生成函数。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyGenerator | (item: T, index: number) => string | 是 | 键值生成函数。  item：arr数组中的数据项，可选。  index：arr数组中的数据项索引，可选。 |

**示例：**

```
1. // arr是Array<string>类型的数组，为每个数据创建一个Text组件
2. // 并将字符串的值作为其键值
3. Repeat<string>(this.arr)
4. .each((obj: RepeatItem<string>) => { Text(obj.item) })
5. .key((obj: string) => obj)
```

### virtualScroll

PhonePC/2in1TabletTVWearable

virtualScroll(virtualScrollOptions?: VirtualScrollOptions)

Repeat开启虚拟滚动。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| virtualScrollOptions | [VirtualScrollOptions](ts-rendering-control-repeat.md#virtualscrolloptions) | 否 | 虚拟滚动配置项。  默认值为undefined。 |

**示例：**

```
1. // arr是Array<string>类型的数组，为每个数据创建一个Text组件
2. // 在List容器组件中使用Repeat，并打开virtualScroll
3. List() {
4. Repeat<string>(this.arr)
5. .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
6. .virtualScroll()
7. }
```

### template

PhonePC/2in1TabletTVWearable

template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions)

由template type渲染对应的template子组件。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 当前模板类型。 |
| itemBuilder | [RepeatItemBuilder](ts-rendering-control-repeat.md#repeatitembuildert)<T> | 是 | 组件生成函数。 |
| templateOptions | [TemplateOptions](ts-rendering-control-repeat.md#templateoptions对象说明) | 否 | 当前模板配置项。  默认值为undefined。 |

**示例：**

```
1. // arr是Array<string>类型的数组
2. // 在List容器组件中使用Repeat，并打开virtualScroll
3. // 创建模板temp，该模板为数据创建Text组件
4. List() {
5. Repeat<string>(this.arr)
6. .each((obj: RepeatItem<string>) => {})
7. .virtualScroll()
8. .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
9. }
```

### templateId

PhonePC/2in1TabletTVWearable

templateId(typedFunc: TemplateTypedFunc<T>)

为当前数据项分配template type。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedFunc | [TemplateTypedFunc](ts-rendering-control-repeat.md#templatetypedfunct)<T> | 是 | 生成当前数据项对应的template type。 |

**示例：**

```
1. // arr是Array<string>类型的数组
2. // 在List容器组件中使用Repeat，并打开virtualScroll
3. // 创建模板temp，该模板为数据创建Text组件
4. // 所有数据项都使用temp模板
5. List() {
6. Repeat<string>(this.arr)
7. .each((obj: RepeatItem<string>) => {})
8. .virtualScroll()
9. .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
10. .templateId((item: string, index: number) => { return 'temp' })
11. }
```

## RepeatArray<T>18+

PhonePC/2in1TabletTVWearable

type RepeatArray<T> = Array<T> | ReadonlyArray<T> | Readonly<Array<T>>

Repeat数据源参数联合类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Array<T> | 常规数组类型。 |
| ReadonlyArray<T> | 只读数组类型，不允许数组对象变更。 |
| Readonly<Array<T>> | 只读数组类型，不允许数组对象变更。 |

## RepeatItem<T>

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| item | T | 否 | 否 | arr中每一个数据项。T为开发者传入的数据类型。 |
| index | number | 否 | 否 | 当前数据项对应的索引。 |

## VirtualScrollOptions

PhonePC/2in1TabletTVWearable

配置懒加载模式下期望加载的数据项总数、复用能力、数据精准懒加载能力。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| totalCount | number | 否 | 是 | 期望加载的数据项总数，可以不等于数据源长度（实际传入Repeat的数组的长度）。  取值范围：自然数。  totalCount缺省或超出取值范围时，totalCount取值为数据源长度，列表正常滚动。  totalCount = 0时，不加载数据。  0 < totalCount <= 数据源长度时，界面中只渲染区间[0, totalCount - 1]范围内的数据。  totalCount > 数据源长度时，Repeat将渲染区间[0, totalCount - 1]范围内的数据，容器组件滚动条样式根据totalCount值变化。在容器组件滚动过程中，应用需要保证在列表即将滑动到数据源末尾时请求后续数据。开发者需要对数据请求的错误场景（如网络延迟）进行保护操作，直到数据源全部加载完成，否则列表滑动过程中会出现滚动效果异常。建议配合使用[onLazyLoading](ts-rendering-control-repeat.md#onlazyloading19)实现数据懒加载。  除totalCount属性外，开发者也可以通过[onTotalCount](ts-rendering-control-repeat.md#ontotalcount19)方法设置自定义方法，计算期望加载的数据项总数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| reusable18+ | boolean | 否 | 是 | 是否开启复用功能。  true：开启复用。  false：关闭复用。  默认值：true  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

**示例**

```
1. // arr是Array<string>类型的数组，在List容器组件中使用Repeat，并打开virtualScroll
2. // 将加载的数据项总数设为数据源的长度，并开启复用功能
3. List() {
4. Repeat<string>(this.arr)
5. .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
6. .virtualScroll( { totalCount: this.arr.length, reusable: true } )
7. }
```

### onTotalCount19+

PhonePC/2in1TabletTVWearable

onTotalCount?(): number

可选方法，计算期望加载的数据项总数。需要开发者给定计算方法，其返回值可以不等于数据源长度（实际传入Repeat的数组的长度）。

[totalCount](ts-rendering-control-repeat.md#virtualscrolloptions)和onTotalCount()的返回值都表示期望加载的数据项总数。开发者可直接设置totalCount属性，给出期望加载的数据项总数，也可以通过onTotalCount()设定自定义方法，计算期望加载的数据项总数。totalCount与onTotalCount()最多设置一个。如果均未设置，则采用默认值：数据源长度；如果同时设置，则忽略totalCount。

onTotalCount()不同返回值的数据加载处理规则与totalCount一致，具体如下：

* onTotalCount()返回值 = 0时，不加载数据。
* 0 < onTotalCount()返回值 <= 数据源长度时，只加载区间[0, onTotalCount()返回值 - 1]索引范围内的数据。
* onTotalCount()返回值 > 数据源长度时，代表Repeat期望加载区间[0, onTotalCount()返回值 - 1]索引范围内的数据，容器组件滚动条样式根据totalCount值变化。在容器组件滚动过程中，应用需要保证在列表即将滑动到数据源末尾时请求后续数据。开发者需要对数据请求的错误场景（如网络延迟）进行保护操作，直到数据源全部加载完成，否则列表滑动过程中会出现滚动效果异常。建议配合使用[onLazyLoading](ts-rendering-control-repeat.md#onlazyloading19)实现数据懒加载。
* onTotalCount()返回值是非自然数时，由数据源长度取代其返回值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 期望加载的数据项总数。  取值范围：自然数。 |

### onLazyLoading19+

PhonePC/2in1TabletTVWearable

onLazyLoading?(index: number): void

可选方法，懒加载指定索引的数据。需要开发者给定数据加载方法。

onLazyLoading方法需在懒加载场景下使用。开发者可设置自定义方法，用于向指定的数据源index中写入数据。以下为onLazyLoading的处理规则：

* Repeat读取数据源中index对应的数据之前，会先检查index处是否存在数据。
* 如果不存在数据，但开发者提供了onLazyLoading方法，Repeat将调用此方法。
* 在onLazyLoading方法中，开发者需要向Repeat指定的index中写入数据，方式如下：arr[index] = ...，其中arr表示传入Repeat的数组。不允许使用除[]以外的数组操作，且不允许写入指定index以外的元素，否则系统将抛出异常。
* onLazyLoading方法执行完成后，若指定index中仍无数据，将导致当前index和后续索引对应的组件无法加载。
* 精准懒加载能力为可选配置项。当onLazyLoading缺省，并且totalCount或onTotalCount的返回值大于数据源长度时，Repeat不负责列表滚动到底部的渲染效果。
* onLazyLoading方法中应避免高耗时操作。若数据加载耗时较长，建议先在onLazyLoading方法中为此数据创建占位符，再创建异步任务加载数据。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 需要加载的数据项对应的索引。  取值范围：自然数。 |

**示例**

```
1. // 假设数据项总数为100，首屏渲染需3项数据
2. // 初始数组提供前3项数据（arr = ['No.0', 'No.1', 'No.2']），并开启数据懒加载功能
3. List() {
4. Repeat<string>(this.arr)
5. .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
6. .virtualScroll({
7. onTotalCount: () => { return 100; },
8. onLazyLoading: (index: number) => { this.arr[index] = `No.${index}`; }
9. })
10. }
```

## RepeatItemBuilder<T>

PhonePC/2in1TabletTVWearable

type RepeatItemBuilder<T> = (repeatItem: RepeatItem<T>) => void

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| repeatItem | [RepeatItem](ts-rendering-control-repeat.md#repeatitemt)<T> | 否 | 将item和index结合到一起的一个状态变量。  缺省时默认忽略该参数，请勿在闭包函数的实现中使用该参数，否则会编译报错。 |

## TemplateOptions对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cachedCount | number | 否 | 是 | 当前template的缓存池中可缓存子组件节点的最大数量。取值范围是[0, +∞)，默认值为容器组件显示区域节点与预加载区域节点的个数之和。当容器组件显示区域节点与预加载节点的个数之和增多时（滑动过程中，只有部分高度的子组件在显示区域），cachedCount也会对应增长。需要注意cachedCount数量不会减少。 |

当cachedCount值被设置为当前template在容器组件显示区域的最大节点数量时，Repeat会做到最大程度的复用。当容器组件显示区域内没有当前template的节点时，缓存列表不会释放，同时应用内存增大。开发者需要根据具体情况自行把控，推荐cachedCount值设置为容器组件显示区域内节点个数。需要注意，不建议设置cachedCount小于2，这会导致在快速滑动场景下频繁创建新的节点，从而造成性能劣化。

说明

滚动容器组件属性.cachedCount()和Repeat组件属性.template()的参数cachedCount都是为了平衡性能和内存，但是含义是不同的。

* 滚动容器组件.cachedCount()：是指在容器组件显示区域外预加载区域的大小，该区域内子组件节点位于组件树上。滚动容器组件会额外渲染这些预加载区域的节点，从而提高列表滑动性能。
* .template()中的cachedCount: 指Repeat每个template的缓存池大小，当渲染新的子组件时，Repeat先判断对应template缓存池中是否有可用节点，有则复用，没有则创建新节点。

**示例：**

```
1. // arr是Array<string>类型的数组，在List容器组件中使用Repeat，并打开virtualScroll
2. // 创建模板temp，该模板为数据创建Text组件，所有数据项都使用temp模板
3. // 将temp模板的最大缓存节点数量设为2
4. List() {
5. Repeat<string>(this.arr)
6. .each((obj: RepeatItem<string>) => {})
7. .virtualScroll()
8. .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }}, { cachedCount: 2 })
9. .templateId((item: string, index: number) => { return 'temp' })
10. }
```

## TemplateTypedFunc<T>

PhonePC/2in1TabletTVWearable

type TemplateTypedFunc<T> = (item: T, index: number) => string

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | T | 否 | arr中每一个数据项。T为开发者传入的数据类型。  缺省时默认忽略该参数，请勿在闭包函数的实现中使用该参数，否则会编译报错。 |
| index | number | 否 | 当前数据项对应的索引。  缺省时默认忽略该参数，请勿在闭包函数的实现中使用该参数，否则会编译报错。 |
