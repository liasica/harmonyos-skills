---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smart-reach
title: 智感握姿
breadcrumb: 最佳实践 > 技术创新 > 智感握姿
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:49b319fb1e5fdb91fe6d3197eac846d87a86223f555fab2c4db62d1be92575c1
---

随着大屏和折叠屏设备的普及，用户单手握持设备时，拇指难以覆盖整个屏幕区域，尤其是位于屏幕顶部与侧边的交互元素往往难以触及。为有效解决这一痛点，HarmonyOS系统提供了[智感握姿](../design-guides/smart-reachability-0000002556657823.md)能力。该能力能够实时识别用户与设备的交互姿态，应用可据此将核心高频组件动态调整至拇指的可达范围内，从而显著提升单手操作的便捷性。智感握姿示例图如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Z8CRsm5qRk21-C06kBbbLA/zh-cn_image_0000002594053134.png "点击放大")

本文将从智感握姿的概念与适用场景出发，结合新闻阅读应用示例，详细讲解如何在HarmonyOS应用中接入智感握姿能力，具体包括组件原生适配与自定义交互感知两种方案。

## 智感握姿介绍

### 什么是智感握姿

智感握姿是HarmonyOS系统提供的一项交互增强能力。系统通过设备传感器实时识别用户与设备的交互姿态，并将该状态暴露给应用层。应用可以根据握持手信息或者交互手信息，动态调整UI布局，将操作按钮、导航栏等关键交互元素移动到用户拇指舒适可达的区域。智感握姿包括以下两种能力：

* 握持手识别：设备当前被哪只手握着 (左/右/双手/未握持) 。
* 交互手识别：用户当前用哪只手在屏上操作 (左/右手) 。

这一能力的核心价值在于：

* 降低操作负担：通过动态调整组件位置，降低操作吃力感与误触率。
* 智能姿态感知：基于对“握持手”与“交互手”的实时识别，实现组件随用户习惯动态适配。

### 适用场景

智感握姿在以下场景中能显著提升用户体验：

| **场景** | **说明** |
| --- | --- |
| **浮动按钮/面板自动切换** | 悬浮操作按钮、浮动面板根据握持手或者交互手自动左右切换位置，始终处于拇指可达区域。 |
| **单手模式UI适配** | 在单手握持时，将关键操作区域（如底部导航、侧边栏）调整到握持手一侧。 |
| **阅读应用翻页按钮优化** | 翻页按钮、阅读工具栏根据握持手动态调整位置，避免手指跨越整个屏幕操作。 |

不接入场景：

* 低频/非操作类组件不建议接入，避免界面不稳定。
* 广告/诱导类组件不建议接入。

## 应用接入智感握姿方案

在HarmonyOS中，接入智感握姿主要有两种方案：

1. 自定义交互感知：通过监听系统握持手或者交互手状态变化，自行控制UI布局的动态调整。
2. 组件原生适配：使用系统组件（如[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)）内置的智感握姿支持，通过简单属性配置即可实现。

### 方案一：自定义交互感知实现智感握姿

当系统组件未开放相应属性或参数，开发者可以使用HarmonyOS提供的对用户动作的感知能力，包括用户的握持手状态、交互手状态等，详细的接口介绍请参考[@ohos.multimodalAwareness.motion (动作感知能力)](../harmonyos-references/js-apis-awareness-motion.md)。具体开发步骤可以查看[获取用户动作开发指导](../harmonyos-guides/motion-guidelines.md)。其中包括：

