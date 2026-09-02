---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1400
title: 卡包展开折叠动画实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 卡包展开折叠动画实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2b9e55f5ce8be3c757c5da4766f4f0e282cb2d119e5c997feba27a7bce5f69c9
---

## 问题现象

如何实现银行卡包的展开折叠动效？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/DsEQYAUbT6STT138cYWSeQ/zh-cn_image_0000002628763132.png "点击放大")

## 背景知识

* HarmonyOS提供全局[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)是一种通用事件，手指的触摸动作会触发该回调，鼠标左键按下时对应的事件也会转换成触摸事件并触发该回调。
* [@ObservedV2和@Trace装饰器](../harmonyos-guides/arkts-new-observedv2-and-trace.md)提供了对嵌套类对象属性变化直接观测的能力，是状态管理V2中相对核心的能力之一。为了增强状态管理框架对类对象中属性的观测能力，开发者可以使用@ObservedV2装饰器和@Trace装饰器装饰类以及类中的属性。

## 解决方案

1. 创建Card类，定义缩放比例scale，在y轴上的偏移量offsetY，组件堆叠顺序zIndex，卡片文字title等属性。在Index组件中添加listData属性，该变量类型为Card数组，创建字符串数组creditCard，用于存储银行卡数据。
2. 定义initData方法，初始化listData银行卡数组。在Column容器中，使用Stack和ForEach循环渲染出每个Card组件，其中Text组件用来展示文字，border属性用来设置边框，borderRadius用于设置圆角样式，color属性的rgb值由random方法随机生成，以此实现银行卡包效果。
3. 银行卡包有两种状态，包括展开和折叠状态，通过Button组件控制状态切换。在两种状态下，分别使用handleDataUnfold和handleDataFold方法用来进行数据展示，它们的核心区别是设置银行卡的不同y轴偏移量offsetY。
4. 卡包处于展开状态时，每张银行卡的y轴偏移量的计算结果为初始offsetY乘以index，位于较后位置的Card的offsetY值会以倍数形式增加，从而实现展开效果。在卡包处于折叠状态时，处于最后位置的银行卡的offsetY和scale的值会设置得偏大，且会使用自定义changeFirstIndex方法进行卡片位置移动，以实现动态切换的效果。

```ts
@ObservedV2
class Card {
  title: string = '';
  @Trace scale: number = 1;
  // 设置每个卡包在y轴的偏移量
  @Trace offsetY: number = 0;
  @Trace index: number = 0;
  // zIndex设置组件堆叠顺序，值越大越往上
  @Trace zIndex: number = 0;
  @Trace opacity: number = 1;
  color: string[] =
    ['#47D34C', '#ECA724', '#57C8FC', '#2E6FDB', '#A45AC6', '#5FBA82', '#59DCC5', '#0D5AF5', '#8C43F2', '#EC7024'];

  constructor(title: string) {
    this.title = title;
  }
}
@Entry
@Component
struct CardHolderFoldPage {
  @State listData: Card[] = [];
  @State offsetY: number = 0;
  @State outBoxHeight: number = 500;
  boxItemHeight: number = 100;
  intervalNum: number = -1;
  @State creditCard: string[] = ['***银行', '***银行', '***银行', '***银行', '***银行',
    '***银行', '***银行', '***银行', '***银行', '***银行'];

  aboutToAppear(): void {
    this.initData();
    this.handleDataUnfold();
  }

  // 初始化listData数组
  initData() {
    for (let index = 0; index < 10; index++) {
      let item = new Card(this.creditCard[index]);
      item.zIndex = index;
      this.listData.push(item);
    }
  }

  handleDataUnfold() {
    this.offsetY = (this.outBoxHeight - this.boxItemHeight) / (this.listData.length - 1);
    for (let index = 0; index < this.listData.length; index++) {
      let item = this.listData[index];
      item.zIndex = index;
      item.scale = 1;
      item.opacity = 1;
      item.offsetY = this.offsetY * index;
    }
  }

  handleDataFold() {
    this.offsetY = (this.outBoxHeight - this.boxItemHeight) / (this.listData.length - 1);
    for (let index = 0; index < this.listData.length; index++) {
      let item = this.listData[index];
      item.zIndex = index;
      item.opacity = 1 * index / this.listData.length;
      item.scale = 0.5 + 0.4 * index / this.listData.length;
      item.offsetY = 40;
      if (index === this.listData.length - 1) {
        item.offsetY = 70;
        item.opacity = 1;
        item.scale = 1;
      }
    }
  }

  changeFirstIndex() {
    let length = this.listData.length;
    let cacheItem = this.listData[length - 1];
    this.getUIContext().animateTo({
      duration: 500,
      onFinish: () => {
        if (this.outBoxHeight === 500) {
          return;
        }
        this.listData.pop();
        cacheItem.offsetY = 40;
        cacheItem.scale = 0.1;
        cacheItem.zIndex = 0;
        this.listData.unshift(cacheItem);
      }
    }, () => {
      // 所有卡片进1
      for (let index = 0; index < this.listData.length; index++) {
        let item = this.listData[index];
        item.zIndex += 1;
        item.opacity = 1 * (index + 1) / this.listData.length;
        item.scale = 0.5 + 0.4 * (index + 1) / this.listData.length;
      }
      // 当前卡片下移
      let length = this.listData.length;
      cacheItem.offsetY = 150;
      cacheItem.scale = 0.9;
      // 上一卡片上移
      let nowItem = this.listData[length - 2];
      nowItem.offsetY = 70;
      nowItem.scale = 1;
    });
  }

  build() {
    Column() {
      Stack() {
        ForEach(this.listData, (item: Card, index) => {
          Column() {
            Text(item.title)
              .fontColor(Color.White)
              .fontSize(20)
              .padding(20);
          }
          // 设置位置
          .alignItems(HorizontalAlign.Start)
          .justifyContent(FlexAlign.Start)
          .zIndex(item.zIndex)
          .offset({ y: item.offsetY })
          // 设置组件缩放
          .scale({ x: item.scale, y: item.scale })
          .width('90%')
          .height(this.boxItemHeight)
          .borderRadius(20)
          .backgroundColor(item.color[index])
          // 点击银行卡，可实现一个放大效果
          .onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type === TouchType.Down) {
                this.getUIContext().animateTo({
                  duration: 100
                }, () => {
                  item.scale = 1.05;
                });
              }
              if (event.type === TouchType.Up) {
                this.getUIContext().animateTo({
                  duration: 100
                }, () => {
                  item.scale = 1;
                });
              }
            }
          });
        }, (item: Card) => item.title);
      }
      // 对子组件超出当前组件范围外的区域进行裁剪
      .clip(true)
      .alignContent(Alignment.Top)
      .width(300)
      .height(this.outBoxHeight);

      Button('点击切换')
        .margin(40)
        .onClick(() => {
          // 如果是展开状态，则设置为折叠状态
          if (this.outBoxHeight === 500) {
            this.getUIContext().animateTo({
              duration: 400
            }, () => {
              this.outBoxHeight = 175;
              this.handleDataFold();
            });
            this.intervalNum = setInterval(() => {
              this.changeFirstIndex();
            }, 2000);
          }
          // 如果是折叠状态，则设置为展开状态
          else {
            this.getUIContext().animateTo({
              duration: 400
            }, () => {
              this.outBoxHeight = 500;
              this.handleDataUnfold();
            });
            clearInterval(this.intervalNum);
          }
        });
    }
    .width('100%');
  }
}
```

## 总结

该动画效果实现的核心在于通过自定义方法计算实现动画过程中的关键值，以达到更改组件样式的效果。
