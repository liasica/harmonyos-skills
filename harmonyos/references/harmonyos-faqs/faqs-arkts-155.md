---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-155
title: 页面上展示的日期与实际时间不符
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 页面上展示的日期与实际时间不符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:71b43645492566b7cae0a2c7e4e25b309575db551a77d21a8b2d50edcdd09e1e
---

## 问题现象

应用中展示的当前时间中，月份比当前系统时间的月份小1。例如，当前系统时间为2025年7月25日。应用中展示的当前时间是2025年6月25日。

问题代码为：

```ts
// ...
@State newTime: string = '';

// ...
const nowTime = new Date();
nowTime.toDateString();
const nowYear = nowTime.getFullYear();
const nowMonth = nowTime.getMonth();
const nowDate = nowTime.getDate();
this.newTime = ((((nowYear + "年") + nowMonth) + "月") + nowDate) + "日";
// ...
```

## 背景知识

* Date.getMonth()，其获取的月份从0开始。因此，在月份数据处理上需要做加1处理。
* [时区](../harmonyos-guides/i18n-time-zone.md)：全球各国家和地区的经度不同，地方时间也有所不同，因此划分了不同的时区。例如，英国采用0时区，中国采用东8时区，中国时间要比英国快8小时，中国北京中午12:00，对应英国伦敦是凌晨4:00。时区模块可用于获取时区列表，应用可基于该列表实现业务逻辑，如双时钟应用。

## 问题定位

检查代码，可以发现对于日期的处理采用了拼接的方式，且月份直接通过getMonth()获取。

## 分析结论

Date.getMonth()，其获取的月份从0开始，没有做加1处理，导致实际展示的月份比实际月份小1。

## 修改建议

* 自拼接处理需要在月份上做加1处理。
* 推荐使用时间日期国际化，对时间日期格式化处理。同时，还可以根据不同的国家，进行针对性的格式化处理满足国际化的需求。

示例代码如下：

```ts
@Entry
@Component
struct ThisTime {
  @State newTime: string = '拼接处理的时间：';
  @State formatDate: string = '格式化处理的时间：';

  build() {
    Column({ space: 20 }) {
      Column() {
        Button('自拼接处理').onClick(() => {
          const nowTime = new Date();
          nowTime.toDateString();
          const nowYear = nowTime.getFullYear();
          const nowMonth = nowTime.getMonth() + 1;
          const nowDate = nowTime.getDate();
          this.newTime = ((((nowYear + '年') + nowMonth) + '月') + nowDate) + '日';
        });

        Button('推荐使用时间日期国际化').onClick(() => {
          const date = new Date();
          // 创建DateTimeFormat对象
          let fullFormat: Intl.DateTimeFormat =
            new Intl.DateTimeFormat('zh-CN', { dateStyle: 'full', timeStyle: 'full' });
          let formattedDate: string = fullFormat.format(date);
          this.newTime =
            '拼接处理的时间（月份需要+1）：' + date.getFullYear() + '年' + (date.getMonth() + 1) + '月' + date.getDate() +
              '日';
          this.formatDate = '格式化处理的时间：' + formattedDate;
        });
        Text(this.newTime);
        Text(this.formatDate);
      };
    }.width('100%').alignItems(HorizontalAlign.Center);
  }
}
```
