---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-490
title: 自定义键盘如何设置可与输入框贴边
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义键盘如何设置可与输入框贴边
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c9cbd96f977b7968eb8aeba46f3ea4b89b1ebb1b4a5a66ce5461f0cbe8342f8e
---

自定义键盘可以通过自定义弹窗来实现，自定义弹窗默认位置会和底部保持距离。

1、可以通过设置offset来实现贴边。

```screen
@Entry
@Component
struct CustomDialogPage {
  @State message: string = 'CustomDialogPage';
  customDialogController: CustomDialogController = new CustomDialogController({
    builder: CustomEditDialogWidget({
      inputType: InputType.Normal,
      textInputConString: () => {
      }
    }),
    alignment: DialogAlignment.Bottom,
    maskColor: Color.White,
    customStyle: true
  });

  build() {
    Row() {
      Column() {
        Button(this.message).onClick(() => {
          this.customDialogController.open();
        });
      }
      .width('100%');
    }
    .height('100%');
  }
}

@CustomDialog
@Component
export struct CustomEditDialogWidget {
  controller?: CustomDialogController;
  @State textInputString: string = '';
  textInputConString = () => {
  };
  inputType: InputType = InputType.Normal;

  build() {
    Column() {
      TextArea({ placeholder: 'please input' })
        .width('80%')
        .backgroundColor(Color.Transparent)
        .defaultFocus(true)
        .onChange((value: string) => {
          this.textInputString = value;
        });
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Start)
    .width('80%')
    .height(450)
    .borderRadius(10)
    .backgroundColor('#fffaf7f7')
    .offset({ x: 0, y: 16 });
  }
}
```

2、还可以通过设置keyboardAvoidDistance来实现和键盘贴边，示例参见：[设置弹出框避让软键盘的距离](../harmonyos-guides/arkts-common-components-custom-dialog.md#设置弹出框避让软键盘的距离)。
