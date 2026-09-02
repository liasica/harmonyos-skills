---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-619
title: ForEach循环渲染中组件UI刷新异常问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > ForEach循环渲染中组件UI刷新异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ca7a1031da4ddac7adf320b6cfe54f3cc34df99f88d22e2041434004fdc68a65
---

## 问题现象

ForEach循环渲染中当数据发生变化UI会出现异常展示，问题如下：

* 问题一：当ForEach组件进行的是非初次渲染，会出现数据更改但UI不刷新现象，问题代码如下，当点击“按钮1”时UI未刷新：

  ```ts
  export class TestClass {
    label: string;
    value: string;

    constructor(label: string, value: string) {
      this.label = label;
      this.value = value;
    }
  }

  @Entry
  @Component
  struct Index {
    @State arrData: Array<TestClass> =
      [new TestClass('label1', 'value1'), new TestClass('label2', 'value2'), new TestClass('label3', 'value3')];

    @Builder
    ListBuilder() {
      Column() {
        ForEach(this.arrData, (item: TestClass) => {
          Text(item.value)
            .padding(8);
        }, (item: TestClass) => item.label);
      };
    }

    build() {
      Column() {
        this.ListBuilder();
        Button('按钮1')
          .margin({ top: 10 })
          .onClick(() => {
            this.arrData = [];
            // 未改变label值，UI未刷新
            this.arrData =
              [new TestClass('label1', 'value11'), new TestClass('label2', 'value21'),
                new TestClass('label3', 'value631')];
          });

        Button('按钮2')
          .margin({ top: 10 })
          .onClick(() => {
            this.arrData = [];
            // 改变了label值，UI刷新
            this.arrData =
              [new TestClass('label4', 'value12'), new TestClass('label5', 'value22'),
                new TestClass('label6', 'value32')];
          });
      }
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```
* 问题二：当数组数据被删除时，出现重复显示问题，问题代码如下，当删除第三项ListItem时，剩余的ListItem会出现“选项6”重复显示的问题：

  ```ts
  class TestItem {
    id: number = 0;
    content: string = '';
  }

  @Entry
  @Component
  struct ListTestPage {
    @State testArray: Array<TestItem> = [];

    // 删除数组项
    changeArray(testArray: Array<TestItem>, index: number): Array<TestItem> {
      if (testArray.length <= 0 || index < 0 || index >= testArray.length) {
        return testArray;
      }
      return testArray.filter((_, i) => i !== index);
    }

    build() {
      Column() {
        Text('测试List复用异常的问题')
          .fontColor(Color.Black)
          .fontSize(18);
        List({ space: 8 }) {
          ForEach(this.testArray, (itemBean: TestItem, index: number) => {
            ListItem() {
              this.builderVoteOpinionView(itemBean, index);
            };
          });
        }
        .width('90%')
        .enableScrollInteraction(false)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None)
        .margin({ top: 30 });

        // 添加按钮
        Row() {
          Button('添加列表数量');
        }
        .margin({ top: 20 })
        .borderRadius(4)
        .alignItems(VerticalAlign.Center)
        .onClick(() => {
          this.testArray.push(new TestItem());
        });
      }
      .width('100%')
      .backgroundColor(Color.White)
      .alignItems(HorizontalAlign.Center);
    }

    @Builder
    private builderVoteOpinionView(itemBean: TestItem, index: number) {
      Row() {
        TextInput({
          text: itemBean.content,
          placeholder: `选项${index + 1}`
        })
          .layoutWeight(1)
          .maxLength(14)
          .onChange((value: string) => {
            itemBean.content = value;
          })
          .defaultFocus(false); // 弹出软键盘
        Text('删除')
          .visibility(index >= 2 ? Visibility.Visible : Visibility.None)
          .onClick(() => {
            this.testArray = this.changeArray(this.testArray, index);
          });
      };
    }
  }
  ```
