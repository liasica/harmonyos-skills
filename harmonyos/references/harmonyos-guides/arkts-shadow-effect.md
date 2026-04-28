---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shadow-effect
title: 阴影
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画效果 > 阴影
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f02a7817e630f536b7fd1f5ec900e7ea36871b8ef958851caf90cc3983e4a19b
---

阴影接口[shadow](../harmonyos-references/ts-universal-attributes-image-effect.md#shadow)可以为当前组件添加阴影效果，该接口支持两种类型参数，开发者可配置[ShadowOptions](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)自定义阴影效果。ShadowOptions模式下，当radius = 0或者color的透明度为0时，无阴影效果。

```
1. @Entry
2. @Component
3. struct ShadowOptionDemo {
4. build() {
5. Row() {
6. Column() {
7. Column() {
8. Text('shadowOption').fontSize(12)
9. }
10. .width(100)
11. .aspectRatio(1)
12. .margin(10)
13. .justifyContent(FlexAlign.Center)
14. .backgroundColor(Color.White)
15. .borderRadius(20)
16. .shadow({ radius: 10, color: Color.Gray })

18. Column() {
19. Text('shadowOption').fontSize(12)
20. }
21. .width(100)
22. .aspectRatio(1)
23. .margin(10)
24. .justifyContent(FlexAlign.Center)
25. .backgroundColor('#a8a888')
26. .borderRadius(20)
27. .shadow({
28. radius: 10,
29. color: Color.Gray,
30. offsetX: 20,
31. offsetY: 20
32. })
33. }
34. .width('100%')
35. .height('100%')
36. .justifyContent(FlexAlign.Center)
37. }
38. .height('100%')
39. }
40. }
```

[Shadow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Shadow/entry/src/main/ets/pages/Shadow.ets#L16-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/duaKrTvRQTa7qTV51NrzUw/zh-cn_image_0000002552798352.png?HW-CC-KV=V1&HW-CC-Date=20260427T233958Z&HW-CC-Expire=86400&HW-CC-Sign=1F6CD4FBCC06C74D0BE785C3DF6FD9AA9D92CE1AA0BAB025A31756625CAE5795)
