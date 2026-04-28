---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-split-line
title: 设置页签栏的分割线
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的分割线
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e5766fb03d4d4f9ca9e1eb548be32d9f6ae5ba4c9c92c4ec0e50b9052b4501c
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置页签栏的分割线。

[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)容器组件扩展支持页签栏分割线常隐、常显和渐进显隐。当应用开发者需要分割线一直显示、一直隐藏或者内容区超过页签栏8vp后分割线完全消失时，可以通过设置HdsTabs组件的分割线的模式，同时也支持自定义分割线样式。

| 常显 | 常隐 | 跟手 |
| --- | --- | --- |
|  |  |  |

## 约束条件

1. 将页签栏置于容器的底部且支持模糊，即barPosition设置为BarPosition.End，vertical设置为false和barOverlap设置为true。
2. 分割线模式设置为跟手滑动模式时，跟手滑动效果仅限支持滚动的通用接口的组件，其他类型组件由开发者自己实现。
3. 跟手滑动效果依赖HdsTabs控制器绑定需要设置的list滑动控制器。

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   2. import { HdsTabs, HdsTabsController, DividerMode, HdsTabsAttribute } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置的Button可以切换分割线展示效果，分别是常显、常隐和跟手滑动效果。

   * 初始化list滑动控制器和HdsTabs控制器，将list滑动控制器绑定在HdsTabs控制器上，确保联动，否则跟手滑动没有渐变效果。

     ```
     1. private controller: HdsTabsController = new HdsTabsController();
     2. listScroller0: ListScroller = new ListScroller();
     3. listScroller1: ListScroller = new ListScroller();

     5. aboutToAppear(): void {
     6. this.controller.bindScroller(0, this.listScroller0);
     7. this.controller.bindScroller(1, this.listScroller1);
     8. }

     10. aboutToDisappear(): void {
     11. this.controller.unbindScroller(this.listScroller0);
     12. this.controller.unbindScroller(this.listScroller1);
     13. }
     ```
   * 设置页签栏置于容器的底部且支持模糊，否则跟手滑动没有渐变效果。

     ```
     1. .barOverlap(true)
     2. .barPosition(BarPosition.End)
     3. .vertical(false)
     4. .divider({
     5. mode: DividerMode.FOLLOW_SCROLL,
     6. style: {
     7. color: Color.Black,
     8. strokeWidth: 1,
     9. startMargin: 0,
     10. endMargin: 0
     11. }
     12. })
     ```
   * 跟手滑动效果仅限支持滚动的通用接口的组件，如List，Scroll等。

     ```
     1. HdsTabs({ controller: this.controller }) {
     2. TabContent() {
     3. List({ scroller: this.listScroller0 }) {} // listScroller是开发者设置的滑动控制器，list子组件可以自定义添加。
     4. }
     5. .tabBar({ icon: $r('app.media.startIcon'), text: '页签1' })
     6. TabContent() {
     7. List({ scroller: this.listScroller1 }) {}
     8. }
     9. .tabBar({ icon: $r('app.media.startIcon'), text: '页签2' })
     10. }
     ```
