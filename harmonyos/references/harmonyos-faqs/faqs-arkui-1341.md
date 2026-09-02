---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1341
title: List组件分组滚动效果实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List组件分组滚动效果实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:73c45e4a14db65fc2908e789fc23e5bc84801e28d63cead558c727277a5bc12e
---

## 问题现象

实现一个多标签页切换功能的界面。所有的ListItem按标签分为三类，该界面的具体效果诉求如下：

1.响应滚动位置；例如，在资讯列表滚动时，如果滚动到第二个分类，则顶部分类标签栏也需要更新到对应的位置;

2.控制滚动位置；例如，点击标签，自动跳转到该标签对应分类中的第一个元素;

3.滑动后每个分类的末尾元素需要靠后对齐；例如，下图中的hotPage5是靠后对齐；

## 背景知识

* 状态管理：通过[@State](../harmonyos-guides/arkts-state.md)装饰器定义响应式状态变量，当这些变量的值发生变化时，会自动触发组件的重新渲染，实现数据与UI的同步更新。
* 组件使用：[List](../harmonyos-references/ts-container-list.md)组件用于展示列表数据，[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)循环用于遍历数组生成列表项，[scroller](../harmonyos-references/ts-container-scroll.md#scroller)属性关联滚动条，[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)回调函数用于监听列表滚动过程中的索引变化。
* 自定义方法：在组件中定义自定义方法（如tabBuilder、newsBuilder、calcNewsGroup、clickToNewsGroup），用于封装特定的业务逻辑，提高代码的可维护性和复用性。

## 解决方案

1.使用List组件的[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)获取到当前界面的子组件的标号（currentListIndex），根据子组件标号操作对应标签颜色变化，实现标签响应列表滚动位置的效果；

2.使用[onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)为组件添加点击事件，该事件发生后调用[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)滑动到指定Index，实现List组件跳转;

3.使用通用事件[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)识别抬手时，当前界面的子组件的标号（currentListIndex）是末尾元素时，调用[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)方法实现靠后对齐效果；

```ts
@Entry
@Component
struct TabsExample {
  private arr: number[] = [];
  private arrTitleBar: string[] = ['g1', 'g2', 'g3'];
  private arrTitleBarEx: string[] = ['c0-5', 'c6-10', 'c11-14'];
  private arrContent: string[] = ['content1: XXXXXXXXXXXXX', 'content2: XXXXXXXXXXXXX', 'content3: XXXXXXXXXXXXX'];
  private scrollerForList: Scroller = new Scroller();
  @State currentListIndex: number = 0;

  aboutToAppear() {
    for (let i = 0; i < 15; i++) {
      this.arr.push(i);
    }
  };

  // 自定义的构建标签栏内容的方法，接收标签标题和目标索引作为参数
  @Builder
  tabBuilder(title: string, targetIndex: number) {
    Column() {
      Button(title).fontColor(0 === targetIndex ? Color.White : Color.Black).backgroundColor('rgba(0, 0, 0, 0.05)');
    }.width('100%')
    .height(30);

  };

  // 自定义的构建标签栏内容的方法，接收标签标题和目标索引作为参数
  @Builder
  newsBuilder(targetIndex: number) {
    Column() {
      // 三元表达式判别标签内容及颜色
      Text(this.calcNewsGroup(this.currentListIndex) === targetIndex ? this.arrTitleBarEx[targetIndex] :
        this.arrTitleBar[targetIndex])
        .margin({
          top: 8,
          bottom: 8,
          left: 8,
          right: 8
        })
        .onClick(() => {
          // 实现点击标签list组件可以自动跳转到该标签对应listitem分类的首个item
          this.scrollerForList.scrollToIndex(this.clickToNewsGroup(targetIndex), true);
        })
        .fontColor(this.calcNewsGroup(this.currentListIndex) === targetIndex ? Color.Black : Color.Gray);
    }
    .height(33)
    .width(70)
    .margin({ right: 20 })
    .backgroundColor(this.calcNewsGroup(this.currentListIndex) === targetIndex ? 'rgba(255, 255, 255, 1)' :
      'rgba(242, 243, 245, 1)')
    .borderRadius(16)
    .margin({
      left: 10,
      right: 10,
      top: 40,
      bottom: 40
    });
  };

  calcNewsGroup(index: number): number {
    if (index <= 5) {
      return 0;
    } else if (index <= 10 && index > 5) {
      return 1;
    } else {
      return 2;
    }
  };

  clickToNewsGroup(index: number): number {
    if (index === 0) {
      return 0;
    } else if (index === 1) {
      return 6;
    } else {
      return 11;
    }
  };

  calcScrollAlign(index: number): ScrollAlign {
    if (index === 5 || index === 10) {
      return ScrollAlign.END;
    } else if (index === 6 || index === 11) {
      return ScrollAlign.START;
    } else {
      return ScrollAlign.AUTO;
    }
  };

  // 组件的构建方法，用于定义组件的整体UI结构和布局
  build() {
    Column() {
      // 画面顶部的标签
      Column() {
        Column() {
          Row() {
            this.newsBuilder(0);
            this.newsBuilder(1);
            this.newsBuilder(2);
          }
          .height(20);
        }
        .width('90%') // 设置宽度
        .height(40) // 设置高度
        .backgroundColor('rgba(242, 243, 245, 1)') // 背景色（可自定义）
        .borderRadius(20) // 半径为高度的一半（60 / 2 = 30），形成胶囊形
        .margin({ left: 18, right: 18 })
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center);

        // 画面中部的List组件，用于创建水平滚动的列表，设置了列表项间距、初始索引和滚动条
        Row() {
          List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Column() {
                  Text('hotPage' + item)
                    .width('100%')
                    .fontSize(16)
                    .fontColor(Color.Black)
                    .backgroundColor('rgba(241, 243, 245, 1)')
                    .borderRadius(16)
                    .margin({ top: 20, bottom: 20 })
                    .textAlign(TextAlign.Center)
                    .align(Alignment.Top);
                  Text('Content ' + this.arrContent[item % 3])
                  // .textAlign(TextAlign.Center)
                    .align(Alignment.Top);
                }
                .height('100%')
                .justifyContent(FlexAlign.Start)
                .alignItems(HorizontalAlign.Center);

              }
              .backgroundColor('rgba(242, 243, 245, 1)')
              .borderRadius(16)
              .width('100%')
              .height('100%');
            }, (item: number) => JSON.stringify(item));
          }
          .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
            this.currentListIndex = centerIndex; // 获取到当前界面居中的子组件listitem
          })
          .chainAnimation(true)
          .edgeEffect(EdgeEffect.Spring)
          .listDirection(Axis.Horizontal)
          .height('100%')
          .width('100%')
          // 识别抬手时，listitem为每个分类的末尾item既调用scrollToIndex并靠后对齐
          .onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type === TouchType.Up) {
                this.scrollerForList.scrollToIndex(this.currentListIndex, true,
                  (this.currentListIndex === 5 || this.currentListIndex === 10) ? ScrollAlign.END :
                    ScrollAlign.START);
              }
            }
          });
        }
        .alignItems(VerticalAlign.Top)
        .width('100%')
        .height('100%')
        .padding({ top: 10 });
      }
      .width('90%')
      .height('100%')
      .justifyContent(FlexAlign.SpaceBetween)
      .alignItems(HorizontalAlign.Start);
    }
    .width('100%');
  };
}
```

## 总结

该案例是使用List组件呈现资讯的一种通用场景，根据List组件、Scroll组件的接口文档，以及组件的通用事件组合实现了分组滚动的效果。
