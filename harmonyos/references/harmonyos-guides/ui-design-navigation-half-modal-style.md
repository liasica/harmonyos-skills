---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-half-modal-style
title: 半模态样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 半模态样式
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6b9dcd0f3b6fb37e9555bf950ffd6989c4e00e42c2718c57f9a1bed86634a221
---

## 场景介绍

从6.0.0(20)版本开始，导航组件新增支持半模态中的标题栏样式，并在该样式下支持标题栏模糊效果。

用于半模态弹窗中使用导航组件场景。通过设置[HdsNavigationTitleMode](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationtitlemode)为MODAL可以实现标题栏半模态样式及动态模糊。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/UU9Q-sxyRWCP_lB727k4KQ/zh-cn_image_0000002589324703.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053019Z&HW-CC-Expire=86400&HW-CC-Sign=A577F3A79EC7AB35A66A5886F2E6C017B96C7621AAD0F0FE0596B016F3347002 "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { IconStyleMode, HdsNavigationAttribute, HdsNavigation, HdsNavigationTitleMode } from '@kit.UIDesignKit';
   ```
2. 创建一级导航组件，通过设置titleMode属性为HdsNavigationTitleMode.MODAL实现标题栏半模态样式。

   ```
   1. @Entry
   2. @Component
   3. struct SheetTransitionExample {
   4. @State isShow: boolean = false;
   5. scroller: Scroller = new Scroller();

   7. @Builder
   8. HdsNavigationBuilder() {
   9. HdsNavigation() {
   10. Scroll(this.scroller) {
   11. Image($r('app.media.scenery2'))
   12. .height('100%')
   13. }
   14. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   15. .scrollBar(BarState.Off)
   16. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
   17. }
   18. .titleBar({
   19. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   20. content: {
   21. title: {
   22. mainTitle: '壁纸',
   23. },
   24. // 设置HdsNavigation关闭按钮，与半模态按钮规格一致
   25. menu: {
   26. value: [{
   27. content: {
   28. icon: $r('sys.symbol.xmark'),
   29. type: IconStyleMode.SMALL,
   30. action: () => {
   31. this.isShow = false;
   32. },
   33. }
   34. }]
   35. },
   36. },
   37. })
   38. .titleMode(HdsNavigationTitleMode.MODAL) // 设置导航标题栏模式为半模态
   39. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   40. }

   42. build() {
   43. Column({ space: 8 }) {
   44. Button('open modal')
   45. .onClick(() => {
   46. this.isShow = true;
   47. })
   48. .fontSize(20)
   49. .margin(10)
   50. .bindSheet($$this.isShow, this.HdsNavigationBuilder(), {
   51. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
   52. showClose: false, // 关闭半模态关闭按钮，推荐使用HdsNavigation关闭按钮
   53. enableFloatingDragBar: true,
   54. })
   55. }
   56. .width('100%')
   57. .height('100%')
   58. }
   59. }
   ```
