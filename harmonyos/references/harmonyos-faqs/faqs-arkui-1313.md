---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1313
title: Tabs中实现自定义组件间的样式复用与数据隔离
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs中实现自定义组件间的样式复用与数据隔离
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ccbf0a6f81592bff611dbbb4fa45358e75d77a38f0c35f798e5e913c4e97b828
---

## 问题现象

应用采用Tabs导航来快速实现视图内容的切换，其中视图内容之间的组件样式相互复用。由于组件复用，导致其中一个视图内容下拉刷新的时候，其他页面的数据也跟随变化，如何实现只刷新当前视图内容数据，其他视图内容保持不变？

## 背景知识

当页面信息较多时，[Tabs组件](../harmonyos-guides/arkts-navigation-tabs.md)可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。为了提高代码可复用性，可以通过[自定义组件](../harmonyos-guides/arkts-custom-components.md)的方式来提高代码可复用性。

## 解决方案

为了实现不同视图内容中复用组件间数据的隔离，需要为每个视图内容创建单独的刷新函数。当监听到Tabs页切换时，立即将每个视图内容独有的刷新函数与共享的刷新监听器重新绑定，以确保后续在当前页面执行刷新操作时，仅修改当前页面的数据。完整示例参考如下：

1. 定义页面中使用的常量（实际使用时需要从后端服务器获取）：

   ```ts
   // 定义页面中使用的常量
   export class SleepStyleModel {
     name: string;
     key: string;

     constructor(name: string, key: string) {
       this.name = name;
       this.key = key;
     }
   }

   export const styleData: SleepStyleModel[] = [
     new SleepStyleModel('全部', 'ALL'),
     new SleepStyleModel('睡眠', 'FastSleep')
   ];
   ```
2. 定义监听器。

   ```ts
   // 定义监听器
   export class RefreshListener {
     // key: string;
     onRefresh = (key: string) => {
       // return key
       console.info(key);
     };
   }
   ```
3. 定义Tab页中复用组件。

   ```ts
   @Component({ freezeWhenInactive: true })
   export struct StyleList {
     @Prop typeKey: string;
     @Prop isRefreshing: boolean = false;
     @State list: string[] = [];
     // 监听Tabs切换
     @Prop @Watch('onIndexChange') currentIndex: number;
     listener: RefreshListener = new RefreshListener();
     private onRefresh = (key: string) => {
       console.info(`key==============: ${key}`);
       this.typeKey = key;
       this.loadData();
     };

     // 监听回调函数
     onIndexChange() {
       console.info('---------------------监听切换视图页面');
       if (styleData[this.currentIndex].key == this.typeKey) {
         // 重新绑定刷新函数
         console.info(`---------------------重新绑定监听函数${this.currentIndex}`);
         this.listener.onRefresh = this.onRefresh;
       }
     }

     aboutToAppear(): void {
       this.listener.onRefresh = this.onRefresh;
       this.loadData();
     }

     loadData() {
       const arr: string[] = [];
       switch (this.typeKey) {
         case 'ALL':
           for (let i = 0; i < 5; i++) {
             arr.push(this.typeKey + i.toString());
           }
           this.list = arr;
           break;
         case 'FastSleep':
           for (let i = 5; i < 10; i++) {
             arr.push(this.typeKey + i.toString());
           }
           this.list = arr;
           break;
       }
     }

     build() {
       Column() {
         List() {
           ForEach(this.list, (item: string) => {
             ListItem() {
               Text('' + item)
                 .width('70%')
                 .height(80)
                 .margin(10)
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .backgroundColor(0xFFFFFF);
             };
           }, (item: string) => item + new Date().getTime());
         }
         .width('100%')
         .height('100%')
         .alignListItem(ListItemAlign.Center)
         .scrollBar(BarState.Off);
       };
     }
   }
   ```
4. 定义首页，调用复用组件。

   ```ts
   @Entry
   @Component
   export struct SleepMusicPage {
     @State styleList: SleepStyleModel[] = styleData;
     @State currentIndex: number = 0;
     @State selectedIndex: number = 0;
     @State isRefreshing: boolean = false;
     private controller: TabsController = new TabsController();
     private listener: RefreshListener = new RefreshListener();
     private currentKey: string = 'ALL';

     @Builder
     tabBuilder(index: number, name: string) {
       Column() {
         Text(name)
           .fontColor(this.selectedIndex === index ? '#1E2029' : '#91979F')
           .fontSize(12)
           .fontWeight(this.selectedIndex === index ? 500 : 400)
           .lineHeight(22)
           .margin({
             top: 17,
             bottom: 7
           });
         Divider()
           .strokeWidth(2)
           .color('#1E2029')
           .opacity(this.selectedIndex === index ? 1 : 0);
       }.width('100%');
     }

     build() {
       Refresh({
         refreshing: $$this.isRefreshing
       }) {
         Column() {
           Tabs({
             barPosition: BarPosition.Start,
             index: this.currentIndex,
             controller: this.controller
           }) {
             ForEach(this.styleList, (item: SleepStyleModel, index: number) => {
               TabContent() {
                 // 外部调用复用组件
                 StyleList({
                   typeKey: item.key,
                   isRefreshing: this.isRefreshing,
                   // 共享的刷新监听器
                   listener: this.listener,
                   currentIndex: this.currentIndex
                 });
               }.tabBar(this.tabBuilder(index, item.name));
             }, (item: SleepStyleModel) => JSON.stringify(item.key) + new Date().getTime());
           }
           .animationDuration(400)
           .onChange((index: number) => {
             this.currentIndex = index;
             this.selectedIndex = index;
             this.currentKey = this.styleList[this.selectedIndex].key;
           });
         }.width('100%').height('100%');
       }
       .onRefreshing(() => {
         this.isRefreshing = true;
         this.listener.onRefresh(this.currentKey);
         setTimeout(() => {
           this.isRefreshing = false;
         }, 1000);
       })
       .backgroundColor(0x89CFF0)
       .refreshOffset(64)
       .pullToRefresh(true);
     }
   }
   ```

