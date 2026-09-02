---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-13
title: PC中List如何通过上下键循环走焦
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > PC中List如何通过上下键循环走焦
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:101127a3d8f9dafb586963e071ba118528ab1f87302c3322eed8bb10126a3daf
---

## 问题现象

在PC中使用方向键中的上下键对List进行走焦时，无法实现循环走焦，即无法通过上键从第一个ListItem走到最后一个，也无法通过下键从最后一个ListItem走到第一个。如何能够实现上下键循环走焦？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/2jWQqYswT1mnCpvJqXXdqQ/zh-cn_image_0000002628392468.png "点击放大")

## 背景知识

[nextFocus](../harmonyos-references/ts-universal-attributes-focus.md#nextfocus18)设置组件的自定义焦点走焦逻辑。可以指定某个按键下一次的走焦对象，该对象通过组件ID确定。

## 解决方案

将LazyForEach中Item的值作为每个ListItem的ID，对每个ListItem设置nextFocus方法，如果当前为第一个ListItem，则方向上键走到最后一个ListItem，如果当前为最后一个ListItem，则方向下键走到第一个ListItem。如果不是第一个或最后一个ListItem，则方向上键走到上个ListItem，方向下键走到下一个ListItem。

```ts
// BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return this.originDataArray.length;
  }

  public getData(index: number): string {
    return this.originDataArray[index];
  }

  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
    });
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
    });
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
    });
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
      // 写法2：listener.onDatasetChange(
      //         [{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
    });
  }

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    });
  }
}

class MyDataSource extends BasicDataSource {
  private dataArray: string[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string {
    return this.dataArray[index];
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

@Entry
@Component
struct CycleFocus {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i <= 20; i++) {
      this.data.pushData(`${i}`);
    }
  }

  build() {
    Column() {
      List({ space: 3 }) {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            Row() {
              Text(item)
                .fontSize(50)
                .focusable(true);
            }
            .width('100%')
            .justifyContent(FlexAlign.Center)
            .focusOnTouch(true)
            .id(item)
            .nextFocus({
              up: item === '0' ? '20' : String(Number(item) - 1),
              down: item === '20' ? '0' : String(Number(item) + 1)
            })
            .onFocus(() => {
              console.info(`onfocus:${item}`);
            })
            .focusable(true)
            .margin({ left: 10, right: 10 });
          }
          .focusable(true);
        }, (item: string, index: number) => item + index.toString());
      };
    };
  };
}
```
