---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-animation
title: 请求动画绘制帧率
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 使用可变帧率能力定制不同内容的绘制帧率 > 请求动画绘制帧率
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:77006273aac3375555e17d69a8a14105363f658520fa7576fccd4568bd204ed8
---

在应用开发中，[属性动画](../harmonyos-references/ts-animatorproperty.md)和[显式动画](../harmonyos-references/ts-explicit-animation.md)能够使用可选参数[ExpectedFrameRateRange](../harmonyos-references/ts-explicit-animation.md#expectedframeraterange11)，为不同的动画配置不同的期望绘制帧率。

## 请求属性动画的绘制帧率

定义文本组件的属性动画，请求绘制帧率为60，范例如下：

```
1. Text('60')
2. // ...
3. .animation({
4. duration: 1200,
5. iterations: 10,
6. // ...
7. expectedFrameRateRange: {
8. expected: 60,
9. min: 0,
10. max: 120,
11. },
12. })
```

[PropertyAnimationDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/PropertyAnimationDisplaySync.ets#L66-L91)

## 请求显式动画的绘制帧率

定义按钮组件的显式动画，请求绘制帧率为30，范例如下：

```
1. Button('Start')
2. // ...
3. .onClick(() => {
4. // ...

6. this.uiContext?.animateTo({
7. duration: 1200,
8. iterations: 10,
9. // ...
10. expectedFrameRateRange: {
11. expected: 30,
12. min: 0,
13. max: 120,
14. },
15. }, () => {
16. // ...
17. })

19. // ...
20. })
```

[PropertyAnimationDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/PropertyAnimationDisplaySync.ets#L96-L143)
