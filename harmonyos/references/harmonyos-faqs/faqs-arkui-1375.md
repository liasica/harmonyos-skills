---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1375
title: 如何同时绑定全模态和半模态转场
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何同时绑定全模态和半模态转场
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f57413b99a156659aeada8a8c569f22d1422739b88b2747fab2210f8bdae54a0
---

## 问题现象

* 在同一个组件上用bindContentCover和bindSheet绑定全模态和半模态转场，在状态没有冲突的情况下全模态不会生效或者转场逻辑会出现混乱。
* 按照目前的规格，在同一个组件下同时绑定这两个转场，半模态可以生效但全模态不会生效或者效果不会符合预期；如下用例，这样直接绑定效果会有错乱：

```ts
Row()
  .bindSheet(this.isShowSheet, this.mySheet(), {
    height: 300,
    dragBar: false,
    onDisappear: () => {
      this.isShowSheet = false;
    }
  })
  .bindContentCover(this.isPresent, this.MyBuilder(), {
    modalTransition: ModalTransition.DEFAULT,
    onDisappear: () => {
      this.isPresent = false;
    }
  })
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/muX9DIziT5-FaOns9N9IyA/zh-cn_image_0000002628761926.png "点击放大")

## 背景知识

* [全模态转场bindContentCover](../harmonyos-guides/arkts-modal-transition.md#使用bindcontentcover构建全屏模态转场效果)：为组件绑定全屏模态页面，在组件出现和消失时可通过设置转场参数ModalTransition添加过渡动效。
* [半模态转场bindSheet](../harmonyos-guides/arkts-modal-transition.md#使用bindsheet构建半模态转场效果)：为组件绑定半模态页面，在组件出现时可通过设置自定义或默认的内置高度确定半模态大小。

## 解决方案

可以在需要绑定的组件上再套上一层组件，然后在内外组件绑定不同的模态转场。完整示例代码如下：

```ts
import { curves } from '@kit.ArkUI';

interface PersonList {
  name: string,
  cardnum: string
}
 
@Entry
@Component
struct BindContentCoverDemo {
  private personList: Array<PersonList> = [
    { name: '王**', cardnum: '1234***********789' },
    { name: '宋*', cardnum: '2345***********789' },
    { name: '许**', cardnum: '3456***********789' },
    { name: '唐*', cardnum: '4567***********789' }
  ];
  @State isShowSheet: boolean = false;
  private menuList: string[] = ['广州南', '虎门站', '深圳北站', '佛山站', '东莞南站', '贵阳北站', '北京西站'];
  // 第一步：定义全屏模态转场效果bindContentCover
  // 模态转场控制变量
  @State isPresent: boolean = false;

