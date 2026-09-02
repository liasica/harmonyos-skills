---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-899
title: 如何进行自定义弹窗的封装调用
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何进行自定义弹窗的封装调用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2f847b071f99c718cb24461a1fc70508f70d2fd44c1ed0f796373c7442a493a8
---

## 问题现象

如果一个页面需要弹出自定义弹窗，那么页面就需要定义CustomDialogController。

1. 多个页面就会出现多份重复的定义CustomDialogController代码。
2. 一个页面需要定义多个自定义弹窗时，会出现多份重复的CustomDialogController定义代码。
3. 相同的自定义弹窗在多个页面使用，每个页面都需要去定义CustomDialogController，造成大量代码的重复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/W8apQcbaSXaY74qgCb7pSA/zh-cn_image_0000002628399752.png)

   综上，重复的定义CustomDialogController代码会影响开发者的开发效率以及代码的整洁。

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/KN4lifa-QgyogXn4vhar4A/zh-cn_image_0000002658799019.png "点击放大")

## 背景知识

通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义，详情请参考[自定义弹窗 (CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md)。

## 解决方案

可以通过封装自定义弹窗模块，这样就无需在每个页面定义CustomDialogController，仅需传入以下两个参数，调用方法即可获得自定义弹窗：

* 传入弹窗名称；
* 传入弹窗自定义内容，如文本内容，图片内容。

代码示例如下，调用的是testPromptDialog方法：

```typescript
// 封装弹窗的方法，传入页面名称和文本内容
export function testPromptDialog(pageName: string, text: string, controller: Function) {
  let that = GlobalContext.getGlobalContext().getObject(pageName) as UIContext;
  let context = GlobalContext.getGlobalContext().getObject('UIContext') as UIContext;
  if (that) {
    context.getPromptAction().openCustomDialog({
      builder: controller.bind(that, text)
    }).then((dialogId: number) => {
      customDialogId = dialogId;
    });
  }
}
```

开发步骤如下:

1. 新建GlobalContext.ets工具类，用于页面Context的保存和获取。

   ```typescript
   export class GlobalContext {
     private constructor() {
     }
     // 定义GlobalContext供全局调用
     private static instance: GlobalContext;
     private _objects = new Map<string, Object>();
     // GlobalContext的单例方法
     public static getGlobalContext(): GlobalContext {
       if (!GlobalContext.instance) {
         GlobalContext.instance = new GlobalContext();
       }
       return GlobalContext.instance;
     }
     // 取值
     getObject(value: string): Object | undefined {
       return this._objects.get(value);
     }
     // 存值
     setObject(key: string, objectClass: Object): void {
       this._objects.set(key, objectClass);
     }
   }
   ```
2. 新建DialogUtils.ets工具类，工具类中已封装了自定义弹窗，以及弹出自定义弹窗的方法。拉起弹窗通过this.getUIContext().getPromptAction().openCustomDialog来实现。

   ```typescript
   import { GlobalContext } from './GlobalContext';

   let customDialogId: number = 0;
   // 定义失败builder
   @Builder
   export function failDialogBuilder(content: String) {
     Column() {
       Text(content as string)
         .fontSize(20).height('30%');
       Text('失败原因：' + content).fontSize(16).height('30%');
       Row() {
         Button('确认').onClick(() => {
           let that = GlobalContext.getGlobalContext().getObject('UIContext') as UIContext;
           if (that) {
             that.getPromptAction().closeCustomDialog(customDialogId);
           }
         });
         Blank().width(50);
         Button('取消').onClick(() => {
           let that = GlobalContext.getGlobalContext().getObject('UIContext') as UIContext;
           if (that) {
             that.getPromptAction().closeCustomDialog(customDialogId);
           }
         });
       }
       .margin({ top: 30 });
     }.height(200).padding(5);
   }
   // 定义成功builder
   @Builder
   export function successDialogBuilder(content: String) {
     Column() {
       Text(content as string)
         .fontSize(20).height('30%');
       Text('成功原因：' + content).fontSize(16).height('30%');
       Row() {
         Button('确认').onClick(() => {
           let that = GlobalContext.getGlobalContext().getObject('UIContext') as UIContext;
           if (that) {
             that.getPromptAction().closeCustomDialog(customDialogId);
           }
         });
         Blank().width(50);
         Button('取消').onClick(() => {
           let that = GlobalContext.getGlobalContext().getObject('UIContext') as UIContext;
           if (that) {
             that.getPromptAction().closeCustomDialog(customDialogId);
           }
         });
       }
       .margin({ top: 30 });
     }.height(200).padding(5);
   }
   // 封装弹窗的方法，传入页面名称和文本内容
   export function testPromptDialog(pageName: string, text: string, controller: Function) {
     let that = GlobalContext.getGlobalContext().getObject(pageName) as UIContext;
     let context = GlobalContext.getGlobalContext().getObject('UIContext') as UIContext;
     if (that) {
       context.getPromptAction().openCustomDialog({
         builder: controller.bind(that, text)
       }).then((dialogId: number) => {
         customDialogId = dialogId;
       });
     }
   }
   ```
3. 页面初始化时存入Context，然后在入口处调用自定义弹窗封装方法。

   ```typescript
   import { GlobalContext } from './GlobalContext';
   import { failDialogBuilder, successDialogBuilder, testPromptDialog } from './DialogUtils';

   @Entry
   @Component
   struct Index {
     aboutToAppear(): void {
       // 设置page的Context
       GlobalContext.getGlobalContext().setObject('pageName', this);
       GlobalContext.getGlobalContext().setObject('UIContext', this.getUIContext());
     }

     build() {
       Row() {
         Column() {
           Button('promptAction失败弹窗')
             .onClick(() => {
               testPromptDialog('pageName', 'this is  dialog1', failDialogBuilder);
             });
           Button('promptAction成功弹窗')
             .margin({ top: 15 })
             .onClick(() => {
               testPromptDialog('pageName', 'this is dialog2', successDialogBuilder);
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```

## 总结

在开发中，遇到需要重复定义的工具类代码，可以封装工具类，并使用GlobalContext去记录页面Context，通过封装方法并传入参数的方式获得想要的弹窗等功能。
