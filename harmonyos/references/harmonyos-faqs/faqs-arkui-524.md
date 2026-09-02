---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-524
title: 使用Scroll嵌套List实现可滚动表格
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用Scroll嵌套List实现可滚动表格
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b0c176b20b1e2bbebf600ed0b511617615a77bf03a3b2572b19463a0c88d9d55
---

## 问题现象

当Scroll组件里面包含ColumnSplit、RowSplit组件时，会影响Scroll滚动。现在没有对应的表格组件，如果要实现表格的效果可以用什么组件去实现呢？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/VtFZYuKvSvKx1WWgVhuAJw/zh-cn_image_0000002628391172.png "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)：主要用于创建一个可滚动的容器，当其子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。支持设置滚动方向和滚动条状态，这可以通过[scrollable](../harmonyos-references/ts-container-scroll.md#scrollable)和[scrollBar](../harmonyos-references/ts-container-scroll.md#scrollbar)属性来控制。
* [ColumnSplit](../harmonyos-references/ts-container-columnsplit.md)：将子组件纵向布局，并在每个子组件之间插入横向分割线。可以包含子组件。ColumnSplit通过分割线限制子组件的高度。初始化时，分割线位置根据子组件的高度来计算。初始化后，动态修改子组件的高度不生效，分割线位置保持不变，可通过拖动相邻分割线改变子组件高度。
* [RowSplit](../harmonyos-references/ts-container-rowsplit.md)：将子组件横向布局，并在每个子组件之间插入纵向分割线。可以包含子组件。RowSplit通过分割线限制子组件的宽度。初始化时，分割线位置根据子组件的宽度来计算。初始化后，动态修改子组件的宽度不生效，分割线位置保持不变，可以通过拖动相邻分割线改变子组件宽度。

## 解决方案

Scroll组件如果嵌套ColumnSplit和RowSplit会导致无法滚动，目前可使用嵌套List实现一个表格。

核心流程：

1. 数据初始化：Index组件初始化数据源并推送数据到ListCard。
2. 渲染列表：List组件遍历数据源，生成每个项目的ListItem。
3. 滚动控制：ListCard内部的Scroller处理滚动事件，更新scrollOffset，并通过onScroll事件更新父组件的滚动状态。
4. 状态同步：通过scrollStart和scrollOffset属性，确保滚动位置在父组件和子组件之间正确同步。

示例代码如下所示：

1. Index.ets：

   ```ts
   import { CommonDataSource } from './CommonDataSource';
   import { ListCard } from './ListCard';

   @Entry
   @Component
   struct Index {
     @State scrollStart: number = 0;
     @State scrollOffset: number = 0;
     private arr1: string[] = [];
     dataSource = new CommonDataSource<String>();

     aboutToAppear(): void {
       for (let i = 0; i < 100; i++) {
         this.arr1.push('1-' + i.toString());
       }
       this.dataSource.pushDataArray(...this.arr1);
     }

     build() {
       List() {
         LazyForEach(this.dataSource, (item: String) => {
           ListItem() {
             Row() {
               Text(item.toString())
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .width(80)
                 .height(45)
                 .borderWidth(2)
                 .margin({left:8,right:4})
                 .borderColor('#F1F3F5')
                 .backgroundColor('#F1F3F5');
               ListCard({
                 itemText: item.toString(),
                 scrollStart: this.scrollStart,
                 scrollOffset: this.scrollOffset
               });
             }.margin({top:5});
           };
         });
       }
       .margin({left:8,right:0})
       .backgroundColor(Color.White)
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
       .width('95%')
       .height('100%');
     }
   }
   ```
