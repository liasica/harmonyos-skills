---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-timezone-interface-check
title: @performance/timezone-interface-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/timezone-interface-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:19+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d27ea6d895576e4a7b659206a0b48ecb1b3c4ce1044b7cc858c15ce3c6959050
---

在获取非本地时间时，建议使用统一标准的i18n.Calendar接口获取时间时区相关信息。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/timezone-interface-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例1

```
1. import i18n from '@ohos.i18n';

3. let calendar = i18n.getCalendar(i18n.getSystemLocale());
4. calendar.setTimeZone(i18n.getTimeZone().getID());
```

## 正例2

```
1. import i18n from '@ohos.i18n';

3. let timeZone1 = '123';
4. let calendar1 = i18n.getCalendar(i18n.getSystemLocale());
5. calendar1.setTimeZone(timeZone1);
6. calendar1.get('zone_offset');
7. calendar1.get('dst_offset');
```

## 反例1

```
1. import i18n from '@ohos.i18n';

3. let timeZone1 = '123';
4. let calendar1 = i18n.getCalendar(i18n.getSystemLocale());
5. calendar1.setTimeZone(timeZone1);
6. //告警，缺少获取dst_offset
7. calendar1.get('zone_offset');
8. //calendar1.get('dst_offset');
```

## 反例2

```
1. import moment from '@hview/moment';
2. //告警
3. moment().utcOffset();
4. //告警
5. moment().utcOffset(120);
6. //告警
7. moment().utcOffset("+08:00");
8. //告警
9. moment().utcOffset(-5, true);
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
