---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-519
title: WaterFlow实现横向布局展示和滑动，并实现内容循环展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > WaterFlow实现横向布局展示和滑动，并实现内容循环展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:968f375735c2afc43d17f5e9be20f217b70cee1850696c2b005406aef6df3741
---

## 问题现象

WaterFlow瀑布流默认是纵向布局展示，本方案实现横向布局展示和横向滑动。

## 背景知识

* [layoutDirection](../harmonyos-references/ts-container-waterflow.md#layoutdirection)属性，设置布局的主轴方向，即WaterFlow的滑动方向。
* [onReachEnd](../harmonyos-references/ts-container-waterflow.md#onreachend)，瀑布流内容到达末尾位置时触发回调。

## 解决方案

1. 设置WaterFlow的layoutDirection为FlexDirection.Row，实现横向滑动，并设置展示几行，如下方示例，设置为展示2行。

   ```ts
   .layoutDirection(FlexDirection.Row)
   .columnsTemplate('1fr 1fr 1fr')
   .rowsTemplate('1fr 1fr')
   ```
2. 配置FlowItem和展示图片内容的高度为100%。此时已经可以实现横向展示和滑动。

   ```ts
   FlowItem() {
     Column() {
       Text(`N${item}`).fontSize(12).height('16')
       // 存在对应的jpg文件才会显示图片
       Image(`res/waterFlowTest(${item % 5}).jpg`)
         .objectFit(ImageFit.Fill)
         .height('100%')
         .layoutWeight(1)
     }
   }
   .width(this.itemWidthArray[item % 100])
   .height('100%')
   .backgroundColor(this.colors[item % 3])
   ```
3. 设计内容循环，初始化this.dataSource数量大于内容数量，加载图片内容名称固定格式以数字序号区分，加载图片时按图片序号和图片总数取余，实现无限依次加载图片。

   ```ts
   Image(`res/waterFlowTest(${item % 5}).jpg`)
     .objectFit(ImageFit.Fill)
     .height('100%')
     .layoutWeight(1)
   ```
4. WaterFlow滑动时，通过onReachEnd回调，给this.dataSource再次增加数量。

   ```ts
   .onReachEnd(() => {
     console.info('onReachEnd');
     for (let i = 0; i < 100; i++) {
       this.dataSource.addLastItem();
     }
   })
   ```
5. 完整示例参考如下：

   Index页面：

   ```ts
   import { WaterFlowDataSource } from '../DataSource/WaterFlowDataSource';

   @Entry
   @Component
   struct WaterFlowDemo {
     private minSize: number = 80;
     private maxSize: number = 180;
     @State colors: number[] = [0x86C5E3, 0x61CFBE, 0x8981F7, 0x86C5E3, 0x61CFBE];
     scroller: Scroller = new Scroller();
     dataSource: WaterFlowDataSource = new WaterFlowDataSource();
     private itemWidthArray: number[] = [];

     // 设置FlowItem的宽/高数组
     setItemSizeArray() {
       for (let i = 0; i < 100; i++) {
         if (i === 0) {
           this.itemWidthArray.push(this.minSize);
         }
         this.itemWidthArray.push(this.maxSize);
       }
     }

     aboutToAppear() {
       this.setItemSizeArray();
     }

     build() {
       Column({ space: 2 }) {
         WaterFlow() {
           LazyForEach(this.dataSource, (item: number) => {
             FlowItem() {
               Column() {
                 Text(`N${item}`).fontSize(12).height('16')
                 // 存在对应的jpg文件才会显示图片
                 Image(`res/waterFlowTest(${item % 5}).jpg`)
                   .objectFit(ImageFit.Fill)
                   .height('100%')
                   .layoutWeight(1)
               }
             }
             .width(this.itemWidthArray[item % 100])
             .height('100%')
             .backgroundColor(this.colors[item % 3])
           }, (item: string) => item)
         }
         .layoutDirection(FlexDirection.Row)
         .columnsTemplate('1fr 1fr 1fr')
         .rowsTemplate('1fr 1fr')
         .columnsGap(10)
         .rowsGap(5)
         .backgroundColor(0xFAEEE0)
         .width('100%')
         .height('100%')
         // 触底加载数据
         .onReachEnd(() => {
           console.info('onReachEnd');
           for (let i = 0; i < 100; i++) {
             this.dataSource.addLastItem();
           }
         })
       }
     }
   }
   ```

   dataSource类页面：

   ```ts
   export class WaterFlowDataSource implements IDataSource {
     private dataArray: number[] = [];
     private listeners: DataChangeListener[] = [];

     constructor() {
       for (let i = 0; i < 100; i++) {
         this.dataArray.push(i);
       }
     }

     // 获取索引对应的数据
     public getData(index: number): number {
       return this.dataArray[index];
     }

     // 通知控制器数据重新加载
     notifyDataReload(): void {
       this.listeners.forEach(listener => {
         listener.onDataReloaded();
       });
     }

     // 通知控制器数据增加
     notifyDataAdd(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataAdd(index);
       });
     }

     // 通知控制器数据变化
     notifyDataChange(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataChange(index);
       });
     }

     // 通知控制器数据删除
     notifyDataDelete(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataDelete(index);
       });
     }

     // 通知控制器数据位置变化
     notifyDataMove(from: number, to: number): void {
       this.listeners.forEach(listener => {
         listener.onDataMove(from, to);
       });
     }

     // 通知控制器数据批量修改
     notifyDatasetChange(operations: DataOperation[]): void {
       this.listeners.forEach(listener => {
         listener.onDatasetChange(operations);
       });
     }

     // 获取数据总数
     public totalCount(): number {
       return this.dataArray.length;
     }

     // 注册改变数据的控制器
     registerDataChangeListener(listener: DataChangeListener): void {
       if (this.listeners.indexOf(listener) < 0) {
         this.listeners.push(listener);
       }
     }

     // 注销改变数据的控制器
     unregisterDataChangeListener(listener: DataChangeListener): void {
       const pos = this.listeners.indexOf(listener);
       if (pos >= 0) {
         this.listeners.splice(pos, 1);
       }
     }

     // 增加数据
     public add1stItem(): void {
       this.dataArray.splice(0, 0, this.dataArray.length);
       this.notifyDataAdd(0);
     }

     // 在数据尾部增加一个元素
     public addLastItem(): void {
       this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length);
       this.notifyDataAdd(this.dataArray.length - 1);
     }

     // 在指定索引位置增加一个元素
     public addItem(index: number): void {
       this.dataArray.splice(index, 0, this.dataArray.length);
       this.notifyDataAdd(index);
     }

     // 删除第一个元素
     public delete1stItem(): void {
       this.dataArray.splice(0, 1);
       this.notifyDataDelete(0);
     }

     // 删除第二个元素
     public delete2ndItem(): void {
       this.dataArray.splice(1, 1);
       this.notifyDataDelete(1);
     }

     // 删除最后一个元素
     public deleteLastItem(): void {
       this.dataArray.splice(-1, 1);
       this.notifyDataDelete(this.dataArray.length);
     }

     // 在指定索引位置删除一个元素
     public deleteItem(index: number): void {
       this.dataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     // 重新加载数据
     public reload(): void {
       this.dataArray.splice(1, 1);
       this.dataArray.splice(3, 2);
       this.notifyDataReload();
     }
   }
   ```
