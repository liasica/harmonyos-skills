---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-916
title: "@Consume和@ObjectLink的核心差异是什么"
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > @Consume和@ObjectLink的核心差异是什么
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:91d8c9b06ef9a31aa710bf550439c178f092e6bc08aaadc213fed44d57d421bf
---

## 问题现象

在HarmonyOS的ArkUI开发中，@Consume和@ObjectLink装饰器均可实现跨组件状态共享，它们的核心差异是什么？

## 背景知识

* [@Provide和@Consume装饰器](../harmonyos-guides/arkts-provide-and-consume.md)，应用于组件与其后代组件的双向数据同步。在祖先组件中通过@Provide装饰变量，以此给所有后代组件提供状态变量，后代组件中通过@Consume装饰的变量来接收这些状态变量，实现跨组件状态共享。
* 在实际应用开发中，应用会根据开发需要，封装自己的数据模型。对于数据模型多层嵌套的场景，[@Observed/@ObjectLink装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)配套使用可以弥补@Provide/@Consume装饰器仅能观察一层的能力限制。

## 解决方案

* @Provide和@Consume作用于多层组件的参数传递，其中@Consume为数据消费方，可以通过绑定同样的key获取其最近父节点的@Provide的数据，@Provide和@Consume装饰数据类型需要一致。示例代码参考如下：

  ```ts
  @Component
  struct SceneOneChild {
    @Consume selectedDate: Date;

    build() {
      Column() {
        Button('child increase the day by 1')
          .onClick(() => {
            this.selectedDate.setDate(this.selectedDate.getDate() + 1);
          });
        Button('child update the new date')
          .margin(10)
          .onClick(() => {
            this.selectedDate = new Date('2023-09-09');
          });
        DatePicker({
          start: new Date('1970-1-1'),
          end: new Date('2100-1-1'),
          selected: this.selectedDate
        });
      };
    }
  }

  @Entry
  @Component
  struct SceneOneParent {
    @Provide selectedDate: Date = new Date('2021-08-08');

    build() {
      Column() {
        Button('parent increase the day by 1')
          .margin(10)
          .onClick(() => {
            this.selectedDate.setDate(this.selectedDate.getDate() + 1);
          });
        Button('parent update the new date')
          .margin(10)
          .onClick(() => {
            this.selectedDate = new Date('2023-07-07');
          });
        DatePicker({
          start: new Date('1970-1-1'),
          end: new Date('2100-1-1'),
          selected: this.selectedDate
        });
        SceneOneChild();
      };
    }
  }
  ```
* @Provide和@Consume只能观察到嵌套对象的第一层属性变化。而@Observed和@ObjectLink作用于父子组件间复杂对象的深层嵌套观察。示例代码参考如下：

  ```ts
  @Observed
  class Info {
    count: number;

    constructor(count: number) {
      this.count = count;
    }
  }

  @Component
  struct SceneTwoChild {
    @ObjectLink num: Info;

    build() {
      Column() {
        Text(`num的值: ${this.num.count}`)
          .onClick(() => {
            // 正确写法，可以更改@ObjectLink装饰变量的成员属性
            this.num.count = 20;
          });
      };
    }
  }

  @Entry
  @Component
  struct SceneTwoParent {
    @State num: Info = new Info(10);

    build() {
      Column() {
        Text(`count的值: ${this.num.count}`);
        Button('click')
          .onClick(() => {
            // 可以在父组件做整体替换
            this.num = new Info(30);
          });
        SceneTwoChild({ num: this.num });
      };
    }
  }
  ```

## 总结

| 装饰器 | 用法差异 | 功能差异 |
| --- | --- | --- |
| @Consume/@Provide | 父子组件传参，通过key同步数据，无需使用子组件时手动传参。 | 适用于多层组件嵌套的场景，实现跨层数据双向同步，若数据为嵌套对象只能感知第一层属性变化，无法进行深层数据变化感知。 |
| @Observed/@ObjectLink | 父子组件传参，调用子组件时需要传入参数，并通过@ObjectLink接收。 | 适用于父子组件之间双向同步复杂对象/对象数组的场景，实现嵌套对象深层属性变化的感知，并刷新渲染UI。 |
