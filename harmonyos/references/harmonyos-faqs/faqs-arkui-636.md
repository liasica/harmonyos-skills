---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-636
title: 如何实现不关闭弹窗的情况下跳转页面，并且页面返回时弹窗仍不关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现不关闭弹窗的情况下跳转页面，并且页面返回时弹窗仍不关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:489cee59b83f6521445b2b1ee0e8252afabb7a982079e996fc596f4b3a5bb41f
---

## 问题现象

如何实现跳转新页面后，返回页面时，原页面弹窗仍保持拉起状态？

## 背景知识

* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：NavDestination是路由系统中用于定义页面路径和导航目标的抽象概念，它相当于一个“导航目的地”的描述对象。
* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：创建并弹出自定义弹窗。通过Promise异步回调返回供[closeCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closecustomdialog12)使用的对话框id。
* [Stack](../harmonyos-references/ts-container-stack.md)：是堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

* 方案一：使用NavDestination的Dialog模式实现。

  自定义一个NavDestination组件，通过设置mode为NavDestinationMode.DIALOG使整个NavDestination无组件占位，默认透明显示。核心代码示例如下：
  1. Index\_solution1.ets。

     ```ts
     @Entry
     @Component
     struct Index_solution1 {
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

       build() {
         Navigation(this.pathStack) {

           RelativeContainer() {
             Button('打开弹窗')
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
               .onClick(() => {
                 this.pathStack.pushPathByName('CustomDialog', '', false); // 推送弹窗页面
               });

           }
           .width('100%')
           .height('100%');
         }

         .mode(NavigationMode.Auto)
         .width('100%')
         .height('100%');
       }
     }
     ```
  2. CustomDialog.ets。

     ```ts
     @Builder
     export function CustomDialogBuilder() {
       CustomDialog();
     }

     @Component
     export struct CustomDialog {

       @Consume('pathStack') pathStack: NavPathStack;

       build() {
         NavDestination() {
           Stack({ alignContent: Alignment.Center }) {
             Text('123123') // 弹窗遮罩
               .onClick(() => {
                 // 点击遮罩退出该页面，达到关闭弹窗效果
                 this.pathStack.pop();
               })
               .width('100%')
               .height('100%')
               .opacity(0.1) // 遮罩透明度调节
               .backgroundColor(0x000000)
             Column() {
               Text('我是自定义弹窗')
                 .fontSize(20)
                 .height(100)
                 .margin({top:20})
               Row() {
                 Button('取消').onClick(() => {
                   this.pathStack.pop();
                 })
                 Blank().width(50)
                 Button('确定').onClick(() => {
                   this.pathStack.pushPathByName('DetailPage', '', false);
                 })
               }
               .margin({bottom:25})
             }
             .justifyContent(FlexAlign.Center)
             .backgroundColor(Color.White)
             .borderRadius(20)
             .width('95%')
           }.height('100%').width('100%')
         }

         .backgroundColor('rgba(0,0,0,0.5)')
         .hideTitleBar(true)
         .mode(NavDestinationMode.DIALOG)
         .systemTransition(NavigationSystemTransitionType.NONE)
       }
     }
     ```
  3. DetailPage.ets。

     ```ts
     @Builder
     export function DetailPageBuilder() {
       DetailPage()
     }
     @Entry
     @Component
     export  struct DetailPage {
       @State message: string = 'Hello World';
        pageInfos: NavPathStack = new NavPathStack();
       build() {
         NavDestination(){
           RelativeContainer() {
             Text(this.message)
               .id('DetailPageHelloWorld')
               .fontSize($r('app.float.page_text_font_size'))
               .fontWeight(FontWeight.Bold)
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
               .onClick(() => {
                 this.message = 'Welcome';
               });
           }
           .height('100%')
           .width('100%');
         }.title('DetailPage')
       }
     }
     ```
  4. 在module.json5中配置"routerMap":"$profile:route\_map",并在资源目录下profile目录内创建route\_map.json文件。

     ```json
     {
       "routerMap": [
         {
           "name": "CustomDialog",
           "pageSourceFile": "src/main/ets/pages/CustomDialog.ets",
           "buildFunction": "CustomDialogBuilder",
           "data": {
             "description" : "this is PageOne"
           }
         },
         {
           "name": "DetailPage",
           "pageSourceFile": "src/main/ets/pages/DetailPage.ets",
           "buildFunction": "DetailPageBuilder",
           "data": {
             "description" : "this is DetailPage"
           }
         }
       ]
     }
     ```
