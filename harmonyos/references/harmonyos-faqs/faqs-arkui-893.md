---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-893
title: 如何实现组件数据双向同步
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现组件数据双向同步
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:30c43e6b79260b3ef5606306511070e5254b2ac4312932b0141cc42b5969c824
---

## 问题现象

开发者经常遇到需要实现各种场景下组件数据的双向绑定与同步的功能，如系统组件内部状态和状态变量之间、父子组件之间、兄弟组件之间、多层嵌套组件之间等，如何选择合适的方案？

## 背景知识

ArkUI[状态管理](../harmonyos-guides/arkts-state-management-overview.md)有两个版本：[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)和[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)。

* 在状态管理（V1）中，实现组件双向同步的方法有[$$语法](../harmonyos-guides/arkts-two-way-sync.md)，[@Link装饰器](../harmonyos-guides/arkts-link.md)，[@Provide装饰器和@Consume装饰器](../harmonyos-guides/arkts-provide-and-consume.md)等。
* 在状态管理（V2）中，也有相应的方法实现数据双向同步，例如[!!语法](../harmonyos-guides/arkts-new-binding.md)，[@Param](../harmonyos-guides/arkts-new-param.md)和[@Event](../harmonyos-guides/arkts-new-event.md)装饰器，[@Provider装饰器和@Consumer装饰器](../harmonyos-guides/arkts-new-provider-and-consumer.md)等。

## 解决方案

对于如何实现各种场景下组件数据的双向绑定与同步，总结如下：

