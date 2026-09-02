---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-829
title: 应用内列表滑动后出现重复数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用内列表滑动后出现重复数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6e52126b295314aab9a8c33307e9114d76e0727c7b5f381bf592cff8b61f8cd1
---

## 问题现象

进入应用，在应用搜索框输入搜索关键词，得到搜索结果数据列表，进行滑动之后，出现了重复的搜索结果。

## 背景知识

[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#basicdatasource示例代码)，LazyForEach从数据源中按需迭代数据，并在每次迭代时创建相应组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。

在LazyForEach循环渲染过程中，系统为每个item生成一个唯一且持久的[键值](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#键值生成规则)，用于标识对应的组件。键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并基于新的键值创建新的组件。

## 问题定位

1. 复现问题获取日志，从问题日志信息中可以看到，应用在数据懒加载的过程中，使用了重复的键值：

   ```shell
   06-13 14:52:33.803   30081-30081   C0392D/com.dou...ceLazyForEach  com.xxx.xxx  W     [(100000:100000:scope)] Use repeat key for index: 3
   06-13 14:52:33.804   30081-30081   C0392D/com.dou...ceLazyForEach  com.xxx.xxx  W     [(100000:100000:scope)] Use repeat key for index: 4
   06-13 14:52:33.805   30081-30081   C0392D/com.dou...ceLazyForEach  com.xxx.xxx  W     [(100000:100000:scope)] Use repeat key for index: 13
   06-13 14:52:33.806   30081-30081   C0392D/com.dou...ceLazyForEach  com.xxx.xxx  W     [(100000:100000:scope)] Use repeat key for index: 14
   06-13 14:52:33.807   30081-30081   C0392D/com.dou...ceLazyForEach  com.xxx.xxx  W     [(100000:100000:scope)] Use repeat key for index: 15
   ```
2. 进一步分析在数据懒加载的过程中，当不同数据项生成的键值相同时，框架的行为是不可预测的。在滑动过程中，LazyForEach会预加载划入划出当前页面的子组件，而新建的子组件和销毁的旧子组件具有相同的键值，框架可能取用错误的缓存，导致子组件渲染出现问题。
3. 若未发现键值重复日志或问题，可能是数据源重复导致的，需要排查数据源是否重复。

## 分析结论

应用在数据懒加载的过程中，使用了重复的键值，导致子组件渲染出现问题。

## 修改建议

修改LazyForEach的键值生成函数，使每个数据项生成唯一的键值，保证渲染效果符合预期。示例代码如下：

```ts
@Entry
@Component
struct LazyForEachTest {
  private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text(item.toString())
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .cachedCount(5)
      .listDirection(Axis.Vertical) // 排列方向
      .scrollBar(BarState.Off)
      .friction(0.6)
      .divider({
        strokeWidth: 2,
        color: 0xFFFFFF,
        startMargin: 20,
        endMargin: 20
      }) // 每行之间的分界线
      .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}
```

以下是数据项中自定义数据源的实现：

```ts
class ListDataSource implements IDataSource {
  private list: number[] = [];
  private listeners: DataChangeListener[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
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

  // 通知控制器数据删除
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

  // 通知控制器添加数据
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  // 在指定索引位置删除一个元素
  public deleteItem(index: number): void {
    this.list.splice(index, 1);
    this.notifyDataDelete(index);
  }

  // 在指定索引位置插入一个元素
  public insertItem(index: number, data: number): void {
    this.list.splice(index, 0, data);
    this.notifyDataAdd(index);
  }
}
```
