---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query
title: 媒体查询 (@ohos.mediaquery)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 媒体查询 (@ohos.mediaquery)
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ebcd8d08cb13dce92921ccfce383274a26e664fa2a34be62927299f7e13f5f6f
---

## 概述

[媒体查询](../harmonyos-references/js-apis-mediaquery.md)作为响应式设计的核心，在移动设备上应用十分广泛。媒体查询可根据不同设备类型或同设备不同状态修改应用的样式。媒体查询常用于下面两种场景：

1. 针对设备和应用的属性信息（比如显示区域、深浅色、分辨率），设计出相匹配的布局。
2. 当屏幕发生动态改变时（比如分屏、横竖屏切换），同步更新应用的页面布局。

## 引入与使用流程

媒体查询通过mediaquery模块接口，设置查询条件并绑定回调函数，任一[媒体特征](arkts-layout-development-media-query.md#媒体特征media-feature)改变时，均会触发回调函数，返回匹配结果，根据返回值更改页面布局或者实现业务逻辑，实现页面的响应式设计。具体步骤如下：

首先导入媒体查询模块。

```
1. import { mediaquery } from '@kit.ArkUI';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MediaQuerySample/entry/src/main/ets/pages/Index.ets#L17-L19)

通过matchMediaSync接口设置媒体查询条件，保存返回的条件监听句柄listener。例如监听横屏事件：

```
1. listener:mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MediaQuerySample/entry/src/main/ets/pages/Index.ets#L29-L31)

给条件监听句柄listener绑定回调函数onPortrait，当listener检测设备状态变化时执行回调函数。在回调函数内，根据不同设备状态更改页面布局或者实现业务逻辑。

```
1. onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
2. if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的页面布局
3. // ···
4. } else {
5. // ···
6. }
7. }

9. // ···
10. this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
11. // ···
12. });
13. // ···
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MediaQuerySample/entry/src/main/ets/pages/Index.ets#L34-L62)

## 媒体查询条件

媒体查询条件由媒体类型、逻辑操作符、媒体特征组成，其中媒体类型可省略，逻辑操作符用于连接不同媒体类型与媒体特征，媒体特征要使用()包裹且可以有多个。

### 语法规则

语法规则包括[媒体类型（media-type）](arkts-layout-development-media-query.md#媒体类型media-type)、[媒体逻辑操作（media-logic-operations）](arkts-layout-development-media-query.md#媒体逻辑操作media-logic-operations)和[媒体特征（media-feature）](arkts-layout-development-media-query.md#媒体特征media-feature)。

```
1. [media-type] [media-logic-operations] [(media-feature)]
```

例如：

* screen and (round-screen: true) ：表示当设备屏幕是圆形时条件成立。
* (max-height: 800px) ：表示当高度小于等于800px时条件成立。
* (height <= 800px) ：表示当高度小于等于800px时条件成立。
* screen and (device-type: tv) or (resolution < 2) ：表示包含多个媒体特征的多条件复杂语句查询，当设备类型为tv或设备分辨率小于2时条件成立。
* (dark-mode: true) ：表示当系统为深色模式时成立。

### 媒体类型（media-type）

查询条件未写媒体类型时，默认为screen。媒体类型必须写在查询条件开头。

| **类型** | **说明** |
| --- | --- |
| screen | 按屏幕相关参数进行媒体查询。 |

### 媒体逻辑操作（media-logic-operations）

媒体逻辑操作符包括and、or、not、only，用于构成复杂媒体查询，也可以通过逗号,将其组合，详细解释说明如下表。

**表1** 媒体逻辑操作符

| 类型 | 说明 |
| --- | --- |
| and | 将多个媒体特征（Media Feature）以“与”的方式连接成一个媒体查询，只有当所有媒体特征都为true时，查询条件成立。另外，它还可以将媒体类型和媒体功能结合起来。例如：screen and (device-type: wearable) and (max-height: 600px) 表示当设备类型是智能穿戴且应用的最大高度小于等于600个像素单位时成立。 |
| or | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。例如：screen and (max-height: 1000px) or (round-screen: true) 表示当应用高度小于等于1000个像素单位或者设备屏幕是圆形时，条件成立。 |
| not | not操作符必须搭配screen使用，取反媒体查询结果，媒体查询结果不成立时返回true，否则返回false。例如：not screen and (min-height: 50px) and (max-height: 600px) 表示当应用高度小于50个像素单位或者大于600个像素单位时成立。 |
| only | only操作符必须搭配screen使用, 当前效果与单独使用screen相同。例如：only screen and (height <= 50) 。 |
| comma（, ） | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。其效果等同于or运算符。例如：screen and (min-height: 1000px), (round-screen: true) 表示当应用高度大于等于1000个像素单位或者设备屏幕是圆形时，条件成立。 |

媒体范围操作符包括<=，>=，<，>，详细解释说明如下表。

**表2** 媒体逻辑范围操作符

| 类型 | 说明 |
| --- | --- |
| <= | 小于等于，例如：screen and (height <= 50)。 |
| >= | 大于等于，例如：screen and (height >= 600)。 |
| < | 小于，例如：screen and (height < 50)。 |
| > | 大于，例如：screen and (height > 600)。 |

### 媒体特征（media-feature）

媒体特征包括应用显示区域的宽高、设备分辨率以及设备的宽高等属性，详细说明如下表。

**表3** 媒体特征说明表

比较height、width等宽高尺寸时，支持vp和px单位，无单位时默认为px。

| 类型 | 说明 |
| --- | --- |
| height | 应用页面可绘制区域的高度。 |
| min-height | 应用页面可绘制区域的最小高度。 |
| max-height | 应用页面可绘制区域的最大高度。 |
| width | 应用页面可绘制区域的宽度。 |
| min-width | 应用页面可绘制区域的最小宽度。 |
| max-width | 应用页面可绘制区域的最大宽度。 |
| resolution | 设备的分辨率，支持dpi，dppx和dpcm单位。其中：  - dpi表示每英寸中物理像素个数，1dpi ≈ 0.39dpcm；  - dpcm表示每厘米上的物理像素个数，1dpcm ≈ 2.54dpi；  - dppx表示每个px中的物理像素数（此单位按96px = 1英寸为基准，与页面中的px单位计算方式不同），1dppx = 96dpi。 |
| min-resolution | 设备的最小分辨率。 |
| max-resolution | 设备的最大分辨率。 |
| orientation | 屏幕的方向。  可选值：  - orientation: portrait（设备竖屏）；  - orientation: landscape（设备横屏）。 |
| device-height | 设备的高度。 |
| min-device-height | 设备的最小高度。 |
| max-device-height | 设备的最大高度。 |
| device-width | 设备的宽度。当前仅在应用初始化时保存一次，不会随设备宽度变化实时更新，例如折叠屏的折叠展开场景。 |
| device-type | 设备的类型。  可选值：default、phone、tablet、tv、car、wearable、2in1。 |
| min-device-width | 设备的最小宽度。 |
| max-device-width | 设备的最大宽度。 |
| round-screen | 屏幕类型，圆形屏幕为true，非圆形屏幕为false。 |
| dark-mode | 系统当前的深浅模式。可选值：true、false。  深色模式为true，浅色模式为false。 |

说明

目前在卡片中使用媒体查询，只支持height、width。

## 场景示例

下面给出两个媒体查询的使用示例。

示例一使用媒体查询，实现屏幕横竖屏切换时，为页面文本应用添加不同的内容和样式。

Stage模型下的示例：

```
1. import { mediaquery } from '@kit.ArkUI';
2. import { window } from '@kit.ArkUI';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct MediaQueryExample {
8. @State color: string = '#DB7093';
9. @State text: string = 'Portrait';
10. // 当设备横屏时条件成立
11. listener:mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');

13. // 当满足媒体查询条件时，触发回调
14. onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
15. if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的页面布局
16. this.color = '#FFD700';
17. this.text = 'Landscape';
18. } else {
19. this.color = '#DB7093';
20. this.text = 'Portrait';
21. }
22. }

