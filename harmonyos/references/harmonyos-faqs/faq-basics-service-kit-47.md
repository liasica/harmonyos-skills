---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-47
title: 如何不受系统设置的时区影响按照固定时区解析时间
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何不受系统设置的时区影响按照固定时区解析时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:016a6ae39907c1d3170718b32102fbeefb188e9e2b4483ee32217e1013b77b83
---

## 问题现象

当系统时区已设置，应用中的时间解析会遵循该系统时区。为了确保相关代码业务逻辑不受系统时区影响，而是按照固定的时区进行解析，应该采取哪些措施？

## 背景知识

* 全球各国家和地区的经度不同，地方时间也有所不同，因此划分了不同的时区。例如英国采用0时区，中国采用东8时区，中国时间要比英国早8个小时，中国北京中午12:00是英国伦敦凌晨4点。
* [@ohos.i18n (国际化-I18n)](../harmonyos-references/js-apis-i18n.md)模块提供系统相关的或者增强的国际化能力，其中提供方法[setTimeZone](../harmonyos-references/js-apis-i18n.md#settimezone8)可用于设置日历对象的时区。

## 解决方案

要确保时间解析不受系统设置影响并固定到指定时区，可以通过国际化能力实现。具体而言，使用[getCalendar](../harmonyos-references/js-apis-i18n.md#i18ngetcalendar8)方法获取日历对象，再通过setTimeZone设置目标时区，即可获得该时区的时间对象。实现方式如下：

```ts
import { i18n } from '@kit.LocalizationKit';

@Entry
@Component
struct Index {
  @State beijingTime: string = '';

  getBeijingTime() {
    // 获取日历对象
    let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans-CN');
    // 设置日历对象的时区
    calendar.setTimeZone('Asia/Shanghai');
    // 获取时间对象中相应的值
    let year: number = calendar.get('year');
    let month: number = calendar.get('month') + 1;
    let day: number = calendar.get('date');
    let hour: number = calendar.get('hour');
    let minute: number = calendar.get('minute');
    let second: number = calendar.get('second');
    this.beijingTime = `${year}/${month}/${day} ${hour}:${minute}:${second}`;
  }

  aboutToAppear(): void {
    this.getBeijingTime();
  }

  build() {
    Column() {
      Text(`系统时间：${new Date().toTimeString()}`)
        .fontSize(20);
      Text(`北京时间：${this.beijingTime}`)
        .fontSize(20)
        .margin({ top: 40 });
    }
    .padding(30);
  }
}
```

示例中将手机时区设置为西六区，与北京时间东八区相差14小时，运行效果如下

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/iWnDrjthRFC1uGxhC-5L0A/zh-cn_image_0000002628613952.png "点击放大")
