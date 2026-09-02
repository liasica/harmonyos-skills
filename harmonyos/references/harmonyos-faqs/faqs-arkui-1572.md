---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1572
title: 使用子窗口实现自定义宽度和圆角的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 使用子窗口实现自定义宽度和圆角的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:fd378f6a4a248ab98a7b65b3940ffe95374b70934eab3d4fe97bcc7e4afc08a9
---

## 问题现象

当需要灵活定义弹窗尺寸、圆角以及封装成工具快速调用时，可以使用子窗口的方式来实现弹窗。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/SyJ7oJRGT7yRMcGnB1pj9A/zh-cn_image_0000002628769764.png "点击放大")

## 背景知识

[createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9)：可以创建当前windowStage实例下的子窗口，并且子窗口创建后默认是[沉浸式布局](../harmonyos-guides/window-terminology.md#immersive-layout沉浸式布局)，可以改变其大小、位置等，还可以根据应用需要设置窗口背景色、亮度等属性。

## 解决方案

使用子窗口实现弹窗在应用开发中具有以下显著优势，可提升交互灵活性和用户体验：

1. 精准的层级控制。

   弹窗层级直接关联所属窗口，通过子窗口可避免主窗口内容遮挡弹窗。场景示例：支付弹窗需强制展示时，将焦点切换到子窗口打开弹窗，确保不被其他窗口覆盖。
2. 灵活的焦点管理。弹窗出现位置由当前焦点窗口决定：
   * 重要弹窗：焦点切换到子窗口，确保弹窗显示在顶层（如支付确认）。
   * 次要弹窗：焦点留在主窗口，避免打断用户子窗口操作（如后台节目提示）。
3. 沉浸式体验优化。

   子窗口独立于主窗口生命周期，主窗口可保持沉浸式设计（如隐藏状态栏/导航栏），子窗口专注弹窗交互。
4. 交互扩展性强。

   支持复杂交互特性：
   * 侧滑拦截：防止用户误触关闭关键弹窗。
   * 点击外部不关闭：强制用户处理重要操作（如协议确认）。
   * 页面切换不消失：弹窗跨页面持续显示（如全局进度条）。
5. 动画与样式定制。

   子窗口弹窗支持自定义进出场动画（如渐入、缩放），提升视觉连贯性。

* 场景示例。
  + 安全校验：验证码输入子窗口（如登录流程），与主窗口解耦。
  + 全局提示：低优先级通知在主窗口弹出，不干扰子窗口操作。
  + 流程引导：多步骤弹窗在子窗口保持连续显示，避免页面跳转中断。通过子窗口管理弹窗，可精细控制交互优先级和视觉层次，兼顾功能性与用户体验。

以下为实现步骤：

1. 在EntryAbility.ets中保存windowStage，供后续创建子窗口时随时取用。

   ```ts
   windowStage.loadContent('pages/Index', (err) => {
     AppStorage.setOrCreate('windowStage',windowStage);
     if (err.code) {
       return;
     }
     hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   });
   ```
2. 将创建窗口封装成函数实现快速调用创建窗口。

   ```ts
   // 步骤1：将创建窗口封装成函数实现快速调用创建窗口。
   export function createSubWindow(sub: SubWindowClass, positionX: number, positionY: number, width: number) {
     // 1.获取主窗口windowStage。2.创建子窗口。3.设置子窗口属性。4.加载子窗口内容。5.显示子窗口内容
     // 获取主窗口windowStage
     windowStage_ = AppStorage.get('windowStage');
     if (windowStage_ == null) {
     }
     // 创建子窗口
     windowStage_?.createSubWindow(sub.windowName, (err: BusinessError, data) => {
       let errCode = err.code;
       if (errCode) {
         return;
       }
       if (data) {
         sub.subWindowClass = data;
         // 设置子窗口属性：大小，位置等
         // 设置子窗口位置
         sub.subWindowClass.moveWindowTo(positionX, positionY, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 设置子窗口大小
         sub.subWindowClass.resize(width, sub.windowHeight, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 设置子窗口是否可触
         sub.subWindowClass.setWindowTouchable(true, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 加载子窗口页面
         sub.subWindowClass.setUIContent(sub.windowPath, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 显示子窗口内容
         sub.subWindowClass.showWindow((err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
       }
     });
   }
   ```
3. 将关闭子窗口封装成函数实现任意位置调用关闭任意窗口。

   ```ts
   // 步骤2：将关闭子窗口封装成函数实现任意位置调用关闭任意窗口。
   export function destroySubWindow(sub: SubWindowClass) {
     sub.subWindowClass?.destroyWindow((err: BusinessError) => {
       if (err.code) {
         return;
       }
     });
   }
   ```
4. 将窗口尺寸、位置通过参数传入创建函数，实现窗口属性可自定义。

   ```ts
   // 步骤3：将窗口尺寸、位置通过参数传入创建函数，实现窗口属性可自定义。
   class SubWindowClass {
     subWindowClass: window.Window | null = null;
     windowName: string = '';
     windowWidth: number = 0;
     windowHeight: number = 0;
     positionX: number = 0;
     positionY: number = 0;
     windowPath: string = '';

     constructor(subWindowClass: window.Window | null, windowName: string, windowWidth: number, windowHeight: number,
       positionX: number, positionY: number, windowPath: string) {
       this.subWindowClass = subWindowClass;
       this.windowName = windowName;
       this.windowWidth = windowWidth;
       this.windowHeight = windowHeight;
       this.positionX = positionX;
       this.positionY = positionY;
       this.windowPath = windowPath;
     }
   }
   ```
5. 被调用页面实现，可自定义圆角。

   ```ts
   build() {
     Column() {
       Text(this.message)
         .margin({ top: 10 })
         .fontColor(Color.White);
       Button() {
         Text('close sub window1')
           .padding(8)
           .borderRadius(8)
           .backgroundColor(Color.Gray)
           .fontColor(Color.White);

       }
       .margin({ top: 10 })
       .onClick(() => {
         destroySubWindow(sub1);
       });
     }
     .width('100%')
     .height('100%')
     // 步骤4：被调用页面实现，可自定义圆角。
     .borderRadius(10)
     .backgroundColor('#ff4b7fe9');
   }
   ```

完整示例参考如下：

1. Index.ets调用页。

   ```ts
   // 调用页 index.ets
   import { display, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { JSON } from '@kit.ArkTS';

   let windowStage_: window.WindowStage | null | undefined = null;

   // 步骤3：将窗口尺寸、位置通过参数传入创建函数，实现窗口属性可自定义。
   class SubWindowClass {
     subWindowClass: window.Window | null = null;
     windowName: string = '';
     windowWidth: number = 0;
     windowHeight: number = 0;
     positionX: number = 0;
     positionY: number = 0;
     windowPath: string = '';

     constructor(subWindowClass: window.Window | null, windowName: string, windowWidth: number, windowHeight: number,
       positionX: number, positionY: number, windowPath: string) {
       this.subWindowClass = subWindowClass;
       this.windowName = windowName;
       this.windowWidth = windowWidth;
       this.windowHeight = windowHeight;
       this.positionX = positionX;
       this.positionY = positionY;
       this.windowPath = windowPath;
     }
   }

   let subWindowClass1: window.Window | null = null;
   let subWindowClass2: window.Window | null = null;

   export const sub1 = new SubWindowClass(subWindowClass1, 'mysub1', 500, 400, 10, 1520, 'pages/SubWindow');

   export const sub2 = new SubWindowClass(subWindowClass2, 'mysub2', 500, 400, 690, 1520, 'pages/SubWindow2');

   // 步骤1：将创建窗口封装成函数实现快速调用创建窗口。
   export function createSubWindow(sub: SubWindowClass, positionX: number, positionY: number, width: number) {
     // 1.获取主窗口windowStage。2.创建子窗口。3.设置子窗口属性。4.加载子窗口内容。5.显示子窗口内容
     // 获取主窗口windowStage
     windowStage_ = AppStorage.get('windowStage');
     if (windowStage_ == null) {
     }
     // 创建子窗口
     windowStage_?.createSubWindow(sub.windowName, (err: BusinessError, data) => {
       let errCode = err.code;
       if (errCode) {
         return;
       }
       if (data) {
         sub.subWindowClass = data;
         // 设置子窗口属性：大小，位置等
         // 设置子窗口位置
         sub.subWindowClass.moveWindowTo(positionX, positionY, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 设置子窗口大小
         sub.subWindowClass.resize(width, sub.windowHeight, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 设置子窗口是否可触
         sub.subWindowClass.setWindowTouchable(true, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 加载子窗口页面
         sub.subWindowClass.setUIContent(sub.windowPath, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
         // 显示子窗口内容
         sub.subWindowClass.showWindow((err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
       }
     });
   }

   // 步骤2：将关闭子窗口封装成函数实现任意位置调用关闭任意窗口。
   export function destroySubWindow(sub: SubWindowClass) {
     sub.subWindowClass?.destroyWindow((err: BusinessError) => {
       if (err.code) {
         return;
       }
     });
   }

   @Entry
   @Component
   struct Index {
     @State positionY: number = 0;
     @State positionX: number = 0;
     @State screenWidth: number = 0;

     aboutToAppear(): void {
       this.screenWidth = display.getDefaultDisplaySync().width;
     }

     build() {
       Column() {
         Row() {
           Text('我是主页面')
             .fontColor(Color.White)
             .margin({ top: 20 });
         }
         .width('100%')
         .height(150)
         .backgroundColor('#ffb7afaf')
         .justifyContent(FlexAlign.Center)
         .alignItems(VerticalAlign.Top);

         Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceAround }) {
           Button('open sub window1')
             .width((this.screenWidth - 30) / 2)

             .margin({ left: 10 })
             .onClick(() => {
               createSubWindow(sub1, this.positionX, this.positionY,
                 (this.screenWidth - this.getUIContext().vp2px(30)) / 2);
             });

           Button('open sub window2')
             .width((this.screenWidth - 30) / 2)
             .margin({ left: 10, right: 10 })
             .onClick(() => {
               createSubWindow(sub2, (this.screenWidth / 2 + this.getUIContext().vp2px(5)), this.positionY,
                 (this.screenWidth - this.getUIContext().vp2px(30)) / 2);
             });
         }
         .margin({ top: 20 });

         Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceAround }) {
           Button('close sub window1')
             .width((this.screenWidth - 30) / 2)
             .margin({ left: 10 })
             .id('itemOne')
             .onAppear(() => {
               setTimeout(() => {
                 const infoOne = this.getUIContext().getComponentUtils().getRectangleById('itemOne');
                 this.positionY = infoOne.windowOffset.y + infoOne.size.height + 15;
                 this.positionX = infoOne.windowOffset.x;
                 console.info('ssssss=', JSON.stringify(infoOne));
               }, 100);

             })
             .onClick(() => {
               destroySubWindow(sub1);
             });

           Button('close sub window2')
             .width((this.screenWidth - 30) / 2)

             .margin({ left: 10, right: 10 })
             .onClick(() => {
               destroySubWindow(sub2);
             });
         }
         .margin({ top: 20 });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
2. 被调用页1。

   ```ts
   import { destroySubWindow, sub1 } from './Index';

   @Entry
   @Component
   struct SubWindow {
     private message: string = 'Hello World';

     build() {
       Column() {
         Text(this.message)
           .margin({ top: 10 })
           .fontColor(Color.White);
         Button() {
           Text('close sub window1')
             .padding(8)
             .borderRadius(8)
             .backgroundColor(Color.Gray)
             .fontColor(Color.White);

         }
         .margin({ top: 10 })
         .onClick(() => {
           destroySubWindow(sub1);
         });
       }
       .width('100%')
       .height('100%')
       // 步骤4：被调用页面实现，可自定义圆角。
       .borderRadius(10)
       .backgroundColor('#ff4b7fe9');
     }

   }
   ```
3. 被调用页2。

   ```screen
   import { destroySubWindow, sub2 } from './Index';

   @Entry
   @Component
   struct SubWindow2 {
     private message: string = 'Hello World';

     build() {
       Column() {
         Text(this.message)
           .margin({ top: 10 })
           .fontColor(Color.White);
         Button() {
           Text('close sub window2')
             .padding(8)
             .borderRadius(8)
             .backgroundColor(Color.Gray)
             .fontColor(Color.White);
         }
         .margin({ top: 10 })
         .onClick(() => {
           destroySubWindow(sub2);
         });
       }
       .width('100%')
       .height('100%')
       // 步骤4：被调用页面实现，可自定义圆角。
       .borderRadius(10)
       .backgroundColor('#ff4b7fe9');
     }
   }
   ```
