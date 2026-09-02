---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-317
title: 如何合并两个列表并支持懒加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何合并两个列表并支持懒加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a0401803eaccdf0bb79082553bd60f346127ef3f7eea04650c30e06140f4e67a
---

外层布局使用Scroll，内层布局包含两个List：ListA和ListB。ListA位于上方，ListB位于下方。两者均采用LazyForEach方式加载数据，并绑定nestedScroll属性。

参考代码如下：

```typescript
import { MyDataSource } from './DataUtil';

@Entry
@Component
struct DoubleLazyForEach {
  private scrollerForScroll: Scroller = new Scroller();

  build() {
    Flex() {
      Scroll(this.scrollerForScroll) {
        Column() {
          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor(0X330000FF)
            .fontSize(16)
            .textAlign(TextAlign.Center)
          ListA().height('80%')
          ListB().height('80%')
        }
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding(20)
  }
}

@Component
struct ListA {
  private scrollerForListA: Scroller = new Scroller();
  private dataOne: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i <= 20; i++) {
      this.dataOne.pushData(`Hello One ${i}`);
    }
  }

  build() {
    Column() {
      List({ space: 20, scroller: this.scrollerForListA }) {
        LazyForEach(this.dataOne, (item: string) => {
          ListItem() {
            Text('ListItem' + item)
              .width('100%')
              .height('100%')
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor(Color.White)
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
      .edgeEffect(EdgeEffect.None)
      .friction(0.6)
      .nestedScroll({
        scrollForward: NestedScrollMode.SELF_FIRST,
        scrollBackward: NestedScrollMode.PARENT_FIRST
      })
    }
    .height('100%')
    .width('100%')
  }
}

@Component
struct ListB {
  private dataTwo: MyDataSource = new MyDataSource();
  private scrollerForListB: Scroller = new Scroller();

  aboutToAppear() {
    for (let i = 0; i <= 20; i++) {
      this.dataTwo.pushData(`Hello Two ${i}`);
    }
  }

  build() {
    Column() {
      List({ space: 20, scroller: this.scrollerForListB }) {
        LazyForEach(this.dataTwo, (item: string) => {
          ListItem() {
            MyText({ state_value: item })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
      .edgeEffect(EdgeEffect.None)
      .friction(0.6)
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      })
    }
  }
}

@Component
struct MyText {
  @State private state_value: string = 'Hello';

  build() {
    Text('ListItem' + this.state_value)
      .width('100%')
      .height('100%')
      .borderRadius(15)
      .fontSize(16)
      .textAlign(TextAlign.Center)
      .backgroundColor(Color.Pink)
  }
}
```

```ts
// DataUtil.ets
export class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): string {
    return this.originDataArray[index];
  }

  // This method is called on the framework side to add listener listening to the LazyForEach component at its data source
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  // This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  // Notify LazyForEach component to reload all child components
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  // Notify LazyForEach component to add a sub component at the index corresponding to the index
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  // Notify LazyForEach component that there is a change in data at the index corresponding to the index, and that the sub component needs to be rebuilt
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  // Notify LazyForEach component to remove the sub component at the index corresponding to the index
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  // Notify LazyForEach component to swap the subcomponents at the from index and to index
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }
}

export class MyDataSource extends BasicDataSource {
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
```
