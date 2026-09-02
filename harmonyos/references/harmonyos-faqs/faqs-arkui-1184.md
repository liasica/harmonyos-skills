---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1184
title: 如何监听自定义子组件中TextInput输入内容的变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何监听自定义子组件中TextInput输入内容的变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd8ad12ed35ce0416b89c8ae7d648908762b64647ffdf14ea10fae32379bd25f
---

## 问题现象

在父组件中，如何获取并响应自定义子组件内TextInput输入框内容的变化？

## 背景知识

* [onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)：当[TextInput](../harmonyos-references/ts-basic-components-textinput.md)输入内容发生变化时，触发该回调。
* [@Watch](../harmonyos-guides/arkts-watch.md)：@Watch用于监听状态变量的变化，当状态变量变化时，@Watch的回调方法将被调用。
* [@Link](../harmonyos-guides/arkts-link.md#简单类型和类对象类型的link)：实现父子双向同步，子组件中被@Link装饰的变量与其父组件中对应的数据源建立双向数据绑定。

## 解决方案

* 方案一：父组件向子组件传递回调函数，在子组件TextInput的onChange回调中调用该函数，实现对输入内容变化的监听。

  ```ts
  @Component
  struct ChildComponent {
    onChange?: (value: string) => void = () => {
    };

    build() {
      Column() {
        TextInput()
          .width('80%')
          .onChange((value: string) => {
            // 更新子组件本地状态
            this.onChange?.(value);
          });
      }
      .justifyContent(FlexAlign.Center)
      .padding(20);
    }
  }

  @Entry
  @Component
  struct ParentComponent {
    // 父组件的状态：用于接收子组件传递的值
    @State parentValue: string = '';

    build() {
      Column() {
        ChildComponent({
          onChange: (value: string) => {
            // 接收子组件传递的值，并更新父组件状态
            this.parentValue = value;
          }
        });
        Text(`父组件接收到的值：${this.parentValue}`)
          .fontSize(16)
          .margin({ top: 10 });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .padding(40);
    }
  }
  ```
* 方案二：通过[@State](../harmonyos-guides/arkts-state.md)与@Link实现父子组件变量双向绑定，并在父组件中通过@Watch监听变量的变化，实现监听的目的。

  ```ts
  @Component
  struct ChildComponent1 {
    // 使用@Link修饰符绑定父组件的值，实现双向数据同步
    @Link value: string;

    build() {
      Column() {
        TextInput()
          .width('80%')
          .onChange((newValue: string) => {
            this.value = newValue;
          });
      }
      .justifyContent(FlexAlign.Center)
      .padding(20);
    }
  }

  @Entry
  @Component
  struct ParentComponent1 {
    @State @Watch('dataChange') parentValue: string = '';

    dataChange() {
      console.info('Value changed in child:', this.parentValue);
    }

    build() {
      Column() {
        // 通过$符号绑定父组件的state，实现双向绑定
        ChildComponent1({
          value: $parentValue
        });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .padding(40);
    }
  }
  ```
