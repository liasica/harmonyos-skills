---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1461
title: List下拉刷新时如何保证更新后的页面停留在原始位置上
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List下拉刷新时如何保证更新后的页面停留在原始位置上
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32bf2162855780ca0e1247ecd74aa571520703588e0f9a4b4774dfe749017227
---

## 问题现象

在使用List组件实现下拉刷新功能时，当向LazyForEach数据源头部插入新数据后，界面默认会替换当前展示的Item数据，导致用户无法继续向上滑动查看新增数据。如何实现新增数据在顶部展示，同时保持当前展示的Item不变，使用户可以继续向上滑动查看新增数据？

## 背景知识

* [List组件](../harmonyos-references/ts-container-list.md)可以轻松高效地显示结构化、可滚动的信息，页面的下拉刷新与上拉加载功能在移动应用中十分常见，该操作可使用[Refresh组件](../harmonyos-references/ts-container-refresh.md)实现。
  + 通过[maintainVisibleContentPosition](../harmonyos-references/ts-container-list.md#maintainvisiblecontentposition12)设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。
  + 通过[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)、[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)来控制滚动位置以实现列表的快速定位。
* [LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件和销毁无用组件。[IDataSource](../harmonyos-references/ts-rendering-control-lazyforeach.md#idatasource)是LazyForEach数据源，需要开发者实现相关接口。其中关键为[DataChangeListener](../harmonyos-references/ts-rendering-control-lazyforeach.md#datachangelistener)数据变化监听器，进行批量的数据处理后，使用[onDatasetChange](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondatasetchange12)通知组件刷新。

## 解决方案

根据具体使用maintainVisibleContentPosition、scrollToIndex或scrollTo的需求，可分别采用以下两种实现方案。

* **方案一**：通过maintainVisibleContentPosition控制可见内容位置不变。
  1. 根据业务需要构建数据源IDataSource，然后实现相关数据更新接口，在数据更新后，使用onDatasetChange通知组件数据更新。
  2. 根据界面设计绘制界面，当触发数据增加时，调用pushDataPositionArray进行数据处理。

  详细示例代码如下：

  + 数据类实现LazyDataSource1.ets：

    ```ts
    // 重写数据类
    @Observed
    export class ObservedArray<T> extends Array<T> {
      constructor(args?: T[]) {
        if (args instanceof Array) {
          super(...args);
        } else {
          super();
        }
      }
    }

    // 数据更新监听处理
    class BasicDataSource<T> implements IDataSource {
      private listeners: DataChangeListener[] = [];

      // 数据交给上层处理，若未定义则抛出错误
      totalCount(): number {
        throw new Error('Method not implemented.');
      }

      // 数据交给上层处理，若未定义则抛出错误
      getData(index: number): T {
        console.info(`index: ${index}`);
        throw new Error('Method not implemented.');
      }

      // 数据添加处理
      public notifyDataArrayAdd(index: number, count: number, key: string[]): void {
        this.listeners.forEach(listener => {
          listener.onDatasetChange([{
            type: DataOperationType.ADD,
            index: index,
            count: count,
            key: key
          }]);
        });
      }

      // 注册监听
      registerDataChangeListener(listener: DataChangeListener): void {
        if (this.listeners.indexOf(listener) < 0) {
          this.listeners.push(listener);
        }
      }

      // 取消监听
      unregisterDataChangeListener(listener: DataChangeListener): void {
        const pos = this.listeners.indexOf(listener);
        if (pos >= 0) {
          this.listeners.splice(pos, 1);
        }
      }

      // 数据重新加载
      notifyDataReload(): void {
        this.listeners.forEach(listener => {
          listener.onDataReloaded();
        });
      }
    }

    // 业务数据操作
    export class LazyDataSource<T> extends BasicDataSource<T> {
      dataArray: T[] = [];

      // 获取数据数量
      public totalCount(): number {
        return this.dataArray.length;
      }

      // 获取指定数据
      public getData(index: number): T {
        return this.dataArray[index];
      }

      // 指定位置添加数据
      public pushDataPositionArray(index: number, newData: ObservedArray<T>, key: string[]): void {
        this.dataArray.splice(index, 0, ...newData);
        this.notifyDataArrayAdd(index, newData.length, key);
      }
    }
    ```
  + 界面详细实现Index1.ets：

    ```ts
    import { LazyDataSource } from './LazyDataSource1';

    @Entry
    @ComponentV2
    export struct Index1 {
      @Local isRefreshing: boolean = false;
      @Local refreshText: string = '';
      @Local lazyDataModel: LazyDataSource<string> = new LazyDataSource();
      @Local timer: number = 1;

      // 生成数据
      aboutToAppear(): void {
        let arr: string[] = [];
        for (let i = 0; i < 30; i++) {
          arr.push(`${i}Text Item`);
        }
        this.lazyDataModel.dataArray = arr;
        this.lazyDataModel.notifyDataReload();
      }

      // 刷新UI提示
      @Builder
      getRefreshBuilder() {
        Row({ space: 8 }) {
          LoadingProgress()
            .width(20)
            .aspectRatio(1);
          Text(this.refreshText)
            .fontSize(14)
            .fontColor('#818181');
        };
      }

      // 添加数据
      addData(timer: number) {
        let arr: string[] = [];
        for (let index = 5; index > 0; index--) {
          arr.push(`第 ${timer} 次 add HeadItem ${index}`);
        }
        this.lazyDataModel.pushDataPositionArray(0, arr, arr);
        this.isRefreshing = false;
      }

      build() {
        Column() {
          Refresh({ refreshing: $$this.isRefreshing, builder: this.getRefreshBuilder() }) {
            List() {
              LazyForEach(this.lazyDataModel, (item: string) => {
                ListItem() {
                  Column() {
                    Text(item)
                      .fontSize(18)
                      .height(52);
                  }
                  .height(56)
                  .width('100%')
                  .padding({ left: 10, right: 10 });
                };
              }, (item: string) => item.toString());
            }
            .maintainVisibleContentPosition(true) // 设置可见内容位置不变
            .width('100%')
            .height('100%')
            .scrollBar(BarState.Off)
            .edgeEffect(EdgeEffect.None);
          }
          .onStateChange(async (status) => {
            switch (status) {
              case RefreshStatus.Inactive:
                break;
              case RefreshStatus.Drag:
                this.refreshText = '继续往下拉';
                break;
              case RefreshStatus.OverDrag:
                this.refreshText = '松手加载';
                break;
              case RefreshStatus.Refresh:
                this.refreshText = '加载中';
                await this.addData(this.timer);
                this.timer++;
                break;
              case RefreshStatus.Done:
                this.refreshText = '加载成功';
            }
          });
        };
      }
    }
    ```

    效果图如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/O6Q_VhkvRgudEdderrfmOA/zh-cn_image_0000002628605352.png "点击放大")
* **方案二**：通过scrollToIndex、scrollTo控制滚动，使得可视区域不变。
  1. LazyDataSource2.ets：定义LazyForEach懒加载数据通用工具类。

     ```ts
     @Observed
     export class ObservedArray<T> extends Array<T> {
       constructor(args?: T[]) {
         if (args instanceof Array) {
           super(...args);
         } else {
           super();
         }
       }
     }

     class BasicDataSource<T> implements IDataSource {
       private listeners: DataChangeListener[] = [];

       public totalCount(): number {
         return 0;
       }

       public getData(index: number): T | undefined {
         console.info(`index: ${index}`);
         return undefined;
       }

       registerDataChangeListener(listener: DataChangeListener): void {
         if (this.listeners.indexOf(listener) < 0) {
           this.listeners.push(listener);
         }
       }

       unregisterDataChangeListener(listener: DataChangeListener): void {
         const pos = this.listeners.indexOf(listener);
         if (pos >= 0) {
           this.listeners.splice(pos, 1);
         }
       }

       notifyDataReload(): void {
         this.listeners.forEach(listener => {
           listener.onDataReloaded();
         });
       }
     }

     export class LazyDataSource<T> extends BasicDataSource<T> {
       dataArray: T[] = [];

       public totalCount(): number {
         return this.dataArray.length;
       }

       public getData(index: number): T {
         return this.dataArray[index];
       }

       public pushDataPositionArray(index: number, newData: ObservedArray<T>): void {
         this.dataArray.splice(index, 0, ...newData);
         this.notifyDataReload();
       }
     }
     ```
  2. Index2.ets：实现下拉刷新，向头部添加数据。使用scrollToIndex方法滚动至头部新增数据长度的索引位置，保持当前展示的Item数据不变。

     ```ts
     import { LazyDataSource } from './LazyDataSource2';

     @Entry
     @ComponentV2
     export struct Index2 {
       @Local isRefreshing: boolean = false;
       @Local refreshText: string = '';
       @Local lazyDataModel: LazyDataSource<string> = new LazyDataSource();
       @Local listScroller: ListScroller = new ListScroller();
       @Local timer: number = 1;
       @Local listItemHeight: number = 0;

       aboutToAppear(): void {
         let arr: string[] = [];
         for (let i = 0; i < 30; i++) {
           arr.push(`${i}Text Item`);
         }
         this.lazyDataModel.dataArray = arr;
         this.lazyDataModel.notifyDataReload();
       }

       @Builder
       getRefreshBuilder() {
         Row({ space: 8 }) {
           LoadingProgress()
             .width(20)
             .aspectRatio(1);
           Text(this.refreshText)
             .fontSize(14)
             .fontColor('#818181');
         };
       }

       async getData(timer: number) {
         let arr: string[] = [];
         for (let i = 5; i > 0; i--) {
           arr.push(`第 ${timer} 次 add HeadItem ${i}`);
         }
         setTimeout(() => {
           // 向lazyDataModel数据源头部添加一组数据，并使用scrollToIndex、scrollTo滚动到指定位置，使当前页面顶部展示数据不变。
           this.lazyDataModel.pushDataPositionArray(0, arr);
           // 使用scrollToIndex滚动到指定Item索引位置
           this.listScroller.scrollToIndex(arr.length);
           this.isRefreshing = false;
         }, 500);
       }

       build() {
         Column() {
           Refresh({ refreshing: $$this.isRefreshing, builder: this.getRefreshBuilder() }) {
             List({ scroller: this.listScroller }) {
               LazyForEach(this.lazyDataModel, (item: string) => {
                 ListItem() {
                   Column() {
                     Text(item)
                       .fontSize(18)
                       .height(52);
                   }
                   .height(56)
                   .width('100%')
                   .padding({ left: 10, right: 10 });
                 }
                 .onAreaChange((newValue: Area) => {
                   this.listItemHeight = Number(newValue.height); // 获取item的高度
                 });
               }, (item: string) => item.toString());
             }
             .width('100%')
             .height('100%')
             .scrollBar(BarState.Off)
             .edgeEffect(EdgeEffect.None);
           }
           .onStateChange(async (status) => {
             switch (status) {
               case RefreshStatus.Inactive:
                 break;
               case RefreshStatus.Drag:
                 this.refreshText = '继续往下拉';
                 break;
               case RefreshStatus.OverDrag:
                 this.refreshText = '松手加载';
                 break;
               case RefreshStatus.Refresh:
                 this.refreshText = '加载中';
                 await this.getData(this.timer);
                 this.timer++;
                 break;
               case RefreshStatus.Done:
                 this.refreshText = '加载成功';
             }
           });
         };
       }
     }
     ```

     效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/xfwoiYSmQ96s7cj0otfphg/zh-cn_image_0000002658844609.png "点击放大")

## 常见FAQ

Q：为什么使用onDataReloaded更新数据，无法达成可视区域不变的效果？

A：onDataReloaded是数据重新加载，使用LazyForEach重新加载数据时，即maintainVisibleContentPosition属性设置为true，可见区内容位置也会跟随变化。

Q：List绑定scroller的场景下，scroller已经被下拉到某个位置，当数据源被替换（如刷新、切换分类）时，如何让滚动位置重置到顶部？

A：[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)支持指定偏移量滚动，通过设置偏移量({yOffset: 0, xOffset: 0 })可实现重置scroller滚动位置到组件最顶端。
