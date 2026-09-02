---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1269
title: 如何实现评论区楼层效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现评论区楼层效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d509c8bca8e0e4c46687d2219e3e18d10ed60858fa108b31ad82250e08617af3
---

## 问题现象

如何实现贴吧评论区楼层的效果，要求如下：

* 实现循环遍历每一层外边都添加一个边框。
* 最多展示4层外边框。

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)布局是一种层叠容器，允许子组件按添加顺序堆叠，后添加的组件覆盖在先前的组件上，常用于实现悬浮按钮、弹窗等场景。
* [Scroll](../harmonyos-references/ts-container-scroll.md)：为可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 解决方案

利用Stack组件用于垂直堆叠子组件，并通过Alignment.Top，使得所有子组件的内容都对齐到顶部达到楼层堆叠的效果。通过监听组件高度的变化，动态调整每个楼层组件的高度和调整边框，并在用户点击展开全部按钮时重新布局。

* FloorDetail页面（定义数据）。

  ```screen
  export class FloorDetail {
    image?: Resource;
    floor?: number = 0;
    commentator?: string = '';
    accountType?: string = '';
    date?: string = '';
    comment: string = '';
    agree: number = 0;
    disagree: number = 0;
    collect: number = 0;
    reply: number = 0;

    constructor(head: Resource | undefined, floor: number, commentator: string, accType: string, date: string,
      comment: string, agree: number, disagree: number, collect: number, reply: number) {
      this.image = head;
      this.floor = floor;
      this.commentator = commentator;
      this.accountType = accType;
      this.date = date;
      this.comment = comment;
      this.agree = agree;
      this.disagree = disagree;
      this.collect = collect;
      this.reply = reply;
    }
  }

  export const floorMessages: FloorDetail[] = [
    new FloorDetail($r('app.media.startIcon'), 9, '天气预报', '官方账号', '2024-11-11', '徽山风景区', 0, 0, 0, 3),
    new FloorDetail($r('app.media.startIcon'), 8, '市气象台', '官方账号', '2024-11-11', '泰山风景区', 0, 0, 0, 5),
    new FloorDetail($r('app.media.startIcon'), 7, '寒潮预报', '官方账号', '2024-11-11', '黄山风景区', 0, 0, 0, 4),
    new FloorDetail($r('app.media.startIcon'), 6, '寒潮天气', '官方账号', '2024-11-11', '华山风景区', 0, 0, 0,
      4),
    new FloorDetail($r('app.media.startIcon'), 5, '大雾天气', '官方账号',
      '皎若太阳升朝霞，灼若芙蕖出渌波，洛神之光，犹如朝阳初升，芙蕖绽放，照亮了整个洛水。',
      '雪后黄山银装素', 0, 0, 0, 0),
    new FloorDetail($r('app.media.startIcon'), 4, '气象台首', '官方账号', '2024-11-11', '珥瑶碧之华琚', 0, 0, 0, 2),
    new FloorDetail($r('app.media.startIcon'), 3, '大雪天气', '官方账号', '2024-11-11', '披罗衣之璀粲兮', 0, 0, 0, 5),
    new FloorDetail($r('app.media.startIcon'), 2, '北京下雪', '官方账号', '2024-11-11', '婉若游龙', 0, 0, 0, 2),
    new FloorDetail($r('app.media.startIcon'), 1, '大雨天气', '官方账号', '2024-11-11', '翩若惊鸿', 0, 0, 0, 1)
  ];
  ```
* Floor页面（自定义组件）。

  ```screen
  import { FloorDetail } from './FloorDetail';

  @Component
  export struct Floor {
    @Prop floorDetail: FloorDetail;
    colWidth: number = 200;

    build() {
      Row() {
        Column() {
          Row({ space: 5 }) {
            Text(`${this.floorDetail.floor}`)
              .backgroundColor(0xFCEED4)
              .padding({ left: 2, right: 2 })
              .fontColor(Color.Orange)
            Text(this.floorDetail.commentator)
              .fontColor(Color.Orange)
              .padding({ left: 2, right: 2 })
          }
          .width('100%')
          .margin({ bottom: 8 })

          Text(`${this.floorDetail.accountType} ${this.floorDetail.date}`)
            .width('100%')
            .fontSize('10fp')
            .fontColor(Color.Gray)
            .padding({ left: 7 })
            .margin({ bottom: 10 })
          Text(this.floorDetail.comment)
            .width('100%')
            .fontSize('14fp')
            .padding({ left: 7, right: 4 })
            .margin({ bottom: 15 })
          Row() {
            Text(`赞同(${this.floorDetail.agree})`)
              .fontColor(Color.Gray)
              .fontSize('10fp')
            Text(`反对(${this.floorDetail.disagree})`)
              .fontColor(Color.Gray)
              .fontSize('10fp')
            Text(`收藏(${this.floorDetail.collect})`)
              .fontColor(Color.Gray)
              .fontSize('10fp')
            Text(`${this.floorDetail.reply} 回复`)
              .fontWeight(FontWeight.Bold)
              .backgroundColor(Color.Gray)
              .fontSize('10fp')
          }
          .width('100%')
          .justifyContent(FlexAlign.End)
        }
        .justifyContent(FlexAlign.End)
        .alignItems(HorizontalAlign.Start)
        .width(this.colWidth)
        .padding({ top: 8, bottom: 8 })
      }
      .margin({ top: 10 })
    }
  }
  ```

