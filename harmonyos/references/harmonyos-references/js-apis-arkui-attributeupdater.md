---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-attributeupdater
title: AttributeUpdater
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > AttributeUpdater
category: harmonyos-references
scraped_at: 2026-04-28T08:00:37+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:d57916fafbf824768d1f21baa8c9f6324db54b5d3fe5e120c6adf33d4dd9c783
---

将属性直接设置给组件，无需标记为状态变量即可直接触发UI更新。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AttributeUpdater } from '@kit.ArkUI';
```

说明

1. 由于与属性方法同时设置或者在AttributeUpdater中实现applyNormalAttribute等方法时，涉及到与状态管理更新机制同时使用，易出现混淆，因此不建议在同一组件上同时用两种方法设置相同属性。
2. 当与属性方法同时设置时，属性生效的原则为：后设置的生效。

   若先进行属性直通更新，后通过状态管理机制更新属性方法，则后更新的属性方法生效；

   若先通过状态管理机制更新属性方法，后进行属性直通更新，则属性直通更新生效。
3. 一个AttributeUpdater对象只能同时关联一个组件，否则将出现设置的属性只在一个组件上生效的现象。
4. 开发者需要自行保障AttributeUpdater中T和C的类型匹配。比如T为ImageAttribute，C要对应为ImageInterface，否则可能导致

   使用updateConstructorParams时功能异常。
5. updateConstructorParams当前只支持Button，Image，Text，Span，SymbolSpan和ImageSpan组件。
6. AttributeUpdater不支持深浅色切换等状态管理相关的操作。
7. 在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的场景中调用[AttributeUpdater](js-apis-arkui-attributeupdater.md#attributeupdatert-c--initializert)对象的接口时，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口明确UI上下文，参考[执行绑定UI实例的闭包](../harmonyos-guides/arkts-global-interface.md#执行绑定ui实例的闭包)示例。

## Initializer<T>

PhonePC/2in1TabletTVWearable

type Initializer<T> = () => T

可以将属性更新到本地的修饰器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AttributeUpdater<T, C = Initializer<T>>

PhonePC/2in1TabletTVWearable

为[AttributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifiert)的实现类，开发者需要自定义class继承AttributeUpdater。

其中C代表组件的构造函数类型，比如Text组件的TextInterface，Image组件的ImageInterface等，仅在使用updateConstructorParams时才需要传递C类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### applyNormalAttribute

PhonePC/2in1TabletTVWearable

applyNormalAttribute?(instance: T): void

定义正常态更新属性函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如Button组件的ButtonAttribute，Text组件的TextAttribute等。 |

### initializeModifier

PhonePC/2in1TabletTVWearable

initializeModifier(instance: T): void

AttributeUpdater首次设置给组件时提供的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如Button组件的ButtonAttribute，Text组件的TextAttribute等。 |

**示例：**

通过initializeModifier方法初始化设置属性值。

```
1. // xxx.ets
2. import { AttributeUpdater } from '@kit.ArkUI';

4. class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
5. // 该AttributeUpdater对象第一次使用的时候触发的回调
6. initializeModifier(instance: ButtonAttribute): void {
7. instance.backgroundColor('#ffd5d5d5')
8. .labelStyle({ maxLines: 3 })
9. .width('80%')
10. }

