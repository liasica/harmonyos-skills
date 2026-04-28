---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-time-date
title: 时间日期国际化
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 时间日期国际化
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5c3e69a372e5f94eb93c22aa317df9a93377c2c5d945078ee311d7a1a5888570
---

## 使用场景

在不同国家和文化中，时间和日期的表示方法存在差异，主要体现在年月日的顺序以及时分秒的分隔符。若应用中需展示时间日期，要确保界面以合适的方式显示，以便用户能够理解。

时间日期国际化包括时间日期格式化、相对时间格式化和时间段格式化。时间日期格式化是指将时间和日期转换为指定格式的字符串。相对时间格式化是指将一个时间点与另一个时间点之间的时间差转换为指定格式，例如“30秒前”、“1天后”。时间段格式化是指将一段时间转换为指定格式，例如“星期三”、“8:00 - 11:30”。

## 开发步骤

### 时间日期格式化

时间日期格式化请参考[Intl.DateTimeFormat](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)接口。

### 相对时间格式化

相对时间格式化请参考[format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)接口。

### 时间段格式化

时间段格式化请参考[formatRange](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange)接口。
