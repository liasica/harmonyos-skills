---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-621
title: 上拉页面时，页面下方部分出现空白，显示异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 上拉页面时，页面下方部分出现空白，显示异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5941b8f43b351ca5f8f8f5790c74e566ededa5f65b9227bab6d092b02dd6d030
---

## 问题现象

上拉页面时，上方组件收缩，下方组件上移，组件下方显示大量空白。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Xi1R_ZlVRP6qhu3MmSVz0Q/zh-cn_image_0000002658913483.png "点击放大")

## 背景知识

[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)为滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 问题定位

查看下方组件的设置，发现未根据上方组件的变化动态设置自身的尺寸。

```screen
class TimeTableDataSource implements IDataSource {
  private list: TimeTable[] = [];
  private listeners: DataChangeListener[] = [];

  constructor(list: TimeTable[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): TimeTable {
    return this.list[index];
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

  // 通知控制器数据变化
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

  // 修改第一个元素
  public change1stItem(temp: TimeTable): void {
    this.list[0] = temp;
    this.notifyDataChange(0);
  }
}

class ProjectsDataSource implements IDataSource {
  private list: string[] = [];

  constructor(list: string[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): string {
    return this.list[index];
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

interface TimeTable {
  title: string;
  projects: string[];
}

@Entry
@Component
struct ListItemGroupExample {
  itemGroupArray: TimeTableDataSource = new TimeTableDataSource([]);
  @State show: boolean = true;
  @State textHeight: string = '30%';
  private tuesday: TimeTable = {
    title: '星期二',
    projects: ['物理', '化学', '生物', '历史', '地理']
  };

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .width('100%')
      .padding(10);
  }

  build() {
    Column() {
      Text('收缩组件')
        .height(this.textHeight)
        .textAlign(TextAlign.Center)
        .width('90%')
        .borderRadius(20)
        .backgroundColor('#f1f3f5');
      List() {
        ListItemGroup({
          header: this.itemHead(this.tuesday.title),
          space: 10
        }) {
          LazyForEach(new ProjectsDataSource(this.tuesday.projects), (project: string) => {
            ListItem() {
              Text(project)
                .width('100%')
                .height(150)
                .fontSize(20)
                .textAlign(TextAlign.Center)
                .backgroundColor('#f1f3f5')
                .borderRadius(20)
            };
          }, (item: string) => item);
        }
      }
      .width('90%')
      .height('70%') // 列表高度固定，未根据上方组件的变化动态设置自身的尺寸
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off);
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
    .padding({ top: 5 })
    .gesture(
      // 绑定拖动手势
      PanGesture()
        .onActionStart(() => {
          this.show = !this.show;
          // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
          if (this.show) {
            this.textHeight = '30%';
          } else {
            this.textHeight = '5%';
          }
        })
    );
  }
}
```

## 分析结论

上方组件收缩时，下方组件未动态调整自身尺寸，导致页面部分空白。

## 修改建议

上方组件收缩时，下方组件动态调整自身尺寸。

```screen
import { ProjectsDataSource, TimeTable, TimeTableDataSource } from '../utils/ListDataSource';

@Entry
@Component
struct ListItemGroupExample {
  itemGroupArray: TimeTableDataSource = new TimeTableDataSource([]);
  @State show: boolean = true;
  @State textHeight: string = '30%';
  @State listHeight: string = '70%';
  private tuesday: TimeTable = {
    title: '星期二',
    projects: ['物理', '化学', '生物', '历史', '地理']
  };

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor('#f1f3f5')
      .width('100%')
      .padding(10);
  }

  @Builder
  itemFoot(num: number) {
    Text('共' + num + '节课')
      .fontSize(16)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(5);
  }

  build() {
    Column() {
      Text()
        .height(this.textHeight)
        .width('100%')
        .backgroundColor('#ccffff');
      List({ space: 20 }) {
        ListItemGroup({
          header: this.itemHead(this.tuesday.title),
          footer: this.itemFoot(this.tuesday.projects.length)
        }) {
          LazyForEach(new ProjectsDataSource(this.tuesday.projects), (project: string) => {
            ListItem() {
              Text(project)
                .width('100%')
                .height(150)
                .fontSize(20)
                .textAlign(TextAlign.Center)
                .backgroundColor(0xFFFFFF);
            };
          }, (item: string) => item);
        }
        .divider({ strokeWidth: 1, color: '#f1f3f5' }); // 每行之间的分界线
      }
      .width('100%')
      .height(this.listHeight)
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off);
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
    .padding({ top: 5 })
    .gesture(
      // 绑定拖动手势
      PanGesture()
        .onActionStart(() => {
          this.show = !this.show;
          if (this.show) {
            this.textHeight = '30%';
            this.listHeight = '70%';
          } else {
            this.textHeight = '5%';
            this.listHeight = '95%'; // 上方组件收缩时，下方组件动态调整自身尺寸
          }
        })
      // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
    );
  }
}
```

src/main/ets/utils/ListDataSource.ets：

```screen
export class TimeTableDataSource implements IDataSource {
  private list: TimeTable[] = [];
  private listeners: DataChangeListener[] = [];

  constructor(list: TimeTable[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): TimeTable {
    return this.list[index];
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

  // 通知控制器数据变化
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

  // 修改第一个元素
  public change1stItem(temp: TimeTable): void {
    this.list[0] = temp;
    this.notifyDataChange(0);
  }
}

export class ProjectsDataSource implements IDataSource {
  private list: string[] = [];

  constructor(list: string[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): string {
    return this.list[index];
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

export interface TimeTable {
  title: string;
  projects: string[];
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/caOW8XtjRbeU31ew4FvJAQ/zh-cn_image_0000002658793531.png "点击放大")
