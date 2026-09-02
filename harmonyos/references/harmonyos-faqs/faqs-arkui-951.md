---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-951
title: 如何使用List组件实现流畅的无限下拉滑动效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用List组件实现流畅的无限下拉滑动效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3d0b07f3ea600fd7a2fba1c2b77d13c363e0c0957eca2d67036d7a13fe26dab2
---

## 问题现象

使用List组件实现日历无限下拉业务场景下，下拉加载更多新增数据的时候，UI更新闪烁，如何实现流畅滑动效果？

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项，适合连续、多行呈现同类数据，例如图片和文本。
* [onReachStart](../harmonyos-references/ts-container-list.md#onreachstart)回调在列表到达起始位置时触发。List初始化时如果initialIndex为0会触发一次，List滚动到起始位置时触发一次。List边缘效果为弹簧效果时，滑动经过起始位置时触发一次，回弹回起始位置时再触发一次。
* [onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)回调在有子组件滑入或滑出List显示区域时触发。计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

## 解决方案

在List列表滑动到顶部，在onReachStart方法里向数组开头添加元素，并滚动到指定index，具体实现如下：

* 场景一：在状态管理V2场景中实现。

  使用List组件的onReachStart回调，在List列表滑动到顶部时，onReachStart回调在列表滚动到起始位置时触发，在事件触发时，将数组的第一个元素插入到数组的开头，并调用[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)方法使滚动器滚动到指定的索引位置，并且在onScrollIndex方法中监听滚动索引的变化，更新start变量，实现List列表能够无限下拉的效果，示例代码如下：

  ```ts
  // 定义一个类，标记为可观察的
  // 类中自定义一个数组，标记为可追踪的
  @ObservedV2
  class ArrayHolderVTwo {
    @Trace arr: Array<number> = [];

    // constructor，用于初始化数组个数
    constructor(count: number) {
      for (let i = 0; i < count; i++) {
        this.arr.push(i);
      }
    }
  }

  @Entry
  @ComponentV2
  struct Index {
    @Local arrayHolder: ArrayHolderVTwo = new ArrayHolderVTwo(10);
    @Local totalCount: number = this.arrayHolder.arr.length;
    scroller: Scroller = new Scroller();
    private iCount: number = 1;
    private start: number = 1;

    build() {
      Column({ space: 5 }) {
        List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
          Repeat(this.arrayHolder.arr)
            .virtualScroll({ totalCount: this.totalCount })
            .templateId(() => {
              return 'number';
            })
            .template('number', (r) => {
              ListItem() {
                Column() {
                  Row() {
                    Text(r.item.toString());
                    Text(r.item.toString());
                    Text(r.item.toString());
                  };

                  Row() {
                    Text(r.item.toString());
                    Text(r.item.toString());
                    Text(r.item.toString());
                  };

                  Row() {
                    Text(r.item.toString());
                    Text(r.item.toString());
                    Text(r.item.toString());
                  };
                };
              }
              .margin({ bottom: 5 });
            })
            .each((r) => {
              ListItem() {
                Text(r.index! + ':' + r.item + 'eachMessage');
              };
            });
        }.height('100%')
        .onScrollIndex((start) => {
          this.start = start;
        })
        .onReachStart(() => {
          //  元素位置为屏幕显示的前一个元素
          this.arrayHolder.arr.unshift(this.iCount);
          this.scroller.scrollToIndex(this.start + 1); // 滑动到指定index
          this.iCount++;
        });
      }
      .width('100%')
      .margin({ top: 5 })
      .position({
        left: 20
      });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/BXB4d9ElTUif-Fm8vG-1IQ/zh-cn_image_0000002628401248.gif "点击放大")

* 场景二：在状态管理V1场景中实现，具体实现方法与场景一相似，示例代码如下：

  ```ts
  @Observed
  class ArrayHolder {
    @Track arr: Array<number> = [];

    // constructor，用于初始化数组个数
    constructor(count: number) {
      for (let i = 0; i < count; i++) {
        this.arr.push(i);
      }
    }
  }

  // BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
  class BasicDataSource implements IDataSource {
    private listeners: DataChangeListener[] = [];
    private originDataArray: string[] = [];

    public totalCount(): number {
      return this.originDataArray.length;
    }

    public getData(index: number): string {
      return this.originDataArray[index];
    }

    // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
    registerDataChangeListener(listener: DataChangeListener): void {
      if (this.listeners.indexOf(listener) < 0) {
        console.info('add listener');
        this.listeners.push(listener);
      }
    }

    // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
    unregisterDataChangeListener(listener: DataChangeListener): void {
      const pos = this.listeners.indexOf(listener);
      if (pos >= 0) {
        console.info('remove listener');
        this.listeners.splice(pos, 1);
      }
    }

    // 通知LazyForEach组件需要重载所有子组件
    notifyDataReload(): void {
      this.listeners.forEach(listener => {
        listener.onDataReloaded();
      });
    }

    // 通知LazyForEach组件需要在index对应索引处添加子组件
    notifyDataAdd(index: number): void {
      this.listeners.forEach(listener => {
        listener.onDataAdd(index);
      });
    }

    // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
    notifyDataChange(index: number): void {
      this.listeners.forEach(listener => {
        listener.onDataChange(index);
      });
    }

    // 通知LazyForEach组件需要在index对应索引处删除该子组件
    notifyDataDelete(index: number): void {
      this.listeners.forEach(listener => {
        listener.onDataDelete(index);
      });
    }

    // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
    notifyDataMove(from: number, to: number): void {
      this.listeners.forEach(listener => {
        listener.onDataMove(from, to);
      });
    }

    notifyDatasetChange(operations: DataOperation[]): void {
      this.listeners.forEach(listener => {
        listener.onDatasetChange(operations);
      });
    }
  }

  class MyDataSource extends BasicDataSource {
    private dataArray: string[] = [];

    public totalCount(): number {
      return this.dataArray.length;
    }

    unshiftData(data: string, index: number): void {
      this.dataArray.unshift(data);
      this.notifyDataAdd(index);
    }

    public getData(index: number): string {
      return this.dataArray[index];
    }

    public pushData(data: string): void {
      this.dataArray.push(data);
      this.notifyDataAdd(this.dataArray.length - 1);
    }

    public deleteData(index: number): void {
      if (index >= 0 && index < this.dataArray.length) {
        this.dataArray.splice(index, 1);
        this.notifyDataDelete(index);
      }
    }
  }

  @Entry
  @Component
  struct RepeatScrollPage {
    arrayHolder: ArrayHolder = new ArrayHolder(10);
    @State totalCount: number = this.arrayHolder.arr.length;
    @State dataSource: MyDataSource = new MyDataSource();
    scroller: Scroller = new Scroller();
    private iCount: number = 0;
    // fix
    private start: number = 1;
    @State end: number = 1;

    // end
    aboutToAppear(): void {
      // 添加1-10的数字做数据源
      for (let i = 1; i <= 10; i++) {
        this.dataSource.pushData(i.toString());
      }
    }

    build() {
      Column({ space: 5 }) {
        List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
          LazyForEach(this.dataSource, (r: string) => {
            ListItem() {
              Column() {
                Row() {
                  Text(r);
                  Text(r);
                  Text(r);
                  Text(r);
                };

                Row() {
                  Text(r);
                  Text(r);
                  Text(r);
                  Text(r);
                };

                Row() {
                  Text(r);
                  Text(r);
                  Text(r);
                  Text(r);
                };
              };
            }
            .margin({ bottom: 5 });
          }, (item: string, index: number) => item + index);
        }.height('100%')
        .onScrollIndex((start, end) => {
          this.start = start;
          this.end = end;
        })
        // end
        .onReachStart(() => {
          // 元素位置为屏幕显示的前一个元素
          this.dataSource.unshiftData(this.iCount.toString(), this.start);
          // fix
          let rect = this.scroller.getItemRect(this.start + 1); // 获取子组件的大小位置
          this.scroller.scrollToIndex(this.start + 1); // 滑动到指定index
          this.scroller.scrollBy(0, -rect.y); // 滑动指定距离
          // end
          this.totalCount = this.dataSource.totalCount();
          this.iCount++;
        });

      }
      .width('100%')
      .margin({ top: 5 })
      .position({
        left: 20
      });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ERdwVJslRF-KDAZ-z1WStg/zh-cn_image_0000002658800515.gif "点击放大")
* 场景三：当ListItem类型不同时，在[onScrollStart](../harmonyos-references/ts-container-list.md#onscrollstart9)触发时通过滚动偏移量和ListItem的高度进行比较，提前加载更多数据。

  ```ts
  @Entry
  @Component
  struct IndexThree {
    @State arr: Array<string> = [];
    @State page: number = 1;
    pageSize = 10;
    scroller: Scroller = new Scroller();

    aboutToAppear(): void {
      let listData = new ListData();
      let list = listData.getData(this.page, this.pageSize);
      list.forEach(item => {
        this.arr.push(item);
      });
    }

    build() {
      RelativeContainer() {
        List({ scroller: this.scroller }) {
          ListItem() {
            Text('Type1');
          }
          .height(200)
          .width('100%')
          .margin({ bottom: 5 })
          .backgroundColor('#ace');

          ListItem() {
            Text('Type2');
          }
          .height(100)
          .width('100%')
          .margin({ bottom: 5 })
          .backgroundColor('#acF');

          ListItem() {
            WaterFlow() {
              ForEach(this.arr, (item: number, index: number) => {
                FlowItem() {
                  Text('Type3: ' + item.toString());
                }
                .height(index % 2 === 0 ? 150 : 200)
                .width('100%')
                .margin({ bottom: 5 })
                .backgroundColor('#ace');
              });
            }
            .columnsGap(7)
            .columnsTemplate('1fr 1fr');
          };
        }
        .onScrollStart(() => {
          if (this.scroller.currentOffset().yOffset > this.scroller.getItemRect(2).height - 1000) {
            this.page++;
            let listData = new ListData();
            let list = listData.getData(this.page, this.pageSize);
            list.forEach(item => {
              this.arr.push(item);
            });
          }
        });
      }
      .height('100%')
      .width('100%');
    }
  }

  export class ListData {
    data: Array<string> = [];
    totalCount: number = 100;

    constructor() {
      for (let index = 0; index < this.totalCount; index++) {
        this.data.push(index.toString());
      }
    }

    getData(page: number, pageSize: number) {
      let startIndex = (page - 1) * pageSize;
      return this.data.slice(startIndex, startIndex + pageSize);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4musROLISgaD5hz5BnD8eg/zh-cn_image_0000002628561156.png "点击放大")
