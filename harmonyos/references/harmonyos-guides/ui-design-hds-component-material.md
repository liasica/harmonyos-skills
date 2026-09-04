---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-component-material
title: 沉浸光感
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 沉浸光感
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:16+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:75dff956ef33807db0dc6f750ca152ff7dde23fc72dc291246c877730763b44c
---

## 场景介绍

从6.1.0(23) 版本开始，新增支持HDS组件的沉浸光感材质能力。

* **HDS导航**：通过设置[TitleBarStyleOptions](../harmonyos-references/ui-design-hdsnavigation.md#titlebarstyleoptions)的systemMaterialEffect参数，可为标题栏按钮设置沉浸光感视效。
* **HDS底部页签**：通过设置[HdsTabsFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#hdstabsfloatingstyle)的systemMaterialEffect参数，可为底部页签设置沉浸光感视效。

## 使用系统自适应的沉浸光感

推荐使用系统自适应的沉浸光感效果，系统会根据当前设备的算力动态调整组件的材质效果，实现性能与显示效果的最佳平衡体验。

### 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsNavigation, HdsNavigationTitleMode, HdsTabs, HdsTabsController, HdsNavigationMenuContentOptions, ScrollEffectType, hdsMaterial } from '@kit.UIDesignKit';
   import { SymbolGlyphModifier } from '@kit.ArkUI';
   ```
2. 创建HDS导航和底部页签组件。导航标题栏包含1个返回按钮和3个功能按钮，底部页签包含3个子项。

   以下示例代码为底部页签和标题栏的4个按钮设置了沉浸光感效果，该效果将根据系统能力自适应调整。

   ```typescript
   // 自适应沉浸光感示例
   @Entry
   @Component
   export struct AdaptiveIndex {
     private scrollerForScroll: Scroller = new Scroller();
     private controller: HdsTabsController = new HdsTabsController();

     private menus: HdsNavigationMenuContentOptions = {
       value: [{
         content: {
           label: 'menu1',
           icon: $r('sys.symbol.square_and_pencil')
         }
       }, {
         content: {
           label: 'menu2',
           icon: $r('sys.symbol.star')
         }
       },{
         content: {
           label: 'menu3',
           icon: $r('sys.symbol.more')
         }
       }
       ]
     };

     build() {
       HdsNavigation() {
         HdsTabs({ controller: this.controller }) {
           ForEach(MENU_CONFIG, (item: MenuItem) => {
             TabContent() {
               Stack() {
                 Scroll(this.scrollerForScroll) {
                   Column() {
                     Image($r('app.media.scenery01')).width('100%') // scenery为自定义资源，开发者需替换本地资源
                   }
                 }
                 .clipContent(ContentClipMode.SAFE_AREA)
                 .height('100%')
               }
             }
             .tabBar(new BottomTabBarStyle({
               normal: item.symbolGlyph, selected: item.symbolGlyph1
             }, item.label))
           })
         }
         .barOverlap(true)
         .vertical(false)
         .barPosition(BarPosition.End)
         .barFloatingStyle({
           barBottomMargin: 28,
           // 设置沉浸光感效果：ADAPTIVE类型表示自适应系统材质，ADAPTIVE等级表示材质生效策略由系统根据设备性能自适应决定
           systemMaterialEffect: {
             materialType: hdsMaterial.MaterialType.ADAPTIVE,
             materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE // 底部悬浮页签沉浸光感效果跟随系统策略自适应
           }
         })
       }
       .mode(NavigationMode.Stack)
       .titleBar({
         content: {
           title: {
             mainTitle: 'MainTitle',
           },
           menu: this.menus,
         },
         style: {
           scrollEffectOpts: {
             enableScrollEffect: false,
             scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
           },
           // 设置沉浸光感效果：ADAPTIVE类型表示自适应系统材质，ADAPTIVE等级表示材质生效策略由系统根据设备性能自适应决定
           systemMaterialEffect: {
             materialType: hdsMaterial.MaterialType.ADAPTIVE,
             materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE // 标题栏按钮沉浸光感效果跟随系统策略自适应
           },
         },
         avoidLayoutSafeArea: false,
         enableComponentSafeArea: false
       })
       .bindToScrollable([this.scrollerForScroll])
       .hideBackButton(false)
       .titleMode(HdsNavigationTitleMode.MINI)
       .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
     }
   }

   interface MenuItem {
     symbolGlyph: SymbolGlyphModifier,
     symbolGlyph1: SymbolGlyphModifier,
     label: string,
     defaultBgColor: ResourceColor,
     hoverBgColor: ResourceColor,
     pressBgColor: ResourceColor,
   };

   const MENU_CONFIG: MenuItem[] = [
     {
       symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
           $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
       symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
       label: '闹钟',
       defaultBgColor: Color.Transparent,
       hoverBgColor: $r('sys.color.ohos_id_color_hover'),
       pressBgColor: $r('sys.color.ohos_id_color_click_effect')
     },
     {
       symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
           $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
       symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
       label: '时钟',
       defaultBgColor: Color.Transparent,
       hoverBgColor: $r('sys.color.ohos_id_color_hover'),
       pressBgColor: $r('sys.color.ohos_id_color_click_effect')
     },
     {
       symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
           $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
       symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
       label: '秒表',
       defaultBgColor: Color.Transparent,
       hoverBgColor: $r('sys.color.ohos_id_color_hover'),
       pressBgColor: $r('sys.color.ohos_id_color_click_effect')
     }
   ];
   ```

## 使用自定义沉浸光感效果

如果使用自定义沉浸光感的视觉效果，请先调用[getSystemMaterialTypes()](../harmonyos-references/ui-design-hdsmaterial.md#getsystemmaterialtypes)接口查询当前设备所支持的材质能力，再根据查询结果选用相应的材质效果枚举：

1. 如果查询结果显示当前设备支持IMMERSIVE材质类型，可选用EXQUISITE或GENTLE效果。
2. 如果查询结果显示当前设备不支持IMMERSIVE材质类型，则建议使用SMOOTH效果，以降低卡顿和发热风险，保障用户体验。

### 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsNavigation, HdsNavigationTitleMode, HdsTabs, HdsTabsController, HdsNavigationMenuContentOptions, ScrollEffectType, hdsMaterial } from '@kit.UIDesignKit';
   import { SymbolGlyphModifier } from '@kit.ArkUI';
   ```
2. 创建HDS导航和底部页签组件。导航标题栏包含1个返回按钮和3个功能按钮，底部页签包含3个子项。

   以下示例代码为底部页签和标题栏的4个按钮设置了沉浸光感效果，根据设备所能支持的材质能力自定义动态切换显示效果。

   ```typescript
   // 自定义沉浸光感示例
   @Entry
   @Component
   export struct CustomIndex {
     private scrollerForScroll: Scroller = new Scroller();
     private controller: HdsTabsController = new HdsTabsController();
     @State customMaterialLevel: hdsMaterial.MaterialLevel = hdsMaterial.MaterialLevel.EXQUISITE;

     private menus: HdsNavigationMenuContentOptions = {
       value: [{
         content: {
           label: 'menu1',
           icon: $r('sys.symbol.square_and_pencil')
         }
       }, {
         content: {
           label: 'menu2',
           icon: $r('sys.symbol.star')
         }
       },{
         content: {
           label: 'menu3',
           icon: $r('sys.symbol.more')
         }
       }
       ]
     };

     aboutToAppear(): void {
       // 获取系统支持的材质类型，用于根据设备能力选择合适的材质等级
       let materialTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
       if (materialTypes.indexOf(hdsMaterial.MaterialType.IMMERSIVE) < 0) {
         // 当前设备不支持IMMERSIVE材质类型，则使用SMOOTH效果以优化性能，降低卡顿和发热风险
         this.customMaterialLevel = hdsMaterial.MaterialLevel.SMOOTH;
       }
     }

     build() {
       HdsNavigation() {
         HdsTabs({ controller: this.controller }) {
           ForEach(MENU_CONFIG, (item: MenuItem) => {
             TabContent() {
               Stack() {
                 Scroll(this.scrollerForScroll) {
                   Column() {
                     Image($r('app.media.scenery01')).width('100%') // scenery为自定义资源，开发者需替换本地资源
                   }
                 }
                 .clipContent(ContentClipMode.SAFE_AREA)
                 .height('100%')
               }
             }
             .tabBar(new BottomTabBarStyle({
               normal: item.symbolGlyph, selected: item.symbolGlyph1
             }, item.label))
           })
         }
         .barOverlap(true)
         .vertical(false)
         .barPosition(BarPosition.End)
         .barFloatingStyle({
           barBottomMargin: 28,
           systemMaterialEffect: {
             materialType: hdsMaterial.MaterialType.ADAPTIVE,
             materialLevel: this.customMaterialLevel // 底部悬浮页签自定义沉浸光感材质效果
           }
         })
       }
       .mode(NavigationMode.Stack)
       .titleBar({
         content: {
           title: {
             mainTitle: 'MainTitle',
           },
           menu: this.menus,
         },
         style: {
           scrollEffectOpts: {
             enableScrollEffect: false,
             scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
           },
           systemMaterialEffect: {
             materialType: hdsMaterial.MaterialType.ADAPTIVE,
             materialLevel: this.customMaterialLevel // 标题栏按钮自定义沉浸光感材质效果
           },
         },
         avoidLayoutSafeArea: false,
         enableComponentSafeArea: false
       })
       .bindToScrollable([this.scrollerForScroll])
       .hideBackButton(false)
       .titleMode(HdsNavigationTitleMode.MINI)
       .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
     }
   }

   interface MenuItem {
     symbolGlyph: SymbolGlyphModifier,
     symbolGlyph1: SymbolGlyphModifier,
     label: string,
     defaultBgColor: ResourceColor,
     hoverBgColor: ResourceColor,
     pressBgColor: ResourceColor,
   };

   const MENU_CONFIG: MenuItem[] = [
     {
       symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
           $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
       symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.alarm_fill_1')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
       label: '闹钟',
       defaultBgColor: Color.Transparent,
       hoverBgColor: $r('sys.color.ohos_id_color_hover'),
       pressBgColor: $r('sys.color.ohos_id_color_click_effect')
     },
     {
       symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
           $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
       symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.worldclock_fill_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
       label: '时钟',
       defaultBgColor: Color.Transparent,
       hoverBgColor: $r('sys.color.ohos_id_color_hover'),
       pressBgColor: $r('sys.color.ohos_id_color_click_effect')
     },
     {
       symbolGlyph: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_bottom_tab_icon_off'),
           $r('sys.color.ohos_id_color_bottom_tab_icon_auxcolor_off02')]),
       symbolGlyph1: new SymbolGlyphModifier($r('sys.symbol.stopwatch_2')).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
         .fontColor([$r('sys.color.ohos_id_color_activated'), $r('sys.color.ohos_id_color_primary_contrary')]),
       label: '秒表',
       defaultBgColor: Color.Transparent,
       hoverBgColor: $r('sys.color.ohos_id_color_hover'),
       pressBgColor: $r('sys.color.ohos_id_color_click_effect')
     }
   ];
   ```

   **沉浸光感材质效果展示**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/P-sCQ1R4TSCNQ3gWXcJVig/zh-cn_image_0000002712244488.png)
