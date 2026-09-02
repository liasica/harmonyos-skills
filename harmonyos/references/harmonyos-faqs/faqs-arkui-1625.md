---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1625
title: 地图放大后，亮度显示不足，影响用户体验
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 地图放大后，亮度显示不足，影响用户体验
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:181dafc67ead39a0c86bbc3f7020959ec731096b42a1d8b64e36cef2191eb0a9
---

## 问题现象

地图放大后，页面显示亮度较低，内容看不清，影响体验，如何在应用内设置屏幕亮度。

## 背景知识

* [setWindowBrightness](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)：允许应用主窗口设置屏幕亮度值，使用callback异步回调。
* [getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)：获取当前窗口的属性，返回WindowProperties。

## 问题定位

排查应用是否通过window实例提供的setWindowBrightness方法设置屏幕亮度，没有设置的话亮度跟随系统，此时亮度值为-1。

## 分析结论

应用没有使用setWindowBrightness方法锁定屏幕亮度，导致地图放大后，显示亮度较低，影响体验。

## 修改建议

使用setWindowBrightness方法锁定屏幕亮度。

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct FixedBrightnessDemo {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });

      Button('设置屏幕亮度')
        .id('SetBrightnessBtn') // 关键点1：必须设置 ID
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          left: { anchor: '__container__', align: HorizontalAlign.Start }
        })
        .margin({ top: 50, left: 20 })
        .onClick(async () => {
          // 关键点2：在点击事件中获取上下文，此时 Context 绝对可用且稳定
          try {
            const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            // 获取当前窗口
            const win = await window.getLastWindow(context);
            // 设置亮度 (1.0 最亮, 0.0 最暗, -1.0 跟随系统)
            await win.setWindowBrightness(1.0);
          } catch (err) {
            const error = err as BusinessError;
            console.error(`设置失败: Code=${error.code}, Message=${error.message}`);
          }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/sotUCfvgRv-Kf3ZJdL1yrw/zh-cn_image_0000002658856845.png "点击放大")
