---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-988
title: 如何使自定义弹窗的侧滑事件作用到页面组件上
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使自定义弹窗的侧滑事件作用到页面组件上
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:085499f5794b649684f065cebe4283329a5e25ae4564e51441191068d90c766f
---

## 问题现象

页面同时存在弹窗和自定义组件（比如Column()），希望弹窗打开的情况下，第一次侧滑关闭页面的自定义组件，第二次侧滑退出页面，如何实现？

## 背景知识

* [即时反馈（Toast）](../harmonyos-guides/arkts-create-toast.md)是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。它通常在屏幕的底部或顶部短暂弹出，随后在一段时间后自动消失。即时反馈的主要目的是提供简洁、不打扰的信息反馈，避免干扰用户当前的操作流程。
* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)创建并弹出自定义弹窗。使用Promise异步回调返回对话框的id，可供closeCustomDialog使用。
* [emitter](../harmonyos-references/js-apis-emitter.md)提供了在同一进程不同线程间或同一线程内发送和处理事件的能力，支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。

## 解决方案

实现弹窗不消费侧滑事件，而是作用到页面组件上，有两种实现方式：

**方式一**：使用Toast创建即时反馈弹窗，该弹窗提供简洁、不打扰的信息反馈，不会干扰用户当前的操作流程，侧滑事件默认作用到页面组件上。示例参考[创建即时反馈](../harmonyos-guides/arkts-create-toast.md#创建即时反馈)。

**方式二**：创建自定义弹窗，通过在onWillDismiss回调里拦截侧滑操作，使用emitter向页面自定义组件通知侧滑事件来操作组件关闭。示例代码如下：

* Toast.ets：封装全局自定义弹窗，在onWillDismiss回调里拦截侧滑操作，使用emitter向页面自定义组件通知侧滑事件。

  ```ts
  import { ComponentContent, promptAction } from '@kit.ArkUI';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { emitter, BusinessError } from '@kit.BasicServicesKit';

  @Builder
  function Toast() {
    Row() {
      Text('这是一个Toast弹窗');
    }
    .padding(10)
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#6b4c4c4b')
    .borderRadius('50%');
  }

  export class PromptActionClass {
    static ctx: UIContext;
    static contentNode: ComponentContent<Object>;
    static options: promptAction.BaseDialogOptions;

    static setContext(context: UIContext) {
      PromptActionClass.ctx = context;
    }

    static setContentNode(node: ComponentContent<Object>) {
      PromptActionClass.contentNode = node;
    }

    static setOptions(options: promptAction.BaseDialogOptions) {
      PromptActionClass.options = options;
    }

    static openDialog() {
      if (PromptActionClass.contentNode !== null) {
        PromptActionClass.ctx.getPromptAction()
          .openCustomDialog(PromptActionClass.contentNode, PromptActionClass.options)
          .then(() => {
            hilog.info(0xFF00, 'TAG', 'OpenCustomDialog complete');
          })
          .catch((error: BusinessError) => {
            hilog.info(0xFF00, 'TAG', `OpenCustomDialog args error code is ${error.code}, message is ${error.message}`);
          });
      }
    }

    static closeDialog(contentNode: ComponentContent<Object>) {
      if (PromptActionClass.contentNode !== null) {
        PromptActionClass.ctx.getPromptAction()
          .closeCustomDialog(contentNode)
          .then(() => {
            hilog.info(0xFF00, 'TAG', 'CloseCustomDialog complete');
          })
          .catch((error: BusinessError) => {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            hilog.info(0xFF00, 'TAG', `CloseCustomDialog args error code is ${code}, message is ${message}`);
          });
      }
    }

    static updateDialog(options: promptAction.BaseDialogOptions) {
      if (PromptActionClass.contentNode !== null) {
        PromptActionClass.ctx.getPromptAction()
          .updateCustomDialog(PromptActionClass.contentNode, options)
          .then(() => {
            hilog.info(0xFF00, 'TAG', 'UpdateCustomDialog complete');
          })
          .catch((error: BusinessError) => {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            hilog.info(0xFF00, 'TAG', `UpdateCustomDialog args error code is ${code}, message is ${message}`);
          });
      }
    }
  }

  export function showToast(ctx: UIContext) {
    if (PromptActionClass.contentNode) {
      PromptActionClass.closeDialog(PromptActionClass.contentNode);
    }
    PromptActionClass.setContext(ctx);
    let toastNode = new ComponentContent(ctx, wrapBuilder(Toast));
    PromptActionClass.setContentNode(toastNode);
    PromptActionClass.setOptions({
      isModal: false,
      focusable: false,
      autoCancel: false,
      onWillDismiss: (data) => {
        if (data.reason == DismissReason.PRESS_BACK) {
          // 拦截侧滑，进行侧滑事件通知
          let eventData: emitter.EventData = {
            data: {
              'content': 'content',
              'id': 1,
            }
          };
          emitter.emit('eventId', eventData);
          return false;
        }
        return true;
      }
    });
    PromptActionClass.openDialog();
  }

  export function closeToast() {
    if (PromptActionClass.contentNode) {
      PromptActionClass.closeDialog(PromptActionClass.contentNode);
    }
  }
  ```
* Index.ets：主页面，进行页面跳转。

  ```ts
  @Entry
  @Component
  struct Index {
    private message: string = '跳转到下一页';

    build() {
      Column({ space: 10 }) {
        Text('Page1')
          .fontColor(Color.White)
          .fontSize(50)
          .fontWeight(500);
        Button(this.message)
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/Page2' });
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* Page2.ets：在此页面创建自定义组件，并打开弹窗，进行侧滑事件接收并处理自定义组件关闭及跳转上一页。

  ```ts
  import { closeToast, showToast } from './Toast';
  import { emitter } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  @Entry
  @Component
  struct Page2 {
    // 自定义组件显隐控制变量
    @State isShow: boolean = false;
    // 自定义弹窗显隐控制变量
    @State isShowToast: boolean = false;
    // 事件通知回调
    callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
      hilog.info(0xFF00, 'TAG', JSON.stringify(eventData));

      if (this.isShow) {
        this.isShow = false;
        return true;
      } else {
        if (this.isShowToast) {
          closeToast();
          this.isShowToast = false;
          this.getUIContext().getRouter().back();
        }
        return false;
      }
    };

    // 收到eventId为1的事件后执行回调函数
    aboutToAppear(): void {
      emitter.on(`eventId`, this.callback);
    }

    build() {
      Column({ space: 10 }) {
        Text('Page2')
          .onClick(() => {
            let eventData: emitter.EventData = {
              data: {
                'content': 'content',
                'id': 1,
              }
            };

            emitter.emit('eventId', eventData);
          })
          .fontColor(Color.Pink)
          .fontSize(50)
          .fontWeight(500);
        Button('打开Page2的自定义组件')
          .onClick(() => {
            this.isShow = true;
          });
        Button('打开弹窗')
          .onClick(() => {
            if (this.isShowToast) {
              closeToast();
            } else {
              showToast(this.getUIContext());
            }
            this.isShowToast = !this.isShowToast;
          });

        if (this.isShow) {
          Column() {
            Text('我是Page2的自定义组件')
              .fontColor(Color.Black)
              .fontSize(30)
              .fontWeight(500);
            Text('现象：\n' +
              '弹窗存在情况下，点击第一次返回键会关闭自定义组件，第二次返回键会返回上一个页面\n')
              .fontColor(Color.Black);
          }
          .width('100%')
          .height(300)
          .justifyContent(FlexAlign.Center)
          .alignItems(HorizontalAlign.Center)
          .backgroundColor(Color.White);
        }

      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink);
    }
  }
  ```
