---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1055
title: 如何实现全局可调用弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现全局可调用弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:921a79598bed72f173bfbd2bf939f3fa7025a7a8296402f10cfa85cd1fca65e0
---

## 问题现象

应用/元服务如何实现一个全局可调用的弹窗？

## 背景知识

* [windowStage](../harmonyos-references/arkts-apis-window-windowstage.md)为窗口管理器，管理各个基本窗口单元。
* [通过CustomDialogController类显示自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)，需要使用@CustomDialog定义弹窗内容。调用弹窗时，需要new CustomDialogController()，并将@CustomDialog作为[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的builder参数传入。
* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)用于创建并弹出dialogContent对应的自定义弹窗。

## 解决方案

实现一个全局可调用弹窗，可通过如下三种方式实现：

* 方案一：实现全局可调用弹窗推荐使用：[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)，示例请参考[完整示例](../harmonyos-guides/arkts-uicontext-custom-dialog.md#完整示例)。
* 方案二：可使用子窗口方式实现全局可调用弹窗，实现方式如下：
  1. 在EntryAbility.ets中通过[AppStorage](../harmonyos-guides/arkts-appstorage.md)获取窗口管理器用于后续获取Window实例实现子窗口的创建与销毁，代码如下：

     ```ts
     import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       onCreate(): void {
         try {
           this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         } catch (err) {
           hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
         }
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       }

       onDestroy(): void {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         AppStorage.setOrCreate('windowStage', windowStage);
         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
       }

       onForeground(): void {
         // Ability has brought to foreground
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
       }

       onBackground(): void {
         // Ability has back to background
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
       }
     };
     ```
  2. SubWindow.ets页面封装打开弹窗createMySubWindowFun方法，通过[createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9)实现弹窗的弹出，使用[setUIContent](../harmonyos-references/arkts-apis-window-window.md#setuicontent9)设置SubPage页面为子窗口加载的具体页面内容，通过[moveWindowTo](../harmonyos-references/arkts-apis-window-window.md#movewindowto9)、[resize](../harmonyos-references/arkts-apis-window-window.md#resize9)等方法设置子窗口样式。封装deleteMySubWindowFun方法通过[destroyWindow](../harmonyos-references/arkts-apis-window-window.md#destroywindow9)实现弹窗的关闭。代码如下：

     ```ts
     import { window } from '@kit.ArkUI';
     import { BusinessError } from '@kit.BasicServicesKit';

     // 获取windowStage
     let windowStage = AppStorage.get('windowStage') as window.WindowStage;
     let windowClass: window.Window | undefined = undefined;

     export class mySubWindow {
       createMySubWindowFun(subWindowName: string) {
         // 创建子窗口
         windowStage.createSubWindow(subWindowName, (err: BusinessError, data) => {
           windowClass = data;
           data.setUIContent('pages/SubPage', () => {
             // 设置子窗口左上角坐标
             data.moveWindowTo(150, 300);
             // 设置子窗口大小
             data.resize(1000, 1000);
             // 展示子窗口
             data.showWindow();
           });
         });
       }

       deleteMySubWindowFun() {
         if (windowClass) {
           windowClass.destroyWindow();
         }
       }
     }
     ```
  3. SubPage.ets页面用于展示子窗页面内容，代码如下：

     ```ts
     // 子窗口显示页面
     import { mySubWindow } from '../utils/SubWindow';

     @Entry
     @Component
     struct SubPage {
       mySubWindow: mySubWindow = new mySubWindow();

       build() {
         Column() {
           Text('子窗口页面')
             .fontSize(40)
             .margin({ top: 30 });
           Button('点击关闭')
             .onClick(() => {
               this.mySubWindow.deleteMySubWindowFun();
             })
             .margin({ top: 100 });
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
  4. Index.ets页面使用方式通过引入SubWindow页面，通过调用封装的createMySubWindowFun方法实现弹窗的打开，代码如下：

     ```ts
     import { mySubWindow } from '../utils/SubWindow';

     @Entry
     @Component
     struct Index {
       mySubWindow: mySubWindow = new mySubWindow();

       build() {
         RelativeContainer() {
           Text('点击打开弹窗')
             .id('HelloWorld')
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               this.mySubWindow.createMySubWindowFun('mySubWindow');
             });
         }
         .height('100%')
         .width('100%')
         .backgroundColor('#F1F3F5');
       }
     }
     ```

     运行效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Eyn4ZTOqRQGxvei95GcAXg/zh-cn_image_0000002628565460.png "点击放大")
* 方案三：通过自定义弹窗(CustomDialog)封装成自定义组件的方式：
  1. 封装弹窗控制方法Dialog.ets，使用[@watch](../harmonyos-guides/arkts-watch.md)监听外部传入的变量变化，通过CustomDialogController控制弹窗的显示隐藏，代码如下：

     ```ts
     import { CustomDialogView } from './CustomDialogView';

     @Component
     export struct Dialog {
       // 监听外部传入的visible变量，visible值发生变化时触发onChange回调函数
       @Watch('onChange') @Link visible: boolean;
       onCancel?: () => void;
       onConfirm?: () => void;
       // 通过CustomDialogController的builder参数绑定弹窗组件CustomDialogView
       private controller = new CustomDialogController({
         builder: CustomDialogView({
           visible: $visible,
           onCancel: this.onCancel,
           onConfirm: this.onConfirm,
         }),
         autoCancel: false,
         alignment: DialogAlignment.Center,
       });

       // 当visible的值变化时触发回调
       onChange(): void {
         if (this.visible) {
           this.controller.open();
         } else {
           this.controller.close();
         }
       }

       // 二次封装的Dialog组件主要通过控制器控制弹窗，不需要任何界面
       build() {
       }
     }
     ```
  2. 封装弹窗视图页面CustomDialogView.ets，作用于弹窗中作为展示页面，代码如下：

     ```ts
     @CustomDialog
     export struct CustomDialogView {
       @Link visible: boolean;
       controller: CustomDialogController;
       // 弹窗交互事件参数，点击确认和取消按钮时的回调函数
       onCancel?: () => void;
       onConfirm?: () => void;

       build() {
         Column() {
           Text('自定义弹窗')
             .margin({ top: 20, bottom: 40 });
           Button('点击关闭弹窗').onClick(() => {
             // 重置弹窗显隐参数
             this.visible = false;
             // 关闭弹窗
             this.controller.close();
           });
         }
         .width('100%')
         .height(200)
         .backgroundColor(Color.White);
       }
     }
     ```
  3. 使用弹窗页面CustomDialog.ets，通过给引入的Dialog组件传入visible控制弹窗的弹出，代码如下：

     ```ts
     import { Dialog } from './Dialog';

     @Entry
     @Component
     export struct CustomDialog {
       // 外部定义visible变量作为弹窗组件入参，控制弹窗显隐
       @State visible: boolean = false;

       build() {
         Column({ space: 20 }) {
           Button('点击打开弹窗')
           // 点击修改visible变量后，visible的值可以被Dialog组件监听并响应
             .onClick(() => this.visible = !this.visible)
             .margin({ top: 40 });
           // 通过双向绑定visible变量，实现外部控制弹窗
           Dialog({
             visible: $visible,
           });
         }
         .width('100%');
       }
     }
     ```

     运行效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/lLZCuzzrTcuHrtrWMtQNow/zh-cn_image_0000002658924769.png "点击放大")

## 总结

实现全局可调用弹窗可通过openCustomDialog、子窗口与自定义弹窗方式实现，openCustomDialog通过ComponentContent封装内容可以与UI界面解耦，调用更加灵活，可以满足开发者的封装诉求，优先推荐使用。子窗口方式需要使用页面当作弹窗内容且需要获取窗口管理器，代码复杂性较高。自定义弹窗方式与调用UI界面耦合性较高也不建议使用。
