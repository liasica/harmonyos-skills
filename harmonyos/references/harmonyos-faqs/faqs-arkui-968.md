---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-968
title: 如何实现List组件所有分组上滑吸顶效果及触底提示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现List组件所有分组上滑吸顶效果及触底提示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f53d116c604a8b9d87336e834cce2911ec85c67bde811853f288266ac689bd45
---

## 问题现象

期望实现这样一个List列表：

* 列表内有很多分组ListItemGroup，支持吸顶，最后一个分组可能无法撑满List，希望同样能实现吸顶效果；
* 当列表滚动至底部后，用户继续向上滑动时，希望随着用户的滑动在列表底部展示“到底啦~~~”提示文本，用户松手后消失。

## 背景知识

* [列表List](../harmonyos-guides/arkts-layout-development-create-list.md)是一种复杂的容器，当列表项达到一定数量，内容超过屏幕大小时，能够提供滚动功能。通过配合[列表组ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)可以对[列表项ListItem](../harmonyos-references/ts-container-listitem.md)分组展示，并自定义分组头部组件和尾部组件。
* ListItemGroup支持通过[sticky](../harmonyos-references/ts-container-list.md#sticky9)设置吸顶效果。点击查看[设置吸顶/吸底](../harmonyos-references/ts-container-listitemgroup.md#示例1设置吸顶吸底)示例。
* 当组件布局大小发生变化时，会触发[onSizeChange()](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)方法回调。
* 当手指触摸组件时，会触发[onTouch()](../harmonyos-references/ts-universal-events-touch.md#ontouch)方法回调。

## 解决方案

实现思路：

* 在最后一个列表分组之后，增加动态调整高度的空白占位块。
  + 空白占位块的高度=列表高度－最后一个列表组高度。

    ```ts
    // 列表空白Item填充
    ListItem().height(this.listHeight - this.lastEmptyItemHeight - 2 * this.spaceHeight)
    ```
  + 列表高度和最后一个列表组高度通过onSizeChange()获取。

* 在空白占位块之后，增加动态调整高度的触底块。
  + 触底块高度默认0，即默认不展示。

    ```ts
    // 列表底部触底提示Item
    ListItem() {
      Text('到底啦~~~')
        .width('100%')
        .fontSize(20)
        .textAlign(TextAlign.Center);
    }.height(this.bottomTipHeight);
    ```
  + 当手指向上滑动时，触底块高度=向上滑动距离，可设置最大值优化体验。
  + 当抬起手指后，触底块高度重置为0。

    ```ts
    .onTouch((event) => {
      switch (event.type) {
        case TouchType.Down:
          // 记录手指初始触摸点，用于计算上滑期间触底提示块的高度
          this.startTouchY = event.touches[0].y;
          break;
        case TouchType.Move:
          // 手指上滑期间，动态计算触底提示块高度
          if (this.bottomTipHeight < MAX_BOTTOM_TIP_HEIGHT) {
            this.bottomTipHeight = Math.min(MAX_BOTTOM_TIP_HEIGHT, this.startTouchY - event.touches[0].y);
            console.log(`event.touches[0].y: ${event.touches[0].y.toFixed(2)}, this.currentOffsetY: ${this.startTouchY.toFixed(2)}, tipsHeight: ${this.bottomTipHeight.toFixed(2)}`);
          }
          break;
        case TouchType.Up:
          // 手指抬起后，触底提示块高度重置为0
          this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
            this.bottomTipHeight = 0;
          });
      }
    ```

  完整代码如下：

  ```ts
  import { curves } from '@kit.ArkUI';

  // 底部提示块最大高度
  const MAX_BOTTOM_TIP_HEIGHT = 70;

  /**
   * 列表吸顶
   */
  @Entry
  @ComponentV2
  struct Index {
    @Local bottomTipHeight: number = 0; // 底部提示高度
    @Local lastEmptyItemHeight: number = 0; // 最后的空白块高度
    private listHeight: number = 0; // 列表高度
    private startTouchY: number = 0; // 手指触摸屏幕初始纵轴坐标
    private spaceHeight: number = 20; // 列表组间距
    private timeTable: TimeTable[] = [
      {
        title: '周一',
        projects: ['语  文', '数  学', '英  语', '生  物']
      },
      {
        title: '周二',
        projects: ['地  理', '历  史', '政  治']
      },
      {
        title: '周三',
        projects: ['物  理', '化  学']
      },
      {
        title: '周四',
        projects: ['计算机导论', '软件工程', '编译原理', '计算机网络', '计算机组成原理']
      },
      {
        title: '周五',
        projects: ['HarmonyOS开发实战']
      }
    ];

    @Builder
    itemHead(text: string) {
      Text(text)
        .fontSize(20)
        .backgroundColor(0xAABBCC)
        .width('100%')
        .padding(10);
    }

    @Builder
    itemFoot(num: number) {
      Text('今日共 ' + num + ' 门课程')
        .fontSize(16)
        .backgroundColor(0xAABBCC)
        .width('100%')
        .padding(5);
    }

    build() {
      Column() {
        List({ space: this.spaceHeight }) {
          // 内容列表组
          ForEach(this.timeTable, (item: TimeTable, index: number) => {
            ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
              ForEach(item.projects, (project: string) => {
                ListItem() {
                  Text(project)
                    .width('100%')
                    .height(100)
                    .fontSize(20)
                    .textAlign(TextAlign.Center)
                    .backgroundColor(0xFFFFFF);
                };
              }, (item: string) => item);
            }
            .divider({ strokeWidth: 1, color: Color.Blue })
            .onSizeChange((_oldV, newV) => {
              // 获取最后一个ListItemGroup高度
              if (index === this.timeTable.length - 1) {
                this.lastEmptyItemHeight = newV.height?.valueOf() as number;
              }
            });
          });

          // 列表空白Item填充
          ListItem().height(this.listHeight - this.lastEmptyItemHeight - 2 * this.spaceHeight)

          // 列表底部触底提示Item
          ListItem() {
            Text('到底啦~~~')
              .width('100%')
              .fontSize(20)
              .textAlign(TextAlign.Center);
          }.height(this.bottomTipHeight);
        }
        .edgeEffect(EdgeEffect.None)
        .onTouch((event) => {
          switch (event.type) {
            case TouchType.Down:
              // 记录手指初始触摸点，用于计算上滑期间触底提示块的高度
              this.startTouchY = event.touches[0].y;
              break;
            case TouchType.Move:
              // 手指上滑期间，动态计算触底提示块高度
              if (this.bottomTipHeight < MAX_BOTTOM_TIP_HEIGHT) {
                this.bottomTipHeight = Math.min(MAX_BOTTOM_TIP_HEIGHT, this.startTouchY - event.touches[0].y);
                console.log(`event.touches[0].y: ${event.touches[0].y.toFixed(2)}, this.currentOffsetY: ${this.startTouchY.toFixed(2)}, tipsHeight: ${this.bottomTipHeight.toFixed(2)}`);
              }
              break;
            case TouchType.Up:
              // 手指抬起后，触底提示块高度重置为0
              this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
                this.bottomTipHeight = 0;
              });
          }
        })
        .onSizeChange((_oldV, newV) => {
          if (newV && newV.height) {
            this.listHeight = newV.height.valueOf() as number;
          }
        })
        .width('90%')
        .height('100%')
        .sticky(StickyStyle.Header)
        .scrollBar(BarState.Off);
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP])
      .width('100%')
      .height('100%')
      .backgroundColor(0xDCDCDC)
      .padding({ top: 5 });
    }
  }

  interface TimeTable {
    title: string;
    projects: string[];
  }
  ```
