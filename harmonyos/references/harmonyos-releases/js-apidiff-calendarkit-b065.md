---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-calendarkit-b065
title: Calendar Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Calendar Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4f10258def55f93c9660f7e1d96e0516b1caa7b0528ea460493a38c7aee74e21
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.WRITE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.WRITE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar): Promise<void>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar): Promise<void>;  差异内容：ohos.permission.WRITE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.WRITE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.READ\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getCalendar(callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：getCalendar(callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getAllCalendars(): Promise<Calendar[]>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：getAllCalendars(): Promise<Calendar[]>;  差异内容：ohos.permission.READ\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：CalendarManager；  API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void;  差异内容：ohos.permission.READ\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule；  API声明：daysOfWeek?: number[];  差异内容：daysOfWeek?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule；  API声明：daysOfMonth?: number[];  差异内容：daysOfMonth?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule；  API声明：daysOfYear?: number[];  差异内容：daysOfYear?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule；  API声明：weeksOfMonth?: number[];  差异内容：weeksOfMonth?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule；  API声明：weeksOfYear?: number[];  差异内容：weeksOfYear?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule；  API声明：monthsOfYear?: number[];  差异内容：monthsOfYear?: number[]; | api/@ohos.calendarManager.d.ts |
