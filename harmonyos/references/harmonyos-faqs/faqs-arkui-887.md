---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-887
title: 如何实现舵式底部导航
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现舵式底部导航
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a3485ca4a595f11b917ad77f3dd76327bdb83e627fa7c8a387986431aa4b33c0
---

## 问题现象

如何实现底部导航栏中某个页签凸起并超出导航条高度，呈现舵式导航样式？

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [舵式底部导航](../best-practices/bpta-multi-tab-practice.md#section670810557305)：是基础底部导航的一种扩展，中间按钮一般为核心功能，并且在设计效果上中心图标可以超出导航条的高度，两侧为普通操作按钮。
* [offset](../harmonyos-references/ts-universal-attributes-location.md#offset)：相对偏移，组件相对原本的布局位置进行偏移。

## 解决方案

本文将介绍几种常见舵式导航样式和实现方案。

| 实现场景 | 实现方案 |
| --- | --- |
| 场景一：中间图标超出标签栏显示。 | 基于[Flex](../harmonyos-references/ts-container-flex.md)布局实现自定义页签栏，居中页签通过offset属性超出页签栏显示。 |
| 场景二：页签栏实现凸起/凹陷视觉效果，页签点击切换时具有切换动画。 | 自定义组件实现标签栏，通过[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)实现凸起/凹陷的样式、[animateTo](../harmonyos-references/ts-explicit-animation.md)实现切换的动画效果。 |
| 场景三：点击某个页签，此页签能超出页签栏显示。 | 基于[tabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)属性实现页签栏，设置TabBar的clip属性为false，被点击页签通过offset属性超出页签栏显示。 |
| 场景四：中间页签凸起显示，并伴有弧形背景。 | 自定义组件实现页签栏，基于[Stack](../harmonyos-references/ts-container-stack.md)在页签下方叠放弧线背景，设置Stack组件的clip属性为false，居中页签通过offset属性超出页签栏显示。 |

1. **场景一**：中间图标超出标签栏显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ctSEtHiDSaCbWwFm5PUplw/zh-cn_image_0000002658798905.png "点击放大")

   实现方案：导航条通过Flex布局实现，替代tabBar属性设置，并通过offset控制中心图标与两侧图标的位置。详细说明请参考舵式底部导航。实现代码见[基于Tabs组件实现常见导航样式](https://gitcode.com/HarmonyOS_Samples/multi-tab-navigation)。
2. **场景二**：页签栏实现凸起/凹陷视觉效果，页签点击切换时具有切换动画。

   实现方案：未使用tabBar属性，通过自定义组件实现页签栏。详细实现步骤和代码见[自定义TabBar页签凸起和凹陷案例](https://gitee.com/harmonyos-cases/cases/tree/master/CommonAppDevelopment/feature/customdrawtabbar)。
3. **场景三**：点击某个页签，此页签能超出页签栏显示。

   实现方案：基于tabBar属性实现页签栏，通过使用[TabsOptions](../harmonyos-references/ts-container-tabs.md#tabsoptions15)中的barModifier设置TabBar的clip属性为true，再设置页签的offset属性实现页签超出tabBar区域显示效果。实现代码见[页签超出TabBar区域显示](../harmonyos-references/ts-container-tabs.md#示例15页签超出tabbar区域显示)。
4. **场景四**：中间页签凸起显示，并伴有弧形背景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ARV8tZ-IQF2MeqkH3uCH4A/zh-cn_image_0000002628559544.png "点击放大")

   实现方案：未使用tabBar属性，通过自定义组件实现页签栏。通过Stack堆叠组件实现弧形背景，通过offset属性超出页签栏显示。

   ```ts
   @Entry
   @Component
   struct RudderStyleTab {
     @State tabArray: Array<number> = [0, 1, 2, 3, 4];
     @State focusIndex: number = 0;
     private controller: TabsController = new TabsController();

     @Builder
     tabBuilder(tabName: string, tabIndex: number) {
       Column() {
         Stack({ alignContent: Alignment.Center }) {
           if (tabIndex === 2) {
             Column() {
             }
             .width('100%')
             .height('100%')
             .backgroundColor(Color.White)
             .offset({ bottom: 20 })
             .borderRadius({
               topLeft: 100,
               topRight: 100
             });
           }
           Column({ space: 10 }) {
             Image($r('app.media.startIcon'))
               .width(tabIndex === 2 ? 42 : 36);
             Text(tabName);
           }.width('100%').height('100%')
           .offset({ bottom: tabIndex === 2 ? 10 : 0 })
           .justifyContent(FlexAlign.Center);
         }.width('100%').height('100%').clip(false);
       }
       .width('20%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
       .onClick(() => {
         this.controller.changeIndex(tabIndex);
         this.focusIndex = tabIndex;
       });
     }

     build() {
       Flex({ direction: FlexDirection.Column }) {
         Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
           ForEach(this.tabArray, (item: number) => {
             TabContent() {
               Column() {
                 Text('我是页面 ' + item + ' 的内容')
                   .fontSize(30);
               }.width('100%').height('100%').justifyContent(FlexAlign.Center);
             };
           });
         }
         .background('#F1F3F5')
         .barHeight(0)
         .animationDuration(100)
         .onChange((index: number) => {
           console.info('foo change');
           this.focusIndex = index;
         });

         // 页签
         Flex({ alignItems: ItemAlign.End }) {
           ForEach(this.tabArray, (item: number, index: number) => {
             this.tabBuilder('页签 ' + item, index);
           });
         }
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
         .layoutWeight(0)
         .height('90vp')
         .width('100%');
       }.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
       .width('100%')
       .height('100%');
     }
   }
   ```
