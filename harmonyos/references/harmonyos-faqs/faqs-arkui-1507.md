---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1507
title: 实现朋友圈效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现朋友圈效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d003965dab58a808381234848039162303d0c73fc5e5f06acfaa6751a7062a9
---

## 问题现象

如何实现朋友圈效果？

## 效果预览

如下图所示（仅涉及UI，不涉及具体功能）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/cMFN3dHURAKRmDHth4EOjg/zh-cn_image_0000002658965767.png "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表组件包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)从数据源中按需迭代数据，并在每次迭代时创建相应组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。
* [Refresh](../harmonyos-references/ts-container-refresh.md)是一种可以进行页面下拉操作并显示刷新动效的容器组件。
* [@ObservedV2和@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)是状态管理V2中核心能力之一。该装饰器用于装饰类以及类中的属性，使得被装饰的类和属性具有深度观测的能力。

## 解决方案

1. 在主页面创建Refresh组件，并在该组件中使用LazyForEach对MomentListItem进行渲染，并按特定方式实现图片和视频组件的交替渲染，这是该demo的框架功能实现。

   ```screen
   Refresh({ refreshing: $$this.isRefreshing }) {
     List({ space: 20 }) {
       LazyForEach(this.listDataSource, (item: MomentItem) => {
         ListItem() {
           MomentListItem({
             data: item
           });
         }
         .padding({ left: 14, right: 14 })
         .backgroundColor(Color.White)
         .borderRadius(16);
       });
     }
     .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
     .width('100%')
     .height('100%')
     .padding({ left: 14, right: 14 });
   }
   .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
   .onRefreshing(() => {
     setTimeout(() => {
       this.isRefreshing = false;
     }, 1000);
   })
   .pullToRefresh(true);
   ```
