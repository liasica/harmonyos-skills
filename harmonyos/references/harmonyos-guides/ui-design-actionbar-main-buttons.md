---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-actionbar-main-buttons
title: 设置有主按钮的组件
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 核心操作栏 > 设置有主按钮的组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac5ac9a3ae3e884d3625857c5686dc23401b9893dcbe3ef49a79360ff5c46c37
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置有主按钮的组件。

[HdsActionBar](../harmonyos-references/ui-design-hdsactionbar.md)组件支持多个按钮的样式。当应用开发者需要多个按钮并且有主按钮，支持展开和收缩的动效时，可以通过设置主按钮配置样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/4LljLcKyRJ6X8QScKC5Q5g/zh-cn_image_0000002583438393.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234155Z&HW-CC-Expire=86400&HW-CC-Sign=216532788B428A2278F651A4DD41C8BC23A92966CEF22141A4B1C5D768BBCDDE)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit';
   ```
2. 创建左边的按钮数组startButtons，创建右边的按钮数组endButtons，创建主按钮primaryButton，设置isExpand初始值是true表示HdsActionBar的初始状态是展开状态，点击主按钮会收起，再次点击可以展开。

   ```
   1. @Entry
   2. @ComponentV2
   3. struct TestActionBar {
   4. @Local isExpand: boolean = true;

   6. @Local isPrimaryIconChanged: boolean = false;

   8. @Local primaryHoverTips: ResourceStr = '开始';

   10. build() {
   11. Column() {
   12. HdsActionBar({
   13. startButtons: [new ActionBarButton({
   14. baseIcon: $r('sys.symbol.stopwatch_fill')
   15. })],
   16. endButtons: [new ActionBarButton({
   17. baseIcon: $r('sys.symbol.mic_fill')
   18. })],
   19. primaryButton: new ActionBarButton({
   20. baseIcon: $r('sys.symbol.plus'),
   21. altIcon: $r('sys.symbol.play_fill'),
   22. onClick: () => {
   23. this.isExpand = !this.isExpand;
   24. this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
   25. if (this.isPrimaryIconChanged) {
   26. this.primaryHoverTips = '暂停';
   27. } else {
   28. this.primaryHoverTips = '开始';
   29. }
   30. },
   31. hoverTips: this.primaryHoverTips
   32. }),
   33. actionBarStyle: new ActionBarStyle({
   34. isPrimaryIconChanged: this.isPrimaryIconChanged
   35. }),
   36. isExpand: this.isExpand!!
   37. })
   38. }
   39. .width('100%')
   40. .height('100%')
   41. .backgroundColor(0xF1F3F5)
   42. .justifyContent(FlexAlign.Center)
   43. .alignItems(HorizontalAlign.Center)
   44. }
   45. }
   ```
