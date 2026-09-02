---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1655
title: 如何将自定义弹窗Builder作为变量传递实现弹窗控制器
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何将自定义弹窗Builder作为变量传递实现弹窗控制器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9548fd8515d5e474b9952be1e4751ec9effb5418cadacc51b7c2822dcf252916
---

## 问题现象

如何实现类似于CustomDialogController的控制器，可以传递一个@Builder，去加载自定义弹窗。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/G1rhRRYZQCS_Z_l3CJTwyw/zh-cn_image_0000002659020193.png "点击放大")

## 背景知识

* [@Builder装饰器：自定义构建函数](../harmonyos-guides/arkts-builder.md)：@Builder装饰的函数也称为“自定义构建函数”。
* [wrapBuilder：封装全局@Builder](../harmonyos-guides/arkts-wrapbuilder.md)：可以使用wrapBuilder封装全局@Builder。
* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：创建并弹出dialogContent对应的自定义弹窗。
* @Builder装饰器修饰函数不支持传递函数方法，仅支持传值，有按值传递和按引用传递两种。但可以通过WrappedBuilder包装类将@Builder的函数包装，之后将WrappedBuilder对象当作变量进行传递。

## 解决方案

@Builder装饰器修饰函数不支持传递函数方法，但可以通过WrappedBuilder包装类将@Builder的函数包装，之后将WrappedBuilder对象当作变量进行传递。

开发步骤如下：

1. 自定义控制器类，用于创建弹窗、打开弹窗、更新弹窗内容、关闭弹窗等操作。

   ```ts
   class CustomDialogController {
     private uiContext: UIContext;
     private promptDialog: PromptAction;
     private contentNode: ComponentContent<object>;
     params?: Params;

     constructor(uiContext: UIContext, builder: WrappedBuilder<[]>, params?: Params) {
       this.uiContext = uiContext;
       this.promptDialog = this.uiContext.getPromptAction();
       this.params = params;
       this.contentNode = new ComponentContent(this.uiContext, builder, this);
     }

     openDialog() {
       this.promptDialog.openCustomDialog(this.contentNode);
     }

     closeDialog() {
       this.promptDialog.closeCustomDialog(this.contentNode);
     }

     updateDialogContent(params: Params) {
       this.params = params;
       this.contentNode.update(this);
     }
   }
   ```
2. 自定义@Builder，用于显示自定义弹窗内容，更新弹窗内容，关闭弹窗。

   ```ts
   @Builder
   function dialogBuilder(controller?: CustomDialogController) {
     Column() {
       Row() {
         // 实际使用时可替换为实际图片
         Image($r('app.media.img'))
           .width(80)
           .height(80);
         Column() {
           Text('HUAWEI Mate 80 Pro Max 风驰版 16GB+512GB 极夜黑')
             .maxLines(2)
             .textAlign(TextAlign.Start)
             .margin({ right: 15 })
             .fontSize(12);
           Text('麒麟9030 Pro 芯片，风驰散热架构，超空间内存技术')
             .maxLines(2)
             .textAlign(TextAlign.Start)
             .fontSize(10)
             .margin({ right: 15 });
           Row() {
             // 实际使用时可替换为实际图片
             Image($r('app.media.img_2'))
               .backgroundColor('#f1f3f5')
               .onClick(() => {
                 if (goodsCount > 0) {
                   goodsCount--;
                 }
                 controller!.updateDialogContent(new Params(goodsCount));
               })
               .width(20)
               .height(20);
             Text(`${controller!.params?.content}`)
               .margin({ left: 10 });
             // 实际使用时可替换为实际图片
             Image($r('app.media.img_1'))
               .backgroundColor('#f1f3f5')
               .margin({ left: 10 })
               .onClick(() => {
                 goodsCount++;
                 controller!.updateDialogContent(new Params(goodsCount));
               })
               .width(20)
               .height(20);
           }
           .margin({ top: 20 });
         }
         .padding({ top: 8 })
         .justifyContent(FlexAlign.Start)
         .alignItems(HorizontalAlign.Start)
         .width('80%')
         .height(80);
       }
       .justifyContent(FlexAlign.Start);

       Row({ space: 20 }) {
         Text('关闭')
           .fontSize(15)
           .backgroundColor('#f1f3f5')
           .borderRadius(5)
           .fontColor('#0a59f7')
           .width(100)
           .padding({ top: 5, bottom: 5 })
           .textAlign(TextAlign.Center)
           .onClick(() => {
             controller!.closeDialog();
           });
         Text('加入购物车')
           .fontSize(15)
           .backgroundColor('#0a59f7')
           .borderRadius(5)
           .textAlign(TextAlign.Center)
           .width(100)
           .padding({ top: 5, bottom: 5 })
           .fontColor(Color.White)
           .onClick(() => {
             controller!.closeDialog();
           });
       };

     }
     .height(200)
     .width('90%')
     .backgroundColor(Color.White)
     .justifyContent(FlexAlign.SpaceBetween)
     .padding(18)
     .borderRadius(15);
   }
   ```
