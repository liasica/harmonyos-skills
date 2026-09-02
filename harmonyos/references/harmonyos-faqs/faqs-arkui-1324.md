---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1324
title: Dialog弹出多个弹窗后无法关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Dialog弹出多个弹窗后无法关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb8e140cdad3719730dae55f689958736dfdb82275ab0a3c8e796dc43dd41571
---

## 问题现象

如何解决弹出多个弹窗，无法关闭的问题？

问题代码示例参考如下：

```ts
closeDialog() {
  if (DialogUtils.contentNode) {
    let uiContext: UIContext | undefined = AppStorage.get<UIContext>('uiContext')
    if (uiContext) {
      uiContext.getPromptAction().closeCustomDialog(DialogUtils.contentNode)
      // 关闭一个弹窗就清空了，后面调用就都是null，所以关不掉
      DialogUtils.contentNode = null
    }
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/7tvLM56yS66EQEFeNlsZqw/zh-cn_image_0000002658958965.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/C6l5SSHORJi5WNRsZTYpQQ/zh-cn_image_0000002658839015.png "点击放大")

## 背景知识

* [ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)：表示组件内容的实体封装，其对象支持在非UI组件中创建与传递，便于开发者对弹窗类组件进行解耦封装。
* [@ohos.promptAction(弹窗)](../harmonyos-references/js-apis-promptaction.md)：创建并显示文本提示框、对话框和操作菜单。
* contentNode：ComponentContent创建的实例。

## 解决方案

弹窗关闭的代码有误，“DialogUtils.contentNode = null”关闭一个弹窗就清空了，后面调用就都是null，所以关不掉。

方案如下：用个数组存储每个弹窗的contentNode，每关闭一个pop()一个，并将数组最后一个值赋值给contentNode，关闭的就是上一个弹窗的contentNode。

完整示例参考如下：

1. DialogUtils.ets。

   ```ts
   import { ComponentContent, promptAction } from '@kit.ArkUI';

   export class Params {
     content: string = '';
     callback: (isGranted: boolean, msg?: string) => void = (): void => {
     };

     constructor(content: string, callback: (isGranted: boolean, msg?: string) => void) {
       this.content = content;
       this.callback = callback;
     }
   }

   @Builder
   export function buildText(params: Params) {
     Column() {
       Column() {
         // 内容
         Text(params.content)
           .width('100%')
           .textAlign(TextAlign.Start)
           .padding(15)
           .fontSize(18)
           .fontColor('#2c2c2c')

         Column()
           .width('100%')
           .height(0.5)
           .backgroundColor('#E6E6E6')

         // 取消、确定按钮
         Row() {
           // 取消按钮
           Text('取消按钮')
             .width(0)
             .layoutWeight(1)
             .textAlign(TextAlign.Center)
             .padding({ top: 20, bottom: 20 })
             .fontColor('#BDBDBD')
             .borderRadius({ bottomLeft: 5 })
             .fontSize(15)
             .onClick(() => {
               DialogUtils.closeDialog();
             })
           Text('确定按钮')
             .width(0)
             .layoutWeight(1)
             .textAlign(TextAlign.Center)
             .padding({ top: 20, bottom: 20 })
             .fontColor('#BDBDBD')
             .borderRadius({ bottomLeft: 5 })
             .fontSize(15)
             .onClick(() => {
               DialogUtils.closeDialog();
               params.callback(false, 'okk');
             })
         }
         .width('100%')
         .alignItems(VerticalAlign.Center)
         .justifyContent(FlexAlign.SpaceAround)
       }
       .backgroundColor(Color.White)
       .borderRadius(5)
       .margin({ left: 15, right: 15 })
     }
     .height('100%')
     .width('100%')
     .justifyContent(FlexAlign.Center)
     .backgroundColor(Color.Transparent)
   }

   export default class DialogUtils {
     static contentNode: ComponentContent<Params> | null = null;
     static contentNodes: Array<ComponentContent<Params>> = [];

     static showDialog(content: string, callback: (isGranted: boolean, msg?: string) => void) {
       let uiContext: UIContext | undefined = AppStorage.get<UIContext>('uiContext');

       if (uiContext) {
         let promptAction = uiContext.getPromptAction();
         DialogUtils.contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(content, callback));
         DialogUtils.contentNodes.push(DialogUtils.contentNode);

         let options: promptAction.BaseDialogOptions = {
           alignment: DialogAlignment.Top,
           autoCancel: false,
           maskColor: '#cd000000',
         };
         promptAction.openCustomDialog(DialogUtils.contentNode, options);
       }
     }

     public static closeDialog() {
       if (DialogUtils.contentNode) {
         let uiContext: UIContext | undefined = AppStorage.get<UIContext>('uiContext');
         if (uiContext) {
           let promptAction = uiContext.getPromptAction();
           promptAction.closeCustomDialog(DialogUtils.contentNode);
           if (DialogUtils.contentNodes.length > 0) {
             DialogUtils.contentNodes.pop();
             if (DialogUtils.contentNodes.length > 0) {
               DialogUtils.contentNode = DialogUtils.contentNodes[DialogUtils.contentNodes.length - 1];
             } else {
               DialogUtils.contentNode = null;
             }
           }
         }
       }
     }
   }
   ```
2. Index.ets。

   ```ts
   import DialogUtils from './DialogUtils';

   AppStorage.setOrCreate('uiContext', undefined);

   @Entry
   @Component
   struct Index {
     pageInfos: NavPathStack = new NavPathStack();
     @StorageLink('uiContext') uiContext: UIContext | undefined = undefined;

     build() {
       Navigation(this.pageInfos) {
         RelativeContainer() {
           Text('首页')
             .fontSize(22)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.White)
       }
       .hideTitleBar(false)
       .hideToolBar(false)
     }

     aboutToAppear(): void {
       this.uiContext = this.getUIContext();
       let nums: number = 8;
       for (let i = 0; i < nums; i++) {
         DialogUtils.showDialog(`hello world: ${i}`, (isGrant: boolean, msg?: string) => {
           console.log(`${isGrant}--------${msg}`);
         });
       }
     }
   }
   ```
