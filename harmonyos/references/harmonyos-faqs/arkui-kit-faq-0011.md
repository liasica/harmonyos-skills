---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0011
title: ArkUI-List组件滚动与滑动常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > ArkUI-List组件滚动与滑动常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:ac4d8fc8cd2beb72bd668238f9997c25af5717e78e8b0c54ba504254e906a3d9
---

**Q：如何实现列表既可以左右滑、又可以上下滑动？**

**A**：实现列表的上下、左右滑动，参考代码如下：

1. 代码页面布局部分：

   ```ts
   import { CommonDataSource } from '../viewmodel/CommonDataSource';

   @Observed
   class ListItemData {
     text: string = '';
     id: string = '';
   }

   @Observed
   class ListData {
     id: string = '';
     fundName: string = '';
     textDataSource: CommonDataSource<ListItemData> = new CommonDataSource<ListItemData>();
   }

   @Entry
   @Component
   struct ScrollListDemoPage {
     // Horizontal scrolling distance of list data
     @State remainOffset: number = 0;
     // Maintain a list controller array to store ListScrollers for all horizontal lists
     @State listScrollerArr: ListScroller[] = [];
     // The starting index of the list is used to refresh the list area displayed on the current screen
     @State startIndex: number = 0;
     // End index of list
     @State endIndex: number = 0;
     // List Data - Displayed Content
     @State listData: ListItemData[] = [];
     // Head title list, titles for each column
     private titleList: string[] = [];
     // List data source
     private dataSource = new CommonDataSource<ListData>();
     // Vertical scrolling of list data
     verticalScroller: Scroller = new Scroller();
     // Horizontal scrolling of list data
     horizontalScroller: Scroller = new Scroller();
     // Scroll the left name column
     leftScroller: Scroller = new Scroller();
     // Head title column scrolling
     topScroller: Scroller = new Scroller();
     // Head Title List Data Source
     headerList = new CommonDataSource<string>();
     // Actual processed data
     showList: ListData[] = [];

     aboutToAppear(): void {
       this.loadData();
     }

     loadData() {
       for (let i = 0; i < 30; i++) {
         this.titleList.push('title' + i);
         let itemData: ListItemData = {
           text: 'content' + i,
           id: i + ''
         };
         this.listData.push(itemData);
       }
       this.headerList.setData(this.titleList);

       for (let i = 0; i < 20; i++) {
         // Every time the next page of data is obtained, it is necessary to synchronously add a controller to the list
         this.listScrollerArr.push(new ListScroller());
         let listItemData: ListData = new ListData();
         listItemData.fundName = 'Equity fund' + i;
         listItemData.id = 'Equity fund' + i;
         listItemData.textDataSource = new CommonDataSource<ListItemData>();
         listItemData.textDataSource.setData(this.listData);
         this.showList.push(listItemData);
       }
       this.dataSource.setData(this.showList);
     }

     build() {
       Column() {
         // Headline Title
         this.titleBuilder()
         // Divider
         Divider()
           .strokeWidth('100%')
           .color(0xeeeeee)

         Row() {
           // Left column
           this.leftBuilder()
           // Right column
           this.rightScroll()
         }
       }
       .height('100%')
       .alignItems(HorizontalAlign.Start)
     }

     @Builder
     titleBuilder() {
       Row() {
         Column() {
           Text('name')
         }
         .width(140)
         .height(48)
         .backgroundColor(Color.White)
         .justifyContent(FlexAlign.Center)
         .alignItems(HorizontalAlign.Start)
         .padding({ left: 16 })

         // Top Title List
         List({ scroller: this.topScroller }) {
           LazyForEach(this.headerList, (item: string) => {
             ListItem() {
               Text(item)
                 .height(48)
                 .width(120)
                 .textAlign(TextAlign.Start)
                 .padding({ left: 16 })
                 .backgroundColor(0xFFFFFF)
             }
           }, (item: string) => item)
         }
         .listDirection(Axis.Horizontal)
         .edgeEffect(EdgeEffect.None)
         .scrollBar(BarState.Off)
         .width('calc(100% - 140vp)')
         .layoutWeight(1)
         .onScrollFrameBegin((offset: number) => {
           for (let i = this.startIndex; i <= this.endIndex; i++) {
             this.listScrollerArr[i].scrollTo({
               xOffset: this.topScroller.currentOffset().xOffset + offset,
               yOffset: 0,
               animation: false
             });
           }
           return { offsetRemain: offset };
         })
       }
       .height(48)
       .width('100%')
       .justifyContent(FlexAlign.Start)
     }

     @Builder
     leftBuilder() {
       List({ scroller: this.leftScroller }) {
         LazyForEach(this.dataSource, (item: ListData) => {
           ListItem() {
             Column() {
               Text(item.fundName)
                 .height('100%')
                 .backgroundColor(0xFFFFFF)
                 .layoutWeight(1)
                 .margin({ left: 16 })
               Divider()
                 .strokeWidth('100%')
                 .color(0xeeeeee)
             }
             .justifyContent(FlexAlign.Center)
             .alignItems(HorizontalAlign.Start)
           }
           .height(60)
         }, (item: ListData) => JSON.stringify(item))
       }
       .listDirection(Axis.Vertical)
       .scrollBar(BarState.Off)
       .edgeEffect(EdgeEffect.None)
       .height('calc(100% - 48vp)')
       .width(140)
       .onScrollFrameBegin((offset: number) => {
         this.verticalScroller.scrollTo({
           xOffset: 0,
           yOffset: this.leftScroller.currentOffset().yOffset + offset,
           animation: false
         });
         return { offsetRemain: offset };
       })
     }

     @Builder
     rightScroll() {
       Scroll(this.horizontalScroller) {
         List({ initialIndex: 0, scroller: this.verticalScroller }) {
           LazyForEach(this.dataSource, (item: ListData, index: number) => {
             ListItem() {
               Column() {
                 List({ scroller: this.listScrollerArr[index] }) {
                   LazyForEach(item.textDataSource, (item: ListItemData) => {
                     ListItem() {
                       Text(item.text)
                         .height('100%')
                         .width('100%')
                         .textAlign(TextAlign.Start)
                         .padding({ left: 16 })
                         .backgroundColor(0xFFFFFF)
                         .fontColor('#ffe72929')
                         .maxLines(1)
                         .textOverflow({ overflow: TextOverflow.Ellipsis })
                     }
                     .width(120)
                   }, (item: ListItemData, index: number) => JSON.stringify(item) + index + '')
                 }
                 .cachedCount(4)
                 .height('100%')
                 .width('100%')
                 .layoutWeight(1)
                 .listDirection(Axis.Horizontal)
                 .scrollBar(BarState.Off)
                 .nestedScroll({
                   scrollForward: NestedScrollMode.PARENT_FIRST,
                   scrollBackward: NestedScrollMode.PARENT_FIRST
                 })
                 .edgeEffect(EdgeEffect.None)
                 .onDidScroll(() => {
                   this.remainOffset = this.listScrollerArr[index]!.currentOffset().xOffset;
                 })
                 .onScrollFrameBegin((offset: number) => {
                   this.topScroller.scrollTo({
                     xOffset: this.listScrollerArr[index]!.currentOffset().xOffset + offset,
                     yOffset: 0,
                     animation: false
                   });
                   for (let i = this.startIndex; i <= this.endIndex; i++) {
                     if (i !== index) {
                       this.listScrollerArr[i].scrollTo({
                         xOffset: this.listScrollerArr[index]!.currentOffset().xOffset + offset,
                         yOffset: 0,
                         animation: false
                       });
                     }
                   }
                   return { offsetRemain: offset };
                 })

                 Divider()
                   .strokeWidth('100%')
                   .color(0xeeeeee)
               }
               .height(60)
             }
           }, (item: ListData) => JSON.stringify(item))
         }
         .height('100%')
         .cachedCount(2)
         .flingSpeedLimit(1600)
         .listDirection(Axis.Vertical)
         .scrollBar(BarState.Off)
         .edgeEffect(EdgeEffect.None)
         .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
         .onScrollFrameBegin((offset: number) => {
           this.leftScroller.scrollTo({
             xOffset: 0,
             yOffset: this.verticalScroller.currentOffset().yOffset + offset,
             animation: false
           });
           return { offsetRemain: offset };
         })
         .onScrollIndex((start: number, end: number) => {
           this.startIndex = start;
           this.endIndex = end;
           // Scroll only the items within the current display range
           for (let i = start; i <= end; i++) {
             this.listScrollerArr[i].scrollTo({ xOffset: this.remainOffset, yOffset: 0, animation: false });
           }
         })
       }
       .position({ x: 140, y: 0 })
       .onDidScroll(() => {
         this.topScroller.scrollTo({ xOffset: this.remainOffset, yOffset: 0, animation: false });
       })
       .scrollBar(BarState.Off)
       .edgeEffect(EdgeEffect.None)
       .scrollable(ScrollDirection.Horizontal)
       .backgroundColor(0xDCDCDC)
       .height('calc(100% - 48vp)')
       .width('calc(100% - 140vp)')
     }
   }
   ```