* 问题三：当数据源的数组项为对象数据类型，并且只修改某个数组项的属性值时UI未刷新，问题代码如下：

  ```ts
  class TestClass {
    label: string;
    value: string;

    constructor(label: string, value: string) {
      this.label = label;
      this.value = value;
    }
  }

  @Entry
  @Component
  struct Index {
    @State arrData: Array<TestClass> =
      [new TestClass('name1', 'value1'), new TestClass('name2', 'value2'), new TestClass('name3', 'value3')];

    build() {
      Column() {
        TextInput();
        Column() {
          ForEach(this.arrData, (item: TestClass) => {
            Text(item.label);
            Text(item.value);
          }, (item: TestClass) => JSON.stringify(item));
        };

        Button('点击').onClick(() => {
          this.arrData[0].value = 'valueV2';
          this.arrData[0].label = 'labelV2';
        });
      };
    }
  }
  ```

## 背景知识

* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)接口基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。
* 被状态变量装饰器装饰的变量称为状态变量，使普通变量具备状态属性。当状态变量改变时，会触发其直接绑定的UI组件渲染更新，但并不是状态变量的所有更改都会引起UI的刷新，只有可以被框架观察到的修改才会引起UI刷新，具体可参考[观察变化](../harmonyos-guides/arkts-state.md#观察变化)。
* [键值生成规则](../harmonyos-guides/arkts-rendering-control-foreach.md#键值生成规则)：ForEach提供了一个名为keyGenerator的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '\_\_' + JSON.stringify(item); }。

## 解决方案

* 问题一：当ForEach组件进行非初次渲染时，ForEach会根据传入的键值进行匹配，如果没有匹配到相同的键值则会创建一个新的组件，而当键值已存在则不会创建新的组件，转而直接渲染该键值所对应的组件，由于代码中设置label为keyGenerator，且点击按钮1时label值并未发生变化，从而导致了数据变化了但是UI并没有刷新。当出现上述问题，需要给ForEach的键值传入可变参数，修改如下：

  ```ts
  export class TestClass {
    label: string;
    value: string;

    constructor(label: string, value: string) {
      this.label = label;
      this.value = value;
    }
  }

  @Entry
  @Component
  struct S_20250318164735110531 {
    @State arrData: Array<TestClass> =
      [new TestClass('label1', 'value1'), new TestClass('label2', 'value2'), new TestClass('label3', 'value3')];

    @Builder
    ListBuilder() {
      Column() {
        ForEach(this.arrData, (item: TestClass) => {
          Text(item.value)
            .padding(8);
        }, (item: TestClass, index: number) => JSON.stringify(item) + index);
      };
    }

    build() {
      Column() {
        this.ListBuilder();
        Button('按钮1')
          .margin({ top: 10 })
          .onClick(() => {
            this.arrData = [];
            // 未改变label值，UI未刷新
            this.arrData =
              [new TestClass('label1', 'value11'), new TestClass('label2', 'value21'),
                new TestClass('label3', 'value631')];
          });

        Button('按钮2')
          .margin({ top: 10 })
          .onClick(() => {
            this.arrData = [];
            // 改变了label值，UI刷新
            this.arrData =
              [new TestClass('label4', 'value12'), new TestClass('label5', 'value22'),
                new TestClass('label6', 'value32')];
          });
      }
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```
* 问题二：从数据结构上看，ForEach渲染的每一个对象都是一致的，按照ForEach的默认keyGenerator创建规则：如果函数缺省，框架默认的键值生成函数为(item: T, index: number) => { return index + '\_\_' + JSON.stringify(item); }，也就是所有的ListItem的keyGenerator除了Index都是一致的，使得删除操作后，系统默认生成的keyGenerator无法有效区分各个ListItem是否需要新建组件，从而产生刷新异常。可通过给每个数据传入不同的id用做差异化处理，示例代码如下：

  ```ts
  class TestItemOne {
    id: number = 0;
    content: string = '';

    constructor(id: number) {
      // 构造时传入不同的id
      this.id = id;
    }
  }

  @Entry
  @Component
  struct OptionOne {
    @State testArray: Array<TestItemOne> = [];

    // 删除数组项
    changeArray(testArray: Array<TestItemOne>, index: number): Array<TestItemOne> {
      if (testArray.length <= 0 || index < 0 || index >= testArray.length) {
        return testArray;
      }
      return testArray.filter((_, i) => i !== index);
    }

    build() {
      Column() {
        Text('测试List复用异常的问题')
          .fontColor(Color.Black)
          .fontSize(18);
        List({ space: 8 }) {
          ForEach(this.testArray, (itemBean: TestItemOne, index: number) => {
            ListItem() {
              this.builderVoteOpinionView(itemBean, index);
            };
          });
        }
        .width('90%')
        .enableScrollInteraction(false)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None)
        .margin({ top: 30 });

        // 添加按钮
        Row() {
          Button('添加列表数量');
        }
        .margin({ top: 20 })
        .borderRadius(4)
        .alignItems(VerticalAlign.Center)
        .onClick(() => {
          // 构造时传入不同的id，此处以数组的长度作为数组最后一项的id，从而保证每个对象的id都不一致，从而刷新ForEach
          this.testArray.push(new TestItemOne(this.testArray.length));
        });
      }
      .width('100%')
      .backgroundColor(Color.White)
      .alignItems(HorizontalAlign.Center);
    }

    @Builder
    private builderVoteOpinionView(itemBean: TestItemOne, index: number) {
      Row({ space: 10 }) {
        TextInput({
          text: itemBean.content,
          placeholder: `选项${index + 1}`
        })
          .layoutWeight(1)
          .maxLength(14)
          .onChange((value: string) => {
            itemBean.content = value;
          })
          .defaultFocus(false);
        Text('删除')
          .visibility(index >= 2 ? Visibility.Visible : Visibility.None)
          .onClick(() => {
            this.testArray = this.changeArray(this.testArray, index);
          });
      };
    }
  }
  ```
* 问题三：由于数据源为复杂数据类型，ArkUI框架无法监听到@State装饰器修饰的数据源数组中的嵌套属性变化，从而无法触发ForEach的重新渲染，可通过@Observed+@ObjectLink或ObservedV2+@Trace。由于@ObjectLink只能修饰被@Observed装饰的类实例，所以需要在子组件声明类实例，在父组件声明对象数组并进行循环渲染，可参考[数据源数组项子属性变化](../harmonyos-guides/arkts-rendering-control-foreach.md#数据源数组项子属性变化)，这种实现方式相对复杂因此建议采用结合ObservedV2和@Trace装饰器的方式来实现ForEach循环渲染，示例代码如下：

  ```ts
  @ObservedV2
  class TestClass {
    @Trace label: string;
    @Trace value: string;

    constructor(label: string, value: string) {
      this.label = label;
      this.value = value;
    }
  }

  @Entry
  @Component
  struct Index {
    @State arrData: Array<TestClass> =
      [new TestClass('name1', 'value1'), new TestClass('name2', 'value2'), new TestClass('name3', 'value3')];

    build() {
      Column() {
        TextInput();
        Column() {
          ForEach(this.arrData, (item: TestClass) => {
            Text(item.label);
            Text(item.value);
          }, (item: TestClass) => JSON.stringify(item));
        };

        Button('点击').onClick(() => {
          this.arrData[0].value = 'valueV2';
          this.arrData[0].label = 'labelV2';
        });
      };
    }
  }
  ```

## 常见FAQ

Q：为什么使用ForEach渲染列表，编辑列表中的某个属性，界面显示不会实时变化？

A：有如下原因：

1. 属性变化需要用这两种装饰器：
   * 在V1中，@Observed与@ObjectLink装饰器用于观察类对象及其嵌套属性的变化，但V1只能观察对象的最外层属性。嵌套对象的属性需要通过自定义组件和@ObjectLink观察。此外，V1中提供了@Track装饰器实现对属性级别变化的精确控制。
   * 在V2中，结合使用@ObservedV2和@Trace，可以高效实现类对象及其嵌套属性的深度观察，省去对自定义组件的依赖，简化开发流程。同时，@Trace装饰器具备精确更新能力，替代V1中的@Track，实现更高效的UI刷新控制。
2. ForEach中的第三个参数keyGenerator使用不恰当，数据源数组项发生变化时，如果键值生成函数中的返回值没有发生改变，不会触发UI实时刷新。
