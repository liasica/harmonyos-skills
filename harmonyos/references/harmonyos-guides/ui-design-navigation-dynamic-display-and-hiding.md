---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-dynamic-display-and-hiding
title: 标题栏动态显隐
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 标题栏动态显隐
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9efe5d64aed4efa3025e4132b44c50e0cd03ccbd80b34d8dfcd32f1c126bc3c3
---

## 场景介绍

从6.0.0(20)版本开始，导航组件新增支持设置标题栏动态显隐功能。

用于实现标题栏在特定条件下自动显示或隐藏的效果，适用于需要节省屏幕空间的应用界面。当应用开发者需要动态隐藏标题栏时，可通过使用[dynamicHideTitleBar](../harmonyos-references/ui-design-hdsnavigation.md#dynamichidetitlebar)属性实现该功能。在设置动态隐藏标题栏的前提下，才可进一步设置隐藏状态栏。隐藏状态栏表现为状态栏内容区颜色为透明，状态栏区域无模糊。仅在隐藏标题栏区域后，执行隐藏状态栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/eLgds5VjTgC-_gmICIbS7Q/zh-cn_image_0000002558605178.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053019Z&HW-CC-Expire=86400&HW-CC-Sign=10F6388272EA6BE153A088C85013433707A5B2458E792B3125A7763E4247FC95 "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, BottomBuilderShowType, HideMode, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
   ```
2. 创建一级导航组件，通过设置dynamicHideTitleBar属性，可隐藏状态栏、标题区域、BottomBuilder区域。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. scroller: Scroller = new Scroller();
   5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

   7. @Builder
   8. bottomBuilder() {
   9. Column() {
   10. Search({ placeholder: 'Search' })
   11. .height(40)
   12. .placeholderColor($r('sys.color.font_primary'))
   13. .margin({ left: 16, right: 16 })
   14. }
   15. .width('100%')
   16. }

   18. build() {
   19. HdsNavigation() { // 创建HdsNavigation组件
   20. List({ space: 12, initialIndex: 0, scroller: this.scroller }) {
   21. ForEach(this.arr, (item: number) => {
   22. ListItem() {
   23. Column() {
   24. Row({ space: 8 }) {
   25. Button() {
   26. SymbolGlyph($r('sys.symbol.wifi'))
   27. .fontColor([$r('sys.color.icon_on_primary')])
   28. .fontSize(24)
   29. }
   30. .width(35)
   31. .height(35)

   33. Text('list_' + item)
   34. .width('100%')
   35. .height(72)
   36. .fontSize(16)
   37. .fontWeight(500)
   38. }

   40. Divider().margin({ left: 40 })
   41. }
   42. }
   43. .height(56)
   44. }, (item: number) => item.toString())
   45. }
   46. .margin({ left: 16, right: 16 })
   47. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   48. .cachedCount(3, true) // 设置列表中ListItem/ListItemGroup的预加载数量，列表穿透到标题栏下方不会消失
   49. .scrollBar(BarState.Off)
   50. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
   51. }
   52. .titleBar({
   53. content: {
   54. title: { mainTitle: 'MainTitle' },
   55. // 设置HdsNavigation BottomBuilder区域，包括设置高度，显示类型
   56. bottomBuilder: {
   57. builder: (): void => this.bottomBuilder(),
   58. height: 56,
   59. showType: BottomBuilderShowType.DIRECTLY_SHOW
   60. }
   61. },
   62. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   63. })
   64. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   65. .titleMode(HdsNavigationTitleMode.MINI)
   66. .hideBackButton(true)
   67. // 设置HdsNavigation标题栏动态显隐，包括设置标题区域，bottomBuilder区域，状态栏区域是否动态隐藏，隐藏模式以及开始隐藏时内容区的滚动距离。
   68. .dynamicHideTitleBar({
   69. hideTitleArea: true,
   70. hideBottomBuilder: true,
   71. hideStatusBar: false,
   72. mode: HideMode.SCROLL_UP_TO,
   73. hideOffset: 10
   74. })
   75. }
   76. }
   ```
