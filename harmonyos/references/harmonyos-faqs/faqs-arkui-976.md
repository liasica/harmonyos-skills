---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-976
title: 如何在子组件中关闭父组件弹出的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在子组件中关闭父组件弹出的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dcb18d669cde37f471333074221f680055e21f1127729ac890f0cf9173d9e23d
---

## 问题现象

在父组件中调用自定义弹窗函数弹出的弹窗，如何实现在子组件中也能关闭弹窗？

## 背景知识

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)创建并弹出dialogContent对应的自定义弹窗，使用Promise异步回调。通过该接口弹出的弹窗内容样式完全按照dialogContent中设置的样式显示，即相当于openCustomDialog设置customStyle为true时的显示效果。
* [@Require](../harmonyos-guides/arkts-require.md)是校验@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）是否需要构造传参的一个装饰器。

## 解决方案

CustomDialogController仅在作为@CustomDialog和@Component struct成员变量，且在@Component struct内部定义时赋值才有效。因此不可通过传递DialogController给子组件来关闭弹窗，可通过子组件调用父组件中关闭弹窗方法达到在子组件中关闭父组件弹窗的目的。

示例代码如下：

* 父组件Index.ets：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { PromptAction } from '@kit.ArkUI';
  import { DetailDialog } from './DetailPage';

  @Entry
  @ComponentV2
  struct Index {
    @Local message: string = "hello";
    private ctx: UIContext = this.getUIContext();
    private promptAction: PromptAction = this.ctx.getPromptAction();
    private customDialogComponentId: number = 0;

    @Builder
    customDialogComponent() {
      Column() {
        DetailDialog({
          click: () => {
            console.info('关闭弹窗');
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          }
        });
      }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween);
    }

    build() {
      Row() {
        Column({ space: 10 }) {
          Button('打开弹窗')
            .fontSize(20)
            .onClick(() => {
              this.promptAction.openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                },
              })
                .then((dialogId: number) => {
                  this.customDialogComponentId = dialogId;
                })
                .catch((error: BusinessError) => {
                  console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
                });
            });
        }
        .width('100%')
        .height('100%');
      }
      .height('100%');
    }
  }
  ```
* 子组件DetailPage.ets：

  ```ts
  @ComponentV2
  export struct DetailDialog {
    @Param @Require click: () => void;

    build() {
      Column({ space: 50 }) {
        Blank()
        Text('这是弹窗内容')
          .fontSize(30);
        Row({ space: 50 }) {
          Button("关闭弹窗")
            .onClick(() => {
              // 相关业务逻辑
              // 调用父组件关闭弹窗方法
              this.click();
            });
        };
      };
    }
  }
  ```