2. 加载的数据源：

   ```ts
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

     clear() {
       this.originDataArray.splice(0, this.originDataArray.length)
       this.listeners.forEach(listener => {
         listener.onDataDelete(0);
       })
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
       })
     }

     notifyDataAdd(index: number) {
       this.listeners.forEach(listener => {
         listener.onDataAdd(index);
       })
     }

     notifyDataMove(from: number, to: number) {
       this.listeners.forEach(listener => {
         listener.onDataMove(from, to);
       })
     }

     notifyDataDelete(index: number) {
       this.listeners.forEach(listener => {
         listener.onDataDelete(index);
       })
     }

     notifyDataChange(index: number) {
       this.listeners.forEach(listener => {
         listener.onDataChange(index);
       })
     }
   }
   ```

**Q：滚动List组件，如何实时获取第一个可见的Item和最后一个可见的Item的索引位置？**

**A**：具体实现如下：

1. 使用onAreaChange获取List组件的宽高，用于后续判断Item是否在List区域内；
2. 列表初始化后需要先使用onScrollIndex获取第一个和最后一个Item，后续使用onScrollStop来获取首尾的Item；
3. 获取到的首尾Item后，判断其是否完全可见，首部Item不完全可见则取后一位，尾部Item不完全可见则取前一位。

   ```ts
   @Entry
   @Component
   struct ListVisibleByH {
     private arr: number[] = [];
     private scrollerForList: Scroller = new Scroller();
     @State startStr: string = '';
     startIndex = 0; // 保存第一个可见Item
     endIndex = 0; // 保存最后一个可见Item
     listHeight: number = 0; // 保存list的高度

     private judgeVisibleByHeight() {
       console.info('judgeVisibleByHeight');
       this.startStr = '';
       // 判断是否遮挡，判断条件可自行调节，这里设置3vp的误差
       let rect = this.scrollerForList.getItemRect(this.startIndex);
       if (rect.y < -3) {
         this.startIndex = this.startIndex + 1; // 上方元素y坐标小于-3，被遮挡
       }
       rect = this.scrollerForList.getItemRect(this.endIndex);
       if (rect.y + rect.height > this.listHeight + 3) {
         this.endIndex = this.endIndex - 1; // 下方元素高度超过父组件的高度，被遮挡
       }
       if (this.startIndex <= this.endIndex) {
         this.startStr = `首尾可见Item：${this.startIndex}, ${this.endIndex}`;
       } else {
         this.startStr = '没有能全部显示的Item';
       }
     }

     aboutToAppear() {
       for (let i = 0; i < 20; i++) {
         this.arr.push(i);
       }
     }

     build() {
       Flex({ direction: FlexDirection.Column }) {
         Text(this.startStr)
           .textAlign(TextAlign.Center)
           .height(50)
           .width('100%');
         Row() {
           List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
             ForEach(this.arr, (item: number) => {
               ListItem() {
                 Text(`${item}`)
                   .width('100%').fontSize(16)
                   .textAlign(TextAlign.Center);
               }
               .borderRadius(16).backgroundColor('#F1F3F5')
               .width('90%')
               .height(200);
             }, (item: number) => item.toString());
           }
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
           .alignListItem(ListItemAlign.Center)
           .listDirection(Axis.Vertical)
           .height('100%')
           .width('100%')
           .borderRadius(10)
           .onAreaChange((oldValue, newValue) => {
             console.info(`onAreaChange ${oldValue}`);
             this.listHeight = newValue.height as number; // list的高度
             this.judgeVisibleByHeight(); // 初始判断
           })
           .onScrollIndex((start, end) => {
             this.startIndex = start;
             this.endIndex = end;
           })
           .onScrollStop(() => {
             // 缓存开始结束索引：在最后一项继续滑动，不会触发onScrollIndex
             let tmpStart = this.startIndex;
             let tmpEnd = this.endIndex;
             this.judgeVisibleByHeight();
             this.startIndex = tmpStart;
             this.endIndex = tmpEnd;
           });
         }.width('100%').height('100%');
       }.width('100%').height('100%');
     }
   }
   ```

   效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/EjwJbqbGTzutVjgVtRtQLA/zh-cn_image_0000002795262643.png "点击放大")

