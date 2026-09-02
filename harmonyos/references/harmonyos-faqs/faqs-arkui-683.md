---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-683
title: 如何解决LazyForEach刷新数据时List无法滑动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决LazyForEach刷新数据时List无法滑动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:10f26a3ea1d705031ecd1953c0de495e4aa1c9cfb02721c36867a3560f7b7064
---

## 问题现象

通过LazyForEach加载的List列表项，给数据数组重新赋值刷新数据之后，并通过onDataReloaded方法通知组件重新刷新时，List组件滑动一段距离之后无法继续滑动。

问题代码示例参考如下：

```ts
import { BaseDataSource } from './BaseDataSource';
import { StringListModel } from './StringListModel';

@Entry
@Component
struct MyComponent {
  private dataSource: BaseDataSource<string> = StringListModel.instance().getDataSource();

  aboutToAppear() {
    StringListModel.instance().load();
  }

  aboutToDisappear(): void {
    StringListModel.instance().release();
  }

  build() {
    Column() {

      Button('刷新数据-添加hello')
        .onClick(() => {
          StringListModel.instance().loadByKeyword('hello');
        });

      List({ space: 3 }) {
        LazyForEach(this.dataSource, (item: string) => {
          ListItem() {
            Row() {
              Text(item).fontSize(50)
                .onAppear(() => {
                  console.info('appear:', `${item}`);
                });
            }
            .justifyContent(FlexAlign.Center)
            .width('100%')
            .margin({ left: 10, right: 10 });
          };
        }, (item: string) => item);
      }
      .height(0)
      .layoutWeight(1)
      .onReachEnd(() => {
        StringListModel.instance().loadMore();
      });
    };
  }
}
```

BaseDataSource.ets：

```ts
export class BaseDataSource<T> implements IDataSource {
  // 存储实际数据的数组。
  private datas: Array<T> = [];
  // 存储所有已注册的数据变更监听器。
  private listeners: Array<DataChangeListener> = [];

  totalCount(): number {
    return this.datas.length;
  }

  getData(index: number): T {
    return this.datas[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    let index = this.listeners.indexOf(listener);
    if (index < 0) {
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    let index = this.listeners.indexOf(listener);
    if (index >= 0) {
      this.listeners.splice(index, 1);
    }
  }

  private notifyDataReloaded() {
    for (let listener of this.listeners) {
      listener.onDataReloaded();
    }
  }

  private notifyDataAdd(index: number, addCount: number = 1) {
    for (let listener of this.listeners) {
      let addOperation: DataAddOperation = {
        type: DataOperationType.ADD,
        index,
        count: addCount
      };
      listener.onDatasetChange([addOperation]);
    }
  }

  private notifyDataDelete(index: number, delCount: number = 1) {
    for (let listener of this.listeners) {
      let delOperation: DataDeleteOperation = {
        type: DataOperationType.DELETE,
        index,
        count: delCount
      };
      listener.onDatasetChange([delOperation]);
    }
  }

  private notifyDataChange(index: number) {
    for (let listener of this.listeners) {
      listener.onDataChange(index);
    }
  }

  setDatas(datas: Array<T>) {
    this.datas = datas;
    this.notifyDataReloaded();
  }

  addData(data: T) {
    this.addDatas([data]);
  }

  addDatas(datas: Array<T>) {
    let insertIndex = this.datas.length;
    let addCount = datas.length;
    this.datas.push(...datas);
    this.notifyDataAdd(insertIndex, addCount);
  }

  delData(index: number) {
    this.datas.splice(index, 1);
    this.notifyDataDelete(index);
  }

  delAllData() {
    let delCount = this.datas.length;
    this.datas = [];
    this.notifyDataDelete(0, delCount);
  }

  changeData(index: number, data: T) {
    if (index < 0 || index >= this.datas.length) {
      return;
    }
    this.datas[index] = data;
    this.notifyDataChange(index);
  }

  release() {
    this.datas = [];
    this.listeners = [];
  }
}
```

DataLoader.ets：

