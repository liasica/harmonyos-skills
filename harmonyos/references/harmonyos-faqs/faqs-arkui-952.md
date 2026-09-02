---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-952
title: 如何通过List组件实现可自动循环滚动的列表
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何通过List组件实现可自动循环滚动的列表
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:881180a86ec847f12eba0ab25f270dda5d973b17c6f6b631b4d26b9b7380c980
---

## 问题现象

如何通过List组件实现一个既能自动滚动又能无限循环的列表？要求列表需要具备自动滚动功能，并能够实现无缝循环播放的效果，使首尾衔接自然，不出现空白或卡顿现象。

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)组件是可滚动的容器组件列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)定时器可以重复调用一个函数，在每次调用之间可以设置固定的时间延迟。
* [ListScroller](../harmonyos-references/ts-container-list.md#listscroller11)的[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)函数，可以控制List的滚动。

## 解决方案

* 场景一：在纵向实现循环滑动列表：
  1. 通过setInterval定时器循环执行this.scroller.scrollTo达到自动滚动的效果。具体逻辑为：当移动大于五行时，每次执行data数组删除索引为0数据，将该数据加到数组末尾的逻辑，实现循环。

     ```ts
     startAutoRoll() {
       this.last = new Date().getTime();
       this.intervalNum = setInterval(() => {
         if (this.rollOffset > (this.itemWidth * 5)) {
           for (let i = 0; i < 5; i++) {
             // data数组前减后加，实现循环
             this.data.deleteData(0);
             this.data.pushData(this.nextNum.toString());
             if (this.nextNum === 9) {
               this.nextNum = 0;
             } else {
               this.nextNum++;
             }
           }
           // 对应data变化，防止超出
           this.rollOffset -= this.itemWidth * 5;
         }
         let curr = new Date().getTime();
         this.rollOffset += 0.5 * (curr - this.last) / 10;
         // 改为x轴移动
         this.scroller.scrollTo({ xOffset: this.rollOffset, yOffset: 0, animation: false });
         this.last = curr;
       }, 10);
     }
     ```
  2. 在List的onScrollFrameBegin回调里计算实际需要的滚动量并作为事件处理函数的返回值返回，List将按照返回值的实际滚动量进行滚动。

     ```ts
     .onScrollFrameBegin((offset: number) => {
       let currOffset = this.scroller.currentOffset().xOffset; // 改为x轴
       let newOffset = currOffset + offset;
       let totalWidth = this.itemWidth * 10;
       // 左滑
       if (newOffset < totalWidth * 0.5) {
         newOffset += totalWidth;
         // 右滑
       } else if (newOffset > totalWidth * 1.5) {
         newOffset -= totalWidth;
       }
       this.rollOffset = newOffset;
       return { offsetRemain: newOffset - currOffset };
     })
     ```

  完整示例参考如下：

  VerticalCircularList.ets：

  ```ts
  import { MyDataSource } from './MyDataSource';

  @Entry
  @Component
  struct VerticalCircularList {
    private dataSource: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private nextNum: number = 0;
    private data: MyDataSource = new MyDataSource();
    private scroller: Scroller = new Scroller();
    private rollOffset: number = 0;
    private intervalNum: number = 0;
    pathStack: NavPathStack = new NavPathStack();
    private itemHeight: number = 50;
    private last: number = 0;

    startAutoRoll() {
      this.last = new Date().getTime();
      this.intervalNum = setInterval(() => {
        if (this.rollOffset > (this.itemHeight * 5)) {
          for (let i = 0; i < 5; i++) {
            // data数组前减后加，实现循环
            this.data.deleteData(0);
            this.data.pushData(this.nextNum.toString());
            if (this.nextNum === 9) {
              this.nextNum = 0;
            } else {
              this.nextNum++;
            }
          }
          // 对应data变化，防止超出
          this.rollOffset -= this.itemHeight * 5;
        }
        let curr = new Date().getTime();
        this.rollOffset += 0.5 * (curr - this.last) / 10;
        this.scroller.scrollTo({ xOffset: 0, yOffset: this.rollOffset, animation: false });
        this.last = curr;
      }, 10);
    }

    aboutToAppear(): void {
      for (let i = 0; i < 10; i++) {
        this.data.pushData(this.dataSource[i].toString());
      }
      for (let i = 0; i < 10; i++) {
        this.data.pushData(this.dataSource[i].toString());
      }
      this.startAutoRoll();
    }

    build() {
      Navigation(this.pathStack) {
        Row() {
          List({ scroller: this.scroller }) {
            LazyForEach(this.data, (item: string) => {
              ListItem() {
                Column() {
                  Text('宝宝吃完奶后，怎样让他快速入睡。' + item.toString())
                    .fontSize(12)
                    .textAlign(TextAlign.Start)
                    .margin({ left: 8 });
                  Row() {
                    Text('20秒获得回复')
                      .fontSize(10)
                      .textAlign(TextAlign.Start)
                      .fontColor('#ffa933ba')
                      .margin({ left: 8, bottom: 8 });
                    Row() {
                      Text('1位妈妈正在回答')
                        .fontSize(8)
                        .fontColor('#ff656266')
                        .margin({ right: 16, bottom: 12 });
                      Image($r('app.media.startIcon'))
                        .width(15)
                        .height(15)
                        .margin({ right: 16, bottom: 12 });
                    };
                  }
                  .margin({ bottom: 10, top: 5 })
                  .width('100%')
                  .justifyContent(FlexAlign.SpaceBetween);
                }
                .padding({ left: 10, top: 5 })
                .alignItems(HorizontalAlign.Start)
                .width('100%');
              }
              .borderRadius(10)
              .backgroundColor('#FFFFFF')
              .height(40)
              .width('90%')
              .margin({
                left: '4.5%',
                right: '2%',
                top: this.itemHeight * 0.1,
                bottom: this.itemHeight * 0.1
              });
            }, (item: string) => item);
          }
          .scrollBar(BarState.Off)
          .width('100%')
          .height(160)
          .backgroundColor('#FFDCDCDC')
          .listDirection(Axis.Vertical)
          .scrollSnapAlign(ScrollSnapAlign.NONE)
          .friction(0.5)
          .onScrollStart(() => {
            clearInterval(this.intervalNum);
          })
          .onScrollStop(() => {
            this.startAutoRoll();
          })
          .onScrollFrameBegin((offset: number) => {
            let currOffset = this.scroller.currentOffset().yOffset;
            let newOffset = currOffset + offset;
            let totalHeight = this.itemHeight * 10;
            // 上滑
            if (newOffset < totalHeight * 0.5) {
              newOffset += totalHeight;
              // 下滑
            } else if (newOffset > totalHeight * 1.5) {
              newOffset -= totalHeight;
            }
            this.rollOffset = newOffset;
            return { offsetRemain: newOffset - currOffset };
          })
        }
      }
    }
  }
  ```

  BasicDataSource.ets：

  ```ts
  export class BasicDataSource implements IDataSource {
    private listeners: DataChangeListener[] = [];
    private originDataArray: string[] = [];

    public totalCount(): number {
      return 0;
    }

    public getData(index: number): string {
      return this.originDataArray[index];
    }

    registerDataChangeListener(listener: DataChangeListener): void {
      if (this.listeners.indexOf(listener) < 0) {
        console.info('add listener');
        this.listeners.push(listener);
      }
    }

    unregisterDataChangeListener(listener: DataChangeListener): void {
      const pos = this.listeners.indexOf(listener);
      if (pos >= 0) {
        console.info('remove listener');
        this.listeners.splice(pos, 1);
      }
    }

    notifyDataReload(): void {
      this.listeners.forEach(listener => {
        listener.onDataReloaded();
      });
    }

    notifyDataAdd(index: number): void {
      this.listeners.forEach(listener => {
        listener.onDataAdd(index);
      });
    }

    notifyDataChange(index: number): void {
      this.listeners.forEach(listener => {
        listener.onDataChange(index);
      });
    }

    notifyDataDelete(index: number): void {
      this.listeners.forEach(listener => {
        listener.onDataDelete(index);
      });
    }

    notifyDataMove(from: number, to: number): void {
      this.listeners.forEach(listener => {
        listener.onDataMove(from, to);
      });
    }
  }
  ```

  MyDataSource.ets：

  ```ts
  import { BasicDataSource } from './BasicDataSource';

  export class MyDataSource extends BasicDataSource {
    private dataArray: string[] = [];

    public totalCount(): number {
      return this.dataArray.length;
    }

    public getData(index: number): string {
      return this.dataArray[index % this.dataArray.length];
    }

    public addData(index: number, data: string): void {
      this.dataArray.splice(index, 0, data);
      this.notifyDataAdd(index);
    }

    public moveDataWithoutNotify(from: number, to: number): void {
      let tmp = this.dataArray.splice(from, 1);
      this.dataArray.splice(to, 0, tmp[0]);
    }

    public pushData(data: string): void {
      this.dataArray.push(data);
      this.notifyDataAdd(this.dataArray.length - 1);
    }

    public deleteData(index: number): void {
      this.dataArray.splice(index, 1);
      this.notifyDataDelete(index);
    }
  }
  ```

  纵向循环滚动效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/9lAopOnvTUST2cn9BS0tUQ/zh-cn_image_0000002658920467.gif "点击放大")

