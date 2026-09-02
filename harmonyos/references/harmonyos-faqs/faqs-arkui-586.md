---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-586
title: 如何为自定义组件添加一个控制器
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何为自定义组件添加一个控制器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a133dfb79eedea5c8c4a363203465db234e0be40346f15437d6fce675abf567a
---

## 问题现象

在自定义组件中，除通过状态管理装饰器控制UI变化外，能否通过在外部（父组件）使用控制器控制其UI显示？

## 背景知识

* [自定义组件](../harmonyos-guides/arkts-custom-components.md)：进行UI界面开发时，不仅要组合使用系统组件，还需考虑代码的可复用性、业务逻辑与UI的分离，以及后续版本的演进等因素。因此，将UI和部分业务逻辑封装成自定义组件是不可或缺的能力。
* 组件控制器：不同的组件通常有不同的控制器，用于控制组件的行为。例如系统组件的控制器：可滚动容器组件的控制器[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)、List组件的滚动控制器[ListScroller](../harmonyos-references/ts-container-list.md#listscroller11)、Tabs组件的控制器[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)、Text组件的控制器[TextController](../harmonyos-references/ts-basic-components-text.md#textcontroller11)、自定义弹窗的控制器[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)等等。

## 解决方案

实现思路如下：

* 父组件负责创建子组件控制器实例并触发控制逻辑。
* 子组件中进行注册和绑定，使得子组件控制器得到子组件实例引用，建立双向通信通道。

  参考示例：父组件初始化时创建共享Scroller和控制器，通过构造函数将Scroller注入控制器，在子组件完成Scroller绑定。

  ```ts
  // 子组件控制器
  class HelloComponentController {
    private helloComponent?: HelloComponent;
    scroller: Scroller = new Scroller();

    constructor(scroller: Scroller) {
      this.scroller = scroller;
    }

    bindHelloComponentController(helloComponent: HelloComponent) {
      this.helloComponent = helloComponent;
    }

    customFunc() {
      this.helloComponent?.customFunc();
    }
  }

  @Entry
  @Component
  struct ComponentController {
    scroller: Scroller = new Scroller();
    controller: HelloComponentController = new HelloComponentController(this.scroller);

    build() {
      Column() {
        Column() {
          Button('示例: 父组件通过controller控制子组件').onClick(() => {
            // 通过子组件控制器触发子组件滚动
            this.controller?.scroller.scrollTo({ xOffset: 0, yOffset: 200, animation: true });
            // 通过子组件控制器间接调用子组件自定义方法
            this.controller?.customFunc();
          })
            .type(ButtonType.Capsule);
          HelloComponent({ controller: this.controller });
        }
        .height('100%')
        .alignItems(HorizontalAlign.Start);
      };
    }
  }

  @Component
  export struct HelloComponent {
    controller?: HelloComponentController;

    customFunc() {
      console.info('子组件中自定义方法被调用了');
    }

    aboutToAppear(): void {
      // 子组件实例注册到子组件控制器，确保控制器持有子组件实例引用
      this.controller?.bindHelloComponentController(this);
    }

    build() {
      Row() {
        Scroll(this.controller?.scroller) {
          Column() {
            ForEach(new Array(5).fill(''), (_: string, index: number) => {
              Row() {
                Text(index.toString())
                  .fontSize(18);
              }
              .height(200)
              .width('100%')
              .border({ width: 1 })
              .justifyContent(FlexAlign.Center);
            });
          };
        }
        .scrollBar(BarState.Off);
      };
    }
  }
  ```
