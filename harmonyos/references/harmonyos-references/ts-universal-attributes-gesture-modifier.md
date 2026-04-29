---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gesture-modifier
title: 动态手势设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 动态手势设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1309ce98d6b2dae818efaeb5c735c05f50f391906864b1924454e2c46a58a72
---

动态设置组件绑定的手势，支持在属性设置时使用if/else语法。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## gestureModifier

PhonePC/2in1TabletTVWearable

gestureModifier(modifier: GestureModifier): T

动态设置组件绑定的手势。

说明

gestureModifier不支持自定义组件。

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [GestureModifier](ts-universal-attributes-gesture-modifier.md#gesturemodifier-1) | 是 | 动态设置当前组件的手势绑定，支持if/else语法。  modifier: 手势修改器，开发者需自定义class实现GestureModifier接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## GestureModifier

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现GestureModifier接口。

### applyGesture

PhonePC/2in1TabletTVWearable

applyGesture(event: UIGestureEvent): void

手势更新函数。

开发者可根据需要自定义实现该方法，对组件设置需要绑定的手势，支持使用if/else语法进行动态设置。若在当次手势操作过程中触发了组件上的手势动态切换，该切换效果在当次手势结束（所有手指抬起）后的下一次手势操作中生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [UIGestureEvent](ts-uigestureevent.md#uigestureevent) | 是 | UIGestureEvent对象，用于设置组件需要绑定的手势。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（动态绑定手势）

该示例通过gestureModifier动态设置组件绑定的手势。

```
1. // xxx.ets
2. class MyButtonModifier implements GestureModifier {
3. supportDoubleTap: boolean = true;

5. applyGesture(event: UIGestureEvent): void {
6. if (this.supportDoubleTap) {
7. event.addGesture(
8. new TapGestureHandler({
9. count: 2,
10. fingers: 1,
11. // 从API version 23开始，新增distanceThreshold属性
12. distanceThreshold: 100
13. })
14. .tag("aaa")
15. .onAction((event: GestureEvent) => {
16. console.info('Gesture Info is', JSON.stringify(event));
17. console.info('button tap');
18. })
19. )
20. } else {
21. event.addGesture(
22. new PanGestureHandler()
23. .onActionStart(() => {
24. console.info('Pan start');
25. })
26. )
27. }
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. @State modifier: MyButtonModifier = new MyButtonModifier();

36. build() {
37. Row() {
38. Column() {
39. Column()
40. .gestureModifier(this.modifier)
41. .width(500)
42. .height(500)
43. .backgroundColor(Color.Gray)
44. Button('changeGesture')
45. .onClick(() => {
46. this.modifier.supportDoubleTap = !this.modifier.supportDoubleTap;
47. })
48. .margin({ top: 10 })
49. }
50. .width('100%')
51. }
52. .height('100%')
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Op2qec52TNmxgJ1L2ZhcEA/zh-cn_image_0000002589245907.png?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=5624FA8BF090BB34D470E3EF2773998CBCFCB5DAAF9AFFB90095CD641EE2A2B6)

### 示例2（动态绑定手势组）

该示例通过gestureModifier动态设置组件绑定的手势组。

```
1. class MyButtonModifier implements GestureModifier {
2. isExclusive: boolean = true;

4. applyGesture(event: UIGestureEvent): void {
5. if (this.isExclusive) {
6. // 绑定互斥手势组
7. event.addGesture(new GestureGroupHandler({
8. mode: GestureMode.Exclusive,
9. gestures: [new TapGestureHandler({ count: 2, fingers: 1 }).onAction((event) => {
10. console.info('event info is', JSON.stringify(event));
11. console.info('ExclusiveGroupGesture TapGesture is called');
12. }), new LongPressGestureHandler({ repeat: true, fingers: 1 }).onAction((event) => {
13. console.info('event info is', JSON.stringify(event));
14. console.info('ExclusiveGroupGesture LongPressGesture is called');
15. }), new PanGestureHandler({ fingers: 1 }).onActionStart((event) => {
16. console.info('event info is', JSON.stringify(event));
17. console.info('ExclusiveGroupGesture PanGesture onActionStart is called');
18. }).onActionEnd((event) => {
19. console.info('event info is', JSON.stringify(event));
20. console.info('ExclusiveGroupGesture PanGesture onActionEnd is called');
21. })]
22. }))
23. } else {
24. // 绑定并行手势组
25. event.addGesture(new GestureGroupHandler({
26. mode: GestureMode.Parallel,
27. gestures: [new TapGestureHandler({ count: 2, fingers: 1 }).onAction((event) => {
28. console.info('event info is', JSON.stringify(event));
29. console.info('ParallelGroupGesture TapGesture is called');
30. }), new LongPressGestureHandler({ repeat: true, fingers: 1 }).onAction((event) => {
31. console.info('event info is', JSON.stringify(event));
32. console.info('ParallelGroupGesture LongPressGesture is called');
33. }), new PanGestureHandler({ fingers: 1 }).onActionStart((event) => {
34. console.info('event info is', JSON.stringify(event));
35. console.info('ParallelGroupGesture PanGesture onActionStart is called');
36. }).onActionEnd((event) => {
37. console.info('event info is', JSON.stringify(event));
38. console.info('ParallelGroupGesture PanGesture onActionEnd is called');
39. })]
40. }))
41. }
42. }
43. }

45. @Entry
46. @Component
47. struct Index {
48. @State modifier: MyButtonModifier = new MyButtonModifier();

50. build() {
51. Row() {
52. Column() {
53. Column()
54. .gestureModifier(this.modifier)
55. .width(500)
56. .height(500)
57. .backgroundColor(Color.Gray)

59. Button('changeGestureGroupType')
60. .onClick(() => {
61. this.modifier.isExclusive = !this.modifier.isExclusive;
62. })
63. .margin({ top: 10 })
64. }
65. .width('100%')
66. }
67. .height('100%')
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/xktKY22PQWuLORZmOezmPg/zh-cn_image_0000002558766098.png?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=D8B934E47AB7CAE8101150F003361224D0D33F44F17B7D2C1B93233E423B0E0E)