24. aboutToAppear() {
25. // 绑定当前应用实例
26. // 绑定回调函数
27. this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
28. this.onPortrait(mediaQueryResult);
29. });
30. }

32. aboutToDisappear() {
33. // 解绑listener中注册的回调函数
34. this.listener.off('change');
35. }

37. // 改变设备横竖屏状态函数
38. private changeOrientation(isLandscape: boolean) {
39. // 获取UIAbility实例的上下文信息
40. let context:common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
41. // 调用该接口手动改变设备横竖屏状态
42. window.getLastWindow(context).then((lastWindow) => {
43. lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
44. });
45. }

47. build() {
48. Column({ space: 50 }) {
49. Text(this.text).fontSize(50).fontColor(this.color);
50. Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
51. .onClick(() => {
52. this.changeOrientation(true);
53. });
54. Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
55. .onClick(() => {
56. this.changeOrientation(false);
57. });
58. }
59. .width('100%').height('100%')
60. }
61. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MediaQuerySample/entry/src/main/ets/pages/Index.ets#L16-L94)

FA模型下的示例：

```
1. import { mediaquery } from '@kit.ArkUI';
2. import { featureAbility } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct MediaQueryExample {
7. @State color: string = '#DB7093';
8. @State text: string = 'Portrait';
9. listener:mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // 当设备横屏时条件成立

11. onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) { // 当满足媒体查询条件时，触发回调
12. if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的文本内容与字体颜色
13. this.color = '#FFD700';
14. this.text = 'Landscape';
15. } else {
16. this.color = '#DB7093';
17. this.text = 'Portrait';
18. }
19. }

21. aboutToAppear() {
22. // 绑定当前应用实例
23. this.listener.on('change', (mediaQueryResult:mediaquery.MediaQueryResult) => { this.onPortrait(mediaQueryResult) }); //绑定回调函数
24. }

26. aboutToDisappear() {
27. // 解绑listener中注册的回调函数
28. this.listener.off('change');
29. }

31. build() {
32. Column({ space: 50 }) {
33. Text(this.text).fontSize(50).fontColor(this.color)
34. Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
35. .onClick(() => {
36. let context = featureAbility.getContext();
37. context.setDisplayOrientation(0); //调用该接口手动改变设备横竖屏状态
38. })
39. Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
40. .onClick(() => {
41. let context = featureAbility.getContext();
42. context.setDisplayOrientation(1); //调用该接口手动改变设备横竖屏状态
43. })
44. }
45. .width('100%').height('100%')
46. }
47. }
```