3. 页面初始化弹窗控制器并使用。

   ```ts
   @Entry
   @Component
   struct CustomDialogPageExample {
     uiContext = this.getUIContext();
     private customDialogController: CustomDialogController =
       new CustomDialogController(this.getUIContext(), wrapBuilder(dialogBuilder), new Params(goodsCount));

     build() {
       Column() {
         Button('open dialog')
           .fontWeight(FontWeight.Bold)
           .onClick(() => {
             this.customDialogController!.openDialog();
           });
       }
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .width('100%')
       .height('100%');
     }
   }
   ```

完整示例参考如下：

```ts
import { ComponentContent, PromptAction } from '@kit.ArkUI';

let goodsCount: number = 0;

class Params {
  content: number;

  constructor(content: number) {
    this.content = content;
  }
}
class CustomDialogController {
  private uiContext: UIContext;
  private promptDialog: PromptAction;
  private contentNode: ComponentContent<object>;
  params?: Params;

  constructor(uiContext: UIContext, builder: WrappedBuilder<[]>, params?: Params) {
    this.uiContext = uiContext;
    this.promptDialog = this.uiContext.getPromptAction();
    this.params = params;
    this.contentNode = new ComponentContent(this.uiContext, builder, this);
  }

  openDialog() {
    this.promptDialog.openCustomDialog(this.contentNode);
  }

  closeDialog() {
    this.promptDialog.closeCustomDialog(this.contentNode);
  }

  updateDialogContent(params: Params) {
    this.params = params;
    this.contentNode.update(this);
  }
}
@Entry
@Component
struct CustomDialogPageExample {
  uiContext = this.getUIContext();
  private customDialogController: CustomDialogController =
    new CustomDialogController(this.getUIContext(), wrapBuilder(dialogBuilder), new Params(goodsCount));

  build() {
    Column() {
      Button('open dialog')
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.customDialogController!.openDialog();
        });
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
@Builder
function dialogBuilder(controller?: CustomDialogController) {
  Column() {
    Row() {
      // 实际使用时可替换为实际图片
      Image($r('app.media.img'))
        .width(80)
        .height(80);
      Column() {
        Text('HUAWEI Mate 80 Pro Max 风驰版 16GB+512GB 极夜黑')
          .maxLines(2)
          .textAlign(TextAlign.Start)
          .margin({ right: 15 })
          .fontSize(12);
        Text('麒麟9030 Pro 芯片，风驰散热架构，超空间内存技术')
          .maxLines(2)
          .textAlign(TextAlign.Start)
          .fontSize(10)
          .margin({ right: 15 });
        Row() {
          // 实际使用时可替换为实际图片
          Image($r('app.media.img_2'))
            .backgroundColor('#f1f3f5')
            .onClick(() => {
              if (goodsCount > 0) {
                goodsCount--;
              }
              controller!.updateDialogContent(new Params(goodsCount));
            })
            .width(20)
            .height(20);
          Text(`${controller!.params?.content}`)
            .margin({ left: 10 });
          // 实际使用时可替换为实际图片
          Image($r('app.media.img_1'))
            .backgroundColor('#f1f3f5')
            .margin({ left: 10 })
            .onClick(() => {
              goodsCount++;
              controller!.updateDialogContent(new Params(goodsCount));
            })
            .width(20)
            .height(20);
        }
        .margin({ top: 20 });
      }
      .padding({ top: 8 })
      .justifyContent(FlexAlign.Start)
      .alignItems(HorizontalAlign.Start)
      .width('80%')
      .height(80);
    }
    .justifyContent(FlexAlign.Start);

    Row({ space: 20 }) {
      Text('关闭')
        .fontSize(15)
        .backgroundColor('#f1f3f5')
        .borderRadius(5)
        .fontColor('#0a59f7')
        .width(100)
        .padding({ top: 5, bottom: 5 })
        .textAlign(TextAlign.Center)
        .onClick(() => {
          controller!.closeDialog();
        });
      Text('加入购物车')
        .fontSize(15)
        .backgroundColor('#0a59f7')
        .borderRadius(5)
        .textAlign(TextAlign.Center)
        .width(100)
        .padding({ top: 5, bottom: 5 })
        .fontColor(Color.White)
        .onClick(() => {
          controller!.closeDialog();
        });
    };

  }
  .height(200)
  .width('90%')
  .backgroundColor(Color.White)
  .justifyContent(FlexAlign.SpaceBetween)
  .padding(18)
  .borderRadius(15);
}
```