**Q：在List组件中使用ListItemGroup的情况下，如何获取其中ListItem的索引值？**

**A**：onScrollIndex回调将ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值，因此就会获取不到当前ListItemGroup内ListItem的索引值。可以用[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)回调来监听ListItem的可见状态变化。

**Q：怎么设置多个ListItemGroup同时出现时，只显示最顶部的header中的Button按钮？**

**A**：通过给ListItemGroup组件添加onVisibleAreaChange事件中，判断当前显示了哪些ListItemGroup，同时选择其中最顶部的ListItemGroup显示Button。

**Q：List组件如何控制滑动的幅度和范围？**

**A**：List组件控制滑动幅度和范围的方法如下：

* onScrollFrameBegin的入参offset表示即将发生的滑动量，单位vp。返回参数offsetRemain表示实际滑动量。通过offset的大小来判断即将发生的滑动幅度是否超过预期值，通过控制返回的offsetRemain大小来限制实际的滑动量。核心代码如下：

  ```ts
  .onScrollFrameBegin((offset: number) => {
          if (offset > 1) {
            offset = 1;
          }
          if (offset < -1) {
            offset = -1;
          }
          return { offsetRemain: offset };
        })
  ```

  控制offsetRemain，滑动速度很缓慢，效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Cbr8RzbBRd6ZCFBb80Z01w/zh-cn_image_0000002766024018.png "点击放大")
