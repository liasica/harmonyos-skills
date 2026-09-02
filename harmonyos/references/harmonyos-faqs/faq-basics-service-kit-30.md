---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-30
title: Emitter刷新UI失败问题
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > Emitter刷新UI失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a14016d1e0339420196da6a149a091d6e0d3355d2a9a8ea6c9a1c90adc0ef512
---

## 问题现象

在使用Emitter的过程中，将Emitter的订阅和取消都封装在class中，通过new实例来调用。Emitter订阅callback后，发送Emitter事件，参数会发生变化，但是ui并没有实际刷新。

```ts
import { emitter } from '@kit.BasicServicesKit'

export class BaseA {
  static MESSAGE_ONE = '1'
  static MESSAGE_TWO = '2'
  number1: number = 0
  number2: number = 0

  register1() {
    emitter.on(BaseA.MESSAGE_ONE, this.callback1)
  }

  register2() {
    emitter.on(BaseA.MESSAGE_TWO, () => this.callback2())
  }

  private callback1 = () => {
    this.number1 += 1
  }

  private callback2() {
    this.number2 += 1
  }
}

@Entry
@Component
struct EmitterTestPage {
  viewModel: BaseA = new BaseA()

  build() {
    Column({ space: 10 }) {
      Text('callback1:' + this.viewModel.number1.toString())
        .fontSize(18)
        .fontColor('#f00')
        .margin({ top: 20 })
      Text('callback2:' + this.viewModel.number2.toString())
        .fontSize(18)
        .fontColor('#0f0')
        .margin({ top: 20 })
      Button('发送消息，直接更新').onClick(() => {
        this.viewModel.number1 += 1
        this.viewModel.number2 += 1
      })
      Button('在viewmodel订阅消息第一种方式').onClick(() => {
        this.viewModel.register1()
      })
      Button('在viewmodel订阅消息第二种方式').onClick(() => {
        this.viewModel.register2()
      })
      Button('发送消息，更新MessageOne')
        .onClick(() => {
          emitter.emit(BaseA.MESSAGE_ONE)
        })
      Button('发送消息，更新MessageTwo')
        .onClick(() => {
          emitter.emit(BaseA.MESSAGE_TWO)
        })
    }.margin({ top: 20 })
  }
}
```

## 背景知识

[Emitter](../harmonyos-references/js-apis-emitter.md)是一个在HarmonyOS中用于进程内或同一线程间的事件处理机制，它允许应用程序进行事件的订阅、发布和取消订阅。以下是关于Emitter的详细介绍：

* 事件订阅：应用程序可以订阅一个或多个事件，当这些事件被触发时，应用程序会接收到通知。
* 事件发布：应用程序可以发布事件，这些事件会被分发给所有已订阅的监听者。
* 取消订阅：当应用程序不再需要监听特定事件时，可以取消订阅以释放资源。
* 使用场景：Emitter适用于同一进程内或不同线程间的事件处理。例如，当一个线程检测到某种状态变化时，可以通过Emitter发布事件，其他线程则可以订阅这些事件并执行相应的操作。

## 问题定位

1. 判断箭头函数中的this指向是否正确。
2. 分析变量在改变时是否有状态代理。

## 分析结论

因为箭头函数的写法本质上是变量，而变量赋值的时机是构造器刚执行的时机，@Provide将变量包装成状态变量的时机是构造器执行完毕之后，所以箭头函数里拿到的是个裸对象，不具备状态管理的能力。

## 修改建议

