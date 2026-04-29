---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation
title: 页面间转场 (pageTransition)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 页面间转场 (pageTransition)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:460f3d3e2700a61bc987d2407b6ac6e77ec7e68be85308480d628e5607c17fd4
---

当路由([router](js-apis-router.md))进行切换时，可以通过在[pageTransition](ts-custom-component-lifecycle.md#pagetransition9)函数中自定义页面入场和页面退场的转场动效。详细指导请参考[页面转场动画](../harmonyos-guides/arkts-page-transition-animation.md)。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

为了实现更好的转场效果，推荐使用[Navigation组件](../harmonyos-guides/arkts-navigation-architecture.md)和[模态转场](../harmonyos-guides/arkts-modal-transition.md)。

## PageTransitionEnter

PhonePC/2in1TabletTVWearable

PageTransitionEnter(value: PageTransitionOptions)

设置当前页面的自定义入场动效。继承自[CommonTransition](ts-page-transition-animation.md#commontransition)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](ts-page-transition-animation.md#pagetransitionoptions对象说明) | 是 | 配置入场动效的参数。 |

### onEnter

PhonePC/2in1TabletTVWearable

onEnter(event: PageTransitionCallback): PageTransitionEnterInterface

逐帧回调，直到入场动画结束，progress从0变化到1。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](ts-page-transition-animation.md#pagetransitioncallback18) | 是 | 入场动画的逐帧回调直到入场动画结束，progress从0变化到1。 |

**示例：**

```
1. pageTransition() {
2. PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
3. // 转场动画时入场动画 type 为路由类型 ，progress为从0到1逐渐变大
4. .onEnter((type: RouteType, progress: number) => {
5. // 业务逻辑代码
6. })
7. }
```

## PageTransitionExit

PhonePC/2in1TabletTVWearable

PageTransitionExit(value: PageTransitionOptions)

设置当前页面的自定义退场动效。继承自[CommonTransition](ts-page-transition-animation.md#commontransition)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](ts-page-transition-animation.md#pagetransitionoptions对象说明) | 是 | 配置退场动效的参数。 |

### onExit

PhonePC/2in1TabletTVWearable

onExit(event: PageTransitionCallback): PageTransitionExitInterface

逐帧回调，直到出场动画结束，progress从0变化到1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](ts-page-transition-animation.md#pagetransitioncallback18) | 是 | 出场动画的逐帧回调直到出场动画结束，progress从0变化到1。 |

**示例：**

```
1. pageTransition() {
2. PageTransitionExit({ duration: 1200, curve: Curve.Linear })
3. // 转场动画时出场动画 type 为路由类型 ，progress为从0到1逐渐变大
4. .onExit((type: RouteType, progress: number) => {
5. // 业务逻辑代码
6. })
7. }
```

## PageTransitionOptions对象说明

PhonePC/2in1TabletTVWearable

退场/进场动效的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [RouteType](ts-page-transition-animation.md#routetype枚举说明) | 否 | 是 | 页面转场效果生效的路由类型。  默认值：RouteType.None。 |
| duration | number | 否 | 是 | 动画的时长。  单位：毫秒  默认值：1000  取值范围：[0, +∞) |
| curve | [Curve](ts-appendix-enums.md#curve) | string | [ICurve](js-apis-curve.md#icurve9)10+ | 否 | 是 | 动画曲线。  推荐以Curve或ICurve形式指定。  当类型为string时，为动画插值曲线，取值参考[AnimateParam](ts-explicit-animation.md#animateparam对象说明)的curve参数。  默认值：Curve.Linear |
| delay | number | 否 | 是 | 动画延迟时长。  单位：毫秒  默认值：0  **说明：**  没有匹配时使用系统默认的页面转场效果(根据设备可能会有差异)，如需禁用系统默认页面转场效果，可以指定duration为0。 |

## CommonTransition

PhonePC/2in1TabletTVWearable

页面转场通用动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor()

转场通用动效的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### slide

PhonePC/2in1TabletTVWearable

slide(value: SlideEffect): T

设置页面转场时的滑入滑出效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SlideEffect](ts-page-transition-animation.md#slideeffect枚举说明) | 是 | 页面转场时的滑入滑出效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

### translate

PhonePC/2in1TabletTVWearable

translate(value: TranslateOptions): T

设置页面转场时的平移效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明) | 是 | 设置页面转场时的平移效果，为入场时起点和退场时终点的值，和slide同时设置时默认生效slide。  - x：横向的平移距离。  - y：纵向的平移距离。  - z：竖向的平移距离。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

### scale

PhonePC/2in1TabletTVWearable

scale(value: ScaleOptions): T

设置页面转场时的缩放效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明) | 是 | 设置页面转场时的缩放效果，为入场时起点和退场时终点的值。  - x：横向放大倍数（或缩小比例）。  - y：纵向放大倍数（或缩小比例）。  - z：竖向放大倍数（或缩小比例）。  - centerX、centerY缩放中心点。centerX和centerY默认值是"50%"，即默认以页面的中心点为旋转中心点。  - 中心点为(0, 0)代表页面的左上角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

### opacity

PhonePC/2in1TabletTVWearable

opacity(value: number): T

设置入场的起点透明度值或者退场的终点透明度值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置入场的起点透明度值或者退场的终点透明度值。  取值范围：[0, 1] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## PageTransitionCallback18+

PhonePC/2in1TabletTVWearable

type PageTransitionCallback = (type: RouteType, progress: number) => void

页面转场事件回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [RouteType](ts-page-transition-animation.md#routetype枚举说明) | 是 | 页面转场类型。 |
| progress | number | 是 | 转场进度。progress从0变化到1。 |

## RouteType枚举说明

PhonePC/2in1TabletTVWearable

页面转场类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | 页面未重定向。如Push和Pop描述中RouteType为None的情形，即页面进场时PageTransitionEnter的转场效果生效；退场时PageTransitionExit的转场效果生效。 |
| Push | 1 | 跳转到下一页面。PageA跳转到下一个新的界面PageB。对于PageA，指定RouteType为None或者Push的PageTransitionExit组件样式生效，对于PageB，指定RouteType为None或者Push的PageTransitionEnter组件样式生效。 |
| Pop | 2 | 重定向指定页面。从PageB回退到之前的页面PageA。对于PageB，指定RouteType为None或者Pop的PageTransitionExit组件样式生效，对于PageA，指定RouteType为None或者Pop的PageTransitionEnter组件样式生效。 |

## SlideEffect枚举说明

PhonePC/2in1TabletTVWearable

页面转场时的滑入滑出效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Left | 1 | 设置到入场时表示从左边滑入，出场时表示滑出到左边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Right | 2 | 设置到入场时表示从右边滑入，出场时表示滑出到右边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Top | 3 | 设置到入场时表示从上边滑入，出场时表示滑出到上边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Bottom | 4 | 设置到入场时表示从下边滑入，出场时表示滑出到下边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| START12+ | 5 | 设置LTR入场时表示从左边滑入，出场时表示滑出到左边。RTL入场时表示从右边滑入，出场时表示滑出到右边。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| END12+ | 6 | 设置LTR入场时表示从右边滑入，出场时表示滑出到右边。RTL入场时表示从左边滑入，出场时表示滑出到左边。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置退入场动画）

自定义方式1：通过不同的退入场类型配置不同的退场，入场动画。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. @State scale1: number = 1;
6. @State opacity1: number = 1;

8. build() {
9. Column() {
10. // $r("app.media.transition_image1")需要替换为开发者所需的图像资源文件。
11. Image($r("app.media.transition_image1")).width('100%').height('100%')
12. }
13. .width('100%')
14. .height('100%')
15. .scale({ x: this.scale1 })
16. .opacity(this.opacity1)
17. .onClick(() => {
18. this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
19. })
20. }

22. pageTransition() {
23. PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
24. .onEnter((type: RouteType, progress: number) => {
25. if (type == RouteType.Push || type == RouteType.Pop) {
26. this.scale1 = progress;
27. this.opacity1 = progress;
28. }
29. })
30. PageTransitionExit({ duration: 1200, curve: Curve.Ease })
31. .onExit((type: RouteType, progress: number) => {
32. if (type == RouteType.Push) {
33. this.scale1 = 1 - progress;
34. this.opacity1 = 1 - progress;
35. }
36. })
37. }
38. }
```

```
1. // Page1.ets
2. @Entry
3. @Component
4. struct Page1 {
5. @State scale2: number = 1;
6. @State opacity2: number = 1;

8. build() {
9. Column() {
10. // $r("app.media.transition_image2")需要替换为开发者所需的图像资源文件。
11. Image($r("app.media.transition_image2")).width('100%').height('100%') // 图片存放在media文件夹下
12. }
13. .width('100%')
14. .height('100%')
15. .scale({ x: this.scale2 })
16. .opacity(this.opacity2)
17. .onClick(() => {
18. this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
19. })
20. }

22. pageTransition() {
23. PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
24. .onEnter((type: RouteType, progress: number) => {
25. if (type == RouteType.Push || type == RouteType.Pop) {
26. this.scale2 = progress;
27. }
28. this.opacity2 = progress;
29. })
30. PageTransitionExit({ duration: 1200, curve: Curve.Ease })
31. .onExit((type: RouteType, progress: number) => {
32. if (type == RouteType.Pop) {
33. this.scale2 = 1 - progress;
34. this.opacity2 = 1 - progress;
35. }
36. })
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ErXeeD7MTiCqMHyHb5qNzg/zh-cn_image_0000002558606890.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=AD7EACFA38883BB697B42BE79D8662777B90EA79DBD6A7747F531D5DA83C5FCB)

自定义方式2：配置了当前页面的入场动画为从左侧滑入，退场为平移加透明度变化。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. // $r('app.media.bg1')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.bg1')).width('100%').height('100%') // 图片存放在media文件夹下
9. }
10. .onClick(() => {
11. this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
12. })
13. }

15. // 自定义方式2：使用系统提供的多种默认效果(平移、缩放、透明度等)
16. pageTransition() {
17. // 该页面进入动画时长为1200ms，尽量与另一页面的退出动画时长匹配
18. PageTransitionEnter({ duration: 1200 })
19. .slide(SlideEffect.Left)
20. // 该页面退出动画时长为1000ms，尽量与另一页面的进入动画时长匹配
21. PageTransitionExit({ duration: 1000 })
22. .translate({ x: 100.0, y: 100.0 })
23. .opacity(0)
24. }
25. }
```

```
1. // Page1.ets
2. @Entry
3. @Component
4. struct Page1 {
5. build() {
6. Column() {
7. // $r('app.media.bg2')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.bg2')).width('100%').height('100%') // 图片存放在media文件夹下
9. }
10. .onClick(() => {
11. this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
12. })
13. }

15. // 自定义方式2：使用系统提供的多种默认效果(平移、缩放、透明度等)
16. pageTransition() {
17. // 该页面进入动画时长为1000ms，尽量与另一页面的退出动画时长匹配
18. PageTransitionEnter({ duration: 1000 })
19. .slide(SlideEffect.Left)
20. // 该页面退出动画时长为1200ms，尽量与另一页面的进入动画时长匹配
21. PageTransitionExit({ duration: 1200 })
22. .translate({ x: 100.0, y: 100.0 })
23. .opacity(0)
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/QqMjtnOAQJK6acvklGi2PA/zh-cn_image_0000002589326417.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=64E6CF00EB6A8713562AC5F47EA19F46E5B3CD930FF14A20C04F54939C899DEC)

### 示例2（设置退入场平移效果）

自定义方式1：配置提供的不同退入场平移效果，将系统语言排版模式改为RTL。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. @State scale1: number = 1;
6. @State opacity1: number = 1;

8. build() {
9. Column() {
10. Button("页面1").onClick(() => {
11. this.getUIContext().getRouter().pushUrl({
12. url: "pages/Page1"
13. })
14. })
15. .width(200)
16. .height(60)
17. .fontSize(36)
18. Text("START")
19. .fontSize(36)
20. .textAlign(TextAlign.Center)
21. }
22. .scale({ x: this.scale1 })
23. .opacity(this.opacity1)
24. .height("100%")
25. .width("100%")
26. .justifyContent(FlexAlign.Center)
27. }

29. // 自定义方式2：使用系统提供的多种默认效果(平移、缩放、透明度等)
30. pageTransition() {
31. // 设置入场动效
32. PageTransitionEnter({ duration: 200 })
33. .slide(SlideEffect.START)
34. // 设置退场动效
35. PageTransitionExit({ delay: 100 })
36. .slide(SlideEffect.START) //Left
37. }
38. }
```

```
1. // Page1.ets
2. @Entry
3. @Component
4. struct Page1 {
5. @State scale1: number = 1;
6. @State opacity1: number = 1;

8. build() {
9. Column() {
10. Button("页面2").onClick(() => {
11. this.getUIContext().getRouter().pushUrl({
12. url: "pages/Index"
13. });
14. })
15. .width(200)
16. .height(60)
17. .fontSize(36)
18. Text("END")
19. .fontSize(36)
20. .textAlign(TextAlign.Center)
21. }
22. .scale({ x: this.scale1 })
23. .opacity(this.opacity1)
24. .height("100%")
25. .width("100%")
26. .justifyContent(FlexAlign.Center)
27. }

29. // 自定义方式2：使用系统提供的多种默认效果(平移、缩放、透明度等)
30. pageTransition() {
31. PageTransitionEnter({ duration: 200 })
32. .slide(SlideEffect.END) //Right
33. PageTransitionExit({ delay: 100 })
34. .slide(SlideEffect.END) //Right
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/xNsrdz2XSqGMLnMrI-cUUw/zh-cn_image_0000002589246359.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=386C00D7B17BBCEA9621A6B1336FF6EA51E7B5F95CDFA2E8B4A51E2775BC0CFE)

自定义方式2：使用系统默认的退入场效果，将系统语言排版模式改为RTL。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. @State scale1: number = 1;
6. @State opacity1: number = 1;

8. build() {
9. Column() {
10. Button("页面1").onClick(() => {
11. this.getUIContext().getRouter().pushUrl({
12. url: "pages/Page1"
13. });
14. })
15. .width(200)
16. .height(60)
17. .fontSize(36)
18. }
19. .scale({ x: this.scale1 })
20. .opacity(this.opacity1)
21. .height("100%")
22. .width("100%")
23. .justifyContent(FlexAlign.Center)
24. }
25. }
```

```
1. // Page1.ets
2. @Entry
3. @Component
4. struct Page1 {
5. @State scale1: number = 1;
6. @State opacity1: number = 1;

8. build() {
9. Column() {
10. Button("页面2").onClick(() => {
11. this.getUIContext().getRouter().pushUrl({
12. url: "pages/Index"
13. });
14. })
15. .width(200)
16. .height(60)
17. .fontSize(36)
18. }
19. .scale({ x: this.scale1 })
20. .opacity(this.opacity1)
21. .height("100%")
22. .width("100%")
23. .justifyContent(FlexAlign.Center)
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/HP7i2al0QGuaEm9eyvBjIw/zh-cn_image_0000002558766552.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=ACF7F4A2D6A37143ADF9E32B8B9CA3E29CCAAF05EB677B5DBB96E64D79B8C54C)
