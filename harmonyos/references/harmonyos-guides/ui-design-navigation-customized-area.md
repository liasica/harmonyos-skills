---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-customized-area
title: 设置自定义区域
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置自定义区域
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:51+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:334053556f32df8d535c724765da72d0d583a602d9cb08547e313defe5a66aca
---

## 场景介绍

从6.0.0(20)版本开始，导航组件支持设置标题栏的[stackBuilder](../harmonyos-references/ui-design-hdsnavigation.md#titlebarcontentoptions)和[bottomBuilder](../harmonyos-references/ui-design-hdsnavigation.md#titlebarcontentoptions)，允许开发者自定义标题栏样式，以匹配应用的视觉风格。

当应用开发者需要在标题栏区域增加自定义节点时，例如在标题栏上方区域增加分段按钮，标题下方区域增加搜索框、页签时，可以使用标题栏自定义区域设置能力。由于标题栏高度通常由系统或框架统一控制，开发者在添加自定义节点时需注意不要超出标题栏的可用空间，否则可能导致布局溢出或视觉混乱。自定义区域可能会覆盖或影响默认标题栏组件（如返回按钮、标题文字），需谨慎布局，避免交互冲突或遮挡关键元素。如果在标题栏中添加大量交互复杂、渲染频率高的组件，可能会对性能产生影响。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/RDY-nzgOQBmd5qXeEQHp1A/zh-cn_image_0000002583478335.png?HW-CC-KV=V1&HW-CC-Date=20260427T234150Z&HW-CC-Expire=86400&HW-CC-Sign=723D45D22ACEA3E15F804043442ADA3BB38DA4B7D8ABB95E57095040F0B1924F "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/o3hDtkp_SpCkSGj5ZjOMsQ/zh-cn_image_0000002552798686.png?HW-CC-KV=V1&HW-CC-Date=20260427T234150Z&HW-CC-Expire=86400&HW-CC-Sign=582D4C481C69690F3833272AD71223FE26EBA2057D7E7A508FF8DF1E7487FDE6 "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, HdsNavigationTitleMode, HdsNavigationAttribute } from '@kit.UIDesignKit';
   3. import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem } from '@kit.ArkUI';
   ```
2. 创建一级导航组件，通过配置titleBar中content属性的stackBuilder以及bottomBuilder属性，即可实现导航组件的自定义区域设置。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
   5. scroller: Scroller = new Scroller();
   6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
   7. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
   8. buttons: [{ text: '备忘' }, { text: '待办' }] as ItemRestriction<SegmentButtonTextItem>,
   9. selectedFontColor: '#ffe6ba0b',
   10. selectedBackgroundColor: Color.White,
   11. textPadding: {
   12. top: 5,
   13. right: 5,
   14. bottom: 5,
   15. left: 5
   16. },
   17. });
   18. @State tabSelectedIndexes: number[] = [0];

   20. @Builder
   21. stackBuilder() {
   22. Row() {
   23. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
   24. Button() {
   25. SymbolGlyph($r('sys.symbol.open_sidebar'))
   26. .fontColor([$r('sys.color.icon_primary')])
   27. .fontSize(24)
   28. .width(24)
   29. .height(24)
   30. }
   31. .width(40)
   32. .height(40)
   33. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))

   35. SegmentButton({
   36. options: this.tabOptions,
   37. selectedIndexes: $tabSelectedIndexes
   38. })
   39. .width(150)

   41. Button() {
   42. SymbolGlyph($r('sys.symbol.dot_grid_2x2'))
   43. .fontColor([$r('sys.color.icon_primary')])
   44. .fontSize(24)
   45. .width(24)
   46. .height(24)
   47. }
   48. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
   49. .width(40)
   50. .height(40)
   51. }
   52. .margin({ left: 16, right: 16 })
   53. }
   54. .width('100%')
   55. }

   57. build() {
   58. HdsNavigation(this.pageInfos) { // 创建HdsNavigation组件
   59. Row() {
   60. Text('全部备忘')
   61. .fontSize(26)
   62. .fontWeight(FontWeight.Bold)
   63. .layoutWeight(1)
   64. .onClick(() => {
   65. this.pageInfos.pushPath({ name: 'pageOne' });
   66. })
   67. }
   68. .margin({ left: 16, top: 16 })
   69. .justifyContent(FlexAlign.Start)
   70. }
   71. .titleBar({
   72. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   73. content: {
   74. title: { mainTitle: '' },
   75. // 设置HdsNavigation 自定义标题区
   76. stackBuilder: (): void => this.stackBuilder(),
   77. }
   78. })
   79. .hideBackButton(true)
   80. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   81. .titleMode(HdsNavigationTitleMode.MINI)
   82. }
   83. }
   ```