| 场景 | 状态管理V1 | 状态管理V2 | 对比 |
| --- | --- | --- | --- |
| 场景一：系统组件的内部状态和状态变量的双向同步。 | $$语法 | !!语法 | $$语法仅用于系统组件的双向同步，而!!语法除了实现系统组件的双向同步，还可以实现自定义组件之间的双向绑定，适用范围较大，并且!!语法属于状态管理V2，会在将来得到更多的支持与优化。 |
| 场景二：父子组件建立双向数据同步。 | @Link | @Param和@Event | @Link实现父子组件双向数据绑定简单直接，子组件可直接修改父组件状态，但状态变量不能独立于UI存在。而@Param和@Event关联的状态变量独立于UI，更改数据会触发相应视图的更新。 |
| 场景三：跨多层级组件时数据的双向同步。 | @Provide和@Consume | @Provider和@Consumer | 参考官网[@Provider和@Consumer vs @Provide和@Consume能力对比](../harmonyos-guides/arkts-new-provider-and-consumer.md#provider和consumer-vs-provide和consume能力对比)。 |
| 场景四：多层嵌套场景下的数据双向同步。 | @Observed和@ObjectLink | @ObservedV2和@Trace | 相比于@Observed和@ObjectLink，装饰器@ObservedV2装饰器和@Trace装饰器在嵌套层级较深的对象属性类嵌套场景下，易用性更高，观测能力更加强大。 |
| 场景五：页面间组件数据的双向同步。 | LocalStorage和AppStorage | AppStorageV2 | LocalStorage需要配合@LocalStorageProp和@LocalStorageLink装饰器使用，AppStorage需要配合@StorageProp和@StorageLink装饰器使用，易用性差。AppStorageV2直接配合状态管理V2装饰器使用即可，易用性强，对嵌套类中属性变化的观测能力也更加强大。 |

具体每种场景的使用详情如下：

### 场景一：系统组件的内部状态和状态变量的双向同

* **状态管理V1：**

  可以使用[$$](../harmonyos-guides/arkts-two-way-sync.md)语法实现双向绑定变量，使用方法是在变量名前添加$$符号，例如$$this.text，绑定的变量变化时，会触发UI的同步刷新。

  例如，使用单选框组件[Radio](../harmonyos-guides/arkts-common-components-radio-button.md)来控制状态，并通过监听状态变化来执行特定操作：使用[@Watch](../harmonyos-guides/arkts-watch.md)监听状态变量，通过配合将状态变量与组件状态双向绑定，实现限制单选框组件Radio的切换，示例代码如下：

  ```ts
  @Entry
  @Component
  struct TestPage {
    // 定义响应式状态变量flagA，默认值为false，并监听变化调用radioChangeA方法。
    @State @Watch('radioChangeA') flagA: boolean = false;
    // 定义响应式状态变量flagB，默认值为false，并监听变化调用radioChangeB方法。
    @State @Watch('radioChangeB') flagB: boolean = false;
    currentIndex: number = 1;

    // flagA状态变化时触发的回调函数。
    radioChangeA() {
      console.info('触发修改A');
    }

    // flagB状态变化时触发的回调函数。
    radioChangeB() {
      console.info('触发修改B');
      if (this.currentIndex === 1) {
        this.flagB = true;
      } else {
        this.flagB = false;
      }
    }

    build() {
      Row() {
        Column() {
          Text('Radio1');
          Radio({ value: 'Radio1', group: 'radioGroup' }).checked($$this.flagA);
          Radio({ value: 'Radio2', group: 'radioGroup' }).checked($$this.flagB);
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/7DzTxKYgRx-K8bkHyDJ0kQ/zh-cn_image_0000002658798915.png "点击放大")

* **状态管理V2：**

  [!!语法](../harmonyos-guides/arkts-new-binding.md)能够实现双向绑定，添加方式是在变量名后添加，例如isShow!!，具体实现可参考官网[系统组件参数双向绑定使用示例](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)。

**对比：**

| 方法 | 不同点 | 适用场景 |
| --- | --- | --- |
| $$语法 | 支持的系统组件范围：参考官网[$$使用规则](../harmonyos-guides/arkts-two-way-sync.md#使用规则)。 | 适用于对系统组件的参数或属性进行双向同步的场景。 |
| !!语法 | 支持的系统组件范围：参考官网[系统组件参数双向绑定](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)中的“使用规则”。 | 不仅适用于对系统组件的参数进行双向绑定的场景，还可以配合@Param和@Event装饰器实现自定义组件之间的双向绑定。 |

### 场景二：父子组件建立双向数据同步

* **状态管理V1：**提供了[@Link装饰器](../harmonyos-guides/arkts-link.md)实现父子组件的双向数据同步：通过@Link装饰器实现组件间的数据同步，使得父子组件之间的数据变化能够即时反映在对方组件中，具体代码实现可参考示例[简单类型和类对象类型的@Link](../harmonyos-guides/arkts-link.md#简单类型和类对象类型的link)。
* **状态管理V2：**提供了[@Param](../harmonyos-guides/arkts-new-param.md)实现父到子的单向传递，子组件再通过[@Event](../harmonyos-guides/arkts-new-event.md)回调函数触发父组件的状态更新。这种方式使得状态流向更加明确，代码结构更加清晰，维护成本较低，具体代码示例可参考示例[更改父组件中变量](../harmonyos-guides/arkts-new-event.md#更改父组件中变量)。

**对比**：

| 方法 | 不同点 |
| --- | --- |
| @Link | 与数据源之间建立双向同步，当其中一方改变时，另一方也会同步更新。 |
| @Param和@Event | 父组件同步数据给子组件的过程是异步的。使用@Event修改父组件的值是立刻生效的，但从父组件将变化同步回子组件的过程是异步的，即在调用完@Event的方法后，子组件内的值不会立刻变化。 |

### 场景三：跨多层级组件时数据的双向同步

* **状态管理V1：**提供了[@Provide装饰器和@Consume装饰器](../harmonyos-guides/arkts-provide-and-consume.md)，能够将状态数据在多个层级之间传递，与后代组件双向同步，实现跨组件层级的双向同步，具体代码实现可参考文档[使用场景](../harmonyos-guides/arkts-provide-and-consume.md#使用场景)。
* **状态管理V2：**提供了[@Provider装饰器和@Consumer装饰器](../harmonyos-guides/arkts-new-provider-and-consumer.md)用于父子组件以及跨组件层级之间的数据双向同步。父组件使用@Provider提供数据，子组件通过@Consumer消费数据，并可通过事件等方式通知父组件更新数据，具体实现可参考文档[@Provider和@Consumer双向同步](../harmonyos-guides/arkts-new-provider-and-consumer.md#provider和consumer双向同步)。

两种方式的对比可以参考官网[@Provider和@Consumer vs @Provide和@Consume能力对比](../harmonyos-guides/arkts-new-provider-and-consumer.md#provider和consumer-vs-provide和consume能力对比)。

### 场景四：多层嵌套场景下的数据双向同步

* **状态管理V1：**

  提供了@Observed装饰器和@ObjectLink装饰器，实现嵌套层级下的父子类双向同步，能够解决复杂对象内部属性的响应式更新的问题。适用于嵌套对象属性修改、数组元素更新、修改大型对象的局部属性等场景。

  如下示例中，在ViewModel中使用@ObjectLink装饰器装饰类进行双向数据同步，并且将IndexViewModel、IndexItemViewModel都用@Observed修饰来监听嵌套类对象属性的变化，从而在数据变化时通过同步的对象属性来触发UI渲染，示例代码如下：

  ```ts
  // 定义列表项数据模型接口。
  interface IndexItemViewModelType {
    name: string;
    selected: boolean;

    selectItem(): void;
  }

  // 可观察的列表项数据模型实现类。
  @Observed
  class IndexItemViewModel implements IndexItemViewModelType {
    name: string;
    selected: boolean;

    constructor(name: string) {
      this.name = name;
      this.selected = false;
    }

    selectItem(): void {
      this.selected = !this.selected;
    }
  }

  interface IndexViewModelType {
    items: IndexItemViewModelType[];
  }

  @Component
  struct CustomRow {
    @ObjectLink viewModel: IndexItemViewModel;

    build() {
      Column() {

        Text(this.viewModel.name);

        // 修改名称。
        Button('name change').fontSize(20).onClick(() => {
          this.viewModel.name = this.viewModel.name + 'c1';
        });
      };
    }
  }

  @Observed
  class IndexViewModel implements IndexViewModelType {
    items: IndexItemViewModelType[];

    constructor() {
      // 初始化7个测试数据项。
      this.items = [
        new IndexItemViewModel('测试数据1'),
        new IndexItemViewModel('测试数据2'),
        new IndexItemViewModel('测试数据3'),
        new IndexItemViewModel('测试数据4'),
        new IndexItemViewModel('测试数据5'),
        new IndexItemViewModel('测试数据6'),
        new IndexItemViewModel('测试数据7'),
      ];
    }
  }

  @Entry
  @Component
  struct IndexViewTest {
    @State viewModel: IndexViewModelType = new IndexViewModel();

    build() {
      Column() {
        List({ space: 10 }) {
          ForEach(this.viewModel.items, (item: IndexItemViewModelType) => {
            ListItem() {
              CustomRow({ viewModel: item }); // 使用自定义行组件。
            }
            .width('50%')
            .onClick(() => {
              item.selectItem();
            })
            .margin({ right: 105, left: 95 });
          });
        }
        .backgroundColor('#F1F3F5')
        .margin({bottom:12})
        .width('100%')
        .height('50%');

        // 显示前两个列表项。
        CustomRow({ viewModel: this.viewModel.items[0] }).margin({bottom:12});
        CustomRow({ viewModel: this.viewModel.items[1] });
      };
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/N6la-D-_RW2X8nkN5TA-rQ/zh-cn_image_0000002628559554.png "点击放大")
* **状态管理V2：**

  可以通过[@ObservedV2装饰器和@Trace装饰器](../harmonyos-guides/arkts-new-observedv2-and-trace.md)装饰类以及类中的属性，使得被装饰的类和属性具有深度观测的能力，具体示例可参考[@ObservedV2装饰器和@Trace装饰器使用场景](../harmonyos-guides/arkts-new-observedv2-and-trace.md#使用场景)。

| 方法 | 不同点 |
| --- | --- |
| @Observed和@ObjectLink | @Observed装饰器和@ObjectLink装饰器在对嵌套类中属性的变化进行观测的过程中，当嵌套层级较深时，代码将会变得十分复杂，易用性差。 |
| @ObservedV2和@Trace | 装饰器@ObservedV2装饰器和@Trace装饰器提供了对嵌套类对象属性变化直接观测的能力，易用性强，对嵌套类中属性变化的观测能力更加强大。 |

### 场景五：页面间组件数据的双向同步

* **状态管理V1：**

  可以通过LocalStorage和AppStorage实现，使用方法可分别参考[兄弟组件之间同步状态变量](../harmonyos-guides/arkts-localstorage.md#兄弟组件之间同步状态变量)和[AppStorage在多页面中共享使用](../harmonyos-guides/arkts-appstorage.md#appstorage在多页面中共享使用)。
* **状态管理V2：**

  可以通过AppStorageV2实现，具体使用方法可参考[在两个页面之间存储数据](../harmonyos-guides/arkts-new-appstoragev2.md#在两个页面之间存储数据)。

| 方法 | 不同点 |
| --- | --- |
| LocalStorage和AppStorage | LocalStorage需要配合@LocalStorageProp和@LocalStorageLink装饰器使用，AppStorage需要配合@StorageProp和@StorageLink装饰器使用，易用性差。 |
| AppStorageV2 | 直接配合状态管理V2装饰器使用即可，易用性强，对嵌套类中属性变化的观测能力也更加强大。 |

## 常见FAQ

Q：@Link是否需要和@State类型保持完全一致？是否可以本地初始化？

A：@Link需要和@State类型保持完全一致，且必须从父组件初始化。如果没有父组件的初始化，会产生报错。@Link装饰的变量禁止本地初始化，否则编译期会报错。官网中有明确说明，详见[限制条件](../harmonyos-guides/arkts-link.md#限制条件)。