  // 第二步：定义模态展示界面
  // 通过@Builder构建模态展示界面
  @Builder
  MyBuilder() {
    Column() {
      Row() {
        Text('选择乘车人')
          .fontSize(20)
          .fontColor(Color.White)
          .width('100%')
          .textAlign(TextAlign.Center)
          .padding({ top: 30, bottom: 15 })
          .margin({ top: 30 })
      }
      .backgroundColor(0x007dfe)

      Row() {
        Text('+ 添加乘车人')
          .fontSize(16)
          .fontColor(0x333333)
          .margin({ top: 10 })
          .padding({ top: 20, bottom: 20 })
          .width('92%')
          .borderRadius(10)
          .textAlign(TextAlign.Center)
          .backgroundColor(Color.White)
      }

      Column() {
        ForEach(this.personList, (item: PersonList, index: number) => {
          Row() {
            Column() {
              if (index % 2 == 0) {
                Column()
                  .width(20)
                  .height(20)
                  .border({ width: 1, color: 0x007dfe })
                  .backgroundColor('#007dfe')
              } else {
                Column()
                  .width(20)
                  .height(20)
                  .border({ width: 1, color: 0x007dfe })
              }
            }
            .width('20%')

            Column() {
              Text(item.name)
                .fontColor(0x333333)
                .fontSize(18)
              Text(item.cardnum)
                .fontColor(0x666666)
                .fontSize(14)
            }
            .width('60%')
            .alignItems(HorizontalAlign.Start)

            Column() {
              Text('编辑')
                .fontColor(0x007dfe)
                .fontSize(16)
            }
            .width('20%')
          }
          .padding({ top: 10, bottom: 10 })
          .border({ width: { bottom: 1 }, color: 0xf1f1f1 })
          .width('92%')
          .backgroundColor(Color.White)
        })
      }
      .padding({ top: 20, bottom: 20 })

      Text('确认')
        .width('90%')
        .height(40)
        .textAlign(TextAlign.Center)
        .borderRadius(10)
        .fontColor(Color.White)
        .backgroundColor(0x007dfe)
        .onClick(() => {
          this.isPresent = false;
        })
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor(0xf5f5f5)
    // 通过转场动画实现出现消失转场动画效果
    .transition(TransitionEffect.translate({ y: 100 }).animation({ curve: curves.springMotion(0.6, 0.8) }))
  }

  @Builder
  mySheet() {
    Column() {
      Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
        ForEach(this.menuList, (item: string) => {
          Text(item)
            .fontSize(16)
            .fontColor(0x333333)
            .backgroundColor(0xf1f1f1)
            .borderRadius(8)
            .margin(10)
            .padding(10)
        })
      }
      .padding({ top: 18 })
      .margin({ top: 30 })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
    .transition(TransitionEffect.translate({ y: 100 }).animation({ curve: curves.springMotion(0.6, 0.8) }))
  }

  build() {
    Column() {
      Row() {
        Text('确认订单')
          .fontSize(20)
          .fontColor(Color.White)
          .width('100%')
          .textAlign(TextAlign.Center)
          .padding({ top: 30, bottom: 60 })
      }
      .backgroundColor(0x007dfe)

      Column() {
        Row() {
          Column() {
            Text('00:25')
            Text('始发站')
          }
          .width('30%')

          Column() {
            Text('G1234')
            Text('8时1分')
          }
          .width('30%')

          Column() {
            Text('08:26')
            Text('终点站')
          }
          .width('30%')
        }
      }
      .width('92%')
      .padding(15)
      .margin({ top: -30 })
      .backgroundColor(Color.White)
      .shadow({ radius: 30, color: '#aaaaaa' })
      .borderRadius(10)

      Column() {
        Text('+ 选择出发站')
          .fontSize(18)
          .fontColor(Color.Orange)
          .fontWeight(FontWeight.Bold)
          .padding({ top: 10, bottom: 10 })
          .width('60%')
          .textAlign(TextAlign.Center)
          .borderRadius(15)
          .onClick(() => {
            this.isShowSheet = true;
          })
          .margin({ bottom: '10%' })
        Text('+ 选择乘车人')
          .fontSize(18)
          .fontColor(Color.Orange)
          .fontWeight(FontWeight.Bold)
          .padding({ top: 10, bottom: 10 })
          .width('60%')
          .textAlign(TextAlign.Center)
          .borderRadius(15) // 通过选定的模态接口，绑定模态展示界面，ModalTransition是内置的ContentCover转场动画类型，这里选择DEFAULT代表设置上下切换动画效果，通过onDisappear控制状态变量变换。

          .onClick(() => {
            // 第三步：通过模态接口调起模态展示界面，通过转场动画或者共享元素动画去实现对应的动画效果
            // 改变状态变量，显示模态界面
            this.isPresent = true;
          })
        Row() {
          Row()
            .bindSheet(this.isShowSheet, this.mySheet(), {
              height: 300,
              dragBar: false,
              onDisappear: () => {
                this.isShowSheet = false;
              }
            })
        }
        .bindContentCover(this.isPresent, this.MyBuilder(), {
          modalTransition: ModalTransition.DEFAULT,
          onDisappear: () => {
            this.isPresent = false;
          }
        })
      }
      .padding({ top: 60 })
    }
  }
}
```
