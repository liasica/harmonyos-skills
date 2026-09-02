---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-folded-hover
title: 折叠屏悬停态
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 特殊界面布局场景 > 折叠屏悬停态
category: best-practices
scraped_at: 2026-09-02T15:03:18+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:170206bcfea10bf3d69096c89838650d36786640cf4aa505b8094284d5c168b5
---

## 概述

折叠屏提供独特的手持操作体验“悬停态”，用户可以将设备半折后立在桌面上，实现免手持体验。悬停态适用于不需要频繁交互的任务，如视频通话、视频播放、拍照和听歌。进入悬停态时，中间弯折区域难以操作且显示内容会变形，建议页面内容进行折痕区避让适配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/vyXRzwQ1RfCLSvsQhFeLcw/zh-cn_image_0000002194010932.png "点击放大")

本文提供折叠屏悬停态的三种实现方式，并根据其特点给出各自的适用场景。

* [使用FolderStack组件实现悬停态](bpta-folded-hover.md#section9671184110015)，适用于视频全屏播放等交互少的场景。
* [使用FoldSplitContainer组件实现悬停态](bpta-folded-hover.md#section122423387410)，适用于分栏显示内容的场景，例如游戏画面和操作区域。
* [自定义实现悬停态](bpta-folded-hover.md#section4691264319)，适用于页面布局复杂和悬停态触发动作自定义的场景。

实现悬停态的三种方式中，FolderStack组件使用简便，无需关注设备状态，支持自定义页面布局。FoldSplitContainer组件同样易于使用，但其固定的二分栏和三分栏布局限制了使用场景。自定义实现悬停态需要开发者自行监听设备状态并调整组件布局，支持自定义布局，且由于自定义实现悬停态监听，可以限制设备进入悬停态的场景（例如仅允许在横屏下半折叠时进入悬停态）以及自定义窗口旋转策略，使用更加灵活。

|  | FolderStack | FoldSplitContainer | 自定义实现悬停态 |
| --- | --- | --- | --- |
| 展开态/折叠态是否支持自定义布局 | 支持 | 不支持，固定二分栏/三分栏 | 支持 |
| 是否支持由其他页面进入悬停态页面 | 支持 | 支持 | 支持 |
| 是否支持自定义设备状态进入悬停态页面 | 不支持 | 不支持 | 支持 |
| 是否支持自定义悬停态窗口旋转策略 | 不支持 | 不支持 | 支持 |
| 开发难度 | 简单 | 简单 | 困难 |

本文以视频播放类应用的全屏播放页面为例，介绍FolderStack的自定义悬停态实现。同时，以游戏界面为例，介绍FoldSplitContainer的悬停态实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/6j-xhRiUQg21BOBzxIf4oQ/zh-cn_image_0000002193851340.png)

## 使用FolderStack组件实现悬停态

### 实现原理

[FolderStack](../harmonyos-references/ts-container-folderstack.md)是系统提供的ArkTS组件，继承自[层叠布局(Stack)](../harmonyos-guides/arkts-layout-development-stack-layout.md)。在Stack组件的基础上，FolderStack提供监控设备是否进入悬停态并进行重新布局的能力。

FolderStack通过upperItems字段来实现悬停态布局，当设备进入悬停态时，被upperItems字段修饰的组件会堆叠在上半屏，其他未被修饰的组件会堆叠在下半屏并且自动避让折叠屏折痕区。

**说明** 

FolderStack需要撑满页面全屏，如果不撑满页面全屏，则只作为普通Stack使用。

### 开发步骤

使用FolderStack组件实现悬停态的代码时，将页面的父容器设置为FolderStack，并将视频播放组件的ID注册到upperItems数组中。这样，悬停态时视频播放组件会自动调整到上半屏显示，视频控制组件和顶部返回组件则显示在下半屏。

```typescript
FolderStack({ upperItems: ['upper'] }) {
  VideoPlayView({ avPlayerUtil: this.avPlayerUtil })
    .id('upper')

  VideoControlView({ avPlayerUtil: this.avPlayerUtil })

  BackTitleView({
    title: Const.PAGE_TITLES[0]
  })
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/BHIRu2ySRH2_3IfTsf6oIw/zh-cn_image_0000002229451233.png "点击放大")

## 使用FoldSplitContainer组件实现悬停态

### 实现原理

[FoldSplitContainer](../harmonyos-references/ohos-arkui-advanced-foldsplitcontainer.md)是系统提供的分栏类型的ArkTS组件，支持在展开态、悬停态及折叠态下对二分栏和三分栏进行区域布局控制。其中二分栏是上下分栏，三分栏是在二分栏基础上加上侧边栏。

FoldSplitContainer的primary和secondary参数分别设置二分栏的上下区域的布局，extra参数设置三分栏中侧栏区域的布局；通过LayoutOptions参数设置各区域分栏的比例。当设备进入悬停态时，FoldSplitContainer会自动避让折叠屏折痕区。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/7xN4fWdhSiqehSgCnEy_pA/zh-cn_image_0000002229451229.png "点击放大")

### 开发步骤

使用FoldSplitContainer组件实现悬停态的代码结构是将上下屏的组件分别注册到primary和secondary参数的回调中。这样页面呈现为上下分栏布局，并且会在悬停态自动避让折痕区域。二分栏结构已实现页面布局，因此未实现extra参数对应的侧栏。

```typescript
FoldSplitContainer({
  primary: () => {
    this.primaryArea();
  },
  secondary: () => {
    this.secondaryArea();
  }
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/LAgzRX-0SVSv6ariP4L0CA/zh-cn_image_0000002194010928.png "点击放大")

## 自定义实现悬停态

### 实现原理

自定义悬停态布局需要在折叠屏进入悬停态时通过规避折痕避让区，调整页面内组件的尺寸和位置来实现，可分为监听悬停态和调整布局两部分。

1. 监听悬停态：通过[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)接口监听设备是否进入悬停态。同时通过[getlivecreaseregion()](../harmonyos-references/js-apis-display.md#getlivecreaseregion20)接口获取折痕区[FoldCreaseRegion](../harmonyos-references/js-apis-display.md#foldcreaseregion10)，通过折痕区宽高比判断折叠方向：当折痕区宽度大于高度时，表明折痕与屏幕显示方向垂直。当同时满足悬停态和折痕区宽高比条件时，即判断设备进入悬停态。
2. 调整布局：当设备进入悬停态后，通过[display.getCurrentFoldCreaseRegion()](../harmonyos-references/js-apis-display.md#displaygetcurrentfoldcreaseregion10)接口获取折叠屏折痕区域的位置和大小，计算并设置上下半屏组件的尺寸和位置完成悬停态布局。

**说明** 

在退出应用或者退出需要监听折叠态变化的页面时，需要调用[display.off('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayofffoldstatuschange10)接口取消监听。

### 开发步骤

自定义悬停态的视频播放页UI结构较自由，主要实现悬停态监听和组件重新布局。

1. 悬停态通过状态变量isHover进行监听。当折叠屏的折叠状态变化时，判断当前是否为悬停态并更新isHover的值。

   [多设备场景库](https://gitcode.com/HarmonyOS_Samples/MultiDeviceLibrary/tree/dev_hover)封装了悬停态的判断条件，并提供了isHover状态变量，开发者无需关心折叠屏设备的差异，即可高效配悬停态场景。

   在EntryAbility中引入多设备场景库并初始化。

   ```typescript
   const abilityRegi: AbilityRegister = new AbilityRegister(data);
   AppStorage.setOrCreate('multidevicelibrary.abilities', abilityRegi.registerContext('defaults'));
   ```

   通过多设备场景库获取悬停态变量isHover和折痕区变量creaseTopVp，creaseHeightVp。

   ```typescript
   @StorageLink('multidevicelibrary.abilities') @Watch('hoverChange') ctx:
     DefaultContext<Record<keyof string, ConditionValue>> | undefined = undefined;
   @State isHover: boolean = this.ctx?.getField('isHover') as boolean ?? false;
   @State creaseTopVp: number = this.ctx?.getField('creaseTopVp') as number ?? 0;
   @State creaseHeightVp: number = this.ctx?.getField('creaseHeightVp') as number ?? 0;
   private videoHeight: number = DeviceScreen.getDeviceHeight();
   private avPlayerUtil?: AvPlayerUtil;
   private xComponentController: XComponentController = new XComponentController();
   private DEFAULT_VIDEO_RATIO = 1.78

   hoverChange() {
     this.isHover = this.ctx?.getField('isHover') as boolean ?? false;
     this.creaseTopVp = this.ctx?.getField('creaseTopVp') as number ?? 0;
     this.creaseHeightVp = this.ctx?.getField('creaseHeightVp') as number ?? 0;
     Logger.info(`Hover state change ${this.isHover}, ${this.creaseTopVp}, ${this.creaseHeightVp}.`);
     try {
       if (this.windowObj) {
         const screenWidth: number = this.windowObj.getWindowProperties().windowRect.width;
         let currentVideoHeight = this.getUIContext().px2vp(screenWidth) / this.DEFAULT_VIDEO_RATIO;
         this.videoHeight = currentVideoHeight > this.creaseTopVp ? this.creaseTopVp : currentVideoHeight;
       }
     } catch (error) {
       Logger.error(`Window properties get failed, code: ${error.code}, message: ${error.message}.`);
     }
   }
   ```
2. 当设备处于悬停态（isHover为true）时，开发者可以根据creaseTopVp计算组件高度。

   ```typescript
   try {
     if (this.windowObj) {
       const screenWidth: number = this.windowObj.getWindowProperties().windowRect.width;
       let currentVideoHeight = this.getUIContext().px2vp(screenWidth) / this.DEFAULT_VIDEO_RATIO;
       this.videoHeight = currentVideoHeight > this.creaseTopVp ? this.creaseTopVp : currentVideoHeight;
     }
   } catch (error) {
     Logger.error(`Window properties get failed, code: ${error.code}, message: ${error.message}.`);
   }
   ```

   ```typescript
   XComponent({
     id: 'home',
     type: XComponentType.SURFACE,
     controller: this.xComponentController
   })
     .onLoad(() => {
       // ...
     })
     .aspectRatio(this.DEFAULT_VIDEO_RATIO)
     .height(this.isHover ? this.videoHeight : -1)
   ```
3. 根据isHover判断是否处于悬停态状态，并据此调整组件布局。

   处于悬停态时，视频播放组件将上移至屏幕上方。

   ```typescript
   Column() {
     XComponent({
       id: 'home',
       type: XComponentType.SURFACE,
       controller: this.xComponentController
     })
     // ...
   }
   .justifyContent(this.isHover ? FlexAlign.Start : FlexAlign.Center)
   .height(CommonConstants.FULL_PERCENT)
   .width(CommonConstants.FULL_PERCENT)
   ```

   视频控制组件位于下半屏，无需调整。

   ```typescript
   Column() {
     Row() {
       TimeText({ time: this.currentTime })
         .margin({
           left: 36,
           right: 2
         })
       // ...
   }
   .height(CommonConstants.FULL_PERCENT)
   .width(CommonConstants.FULL_PERCENT)
   .justifyContent(FlexAlign.End)
   .visibility(Visibility.Visible)
   ```

**图1** 视频播放页悬停态效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/rwEVn86cQxqnG0ChpY-5Mg/zh-cn_image_0000002728334749.png "点击放大")

## 示例代码

* [多设备场景库](https://gitcode.com/HarmonyOS_Samples/MultiDeviceLibrary/tree/dev_hover)
