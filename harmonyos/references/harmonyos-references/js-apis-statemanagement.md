---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement
title: @ohos.arkui.StateManagement (状态管理)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.StateManagement (状态管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3e0ae19f0d3a2c507d0aa9937c7c758f0ae8bb031bce9b53b06d3c137bfd19c
---

状态管理模块提供了应用程序的数据存储能力、持久化数据管理能力、UIAbility数据存储能力和应用程序需要的环境状态、工具。

说明

本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

本文中T和S的含义如下：

| 类型 | 说明 |
| --- | --- |
| T | Class，number，boolean，string和这些类型的数组形式。 |
| S | number，boolean，string。 |

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AppStorageV2, PersistenceV2, UIUtils } from '@kit.ArkUI';
```

## AppStorageV2

PhonePC/2in1TabletTVWearable

AppStorageV2具体UI使用说明，详见[AppStorageV2(应用全局的UI状态存储)](../harmonyos-guides/arkts-new-appstoragev2.md)。

### connect

PhonePC/2in1TabletTVWearable

static connect<T extends object>(

type: TypeConstructorWithArgs<T>,

keyOrDefaultCreator?: string | StorageDefaultCreator<T>,

defaultCreator?: StorageDefaultCreator<T>

): T | undefined

将键值对数据储存在应用内存中。如果给定的key已经存在于[AppStorageV2](../harmonyos-guides/arkts-new-appstoragev2.md)中，返回对应的值；否则，通过获取默认值的构造器构造默认值，并返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TypeConstructorWithArgs<T>](js-apis-statemanagement.md#typeconstructorwithargst) | 是 | 指定的类型，若未指定key，则使用type的name作为key。 |
| keyOrDefaultCreator | string | [StorageDefaultCreator<T>](js-apis-statemanagement.md#storagedefaultcreatort) | 否 | 指定的key，或者是获取默认值的构造器。默认值为undefined。 |
| defaultCreator | StorageDefaultCreator<T> | 否 | 获取默认值的构造器。默认值为undefined。 |

说明

1、若未指定key，使用第二个参数作为默认构造器；否则使用第三个参数作为默认构造器（第二个参数非法也使用第三个参数作为默认构造器）。

2、确保数据已经存储在AppStorageV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。

3、同一个key，connect不同类型的数据会导致应用异常，应用需要确保类型匹配。

4、key建议使用有意义的值，长度不超过255，使用非法字符或空字符的行为是未定义的。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | 创建或获取AppStorageV2数据成功时，返回数据；否则返回undefined。 |

**示例：**

```
1. import { AppStorageV2 } from '@kit.ArkUI';

3. @ObservedV2
4. class SampleClass {
5. @Trace p: number = 0;
6. }

8. // 将key为SampleClass、value为new SampleClass()对象的键值对存储到内存中，并赋值给as1
9. const as1: SampleClass | undefined = AppStorageV2.connect(SampleClass, () => new SampleClass());

11. // 将key为key_as2、value为new SampleClass()对象的键值对存储到内存中，并赋值给as2
12. const as2: SampleClass = AppStorageV2.connect(SampleClass, 'key_as2', () => new SampleClass())!;

14. // key为SampleClass已经在AppStorageV2中，将key为SampleClass的值返回给as3
15. const as3: SampleClass = AppStorageV2.connect(SampleClass) as SampleClass;
```

### remove

PhonePC/2in1TabletTVWearable

static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void

将指定的键值对数据从[AppStorageV2](../harmonyos-guides/arkts-new-appstoragev2.md)里面删除。如果指定的键值不存在于AppStorageV2中，将删除失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyOrType | string | [TypeConstructorWithArgs](js-apis-statemanagement.md#typeconstructorwithargst)<T> | 是 | 需要删除的key；如果指定的是type类型，删除的key为type的name。 |

说明

删除AppStorageV2中不存在的key会报警告。

**示例：**

```
1. // 假设AppStorageV2中存在key为key_as2的键，从AppStorageV2中删除该键值对数据
2. AppStorageV2.remove('key_as2');

4. // 假设AppStorageV2中存在key为SampleClass的键，从AppStorageV2中删除该键值对数据
5. AppStorageV2.remove(SampleClass);

7. // 假设AppStorageV2中不存在key为key_as1的键，报警告
8. AppStorageV2.remove('key_as1');
```

### keys

PhonePC/2in1TabletTVWearable

static keys(): Array<string>

获取[AppStorageV2](../harmonyos-guides/arkts-new-appstoragev2.md)中的所有key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 所有AppStorageV2中的key。 |

说明

key在Array中的顺序是无序的，与key插入到AppStorageV2中的顺序无关。

**示例：**

```
1. // 假设AppStorageV2中存在两个key（key_as1、key_as2），返回[key_as1、key_as2]赋值给keys
2. const keys: Array<string> = AppStorageV2.keys();
```

## PersistenceV2

PhonePC/2in1TabletTVWearable

继承自[AppStorageV2](js-apis-statemanagement.md#appstoragev2)，PersistenceV2具体UI使用说明，详见[PersistenceV2(持久化存储UI状态)](../harmonyos-guides/arkts-new-persistencev2.md)。

### globalConnect18+

PhonePC/2in1TabletTVWearable

static globalConnect<T extends object>(type: ConnectOptions<T>): T | undefined

将键值对数据储存在应用磁盘中。如果给定的key已经存在于[PersistenceV2](../harmonyos-guides/arkts-new-persistencev2.md)中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。如果globalConnect的是[@ObservedV2](../harmonyos-guides/arkts-new-observedv2-and-trace.md)对象，该对象[@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)属性的变化，会触发整个关联对象的自动刷新；非@Trace属性变化则不会，如有必要，可调用[PersistenceV2.save](js-apis-statemanagement.md#save)接口手动存储。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ConnectOptions<T>](js-apis-statemanagement.md#connectoptions18) | 是 | 传入的connect参数，详细说明见ConnectOptions参数说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | 创建或获取数据成功时，返回数据；否则返回undefined。 |

说明

1、若未指定key，使用第二个参数作为默认构造器；否则使用第三个参数作为默认构造器（第二个参数非法也使用第三个参数作为默认构造器）。

2、确保数据已经存储在PersistenceV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。

3、同一个key，globalConnect不同类型的数据会导致应用异常，应用需要确保类型匹配。

4、key建议使用有意义的值，可由字母、数字、下划线组成，长度不超过255，使用非法字符或空字符的行为是未定义的。

5、关联[@Observed](../harmonyos-guides/arkts-observed-and-objectlink.md)对象时，因为该类型的name属性未定义，需要指定key或者自定义name属性。

6、数据的存储路径为应用级别，不同module使用相同的key和相同的加密分区进行globalConnect，存储的数据副本应用仅有一份。

7、globalConnect使用同一个key但设置了不同的加密级别，数据为第一个使用globalConnect的加密级别，并且PersistenceV2中的数据也会存入最先使用key的加密级别。

8、connect和globalConnect不建议混用，因为数据副本路径不同，如果混用，则key不可以一样，否则会crash。

9、EL5加密要想生效，需要开发者在module.json中配置字段ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA，使用说明见[声明权限](../harmonyos-guides/declare-permissions.md)。

**示例：**

仅供开发者了解globalConnect用法，完整使用需开发者自己写出@Entry组件。

```
1. import { PersistenceV2, Type } from '@kit.ArkUI';
2. import { contextConstant } from '@kit.AbilityKit';

