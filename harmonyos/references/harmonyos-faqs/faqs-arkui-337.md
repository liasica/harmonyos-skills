---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-337
title: 双层嵌套list,如何使用LazyForEach起作用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 双层嵌套list,如何使用LazyForEach起作用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad776de7fdd8fef5ce665c507c70916e59473914512b8769d7a518d0037eb903
---

**问题场景**

在外层ListA中，每个ListItem包含一个内层List，内层List使用LazyForEach实现懒加载效果。设置外层ListItem高度会导致内层LazyForEach失效（所有项一次性加载），而不设置高度时虽可正常懒加载，但可能导致内层列表数据显示不全。

**解决措施**

固定内层List高度。参考如下代码：

```ts
const bgColors: ResourceColor[] = [Color.Blue, Color.Gray];
const rowHeight = 60;

export class BaseDataSource<T> implements IDataSource {
  private readonly listeners: DataChangeListener[] = [];
  protected dataset: T[];

  constructor(dataset?: T[]) {
    this.dataset = dataset ?? [];
  }

  public resetDataset(dataset: T[]) {
    this.dataset = dataset;
    this.notifyDataReload();
  }

  public updateDataAt(index: number, data: T) {
    if (index >= 0 && index < this.dataset.length) {
      this.dataset[index] = data;
      this.notifyDataChange(index);
    } else {
      console.error(`Index ${index} out of bounds`);
    }
  }

  public getDataset() {
    return this.dataset;
  }

  public totalCount(): number {
    return this.dataset.length;
  }

  public getData(index: number): T {
    return this.dataset[index];
  }

  /**
   * Notify LazyForEach component to reload all child components
   */
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  /**
   * Notify LazyForEach component to add a sub component at the index corresponding to the index
   * @param index
   */
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  /**
   * Notify LazyForEach component that there is a change in data at the index corresponding to the index, and that the sub component needs to be rebuilt
   * @param index
   */
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  /**
   * Notify LazyForEach component to remove the sub component at the index corresponding to the index
   * @param index
   */
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  /**
   * Notify LazyForEach component to swap the subcomponents at the from index and to index
   * @param from
   * @param to
   */
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }

  //----------------------------------------------------------------------------------------------------
  // This method is called on the framework side to add listener listening to the LazyForEach component at its data source
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  // This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }
}

class NestedListItemDataSource extends BaseDataSource<string> {
  private dataArray: string[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string {
    return this.dataArray[index];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

/*
 * Header component for nested list items
 * @param title - Display text for header
 */
@Component
struct header {
  title: string = '';

  build() {
    Column() {
      Text(this.title)
        .width('100%')
        .height(40)
        .fontSize(14)
        .backgroundColor(Color.Yellow)
        .fontColor(Color.Blue)
        .textAlign(TextAlign.Center)
    }
  }
}

@Component
struct ItemComponent {
  title: string = '';
  @Prop datas: string[];

  generateDataSource() {
    let datasource: NestedListItemDataSource = new NestedListItemDataSource();
    for (let index = 0; index < this.datas.length; index++) {
      const element = this.datas[index];
      datasource.pushData(element);
    }
    return datasource;
  }

  build() {
    Column() {
      header({ title: this.title })
      List() {
        LazyForEach(this.generateDataSource(), (data: string, index) => {
          ListItem() {
            Text(data)
              .width('100%')
              .fontSize(14)
              .backgroundColor(Color.White)
              .fontColor(bgColors[index % bgColors.length])
              .textAlign(TextAlign.Center)
          }
          .height(rowHeight)
        }, (data: string, index) => {
          console.info(`------- ${data + ' - ' + index.toString()}`);
          return data + ' - ' + index.toString();
        })
      }
      .layoutWeight(1)
      .scrollBar(BarState.Off)
      .cachedCount(10)
      .friction(1.25)
      .edgeEffect(EdgeEffect.None)
    }
  }
}

function generateData(pre: string, count: number) {
  let datas: string[] = [];
  for (let index = 0; index < count; index++) {
    const element = pre + '-' + index.toString();
    datas.push(element);
  }
  return datas;
}

@Entry
@Component
struct Index {
  private scroll: Scroller = new Scroller();

  @Builder
  private mainListView() {
    List({ scroller: this.scroll }) {
      ListItem() {
        ItemComponent({ title: 'A', datas: generateData('A', 200) })
      }

      ListItem() {
        ItemComponent({ title: 'B', datas: generateData('B', 20) })
      }
    }
    .divider({ strokeWidth: 10, color: Color.Gray })
    .height("100%")
    .width("100%")
    .scrollBar(BarState.Off)
    .edgeEffect(EdgeEffect.None)
  }

  build() {
    Column() {
      this.mainListView()
    }.width('100%')
    .height('100%')
    .backgroundColor(Color.White)
  }
}
```
