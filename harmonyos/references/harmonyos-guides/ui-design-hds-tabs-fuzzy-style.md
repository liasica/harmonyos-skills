---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-fuzzy-style
title: 设置页签栏的模糊样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的模糊样式
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:141f2da9c7841948810af45a03f9687fa83d2d455989849573252d72338d96e6
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置页签栏的模糊样式。

[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)容器组件扩展支持页签栏设置直接模糊和渐变模糊效果。

* 直接模糊

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/lx6un6RQTZKnVBRUrN_uFg/zh-cn_image_0000002552958342.png?HW-CC-KV=V1&HW-CC-Date=20260427T234153Z&HW-CC-Expire=86400&HW-CC-Sign=290374C9402980DEDCAA87994F47286A2A142D28BB3C8FEA52539A48E46F2736)
* 渐变模糊

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/T_qHLepBTNSk__JN4Wzcbg/zh-cn_image_0000002583478343.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234153Z&HW-CC-Expire=86400&HW-CC-Sign=207CA6703D80C14B3586E45A23F7FB816889B98566E525ACCEC5B4E0B92C597F)

## 约束条件

1. 依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。
2. TabBar叠加在TabContent之上，barOverlap设置为true。
3. 去掉TabBar节点，barBackgroundBlurStyle默认设置的模糊的属性值为BlurStyle.NONE。

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   2. import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barBackgroundStyle样式，可以自定义模糊的颜色和高度，实现渐变模糊。

   说明

   1. 当开发者通过Tabs组件属性barBackgroundBlurStyle设置模糊时，HdsTabs的默认模糊效果失效。
   2. 当开发者通过Tabs组件属性barBackgroundEffect设置模糊时，HdsTabs的默认模糊效果失效。
   3. 当开发者通过Tabs组件属性barBackgroundColor设置背景色时，HdsTabs的默认模糊效果只有模糊半径生效，模糊半径为80vp。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. private controller: HdsTabsController = new HdsTabsController();

   6. build() {
   7. Column() {
   8. HdsTabs({ controller: this.controller }) {
   9. TabContent() {
   10. Column().width('100%').height('100%').backgroundColor(Color.Pink)
   11. }
   12. .tabBar({ icon: $r('app.media.startIcon'), text: '页签1' })

   14. TabContent() {
   15. Column().width('100%').height('100%').backgroundColor(Color.Blue)
   16. }
   17. .tabBar({ icon: $r('app.media.startIcon'), text: '页签2' })
   18. }
   19. .barOverlap(true)
   20. .barPosition(BarPosition.End)
   21. .vertical(false)
   22. .barBackgroundStyle({
   23. maskColor: Color.Yellow,
   24. maskHeight: 80
   25. })
   26. }
   27. }
   28. }
   ```