4. @ObservedV2
5. class SampleChild {
6. @Trace childId: number = 0;
7. groupId: number = 1;
8. }

10. @ObservedV2
11. export class Sample {
12. // 对于复杂对象需要@Type修饰，确保序列化成功
13. @Type(SampleChild)
14. @Trace father: SampleChild = new SampleChild();
15. }

17. // key不传入尝试用为type的name作为key，加密参数不传入默认加密等级为EL2
18. const p: Sample = PersistenceV2.globalConnect({ type: Sample, defaultCreator: () => new Sample() })!;

20. // 使用key:global1连接，传入加密等级为EL1
21. const p1: Sample = PersistenceV2.globalConnect({
22. type: Sample,
23. key: 'global1',
24. defaultCreator: () => new Sample(),
25. areaMode: contextConstant.AreaMode.EL1
26. })!;

28. // 使用key:global2连接，使用构造函数形式，加密参数不传入默认加密等级为EL2
29. const p2: Sample = PersistenceV2.globalConnect({ type: Sample, key: 'global2', defaultCreator: () => new Sample() })!;

31. // 使用key:global3连接，直接写加密数值，范围只能在0-4，否则运行会crash,例如加密设置为EL3
32. const p3: Sample = PersistenceV2.globalConnect({
33. type: Sample,
34. key: 'global3',
35. defaultCreator: () => new Sample(),
36. areaMode: 3
37. })!;
```

### globalConnect23+

PhonePC/2in1TabletTVWearable

static globalConnect<T extends CollectionType<S>, S extends object>(

type: ConnectOptionsCollections<T, S> | ConnectOptions<T>

): T | undefined

将键值对数据储存在应用磁盘中。支持集合类型[Array，Map，Set，Date，collections.Array, collections.Map, collections.Set类型的持久化](../harmonyos-guides/arkts-new-persistencev2.md#globalconnect支持集合的类型)。注意在持久化Array<ClassA>类型的数据时，需要调用[makeObserved](js-apis-statemanagement.md#makeobserved)使返回的对象被观察到。不支持多个嵌套集合，例如不支持Array<Array<ClassA>>的持久化。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ConnectOptionsCollections<T, S>](js-apis-statemanagement.md#connectoptionscollections23)| [ConnectOptions<T>](js-apis-statemanagement.md#connectoptions18) | 是 | 传入的globalConnect参数，详细说明见ConnectOptions和ConnectOptionsCollections参数说明。  当开发者在ConnectOptionsCollections中提供默认defaultSubCreator时，则需要同时提供默认创建器defaultCreator，如果不提供，会导致持久化失败。且集合项类型S必须与defaultSubCreator的返回类型相同。如果返回类型不一致，编译会报错。 |

当开发者在globalConnect中使用defaultSubCreator选项时，必须要提供defaultCreator。且defaultSubCreator函数的返回类型必须与defaultCreator返回的集合项类型相同。

当globalConnect持久化Array<ClassA>类型的数据时，开发者需要使用defaultSubCreator选项去告诉状态管理框架创建ClassA类的一个实例。如下是globalConnect持久化Array<ClassA>类型的数据的示例：

```
1. class ClassA {
2. propA: number;
3. // ...
4. }

6. @ComponentV2
7. struct Page1 {
8. // 顶层持久化数据类型为Array<ClassA>
9. @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
10. type: Array<ClassA>,
11. defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
12. // 添加defaultSubCreator，通知状态管理框架如何创建ClassA对象
13. // 另外持久化后的数据需要加上makeObserved，否则会持久化失败
14. defaultSubCreator: () => UIUtils.makeObserved(new ClassA())
15. })!
16. // ...
17. }
```

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | 创建或获取数据成功时，返回数据；否则返回undefined。 |

**示例：**

如下展示globalConnect持久化Map类型的示例代码：

```
1. import { PersistenceV2, ConnectOptions } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Page1 {
6. // globalConnect支持持久化Map类型的数据
7. @Local map: Map<number, number> = PersistenceV2.globalConnect({
8. type: Map<number, number>, defaultCreator: () => new Map<number, number>()
9. })!
10. output: string[] = [];

12. // 启动应用，第一次进入，展示restored Map.size=0, map.get(0)=undefined, map.get(1)=undefined, map.get(2)=undefined
13. // 关闭应用，第二次进入，展示restored Map.size=1, map.get(0)=0, map.get(1)=undefined, map.get(2)=undefined
14. // 关闭应用，第三次进入，展示restored Map.size=2, map.get(0)=0, map.get(1)=1, map.get(2)=undefined
15. // 关闭应用，第四次进入，展示restored Map.size=3, map.get(0)=0, map.get(1)=1, map.get(2)=2
16. aboutToAppear(): void {
17. const restoredMapSize = this.map.size;
18. this.output.push(`restored Map.size=${restoredMapSize}, map.get(0)=${this.map.get(0)}, map.get(1)=${this.map.get(1)}, map.get(2)=${this.map.get(2)}`);
19. this.map.set(restoredMapSize, restoredMapSize);
20. // 需要手工持久化
21. PersistenceV2.save('Map');
22. }

24. build() {
25. Column() {
26. Row() {
27. Text(this.output.join('\n\n'))
28. .fontSize(24)
29. }
30. }
31. .width('100%')
32. }
33. }
```

### save

PhonePC/2in1TabletTVWearable

static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void

将指定的键值对数据持久化一次。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyOrType | string | [TypeConstructorWithArgs<T>](js-apis-statemanagement.md#typeconstructorwithargst) | 是 | 需要持久化的key；如果指定的是type类型，持久化的key为type的name。 |

说明

由于非[@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)的数据改变不会触发[PersistenceV2](../harmonyos-guides/arkts-new-persistencev2.md)的自动持久化，如有必要，可调用该接口持久化对应key的数据。

手动持久化当前内存中不处于connect状态的key是无意义的。

**示例：**

```
1. @ObservedV2
2. class SampleClass {
3. @Trace p: number = 0;
4. }

6. // 假设PersistenceV2中存在key为key_as2的键，持久化该键值对数据
7. PersistenceV2.save('key_as2');

9. // 假设PersistenceV2中存在key为SampleClass的键，持久化该键值对数据
10. PersistenceV2.save(SampleClass);

