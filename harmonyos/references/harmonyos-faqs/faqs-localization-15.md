---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-15
title: 显示的农历月份比实际少一个月
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 显示的农历月份比实际少一个月
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:8624e92d4ce847451805011e1c973a37eee76f2c5ab8b9fc18d98c103012da39
---

## 问题现象

显示农历日期，日数是对的，但月份比实际少一个月，如2025年7月9日对应的农历日期应为6月15日，但显示为5月15日。

## 背景知识

* [i18n.getCalendar](../harmonyos-references/js-apis-i18n.md#i18ngetcalendar8)：获取指定区域和历法的日历对象。
  + i18n.getCalendar('zh-Hans', 'chinese')：获取中国农历历法日历对象。
* [Calendar](../harmonyos-references/js-apis-i18n.md#calendar)：日历对象。
  + [setTime](../harmonyos-references/js-apis-i18n.md#settime8)：设置日历对象内部的时间、日期。
  + [get('month')](../harmonyos-references/js-apis-i18n.md#get8)：获取日历对象中月份的值。注意月份从0开始计数，例如0表示一月。

## 问题定位

1. 检查代码中获取的日历对象是否是中国农历历法，即[i18n.getCalendar](../harmonyos-references/js-apis-i18n.md#i18ngetcalendar8)的第二个参数（type）是否为字符串'chinese'。
2. [get('month')](../harmonyos-references/js-apis-i18n.md#get8)获取的月份是从0开始计数，排查代码中是否在获取月份时对数值做了+1处理，错误代码如下所示：

   ```ts
   import { i18n } from '@kit.LocalizationKit';

   // 获取中国农历历法
   let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans', 'chinese');
   // 显示的月份数=calendar.get('month')将导致比实际月份数少1
   let month: number = calendar.get('month');
   ```

## 分析结论

因问题现象为日数正确、月份数比实际月份少1个月，所以可能的问题原因为显示农历月份时，直接显示了[calendar.get('month')](../harmonyos-references/js-apis-i18n.md#get8)获取到的月份数，没有在此基础上+1。

## 修改建议

显示月份时，在[calendar.get('month')](../harmonyos-references/js-apis-i18n.md#get8)获取到的月份数上+1，得到实际的月份。

```ts
import { i18n } from '@kit.LocalizationKit';

// 获取中国农历历法
let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans', 'chinese');
// 显示的月份数=calendar.get('month')+1
let month: number = calendar.get('month') + 1;
```
