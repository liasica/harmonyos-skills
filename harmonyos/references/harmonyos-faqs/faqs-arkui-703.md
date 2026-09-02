---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-703
title: 如何使父组件能够调用子组件中的方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使父组件能够调用子组件中的方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6036e5b43ac40ce854e2b26a49bdd188e9d948e5c67df451d3317eb799be4820
---

## 问题现象

在组件的继承关系中，子组件时常会继承父组件的属性和方法并调用，是否有方案能实现父组件调用子组件中的方法？

## 背景知识

* ArkUI状态管理提供了多种[装饰器](../harmonyos-guides/arkts-state-management-overview.md#装饰器总览)，通过使用这些装饰器可以进行[状态管理](../harmonyos-guides/arkts-state-management-overview.md)。目前状态管理有两个版本：[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)和[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)。
  + 其中，V1中的装饰器[@Link](../harmonyos-guides/arkts-link.md)装饰的变量与其父组件中对应的数据源建立双向数据绑定，如果使父子组件共享的对象中的方法始终指向子组件，即可实现父组件能够调用子组件中的方法。V2中的装饰器[@Event](../harmonyos-guides/arkts-new-event.md)主要用于实现父组件向子组件传递事件，可以实现子组件调用父组件的方法修改父组件变量。
* 通过[Emitter](../harmonyos-references/js-apis-emitter.md)或[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)在子组件中设置事件监视器，在父组件中触发事件以此来实现父组件调用子组件中的方法。其中，EventHub需要通过UIAbility实例的成员变量context获取，不同的context对象拥有不同的EventHub对象，事件的订阅、取消订阅、触发都作用在某一个具体的EventHub对象上，因此不能用于虚拟机间或者进程间的事件传递。而Emitter能够在同一进程不同线程间或同一线程内发送和处理事件。

## 解决方案

* 方案一：父子组件间的数据同步与共享。
  1. 定义一个空函数的Controller类，在父组件创建该类的Controller实例并传递给子组件。
  2. 在子组件中定义实际方法，并赋值给该Controller实例，将其内部方法重载。
  3. 父组件再次调用该实例内的方法时，可以实现调用子组件重载后的新方法。

  父子组件间的数据同步与共享可参考官网常见问题：[如何实现组件数据双向同步](faqs-arkui-893.md)，以@Link为例（状态管理V2版本使用[@Param](../harmonyos-guides/arkts-new-param.md)代替@Link），示例代码如下：

  ```ts
  @Entry
  @Component
  struct ParentComponent {
    @State childController: ChildController = new ChildController(this.getUIContext());

    build() {
      Column() {
        ChildComponent({ controller: this.childController }); // 父组件引用传递单例给子组件
        Button('调用子组件方法')
          .onClick(() => {
            this.childController.changeText();
          });
      }
      .height('100%')
      .width('100%');
    }
  }

  class ChildController {
    uiContext?: UIContext;
    changeText = () => {
    };

    constructor(uiContext: UIContext) {
      this.uiContext = uiContext;
    }
  }

  @Component
  struct ChildComponent {
    @Link controller: ChildController;
    uiContext: UIContext = this.getUIContext();
    message: string = '';

    aboutToAppear() {
      if (this.controller) {
        this.controller.changeText = this.onShowToast;
      }
    }

    onShowToast() {
      this.message = '子组件被调用';
      console.info(this.message);
      if (this.message) {
        this.uiContext.getPromptAction().showToast({ message: this.message });
      } else {
        this.uiContext.getPromptAction().showToast({ message: 'this.hi is Null' });
      }
    }

    build() {
      Column() {
        Text('Hello World')
          .id('PageHelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold);
      };
    }
  }
  ```

  实现效果如下：点击父组件中的Button时，触发了子组件的弹窗效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/DZUe_sQQRDi3TQ6NMehNyQ/zh-cn_image_0000002658794251.png "点击放大")
* 方案二：父组件通知子组件调用子组件函数。

  参考[@Watch和自定义组件更新](../harmonyos-guides/arkts-watch.md#watch和自定义组件更新)，子组件通过观察父组件传递的状态变量的变化，来判断是否调用自身的函数。状态管理V2版本可以通过[@Monitor](../harmonyos-guides/arkts-new-monitor.md)代替@Watch。
* 方案三：使用通过Emitter或EventHub在子组件中设置事件监视器，在父组件中触发事件以此来实现父组件调用子组件中的方法。
  + 使用Emitter:

    ```ts
    import { emitter } from '@kit.BasicServicesKit';

    @Component
    struct EmitterChildComponent {
      // 组件加载时设置事件监听器
      aboutToAppear(): void {
        // 监听指定ID为1的事件
        emitter.on({ eventId: 1 }, (event) => {
          // 如果事件携带数据，则调用子组件方法处理数据
          if (event.data && event.data.data) {
            this.handleChildMethod(event.data.data as number);
          }
        });
      }

      // 组件销毁时，关闭事件监听
      aboutToDisappear(): void {
        emitter.off(1);
      }

      // 子组件处理方法
      handleChildMethod(value: number) {
        // 输出日志，表明子组件方法已由父组件传递的值触发
        console.info('我是子组件方法', `父组件传递的值为：${value}`);
      }

      build() {
      }
    }

    @Entry
    @Component
    struct EmitterParentComponent {
      build() {
        Column() {
          Button('调用子组件方法').onClick(() => {
            // 触发ID为1的事件，设置优先级为IMMEDIATE
            emitter.emit(
              { eventId: 1, priority: emitter.EventPriority.IMMEDIATE },
              { data: { 'data': 33 } }
            );
          });
          EmitterChildComponent();
        }
        .width('100%');
      }
    }
    ```
  + 使用EventHub:

    ```ts
    @Component
    struct EventHubChildComponent {
      // 组件加载时设置事件监听器
      aboutToAppear(): void {
        this.getUIContext().getHostContext()!.eventHub.on('1', (data: number) => {
          this.handleChildMethod(data as number);
        });
      }

      // 组件销毁时，关闭事件监听
      aboutToDisappear(): void {
        this.getUIContext().getHostContext()!.eventHub.off('1');
      }

      // 子组件处理方法
      handleChildMethod(value: number) {
        // 输出日志，表明子组件方法已由父组件传递的值触发
        console.info('我是子组件方法', `父组件传递的值为：${value}`);
      }

      build() {
      }
    }

    @Entry
    @Component
    struct EventHubParentComponent {
      build() {
        Column() {
          Button('调用子组件方法').onClick(() => {
            this.getUIContext().getHostContext()!.eventHub.emit('1', 33);
          });
          EventHubChildComponent();
        }
        .width('100%');
      }
    }
    ```

## 常见FAQ

Q：在子组件中如何调用父组件的方法？

A：参考方案一中常见问题“如何实现组件数据双向同步”的官网链接。

## 总结

| 实现方式 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| 父子组件间的数据同步与共享 | 简单直接，子组件修改可以同步到父组件 | 部分装饰器耦合度高，需要注意父子组件间函数this指针的指向问题 | 多数情况下适用 |
| @Watch/@Monitor回调 | 简单直接 | 需要联动多个字段时@Watch变得难以维护 | 需要针对单个字段做出反馈 |
| Emitter或EventHub设置事件监视器 | 简单直接，且通信方式可以不依赖于父子组件的关系 | 依靠字符串ID进行通信，难以追踪和定位；组件销毁时未移除监听可能会造成内存泄漏风险，性能消耗高 | 谨慎使用 |
