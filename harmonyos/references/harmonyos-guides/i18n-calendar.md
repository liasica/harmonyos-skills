---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-calendar
title: 设置日历和历法
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 设置日历和历法
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ba44de80295c149fac61231684b29f90296dfeea1050b1b650c3bc8be58d553
---

## 功能介绍

不同地区的用户使用不同的历法，大多数地区使用公历，也有些地区的用户使用其他历法，例如农历、伊斯兰历或希伯来历。日历上的时间和日期根据历法计算得到，并会随时区和夏令时的变化而调整。因此，用户需要设置符合本地习惯的历法。国际化提供了[Calendar](../harmonyos-references/js-apis-i18n.md#calendar8)类，可以设置历法、日期、时区、一周的起始日期和一年中第一周的最小天数。此外，还可以判断具体某一天在日历中是否为周末以及计算相差天数。在应用开发过程中，可以根据业务需求选择使用不同功能。

## 开发步骤

以查看公历日期对应的农历日期为例，说明如何使用[Calendar](../harmonyos-references/js-apis-i18n.md#calendar8)类接口。

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   ```

   [CalendarSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CalendarSetting.ets#L19-L21)
2. 使用场景。

* 公历相关用法。

  ```
  1. let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans', 'gregory');
  2. // 设置日历对象的时间日期为2022.06.13 08:00:00
  3. calendar.setTime(new Date(2022, 5, 13, 8, 0, 0));
  4. calendar.setTime(10540800000);

  6. // 设置日历对象的时间日期为2022.06.13 08:00:00
  7. calendar.set(2022, 5, 13, 8, 0, 0);

  9. // 设置日历对象的时区
  10. calendar.setTimeZone('Asia/Shanghai');

  12. // 获取日历对象的时区
  13. let timezone = calendar.getTimeZone(); // timezone = 'Asia/Shanghai'

  15. // 获取日历对象的一周起始日
  16. let firstDayOfWeek = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 1

  18. // 设置每一周的起始日
  19. calendar.setFirstDayOfWeek(1);

  21. // 获取一年中第一周的最小天数
  22. let minimalDaysInFirstWeek = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 1

  24. // 设置一年中第一周的最小天数
  25. calendar.setMinimalDaysInFirstWeek(3);

  27. // 获取日历对象中与field相关联的值
  28. let year = calendar.get('year'); // year = 2022

  30. // 获取日历对象本地化名称
  31. let calendarName = calendar.getDisplayName('zh-Hans'); // calendarName = '公历'

  33. // 判断指定的日期在日历中是否为周末
  34. let isWeekend = calendar.isWeekend(new Date(2023, 9, 15)); // isWeekend = true

  36. // 在日历的给定字段进行加减操作
  37. calendar.set(2023, 10, 15);
  38. calendar.add('date', 2);
  39. let day = calendar.get('date'); // day = 17

  41. // 比较日历和指定日期相差的天数
  42. let daysDifference = calendar.compareDays(new Date(2023, 10, 15)); // daysDifference = -3
  ```

  [CalendarSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CalendarSetting.ets#L23-L66)
* 获取公历日期对应的农历日期。

  ```
  1. let calendarChinese: i18n.Calendar = i18n.getCalendar('zh-Hans', 'chinese');
  2. // 将公历日期设置到calendar对象，时间日期为2023.07.25 08:00:00
  3. calendarChinese.setTime(new Date(2023, 6, 25, 8, 0, 0));

  5. // 获取农历年月日
  6. let yearChinese = calendarChinese.get('year'); // year = 40，指干支纪年40，范围1-60
  7. let monthChinese = calendarChinese.get('month'); // month = 5，指6月
  8. let dayChinese = calendarChinese.get('date'); // day = 8，指8日
  ```

  [CalendarSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CalendarSetting.ets#L68-L77)

**表1** 支持的历法

| 类型 | 中文名称 |
| --- | --- |
| buddhist | 佛历 |
| chinese | 农历 |
| coptic | 科普特历 |
| ethiopic | 埃塞俄比亚历 |
| hebrew | 希伯来历 |
| gregory | 公历 |
| indian | 印度历 |
| islamic\_civil | 伊斯兰希吉来历 |
| islamic\_tbla | 伊斯兰天文历 |
| islamic\_umalqura | 伊斯兰历（乌姆库拉） |
| japanese | 日本历 |
| persian | 波斯历 |

## 示例代码

* [国际化-日历](https://gitcode.com/harmonyos_samples/international)
