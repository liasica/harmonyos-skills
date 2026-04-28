---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-sidebar-alignment-substyle
title: 设置侧边栏半屏居中对齐样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置侧边栏半屏居中对齐样式
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8407813ae5569f139b6ca689b0ae28d22bacdbcc5771dfb9981a1ee578a8f3f5
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置侧边栏半屏居中对齐样式。

[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)容器组件侧边栏支持半屏居中对齐布局。横向Tabs时，若没有主动设置TabBar高度，则TabBar默认高度为48vp，纵向TabBar默认宽度为96vp，barHeight设成固定值后，TabBar无法扩展底部安全区。当safeAreaPadding不设置bottom或者bottom设置为0时，可以实现扩展安全区。

* 半屏居中对齐布局

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/6Rq_n1IUQVGbTHo1VFuUqg/zh-cn_image_0000002583438389.png?HW-CC-KV=V1&HW-CC-Date=20260427T234153Z&HW-CC-Expire=86400&HW-CC-Sign=A14E292EAE088CCE26453D4D491BA75BA85D706A41B0917664FEDC8BDA9159C2)
* 默认横向和纵向宽度

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/ry9YJuokQkeIUedAAVTduA/zh-cn_image_0000002552958344.png?HW-CC-KV=V1&HW-CC-Date=20260427T234153Z&HW-CC-Expire=86400&HW-CC-Sign=BD1DC4B4369F8A8E1F2E7642C948A2D4933D652EE1DF0ECE42CF8208A813651F)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/C_YyOwRQR76M1-N_JvrTNg/zh-cn_image_0000002583478345.png?HW-CC-KV=V1&HW-CC-Date=20260427T234153Z&HW-CC-Expire=86400&HW-CC-Sign=9A98C2552242ED5ACB35D6558FA1D0FBC629C4BD4A4759779D2EDF03C44C81C3)

## 约束条件

1. 依赖页签位于侧边栏，vertical设置为true。
2. 页签使用BottomTabBarStyle样式。

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   2. import { HdsTabs, ExtendBarMode, HdsTabsAttribute } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barMode样式为ExtendBarMode.HALF\_SCREEN\_FIXED，所有页签总高度之和为HdsTabs组件高度的四分之一，且处在二分之一屏的居中位置。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State isVertical: boolean = false;

   6. build() {
   7. Column() {
   8. Column() {
   9. Row() {
   10. Button('verticalChange')
   11. .onClick(() => {
   12. this.isVertical = !this.isVertical;
   13. })
   14. }
   15. }
   16. .margin({ top: 20 })
   17. .width('100%')
   18. .height('10%')
   19. HdsTabs({ barPosition: BarPosition.End }) {
   20. TabContent() {
   21. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
   22. }
   23. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))
   24. TabContent() {
   25. Column().width('100%').height('100%').backgroundColor(Color.Blue)
   26. }
   27. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))
   28. TabContent() {
   29. Column().width('100%').height('100%').backgroundColor(Color.Pink)
   30. }
   31. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))
   32. }
   33. .vertical(this.isVertical)
   34. .barMode(ExtendBarMode.HALF_SCREEN_FIXED)
   35. .width('100%')
   36. .height('90%')
   37. }
   38. }
   39. }
   ```