* onScrollIndex的入参firstIndex超过预期值时，表示已经滑动出了预期范围，用this.scroller.scrollToIndex()把滑动强制拉回到预期值。核心代码如下：

  ```ts
  .onScrollIndex((firstIndex: number) => {
          if (firstIndex > 10) {
            this.scroller.scrollToIndex(10);
          }
        })
  ```

  下滑超过10之后继续滑动，会强制跳回10，效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ywm93OFKQI2xFZE_yLPuXA/zh-cn_image_0000002795262887.png "点击放大")

  全量代码如下：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct ScrollerPage {
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
    scroller: Scroller = new Scroller();

    // 沉浸式窗口
    onPageShow(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
        win.setWindowLayoutFullScreen(true);
      });
    }

    onPageHide(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
        win.setWindowLayoutFullScreen(false);
      });
    }

    build() {
      Column() {
        List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xDCDCDC);
            };
          }, (item: string) => item);
        }
        // 排列方向
        .listDirection(Axis.Vertical)
        .scrollBar(BarState.Off)
        .friction(0.6)
        .edgeEffect(EdgeEffect.None)
        .onScrollFrameBegin((offset: number) => {
          if (offset > 1) {
            offset = 1;
          }
          if (offset < -1) {
            offset = -1;
          }
          return { offsetRemain: offset };
        })
        // 根据List显示组件的索引值判断是否滑动到顶部
        .onScrollIndex((firstIndex: number) => {
          if (firstIndex > 10) {
            this.scroller.scrollToIndex(10);
          }
        })
        .width('90%');
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

**Q：聊天列表是即时通讯中比较重要的功能，如何使用List组件实现聊天列表功能？**

**A**：场景一：收到新数据时从底部开始显示。

* 实现原理：使用[@Watch](../harmonyos-guides/arkts-watch.md)监听数据源的变化，当数据源变化时，若List不在最底部显示，则将List自动滚到最底部。
* 示例代码：

  ```ts
  @Component
  struct Chat {
    // 这个列表代表聊天内容，每次发送和接收消息时，把聊天内容加入这个列表。当监听到列表发生变化时，执行函数scrollerBottom，把list滑动到最底部。
    @Prop @Watch('scrollerBottom') list: string[] = [];
    scroller: Scroller = new Scroller();

    scrollerBottom() {
      this.scroller.scrollEdge(Edge.Bottom);
    }

    build() {
      // initialIndex代表列表生成时，从第几个索引值开始展示，选择最后一个索引值，就实现了显示最底部的消息。scroller代表绑定滚动事件，配合List监听，实现发送和接收消息，都能滚动到最底部。
      List({ initialIndex: this.list.length - 1, scroller: this.scroller }) {
        ForEach(this.list, (item: string) => {
          ListItem() {
            Text(item)
              .width('100%')
              .margin(5)
              .textAlign(TextAlign.Center)
          }
        });
      }
      .width('100%')
      .height('100%');
    }
  }

  @Entry
  @Component
  struct ListChat {
    @State message: string[] = [];
    count: number = 0;

    build() {
      Column(){
        Column() {
          Chat({ list: this.message })
            .width('90%')
            .borderRadius(12)
            .backgroundColor('#F1F3F5');
          Button('新增消息')
            .onClick(() => {
              this.message.push('新消息' + (this.count++).toString());
            })
            .width('90%')
            .margin({ top: 20 })
            .backgroundColor('#0A59F7');
        }
        .height('50%')
        .width('100%')
      }
      .justifyContent(FlexAlign.Center).height('100%')
      .alignItems(HorizontalAlign.Center);
    }
  }
  ```
