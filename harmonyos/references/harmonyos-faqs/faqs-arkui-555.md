---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-555
title: CustomDialog动态设置宽高
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > CustomDialog动态设置宽高
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e01d755b9cd3fd6def6025a4f4cf95e424f0236435b1e2c154b3138ca952db11
---

## 问题现象

如何动态修改弹出框的样式，如宽、高等？

## 背景知识

* 自定义弹窗[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)通过CustomDialogController类显示自定义弹窗，弹窗在初始化时通过入参CustomDialogControllerOptions配置参数。自定义弹窗的所有参数，不支持动态刷新，如CustomDialogControllerOptions可设置弹窗的宽高等参数，但设置之后不可改变。
* [ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)实现组件内容的实体封装，其对象支持在非UI组件中创建与传递，便于开发者对弹窗类组件进行解耦封装。
* [update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)：用于更新WrappedBuilder对象封装的builder函数参数，与constructor传入的参数类型保持一致。
* [PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)：创建并显示文本提示框、对话框和操作菜单，和当前UI上下文相关联。
* [updateCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatecustomdialog12)：更新已弹出的dialogContent对应的自定义弹窗的样式，使用Promise异步回调。

## 解决方案

* **方案一**：一个CustomDialogController类对应一个CustomDialog弹窗，由于CustomDialogController内部参数不支持动态刷新，可通过创建新的CustomDialogController实例实现动态修改弹窗样式的效果。

  ```ts
  @CustomDialog
  struct CustomDialogExample {
    controller?: CustomDialogController;

    build() {
      Column({ space: 24 }) {
        Text('这是自定义弹窗')
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .fontSize(16);
        Button('Close')
          .onClick(() => {
            if (this.controller !== undefined) {
              this.controller.close();
            }
          });
      }.padding(24);
    }
  }

  @Entry
  @Component
  struct CustomDialogUser {
    dialogController: CustomDialogController | null = null;

    aboutToAppear(): void {
      this.createDialogCtl(300); // 创建CustomDialogController对象，宽度300
    }

    aboutToDisappear() {
      this.dialogController = null; // 将dialogController置空
    }

    // 创建宽度不同的新弹窗
    createDialogCtl(width: number): void {
      this.dialogController = new CustomDialogController({
        builder: CustomDialogExample(),
        autoCancel: true,
        alignment: DialogAlignment.Center,
        offset: { dx: 0, dy: -20 },
        customStyle: false,
        cornerRadius: 20,
        width: width,
        backgroundColor: Color.White,
      });
    }

    build() {
      Column({ space: 24 }) {
        Button('click me')
          .onClick(() => {
            if (this.dialogController != null) {
              this.dialogController.open();
            }
          });
        Button('change')
          .onClick(() => {
            this.createDialogCtl(150); // 创建新的CustomDialogController对象，宽度150
          });
      }.width('100%').margin({ top: 16 });
    }
  }
  ```

  + 使用限制：实际是创建了新弹窗，所以修改样式后需要先关闭弹窗再重新打开弹窗才有效。
  + 样式修改的范围：[CustomDialogControllerOptions对象](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)支持的参数均可修改，如width、maskColor、offset等。
  + 效果如下：点击change按钮后，创建了一个新的弹窗，改变了原弹窗的宽度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/YssehmbETMG1842IJsRxAw/zh-cn_image_0000002628551602.gif "点击放大")
* **方案二**：使用ComponentContent封装弹窗的UI，使用PromptAction控制弹窗的显隐，使用ComponentContent的update方法更新弹窗，实现动态修改弹窗样式的效果。

  ```screen
  import { ComponentContent } from '@kit.ArkUI';

  interface ParamsInterface {
    text: string;
  }

  @Builder
  function buildText(params: ParamsInterface) {
    Column() {
      Text(params.text)
        .fontSize(24);
    }.padding(24)
    .borderRadius(16)
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.White);
  }

  @Entry
  @Component
  struct ComponentContentDemo {
    build() {
      Column() {
        Button('click me')
          .onClick(() => {
            let uiContext = this.getUIContext();
            let promptAction = uiContext.getPromptAction();
            // 自定义弹窗的内容
            let contentNode = new ComponentContent<ParamsInterface>(uiContext, wrapBuilder<[ParamsInterface]>(buildText),
              { text: 'old style' });
            promptAction.openCustomDialog(contentNode);
            setTimeout(() => {
              contentNode.update({ text: 'new style' });
            }, 2000); // 2秒后自动更新弹窗内容文本
          });
      }.width('100%').height('100%').margin({ top: 16 });
    }
  }
  ```

  + 可以在弹窗展示的过程中动态修改样式，只要update方法支持传递的参数均可用于动态修改样式。
  + 效果如下：在弹窗显示的过程中，更新弹窗的文字。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/D-RpiaMpSLOs8qW5wltXXQ/zh-cn_image_0000002628391704.gif "点击放大")
* **方案三**：和方案二一样使用PromptAction显示弹窗，使用updateCustomDialog更新弹窗样式，但目前仅支持更新alignment、offset、autoCancel、maskColor四种属性。使用方法可参考[updateCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatecustomdialog12)下方的代码示例。

## 常见FAQ

Q：CustomDialog的offset能不能响应式更新？

A：自定义弹窗(CustomDialog)的所有参数，不支持动态刷新。推荐使用[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)。

Q：如何让dialog在隐藏的情况下，再展示时，数据不消失？

A：可以将弹窗数据同步保存至父组件中，可以参考[使用@Link和@Consume监听数据变化](../harmonyos-references/ts-methods-custom-dialog-box.md#示例6使用link和consume监听数据变化)。

Q：如何设置弹窗的位置，使其弹出到屏幕上层？

A：可以修改CustomDialogControllerOptions对象的offset参数，实现改变弹窗的位置。
