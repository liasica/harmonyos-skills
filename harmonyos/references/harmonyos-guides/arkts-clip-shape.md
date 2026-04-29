---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-clip-shape
title: 形状裁剪（clipShape）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 几何图形绘制 > 形状裁剪（clipShape）
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5fb8c4f93f3ff745e25ca9e7d4192e744964df11222478dcc3fc48c64f499a3a
---

可利用[clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)接口将组件裁剪为所需的形状。调用该接口后，可以保留该形状覆盖的组件部分，同时移除组件的其余部分。裁剪形状本身是不可见的。

说明

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度，具体形状支持的属性参考具体[形状](../harmonyos-references/js-apis-arkui-shape.md)的文档。

形状中的[fill](../harmonyos-references/js-apis-arkui-shape.md#fill)属性对clipShape接口不生效。

## 裁剪圆形

通过设置CircleShape，将图片裁剪为圆形。

```
1. // xxx.ets
2. import { CircleShape } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ClipShapeExample {
7. build() {
8. Column({ space: 15 }) {
9. // 用一个280px直径的圆对图片进行裁剪
10. // 请将$r('app.media.background')替换为实际资源文件
11. Image($r('app.media.background'))
12. .clipShape(new CircleShape({ width: '280px', height: '280px' }))
13. .width('500px').height('280px')

15. // 用一个350px直径的圆对图片进行裁剪
16. // 请将$r('app.media.background')替换为实际资源文件
17. Image($r('app.media.background'))
18. .clipShape(new CircleShape({ width: '350px', height: '350px' }))
19. .width('500px').height('370px')
20. }
21. .width('100%')
22. .margin({ top: 15 })
23. }
24. }
```

[ClipShapeExample1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample1.ets#L15-L40)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/abOw0pOQR6aahOBgdDQXJQ/zh-cn_image_0000002558604770.png?HW-CC-KV=V1&HW-CC-Date=20260429T052800Z&HW-CC-Expire=86400&HW-CC-Sign=3719D74D23ABD8BE309F5FDE5FE007A4315585D1BDC58F208CE20163D5815473)

## 裁剪椭圆形

通过设置EllipseShape，将图片裁剪为椭圆形。

```
1. // xxx.ets
2. import { EllipseShape } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ClipShapeExample {
7. build() {
8. Column({ space: 15 }) {
9. // 请将$r('app.media.background')替换为实际资源文件
10. Image($r('app.media.background'))
11. .clipShape(new EllipseShape({ width: '280px', height: '200px' }))
12. .width('500px').height('400px')

14. // 请将$r('app.media.background')替换为实际资源文件
15. Image($r('app.media.background'))
16. .clipShape(new EllipseShape({ width: '380px', height: '280px' }))
17. .width('500px').height('400px')
18. }
19. .width('100%')
20. .margin({ top: 15 })
21. }
22. }
```

[ClipShapeExample2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample2.ets#L15-L38)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/9MirZ29LSDuPvISz7HvGkw/zh-cn_image_0000002589324295.png?HW-CC-KV=V1&HW-CC-Date=20260429T052800Z&HW-CC-Expire=86400&HW-CC-Sign=F1183E5561A137350EAD73EC6637EFF5FBB2CA717ED62534C86F29F1B625873F)

## 裁剪矩形

通过设置RectShape，将图片裁剪为矩形。

```
1. // xxx.ets
2. import { RectShape } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ClipShapeExample {
7. build() {
8. Column({ space: 15 }) {
9. // 请将$r('app.media.background')替换为实际资源文件
10. Image($r('app.media.background'))
11. .clipShape(new RectShape({ width: '200px', height: '200px' }))
12. .width('500px').height('400px')

14. // 请将$r('app.media.background')替换为实际资源文件
15. Image($r('app.media.background'))
16. .clipShape(new RectShape({ width: '380px', height: '280px' }))
17. .width('500px').height('400px')
18. }
19. .width('100%')
20. .margin({ top: 15 })
21. }
22. }
```

[ClipShapeExample3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample3.ets#L15-L38)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/XKFl4fw8R6yc0Yitv-0yHw/zh-cn_image_0000002589244235.png?HW-CC-KV=V1&HW-CC-Date=20260429T052800Z&HW-CC-Expire=86400&HW-CC-Sign=E934A7885397F8F2E7450DA4F978BA7DAF26323124E8C05B2313990DDB3F0D7C)

## 裁剪不规则形状

通过设置PathShape，将图片裁剪为不规则形状。

```
1. // xxx.ets
2. import { PathShape } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ClipShapeExample {
7. build() {
8. Column({ space: 15 }) {
9. Row() {
10. // 请将$r('app.media.background')替换为实际资源文件
11. Image($r('app.media.background'))
12. .clipShape(new PathShape({ commands: 'M0 0 H400 V200 H0 Z' }))
13. .width('500px').height('300px')
14. }
15. .clip(true)
16. .borderRadius(20)
17. }
18. .width('100%')
19. .margin({ top: 15 })
20. }
21. }
```

[ClipShapeExample4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample4.ets#L15-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WBfIiBjpTxqWAlRGc3cg9w/zh-cn_image_0000002558764428.png?HW-CC-KV=V1&HW-CC-Date=20260429T052800Z&HW-CC-Expire=86400&HW-CC-Sign=B45B00F7A3F55F40791E4D419EE53D215C38834907C2185ED028A13D358F56B1)
