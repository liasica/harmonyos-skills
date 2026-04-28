---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-message-reminder
title: 设置信息提醒
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置信息提醒
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:51+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5ceedb7ac85585de73e43051bec9f81365e0bd399e9595acfd6e285bb07562de
---

## 场景介绍

从5.1.0(18)版本开始，导航组件新增支持菜单栏设置信息提醒能力。

当应用开发者需要在导航组件菜单项右上角附加消息提醒时，可以通过设置标题栏菜单中的[badge](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationbadgeiconoptions)属性，实现信息提醒能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/SEs1StHeTnmaxEz7v7X7Hg/zh-cn_image_0000002552958334.png?HW-CC-KV=V1&HW-CC-Date=20260427T234150Z&HW-CC-Expire=86400&HW-CC-Sign=2D4D3DA57EBF4D43B683926473D8FF241DA6BFADDBBE3B8B78A6CBAAEBA08452 "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
   ```
2. 创建一级导航组件，通过配置titleBar中menu的badge属性，设置信息提醒样式。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. HdsNavigation() { // 创建HdsNavigation组件
   6. }
   7. .titleBar({
   8. content: {
   9. // HdsNavigation标题栏内容设置
   10. menu: {
   11. // HdsNavigation标题栏菜单区域内容设置
   12. value: [{
   13. content: {
   14. // 第一个菜单项内容设置
   15. label: 'menu1',
   16. icon: $r('sys.symbol.AI_search'),
   17. isEnabled: true,
   18. },
   19. badge: {
   20. // 第一个菜单项信息提醒设置
   21. count: 1,
   22. }
   23. }, {
   24. content: {
   25. // 设置第一个菜单项内容，设置为普通文本按钮
   26. label: 'menu2',
   27. icon: $r('sys.symbol.wifi'),
   28. isEnabled: true,
   29. componentId: 'menu_1',
   30. action: () => {
   31. },
   32. },
   33. badge: {
   34. // 第二个菜单项信息提醒设置
   35. value: '消息'
   36. }
   37. }]
   38. },
   39. title: { mainTitle: 'MainTitle' },
   40. }
   41. })
   42. .titleMode(HdsNavigationTitleMode.MINI)
   43. .hideBackButton(true)
   44. }
   45. }
   ```
