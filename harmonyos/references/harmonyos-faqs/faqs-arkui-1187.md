---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1187
title: 父组件如何获取子组件方法执行结果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 父组件如何获取子组件方法执行结果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aa47372e55802d056c292d10e30e39c68253480a6b60685215e3e1377a868f0e
---

## 问题现象

有个子组件选择颜色的弹窗，在子组件选择颜色后，点击弹窗的确认按钮后，如何把已选的颜色传递到父组件进行展示。

## 背景知识

UIContext中getPromptAction获取PromptAction实例提供了openCustomDialog和closeCustomDialog方法，分别用来实现打开和关闭自定义弹窗：

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：打开自定义弹窗，弹窗支持自定义样式，如宽度、高度、背景色、阴影。
* [closeCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closecustomdialog12)：关闭自定义弹窗。

## 解决方案

父组件Index默认颜色白色，点击“打开弹窗”，点击“选择颜色-红色”，通过selectColorFunc方法把SelectColorComponent组件选择的颜色传递到父组件Index中并展示，代码示例如下：

```ts
@Entry
@Component
struct SelectColorPage {
  @State selectColor: string = '白色';

  build() {
    Column() {
      Text(this.selectColor)
        .fontSize(30)
      SelectColorComponent({
        // 父组件接收结果
        selectColorFunc: (res: string) => {
          // 获取子组件结果
          this.selectColor = res;
        }
      })
    }
    .backgroundColor(this.selectColor == '红色' ? Color.Red : Color.White)
    .justifyContent(FlexAlign.SpaceAround)
    .height('100%')
    .width('100%')
  }
}

@Component
export struct SelectColorComponent {
  dialogID: number = -1;
  selectColorRed: string = '';
  // 子组件里声明方法
  selectColorFunc = (res: string) => {
    console.info(`selectColor:${res}`);
  };

  build() {
    Column() {
      Button('打开弹窗').onClick(() => {
        // 打开弹窗
        this.selectColor();
      })
    }
  }

  @Builder
  ColorPicker() {
    Column() {
      Button('选择颜色-红色').onClick(() => {
        this.selectColorRed = '红色';
      })
      Row() {
        Button('确定')
          .onClick(() => {
            // 获取结果传递给父组件
            this.selectColorFunc(this.selectColorRed);
            // 关闭弹窗。
            this.getUIContext().getPromptAction().closeCustomDialog(this.dialogID);
          })
        Button('取消')
          .onClick(() => {
            // 关闭弹窗。
            this.getUIContext().getPromptAction().closeCustomDialog(this.dialogID);
          })
      }
      .padding(8)
    }
  }

  // 定义弹窗打开的方法。
  selectColor() {
    this.getUIContext().getPromptAction().openCustomDialog({
      builder: () => {
        this.ColorPicker();
      }
    }).then((dialogID) => {
      this.dialogID = Number(dialogID);
    });
  };
}
```
