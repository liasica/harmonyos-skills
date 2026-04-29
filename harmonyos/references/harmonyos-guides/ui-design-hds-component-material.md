---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-component-material
title: 沉浸光感
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 沉浸光感
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:589da5a10cdd91a9e186a223133596c95be55d2be8cc4a9164fe267d3e4db389
---

## 场景介绍

从6.1.0(23) 版本开始，新增支持HDS组件的沉浸光感材质能力。

* **HDS导航**：通过设置[TitleBarStyleOptions](../harmonyos-references/ui-design-hdsnavigation.md#titlebarstyleoptions)的systemMaterialEffect参数，可为标题栏按钮设置沉浸光感视效。
* **HDS底部页签**：通过设置[HdsTabsFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#hdstabsfloatingstyle)的systemMaterialEffect参数，可为底部页签设置沉浸光感视效。

## 使用系统自适应的沉浸光感

推荐使用系统自适应的沉浸光感效果，系统会根据当前设备的算力动态调整组件的材质效果，实现性能与显示效果的最佳平衡体验。

### 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsNavigation, HdsNavigationTitleMode, HdsTabs, HdsTabsController, HdsNavigationMenuContentOptions, ScrollEffectType, hdsMaterial, } from '@kit.UIDesignKit';
   2. import { SymbolGlyphModifier } from "@kit.ArkUI";
   ```
2. 创建HDS导航和底部页签组件。导航标题栏包含1个返回按钮和3个功能按钮，底部页签包含3个子项。

   以下示例代码为底部页签和标题栏的4个按钮设置了沉浸光感效果，该效果将根据系统能力自适应调整。

   ```
   1. @Entry
   2. @Component
   3. export struct Index {
   4. private scrollerForScroll: Scroller = new Scroller();
   5. private controller: HdsTabsController = new HdsTabsController();

   7. private menus: HdsNavigationMenuContentOptions = {
   8. value: [{
   9. content: {
   10. label: 'menu1',
   11. icon: $r('sys.symbol.square_and_pencil'),
   12. }
   13. }, {
   14. content: {
   15. label: 'menu2',
   16. icon: $r('sys.symbol.star')
   17. },
   18. },{
   19. content: {
   20. label: 'menu3',
   21. icon: $r('sys.symbol.more')
   22. },
   23. }
   24. ],
   25. };

   27. build() {
   28. HdsNavigation() {
   29. HdsTabs({ controller: this.controller }) {
   30. ForEach(MENU_CONFIG, (item: MenuItem) => {
   31. TabContent() {
   32. Stack() {
   33. Scroll(this.scrollerForScroll) {
   34. Column() {
   35. Image($r("app.media.scenery01")).width('100%') // scenery为自定义资源，开发者需替换本地资源
   36. }
   37. }
   38. .clipContent(ContentClipMode.SAFE_AREA)
   39. .height('100%')
   40. }
   41. }
   42. .tabBar(new BottomTabBarStyle({
   43. normal: item.symbolGlyph, selected: item.symbolGlyph1
   44. }, item.label))
   45. })
   46. }
   47. .barOverlap(true)
   48. .vertical(false)
   49. .barPosition(BarPosition.End)
   50. .barFloatingStyle({
   51. barBottomMargin: 28,
   52. systemMaterialEffect:  {
   53. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   54. materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE // 底部悬浮页签沉浸光感效果跟随系统策略自适应
   55. }
   56. })
   57. }
   58. .mode(NavigationMode.Stack)
   59. .titleBar({
   60. content: {
   61. title: {
   62. mainTitle: 'MainTitle',
   63. },
   64. menu: this.menus,
   65. },
   66. style: {
   67. scrollEffectOpts: {
   68. enableScrollEffect: false,
   69. scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
   70. },
   71. systemMaterialEffect: {
   72. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   73. materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE // 标题栏按钮沉浸光感效果跟随系统策略自适应
   74. },
   75. },
   76. avoidLayoutSafeArea: false,
   77. enableComponentSafeArea: false
   78. })
   79. .bindToScrollable([this.scrollerForScroll])
   80. .hideBackButton(false)
   81. .titleMode(HdsNavigationTitleMode.MINI)
   82. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
   83. }
   84. }

   86. interface MenuItem {
   87. symbolGlyph: SymbolGlyphModifier,
   88. symbolGlyph1: SymbolGlyphModifier,
   89. label: string,
   90. defaultBgColor: ResourceColor,
   91. hoverBgColor: ResourceColor,
   92. pressBgColor: ResourceColor,
   93. };

   95. const MENU_CONFIG: MenuItem[] = [
   96. {
   97. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   98. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   99. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   100. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   101. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   102. label: '闹钟',
   103. defaultBgColor: Color.Transparent,
   104. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   105. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   106. },
   107. {
   108. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   109. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   110. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   111. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   112. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   113. label: '时钟',
   114. defaultBgColor: Color.Transparent,
   115. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   116. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   117. },
   118. {
   119. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   120. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   121. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   122. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   123. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   124. label: '秒表',
   125. defaultBgColor: Color.Transparent,
   126. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   127. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   128. }
   129. ];
   ```

## 使用自定义沉浸光感效果

如果使用自定义沉浸光感的视觉效果，请先调用[getSystemMaterialTypes()](../harmonyos-references/ui-design-hdsmaterial.md#getsystemmaterialtypes)接口查询当前设备所支持的材质能力，再根据查询结果选用相应的材质效果枚举：

1. 如果查询结果显示当前设备支持IMMERSIVE材质类型，可选用EXQUISITE或GENTLE效果。
2. 如果查询结果显示当前设备不支持IMMERSIVE材质类型，则建议使用SMOOTH效果，以降低卡顿和发热风险，保障用户体验。

### 开发步骤

1. 导入相关模块。

   ```
   1. import { HdsNavigation, HdsNavigationTitleMode, HdsTabs, HdsTabsController, HdsNavigationMenuContentOptions, ScrollEffectType, hdsMaterial, } from '@kit.UIDesignKit';
   2. import { SymbolGlyphModifier } from "@kit.ArkUI";
   ```
2. 创建HDS导航和底部页签组件。导航标题栏包含1个返回按钮和3个功能按钮，底部页签包含3个子项。

   以下示例代码为底部页签和标题栏的4个按钮设置了沉浸光感效果，根据设备所能支持的材质能力自定义动态切换显示效果。

   ```
   1. @Entry
   2. @Component
   3. export struct Index {
   4. private scrollerForScroll: Scroller = new Scroller();
   5. private controller: HdsTabsController = new HdsTabsController();
   6. @State customMaterialLevel: hdsMaterial.MaterialLevel = hdsMaterial.MaterialLevel.EXQUISITE;

   8. private menus: HdsNavigationMenuContentOptions = {
   9. value: [{
   10. content: {
   11. label: 'menu1',
   12. icon: $r('sys.symbol.square_and_pencil'),
   13. }
   14. }, {
   15. content: {
   16. label: 'menu2',
   17. icon: $r('sys.symbol.star')
   18. },
   19. },{
   20. content: {
   21. label: 'menu3',
   22. icon: $r('sys.symbol.more')
   23. },
   24. }
   25. ],
   26. };

   28. aboutToAppear(): void {
   29. let materialTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
   30. if (materialTypes.indexOf(hdsMaterial.MaterialType.IMMERSIVE) < 0) {
   31. this.customMaterialLevel = hdsMaterial.MaterialLevel.SMOOTH; // 当前设备不支持IMMERSIVE材质类型，则使用SMOOTH效果
   32. }
   33. }

   35. build() {
   36. HdsNavigation() {
   37. HdsTabs({ controller: this.controller }) {
   38. ForEach(MENU_CONFIG, (item: MenuItem) => {
   39. TabContent() {
   40. Stack() {
   41. Scroll(this.scrollerForScroll) {
   42. Column() {
   43. Image($r("app.media.scenery01")).width('100%') // scenery为自定义资源，开发者需替换本地资源
   44. }
   45. }
   46. .clipContent(ContentClipMode.SAFE_AREA)
   47. .height('100%')
   48. }
   49. }
   50. .tabBar(new BottomTabBarStyle({
   51. normal: item.symbolGlyph, selected: item.symbolGlyph1
   52. }, item.label))
   53. })
   54. }
   55. .barOverlap(true)
   56. .vertical(false)
   57. .barPosition(BarPosition.End)
   58. .barFloatingStyle({
   59. barBottomMargin: 28,
   60. systemMaterialEffect:  {
   61. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   62. materialLevel: this.customMaterialLevel // 底部悬浮页签自定义沉浸光感材质效果
   63. }
   64. })
   65. }
   66. .mode(NavigationMode.Stack)
   67. .titleBar({
   68. content: {
   69. title: {
   70. mainTitle: 'MainTitle',
   71. },
   72. menu: this.menus,
   73. },
   74. style: {
   75. scrollEffectOpts: {
   76. enableScrollEffect: false,
   77. scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
   78. },
   79. systemMaterialEffect: {
   80. materialType: hdsMaterial.MaterialType.ADAPTIVE,
   81. materialLevel: this.customMaterialLevel // 标题栏按钮自定义沉浸光感材质效果
   82. },
   83. },
   84. avoidLayoutSafeArea: false,
   85. enableComponentSafeArea: false
   86. })
   87. .bindToScrollable([this.scrollerForScroll])
   88. .hideBackButton(false)
   89. .titleMode(HdsNavigationTitleMode.MINI)
   90. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
   91. }
   92. }

   94. interface MenuItem {
   95. symbolGlyph: SymbolGlyphModifier,
   96. symbolGlyph1: SymbolGlyphModifier,
   97. label: string,
   98. defaultBgColor: ResourceColor,
   99. hoverBgColor: ResourceColor,
   100. pressBgColor: ResourceColor,
   101. };

   103. const MENU_CONFIG: MenuItem[] = [
   104. {
   105. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   106. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   107. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   108. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   109. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   110. label: '闹钟',
   111. defaultBgColor: Color.Transparent,
   112. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   113. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   114. },
   115. {
   116. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   117. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   118. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   119. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   120. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   121. label: '时钟',
   122. defaultBgColor: Color.Transparent,
   123. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   124. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   125. },
   126. {
   127. symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   128. .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
   129. $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
   130. symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
   131. .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
   132. label: '秒表',
   133. defaultBgColor: Color.Transparent,
   134. hoverBgColor: $r('sys.color.ohos_id_color_hover'),
   135. pressBgColor: $r('sys.color.ohos_id_color_click_effect')
   136. }
   137. ];
   ```

   **沉浸光感材质效果展示**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/0KherWvbTBGUmHllhGx8Jw/zh-cn_image_0000002589324721.png?HW-CC-KV=V1&HW-CC-Date=20260429T053026Z&HW-CC-Expire=86400&HW-CC-Sign=455B43E9EEDEF5205F2EC9AC8B47820AF376B91124F0885EB7FF166A923FE3FA)
