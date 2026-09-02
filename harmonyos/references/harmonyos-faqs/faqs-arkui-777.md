---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-777
title: 滚动条组件ScrollBar滑动时出现跳动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 滚动条组件ScrollBar滑动时出现跳动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:169ca8fc9a2d64b25e7429d02b3d0d937b153fac15d8a91b31262b9eba0b54e6
---

## 问题现象

滚动条ScrollBar配合List，通过懒加载实现子组件ListItem按需加载。但是滑动ScrollBar时，若持续加载ListItem，ScrollBar组件滑动距离会骤变。

```ts
export class MyDataSource implements IDataSource {
  private dataArray: HSFileItemForOperation[] = [];
  private listeners: DataChangeListener[] = [];

  public pushInitData(dataArray: HSFileItemForOperation[]) {
    for (let i = 0; i < dataArray.length; i++) {
      this.dataArray.push(dataArray[i]);
    }

    this.notifyDataReload();
  }

  public getData(index: number): HSFileItemForOperation {
    return this.dataArray[index];
  }

  // 数据源的数据总量
  public totalCount(): number {
    return this.dataArray.length;
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

@Observed
export class HSFileItemForOperation implements IDataSource {
  private dataArray: number[] = [];

  public pushData(dataArray: number[]) {
    for (let i = 0; i < dataArray.length; i++) {
      this.dataArray.push(dataArray[i]);
    }
  }

  constructor(dataArray: number[]) {
    this.dataArray = dataArray;
  }

  // 返回指定索引位置的数据
  public getData(index: number): number {
    return this.dataArray[index];
  }

  // 数据源的数据总量
  public totalCount(): number {
    return this.dataArray.length;
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

// 模拟数据
export const FILEITEM_LIST: HSFileItemForOperation[] = [
  new HSFileItemForOperation([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  ]),
  new HSFileItemForOperation([
    21, 22, 23,
    24, 25, 26, 27, 28,
    29, 30
  ]),
  new HSFileItemForOperation([
    31, 32, 33, 34, 35, 36, 37
  ]),
  new HSFileItemForOperation(
    [38, 39,])
];

@Entry
@Component
struct Page {
  private scroller: Scroller = new Scroller();

  build() {
    Column() {
      Stack() {
        Scroll(this.scroller) {
          Column() {
            TabsView();
          };
        }
        .width('100%')
        .height('100%')
        .scrollable(ScrollDirection.Vertical)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None);
      }
      .width('100%')
      .height('100%')
      .alignContent(Alignment.Top);
    };
  }
}

@Component
export struct TabsView {
  private tabController: TabsController = new TabsController();
  private groups: MyDataSource = new MyDataSource();
  private scroller: Scroller = new Scroller();

  aboutToAppear(): void {
    this.groups.pushInitData(FILEITEM_LIST);
  }

  build() {
    Tabs({ controller: this.tabController }) {
      TabContent() {
        Stack({ alignContent: Alignment.End }) {
          List({ scroller: this.scroller }) {
            LazyForEach(this.groups, (headItem: HSFileItemForOperation, index: number) => {
              ReusableListGroupComponent({
                group: headItem,
                index: index
              });
            }, (headItem: number) => headItem.toString() + Math.random() * 10);
          }
          .width('100%')
          .height('100%')
          .lanes(4)
          .sticky(StickyStyle.Header)
          .backgroundColor(Color.White)
          .nestedScroll({
            scrollForward: NestedScrollMode.PARENT_FIRST,
            scrollBackward: NestedScrollMode.SELF_FIRST
          })
          .edgeEffect(EdgeEffect.None)
          .scrollBar(BarState.Off);

          ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
            Stack() {
              Image($r('app.media.startIcon'))
                .width(40);
            };
          }
          .backgroundColor(0xF1F3F5)
          .hitTestBehavior(HitTestMode.Transparent);
        };
      }.tabBar('test');
    };
  }
}

@Component
struct ReusableListGroupComponent {
  @ObjectLink group: HSFileItemForOperation;
  @Prop index: number;

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .margin(10)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10);
  }

  build() {
    ListItemGroup({ header: this.itemHead('group' + this.index.toString()) }) {
      LazyForEach(this.group, (item: number, index: number) => {
        ListItem() {
          // 使用可复用自定义组件
          ReusableChildComponent({ item: item })
            .onAppear(() => {
              console.info('ReusableChildComponent', index);
            });
        };
      }, (item: number) => item.toString() + Math.random());
    };
  }
}

@Reusable
@Component
struct ReusableChildComponent {
  @State item: number = 0;

  aboutToReuse(params: Record<string, number>) {
    this.item = params.item;
  }

  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .padding(15)
        .objectFit(ImageFit.Fill)
        .layoutWeight(1);
      Text(`图片${this.item}`)
        .fontSize(16)
        .textAlign(TextAlign.Center);
    }
    .width('100%')
    .height(120)
    .backgroundColor(0xF9CF93);
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/zubPm7zLRLOr09oBgsR5Ow/zh-cn_image_0000002628395810.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/kZccWYy8Sv-ssufyLdXT3w/zh-cn_image_0000002658795075.gif "点击放大")

## 背景知识

* [LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)是对数组类型数据进行迭代渲染，并在每次迭代过程中创建相应组件的接口。其数据源需要实现IDataSource，用于管理listener监听，以及通知LazyForEach数据更新。
* [childrenMainSize](../harmonyos-references/ts-container-listitemgroup.md#childrenmainsize12)：设置ListItemGroup组件的子组件在主轴方向的大小信息。
* [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)：该组件用来展示列表item分组，宽度默认充满[List](../harmonyos-references/ts-container-list.md)组件，必须配合[List](../harmonyos-references/ts-container-list.md)组件来使用。
* [ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)：滚动条组件，用于配合可滚动组件使用，如[ArcList](../harmonyos-references/ts-container-arclist.md)、[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)。

## 问题定位

排查是否使用LazyForEach懒加载遍历：在懒加载场景，ListItemGroup内容高度不同的场景下，ScrollBar组件需要获取ListItemGroup的高度。

## 分析结论

分组遍历的ListItemGroup内容高度不同的情况下，使用LazyForEach无法获取确定子组件的高度。

## 修改建议

可以使用childrenMainSize接口提前设置ListItemGroup内容的高度。

页面加载前使用[ChildrenMainSize](../harmonyos-references/ts-container-scrollable-common.md#childrenmainsize12对象说明)对象提供的splice方法批量增删改子组件在主轴方向的大小信息。

```ts
aboutToAppear(): void {
  // splice方法批量增删改子组件在主轴方向的大小信息。
  let childrenSize: Array<number> = [];
  LIST_DATA.forEach((data: GroupItemSource) => {
    childrenSize.push(Math.ceil(data.dataArray.length / 4) * this.listItemHeight + this.groupHeaderHeight);
  });
  this.childrenSize.splice(0, 3, childrenSize);
  this.groups.pushInitData(LIST_DATA);
}
```

示例代码如下：

```ts
// 自定义数据源
export class MyDataSource implements IDataSource {
  dataArray: GroupItemSource[] = [];
  private listeners: DataChangeListener[] = [];