```ts
export class DataLoader {
  static async getByPage(page: number, pageSize: number) {
    let datas: Array<string> = []
    for (let i = 0; i < pageSize; i++) {
      datas.push(`第${page}页-${i}`)
    }
    return datas
  }

  static async getByKeyWord(keyword: string, page: number, pageSize: number) {
    let datas: Array<string> = []
    for (let i = 0; i < pageSize; i++) {
      datas.push(`${keyword}-第${page}页-${i}`)
    }
    return datas
  }

  static async getByFirstLetter(letter: string, page: number, pageSize: number) {
    let datas: Array<string> = []
    for (let i = 0; i < pageSize; i++) {
      datas.push(`${letter}-第${page}页-${i}`)
    }
    return datas
  }
}
```

StringListModel.ets：

```ts
import { BaseDataSource } from './BaseDataSource';
import { DataLoader } from './DataLoader';

const MIN_PAGE_SIZE = 30;

export class StringListModel {
  private static sInstance: StringListModel | null;
  private stringDataSource: BaseDataSource<string> = new BaseDataSource();
  private curPage: number = 0;
  private pageSize: number = MIN_PAGE_SIZE;
  private hasMoreData: boolean = true;
  private keyword?: string;
  private firstLetter?: string;

  private constructor() {
  }

  static instance() {
    if (!StringListModel.sInstance) {
      StringListModel.sInstance = new StringListModel();
    }
    return StringListModel.sInstance;
  }

  // 设置每页加载的数量。
  setPageSize(pageSize: number) {
    if (pageSize >= MIN_PAGE_SIZE) {
      this.pageSize = pageSize;
    }
  }

  getDataSource() {
    return this.stringDataSource;
  }

  // 加载第一页成语数据。
  load() {
    this.keyword = undefined;
    this.firstLetter = undefined;
    this.curPage = 0;
    this.hasMoreData = true;
    this.loadData(true);
  }

  // 通过关键字来查找并加载第一页成语数据。
  loadByKeyword(keyword: string) {
    if (this.keyword !== undefined && this.keyword === keyword) {
      return;
    }
    this.keyword = keyword;
    this.firstLetter = undefined;
    this.curPage = 0;
    this.hasMoreData = true;
    this.loadData(true);
  }

  // 通过拼音首字母来查找并加载第一页成语数据。
  loadByFirstLetter(firstLetter: string) {
    if (this.firstLetter !== undefined && this.firstLetter === firstLetter) {
      return;
    }
    this.firstLetter = firstLetter;
    this.keyword = undefined;
    this.curPage = 0;
    this.hasMoreData = true;
    this.loadData(true);
  }

  // 加载更多成语数据。
  loadMore() {
    if (!this.hasMoreData) {
      return;
    }
    this.curPage++;
    this.loadData(false);
  }

  private loadData(isFirstPage: boolean) {
    let loadCallback = (datas: Array<string>) => {
      if (!datas || datas.length === 0) {
        this.hasMoreData = false;
        return;
      }

      this.hasMoreData = datas.length === this.pageSize;
      if (isFirstPage && this.stringDataSource.totalCount() > 0) {
        this.stringDataSource.setDatas(datas);
      } else {
        this.stringDataSource.addDatas(datas);
      }
    };

    if (this.keyword !== undefined) {
      DataLoader.getByKeyWord(this.keyword, this.curPage, this.pageSize).then(loadCallback);
    } else if (this.firstLetter !== undefined) {
      DataLoader.getByFirstLetter(this.firstLetter, this.curPage, this.pageSize).then(loadCallback);
    } else {
      DataLoader.getByPage(this.curPage, this.pageSize).then(loadCallback);
    }
  }

  // 在页面销毁时调用。
  release() {
    this.stringDataSource.release();
    StringListModel.sInstance = null;
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/JRY4Be2JQ6el1aQn5OSkyQ/zh-cn_image_0000002658794111.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/mcqgmOQpSV2Vyl1mAJlJjg/zh-cn_image_0000002628554746.gif "点击放大")

## 背景知识

* [onDataReloaded](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondatareloaded)能够通知组件重新加载所有数据，键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件，重新加载数据完成后调用。
* [onDatasetChange](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondatasetchange12)进行批量的数据处理后，调用onDatasetChange接口通知组件按照dataOperations刷新组件，与其它操作数据的接口不能混用。

## 问题定位

由问题代码可知，自定义方法notifyDataReloaded调用了onDataReloaded通知数据的重新加载，而调用onDataReloaded时，键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件，而单纯的调用onDataReloaded刷新数据并不会更新键值，因此在问题图中，当LazyForEach刷新数据之后，由于没有继续重建子组件，而是复用了原先的子组件，导致List列表项下滑到一定程度就无法继续下滑。

## 分析结论

在刷新数据时需要进行数据添加操作，使子组件得以重建而非复用。

## 修改建议

* **方案一**：在自定义方法notifyDataReloaded中使用onDatasetChange方法代替onDataReloaded进行组件重新加载数据，onDatasetChange能够进行批量的数据处理，包括数据添加、重载所有数据等操作，可以避免复用原先的子组件。也可以对调用notifyDataReloaded方法的setDatas方法添加数据添加功能，修改后的BaseDataSource：

  ```ts
  export class BaseDataSource<T> implements IDataSource {
    private datas: Array<T> = [];
    private listeners: Array<DataChangeListener> = [];

    totalCount(): number {
      return this.datas.length;
    }

    getData(index: number): T {
      return this.datas[index];
    }

    registerDataChangeListener(listener: DataChangeListener): void {
      let index = this.listeners.indexOf(listener);
      if (index < 0) {
        this.listeners.push(listener);
      }
    }

    unregisterDataChangeListener(listener: DataChangeListener): void {
      let index = this.listeners.indexOf(listener);
      if (index >= 0) {
        this.listeners.splice(index, 1);
      }
    }

    private notifyDataReloaded() {
      for (let listener of this.listeners) {
        let reloadOperation: DataReloadOperation = {
          type: DataOperationType.RELOAD
        };
        listener.onDatasetChange([reloadOperation]);
      }
    }

    private notifyDataAdd(index: number, addCount: number = 1) {
      for (let listener of this.listeners) {
        let addOperation: DataAddOperation = {
          type: DataOperationType.ADD,
          index,
          count: addCount
        };
        listener.onDatasetChange([addOperation]);
      }
    }

    private notifyDataDelete(index: number, delCount: number = 1) {
      for (let listener of this.listeners) {
        let delOperation: DataDeleteOperation = {
          type: DataOperationType.DELETE,
          index,
          count: delCount
        };
        listener.onDatasetChange([delOperation]);
      }
    }

    private notifyDataChange(index: number) {
      for (let listener of this.listeners) {
        listener.onDataChange(index);
      }
    }

    setDatas(datas: Array<T>) {
      this.datas = datas;
      let insertIndex = this.datas.length;
      let addCount = datas.length;
      this.datas.push(...datas);
      this.notifyDataAdd(insertIndex, addCount);
    }

    addData(data: T) {
      this.addDatas([data]);
    }

    addDatas(datas: Array<T>) {
      let insertIndex = this.datas.length;
      let addCount = datas.length;
      this.datas.push(...datas);
      this.notifyDataAdd(insertIndex, addCount);
    }

    delData(index: number) {
      this.datas.splice(index, 1);
      this.notifyDataDelete(index);
    }

    delAllData() {
      let delCount = this.datas.length;
      this.datas = [];
      this.notifyDataDelete(0, delCount);
    }

    changeData(index: number, data: T) {
      if (index < 0 || index >= this.datas.length) {
        return;
      }
      this.datas[index] = data;
      this.notifyDataChange(index);
    }

    release() {
      this.datas = [];
      this.listeners = [];
    }
  }
  ```
* **方案二**：将setDatas方法替换为先删除后再添加的方法，修改后StringListModel：

  ```ts
  import { BaseDataSource } from './BaseDataSource';
  import { DataLoader } from './DataLoader';

  const MIN_PAGE_SIZE = 30;

  export class StringListModel {
    private static sInstance: StringListModel | null;
    private stringDataSource: BaseDataSource<string> = new BaseDataSource();
    private curPage: number = 0;
    private pageSize: number = MIN_PAGE_SIZE;
    private hasMoreData: boolean = true;
    private keyword?: string;
    private firstLetter?: string;

    private constructor() {
    }

    static instance() {
      if (!StringListModel.sInstance) {
        StringListModel.sInstance = new StringListModel();
      }
      return StringListModel.sInstance;
    }

    /**
     * 设置每页加载的数量
     * @param pageSize 每页加载数量不能小于最小加载数量
     */
    setPageSize(pageSize: number) {
      if (pageSize >= MIN_PAGE_SIZE) {
        this.pageSize = pageSize;
      }
    }

    getDataSource() {
      return this.stringDataSource;
    }

    /**
     * 加载第一页成语数据
     */
    load() {
      this.keyword = undefined;
      this.firstLetter = undefined;
      this.curPage = 0;
      this.hasMoreData = true;
      this.loadData(true);
    }

    /**
     * 通过关键字来查找并加载第一页成语数据
     * @param keyword
     */
    loadByKeyword(keyword: string) {
      if (this.keyword !== undefined && this.keyword === keyword) {
        return;
      }
      this.keyword = keyword;
      this.firstLetter = undefined;
      this.curPage = 0;
      this.hasMoreData = true;
      this.loadData(true);
    }

    /**
     * 通过拼音首字母来查找并加载第一页成语数据
     * @param firstLetter
     */
    loadByFirstLetter(firstLetter: string) {
      if (this.firstLetter !== undefined && this.firstLetter === firstLetter) {
        return;
      }
      this.firstLetter = firstLetter;
      this.keyword = undefined;
      this.curPage = 0;
      this.hasMoreData = true;
      this.loadData(true);
    }

    /**
     * 加载更多成语数据
     */
    loadMore() {
      if (!this.hasMoreData) {
        return;
      }
      this.curPage++;
      this.loadData(false);
    }

    private loadData(isFirstPage: boolean) {
      let loadCallback = (datas: Array<string>) => {
        if (!datas || datas.length === 0) {
          this.hasMoreData = false;
          return;
        }

        this.hasMoreData = datas.length === this.pageSize;

        if (isFirstPage && this.stringDataSource.totalCount() > 0) {
          this.stringDataSource.delAllData();
          this.stringDataSource.addDatas(datas);
        } else {
          this.stringDataSource.addDatas(datas);
        }

      };
      if (this.keyword !== undefined) {
        DataLoader.getByKeyWord(this.keyword, this.curPage, this.pageSize).then(loadCallback);
      } else if (this.firstLetter !== undefined) {
        DataLoader.getByFirstLetter(this.firstLetter, this.curPage, this.pageSize).then(loadCallback);
      } else {
        DataLoader.getByPage(this.curPage, this.pageSize).then(loadCallback);
      }
    }

    /**
     * 释放。可在页面销毁时调用，如page页中的aboutToDisappear方法中
     */
    release() {
      this.stringDataSource.release();
      StringListModel.sInstance = null;
    }
  }
  ```

## 常见FAQ

Q：为什么onDatasetChange方法不能与其它操作数据的接口混用？

A：onDatasetChange方法用于通知LazyForEach组件进行批量的数据处理。该方法接受一个包含多个数据操作的数组作为参数。这些操作可以包括数据的添加、删除、移动等。当在onDatasetChange中传入包含删除操作的数据集时，系统会认为这是一个不兼容的操作，从而导致崩溃。因此onDatasetChange方法不能与其他操作数据的接口混用。

Q：使用onDatasetChange方法有哪些注意点？

A：调用一次onDatasetChange时，每个index对应的数据只能被操作一次。如果多次操作同一个index，LazyForEach仅生效第一次操作。并且onDatasetChange不能与其他DataChangeListener的更新接口混用。如在同一个LazyForEach中，调用过onDataAdd接口后，不能再调用onDatasetChange接口；反之，调用过onDatasetChange接口后，也不能调用onDataAdd等其他更新接口。页面中不同LazyForEach之间互不影响。具体可参考官网指南LazyForEach中的[数据更新](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#数据更新)、onDatasetChange。
