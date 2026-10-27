---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1368
title: 如何判断APP内容是否被截屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何判断APP内容是否被截屏
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:28+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:99ad5558a757eb265ca3b35795331f5bb6227e5ef71557c466d2884b4bb8ebdf
---

## 问题现象

window模块提供的对截屏事件的监听，不仅在应用内截屏会触发，当系统下拉菜单（通知栏、控制栏）时截屏，也会触发截屏事件，如何区分截屏在应用内还是其他场景？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/1POvJ1xWTtyVrZhilsNKQQ/zh-cn_image_0000002658841303.gif "点击放大")

## 背景知识

[window模块](../harmonyos-references/arkts-apis-window.md)提供对窗口管理的基本能力，可通过[on('screenshot')](../harmonyos-references/arkts-apis-window-window.md#onscreenshot9)接口开启截屏事件的监听。[isFocused](../harmonyos-references/arkts-apis-window-window.md#isfocused12)是判断当前窗口是否获焦的接口，可以用来判断当前窗口是否位于上层。

## 解决方案

使用on('screenshot')监控当前窗口是否发生截屏事件，并在回调中添加isFocused，用于判断当前窗口是否获焦，若获焦，表明应用窗口位于最上层被截图。

```screen
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Screenshot {
  @State remind: string = '未截图';

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data: window.Window) => {
      if (err) {
        console.error(`GetLastWindow failed, error code: ${err.code}, error message: ${err.message}`);
      }
      data.on('screenshot', () => {
        if (data.isFocused()) {
          this.remind = '应用内截图';
        } else {
          this.remind = '非应用内截图';
        }
      });
    });
  }

  build() {
    Column() {
      Text(this.remind)
        .fontSize(50);
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
