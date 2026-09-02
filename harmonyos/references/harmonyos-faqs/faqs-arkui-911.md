---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-911
title: 自定义弹窗从屏幕底部向上弹出的实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义弹窗从屏幕底部向上弹出的实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:2186f4d259dd754df8b9d2e7caff4fae04d79a3967b7a4b23e26c3ae2dc8b849
---

## 问题现象

如何实现弹窗从屏幕底部向上弹出展示的动画？

## 背景知识

* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)是一种可以用来展示广告、中奖信息、警告提示或软件更新通知等与用户互动内容的自定义弹出框。开发人员能够利用CustomDialogController类来控制并展示这些个性化的弹窗。
* 在组件内部实现过渡效果主要是通过设置[transition](../harmonyos-references/ts-transition-animation-component.md)属性来定义过渡的参数。这种做法使得当组件被添加或移除时，能够展示出平滑的动画效果。这通常应用于容器组件中，当其子组件被插入或删除时，以此增强用户的交互体验。

## 解决方案

* 方案一：利用CustomDialogController类和@CustomDialog装饰器创建弹窗，通过为弹窗组件的根容器设置transition属性来实现。
  1. 定义动画时长duration。
  2. 在@CustomDialog构造的弹窗中对根容器使用transition来设置动画时长和y轴上的位移效果。

  示例代码如下：

  ```ts
  // 弹窗交互
  @CustomDialog
  struct CustomDialogExample {
    controller: CustomDialogController = new CustomDialogController({
      builder: CustomDialogExample(),
      autoCancel: true
    });
    @State showFlag: Visibility = Visibility.Visible;

    build() {
      Column() {
        Row() {
          Text('自定义动画的弹窗');
        }
        .justifyContent(FlexAlign.Center)
        .padding(8)
        .backgroundColor('#FFFFFF')
        .height(100)
        .margin({ bottom: 30 })
        .width('80%')
        .borderRadius(32);
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%')
      .onClick(() => {
        this.cancel();
      })
      .visibility(this.showFlag)
      // 定义进场出场转场动画效果
      .transition(TransitionEffect.OPACITY.animation({ duration: 1000 })
        .combine(TransitionEffect.translate({ y: 400 })), (transitionIn: boolean) => {
        if (this.showFlag === Visibility.Hidden && transitionIn === false) {
          this.controller.close();
        }
      });
    }

    cancel() {
      this.showFlag = Visibility.Hidden;
    }
  }

  @Entry
  @Component
  struct CustomDialogUser {
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogExample(),
      customStyle: true
    });

    build() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.dialogController.open();
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* 方案二：使用[UIContext.getPromptAction弹窗](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)，通过[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)的transition参数设置弹窗显示动画效果。参考官网[实现进度展示弹窗](../harmonyos-guides/custom-dialog-select-develop.md#实现进度展示弹窗)示例中【自定义弹窗显示和退出动画】一节，将this.getUIContext().getPromptAction().openCustomDialog方法修改为如下代码：
  1. 定义动画时长duration。
  2. 定义y轴上的位移效果。

     ```ts
     this.getUIContext().getPromptAction().openCustomDialog({
       builder: () => {
         this.customDialogComponent();
       },
       alignment: DialogAlignment.Center,
       maskColor: 'rgba(0, 0, 0, 0.2)',
       transition: TransitionEffect.OPACITY
         .animation({ duration: anmDuration })
         .combine(TransitionEffect.translate({ y: 1000 }))
     })
     ```

完整代码如下：

* Index.ets：

  ```ts
  import { InterceptReturn } from './InterceptReturn';

  @Entry
  @Component
  struct Index {
    @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

    @Builder
    PagesMap(name: string) {
      if (name === 'InterceptReturn01') {
        InterceptReturn();
      }
    }

    build() {
      Navigation(this.pageStack) {
        Column() {
          Column({ space: 12 }) {
            Button('Intercept Return')
              .width('100%')
              .backgroundColor('#0A59F7')
              .onClick(() => {
                this.pageStack.pushPathByName('InterceptReturn01', '');
              });
          }
          .width('100%')
          .justifyContent(FlexAlign.End);
        }
        .width('100%')
        .height('100%')
        .padding({
          left: 16,
          right: 16
        })
        .justifyContent(FlexAlign.End);
      }
      .title('Use of CustomDialog')
      .height('100%')
      .width('100%')
      .navDestination(this.PagesMap);
    }
  }
  ```
* InterceptReturn.ets：

  ```ts
  @Component
  export struct InterceptReturn {
    private customDialogComponentId: number = 0;
    @Consume('NavPathStack') pageStack: NavPathStack;

    @Builder
    customDialogComponent() {
      Column() {
        Row() {
          Text('Title')
            .fontSize(20)
            .fontWeight(FontWeight.Bold);
        }
        .width('100%')
        .height(56)
        .justifyContent(FlexAlign.Center);

        Text('This is a dialog content.')
          .fontSize(14);
        Button('CONFIRM')
          .fontSize(16)
          .fontColor('#0A59F7')
          .backgroundColor(Color.White)
          .onClick(() => {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          })
          .width('100%')
          .margin({
            top: 8,
            bottom: 16
          });
      }
      .padding({
        left: 24,
        right: 24
      })
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
      .backgroundColor(Color.White)
      .borderRadius(32)
      .margin({
        left: 16,
        right: 16
      });
    }

    build() {
      NavDestination() {
        Column() {
          Row() {
            Button('OPEN')
              .fontSize(16)
              .width('100%')
              .borderRadius(20)
              .margin({ bottom: 16 })
              .backgroundColor('#0A59F7')
              .onClick(() => {
                let anmDuration: number = 300;
                this.getUIContext().getPromptAction().openCustomDialog({
                  builder: () => {
                    this.customDialogComponent();
                  },
                  alignment: DialogAlignment.Center,
                  maskColor: 'rgba(0, 0, 0, 0.2)',
                  transition: TransitionEffect.OPACITY
                    .animation({ duration: anmDuration })
                    .combine(TransitionEffect.translate({ y: 1000 }))
                })
                  .then((dialogId: number) => {
                  this.customDialogComponentId = dialogId;
                });
              });
          }
          .width('100%')
          .alignItems(VerticalAlign.Center);
        }
        .width('100%')
        .height('100%')
        .padding({
          left: 16,
          right: 16
        })
        .justifyContent(FlexAlign.End);
      };
    }
  }
  ```

| 为弹窗组件的根容器设置transition属性来实现 | 为promptAction.openCustomDialog()设置transition属性实现 |
| --- | --- |
|  |  |
| 由于transition是设置为弹窗组件的根容器，所以实现的动画效果不涉及蒙版，只实现了弹窗本身的动画效果 | 在promptAction.openCustomDialog()中设置的动画效果针对的是整个弹窗，所以蒙版会跟随弹窗一起实现动画效果 |

## 常见FAQ

Q：是否支持弹出和消失时使用不同的动画？例如从底部向上弹出，从顶部向上消失。

A：[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)的asymmetric接口支持指定非对称的转场效果，第一个参数指定出现的转场效果，第二个参数指定消失的转场效果。

如果需要从底部向上弹出，从顶部向上消失，可以设置transition属性为：

```ts
.transition(TransitionEffect.asymmetric(
  TransitionEffect.move(TransitionEdge.BOTTOM).animation({ duration: 300 }),
  TransitionEffect.move(TransitionEdge.TOP).animation({ duration: 300 })
))
```

BaseDialogOptions的transition参数同理。
