---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1355
title: LazyForEach删除数据出错
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > LazyForEach删除数据出错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:718bf95a35790ac94bb59570e4f37e38a2e5db02099561496c8be72b906ce13c
---

## 问题现象

LazyForEach删除数据时结果非预期效果，出现删除后数据混乱、分组数据全部删除会有遗漏等问题。

## 背景知识

[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)是对数组类型数据进行迭代渲染，并在每次迭代过程中创建相应组件的接口。其数据源需要实现IDataSource，用于管理listener监听，以及通知LazyForEach数据更新。

## 解决方案

LazyForEach删除数据时，组件需要重新加载所有子组件，否则删除后会出现数据混乱等问题。

具体删除步骤如下：

1. 先通过索引值删除数组dataArray对应下标数据。
2. 然后调用listener.onDataDelete方法通知LazyForEach有数据删除。
3. 最后调用listener.onDataReloaded方法通知LazyForEach需要重建所有子节点。

核心代码如下所示：

```ts
// 数据源删除方法实现代码
class MyDataSource implements IDataSource {
  public totalCount(): number {
    return this.dataArray.length;
  };

  public getData(index: number): string {
    return this.dataArray[index];
  };

  registerDataChangeListener(): void {
    // ...
  };

  unregisterDataChangeListener(): void {
    // ...
  };

  private listeners: DataChangeListener[] = [];
  private dataArray: string[] = [];

  public deleteData(index: number): void {
    // 通过索引值删除数组对应数据
    this.dataArray.splice(index, 1);
    // 通知LazyForEach组件需要在index对应索引处删除该子组件
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  };

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  };
};
```

```ts
// 删除操作示例代码
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();

  build() {
    List({ space: 3 }) {
      LazyForEach(this.data, (item: string, index: number) => {
        ListItem() {
          // ...
        }
        .onClick(() => {
          this.data.deleteData(index);
          this.data.notifyDataReload();
        });
      }, (item: string) => JSON.stringify(item));
    }.cachedCount(5);
  };
};
```

## 常见FAQ

Q：调用onDatasetChange接口时报错onDatasetChange cannot be used with other interface是什么原因？

A：[onDatasetChange](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondatasetchange12)接口不能与其他DataChangeListener的更新接口（onDataDelete、onDataAdd等）混用。
