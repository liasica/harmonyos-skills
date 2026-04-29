---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-attributeupdater
title: 属性更新器 (AttributeUpdater)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > Modifier机制 > 属性更新器 (AttributeUpdater)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62a6dd324186125bfa6479f97e63541bd280ef71756ca37a1ee606de3477a61a
---

## 概述

在大量属性频繁更新的场景下，使用状态变量可能导致前端状态管理的计算量过大，并且需要对单个组件进行全量属性更新。尽管可以通过[AttributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)机制实现按需更新属性，但前端仍会采用一定的diff和reset策略，这可能带来性能问题。

AttributeUpdater作为一个特殊的AttributeModifier，不仅继承了AttributeModifier的功能，还提供了直接获取属性对象的能力。通过属性对象，开发者能够直接更新对应属性，无需经过状态变量。开发者可以利用AttributeUpdater实现自定义的更新策略，从而进一步提升属性更新的性能。

由于AttributeUpdater提供了较高的灵活性，无法限制“单一数据源”的规则，因此在与状态变量同时更新同一属性时，存在相互覆盖的情况。这要求开发者必须确保属性设置的合理性。

## 接口定义

```
1. export declare class AttributeUpdater<T, C = Initializer<T>> implements AttributeModifier<T> {

3. applyNormalAttribute?(instance: T): void;

5. initializeModifier(instance: T): void;

7. get attribute(): T | undefined;

9. public updateConstructorParams: C;
10. }
```

[Common.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkTSUserAttributeUpdater/entry/src/main/ets/pages/Common.ets#L15-L26)

AttributeUpdater实现了AttributeModifier接口，并额外提供了initializeModifier，可以对组件的属性进行初始化。通过attribute属性方法可以获取属性对象，直接更新对应组件的属性。另外也可以直接通过updateConstructorParams更新组件的构造参数。

## 使用说明

* 开发者可以继承AttributeUpdater<T>类，并通过组件的通用方法attributeModifier设置，首次绑定时会触发initializeModifier方法，进行属性的初始化，后续其它的生命周期和AttributeModifier保持一致。
* 组件初始化完成之后，开发者可以通过AttributeUpdater实例的attribute属性方法，获取到属性对象，若获取不到则为undefined。
* 通过attribute属性对象直接修改属性，会将最新设置的属性记录在当前对象中，并立即触发组件属性的更新。
* 如果将AttributeUpdater实例标记为状态变量进行修改，或者通过其它状态变量更新对应组件的属性，会触发applyNormalAttribute的流程，如果开发者没有复写该逻辑，默认会将属性对象记录的所有属性，进行一次批量更新。
* 如果开发者复写applyNormalAttribute的逻辑，并且不调用super的该方法，将会失去获取attribute属性对象的能力，不会调用initializeModifier方法。
* 一个AttributeUpdater对象只能同时关联一个组件，否则只会有一个组件的属性设置生效。

## 通过modifier直接修改属性

组件初始化完成之后，开发者可以通过AttributeUpdater实例的attribute属性方法，获取到属性对象。通过属性对象直接修改属性，会立即触发组件属性的更新。

```
1. import { AttributeUpdater } from '@kit.ArkUI';

3. class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
4. // 首次绑定时触发initializeModifier方法，进行属性初始化
5. initializeModifier(instance: ButtonAttribute): void {
6. instance.backgroundColor('#2787D9')
7. .width('50%')
8. .height(30)
9. }
10. }

12. @Entry
13. @Component
14. struct updaterDemo {
15. modifier: MyButtonModifier = new MyButtonModifier()

17. build() {
18. Row() {
19. Column() {
20. Button('Button')
21. .attributeModifier(this.modifier)
22. .onClick(() => {
23. // 通过attribute，直接修改组件属性，并立即触发组件属性更新
24. this.modifier.attribute?.backgroundColor('#17A98D').width('30%')
25. })
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

[AttModifier.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkTSUserAttributeUpdater/entry/src/main/ets/pages/AttModifier.ets#L15-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/TtFDac1jR6qxu7LdVKacHA/zh-cn_image_0000002558604864.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052823Z&HW-CC-Expire=86400&HW-CC-Sign=CB5DDE8FB2239161BC57D15D42D4F2D6D132AB0948BDD011A4F1437525BB5909)

## 通过modifier更新组件的构造参数

可以通过AttributeUpdater实例的updateConstructorParams方法，直接更新组件的构造参数。

```
1. import { AttributeUpdater } from '@kit.ArkUI';

3. class MyTextModifier extends AttributeUpdater<TextAttribute, TextInterface> {
4. initializeModifier(instance: TextAttribute): void {
5. }
6. }

8. @Entry
9. @Component
10. struct updaterDemo {
11. modifier: MyTextModifier = new MyTextModifier();

13. build() {
14. Row() {
15. Column() {
16. Text('Text')
17. .attributeModifier(this.modifier)
18. .fontColor(Color.White)
19. .fontSize(14)
20. .border({ width: 1 })
21. .textAlign(TextAlign.Center)
22. .lineHeight(20)
23. .width(200)
24. .height(50)
25. .backgroundColor('#2787D9')
26. .onClick(() => {
27. // 调用updateConstructorParams方法，直接更新组件的构造参数
28. this.modifier.updateConstructorParams('Update');
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

[AttUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkTSUserAttributeUpdater/entry/src/main/ets/pages/AttUpdate.ets#L15-L51)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/SUeUgMW_Tey1E8mGltZ5Ig/zh-cn_image_0000002589324389.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052823Z&HW-CC-Expire=86400&HW-CC-Sign=6E7EDA666A3525A5FB31E08EBA56842AFD71C720D98766CC7C4F243A5B42AC99)