  public pushInitData(dataArray: GroupItemSource[]) {
    for (let i = 0; i < dataArray.length; i++) {
      this.dataArray.push(dataArray[i]);
    }
    this.notifyDataReload();
  }

  public getData(index: number): GroupItemSource {
    return this.dataArray[index];
  }

  // 数据源的数据总量
  public totalCount(): number {
    return this.dataArray.length;
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

@Observed
export class GroupItemSource implements IDataSource {
  dataArray: number[] = [];

  public pushData(dataArray: number[]) {
    for (let i = 0; i < dataArray.length; i++) {
      this.dataArray.push(dataArray[i]);
    }
  }

  constructor(dataArray: number[]) {
    this.dataArray = dataArray;
  }

  // 返回指定索引位置的数据
  public getData(index: number): number {
    return this.dataArray[index];
  }

  // 数据源的数据总量
  public totalCount(): number {
    return this.dataArray.length;
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

// 模拟List数据
export const LIST_DATA: GroupItemSource[] = [
  new GroupItemSource([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  ]),
  new GroupItemSource([
    21, 22, 23,
    24, 25, 26, 27, 28,
    29, 30
  ]),
  new GroupItemSource([
    31, 32, 33, 34, 35, 36, 37
  ]),
  new GroupItemSource(
    [38, 39,])
];

@Entry
@Component
struct Page {
  private scroller: Scroller = new Scroller();

  build() {
    Column() {
      Stack() {
        Scroll(this.scroller) {
          Column() {
            TabsView();
          };
        }
        .width('100%')
        .height('100%')
        .scrollable(ScrollDirection.Vertical)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None);
      }
      .width('100%')
      .height('100%')
      .alignContent(Alignment.Top);
    }.margin({ left: 8, right: 8 });
  }
}

@Component
export struct TabsView {
  private tabController: TabsController = new TabsController();
  private groups: MyDataSource = new MyDataSource();
  private scroller: Scroller = new Scroller();
  private listItemHeight: number = 120; // listItem子组件高度
  private groupHeaderHeight: number = 40; // groupHeader高度
  private columns: number = 4; // 列数
  @State childrenSize: ChildrenMainSize = new ChildrenMainSize(this.listItemHeight);

  aboutToAppear(): void {
    // splice方法批量增删改子组件在主轴方向的大小信息。
    let childrenSize: Array<number> = [];
    LIST_DATA.forEach((data: GroupItemSource) => {
      childrenSize.push(Math.ceil(data.dataArray.length / 4) * this.listItemHeight + this.groupHeaderHeight);
    });
    this.childrenSize.splice(0, 3, childrenSize);
    this.groups.pushInitData(LIST_DATA);
  }

  build() {
    Tabs({ controller: this.tabController }) {
      TabContent() {
        Stack({ alignContent: Alignment.End }) {
          List({ scroller: this.scroller }) {
            LazyForEach(this.groups, (headItem: GroupItemSource, index: number) => {
              ReusableListGroupComponent({
                group: headItem,
                index: index
              });
            });
          }
          .childrenMainSize(this.childrenSize)
          .width('100%')
          .height('100%')
          .lanes(this.columns)
          .sticky(StickyStyle.Header)
          .backgroundColor(Color.White)
          .nestedScroll({
            scrollForward: NestedScrollMode.PARENT_FIRST,
            scrollBackward: NestedScrollMode.SELF_FIRST
          })
          .edgeEffect(EdgeEffect.None)
          .scrollBar(BarState.Off);

          ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
            Stack() {
              // 此处'app.media.startIcon'仅作示例
              Image($r('app.media.startIcon'))
                .width(40)
                .aspectRatio(1);
            };
          }
          .backgroundColor(Color.Blue)
          .hitTestBehavior(HitTestMode.Transparent);
        };
      }.tabBar('test');
    };
  }
}

@Component
struct ReusableListGroupComponent {
  @ObjectLink group: GroupItemSource;
  @Prop index: number;
  @State childrenSize: ChildrenMainSize = new ChildrenMainSize(120); // 设置ListItemGroup组件的子组件在主轴方向的大小信息
  private groupHeaderHeight: number = 40;

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .height(this.groupHeaderHeight);
  }

  build() {
    ListItemGroup({ header: this.itemHead('group' + this.index.toString()) }) {
      LazyForEach(this.group, (item: number, index: number) => {
        ListItem() {
          // 使用可复用自定义组件
          ReusableChildComponent({ item: item })
            .onAppear(() => {
              console.info(`ReusableChildComponent:\n${index}`);
            });
        };
      });
    }
    .childrenMainSize(this.childrenSize);
  }
}

@Reusable
@Component
struct ReusableChildComponent {
  @State item: number = 0;
  private listItemHeight: number = 120;

  aboutToReuse(params: Record<string, number>) {
    this.item = params.item;
  }

  build() {
    Column() {
      // 此处'app.media.startIcon'仅作示例
      Image($r('app.media.startIcon'))
        .padding(5)
        .objectFit(ImageFit.Fill)
        .layoutWeight(1);
      Text(`图片${this.item}`)
        .fontSize(16)
        .textAlign(TextAlign.Center);
    }
    .width('100%')
    .height(this.listItemHeight)
    .backgroundColor(0xF1F3F5);
  }
}
```