* 效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Sa02gOZhQHOWWjSmYVN4gg/zh-cn_image_0000002795423231.png "点击放大")

场景二：消息列表从底部开始加载，点击按钮回到最新位置。

* 实现原理：将List组件的[stackFromEnd](../harmonyos-references/ts-container-list.md#stackfromend19)属性设置为true可以实现列表从底部开始布局加载，给[scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)绑定List底部边界，实现跳转回到最新位置。

  **说明** 

  属性stackFromEnd从API version 19开始支持使用。
* 示例代码：

  ```ts
  @Entry
  @Component
  struct ListBottom {
    @State listContent: Array<string> = ['旧消息'];
    listScroller: ListScroller = new ListScroller();

    build() {
      Column() {
        List({ space: 10, scroller: this.listScroller }) {
          ForEach(this.listContent, (value: string) => {
            ListItem() {
              Text(value);
            }
            .width('90%')
            .height(200)
            .border({
              width: 0,
              radius: 20,
            })
            .backgroundColor(Color.White);
          });
        }
        .width('100%')
        .height('82%')
        .stackFromEnd(true) // 设置为true表示列表从底部开始布局
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)

        Column() {
          Button('新增消息')
            .onClick(() => {
              this.listContent.push('新消息' + this.listContent.length.toString());
            })
            .width('100%')
            .margin({ top:8 ,bottom:5})

          Button('回到最新位置')
            .onClick(() => {
              this.listScroller.scrollEdge(Edge.Bottom); // 将列表滚动到底部边界位置
            })
            .width('100%')
            .margin({top:8,bottom:20})
        }
        .width('90%')
        .justifyContent(FlexAlign.SpaceAround);
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM,SafeAreaEdge.TOP])
      .backgroundColor('#F1F3F5')
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.SpaceBetween);
    }
  }
  ```
* 效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/I6frokz1Q6yjIfyWjVXHaA/zh-cn_image_0000002765865230.png "点击放大")

场景三：图片异步加载完成后列表以顶部为锚点拉伸，最新消息被推出可视区域。

聊天页面使用List组件展示消息时，列表默认以顶部为锚点进行内容扩展。当消息中的图片等异步资源加载完成、内容高度从预加载的固定高度增大为真实高度时，列表从顶部向下拉伸，导致原本已滚动到底部对齐的最新消息被推出可视区域，用户看到的是历史消息而非最新消息。

