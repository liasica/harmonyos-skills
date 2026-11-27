---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-kit-faq-0002
title: 查询联系人信息常见问题
breadcrumb: FAQ > 应用服务开发 > 联系人服务（Contacts Kit） > 常见问题 > 查询联系人信息常见问题
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:41+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:a1f68e5d24ab3663dfbd5b482a678a2c3b861a106ef3f122e5d5c1427d84d5c6
---

**Q：查询联系人信息时，存在events有值而significantDates没有值的场景，应用应如何处理？**

**A：**Contact对象中events的类型labelId与通讯录实际存储/显示语义相反。通讯录存储为1=生日、3=周年纪念日，而Contact对象的Event常量为EVENT\_ANNIVERSARY(1)=周年纪念日、EVENT\_BIRTHDAY(3)=生日，导致与通讯录的显示相反。为了避免新的数据significantDates被历史错乱的数据污染，联系人存储端未将历史数据events同步到significantDates，查询联系人信息时，存在events有值而significantDates没有值的场景，建议处理措施如下：

1. significantDates有值时，直接使用significantDates的值，无需进行转换。
2. significantDates没有值时，先读取events数据，转换为significantDates（转换规则如下表，注意：若应用之前已识别到通讯录显示和资料定义相反的问题，并反着调用，则联系人存储的数据是正确的，否则联系人存储的数据是相反的），再进行更新或插入。

events和significantDates的类型转换规则如下：

| events数据中的类型（labelId） | 通讯录实际显示（真实类型） | 转换后significantDates类型（dateType） |
| --- | --- | --- |
| EVENT\_ANNIVERSARY = 1（周年纪念日） | 生日 | DATE\_TYPE\_BIRTHDAY = 1 |
| EVENT\_BIRTHDAY = 3（生日） | 周年纪念日 | DATE\_TYPE\_ANNIVERSARY = 3 |
| EVENT\_OTHER = 2（其他） | 农历生日 | DATE\_TYPE\_LUNAR\_BIRTHDAY = 2 |
| CUSTOM\_LABEL = 0（自定义） | 其他 | DATE\_TYPE\_OTHER = 0 |

示例代码

```ts
/**
 * 应用之前未识别到通讯录显示和资料定义相反的问题，按照kit资料定义添加联系人，通讯录实际显示和资料相反的场景。
 * 将历史events数据（生日/周年纪念日与通讯录显示相反）转换为significantDates数据。
 * events中类型为"周年纪念日"（EVENT_ANNIVERSARY）的数据，通讯录显示为生日。
 * events中类型为"生日"（EVENT_BIRTHDAY）的数据，通讯录显示为周年纪念日。
 */
private convertEventsToSignificantDates(events: Array<contact.Event>): Array<contact.SignificantDate> {
  let significantDates: Array<contact.SignificantDate> = [];
  events.forEach((event: contact.Event) => {
    if (event.labelId === contact.Event.EVENT_ANNIVERSARY) {
      significantDates.push({
        dateValue: event.eventDate,
        dateType: contact.SignificantDateType.DATE_TYPE_ANNIVERSARY
      });
    } else if (event.labelId === contact.Event.EVENT_BIRTHDAY) {
      significantDates.push({
        dateValue: event.eventDate,
        dateType: contact.SignificantDateType.DATE_TYPE_BIRTHDAY
      });
    }
  });
  return significantDates;
}

/**
 * 应用之前已识别到通讯录显示和资料定义相反的问题，生日和周年纪念日按照kit资料反着调用添加联系人，通讯录实际显示和资料匹配的场景。
 * 将历史events数据（通讯录显示正确）转换为significantDates数据。
 */
private convertEventsToSignificantDates(events: Array<contact.Event>): Array<contact.SignificantDate> {
  let significantDates: Array<contact.SignificantDate> = [];
  events.forEach((event: contact.Event) => {
    if (event.labelId === contact.Event.EVENT_ANNIVERSARY) {
      significantDates.push({
        dateValue: event.eventDate,
        dateType: contact.SignificantDateType.DATE_TYPE_BIRTHDAY
      });
    } else if (event.labelId === contact.Event.EVENT_BIRTHDAY) {
      significantDates.push({
        dateValue: event.eventDate,
        dateType: contact.SignificantDateType.DATE_TYPE_ANNIVERSARY
      });
    }
  });
  return significantDates;
}
```
