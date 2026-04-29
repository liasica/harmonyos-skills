---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-set-multi-window
title: 设置应用内多窗
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置应用内多窗
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:21+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ec0d98207b15f741afb85d39c9183d35c9d96c6aeba5cc2b0e351bc8af25512a
---

## 场景介绍

从6.0.0(20)版本开始，新增支持应用内多窗。

当应用开发者需要使用应用内多窗图标（分屏按钮）时，可通过配置titleBar中的menu的[multiWindowEntryInAPPMenu](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationmenucontentoptions)属性实现该功能。

## 约束条件

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备形态，该组件不可交互，不响应点击事件。

## 开发步骤

1. 导入模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, HdsNavigationMenuContentOptions, HdsNavigationAttribute } from '@kit.UIDesignKit';
   3. import { Want } from '@kit.AbilityKit';
   ```
2. 创建一级导航组件，通过配置titleBar中的menu上的multiWindowEntryInAPPMenu属性，实现应用内多窗图标设置。

   ```
   1. @Entry
   2. @Component
   3. struct MultiWindowEntryInAPPTest {
   4. private want: Want = {
   5. // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
   6. bundleName: "com.example.myapplication",
   7. moduleName: "entry",
   8. abilityName: "FuncAbility",
   9. }
   10. @State menuContent: HdsNavigationMenuContentOptions = {
   11. multiWindowEntryInAPPMenu: {
   12. want: this.want,
   13. },
   14. maxCount: 3,
   15. value: [
   16. { content: { label: 'menu1', icon: $r('sys.symbol.search_things'), } },
   17. { content: { label: 'menu2', icon: $r('sys.symbol.plus'), } }
   18. ]
   19. }

   21. build() {
   22. HdsNavigation() {
   23. Stack() {
   24. Text("Page1")
   25. }.alignContent(Alignment.Center)
   26. .width("100%")
   27. .height("100%")
   28. }
   29. .hideToolBar(false)
   30. .navBarWidth('100%')
   31. .titleBar({
   32. content: {
   33. title: {
   34. mainTitle: "Index"
   35. },
   36. menu: this.menuContent
   37. }
   38. })
   39. }
   40. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/QJZ2-qUcT2K2orpHDY_rCQ/zh-cn_image_0000002558764836.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053020Z&HW-CC-Expire=86400&HW-CC-Sign=F0BD1079B0125F77B81E9A48B0D7F3EB0BDCAB7CD06B2E5C554FB41EB509A0B0)