* 方案二：使用getUIContext().getPromptAction().openCustomDialog自定义弹窗实现。设置弹窗属性levelMode为LevelMode.EMBEDDED表示开启页面级弹出框能力。代码示例如下：
  1. Index\_solution2.ets。

     ```ts
     import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

     let customDialogId: number = 0;

     @Builder
     function customDialogBuilder(uiContext: UIContext) {
       Column() {
         Text('我是自定义弹窗')
           .fontSize(20)
           .height(100);
         Row() {
           Button('取消').onClick(() => {
             uiContext.getPromptAction().closeCustomDialog(customDialogId);
           });
           Blank().width(50);
           Button('确定').onClick(() => {
             uiContext.getRouter().pushUrl({ url: 'pages/DetailPage2' });
           });
         };
       }
       .padding(20);
     }

     @Entry
     @Component
     struct Index_solution2 {
       private uiContext: UIContext = this.getUIContext();
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
       @Builder
       customDialogComponent() {
         customDialogBuilder(this.uiContext);
       }

       build() {

         Row() {
           Column() {
             Button('打开弹窗')
               .onClick(() => {
                 const node: FrameNode | null = this.getUIContext().getFrameNodeById('test_text') || null;
                 this.uiContext.getPromptAction().openCustomDialog({
                   builder: () => {
                     this.customDialogComponent();
                   },
                   levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
                   levelUniqueId: node?.getUniqueId(), // 设置页面级弹出框所在页面的任意节点ID
                   immersiveMode: ImmersiveMode.EXTEND, // 设置页面级弹出框蒙层的显示模式
                 }).then((dialogId: number) => {
                   customDialogId = dialogId;
                 });
               });
           }
           .width('100%');
         }
         .height('100%');
       }
     }
     ```
  2. DetailPage2.ets。

     ```ts
     @Entry
     @Component
     struct DetailPage2 {
       @State message: string = 'Hello World';

       build() {
         RelativeContainer() {
           Text(this.message)
             .id('DetailPageHelloWorld')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               this.message = 'Welcome';
             });
         }
         .height('100%')
         .width('100%');
       }
     }
     ```
* 方案三：通过Visibility控制实现仿Dialog弹窗功能。

  使用Stack布局实现了一个自定义Dialog弹窗效果，通过Visibility状态控制弹窗的显示与隐藏，使用Text组件模拟遮罩层，点击遮罩可关闭弹窗。代码示例如下：
  1. Index\_solution3.ets。

     ```ts
     @Entry
     @Component
     struct Index_solution3 {
       pathStack: NavPathStack = new NavPathStack();
       // 显隐控制设置为不占用
       @State visible: Visibility = Visibility.None;

       build() {
         Navigation(this.pathStack) {
           // 使用stack可以实现假的dialog覆盖原页面上面
           Stack() {
             Row() {
               // 初始页面
               Column() {
                 Button('打开弹窗')
                   .onClick(() => {
                     // 用于检测点击事件是否透传到原页面
                     if (this.visible === Visibility.Visible) {
                       this.visible = Visibility.None;
                     } else {
                       this.visible = Visibility.Visible;
                     }
                   });

               }
               .width('100%');
             }
             .height('100%')
             .backgroundColor(Color.White);

             // 制造弹窗效果，模拟半透明灰色的蒙层效果
             Text('')
               .onClick(() => {
                 if (this.visible === Visibility.Visible) {
                   this.visible = Visibility.None;
                 } else {
                   this.visible = Visibility.Visible;
                 }
               })
               .width('100%')
               .height('100%')
               .opacity(0.16)
               .backgroundColor(0x000000)
               .visibility(this.visible);
             Column() {
               // 这个可以调节对话框效果，栅格布局，xs，sm，md，lg分别为四种规格
               // 下面的breakpoints是用来区别当前属于哪个类型的断点
               // gridRow里的栅格数量为总数，gridCol里的就是偏移和假Dialog所占据的栅格数
               GridRow({
                 columns: {
                   xs: 1,
                   sm: 4,
                   md: 8,
                   lg: 12
                 },
                 breakpoints: {
                   value: ['400vp', '600vp', '800vp'],
                   reference: BreakpointsReference.WindowSize
                 },
               }) {
                 GridCol({
                   span: {
                     xs: 1,
                     sm: 2,
                     md: 4,
                     lg: 8
                   },
                   offset: {
                     xs: 0,
                     sm: 1,
                     md: 2,
                     lg: 2
                   }
                 }) {
                   Column() {
                     Text('我是自定义弹窗')
                       .fontSize(20)
                       .height(100)
                       .margin({ top: 20 });
                     Row() {
                       Button('取消').onClick(() => {
                         if (this.visible === Visibility.Visible) {
                           this.visible = Visibility.None;
                         } else {
                           this.visible = Visibility.Visible;
                         }
                       });
                       Blank().width(50);
                       Button('确定').onClick(() => {
                         this.getUIContext().getRouter().pushUrl({ url: 'pages/DetailPage2' });
                       });
                     }
                     .margin({ bottom: 25 });
                   }
                   .width('95%')
                   .backgroundColor(0xffffff)
                   .visibility(this.visible)
                   .clip(true)
                   .borderRadius(20);
                 };
               };
             }
             .width('95%');
           };
         }
         .hideTitleBar(true);
       }
     }
     ```
  2. DetailPage2.ets。

     ```ts
     @Entry
     @Component
     struct DetailPage2 {
       @State message: string = 'Hello World';

       build() {
         RelativeContainer() {
           Text(this.message)
             .id('DetailPageHelloWorld')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               this.message = 'Welcome';
             });
         }
         .height('100%')
         .width('100%');
       }
     }
     ```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/I-5npAiBSoudIhZvXIY04w/zh-cn_image_0000002635192052.png "点击放大")
