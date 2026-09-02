---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1363
title: 如何实现多列卡片列表无限循环滚动功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现多列卡片列表无限循环滚动功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:ee839249c04aaefb9026dd8afeca163d0a85f85d6b86e889a0c9fdfd8b004477
---

## 问题现象

希望实现一个显示三列卡片的数据流，所有的卡片高度一致，起始状态中间列第一张卡片展示一半的高度，每列数据3s自动移动一个卡片高度的位移，所有卡片循环显示。

## 背景知识

[Swiper](../harmonyos-references/ts-container-swiper.md)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。

## 解决方案

1. 实现包含三个垂直滚动Swiper组件的界面，每个组件显示不同数量的项目。定义MyDataSource类实现IDataSource接口，管理数据源。在aboutToAppear方法中初始化数据，并通过SwiperFlow构建器创建Swiper组件，使用LazyForEach渲染数据项。
2. Swiper组件配置为垂直滚动、自动播放和循环模式，实现流畅的数据展示。要实现组件自动滑动时较为平顺，需要将Swiper组件的curve属性设置为Curve.Linear，且duration属性设置为自动滚动的时长。示例代码如下：

   ```ts
   class BasicDataSource<T> implements IDataSource {
     private listeners: DataChangeListener[] = [];
     private originDataArray: T[] = [];

     public totalCount(): number {
       return 0;
     }

     public getData(index: number): T {
       return this.originDataArray[index];
     }

     // 注册数据改变的监听器。
     registerDataChangeListener(listener: DataChangeListener): void {
       if (this.listeners.indexOf(listener) < 0) {
         console.info('add listener');
         this.listeners.push(listener);
       }
     }

     // 注销数据改变的监听器。
     unregisterDataChangeListener(listener: DataChangeListener): void {
       const pos = this.listeners.indexOf(listener);
       if (pos >= 0) {
         console.info('remove listener');
         this.listeners.splice(pos, 1);
       }
     }

     // 重新加载数据完成后调用
     notifyDataReload(): void {
       this.listeners.forEach(listener => {
         listener.onDataReloaded();
       });
     }

     // 添加数据完成后调用
     notifyDataAdd(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataAdd(index);
       });
     }

     // 改变数据完成后调用
     notifyDataChange(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataChange(index);
       });
     }

     // 删除数据完成后调用
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

   export class MyListDataSource<T> extends BasicDataSource<T> {
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

     // 添加数据
     public pushData(data: T): void {
       this.dataArray.push(data);
       this.notifyDataAdd(this.dataArray.length - 1);
       console.info('this.data', JSON.stringify(this.dataArray));
     }

     // 修改数据
     public changeData(index: number, data: T): void {
       this.dataArray.splice(index, 1, data);
       this.notifyDataChange(index);
     }

     // 删除数据
     public deleteData(index: number): void {
       this.dataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     // 移动数据
     public moveData(from: number, to: number): void {
       let temp: T = this.dataArray[from];
       this.dataArray[from] = this.dataArray[to];
       this.dataArray[to] = temp;
       this.notifyDataMove(from, to);
     }

     // 修改全部数据
     public modifyAllData(): void {
       this.dataArray = [];
       // 通知LazyForEach需要重建所有子节点
       this.notifyDataReload();
     }
   }

   @Observed
   class imageList {
     id: string = '';
     picUrl: string | Resource = '';
   }

   /**
    *
    * 为了实现一个包含三个垂直滚动Swiper组件的界面，每个组件显示不同数量的项目。
    * 定义MyDataSource类实现了IDataSource接口，用于管理数据源。
    * 在aboutToAppear方法中初始化数据，并通过SwiperFlow构建器创建Swiper组件，使用LazyForEach渲染数据项。
    * Swiper组件配置为垂直滚动、自动播放和循环模式，实现流畅的数据展示。
    * 要实现组件自动滑动时较为平顺，需要将Swiper组件的curve属性设置为Curve.Linear，且duration属性设置为自动滚动的时长。
    * */
   @Entry
   @Component
   struct SwiperExample {
     @State imageData1: MyListDataSource<imageList> = new MyListDataSource();
     @State imageData2: MyListDataSource<imageList> = new MyListDataSource();
     @State imageData3: MyListDataSource<imageList> = new MyListDataSource();
     @State isRefreshing: boolean = false;
     @State arr: String[] = ['0', '1', '2', '3'];

     aboutToAppear(): void {
       this.getImageList();
     }

     getImageList() {
       let list: imageList[] = [{
         'id': '1956619377562xxx',
         'picUrl': 'https://xxx'
       }];
       const defaultImage: imageList = { id: '-1', picUrl: '' };
       while (list.length < 9) {
         list.push({
           id: String(list.length + 1),
           picUrl: defaultImage.picUrl
         });
       }
       // 将数组分成三份
       const chunkSize = Math.ceil(list.length / 3);
       const chunk1 = list.slice(0, chunkSize);
       const chunk2 = list.slice(chunkSize, chunkSize * 2);
       const chunk3 = list.slice(chunkSize * 2);
       // 为每一份数据创建无缝列表

       const chunk1sub = chunk1.length > 1 ? chunk1.slice(0, chunk1.length - 1) : chunk1;
       const seamlessChunk1 = [
         chunk1[chunk1.length - 1],
         ...chunk1,
         ...chunk1sub
       ];
       const chunk2sub = chunk2.length > 1 ? chunk2.slice(0, chunk2.length - 1) : chunk2;
       const seamlessChunk2 = [
         chunk2[chunk2.length - 1],
         ...chunk2,
         ...chunk2sub
       ];
       const chunk3sub = chunk3.length > 1 ? chunk3.slice(0, chunk3.length - 1) : chunk3;
       const seamlessChunk3 = [
         chunk3[chunk3.length - 1],
         ...chunk3,
         ...chunk3sub
       ];
       this.imageData1.dataArray = seamlessChunk1;
       this.imageData2.dataArray = seamlessChunk2;
       this.imageData3.dataArray = seamlessChunk3;
       this.imageData1.notifyDataReload();
       this.imageData2.notifyDataReload();
       this.imageData3.notifyDataReload();
     }

     updateImageList() {
       let list: imageList[] = [{
         'id': '1956619377562xxx',
         'picUrl': 'https://yyy'
       }];
       const defaultImage: imageList = { id: '-1', picUrl: '' };
       while (list.length < 9) {
         list.push({
           id: String(list.length + 1),
           picUrl: defaultImage.picUrl
         });
       }
       // 将数组分成三份
       const chunkSize = Math.ceil(list.length / 3);
       const chunk1 = list.slice(0, chunkSize);
       const chunk2 = list.slice(chunkSize, chunkSize * 2);
       const chunk3 = list.slice(chunkSize * 2);
       // 为每一份数据创建无缝列表
       const seamlessChunk1 = [chunk1[chunk1.length - 1], ...chunk1, chunk1[0], chunk1[1]] as imageList[];
       const seamlessChunk2 = [chunk2[chunk2.length - 1], ...chunk2, chunk2[0]] as imageList[];
       const seamlessChunk3 = [chunk3[chunk3.length - 1], ...chunk3, chunk3[0]] as imageList[];
       this.imageData1.dataArray = seamlessChunk1;
       this.imageData2.dataArray = seamlessChunk2;
       this.imageData3.dataArray = seamlessChunk3;
       this.imageData1.notifyDataReload();
       this.imageData2.notifyDataReload();
       this.imageData3.notifyDataReload();
     }

     build() {
       Column() {
         Refresh({ refreshing: $$this.isRefreshing }) {
           Scroll() {
             Column() {
               ForEach(this.arr, (item: string) => {
                 Row() {
                   Text('' + item)
                     .width('70%')
                     .height(80)
                     .fontSize(16)
                     .margin(10)
                     .textAlign(TextAlign.Center)
                     .borderRadius(10)
                     .backgroundColor('#ffdedbdb');
                 };
               }, (item: string) => item);
               Row({ space: 5 }) {
                 Swiper() {
                   LazyForEach(this.imageData1, (item: imageList) => {
                     // 开发者使用时将app.media.scene替换为需要展示的图片。
                     Image(item.picUrl || $r('app.media.scene'))
                       .width('100%')
                       .height(112)
                       .borderRadius(8)
                       .padding({ left: 15 })
                       .alt($r('app.media.scene'));
                   }, () => String(new Date().getTime()));
                 }
                 .width('33%')
                 .indicator(false)
                 .vertical(true)
                 .index(1)
                 .autoPlay(true)
                 .interval(0)
                 .duration(3000)
                 .loop(true)
                 .itemSpace(5)
                 .displayCount(3)
                 .curve(Curve.Linear)
                 .disableSwipe(true);

                 Swiper() {
                   LazyForEach(this.imageData1, (item: imageList) => {
                     // 开发者使用时将app.media.scene1替换为需要展示的图片。
                     Image(item.picUrl || $r('app.media.scene1'))
                       .width('100%')
                       .height(112)
                       .borderRadius(8)
                       .padding({ left: 10, right: 10 })
                       .alt($r('app.media.scene1'));
                   }, () => String(new Date().getTime()));
                 }
                 .width('33%')
                 .indicator(false)
                 .vertical(true)
                 .index(1)
                 .autoPlay(true)
                 .interval(0)
                 .duration(3000)
                 .loop(true)
                 .itemSpace(5)
                 .displayCount(3)
                 .curve(Curve.Linear)
                 .disableSwipe(true);

                 Swiper() {
                   LazyForEach(this.imageData3, (item: imageList) => {
                     // 开发者使用时将app.media.scene替换为需要展示的图片。
                     Image(item.picUrl || $r('app.media.scene'))
                       .width('100%')
                       .height(112)
                       .borderRadius(8)
                       .padding({ right: 15 })
                       .alt($r('app.media.scene'));
                   }, () => String(new Date().getTime()));
                 }
                 .width('33%')
                 .indicator(false)
                 .vertical(true)
                 .index(1)
                 .autoPlay(true)
                 .interval(0)
                 .duration(3000)
                 .loop(true)
                 .itemSpace(5)
                 .displayCount(3)
                 .curve(Curve.Linear)
                 .disableSwipe(true);

               }
               .width('100%')
               .height('40%');
             };
           };
         }
         .onRefreshing(() => {
           setTimeout(() => {
             this.updateImageList();
             this.isRefreshing = false;
           }, 500);
         })
         .backgroundColor(Color.White)
         .refreshOffset(64)
         .pullToRefresh(true);
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

   效果如下图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/0Ot3vLSvSXCeivmIzIlWZQ/zh-cn_image_0000002678018893.png "点击放大")