2. 在MomentListItem组件中，对用户昵称，头像，时间以及文案内容，评论，点赞进行展示，并根据data属性的不同，进行图片和视频的展示。

   具体代码展示如下，以下各代码文件均位于pages目录下：

   Moment.ets：

   ```screen
   import { CommonDataSource } from './CommonDataSource';
   import { MomentItem } from './ListModel';
   import { MomentListItem } from './MomentListItem';

   @Entry
   @Component
   struct Moments {
     @State isRefreshing: boolean = false;
     private listDataSource = new CommonDataSource<MomentItem>();

     aboutToAppear(): void {
       this.getListData();
     }

     getListData() {
       let followList: MomentItem[] = [];
       for (let i = 0; i < 10; i++) {
         // 此处'itemData值'仅作示例
         let itemData: MomentItem = new MomentItem();
         itemData.id = 'id_' + i;
         itemData.userId = 'userId_' + i;
         // 此处资源文件仅作展示，根据实际情况可自行替换
         itemData.userName = $r('app.string.userName');
         itemData.postingTime = '2025/07/09 10:30:00';
         itemData.isFollow = false;
         if (i % 2 === 0) {
           // 此处资源文件仅作展示，根据实际情况可自行替换
           itemData.title = $r('app.string.content1');
           itemData.images = [
           // 此处图片资源仅作展示，根据实际情况可自行替换
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
             $r('app.media.img'),
           ];
         } else {
           // 此处'video.mp4'仅作示例
           itemData.videoUrl = $rawfile('video.mp4');
           // 此处资源文件仅作展示，根据实际情况可自行替换
           itemData.title = $r('app.string.content2');
         }
         followList.push(itemData);
       }
       this.listDataSource.setData(followList);
     }

     @Builder
     ListContent() {
       Refresh({ refreshing: $$this.isRefreshing }) {
         List({ space: 20 }) {
           LazyForEach(this.listDataSource, (item: MomentItem) => {
             ListItem() {
               MomentListItem({
                 data: item
               });
             }
             .padding({ left: 14, right: 14 })
             .backgroundColor(Color.White)
             .borderRadius(16);
           });
         }
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
         .width('100%')
         .height('100%')
         .padding({ left: 14, right: 14 });
       }
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
       .onRefreshing(() => {
         setTimeout(() => {
           this.isRefreshing = false;
         }, 1000);
       })
       .pullToRefresh(true);

     }

     build() {
       Column() {
         this.ListContent();
       }
       .width('100%')
       .height('100%')
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
       .backgroundColor('#f1f3f5');
     }
   }
   ```

   ListModel.ets：

   ```screen
   @ObservedV2
   export class MomentItem {
     id: string = '';
     userId: string = '';
     @Trace userName: ResourceStr = '';
     // 此处图片资源仅作展示，根据实际情况可自行替换
     @Trace userIcon: Resource = $r('app.media.avatar');
     @Trace title: ResourceStr = '';
     @Trace postingTime: string = '';
     @Trace isFollow: boolean = false;
     @Trace images: Resource[] = [];
     @Trace videoUrl: Resource | string = '';
     @Trace videoPreviewUrl: Resource | string = '';
     @Trace likeCount: number = 0;
     @Trace shareCount: number = 0;
     @Trace commentCount: number = 0;
     favorite: number = 0;
   }
   ```

   MomentListItem.ets：

   ```screen
   import { MomentItem } from './ListModel';

   @Component
   export struct MomentListItem {
     data: MomentItem | null = null;
     controller: VideoController = new VideoController();
     isPlay: boolean = false;

     getPostingTime(time: string = ''): string {
       let date: Date = new Date(time);

       let M: number = date.getMonth() + 1;
       let D: number = date.getDate();
       let h: number = date.getHours();
       let m: number = date.getMinutes();

       return `${M}-${D} ${h}:${m}`;
     }

     build() {
       Column() {
         Row() {
           Image(this.data?.userIcon).width(30).height(30);
           Column() {
             Text(this.data?.userName)
               .fontSize(13)
               .fontColor('#e6000000')
               .fontWeight(FontWeight.Bold);
             Text(this.getPostingTime(this.data?.postingTime))
               .fontSize(10)
               .fontColor('#99000000')
               .margin({ top: 2 });
           }
           .offset({ x: 8 })
           .alignItems(HorizontalAlign.Start);
         }
         .width('100%');

         Text(this.data?.title)
           .fontSize(16)
           .width('100%')
           .fontColor('#e6000000')
           .margin({ top: 12 });

         Column() {
           if (this.data?.images && this.data.images.length) {
             if (this.data.images.length > 2) {
               this.imageGridBuilder(this.data.images);
             } else {
               this.imageBuilder(this.data.images);
             }
           }
           if (this.data?.videoUrl) {
             this.videoBuilder(this.data);
           }
         }
         .margin({ top: 8 })
         .alignItems(HorizontalAlign.Start);

         // 判断是否存在评论
         if (true) {
           Column({ space: 10 }) {
             ForEach([1, 2, 3], () => {
               this.CommentListView();
             });
             // 判断评论数量是否超过3条
             if (true) {
               Text('查看更多回复')
                 .fontColor('#0A59F7')
                 .fontSize(12)
                 .margin({ left: 38 })
                 .onClick(() => {
                 });
             }
           }
           .padding({
             left: 14,
             right: 14,
             top: 14,
             bottom: 12
           })
           .backgroundColor('#F1F3F5')
           .margin({ top: 10 })
           .borderRadius(12)
           .alignItems(HorizontalAlign.Start);
         }
       }
       .width('100%')
       .height('auto')
       .borderRadius(16)
       .padding({ bottom: 16 })
       .margin({ top: 16 });
     }

     @Builder
     CommentListView() {
       Column() {
         Row() {
           Image(this.data?.userIcon).width(30).height(30);
           Column() {
             Text(this.data?.userName).fontSize(12).fontColor('#e6000000');
             Text(this.getPostingTime(this.data?.postingTime))
               .fontSize(10)
               .fontColor('#99000000')
               .margin({ top: 2 });
           }
           .alignItems(HorizontalAlign.Start)
           .offset({ x: 8 });
         }
         .width('100%');

         Text(this.data?.title)
           .fontSize(12)
           .margin({ left: 38 });
       }
       .width('100%')
       .alignItems(HorizontalAlign.Start);
     }

     @Builder
     imageBuilder(images: Resource[]) {
       Row({ space: 6 }) {
         ForEach(images, (item: Resource) => {
           Image(item).width(`${100 / 2}%`);
         });
       };
     }

     @Builder
     imageGridBuilder(images: Resource[]) {
       Grid() {
         ForEach(images, (item: Resource) => {
           GridItem() {
             Column() {
               Image(item)
                 .borderRadius(4)
                 .width('calc((100% - 16vp) / 3)')
                 .aspectRatio(1);
             }
             .onClick(() => {
             });
           };
         });
       }
       .width('100%')
       .constraintSize({ maxWidth: '100%' })
       .maxCount(3)
       .columnsGap(8)
       .rowsGap(8)
       .backgroundColor(Color.White);
     }

     @Builder
     videoBuilder(item: MomentItem) {
       Stack() {
         Video({ src: item.videoUrl, controller: this.controller })
           .width('50%')
           .height(220)
           .loop(false)
           .objectFit(ImageFit.Contain)
           .autoPlay(true)
           .controls(false);
       }
       .onClick(() => {
         this.isPlay = !this.isPlay;
         if (this.isPlay) {
           this.controller.start();
         } else {
           this.controller.pause();
         }
       });
     }

     @Builder
     cellItemBuilder(icon: Resource, text: string) {
       Row() {
         Image(icon).width(16).height(16);
         Text(text).fontSize(12).margin({ left: 2 });
       };
     }
   }
   ```

   CommonDataSource.ets：

   ```screen
   export class CommonDataSource<T> implements IDataSource {
     private listeners: DataChangeListener[] = [];
     originDataArray: T[] = [];

     totalCount(): number {
       return this.originDataArray.length;
     }

     getAllData(): T[] {
       return this.originDataArray;
     }

     getData(index: number) {
       return this.originDataArray[index];
     }

     addData(index: number, data: T): void {
       this.originDataArray.splice(index, 0, data);
       this.notifyDataAdd(index);
     }

     pushData(data: T): void {
       this.originDataArray.push(data);
       this.notifyDataAdd(this.originDataArray.length - 1);
     }

     pushDataArray(...items: T[]): void {
       for (let data of items) {
         this.originDataArray.push(data);
         this.notifyDataAdd(this.originDataArray.length - 1);
       }
     }

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

     deleteData(index: number): void {
       this.originDataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     clear() {
       this.originDataArray.splice(0, this.originDataArray.length);
       this.listeners.forEach(listener => {
         listener.onDataDelete(0);
       });
     }

     setData(dataArray?: T[]) {
       if (dataArray) {
         this.originDataArray = dataArray;
       } else {
         this.originDataArray = [];
       }
       this.notifyDataReload();
     }

     refreshDataByIndex(start: number, end: number, dataArray: T[]) {
       this.originDataArray.splice(start, end - start, ...dataArray);
       this.notifyDataReload();
     }

     changeData(index: number, data: T): void {
       this.originDataArray.splice(index, 1, data);
       this.notifyDataChange(index);
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

## 总结

该demo主要使用LazyForEach对List数据元素进行渲染展示，对相关内容使用ArkTS组件中的通用位置属性进行布局，是一个较为综合的案例。
