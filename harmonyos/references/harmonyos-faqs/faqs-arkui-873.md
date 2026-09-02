---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-873
title: 标题栏与底部的列表条目无法一起滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 标题栏与底部的列表条目无法一起滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:49e7db4b3bdbf4c7c0a70ba7366147ce2af609df189a95273d367c8f937bb95a
---

## 问题现象

在页面结构中，存在一个标题栏和多个底部列表条目。当用户横向滑动标题栏时，底部对应的列表条目未能同步滑动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/egKmdPlkQ72CSr_beQCowQ/zh-cn_image_0000002722988121.png "点击放大")

## 背景知识

* 当主组件滚动时，可通过控制器ScrollController动态设置组件（列表条目）的滚动位置。
* [onScrollFrameBegin](../harmonyos-references/ts-container-list.md#onscrollframebegin9)该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。

## 问题定位

1. 检查滚动组件绑定：查看标题栏和列表条目的代码实现，检查是否有ScrollController。
2. 验证事件传递：若使用ScrollController，则在标题栏的滚动回调函数中打印日志，检查底部条目是否滑动。

## 分析结论

标题栏的滑动事件未传递到底部条目的原因有：

1. 条目未绑定控制器：列表条目的Scroll未挂载控制器，无法接受外部滚动指令。
2. 事件未同步调用：标题栏的滚动回调未遍历调用所有条目的控制器方法。

## 修改建议

1. 为每个列表条目添加控制器：为每个条目的滚动容器初始化独立的控制器，并存储到全局集合中。

   ```ts
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   const leftItemWidth = 100;
   const rightItemWidth = 100;
   const itemHeight = 90;
   const groupHeight = 50;

   @Component
   struct ItemComponent {
     private arr: string[] = [
       '1', '2', '3', '4', '5', '6', '7', '8'];
     dataSource = new CommonDataSource<string>();
     scroller?: Scroller = undefined;
     scrollCallBack?: (param: number) => void;
     remainOffsetCallBack?: (param: number) => void;

     aboutToAppear(): void {
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true); // 设置页面全屏
       });
       this.dataSource.setData(this.arr);
     }

     // 下部分参数列表每行数据List
     @Builder
     rightSingleLineList() {
       List({ scroller: this.scroller }) {
         LazyForEach(this.dataSource, (item: string) => {
           ListItem() {
             Text(item)
               .height('100%')
               .width('100%')
               .fontSize(16)
               .textAlign(TextAlign.Start)
               .borderRadius(0)
               .padding(10)
               .backgroundColor(0xFFFFFF);
           }
           .width(rightItemWidth);
         }, (item: string) => item);
       }
       .height('100%')
       .width('100%')
       .layoutWeight(1)
       .listDirection(Axis.Horizontal)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .divider({ strokeWidth: 0.5, color: 0xeeeeee }) // 每行之间的分界线
       .edgeEffect(EdgeEffect.None) // 边缘效果设置为Spring
       .onDidScroll(() => {
         // 通过callBack回调行在横向滚动时，Scroller当前的offset
         if (this.remainOffsetCallBack) {
           this.remainOffsetCallBack(this.scroller!.currentOffset().xOffset);
         }
       })
       .onScrollFrameBegin((offset: number) => {
         if (this.scrollCallBack) {
           this.scrollCallBack(this.scroller!.currentOffset().xOffset + offset);
         }
         return { offsetRemain: offset };
       });
     }

     build() {
       Column() {
         this.rightSingleLineList();
         Line().width('100%').height(0.5).backgroundColor(0xeeeeee);
       }.height(itemHeight);
     }
   }

   @Entry
   @Component
   export struct Compare {
     private topRightArr: string[] = [
       '苹果', '香蕉', '橙子', '草莓', '芒果', '葡萄', '西瓜', '桃子'];
     // 参数行在横向滚动时的offset
     @State remainOffset: number = 0;
     private bottomRightScroller: Scroller = new Scroller();
     private bottomLeftScroller: Scroller = new Scroller();
     private topRightScroller: Scroller = new Scroller();
     private showDataArray: ShowData[] = [];
     private dataSource = new CommonDataSource<ShowData>();
     private leftItems: string[] = [
       '市场零售价',
       '原产地',
       '水果等级',
       '品种类型',
       '上市季节',
       '核心品种',
       '甜度指数',
       '果径大小',
       '保鲜方式',
       '外形特征',
       '果皮类型',
       '最佳储存温度',
       '成熟周期',
       '糖度含量',
       '实测酸度',
       '保质期限',
       '运输成本'
     ];

     aboutToAppear(): void {
       this.loadData();
     }

     private async loadData() {
       // 水果数据
       let resp: DataItem[] = [
         {
           'sticky': '营养成分',
           'sub': ['热量', '糖分', '维生素', '膳食纤维', '水分含量']
         },
         {
           'sticky': '外观特征',
           'sub': ['颜色', '形状', '大小', '重量', '表皮质地']
         },
         {
           'sticky': '口感风味',
           'sub': ['甜度', '酸度', '香味', '口感', '汁水']
         }
       ];
       for (let i = 0; i < resp.length; i++) {
         let item = resp[i];
         let showData = new ShowData();
         showData.sticky = item.sticky;
         showData.sub = item.sub;
         showData.sub!.forEach(() => {
           let scroller: Scroller = new Scroller();
           showData.scrollerArray!.push(scroller);
         });
         this.showDataArray.push(showData);
       }
       this.dataSource.setData(this.showDataArray);
     }

     build() {
       Column() {
         // 上部分
         this.topFixed();
         // 下部分
         Row() {
           this.leftList();
           this.rightList();
           Line()
             .height('100%')
             .width(0.5)
             .backgroundColor('#EEEEEE')
             .position({ x: leftItemWidth });
         }
         .justifyContent(FlexAlign.Start)
         .alignItems(VerticalAlign.Top);
       }
       .height('100%')
       .justifyContent(FlexAlign.Start)
       .alignItems(HorizontalAlign.Start);
     }

     @Builder
     // 修改leftStickyHeader方法
     leftStickyHeader(title: string) {
       Text(title)
         .width(leftItemWidth)
         .height(groupHeight)
         .backgroundColor('#f1f3f5')
         .textAlign(TextAlign.Center)
         .border({ width: 1 });
     }

     // 上部分整体Row(Column + List)
     @Builder
     topFixed() {
       Row() {
         // 上部分左侧固定信息
         Column() {
           Text('水果')
             .fontSize(15);
         }
         .width(leftItemWidth)
         .height(100)
         .backgroundColor(Color.White)
         .justifyContent(FlexAlign.Center)
         .alignItems(HorizontalAlign.Start)
         .padding(10);

         // 分割线
         Line()
           .height(100)
           .width(0.5)
           .backgroundColor(0xeeeeee);
         // 上部分右侧车型横向滚动列表
         List({ scroller: this.topRightScroller/* 绑定Scroller控制器与其他控制器联动*/ }) {
           ForEach(this.topRightArr, (item: string) => {
             ListItem() {
               Text(item)
                 .height(100)
                 .width(rightItemWidth)
                 .fontSize(16)
                 .textAlign(TextAlign.Start)
                 .borderRadius(0)
                 .padding(10)
                 .backgroundColor(0xFFFFFF);
             };
           }, (item: string) => item);
         }
         .listDirection(Axis.Horizontal) // 设置滚动方向为横向滚动
         .edgeEffect(EdgeEffect.None)
         .divider({ strokeWidth: 0.5, color: 0xeeeeee })
         .scrollBar(BarState.Off)
         .width('100%')
         .height('100%')
         .layoutWeight(1)
         .onScrollFrameBegin((offset: number) => {
           // 关键联动，通过对象保存的Scroller控制器数组遍历保持offset同步
           this.dataSource.getAllData().forEach(showData => {
             showData.scrollerArray!.forEach(scroller => {
               scroller.scrollTo({ xOffset: this.topRightScroller.currentOffset().xOffset + offset, yOffset: 0 });
             });
           });
           return { offsetRemain: offset };
         });

       }
       .height(100)
       .width('100%');
     }

     // 下部分左侧行标题列表纵向滚动List
     @Builder
     leftList() {
       List({ scroller: this.bottomLeftScroller/* 绑定控制器与其他控制器联动*/ }) {
         ForEach(this.leftItems, (item: string) => {
           ListItem() {
             Text(item)
               .width(leftItemWidth)
               .height(itemHeight)
               .textAlign(TextAlign.Center);
           };
         }, (item: string) => item);

       }
       .sticky(StickyStyle.Header)
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .edgeEffect(EdgeEffect.None)
       .height('calc(100% - 100vp)')
       .width(leftItemWidth)
       .onScrollFrameBegin((offset: number) => {
         // 带动右侧纵向Scroll组件绑定的Scroller控制器同步滑动
         this.bottomRightScroller.scrollTo({
           xOffset: 0,
           yOffset: this.bottomLeftScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       });
     }

     // 下部分右侧内容显示区域纵向List(ListItem(List))
     @Builder
     rightList() {
       List({ initialIndex: 0, scroller: this.bottomRightScroller }) {
         // 通过LazyForEach加载每一行
         LazyForEach(this.dataSource, (item: ShowData) => {
           ListItemGroup({}) {
             ForEach(item.sub, (subItem: string) => {
               // 自定义ListItem中包含横向滚动List
               ItemComponent({
                 scroller: item.scrollerArray![item.sub!.indexOf(subItem)],
                 scrollCallBack: (value) => {
                   // value为子List横向滚动onScrollFrameBegin回传offset，在手指拖动时保持联动一致
                   // 顶部车型List跟随联动
                   this.topRightScroller.scrollTo({ xOffset: value, yOffset: 0 });
                   // 通过对象保存的Scroller数组跟随保持联动
                   this.dataSource.getAllData().forEach(showData => {
                     showData.scrollerArray!.forEach(scroller => {
                       if (scroller !== item.scrollerArray![item.sub!.indexOf(subItem)]) {
                         scroller.scrollTo({ xOffset: value, yOffset: 0 });
                       }
                     });
                   });
                 },
                 remainOffsetCallBack: (value) => {
                   // 滚动过程中回传保持同步的offset值
                   this.remainOffset = value;
                 }
               });
             }, (item: string) => item);
           };

         }, (item: ShowData, index: number) => item.sticky! + index);
       }
       .sticky(StickyStyle.Header)
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .edgeEffect(EdgeEffect.None)
       .onScrollFrameBegin((offset: number) => {
         // 内容List纵向滚动带动左侧标题List跟随滚动
         this.bottomLeftScroller.scrollTo({
           xOffset: 0,
           yOffset: this.bottomRightScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       })
       .onDidScroll(() => {
         // 内容List纵向滚动过程中，每一行中子List的Scroller滚动到remainOffset与已显示的行位置保持一致
         this.dataSource.getAllData().forEach(showData => {
           showData.scrollerArray!.forEach(scroller => {
             scroller.scrollTo({ xOffset: this.remainOffset, yOffset: 0 });
           });
         });
       })

       .position({ x: leftItemWidth, y: 0 })
       .edgeEffect(EdgeEffect.None) // 边缘效果设置为Spring
       .backgroundColor(0xDCDCDC)
       .height('calc(100% - 100vp)')
       .width('calc(100% - 100vp)');
     }
   }

   class ShowData {
     sticky?: string;
     sub?: string[];
     scrollerArray?: Scroller[] = [];
   }

   export class CommonDataSource<T> implements IDataSource {
     private listeners: DataChangeListener[] = [];
     protected originDataArray: T[] = [];

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
       if (delIndex != -1) {
         this.deleteData(delIndex);
       }
     }

     deleteData(index: number): void {
       this.originDataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     setData(dataArray?: T[]) {
       if (dataArray) {
         this.originDataArray = dataArray;
       } else {
         this.originDataArray = [];
       }
       this.notifyDataReload();
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
   }

   interface DataItem {
     sticky: string;
     sub: string [];
   }
   ```
2. 标题栏滚动时同步调用条目控制器：在标题栏的滚动监听中，遍历所有条目控制器并设置相同滚动位置。

   ```ts
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   const leftItemWidth = 100;
   const rightItemWidth = 100;
   const itemHeight = 90;
   const groupHeight = 50;

   @Component
   struct ItemComponent {
     private arr: string[] = [
       '1', '2', '3', '4', '5', '6', '7', '8'];
     dataSource = new CommonDataSource<string>();
     scroller?: Scroller = undefined;
     scrollCallBack?: (param: number) => void;
     remainOffsetCallBack?: (param: number) => void;

     aboutToAppear(): void {
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true); // 设置页面全屏
       });
       this.dataSource.setData(this.arr);
     }

     // 下部分参数列表每行数据List
     @Builder
     rightSingleLineList() {
       List({ scroller: this.scroller }) {
         LazyForEach(this.dataSource, (item: string) => {
           ListItem() {
             Text(item)
               .height('100%')
               .width('100%')
               .fontSize(16)
               .textAlign(TextAlign.Start)
               .borderRadius(0)
               .padding(10)
               .backgroundColor(0xFFFFFF);
           }
           .width(rightItemWidth);
         }, (item: string) => item);
       }
       .height('100%')
       .width('100%')
       .layoutWeight(1)
       .listDirection(Axis.Horizontal)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .divider({ strokeWidth: 0.5, color: 0xeeeeee }) // 每行之间的分界线
       .edgeEffect(EdgeEffect.None) // 边缘效果设置为Spring
       .onDidScroll(() => {
         // 通过callBack回调行在横向滚动时，Scroller当前的offset
         if (this.remainOffsetCallBack) {
           this.remainOffsetCallBack(this.scroller!.currentOffset().xOffset);
         }
       })
       .onScrollFrameBegin((offset: number) => {
         if (this.scrollCallBack) {
           this.scrollCallBack(this.scroller!.currentOffset().xOffset + offset);
         }
         return { offsetRemain: offset };
       });
     }

     build() {
       Column() {
         this.rightSingleLineList();
         Line().width('100%').height(0.5).backgroundColor(0xeeeeee);
       }.height(itemHeight);
     }
   }

   @Entry
   @Component
   export struct Compare {
     private topRightArr: string[] = [
       '苹果', '香蕉', '橙子', '草莓', '芒果', '葡萄', '西瓜', '桃子'];
     // 参数行在横向滚动时的offset
     @State remainOffset: number = 0;
     private bottomRightScroller: Scroller = new Scroller();
     private bottomLeftScroller: Scroller = new Scroller();
     private topRightScroller: Scroller = new Scroller();
     private showDataArray: ShowData[] = [];
     private dataSource = new CommonDataSource<ShowData>();
     private leftItems: string[] = [
       '市场零售价',
       '原产地',
       '水果等级',
       '品种类型',
       '上市季节',
       '核心品种',
       '甜度指数',
       '果径大小',
       '保鲜方式',
       '外形特征',
       '果皮类型',
       '最佳储存温度',
       '成熟周期',
       '糖度含量',
       '实测酸度',
       '保质期限',
       '运输成本'
     ];

     aboutToAppear(): void {
       this.loadData();
     }

     private async loadData() {
       // 水果数据
       let resp: DataItem[] = [
         {
           'sticky': '营养成分',
           'sub': ['热量', '糖分', '维生素', '膳食纤维', '水分含量']
         },
         {
           'sticky': '外观特征',
           'sub': ['颜色', '形状', '大小', '重量', '表皮质地']
         },
         {
           'sticky': '口感风味',
           'sub': ['甜度', '酸度', '香味', '口感', '汁水']
         }
       ];
       for (let i = 0; i < resp.length; i++) {
         let item = resp[i];
         let showData = new ShowData();
         showData.sticky = item.sticky;
         showData.sub = item.sub;
         showData.sub!.forEach(() => {
           let scroller: Scroller = new Scroller();
           showData.scrollerArray!.push(scroller);
         });
         this.showDataArray.push(showData);
       }
       this.dataSource.setData(this.showDataArray);
     }

     build() {
       Column() {
         // 上部分
         this.topFixed();
         // 下部分
         Row() {
           this.leftList();
           this.rightList();
           Line()
             .height('100%')
             .width(0.5)
             .backgroundColor('#EEEEEE')
             .position({ x: leftItemWidth });
         }
         .justifyContent(FlexAlign.Start)
         .alignItems(VerticalAlign.Top);
       }
       .height('100%')
       .justifyContent(FlexAlign.Start)
       .alignItems(HorizontalAlign.Start);
     }

     @Builder
     // 修改leftStickyHeader方法
     leftStickyHeader(title: string) {
       Text(title)
         .width(leftItemWidth)
         .height(groupHeight)
         .backgroundColor('#f1f3f5')
         .textAlign(TextAlign.Center)
         .border({ width: 1 });
     }

     // 上部分整体Row(Column + List)
     @Builder
     topFixed() {
       Row() {
         // 上部分左侧固定信息
         Column() {
           Text('水果')
             .fontSize(15);
         }
         .width(leftItemWidth)
         .height(100)
         .backgroundColor(Color.White)
         .justifyContent(FlexAlign.Center)
         .alignItems(HorizontalAlign.Start)
         .padding(10);

         // 分割线
         Line()
           .height(100)
           .width(0.5)
           .backgroundColor(0xeeeeee);
         // 上部分右侧车型横向滚动列表
         List({ scroller: this.topRightScroller/* 绑定Scroller控制器与其他控制器联动*/ }) {
           ForEach(this.topRightArr, (item: string) => {
             ListItem() {
               Text(item)
                 .height(100)
                 .width(rightItemWidth)
                 .fontSize(16)
                 .textAlign(TextAlign.Start)
                 .borderRadius(0)
                 .padding(10)
                 .backgroundColor(0xFFFFFF);
             };
           }, (item: string) => item);
         }
         .listDirection(Axis.Horizontal) // 设置滚动方向为横向滚动
         .edgeEffect(EdgeEffect.None)
         .divider({ strokeWidth: 0.5, color: 0xeeeeee })
         .scrollBar(BarState.Off)
         .width('100%')
         .height('100%')
         .layoutWeight(1)
         .onScrollFrameBegin((offset: number) => {
           // 关键联动，通过对象保存的Scroller控制器数组遍历保持offset同步
           this.dataSource.getAllData().forEach(showData => {
             showData.scrollerArray!.forEach(scroller => {
               scroller.scrollTo({ xOffset: this.topRightScroller.currentOffset().xOffset + offset, yOffset: 0 });
             });
           });
           return { offsetRemain: offset };
         });

       }
       .height(100)
       .width('100%');
     }

     // 下部分左侧行标题列表纵向滚动List
     @Builder
     leftList() {
       List({ scroller: this.bottomLeftScroller/* 绑定控制器与其他控制器联动*/ }) {
         ForEach(this.leftItems, (item: string) => {
           ListItem() {
             Text(item)
               .width(leftItemWidth)
               .height(itemHeight)
               .textAlign(TextAlign.Center);
           };
         }, (item: string) => item);

       }
       .sticky(StickyStyle.Header)
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .edgeEffect(EdgeEffect.None)
       .height('calc(100% - 100vp)')
       .width(leftItemWidth)
       .onScrollFrameBegin((offset: number) => {
         // 带动右侧纵向Scroll组件绑定的Scroller控制器同步滑动
         this.bottomRightScroller.scrollTo({
           xOffset: 0,
           yOffset: this.bottomLeftScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       });
     }

     // 下部分右侧内容显示区域纵向List(ListItem(List))
     @Builder
     rightList() {
       List({ initialIndex: 0, scroller: this.bottomRightScroller }) {
         // 通过LazyForEach加载每一行
         LazyForEach(this.dataSource, (item: ShowData) => {
           ListItemGroup({}) {
             ForEach(item.sub, (subItem: string) => {
               // 自定义ListItem中包含横向滚动List
               ItemComponent({
                 scroller: item.scrollerArray![item.sub!.indexOf(subItem)],
                 scrollCallBack: (value) => {
                   // value为子List横向滚动onScrollFrameBegin回传offset，在手指拖动时保持联动一致
                   // 顶部车型List跟随联动
                   this.topRightScroller.scrollTo({ xOffset: value, yOffset: 0 });
                   // 通过对象保存的Scroller数组跟随保持联动
                   this.dataSource.getAllData().forEach(showData => {
                     showData.scrollerArray!.forEach(scroller => {
                       if (scroller !== item.scrollerArray![item.sub!.indexOf(subItem)]) {
                         scroller.scrollTo({ xOffset: value, yOffset: 0 });
                       }
                     });
                   });
                 },
                 remainOffsetCallBack: (value) => {
                   // 滚动过程中回传保持同步的offset值
                   this.remainOffset = value;
                 }
               });
             }, (item: string) => item);
           };

         }, (item: ShowData, index: number) => item.sticky! + index);
       }
       .sticky(StickyStyle.Header)
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .edgeEffect(EdgeEffect.None)
       .onScrollFrameBegin((offset: number) => {
         // 内容List纵向滚动带动左侧标题List跟随滚动
         this.bottomLeftScroller.scrollTo({
           xOffset: 0,
           yOffset: this.bottomRightScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       })
       .onDidScroll(() => {
         // 内容List纵向滚动过程中，每一行中子List的Scroller滚动到remainOffset与已显示的行位置保持一致
         this.dataSource.getAllData().forEach(showData => {
           showData.scrollerArray!.forEach(scroller => {
             scroller.scrollTo({ xOffset: this.remainOffset, yOffset: 0 });
           });
         });
       })

       .position({ x: leftItemWidth, y: 0 })
       .edgeEffect(EdgeEffect.None) // 边缘效果设置为Spring
       .backgroundColor(0xDCDCDC)
       .height('calc(100% - 100vp)')
       .width('calc(100% - 100vp)');
     }
   }

   class ShowData {
     sticky?: string;
     sub?: string[];
     scrollerArray?: Scroller[] = [];
   }

   export class CommonDataSource<T> implements IDataSource {
     private listeners: DataChangeListener[] = [];
     protected originDataArray: T[] = [];

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
       if (delIndex != -1) {
         this.deleteData(delIndex);
       }
     }

     deleteData(index: number): void {
       this.originDataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     setData(dataArray?: T[]) {
       if (dataArray) {
         this.originDataArray = dataArray;
       } else {
         this.originDataArray = [];
       }
       this.notifyDataReload();
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
   }

   interface DataItem {
     sticky: string;
     sub: string [];
   }
   ```
3. 为标题栏添加背景色：为标题栏组件设置背景色，避免列表内容透过标题栏显示。

   完整代码如下：

   ```ts
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   const leftItemWidth = 100;
   const rightItemWidth = 100;
   const itemHeight = 90;
   const groupHeight = 50;

   @Component
   struct ItemComponent {
     private arr: string[] = [
       '1', '2', '3', '4', '5', '6', '7', '8'];
     dataSource = new CommonDataSource<string>();
     scroller?: Scroller = undefined;
     scrollCallBack?: (param: number) => void;
     remainOffsetCallBack?: (param: number) => void;

     aboutToAppear(): void {
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true); // 设置页面全屏
       });
       this.dataSource.setData(this.arr);
     }

     // 下部分参数列表每行数据List
     @Builder
     rightSingleLineList() {
       List({ scroller: this.scroller }) {
         LazyForEach(this.dataSource, (item: string) => {
           ListItem() {
             Text(item)
               .height('100%')
               .width('100%')
               .fontSize(16)
               .textAlign(TextAlign.Start)
               .borderRadius(0)
               .padding(10)
               .backgroundColor(0xFFFFFF);
           }
           .width(rightItemWidth);
         }, (item: string) => item);
       }
       .height('100%')
       .width('100%')
       .layoutWeight(1)
       .listDirection(Axis.Horizontal)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .divider({ strokeWidth: 0.5, color: 0xeeeeee }) // 每行之间的分界线
       .edgeEffect(EdgeEffect.None) // 边缘效果设置为Spring
       .onDidScroll(() => {
         // 通过callBack回调行在横向滚动时，Scroller当前的offset
         if (this.remainOffsetCallBack) {
           this.remainOffsetCallBack(this.scroller!.currentOffset().xOffset);
         }
       })
       .onScrollFrameBegin((offset: number) => {
         if (this.scrollCallBack) {
           this.scrollCallBack(this.scroller!.currentOffset().xOffset + offset);
         }
         return { offsetRemain: offset };
       });
     }

     build() {
       Column() {
         this.rightSingleLineList();
         Line().width('100%').height(0.5).backgroundColor(0xeeeeee);
       }.height(itemHeight);
     }
   }

   @Entry
   @Component
   export struct Compare {
     private topRightArr: string[] = [
       '苹果', '香蕉', '橙子', '草莓', '芒果', '葡萄', '西瓜', '桃子'];
     // 参数行在横向滚动时的offset
     @State remainOffset: number = 0;
     private bottomRightScroller: Scroller = new Scroller();
     private bottomLeftScroller: Scroller = new Scroller();
     private topRightScroller: Scroller = new Scroller();
     private showDataArray: ShowData[] = [];
     private dataSource = new CommonDataSource<ShowData>();
     private leftItems: string[] = [
       '市场零售价',
       '原产地',
       '水果等级',
       '品种类型',
       '上市季节',
       '核心品种',
       '甜度指数',
       '果径大小',
       '保鲜方式',
       '外形特征',
       '果皮类型',
       '最佳储存温度',
       '成熟周期',
       '糖度含量',
       '实测酸度',
       '保质期限',
       '运输成本'
     ];

     aboutToAppear(): void {
       this.loadData();
     }

     private async loadData() {
       // 水果数据
       let resp: DataItem[] = [
         {
           'sticky': '营养成分',
           'sub': ['热量', '糖分', '维生素', '膳食纤维', '水分含量']
         },
         {
           'sticky': '外观特征',
           'sub': ['颜色', '形状', '大小', '重量', '表皮质地']
         },
         {
           'sticky': '口感风味',
           'sub': ['甜度', '酸度', '香味', '口感', '汁水']
         }
       ];
       for (let i = 0; i < resp.length; i++) {
         let item = resp[i];
         let showData = new ShowData();
         showData.sticky = item.sticky;
         showData.sub = item.sub;
         showData.sub!.forEach(() => {
           let scroller: Scroller = new Scroller();
           showData.scrollerArray!.push(scroller);
         });
         this.showDataArray.push(showData);
       }
       this.dataSource.setData(this.showDataArray);
     }

     build() {
       Column() {
         // 上部分
         this.topFixed();
         // 下部分
         Row() {
           this.leftList();
           this.rightList();
           Line()
             .height('100%')
             .width(0.5)
             .backgroundColor('#EEEEEE')
             .position({ x: leftItemWidth });
         }
         .justifyContent(FlexAlign.Start)
         .alignItems(VerticalAlign.Top);
       }
       .height('100%')
       .justifyContent(FlexAlign.Start)
       .alignItems(HorizontalAlign.Start);
     }

     @Builder
     // 修改leftStickyHeader方法
     leftStickyHeader(title: string) {
       Text(title)
         .width(leftItemWidth)
         .height(groupHeight)
         .backgroundColor('#f1f3f5')
         .textAlign(TextAlign.Center)
         .border({ width: 1 });
     }

     // 上部分整体Row(Column + List)
     @Builder
     topFixed() {
       Row() {
         // 上部分左侧固定信息
         Column() {
           Text('水果')
             .fontSize(15);
         }
         .width(leftItemWidth)
         .height(100)
         .backgroundColor(Color.White)
         .justifyContent(FlexAlign.Center)
         .alignItems(HorizontalAlign.Start)
         .padding(10);

         // 分割线
         Line()
           .height(100)
           .width(0.5)
           .backgroundColor(0xeeeeee);
         // 上部分右侧车型横向滚动列表
         List({ scroller: this.topRightScroller/* 绑定Scroller控制器与其他控制器联动*/ }) {
           ForEach(this.topRightArr, (item: string) => {
             ListItem() {
               Text(item)
                 .height(100)
                 .width(rightItemWidth)
                 .fontSize(16)
                 .textAlign(TextAlign.Start)
                 .borderRadius(0)
                 .padding(10)
                 .backgroundColor(0xFFFFFF);
             };
           }, (item: string) => item);
         }
         .listDirection(Axis.Horizontal) // 设置滚动方向为横向滚动
         .edgeEffect(EdgeEffect.None)
         .divider({ strokeWidth: 0.5, color: 0xeeeeee })
         .scrollBar(BarState.Off)
         .width('100%')
         .height('100%')
         .layoutWeight(1)
         .onScrollFrameBegin((offset: number) => {
           // 关键联动，通过对象保存的Scroller控制器数组遍历保持offset同步
           this.dataSource.getAllData().forEach(showData => {
             showData.scrollerArray!.forEach(scroller => {
               scroller.scrollTo({ xOffset: this.topRightScroller.currentOffset().xOffset + offset, yOffset: 0 });
             });
           });
           return { offsetRemain: offset };
         });

       }
       .height(100)
       .width('100%');
     }

     // 下部分左侧行标题列表纵向滚动List
     @Builder
     leftList() {
       List({ scroller: this.bottomLeftScroller/* 绑定控制器与其他控制器联动*/ }) {
         ForEach(this.leftItems, (item: string) => {
           ListItem() {
             Text(item)
               .width(leftItemWidth)
               .height(itemHeight)
               .textAlign(TextAlign.Center);
           };
         }, (item: string) => item);

       }
       .sticky(StickyStyle.Header)
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .edgeEffect(EdgeEffect.None)
       .height('calc(100% - 100vp)')
       .width(leftItemWidth)
       .onScrollFrameBegin((offset: number) => {
         // 带动右侧纵向Scroll组件绑定的Scroller控制器同步滑动
         this.bottomRightScroller.scrollTo({
           xOffset: 0,
           yOffset: this.bottomLeftScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       });
     }

     // 下部分右侧内容显示区域纵向List(ListItem(List))
     @Builder
     rightList() {
       List({ initialIndex: 0, scroller: this.bottomRightScroller }) {
         // 通过LazyForEach加载每一行
         LazyForEach(this.dataSource, (item: ShowData) => {
           ListItemGroup({}) {
             ForEach(item.sub, (subItem: string) => {
               // 自定义ListItem中包含横向滚动List
               ItemComponent({
                 scroller: item.scrollerArray![item.sub!.indexOf(subItem)],
                 scrollCallBack: (value) => {
                   // value为子List横向滚动onScrollFrameBegin回传offset，在手指拖动时保持联动一致
                   // 顶部车型List跟随联动
                   this.topRightScroller.scrollTo({ xOffset: value, yOffset: 0 });
                   // 通过对象保存的Scroller数组跟随保持联动
                   this.dataSource.getAllData().forEach(showData => {
                     showData.scrollerArray!.forEach(scroller => {
                       if (scroller !== item.scrollerArray![item.sub!.indexOf(subItem)]) {
                         scroller.scrollTo({ xOffset: value, yOffset: 0 });
                       }
                     });
                   });
                 },
                 remainOffsetCallBack: (value) => {
                   // 滚动过程中回传保持同步的offset值
                   this.remainOffset = value;
                 }
               });
             }, (item: string) => item);
           };

         }, (item: ShowData, index: number) => item.sticky! + index);
       }
       .sticky(StickyStyle.Header)
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .friction(0.6)
       .edgeEffect(EdgeEffect.None)
       .onScrollFrameBegin((offset: number) => {
         // 内容List纵向滚动带动左侧标题List跟随滚动
         this.bottomLeftScroller.scrollTo({
           xOffset: 0,
           yOffset: this.bottomRightScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       })
       .onDidScroll(() => {
         // 内容List纵向滚动过程中，每一行中子List的Scroller滚动到remainOffset与已显示的行位置保持一致
         this.dataSource.getAllData().forEach(showData => {
           showData.scrollerArray!.forEach(scroller => {
             scroller.scrollTo({ xOffset: this.remainOffset, yOffset: 0 });
           });
         });
       })

       .position({ x: leftItemWidth, y: 0 })
       .edgeEffect(EdgeEffect.None) // 边缘效果设置为Spring
       .backgroundColor(0xDCDCDC)
       .height('calc(100% - 100vp)')
       .width('calc(100% - 100vp)');
     }
   }

   class ShowData {
     sticky?: string;
     sub?: string[];
     scrollerArray?: Scroller[] = [];
   }

   export class CommonDataSource<T> implements IDataSource {
     private listeners: DataChangeListener[] = [];
     protected originDataArray: T[] = [];

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
       if (delIndex != -1) {
         this.deleteData(delIndex);
       }
     }

     deleteData(index: number): void {
       this.originDataArray.splice(index, 1);
       this.notifyDataDelete(index);
     }

     setData(dataArray?: T[]) {
       if (dataArray) {
         this.originDataArray = dataArray;
       } else {
         this.originDataArray = [];
       }
       this.notifyDataReload();
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
   }

   interface DataItem {
     sticky: string;
     sub: string [];
   }
   ```
