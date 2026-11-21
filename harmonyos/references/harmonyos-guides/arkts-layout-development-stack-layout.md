---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout
title: 层叠布局 (Stack)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 层叠布局 (Stack)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9c38ebfb661fbcea28d0e4a4a01eaf05183e6a6935d6eaab6a7ab8b9aed32981
---

## 概述

层叠布局（Stack）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](../harmonyos-references/ts-container-stack.md)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素的顺序为Item1->Item2->Item3。

**图1** 层叠布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/MzMkxBYHQeCzOdhuitMHjw/zh-cn_image_0000002793036468.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D641AAA084811A51257388E12EB29AA56F0B5B767C27DA3AC56B09E6C45EEF2)

**说明** 

过多的嵌套组件数会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠布局的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](../best-practices/bpta-component-nesting-optimization.md#section78181114123811)。

## 开发布局

Stack组件为容器组件，容器内可包含各种子元素。其中子元素默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

```typescript
// xxx.ets
let mTop:Record<string,number> = { 'top': 50 }

@Entry
@Component
struct StackLayoutExample {
  build() {
    Column(){
      Stack({ }) {
        Column(){}.width('90%').height('100%').backgroundColor('#ff58b87c')
        Text('text').width('60%').height('60%').backgroundColor('#ffc3f6aa')
        Button('button').width('30%').height('30%').backgroundColor('#ff8ff3eb').fontColor('#000')
      }.width('100%').height(150).margin(mTop)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/eGEKCbAeTLieihclFMlP8g/zh-cn_image_0000002792876500.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=C02CB8BCA9A5FF05CE9077BD393E18DA3A279F897DDB18D4AAC5B3758DA1CE7C)

## 对齐方式

Stack组件通过[alignContent参数](../harmonyos-references/ts-container-stack.md#aligncontent)实现位置的相对移动。如图2所示，支持九种对齐方式。

**图2** Stack容器内元素的对齐方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/jBWgtBfHRXCgnT--fm3Tbg/zh-cn_image_0000002821836405.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDB0641F569E53D4B0B7F716B4F676529FCA6BCAA51621FED877FEDBE4F524E5)

```typescript
// xxx.ets
@Entry
@Component
struct StackAlignContentExample {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Text('Stack').width('90%').height('100%').backgroundColor('#e1dede').align(Alignment.BottomEnd)
      Text('Item 1').width('70%').height('80%').backgroundColor(0xd2cab3).align(Alignment.BottomEnd)
      Text('Item 2').width('50%').height('60%').backgroundColor(0xc1cbac).align(Alignment.BottomEnd)
    }.width('100%').height(150).margin({ top: 5 })
  }
}
```

## Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](../harmonyos-references/ts-universal-attributes-z-order.md)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

```typescript
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    // 请将$r('app.string.stack_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
    Text($r('app.string.stack_num1')).textAlign(TextAlign.End).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306)

  Column() {
    // 请将$r('app.string.stack_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
    Text($r('app.string.stack_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink)

  Column() {
    // 请将$r('app.string.stack_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
    Text($r('app.string.stack_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/wF3SsBE2Qm6ytu_RzYhyNg/zh-cn_image_0000002821756407.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=73CBB2DADA19AE2FE506FE2A673064A0D45C25609F5BE633DA0BAD9CDB0A3BF8)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1、子元素2的zIndex属性后，可以将元素展示出来。

```typescript
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    // 请将$r('app.string.stack_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
    Text($r('app.string.stack_num1')).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)

  Column() {
    // 请将$r('app.string.stack_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
    Text($r('app.string.stack_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)

  Column() {
    // 请将$r('app.string.stack_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
    Text($r('app.string.stack_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Fxj5ndheRE62BSLDTVJLrA/zh-cn_image_0000002793036470.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=732A804D8DB4EA2B7A1EE1C63DD38C2CB37F07C5C81388A9E3A39A44EBC507A8)

## 场景示例

使用层叠布局快速搭建页面。

```typescript
@Entry
@Component
struct StackSample {
  private arr: string[] = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'];

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Flex({ wrap: FlexWrap.Wrap }) {
        ForEach(this.arr, (item:string) => {
          Text(item)
            .width(100)
            .height(100)
            .fontSize(16)
            .margin(10)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }, (item:string):string => item)
      }.width('100%').height('100%')

      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // 请将$r('app.string.contacts')替换为实际资源文件，在本示例中该资源文件的value值为"联系人"
        Text($r('app.string.contacts')).fontSize(16)
        // 请将$r('app.string.setting')替换为实际资源文件，在本示例中该资源文件的value值为"设置"
        Text($r('app.string.setting')).fontSize(16)
        // 请将$r('app.string.text_message')替换为实际资源文件，在本示例中该资源文件的value值为"短信"
        Text($r('app.string.text_message')).fontSize(16)
      }
      .width('50%')
      .height(50)
      .backgroundColor('#16302e2e')
      .margin({ bottom: 15 })
      .borderRadius(15)
    }.width('100%').height('100%').backgroundColor('#CFD0CF')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/SO9DGJwmSvCICAnkf-ZtvA/zh-cn_image_0000002792876502.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=745DBB35560C237A080DDAAD850B9AE319D323E859D768A9CC98B7A2BE0A52CE)

## 示例代码

* [组件堆叠](https://gitcode.com/HarmonyOS_Samples/component-stack)
