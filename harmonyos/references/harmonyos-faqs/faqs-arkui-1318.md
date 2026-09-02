---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1318
title: 应用未适配悬浮窗模式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用未适配悬浮窗模式
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0f3e2ae1577e0b3efcc0ccd83d83103776ecd1d1bbaa7bcd1a9dc892e1e8e961
---

## 问题现象

问题一：应用上滑，右上角未出现悬浮窗图标，确认应用不支持悬浮窗。

问题二：应用未适配悬浮窗，出现页面截断、图片挤压、组件堆叠等现象。

问题三：应用是横屏应用，打开了默认的竖向悬浮窗。

## 背景知识

1. [module.json5](../harmonyos-guides/module-configuration-file.md)的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中supportWindowMode标识当前UIAbility组件所支持的窗口模式，preferMultiWindowOrientation属性主要标识当前UIAbility组件多窗布局方向。
2. [on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)方法可和[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口是否进入悬浮窗模式及尺寸大小变化的监听。
3. [顶部窗口控制条避让适配智慧多窗](../harmonyos-guides/multi-window-controlbar-adapt.md)，顶部横条的避让可通过以下两种方式适配：
   * 使用窗口的避让能力：通过setWindowLayoutFullScreen设置窗口布局是否为沉浸式布局。
   * 应用主动避让：应用不使用窗口避让能力（即设置窗口为沉浸式布局），通过getWindowAvoidArea接口获取屏幕顶部需要规避的矩阵区域topRect，获取到该值后应用可对应做布局避让。

## 问题定位

### 问题一

应用不支持悬浮窗模式。

检查应用是否支持悬浮窗模式。查看module.json5文件中abilities标签中supportWindowMode配置项，未缺省且未设置floating。

### 问题二

应用未适配悬浮窗模式。

1. 检查是否开启窗口模式变化的监听，通过[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)方法，根据窗口模式发生变化时返回值对应为[WindowStatusType](../harmonyos-references/arkts-apis-window-e.md#windowstatustype11)来判断当前界面状态，[WindowStatusType](../harmonyos-references/arkts-apis-window-e.md#windowstatustype11)=4为悬浮窗模式。
2. 通过getWindowProperties方法返回的windowRect属性获取窗口尺寸，存入AppStorage。使用[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法来监听窗口尺寸的变化。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
       console.info('Ability onWindowStageCreate.');
       windowStage.getMainWindow().then((windowClass) => {
         // 获取窗口尺寸，存入AppStorage
         AppStorage.setOrCreate('winWidth', windowClass.getWindowProperties().windowRect.width);
         AppStorage.setOrCreate('winHeight', windowClass.getWindowProperties().windowRect.height);
         // 监听窗口尺寸变化
         windowClass.on('windowSizeChange', (windowSize) => {
           AppStorage.setOrCreate('winWidth', windowSize.width);
           AppStorage.setOrCreate('winHeight', windowSize.height);
         });
       });
   }
   ```
3. UI侧通过@StorageLink绑定窗口尺寸后，AppStorage中属性key值对应的数据一旦改变，UI侧会同步修改。通过@StorageLink装饰的数据在窗口尺寸发生变化时会引起组件的重新渲染，可以根据最新的窗口尺寸动态调整应用布局。

   ```ts
   // Index.ets
   @Entry
   @Component
   struct Index {
     // 初始化参数，这里会初始化为AppStorage中存储的值
     @StorageLink('winWidth') winWidth: number | undefined = AppStorage.get('winWidth');
     @StorageLink('winHeight') winHeight: number | undefined = AppStorage.get('winHeight');

     build() {
       Row() {
         // 根据winWidth、winHeight动态调整应用布局
       }
       .size({
         width: this.getUIContext().px2vp(this.winWidth),
         height: this.getUIContext().px2vp(this.winHeight)
       })
     }
   }
   ```

### 问题三

应用未支持横向悬浮窗模式。搜索关键词module.json5文件中abilities标签中preferMultiWindowOrientation配置项，是否配置landscape值。

## 分析结论

### 问题一

应用不支持悬浮窗模式：未在module.json5文件中abilities标签里supportWindowMode配置项中未缺省且未配置floating值。

### 问题二

未适配悬浮窗模式：未监听'windowStatusChange'事件或未监听'windowSizeChange'事件，并且动态调整布局。

### 问题三

不支持横向悬浮窗模式：未在module.json5文件中abilities标签里preferMultiWindowOrientation配置项配置landscape支持横向悬浮窗。

## 修改建议

### 问题一

应用不支持悬浮窗模式：在module.json5文件中abilities标签里supportWindowMode配置项直接缺省（缺省时，缺省值为["fullscreen", "split", "floating"]），或配置时加上floating值。

### 问题二

未适配悬浮窗模式，监听windowStatusChange、windowSizeChange事件，需要动态调整布局。应用要保证页面布局能够完整显示，避免出现截断、挤压、堆叠等现象。

### 问题三

在module.json5文件中abilities标签里preferMultiWindowOrientation配置项配置支持横向悬浮窗的设置。（默认为竖向悬浮窗）可参考[官方示例](../best-practices/bpta-multi-window-practice.md#section364215616276)。
