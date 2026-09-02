---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-12
title: 应用在平板设备竖屏时，界面下方有留白且文字溢出界面
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 应用在平板设备竖屏时，界面下方有留白且文字溢出界面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8fb2eb7f00991acedfd0a988b6c68bef01c8dbccff961579f4ffb4e880aaba64
---

## 问题现象

平板竖屏状态打开应用，界面下方大面积留白，应用内容未铺满界面，同时文字显示有溢出界面，显示不全的问题。

## 背景知识

* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口尺寸大小变化的监听，再根据窗口的尺寸变化，更新调整自身应用布局以实现适配。
* [Scroll](../harmonyos-references/ts-container-scroll.md)是可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。因此在页面局部展示区域固定的情况下，可以使用Scroll组件来显示超过Scroll尺寸的子组件内容。

## 问题定位

1. 应用中搜索windowSizeChange查看应用是否开启窗口尺寸变化的监听。
2. 排查相关页面的代码，水平方向组件的宽度之和是否超出平板竖屏时的屏幕宽度，示例如下：

   ```ts
   let displayClass: display.Display | null = null;
   displayClass = display.getDefaultDisplaySync();
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

1. 未监听'windowSizeChange'事件，并且动态调整布局，导致竖屏时应用页面下方留白，未铺满整个页面。
2. 页面上组件水平方向的总宽度超过了屏幕宽度，导致水平方向页面显示不全，文字溢出了界面。

## 修改建议

1. 通过监听'windowSizeChange'事件，获取窗口尺寸变化，动态调整页面布局，避免出现大面积留白。

   ```ts
   windowStage.getMainWindow().then((windowClass) => {
     AppStorage.setOrCreate('winWidth', windowClass.getWindowProperties().windowRect.width);
     AppStorage.setOrCreate('winHeight', windowClass.getWindowProperties().windowRect.height);
     windowClass.on('windowSizeChange', (windowSize) => {
       AppStorage.setOrCreate('winWidth', windowSize.width);
       AppStorage.setOrCreate('winHeight', windowSize.height);
     });
   });
   ```
2. 在页面组件总宽度超过屏幕的总宽度时，可以在部分组件外包一层Scroll组件，通过滚动的方式在有限的区域显示更多的内容，避免出现文字溢出界面的问题。

   ```ts
   @Entry
   @Component
   struct Index {
     @StorageLink('winWidth') winWidth: number = 1080;
     @StorageLink('winHeight') winHeight: number = 1960;

     aboutToAppear() {
       console.info(`Current window size. width: ${this.winWidth}, height: ${this.winHeight}`);
     }

     build() {
       Row() {
         // 此处无论Scroll子组件Text的宽度有多宽，均可通过横向滑动展示
         Scroll() {
           Row() {
             Text('hello')
               .width('150vp')
               .fontSize(50);
             Text('world')
               .width('300vp')
               .fontSize(50);
             Text('你好')
               .width('500vp')
               .fontSize(50);
             Text('世界')
               .width('1000vp')
               .fontSize(50);
           }
           .margin({ bottom: 8 });
         }
         // 设置滚动方向为水平方向
         .scrollable(ScrollDirection.Horizontal);
       }
       .size({
         width: this.getUIContext().px2vp(this.winWidth),
         height: this.getUIContext().px2vp(this.winHeight)
       });
     }
   }
   ```
