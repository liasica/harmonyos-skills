---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1227
title: 实现自定义时间滑动选择器弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现自定义时间滑动选择器弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7205b887e911f3a285ec86b34eca48ca3e894065efc095ce94613ee243e88bba
---

## 问题现象

开发场景中需要实现日期选择功能，在界面上提供一个按钮或图标，点击后弹出一个日期选择器，显示当前日期，并允许用户从当前日期开始选择。

## 背景知识

* [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)是时间选择组件，用于根据指定参数创建选择器，支持选择小时及分钟。
* [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)是日期选择器组件，用于根据指定日期范围创建日期滑动选择器。

## 解决方案

通过TextPicker主界面触发弹窗，可以利用独立的TextPicker1自定义对话框组件承载日期选择功能。在此过程中，应借助CustomDialogController和回调函数建立起有效的通信链路，确保用户在对话框中选定的日期能够实时反馈并更新至主界面上显示。

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';

let anmDuration: number = 200;

@Entry
@Component
struct TextPickerExample1 {
  @State firstDate: string = '2024-06-19';
  @State date: string = '2024年06月19日';
  controller: CustomDialogController = new CustomDialogController({
    builder: TextPicker1({
      cancel: (date: string) => {
        this.onCancel(date);
      },
      confirm: (date: string, date1: Date) => {
        this.onAccept(date, date1);
      },
      date: this.firstDate,
    }),
    autoCancel: false,
    cornerRadius: 0,
    customStyle: true,
    alignment: DialogAlignment.BottomEnd
  });

  onCancel(date: string) {
    hilog.info(0x0000, 'tag', `date: ${date}`);
  }

  onAccept(date: string, date1: Date) {
    hilog.info(0x0000, 'tag', `date: ${date}`);
    let year: string = date1.getFullYear().toString();
    let month: string =
      (date1.getMonth() + 1) < 10 ? ('0' + (date1.getMonth() + 1)).toString() : (date1.getMonth() + 1).toString();
    let day: string = date1.getDate().toString();
    this.date = year + '年' + month + '月' + day + '日';
    this.firstDate = year + '-' + month + '-' + day;
  }

  build() {
    Column() {
      Text(this.date);
      Text('日期').onClick(() => {
        this.controller.open();
      });
    };
  }
}

@CustomDialog
struct TextPicker1 {
  aboutToAppear(): void {
    this.selectedDate = new Date(this.date);
  }

  @State date: string = '2026-08-08';
  controller: CustomDialogController;
  // 起始年份
  @State showFlag: Visibility = Visibility.Visible;
  @State selectedDate: Date = new Date(this.date);
  cancel?: (date: string) => void;
  confirm?: (date: string, date1: Date) => void;
  // 延迟关闭弹窗，让自定义的出场动画显示

  @State nowDate: Date = new Date();

  destroy() {
    this.showFlag = Visibility.Hidden;
    setTimeout(() => {
      this.controller.close();
    }, anmDuration);
  }

  build() {
    Column() {
      Column() {
        Row() {
          Button('取消', { type: ButtonType.Normal }).backgroundColor(Color.White).fontColor(Color.Gray)
            .onClick(() => {
              if (this.cancel) {
                this.destroy();
                this.cancel(this.date);
              }
            });
          Button('确定', { type: ButtonType.Normal }).backgroundColor(Color.White).fontColor('#fff5b6dd')
            .onClick(() => {
              if (this.confirm) {
                this.destroy();
                this.date = this.nowDate.toString();
                this.confirm(this.date, this.nowDate);
              }
            });
        }.width('100%').justifyContent(FlexAlign.SpaceBetween);

        DatePicker({
          start: new Date('1970-1-1'),
          end: new Date('2100-1-1'),
          selected: this.selectedDate
        })
          .disappearTextStyle({ color: Color.Gray, font: { size: '16fp', weight: FontWeight.Bold } })
          .textStyle({ color: '#ff182431', font: { size: '16', weight: FontWeight.Normal } })
          .selectedTextStyle({ color: '#fff5b6dd', font: { size: '22fp', weight: FontWeight.Regular } })
          .onDateChange((value: Date) => {
            this.nowDate = value;
            console.info(`select current date is:${value}`);
          });
      };
    }.width('100%').backgroundColor(Color.White).visibility(this.showFlag)
    // 定义进场出场转场动画效果
    .transition(TransitionEffect.OPACITY.animation({ duration: anmDuration })
      .combine(TransitionEffect.translate({ y: 100 })));
  }
}
```

## 常见FAQ

Q：如何实现日期与时间的同步选择？

A：日期与时间同步选择请参考：[弹出日期选择弹窗](../harmonyos-references/ts-methods-datepicker-dialog.md#示例1设置显示时间)。

Q：时间选择器不支持选择到秒吗？

A：在使用时间选择器时，若需精确到秒，则可以通过将配置项containSecond设置为true来实现；反之，若不需要显示秒，则将其设置为false。具体操作请参照相关文档：[时间选择器](../harmonyos-references/js-components-basic-picker-view.md#时间选择器)。
