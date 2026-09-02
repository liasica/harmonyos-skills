---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-51
title: WaterFlow组件切换列数时卡顿
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > WaterFlow组件切换列数时卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3cebcc1dd2511232077e8587f98b6741aa0aa57622aa837a0977b3c69da41083
---

## 问题现象

使用WaterFlow组件，加载较多数据，切换列数时出现卡顿。

## 背景知识

[WaterFlow](../harmonyos-references/ts-container-waterflow.md)：瀑布流容器，由“行”和“列”分割的单元格所组成，通过容器自身的排列规则，将不同大小的“项目”自上而下，如瀑布般紧密布局。瀑布流组件布局模式有从上到下的布局模式（[ALWAYS\_TOP\_DOWN](../harmonyos-references/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)）和移动窗口式的布局模式（[SLIDING\_WINDOW](../harmonyos-references/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)）。

采用从上到下的布局模式时，视窗内的子组件依赖视窗上方所有子组件的布局信息，切换列数时需要计算上方所有子组件的布局信息，而采用移动窗口式的布局模式时，切换列数时只需要布局视窗内的子组件，对视窗上方的子组件没有依赖关系。在创建WaterFlow时可设置[layoutMode](../harmonyos-references/ts-container-waterflow.md#waterflowoptions对象说明)参数来设置布局模式，默认是从上到下的布局模式。

## 问题定位

WaterFlow组件加载较多数据，在切换列数时出现卡顿现象，则排查WaterFlow组件创建时是否设置layoutMode为WaterFlowLayoutMode.SLIDING\_WINDOW，如下关键代码可看到未设置layoutMode参数，会导致在切换列数时会计算上方所有子组件的布局信息，组件数量过多时布局耗时多，会出现卡顿现象。

```ts
class WaterFlowDataSource implements IDataSource {
  private dataArray: number[] = [];
  private listeners: DataChangeListener[] = [];

  constructor() {
    for (let i = 0; i < 1000; i++) {
      this.dataArray.push(i);
    }
  }

  public getData(index: number): number {
    return this.dataArray[index];
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  public totalCount(): number {
    return this.dataArray.length;
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

  public addItem(index: number): void {
    this.dataArray.splice(index, 0, this.dataArray.length);
    this.notifyDataAdd(index);
  }
}

@Reusable
@Component
struct ReusableFlowItem {
  item: number = 0;

  build() {
    Text(`${this.item}`)
      .fontWeight(FontWeight.Regular)
      .fontSize(20)
      .fontColor(Color.White)
  }
}

@Entry
@Component
export struct WaterFlowComponentPage {
  private list: WaterFlowDataSource = new WaterFlowDataSource();
  @State column: number = 3;
  scroller: Scroller = new Scroller();

  build() {
    Column() {
      WaterFlow({
        scroller: this.scroller
      }) {
        LazyForEach(this.list, (item: number) => {
          FlowItem() {
            ReusableFlowItem({ item: item })
          }
          .backgroundColor('#0A59F7')
          .border({ radius: 8 })
          .width('100%')
          .height(120)

        }, (item: string, _index: number) => item.toString() + _index)
      }
      .cachedCount(2)
      .width('300vp')
      .height('200vp')
      .layoutDirection(FlexDirection.Column)
      .friction(0.75)
      .columnsTemplate('1fr '.repeat(this.column))
      .rowsTemplate('1fr 1fr 1fr')
      .columnsGap(6)
      .rowsGap(6)
      .padding(2)
      .border({
        width: 1,
        color: '#0A59F7',
        radius: 12
      })
      .onAppear(() => {
        // 滚动到底部
        setTimeout(() => {
          this.scroller.scrollEdge(Edge.End);
        }, 1000);
      })

      Slider({
        value: this.column,
        min: 1,
        max: 4
      }).onChange((value: number) => {
        // 切换显示的列数
        this.column = value;
      })
    }
    .width('100%')
  }
}
```

## 分析结论

使用WaterFlow组件时采用了从上到下的布局模式，在切换列数时需要计算视窗内上方所有子组件的布局信息，当子组件数量过多时，布局耗时多，会出现卡顿现象。

## 修改建议

将layoutMode设置成WaterFlowLayoutMode.SLIDING\_WINDOW，采用移动窗口式的布局模式。

```ts
class WaterFlowDataSource implements IDataSource {
  private dataArray: number[] = [];
  private listeners: DataChangeListener[] = [];

  constructor() {
    for (let i = 0; i < 1000; i++) {
      this.dataArray.push(i);
    }
  }

  public getData(index: number): number {
    return this.dataArray[index];
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  public totalCount(): number {
    return this.dataArray.length;
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

  public addItem(index: number): void {
    this.dataArray.splice(index, 0, this.dataArray.length);
    this.notifyDataAdd(index);
  }
}

@Reusable
@Component
struct ReusableFlowItem {
  item: number = 0;

  build() {
    Text(`${this.item}`)
      .fontWeight(FontWeight.Regular)
      .fontSize(20)
      .fontColor(Color.White)
  }
}

@Entry
@Component
export struct WaterFlowComponentPage {
  private list: WaterFlowDataSource = new WaterFlowDataSource();
  @State column: number = 3;
  scroller: Scroller = new Scroller();

  build() {
    Column() {
      WaterFlow({
        scroller: this.scroller,
        layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW
      }) {
        LazyForEach(this.list, (item: number) => {
          FlowItem() {
            ReusableFlowItem({ item: item })
          }
          .backgroundColor('#0A59F7')
          .border({ radius: 8 })
          .width('100%')
          .height(120)

        }, (item: string, _index: number) => item.toString() + _index)
      }
      .cachedCount(2)
      .width('300vp')
      .height('200vp')
      .layoutDirection(FlexDirection.Column)
      .friction(0.75)
      .columnsTemplate('1fr '.repeat(this.column))
      .rowsTemplate('1fr 1fr 1fr')
      .columnsGap(6)
      .rowsGap(6)
      .padding(2)
      .border({
        width: 1,
        color: '#0A59F7',
        radius: 12
      })
      .onAppear(() => {
        // 滚动到底部
        setTimeout(() => {
          this.scroller.scrollEdge(Edge.End);
        }, 1000);
      })

      Slider({
        value: this.column,
        min: 1,
        max: 4
      }).onChange((value: number) => {
        // 切换显示的列数
        this.column = value;
      })
    }
    .width('100%')
  }
}
```
