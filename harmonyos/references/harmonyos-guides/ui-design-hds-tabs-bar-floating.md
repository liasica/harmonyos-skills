---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating
title: 设置页签栏的悬浮样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的悬浮样式
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45889b0966dc3dc606017a80eaf6ee6ca61197175a89ced1f985588ae05bb812
---

## 场景介绍

从6.1.0(23) 版本开始，新增支持设置页签栏的悬浮样式以及迷你栏。

## 页签栏

页签栏悬浮样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/tm3tn5HaS1uhNst-wuFfXw/zh-cn_image_0000002558764844.png?HW-CC-KV=V1&HW-CC-Date=20260429T053022Z&HW-CC-Expire=86400&HW-CC-Sign=AAC39F0F6B96BF8A9C7742992C0E189EE86724B261917D4D464AF0FAF8B43EBE)

## 迷你栏

迷你栏是新增的自定义区域，跟页签栏高度相等且水平对齐，支持展开和折叠两种样式。

迷你栏的折叠样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/IEbNMm4nTly7DP7YYF4EXQ/zh-cn_image_0000002558605188.png?HW-CC-KV=V1&HW-CC-Date=20260429T053022Z&HW-CC-Expire=86400&HW-CC-Sign=5891A63127E1BBD198B7402368E633DC31E1F71095B9244A53D9992A91D1B067)

迷你栏的展开样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/O7JeWuNzRvKtIwAHZz7r6Q/zh-cn_image_0000002589324713.png?HW-CC-KV=V1&HW-CC-Date=20260429T053022Z&HW-CC-Expire=86400&HW-CC-Sign=8A7E21A9230140B6A8899F2F5177D31598A195E5B8BA255E343F3914D30B6EBC)

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   2. import { hdsMaterial } from '@hms.hds.hdsMaterial'
   3. import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barFloatingStyle样式，并设置barOverlap为true，vertical为false，barPosition为BarPosition.End，可实现页签栏的悬浮样式。若在barFloatingStyle中设置miniBar，则可实现迷你栏。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // 初始化HdsTabs控制器。
   5. private controller: HdsTabsController = new HdsTabsController();

   7. @Builder
   8. tabContentBuilder(color: Color) {
   9. List() {
   10. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
   11. ListItem() {
   12. Column() {
   13. Row() {
   14. }.height(200)
   15. .width('100%')

   17. Row() {
   18. }.width('100%')
   19. .height(50)
   20. .background(color)
   21. }
   22. }
   23. })
   24. }
   25. }

   27. @Builder
   28. miniBarBuilder() {
   29. Row() {
   30. Column() {
   31. Image($r('app.media.alarm_stop'))
   32. .width(40)
   33. .height(40)
   34. .borderRadius(40)
   35. }.width(48).height(48).justifyContent(FlexAlign.Center)

   37. Text('Hello')

   39. Column() {
   40. Image($r('sys.media.ohos_ic_public_pause'))
   41. .width(40)
   42. .height(40)
   43. .borderRadius(40)
   44. }.width(48).height(48).justifyContent(FlexAlign.Center)
   45. }
   46. }

   48. build() {
   49. Column() {
   50. HdsTabs({ controller: this.controller }) {
   51. TabContent() {
   52. this.tabContentBuilder(Color.Green)
   53. }
   54. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Green'))

   56. TabContent() {
   57. this.tabContentBuilder(Color.Blue)
   58. }
   59. .tabBar(new BottomTabBarStyle($r('sys.media.wifi_router_fill'), 'Blue'))

   61. TabContent() {
   62. this.tabContentBuilder(Color.Yellow)
   63. }
   64. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Yellow'))
   65. }
   66. // 设置barOverlap为true，vertical为false，barPosition为BarPosition.End
   67. .barOverlap(true)
   68. .barPosition(BarPosition.End)
   69. .vertical(false)
   70. // 设置页签栏悬浮样式。
   71. .barFloatingStyle({
   72. barWidth: { smallWidth: 200, mediumWidth: 300, largeWidth: 400 },
   73. barBottomMargin: 28,
   74. gradientMask: { maskColor: '#66F1F3F5', maskHeight: 92 },
   75. systemMaterialEffect: {
   76. materialType: hdsMaterial.MaterialType.IMMERSIVE,
   77. materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
   78. },
   79. // 设置迷你栏，若不设置，则仅有页签栏。
   80. miniBar: {
   81. miniBarBuilder: () => this.miniBarBuilder()
   82. }
   83. })
   84. }
   85. }
   86. }
   ```
