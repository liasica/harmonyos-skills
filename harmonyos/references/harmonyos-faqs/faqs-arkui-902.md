---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-902
title: wrapBuilder函数内部状态无法刷新问题怎么处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > wrapBuilder函数内部状态无法刷新问题怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4268e94192a0e1812c4460015cb1c15ef53af9cd184f4354fc423e01f65d64c2
---

## 问题现象

传入wrapBuilder函数的参数变化时，没有引起内部UI的刷新，如何实现Builder内部UI刷新？

## 背景知识

* Builder函数：ArkUI提供了一种轻量的UI元素复用机制@Builder，该自定义组件内部UI结构固定，仅与使用方进行数据传递，开发者可以将重复使用的UI元素抽象成一个方法，在build方法里调用。详见[@Builder装饰器：自定义构建函数](../harmonyos-guides/arkts-builder.md)。
* wrapBuilder函数：当@Builder方法赋值给变量或者数组后，赋值的变量或者数组在UI方法中无法使用。为了解决这一问题，引入wrapBuilder作为全局@Builder封装函数。wrapBuilder的参数返回WrappedBuilder对象，实现全局@Builder可以进行赋值和传递。详见[wrapBuilder：封装全局@Builder](../harmonyos-guides/arkts-wrapbuilder.md)。

全局@Builder作为wrapBuilder的参数返回WrappedBuilder对象，实现全局@Builder可以进行赋值和传递。但是它的传参存在限制条件，不满足会导致UI不刷新。详情请见官方文档：[Builder限制条件](../harmonyos-guides/arkts-builder.md#限制条件)。

## 解决方案

1. Builder只传一个参数时，按引用传递UI会刷新，按值传递UI不刷新。

   Builder代码示例如下：

   ```screen
   import { util } from '@kit.ArkTS';

   class Tmp {
     paramA1: string = '';
   }

   // 只设置一个参数
   @Builder
   function test(param: Tmp) {
     Column() {
       HelloComponent({ message: param.paramA1 });
     };
   }

   // 只设置一个参数
   @Builder
   function test2(message: string) {
     Column() {
       HelloComponent({ message: message });
     };
   }

   @Component
   struct HelloComponent {
     @Prop message: string;

     build() {
       Column() {
         Text(this.message);
       };
     }
   }

   let globalBuilder2: WrappedBuilder<[string]> = wrapBuilder(test2);
   let globalBuilder: WrappedBuilder<[Tmp]> = wrapBuilder(test);
   ```

   组件代码示例如下：

   ```screen
   @Entry
   @Component
   struct WrappedBuilderDemoPage {
     @State message: string = 'message';

     build() {
       Row() {
         Column({ space: 10 }) {
           Button(`点击改变builder传值`).onClick(() => {
             this.message = util.generateRandomUUID();
           });
           Column() {
             Text('传递给Builder的参数');
             Text(this.message);
           }.width('100%')
           .alignItems(HorizontalAlign.Start);

           Text('按引用传递').width('100%').fontWeight(FontWeight.Bold).fontSize(20).margin({ top: 20 });
           Column() {
             Column() {
               Text('Builder呈现的').margin({ bottom: 10 });
               globalBuilder.builder({ paramA1: this.message }); // 引用传递
             }.alignItems(HorizontalAlign.Start);
           }
           .width('100%')
           .justifyContent(FlexAlign.Start)
           .alignItems(HorizontalAlign.Start);

           Text('按值传递').width('100%').fontWeight(FontWeight.Bold).fontSize(20).margin({ top: 20 });
           Column() {
             Column() {
               Text('Builder呈现的').margin({ bottom: 10 });
               globalBuilder2.builder(this.message); // 值传递
             }.alignItems(HorizontalAlign.Start);
           }
           .width('100%')
           .justifyContent(FlexAlign.Start)
           .alignItems(HorizontalAlign.Start);
         }
         .width('100%')
         .padding(20);
       }
       .height('100%');
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/VzIm6iSJT6Ci2sz6YHIwbA/zh-cn_image_0000002628399754.png "点击放大")
2. 当存在两个或两个以上的参数时，按值传递UI不会刷新。即使通过对象字面量形式传递，值的改变也不会触发UI刷新。所以通常将多个需要传递的参数封装成一个对象，同时保证只传递这一个对象，UI可正常刷新。

   Builder代码示例如下：

   ```screen
   import { util } from '@kit.ArkTS';

   interface HelloComponentParam {
     message: string;
     message2: string;
   }

   // 多个参数接收
   @Builder
   function test(message: string, message2: string) {
     HelloComponentTwo({
       param: { message: message, message2: message2 }
     });
   }

   // 一个参数接收
   @Builder
   function test2(param: HelloComponentParam) {
     HelloComponentTwo({
       param: { message: param.message, message2: param.message2 }
     });
   }

   @Component
   struct HelloComponentTwo {
     @Prop
     param: HelloComponentParam = {
       message: '',
       message2: ''
     };

     build() {
       Column() {
         Text(this.param.message);
         Text(this.param.message2);
       };
     }
   }

   let globalBuilder: WrappedBuilder<[string, string]> = wrapBuilder(test);
   let globalBuilder2: WrappedBuilder<[HelloComponentParam]> = wrapBuilder(test2);
   ```

   组件代码示例如下：

   ```screen
   @Entry
   @Component
   struct WrappedBuilderDemoPageTwo {
     @State param: HelloComponentParam = {
       message: 'message',
       message2: 'message',
     };

     build() {
       Row() {
         Column({ space: 10 }) {
           Button(`点击改变builder传值`).onClick(() => {
             this.param = {
               message: util.generateRandomUUID(),
               message2: util.generateRandomUUID()
             };
           });
           Column() {
             Text('传递给Builder的参数');
             Text(JSON.stringify(this.param));
           }.width('100%')
           .alignItems(HorizontalAlign.Start);

           Text('多个参数拆开传入').width('100%').fontWeight(FontWeight.Bold).fontSize(20).margin({ top: 20 });
           Column() {
             Column() {
               Text('Builder呈现的').margin({ bottom: 10 });
               globalBuilder.builder(this.param.message, this.param.message2);
             }.alignItems(HorizontalAlign.Start);
           }
           .width('100%')
           .justifyContent(FlexAlign.Start)
           .alignItems(HorizontalAlign.Start);

           Text('多个参数放在一个对象字面量内').width('100%').fontWeight(FontWeight.Bold).fontSize(20).margin({ top: 20 });
           Column() {
             Column() {
               Text('Builder呈现的').margin({ bottom: 10 });
               globalBuilder2.builder({ message: this.param.message, message2: this.param.message2 });
             }.alignItems(HorizontalAlign.Start);
           }
           .width('100%')
           .justifyContent(FlexAlign.Start)
           .alignItems(HorizontalAlign.Start);
         }
         .width('100%')
         .padding(20);
       }
       .height('100%');
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/S4MOkcjDRX67WbHl9PEZjA/zh-cn_image_0000002658799023.png "点击放大")
