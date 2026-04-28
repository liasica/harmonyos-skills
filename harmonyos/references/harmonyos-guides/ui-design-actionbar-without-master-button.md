---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-actionbar-without-master-button
title: 设置无主按钮的组件
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 核心操作栏 > 设置无主按钮的组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6cf4700e09c857747b962fb6d9f0c2877822941af2008f8114cf86f7548fce2
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置无主按钮的组件。

[HdsActionBar](../harmonyos-references/ui-design-hdsactionbar.md)组件支持多个按钮的样式。当应用开发者需要多个按钮并且没有主按钮，没有展开和收缩的动效时，可以通过设置左按钮和右按钮配置样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/iwNDCtyWQNewJUze5W1_fA/zh-cn_image_0000002552958348.png?HW-CC-KV=V1&HW-CC-Date=20260427T234155Z&HW-CC-Expire=86400&HW-CC-Sign=0A3B6B947A82798FC903C72EB3C9C3A67E7D03C4381A7AD36FB3D7338694E796)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsActionBar, ActionBarButton } from '@kit.UIDesignKit'
   ```
2. 创建左边的按钮数组startButtons，创建右边的按钮数组endButtons，无主按钮，不支持切换展开和收缩状态。

   ```
   1. @Entry
   2. @ComponentV2
   3. struct TestNoPrimaryButton {

   5. build() {
   6. Column() {
   7. HdsActionBar({
   8. startButtons: [new ActionBarButton({
   9. baseIcon: $r('sys.symbol.stopwatch_fill')
   10. }), new ActionBarButton({
   11. baseIcon: $r('sys.symbol.stopwatch_fill')
   12. })],
   13. endButtons: [new ActionBarButton({
   14. baseIcon: $r('sys.symbol.mic_fill')
   15. })]
   16. })
   17. }
   18. .width('100%')
   19. .height('100%')
   20. .backgroundColor(0xF1F3F5)
   21. .justifyContent(FlexAlign.Center)
   22. .alignItems(HorizontalAlign.Center)
   23. }
   24. }
   ```