利用@Watch监听数据变化、[Image.onComplete](../harmonyos-references/ts-basic-components-image.md#oncomplete)监听图片加载完成、[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)监听布局变化，在内容高度增大后重新调用[scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)(Edge.Bottom)滚动到底部。

```ts
interface ChatItem {
  content: string;
  url?: string;
}

@Component
struct ImageChatList {
  @Prop @Watch('scrollToBottom') chatList: ChatItem[] = [];
  scroller: Scroller = new Scroller();

  scrollToBottom() {
    this.scroller.scrollEdge(Edge.Bottom);
  }

  build() {
    List({ scroller: this.scroller }) {
      ForEach(this.chatList, (item: ChatItem) => {
        ListItem() {
          Column() {
            if (item.url) {
              // 图片加载完成后触发回滚到底部
              Image(item.url)
                .height(200)
                .width(200)
                .onComplete(() => {
                  setTimeout(() => {
                    this.scroller.scrollEdge(Edge.Bottom);
                  }, 50);
                })
            } else {
              Text(item.content)
                .width('100%')
                .margin(5)
                .textAlign(TextAlign.Center)
            }
          }
        }
      });
    }
    .width('100%')
    .height('100%')
    // 监听List内容区域尺寸变化，内容高度增大后回滚到底部
    .onAreaChange((_oldValue: Area, _newValue: Area) => {
      this.scroller.scrollEdge(Edge.Bottom);
    })
  }
}

@Entry
@Component
struct ImageChatPage {
  @State chatList: ChatItem[] = [];

  build() {
    Column() {
      Column() {
        ImageChatList({ chatList: this.chatList })
          .width('90%')
          .borderRadius(12)
          .backgroundColor('#F1F3F5')
        Button('新增文字消息')
          .onClick(() => {
            this.chatList.push({ content: '文字消息' + this.chatList.length.toString() });
          })
          .width('90%')
          .margin({ top: 20 })
          .backgroundColor('#0A59F7')
        Button('新增图片消息')
          .onClick(() => {
            // url请替换为实际图片地址
            this.chatList.push({ content: '', url: 'https://www.example.com/image.png' });
          })
          .width('90%')
          .margin({ top: 10 })
          .backgroundColor('#0A59F7')
      }
      .height('50%')
      .width('100%')
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```

**说明** 

[scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)不能在aboutToAppear中调用（此时组件未完成渲染），应在onAppear回调或数据变化后的延迟回调中调用。

该方案为API 17兼容方案。若后续不再需要适配低版本，建议迁移至API 19的[stackFromEnd](../harmonyos-references/ts-container-list.md#stackfromend19)属性，届时可移除回滚逻辑。

**Q：如何解决插入图片发生闪烁问题？**

**A**：可以使用syncLoad属性解决，具体可以参考[社区解决方案](https://developer.huawei.com/consumer/cn/blog/topic/03154617617506006)。

**Q：bindSheet的内容是个List，点击某个ListItem跳转至其他页面，如何实现从其他页面返回后bindSheet仍是打开状态，且List仍保持原样？**

**A**：在[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)生命周期中，通过AppStorage获取当前bindSheet显示状态以及List滑动距离，在跳转其他页面时记录当前List滑动距离，当目标页面返回时将bindSheet显隐状态绑定的变量设置为true，且在List的onAppear中通过Scroller滑动至之前保存的位置，实现保持原样的效果。参考代码如下：

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct BindSheetOnePage {
  @StorageProp('isTrue') isShow: boolean = false;
  @State numArr: number[] = [];
  private scrollerForList: Scroller = new Scroller();
  @State currentY: number = 0;

  onPageShow(): void {
    // 全局获取半模态的状态
    this.isShow = AppStorage.get('isTrue') as boolean;
    // 全局获取List当前位置
    this.currentY = AppStorage.get('currentY') as number;
    // 设置沉浸式
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      console.error(`err: ${err}`);
      win.setWindowLayoutFullScreen(true);
    });
  }

  aboutToAppear(): void {
    // 插入list数据
    for (let index = 0; index < 20; index++) {
      this.numArr.push(index);
    }
  }

  @Builder
  myBuilder() {
    List({ scroller: this.scrollerForList }) {
      ForEach(this.numArr, (item: number) => {
        ListItem() {
          Column() {
            Text(item.toString());
          }
          .justifyContent(FlexAlign.Center)
          .height('20%')
          .width('100%')
          .backgroundColor('#F3F3F3')
          .onClick(() => {
            // 全局存储当前List滑动距离
            AppStorage.setOrCreate('currentY', this.scrollerForList.currentOffset().yOffset);
            // 跳转到下一个页面
            this.getUIContext().getRouter().pushUrl({
              url: 'pages/BindSheetTwoPage'
            }).catch((e: BusinessError) => {
              console.error(`e: ${e}`);
            });
          });
        };
      });
    }
    .margin({
      left: 16,
      right: 16
    })
    .onAppear(() => {
      // 通过Scroller滑动至之前保存的位置，实现保持原样的效果
      this.scrollerForList.scrollTo({ xOffset: 0, yOffset: this.currentY });
    })
    .height('100%');
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
          // 点击打开半模态
          this.isShow = true;
          // 全局存储半模态状态
          AppStorage.setOrCreate('isTrue', true);
        })
        .fontSize(20)
        .margin(10)
        // $$双向同步半模态的状态
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: 600,
          title: { title: "title" },
          onAppear: () => {
            console.info('BindSheet onAppear.');
          },
          onDisappear: () => {
            console.info('BindSheet onDisappear.');
          }
        });
    }
    .backgroundColor($r('sys.color.point_color_checked'))
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

路由目标页面代码如下：

```ts
@Entry
@Component
struct BindSheetTwoPage {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // 点击返回上个页面
          this.getUIContext().getRouter().back();
        });
    }
    .backgroundColor($r('sys.color.point_color_checked'))
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D8_IVysiQ8a4OPo6Bc4LRQ/zh-cn_image_0000002795424595.png "点击放大")
