---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-object
title: 内置对象的迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 内置对象的迁移
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb473eec1787e1923c662d0a3ffe9236ade3e96d175d18a4cd5f769c5be96091
---

本文档主要介绍组件内置对象从V1向V2的迁移，涉及如下装饰器。

| V1装饰器名称/场景 | V2装饰器名称 |
| --- | --- |
| 滚动组件场景 | [makeObserved](arkts-new-makeobserved.md) |
| [Modifier](arkts-user-defined-modifier.md) | [makeObserved](arkts-new-makeobserved.md)、[@ObservedV2](arkts-new-observedv2-and-trace.md)、[@Trace](arkts-new-observedv2-and-trace.md) |

## 滚动组件

### List

开发者可以通过[ChildrenMainSize](../harmonyos-references/ts-container-list.md#childrenmainsize12)来设置[List](../harmonyos-references/ts-container-list.md)的子组件在主轴方向的大小信息。

V1：

在状态管理V1中，可以通过[@State](arkts-state.md)装饰观察其api调用。

具体示例如下：

```
1. @Entry
2. @Component
3. struct ListExample {
4. private arr: Array<number> = new Array(10).fill(0);
5. private scroller: ListScroller = new ListScroller();
6. @State listSpace: number = 10;
7. @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);

9. build() {
10. Column() {
11. Button('change Default').onClick(() => {
12. this.listChildrenSize.childDefaultSize += 10;
13. })

15. Button('splice 5').onClick(() => {
16. this.listChildrenSize.splice(0, 5, [100, 100, 100, 100, 100]);
17. })

19. Button('update 5').onClick(() => {
20. this.listChildrenSize.update(0, 200);
21. })

23. List({ space: this.listSpace, scroller: this.scroller }) {
24. ForEach(this.arr, (item: number) => {
25. ListItem() {
26. Text(`item-` + item)
27. }.backgroundColor(Color.Pink)
28. })
29. }
30. .childrenMainSize(this.listChildrenSize) // 10
31. }
32. }
33. }
```

[InternalOtherMigrationsListV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalOtherMigrationsListV1.ets#L15-L49)

V2：

在状态管理V2中，[@Local](arkts-new-local.md)只能观察本身的变化，无法观察第一层的变化，而由于ChildrenMainSize定义在List组件框架中，开发者无法使用[@Trace](arkts-new-observedv2-and-trace.md)来标注ChildrenMainSize属性。可以使用[makeObserved](arkts-new-makeobserved.md)替代。从API version 22开始，可以无需使用makeObserved，直接使用@Local标注的ChildrenMainSize设置List的子组件在主轴方向的大小信息。

具体示例如下：

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct ListExample {
6. private arr: Array<number> = new Array(10).fill(0);
7. private scroller: ListScroller = new ListScroller();
8. listSpace: number = 10;
9. // 使用makeObserved的能力来观测ChildrenMainSize
10. listChildrenSize: ChildrenMainSize = UIUtils.makeObserved(new ChildrenMainSize(100));

12. build() {
13. Column() {
14. Button('change Default').onClick(() => {
15. this.listChildrenSize.childDefaultSize += 10;
16. })

18. Button('splice 5').onClick(() => {
19. this.listChildrenSize.splice(0, 5, [100, 100, 100, 100, 100]);
20. })

22. Button('update 5').onClick(() => {
23. this.listChildrenSize.update(0, 200);
24. })

26. List({ space: this.listSpace, scroller: this.scroller }) {
27. ForEach(this.arr, (item: number) => {
28. ListItem() {
29. Text(`item-` + item)
30. }.backgroundColor(Color.Pink)
31. })
32. }
33. .childrenMainSize(this.listChildrenSize) // 10
34. }
35. }
36. }
```

[InternalOtherMigrationsListV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalOtherMigrationsListV2.ets#L15-L52)

### WaterFlow

开发者可以通过[WaterFlowSections](../harmonyos-references/ts-container-waterflow.md#waterflowsections12)来设置WaterFlow瀑布流分组信息。

需要注意的是，数组arr的长度需要与WaterFlowSections的所有SectionOptions的itemsCount总和一致，否则WaterFlow无法处理，导致UI不刷新。

以下两个示例请按照push option -> splice option -> update option的顺序进行点击。

V1：

在状态管理V1中，可以通过[@State](arkts-state.md)装饰观察其api调用。

具体示例如下：

```
1. @Entry
2. @Component
3. struct WaterFlowSample {
4. @State colors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Blue, Color.Pink];
5. @State sections: WaterFlowSections = new WaterFlowSections();
6. scroller: Scroller = new Scroller();
7. @State private arr: Array<number> = new Array(9).fill(0);
8. oneColumnSection: SectionOptions = {
9. itemsCount: 4,
10. crossCount: 1,
11. columnsGap: '5vp',
12. rowsGap: 10,
13. };
14. twoColumnSection: SectionOptions = {
15. itemsCount: 2,
16. crossCount: 2,
17. };
18. lastSection: SectionOptions = {
19. itemsCount: 3,
20. crossCount: 3,
21. };

23. aboutToAppear(): void {
24. let sectionOptions: SectionOptions[] = [this.oneColumnSection, this.twoColumnSection, this.lastSection];
25. this.sections.splice(0, 0, sectionOptions);
26. }

28. build() {
29. Column() {
30. Text(`${this.arr.length}`)

32. Button('push option').onClick(() => {
33. let section: SectionOptions = {
34. itemsCount: 1,
35. crossCount: 1,
36. };
37. this.sections.push(section);
38. this.arr.push(100);
39. })

41. Button('splice option').onClick(() => {
42. let section: SectionOptions = {
43. itemsCount: 8,
44. crossCount: 2,
45. };
46. this.sections.splice(0, this.arr.length, [section]);
47. this.arr = new Array(8).fill(10);
48. })

50. Button('update option').onClick(() => {
51. let section: SectionOptions = {
52. itemsCount: 8,
53. crossCount: 2,
54. };
55. this.sections.update(1, section);
56. this.arr = new Array(16).fill(1);
57. })

59. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
60. ForEach(this.arr, (item: number) => {
61. FlowItem() {
62. Text(`${item}`)
63. .border({ width: 1 })
64. .backgroundColor(this.colors[item % 6])
65. .height(30)
66. .width(50)
67. }
68. })
69. }
70. }
71. }
72. }
```

[InternalOtherMigrationsWaterFlowV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalOtherMigrationsWaterFlowV1.ets#L15-L88)

V2：

在状态管理V2中，[@Local](arkts-new-local.md)只能观察本身的变化，无法观察第一层的变化，由于WaterFlowSections定义在框架中，开发者无法使用[@Trace](arkts-new-observedv2-and-trace.md)标注其属性，此时可以使用[makeObserved](arkts-new-makeobserved.md)替代。

具体示例如下：

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct WaterFlowSample {
6. colors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Blue, Color.Pink];
7. // 使用makeObserved的能力来观测WaterFlowSections
8. sections: WaterFlowSections = UIUtils.makeObserved(new WaterFlowSections());
9. scroller: Scroller = new Scroller();
10. @Local private arr: Array<number> = new Array(9).fill(0);
11. oneColumnSection: SectionOptions = {
12. itemsCount: 4,
13. crossCount: 1,
14. columnsGap: '5vp',
15. rowsGap: 10,
16. };
17. twoColumnSection: SectionOptions = {
18. itemsCount: 2,
19. crossCount: 2,
20. };
21. lastSection: SectionOptions = {
22. itemsCount: 3,
23. crossCount: 3,
24. };

26. aboutToAppear(): void {
27. let sectionOptions: SectionOptions[] = [this.oneColumnSection, this.twoColumnSection, this.lastSection];
28. this.sections.splice(0, 0, sectionOptions);
29. }

31. build() {
32. Column() {
33. Text(`${this.arr.length}`)

35. Button('push option').onClick(() => {
36. let section: SectionOptions = {
37. itemsCount: 1,
38. crossCount: 1,
39. };
40. this.sections.push(section);
41. this.arr.push(100);
42. })

44. Button('splice option').onClick(() => {
45. let section: SectionOptions = {
46. itemsCount: 8,
47. crossCount: 2,
48. };
49. this.sections.splice(0, this.arr.length, [section]);
50. this.arr = new Array(8).fill(10);
51. })

53. Button('update option').onClick(() => {
54. let section: SectionOptions = {
55. itemsCount: 8,
56. crossCount: 2,
57. };
58. this.sections.update(1, section);
59. this.arr = new Array(16).fill(1);
60. })

62. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
63. ForEach(this.arr, (item: number) => {
64. FlowItem() {
65. Text(`${item}`)
66. .border({ width: 1 })
67. .backgroundColor(this.colors[item % 6])
68. .height(30)
69. .width(50)
70. }
71. })
72. }
73. }
74. }
75. }
```