完整示例参考如下：

```ts
// 定义页面中使用的常量
export class SleepStyleModel {
  name: string;
  key: string;

  constructor(name: string, key: string) {
    this.name = name;
    this.key = key;
  }
}

export const styleData: SleepStyleModel[] = [
  new SleepStyleModel('全部', 'ALL'),
  new SleepStyleModel('睡眠', 'FastSleep')
];

// 定义监听器
export class RefreshListener {
  // key: string;
  onRefresh = (key: string) => {
    // return key
    console.info(key);
  };
}

@Component({ freezeWhenInactive: true })
export struct StyleList {
  @Prop typeKey: string;
  @Prop isRefreshing: boolean = false;
  @State list: string[] = [];
  // 监听Tabs切换
  @Prop @Watch('onIndexChange') currentIndex: number;
  listener: RefreshListener = new RefreshListener();
  private onRefresh = (key: string) => {
    console.info(`key==============: ${key}`);
    this.typeKey = key;
    this.loadData();
  };

  // 监听回调函数
  onIndexChange() {
    console.info('---------------------监听切换视图页面');
    if (styleData[this.currentIndex].key == this.typeKey) {
      // 重新绑定刷新函数
      console.info(`---------------------重新绑定监听函数${this.currentIndex}`);
      this.listener.onRefresh = this.onRefresh;
    }
  }

  aboutToAppear(): void {
    this.listener.onRefresh = this.onRefresh;
    this.loadData();
  }

  loadData() {
    const arr: string[] = [];
    switch (this.typeKey) {
      case 'ALL':
        for (let i = 0; i < 5; i++) {
          arr.push(this.typeKey + i.toString());
        }
        this.list = arr;
        break;
      case 'FastSleep':
        for (let i = 5; i < 10; i++) {
          arr.push(this.typeKey + i.toString());
        }
        this.list = arr;
        break;
    }
  }

  build() {
    Column() {
      List() {
        ForEach(this.list, (item: string) => {
          ListItem() {
            Text('' + item)
              .width('70%')
              .height(80)
              .margin(10)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF);
          };
        }, (item: string) => item + new Date().getTime());
      }
      .width('100%')
      .height('100%')
      .alignListItem(ListItemAlign.Center)
      .scrollBar(BarState.Off);
    };
  }
}

@Entry
@Component
export struct SleepMusicPage {
  @State styleList: SleepStyleModel[] = styleData;
  @State currentIndex: number = 0;
  @State selectedIndex: number = 0;
  @State isRefreshing: boolean = false;
  private controller: TabsController = new TabsController();
  private listener: RefreshListener = new RefreshListener();
  private currentKey: string = 'ALL';

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? '#1E2029' : '#91979F')
        .fontSize(12)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({
          top: 17,
          bottom: 7
        });
      Divider()
        .strokeWidth(2)
        .color('#1E2029')
        .opacity(this.selectedIndex === index ? 1 : 0);
    }.width('100%');
  }

  build() {
    Refresh({
      refreshing: $$this.isRefreshing
    }) {
      Column() {
        Tabs({
          barPosition: BarPosition.Start,
          index: this.currentIndex,
          controller: this.controller
        }) {
          ForEach(this.styleList, (item: SleepStyleModel, index: number) => {
            TabContent() {
              // 外部调用复用组件
              StyleList({
                typeKey: item.key,
                isRefreshing: this.isRefreshing,
                // 共享的刷新监听器
                listener: this.listener,
                currentIndex: this.currentIndex
              });
            }.tabBar(this.tabBuilder(index, item.name));
          }, (item: SleepStyleModel) => JSON.stringify(item.key) + new Date().getTime());
        }
        .animationDuration(400)
        .onChange((index: number) => {
          this.currentIndex = index;
          this.selectedIndex = index;
          this.currentKey = this.styleList[this.selectedIndex].key;
        });
      }.width('100%').height('100%');
    }
    .onRefreshing(() => {
      this.isRefreshing = true;
      this.listener.onRefresh(this.currentKey);
      setTimeout(() => {
        this.isRefreshing = false;
      }, 1000);
    })
    .backgroundColor(0x89CFF0)
    .refreshOffset(64)
    .pullToRefresh(true);
  }
}
```
