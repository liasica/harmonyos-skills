---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1218
title: 设置状态栏与导航栏的颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 设置状态栏与导航栏的颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6ccd5d1253b19df0ed6f8a5e2138b8babef7ec5ce908cfc51a5e9e6eb52b6be8
---

## 问题现象

在应用开发过程中，需要通过调整状态栏、导航栏的颜色及文字颜色，以适应不同界面的设计需求。

## 背景知识

* [@ohos.window（窗口）](../harmonyos-references/arkts-apis-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
* [setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)：设置主窗口状态栏的属性，可以在入参[SystemBarProperties](../harmonyos-references/arkts-apis-window-i.md#systembarproperties)配置状态栏和三键导航栏的颜色。该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态的设备上调用不生效也不报错。其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

## 解决方案

若想设置状态栏、导航栏颜色，相关的属性有如下四个：statusBarColor、statusBarContentColor、navigationBarColor、navigationBarContentColor。下文将以设置**状态栏背景颜色与状态栏字体颜色**举例说明用法。

* 方案一：直接在UI组件中调用setWindowSystemBarProperties方法设置状态栏颜色和状态栏字体颜色。

  ```ts
  import window from '@ohos.window';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Solution1 {
    build() {
      RelativeContainer() {
        Text('Hello World')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            window.getLastWindow(this.getUIContext().getHostContext()!, (err: BusinessError, windowClass) => {
              if (err.code) {
                console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
                return;
              }
              let systemBarProperties: window.SystemBarProperties = {
                statusBarColor: '#F1F3F5', // 状态栏背景色
                statusBarContentColor: '#0A59F7' // 状态栏文字颜色
              };
              windowClass.setWindowSystemBarProperties(systemBarProperties).then(() => {
                console.info('Succeeded in setting the system bar properties.');
              }).catch((err: BusinessError) => {
                console.error(`Failed to set systemBar properties. Cause code: ${err.code}, message: ${err.message}`);
              });
            });
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

* 方案二：封装修改状态栏颜色的工具类StatusBarManager，在UI组件中调用工具类改变状态栏颜色。
  1. 通过传入Context，进而能够获取到Window实例来执行setWindowSystemBarProperties方法。
  2. 传入包含状态栏属性的JSON字符串，工具类解析字符串后使用。

     ```ts
     import { window } from '@kit.ArkUI';
     import { common } from '@kit.AbilityKit';
     import { BusinessError } from '@kit.BasicServicesKit';

     export class StatusBarManager {
       static handleStatusBarAction(context: common.BaseContext, p: string): void {
         try {
           interface ParamsType {
             action: string;
             args: Array<string>;
           }

           // 解析入参，用于设置状态栏的颜色
           const params: ParamsType = JSON.parse(p);
           const action: string = params.action;
           const args: Array<string> = params.args;
           let statusBarColor = '#FFFFFF'; // 默认白色
           let statusBarContentColor = '#000000'; // 默认黑色
           if (action === 'backgroundColorByHexString') {
             statusBarColor = args[0] || statusBarColor;
             statusBarContentColor = args[1] || statusBarContentColor;
           }
           // 创建SystemBarProperties对象
           const systemBarProperties: window.SystemBarProperties = {
             statusBarColor: statusBarColor,
             statusBarContentColor: statusBarContentColor,
           };
           StatusBarManager.setStatusBarBgColor(context, systemBarProperties);
         } catch (error) {
           console.error('Failed to parse or handle status bar action. Error:');
         }
       }

       private static setStatusBarBgColor(context: common.BaseContext,
         systemBarProperties: window.SystemBarProperties): void {
         window.getLastWindow(context).then((windowClass: window.Window) => {
           try {
             windowClass.setWindowSystemBarProperties(systemBarProperties);
             console.info('Status bar color updated successfully.');
           } catch (exception) {
             console.error(`Failed to set the system bar properties. Cause: ${JSON.stringify(exception)}`);
           }
         }).catch((error: BusinessError) => {
           console.error(`Failed to get last window. Error: ${JSON.stringify(error)}`);
         });
       }
     }
     ```

     在UI组件中调用：

     ```ts
     import { StatusBarManager } from './StatusBarManager';
     import { JSON } from '@kit.ArkTS';

     @Entry
     @Component
     struct Solution2 {
       build() {
         RelativeContainer() {
           Text('Hello World')
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               // 调用封装的StatusBarManager类设置状态栏颜色
               StatusBarManager.handleStatusBarAction(this.getUIContext().getHostContext()!,
                 JSON.stringify({ 'action': 'backgroundColorByHexString', 'args': ['#F1F3F5', '#0A59F7'] }));
             });
         }
         .height('100%')
         .width('100%');
       }
     }
     ```

  **说明** 

  设置状态栏与导航栏颜色的重要前提是获取Context，getLastWindow方法会在获取Context后确定操作的对象是哪一个窗口实例。在封装成工具类时，可以在类中获取Context，也可以将UI组件中获取的Context作为参数传给类中方法，为保证Context的一致性和准确性，更推荐在UI组件中获取Context并传给类中方法。
* 两种方案的实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/7OIKjheSRjKSJoLho5FTqA/zh-cn_image_0000002628753914.png "点击放大")

  若是想要设置导航栏，则需要在SystemBarProperties中给navigationBarColor、navigationBarContentColor赋值。

## 常见FAQ

Q：为什么设置了navigationBarColor，但是导航栏颜色没生效？

A：navigationBarColor是设置导航栏的背景颜色，也就是传统的三键导航，如果设备没有该底部导航栏，则设置不会生效。

Q：如何设置底部导航条区域背景色和导航条的颜色？

A：目前无相关API，即底部导航条颜色不可设置，底部导航条区域背景色设置可以通过扩展布局，全屏显示，不隐藏避让区实现，去掉顶部和底部的padding设置，即不避让状态栏和导航条，UI元素就会发生重叠。状态栏和导航区域默认是透明的，透传的是应用界面的背景色。参考文档：[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。

Q：如何只针对某一个页面设置状态栏颜色？

A：可以在该页面的aboutToAppear设置状态栏颜色，并在设置前使用getWindowSystemBarProperties获取状态栏颜色，在aboutToDisappear中设置为保存的状态栏颜色，以此达到针对一个页面修改颜色的效果。

Q：设置了沉浸式，如何修改导航栏颜色？

A：可以在最外层嵌套一层容器，使用padding空出底部位置，设置背景色即可。

Q：PC端应用如何设置顶部状态栏的背景色？

A：[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)该接口在2in1(PC)设备上调用不生效，暂不支持在PC端应用设置顶部状态栏的背景色。

Q：深色模式后状态栏看不到状态信息（时间、电量等）？

A：需要做页面[状态栏深色模式的适配](https://developer.huawei.com/consumer/cn/forum/topic/0208153170088597816?fid=0109140870620153026)。

Q：如何实现状态栏透明背景颜色？

A：在需要改变的页面直接调用setWindowSystemBarProperties方法，如果要设置状态栏整体透明度，可以使用RGBA对状态栏每部分设置相同透明度实现。
