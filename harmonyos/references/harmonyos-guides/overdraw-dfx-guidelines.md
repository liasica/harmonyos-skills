---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/overdraw-dfx-guidelines
title: 过度绘制调试使用指导
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 过度绘制调试使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7fbceb06699469e1e97ec25ed2f849c7c235d1e16ddfcebc2d08b424ade90b09
---

当应用页面布局的嵌套程度过深时，应用渲染阶段会存在一些组件的绘制指令被其他组件的绘制指令部分或完全覆盖遮挡的情况，造成冗余的CPU、GPU等计算资源的使用。这种一个屏幕上的像素点被重复绘制了多次的情况被称为过度绘制（Overdraw）。开发者可通过系统提供的过度绘制调试指令，查看引起过度绘制的组件位置及其层级，从而减轻应用渲染时的负载。

本文将分别介绍过度绘制调试功能的使用方式，以及如何进行过度绘制的分析和优化。

## 使用方式

系统提供的过度绘制调试功能，可通过shell进行开启或者关闭。

* 使用前提：需在系统设置中开启开发者模式。
* 开启过度绘制调试功能：

  ```
  1. param set debug.graphic.overdraw true
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/09qrKsmoR1qJEiidFqtA5g/zh-cn_image_0000002552958630.png?HW-CC-KV=V1&HW-CC-Date=20260427T234707Z&HW-CC-Expire=86400&HW-CC-Sign=8D3B16BF026515BF30D2E643360C45F20A41EFDDC1074D778FFF88B36FBE724C)
* 关闭过度绘制调试功能：

  ```
  1. param set debug.graphic.overdraw false
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/LFLH0AEoQs25DZSdI9sf4g/zh-cn_image_0000002583478631.png?HW-CC-KV=V1&HW-CC-Date=20260427T234707Z&HW-CC-Expire=86400&HW-CC-Sign=59EA77D7633DFB0620DED5283AF7FCF6FFE03002D951C4124069DF9096752B04)
* 查看是否开启了过度绘制调试功能：

  true表示开启了过度绘制功能，false则表示未开启。

  ```
  1. param get debug.graphic.overdraw
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pKsblRY0Ro6RiFEiAjapEQ/zh-cn_image_0000002552798982.png?HW-CC-KV=V1&HW-CC-Date=20260427T234707Z&HW-CC-Expire=86400&HW-CC-Sign=B9F572B2BD96AF3525814225670CFE9D1360AD9A02045F8BFB2BFD63B1E7D163)

## 过度绘制组件分析

开启了过度绘制调试功能后，打开应用界面，存在过度绘制情况的像素会被代表着不同级别的颜色方框高亮出来，其颜色越深代表过度绘制情况越严重，对应关系如下：

* 原色：无过度绘制情况。
* 蓝紫色：存在一次过度绘制。
* 绿色：存在两次过度绘制。
* 浅红色：存在三次过度绘制。
* 深红色：存在四次或更多次过度绘制。

以下是一个存在冗余的背景颜色嵌套问题的示例应用程序，及其对应的开启过度绘制调试功能的界面显示情况。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World'

6. build() {
7. Row() {
8. Column() {
9. Column() {
10. Column() {
11. Column() {
12. Column() {
13. Text("Hello World")
14. }
15. .width('80%')
16. .height('80%')
17. .backgroundColor(Color.White)
18. }
19. .width('80%')
20. .height('80%')
21. .backgroundColor(Color.White)
22. }
23. .width('80%')
24. .height('80%')
25. .backgroundColor(Color.White)
26. }
27. .width('80%')
28. .height('80%')
29. .backgroundColor(Color.White)
30. }
31. .width('80%')
32. }
33. .height('80%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Se4bR7DbSyWFWIiybSskVA/zh-cn_image_0000002583438677.png?HW-CC-KV=V1&HW-CC-Date=20260427T234707Z&HW-CC-Expire=86400&HW-CC-Sign=A0A68C95CFF46438D0376A0D1761FA388B37D69192A2B049BE1E818AC50E7ED3)

编译安装后打开过度绘制调试功能，应用界面如上图所示。

可以发现，从Hello World文字组件开始，由内到外的这几个Column组件在界面上分别显示为深红色-浅红色-绿色-蓝紫色-原色。这种现象说明，随着嵌套程度的加深，每一个Column组件的背景颜色绘制都会带来一次过度绘制。

另外，状态栏、侧边栏等系统界面也会在过度绘制调试功能中被统计到，此为正常现象。

## 如何减少过度绘制现象

通过上文所述的调试功能可以帮助我们发现应用界面里存在的过度绘制问题，通常我们建议采用如下方式减少过度绘制的现象：

* 通过显隐控制或者if-else条件，减少页面上冗余的组件。
* 减少被完全遮挡的组件上的绘制指令，如背景颜色、组件内容等。
* 采用扁平化布局，减少组件嵌套深度，比如将大小相近、功能类似的布局组件合并为一个组件等。
