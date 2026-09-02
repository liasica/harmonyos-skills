---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-247
title: ListItemGroup和LazyForEach如何结合使用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ListItemGroup和LazyForEach如何结合使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:feff7ddc083e3d872d4454ab4de5b70fd1680e877786152f343be7d8503abf59
---

在List容器组件内可以将ListItemGroup和LazyForEach结合使用。参考代码如下：

```typescript
@Entry
@Component
struct LazyForEachDemo {
  private list: MyDataSource2 = new MyDataSource2();

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10)
  }

  @Builder
  itemFoot(num: number) {
    Text('common' + num + 'period')
      .fontSize(16)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(5)
  }

  aboutToAppear() {
    for (let date = 1; date < ~~(Math.random() * 30) + 3; date++) {
      let dayData = new DateListItem(date + '');
      for (let index = 1; index < ~~(Math.random() * 100) + 30; index++) {
        dayData.orderList.pushData(`hello${index}`);
      }
      this.list.pushData(dayData);
    }
  }

  build() {
    Column() {
      List({ space: 20 }) {
        LazyForEach(this.list, (item: DateListItem) => {
          ListItemGroup({ header: this.itemHead(item.date + ''), footer: this.itemFoot(item.orderList.totalCount()) }) {
            LazyForEach(item.orderList, (order: string) => {
              ListItem() {
                Text(order)
                  .width('100%')
                  .height(60)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(0xFFFFFF)
              }
            }, (item: string) => JSON.stringify(item))
          }
          .divider({ strokeWidth: 1, color: Color.Blue })
        })
      }
      .height('100%')
      .cachedCount(1)
      .width('90%')
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): string | DateListItem {
    return this.originDataArray[index];
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
    })
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }
}

class MyDataSource1 extends BasicDataSource {
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

class MyDataSource2 extends BasicDataSource {
  private dataArray: DateListItem[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): DateListItem {
    return this.dataArray[index];
  }

  public addData(index: number, data: DateListItem): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: DateListItem): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

class DateListItem {
  date: string;
  orderList: MyDataSource1;

  constructor(date: string) {
    this.date = date;
    this.orderList = new MyDataSource1();
  }
}
```
