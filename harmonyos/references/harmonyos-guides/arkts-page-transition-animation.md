---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-transition-animation
title: 页面转场动画 (不推荐)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 页面转场动画 (不推荐)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24e924ab4914c7e2e5c09ebfc81f17b42b5e4a3498214330c7b3fce07a47975f
---

为了实现更好的转场效果，推荐使用[Navigation转场动画](arkts-navigation-animation.md)和[模态转场](arkts-modal-transition.md)。

两个页面间发生跳转，一个页面消失，另一个页面出现，这时可以配置各自页面的页面转场参数实现自定义的页面转场效果。[页面转场](../harmonyos-references/ts-page-transition-animation.md)效果写在pageTransition函数中，通过[PageTransitionEnter](../harmonyos-references/ts-page-transition-animation.md#pagetransitionenter)和[PageTransitionExit](../harmonyos-references/ts-page-transition-animation.md#pagetransitionexit)指定页面进入和退出的动画效果。

pageTransition的函数为：

```
1. pageTransition() {
2. PageTransitionEnter()
3. PageTransitionExit()
4. }
```

PageTransitionEnter的接口为：

```
1. PageTransitionEnter({ type?: RouteType, duration?: number, curve?: Curve | string, delay?: number })
```

PageTransitionExit的接口为：

```
1. PageTransitionExit({ type?: RouteType, duration?: number, curve?: Curve | string, delay?: number })
```

上述接口定义了PageTransitionEnter和PageTransitionExit组件，可通过[slide](../harmonyos-references/ts-page-transition-animation.md#slide)、[translate](../harmonyos-references/ts-page-transition-animation.md#translate)、[scale](../harmonyos-references/ts-page-transition-animation.md#scale)、[opacity](../harmonyos-references/ts-page-transition-animation.md#opacity)属性定义不同的页面转场效果。对于PageTransitionEnter而言，这些效果表示入场时起点值，对于PageTransitionExit而言，这些效果表示退场的终点值，这一点与组件转场[transition](../harmonyos-references/ts-transition-animation-component.md)配置方法类似。此外，PageTransitionEnter提供了onEnter接口进行自定义页面入场动画的回调，PageTransitionExit提供了onExit接口进行自定义页面退场动画的回调。

上述接口中的参数type，表示路由生效的类型，这一点开发者容易混淆其含义。页面转场的两个页面，必定有一个页面退出，一个页面进入。如果通过[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)操作从页面A跳转到页面B，则页面A退出，做页面退场动画，页面B进入，做页面入场动画。如果通过[back](../harmonyos-references/arkts-apis-uicontext-router.md#back)操作从页面B返回到页面A，则页面B退出，做页面退场动画，页面A进入，做页面入场动画。即页面的PageTransitionEnter既可能是由于新增页面(push，入栈)引起的新页面的入场动画，也可能是由于页面返回(back，或pop，出栈)引起的页面栈中老页面的入场动画，为了能区分这两种形式的入场动画，提供了type参数，这样开发者能完全定义所有类型的页面转场效果。

## type配置为RouteType.None

type为RouteType.None表示对页面栈的push、pop操作均生效，type的默认值为RouteType.None。

```
1. // page A
2. pageTransition() {
3. // 定义页面进入时的效果，从左侧滑入，时长为1200ms，无论页面栈发生push还是pop操作均可生效
4. PageTransitionEnter({ type: RouteType.None, duration: 1200 })
5. .slide(SlideEffect.Left)
6. // 定义页面退出时的效果，向左侧滑出，时长为1000ms，无论页面栈发生push还是pop操作均可生效
7. PageTransitionExit({ type: RouteType.None, duration: 1000 })
8. .slide(SlideEffect.Left)
9. }
```

[PageTransitionSrc3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template5/PageTransitionSrc3.ets#L45-L55)

```
1. // page B
2. pageTransition() {
3. // 定义页面进入时的效果，从右侧滑入，时长为1000ms，无论页面栈发生push还是pop操作均可生效
4. PageTransitionEnter({ type: RouteType.None, duration: 1000 })
5. .slide(SlideEffect.Right)
6. // 定义页面退出时的效果，向右侧滑出，时长为1200ms，无论页面栈发生push还是pop操作均可生效
7. PageTransitionExit({ type: RouteType.None, duration: 1200 })
8. .slide(SlideEffect.Right)
9. }
```

[PageTransitionDst3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template5/PageTransitionDst3.ets#L45-L55)

假设页面跳转配置为多实例模式，即页面栈中允许存在重复的页面。可能会有4种场景，对应的页面转场效果如下表。

| 路由操作 | 页面A转场效果 | 页面B转场效果 |
| --- | --- | --- |
| pushUrl，从页面A跳转到新增的页面B | 页面退出，PageTransitionExit生效，向左侧滑出屏幕 | 页面进入，PageTransitionEnter生效，从右侧滑入屏幕 |
| back，从页面B返回到页面A | 页面进入，PageTransitionEnter生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit生效，向右侧滑出屏幕 |
| pushUrl，从页面B跳转到新增的页面A | 页面进入，PageTransitionEnter生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit生效，向右侧滑出屏幕 |
| back，从页面A返回到页面B | 页面退出，PageTransitionExit生效，向左侧滑出屏幕 | 页面进入，PageTransitionEnter生效，从右侧滑入屏幕 |

如果希望pushUrl进入的页面总是从右侧滑入，back时退出的页面总是从右侧滑出，则上表中的第3、4种情况不满足要求，那么需要完整的定义4个页面转场效果。

## type配置为RouteType.Push或RouteType.Pop

[type](../harmonyos-references/ts-page-transition-animation.md#pagetransitionoptions对象说明)为[RouteType.Push](../harmonyos-references/ts-page-transition-animation.md#routetype枚举说明)表示仅对页面栈的push操作生效，type为RouteType.Pop表示仅对页面栈的pop操作生效。

```
1. // page A
2. pageTransition() {
3. // 定义页面进入时的效果，从右侧滑入，时长为1200ms，页面栈发生push操作时该效果才生效
4. PageTransitionEnter({ type: RouteType.Push, duration: 1200 })
5. .slide(SlideEffect.Right)
6. // 定义页面进入时的效果，从左侧滑入，时长为1200ms，页面栈发生pop操作时该效果才生效
7. PageTransitionEnter({ type: RouteType.Pop, duration: 1200 })
8. .slide(SlideEffect.Left)
9. // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
10. PageTransitionExit({ type: RouteType.Push, duration: 1000 })
11. .slide(SlideEffect.Left)
12. // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
13. PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
14. .slide(SlideEffect.Right)
15. }
```

[PageTransitionSrc4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template6/PageTransitionSrc4.ets#L45-L61)

```
1. // page B
2. pageTransition() {
3. // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
4. PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
5. .slide(SlideEffect.Right)
6. // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
7. PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
8. .slide(SlideEffect.Left)
9. // 定义页面退出时的效果，向左侧滑出，时长为1200ms，页面栈发生push操作时该效果才生效
10. PageTransitionExit({ type: RouteType.Push, duration: 1200 })
11. .slide(SlideEffect.Left)
12. // 定义页面退出时的效果，向右侧滑出，时长为1200ms，页面栈发生pop操作时该效果才生效
13. PageTransitionExit({ type: RouteType.Pop, duration: 1200 })
14. .slide(SlideEffect.Right)
15. }
```

[PageTransitionDst4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template6/PageTransitionDst4.ets#L45-L61)

以上代码则完整的定义了所有可能的页面转场样式。假设页面跳转配置为多实例模式，即页面栈中允许存在重复的页面。可能会有4种场景，对应的页面转场效果如下表。

| 路由操作 | 页面A转场效果 | 页面B转场效果 |
| --- | --- | --- |
| pushUrl，从页面A跳转到新增的页面B | 页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕 | 页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕 |
| back，从页面B返回到页面A | 页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕 |
| pushUrl，从页面B跳转到新增的页面A | 页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕 | 页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕 |
| back，从页面A返回到页面B | 页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕 | 页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕 |

说明

* 由于每个页面的页面转场样式都可由开发者独立配置，而页面转场涉及到两个页面，开发者应考虑两个页面的页面转场效果的衔接，如时长尽量保持一致。
* 如果没有定义匹配的页面转场样式，则该页面使用系统默认的页面转场样式。

## 禁用某页面的页面转场

通过设置页面转场的时长为0，可使该页面无页面转场动画。

```
1. pageTransition() {
2. PageTransitionEnter({ type: RouteType.None, duration: 0 })
3. PageTransitionExit({ type: RouteType.None, duration: 0 })
4. }
```

## 场景示例

下面介绍了利用[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)跳转能力定义了所有的四种页面转场样式的页面转场动画示例。

```
1. // PageTransitionSrc1
2. @Entry
3. @Component
4. struct PageTransitionSrc1 {
5. build() {
6. Column() {
7. // 请将$r('app.media.mountain')替换为实际资源文件
8. Image($r('app.media.mountain'))
9. .width('90%')
10. .height('80%')
11. .objectFit(ImageFit.Fill)
12. .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
13. .margin(30)

15. Row({ space: 10 }) {
16. Button('pushUrl')
17. .onClick(() => {
18. // 路由到下一个页面，push操作
19. this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template3/pageTransitionDst1' });
20. })
21. Button('back')
22. .onClick(() => {
23. // 返回到上一页面，相当于pop操作
24. this.getUIContext().getRouter().back();
25. })
26. }.justifyContent(FlexAlign.Center)
27. }
28. .width('100%').height('100%')
29. .alignItems(HorizontalAlign.Center)
30. }

32. pageTransition() {
33. // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
34. PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
35. .slide(SlideEffect.Right)
36. // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
37. PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
38. .slide(SlideEffect.Left)
39. // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
40. PageTransitionExit({ type: RouteType.Push, duration: 1000 })
41. .slide(SlideEffect.Left)
42. // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
43. PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
44. .slide(SlideEffect.Right)
45. }
46. }
```

[pageTransitionSrc1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template3/pageTransitionSrc1.ets#L15-L62)

```
1. // PageTransitionDst1
2. @Entry
3. @Component
4. struct PageTransitionDst1 {
5. build() {
6. Column() {
7. // 请将$r('app.media.forest')替换为实际资源文件
8. Image($r('app.media.forest'))
9. .width('90%')
10. .height('80%')
11. .objectFit(ImageFit.Fill)
12. .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
13. .margin(30)

15. Row({ space: 10 }) {
16. Button('pushUrl')
17. .onClick(() => {
18. // 路由到下一页面，push操作
19. this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template3/pageTransitionSrc1' });
20. })
21. Button('back')
22. .onClick(() => {
23. // 返回到上一页面，相当于pop操作
24. this.getUIContext().getRouter().back();
25. })
26. }.justifyContent(FlexAlign.Center)
27. }
28. .width('100%').height('100%')
29. .alignItems(HorizontalAlign.Center)
30. }

32. pageTransition() {
33. // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
34. PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
35. .slide(SlideEffect.Right)
36. // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
37. PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
38. .slide(SlideEffect.Left)
39. // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
40. PageTransitionExit({ type: RouteType.Push, duration: 1000 })
41. .slide(SlideEffect.Left)
42. // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
43. PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
44. .slide(SlideEffect.Right)
45. }
46. }
```

[pageTransitionDst1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template3/pageTransitionDst1.ets#L15-L62)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Dtyhsix8Q1uY3Lrzf56TeA/zh-cn_image_0000002558604826.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=D15D9EB8AEEDB4367EF80C524D442EE0683FA3BBFCD7FF213F2D1586A8EE4FCD)

下面介绍使用了type为None的页面转场动画示例。

```
1. // PageTransitionSrc2
2. @Entry
3. @Component
4. struct PageTransitionSrc2 {
5. build() {
6. Column() {
7. // 请将$r('app.media.mountain')替换为实际资源文件
8. Image($r('app.media.mountain'))
9. .width('90%')
10. .height('80%')
11. .objectFit(ImageFit.Fill)
12. .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
13. .margin(30)

15. Row({ space: 10 }) {
16. Button('pushUrl')
17. .onClick(() => {
18. // 路由到下一页面，push操作
19. this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template4/pageTransitionDst2' });
20. })
21. Button('back')
22. .onClick(() => {
23. // 返回到上一页面，相当于pop操作
24. this.getUIContext().getRouter().back();
25. })
26. }.justifyContent(FlexAlign.Center)
27. }
28. .width('100%').height('100%')
29. .alignItems(HorizontalAlign.Center)
30. }

32. pageTransition() {
33. // 定义页面进入时的效果，从左侧滑入，时长为1000ms，无论页面栈发生push还是pop操作均可生效
34. PageTransitionEnter({ duration: 1000 })
35. .slide(SlideEffect.Left)
36. // 定义页面退出时的效果，相对于正常页面位置x方向平移100vp，y方向平移100vp，透明度变为0，时长为1200ms，无论页面栈发生push还是pop操作均可生效
37. PageTransitionExit({ duration: 1200 })
38. .translate({ x: 100.0, y: 100.0 })
39. .opacity(0)
40. }
41. }
```

[pageTransitionSrc2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template4/pageTransitionSrc2.ets#L15-L57)

```
1. // PageTransitionDst2
2. @Entry
3. @Component
4. struct PageTransitionDst2 {
5. build() {
6. Column() {
7. // 请将$r('app.media.forest')替换为实际资源文件
8. Image($r('app.media.forest'))
9. .width('90%')
10. .height('80%')
11. .objectFit(ImageFit.Fill)
12. .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
13. .margin(30)

15. Row({ space: 10 }) {
16. Button('pushUrl')
17. .onClick(() => {
18. // 路由到下一页面，push操作
19. this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template4/pageTransitionSrc2' });
20. })
21. Button('back')
22. .onClick(() => {
23. // 返回到上一页面，相当于pop操作
24. this.getUIContext().getRouter().back();
25. })
26. }.justifyContent(FlexAlign.Center)
27. }
28. .width('100%').height('100%')
29. .alignItems(HorizontalAlign.Center)
30. }

32. pageTransition() {
33. // 定义页面进入时的效果，从左侧滑入，时长为1200ms，无论页面栈发生push还是pop操作均可生效
34. PageTransitionEnter({ duration: 1200 })
35. .slide(SlideEffect.Left)
36. // 定义页面退出时的效果，相对于正常页面位置x方向平移100vp，y方向平移100vp，透明度变为0，时长为1000ms，无论页面栈发生push还是pop操作均可生效
37. PageTransitionExit({ duration: 1000 })
38. .translate({ x: 100.0, y: 100.0 })
39. .opacity(0)
40. }
41. }
```

[pageTransitionDst2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/pageTransition/template4/pageTransitionDst2.ets#L15-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/VlOHW2GRSEua5uJZbRHnig/zh-cn_image_0000002589324351.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=94A0E7968C985762271E4A6264CCB0982260A9ADE10CD2C023D4F6A73C49AD04)