12. // 该AttributeUpdater对象后续使用或者更新的时候触发的回调
13. applyNormalAttribute(instance: ButtonAttribute): void {
14. instance.borderWidth(1);
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. modifier: MyButtonModifier = new MyButtonModifier();
22. @State flushTheButton: string = 'Button';

24. build() {
25. Row() {
26. Column() {
27. Button(this.flushTheButton)
28. .attributeModifier(this.modifier)
29. .onClick(() => {
30. // 通过AttributeUpdater的attribute对属性进行修改
31. // 需要注意先通过组件的attributeModifier属性方法建立组件与AttributeUpdater绑定关系
32. this.modifier.attribute?.backgroundColor('#ff2787d9').labelStyle({ maxLines: 5 });
33. })
34. .margin('10%')
35. Button('Trigger Button Update')
36. .width('80%')
37. .labelStyle({ maxLines: 2 })
38. .onClick(() => {
39. this.flushTheButton = this.flushTheButton + ' Updated';
40. })
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/v1GdaZRzTkegMMvUzUh1Vg/zh-cn_image_0000002552959458.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=975F9F9042B681169EB2203A793176ED2ED15C9991AC19781FFA4BA1631DC5B2)

### attribute

PhonePC/2in1TabletTVWearable

get attribute(): T | undefined

获取AttributeUpdater中组件对应的属性类实例，通过该实例实现属性直通更新的功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | 如果AttributeUpdater中组件的属性类实例存在，则返回对应组件的属性类实例，否则返回undefined。 |

**示例：**

通过属性直通设置方式更新属性值。

```
1. // xxx.ets
2. import { AttributeUpdater } from '@kit.ArkUI';

4. class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
5. initializeModifier(instance: ButtonAttribute): void {
6. instance.backgroundColor('#ffd5d5d5')
7. .width('50%')
8. .height(30);
9. }
10. }

12. @Entry
13. @Component
14. struct updaterDemo2 {
15. modifier: MyButtonModifier = new MyButtonModifier();

17. build() {
18. Row() {
19. Column() {
20. Button("Button")
21. .attributeModifier(this.modifier)
22. .onClick(() => {
23. this.modifier.attribute?.backgroundColor('#ff2787d9').width('30%');
24. })
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Tax7pb3mTby-dRbHeLeCRQ/zh-cn_image_0000002583479459.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=6BCDF5EAB1F99DE563DF1049D104C3AF6C3B3E04985602951522DCA67F2F0233)

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateConstructorParams | [C](js-apis-arkui-attributeupdater.md#attributeupdatert-c--initializert) | 否 | 否 | C代表组件的构造函数类型，比如Text组件的TextInterface，Image组件的ImageInterface等。用于更改组件的构造函数入参。 |

**示例：**

使用updateConstructorParams更新组件的构造入参。

```
1. // xxx.ets
2. import { AttributeUpdater } from '@kit.ArkUI';

4. class MyTextModifier extends AttributeUpdater<TextAttribute, TextInterface> {
5. initializeModifier(instance: TextAttribute) {
6. }
7. }

9. @Entry
10. @Component
11. struct attributeDemo3 {
12. private modifier: MyTextModifier = new MyTextModifier();

14. build() {
15. Row() {
16. Column() {
17. Text("Initialize")
18. .attributeModifier(this.modifier)
19. .fontSize(14).border({ width: 1 }).textAlign(TextAlign.Center).lineHeight(20)
20. .width(200).height(50)
21. .backgroundColor('#fff7f7f7')
22. .onClick(() => {
23. this.modifier.updateConstructorParams("Updated");
24. })
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/o03xUKE3Ry2hJjCAjzFnUg/zh-cn_image_0000002552799810.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=11C73096B7111E607B326494072E44289EFD77C8A9C46313F4F62960427B5D4B)

### onComponentChanged

PhonePC/2in1TabletTVWearable

onComponentChanged(component: T): void

绑定相同的自定义的Modifier对象，组件发生切换时，通过该接口通知到应用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如Button组件的ButtonAttribute，Text组件的TextAttribute等。 |

**示例：**

```
1. // xxx.ets
2. import { AttributeUpdater } from '@kit.ArkUI';

4. class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
5. initializeModifier(instance: ButtonAttribute): void {
6. instance.backgroundColor('#ff2787d9')
7. .width('50%')
8. .height(30);
9. }

11. onComponentChanged(instance: ButtonAttribute): void {
12. instance.backgroundColor('#ff519db4')
13. .width('50%')
14. .height(30);
15. }
16. }

18. @Entry
19. @Component
20. struct updaterDemo4 {
21. @State btnState: boolean = false;
22. modifier: MyButtonModifier = new MyButtonModifier();

24. build() {
25. Row() {
26. Column() {
27. Button("Test")
28. .onClick(() => {
29. this.btnState = !this.btnState;
30. }).margin({ bottom: 20 })

32. if (this.btnState) {
33. Button("Button")
34. .attributeModifier(this.modifier)
35. } else {
36. Button("Button")
37. .attributeModifier(this.modifier)
38. }
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/tfEB0wfzRZGXTwhJUpoIrQ/zh-cn_image_0000002583439505.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=34D1C6CDECB146CB84120D041EEE15F93A90E87DD7DA0FCEC6BE07AB7A560E82)
