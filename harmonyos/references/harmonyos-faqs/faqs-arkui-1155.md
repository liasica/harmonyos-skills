---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1155
title: 通过监听List滑动位置实现唤起组件的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 通过监听List滑动位置实现唤起组件的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:89fc18e9d99b0fbfe725f501b627fa8a58de147a2f0bf4fd6d54ad89784f8cec
---

## 问题现象

在某些特定的场景下，需要实现滑动列表，唤起组件的功能，来提升人机交互的体验效果。如何实现该功能？

## 背景知识

[List组件](../harmonyos-references/ts-container-list.md)作为官方提供的列表组件，与其它滚动组件一样具有位置监听功能，从而能实现滑动到指定位置唤起相关组件的功能。

* 监听坐标位置的方法：[onAreaChange事件](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：监听由布局变化所导致的组件大小、位置发生变化时的回调。其参数为：
  + oldValue：返回目标元素变化之前的宽高以及目标元素相对父元素和页面左上角的坐标位置。
  + newValue：返回目标元素变化之后的宽高以及目标元素相对父元素和页面左上角的坐标位置。
* 监听偏移量的方法：
  + [onWillScroll事件](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)：回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定滚动组件将要滚动的偏移。其参数类型为[OnWillScrollCallback](../harmonyos-references/ts-container-scrollable-common.md#onwillscrollcallback12)。
  + [onScrollFrameBegin事件](../harmonyos-references/ts-container-list.md#onscrollframebegin9)：列表开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。
  + [onDidScroll事件](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)：滚动组件滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

## 解决方案

* 场景一：onAreaChange事件位置监听实现左滑唤醒弹窗：

  ```ts
  @Entry
  @Component
  struct ListRefreshLoad {
    listScroller: ListScroller = new ListScroller();
    @State arr: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    @State startOffset: number = 0;
    @State currentOffset: number = 0;
    @State listWidth: number = 0;
    @State allowOffset: number = 0;
    @State isShow: boolean = false;

    // 获取列表项的总长度
    getMaxWidth() {
      let widthAll = 0;
      for (let index = 0; index < this.arr.length; index++) {
        widthAll += 180;
      }
      widthAll -= this.listWidth;
      this.allowOffset = widthAll;
    }

    // 控制“更多”字体大小，
    getScale() {
      let scale = (this.currentOffset + this.startOffset - this.allowOffset - 30) / 30;
      if (scale > 1) {
        scale = 1;
      }
      return scale;
    }

    build() {
      Column() {
        Row() {
          List({ scroller: this.listScroller }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Row() {
                  Text(item.toString());
                }
                .width(180)
                .height(80)
                .justifyContent(FlexAlign.Center)
                .alignItems(VerticalAlign.Center);
              };
            });
          }
          .scrollBar(BarState.Off)
          .height(80)
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: 180
          })
          .onAreaChange((old, newVal) => {
            this.listWidth = Number(newVal.width);
          })
          .onScrollStart(() => {
            this.getMaxWidth();
            let offset = this.listScroller.currentOffset();
            this.startOffset = offset.xOffset;
            this.currentOffset = 0;
            this.isShow = false;
          })
          .onWillScroll((offset: number, state: ScrollState) => {
            this.currentOffset += offset;
            if (state === 2 && this.allowOffset + 60 < this.currentOffset + this.startOffset) {
              if (this.isShow) {
                return;
              }
              this.isShow = true;
            }
          })
          .listDirection(Axis.Horizontal);

          Column() {
            Text('更多')
              .fontSize(15);
          }
          .scale({ x: 0.7 + 0.3 * this.getScale(), y: 0.7 + 0.3 * this.getScale() })
          .justifyContent(FlexAlign.Center)
          .width(16)
          .height(80)
          .position({
            x: this.listWidth - 30 * this.getScale(),
            y: 0
          });
        };
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }

    @Builder
    myBuilder() {
      Column() {
        Text('弹窗')
          .margin({ top: 20 });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ynE8MG2eRuaVoJPQ_4AJqw/zh-cn_image_0000002661497527.png "点击放大")
* 场景二：偏移量监听实现上滑唤醒按钮下滑隐藏按钮：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    @State showTitle: boolean = false;
    @State msg: string[] = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj'];
    private scrollerForList: Scroller = new Scroller();
    scrollGetData: number[] = [];

    aboutToAppear(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
        data?.setWindowLayoutFullScreen(true); // 设置沉浸式布局
      });
    }

    build() {
      Stack({ alignContent: Alignment.Top }) {
        List({ space: 10, scroller: this.scrollerForList }) {
          ForEach(this.msg, (item: string) => {
            ListItem() {
              Text(`ListItem${item}`)
                .width('100%')
                .height('100%')
                .borderRadius(15)
                .fontSize(24)
                .textAlign(TextAlign.Center)
                .backgroundColor('#f1f3f5');
            }
            .width('90%')
            .height(100);
          }, (item: string) => item);
        }
        .alignListItem(ListItemAlign.Center)
        .width('100%')
        .edgeEffect(EdgeEffect.None)
        .onDidScroll((offset: number, State: ScrollState) => {
          if (offset < 0 && this.showTitle === true) {
            this.showTitle = false; // 下滑隐藏组件
          }
          if (offset > 0 && this.showTitle === false) {
            this.showTitle = true; // 上滑显示组件
          }
          console.info(`offset：${offset},State：${JSON.stringify(State)}`);
        });

        // 控制是否展示以下'开始组题'的UI组件
        if (this.showTitle) {
          Row() {
            Button('开始组题')
              .backgroundColor('#0A59F7');
          }
          .justifyContent(FlexAlign.Center)
          .width('80%')
          .height('8%')
          .position({ x: '10%', y: '90%' });
        }
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  手指向上滑动同时内容向上，为上滑；手指向下滑动同时内容向下，为下滑。实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/jhU4EajNQ42Gj1kwdkgJTg/zh-cn_image_0000002631307298.gif "点击放大")

## 常见FAQ

Q：采用偏移量监听List组件，滑动到边界时唤起组件显示异常？

A：以方案二为例，由于滑动组件默认有回弹模式，滑动到边缘时，回弹的偏移会导致showTitle变化，需要设置edgeEffect属性为None，或者增加滑动到边缘的控制条件，限制showTitle变化。

Q：半模态内嵌套[Scroll组件](../harmonyos-references/ts-container-scroll.md)如何实现下拉关闭功能？

A：在半模态组件中，监听滚动事件，如果是向下滑动且滑动距离超过一定阈值，则关闭半模态组件即可。
