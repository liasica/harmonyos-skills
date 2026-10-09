---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-timezone-interface-check
title: "@performance/timezone-interface-check"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/timezone-interface-check
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b1d8c41cb809a09a8ef7b968a80b6bbbd82f65d48dd7c7040d673af59c2d8ab7
---

在获取非本地时间时，建议使用统一标准的i18n.Calendar接口获取时间时区相关信息。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/timezone-interface-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例1

```ts
import i18n from '@ohos.i18n';

let calendar = i18n.getCalendar(i18n.getSystemLocale());
calendar.setTimeZone(i18n.getTimeZone().getID());
```

## 正例2

```ts
import i18n from '@ohos.i18n';

let timeZone1 = '123';
let calendar1 = i18n.getCalendar(i18n.getSystemLocale());
calendar1.setTimeZone(timeZone1);
calendar1.get('zone_offset'); 
calendar1.get('dst_offset');
```

## 反例1

```ts
import i18n from '@ohos.i18n';

let timeZone1 = '123';
let calendar1 = i18n.getCalendar(i18n.getSystemLocale());
calendar1.setTimeZone(timeZone1);
//告警，缺少获取dst_offset
calendar1.get('zone_offset'); 
//calendar1.get('dst_offset');
```

## 反例2

```ts
import moment from '@hview/moment';
//告警
moment().utcOffset();
//告警
moment().utcOffset(120);
//告警
moment().utcOffset("+08:00");
//告警
moment().utcOffset(-5, true);
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
