---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-side-menu
title: 侧边栏菜单样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 侧边栏菜单样式
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:52d35960e8c95a62dff9113f6d4f7a0aa6cdaa9e913fb2cd44afd59471d656dc
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置侧边栏菜单样式。

[HdsSideMenu](../harmonyos-references/ui-design-hdssidemenu.md)提供一种菜单栏样式组件。设置侧边栏对应的一级菜单和二级菜单，并显示其新消息数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/FEwuP1AxSRG577i4S-7RWQ/zh-cn_image_0000002589324707.png?HW-CC-KV=V1&HW-CC-Date=20260429T053021Z&HW-CC-Expire=86400&HW-CC-Sign=D77D1BFCE50EC0902D7609C5F452F9466BD01AAEEA8308B40C10F770157E3FAA)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsSideMenu, HdsSideMenuMainItem, HdsSideMenuSubItem, HdsSideMenuBadgeParam, HdsSideBar } from '@kit.UIDesignKit';
   2. import { SymbolGlyphModifier } from '@kit.ArkUI';
   ```
2. 设置对应的一级菜单和二级菜单，并显示其新消息数量。

   ```
   1. @Entry
   2. @ComponentV2
   3. struct Index {
   4. @Local showControlButton: boolean = true;
   5. @Local sideBarMask: boolean = false;
   6. @Local autoHide: boolean = true;
   7. @Local barStateTypeText: string = "Select BarState";
   8. @Local widthIndex: number = 0;
   9. @Local badgeNumber: HdsSideMenuBadgeParam = { count: 50 };
   10. @Local useTheme: boolean = false;
   11. @Local selectedIndex: number = 2;
   12. @Local selectedTransparency: number = 0.6;
   13. @Local str: string = "短信";
   14. @Local isShowSidebar: boolean = true;
   15. listOptionsDefault?: HdsSideMenuMainItem[] = [
   16. new HdsSideMenuMainItem(
   17. {
   18. symbol: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontSize(14),
   19. label: $r('sys.string.TextView_engr_phone'),
   20. }),
   21. new HdsSideMenuMainItem({
   22. icon: $r('sys.symbol.person_wave_3'),
   23. label: 'Tuesday',
   24. hdsSideMenuSubItem: [
   25. new HdsSideMenuSubItem({ label: this.str, badge: this.badgeNumber })],
   26. }),
   27. new HdsSideMenuMainItem({
   28. symbol: new SymbolGlyphModifier($r('sys.symbol.person_crop_circle_fill_1')),
   29. label: 'Wednesday',
   30. }),
   31. ]
   32. @Builder
   33. SideBarPanelBuilder() {
   34. Column() {
   35. HdsSideMenu({
   36. items: this.listOptionsDefault,
   37. selectedIndex: this.selectedIndex,
   38. $selectedIndex: (selectedIndex: number) => {
   39. this.selectedIndex = selectedIndex;
   40. },
   41. })
   42. }
   43. .height('100%')
   44. }
   45. //右侧内容区
   46. @Builder
   47. ContentPanelBuilder() {
   48. Column() {
   49. Column() {
   50. Button() {
   51. SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open_sidebar') : $r('sys.symbol.close_sidebar'))
   52. .fontWeight(FontWeight.Normal)
   53. .fontSize($r('sys.float.ohos_id_text_size_headline7'))
   54. .fontColor([$r('sys.color.ohos_id_color_titlebar_icon')])
   55. .hitTestBehavior(HitTestMode.None)
   56. }
   57. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
   58. .height(24)
   59. .width(24)
   60. .animation({ curve: Curve.Sharp, duration: 100 })
   61. .onClick(() => {
   62. this.isShowSidebar = !this.isShowSidebar;
   63. })
   64. }
   65. }
   66. .height('100%')
   67. .width('100%')
   68. }
   69. @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder
   70. @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
   71. @Builder
   72. build() {
   73. Column() {
   74. HdsSideBar({
   75. sideBarPanelBuilder: (): void => {
   76. this.sideBarBuilder()
   77. },
   78. contentPanelBuilder: (): void => {
   79. this.contentBuilder()
   80. },
   81. isShowSideBar: this.isShowSidebar,
   82. $isShowSideBar: (isShowSidebar: boolean) => {
   83. this.isShowSidebar = !isShowSidebar
   84. },
   85. })
   86. }
   87. }
   88. }
   ```