3. 在PageOne页面创建二级导航组件。通过titleBar接口设置HdsNavDestination标题栏HarmonyOS风格化样式及内容设置。展示NavPathStack路由使用示例。

   ```
   1. // PageOne.ets
   2. // 模块导入
   3. // 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
   4. import { BottomBuilderShowType, HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';

   6. @Builder
   7. export function PageOneBuilder() {
   8. PageOne()
   9. }

   11. @Component
   12. export struct PageOne {
   13. @Consume('pageInfos') pageInfos: NavPathStack;
   14. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
   15. scroller: Scroller = new Scroller();

   17. @Builder
   18. bottomBuilder() {
   19. Column() {
   20. Search({ placeholder: 'Search' })
   21. .height(40)
   22. .placeholderColor($r('sys.color.font_primary'))
   23. .margin({ left: 16, right: 16 })
   24. }
   25. .width('100%')
   26. }

   28. build() {
   29. HdsNavDestination() { // 创建HdsNavDestination组件
   30. Scroll(this.scroller) { // HdsNavDestination内容区设置可滚动容器组件，用于实现内容区滚动联动标题栏动态模糊样式
   31. Image($r('app.media.scenery2')) // scenery2为自定义资源，开发者需替换本地资源
   32. .height('100%')
   33. }
   34. .edgeEffect(EdgeEffect.Spring)
   35. .scrollBar(BarState.Off)
   36. .margin({ left: 16, right: 16 })
   37. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   38. }
   39. .titleBar({
   40. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   41. content: {
   42. // HdsNavigation标题栏内容区设置
   43. title: {
   44. // HdsNavigation标题栏标题设置
   45. mainTitle: 'PageOne',
   46. },
   47. // HdsNavigation标题栏返回按钮设置
   48. backIcon: {
   49. label: 'backIcon', // 无障碍播报内容
   50. componentId: 'backIconId', // 返回按钮id
   51. },
   52. // 设置HdsNavigation BottomBuilder区域，包括设置高度，显示类型
   53. bottomBuilder: {
   54. builder: (): void => this.bottomBuilder(),
   55. height: 56,
   56. showType: BottomBuilderShowType.DIRECTLY_SHOW
   57. },
   58. menu: {
   59. // HdsNavigation标题栏菜单设置
   60. value: [{
   61. // 菜单项内容设置
   62. content: {
   63. label: 'menu',
   64. icon: $r('sys.symbol.ohos_circle'),
   65. },
   66. }]
   67. },
   68. }
   69. })
   70. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   71. }
   72. }
   ```
4. 工程entry/src/main/module.json5文件中的“module”下新增如下配置，用于页面跳转。

   ```
   1. "routerMap": "$profile:route_map"
   ```
5. 工程entry/src/main/resources/base/profile目录下增加route\_map.json文件。

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "pageOne",
   5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
   6. "buildFunction": "PageOneBuilder",
   7. "data": {
   8. "description": "this is pageOne"
   9. }
   10. }
   11. ]
   12. }
   ```
