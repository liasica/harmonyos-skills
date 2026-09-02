---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1068
title: 使用状态管理V1、V2进行深度观测的区别和优缺点
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用状态管理V1、V2进行深度观测的区别和优缺点
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dde718bb7a5de3528423c1178b54029f72cac470784cf7a6f67849b057c930eb
---

## 问题现象

当声明的状态变量是复杂的嵌套对象时，V1，V2版本如何分别实现深层属性监听，应该分别注意哪些事项？

## 背景知识

* 在状态管理V1版本中：

  [@State](../harmonyos-guides/arkts-state.md)、[@Prop](../harmonyos-guides/arkts-prop.md)、[@Link](../harmonyos-guides/arkts-link.md)、[@Provide和@Consume](../harmonyos-guides/arkts-provide-and-consume.md)装饰器仅能观察到本身及对象第一层属性的变化，但是在实际应用开发中，应用会根据开发需要，封装自己的数据模型。对于多层嵌套的情况，比如二维数组，或者对象数组等。若仅仅使用上述的装饰器，无法实现嵌套对象的深层属性的监听。此时需要使用[@Observed和@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)实现嵌套数据的深层观测。
* 在状态管理V2版本中：

  [@Local](../harmonyos-guides/arkts-new-local.md)，[@Param](../harmonyos-guides/arkts-new-param.md)，[@Provider和@Consumer](../harmonyos-guides/arkts-new-provider-and-consumer.md)仅能观察到变量本身的变化，取消了对象第一层属性观察的能力，若需要观察对象属性的变化或更深层次的属性变化，需要搭配[@ObservedV2和@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)使用。

## 解决方案

V1版本的复杂嵌套数据的深层嵌套观测相较于V2版本的深层嵌套观测存在一定的局限性，为尽可能的体现深层嵌套的场景，以下示例方案的数据类型采用双层对象数组：

* 方案一：通过@Observed/@ObjectLink实现双层对象数组的UI刷新。
  1. @Observed/@ObjectLink每需要观测一个对象内的属性变化，都需要创建一个子组件并用@ObjectLink接收该对象，才能实现深度观测。
  2. 所以若需要观测双层对象数组，需要分别创建两个嵌套的子组件，分别用@ObjectLink接收对应数组的对象。
  3. 创建的对象通过new操作符创建，实现状态变量代理。

     完整示例代码如下：

     ```ts
     // 第二层最基础的信息类
     @Observed
     class SecondItem {
       id?: number;
       text?: string;

       constructor(id: number, text: string) {
         this.id = id;
         this.text = text;
       }
     }

     // 第一层信息类
     @Observed
     class FirstItem {
       id?: number;
       text?: string;
       // 第一层基础信息的数组
       itemList?: Array<SecondItem>;

       constructor(id: number, text: string, itemList: Array<SecondItem>) {
         this.id = id;
         this.text = text;
         this.itemList = itemList;
       }
     }

     // 第二层UI组件
     @Component
     struct SecondComponent {
       @ObjectLink secondItem: SecondItem;

       build() {
         Column({ space: 10 }) {
           Column({ space: 10 }) {
             Text(`id:${this.secondItem.id}, text: ${this.secondItem.text}`).fontSize(20).textAlign(TextAlign.Center);
             Button('修改第二层子组件对应的第二层对象属性')
               .onClick(() => {
                 this.secondItem.text += '+2';
               });
           }.width('100%').justifyContent(FlexAlign.Center);
         }
         .padding({ top: 10, bottom: 10 })
         .width('100%')
         .justifyContent(FlexAlign.Center)
         .backgroundColor('#F1F3F5')
         .borderRadius(15);
       }
     }

     @Component
     struct FirstComponent {
       @ObjectLink firstItem: FirstItem;

       build() {
         Column({ space: 10 }) {
           Row() {
             Text(`id:${this.firstItem.id}, text: ${this.firstItem.text}`).fontSize(20).textAlign(TextAlign.Center);
           }.width('100%').justifyContent(FlexAlign.SpaceBetween);

           Row() {
             List({ space: 10 }) {
               ForEach(this.firstItem.itemList, (item: SecondItem) => {
                 ListItem() {
                   Column() {
                     SecondComponent({
                       secondItem: item
                     });
                   };
                 };
               });
             };
           }.width('100%');

           Button('修改第一层子组件对应的第一层对象属性')
             .onClick(() => {
               this.firstItem.text += '+1';
             });
         }
         .padding(10)
         .backgroundColor(Color.White)
         .width('100%')
         .borderRadius(15);
       }
     }

     @Entry
     @Component
     struct OptionOne {
       // 二维对象数组
       @State itemInfos: FirstItem[] = [
         new FirstItem(1, `firstItem1`, [new SecondItem(10, `secondItem1`), new SecondItem(11, `secondItem2`)]),
         new FirstItem(2, `firstItem2`, [new SecondItem(13, `secondItem3`), new SecondItem(14, `secondItem4`)])
       ];

       build() {
         Column() {
           Row() {
             List({ space: 10 }) {
               ForEach(this.itemInfos, (item: FirstItem) => {
                 ListItem() {
                   FirstComponent({
                     firstItem: item
                   });
                 };
               });
             };
           }.width('90%').justifyContent(FlexAlign.SpaceBetween);

           Column() {
             Button('父组件，改变数组[0][1]的text值')
               .onClick(() => {
                 this.itemInfos[0].itemList![1].text = new Date().toString();
               });
             Divider().height(10);
             Button('父组件，改变数组[1][0]的text值')
               .onClick(() => {
                 this.itemInfos[1].itemList![0].text = new Date().toString();
               });
           }.margin({ top: 50 }).width('90%').justifyContent(FlexAlign.SpaceBetween);
         }.width('100%').justifyContent(FlexAlign.Center);
       }
     }
     ```

     实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/sUMu7wd2RqmZBqqQfy_PGw/zh-cn_image_0000002628407224.png "点击放大")

     **说明** 

     @Observed/@ObjectLink可以实现父组件修改深层属性后，刷新子组件对应属性绑定的UI的功能，但是当子组件内修改深层属性，父组件并不会刷新对应属性绑定的UI。比如上述代码中，给父组件“OptionOne”增加一段绑定深层属性的UI代码：

     ```ts
     Text(`父组件绑定数组[0][1]的text是否刷新：${this.itemInfos[0].itemList![1].text}`);
     ```

     发现无论是在子组件中修改对应的属性，还是在父组件中修改this.itemInfos[0].itemList![1].text，都不会刷新父组件的UI。

