---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior
title: 触摸测试控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 触摸交互控制 > 触摸测试控制
category: harmonyos-references
scraped_at: 2026-04-28T08:01:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c4a27088addc7993fc9be7c7d944f90dab6f55ca08aa8c981838699caba592d8
---

设置组件的[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)类型。在ArkUI开发框架中，处理触屏事件和鼠标事件时，会在事件触发前进行按压点与组件响应热区的触摸测试，以收集需响应事件的组件。基于测试结果，框架会分发相应的事件。hitTestBehavior属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续事件分发。具体影响参考[HitTestMode](ts-appendix-enums.md#hittestmode9)枚举说明。影响[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[拖拽事件](ts-universal-events-drag-drop.md)、[鼠标事件](ts-universal-mouse-key.md)、[轴事件](ts-universal-events-axis.md)、[悬浮事件](ts-universal-events-hover.md)、[无障碍悬浮事件](ts-universal-accessibility-hover-event.md)和[手势事件](ts-gesture-settings.md)的分发。

说明

* 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当Stack组件中有多个节点触摸区域重叠时，如果最上层节点的子组件命中，则默认只会对显示在最上层的节点做触摸测试。此时只有给显示在最上层的节点设置hitTestBehavior为HitTestMode.Transparent时，才能使显示在下层的节点触发触摸测试。
* 存在新增节点时，如需该节点响应触摸测试，需要对其设置[HitTestMode](ts-appendix-enums.md#hittestmode9)。当新增节点存在多层级节点时，仅需设置根节点的HitTestMode。

## hitTestBehavior

PhonePC/2in1TabletTVWearable

hitTestBehavior(value: HitTestMode): T

设置组件的触摸测试类型。如果组件不设置hitTestBehavior，其默认触摸测试类型为HitTestMode.Default。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HitTestMode](ts-appendix-enums.md#hittestmode9) | 是 | 设置当前组件的触摸测试类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（触摸测试类型为Block和Transparent的触摸测试效果）

该示例通过设置不同的[HitTestMode](ts-appendix-enums.md#hittestmode9)值演示了Block和Transparent的触摸测试效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct HitTestBehaviorExample {
5. build() {
6. // outer stack
7. Stack() {
8. Button('outer button')
9. .onTouch((event) => {
10. console.info(`outer button touched type: ${(event as TouchEvent).type}`)
11. })
12. // inner stack
13. Stack() {
14. Button('inner button')
15. .onTouch((event) => {
16. console.info(`inner button touched type: ${(event as TouchEvent).type}`)
17. })
18. }
19. .width("100%").height("100%")
20. .hitTestBehavior(HitTestMode.Block)
21. .onTouch((event) => {
22. console.info(`stack touched type: ${(event as TouchEvent).type}`)
23. })

25. Text('Transparent')
26. .hitTestBehavior(HitTestMode.Transparent)
27. .width("100%").height("100%")
28. .onTouch((event) => {
29. console.info(`text touched type: ${(event as TouchEvent).type}`)
30. })
31. }.width(300).height(300)
32. }
33. }
```

### 示例2（触摸测试类型为BLOCK\_HIERARCHY时的触摸测试效果）

从API version 20开始，该示例演示了设置触摸测试类型为BLOCK\_HIERARCHY时的触摸测试效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BlockHierarchy {
5. build() {
6. // outer stack
7. Stack() {
8. Stack() {
9. Button('outer button')
10. .onTouch((event) => {
11. console.info(`HitTestMode outer button touched type: ${(event as TouchEvent).type}`);
12. })
13. .width(200)
14. .height(200)
15. .backgroundColor('#D5D5D5')
16. // inner stack
17. Stack() {
18. Button()
19. .id('button150')
20. .backgroundColor('#F7F7F7')
21. .width(150)
22. .height(150)
23. .onTouch((event) => {
24. console.info(`HitTestMode button150 touched type: ${(event as TouchEvent).type}`);
25. })
26. .hitTestBehavior(HitTestMode.Transparent)
27. Button()
28. .id('button100')
29. .backgroundColor('#707070')
30. .width(100)
31. .height(100)
32. .onTouch((event) => {
33. console.info(`HitTestMode button100 touched type: ${(event as TouchEvent).type}`);
34. })
35. .hitTestBehavior(HitTestMode.Transparent)
36. Button()
37. .id('button050')
38. .backgroundColor('#D5D5D5')
39. .width(50)
40. .height(50)
41. .onTouch((event) => {
42. console.info(`HitTestMode button050 touched type: ${(event as TouchEvent).type}`);
43. })
44. .hitTestBehavior(HitTestMode.Transparent)
45. }
46. .width("100%").height("100%")
47. // 设置触摸测试模式，自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试
48. .hitTestBehavior(HitTestMode.BLOCK_HIERARCHY)
49. .onTouch((event) => {
50. console.info(`HitTestMode stack touched type: ${(event as TouchEvent).type}`);
51. })

53. Text('Transparent')
54. .hitTestBehavior(HitTestMode.Transparent)
55. .width("100%").height("100%")
56. .onTouch((event) => {
57. console.info(`HitTestMode text touched type: ${(event as TouchEvent).type}`);
58. })
59. }.width(300).height(300)
60. .borderWidth(2)
61. .onTouch((event) => {
62. console.info(`HitTestMode father stack touched type: ${(event as TouchEvent).type}`);
63. })
64. }.width(500).height(500)
65. .borderWidth(2)
66. .onTouch((event) => {
67. console.info(`HitTestMode grandfather stack touched type: ${(event as TouchEvent).type}`);
68. })
69. }
70. }
```

### 示例3（触摸测试类型为BLOCK\_DESCENDANTS时的触摸测试效果）

从API version 20开始，该示例演示了设置触摸测试类型为BLOCK\_DESCENDANTS时的触摸测试效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BlockDescendants {
5. build() {
6. // outer stack
7. Stack() {
8. Stack() {
9. Button('outer button')
10. .onTouch((event) => {
11. console.info(`HitTestMode outer button touched type: ${(event as TouchEvent).type}`);
12. })
13. .width(200)
14. .height(200)
15. .backgroundColor('#D5D5D5')
16. // inner stack
17. Stack() {
18. Button('inner button')
19. .width(100)
20. .height(100)
21. .onTouch((event) => {
22. console.info(`HitTestMode inner button touched type: ${(event as TouchEvent).type}`);
23. })
24. }
25. .width("100%").height("100%")
26. // 设置触摸测试模式，自身不响应触摸测试，并且所有的后代（孩子，孙子等）也不响应触摸测试
27. .hitTestBehavior(HitTestMode.BLOCK_DESCENDANTS)
28. .onTouch((event) => {
29. console.info(`HitTestMode stack touched type: ${(event as TouchEvent).type}`);
30. })

32. Text('Transparent')
33. .hitTestBehavior(HitTestMode.Transparent)
34. .width("100%").height("100%")
35. .onTouch((event) => {
36. console.info(`HitTestMode text touched type: ${(event as TouchEvent).type}`);
37. })
38. }.width(300).height(300)
39. .borderWidth(2)
40. .onTouch((event) => {
41. console.info(`HitTestMode father stack touched type: ${(event as TouchEvent).type}`);
42. })
43. }.width(500).height(500)
44. .borderWidth(2)
45. .onTouch((event) => {
46. console.info(`HitTestMode grandfather stack touched type: ${(event as TouchEvent).type}`);
47. })
48. }
49. }
```

### 示例4（Stack组件中多节点重合时的触摸测试效果）

该示例演示了在Stack组件中存在多节点触摸区域重叠时的触摸测试效果。此时设置[HitTestMode](ts-appendix-enums.md#hittestmode9)为None时，重叠的背景区域无法响应触摸测试；只有设置为Transparent时，背景区域才能响应触摸测试。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State @Watch('onModeChange') mode: number = HitTestMode.None;
6. @State modeStr: string = 'None';

8. onModeChange() {
9. this.modeStr = this.mode === HitTestMode.None ? 'None' : 'Transparent';
10. }

12. build() {
13. Stack() {
14. Column()
15. .height('100%')
16. .width('100%')
17. .onTouch(() => {
18. console.info('background hit test!')
19. })
20. Stack() {
21. // 点击按钮进行触摸测试
22. Button('HitTest')
23. // 点击按钮切换不同的触摸测试模式
24. Button('HitTestMode: ' + this.modeStr)
25. .margin({ top: 100 })
26. .onClick(() => {
27. this.mode = this.mode === HitTestMode.None ?
28. HitTestMode.Transparent : HitTestMode.None;
29. })
30. }
31. .height('100%')
32. .width('100%')
33. // 只有上层节点的HitTestMode设置为Transparent时，下层节点才能响应触摸测试
34. .hitTestBehavior(this.mode)
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```
