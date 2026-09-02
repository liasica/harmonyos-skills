---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1467
title: 如何让有自定义弹窗的应用进入多任务页面时，弹窗模糊显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何让有自定义弹窗的应用进入多任务页面时，弹窗模糊显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:264e8ac25d576501ca31b24c8b8b6c115e58aca630d0495fb64442098cde8dc8
---

## 问题现象

当应用当前页面有自定义弹窗时，在当前页面使用foregroundBlurStyle()属性设置模糊，只能让页面模糊，自定义弹窗不会模糊。如何让有自定义弹窗的应用进入多任务页面时，弹窗模糊显示？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/U-10pfPGQtWMVMcBN2bhkg/zh-cn_image_0000002628765246.png "点击放大")

## 背景知识

* [on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)接口可以实时监听窗口状态。
* [wrapBuilder()](../harmonyos-guides/arkts-wrapbuilder.md)作为全局@Builder封装函数返回WrappedBuilder对象，实现全局@Builder可以进行赋值和传递。
* [ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)的[update()](../harmonyos-references/js-apis-arkui-componentcontent.md#update)方法提供了一种动态更新WrappedBuilder对象封装的Builder函数参数的方法，与constructor传入的参数类型保持一致。
* [foregroundBlurStyle()](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle)是一个实时模糊接口，为当前组件动态提供内容模糊能力。
* [ForegroundBlurStyleOptions](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyleoptions对象说明)对象的scale选项可以调整内容模糊程度。

## 解决方案

通过on('windowStageEvent')接口实时监听窗口状态，动态设置弹窗组件的foregroundBlurStyle()属性实现模糊性效果。

1. 添加一个参数类，为update()方法提供带有constructor构造函数的入参。

   ```ts
   class Params {
     shown: boolean = true;

     constructor(shown: boolean) {
       this.shown = shown;
     }
   }
   ```
2. 使用@Builder装饰器，自定义构建函数。

   ```ts
   @Builder
   function
   customDialogComponent(params: Params) {
     Column() {
       Text('自定义弹窗')
         .fontSize(20)
         .fontColor(Color.Black)
         .margin({ top: 0 });
       Row() {
         Button('确认').onClick(() => {

         });
         Blank().width(50);
         Button('取消').onClick(() => {
         });
       }
       .height('30%')
       .width('100%')
       .justifyContent(FlexAlign.Center);
     }
     .justifyContent(FlexAlign.SpaceAround)
     .height('20%')
     .width('80%')
     .borderRadius(20)
     .backgroundColor(Color.White)
     // 此处添加foregroundBlurStyle属性，并为其scale选项设置三目运算符，
     // 根据标志位动态调整内容模糊程度
     .foregroundBlurStyle(BlurStyle.Thin, { scale: params.shown ? 0 : 1 });
   }
   ```
3. 声明ComponentContent对象，将自定义构建函数的WrappedBuilder对象和参数传入。在监听windowStageEvent状态时，根据不同的前台状态，设置不同的标志位状态，再调用update方法刷新弹窗UI。

   ```ts
   @Entry
   @Component
   struct CustomDialogBlurDemo {
     public message: string = 'Show CustomDialog';
     private uiContext: UIContext = this.getUIContext();
     // 声明状态变量做标志位
     @State shown: boolean = true;
     // 声明ComponentContent对象以调用update方法，将自定义构建函数的WrappedBuilder对象和参数传入
     @State contentNode: ComponentContent<Params> =
       new ComponentContent(this.uiContext, wrapBuilder(customDialogComponent), new Params(this.shown));

     aboutToAppear(): void {
       // 监听windowStageEvent
       (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.on('windowStageEvent',
         (windowEvent) => {
           if (windowEvent === 5) {
             // 前台可交互时标志位置true，调用update方法更新构建参数
             this.shown = true;
             this.contentNode.update(new Params(this.shown));
             console.info('this.shown is false');
           } else if (windowEvent === 6) {
             // 前台不可交互时标志位置false，调用update方法更新构建参数
             this.shown = false;
             this.contentNode.update(new Params(this.shown));
             console.info('this.shown is true');
           }
           console.info(`Window event happened.  Event: ${windowEvent}`);
         });
     }

     build() {
       Row() {
         Column() {
           Button(this.message)
             .fontSize(30)
             .fontColor(Color.White)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               // 拉起弹窗
               let uiContext = this.getUIContext();
               let PromptAction = uiContext.getPromptAction();
               let contentNode =
                 new ComponentContent(uiContext, wrapBuilder(customDialogComponent), new Params(this.shown));
               this.contentNode = contentNode;
               PromptAction.openCustomDialog(this.contentNode).catch(() => {
                 console.info('Failed to show the CustomDialog !!!');
               });
             });
         }
         .width('100%')
         .height('50%');
       }
       .height('100%')
       .backgroundImageSize({ width: 600, height: 800 })
       .foregroundBlurStyle(BlurStyle.Thin, { scale: this.shown ? 0 : 1 });
     }
   }
   ```

完整代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { ComponentContent } from '@kit.ArkUI';

class Params {
  shown: boolean = true;

  constructor(shown: boolean) {
    this.shown = shown;
  }
}
@Builder
function
customDialogComponent(params: Params) {
  Column() {
    Text('自定义弹窗')
      .fontSize(20)
      .fontColor(Color.Black)
      .margin({ top: 0 });
    Row() {
      Button('确认').onClick(() => {

      });
      Blank().width(50);
      Button('取消').onClick(() => {
      });
    }
    .height('30%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
  .justifyContent(FlexAlign.SpaceAround)
  .height('20%')
  .width('80%')
  .borderRadius(20)
  .backgroundColor(Color.White)
  // 此处添加foregroundBlurStyle属性，并为其scale选项设置三目运算符，
  // 根据标志位动态调整内容模糊程度
  .foregroundBlurStyle(BlurStyle.Thin, { scale: params.shown ? 0 : 1 });
}
@Entry
@Component
struct CustomDialogBlurDemo {
  public message: string = 'Show CustomDialog';
  private uiContext: UIContext = this.getUIContext();
  // 声明状态变量做标志位
  @State shown: boolean = true;
  // 声明ComponentContent对象以调用update方法，将自定义构建函数的WrappedBuilder对象和参数传入
  @State contentNode: ComponentContent<Params> =
    new ComponentContent(this.uiContext, wrapBuilder(customDialogComponent), new Params(this.shown));

  aboutToAppear(): void {
    // 监听windowStageEvent
    (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.on('windowStageEvent',
      (windowEvent) => {
        if (windowEvent === 5) {
          // 前台可交互时标志位置true，调用update方法更新构建参数
          this.shown = true;
          this.contentNode.update(new Params(this.shown));
          console.info('this.shown is false');
        } else if (windowEvent === 6) {
          // 前台不可交互时标志位置false，调用update方法更新构建参数
          this.shown = false;
          this.contentNode.update(new Params(this.shown));
          console.info('this.shown is true');
        }
        console.info(`Window event happened.  Event: ${windowEvent}`);
      });
  }

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(30)
          .fontColor(Color.White)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 拉起弹窗
            let uiContext = this.getUIContext();
            let PromptAction = uiContext.getPromptAction();
            let contentNode =
              new ComponentContent(uiContext, wrapBuilder(customDialogComponent), new Params(this.shown));
            this.contentNode = contentNode;
            PromptAction.openCustomDialog(this.contentNode).catch(() => {
              console.info('Failed to show the CustomDialog !!!');
            });
          });
      }
      .width('100%')
      .height('50%');
    }
    .height('100%')
    .backgroundImageSize({ width: 600, height: 800 })
    .foregroundBlurStyle(BlurStyle.Thin, { scale: this.shown ? 0 : 1 });
  }
}
```
