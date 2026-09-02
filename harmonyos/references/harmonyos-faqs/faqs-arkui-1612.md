---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1612
title: 页面溢出显示区域，显示不全
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面溢出显示区域，显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:90cc91cd09c7807ed3fbf0ec996b4ffe93c5b5c08c20db79bc36bbd061892612
---

## 问题现象

打开应用，出现部分页面的内容区域超出屏幕，显示不全，被截断或看不见。

## 背景知识

* 组件[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)属性用于设置组件的外边距，top表示距上面组件的距离，bottom表示距下面组件的距离，left表示距左边组件的距离，right表示距右边组件的距离。页面开发时需要考虑组件间的距离，保证页面的正常显示。
* [Scroll](../harmonyos-references/ts-container-scroll.md)是可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。因此在页面局部展示区域固定的情况下，可以使用Scroll组件来显示超过Scroll尺寸的子组件内容。

## 问题定位

1. 查找设备屏幕的宽度和高度。

   ```ts
   import { display } from '@kit.ArkUI';

   // 获取设备屏幕的宽度和高度
   getScreenWH() {
     let displayClass: display.Display | null = null;
     displayClass = display.getDefaultDisplaySync();

     // 获取屏幕宽度,并转换成VP
     console.info(`The screen width is ${this.getUIContext().px2vp(displayClass.width)}vp.`);
     // 获取屏幕高度，并转换成VP
     console.info(`The screen height is ${this.getUIContext().px2vp(displayClass.height)}vp.`);
   }
   ```
2. 查阅代码中相关页面的代码，排查竖直方向已设定高度组件的高度之和（包含组件margin的top和bottom）是否超出平板横屏时的屏幕高度。

   ```ts
   // 例如此页面的总高度就是Text的高度200vp+Column的高度500vp=700vp
   build() {
     Column(){
       Text(this.message)
         .backgroundColor(Color.Gray)
         .height('200vp')
       Column(){

       }
       .backgroundColor(Color.Green)
       .height('500vp')
     }
   }
   ```
3. 查阅代码中相关页面的代码，排查水平方向已设定宽度组件的宽度之和（包含组件margin的left和right）是否超出平板横屏时的屏幕宽度。

   ```ts
   // 例如此页面的总宽度就是3个Row的宽度和，100vp+200vp+100vp=400vp
   build() {
     Column(){
       Row(){
         Row()
           .width('100vp')
         Row()
           .width('200vp')
         Row()
           .width('100vp')
       }
       Text(this.message)
         .backgroundColor(Color.Gray)
         .height('200vp')
       Column(){
       }
       .backgroundColor(Color.Green)
       .height('500vp')
     }
   }
   ```

## 分析结论

1. 页面竖直方向的总高度超过屏幕高度，导致竖直方向页面显示不全。
2. 页面水平方向的总宽度超过屏幕宽度，导致水平方向页面显示不全。

## 修改建议

针对页面总宽度或总高度超过屏幕的总宽度或总高度，可以在部分组件外包一层Scroll组件，通过滚动的方式在有限的界面区域显示出更多的内容。

竖直方向和水平方向显示不全后通过Scroll组件解决：

```ts
@Entry
@Component
struct ScrollDemo {
  build() {
    Column() {
      // 此处无论Scroll子组件Column组件高度有多高，显示区域均只占Scroll同级别组件高度的40%
      Scroll() {
        Column() {
          ForEach([0, 1, 2, 3, 4, 5], (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => `vertical${item}`)
        }
        .padding({ left: 16, right: 16 })
      }
      .height('40%')
      .backgroundColor(Color.Gray)

      // 此处无论Scroll子组件Text的宽度有多宽，均可通过横向滑动展示
      Scroll() {
        Row() {
          ForEach([0, 1, 2, 3, 4, 5], (item: number) => {
            Text(item.toString())
              .width('90%')
              .height('90%')
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ left: 10, top: 10 })
          }, (item: string) => `horizontal${item}`)
        }
        .justifyContent(FlexAlign.SpaceAround)
      }
      .height('40%')
      // 设置滚动方向为水平方向
      .scrollable(ScrollDirection.Horizontal)
      .backgroundColor(Color.Gray)
    }
    .justifyContent(FlexAlign.SpaceAround)
    .height('100%')
  }
}
```
