---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-169
title: 如何自定义日期时间格式
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何自定义日期时间格式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4b2782fc15209e175975dd604b994b7524ea1c1592145efebd2692fc9963cbf9
---

## 问题现象

如何实现自定义的日期时间格式？比如xx月xx日周xx下午xx:xx。

## 背景知识

* 时间日期格式化将表示时间日期的Date对象，通过DateTimeFormat类的format()接口实现格式化。

  从API version 20开始，该接口建议使用[Intl.DateTimeFormat.prototype.format()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)替代。
* DateTimeOptions：时间、日期格式化时可设置的配置项。
  + dateStyle和timeStyle需同时设置。设置timeStyle但不设置dateStyle时，只显示时间；设置dateStyle但不设置timeStyle时，只显示日期。
  + 设置dateStyle或timeStyle时，不支持设置年、月、日、时、分、秒、工作日格式；不设置dateStyle和timeStyle时，支持独立设置年、月、日、时、分、秒、工作日格式。

  从API version 20开始，建议使用[Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)替代。

## 解决方案

可以将年月日看作整体设置DateTimeOptions配置项，把时分秒看作整体设置DateTimeOptions配置项。

```screen
import { i18n } from '@kit.LocalizationKit';

@Entry
@Component
struct Index {
  @State dateTime: string = '';
  msg_text: string = '时间';
  msg_button: string = '打开时间选择器';
  selectedDate: Date = new Date();

  build() {
    Column() {
      Text(this.dateTime === '' ? this.msg_text : this.dateTime)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 10 });

      Button(this.msg_button)
        .onClick(() => {
          // 获取系统语言，如果为英文，区域ID为en，否则为zh-CN
          getSystemLanguage();

          let md = getDateTimeFormat(systemLocale, mdOptions);
          let mdw = getDateTimeFormat(systemLocale, mdwOptions);
          let ymdw = getDateTimeFormat(systemLocale, ymdwOptions);
          let hourCycle = getDateTimeFormat(systemLocale, hourCycleOptions);

          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-1-1'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            showTime: true,
            useMilitaryTime: false,
            dateTimeOptions: { hour: 'numeric', minute: '2-digit' },
            onDateAccept: (value: Date) => {
              if (systemLocale === 'en') { // 判断区域ID为en或zh-CN
                //先判断当前是昨天、今天或明天
                if (daysUS.includes(compareDates(value, systemLocale))) {
                  this.dateTime =
                    compareDates(value, systemLocale) + ',' + md.format(value) + ' ' + hourCycle.format(value);
                } else if (isYear(value.getFullYear())) { // 判断当前是否为今年
                  this.dateTime = mdw.format(value) + ' ' + hourCycle.format(value);
                } else {
                  this.dateTime = ymdw.format(value) + ' ' + hourCycle.format(value);
                }
              } else {
                if (days.includes(compareDates(value, systemLocale))) {
                  this.dateTime = md.format(value) + compareDates(value, systemLocale) + ' ' + hourCycle.format(value);
                } else if (isYear(value.getFullYear())) {
                  this.dateTime = mdw.format(value) + ' ' + hourCycle.format(value);
                } else {
                  this.dateTime = ymdw.format(value) + ' ' + hourCycle.format(value);
                }
              }
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            }
          });
        });
    }
    .height('100%')
    .width('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }
}

// 区域ID
let systemLocale: string = '';

let days: Array<string> = ['今天', '昨天', '明天'];
let daysUS: Array<string> = ['Today', 'Tomorrow', 'Yesterday'];

let mdOptions: Intl.DateTimeFormatOptions = { month: 'long', day: 'numeric' };
let mdwOptions: Intl.DateTimeFormatOptions = { month: 'long', day: 'numeric', weekday: 'short' };
let ymdwOptions: Intl.DateTimeFormatOptions = {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  weekday: 'short'
};
let hourCycleOptions: Intl.DateTimeFormatOptions = { hourCycle: 'h12', hour: '2-digit', minute: '2-digit' };

// 获取一个DateTimeFormat对象
function getDateTimeFormat(locale: string, options: Intl.DateTimeFormatOptions): Intl.DateTimeFormat {
  return new Intl.DateTimeFormat(locale, options);
}

// 获取系统语言，如果为英文，区域ID为en，否则为zh-CN
function getSystemLanguage() {
  let systemLanguage: string = i18n.System.getSystemLanguage();
  if (systemLanguage === 'en-Latn-US' || systemLanguage.includes('en')) {
    systemLocale = 'en';
  } else {
    systemLocale = 'zh-CN';
  }
}

// 判断当前是否为今年
function isYear(year: number): boolean {
  if (year === new Date().getFullYear()) {
    return true;
  } else {
    return false;
  }
}

// 判断当前是昨天、今天或明天
function compareDates(selected: Date, systemLocale: string): string {
  const currentDate = new Date(); // 当前时间
  currentDate.setHours(0, 0, 0, 0); // 清零时分秒毫秒

  const selectedDate = new Date(selected); // 选中时间
  selectedDate.setHours(0, 0, 0, 0); // 标准化选中日期

  const timeDiff = selectedDate.getTime() - currentDate.getTime();
  const dayDiff = Math.floor(timeDiff / (1000 * 3600 * 24));
  if (systemLocale === 'en') {
    if (dayDiff === 0) {
      return 'Today';
    } else if (dayDiff === 1) {
      return 'Tomorrow';
    } else if (dayDiff === -1) {
      return 'Yesterday';
    } else {
      return '';
    }
  } else {
    if (dayDiff === 0) {
      return '今天';
    } else if (dayDiff === 1) {
      return '明天';
    } else if (dayDiff === -1) {
      return '昨天';
    } else {
      return '';
    }
  }
}
```

## 常见FAQ

Q：使用[Intl.DateTimeFormat.prototype.format()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)对时间戳进行格式化时，无论入参时间戳为多少，格式化的结果都是当前手机显示的时间。

A：排查入参时间戳的数据类型是否为正确的类型（Date或number），如果传入的是string类型，那格式化出来的时间为当前系统时间。解决方案可以先通过Number("1762114200299")将string类型转换为number类型的入参时间戳，然后再进行格式化。
