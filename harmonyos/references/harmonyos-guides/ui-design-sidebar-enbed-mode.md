---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-sidebar-enbed-mode
title: 设置embed模式的侧边栏
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 侧边栏样式 > 设置embed模式的侧边栏
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b30fae07440e893601f7f879a6e1b1caa9187761e65ee1c0650d020ecb3ca10
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置embed模式的侧边栏。

[HdsSideBar](../harmonyos-references/ui-design-hdssidebar.md)提供可以显示和隐藏的侧边栏容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区，通过设置[sideBarContainerType](../harmonyos-references/ts-container-sidebarcontainer.md#sidebarcontainertype枚举说明)的值为SideBarContainerType.Embed，使得当前HdsSideBar为嵌入样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/JYLbjdr8QG6jIYTx2J6nAw/zh-cn_image_0000002558764838.png?HW-CC-KV=V1&HW-CC-Date=20260429T053020Z&HW-CC-Expire=86400&HW-CC-Sign=A0CF893A3BC13D91E76D42B0D927CB3812D4F985BF8A5093F0CFA8F22FD34A74)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsSideBar } from '@kit.UIDesignKit';
   ```
2. 设置图片。

   将图片资源，放到entry/src/main/resources/base/media下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/K8x_24NwQsOVOax5hGhUHg/zh-cn_image_0000002558605182.png?HW-CC-KV=V1&HW-CC-Date=20260429T053020Z&HW-CC-Expire=86400&HW-CC-Sign=B08B789A16CE2692483449EEDEF64AC9AE01443F46C316E35A4CEE7E6E28346E)
3. 创建HdsSideBar侧边栏组件，设置展开模式为embed。

   ```
   1. @Entry
   2. @ComponentV2
   3. struct Index {
   4. @Local isSideBarContainerMask: boolean = true;
   5. @Local blankHeight: number = 48;
   6. @Local isAutoHide: boolean = false;
   7. @Local isShowSidebar: boolean = true;
   8. @Local triggerValueReplace: number = 0;
   9. //左侧侧边栏区
   10. @Builder
   11. SideBarPanelBuilder() {
   12. Column() {
   13. Blank().height(this.blankHeight)
   14. Text('HDSSideBar Menu 1')
   15. .fontSize(14)
   16. Text('HDSSideBar Menu 2')
   17. .fontSize(14)
   18. }
   19. .width('100%')
   20. .height('100%')
   21. }
   22. //右侧内容区
   23. @Builder
   24. ContentPanelBuilder() {
   25. Column(){
   26. Blank().height(this.blankHeight)
   27. Image($r('app.media.view')) // view为自定义资源，开发者需替换本地资源
   28. .width('80%')
   29. .height('50%')
   30. .margin({ top: 8 })
   31. .padding({
   32. right: '16vp',
   33. left: '16vp',
   34. bottom: '16vp',
   35. })
   36. .borderRadius(8)
   37. Column() {
   38. Text('HDSSideBar content text1')
   39. .fontSize(14)
   40. Text('HDSSideBar content text2')
   41. .fontSize(14)
   42. }
   43. Button() {
   44. SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open_sidebar') : $r('sys.symbol.close_sidebar'))
   45. .fontWeight(FontWeight.Normal)
   46. .fontSize($r('sys.float.ohos_id_text_size_headline7'))
   47. .fontColor([$r('sys.color.ohos_id_color_titlebar_icon')])
   48. .hitTestBehavior(HitTestMode.None)
   49. }
   50. .id('side_bar_button')
   51. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
   52. .height(24)
   53. .width(24)
   54. .animation({ curve: Curve.Sharp, duration: 100 })
   55. .onClick(() => {
   56. this.isShowSidebar = !this.isShowSidebar;
   57. })
   58. }
   59. }
   60. @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
   61. @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder
   62. @Builder
   63. HDSSideBarBuilder() {
   64. HdsSideBar({
   65. sideBarPanelBuilder: (): void => {
   66. this.sideBarBuilder()
   67. },
   68. contentPanelBuilder: (): void => {
   69. this.contentBuilder()
   70. },
   71. autoHide: this.isAutoHide,
   72. contentAreaMask: this.isSideBarContainerMask,
   73. sideBarContainerType: SideBarContainerType.Embed,
   74. isShowSideBar: this.isShowSidebar,
   75. $isShowSideBar: (isShowSidebar: boolean) => {
   76. this.isShowSidebar = !isShowSidebar
   77. },
   78. })
   79. }
   80. @Builder
   81. build() {
   82. Stack() {
   83. this.HDSSideBarBuilder()
   84. }
   85. }
   86. }
   ```