2. ListCard.ets：

   ```ts
   import { CommonDataSource } from './CommonDataSource';

   @Component
   export struct ListCard {
     itemText?: string;
     @Watch('onScrollReset') @Link scrollStart: number;
     @Watch('onScrollOffsetChange') @Link scrollOffset: number;
     private onScroll = false;
     private scroller = new Scroller();
     dataSource = new CommonDataSource<Number>();

     aboutToAppear(): void {
       let arr: Number[] = [];
       for (let i = 0; i < 30; i++) {
         arr.push(i);
       }
       this.dataSource.pushDataArray(...arr);
     }

     build() {
       List({ scroller: this.scroller }) {
         LazyForEach(this.dataSource, (item: Number) => {
           ListItem() {
             Text(item.toString())
               .textAlign(TextAlign.Center)
               .backgroundColor('#F1F3F5')
               .borderRadius(10)
               .width(80)
               .height(45);
           }
           .borderWidth(4)
           .borderColor(Color.White);
         });
       }
       .scrollBar(BarState.Off)
       .listDirection(Axis.Horizontal)
       // 在组件出现时滚动到之前记录的位置
       .onAppear(() => {
         if (this.scrollOffset) {
           this.scroller.scrollTo({ xOffset: this.scrollOffset, yOffset: 0 });
         }
       })
       // 在区域变化时调整滚动位置
       .onAreaChange(() => {
         if (this.scrollOffset !== this.scroller.currentOffset().xOffset) {
           this.scroller.scrollTo({ xOffset: this.scrollOffset, yOffset: 0 });
         }
       })
       .onScrollStart(() => {
         this.scrollStart++;
         this.onScroll = true;
       })
       .onScrollStop(() => {
         this.updateScrollOffset();
         this.onScroll = false;
       });
     }

     // 在滚动时更新偏移量，并确保滚动位置正确。
     private updateScrollOffset() {
       if (this.onScroll) {
         let offset: number = this.scroller.currentOffset().xOffset;
         if (offset !== undefined) {
           this.scrollOffset = offset;
           this.scroller.scrollTo({ xOffset: this.scrollOffset, yOffset: 0 });
         }
       }
     }

     // 处理滚动状态
     private onScrollReset() {
       this.onScroll = false;
     }

     // 处理偏移量的变化
     private onScrollOffsetChange() {
       console.info('Test ',
         `onScrollOffsetChange,itemText =  ${this.itemText} onScroll = ${this.onScroll} ; offset = +
         ${this.scrollOffset}`);
       if (!this.onScroll) {
         this.scroller.scrollTo({ xOffset: this.scrollOffset, yOffset: 0 });
       }
     }
   }
   ```
3. CommonDataSource.ets：实现了IDataSource接口，确保遵循特定的数据源规范。

   ```ts
   export class CommonDataSource<T> implements IDataSource {
     private listeners: DataChangeListener[] = []; // 存储所有注册的数据变化监听器
     protected originDataArray: T[] = []; // 存储实际的数据项

     // 返回数据项的总数
     totalCount(): number {
       return this.originDataArray.length;
     }

     // 返回所有数据项的数组
     getAllData(): T[] {
       return this.originDataArray;
     }

     // 根据索引获取单个数据项
     getData(index: number) {
       return this.originDataArray[index];
     }

     // 在指定位置插入数据项
     addData(index: number, data: T): void {
       this.originDataArray.splice(index, 0, data);
       this.notifyDataAdd(index);
     }

     // 替换指定位置的数据项
     pushByIndexed(index: number, count: number, items: T[]) {
       this.originDataArray.splice(index, count, ...items);
       this.notifyDataReload();
     }

     // 在末尾添加单个数据项
     pushData(data: T): void {
       this.originDataArray.push(data);
       this.notifyDataAdd(this.originDataArray.length - 1);
     }

     // 在末尾添加多个数据项
     pushDataArray(...items: T[]): void {
       for (let data of items) {
         this.originDataArray.push(data);
         this.notifyDataAdd(this.originDataArray.length - 1);
       }
     }

     // 根据内容查找并删除数据项
     deleteDataUseContent(data: T): void {
       let delIndex: number = -1;
       for (let index = 0; index < this.originDataArray.length; index++) {
         const element = this.originDataArray[index];
         if (data === element) {
           delIndex = index;
         }
       }
       if (delIndex !== -1) {
         this.deleteData(delIndex);
       }
     }

     // 根据索引删除数据项
     deleteData(index: number): void {
       this.originDataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     // 清空数据数组
     clear() {
       this.originDataArray = [];
       this.notifyDataReload();
     }

     // 替换整个数据数组
     setData(dataArray?: T[]) {
       if (dataArray) {
         this.originDataArray.splice(0, this.originDataArray.length);
         this.originDataArray.push(...dataArray);
       } else {
         this.originDataArray = [];
       }
       this.notifyDataReload();
     }

     // 注册一个数据变化监听器
     registerDataChangeListener(listener: DataChangeListener): void {
       if (this.listeners.indexOf(listener) < 0) {
         this.listeners.push(listener);
       }
     }

     // 注销一个数据变化监听器
     unregisterDataChangeListener(listener: DataChangeListener): void {
       const pos = this.listeners.indexOf(listener);
       if (pos >= 0) {
         this.listeners.splice(pos, 1);
       }
     }

     // 通知数据已重新加载
     notifyDataReload() {
       this.listeners.forEach(listener => {
         listener.onDataReloaded();
       });
     }

     notifyDataAdd(index: number) {
       this.listeners.forEach(listener => {
         listener.onDataAdd(index);
       });
     }

     notifyDataMove(from: number, to: number) {
       this.listeners.forEach(listener => {
         listener.onDataMove(from, to);
       });
     }

     notifyDataDelete(index: number) {
       this.listeners.forEach(listener => {
         listener.onDataDelete(index);
       });
     }

     notifyDataChange(index: number) {
       this.listeners.forEach(listener => {
         listener.onDataChange(index);
       });
     }
   }
   ```