* 方案二：通过@ObservedV2和@Trace实现双层对象数组的UI刷新。
  1. @ObservedV2和@Trace无需通过逐层封装子组件接收对应层级的嵌套对象，只需要采用@ObservedV2装饰对应的类，以及@Trace装饰要观测的类的属性即可。
  2. 创建的对象通过new操作符创建，实现状态变量代理。

     完整示例代码如下：

     ```ts
     // 第二层最基础的信息类
     @ObservedV2
     class SecondItemTwo {
       id?: number;
       @Trace text?: string;

       constructor(id: number, text: string) {
         this.id = id;
         this.text = text;
       }
     }

     // 第一层信息类
     @ObservedV2
     class FirstItemTwo {
       id?: number;
       @Trace text?: string;
       // 第一层基础信息的数组
       @Trace itemList?: Array<SecondItemTwo>;

       constructor(id: number, text: string, itemList: Array<SecondItemTwo>) {
         this.id = id;
         this.text = text;
         this.itemList = itemList;
       }
     }

     @Entry
     @ComponentV2
     struct OptionTwo {
       // 二维对象数组
       @Local itemInfos: FirstItemTwo[] = [
         new FirstItemTwo(1, `firstItem1`, [new SecondItemTwo(10, `secondItem1`), new SecondItemTwo(11, `secondItem2`)]),
         new FirstItemTwo(2, `firstItem2`, [new SecondItemTwo(13, `secondItem3`), new SecondItemTwo(14, `secondItem4`)])
       ];

       build() {
         Column() {
           Row() {
             List({ space: 10 }) {
               ForEach(this.itemInfos, (firstItem: FirstItemTwo) => {
                 ListItem() {
                   Column({ space: 10 }) {
                     Row() {
                       Text(`id:${firstItem.id}, text: ${firstItem.text}`).fontSize(20).textAlign(TextAlign.Center);
                     }.width('100%').justifyContent(FlexAlign.SpaceBetween);

                     Row() {
                       List({ space: 10 }) {
                         ForEach(firstItem.itemList, (secondItem: SecondItemTwo) => {
                           ListItem() {
                             Column({ space: 10 }) {
                               Text(`id:${secondItem.id}, text: ${secondItem.text}`)
                                 .fontSize(20)
                                 .textAlign(TextAlign.Center);
                               Button('修改第二层子组件对应的第二层对象属性')
                                 .onClick(() => {
                                   secondItem.text += '+2';
                                 });
                             }
                             .padding({ top: 10, bottom: 10 })
                             .width('100%')
                             .justifyContent(FlexAlign.Center)
                             .backgroundColor('#F1F3F5')
                             .borderRadius(15);
                           };
                         });
                       };
                     }.width('100%');

                     Button('修改第一层子组件对应的第一层对象属性')
                       .onClick(() => {
                         firstItem.text += '+1';
                       });
                   }
                   .padding(10)
                   .backgroundColor(Color.White)
                   .width('100%')
                   .borderRadius(15);
                 };
               });
             };
           }.width('90%').justifyContent(FlexAlign.SpaceBetween);

           Column() {
             Text(`父组件绑定数组[0][1]的text是否刷新：${this.itemInfos[0].itemList![1].text}`)
               .margin({ bottom: 10 });
             Button('父组件，改变数组[0][1]的text值')
               .onClick(() => {
                 this.itemInfos[0].itemList![1].text = new Date().toString();
               });
             Divider().height(10);
             Button('父组件，改变数组[1][0]的text值')
               .onClick(() => {
                 this.itemInfos[1].itemList![0].text = new Date().toString();
               });
           }
           .width('90%')
           .justifyContent(FlexAlign.SpaceBetween);
         }.width('100%').justifyContent(FlexAlign.Center);
       }
     }
     ```

     实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/3dAcdnUUSZqchtfYwNRToQ/zh-cn_image_0000002658806487.png "点击放大")

     **说明** 

     与方案一不同，方案二没有“子组件内修改深层属性，父组件并不会刷新对应属性绑定的UI”的局限性。

