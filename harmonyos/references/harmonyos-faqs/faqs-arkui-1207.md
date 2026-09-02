---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1207
title: 弹窗在跳转新页面后未消失，覆盖在新页面上方
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 弹窗在跳转新页面后未消失，覆盖在新页面上方
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0ac56b17e05eedc3993764bbe388911b0428ca80783104045d484a5f4ea090c0
---

## 问题现象

弹窗在跳转新页面之后没有自动消失，显示在新页面上方，对新页面造成遮挡。

## 背景知识

* [弹窗](../harmonyos-guides/arkts-dialog-overview.md)：根据用户交互操作场景，弹窗可分为模态弹窗和非模态弹窗两种类型，其区别在于用户是否必须对其做出响应。
  + 模态弹窗：为强交互形式，会中断用户当前的操作流程，要求用户必须做出响应才能继续其他操作，通常用于需要向用户传达重要信息的场景。
  + 非模态弹窗：为弱交互形式，不会影响用户当前操作行为，用户可以不对其进行回应，通常都有时间限制，出现一段时间后会自动消失。一般用于告诉用户信息内容外还需要用户进行功能操作的场景。
* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：给组件绑定半模态页面，点击后显示模态页面。
* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)：自定义弹窗。
* [isModal](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)配置项：用于配置弹窗是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与弹窗周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与弹窗周围其他控件进行交互。默认值：true，此时弹窗有蒙层。

## 问题定位

排查代码中使用的是模态弹窗还是非模态弹窗。如果使用了bindSheet或bindContentCover作为弹窗，则属于模态弹窗。如果使用CustomDialog等Dialog作为弹窗，需要检查弹窗配置中的isModal配置项，如果是false则是非模态弹窗。

* 使用模态弹窗。

  排查代码，是否在跳转页面时配置isShow属性，弹窗组件属于全局顶层窗口，其显示层级高于所有页面，如果不进行手动关闭，会导致弹窗在跳转新页面后未消失，覆盖在新页面上方。

  ```screen
  @Builder
  myBuilder() {
    Scroll() {
      Column() {
        Button("倍速")
          .margin(10)
          .fontSize(20)
          .onClick(() => {
            // 页面跳转
            routerMap_Stack.pushPath({ name: 'routerMap_ViewOne' });
          })
      }
    }
    .width('100%')
    .height('100%')
  }
  build() {
    Navigation(routerMap_Stack) {
      Column() {
        Image($r('app.media.23'))
          .width(120)
          .height(120)
          .margin({ left: -200 })
          .onClick(() => {
            // 显示半模态页面
            this.isShow = true;
          })
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: '30%',
            backgroundColor: Color.Green,
            onWillAppear: () => {
            },
            onAppear: () => {
            },
            onWillDisappear: () => {
            },
            onDisappear: () => {
            }
          })
        Slider({
          value: this.currentProgress,
          min: 0,
          max: this.duration
        })
          .width('90%')
      }
      .justifyContent(FlexAlign.End)
      .width('100%')
      .height('100%')
    }
  ```
* 使用非模态弹窗。

  排查代码，是否在跳转页面时调用close()方法，close()方法可以关闭显示的自定义弹窗，如果没有调用，会导致弹窗在跳转新页面后未消失，覆盖在新页面上方。

  ```screen
  struct CustomDialogExample {
    controller?: CustomDialogController;
    build() {
      Column({ space: 5 }) {
        Text('自定义弹窗')
          .fontSize(30)
          .height(100)
        Button('跳转到其他页面').onClick(() => {
          routerMap_Stack.pushPath({ name: 'routerMap_ViewOne' });
        })
      }
    }
  }
  ```

## 分析结论

* 模态弹窗未在跳转页面时改变弹窗显示状态，而弹窗窗口的显示层级高，导致弹窗在跳转新页面后未消失，覆盖在新页面上方。
* 非模态弹窗在跳转页面前未调用close()方法，导致弹窗在跳转新页面后未消失，覆盖在新页面上方。

## 修改建议

* 模态弹窗定义状态变量isShow控制弹窗显隐。

  ```screen
  @Builder
  myBuilder() {
    Scroll() {
      Column() {
        Button('跳转页面')
          .margin(10)
          .fontSize(20)
          .onClick(() => {
            // 跳转页面前隐藏弹窗
            this.isShow = false;
            // 跳转页面
            this.pageInfo.pushPath({ name: 'PageOne' });
          });
      };
    }
    .width('100%')
    .height('100%');
  }
  ```
* 非模态弹窗在跳转页面前使用close()方法，关闭页面弹窗。

  ```screen
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      confirm: () => {
        // 跳转页面前隐藏弹窗
        this.dialogController?.close();
        // 跳转页面
        this.pageInfo.pushPath({ name: 'PageOne' });
      }
    }),
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      console.info(`reason= ${dismissDialogAction.reason}`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
    cornerRadius: 10,
  });
  ```

完整示例代码如下：

```screen
@CustomDialog
@Component
struct CustomDialogExample {
  controller?: CustomDialogController;
  confirm: () => void = () => {
  };

  build() {
    Column() {
      Button('跳转页面')
        .onClick(() => {
          this.confirm();
        })
        .margin(20);
    }.borderRadius(10);
  }
}

@Entry
@Component
struct CustomDialogUser {
  @State isShow: boolean = false;
  pageInfo: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'PageOne') {
      PageOne();
    }
  }

  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      confirm: () => {
        // 跳转页面前隐藏弹窗
        this.dialogController?.close();
        // 跳转页面
        this.pageInfo.pushPath({ name: 'PageOne' });
      }
    }),
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      console.info(`reason= ${dismissDialogAction.reason}`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
    cornerRadius: 10,
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
  }

  @Builder
  myBuilder() {
    Scroll() {
      Column() {
        Button('跳转页面')
          .margin(10)
          .fontSize(20)
          .onClick(() => {
            // 跳转页面前隐藏弹窗
            this.isShow = false;
            // 跳转页面
            this.pageInfo.pushPath({ name: 'PageOne' });
          });
      };
    }
    .width('100%')
    .height('100%');
  }

  build() {
    Navigation(this.pageInfo) {
      Column({ space: 20 }) {
        Button('bindSheet', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.isShow = true;
          })
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: '30%',
            backgroundColor: Color.Green,
            onWillAppear: () => {
            },
            onAppear: () => {
            },
            onWillDisappear: () => {
            },
            onDisappear: () => {
            }
          });
        Button('CustomDialog', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            if (this.dialogController != null) {
              this.dialogController.open();
            }
          });
      };
    }.title('NavIndex')
    .navDestination(this.PagesMap);
  }
}

@Builder
export function PageOneBuilder() {
  PageOne();
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  message: string = 'Hello World';

  build() {
    NavDestination() {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10);
      }.width('100%').height('100%');
    }.title('PageOne')
    .onBackPressed(() => {
      this.pageInfo.pop({ number: 1 }); // 弹出路由栈栈顶元素。
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    });
  }
}
```
