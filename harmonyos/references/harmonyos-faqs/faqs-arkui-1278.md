---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1278
title: 如何实现Tabs自定义页签的下划线与文字内容宽度一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Tabs自定义页签的下划线与文字内容宽度一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:52cf348bdf45257737ffb21acbe0cb4f4376d228715af19adabd2f41698ce4cc
---

## 问题现象

存在多个自定义页签，且每个页签下方都有下划线，如何控制页签的下划线与其文字内容的宽度保持一致？

页签文字短：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/1gBT7PzjTWOQffBtHtdehw/zh-cn_image_0000002658957167.png "点击放大")

页签文字长：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/u_xD8LliRGKJDmz4hNMb0Q/zh-cn_image_0000002658837237.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/69qrw25fQZSOhqhL8F4zaQ/zh-cn_image_0000002628597972.gif "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)是通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。不支持自定义组件作为子组件，仅可包含子组件[TabContent](../harmonyos-references/ts-container-tabcontent.md)。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)在组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 解决方案

1. 通过点击事件，标记当前焦点所在的页面。

   ```screen
   ListItem() {
     Column() {
       Text((item == 2) ? '页签222222' : ('页签' + item))
         .fontWeight(index === this.focusIndex ? FontWeight.Bold : FontWeight.Normal)
         .onAreaChange((newValue: Area) => {
           if (index === this.focusIndex) {
             this.sizeValue = newValue.width;
           }
         });

       if (index === this.focusIndex) {
         Column().width(this.sizeValue).height(2).backgroundColor(Color.Gray);
       }
     };
   }
   .borderRadius(10).backgroundColor(0xFFFFFF)
   .height(50)
   .onClick(() => {
     this.controller.changeIndex(index);
     this.focusIndex = index;
     this.scrollerForList.scrollToIndex(index, true, ScrollAlign.CENTER);
   });
   ```
2. 通过onAreaChange组件区域变化事件获取当前Text组件的宽度。

   ```screen
   Text((item == 2) ? '页签222222' : ('页签' + item))
     .fontWeight(index === this.focusIndex ? FontWeight.Bold : FontWeight.Normal)
     .onAreaChange((newValue: Area) => {
       if (index === this.focusIndex) {
         this.sizeValue = newValue.width;
       }
     });
   ```
3. 将宽度赋值给下划线，从而实现下划线与文字内容保持一致。

   ```screen
   if (index === this.focusIndex) {
     Column().width(this.sizeValue).height(2).backgroundColor(Color.Gray);
   }
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct TabsExample {
  @State tabArray: number[] = [0, 1, 2, 3, 4];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();
  private scrollerForList: Scroller = new Scroller();
  @State sizeValue: Length = 0;

  build() {
    Column() {
      // 使用自定义页签组件
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        ForEach(this.tabArray, (index: number, item: number) => {
          ListItem() {
            Column() {
              Text((item == 2) ? '页签222222' : ('页签' + item))
                .fontWeight(index === this.focusIndex ? FontWeight.Bold : FontWeight.Normal)
                .onAreaChange((newValue: Area) => {
                  if (index === this.focusIndex) {
                    this.sizeValue = newValue.width;
                  }
                });

              if (index === this.focusIndex) {
                Column().width(this.sizeValue).height(2).backgroundColor(Color.Gray);
              }
            };
          }
          .borderRadius(10).backgroundColor(0xFFFFFF)
          .height(50)
          .onClick(() => {
            this.controller.changeIndex(index);
            this.focusIndex = index;
            this.scrollerForList.scrollToIndex(index, true, ScrollAlign.CENTER);
          });

        }, (item: number) => JSON.stringify(item));
      }
      .chainAnimation(true)
      .edgeEffect(EdgeEffect.Spring)
      .listDirection(Axis.Horizontal)
      .height('50')
      .width('100%')
      .scrollBar(0);

      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
        ForEach(this.tabArray, (item: number) => {
          TabContent() {
            Text('我是页面 ' + item + ' 的内容')
              .fontSize(30);
          };
        });
      }.barHeight(0)
      .onChange((index: number) => {
        // currentIndex控制TabContent显示页签
        this.focusIndex = index;
        this.scrollerForList.scrollToIndex(index, true, ScrollAlign.CENTER);
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
