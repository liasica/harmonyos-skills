---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-766
title: 如何使用Swiper实现四宫格会议页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用Swiper实现四宫格会议页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4b3ae5007e119777f760c2bb7ff3269422480eb2ebf292fd022801874ece54ce
---

## 问题现象

需要实现一个动态会议的布局场景：

1. 会议参与者人数动态增加和减少，具体人数不确定。
2. 每个页面排列四个人，采用2×2的布局方式。如果人数超过四个，会自动排在下一页。
3. 支持左右滑动切换页面。
4. 页面底部显示当前页数和总页数。

## 效果预览

| 会议页 | 与会人页面1 | 与会人页面2 | 运行效果图 |
| --- | --- | --- | --- |
|  |  |  |  |

## 背景知识

* 滑块视图容器组件[Swiper](../harmonyos-references/ts-container-swiper.md)能够实现子组件的滑动轮播，并且可以结合[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)懒加载优化性能。Swiper组件允许用户通过滑动手势在多个页面之间进行切换。
* LazyForEach用于在列表中延迟加载项，以提升应用的加载速度和性能。[Flex](../harmonyos-references/ts-container-flex.md)组件能够使容器内的子元素在指定方向上自动对齐和均匀分布，适用于动态布局场景，可以使用Flex布局实现四宫格效果。

## 解决方案

主要功能实现在MeetingSwiper.ets中，LazyDataSource.ets为懒加载数据通用工具类，ObservedArray.ets是一个继承自Array的类，通过new操作符创建的ObservedArray的实例可以观察到属性变化。MeetingSwiper.ets中的功能实现：

1. 将原始数据列表拆分为每4个元素一组的子数组，每个子数组代表一个页面的数据。
2. 使用Swiper组件实现页面的滑动切换，每个页面展示一个子数组的数据。
3. 使用Flex布局在每个页面内实现2×2的四宫格展示。
4. 第一个页面用空数组占位，显示会议界面。
5. 使用Swiper().indicator(Indicator.digit())实现在页面底部显示当前页数和总页数。

完整示例参考如下：

* MeetingSwiper.ets代码示例如下：

  ```ts
  import { JSON } from '@kit.ArkTS';
  import { LazyDataSource } from './LazyDataSource';

  // 与会人
  class ItemParam {
    name: string = '';

    constructor(name: string) {
      this.name = name;
    }
  }

  @Entry
  @Component
  struct MeetingSwiper {
    private swiperController: SwiperController = new SwiperController();
    @State private dataArr: LazyDataSource<ItemParam[]> = new LazyDataSource(); // 处理后的数据
    list: ItemParam[] = []; // 初始数据

    aboutToAppear(): void {
      // 初始化数据
      for (let i = 1; i <= 6; i++) {
        let param = new ItemParam(`第${i}个`);
        this.list.push(param);
      }
      this.resetDataArr();
    }

    resetDataArr() {
      // 将数据按四个拆分
      let listArr: ItemParam[][] = [];
      for (let i = 0; i < this.list.length; i += 4) {
        listArr.push(this.list.slice(i, i + 4));
      }
      // 清空数据
      this.dataArr.clear();
      // 添加第一屏会议界面
      this.dataArr.pushData([]);
      // 添加与会人
      this.dataArr.pushDataPositionArray(1, listArr);
    }

    build() {
      Column() {
        Swiper(this.swiperController) {
          LazyForEach(this.dataArr, (item: ItemParam[], index: number) => {
            if (index === 0) {
              Column() {
                Text('主持')
                  .fontSize(40)
                  .width(80)
                  .height(80)
                  .borderRadius(40)
                  .backgroundColor('#f1f3f5')
              }
              .justifyContent(FlexAlign.Center)
              .width('100%')
              .height('100%')
            } else {
              Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.SpaceBetween }) { // 子组件多行布局
                ForEach(item, (param: ItemParam,itemIndex:number) => {
                  Text(param.name)
                    .width('calc((100% - 40vp)/2)')
                    .height('calc((95% - 40vp)/2)')
                    .textAlign(TextAlign.Center)
                    .margin(10)
                    .backgroundColor('#f1f3f5')
                    .borderRadius(20)
                    .onClick(() => {
                      // 点击按钮，删除对应与会人，更新数据
                      if(itemIndex === 0 && (((index-1)*4+ itemIndex) === this.list.length - 1)) {
                        //当点击的是当前屏最后一个按钮时，先跳转前一页，然后删除并刷新数据
                        this.swiperController.changeIndex(index-1);
                        setTimeout(()=>{
                          this.list.splice((index-1)*4+ itemIndex, 1);
                          this.resetDataArr();
                        },200);
                      }else {
                        this.list.splice((index-1)*4+ itemIndex, 1);
                        this.resetDataArr();
                      }
                    })
                }, (param: ItemParam) => JSON.stringify(param))
              }
            }
          }, (item: ItemParam[]) => JSON.stringify(item))
        }
        .indicator(Indicator.digit()) // 设置数字导航点样式
        .loop(false)
        .width('100%')
        .height('100%')
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* LazyDataSource.ets代码示例如下：

  ```ts
  import { ObservedArray } from './ObservedArray';

  class BasicDataSource<T> implements IDataSource {
    private listeners: DataChangeListener[] = [];

    public totalCount(): number {
      return 0;
    }

    public getData(index: number): T | undefined {
      console.info('index:',index);
      return undefined;
    }

    // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
    registerDataChangeListener(listener: DataChangeListener): void {
      if (this.listeners.indexOf(listener) < 0) {
        this.listeners.push(listener);
      }
    }

    // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
    unregisterDataChangeListener(listener: DataChangeListener): void {
      const pos = this.listeners.indexOf(listener);
      if (pos >= 0) {
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

  @Observed
  export class LazyDataSource<T> extends BasicDataSource<T> {
    dataArray: T[] = [];

    public totalCount(): number {
      return this.dataArray.length;
    }

    public getData(index: number): T {
      return this.dataArray[index];
    }

    public addData(index: number, data: T): void {
      this.dataArray.splice(index, 0, data);
      this.notifyDataAdd(index);
    }

    public pushData(data: T): void {
      this.dataArray.push(data);
      this.notifyDataAdd(this.dataArray.length - 1);
    }

    public pushArrayData(newData: ObservedArray<T>): void {
      this.clear();
      this.dataArray.push(...newData);
      this.notifyDataReload();
    }

    public pushDataPositionArray(index: number, newData: ObservedArray<T>): void {
      this.dataArray.splice(index, 0, ...newData);
      this.notifyDataReload();
    }

    public appendArrayData(addData: ObservedArray<T>): void {
      this.dataArray.push(...addData);
      this.notifyDataReload();
    }

    public deleteData(index: number): void {
      this.dataArray.splice(index, 1);
      this.notifyDataDelete(index);
    }

    public getDataList(): ObservedArray<T> {
      return this.dataArray;
    }

    public clear(): void {
      this.dataArray.splice(0, this.dataArray?.length);
    }

    public isEmpty(): boolean {
      return this.dataArray.length === 0;
    }

    public prependAllData(data: Array<T>): void {
      this.dataArray.unshift(...data);
      this.notifyDatasetChange([
        { type: DataOperationType.ADD, index: -data.length, count: data.length },
        { type: DataOperationType.RELOAD }
      ]);
    }
  }
  ```
* ObservedArray.ets：

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
  ```