* Index页面（核心代码）。
  1. 利用Stack垂直堆叠子组件，达到模拟楼层的目的。
  2. 遍历所有楼层信息，计算出大于三层和小于等于三层的情况。
  3. 创建楼层组件，设置索引的增加，宽度会逐渐减少。
  4. 动态决定组件的高度。如果高度为0，则使用自动高度；否则使用存储的高度值。
  5. 监听组件区域的变化，当组件大小发生变化时更新当前楼层组件的高度。
  6. 通过(index > 4 ? 4 : index) \* this.border\_num来控制索引大于4的楼层不显示边框，达到最多显示4层边框效果。

  ```screen
  import { floorMessages, FloorDetail } from './FloorDetail';
  import { Floor } from './Floor';

  @Entry
  @Component
  struct Index {
    scroller: Scroller = new Scroller();
    @State allFloorMessages: FloorDetail[] = floorMessages; // 所有可用的楼层消息
    @State showFloorMessages: FloorDetail[] = []; // 当前显示的楼层消息
    @State componentHeight: number[] = []; // 每个楼层组件的高度
    @State isShowAll: boolean = false; // 标志，指示是否显示所有消息
    @State isGet: boolean = false; // 标志，指示是否已获取组件高度
    @State showFloors: number = 0; // 要显示的楼层数量
    @State flag: number = 0; // 用于跟踪已处理的楼层数量
    private allFloors: number = this.allFloorMessages.length; // 所有楼层消息的总数
    borderNum: number = 2;

    aboutToAppear(): void {
      if (this.allFloors < 4) {
        this.isShowAll = true;
        this.showFloorMessages = this.allFloorMessages;
        this.showFloors = this.allFloors;
      } else {
        this.showFloorMessages.push(this.allFloorMessages[0]);
        this.showFloorMessages.push(this.allFloorMessages[this.allFloors - 2]);
        this.showFloorMessages.push(this.allFloorMessages[this.allFloors - 1]);
        this.showFloors = 3;
      }
      for (let i: number = 0; i < this.showFloors; i++) {
        this.componentHeight.push(0);
      }
    }

    build() {
      Scroll(this.scroller) {
        Stack({ alignContent: Alignment.Top }) {
          if (!this.isGet) {
            ForEach(this.showFloorMessages, (message: FloorDetail, index: number) => {
              Floor({ floorDetail: message, colWidth: 300 - index * 5 })
                .height(this.componentHeight[index] === 0 ? 'auto' : this.componentHeight[index])
                .onAreaChange((oldValue: Area, newValue: Area) => {
                  this.componentHeight[index] = newValue.height as number;
                  this.flag += 1;
                  if (this.flag === this.showFloors) {
                    for (let i: number = this.showFloors - 2; i >= 0; i--) {
                      this.componentHeight[i] += this.componentHeight[i + 1];
                    }
                    if (this.isShowAll === false) {
                      this.componentHeight[1] += 30;
                      this.componentHeight[0] += 30;
                    }
                    this.isGet = true;
                  }
                })
            })
          } else {
            ForEach(this.showFloorMessages, (message: FloorDetail, index: number) => {
              Column() {
                Floor({ floorDetail: message, colWidth: 300 - index * 5 })
                if (this.isShowAll === false && index === 1) {
                  Column() {
                    Divider()
                      .strokeWidth(1)
                      .margin({ top: 5, bottom: 5 })
                    Text('展开全部')
                      .width('100%')
                      .textAlign(TextAlign.Center)
                      .fontColor(Color.Gray)
                      .fontSize('12fp')
                      .margin({ bottom: 5 })
                  }
                  .width(300 - index * 5)
                  .height(25)
                  .onClick(() => {
                    this.flag = 0;
                    this.isShowAll = true;
                    this.showFloorMessages = this.allFloorMessages;
                    this.showFloors = this.allFloors;
                    this.componentHeight = [];
                    for (let i: number = 0; i < this.showFloors; i++) {
                      this.componentHeight.push(0);
                    }
                    this.isGet = !this.isGet;
                  })
                }
              }
              .height(this.componentHeight[index])
              .backgroundColor(0xFFF9F2)
              .borderWidth(index > 4 ? { bottom: 0.5, top: 0.5 } : 0.5)
              .padding(3)
              .borderColor(Color.Black)
              .justifyContent(FlexAlign.End)
              .margin({
                top: (index > 4 ? 4 : index) * this.borderNum
              })
            })
          }
        }
      }
      .width('100%')
    }
  }
  ```
