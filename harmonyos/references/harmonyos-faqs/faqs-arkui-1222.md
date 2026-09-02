---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1222
title: List嵌套Grid实现内容分类展示效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List嵌套Grid实现内容分类展示效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1e33f563e3b96977db3e7e601076abcf76ccf2e1355090a4868268e5573d2cde
---

## 问题现象

如何使用List嵌套Grid实现内容分类展示效果？如何实现这种组合布局？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/HxhjgNXESY2BsDMOVUs6QQ/zh-cn_image_0000002658833271.gif "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)组件包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [Grid](../harmonyos-references/ts-container-grid.md)网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数在创建自定义组件的新实例后，在执行其build()函数之前执行。

## 解决方案

1. ListGridDemo.ets：
   * 定义状态变量curIndex用于跟踪当前选中的标签索引，以及tabItem数组用于存储各个分类的名称。
   * 实现tabBuilder方法，用于构建每个标签的样式，即选中时的字体变化。
   * ForEach循环遍历tabItem数组，为每个标签创建TabContent。每个TabContent内部是一个Scroll组件，里面嵌入ItemsPageView组件，并传递tabBarIndex参数。

   ```screen
   import { ItemsPageView } from './ItemsPageView';

   @Entry
   @Component
   struct ListGridDemo {
     @State curIndex: number = 0;
     @State tabItem: Array<string> =
       ['全部', '咨询', '医生', '经络', '膳食', '茶饮', '运动', '足浴'];

     @Builder
     tabBuilder(index: number, name: string) {
       Column() {
         Text(name)
           .fontSize(this.curIndex === index ? 20 : 16)
           .fontColor(Color.Black)
           .fontWeight(this.curIndex === index ? FontWeight.Bold : FontWeight.Normal)
           .id(index.toString())
           .margin({ bottom: 10 });
       }
       .margin({ left: 10, right: 10 })
       .width(this.curIndex === index ? name.length * 20 : name.length * 16)
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .height(56);
     }

     build() {
       Column() {
         Stack({ alignContent: Alignment.TopStart }) {
           Column() {
             Tabs({ index: this.curIndex, barPosition: BarPosition.Start }) {
               ForEach(this.tabItem, (item: string, index: number) => {
                 TabContent() {
                   Scroll() {
                     Column() {
                       ItemsPageView({ tabBarIndex: this.curIndex }).expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
                     }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]) ;
                   }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
                 }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
                 .tabBar(this.tabBuilder(index, item));
               });
             }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
             .onTabBarClick((index: number) => {
               this.curIndex = index;
             })
             .onChange((index: number) => {
               this.curIndex = index;
             })
             .layoutWeight(1)
             .barOverlap(false)
             .barMode(BarMode.Scrollable)
             .barHeight(56);
           }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
         }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
         .height('100%')
         .width('100%');
       }.backgroundColor(Color.White).expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
     }
   }
   ```
2. ItemsPageView.ets：
   * 定义两个数据模型gridItems和listItems，分别用于网格和列表布局。
   * 使用ListItemAdapter管理数据，在aboutToAppear方法中将gridItems和listItems添加到Adapter中。
   * 使用LazyForEach遍历Adapter中的每个数据项，根据itemType字段决定渲染ListComponent还是GridComponent。

   ```screen
   import { ListItemAdapter } from './ListItemAdapter';

   @Component
   export struct ItemsPageView {
     @Prop tabBarIndex: number;
     @State private adapter: ListItemAdapter<DataModel> = new ListItemAdapter();
     gridItems: DataModel = {
       itemType: ItemType.gridItems,
       'result': [
         {
           'name': 'grid_1',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'grid_2',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'grid_3',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'grid_4',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         }
       ]
     };
     listItems: DataModel = {
       itemType: ItemType.listItems,
       'result': [
         {
           'name': 'list_1',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_2',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_3',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_4',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_5',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_6',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_7',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_8',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         }
       ]
     };

     aboutToAppear(): void {
       let tmp: DataModel[] = [];
       tmp.push(this.listItems);
       tmp.push(this.gridItems);
       this.adapter.addList(tmp);
     }

     build() {
       Column() {
         // 使用LazyForEach遍历adapter中的数据，并根据itemType决定渲染列表还是网格
         LazyForEach(this.adapter, (item: DataModel) => {
           if (item.itemType === ItemType.listItems) {
             ListComponent({ listItemData: item.result });
           } else if (item.itemType === ItemType.gridItems) {
             GridComponent({ gridItemData: item.result });
           }
         });
       }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
       .height('auto')
       .padding(10);
     }
   }

   export interface Grids {
     icon?: Resource;
     name: string;
   }

   @Component
   export struct GridComponent {
     gridAdapter: ListItemAdapter<Grids> = new ListItemAdapter();
     gridItemData: Array<Grids> = [];

     aboutToAppear(): void {
       this.gridAdapter.addList(this.gridItemData);
     }

     build() {
       Grid() {
         LazyForEach(this.gridAdapter, (item: Grids) => {
           GridItem() {
             Column() {
               Text(item.name)
                 .textAlign(TextAlign.Center)
                 .width('100%')
                 .height('50%');
             }
           }.backgroundColor('#F1F3F5').borderRadius(15);
         }, (item: Grids) => item.name);
       }
       .layoutDirection(GridDirection.Column)
       .columnsTemplate('1fr 1fr')
       .rowsGap(15)
       .columnsGap(10)
       .padding({ top: 10, bottom: 10 })
       .height(210)
       .width('100%');
     }
   }

   export interface Lists {
     icon?: Resource;
     name: string;
   }

   @Component
   export struct ListComponent {
     listAdapter: ListItemAdapter<Lists> = new ListItemAdapter();
     listItemData: Array<Lists> = [];

     aboutToAppear(): void {
       this.listAdapter.addList(this.listItemData);
     }

     build() {
       Column() {
         LazyForEach(this.listAdapter, (item: Lists) => {
           Column() {
             Text(item.name)
               .textAlign(TextAlign.Center)
               .width('100%')
               .height('20%')
               .margin({ top: 15 });
           }.backgroundColor('#F1F3F5')
           .borderRadius(15)
           .margin({bottom:12});
         }, (item: Lists) => item.name);
       }
       .padding({ top: 10, bottom: 10 })
       .height('auto')
       .width('100%');
     }
   }

   export enum ItemType {
     listItems = 'listItems',
     gridItems = 'gridItems'
   }

   export class DataModel {
     itemType: ItemType = ItemType.listItems;
     result: ESObject;
   }
   ```
3. ListItemAdapter.ets：
   * 实现一个泛型类，实现IDataSource接口。
   * 维护一个列表listItems和数据变更的监听器listeners。

   ```screen
   export class ListItemAdapter<T> implements IDataSource {
     private listItems: T[] = [];
     private listeners: DataChangeListener[] = [];

     getList(): T[] {
       return this.listItems;
     }

     setList(list: T[]) {
       this.listItems = list;
     }

     addList(list: T[]) {
       this.listItems = this.listItems.concat(list);
       this.notifyDataAdd(this.listItems.length - 1);
     }

     totalCount(): number {
       return this.listItems.length;
     }

     getData(index: number): T {
       return this.listItems[index];
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

## 常见FAQ

Q：怎样在此场景上实现下拉刷新功能？

A：下拉刷新可以使用Refresh嵌套List来实现，刷新逻辑在onRefreshing回调方法里面执行，具体参考[官方文档](faqs-arkui-278.md)。