12. // 假设PersistenceV2中不存在key为key_as1的键，无意义的操作
13. PersistenceV2.save('key_as1');
```

### notifyOnError

PhonePC/2in1TabletTVWearable

static notifyOnError(callback: PersistenceErrorCallback | undefined): void

在持久化失败时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PersistenceErrorCallback](js-apis-statemanagement.md#persistenceerrorcallback) | undefined | 是 | 持久化失败时调用。 |

**示例：**

```
1. // 持久化失败时调用
2. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
3. console.error(`error key: ${key}, reason: ${reason}, message: ${msg}`);
4. });
```

## ConnectOptions18+

PhonePC/2in1TabletTVWearable

globalConnect参数类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TypeConstructorWithArgs<T>](js-apis-statemanagement.md#typeconstructorwithargst) | 否 | 否 | 指定的类型。 |
| key | string | 否 | 是 | 传入的key，不传则使用type的名字作为key。 |
| defaultCreator | [StorageDefaultCreator<T>](js-apis-statemanagement.md#storagedefaultcreatort) | 否 | 是 | 默认数据的构造器，建议传递，如果globalConnect是第一次连接key，不传会报错。 |
| areaMode | [contextConstant.AreaMode](js-apis-app-ability-contextconstant.md#areamode) | 否 | 是 | 加密级别：EL1-EL5，详见[加密级别](../harmonyos-guides/application-context-stage.md#获取和修改加密分区)，对应数值：0-4，不传时默认为EL2，不同加密级别对应不同的加密分区，即不同的存储路径，传入的加密等级数值不在0-4会直接运行crash。 |

## ConnectOptionsCollections23+

PhonePC/2in1TabletTVWearable

[globalConnect](js-apis-statemanagement.md#globalconnect23)接口参数类型，ConnectOptionsCollections继承自[ConnectOptions](js-apis-statemanagement.md#connectoptions18)。当开发者需要持久化容器类型数据（如Array<S>）时，需要使用ConnectOptionsCollections入参。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultCreator | [StorageDefaultCreator<T>](js-apis-statemanagement.md#storagedefaultcreatort) | 否 | 是 | 用于持久化容器类型数据，当提供默认defaultSubCreator时，则需要同时提供默认创建器defaultCreator，不提供默认创建器，会导致无法持久化容器类型数据。集合项类型S必须与defaultSubCreator的返回类型相同。如果提供defaultSubCreator，没有提供defaultCreator，会导致持久化失败。 |
| defaultSubCreator | [StorageDefaultCreator<S>](js-apis-statemanagement.md#storagedefaultcreatort) | 否 | 是 | 使用该集合项默认构造函数，用于持久化容器类数据。如果defaultSubCreator返回的是undefined或null，会导致持久化失败。 当持久化用户自定义class类集合（如Array<ClassA>）时，defaultCreator中的泛型类型T为Array<ClassA>，则defaultSubCreator中的泛型类型S为ClassA。 |

如下展示StorageDefaultCreator<T>和StorageDefaultCreator<S>示例：

**示例：**

```
1. class ClassA {
2. propA: number;
3. // ...
4. }

