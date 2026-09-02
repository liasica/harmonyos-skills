---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1502
title: 悬浮窗模式，应用页面未避让顶部窗口控制条
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 悬浮窗模式，应用页面未避让顶部窗口控制条
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:21cf30cb2be3231fa88b13e356b2556df052a7e23e5efbc811e13ec9f9620cb1
---

## 问题现象

应用在悬浮窗模式下，页面是沉浸式布局，但是未注意悬浮窗模式时，顶部存在的窗口控制条，页面顶部内容与悬浮窗的顶部窗口控制条重叠，可能导致Header区域点击事件被窗口控制条拦截而无法正常点击。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/fvZmgv6JQI2fEfnJE4CDuQ/zh-cn_image_0000002679982924.png "点击放大")

## 背景知识

* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：可设置窗口布局是否为沉浸式布局。
* [顶部窗口控制条](../harmonyos-guides/multi-window-controlbar-adapt.md)：顶部窗口控制条是应用窗口处于智慧多窗模式下，应用顶部的操作横条。
* [沉浸式布局](../best-practices/bpta-multi-device-window-immersive.md)是指应用布局不避让状态栏、导航栏以及智慧多窗顶部横条，这可能发生组件与顶部横条的重叠，导致文字遮挡、点击事件冲突等情况。
* [getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)：获取当前应用窗口避让区。避让区指系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。
* [on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)：开启当前应用窗口系统避让区变化的监听。

## 问题定位

1. 查阅代码中是否调用setWindowLayoutFullScreen接口并设置为true。

   ```ts
   windowClass.setWindowLayoutFullScreen(true)
   ```
2. 查阅代码中是否调用getWindowAvoidArea获取系统默认区域的高度（通常表示状态栏区域，悬浮窗状态下的应用主窗中表示顶部窗口控制条区域）。

   ```ts
   this.topSafeHeight = this.getUIContext().px2vp(windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height)
   ```
3. 查阅代码中是否调用on('avoidAreaChange')监听系统默认区域高度的变化。

   ```ts
   windowClass.on('avoidAreaChange', (data) => {
     if (data.type == window.AvoidAreaType.TYPE_SYSTEM) {
       this.topSafeHeight = this.getUIContext().px2vp(data.area.topRect.height)
     }
   })
   ```
4. 查阅代码中是否设置padding进行顶部避让。

   ```ts
   build() {
     Stack({ alignContent: Alignment.TopStart }) {
       // 顶部避让区域
       Row() {
       }
       .padding({top:this.topSafeHeight})
       .width("100%")    
     }
     .height('100%')
   }
   ```
5. 查阅代码中是否通过isLayoutFullScreen()等全屏模式判断来硬编码设置顶部margin或padding值，若存在类似.margin({ top: isLayoutFullScreen() ? 40 : 0 })的写法，该判断方式在悬浮窗模式下无法正确获取顶部避让高度。

## 分析结论

应用代码中调用了setWindowLayoutFullScreen接口，打开了窗口沉浸式，故应用不会自动避让状态栏或者三点功能栏，而应用中未调用avoidAreaChange接口监听系统默认区域高度变化，动态配置顶部避让区域，导致悬浮窗场景下，页面内容未避让顶部窗口控制条。若代码中通过isLayoutFullScreen()判断来设置顶部margin值，由于悬浮窗模式下isLayoutFullScreen返回false，悬浮窗放大后isInFreeWindowMode也为false，无法通过全屏模式或悬浮窗模式判断来准确获取顶部避让高度。

## 修改建议

应用开启沉浸式布局后，可以通过getWindowAvoidArea接口可获取屏幕顶部需要避让的矩阵区域topRect，获取到该值后应用可对应使用padding进行布局避让，并且注册on('avoidAreaChange')监听系统避让区域变化以进行布局的动态调整。不应通过isLayoutFullScreen()等全屏模式判断来设置顶部margin值，应统一使用安全区域高度进行避让。

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct topSafePage {
  @State topSafeHeight: number = 0;

  getWindow(): window.Window {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowStage = context.windowStage;
    let windowClass = windowStage.getMainWindowSync();
    return windowClass;
  }

  aboutToAppear(): void {
    let windowClass: window.Window = this.getWindow();
    this.topSafeHeight =
      this.getUIContext().px2vp(windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
    windowClass.setWindowLayoutFullScreen(true);
    windowClass.on('avoidAreaChange', (data) => {
      if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
        this.topSafeHeight = this.getUIContext().px2vp(data.area.topRect.height);
      }
    });
  }

  build() {
    Column() {
      Row() {
        // 内容区域
        Text('进行顶部三点区域避让');
      }
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
    // 使用padding进行避让
    .padding({ top: this.topSafeHeight });
  }
}
```

若需要在多个页面或组件间共享安全区域高度，可在EntryAbility中通过[AppStorage.setOrCreate](../harmonyos-references/ts-state-management.md#setorcreate9)存储安全区域高度，页面中通过[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)装饰器获取。

```ts
// 在EntryAbility中添加安全区域高度监听
let avoidArea = mainWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
let topHeight = px2vp(avoidArea.topRect.height);
AppStorage.setOrCreate('topSafeAreaHeight', topHeight);

mainWindow.on('avoidAreaChange', (data: window.AvoidAreaOptions) => {
  if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
    let newTopHeight = px2vp(data.area.topRect.height);
    AppStorage.setOrCreate('topSafeAreaHeight', newTopHeight);
  }
});
```

页面组件中通过@StorageProp获取安全区域高度，用于顶部margin避让。

```ts
@StorageProp('topSafeAreaHeight') topSafeAreaHeight: number = 0;

// Header区域使用安全区域高度作为顶部margin
.margin({ top: this.topSafeAreaHeight })
```
