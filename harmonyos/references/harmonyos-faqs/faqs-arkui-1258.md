---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1258
title: 如何获取LocalStorage实例对象
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取LocalStorage实例对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:37f360cc42b994d9aff51270903f655dad789d70865fe4d0507fb59ea6fafe71
---

## 问题现象

在组件中创建LocalStorage实例的情况下，其他组件如何获取该组件的LocalStorage实例？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/3RMSyjMWSviXUcb_J3CWvg/zh-cn_image_0000002658955245.gif "点击放大")

## 背景知识

* [LocalStorage](../harmonyos-guides/arkts-localstorage.md)是页面级的UI状态存储，通过@Entry装饰器接收的参数可以在页面内共享同一个LocalStorage实例。LocalStorage中，[@LocalStorageLink](../harmonyos-guides/arkts-localstorage.md#localstoragelink)装饰的变量能够与LocalStorage中给定属性建立双向同步关系。
* [export](../harmonyos-guides/in-app-hsp.md#导出类和方法)导出方法和import导入方法可以将对象、变量等传递给其他组件。

## 解决方案

* **方案一**：通过export将Storage实例导出。

  在模块化清晰、单向访问的场景，可以通过export将组件中创建的Storage实例导出，在其他组件用import导入，即可使其他组件直接访问Storage对象，并且可以通过应用逻辑方式修改数据，这种方法简单易用并且在性能上相比于使用@LocalStorageLink有一定优势，适用于工具箱之类的小型项目。

  组件导出Storage：

  ```ts
  let para: Record<string, number> = { 'propA': 47 };

  const storage: LocalStorage = new LocalStorage(para);

  export { storage };
  ```

  其他组件接收Storage实例，并通过应用逻辑方式修改数据。

  ```ts
  import { storage } from './LocalStorageFatherOne';

  @Entry
  @Component
  export struct LocalStorageChildOne {
    @State link1: SubscribedAbstractProperty<number> = storage.link('propA');

    build() {
      Column() {
        Text('子组件linkChild：' + JSON.stringify(this.link1.get()))
          .onClick(() => {
            this.link1.set(this.link1.get() + 1);
          });
      }.width('100%').height('100%').justifyContent(FlexAlign.Center);
    }
  }
  ```

* **方案二**：使用LocalStorage装饰器@LocalStorageLink。

  可以使用LocalStorage装饰器@LocalStorageLink实现父子组件双向同步，子组件就能实现对LocalStorage实例的访问，能够将状态变量更新同步回LocalStorage中，可以参考官网[@LocalStorageLink和LocalStorage双向同步的简单场景](../harmonyos-guides/arkts-localstorage.md#localstoragelink和localstorage双向同步的简单场景)。

* **方案三**：通过状态变量在父子组件之间传递Storage。

  当父子组件之间需要频繁地交互LocalStorage中的数据时，就可以使用状态变量传递LocalStorage实例，此时子组件只需要接收父组件的实例，可以避免数据混淆，便于数据分类，适用于表单系统等场景。

  父组件：

  ```ts
  import { LocalStorageChildTwo } from './LocalStorageChildTwo';

  // 创建新实例并使用给定对象初始化
  let para: Record<string, number> = { 'propA': 47 };
  let storage: LocalStorage = new LocalStorage(para);

  @Entry
  @Component
  struct LocalStorageFatherTwo {
    @State storageFather: LocalStorage = storage;

    build() {
      Column({ space: 15 }) {
        // @Component子组件自动获得对LocalStorage实例的访问权限。
        LocalStorageChildTwo({ storageChild: this.storageFather });
      };
    }
  }
  ```

  在需要获取LocalStorage实例的组件中，通过@Link装饰器将storageChild属性链接到父组件的LocalStorage实例，并且使用this.storageChild.link('propA')将link1状态链接到LocalStorage中名为propA的属性。为Text组件添加onClick事件处理程序，在每次点击时，都将更新link1的值，实现状态的共享和更新。

  子组件：

  ```ts
  @Component
  export struct LocalStorageChildTwo {
    @Link storageChild: LocalStorage;
    @State link1: SubscribedAbstractProperty<number> = this.storageChild.link('propA');

    build() {
      Column() {
        Text('子组件linkChild：' + JSON.stringify(this.link1.get()))
          .onClick(() => {
            this.link1.set(this.link1.get() + 1);
          });
      }.width('100%').height('100%').justifyContent(FlexAlign.Center);
    }
  }
  ```

## 常见FAQ

Q：LocalStorage实例在文件根目录进行初始化，其生命周期会跟随页面的生命周期吗？

A：LocalStorage对象的生命周期由应用程序决定，当应用释放最后一个指向LocalStorage的引用时才会被JS Engine垃圾回收。

Q：子组件可以通过LocalStorage.getShared()方法获取LocalStorage实例吗？

A：未被@Entry装饰的组件不可被独立分配LocalStorage实例，只能接受父组件通过@Entry传递来的LocalStorage实例，子组件实例自动获得对该LocalStorage实例的访问权限。LocalStorage.getShared只能在父组件才能获取到数据。

Q：在主页面中调用loadContent传递LocalStorage实例，为什么在其他页面中通过LocalStorage.getShared()获取的值是undefined？

A：LocalStorage是页面级存储，getShared()接口仅能获取当前Stage通过windowStage.loadContent传入的LocalStorage实例，否则返回undefined，可以参考[LocalStorage使用的限制条件](../harmonyos-guides/arkts-localstorage.md#限制条件)和示例[将LocalStorage实例从UIAbility共享到一个或多个页面](../harmonyos-guides/arkts-localstorage.md#将localstorage实例从uiability共享到一个或多个页面)。

## 总结

关于子组件如何获取LocalStorage实例，本文一共提供了三种方案。

| 方案 | 适用场景 |
| --- | --- |
| 通过export将Storage实例导出 | 该方案不能做到组件之间双向同步。适用于模块化清晰、单向访问的场景。 |
| 使用LocalStorage装饰器@LocalStorageLink | 官网文档提供的方法，适用于大多数场景。 |
| 通过状态变量传递Storage | 通过状态变量传递Storage实例，子组件无法访问全局LocalStorage实例，灵活性被限制，但是子组件只接收父组件的实例，可以避免引起频繁刷新影响性能，也可以防止数据混淆，适用于频繁交互数据的场景。 |
