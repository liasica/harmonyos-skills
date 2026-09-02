---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1120
title: 页面和导航条区域的色调不一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 页面和导航条区域的色调不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:6d8ce9cca4d4ac1fb5191be041f9784311d2a6fb549af56514ccafbb975624a4
---

## 问题现象

应用未适配沉浸式显示，底部导航栏突兀。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/QJQ0xlLuQgmXjCZ1L0NVrQ/zh-cn_image_0000002675464354.png)

## 背景知识

* [窗口全屏布局方案](../harmonyos-guides/arkts-develop-apply-immersive-effects.md#窗口全屏布局方案)：通过[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)调整布局系统为全屏布局，界面元素延伸到状态栏和导航区域实现沉浸式效果。当不隐藏避让区时，通过接口查询状态栏和导航区域进行可交互元素避让处理，并设置状态栏或导航栏的颜色等属性与界面元素匹配；当隐藏避让区时，通过对应接口设置全屏布局。
* [setSpecificSystemBarEnabled](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)：设置主窗口状态栏、底部导航区域的显示或隐藏，使用Promise异步回调。
* [setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)：在全屏主窗口下用于设置窗口内导航栏和状态栏的属性。
* [SystemBarProperties](../harmonyos-references/arkts-apis-window-i.md#systembarproperties)：包括背景颜色、文字颜色、图标是否高亮和图标动画等属性，适配可以参考[如何实现状态栏背景颜色沉浸](faqs-arkui-358.md)。
* [expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)：允许开发者设置组件绘制内容突破[安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)的限制。

## 问题定位

1. 全局搜索关键字setWindowLayoutFullScreen或expandSafeArea，查看应用页面是否设置为全屏模式。该页面使用setWindowLayoutFullScreen设置为全屏模式。

   ```ts
   aboutToAppear(): void {
     window.getLastWindow(this.getUIContext().getHostContext())
       .then(win => {
         win.setWindowLayoutFullScreen(true); // 设置全屏
       })
   }
   ```
2. 全局搜索关键字setSpecificSystemBarEnabled，查看页面是否通过接口设置状态栏/导航栏的具体显示/隐藏状态。页面未使用setSpecificSystemBarEnabled方法对系统导航栏进行设置。
3. 全局搜索关键字setWindowSystemBarProperties，查看页面是否设置状态栏导航栏样式。页面设置为导航栏背景色为白色。页面未使用setWindowSystemBarProperties对导航栏颜色等属性进行设置。

## 分析结论

当应用调用setWindowLayoutFullScreen接口设置窗口全屏布局时，未使用setSpecificSystemBarEnabled方法对系统导航栏进行隐藏，也未使用setWindowSystemBarProperties将导航栏颜色等属性与界面元素进行匹配。

## 修改建议

参考[沉浸式页面实现](../best-practices/bpta-multi-device-window-immersive.md)实现页面沉浸式适配。

若需单独控制状态栏或导航栏的显示与隐藏，可在EntryAbility的onWindowStageCreate生命周期回调中调用[setSpecificSystemBarEnabled](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口进行设置：

```ts
import { window } from '@kit.ArkUI';

onWindowStageCreate(windowStage: window.WindowStage): void {
  let windowClass: window.Window = windowStage.getMainWindowSync();
  if (!windowClass) {
    console.info('windowClass is null');
    return;
  }
  try {
    windowClass.setSpecificSystemBarEnabled('status', false); // 隐藏状态栏
    windowClass.setSpecificSystemBarEnabled('navigationIndicator', false); // 隐藏导航条
  } catch (exception) {
    console.error(`Failed to set specific system bar enabled. Cause: ${JSON.stringify(exception)}`);
  }
  windowStage.loadContent('pages/Index', (err) => {
    // ...
  });
}
```
