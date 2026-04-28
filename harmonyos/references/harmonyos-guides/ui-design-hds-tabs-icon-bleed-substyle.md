---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-icon-bleed-substyle
title: 设置页签的图标出血样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签的图标出血样式
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e31b53e938f2218ff56369e4406aa9e134d6a4d8cbe03de9f60a9d9ac8f856b
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置页签的图标出血样式。

[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)容器组件扩展支持出血图标样式。当应用开发者需要tabBar内的页签高度超出tabBar时，可以通过设置对应页签的属性，添加出血效果的自定义组件，图标超出容器部分最大高度为4vp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/rmvJG0Y1QUi-nf31B-SiFQ/zh-cn_image_0000002552798694.png?HW-CC-KV=V1&HW-CC-Date=20260427T234153Z&HW-CC-Expire=86400&HW-CC-Sign=F40459EF2CB56525C8F296F10AEE7D83795FF36DD52D5C3F2AE525814ECAABF4)

## 约束条件

依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   2. import { HdsTabs, HdsTabsAttribute } from '@kit.UIDesignKit';
   3. import { bleedIconStyle } from '@hms.hds.HdsStyle';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的子组件TabContent的tabBar样式。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. Stack() {
   6. HdsTabs() {
   7. TabContent() {
   8. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
   9. }
   10. .tabBar(bleedIconStyle(() => {
   11. this.tabBuilder()
   12. }))
   13. TabContent() {
   14. Column().width('100%').height('100%').backgroundColor(Color.Blue)
   15. }
   16. .tabBar(this.tabBuilder())
   17. }
   18. .vertical(false)
   19. .barPosition(BarPosition.End)
   20. }
   21. }

   23. @Builder
   24. tabBuilder() {
   25. Column() {
   26. Image($r('app.media.startIcon'))
   27. .width(48)
   28. .height(48)
   29. .borderRadius(24)
   30. }
   31. }
   32. }
   ```