**图1** 竖屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/U3AqHjT-TpadI3QqaIsOaQ/zh-cn_image_0000002552798408.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234010Z&HW-CC-Expire=86400&HW-CC-Sign=0D01ED930C74CB38FF7F8899A482261628DCD3658359F95CB3B011ECF0814ED9)

**图2** 横屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/gZemF17YTyiQw9ZZ82qjlA/zh-cn_image_0000002583438103.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234010Z&HW-CC-Expire=86400&HW-CC-Sign=E62AE4290DD5FCF3870FE78875FC978E6F2A34AEEDD4DDA62373445201EC3D95)

示例二使用媒体查询实现屏幕横竖屏切换时Flex组件的不同布局，竖屏时Flex采用垂直方向布局，横屏时采用水平方向布局。

```
1. import { LengthMetrics, mediaquery, window } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct MediaQueryExample {
7. @State color: string = '#DB7093';
8. @State text: string = 'Portrait';
9. @State dir: FlexDirection = FlexDirection.Column
10. @State textHeight: string = "30%"
11. @State textWidth: string = "100%"
12. // 当设备横屏时条件成立
13. listener: mediaquery.MediaQueryListener =
14. this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');

16. // 当满足媒体查询条件时，触发回调
17. onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
18. if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的文本内容与字体颜色
19. this.color = '#FFD700';
20. this.text = 'Landscape';
21. this.dir = FlexDirection.Row;
22. this.textHeight = "100%"
23. this.textWidth = "33%"
24. } else {
25. this.color = '#DB7093';
26. this.text = 'Portrait';
27. this.dir = FlexDirection.Column;
28. this.textHeight = "33%"
29. this.textWidth = "100%"
30. }
31. }

33. aboutToAppear() {
34. // 绑定当前应用实例
35. // 绑定回调函数
36. this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
37. this.onPortrait(mediaQueryResult)
38. });
39. }

41. aboutToDisappear() {
42. // 解绑listener中注册的回调函数
43. this.listener.off('change');
44. }

46. // 改变设备横竖屏状态函数
47. private changeOrientation(isLandscape: boolean) {
48. // 获取UIAbility实例的上下文信息
49. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
50. // 调用该接口手动改变设备横竖屏状态
51. window.getLastWindow(context).then((lastWindow) => {
52. lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT)
53. });
54. }

56. build() {
57. Column({ space: 30 }) {
58. Text(this.text).fontSize(24).fontColor(this.color)
59. Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
60. .onClick(() => {
61. this.changeOrientation(true);
62. })
63. Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
64. .onClick(() => {
65. this.changeOrientation(false);
66. })
67. Flex({ direction: this.dir, space: { main: LengthMetrics.vp(10), cross: LengthMetrics.vp(5) } }) {
68. Text('1')
69. .height(this.textHeight)
70. .width(this.textWidth)
71. .textAlign(TextAlign.Center)
72. .backgroundColor('rgb(0, 74, 175)')
73. Text('2')
74. .height(this.textHeight)
75. .width(this.textWidth)
76. .textAlign(TextAlign.Center)
77. .backgroundColor('rgb(39, 135, 217)')
78. Text('3')
79. .height(this.textHeight)
80. .width(this.textWidth)
81. .textAlign(TextAlign.Center)
82. .backgroundColor('rgb(240, 250, 255)')
83. }.layoutWeight(1)
84. .width("100%")
85. }
86. .width('100%').height('100%')
87. }
88. }
```

**图3** 竖屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/b1kdpezUT7amhFo4F-1y4A/zh-cn_image_0000002552958058.png?HW-CC-KV=V1&HW-CC-Date=20260427T234010Z&HW-CC-Expire=86400&HW-CC-Sign=68AF781AC0D19B5C8CB8153A0048CA22ECFA2D513F707F6838D59221307DCF13)

**图4** 横屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/xVINUTjNSa-znKgZSFNVZQ/zh-cn_image_0000002583478059.png?HW-CC-KV=V1&HW-CC-Date=20260427T234010Z&HW-CC-Expire=86400&HW-CC-Sign=5F243816A61F1128D0927284F535A7B5BE60B91F666D3F70F141548655BAF85F)
