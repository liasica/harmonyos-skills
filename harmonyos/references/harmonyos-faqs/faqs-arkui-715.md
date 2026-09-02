---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-715
title: 使用openCustomDialog实现菜单弹窗并返回选中项回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用openCustomDialog实现菜单弹窗并返回选中项回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad32bf256467fef643a9f4066a5c089dacc4b3b2c66b131465972918a53a65fe
---

## 问题现象

如何使用openCustomDialog实现一个从外部传参的菜单弹窗，并且可以在外部监听菜单项的选中状态。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/QfF2XLtPRL-rZEzmh8cV6Q/zh-cn_image_0000002628395012.gif "点击放大")

## 背景知识

[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)存在两种入参方式创建自定义弹出框，[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md#componentcontent-1)和[Builder](../harmonyos-guides/arkts-builder.md)：

* ComponentContent封装内容可以与UI界面解耦，调用更加灵活。
* 使用Builder的方式，必须要与上下文做绑定，与UI存在一定耦合，具体请参考：[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)的说明部分和[@Builder装饰器使用说明](../harmonyos-guides/arkts-builder.md#装饰器使用说明)。

## 解决方案

1. 参考[完整示例](../harmonyos-guides/arkts-uicontext-custom-dialog.md#完整示例)实现弹窗工具类，其核心是以下属性的具体实现：
   * ctx：获取UI上下文用于实现弹窗服务。
   * contentNode：构建弹窗的内容节点，其中弹窗中菜单项的个数，内容和传给外部监听的回调通过Params类型的数组传递。
   * options：弹窗的配置选项，如位置、样式、动画等。

     ```ts
     export class CustomerPromptAction {
       static ctx: UIContext;
       static contentNode: ComponentContent<Object>;
       static options: promptAction.BaseDialogOptions;

       // 定义方法，从外部传入上下文。
       static setContext(context: UIContext) {
         CustomerPromptAction.ctx = context;
       }

       // 配置内容节点。
       static setContentNode(context: UIContext, para: Params[]) {
         let contentNode: ComponentContent<Object> = new ComponentContent(context, wrapBuilder(buildText), para);
         CustomerPromptAction.contentNode = contentNode;
       }

       // 弹窗配置项。
       static setOptions(options: promptAction.BaseDialogOptions) {
         CustomerPromptAction.options = options;
       }

       // 定义弹窗打开的方法。
       static openDialog(options: promptAction.BaseDialogOptions, context: UIContext, para: Params[]) {
         CustomerPromptAction.setContext(context);
         CustomerPromptAction.setContentNode(context, para);
         CustomerPromptAction.setOptions({ alignment: DialogAlignment.Bottom, offset: { dx: 0, dy: -20 } });
         if (CustomerPromptAction.contentNode !== null) {
           CustomerPromptAction.ctx.getPromptAction()
             .openCustomDialog(CustomerPromptAction.contentNode, options)
             .then(() => {
             })
             .catch(() => {
             });
         }
       }

       // 关闭弹窗。
       static closeDialog() {
         if (CustomerPromptAction.contentNode !== null) {
           CustomerPromptAction.ctx.getPromptAction()
             .closeCustomDialog(CustomerPromptAction.contentNode)
             .then(() => {
             })
             .catch(() => {
             });
         }
       }
     }
     ```
2. 在页面中调用弹窗。
   * 自定义菜单项实体类，声明属性方法，并通过构造器实例化。

     ```ts
     export class Params {
       title: string = "";
       iconName: Resource;
       click: (index: number) => void;

       constructor(title: string, iconName: Resource, click: (index: number) => void) {
         this.title = title;
         this.iconName = iconName;
         this.click = click;
       }
     }
     ```
   * 定义接收菜单项选中回调的函数，根据返回的index处理逻辑。

     ```ts
     // 点击弹窗中按钮的回调，并根据返回的index判断逻辑。
     callBack = (index: number) => {
       switch (index) {
         case 0:
           this.getUIContext().getPromptAction().showToast({
             message: '点击了关闭',
             duration: 2000
           });
           break;
         case 1:
           this.getUIContext().getPromptAction().showToast({
             message: '点击了刷新',
             duration: 2000
           });
           break;
         case 2:
           this.getUIContext().getPromptAction().showToast({
             message: '点击了帮助',
             duration: 2000
           });
           break;
       }
     };
     ```
   * 初始化菜单数据源。

     ```ts
     @State arr: Params[] = [
       new Params('关闭', $r('app.media.startIcon'), this.callBack),
       new Params('刷新', $r('app.media.startIcon'), this.callBack),
       new Params('帮助', $r('app.media.startIcon'), this.callBack)];
     ```

完整示例参考如下：

1. CustomerPromptAction.ets。

   ```ts
   import { ComponentContent, promptAction } from '@kit.ArkUI';
   import { UIContext } from '@ohos.arkui.UIContext';
   import { Params } from './Params';

   @Builder
   function buildText(params: Params[]) {
     Column() {
       Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceAround }) {
         ForEach(params, (item: Params, index: number) => {
           Column() {
             Image(item.iconName)
               .width(30)
               .height(30)
               .margin({ top: 20 })
               .onClick(() => {
                 item.click(index);
               });
             Text(item.title)
               .fontSize(15)
               .margin({ top: 20 });
           };
         });
       }
       .width('100%');

       Text('取消')
         .margin({ top: 20 })
         .height(50)
         .width('100%')
         .textAlign(TextAlign.Center)
         .fontColor(Color.Blue)
         .onClick(() => {
           CustomerPromptAction.closeDialog();
         });
     }
     .backgroundColor('#FFF0F0F0')
     .width('100%')
     .borderRadius(10);
   }
   export class CustomerPromptAction {
     static ctx: UIContext;
     static contentNode: ComponentContent<Object>;
     static options: promptAction.BaseDialogOptions;

     // 定义方法，从外部传入上下文。
     static setContext(context: UIContext) {
       CustomerPromptAction.ctx = context;
     }

     // 配置内容节点。
     static setContentNode(context: UIContext, para: Params[]) {
       let contentNode: ComponentContent<Object> = new ComponentContent(context, wrapBuilder(buildText), para);
       CustomerPromptAction.contentNode = contentNode;
     }

     // 弹窗配置项。
     static setOptions(options: promptAction.BaseDialogOptions) {
       CustomerPromptAction.options = options;
     }

     // 定义弹窗打开的方法。
     static openDialog(options: promptAction.BaseDialogOptions, context: UIContext, para: Params[]) {
       CustomerPromptAction.setContext(context);
       CustomerPromptAction.setContentNode(context, para);
       CustomerPromptAction.setOptions({ alignment: DialogAlignment.Bottom, offset: { dx: 0, dy: -20 } });
       if (CustomerPromptAction.contentNode !== null) {
         CustomerPromptAction.ctx.getPromptAction()
           .openCustomDialog(CustomerPromptAction.contentNode, options)
           .then(() => {
           })
           .catch(() => {
           });
       }
     }

     // 关闭弹窗。
     static closeDialog() {
       if (CustomerPromptAction.contentNode !== null) {
         CustomerPromptAction.ctx.getPromptAction()
           .closeCustomDialog(CustomerPromptAction.contentNode)
           .then(() => {
           })
           .catch(() => {
           });
       }
     }
   }
   ```
2. Index.ets。

   ```ts
   import { Params } from './Params';
   import { CustomerPromptAction } from './CustomerPromptAction';

   @Entry
   @Component
   struct Index {
     // 点击弹窗中按钮的回调，并根据返回的index判断逻辑。
     callBack = (index: number) => {
       switch (index) {
         case 0:
           this.getUIContext().getPromptAction().showToast({
             message: '点击了关闭',
             duration: 2000
           });
           break;
         case 1:
           this.getUIContext().getPromptAction().showToast({
             message: '点击了刷新',
             duration: 2000
           });
           break;
         case 2:
           this.getUIContext().getPromptAction().showToast({
             message: '点击了帮助',
             duration: 2000
           });
           break;
       }
     };
     // 初始化弹窗菜单的数据源。
     @State arr: Params[] = [
       new Params('关闭', $r('app.media.startIcon'), this.callBack),
       new Params('刷新', $r('app.media.startIcon'), this.callBack),
       new Params('帮助', $r('app.media.startIcon'), this.callBack)];

     build() {
       Row() {
         Column() {
           Button('横向菜单')
             .margin({ top: 50 })
             .onClick(() => {
               CustomerPromptAction.openDialog({
                 alignment: DialogAlignment.Bottom,
                 offset: { dx: 0, dy: -20 }
               }, this.getUIContext(), this.arr);
             });
         }
         .width('100%')
         .height('100%');
       }
       .height('100%');
     }
   }
   ```
3. Params.ets。

   ```ts
   export class Params {
     title: string = "";
     iconName: Resource;
     click: (index: number) => void;

     constructor(title: string, iconName: Resource, click: (index: number) => void) {
       this.title = title;
       this.iconName = iconName;
       this.click = click;
     }
   }
   ```