6. @ComponentV2
7. struct Page {
8. // StorageDefaultCreator<T>默认创建器为`() => UIUtils.makeObserved(new Array<ClassA>())`, 其中`T`的类型是指`Array<ClassA>`
9. // StorageDefaultCreator<S> 默认创建器为`() =>UIUtils.makeObserved(new ClassA())`，其中，`S`的类型是指`ClassA`
10. @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
11. type: Array<ClassA>,
12. defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
13. // 添加defaultSubCreator，通知状态管理框架如何创建ClassA对象
14. // 另外持久化后的数据需要加上makeObserved，否则会持久化失败
15. defaultSubCreator: () => UIUtils.makeObserved(new ClassA())
16. })!
17. // ...
18. }
```

当StorageDefaultCreator<S>返回值为undefined或null时，持久化会失败。当StorageDefaultCreator<S>直接设置为undefined或null时,状态管理框架会按照原始的类型（如Object类型）进行持久化，但是会丢失class对象中的方法。在如下示例中，StorageDefaultCreator<S>直接被设置为undefined或null时，持久化过程中ClassA对象中的report方法将被丢失。

```
1. import { PersistenceV2, UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @ObservedV2
5. class ClassA {
6. @Trace public propA: string = '';
7. @Trace public propB: string = '';

9. public report(): string {
10. return `${this.propA} - ${this.propB}`;
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct Comp {
17. // 持久化顶层数据类型为`Array<ClassA>`的数据。
18. @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
19. type: Array<ClassA>,
20. defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
21. // defaultSubCreator的返回的值被设置为`undefined`或`null` (defaultSubCreator: () => undefined)，持久化失败。
22. // defaultSubCreator被直接设置为`undefined`或`null` (defaultSubCreator: undefined))，持久化会丢失`ClassA`中的方法。
23. defaultSubCreator: undefined
24. })!;

26. aboutToAppear(): void {
27. if (this.arr.length) {
28. // 步骤3：再次进入应用，持久化过程中丢失`ClassA中`的方法，当调用`ClassA`对象中的`report`方法，会报`undefined is not callable`的错误。
29. hilog.info(0xFF00, 'testTag', '%{public}s', this.arr[0].report());
30. }
31. }
32. build() {
33. Column() {
34. Repeat(this.arr)
35. .each(ri => {
36. Row() {
37. Text(`propA '${ri.item.propA}'`)
38. Text(`propB '${ri.item.propB}'`)
39. Text(`report?.() '${ri.item.report?.()}'`)
40. }
41. })
42. // 步骤1：点击'add item'，显示`propA 'a' propB 'b'report?.'a' - 'b'`。
43. // 步骤2：关闭应用。
44. Button('add item')
45. .onClick(() => {
46. let temp: ClassA = new ClassA();
47. temp.propA = 'a';
48. temp.propB = 'b';
49. this.arr.push(temp);
50. })
51. }
52. }
53. }
```

## CollectionType23+

PhonePC/2in1TabletTVWearable

type CollectionType<S> = Array<S> | Map<string | number, S> |

Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>

globalConnect的入参泛型，用于定义globalConnect支持的持久化集合数据类型。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| Array<S> | 表示值类型为Array类型。 |
| Map<string | number, S> | 表示值类型为Map类型。 |
| Set<S> | 表示值类型为Set类型。 |
| [collections.Array](arkts-apis-arkts-collections-array.md)<S> | 表示值类型为collections.Array类型。 |
| [collections.Map](arkts-apis-arkts-collections-map.md)<string | number, S> | 表示值类型为collections.Map类型。 |
| [collections.Set](arkts-apis-arkts-collections-set.md)<S> | 表示值类型为collections.Set类型。 |

## ObservedResult23+

PhonePC/2in1TabletTVWearable

对象是否可被观察的结果。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isObserved | boolean | 否 | 否 | 对象是否可被观察。  true：表示是可被观察对象。  false：表示不是可被观察对象。 |
| reason | string | 否 | 否 | 对象是否可被观察的原因。  不可被观察原因：对象本身是不可被观察的。  可被观察原因或使用场景：  1. V1对象被[@Observed](../harmonyos-guides/arkts-observed-and-objectlink.md)装饰器装饰或对象是被[makeV1Observed](js-apis-statemanagement.md#makev1observed19)方法转换的。  2. V1对象被[@Observed](../harmonyos-guides/arkts-observed-and-objectlink.md)装饰器装饰或对象是被[makeV1Observed](js-apis-statemanagement.md#makev1observed19)方法转换的，但对象没有被UI组件使用。  3. V1对象被[enableV2Compatibility](js-apis-statemanagement.md#enablev2compatibility19)方法转换后传入V2组件。  4. V1对象被[enableV2Compatibility](js-apis-statemanagement.md#enablev2compatibility19)方法转换后传入V2组件，但没有被V2组件使用。  5. V2对象是被[@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)装饰的。  6. V2对象是被[makeObserved](js-apis-statemanagement.md#makeobserved)方法转换的。  7. V2对象属于Array/Map/Set/Date类型。  8. V2对象是被[@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)装饰的，但对象没有被UI组件使用。  9. V2对象是被[makeObserved](js-apis-statemanagement.md#makeobserved)方法转换的，但没有被UI组件使用。  10. V2对象属于Array/Map/Set/Date类型，但没有被UI组件使用。 |
| decoratorInfo | Array<[DecoratorInfo](js-apis-statemanagement.md#decoratorinfo23)> | 否 | 否 | 对象可被观察时，数组中内容为对象关联的装饰器和组件信息。对象不可被观察时，此数组为空。 |

## DecoratorInfo23+

PhonePC/2in1TabletTVWearable

可被观察对象关联的装饰器和组件信息。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| decoratorName | string | 否 | 否 | 当对象是V1对象时，值是对象关联的装饰器名称。  当V1对象使用[@Track](../harmonyos-guides/arkts-track.md)时，值为：'@Track'。  当V2对象使用[@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)时，值为：'@Trace'。  当V2对象使用[makeObserved](js-apis-statemanagement.md#makeobserved)时，值为：'MakeObserved'。  当V2对象使用[enableV2Compatibility](js-apis-statemanagement.md#enablev2compatibility19)时，值为：'EnableV2Compatible'。  当V2对象使用built-in类型数据时，值为：'ProxyObservedV2'。 |
| stateVariableName | string | 否 | 否 | 被装饰器装饰的属性名称。 |
| owningComponentOrClassName | string | 否 | 否 | V1对象返回被使用的组件名称。  V1对象有属性使用[@Track](../harmonyos-guides/arkts-track.md)装饰器时返回对象名称。  V2对象返回对象名称。 |
| owningComponentId | number | 否 | 否 | V1对象返回被使用的组件id。  **V1对象有属性使用[@Track](../harmonyos-guides/arkts-track.md)装饰器时和V2对象返回的是对象名称，无组件id，返回-1。** |
| dependentInfo | Array<[ElementInfo](js-apis-statemanagement.md#elementinfo23)> | 否 | 否 | 使用该可观察对象的组件信息。若对象没有用在任何UI上，则返回空数组。 |

## ElementInfo23+

PhonePC/2in1TabletTVWearable

可被观察对象关联的组件信息，包含系统组件和自定义组件。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| elementName | string | 否 | 否 | 组件的名称。 |
| elementId | number | 否 | 否 | 组件的ID。 |

## UIUtils

PhonePC/2in1TabletTVWearable

UIUtils提供一些方法，用于处理状态管理相关的数据转换。

### getTarget

PhonePC/2in1TabletTVWearable

static getTarget<T extends object>(source: T): T

从状态管理框架包裹的代理对象中获取原始对象。详见[getTarget接口：获取状态管理框架代理前的原始对象](../harmonyos-guides/arkts-new-gettarget.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | T | 是 | 数据源对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 数据源对象去除状态管理框架所加代理后的原始对象。 |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. class NonObservedClass {
4. name: string = 'Tom';
5. }

7. let nonObservedClass: NonObservedClass = new NonObservedClass();

9. @Entry
10. @Component
11. struct Index {
12. @State someClass: NonObservedClass = nonObservedClass;

14. build() {
15. Column() {
16. Text(`this.someClass === nonObservedClass: ${this.someClass === nonObservedClass}`) // false
17. Text(`UIUtils.getTarget(this.someClass) === nonObservedClass: ${UIUtils.getTarget(this.someClass) ===
18. nonObservedClass}`) // true
19. }
20. }
21. }
```

### getLifecycle23+

PhonePC/2in1TabletTVWearable

static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle

getLifecycle用于获取[自定义组件的生命周期](ts-custom-component-new-lifecycle.md)实例。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customComponent | T | 是 | 自定义组件实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CustomComponentLifecycle](ts-custom-component-new-lifecycle.md#customcomponentlifecycle) | 自定义组件的生命周期实例。 |

**示例：**

```
1. import { UIUtils, ComponentAppear } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State lifecycleState: number = -1;

8. @ComponentAppear
9. myAppear() {
10. // UIUtils.getLifecycle获得自定义组件的生命周期实例，getCurrentState查询自定义组件当前生命周期。
11. // 预期查询到的生命周期为CustomComponentLifecycleState.APPEARED = 1。
12. this.lifecycleState = UIUtils.getLifecycle(this).getCurrentState();
13. }

15. build() {
16. Text(`${this.lifecycleState}`)
17. }
18. }
```

### canBeObserved23+

PhonePC/2in1TabletTVWearable

static canBeObserved<T extends object>(source: T): ObservedResult

判断数据对象是否为可观察对象，并返回观察结果。详见[canBeObserved接口：判断对象是否为可被观察对象](../harmonyos-guides/arkts-new-canbeobserved.md)。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | T | 是 | 输入一个数据对象，判断其是否可被观察。支持Array、Map、Set和Date类型数据。  具体使用规则，详见[canBeObserved接口：判断对象是否为可被观察对象](../harmonyos-guides/arkts-new-canbeobserved.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ObservedResult](js-apis-statemanagement.md#observedresult23) | 返回对象是否可被观察的结果。 |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { DecoratorInfo, ElementInfo } from '@ohos.arkui.StateManagement';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = 'CanBeObserved';

7. class Student {
8. public name?: string;

10. constructor(name?: string) {
11. this.name = name ?? '';
12. }

14. // 在对象中提供判断该对象是否为可被观察对象的方法
15. test(): void {
16. const result = UIUtils.canBeObserved(this);
17. // 对象是否可被观察
18. const isObserved = result.isObserved;
19. hilog.info(0x00, TAG, `isObserved: ${JSON.stringify(isObserved)}`);
20. // 对象是否可被观察的原因
21. const reason = result.reason;
22. hilog.info(0x00, TAG, `reason: ${reason}`);
23. // 对象可被观察时，对象关联的装饰器信息
24. const decoratorInfoArr = result.decoratorInfo;
25. decoratorInfoArr.forEach((decorator: DecoratorInfo) => {
26. // 装饰器名称
27. const decoratorName = decorator.decoratorName;
28. hilog.info(0x00, TAG, `decoratorName: ${decoratorName}`);
29. // 装饰器装饰的属性名称
30. const stateVariableName = decorator.stateVariableName;
31. hilog.info(0x00, TAG, `stateVariableName: ${stateVariableName}`);
32. // 装饰器所在的组件名称
33. const owningName = decorator.owningComponentOrClassName;
34. hilog.info(0x00, TAG, `owningComponentOrClassName: ${owningName}`);
35. // 装饰器所在的组件id
36. const owningId = decorator.owningComponentId;
37. hilog.info(0x00, TAG, `owningComponentId: ${owningId}`);
38. // 装饰器关联的组件信息
39. const dependentInfo = decorator.dependentInfo;
40. dependentInfo.forEach((elementInfo: ElementInfo) => {
41. // 装饰器关联的组件名称
42. const eleName = elementInfo.elementName;
43. hilog.info(0x00, TAG, `elementName: ${eleName}`);
44. // 装饰器关联的组件id
45. const eleId = elementInfo.elementId;
46. hilog.info(0x00, TAG, `elementId: ${eleId}`);
47. })
48. })
49. }
50. }

52. @Entry
53. @Component
54. struct Index {
55. @State student: Student = new Student('LiMei');

57. build() {
58. Column({ space: 20 }) {
59. Classroom({ student: this.student })
60. Home({ student: this.student })
61. Button('test')
62. .onClick(() => {
63. // 开发者可以在任意页面中使用接口来判断当前对象是否为可被观察对象
64. this.student.test();
65. })
66. }
67. .height('100%')
68. .width('100%')
69. .justifyContent(FlexAlign.Center)
70. .alignItems(HorizontalAlign.Center)
71. }
72. }

74. @Component
75. export struct Classroom {
76. @State student: Student = new Student();

78. build() {
79. Column() {
80. Text('Classroom ' + this.student.name)
81. School({ student: this.student })
82. }
83. }
84. }

86. @Component
87. export struct Home {
88. @State student: Student = new Student();

90. build() {
91. Column() {
92. Text('Home ' + this.student.name)
93. }
94. }
95. }

97. @Component
98. export struct School {
99. @State student: Student = new Student();

101. build() {
102. Column() {
103. Text('School ' + this.student.name)
104. }
105. }
106. }
```

### makeObserved

PhonePC/2in1TabletTVWearable

static makeObserved<T extends object>(source: T): T

将普通不可观察数据变为可观察数据。详见[makeObserved接口：将非观察数据变为可观察数据](../harmonyos-guides/arkts-new-makeobserved.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | T | 是 | 数据源对象。支持非@Observed和@ObservedV2装饰的class，JSON.parse返回的Object和@Sendable修饰的class。  支持Array、Map、Set和Date。  支持collections.Array, collections.Set和collections.Map。  具体使用规则，详见[makeObserved接口：将非观察数据变为可观察数据](../harmonyos-guides/arkts-new-makeobserved.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 可观察的数据。 |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. class NonObservedClass {
4. name: string = 'Tom';
5. }

7. @Entry
8. @ComponentV2
9. struct Index {
10. observedClass: NonObservedClass = UIUtils.makeObserved(new NonObservedClass());
11. nonObservedClass: NonObservedClass = new NonObservedClass();

13. build() {
14. Column() {
15. Text(`observedClass: ${this.observedClass.name}`)
16. .onClick(() => {
17. this.observedClass.name = 'Jane'; // 刷新
18. })
19. Text(`observedClass: ${this.nonObservedClass.name}`)
20. .onClick(() => {
21. this.nonObservedClass.name = 'Jane'; // 不刷新
22. })
23. }
24. }
25. }
```

### enableV2Compatibility19+

PhonePC/2in1TabletTVWearable

static enableV2Compatibility<T extends object>(source: T): T

使V1的状态变量能够在@ComponentV2中观察，主要应用于状态管理V1、V2混用场景。详见[状态管理V1和V2混用指导（API version 19及之后）](../harmonyos-guides/arkts-v1-v2-mixusage.md)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | T | 是 | 数据源，仅支持V1状态数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 如果数据源是V1的状态数据，则返回能够在@ComponentV2中观察的数据。否则返回数据源本身。 |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Observed
4. class ObservedClass {
5. name: string = 'Tom';
6. }

8. @Entry
9. @Component
10. struct CompV1 {
11. @State observedClass: ObservedClass = new ObservedClass();

13. build() {
14. Column() {
15. Text(`@State observedClass: ${this.observedClass.name}`)
16. .onClick(() => {
17. this.observedClass.name = 'State'; // 刷新
18. })
19. // 将V1的状态变量使能V2的观察能力
20. CompV2({ observedClass: UIUtils.enableV2Compatibility(this.observedClass) })
21. }
22. }
23. }

25. @ComponentV2
26. struct CompV2 {
27. @Param observedClass: ObservedClass = new ObservedClass();

29. build() {
30. // V1状态变量在使能V2观察能力后，可以在V2观察第一层的变化
31. Text(`@Param observedClass: ${this.observedClass.name}`)
32. .onClick(() => {
33. this.observedClass.name = 'Param'; // 刷新
34. })
35. }
36. }
```

### makeV1Observed19+

PhonePC/2in1TabletTVWearable

static makeV1Observed<T extends object>(source: T): T

将不可观察的对象包装成状态管理V1可观察的对象，其能力等同于@Observed，可初始化@ObjectLink。

该接口可搭配[enableV2Compatibility](js-apis-statemanagement.md#enablev2compatibility19)应用于状态管理V1和V2混用场景，详见[状态管理V1和V2混用指导（API version 19及之后）](../harmonyos-guides/arkts-v1-v2-mixusage.md)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | T | 是 | 数据源。支持普通class、Array、Map、Set、Date类型。  不支持[collections类型](arkts-apis-arkts-collections.md)和[@Sendable](../harmonyos-guides/arkts-sendable.md)修饰的class。  不支持undefined和null。不支持状态管理V2的数据和[makeObserved](js-apis-statemanagement.md#makeobserved)的返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 对于支持的入参类型，返回状态管理V1的观察数据。对于不支持的入参类型，返回数据源对象本身。 |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. class Outer {
4. outerValue: string = 'outer';
5. inner: Inner;

7. constructor(inner: Inner) {
8. this.inner = inner;
9. }
10. }

12. class Inner {
13. interValue: string = 'inner';
14. }

16. @Entry
17. @Component
18. struct Index {
19. @State outer: Outer = new Outer(UIUtils.makeV1Observed(new Inner()));

21. build() {
22. Column() {
23. // makeV1Observed的返回值可初始化@ObjectLink
24. Child({ inner: this.outer.inner })
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }

31. @Component
32. struct Child {
33. @ObjectLink inner: Inner;

35. build() {
36. Text(`${this.inner.interValue}`)
37. .onClick(() => {
38. this.inner.interValue += '!';
39. })
40. }
41. }
```

### makeBinding20+

PhonePC/2in1TabletTVWearable

static makeBinding<T>(getter: GetterCallback<T>): Binding<T>

创建只读的单向数据绑定实例，用于构建[@Builder](../harmonyos-guides/arkts-builder.md)函数中参数类型为Binding的对应实参。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| getter | [GetterCallback<T>](js-apis-statemanagement.md#gettercallback20) | 是 | 获取值的回调函数，每次访问值都会重新执行函数，获取最新值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Binding<T>](js-apis-statemanagement.md#bindingt20) | 仅包含一个value属性，用于获取当前绑定的值。只能读取值，不能直接修改。 |

**示例：**

```
1. import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function CustomButton(num1: Binding<number>) {
5. Row() {
6. Button(`Custom Button: ${num1.value}`)
7. .onClick(() => {
8. // num1.value += 1; 会报错，Binding类型不支持修改
9. })
10. }
11. }

13. @Entry
14. @ComponentV2
15. struct CompV2 {
16. @Local number1: number = 5;
17. @Local number2: number = 10;

19. build() {
20. Column() {
21. Text('parent component')

23. CustomButton(
24. /**
25. * 创建只读绑定实例
26. * @param getter - 返回this.number1的函数
27. * @returns 只读的Binding<number>对象
28. *
29. * 特点：
30. * 1. 每次访问.value时重新计算
31. * 2. 不能直接修改值
32. */
33. UIUtils.makeBinding<number>(
34. () => this.number1 // GetterCallback
35. )
36. )
37. }
38. }
39. }
```

### makeBinding20+

PhonePC/2in1TabletTVWearable

static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>

创建可修改的双向数据绑定实例，用于构建@Builder函数中参数类型为MutableBinding的对应实参。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| getter | [GetterCallback<T>](js-apis-statemanagement.md#gettercallback20) | 是 | 获取值的回调函数，每次访问值都会重新执行函数，获取最新值。 |
| setter | [SetterCallback<T>](js-apis-statemanagement.md#settercallback20) | 是 | 定义如何更新值，当.value被修改时自动调用此函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MutableBinding<T>](js-apis-statemanagement.md#mutablebindingt20) | 包含一个value属性，支持通过.value读取和修改数据，设置值时会检查类型是否匹配泛型T。 |

**示例：**

```
1. import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function CustomButton(num2: MutableBinding<number>) {
5. Row() {
6. Button(`Custom Button: ${num2.value}`)
7. .onClick(() => {
8. // MutableBinding类型支持修改
9. num2.value += 1;
10. })
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct CompV2 {
17. @Local number1: number = 5;
18. @Local number2: number = 10;

20. build() {
21. Column() {
22. Text('parent component')

24. CustomButton(
25. /**
26. * 创建可变绑定
27. * @param getter - 返回this.number2的函数
28. * @param setter - 当绑定值修改时调用的回调
29. * @returns 可变的MutableBinding<number>对象
30. *
31. * 特点：
32. * 1. 支持读取和写入操作
33. * 2. 修改.value时会自动调用setter回调
34. */
35. UIUtils.makeBinding<number>(
36. () => this.number2, // GetterCallback
37. (val: number) => {
38. this.number2 = val;
39. }) // SetterCallback
40. )
41. }
42. }
43. }
```

### addMonitor20+

PhonePC/2in1TabletTVWearable

static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void

给状态管理V2的状态变量动态添加监听方法，详见[addMonitor/clearMonitor](../harmonyos-guides/arkts-new-addmonitor-clearmonitor.md)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | object | 是 | 目标对象，仅支持[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)和[@ObservedV2](../harmonyos-guides/arkts-new-observedv2-and-trace.md)实例。  对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| path | string | string[] | 是 | 添加监听的变量名路径。可指定一个路径或者传入string数组用于一次性指定多个监听的变量路径。  仅支持string和string数组，对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| monitorCallback | [MonitorCallback](js-apis-statemanagement.md#monitorcallback20) | 是 | 给对应的状态变量注册的监听函数，即path路径对应的状态变量改变时，会回调对应的函数。  对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| options | [MonitorOptions](js-apis-statemanagement.md#monitoroptions20) | 否 | 监听函数的配置项，具体可见[MonitorOptions](js-apis-statemanagement.md#monitoroptions20)。默认为异步回调。 |

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 130000 | The target is not a custom component instance or V2 class instance. |
| 130001 | The path is invalid. |
| 130002 | monitorCallback is not a function or an anonymous function. |

**示例：**

下面的示例：

1. 在ObservedClass的构造方法里，添加对name属性的同步监听回调onChange。
2. 点击Text组件，将name改为Jack和Jane，触发两次onChange回调，打印日志如下。

```
1. ObservedClass property name change from Tom to Jack
2. ObservedClass property name change from Jack to Jane
```

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class ObservedClass {
5. @Trace name: string = 'Tom';

7. onChange(mon: IMonitor) {
8. mon.dirty.forEach((path: string) => {
9. console.info(`ObservedClass property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
10. });
11. }

13. constructor() {
14. // 给当前ObservedClass的实例this添加对属性name的监听回调this.onChange，且当前监听回调是同步监听
15. UIUtils.addMonitor(this, 'name', this.onChange, { isSynchronous: true });
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Index {
22. @Local observedClass: ObservedClass = new ObservedClass();

24. build() {
25. Column() {
26. Text(`name: ${this.observedClass.name}`)
27. .fontSize(20)
28. .onClick(() => {
29. this.observedClass.name = 'Jack';
30. this.observedClass.name = 'Jane';
31. })
32. }
33. }
34. }
```

### clearMonitor20+

PhonePC/2in1TabletTVWearable

static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback): void

删除通过[addMonitor](js-apis-statemanagement.md#addmonitor20)给状态管理V2的状态变量添加的监听方法，详见[addMonitor/clearMonitor](../harmonyos-guides/arkts-new-addmonitor-clearmonitor.md)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | object | 是 | 目标对象，仅支持[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)和[@ObservedV2](../harmonyos-guides/arkts-new-observedv2-and-trace.md)实例。  对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| path | string | string[] | 是 | 删除监听的变量名路径。可指定一个路径或者传入string数组用于一次性指定删除多个状态变量的监听函数。  仅支持string和数组，对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| monitorCallback | [MonitorCallback](js-apis-statemanagement.md#monitorcallback20) | 否 | 指定被删除的监听函数。  当开发者不传此参数时，将删除path对应变量注册的所有监听函数。  对于不支持的类型，会抛出运行时错误，错误码见表格。 |

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 130000 | The target is not a custom component instance or V2 class instance. |
| 130001 | The path is invalid. |
| 130002 | monitorCallback is not a function or an anonymous function. |

**示例：**

在下面的示例中：

1. 在ObservedClass的构造方法中，添加对age属性的同步监听回调onChange。
2. 点击Text组件，触发age自增，onChange的监听回调函数被触发。打印日志如下。

   ```
   1. ObservedClass property age change from 10 to 11
   ```
3. 点击clear monitor，删除age的监听函数onChange。
4. 再次点击Text组件，触发age自增，onChange不会被触发。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class ObservedClass {
5. @Trace age: number = 10;

7. onChange(mon: IMonitor) {
8. mon.dirty.forEach((path: string) => {
9. console.info(`ObservedClass property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
10. });
11. }

13. constructor() {
14. // 给当前ObservedClass的实例this添加对属性age的监听回调this.onChange，且当前监听回调是同步监听
15. UIUtils.addMonitor(this, 'age', this.onChange);
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Index {
22. @Local observedClass: ObservedClass = new ObservedClass();

24. build() {
25. Column() {
26. Text(`age: ${this.observedClass.age}`)
27. .fontSize(20)
28. .onClick(() => {
29. // 点击触发age++，触发onChange回调
30. this.observedClass.age++;
31. })
32. Button('clear monitor')
33. .onClick(() => {
34. // 点击clearMonitor，删除this.observedClass中age的监听函数onChange
35. // 再次点击触发age++，没有触发监听函数onChange
36. UIUtils.clearMonitor(this.observedClass, 'age', this.observedClass.onChange);
37. })
38. }
39. }
40. }
```

### applySync22+

PhonePC/2in1TabletTVWearable

static applySync<T>(task: TaskCallback): T

同步刷新指定的状态变量，该接口接收一个闭包函数，仅刷新闭包函数内的修改，包括更新[@Computed计算](../harmonyos-guides/arkts-new-computed.md)、[@Monitor回调](../harmonyos-guides/arkts-new-monitor.md)以及重新渲染UI节点，详见[applySync/flushUpdates/flushUIUpdates接口：同步刷新](../harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates.md)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [TaskCallback](js-apis-statemanagement.md#taskcallback22) | 是 | 闭包函数，该闭包中产生的状态变量修改会同步执行。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 闭包函数执行得到的返回值。 |

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140001 | The function is not allowed to be called in @Computed. |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local w: number = 50; // 宽度
7. @Local h: number = 50; // 高度
8. @Local message: string = 'Hello';

10. build() {
11. Column() {
12. Button('change size')
13. .margin(20)
14. .onClick(() => {
15. // 在执行动画前，存在额外的修改
16. UIUtils.applySync(() => {
17. this.w = 100;
18. this.h = 100;
19. this.message = 'Hello World';
20. });
21. // 动画在1s内，Column方框的尺寸由（100*100）渐变为（200*200），方框内的文本变为Hello ArkUI
22. this.getUIContext().animateTo({
23. duration: 1000
24. }, () => {
25. console.info(`animateTo-in, w=${this.w}, h=${this.h}`);
26. this.w = 200;
27. this.h = 200;
28. this.message = 'Hello ArkUI';
29. console.info(`animateTo-out, w=${this.w}, h=${this.h}`);
30. });
31. })
32. // Column方框
33. Column() {
34. Text(`${this.message}`)
35. }
36. .backgroundColor('#ff17a98d')
37. .width(this.w)
38. .height(this.h)
39. }
40. }
41. }
```

### flushUpdates22+

PhonePC/2in1TabletTVWearable

static flushUpdates(): void

同步刷新在调用该函数之前所有的状态变量修改，包括更新@Computed计算、@Monitor回调以及重新渲染UI节点，详见[applySync/flushUpdates/flushUIUpdates接口：同步刷新](../harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates.md)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140001 | The function is not allowed to be called in @Computed. |
| 140002 | The function is not allowed to be called in @Monitor. |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local w: number = 50; // 宽度
7. @Local h: number = 50; // 高度
8. @Local message: string = 'Hello';

10. build() {
11. Column() {
12. Button('change size')
13. .margin(20)
14. .onClick(() => {
15. // 在执行动画前，存在额外的修改
16. this.w = 100;
17. this.h = 100;
18. this.message = 'Hello World';
19. UIUtils.flushUpdates();
20. // 动画在1s内，Column方框的尺寸由（100*100）渐变为（200*200），方框内的文本变为Hello ArkUI
21. this.getUIContext().animateTo({
22. duration: 1000
23. }, () => {
24. console.info(`animateTo-in, w=${this.w}, h=${this.h}`);
25. this.w = 200;
26. this.h = 200;
27. this.message = 'Hello ArkUI';
28. console.info(`animateTo-out, w=${this.w}, h=${this.h}`);
29. });
30. })
31. // Column方框
32. Column() {
33. Text(`${this.message}`)
34. }
35. .backgroundColor('#ff17a98d')
36. .width(this.w)
37. .height(this.h)
38. }
39. }
40. }
```

### flushUIUpdates22+

PhonePC/2in1TabletTVWearable

static flushUIUpdates(): void

立即处理在调用该函数之前所有的状态变量修改，同步[标脏](../harmonyos-guides/arkts-state-management-introduce.md#触发更新)对应的UI节点，但不会同步执行@Computed计算和@Monitor回调，详见[applySync/flushUpdates/flushUIUpdates接口：同步刷新](../harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates.md)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140001 | The function is not allowed to be called in @Computed. |
| 140002 | The function is not allowed to be called in @Monitor. |

**示例：**

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local w: number = 50; // 宽度
7. @Local h: number = 50; // 高度
8. @Local message: string = 'Hello';

10. build() {
11. Column() {
12. Button('change size')
13. .margin(20)
14. .onClick(() => {
15. // 在执行动画前，存在额外的修改
16. this.w = 100;
17. this.h = 100;
18. this.message = 'Hello World';
19. UIUtils.flushUIUpdates();
20. // 动画在1s内，Column方框的尺寸由（100*100）渐变为（200*200），方框内的文本变为Hello ArkUI
21. this.getUIContext().animateTo({
22. duration: 1000
23. }, () => {
24. console.info(`animateTo-in, w=${this.w}, h=${this.h}`);
25. this.w = 200;
26. this.h = 200;
27. this.message = 'Hello ArkUI';
28. console.info(`animateTo-out, w=${this.w}, h=${this.h}`);
29. });
30. })
31. // Column方框
32. Column() {
33. Text(`${this.message}`)
34. }
35. .backgroundColor('#ff17a98d')
36. .width(this.w)
37. .height(this.h)
38. }
39. }
40. }
```

## TaskCallback22+

PhonePC/2in1TabletTVWearable

type TaskCallback = () => T

同步执行的回调方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 闭包函数执行得到的返回值。 |

## MonitorOptions20+

PhonePC/2in1TabletTVWearable

[addMonitor](js-apis-statemanagement.md#addmonitor20)的可选参数，用于配置回调类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isSynchronous | boolean | 否 | 是 | 配置当前回调函数否是为同步回调。true为同步回调。默认值为false，即异步回调。 |

## MonitorCallback20+

PhonePC/2in1TabletTVWearable

type MonitorCallback = (monitorValue: IMonitor) => void

参数为[IMonitor](ts-state-management-watch-monitor.md#imonitor12)类型的监听回调函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitorValue | IMonitor | 是 | 回调函数传入的变化信息。 |

## StorageDefaultCreator<T>

PhonePC/2in1TabletTVWearable

type StorageDefaultCreator<T> = () => T

返回默认构造器的函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 默认构造器执行得到的返回值。 |

**示例：**

```
1. import { PersistenceV2 } from '@kit.ArkUI';

3. @ObservedV2
4. class SampleClass {
5. @Trace id: number = 0;
6. count: number = 1;
7. }

9. @ObservedV2
10. class FatherSampleClass {
11. @Trace sampleClass: SampleClass = new SampleClass();
12. }

14. // 将key为SampleClass、value为new SampleClass()对象的键值对持久化，并赋值给source
15. // StorageDefaultCreator 指的是 () => new FatherSampleClass()
16. const source: FatherSampleClass | undefined = PersistenceV2.connect(FatherSampleClass, () => new FatherSampleClass());

18. @Entry
19. @Component
20. struct SampleComp {
21. data: FatherSampleClass | undefined = source;

23. build() {
24. Column() {
25. Text(`${this.data?.sampleClass.id}`)
26. }
27. }
28. }
```

## TypeConstructorWithArgs<T>

PhonePC/2in1TabletTVWearable

含有任意入参的类构造器。

### new

PhonePC/2in1TabletTVWearable

new(...args: any): T

创建并返回一个指定类型T的实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ...args | any | 否 | 函数入参。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | T类型的实例。 |

**示例：**

```
1. import { PersistenceV2 } from '@kit.ArkUI';

3. @ObservedV2
4. // TypeConstructorWithArgs 指的是 SampleClass
5. class SampleClass {
6. @Trace id: number = 0;
7. count: number = 1;
8. }

10. @ObservedV2
11. class FatherSampleClass {
12. @Trace sampleClass: SampleClass = new SampleClass();
13. }

15. // 将key为SampleClass、value为new SampleClass()对象的键值对持久化，并赋值给source
16. const source: FatherSampleClass | undefined = PersistenceV2.connect(FatherSampleClass, () => new FatherSampleClass());

18. @Entry
19. @Component
20. struct SampleComp {
21. data: FatherSampleClass | undefined = source;

23. build() {
24. Column() {
25. Text(`${this.data?.sampleClass.id}`)
26. }
27. }
28. }
```

## PersistenceErrorCallback

PhonePC/2in1TabletTVWearable

type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown', message: string) => void

持久化失败时返回错误原因的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 出错的键值。 |
| reason | 'quota' | 'serialization' | 'unknown' | 是 | 出错的原因类型。 |
| message | string | 是 | 出错的更多消息。 |

**示例：**

```
1. import { PersistenceV2, Type } from '@kit.ArkUI';

3. @ObservedV2
4. class SampleChild {
5. @Trace id: number = 0;
6. count: number = 10;
7. }

9. @ObservedV2
10. export class Sample {
11. // 对于复杂对象需要@Type修饰，确保序列化成功
12. @Type(SampleChild)
13. @Trace sampleChild: SampleChild = new SampleChild();
14. }

16. // 接受序列化失败的回调
17. // PersistenceErrorCallback 指的是 (key: string, reason: string, msg: string) => {console.error(`error key: ${key}, reason: ${reason}, message: ${msg}`);}
18. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
19. console.error(`error key: ${key}, reason: ${reason}, message: ${msg}`);
20. });

22. @Entry
23. @ComponentV2
24. struct Index {
25. // 在PersistenceV2中创建一个key为Sample的键值对（如果存在，则返回PersistenceV2中的数据），并且和data关联
26. // 对于需要换connect对象的data属性，需要加@Local修饰（不建议对属性换connect的对象）
27. @Local data: Sample = PersistenceV2.connect(Sample, () => new Sample())!;
28. pageStack: NavPathStack = new NavPathStack();

30. build() {
31. Text(`Index add 1 to data.id: ${this.data.sampleChild.id}`)
32. .fontSize(30)
33. .onClick(() => {
34. this.data.sampleChild.id++;
35. })
36. }
37. }
```

## TypeConstructor<T>

PhonePC/2in1TabletTVWearable

类构造函数。

### new

PhonePC/2in1TabletTVWearable

new(): T

创建并返回一个指定类型T的实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | T类型的实例。 |

**示例：**

```
1. import { PersistenceV2, Type } from '@kit.ArkUI';

3. @ObservedV2
4. class SampleChild {
5. @Trace id: number = 0;
6. count: number = 10;
7. }

9. @ObservedV2
10. export class Sample {
11. // 对于复杂对象需要@Type修饰，确保序列化成功
12. // TypeConstructor 指的是 SampleChild
13. @Type(SampleChild)
14. @Trace sampleChild: SampleChild = new SampleChild();
15. }

17. @Entry
18. @ComponentV2
19. struct Index {
20. data: Sample = PersistenceV2.connect(Sample, () => new Sample())!;

22. build() {
23. Column() {
24. Text(`Index add 1 to data.id: ${this.data.sampleChild.id}`)
25. .fontSize(30)
26. .onClick(() => {
27. this.data.sampleChild.id++;
28. })
29. }
30. }
31. }
```

## TypeDecorator

PhonePC/2in1TabletTVWearable

type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator

属性装饰器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TypeConstructor<T>](js-apis-statemanagement.md#typeconstructort) | 是 | 标记类属性的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器。 |

**示例：**

```
1. import { PersistenceV2, Type } from '@kit.ArkUI';

3. @ObservedV2
4. class SampleChild {
5. @Trace id: number = 0;
6. count: number = 10;
7. }

9. @ObservedV2
10. export class Sample {
11. // 对于复杂对象需要@Type修饰，确保序列化成功
12. // TypeDecorator 指的是 @Type
13. @Type(SampleChild)
14. @Trace sampleChild: SampleChild = new SampleChild();
15. }

17. @Entry
18. @ComponentV2
19. struct Index {
20. data: Sample = PersistenceV2.connect(Sample, () => new Sample())!;

22. build() {
23. Column() {
24. Text(`Index add 1 to data.id: ${this.data.sampleChild.id}`)
25. .fontSize(30)
26. .onClick(() => {
27. this.data.sampleChild.id++;
28. })
29. }
30. }
31. }
```

## GetterCallback20+

PhonePC/2in1TabletTVWearable

type GetterCallback<T> = () => T

获取值的回调方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | T类型的值。 |

**示例：**

```
1. import { Binding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function CustomButton(num1: Binding<number>) {
5. Row() {
6. Button(`Custom Button: ${num1.value}`)
7. .onClick(() => {
8. // num1.value += 1; 会报错，Binding类型不支持修改
9. })
10. }
11. }

13. @Entry
14. @ComponentV2
15. struct CompV2 {
16. @Local number1: number = 5;
17. @Local number2: number = 10;

19. build() {
20. Column() {
21. Text('parent component')

23. CustomButton(
24. // 对于UIUtils.makeBinding函数的第一个参数需要传入GetterCallback
25. UIUtils.makeBinding<number>(
26. () => this.number1 // GetterCallback
27. )
28. )
29. }
30. }
31. }
```

## SetterCallback20+

PhonePC/2in1TabletTVWearable

type SetterCallback<T> = (newValue: T) => void

设置值的回调方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | 类型为T的参数。 |

**示例：**

```
1. import { MutableBinding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function CustomButton(num2: MutableBinding<number>) {
5. Row() {
6. Button(`Custom Button: ${num2.value}`)
7. .onClick(() => {
8. // MutableBinding支持可变，可以修改num2.value
9. num2.value += 1;
10. })
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct CompV2 {
17. @Local number1: number = 5;
18. @Local number2: number = 10;

20. build() {
21. Column() {
22. Text('parent component')

24. CustomButton(
25. // 对于UIUtils.makeBinding函数的第二个参数需要传入SetterCallback
26. UIUtils.makeBinding<number>(
27. () => this.number2, // GetterCallback
28. (val: number) => {
29. this.number2 = val;
30. }) // SetterCallback 必须提供，否则触发时会造成运行时错误
31. )
32. }
33. }
34. }
```

## Binding<T>20+

PhonePC/2in1TabletTVWearable

只读数据绑定的泛型类，可以绑定任意类型的数据。

### value20+

PhonePC/2in1TabletTVWearable

get value(): T

提供get访问器，用于获取绑定的值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回值类型为泛型参数T，与Binding<T>定义的类型一致。 |

**示例：**

```
1. import { Binding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function CustomButton(num1: Binding<number>) {
5. // CustomButton的第一个参数为Binding，一个只读数据绑定的泛型类
6. Row() {
7. // num1.value Binding类可以使用绑定的值
8. Button(`Custom Button: ${num1.value}`)
9. .onClick(() => {
10. // num1.value += 1; 会报错，只读数据绑定的泛型类不能修改值
11. })
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct CompV2 {
18. @Local number1: number = 5;
19. @Local number2: number = 10;

21. build() {
22. Column() {
23. Text('parent component')

25. CustomButton(
26. UIUtils.makeBinding<number>(
27. () => this.number1 // GetterCallback
28. )
29. )
30. }
31. }
32. }
```

## MutableBinding<T>20+

PhonePC/2in1TabletTVWearable

可变数据绑定的泛型类，允许对绑定值进行读写操作，提供完整的get和set访问器。

### value20+

PhonePC/2in1TabletTVWearable

set value(newValue: T)

提供set访问器，用于设置当前绑定值的值。构造MutableBinding类实例时必须提供set访问器，否则触发set访问器会造成运行时错误。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | 参数类型为泛型参数T，与MutableBinding<T>定义的类型一致。 |

### value20+

PhonePC/2in1TabletTVWearable

get value(): T

提供get访问器，用于获取当前绑定值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回值类型为泛型参数T，与Binding<T>定义的类型一致。 |

**示例：**

```
1. import { MutableBinding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function CustomButton(num2: MutableBinding<number>) {
5. // CustomButton的第二个参数为MutableBinding，一个可变数据绑定的泛型类
6. Row() {
7. Button(`Custom Button: ${num2.value}`)
8. .onClick(() => {
9. // 可变数据绑定的泛型类可以修改绑定的值
10. num2.value += 1;
11. })
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct CompV2 {
18. @Local number1: number = 5;
19. @Local number2: number = 10;

21. build() {
22. Column() {
23. Text('parent component')

25. CustomButton(
26. UIUtils.makeBinding<number>(
27. () => this.number2, // GetterCallback
28. (val: number) => {
29. this.number2 = val;
30. }) // SetterCallback 必须提供，否则触发时会造成运行时错误
31. )
32. }
33. }
34. }
```
