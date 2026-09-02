---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1240
title: 应用未适配分屏模式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用未适配分屏模式
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3f8e8b7c1943a4104688f440c8a2679277601776ceb2a1c99825a779b8b96036
---

## 问题现象

### 问题一

应用上滑，左上角未出现分屏图标，确认应用不支持分屏。

### 问题二

应用未适配分屏模式，出现图片截断、文字挤压、组件遮挡等。

### 问题三

分屏下导致全屏完整显示的内容在上下分屏时显示不全。

## 背景知识

* [abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签中supportWindowMode可以设置UIAbility组件所支持的窗口模式是否支持分屏。preferMultiWindowOrientation属性主要标识当前UIAbility组件多窗布局方向，缺省默认支持。
* 应用可以通过[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)方法可以检测窗口是否进入分屏状态。
* 从全屏进入分屏模式后，窗口尺寸、宽高比例会发生变化。[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)实现对窗口尺寸大小变化的监听，再根据窗口的尺寸变化，更新调整自身应用布局以实现适配。
* 参考[合理控制元素显示与隐藏](../best-practices-V5/bpta-improve-layout-performance-V5.md#section14111154271)设置[小窗口布局](../best-practices-V5/bpta-phone-split-guide-V5.md#section88711672417)。
* [Scroll组件](../harmonyos-references/ts-container-scroll.md)是可滚动的容器组件，上下分屏时，窗口高度会减小至约屏幕的1/2，可能导致全屏完整显示的内容在上下分屏时显示不全。推荐使用Scroll组件实现页面支持滑动。

## 问题定位

### 问题一

对于应用不支持分屏模式。 查看module.json5中abilities标签中supportWindowMode配置项，确定是否未缺省且未配置split。

### 问题二

布局未适配分屏模式。确定是否未监听windowSizeChange事件，判断布局是否适配分屏模式。

### 问题三

分屏下导致全屏完整显示的内容在上下分屏时显示不全：全局搜索Scroll或检查scrollBar属性是否为BarState.Off。

## 分析结论

### 问题一

不支持分屏模式：由于在module.json5中abilities标签中supportWindowMode配置项中未缺省且未配置split。

### 问题二

未适配分屏模式：未监听windowStatusChange事件且未监听windowSizeChange事件，并且动态调整布局和设置小窗口布局。

### 问题三

分屏下导致全屏完整显示的内容在上下分屏时显示不全：未使用Scroll组件（全局搜索Scroll）或设置Scroll组件的scrollBar属性为BarState.Off。

## 修改建议

### 问题一

在module.json5中abilities标签中supportWindowMode配置项中配置split，或将supportWindowMode缺省默认支持分屏模式。

### 问题二

监听windowSizeChange事件，动态调整布局并设置小窗口布局。适配分屏的应用保证页面布局能够完整显示，避免出现截断、挤压、堆叠等现象。

1. 检查是否开启窗口模式变化的监听，通过[on(windowStatusChange)](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)方法，根据窗口windowStatus发生变化时返回值对应[WindowStatusType](../harmonyos-references/arkts-apis-window-e.md#windowstatustype11)为SPLIT\_SCREEN来判断当前界面状态。
2. 检查应用中是否获取窗口属性，用[getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法获取窗口的尺寸信息。

   ```screen
   export default class MainAbility extends UIAbility {
     private windowObj?: window.Window
     private curBp: string = ''
     private updateBreakpoint(windowWidth: number) :void{
       // 拿到当前窗口对象获取当前所在displayId
       let displayId = this.windowObj?.getWindowProperties().displayId
       try {
         let windowWidthVp = windowWidth / display.getDisplayByIdSync(displayId).densityPixels
         let newBp: string = ''
         if (windowWidthVp < 320) {
           newBp = 'xs'
         } else if (windowWidthVp < 600) {
           newBp = 'sm'
         } else if (windowWidthVp < 840) {
           newBp = 'md'
         } else {
           newBp = 'lg'
         }
         if (this.curBp !== newBp) {
           this.curBp = newBp
           AppStorage.setOrCreate('currentBreakpoint', this.curBp);
         }
       } catch(err) {
         console.log("getDisplayByIdSync failed err"+err.code);
       }
     }
   }
   ```
3. 监听窗口尺寸变化。使用[on(windowSizeChange)](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法来监听窗口尺寸的变化。

   ```screen
   onWindowStageCreate(windowStage: window.WindowStage) :void{
       windowStage.getMainWindow().then((windowObj) => {
         this.windowObj = windowObj
         // 获取应用启动时的窗口尺寸
         this.updateBreakpoint(windowObj.getWindowProperties().windowRect.width);
         // 注册回调函数，监听窗口尺寸变化
         windowObj.on('windowSizeChange', (windowSize)=>{
           this.updateBreakpoint(windowSize.width)
         })
       });
       // ...
     }
   ```
4. 窗口尺寸发生变化后需动态调整布局。UI侧通过@StorageLink绑定窗口尺寸后，AppStorage中属性key值对应的数据改变，UI侧会同步修改。@StorageLink绑定的数据是状态变量，窗口尺寸发生变化时，会引起组件的重新渲染。可以参考[应用布局适配智慧多窗的方案](../harmonyos-guides/multi-window-layout-adapt.md#应用布局适配智慧多窗的方案)。
5. 最后检查是否设置了[小窗口布局](../best-practices-V5/bpta-phone-split-guide-V5.md#section88711672417)。在手机上下分屏1:1时，横向断点为sm，纵向断点为md；在手机上下分屏1:2时，比例为1对应窗口的横向断点为sm，纵向断点为sm，推荐使用小窗口布局。上下分屏为2：1时，对应窗口的横向断点为sm，纵向断点为lg。

   ```screen
   // 以设置图片的高度为例，在小窗口布局中高度为24vp，手机全屏时高度为48vp。使用横纵向断点判断，设置具体的属性值。
   Image($r('app.media.arrow_right'))
     .height(this.currentWidthBreakpoint === 'sm' && (this.currentHeightBreakpoint === 'sm' ||
       this.currentHeightBreakpoint === 'md') ? 24 : 48)
     .aspectRatio(1)
   ```

### 问题三

分屏下导致全屏完整显示的内容在上下分屏时显示不全：设置Scroll组件的scrollBar属性为BarState.Off，控制滚动条不显示。当窗口高度足够显示页面全部内容时，Scroll组件自动失效，页面不可滑动；当窗口高度不足以显示页面全部内容时，Scroll组件自动生效，页面可以滑动。

```screen
Scroll() {
  Column() {
    // ...
  }
  .width('100%')
}
.scrollBar(BarState.Off)
.height('100%')
.width('100%')
```
