---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1196
title: 设置应用子窗口
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 设置应用子窗口
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:1ab66cc98d748c7c334ae1f290b1f0be8397e1de31c17dc6336370ea35e53485
---

## 问题现象

如何在应用内实现子窗口效果，包括销毁子窗口、嵌套创建子窗口、创建最大化子窗口、移动子窗口位置、改变子窗口大小、更改子窗口背景色和拖动子窗口？

## 背景知识

* [moveWindowTo](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)：移动窗口位置，使用Promise异步回调。
* [startMoving](../harmonyos-references/arkts-apis-window-window.md#startmoving14)：自由窗口状态下，对系统窗口、应用主窗口、应用子窗口、全局悬浮窗和模态窗口生效。非自由窗口状态下，仅对系统窗口、应用子窗口、全局悬浮窗和模态窗口生效。
* [resize](../harmonyos-references/arkts-apis-window-window.md#resize9-1)：基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。
* [setWindowBackgroundColor](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)：设置窗口的背景色。未调用该接口时，窗口在浅色模式默认背景色为'#FFF0F0F0'，在深色模式默认背景色为'#FF1A1A1A'。
* [createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9-1)：创建该WindowStage实例下的子窗口，使用Promise异步回调。
* [createSubWindowWithOptions](../harmonyos-references/arkts-apis-window-window.md#createsubwindowwithoptions12)：创建主窗口、子窗口或悬浮窗下的子窗口，使用Promise异步回调。
* [destroyWindow](../harmonyos-references/arkts-apis-window-window.md#destroywindow9-1)：销毁当前窗口，使用Promise异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。
* [子窗口开发指导](../harmonyos-guides/subwindow-guide.md)：开发者可以按需创建应用子窗口，如弹窗等，并对其进行属性设置等操作。

## 解决方案

针对不同子窗口场景可以采用以下方式处理：

| 场景 | 方案 |
| --- | --- |
| 如何在子窗口中再创建一个子窗口。 | 可以使用createSubWindowWithOptions为当前子窗口再创建一个子窗口。 |
| 子窗口调用maximize()方法报错：Unauthorized operation.。 | 子窗口需在创建时设置子窗口参数maximizeSupported为true，再调用此接口即可实现最大化功能。 |
| 如何快捷移动子窗口的位置。 | 可以使用moveWindowTo，将子窗口移动至目标位置。 |
| 如何改变子窗口的大小。 | 可以使用resize，基于窗口左上角顶点将子窗口改至目标大小。 |
| 如何设置子窗口的背景色。 | 可以使用setWindowBackgroundColor为子窗口设置十六进制RGB或ARGB颜色。 |
| 如何使子窗口可拖动。 | 可以对组件绑定onTouch事件，并在回调中使用startMoving给子窗口添加移动效果。 |

完整代码参考如下：

1. Index.ets：通过调用createSubWindow创建第一个子窗口，并对其设置基础的位置、大小及相关属性。使用setUIContent为子窗口设置加载的目标页面，同时需要在main\_pages.json文件中添加待加载的页面。当窗口使用结束，调用destroyWindow删除子窗口。

   ```ts
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   let windowStage_: window.WindowStage | undefined = undefined;
   let sub_windowClass: window.Window | undefined = undefined;

   @Entry
   @Component
   struct Index {
     message: string = 'Hello World';
     private CreateSubWindow() {
       windowStage_ = AppStorage.get('windowStage');
       // 1.创建应用子窗口。
       if (windowStage_ == null) {
         console.error('Failed to create the subwindow. Cause: windowStage_ is null');
       } else {
         windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
           let errCode: number = err.code;
           if (errCode) {
             console.error('Failed to create the subwindow. Cause: ' + JSON.stringify(err));
             return;
           }
           sub_windowClass = data;
           // 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
           sub_windowClass.moveWindowTo(150, 300, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to move the window. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in moving the window.');
           });
           sub_windowClass.resize(1000, 1800, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in changing the window size.');
           });
           // 3.为子窗口加载对应的目标页面。
           sub_windowClass.setUIContent('pages/subWindow', (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to load the content. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in loading the content.');
             (sub_windowClass as window.Window).setWindowBackgroundColor('#808080');
             // 3.显示子窗口。
             (sub_windowClass as window.Window).showWindow((err: BusinessError) => {
               let errCode: number = err.code;
               if (errCode) {
                 console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
                 return;
               }
               console.info('Succeeded in showing the window.');
             });
           });
         });
       }
     }

     private destroySubWindow() {
       // 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
       (sub_windowClass as window.Window).destroyWindow((err: BusinessError) => {
         let errCode: number = err.code;
         if (errCode) {
           console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
           return;
         }
         console.info('Succeeded in destroying the window.');
       });
     }

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
           Button() {
             Text('CreateSubWindow')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(220).height(68)
           .margin({ left: 10, top: 60 })
           .onClick(() => {
             this.CreateSubWindow();
           })

           Button() {
             Text('destroySubWindow')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(220).height(68)
           .margin({ left: 10, top: 220 })
           .onClick(() => {
             this.destroySubWindow();
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
2. subWindow：调用createSubWindowWithOptions嵌套创建子窗口，对子窗口属性添加maximizeSupported属性使其可以通过maximize方法实现最大化。通过调用moveWindowTo、resize、setWindowBackgroundColor方法实现子窗口移动位置、修改大小、更改背景色的效果。给组件绑定onTouch事件，并在回调中使用startMoving方法实现子窗口添加可拖动效果。

   ```ts
   import { window } from '@kit.ArkUI';

   let windowStage_ = AppStorage.get('windowStage') as window.WindowStage;
   let sub_windowClass: window.Window | undefined = undefined;

   @Entry
   @Component
   struct SubWindow {
     message: string = 'Hello subWindow';
     move: boolean = true;
     resize: boolean = true;
     color: boolean = true;

     private async CreateSubWindow() {
       if (windowStage_ == null) {
         console.error('Failed to create the subwindow. Cause: windowStage_ is null');
       } else {
         let options: window.SubWindowOptions = {
           title: 'title',
           decorEnabled: false,
           isModal: true,
           maximizeSupported: true
         };
         await windowStage_.createSubWindowWithOptions('mySubWindow2', options).then((data) => {
           data.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
           data.setUIContent('pages/subSubWindow');
           data.showWindow();
         });
       }
     }
     // 移动子窗口
     private moveSubWindow() {
       sub_windowClass = window.findWindow('mySubWindow');
       if (this.move) {
         sub_windowClass.moveWindowTo(150, 600);
         this.move = false;
       } else {
         sub_windowClass.moveWindowTo(150, 300);
         this.move = true;
       }
     }
     // 改变子窗口大小
     private resizeSubWindow() {
       sub_windowClass = window.findWindow('mySubWindow');
       if (this.resize) {
         sub_windowClass.resize(1000, 2200);
         this.resize = false;
       } else {
         sub_windowClass.resize(1000, 1800);
         this.resize = true;
       }
     }
     // 设置子窗口背景颜色
     private setSubWindowColor() {
       sub_windowClass = window.findWindow('mySubWindow');
       if (this.color) {
         sub_windowClass.setWindowBackgroundColor('#0000ff');
         this.color = false;
       } else {
         sub_windowClass.setWindowBackgroundColor('#808080');
         this.color = true;
       }
     }
     // 子窗口可拖动
     private dragSubWindow() {
       sub_windowClass = window.findWindow('mySubWindow');
       sub_windowClass.startMoving();
     }

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
           Button() {
             Text('maxSubSubWindow')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(250).height(68)
           .margin({ left: 10, top: 10 })
           .onClick(() => {
             this.CreateSubWindow();
           })

           Button() {
             Text('moveSubWindow')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(250).height(68)
           .margin({ left: 10, top: 10 })
           .onClick(() => {
             this.moveSubWindow();
           })

           Button() {
             Text('resizeSubWindow')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(250).height(68)
           .margin({ left: 10, top: 10 })
           .onClick(() => {
             this.resizeSubWindow();
           })

           Button() {
             Text('setSubWindowColor')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(250).height(68)
           .margin({ left: 10, top: 10 })
           .onClick(() => {
             this.setSubWindowColor();
           })

           Button() {
             Text('dragSubWindow')
               .fontSize(24)
               .fontWeight(FontWeight.Normal)
           }.width(250).height(68)
           .margin({ left: 10, top: 10 })
           .onTouch(() => {
             this.dragSubWindow();
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
3. subSubWindow：实现嵌套子窗口的样式。通过findWindow方法获取当前子窗口，并调用destroyWindow实现销毁当前子窗口。

   ```ts
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   let sub_windowClass: window.Window | undefined = window.findWindow('mySubWindow2');

   @Entry
   @Component
   struct SubSubWindow {
     message: string = 'subSubWindow';
     private destroySubWindow() {
       (sub_windowClass as window.Window).destroyWindow((err: BusinessError) => {
         let errCode: number = err.code;
         if (errCode) {
           console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
           return;
         }
         console.info('Succeeded in destroying the window.');
       });
     }

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
           Button() {
             Text('destroySubSubWindow')
               .fontSize(20)
               .fontWeight(FontWeight.Normal)
           }.width(220).height(68)
           .margin({ left: 10, top: 60 })
           .onClick(() => {
             this.destroySubWindow();
           })
         }
         .width('100%')
       }
       .height('100%')
       .backgroundColor('#808080')
     }
   }
   ```

运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/tcUJulIFQ12WycNpx1jFag/zh-cn_image_0000002689333382.png "点击放大")

## 常见FAQ

Q：子窗口是否可以设置最大化和最小化按钮？

A：当前的UX规范子窗口没有配置最小化/最大化按钮。如需配置此类按钮，请选择非子窗类型。如果需要对多窗口配置最大化/最小化按钮，可以通过[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)创建多主窗口。

Q：使用getLastWindow()方法获取最上层主窗口，但是当APP有子窗口时，会加载到子窗口中。

A：[getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)在应用子窗口或子窗口未调用showWindow()进行显示时返回应用主窗口。该接口本身不限制窗口类，既可以用来获取子窗也可以用来获取主窗。

Q：主窗口在扩展屏时，通过[createSubWindowWithOptions](../harmonyos-references/arkts-apis-window-window.md#createsubwindowwithoptions12)创建子窗口并调用[moveWindowToGlobal](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal13)移动子窗口后，子窗口出现变大现象是什么原因？

A：createSubWindowWithOptions创建子窗口时，子窗口默认跟随主窗口所在屏幕。如果主窗口在扩展屏，创建的子窗口也在扩展屏。调用moveWindowToGlobal接口时传入的坐标如果对应主屏位置，子窗口会被移动到主屏，由于主屏和扩展屏分辨率不同，子窗口会重新计算大小，导致视觉上出现变大现象。请确保moveWindowToGlobal传入的坐标参数与期望子窗口所在的屏幕一致。
