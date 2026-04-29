---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition
title: 全屏模态转场
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 模态转场设置 > 全屏模态转场
category: harmonyos-references
scraped_at: 2026-04-29T13:51:30+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:e833e2055ba929aaedd60760187cbbf4142e2c325202a192d3e0b8f231e438ec
---

通过bindContentCover属性为组件绑定全屏模态页面，在组件插入和移除时可通过设置转场参数ModalTransition显示过渡动效。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

不支持横竖屏切换。

不支持路由跳转。

## bindContentCover

PhonePC/2in1TabletTVWearable

bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T

给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，显示方式可设置无动画过渡，上下切换过渡以及透明渐变过渡。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShow | boolean | 是 | 是否显示全屏模态页面。  -true：显示全屏模态页面。  -false：隐藏全屏模态页面。  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 配置全屏模态页面内容。builder里面的根节点需要唯一。 |
| type | [ModalTransition](ts-universal-attributes-sheet-transition.md#modaltransition) | 否 | 全屏模态页面的系统转场方式。  默认值：ModalTransition.DEFAULT。  **说明：**  与transition同时设置时，此属性不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## bindContentCover

PhonePC/2in1TabletTVWearable

bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T

给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，可自定义设置转场方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShow | boolean | 是 | 是否显示全屏模态页面。  -true：显示全屏模态页面。  -false：隐藏全屏模态页面。  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 配置全屏模态页面内容。 |
| options | [ContentCoverOptions](ts-universal-attributes-modal-transition.md#contentcoveroptions) | 否 | 配置全屏模态页面的可选属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ContentCoverOptions

PhonePC/2in1TabletTVWearable

继承自[BindOptions](ts-universal-attributes-sheet-transition.md#bindoptions)。

全屏模态页面内容选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| modalTransition | [ModalTransition](ts-universal-attributes-sheet-transition.md#modaltransition) | 否 | 是 | 全屏模态页面的系统转场方式。  默认值：ModalTransition.DEFAULT。  **说明：**  与transition同时设置时，此属性不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback<[DismissContentCoverAction](ts-universal-attributes-modal-transition.md#dismisscontentcoveraction12类型说明)> | 否 | 是 | 全屏模态页面交互式关闭回调函数。  **说明：**  当用户执行back事件关闭交互操作时，如果注册该回调函数，则不会立刻关闭。在回调函数中可以通过reason得到阻拦关闭页面的操作类型，从而根据原因选择是否关闭全屏模态页面。在onWillDismiss回调中，不能再做onWillDismiss拦截。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 全屏模态页面的自定义转场方式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableSafeArea20+ | boolean | 否 | 是 | 全屏模态是否适配安全区域，true表示全屏模态适配安全区域，将内容限制在安全区内，避让导航条和状态栏，false表示不做处理，和之前的样式保持一致。默认值为false。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## DismissContentCoverAction12+类型说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | [Callback](ts-types.md#callback12)<void> | 否 | 否 | 全屏模态页面关闭回调函数。开发者需要退出页面时调用。 |
| reason | [DismissReason](ts-universal-attributes-popup.md#dismissreason12枚举说明) | 否 | 否 | 返回本次拦截全屏模态页面退出的事件原因。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用全屏模态转场）

该示例主要演示通过bindContentCover来实现全屏模态转场。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ModalTransitionExample {
5. @State isShow: boolean = false;
6. @State isShow2: boolean = false;

8. @Builder
9. myBuilder2() {
10. Column() {
11. Button("close modal 2")
12. .margin(10)
13. .fontSize(20)
14. .onClick(() => {
15. this.isShow2 = false;
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }

22. @Builder
23. myBuilder() {
24. Column() {
25. Button("transition modal 2")
26. .margin(10)
27. .fontSize(20)
28. .onClick(() => {
29. this.isShow2 = true;
30. }).bindContentCover(this.isShow2, this.myBuilder2(), {
31. modalTransition: ModalTransition.NONE,
32. backgroundColor: Color.Orange,
33. onWillAppear: () => {
34. console.info("BindContentCover onWillAppear.");
35. },
36. onAppear: () => {
37. console.info("BindContentCover onAppear.");
38. },
39. onWillDisappear: () => {
40. console.info("BindContentCover onWillDisappear.");
41. },
42. onDisappear: () => {
43. console.info("BindContentCover onDisappear.");
44. }
45. })

47. Button("close modal 1")
48. .margin(10)
49. .fontSize(20)
50. .onClick(() => {
51. this.isShow = false;
52. })
53. }
54. .width('100%')
55. .height('100%')
56. .justifyContent(FlexAlign.Center)
57. }

59. build() {
60. Column() {
61. Button("transition modal 1")
62. .onClick(() => {
63. this.isShow = true;
64. })
65. .fontSize(20)
66. .margin(10)
67. .bindContentCover(this.isShow, this.myBuilder(), {
68. modalTransition: ModalTransition.NONE,
69. backgroundColor: Color.Pink,
70. onWillAppear: () => {
71. console.info("BindContentCover onWillAppear.");
72. },
73. onAppear: () => {
74. console.info("BindContentCover onAppear.");
75. },
76. onWillDisappear: () => {
77. console.info("BindContentCover onWillDisappear.");
78. },
79. onDisappear: () => {
80. console.info("BindContentCover onDisappear.");
81. }
82. })
83. }
84. .justifyContent(FlexAlign.Center)
85. .backgroundColor("#ff49c8ab")
86. .width('100%')
87. .height('100%')
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/9-8fJCKRRuSUx2nQeTFKug/zh-cn_image_0000002589325953.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055127Z&HW-CC-Expire=86400&HW-CC-Sign=D51E0AEA64BF131895CC044FF7FB3D4EF1A13D61868090343D5C01905DA50E37)

### 示例2（自定义转场动画）

全屏模态无动画转场模式下，自定义转场动画。

```
1. // xxx.ets
2. import { curves } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ModalTransitionExample {
7. @State @Watch("isShow1Change") isShow: boolean = false;
8. @State @Watch("isShow2Change") isShow2: boolean = false;
9. @State isScale1: number = 1;
10. @State isScale2: number = 1;

12. isShow1Change() {
13. this.isShow ? this.isScale1 = 0.95 : this.isScale1 = 1;
14. }

16. isShow2Change() {
17. this.isShow2 ? this.isScale2 = 0.95 : this.isScale2 = 1;
18. }

20. @Builder
21. myBuilder2() {
22. Column() {
23. Button("close modal 2")
24. .margin(10)
25. .fontSize(20)
26. .onClick(() => {
27. this.isShow2 = false;
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }

34. @Builder
35. myBuilder() {
36. Column() {
37. Button("transition modal 2")
38. .margin(10)
39. .fontSize(20)
40. .onClick(() => {
41. this.isShow2 = true;
42. }).bindContentCover(this.isShow2, this.myBuilder2(), {
43. modalTransition: ModalTransition.NONE,
44. backgroundColor: Color.Orange,
45. onWillAppear: () => {
46. console.info("BindContentCover onWillAppear.");
47. },
48. onAppear: () => {
49. console.info("BindContentCover onAppear.");
50. },
51. onWillDisappear: () => {
52. console.info("BindContentCover onWillDisappear.");
53. },
54. onDisappear: () => {
55. console.info("BindContentCover onDisappear.");
56. }
57. })

59. Button("close modal 1")
60. .margin(10)
61. .fontSize(20)
62. .onClick(() => {
63. this.isShow = false;
64. })
65. }
66. .width('100%')
67. .height('100%')
68. .justifyContent(FlexAlign.Center)
69. .scale({ x: this.isScale2, y: this.isScale2 })
70. .animation({ curve: curves.springMotion() })
71. }

73. build() {
74. Column() {
75. Button("transition modal 1")
76. .onClick(() => {
77. this.isShow = true;
78. })
79. .fontSize(20)
80. .margin(10)
81. .bindContentCover(this.isShow, this.myBuilder(), {
82. modalTransition: ModalTransition.NONE,
83. backgroundColor: Color.Pink,
84. onWillAppear: () => {
85. console.info("BindContentCover onWillAppear.");
86. },
87. onAppear: () => {
88. console.info("BindContentCover onAppear.");
89. },
90. onWillDisappear: () => {
91. console.info("BindContentCover onWillDisappear.");
92. },
93. onDisappear: () => {
94. console.info("BindContentCover onDisappear.");
95. }
96. })
97. }
98. .justifyContent(FlexAlign.Center)
99. .backgroundColor("#ff49c8ab")
100. .width('100%')
101. .height('100%')
102. .scale({ x: this.isScale1, y: this.isScale1 })
103. .animation({ curve: curves.springMotion() })
104. }
105. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Ubn5ap8JTwG_eF3H9h8ExQ/zh-cn_image_0000002589245895.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055127Z&HW-CC-Expire=86400&HW-CC-Sign=9049B669A76EFBA8761AAD9085DB6DE773863F5BB54463893FF989380BAC9FA9)

### 示例3（上下切换转场）

全屏模态上下切换转场。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ModalTransitionExample {
5. @State isShow: boolean = false;
6. @State isShow2: boolean = false;

8. @Builder
9. myBuilder2() {
10. Column() {
11. Button("close modal 2")
12. .margin(10)
13. .fontSize(20)
14. .onClick(() => {
15. this.isShow2 = false;
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }

22. @Builder
23. myBuilder() {
24. Column() {
25. Button("transition modal 2")
26. .margin(10)
27. .fontSize(20)
28. .onClick(() => {
29. this.isShow2 = true;
30. }).bindContentCover(this.isShow2, this.myBuilder2(), {
31. modalTransition: ModalTransition.DEFAULT,
32. backgroundColor: Color.Gray,
33. onWillAppear: () => {
34. console.info("BindContentCover onWillAppear.");
35. },
36. onAppear: () => {
37. console.info("BindContentCover onAppear.");
38. },
39. onWillDisappear: () => {
40. console.info("BindContentCover onWillDisappear.");
41. },
42. onDisappear: () => {
43. console.info("BindContentCover onDisappear.");
44. }
45. })

47. Button("close modal 1")
48. .margin(10)
49. .fontSize(20)
50. .onClick(() => {
51. this.isShow = false;
52. })
53. }
54. .width('100%')
55. .height('100%')
56. .justifyContent(FlexAlign.Center)
57. }

59. build() {
60. Column() {
61. Button("transition modal 1")
62. .onClick(() => {
63. this.isShow = true;
64. })
65. .fontSize(20)
66. .margin(10)
67. .bindContentCover(this.isShow, this.myBuilder(), {
68. modalTransition: ModalTransition.DEFAULT,
69. backgroundColor: Color.Pink,
70. onWillAppear: () => {
71. console.info("BindContentCover onWillAppear.");
72. },
73. onAppear: () => {
74. console.info("BindContentCover onAppear.");
75. },
76. onWillDisappear: () => {
77. console.info("BindContentCover onWillDisappear.");
78. },
79. onDisappear: () => {
80. console.info("BindContentCover onDisappear.");
81. }
82. })
83. }
84. .justifyContent(FlexAlign.Center)
85. .backgroundColor(Color.White)
86. .width('100%')
87. .height('100%')
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/wTuMgR_tQkm8vHoasPTLSA/zh-cn_image_0000002558766086.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055127Z&HW-CC-Expire=86400&HW-CC-Sign=8969AA87CEA2B1EDAEFB79BC0C576E64CA4BC6BE618D64F6BE0DE9C954EC5592)

### 示例4（透明度渐变转场）

全屏模态透明度渐变转场。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ModalTransitionExample {
5. @State isShow: boolean = false;
6. @State isShow2: boolean = false;

8. @Builder
9. myBuilder2() {
10. Column() {
11. Button("close modal 2")
12. .margin(10)
13. .fontSize(20)
14. .onClick(() => {
15. this.isShow2 = false;
16. })
17. }
18. .width('100%')
19. .height('100%')
20. .justifyContent(FlexAlign.Center)
21. }

23. @Builder
24. myBuilder() {
25. Column() {
26. Button("transition modal 2")
27. .margin(10)
28. .fontSize(20)
29. .onClick(() => {
30. this.isShow2 = true;
31. }).bindContentCover(this.isShow2, this.myBuilder2(), {
32. modalTransition: ModalTransition.ALPHA,
33. backgroundColor: Color.Gray,
34. onWillAppear: () => {
35. console.info("BindContentCover onWillAppear.");
36. },
37. onAppear: () => {
38. console.info("BindContentCover onAppear.");
39. },
40. onWillDisappear: () => {
41. console.info("BindContentCover onWillDisappear.");
42. },
43. onDisappear: () => {
44. console.info("BindContentCover onDisappear.");
45. }
46. })

48. Button("close modal 1")
49. .margin(10)
50. .fontSize(20)
51. .onClick(() => {
52. this.isShow = false;
53. })
54. }
55. .width('100%')
56. .height('100%')
57. .justifyContent(FlexAlign.Center)
58. }

60. build() {
61. Column() {
62. Button("transition modal 1")
63. .onClick(() => {
64. this.isShow = true;
65. })
66. .fontSize(20)
67. .margin(10)
68. .bindContentCover(this.isShow, this.myBuilder(), {
69. modalTransition: ModalTransition.ALPHA,
70. backgroundColor: Color.Pink,
71. onWillAppear: () => {
72. console.info("BindContentCover onWillAppear.");
73. },
74. onAppear: () => {
75. console.info("BindContentCover onAppear.");
76. },
77. onWillDisappear: () => {
78. console.info("BindContentCover onWillDisappear.");
79. },
80. onDisappear: () => {
81. console.info("BindContentCover onDisappear.");
82. }
83. })
84. }
85. .justifyContent(FlexAlign.Center)
86. .backgroundColor(Color.White)
87. .width('100%')
88. .height('100%')
89. }
90. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/yu0rY1_yQ_msAZQw8JM4vg/zh-cn_image_0000002558606428.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055127Z&HW-CC-Expire=86400&HW-CC-Sign=8232EB8B07ADEA620EDFFBBBBC41F175DA970C86DE94E2ED539926795A741039)

### 示例5（设置不同效果的自定义转场）

该示例主要演示全屏模态旋转，平移等自定义转场。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ModalTransitionExample {
5. @State isShow: boolean = false;
6. @State isShow2: boolean = false;

8. @Builder
9. myBuilder2() {
10. Column() {
11. Button("Close Modal 2")
12. .margin(10)
13. .fontSize(20)
14. .onClick(() => {
15. this.isShow2 = false;
16. })
17. }
18. .width('100%')
19. .height('100%')
20. .justifyContent(FlexAlign.Center)
21. }

23. @Builder
24. myBuilder() {
25. Column() {
26. Button("Transition Modal 2")
27. .margin(10)
28. .fontSize(20)
29. .onClick(() => {
30. this.isShow2 = true;
31. })
32. .bindContentCover(
33. this.isShow2,
34. this.myBuilder2(),
35. {
36. modalTransition: ModalTransition.DEFAULT,
37. backgroundColor: Color.Gray,
38. transition: TransitionEffect.SLIDE.animation({ duration: 5000, curve: Curve.LinearOutSlowIn }),
39. onWillDismiss: ((dismissContentCoverAction: DismissContentCoverAction) => {
40. if (dismissContentCoverAction.reason == DismissReason.PRESS_BACK) {
41. console.info("BindContentCover dismiss reason is back pressed");
42. }
43. dismissContentCoverAction.dismiss();
44. }),
45. onAppear: () => {
46. console.info("BindContentCover onAppear.");
47. },
48. onDisappear: () => {
49. this.isShow2 = false;
50. console.info("BindContentCover onDisappear.");
51. }
52. })

54. Button("Close Modal 1")
55. .margin(10)
56. .fontSize(20)
57. .onClick(() => {
58. this.isShow = false;
59. })
60. }
61. .width('100%')
62. .height('100%')
63. .justifyContent(FlexAlign.Center)
64. }

66. build() {
67. Column() {
68. Button("Transition Modal 1")
69. .onClick(() => {
70. this.isShow = true;
71. })
72. .fontSize(20)
73. .margin(10)
74. .bindContentCover(
75. this.isShow,
76. this.myBuilder(),
77. {
78. modalTransition: ModalTransition.DEFAULT,
79. backgroundColor: Color.Pink,
80. transition: TransitionEffect.asymmetric(
81. TransitionEffect.OPACITY.animation({ duration: 1100 }).combine(
82. TransitionEffect.rotate({ z: 1, angle: 180 }).animation({ delay: 1000, duration: 1000 }))
83. ,
84. TransitionEffect.OPACITY.animation({ duration: 1200 }).combine(
85. TransitionEffect.rotate({ z: 1, angle: 180 }).animation({ duration: 1300 }))
86. ),
87. onWillDismiss: ((dismissContentCoverAction: DismissContentCoverAction) => {
88. if (dismissContentCoverAction.reason == DismissReason.PRESS_BACK) {
89. console.info("back pressed");
90. }
91. dismissContentCoverAction.dismiss();
92. }),
93. onAppear: () => {
94. console.info("BindContentCover onAppear.");
95. },
96. onDisappear: () => {
97. this.isShow = false;
98. console.info("BindContentCover onDisappear.");
99. }
100. })
101. }
102. .justifyContent(FlexAlign.Center)
103. .backgroundColor(Color.White)
104. .width('100%')
105. .height('100%')
106. }
107. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/o_rGaNpHT6axrW_XcM0MeA/zh-cn_image_0000002589325955.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055127Z&HW-CC-Expire=86400&HW-CC-Sign=B3EE5A9FDC8192F7852D381A111AF84B9C35C15BDD41E1E9C5E14EEC965CA2C0)

### 示例6（设置全屏模态适配安全区）

从API version 20开始，该示例主要演示设置enableSafeArea为true后全屏模态适配安全区的内容效果。全屏模态容器其背景色为浅蓝色，内容颜色为灰色，内容在安全区内布局。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SafeAreaController {
5. @State isShow: boolean = false;
6. @State SafeArea: boolean | undefined = true;
7. @State heightMode: string = '100%';

9. @Builder
10. myBuilder() {
11. Column() {
12. Column() {
13. Button("Content")
14. .fontSize(20)
15. }
16. .width('100%')
17. .height('50%')
18. .borderRadius(10)
19. .borderStyle(BorderStyle.Dotted)
20. .borderWidth(2)
21. Column() {
22. Button("Content")
23. .margin({top:340})
24. .fontSize(20)
25. }
26. .width('100%')
27. .height('50%')
28. .borderRadius(10)
29. .borderStyle(BorderStyle.Dotted)
30. .borderWidth(2)
31. }
32. .backgroundColor(Color.Grey)
33. .justifyContent(FlexAlign.Center)
34. .width('100%')
35. .height(this.heightMode)
36. }
37. build() {
38. Column() {
39. Button("Open ContentCover")
40. .onClick(() => this.isShow = true)
41. .fontSize(20)
42. .margin(10)
43. .bindContentCover(this.isShow, this.myBuilder(), {
44. modalTransition: ModalTransition.ALPHA,
45. backgroundColor: 0x87CEEB,
46. // 动态设置安全区域模式
47. enableSafeArea: this.SafeArea
48. })
49. }
50. .justifyContent(FlexAlign.Center)
51. .width('100%')
52. .height('100%')
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/-j5D--6sS_yZHBLLCSzfrA/zh-cn_image_0000002589245897.png?HW-CC-KV=V1&HW-CC-Date=20260429T055127Z&HW-CC-Expire=86400&HW-CC-Sign=3D8C524087DA878BA239C316BC246E754BBA5517090CCA44AD6555801F6C8116)
