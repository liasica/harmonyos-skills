---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1226
title: TimePickerDialog组件如何隐藏顶部的标题日期
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TimePickerDialog组件如何隐藏顶部的标题日期
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4f507a912d6b3d0c4c6ab4d18802051523a6951e60799e11ec1c6e5b9834fdc4
---

## 问题现象

TimePickerDialog组件标题的日期如何才能隐藏？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/5LEizWLuT2uJusBqFmkRUA/zh-cn_image_0000002658953237.gif "点击放大")

## 背景知识

* 开发者可根据24小时的时间区间，创建时间滑动选择器弹窗[TimePickerDialog](../harmonyos-guides/arkts-fixes-style-dialog.md#时间滑动选择器弹窗-timepickerdialog)，将时间信息清晰地展示在弹出的窗口上。组件顶部标题默认是当日日期，可以通过selected属性来更改日期。
* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)通过CustomDialogController类显示自定义弹窗。
* [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)为时间选择组件，可以根据指定参数创建选择器，支持选择小时及分钟。TimePicker除支持[通用属性](../harmonyos-references/ts-component-general-attributes.md)外，还支持设置[useMilitaryTime](../harmonyos-references/ts-basic-components-timepicker.md#usemilitarytime)、[disappearTextStyle](../harmonyos-references/ts-basic-components-timepicker.md#disappeartextstyle10)、[textStyle](../harmonyos-references/ts-basic-components-timepicker.md#textstyle10)等属性。

## 解决方案

TimePickerDialog属于固定样式弹出框，采用固定的布局格式，暂不支持直接隐藏标题的日期，可在自定义弹窗CustomDialog中加入TimePicker来实现。

```ts
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      TimePicker({})
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            console.info('select current date is: ', JSON.stringify(value));
          }
        })
        .disappearTextStyle({ color: Color.Black, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 20, weight: FontWeight.Bolder } });
    };

  }
}

@Entry
@Component
struct TestPage {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      }
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      console.info('reason:', JSON.stringify(dismissDialogAction.reason));
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    customStyle: false,
    cornerRadius: 20,
    width: 300,
    height: 200,
    backgroundColor: Color.White,
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    RelativeContainer() {
      Button('click me')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff);
    }.width('100%').margin({ top: 5 });
  }
}
```

## 常见FAQ

Q：TimePickerDialog时间滑动选择器弹窗如何显示24小时制？

A：TimePickerDialog默认为12小时制，可通过将useMilitaryTime属性设置为true，将展示时间显示为24小时制。
