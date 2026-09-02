---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-593
title: List嵌套LazyForEach滚动条大小会变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List嵌套LazyForEach滚动条大小会变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc3123726316293eed796a64afa73a20db30067b4accbfa70f55c69ee6404175
---

## 问题现象

使用LazyForEach加载多个ListItemGroup及其内部的多个Item时，滚动条在滑动过程中会出现长度变化问题。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/vzlszmxPQW66c9dwSHq_sg/zh-cn_image_0000002628392522.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/r-09YqjPTIag5xYrkKuyVQ/zh-cn_image_0000002658911741.gif "点击放大")

## 背景知识

* [ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)是一次性加载全量数据至List，界面滚动的高度已经确定，所以滚动条大小不会改变。但是数据量大的情况下会有内存占用大、页面加载缓慢的问题。
* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)采取懒加载策略，根据界面显示范围加载少量数据，在List滚动过程中会逐渐加载新的数据。

## 解决方案

当使用嵌套的LazyForEach结构时（外层加载ListItemGroup，内层加载ListItem），由于LazyForEach的按需加载特性，滚动条长度会根据当前可视区域内已加载的ListItemGroup中的ListItem数量动态计算，而非基于所有ListItemGroup的总项数。这会导致滑动时滚动条尺寸频繁变化，影响视觉体验。

可以采用混合渲染策略：

* 外层使用ForEach一次性加载ListItemGroup，确保滚动条总长度基于完整的列表项数量计算。
* 内层使用LazyForEach按需加载ListItem，在ListItemGroup内部实现子项的懒加载，保持性能优化优势。

使用ForEach加载2个ListItemGroup，第一个ListItemGroup懒加载30个ListItem，第二个ListItemGroup懒加载350个ListItem。

```ts
@Entry
@Component
struct ListScrollBarSize {
  private groupDataSource: GroupDataSource = new GroupDataSource(); // 数据源

  // 初始化数据
  aboutToAppear() {
    const group1 = new GroupItem(`分组1`);
    for (let itemIndex = 1; itemIndex <= 30; itemIndex++) {
      group1.addItem(`第1组-项${itemIndex}`);
    }
    this.groupDataSource.addGroup(group1);
    const group2 = new GroupItem(`分组2`);
    for (let itemIndex = 1; itemIndex <= 350; itemIndex++) {
      group2.addItem(`第2组-项${itemIndex}`);
    }
    this.groupDataSource.addGroup(group2);
  }

  // 分组头部构建器
  @Builder
  groupHeader(title: string) {
    Text(title)
      .fontSize(20)
      .fontWeight(FontWeight.Bold)
      .backgroundColor(Color.White)
      .width('100%')
      .padding({ top: 8, bottom: 8 });
  }

  build() {
    Column() {
      List({ space: 12 }) {
        ForEach(this.groupDataSource.groups, (group: GroupItem) => {
          ListItemGroup({ header: this.groupHeader(group.title), style: ListItemGroupStyle.CARD, space: 12 }) {
            LazyForEach(group.itemSource, (item: string) => {
              ListItem() {
                Text(item)
                  .width('100%')
                  .height(60)
                  .textAlign(TextAlign.Center);
              }
              .borderRadius(12)
              .backgroundColor('#F1F3F5');
            }, (item: string) => item); // 使用内容本身作为唯一标识
          };
        }, (group: GroupItem) => group.title); // 使用分组标题作为唯一标识
      }.padding({ left: 8, right: 8 }).width('100%').height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
    };
  }
}
```

```ts
// 分组数据源实现
class GroupItem {
  title: string;
  itemSource: ItemDataSource;

  constructor(title: string) {
    this.title = title;
    this.itemSource = new ItemDataSource();
  }

  addItem(item: string) {
    this.itemSource.pushData(item);
  }
}

// 主数据源类
class GroupDataSource implements IDataSource {
  groups: GroupItem[] = [];
  private listeners: DataChangeListener[] = [];

  addGroup(group: GroupItem) {
    this.groups.push(group);
    this.notifyDataReload();
  }

  totalCount(): number {
    return this.groups.length;
  }

  getData(index: number): GroupItem {
    return this.groups[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this.listeners.push(listener);
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const index = this.listeners.indexOf(listener);
    if (index >= 0) {
      this.listeners.splice(index, 1);
    }
  }

  private notifyDataReload() {
    this.listeners.forEach(listener => listener.onDataReloaded());
  }
}

// 子项数据源类
class ItemDataSource implements IDataSource {
  private items: string[] = [];
  private listeners: DataChangeListener[] = [];

  pushData(item: string) {
    this.items.push(item);
    this.notifyDataAdd(this.items.length - 1);
  }

  totalCount(): number {
    return this.items.length;
  }

  getData(index: number): string {
    return this.items[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this.listeners.push(listener);
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const index = this.listeners.indexOf(listener);
    if (index >= 0) {
      this.listeners.splice(index, 1);
    }
  }

  private notifyDataAdd(index: number) {
    this.listeners.forEach(listener => listener.onDataAdd(index));
  }
}
```
