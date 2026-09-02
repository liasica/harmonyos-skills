---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1178
title: 如何封装Popup组件到SDK
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何封装Popup组件到SDK
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac77d35a5d5abda0369a6250a288fc682f9147d843cc4443cda6a5e1391358df
---

## 问题现象

如何将Popup组件封装到har包中，以便在项目中统一使用。

## 背景知识

* [Popup](../harmonyos-guides/arkts-popup-and-menu-components-popup.md)：Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。
* [openPopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openpopup18)：创建并弹出以content作为内容的Popup弹窗，使用该接口时，若未传入有效的target，则无法弹出Popup弹窗。
* [TargetInfo](../harmonyos-references/arkts-apis-uicontext-i.md#targetinfo18)：指定组件绑定的目标节点。

## 解决方案

可以使用[openPopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openpopup18)方法为指定组件弹出气泡。示例代码如下：

1. har包封装：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { ComponentContent, TargetInfo, PromptAction } from '@kit.ArkUI';

   export class PromptActionClass {
     private promptAction: PromptAction | null = null;
     private contentNode: ComponentContent<Object> | null = null; // popup弹框组件内容
     private options: PopupCommonOptions | null = null;
     private target: TargetInfo | null = null; // 目标组件信息
     private isPartialUpdate: boolean = false;

     public setPromptAction(promptAction: PromptAction) {
       this.promptAction = promptAction;
     }

     public setContentNode(node: ComponentContent<Object>) {
       this.contentNode = node;
     }

     public setTarget(target: TargetInfo) {
       this.target = target;
     }

     public setOptions(options: PopupCommonOptions) {
       this.options = options;
     }

     public setIsPartialUpdate(isPartialUpdate: boolean) {
       this.isPartialUpdate = isPartialUpdate;
     }

     // 打开popup
     public openPopup() {
       if (this.promptAction != null) {
         this.promptAction.openPopup(this.contentNode, this.target, this.options)
           .then(() => {
             console.info(`openPopup success`);
           })
           .catch((err: BusinessError) => {
             console.error(`openPopup error: ${err.code}  ${err.message}`);
           });
       }
     }

     // 关闭popup
     public closePopup() {
       if (this.promptAction != null) {
         this.promptAction.closePopup(this.contentNode)
           .then(() => {
             console.info(`closePopup success`);
           })
           .catch((err: BusinessError) => {
             console.error(`closePopup error:  ${err.code}  ${err.message}`);
           });
       }
     }

     // 更新popup
     public updatePopup(options: PopupCommonOptions) {
       if (this.promptAction != null) {
         this.promptAction.updatePopup(this.contentNode, options, this.isPartialUpdate)
           .then(() => {
             console.info(`updatePopup success`);
           })
           .catch((err: BusinessError) => {
             console.error(`updatePopup error:  ${err.code}  ${err.message}`);
           });
       }
     }
   }
   ```
2. 在entry包的oh-package.json5中声明har包：

   ```json
   "dependencies": {
     "custompopupsdk": 'file:../CustomPopupSDK'
   },
   ```
3. entry包使用：

   ```ts
   import { PromptActionClass } from 'custompopupsdk';
   import { ComponentContent, PromptAction } from '@kit.ArkUI';

   // 用于传递参数
   class Params {
     title: string = '';
     text: string = '';
     promptActionClass: PromptActionClass = new PromptActionClass();
     ;

     constructor(title: string, text: string, promptActionClass: PromptActionClass) {
       this.title = title;
       this.text = text;
       this.promptActionClass = promptActionClass;
     }
   }

   // popup内容
   @Builder
   function buildText(params: Params) {
     Row() {
       Column() {
         Image($rawfile('logo.png'))
           .width(32)
           .height(32)
           .borderRadius(8)
       }
       .width(32)
       .height(90)

       Column() {
         Column({ space: 2 }) {
           Row() {
             Text(params.title)
               .fontSize(16)
               .fontColor('#000000')
               .fontWeight(500)
               .lineHeight(22)
               .width(214)

             Image($rawfile('xmark.svg')).width(18).height(18)
               .onClick(() => {
                 // 关闭popup
                 params.promptActionClass.closePopup();
               })
               .margin({
                 left: 12
               })
           }
           .width('100%')
           .height(22)

           Text(params.text)
             .fontSize(14)
             .fontWeight(400)
             .lineHeight(19)
             .width('100%')
             .maxLines(2)
             .textOverflow({ overflow: TextOverflow.Ellipsis })
         }
         .justifyContent(FlexAlign.Start)
         .width('100%')
         .height(62)

         Row() {
           Text('Update')
             .fontSize(14)
             .fontColor('#0A59F7')
             .fontWeight(500)
             .lineHeight(19)
             .onClick(() => {
               // 更新popup内容样式
               params.promptActionClass.updatePopup({
                 enableArrow: false,
               });
             })
         }
         .width(244)
         .height(20)
         .margin({
           top: 8
         })
       }
       .margin({
         left: 12
       })
       .width(244)
       .height(90)
       .alignItems(HorizontalAlign.Start)
       .justifyContent(FlexAlign.Start)

     }.justifyContent(FlexAlign.Center)
     .width(312)
     .height(114)
     .borderRadius(20)
   }

   @Entry
   @Component
   struct Index {
     @State title: string = 'Title';
     @State text: string =
       'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';
     private uiContext: UIContext = this.getUIContext();
     private promptAction: PromptAction = this.uiContext.getPromptAction();
     private promptActionClass: PromptActionClass = new PromptActionClass();
     private targetId: string | number = 0; // 目标组件id
     private contentNode: ComponentContent<Object> =
       new ComponentContent(this.uiContext, wrapBuilder(buildText),
         new Params(this.title, this.text, this.promptActionClass)); // 初始化自定义popup组件
     private options: PopupCommonOptions = { enableArrow: true, autoCancel: false };

     build() {
       Column() {
         Column() {
           Text('文本一')
           Text('给文本三加气泡')
             .fontColor('#0A59F7')
             .onClick(() => {
               // 指定弹出组件ID
               let targetId = 'column3';
               if (targetId == undefined) {
                 this.targetId = 0;
               } else {
                 this.targetId = targetId;
               }
               this.promptActionClass.setPromptAction(this.promptAction);
               this.promptActionClass.setContentNode(this.contentNode);
               this.promptActionClass.setOptions(this.options);
               this.promptActionClass.setIsPartialUpdate(false);
               this.promptActionClass.setTarget({ id: this.targetId });
               // 打开popup
               this.promptActionClass.openPopup();
             })
         }
         .width('100%')
         .height(100)
         .backgroundColor('#F1F3F5')
         .borderRadius(20)
         .id('column1')
         .margin({
           top: 10
         })
         .padding({
           top: 15,
           bottom: 15
         })
         .justifyContent(FlexAlign.SpaceEvenly)

         Column() {
           Text('文本二')
           Text('给文本二加气泡')
             .fontColor('#0A59F7')
             .onClick(() => {
               // 指定组件ID
               let targetId = 'column2';
               if (targetId == undefined) {
                 this.targetId = 0;
               } else {
                 this.targetId = targetId;
               }
               this.promptActionClass.setPromptAction(this.promptAction);
               this.promptActionClass.setContentNode(this.contentNode);
               this.promptActionClass.setOptions(this.options);
               this.promptActionClass.setIsPartialUpdate(false);
               this.promptActionClass.setTarget({ id: this.targetId });
               this.promptActionClass.openPopup();
             })
         }
         .width('100%')
         .height(100)
         .backgroundColor('#F1F3F5')
         .borderRadius(20)
         .id('column2')
         .margin({
           top: 10
         })
         .padding({
           top: 15,
           bottom: 15
         })
         .justifyContent(FlexAlign.SpaceEvenly)

         Column() {
           Text('文本三')
           Text('给文本一加气泡')
             .fontColor('#0A59F7')
             .onClick(() => {
               // 指定组件ID
               let targetId = 'column1';
               if (targetId == undefined) {
                 this.targetId = 0;
               } else {
                 this.targetId = targetId;
               }
               this.promptActionClass.setPromptAction(this.promptAction);
               this.promptActionClass.setContentNode(this.contentNode);
               this.promptActionClass.setOptions(this.options);
               this.promptActionClass.setIsPartialUpdate(false);
               this.promptActionClass.setTarget({ id: this.targetId });
               this.promptActionClass.openPopup();
             })
         }
         .width('100%')
         .height(100)
         .borderRadius(20)
         .backgroundColor('#F1F3F5')
         .id('column3')
         .margin({
           top: 10
         })
         .padding({
           top: 15,
           bottom: 15
         })
         .justifyContent(FlexAlign.SpaceEvenly)
       }
     }
   }
   ```

   运行效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/rt4dDRK1RYSW5vRafu5NIw/zh-cn_image_0000002628592954.png "点击放大")
