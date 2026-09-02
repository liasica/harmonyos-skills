---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-370
title: 如何实现沉浸式页面（包括沉浸式状态栏、沉浸式导航条）
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现沉浸式页面（包括沉浸式状态栏、沉浸式导航条）
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3353fc99c68895ffdbf37d4fafd7011bb491b091d299505a4a99a9e46c146cd7
---

**解决措施**

沉浸式页面开发分为以下两步：

1. 实现沉浸式效果。
   * 方案一：使用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法设置窗口为全屏模式。

     ```ts
     import { UIAbility } from '@kit.AbilityKit';
     import { window } from '@kit.ArkUI';
     import { BusinessError } from '@kit.BasicServicesKit';

     export default class EntryAbility extends UIAbility {
       onWindowStageCreate(windowStage: window.WindowStage) {
         // 1.Get the main window of the application.
         let windowClass: window.Window | undefined = undefined;
         windowStage.getMainWindow().then(windowClass => {
           console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(windowClass));
           // 2.Set the window to full screen to achieve immersive effects.
           windowClass.setWindowLayoutFullScreen(true).then(() => {
             console.info('Succeeded in setting the window layout to full-screen mode.');
           }).catch((e: BusinessError) => {
             console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(e));
           })
         }).catch((err: BusinessError) => {
           console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
         })
         // 3.Load the corresponding target page for the immersive window.
         windowStage.loadContent("pages/Index", (err) => {
           if (err.code) {
             console.error('Failed to load the content. Cause:' + JSON.stringify(err));
             return;
           }
           console.info('Succeeded in loading the content.');
         });
       }
     };
     ```
   * 方案二：设置组件的[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性，扩展组件的安全区域到状态栏和导航栏，从而实现沉浸式。

     ```ts
     @Entry
     @Component
     struct Example {
       build() {
         Column() {
           Row() {
             Text('Top Row')
               .fontSize(40)
               .textAlign(TextAlign.Center)
               .width('100%')
           }
           .backgroundColor('#F08080')
           // Set the top drawing to extend to the status bar
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

           Row() {
             Text('ROW2')
               .fontSize(40)
           }
           .backgroundColor(Color.Orange)
           .padding(20)

           Row() {
             Text('ROW3')
               .fontSize(40)
           }
           .backgroundColor(Color.Orange)
           .padding(20)

           Row() {
             Text('ROW4')
               .fontSize(40)
           }
           .backgroundColor(Color.Orange)
           .padding(20)

           Row() {
             Text('ROW5')
               .fontSize(40)
           }
           .backgroundColor(Color.Orange)
           .padding(20)

           Row() {
             Text('Bottom Row')
               .fontSize(40)
               .textAlign(TextAlign.Center)
               .width('100%')
           }
           .backgroundColor(Color.Orange)
           // Set the bottom drawing to extend to the navigation bar
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
         }
         .width('100%')
         .height('100%')
         .alignItems(HorizontalAlign.Center)
         .backgroundColor('#008000')
         .justifyContent(FlexAlign.SpaceBetween)
       }
     }
     ```
2. 处理避让区域与页面内容的适配问题。

   避让区包含状态栏中的电量、时间等系统信息，或手势交互如导航栏点击或上滑。实现应用页面沉浸式效果后，可能会与避让区产生UI元素遮挡、视觉违和或交互冲突等问题。开发者可针对不同场景选择以下方式对避让区和应用页面进行适配。

   * 使用[setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)方法或[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)方法设置状态栏和导航栏的显隐。
   * 使用[setWindowSystemBarProperties()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)方法设置状态栏和导航栏的样式。
   * 使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)方法获取避让区域的高度，据此设置应用页面内容的上下padding实现避让状态栏和导航栏。
   * 使用[getCutoutInfo()](../harmonyos-references/js-apis-display.md#getcutoutinfo9-1)方法获取挖孔区域宽高和位置信息，设置对应避让元素的margin实现挖孔区避让。
   * 对于需要动态调整的场景推荐使用getWindowAvoidArea()方法。

**参考链接**

[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)
