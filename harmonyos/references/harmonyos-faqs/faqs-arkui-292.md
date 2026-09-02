---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-292
title: 如何实现二维数组的懒加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现二维数组的懒加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:12ca171fa71f68af28479bc6c08f8ba0c7fcc69eafe6c5cf4fc804f65ca88eb3
---

通过HashMap存储二维数组数据，并利用ListGroup组件实现分组懒加载，其中HashMap的键为分组标题，值为对应分组的数据源。示例代码如下：

```ts
import { HashMap } from '@kit.ArkTS';

class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: Array<TimeTable> | Array<string> = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): TimeTable | string {
    if (index < 0 || index >= this.originDataArray.length) {
      return '';
    }
    return this.originDataArray[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
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

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }
}

class MyDataSource extends BasicDataSource {
  private dataArray: TimeTable[] | Array<string> = [];

  constructor(data: Array<TimeTable> | Array<string>) {
    super();
    this.dataArray = data;
  }

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): TimeTable | string {
    return this.dataArray[index];
  }

  public addDataTimeTable(index: number, data: TimeTable): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public addDataString(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushDataTimeTable(data: TimeTable): void {
    (this.dataArray as Array<TimeTable>).push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }

  public pushDataString(data: string): void {
    (this.dataArray as Array<string>).push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

/*
 * The course schedule data structure, title represents the day of the week, and projects represents the list of courses for that day
 */
interface TimeTable {
  title: string;
  projects: string[];
}

@Component
export struct TwoNestingArrayLazy {
  @State timeTable: TimeTable[] = [
    {
      title: 'Monday',
      projects: ['language', 'mathematics', 'English']
    },
    {
      title: 'Tuesday',
      projects: ['physics', 'chemistry', 'biology']
    },
    {
      title: 'Wednesday',
      projects: ['history', 'geography', 'politics']
    },
    {
      title: 'Thursday',
      projects: ['the fine arts', 'music', 'sport']
    }
  ];
  private data1: MyDataSource = new MyDataSource(this.timeTable);
  private hashMap: HashMap<string, MyDataSource> = new HashMap<string, MyDataSource>();

  aboutToAppear(): void {
    for (let index = 0; index < this.timeTable.length; index++) {
      this.hashMap.set(this.timeTable[index].title, new MyDataSource(this.timeTable[index].projects));
    }
  }

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10)
  }

  @Builder
  itemFoot(itemCount: number) {
    Text('common' + itemCount + 'period')
      .fontSize(16)
      .backgroundColor(0xAABBCC)
      .width("100%")
      .padding(5)
  }

  build() {
    List({ space: 3 }) {
      LazyForEach(this.data1, (item: TimeTable) => {
        ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
          LazyForEach(this.hashMap.get(item.title), (project: string) => {
            ListItem() {
              Text(project)
                .width('100%')
                .height(100)
                .fontSize(20)
                .textAlign(TextAlign.Center)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .divider({ strokeWidth: 1, color: Color.Blue }) // The boundary line between each row
      }, (item: string) => item)
    }
    .width('100%')
    .height('100%')
  }
}
```
