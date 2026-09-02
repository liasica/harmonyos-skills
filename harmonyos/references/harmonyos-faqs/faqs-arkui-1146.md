---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1146
title: window弹窗打开时onBackPress失效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > window弹窗打开时onBackPress失效
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4233f20dae4ff0c22a3000e4b89b2364894e948a0b734ee30945ce1a4613111b
---

## 问题现象

如下图所示，当Window弹窗不关闭的时候，跳转页面，通过侧滑手势返回无法触发页面的onBackPress进行页面返回：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/t-jKFHduSUm198wkAPigrA/zh-cn_image_0000002628409708.png "点击放大")

问题代码示例参考如下：

```screen
import { window } from '@kit.ArkUI';

export class NYWindowDialog {
  private static windowDialog: NYWindowDialog;
  private dialogWindow: window.Window | undefined = undefined;
  private name: string = 'XX_WINDOW_DIALOG'
  private dialogConfig?: window.Configuration;
  private params: object = new Object();
  private winBgColor: string = '#40000000'

  static getInstance(): NYWindowDialog {
    if (!NYWindowDialog.windowDialog) {
      NYWindowDialog.windowDialog = new NYWindowDialog()
    }
    return NYWindowDialog.windowDialog;
  }

  setParams(param: object): void {
    this.params = param
  }

  getParams(): object {
    return this.params
  }

  showWindowDialog(callback?: () => void): void {
    this.dialogConfig = { name: this.name, windowType: window.WindowType.TYPE_DIALOG }
    if (this.dialogWindow) {
      this.closeWindowDialog();
    }
    window.createWindow(this.dialogConfig, (string, newWindow: window.Window) => {
      if (!newWindow) {
        return
      }
      this.dialogWindow = newWindow;
      newWindow.setWindowTouchable(true);
      newWindow.setUIContent(this.params['page']).then(() => {
        newWindow.setWindowBackgroundColor(this.winBgColor);
      });
      newWindow.showWindow(() => {
        if (callback !== undefined) {
          callback();
        }
      });
    });
  }

  closeWindowDialog(callback?: () => void): void {
    if (this.dialogWindow != null) {
      this.dialogWindow.destroyWindow(() => {
        if (callback !== undefined) {
          callback();
        }
      });
    }
  }

  setWindowBgColor(color: string): void {
    this.winBgColor = color
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/EEgm4i9uQ_S6cc5a89ekNg/zh-cn_image_0000002658928929.png "点击放大")

## 背景知识

[@ohos.window（窗口）](../harmonyos-references/js-apis-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。可通过[window.createWindow](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9-1)中的[Configuration](../harmonyos-references/arkts-apis-window-i.md#configuration9)参数设置窗口属性。

## 问题定位

从GIF图中可以看到，窗口打开后除了不能侧滑返回以外，点击事件依旧能返回上一个页面，

1. 考虑打开弹窗后，是否重写侧滑返回手势功能，禁止了侧滑返回。[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)生命周期内，返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。该生命周期当用户点击返回按钮时触发，仅@Entry装饰的自定义组件生效。
2. 考虑模态弹窗问题。模态弹窗是一种强交互形式的弹窗，它会中断用户当前的操作流程，并要求用户必须做出响应才能继续其他操作。这种类型的弹窗通常用于需要向用户传达重要信息或确认的场景。@ohos.window（窗口）的窗口类型可参考官网[windowType](../harmonyos-references/arkts-apis-window-e.md#windowtype7)。

**说明** 

TYPE\_DIALOG模态窗口页面设计是以模态方式显示，即在显示期间阻止与其他窗口的交互，故不支持侧滑操作。

## 分析结论

问题代码采用的TYPE\_DIALOG模态窗口不支持侧滑返回操作，可以采用其它类型窗口。

## 修改建议

将模态弹窗更改为其它类型弹窗，通过创建子窗口的形式，实现弹窗效果，并实现侧滑返回效果：

1. 修改EntryAbility页面配置。

   ```screen
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
     windowStage.loadContent('pages/PageA', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       AppStorage.setOrCreate('windowStage', windowStage); // 储存窗口
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 主页创建并调用子窗口。

   ```screen
   // PageA.ets页面
   import window from '@ohos.window';
   import * as subWin from './subWindow'; // 导入命名路由页面(子窗口)
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct PageA {
     @State windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;

     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
         Text('这是 page A')
           .fontSize(20)
           .margin({ bottom: 10 });
         Button('点击打开子窗口')
           .onClick(() => {
             this.windowStage.createSubWindow('mySubWindow', (err, windowClass) => {
               try {
                 windowClass.loadContentByName(subWin.entryName, (err: BusinessError) => {
                   const errCode: number = err.code;
                   if (errCode) {
                     console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
                     return;
                   }
                   console.info('Succeeded in loading the content.');
                   // 设置子窗口左上角坐标
                   windowClass.moveWindowTo(0, 0);
                   // 展示子窗口
                   windowClass.showWindow();
                   // 设置子窗口全屏化布局避让安全区
                   windowClass.setWindowLayoutFullScreen(false);
                 });
               } catch (exception) {
                 console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
               }
             });
           });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
3. 自定义子窗口布局，并重写返回逻辑，侧滑销毁子窗口。

   ```screen
   // subWindow.ets页面
   import { window } from '@kit.ArkUI';

   export const entryName: string = 'subWindow';

   @Entry({ routeName: entryName })
   @Component
   export struct subWindow {
     @StorageProp('pageInfos') pageInfos: NavPathStack = new NavPathStack();

     onBackPress(): boolean | void {
       // window.findWindow('mySubWindow').destroyWindow(); // 销毁子窗口
     }

     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
         Text('这是子窗口')
           .fontSize(20)
           .margin({ bottom: 10 });
         Button('点击跳转 Page B')
           .onClick(() => {
             this.getUIContext().getRouter().pushUrl({
               url: 'pages/PageB'
             });
           })
           .margin({
             bottom: 15
           });
         Button('点击关闭子窗口')
           .onClick(() => {
             window.findWindow('mySubWindow').destroyWindow(); // 销毁子窗口
           });
       }
       .backgroundColor(Color.White)
       .width('100%')
       .height('100%');
     }
   }
   ```
4. 创建跳转测试页面。

   ```screen
   // PageB.ets页面
   @Entry
   @Component
   struct pageB {
     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
         Text('这是 Page B，请左滑')
           .fontSize(20)
           .margin({ bottom: 10 });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

**说明** 

以上页面需要新建为Page页面，若是新建的ArkTS File，需要将上述新建的页面，配置在entry/src/main/resources/base/profile中的main\_pages.json文件中

## 常见FAQ

Q：NavDestinationMode.DIALOG弹窗如何实现禁用系统返回关闭弹窗？

A：NavDestinationMode.DIALOG弹窗在onBackPressed生命周期内返回true即可。
