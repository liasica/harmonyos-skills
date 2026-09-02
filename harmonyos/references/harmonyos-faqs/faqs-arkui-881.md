---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-881
title: 快速滑动页面时，顶部区域颜色渐变异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 快速滑动页面时，顶部区域颜色渐变异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc0cfcf2f25c400882b6da87abc28ec9cbfac41cd3bc9209d7618787ac7c75d9
---

## 问题现象

对页面可滚动区域进行上拉操作时，顶部固定区域从透明色平滑渐变为白色，但下拉回弹操作时，顶部区域有概率出现以下异常：

* 颜色卡在半透明色，视觉上颜色断层。
* 渐变延迟（约1秒后才恢复）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ogxggTAwTUKslAkDOiLD3A/zh-cn_image_0000002658918851.png "点击放大")

## 背景知识

* [onWillScroll](../harmonyos-references/ts-container-scroll.md#onwillscroll12)为滚动事件回调，Scroll滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。
* [onDidScroll](../harmonyos-references/ts-container-scroll.md#ondidscroll12)为滚动事件回调，Scroll滚动时触发。返回当前帧滚动的偏移量和当前滚动状态。
* 滚动事件的回调函数在滚动过程中会被频繁触发，因此应避免在该回调函数中执行耗时操作，以防止应用出现卡顿和丢帧的问题。具体内容请参考[主线程耗时操作优化指导-高频回调场景](../best-practices/bpta-time-optimization-of-the-main-thread.md#section10112623611)。

## 问题定位

1. 使用DevEco Testing-实用工具-UIViewer查看布局实现，确认滚动页面基于Scroll组件实现。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/sNmOisjmTIaCmOnhD4uRwA/zh-cn_image_0000002628399636.png "点击放大")
2. 排查代码中关于顶部固定区域透明度变化的相关事件是否在onWillScroll回调函数中执行。

   ```screen
   class Item {
     text: string = '';
     color: string = '';

     constructor(text: string) {
       this.text = text;
     }
   }

   @Entry
   @Component
   struct StackDemo {
     private items: Item[] = [
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello'),
       new Item('hello')
     ];
     private scroller: Scroller = new Scroller();
     private topHeight: number = 88;
     @State private percentage: number = 0.0;
     @StorageLink('statusBarHeight') statusBarHeight: number = 0;

     @Builder
     textLine(text: string) {
       Column() {
         Text(text)
           .backgroundColor('#f1f3f5')
           .borderRadius(25)
           .padding({
             left: 155,
             right: 155,
             bottom: 25,
             top: 25
           });
       }
       .borderRadius(10)
       .width('100%')
       .height('10%');

     }

     build() {
       NavDestination() {
         Stack() {
           Row() {
             Text('顶部区域')
               .fontSize(24)
               .height(56)
               .padding({ left: 24, bottom: 25 })
               .width('100%')
               .textAlign(TextAlign.Start);
           }
           .width('100%')
           .height(this.topHeight)
           .backgroundColor('rgba(255, 255, 255,' + this.percentage + ')')
           .zIndex(1)
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);

           Scroll(this.scroller) {
             Column() {

               Image($r('app.media.top_picture'))
                 .width('100%')
                 .objectFit(ImageFit.Fill)
                 .padding({ bottom: 25 })
                 .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);

               ForEach(this.items, (item: Item) => {
                 this.textLine(item.text);
               });
             };
           }
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
           .zIndex(0)
           .scrollBar(BarState.Off)
           .onWillScroll(() => {
             let yOffset = this.scroller.currentOffset().yOffset;
             console.info('yOffset=%f, statusBarHeight=%f', yOffset, this.statusBarHeight);
             let res = parseFloat((yOffset / this.topHeight).toFixed(1));
             res = Math.max(0, Math.min(1, res));
             this.percentage = res;
           });
         }
         .height('100%')
         .width('100%')
         .alignContent(Alignment.TopStart);
       }
       .hideTitleBar(true);
     }
   }

   @Builder
   export function StackDemoBuilder() {
     StackDemo();
   }
   ```

## 分析结论

顶部固定区域透明度变化相关事件在onWillScroll回调函数中执行，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移，因此在滑动时可能会导致偏移量无法及时更新，顶部区域透明度随之无法更新。

## 修改建议

建议将顶部固定区域透明度变化相关事件在onDidScroll回调函数中执行。

实现代码如下：

```screen
class Item {
  text: string = '';
  color: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

@Entry
@Component
struct StackDemo {
  private items: Item[] = [
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello'),
    new Item('hello')
  ];
  private scroller: Scroller = new Scroller();
  private topHeight: number = 88;
  @State private percentage: number = 0.0;
  @StorageLink('statusBarHeight') statusBarHeight: number = 0;

  @Builder
  textLine(text: string) {
    Column() {
      Text(text)
        .backgroundColor('#f1f3f5')
        .borderRadius(25)
        .padding({
          left: 155,
          right: 155,
          bottom: 25,
          top: 25
        });
    }
    .borderRadius(10)
    .width('100%')
    .height('10%');

  }

  build() {
    NavDestination() {
      Stack() {
        Row() {
          Text('顶部区域')
            .fontSize(24)
            .height(56)
            .padding({ left: 24, bottom: 25 })
            .width('100%')
            .textAlign(TextAlign.Start);
        }
        .width('100%')
        .height(this.topHeight)
        .backgroundColor('rgba(255, 255, 255,' + this.percentage + ')')
        .zIndex(1)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);

        Scroll(this.scroller) {
          Column() {

            Image($r('app.media.top_picture'))
              .width('100%')
              .objectFit(ImageFit.Fill)
              .padding({ bottom: 25 })
              .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);

            ForEach(this.items, (item: Item) => {
              this.textLine(item.text);
            });
          };
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .zIndex(0)
        .scrollBar(BarState.Off)
        .onDidScroll(() => {
          let yOffset = this.scroller.currentOffset().yOffset;
          console.info('yOffset=%f, statusBarHeight=%f', yOffset, this.statusBarHeight);
          let res = parseFloat((yOffset / this.topHeight).toFixed(1));
          res = Math.max(0, Math.min(1, res));
          this.percentage = res;
        });
      }
      .height('100%')
      .width('100%')
      .alignContent(Alignment.TopStart);
    }
    .hideTitleBar(true);
  }
}

@Builder
export function StackDemoBuilder() {
  StackDemo();
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/8UtGeeOwQL--DZjIGXpaDQ/zh-cn_image_0000002658798903.png "点击放大")
