---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pop-up-controls-focus
title: 弹窗类控件走焦
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 弹窗类控件走焦
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9c835e0738289b8a54cffd82772eab39469a1794cdc077ca284f817bfabb4363
---

## 设计场景

根据用户交互操作场景，弹窗可分为模态弹窗和非模态弹窗两种类型，其区别在于用户是否必须对其做出响应。

* 模态弹窗为强交互形式，会中断用户当前的操作流程，要求用户必须做出响应才能继续其他操作，通常用于需要向用户传达重要信息的场景。屏幕朗读模式下，模态弹窗弹出时，焦点会自动聚焦到模态弹窗上，在弹窗关闭前无法聚焦到弹窗外节点。
* 非模态弹窗为弱交互形式，不会影响用户当前操作行为，用户可不进行回应，通常都有时间限制，出现一段时间后会自动消失，一般用于向用户传递信息并引导用户执行功能操作的场景。屏幕朗读模式下，非模态弹窗弹出时，焦点默认自动聚焦到非模态弹窗上，弹窗关闭前允许聚焦到弹窗外节点。特别地，如果弹窗是以子窗形式出现，则只能通过不抬手走焦或触摸聚焦的方式聚焦到弹窗外节点，而无法通过抬手走焦的方式聚焦到弹窗外节点。

支持设置模态类型的弹窗控件包括[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Menu](../harmonyos-references/ts-basic-components-menu.md)、[Diaglog](../harmonyos-references/ohos-arkui-advanced-dialog.md)、[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)。

## 开发流程

如下示例实现一个模态弹窗和一个非模态弹窗，可以通过点击不同的按钮打开：

```typescript
@Entry
@Component
export struct Rule_2_1_17 {
  title: string = 'Rule 2.1.17';
  // 模态对话框控制器。
  private modelDialogController: CustomDialogController = this.createDialogController(true);
  // 非模态对话框控制器。
  private nonModelDialogController: CustomDialogController = this.createDialogController(false);

  /**
   * 创建对话框控制器
   * @param isModal 是否为模态对话框
   * @returns 返回创建的对话框控制器
   */
  private createDialogController(isModal: boolean): CustomDialogController {
    return new CustomDialogController({
      builder: CustomDialogExample({
        controller: isModal ? this.modelDialogController : this.nonModelDialogController,
        isModal: isModal,
        cancel: () => {
          if (isModal) {
            this.modelDialogController.close();
          } else {
            this.nonModelDialogController.close();
          }
        }
      }),
      autoCancel: true,
      isModal: isModal,
      onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
        if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
          dismissDialogAction.dismiss();
        }
        if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
          dismissDialogAction.dismiss();
        }
      },
      showInSubWindow: true,
      alignment: DialogAlignment.Center,
      width: 300,
      height: 250,
    })
  }

  build() {
    NavDestination() {
      Scroll() {
        Column() {
          // 模态对话框按钮。
          Button('模态dialog')
            .margin({ bottom: 5 })
            .onClick(() => {
              this.modelDialogController.open();
            })

          // 非模态对话框按钮。
          Button('非模态dialog')
            .onClick(() => {
              this.nonModelDialogController.open();
            })
        }.margin({ bottom: 5 })
      }
    }.title(this.title)
  }
}

@CustomDialog
struct CustomDialogExample {
  // 是否为模态对话框。
  isModal?: boolean;
  // 对话框控制器。
  controller?: CustomDialogController;
  // 关闭对话框的回调函数。
  cancel: () => void = () => {};

  build() {
    Column() {
      // 显示对话框的标题。
      Text(this.isModal ? '模态弹窗' : '非模态弹窗')
        .fontSize(30)
        .height(100)
      Text('测试节点1')
      Text('测试节点2')
      Text('测试节点3')
      // 关闭对话框按钮。
      Button('关闭')
        .onClick(() => {
          this.cancel?.();
        })
        .margin(20)
    }
  }
}
```
