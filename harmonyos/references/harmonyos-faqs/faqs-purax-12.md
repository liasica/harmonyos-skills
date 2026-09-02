---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-12
title: 折叠屏状态监听
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 折叠屏状态监听
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6895cca387dc10b96169479256c2ff12eea94a8b89749b1dcc6d24c54d1a9600
---

## 问题现象

在使用HarmonyOS操作系统的设备时，应当采取何种方式来确定该设备是否具备可折叠特性？若设备确为可折叠类型，又该如何获取其当前的显示模式，并实现对折叠状态变化的实时监控？

## 背景知识

* 设备信息[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)接口可以返回设备的详细信息。
* 屏幕属性[@ohos.display](../harmonyos-references/js-apis-display.md)接口提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。

## 解决方案

* 判断当前设备是否可折叠：

  根据设备信息接口@ohos.deviceInfo中的[deviceType](../harmonyos-guides/module-configuration-file.md#devicetypes标签)属性，可以查询到设备的具体类型。若需判断设备是否为折叠屏，则可通过调用屏幕相关接口@ohos.display下的[display.isFoldable](../harmonyos-references/js-apis-display.md#displayisfoldable10)方法来获取当前设备是否具备可折叠特性的结果。CAPI可使用[OH\_NativeDisplayManager\_IsFoldable()](../harmonyos-references/capi-oh-display-manager-h.md#oh_nativedisplaymanager_isfoldable)判断。
* 获取可折叠设备的显示模式：

  屏幕属性@ohos.display接口的[getFoldDisplayMode](../harmonyos-references/js-apis-display.md#displaygetfolddisplaymode10)可以获取可折叠设备当前的显示模式。CAPI可使用[OH\_NativeDisplayManager\_GetFoldDisplayMode()](../harmonyos-references/capi-oh-display-manager-h.md#oh_nativedisplaymanager_getfolddisplaymode)获取。
* 获取可折叠设备的折叠状态：

  屏幕属性@ohos.display接口的[getFoldStatus](../harmonyos-references/js-apis-display.md#displaygetfoldstatus10)可以获取可折叠设备当前的折叠状态。
* 实时监听可折叠设备的折叠状态变化：
  + **方案一**：可以通过调用[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)方法来启动对可折叠设备折叠状态变化的监听，代码示例如下：

    ```ts
    // Start solution 1
    import { Callback } from '@kit.BasicServicesKit';
    import { display } from '@kit.ArkUI';

    @Entry
    @Component
    struct Index {
      @State foldStatus: number = 0;

      aboutToAppear(): void {
        let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
          this.foldStatus = data;
        };
        display.on('foldStatusChange', callback);
      }

      build() {
        Column() {
          Text('初始').visibility(this.foldStatus == 0 ? Visibility.Visible : Visibility.None);
          Text('展开').visibility(this.foldStatus == 1 || this.foldStatus == 12 ? Visibility.Visible : Visibility.None);
          Text('折叠').visibility(this.foldStatus == 2 ? Visibility.Visible : Visibility.None);
          Text('悬停')
            .visibility(this.foldStatus == 3 || this.foldStatus == 13 || this.foldStatus == 21 || this.foldStatus == 23 ?
              Visibility.Visible : Visibility.None);
          // 针对三折叠
          Text('三折叠全展开').visibility(this.foldStatus == 11 ? Visibility.Visible : Visibility.None);
        }
      }
    }
    // End solution 1
    ```
  + **方案二**：使用相机框架提供的[CameraManager.on('foldStatusChange')](../harmonyos-references/arkts-apis-camera-cameramanager.md#offfoldstatuschange12)监听设备折叠态变化，详细使用请参考：[获取设备折叠状态](../harmonyos-guides/camera-foldable-display.md#获取设备折叠状态)。

    **两种方案对比**：

    | 方案名称 | 优缺点 | 适用场景 |
    | --- | --- | --- |
    | 方案一：display.on | 直接调用display.on方法使用便捷 | 适用于常规或一般情况下的场景 |
    | 方案二：CameraManager.on | 需要创建相机管理器 | 适用于涉及相机接口应用的各种场景 |
* CAPI判断当前设备是否可折叠、获取可折叠设备的显示模式、实时监听可折叠设备的折叠状态：

  OH\_DisplayManager提供了C/C++层查询屏幕信息、监听屏幕状态变化以及折叠设备折叠状态变化等功能。它能够确定当前设备是否为可折叠设备，并支持对折叠状态（展开或折叠）变化进行监听。详细使用说明请参考：[OH\_DisplayManager](../harmonyos-guides/native-display-manager.md)。

## 常见FAQ

Q：在折叠屏幕设备处于展开状态时，界面出现了兼容性问题。具体而言，采用Navigation框架开发的页面在设备折叠状态下显示正常，但在设备展开状态下页面展示不全？

A：当未指定Navigation组件的模式属性时，默认情况下会采用Auto模式。在此模式下，系统会依据屏幕尺寸自动调整显示方式。对于API版本10及以上的设备，如果屏幕宽度达到或超过600vp，则会启用分栏显示的Split模式。若要使整个页面完全填充屏幕空间，可将模式属性设置为[NavigationMode.Stack](../harmonyos-references/ts-basic-components-navigation.md#navigationmode9枚举说明)。

Q：在折叠屏幕设备上，当屏幕从展开状态转换至收起状态或反之，在Webview中嵌入的H5页面能否捕捉到窗口尺寸变化？

A：折叠屏状态变化时，Webview内H5可以[监听到resize事件](../best-practices/bpta-web-adaptation.md#section1596042141816)：

Q：折叠屏展开状态下，如何判断屏幕的横竖屏状态？

A：通过[display.getDisplayByIdSync](../harmonyos-references/js-apis-display.md#displaygetdisplaybyidsync12)获取对应的Display对象，其rotation属性表示屏幕的旋转角度（0、90、180、270），可据此判断横竖屏状态。同时可通过[display.on('add'|'remove'|'change')](../harmonyos-references/js-apis-display.md#displayonaddremovechange)监听显示设备变化，在回调中实时获取最新的屏幕方向信息。另外，[display.getCurrentFoldCreaseRegion](../harmonyos-references/js-apis-display.md#displaygetcurrentfoldcreaseregion10)可获取折叠区域的折痕信息，辅助判断折叠屏的展开状态。