* [获取操作手状态开发指导](../harmonyos-guides/motion-guidelines.md#获取操作手状态开发指导)
* [获取握持手状态开发指导](../harmonyos-guides/motion-guidelines.md#获取握持手状态开发指导)

### 方案二：组件设置智感握姿

部分[ArkTS组件](../harmonyos-references/ui-design-arkts-component.md)已经内置了智感握姿的支持，开发者只需通过属性配置即可启用。以[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)组件为例，当设置[barOverlap](../harmonyos-references/ui-design-hdstabs.md#baroverlap)启用悬浮态时，通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性中的adaptToHandedness设置为true，即可实现底部页签栏自动跟随交互手切换位置，无需手动监听交互状态。

**说明** 

这种方式的优势在于零代码逻辑。组件内部已经处理了交互手状态监听和位置切换，开发者只需通过简单的属性配置即可获得智感握姿能力。

## 新闻阅读界面适配智感握姿

本示例以新闻阅读应用为场景，完整演示了智感握姿适配：通过HdsTabs实现底部悬浮导航，结合瀑布流内容布局，使页签栏能够智能跟随交互手自动切换位置，同时通过[@ohos.multimodalAwareness.motion (动作感知能力)](../harmonyos-references/js-apis-awareness-motion.md)中的[motion.on('holdingHandChanged')](../harmonyos-references/js-apis-awareness-motion.md#motiononholdinghandchanged-20)，自定义实现实时感知握持手状态，动态调整侧边按钮位置以提升单手操作体验。

### 底部悬浮导航

本示例通过配置HdsTabs的[barOverlap](../harmonyos-references/ui-design-hdstabs.md#baroverlap)属性开启底部悬浮模式，同时启用[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性中的adaptToHandedness参数实现智感握姿自动跟随功能。效果图如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/zI4UtBoGR0GRQLQ5vJOdVw/zh-cn_image_0000002624492661.gif)

具体适配方式如下：

```screen
HdsTabs({ controller: this.controller }) {
  Repeat(this.tabsBar).each((repeatItem: RepeatItem<BottomTabBarStyle>) => {
    TabContent() {
      // ...
    }
    .tabBar(repeatItem.item)
  })
}
.width('100%')
.height('100%')
.barOverlap(true)
.vertical(false)
.onAttach(() => {
  try {
    this.controller.preloadItems([0, 1, 2, 3]);
  } catch (error) {
    Logger.error(TAG, `OnAttach preloadItems failed`);
  }
})
.barPosition(BarPosition.End)
.barFloatingStyle({
  adaptToHandedness: true,
  barBottomMargin: this.globalInfoModel.naviIndicatorHeight > 0 ? this.globalInfoModel.naviIndicatorHeight :
    $r('sys.float.padding_level8'),
  // ...
})
```

**说明** 

关键属性说明：

* barOverlap(true)：允许页签栏与内容区域重叠，实现悬浮效果。
* barPosition(BarPosition.End)：将页签栏放置在底部。
* adaptToHandedness(true)：启用智感握姿，页签栏自动跟随交互手切换左右位置。
* barBottomMargin：设置为导航指示器高度，确保悬浮页签栏不被系统导航指示器遮挡。

### 侧边按钮悬浮导航

本示例中侧边按钮通过自定义感知握持状态实现智感握姿。效果图如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/8-G5c7THRxiYSb1E9G_bPA/zh-cn_image_0000002690301446.gif "点击放大")

具体适配步骤如下：

1. 配置权限

   在module.json5中声明获取用户动作所需的权限：

   ```screen
   {
     "module": {
       // ...
       "requestPermissions": [
         {
           "name": "ohos.permission.DETECT_GESTURE",
           "reason": "$string:gesture_reason",
           "usedScene": {
             "abilities": [
               "SmartreachAbility"
             ],
             "when": "inuse"
           }
         }
       ],
     }
   }
   ```
2. 订阅握持手变化

   通过[@ohos.multimodalAwareness.motion (动作感知能力)](../harmonyos-references/js-apis-awareness-motion.md)中的[motion.on('holdingHandChanged')](../harmonyos-references/js-apis-awareness-motion.md#motiononholdinghandchanged-20)，订阅握持手状态变化。其中，[HoldingHandStatus](../harmonyos-references/js-apis-awareness-motion.md#holdinghandstatus20)支持未握持（NOT\_HELD）、左手握持（LEFT\_HAND\_HELD）、右手握持（RIGHT\_HAND\_HELD）、双手握持（BOTH\_HANDS\_HELD）以及未识别（UNKNOWN\_STATUS）状态。

   ```screen
   import { motion } from '@kit.MultimodalAwarenessKit';
   // ...
     handleHoldingHandChange: Callback<motion.HoldingHandStatus> = (status: motion.HoldingHandStatus) => {
       // ...
     }

     aboutToAppear(): void {
       // ...
       try {
         if (canIUse('SystemCapability.MultimodalAwareness.Motion')) {
           motion.on('holdingHandChanged', this.handleHoldingHandChange);
           Logger.info(TAG, `Succeed handle on holdingHandChanged`);
         } else {
           Logger.error(TAG, `Can not handle on holdingHandChanged`);
         }
       } catch (error) {
         Logger.error(TAG, `Failed on holdingHandChanged. cause${error.message}`);
       }
     }

     aboutToDisappear(): void {
       try {
         if (canIUse('SystemCapability.MultimodalAwareness.Motion')) {
           motion.off('holdingHandChanged', this.handleHoldingHandChange);
         } else {
           Logger.error(TAG, `Can not handle off holdingHandChanged`);
         }
       } catch (error) {
         Logger.error(TAG, `Failed off holdingHandChanged. cause${error.message}`);
       }
     }

     // ...
   ```
3. 设置过渡动画

   侧边悬浮按钮跟手移动方式为从屏外绕行到对侧，即：先沿当前侧边滑出屏幕外消失，再从对侧屏幕外滑入出现。跟手移动时垂直高度不变，左右侧边距一致。动画实现上设置isFloatingRight和floatingHasAppeared状态变量，分别控制悬浮按钮位置和悬浮按钮首次出场，使用if/else条件渲染左右两个悬浮按钮，配合TransitionEffect.move()实现组件插入/移除时的侧边滑入滑出动画。当isFloatingRight状态切换时：

   * 旧按钮触发退出过渡，沿当前侧边滑出消失
   * 新按钮触发进入过渡，从对侧屏幕外滑入出现

   两个过渡由框架自动同步执行，无需手动管理动画时序。

   ```screen
     @Local isFloatingRight: boolean = true;
     @Local floatingHasAppeared: boolean = false;
     handleHoldingHandChange: Callback<motion.HoldingHandStatus> = (status: motion.HoldingHandStatus) => {
       Logger.info(TAG, `handle on holdingHandChanged:::${status}`);
       if (canIUse('SystemCapability.MultimodalAwareness.Motion')) {
         if (status === motion.HoldingHandStatus.LEFT_HAND_HELD) {
           this.isFloatingRight = false;
         } else if (status === motion.HoldingHandStatus.RIGHT_HAND_HELD) {
           this.isFloatingRight = true;
         }
       }
     }

     @Builder
     floatingButton(alignRules: AlignRuleOption, edge: TransitionEdge, curve: ICurve) {
       Row() {
         SymbolGlyph($r('sys.symbol.square_and_pencil_fill'))
           .fontColor([$r('sys.color.icon_on_primary')])
           .fontSize($r('sys.float.Title_M'))
       }
       .alignRules(alignRules)
       .transition(
         TransitionEffect.move(edge)
           .animation({ curve: curve })
       )
       .onAppear(() => {
         this.floatingHasAppeared = true;
       })
       .margin({
         left: new BreakpointType({
           sm: $r('sys.float.padding_level8'),
           md: $r('sys.float.padding_level12'),
           lg: $r('sys.float.padding_level16')
         }).getValue(this.globalInfoModel.widthBreakpoint),
         right: new BreakpointType({
           sm: $r('sys.float.padding_level8'),
           md: $r('sys.float.padding_level12'),
           lg: $r('sys.float.padding_level16')
         }).getValue(this.globalInfoModel.widthBreakpoint),
         bottom: 100,
       })
       .backgroundColor($r('sys.color.background_emphasize'))
       .borderRadius('50%')
       .clip(true)
       .alignItems(VerticalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .width(56)
       .aspectRatio(1)
     }

     build() {
       HdsNavigation() {
         RelativeContainer() {
           HdsTabs({ controller: this.controller }) {
             // ...
           }
           // ...
           if (this.isFloatingRight) {
             this.floatingButton(
               {
                 right: { anchor: '__container__', align: HorizontalAlign.End },
                 bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
               },
               TransitionEdge.END,
               this.floatingHasAppeared ? curves.interpolatingSpring(0, 1, 170, 17) :
                 curves.interpolatingSpring(0, 1, 200, 17)
             )
           } else {
             this.floatingButton(
               {
                 left: { anchor: '__container__', align: HorizontalAlign.Start },
                 bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
               },
               TransitionEdge.START,
               curves.interpolatingSpring(0, 1, 170, 17)
             )
           }
         }
       }
       // ...
     }
   }
   ```

## 常见问题

### 智感握姿在所有设备上都支持吗？

不是。智感握姿依赖设备硬件传感器的支持，部分设备可能不具备握持检测能力。建议在应用中做好兼容处理，当设备不支持时提供默认布局。可以通过功能提示弹窗告知用户"当前机型暂不支持该功能"。自定义握持感知方案可以使用[checkAccessToken](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)判断应用被授予ohos.permission.DETECT\_GESTURE权限状态，如果设备不支持，将返回801错误码。具体可参考获取握持手状态开发指导的[约束与限制](../harmonyos-guides/motion-guidelines.md#约束与限制-1)。

### 如何适配兼容性，最低支持哪个API版本？

HDS（HarmonyOS Design System）组件的智感握姿能力最低从API version 23开始支持。如果应用需要兼容更低版本，应使用自定义交互感知方案。需注意从API version 15开始，支持获取操作手状态。从API version 20开始，支持获取握持手状态。详情查看[获取用户动作开发指导](../harmonyos-guides/motion-guidelines.md)。

### 握持手切换时如何避免UI闪烁？

建议在握持手状态变化时添加过渡动画，设置合理的动画时长和缓动曲线，使位置切换平滑自然。详情参考[悬浮组件](../design-guides/smart-reachability-0000002556657823.md#section1447018517013)和[动效规则](../design-guides/smart-reachability-0000002556657823.md#section6991043126)。

| 场景 | 曲线 | 说明 |
| --- | --- | --- |
| 组件出场位移动画（首次出现） | interpolatingSpring(0, 1, 200, 17) | stiffness=200，弹性稍强，出场更利落 |
| 从屏幕外移出或移入 | interpolatingSpring(0, 1, 170, 17) | stiffness=170，弹性较柔，侧边绕行更自然 |

## 示例代码

* [智感握姿](https://gitcode.com/HarmonyOS_Samples/SmartReach/tree/master)
