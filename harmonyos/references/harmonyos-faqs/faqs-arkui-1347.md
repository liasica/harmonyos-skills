---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1347
title: 折叠屏，页面底部页签与导航栏间空白过大
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 折叠屏，页面底部页签与导航栏间空白过大
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ea02108cac0137ad96bf70c30977b47c6748153abc210ab3adbb58d0b3eab18a
---

## 问题现象

使用折叠屏打开应用，页面底部页签与导航栏之间空白过大。

## 背景知识

* [padding](../harmonyos-references/ts-universal-attributes-size.md#padding)：设置组件的内边距属性，给组件设置四周的边距，可控制离周围组件的距离。
* [getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)：可获取系统导航栏的高度。
* [on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)：开启当前应用窗口系统规避区变化的监听。

## 问题定位

查阅页面代码中，根组件是否设置padding属性，以及该属性内bottom字段的值。

## 分析结论

页面代码中，根组件padding属性的bottom字段设置的下边距过大，导致页面底部页签距离导航栏过远。

## 修改建议

通过on('avoidAreaChange')接口监听系统规避区域的变化，使用getWindowAvoidArea接口实时获取系统规避区域的高度，将实时的导航栏高度赋值给根组件的padding属性，避免padding数值过大产生空白的问题。代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct BottomRectDemo {
  @State bottomRect: number = 0;

  aboutToAppear(): void {
    const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowStage: window.WindowStage = context.windowStage;
    let windowClass: window.Window = windowStage.getMainWindowSync();
    // 初始化获得导航栏区域高度
    this.bottomRect = windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height;
    // 监听系统规避区域的变化，动态获取状态栏区域和导航栏区域
    windowClass.on('avoidAreaChange', () => {
      this.bottomRect =
        windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height;
    });
  }

  build() {
    Column() {
      Text(`测试页面具体底部导航条的距离: ${this.bottomRect}`);
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#D1D1D6')
    // 将导航栏的高度赋值给根组件的padding属性
    .padding({
      bottom: this.getUIContext().px2vp(this.bottomRect)
    });
  }
}
```
