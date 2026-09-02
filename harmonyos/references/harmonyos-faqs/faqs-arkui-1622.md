---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1622
title: 数据库加载成功后，页面无法监听数据变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 数据库加载成功后，页面无法监听数据变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:466cfcae0b7c9463514894d86974b35a295e202dadb2d81d83832d5934e22c5d
---

## 问题现象

从数据库异步获取数据后，有数据发生变化，但是页面显示的数据没有刷新。

## 背景知识

项目开发中，应用可能需要从数据库、服务器等异步获取数据用于在UI页面显示。对于这些数据，开发者通常会选择创建一个数据管理类用来统一管理数据的获取、更新等，而不会选择直接放到UI中。对于这类数据的变化，UI页面需要监听数据类中的数据变化进行刷新。以下提供两种实现方式供开发者参考。

1. [AppStorage](../harmonyos-guides/arkts-appstorage.md)和[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)装饰器（推荐）。
2. 观察者模式，页面订阅数据变化事件。

页面刷新逻辑如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Xah-jTlHTN--uUpCF0r-tQ/zh-cn_image_0000002628617572.png "点击放大")

## 解决方案

* 方案一：AppStorage和@StorageProp装饰器。

  AppStorage能设置应用全局的UI状态存储，可以通过[@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)实现应用和组件状态的双向同步，通过@StorageProp实现应用和组件状态的单向同步。在数据管理类中，使用AppStorage将数据设置为全局状态变量，并在数据变化时实时更新至全局状态变量。在UI页面使用@StorageLink获取该变量，会自动同步全局状态变量的变化。

  DataManager.ets文件代码如下：

  ```ts
  export class Item {
    id: string = '';
    title: string = '';
  }

  export class DataManager {
    private static instance: DataManager;
    public data: Array<Item> = [];

    // 单例模式
    static getInstance(): DataManager {
      if (!DataManager.instance) {
        DataManager.instance = new DataManager();
      }
      return DataManager.instance;
    }

    private flushData() {
      AppStorage.set<Array<Item>>('test', this.data); // key-value形式，设置一个应用级状态变量
    }

    // 模拟从数据库获取数据
    async getDataFromDB() {
      setTimeout(() => {
        this.data.push({ id: '1', title: '2' });
        this.flushData(); // 更新全局状态变量
      }, 2000); // 模拟延时操作
    }

    // 获取数据
    getData(): Array<Item> {
      return this.data;
    }

    // 更新数据
    async updateData(newData: Array<Item>) {
      setTimeout(() => {
        this.data = newData;
        this.flushData(); // 更新全局状态变量
      }, 1000);
    }
  }
  ```

  AppStorageSolution.ets文件代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  import { DataManager, Item } from './DataManager';

  @Entry
  @Component
  struct AppStorageSolution {
    dataManager: DataManager = DataManager.getInstance();
    @StorageLink('test') data: Array<Item> = []; // 全局状态变量的改变会自动同步至data局部变量

    aboutToAppear(): void {
      this.dataManager.getDataFromDB();
    }

    build() {
      RelativeContainer() {
        if (this.data.length > 0) {
          Text(`${this.data[0].id} ${this.data[0].title}`)
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .onClick(() => {
              this.dataManager.updateData([{ id: '2', title: '4' }]);
            });
        }
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

* 方案二：观察者模式。页面订阅数据变化，数据管理类在数据发生变化时通知订阅者。
  1. 在DataManager中创建订阅者集合（回调函数集合）。
  2. 在DataManager中实现注册监听、移除监听、通知监听者三个接口方法（分别对应添加回调函数、移除回调函数、触发回调函数）。
  3. DataManager要在内部data发生变化时执行回调函数，如数据库异步加载数据成功，或者数据被其它页面修改等。
  4. 在PageA中要将要执行的回调函数updateData通过注册监听接口放入DataManager回调函数集合，在DataManager中的数据变化时，会通过回调函数同步至PageA中的data，再通过@State装饰器，页面即可自动刷新。

  DataManager2.ets文件代码如下：

  ```ts
  export class DataManager {
    private static instance: DataManager;
    private data: Array<string> = [];
    private observers: Array<() => void> = []; // 观察者列表

    // 单例模式
    static getInstance(): DataManager {
      if (!DataManager.instance) {
        DataManager.instance = new DataManager();
      }
      return DataManager.instance;
    }

    // 模拟异步操作从数据库/服务器获取数据
    async getDataFromDB() {
      setTimeout(() => {
        this.data = ['1', '2', '3'];
        this.notifyObservers(); // 数据加载完成后通知观察者
      }, 2000); // 模拟延时操作
    }

    // 获取数据
    getData(): Array<string> {
      return this.data;
    }

    // 更新数据
    updateData(newData: Array<string>): void {
      this.data = newData;
      this.notifyObservers(); // 通知所有观察者
    }

    // 注册观察者
    addObserver(callback: () => void): void {
      this.observers.push(callback);
    }

    // 移除观察者
    removeObserver(callback: () => void): void {
      this.observers = this.observers.filter(obs => obs !== callback);
    }

    // 通知所有观察者
    private notifyObservers(): void {
      this.observers.forEach(callback => callback());
    }
  }
  ```

  PageA.ets文件代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```screen
  import { DataManager } from './DataManager2';

  @Entry
  @Component
  struct PageA {
    @State data: Array<string> = [];
    private dataManager = DataManager.getInstance();

    aboutToAppear(): void {
      this.data = this.dataManager.getData();
      this.dataManager.addObserver(this.updateData.bind(this)); // 注册监听
      this.dataManager.getDataFromDB(); // 从数据库获取数据
    }

    aboutToDisappear() {
      // 移除监听防止内存泄漏
      this.dataManager.removeObserver(this.updateData.bind(this));
    }

    updateData(): void {
      this.data = this.dataManager.getData(); // 更新数据
    }

    build() {
      Column() {
        Text(JSON.stringify(this.data));
      }.height('100%').width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