[InternalOtherMigrationsWaterFlowV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalOtherMigrationsWaterFlowV2.ets#L15-L91)

## Modifier

### attributeModifier

开发者可以通过[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置组件的属性方法。

V1：

在状态管理V1中，可以通过[@State](arkts-state.md)装饰观察其变化。

具体示例如下：

```
1. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
2. public isDark: boolean = false;

4. applyNormalAttribute(instance: ButtonAttribute): void {
5. if (this.isDark) {
6. instance.backgroundColor(Color.Black);
7. } else {
8. instance.backgroundColor(Color.Red);
9. }
10. }
11. }

13. @Entry
14. @Component
15. struct AttributeDemo {
16. @State modifier: MyButtonModifier = new MyButtonModifier();

18. build() {
19. Row() {
20. Column() {
21. Button('Button')
22. .attributeModifier(this.modifier)
23. .onClick(() => {
24. this.modifier.isDark = !this.modifier.isDark;
25. })
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

[InternalattributeModifierV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalattributeModifierV1.ets#L15-L47)

V2：

在状态管理V2中，[@Local](arkts-new-local.md)只能观察本身的变化，无法观察第一层的变化，如果要观察attributeModifier的属性变化，可以使用[makeObserved](arkts-new-makeobserved.md)替代。

具体示例如下：

```
1. import { UIUtils } from '@kit.ArkUI';

3. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
4. public isDark: boolean = false;

6. applyNormalAttribute(instance: ButtonAttribute): void {
7. if (this.isDark) {
8. instance.backgroundColor(Color.Black);
9. } else {
10. instance.backgroundColor(Color.Red);
11. }
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct AttributeDemo {
18. // 使用makeObserved的能力观测attributeModifier的属性this.modifier
19. modifier: MyButtonModifier = UIUtils.makeObserved(new MyButtonModifier());

21. build() {
22. Row() {
23. Column() {
24. Button('Button')
25. .attributeModifier(this.modifier)
26. .onClick(() => {
27. this.modifier.isDark = !this.modifier.isDark;
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

[InternalattributeModifierV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalattributeModifierV2.ets#L15-L50)

### CommonModifier

动态设置组件的属性类。以[CommonModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#自定义modifier)为例。

V1：

在状态管理V1中，可以通过[@State](arkts-state.md)装饰观察其变化。

具体实例如下：

```
1. import { CommonModifier } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. class MyModifier extends CommonModifier {
7. applyNormalAttribute(instance: CommonAttribute): void {
8. super.applyNormalAttribute?.(instance);
9. }

11. public setGroup1(): void {
12. this.borderStyle(BorderStyle.Dotted);
13. this.borderWidth(8);
14. }

16. public setGroup2(): void {
17. this.borderStyle(BorderStyle.Dashed);
18. this.borderWidth(8);
19. }
20. }

22. @Component
23. struct MyImage1 {
24. @Link modifier: CommonModifier;

26. build() {
27. // 此处'app.media.app_icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
28. Image($r('app.media.app_icon'))
29. .attributeModifier(this.modifier as MyModifier)
30. }
31. }

33. @Entry
34. @Component
35. struct Index {
36. @State myModifier: CommonModifier = new MyModifier().width(100).height(100).margin(10);
37. index: number = 0;

39. build() {
40. Column() {
41. Button($r('app.string.EntryAbility_label'))
42. .margin(10)
43. .onClick(() => {
44. hilog.info(DOMAIN, 'testTag', 'Modifier', 'onClick');
45. this.index++;
46. if (this.index % 2 === 1) {
47. (this.myModifier as MyModifier).setGroup1();
48. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup1');
49. } else {
50. (this.myModifier as MyModifier).setGroup2();
51. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup2');
52. }
53. })

55. MyImage1({ modifier: this.myModifier })
56. }
57. .width('100%')
58. }
59. }
```

[InternalCommonModifierV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalCommonModifierV1.ets#L15-L75)

V2：

在状态管理V2中，[@Local](arkts-new-local.md)只能观察本身的变化，无法观察第一层的变化，又因为[CommonModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#自定义modifier)在框架内是通过其属性触发刷新，此时可以使用[makeObserved](arkts-new-makeobserved.md)替代。

具体示例如下：

```
1. import { UIUtils, CommonModifier } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. class MyModifier extends CommonModifier {
7. applyNormalAttribute(instance: CommonAttribute): void {
8. super.applyNormalAttribute?.(instance);
9. }

11. public setGroup1(): void {
12. this.borderStyle(BorderStyle.Dotted);
13. this.borderWidth(8);
14. }

16. public setGroup2(): void {
17. this.borderStyle(BorderStyle.Dashed);
18. this.borderWidth(8);
19. }
20. }

22. @ComponentV2
23. struct MyImage1 {
24. @Param @Require modifier: CommonModifier;

26. build() {
27. // 此处'app.media.app_icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
28. Image($r('app.media.app_icon'))
29. .attributeModifier(this.modifier as MyModifier)
30. }
31. }

33. @Entry
34. @ComponentV2
35. struct Index {
36. // 使用makeObserved的能力来观测CommonModifier
37. @Local myModifier: CommonModifier = UIUtils.makeObserved(new MyModifier().width(100).height(100).margin(10));
38. index: number = 0;

40. build() {
41. Column() {
42. Button($r('app.string.EntryAbility_label'))
43. .margin(10)
44. .onClick(() => {
45. hilog.info(DOMAIN, 'testTag', 'Modifier', 'onClick');
46. this.index++;
47. if (this.index % 2 === 1) {
48. (this.myModifier as MyModifier).setGroup1();
49. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup1');
50. } else {
51. (this.myModifier as MyModifier).setGroup2();
52. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup2');
53. }
54. })

56. MyImage1({ modifier: this.myModifier })
57. }
58. .width('100%')
59. }
60. }
```

[InternalCommonModifierV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalCommonModifierV2.ets#L15-L76)

### 组件Modifier

动态设置组件的属性类。以Text组件为例。

V1：

在状态管理V1中，可以通过[@State](arkts-state.md)装饰观察其变化。

具体示例如下：

```
1. import { TextModifier } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. class MyModifier extends TextModifier {
7. applyNormalAttribute(instance: TextModifier): void {
8. super.applyNormalAttribute?.(instance);
9. }

11. public setGroup1(): void {
12. this.fontSize(50);
13. this.fontColor(Color.Pink);
14. }

16. public setGroup2(): void {
17. this.fontSize(50);
18. this.fontColor(Color.Gray);
19. }
20. }

22. @Component
23. struct MyImage1 {
24. @Link modifier: TextModifier;
25. index: number = 0;

27. build() {
28. Column() {
29. Text('Test')
30. .attributeModifier(this.modifier as MyModifier)

32. Button($r('app.string.EntryAbility_label'))
33. .margin(10)
34. .onClick(() => {
35. hilog.info(DOMAIN, 'testTag', 'Modifier', 'onClick');
36. this.index++;
37. if (this.index % 2 === 1) {
38. (this.modifier as MyModifier).setGroup1();
39. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup1');
40. } else {
41. (this.modifier as MyModifier).setGroup2();
42. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup2');
43. }
44. })
45. }
46. }
47. }

49. @Entry
50. @Component
51. struct Index {
52. @State myModifier: TextModifier = new MyModifier().width(100).height(100).margin(10);
53. index: number = 0;

55. build() {
56. Column() {
57. MyImage1({ modifier: this.myModifier })

59. Button('replace whole')
60. .margin(10)
61. .onClick(() => {
62. this.myModifier = new MyModifier().backgroundColor(Color.Orange);
63. })
64. }
65. .width('100%')
66. }
67. }
```

[InternalModuleModifierV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalModuleModifierV1.ets#L15-L83)

V2：

但在状态管理V2中，[@Local](arkts-new-local.md)只能观察本身的变化，无法观察第一层的变化，此时可以使用[makeObserved](arkts-new-makeobserved.md)替代。

具体示例如下：

```
1. import { UIUtils, TextModifier } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. class MyModifier extends TextModifier {
7. applyNormalAttribute(instance: TextModifier): void {
8. super.applyNormalAttribute?.(instance);
9. }

11. public setGroup1(): void {
12. this.fontSize(50);
13. this.fontColor(Color.Pink);
14. }

16. public setGroup2(): void {
17. this.fontSize(50);
18. this.fontColor(Color.Gray);
19. }
20. }

22. @ComponentV2
23. struct MyImage1 {
24. @Param @Require modifier: TextModifier;
25. index: number = 0;

27. build() {
28. Column() {
29. Text('Test')
30. .attributeModifier(this.modifier as MyModifier)

32. Button($r('app.string.EntryAbility_label'))
33. .margin(10)
34. .onClick(() => {
35. hilog.info(DOMAIN, 'testTag', 'Modifier', 'onClick');
36. this.index++;
37. if (this.index % 2 === 1) {
38. (this.modifier as MyModifier).setGroup1();
39. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup1');
40. } else {
41. (this.modifier as MyModifier).setGroup2();
42. hilog.info(DOMAIN, 'testTag', 'Modifier', 'setGroup2');
43. }
44. })
45. }
46. }
47. }

49. @Entry
50. @ComponentV2
51. struct Index {
52. // 使用makeObserved的能力观测TextModifier
53. @Local myModifier: TextModifier = UIUtils.makeObserved(new MyModifier().width(100).height(100).margin(10));
54. index: number = 0;

56. build() {
57. Column() {
58. MyImage1({ modifier: this.myModifier })

60. Button('replace whole')
61. .margin(10)
62. .onClick(() => {
63. this.myModifier = UIUtils.makeObserved(new MyModifier().backgroundColor(Color.Orange));
64. })
65. }
66. .width('100%')
67. }
68. }
```

[InternalModuleModifierV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalModuleModifierV2.ets#L15-L84)

### AttributeUpdater

[AttributeUpdater](arkts-user-defined-extension-attributeupdater.md)可以将属性直接设置给组件，无需标记为状态变量即可直接触发UI更新。

V1：

在状态管理V1中，开发者希望通过修改MyButtonModifier的flag来改变绑定在Button上的属性。由于状态管理V1的@State装饰器支持自身及第一层对象属性的观察能力，因此只需用@State装饰AttributeUpdater，即可监听其变化并触发属性更新。

```
1. // xxx.ets
2. import { AttributeUpdater } from '@kit.ArkUI';

4. class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
5. public flag: boolean = false;

7. initializeModifier(instance: ButtonAttribute): void {
8. instance.backgroundColor('#ff2787d9')
9. .width('50%')
10. .height(30)
11. }

13. applyNormalAttribute(instance: ButtonAttribute): void {
14. if (this.flag) {
15. instance.borderWidth(2);
16. } else {
17. instance.borderWidth(10);
18. }
19. }
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State modifier: MyButtonModifier = new MyButtonModifier();

27. build() {
28. Row() {
29. Column() {
30. Button('Button')
31. .attributeModifier(this.modifier)
32. Button('Update')
33. .onClick(() => {
34. this.modifier.flag = !this.modifier.flag;
35. })
36. }
37. .width('100%')
38. }
39. .height('100%')
40. }
41. }
```

[InternalAttributeUpdaterV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalAttributeUpdaterV1.ets#L15-L57)

V2：

与状态管理V1不同，状态管理V2的@Local仅观察自身变化，因此MyButtonModifier需添加@ObservedV2装饰器，flag需要被@Trace装饰，并且需要在组件创建过程中读取flag以建立其与Button组件的联系。在AttributeUpdater场景中，需在initializeModifier中读取flag（如示例所示），否则无法建立关联。

```
1. // xxx.ets
2. import { AttributeUpdater } from '@kit.ArkUI';

4. @ObservedV2
5. class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
6. @Trace public flag: boolean = false;

8. initializeModifier(instance: ButtonAttribute): void {
9. // initializeModifier会在组件初始化阶段回调，需要在这个地方触发下flag的读，使其建立Button组件的关联。
10. this.flag;
11. instance.backgroundColor('#ff2787d9')
12. .width('50%')
13. .height(30)
14. }

16. applyNormalAttribute(instance: ButtonAttribute): void {
17. if (this.flag) {
18. instance.borderWidth(2);
19. } else {
20. instance.borderWidth(10);
21. }
22. }
23. }

25. @Entry
26. @ComponentV2
27. struct Index {
28. // 状态管理V2装饰器仅观察本层，即当前可以观察到modifier整体赋值的变化。
29. @Local modifier: MyButtonModifier = new MyButtonModifier();

31. build() {
32. Row() {
33. Column() {
34. Button('Button')
35. .attributeModifier(this.modifier)
36. Button('Update')
37. .onClick(() => {
38. this.modifier.flag = !this.modifier.flag;
39. })
40. }
41. .width('100%')
42. }
43. .height('100%')
44. }
45. }
```

[InternalAttributeUpdaterV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalAttributeUpdaterV2.ets#L15-L61)
