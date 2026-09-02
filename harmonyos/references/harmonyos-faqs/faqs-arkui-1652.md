---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1652
title: 应用在启动和退出时，状态栏颜色突兀
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 应用在启动和退出时，状态栏颜色突兀
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc7062652a2c13a865cc446f5f529a1d5ddafc100104cc8ec8302bc259845ddb
---

## 问题现象

进入应用时状态栏颜色由白色突变为黑色，退出应用时状态栏颜色由黑色突变为透明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/hSQrVp8IRFG5eBt54mLDYw/zh-cn_image_0000002628661000.png "点击放大")

## 背景知识

* [setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)在全屏主窗口下用于设置窗口内导航栏和状态栏的属性。
* [SystemBarProperties](../harmonyos-references/arkts-apis-window-i.md#systembarproperties)包括背景颜色、文字颜色、图标是否高亮和图标动画等属性，适配可以参考[如何实现状态栏背景颜色沉浸](faqs-arkui-358.md)。
* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)可设置主窗口或子窗口的布局是否为沉浸式布局，使用Promise异步回调。系统窗口调用不生效。
* [expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)可以控制组件扩展其安全区域。

## 问题定位

查看状态栏设置，全局搜索setWindowSystemBarProperties，发现对SystemBarProperties中的statusBarColor进行了设置，且值没有设置为透明色。

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#000000', // 状态栏背景色黑色
        statusBarContentColor: '#ffffff' // 状态栏文字白色
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties); // 设置主窗口状态栏的属性
    });
  }

  build() {
    Column() {
      Text('Hello World')
        .width('100%')
        .height('100%')
        .fontColor(Color.White)
        .fontSize(20)
        .textAlign(TextAlign.Center);
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.Black)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
  }
}
```

## 分析结论

进入和退出应用时应用更改了状态栏背景色，导致颜色突变。

## 修改建议

1. 将statusBarColor值设置为透明。
2. 使用setWindowLayoutFullScreen设置页面全屏并使用expandSafeArea扩展页面到状态栏。
3. 完整示例如下：

   ```screen
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     aboutToAppear(): void {
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true);
         let systemBarProperties: window.SystemBarProperties = {
           statusBarColor: 'rgba(0, 0, 0, 0)', // 透明
           statusBarContentColor: '#ffffff' // 状态栏文字白色
         };
         lastWindow.setWindowSystemBarProperties(systemBarProperties); // 设置主窗口状态栏的属性
       });
     }

     build() {
       Column() {
         Text('Hello World')
           .width('100%')
           .height('100%')
           .fontColor(Color.White)
           .fontSize(20)
           .textAlign(TextAlign.Center);
       }
       .width('100%')
       .height('100%')
       .backgroundColor(Color.Black)
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP,SafeAreaEdge.BOTTOM]);
     }
   }
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/fQ7IPzXkT3K4wS3TEx2t3A/zh-cn_image_0000002659060261.png "点击放大")
