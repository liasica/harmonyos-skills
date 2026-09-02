---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-736
title: 通过自定义弹窗实现自定义样式的Toast
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 通过自定义弹窗实现自定义样式的Toast
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:59e142d8e0abda821f5f6f206bacdda18bf5ebd16b286a8a8009a3f1078b9450
---

## 问题现象

HarmonyOS的Toast接口，不支持设定圆角样式。如何实现类似其他平台的Toast样式？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/MnsOToPCRf6FOeRY_LoQFg/zh-cn_image_0000002628555228.gif "点击放大")

## 背景知识

* [不依赖UI组件的全局自定义弹出框(openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)，适用于在相对应用复杂的场景来实现自定义弹出框，相较于[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)优势点在于页面解耦，支持[动态刷新](../harmonyos-references/js-apis-arkui-componentcontent.md#update)。
* ArkUI提供轻量的UI元素复用机制[@Builder](../harmonyos-guides/arkts-builder.md)，其内部UI结构固定，仅与使用方进行数据传递。可将重复使用的UI元素抽象成函数，在build函数中调用。
* [Text组件](../harmonyos-references/ts-basic-components-text.md)可以自定义展示文本框的UI样式，包括[边框圆角](../harmonyos-references/ts-universal-attributes-border.md#borderradius)、[内边距](../harmonyos-references/ts-universal-attributes-size.md#padding)等。
* [setTimeout接口](../harmonyos-references/js-apis-timer.md)支持设置一个定时器，该定时器在定时器到期后执行一个函数。

## 解决方案

如果需要实现类似其他平台的Toast样式，可借助自定义弹窗实现。

主要实现思路为，借助Text组件自定义类似其他平台Toast的UI样式，并封装为@Builder构建函数，将该函数传入ComponentContent创建弹窗对象，通过getUIContext开启该弹窗对象，开启后执行setTimeout，等待指定的时间后，执行关闭弹窗对象。详细步骤如下：

1. 配置ToastContent组件属性并封装为@Builder构建函数。

   ```ts
   @Component
   struct ToastContent {
     public text: string = '';
     public clickText: string = '';
     public clickListener = () => {
     };
     private textList: string[] = [];

     aboutToAppear(): void {
       if (this.clickText.length > 0) {
         this.textList = this.text.split(this.clickText);
       }
     }

     build() {
       Column() {
         if (this.clickText === '') {
           Text(this.text).toastText();
         } else {
           Text() {
             ForEach(this.textList, (item: string, num: number) => {
               Span(item);
               if (num < this.textList.length - 1) {
                 Span(this.clickText).fontColor(Color.Yellow);
               }
             });
           }.onClick(this.clickListener).toastText();
         }
       }
       .borderRadius(5)
       .backgroundColor(Color.Black)
       .padding(10)
       .justifyContent(FlexAlign.SpaceBetween)
       .margin({ left: '5%', right: '5%' });
     }
   }

   // 封装Toast的@Builder方法
   @Builder
   function buildText(params: Params) {
     ToastContent({ text: params.text, clickText: params.clickText, clickListener: params.clickListener });
   }

   // 封装公共样式
   @Extend(Text)
   function toastText() {
     .fontSize(20)
     .fontColor(Color.White);
   }
   ```
2. 创建Toast类，并创建构造方法与Toast实例方法。

   ```ts
   /**
    * 封装全局蓝色浮动提示，支持点击
    */
   export class Toast {
     private toastParams: Params;

     constructor(text: string, time: number = 2000) {
       this.toastParams = new Params(text, time);
     }

     setClick(clickText: string, clickListener: () => void): Toast {
       this.toastParams.setClick(clickText, clickListener);
       return this;
     };

     async show() {
       let uiContext = AppStorage.get('currentUIContext') as UIContext;
       let click = this.toastParams.clickListener;
       let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), this.toastParams);
       uiContext.getPromptAction().openCustomDialog(contentNode, {
         showInSubWindow: this.toastParams.clickText === '' ? false : true,
         isModal: false,
         offset: { dx: 0, dy: '10%' }
       }).then(() => {
         setTimeout(() => {
           uiContext.getPromptAction().closeCustomDialog(contentNode);
         }, this.toastParams.time);
       });
       this.toastParams.clickListener = () => {
         click();
         uiContext.getPromptAction().closeCustomDialog(contentNode);
       };
     };
   }
   ```
3. 创建并弹出Toast，并且可以在Toast的setClick回调方法内实现点击Toast后的逻辑，如页面跳转。

   ```ts
   new Toast('点击Toast后屏幕将退出横屏，进入到竖屏状态', 3000).setClick('关闭自动添加', () => {
     this.windowClass.setPreferredOrientation(window.Orientation.PORTRAIT);
     this.pathStack.pushPathByName('DetailPage', null);
   }).show();
   ```

完整示例参考如下：

1. Index.ets。

   ```ts
   import { common } from '@kit.AbilityKit';
   import { Toast } from './ToastContent';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     pathStack: NavPathStack = new NavPathStack();
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     private windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();

     setOrientation(orientation: number) {
       this.windowClass.setPreferredOrientation(orientation).then(() => {
       }).catch(() => {
       });
     }

     async aboutToAppear(): Promise<void> {
       await this.windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE);
       AppStorage.setOrCreate('currentUIContext', this.getUIContext());
     }

     build() {
       Navigation(this.pathStack) {
         RelativeContainer() {
           Column() {
             Text('我的记录')
               .fontSize(50)
               .width('100%')
               .textAlign(TextAlign.Center)
               .fontWeight(FontWeight.Bold)
             Button('保存')
               .onClick(() => {
                 new Toast('点击Toast后屏幕将退出横屏，进入到竖屏状态', 3000).setClick('关闭自动添加', () => {
                   this.windowClass.setPreferredOrientation(window.Orientation.PORTRAIT);
                   this.pathStack.pushPathByName('DetailPage', null);
                 }).show();
               })
               .backgroundColor(Color.Blue)
               .fontColor(Color.White)
           }
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
         }
         .width('100%')
       }
       .mode(NavigationMode.Stack)
       .height('100%')
       .width('100%')
       .height('100%')
       .hideTitleBar(true)
     }
   }
   ```
2. ToastContent.ets。

   ```ts
   import { ComponentContent } from '@kit.ArkUI';
   /**
    * 封装全局蓝色浮动提示，支持点击
    */
   export class Toast {
     private toastParams: Params;

     constructor(text: string, time: number = 2000) {
       this.toastParams = new Params(text, time);
     }

     setClick(clickText: string, clickListener: () => void): Toast {
       this.toastParams.setClick(clickText, clickListener);
       return this;
     };

     async show() {
       let uiContext = AppStorage.get('currentUIContext') as UIContext;
       let click = this.toastParams.clickListener;
       let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), this.toastParams);
       uiContext.getPromptAction().openCustomDialog(contentNode, {
         showInSubWindow: this.toastParams.clickText === '' ? false : true,
         isModal: false,
         offset: { dx: 0, dy: '10%' }
       }).then(() => {
         setTimeout(() => {
           uiContext.getPromptAction().closeCustomDialog(contentNode);
         }, this.toastParams.time);
       });
       this.toastParams.clickListener = () => {
         click();
         uiContext.getPromptAction().closeCustomDialog(contentNode);
       };
     };
   }
   // 参数
   class Params {
     text: string = '';
     time: number = 2000;
     clickText: string = '';
     clickListener = () => {
     };

     constructor(text: string, time: number = 2000) {
       this.text = text;
       this.time = time;
     }

     setClick(clickText: string, clickListener: () => void) {
       this.clickText = clickText;
       this.clickListener = clickListener;
     };
   }
   @Component
   struct ToastContent {
     public text: string = '';
     public clickText: string = '';
     public clickListener = () => {
     };
     private textList: string[] = [];

     aboutToAppear(): void {
       if (this.clickText.length > 0) {
         this.textList = this.text.split(this.clickText);
       }
     }

     build() {
       Column() {
         if (this.clickText === '') {
           Text(this.text).toastText();
         } else {
           Text() {
             ForEach(this.textList, (item: string, num: number) => {
               Span(item);
               if (num < this.textList.length - 1) {
                 Span(this.clickText).fontColor(Color.Yellow);
               }
             });
           }.onClick(this.clickListener).toastText();
         }
       }
       .borderRadius(5)
       .backgroundColor(Color.Black)
       .padding(10)
       .justifyContent(FlexAlign.SpaceBetween)
       .margin({ left: '5%', right: '5%' });
     }
   }

   // 封装Toast的@Builder方法
   @Builder
   function buildText(params: Params) {
     ToastContent({ text: params.text, clickText: params.clickText, clickListener: params.clickListener });
   }

   // 封装公共样式
   @Extend(Text)
   function toastText() {
     .fontSize(20)
     .fontColor(Color.White);
   }
   ```
3. DetailPage.ets

   ```ts
   @Builder
   export function DetailPageBuilder() {
     DetailPage()
   }

   @Component
   export struct DetailPage {
     pageInfos: NavPathStack = new NavPathStack();

     build() {
       NavDestination() {
         Column() {
         }.width('100%').height('100%')
       }.title('DetailPage')

     }
   }
   ```

## 总结

该知识是综合了自定义弹窗和延时关闭功能，实现了自定义样式的Toast。可直接将上述show接口的实现代码，结合业务需要自定义Toast样式，并粘贴至自己的文件调用。