* **方案一**：让箭头函数赋值的逻辑晚于构造器执行逻辑，即在BaseA类中声明一个箭头函数重新赋值的方法registerCallback1，之后在@Provide("BaseA") viewModel: BaseA = new BaseA()执行之后（例如aboutToAppear回调里）调用这个registerCallback1给箭头函数重新赋值。

  ```ts
  import { emitter } from '@kit.BasicServicesKit';

  export class BaseA {
    static MESSAGE_ONE = '1';
    static MESSAGE_TWO = '2';
    number1: number = 0;
    number2: number = 0;
    private callback1 = () => {
      this.number1 += 1;
    };

    public registerCallback1() {
      this.callback1 = () => {
        this.number1 += 1;
      };
    };

    register1() {
      emitter.on(BaseA.MESSAGE_ONE, this.callback1);
    };

    register2() {
      emitter.on(BaseA.MESSAGE_TWO, () => this.callback2());
    };

    private callback2() {
      this.number2 += 1;
    };
  };

  @Entry
  @Component
  struct EmitterTestPage {
    @Provide viewModel: BaseA = new BaseA();

    aboutToAppear(): void {
      this.viewModel.registerCallback1();
    }

    build() {
      Column({ space: 10 }) {
        Text('callback1:' + this.viewModel.number1.toString())
          .fontSize(18)
          .fontColor('#f00')
          .margin({ top: 20 })
        Text('callback2:' + this.viewModel.number2.toString())
          .fontSize(18)
          .fontColor('#0f0')
          .margin({ top: 20 })
        Button('发送消息，直接更新')
          .onClick(() => {
            this.viewModel.number1 += 1;
            this.viewModel.number2 += 1;
          })
        Button('在viewmodel订阅消息第一种方式')
          .onClick(() => {
            this.viewModel.register1();
          })
        Button('在viewmodel订阅消息第二种方式')
          .onClick(() => {
            this.viewModel.register2();
          })
        Button('发送消息，更新MessageOne')
          .onClick(() => {
            emitter.emit(BaseA.MESSAGE_ONE);
          })
        Button('发送消息，更新MessageTwo')
          .onClick(() => {
            emitter.emit(BaseA.MESSAGE_TWO);
          })
      }
      .margin({ top: 20 })
      .alignItems(HorizontalAlign.Center)
      .width('100%')
    }
  }
  ```
* **方案二**：使用@ObservedV2和@Trace将number1包装成状态变量，这样当number1赋值时会直接被包装成状态变量，之后对number1的修改就都能触发状态管理。

  ```ts
  import { emitter } from '@kit.BasicServicesKit';

  @ObservedV2
  export class BaseA {
    static MESSAGE_ONE = '1';
    static MESSAGE_TWO = '2';
    @Trace number1: number = 0;
    @Trace number2: number = 0;
    private callback1 = () => {
      this.number1 += 1;
    };

    register1() {
      emitter.on(BaseA.MESSAGE_ONE, this.callback1);
    };

    register2() {
      emitter.on(BaseA.MESSAGE_TWO, () => this.callback2());
    };

    private callback2() {
      this.number2 += 1;
    };
  };

  @Entry
  @Component
  struct EmitterTestPage {
    viewModel: BaseA = new BaseA();

    build() {
      Column({ space: 10 }) {
        Text('callback1:' + this.viewModel.number1.toString())
          .fontSize(18)
          .fontColor('#f00')
          .margin({ top: 20 })
        Text('callback2:' + this.viewModel.number2.toString())
          .fontSize(18)
          .fontColor('#0f0')
          .margin({ top: 20 })
        Button('发送消息，直接更新')
          .onClick(() => {
            this.viewModel.number1 += 1;
            this.viewModel.number2 += 1;
          })
        Button('在viewmodel订阅消息第一种方式')
          .onClick(() => {
            this.viewModel.register1();
          })
        Button('在viewmodel订阅消息第二种方式')
          .onClick(() => {
            this.viewModel.register2();
          })
        Button('发送消息，更新MessageOne')
          .onClick(() => {
            emitter.emit(BaseA.MESSAGE_ONE);
          })
        Button('发送消息，更新MessageTwo')
          .onClick(() => {
            emitter.emit(BaseA.MESSAGE_TWO);
          })
      }
      .margin({ top: 20 })
      .alignItems(HorizontalAlign.Center)
      .width('100%')
    }
  }
  ```
