---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-dynamic-blur
title: 设置动态模糊样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置动态模糊样式
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3c309661b3931eeee5647e8b93367ff09a2666beed82bc0aab4263a571f78956
---

## 场景介绍

从5.1.0(18)版本开始， 导航组件新增支持标题栏[通用模糊](../harmonyos-references/ui-design-hdsnavigation.md#scrolleffecttype)（适用于列表型非沉浸式场景）样式。

从6.0.0(20)版本开始，新增支持[过渡模糊](../harmonyos-references/ui-design-hdsnavigation.md#scrolleffecttype)（适用于列表型非沉浸式场景）与[渐变模糊](../harmonyos-references/ui-design-hdsnavigation.md#scrolleffecttype)（适用于沉浸式图文类的场景）样式。

当应用开发者需要使用标题栏样式随内容区滚动而动态改变样式的导航组件时，可以通过设置titleBar属性中的[style](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationtitlebaroptions)配置，自定义标题栏样式随滚动距离线性变化。通常需配合滚动容器组件使用，推荐使用bindToScrollable、bindToNestedScrollable属性绑定导航组件和可滚动容器组件。

### 通用模糊样式

对组件背景进行均匀的模糊处理，模糊强度一致，边界清晰，用于强调控件与内容的层级分隔。滑动内容进入/离开标题栏区域过程中，模糊背板和分割线透明渐变出现/消失。此方式适用于非沉浸式场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/22fb8BKTQwaU9UTSWVCRdw/zh-cn_image_0000002583478333.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234150Z&HW-CC-Expire=86400&HW-CC-Sign=C6AABB4E09ADCA20B72E5AA8722D9469DEC8BC5E76ED8B9CF351F86719C04C1E "点击放大")

### 过渡模糊样式

对组件背景进行均匀的模糊处理，模糊强度一致，边界清晰，用于强调控件与内容的层级分隔。滑动时标题栏内容发生颜色/状态变化，滑动过程中，随滑动距离，标题栏样式线性变化。此方式仅适用于沉浸式页面，随内容区滚动修改标题栏样式的场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/HLip7b6jRxKVJ0trgrYfhw/zh-cn_image_0000002552798684.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234150Z&HW-CC-Expire=86400&HW-CC-Sign=03D932629D5D18ACF11ECD8FFD6338BDD68244E2F34AFE5930C24BDEF71E193C "点击放大")

### 渐变模糊样式

模糊效果在空间维度上呈现逐渐增强/减弱的变化，模糊边界柔和，用于增强页面沉浸感。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gCGYfjvCQuC9FH6oqS-7IA/zh-cn_image_0000002583438379.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234150Z&HW-CC-Expire=86400&HW-CC-Sign=2CC5AA222A5F21018D1B5BFA523DD7B701C41AE0ADD9A272CE8ED74CDDE17BB4 "点击放大")

## 开发步骤

1. 导入相关模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   2. import { HdsNavigation, HdsNavigationTitleMode, ScrollEffectType, HdsNavigationAttribute } from '@kit.UIDesignKit';
   3. import { LengthMetrics } from '@kit.ArkUI';
   ```
2. 创建一级导航组件，通过配置titleBar中的scrollEffectType属性，可实现通用模糊、过渡模糊、渐变模糊样式。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. scroller: Scroller = new Scroller();
   5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

   7. build() {
   8. HdsNavigation() { // 创建HdsNavigation组件
   9. List({ space: 12, initialIndex: 0, scroller: this.scroller }) {
   10. ForEach(this.arr, (item: number) => {
   11. ListItem() {
   12. Column() {
   13. Row({ space: 8 }) {
   14. Button() {
   15. SymbolGlyph($r('sys.symbol.wifi'))
   16. .fontColor([$r('sys.color.icon_on_primary')])
   17. .fontSize(24)
   18. }
   19. .width(35)
   20. .height(35)

   22. Text('list_' + item)
   23. .width('100%')
   24. .height(72)
   25. .fontSize(16)
   26. .fontWeight(500)
   27. }

   29. Divider().margin({ left: 40 })
   30. }
   31. }
   32. .height(56)
   33. }, (item: number) => item.toString())
   34. }
   35. .margin({ left: 16, right: 16 })
   36. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   37. .cachedCount(3, true) // 设置列表中ListItem/ListItemGroup的预加载数量，列表穿透到标题栏下方不会消失
   38. .scrollBar(BarState.Off)
   39. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
   40. }
   41. .titleBar({
   42. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   43. style: { // 设置导航组件标题栏样式，推荐使用默认样式
   44. // 标题栏动态模糊样式，包括是否使能滚动动态模糊，动态模糊类型，动态模糊生效的滚动距离等
   45. scrollEffectOpts: {
   46. enableScrollEffect: true,
   47. scrollEffectType: ScrollEffectType.COMMON_BLUR,
   48. blurEffectiveStartOffset: LengthMetrics.vp(0),
   49. blurEffectiveEndOffset: LengthMetrics.vp(20)
   50. },
   51. originalStyle: { // 内容区滚动前初始样式设置
   52. backgroundStyle: { // 标题栏背板样式设置
   53. backgroundColor: $r('sys.color.ohos_id_color_background'),
   54. },
   55. contentStyle: { // 标题栏内容区样式设置，包括标题区域，菜单区域，返回按钮区域
   56. titleStyle: {
   57. mainTitleColor: $r('sys.color.font_primary'),
   58. subTitleColor: $r('sys.color.font_secondary')
   59. },
   60. menuStyle: {
   61. backgroundColor: $r('sys.color.comp_background_tertiary'),
   62. iconColor: $r('sys.color.icon_primary')
   63. },
   64. backIconStyle: {
   65. backgroundColor: $r('sys.color.comp_background_tertiary'),
   66. iconColor: $r('sys.color.icon_primary')
   67. }
   68. }
   69. },
   70. scrollEffectStyle: { // 内容区滚动超过blurEffectiveEndOffset后样式设置
   71. backgroundStyle: {
   72. backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
   73. },
   74. contentStyle: {
   75. titleStyle: {
   76. mainTitleColor: $r('sys.color.font_primary'),
   77. subTitleColor: $r('sys.color.font_secondary')
   78. },
   79. menuStyle: {
   80. backgroundColor: $r('sys.color.comp_background_tertiary'),
   81. iconColor: $r('sys.color.icon_primary')
   82. },
   83. backIconStyle: {
   84. backgroundColor: $r('sys.color.comp_background_tertiary'),
   85. iconColor: $r('sys.color.icon_primary')
   86. }
   87. }
   88. }
   89. },
   90. content: { // 标题栏内容设置
   91. title: { mainTitle: 'MainTitle' },
   92. }
   93. })
   94. .hideBackButton(true)
   95. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   96. .titleMode(HdsNavigationTitleMode.MINI)
   97. }
   98. }
   ```