* **场景二**：在横向实现循环滚动列表。横向滑动与纵向类似，完整代码如下（BasicDataSource.ets和MyDataSource.ets与场景一相同）。

  ```ts
  import { MyDataSource } from './MyDataSource';

  @Entry
  @Component
  struct HorizontalCircularList {
    private dataSource: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private nextNum: number = 0;
    private data: MyDataSource = new MyDataSource();
    private scroller: Scroller = new Scroller();
    private rollOffset: number = 0;
    private intervalNum: number = 0;
    pathStack: NavPathStack = new NavPathStack();
    private itemWidth: number = 350; // 纵向中的itemHeight=50改为itemWidth=350
    private last: number = 0;

    startAutoRoll() {
      this.last = new Date().getTime();
      this.intervalNum = setInterval(() => {
        if (this.rollOffset > (this.itemWidth * 5)) {
          for (let i = 0; i < 5; i++) {
            // data数组前减后加，实现循环
            this.data.deleteData(0);
            this.data.pushData(this.nextNum.toString());
            if (this.nextNum === 9) {
              this.nextNum = 0;
            } else {
              this.nextNum++;
            }
          }
          // 对应data变化，防止超出
          this.rollOffset -= this.itemWidth * 5;
        }
        let curr = new Date().getTime();
        this.rollOffset += 0.5 * (curr - this.last) / 10;
        // 改为x轴移动
        this.scroller.scrollTo({ xOffset: this.rollOffset, yOffset: 0, animation: false });
        this.last = curr;
      }, 10);
    }

    aboutToAppear(): void {
      for (let i = 0; i < 10; i++) {
        this.data.pushData(this.dataSource[i].toString());
      }
      for (let i = 0; i < 10; i++) {
        this.data.pushData(this.dataSource[i].toString());
      }
      this.startAutoRoll();
    }

    build() {
      Navigation(this.pathStack) {
        Row() {
          List({ scroller: this.scroller }) {
            LazyForEach(this.data, (item: string) => {
              ListItem() {
                Column() {
                  Text('宝宝吃完奶后，怎样让他快速入睡。' + item.toString())
                    .fontSize(12)
                    .textAlign(TextAlign.Start)
                    .margin({ left: 8 })
                  Row() {
                    Text('20秒获得回复')
                      .fontSize(10)
                      .textAlign(TextAlign.Start)
                      .fontColor('#ffa933ba')
                      .margin({ left: 8, bottom: 8 })
                    Row() {
                      Text('1位妈妈正在回答')
                        .fontSize(8)
                        .fontColor('#ff656266')
                        .margin({ right: 16, bottom: 12 })
                      Image($r('app.media.startIcon'))
                        .width(15)
                        .height(15)
                        .margin({ right: 16, bottom: 12 })
                    };
                  }
                  .margin({ bottom: 10, top: 5 })
                  .width('100%')
                  .justifyContent(FlexAlign.SpaceBetween)
                }
                .padding({ left: 10, top: 5 })
                .alignItems(HorizontalAlign.Start)
                .width('100%')
              }
              .borderRadius(10)
              .backgroundColor('#FFFFFF')
              .height(40)
              .width('90%')
              .margin({
                left: '2%',
                right: '2%',
                top: 50 * 0.1,
                bottom: 50 * 0.1
              });
            }, (item: string) => item);
          }
          .scrollBar(BarState.Off)
          .width('100%')
          .height(160)
          .backgroundColor('#FFDCDCDC')
          .listDirection(Axis.Horizontal) // 滑动方向改为横向
          .scrollSnapAlign(ScrollSnapAlign.NONE)
          .friction(0.5)
          .onScrollStart(() => {
            clearInterval(this.intervalNum);
          })
          .onScrollStop(() => {
            this.startAutoRoll();
          })
          .onScrollFrameBegin((offset: number) => {
            let currOffset = this.scroller.currentOffset().xOffset; // 改为x轴
            let newOffset = currOffset + offset;
            let totalWidth = this.itemWidth * 10;
            // 左滑
            if (newOffset < totalWidth * 0.5) {
              newOffset += totalWidth;
              // 右滑
            } else if (newOffset > totalWidth * 1.5) {
              newOffset -= totalWidth;
            }
            this.rollOffset = newOffset;
            return { offsetRemain: newOffset - currOffset };
          })
        }
      }
    }
  }
  ```

  横向循环滚动效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/B_m-CuxNSTKgLHHiJJqDYw/zh-cn_image_0000002628401258.gif "点击放大")
