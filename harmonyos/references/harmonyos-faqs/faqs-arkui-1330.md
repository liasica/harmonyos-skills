---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1330
title: 如何实现嵌套的抽屉效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现嵌套的抽屉效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c66156ddd7a18b00a60c5549925d53445c33221e7ce91b2e460126c76afb0b5
---

## 问题现象

如何实现组件从底部上滑弹出，类似于嵌套抽屉的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/EXYyFsZdQsyCZPRpsMvXRw/zh-cn_image_0000002658959113.gif "点击放大")

## 背景知识

* [属性动画 (animation)](../harmonyos-references/ts-animatorproperty.md)能够在组件的某些通用属性变化时，实现渐变过渡效果，提升用户体验。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)能够控制组件的显示或隐藏，实现不同的显隐控制效果。
* [zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)能够设置组件的堆叠顺序，在同一容器中显示兄弟组件的层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

## 解决方案

zIndex属性能够设置组件的堆叠顺序，因此可以通过设置zIndex属性实现抽屉层级效果，而visibility属性能够控制组件的显示与隐藏，因此可以通过设定状态变量，通过状态变量控制visibility属性从而控制组件的显隐，配合animation添加过渡动画，即可实现抽屉的弹出效果，具体实现如下：

1. 定义CustomAlertFirst组件，使用[@Consume装饰器](../harmonyos-guides/arkts-provide-and-consume.md)从父组件中获取两个值：panelHeightSecond和level，在build中的Button按钮上绑定点击事件处理函数：如果panelHeightSecond的值为0，隐藏当前面板，点击按钮后将panelHeightSecond设置为20%，显示当前面板。
2. 定义CustomAlertSecond组件，使用@Consume装饰器绑定两个状态变量：panelHeightSecond和level。在build方法中的Button按钮组件，为按钮添加onClick事件处理函数：当按钮被点击时，会根据当前的panelHeightSecond值来决定是显示还是隐藏CustomAlertSecond组件。
3. 在父组件Index中，定义了状态变量panelHeight、panelHeightSecond和level，用于控制警告组件的高度和层级。调用组件CustomAlert和CustomAlertSecond，都包含一个按钮，点击按钮可以控制组件的高度和层级，从而控制组件的显示和隐藏。

完整代码如下：

```ts
@Entry
@Component
struct DrawerDemo {
  @Provide('panelHeightFirst') panelHeightFirst: string = '0'; // 控制第一层抽屉高度。
  @Provide('panelHeightSecond') panelHeightSecond: string = '0';  // 控制第二层抽屉高度。
  @Provide('level') level: number = 0; // 控制遮罩层级显示。

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Column() {
        Button('弹起')
          .margin({ top: 8 })
          .onClick(() => {
            // 判断当前是否已弹出，切换状态。
            if (this.panelHeightFirst === '0') {
              this.panelHeightFirst = '40%';
              this.level = 2;
            } else {
              this.panelHeightFirst = '0';
              this.level = 0;
            }
          });
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#F1F3F5')
      .zIndex(1)
      .justifyContent(FlexAlign.Center);

      Column() {
      }
      .height('100%')
      .width('100%')
      .backgroundColor(Color.Black)
      .opacity(0.10)
      .zIndex(this.level)
      .onClick(() => {
        // 点击遮罩时关闭所有抽屉。
        this.panelHeightFirst = '0';
        this.panelHeightSecond = '0';
        this.level = 0;
      });

      CustomAlertFirst()
        .height(this.panelHeightFirst)
        .visibility(this.panelHeightFirst === '0' ? Visibility.Hidden : Visibility.Visible)
        .animation({ duration: 300 })
        .zIndex(2);

      CustomAlertSecond()
        .height(this.panelHeightSecond)
        .visibility(this.panelHeightSecond === '0' ? Visibility.Hidden : Visibility.Visible)
        .animation({ duration: 300 })
        .zIndex(3);
    };
  }
}

// 第一层抽屉组件。
@Component
struct CustomAlertFirst {
  @Consume('panelHeightSecond') panelHeightSecond: string;
  @Consume('level') level: number;

  build() {
    Column() {
      Button('再弹/消失')
        .margin({ top: 8 })
        .onClick(() => {
          if (this.panelHeightSecond === '0') {
            this.panelHeightSecond = '20%';
            this.level = 2;
          } else {
            this.panelHeightSecond = '0';
            this.level = 2;
          }
        });
    }
    .width('100%')
    .height('100%')
    .borderRadius({ topLeft: 15, topRight: 15 })
    .backgroundColor('#F1F3F5');
  }
}

// 第二层抽屉组件。
@Component
struct CustomAlertSecond {
  @Consume('panelHeightSecond') panelHeightSecond: string;
  @Consume('level') level: number;

  build() {
    Column() {
      Button('OK')
        .margin({ top: 8 })
        .onClick(() => {
          this.panelHeightSecond = '0';
          this.level = 2;
        });
    }
    .width('100%')
    .height('100%')
    .borderRadius({ topLeft: 15, topRight: 15 })
    .backgroundColor('#ffffffff');
  }
}
```