## 常见FAQ

Q：嵌套过深是否会影响性能？

A：建议不超过三层嵌套。

Q：如何实现深层嵌套观测Map、Set类型数据？

A：状态管理V1版本可参考官方文档：[继承Map类](../harmonyos-guides/arkts-observed-and-objectlink.md#继承map类)、[继承Set类](../harmonyos-guides/arkts-observed-and-objectlink.md#继承set类)，状态管理V2版本可参考官方文档：[@Trace装饰Map类型](../harmonyos-guides/arkts-new-observedv2-and-trace.md#trace装饰map类型)、[@Trace装饰Set类型](../harmonyos-guides/arkts-new-observedv2-and-trace.md#trace装饰set类型)。

Q：上述方案二并没有封装子组件，若存在封装子组件的过程，应该如何实现嵌套数据的双向传递与共享，传递的数据应该用什么接收？

A：若是不传参的方式，可以使用@Provider和@Consumer装饰器通过key进行传递与接收。若是只需要传递嵌套数据的某一个对象给子组件，可以直接使用@Param接收。若@Param接收的是对象，且对象数据修改的属性在V2版本中被@Trace装饰，修改该属性时不需要通过@Event回调也可刷新父组件绑定的对应属性的UI，只有替换对象本身或者简单数据类型（number、string等）需要使用[@Event](../harmonyos-guides/arkts-new-event.md)在父组件修改，做到规范组件的输出。

## 总结

| 方案 | 性能 | 易用性 | 适用场景 |
| --- | --- | --- | --- |
| @Observed和@ObjectLink | 1. 整个对象的属性都刷新，即使只有部分属性发生了变化，也会导致不必要的渲染和性能开销。2. 若需要针对某个属性的刷新，需要搭配@Track使用。 | 1. 每层对象都需要封装一个子组件并且用@ObjectLink接收。导致需要更多的配置和额外的代码来实现类似的功能，使用起来相对复杂。2. 父组件里修改属性可以刷新子组件，但是子组件里修改属性，无法刷新父组件。 | 项目数据结构简单，数据变化单一且嵌套不深的场景。 |
| @ObservedV2和@Trace | @Trace精准更新，只刷新与变化属性相关的组件，避免了对未变化属性的重复渲染，可以提高性能，减少资源浪费。 | 更容易理解和掌握状态管理的逻辑，减少了代码的复杂性。相较于状态管理V1版本，能更自由的封装子组件而不必考虑@ObjectLink接收的问题。 | 复杂的数据模型，包含多个子对象和深层次的属性，以及大量的组件交互。 |
