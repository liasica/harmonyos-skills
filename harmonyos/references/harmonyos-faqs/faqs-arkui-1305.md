---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1305
title: 如何在List使用懒加载时动态修改最后一条数据样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在List使用懒加载时动态修改最后一条数据样式
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e2a99c92600d0f463006cd3213eb31c09d88883c056e46a7486e072bf17fb329
---

## 问题现象

在List使用懒加载加载下一页时，如何确保每次加载完数据后都能动态更新最后一条数据的样式？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/9TVz5nB0SQ6o_T90tnHX4Q/zh-cn_image_0000002658838283.gif "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。List列表可使用[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)进行懒加载。
* [if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)可根据应用状态，使用if、else和else if渲染相应的UI内容。
* [onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)：组件挂载后触发此回调。

## 解决方案

使用LazyForEach加载列表数据，在ListItem下使用条件渲染来判断List列表中的最后一项，并对最后一项通过挂载回调事件onAppear进行条件渲染。

```ts
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
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
    });
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
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

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

@Entry
@Component
struct MyComponent1 {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i <= 20; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }

  addData() {
    for (let i = 21; i <= 40; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }

  build() {
    List({ space: 3 }) {
      LazyForEach(this.data, (item: string, index: number) => {
        ListItem() {
          Row() {
            if (index === this.data.totalCount() - 1) {
              Text(item).fontSize(80)
                .onAppear(() => {
                  console.info("appear:" + item);
                  this.addData();
                });
            } else {
              Text(item).fontSize(50)
                .onAppear(() => {
                  console.info("appear:" + item);
                });
            }
          }.margin({ left: 10, bottom: 50 });
        };
      }, (item: string) => item);
    }.cachedCount(5).backgroundColor('#F1F3F5').expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
  }
}
```

**说明** 

如上示例中，在首次渲染时只加载前20位，直到Hello20，并且因为此时Hello20为最后一位，所以Hello20的fontSize为100，其余项的fontSize为50；在滑到最后一位时触发增加数据的操作，此时数组内有40位数据，并且Hello20不再是最后一位元素，因此fontSize恢复为50，同时Hello40为最后一位数据，fontSize为100。
