---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-calendarkit-6003
title: Calendar Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Calendar Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7e7c34f3aa702f106df7799f74ccfffcb0e850c5db2a29f3f9a9a91e3925dae0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.WRITE\_CALENDAR | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.WRITE\_CALENDAR | 类名：CalendarManager；  API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar): Promise<void>;  差异内容：ohos.permission.WRITE\_CALENDAR | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar): Promise<void>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.WRITE\_CALENDAR | 类名：CalendarManager；  API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.READ\_CALENDAR | 类名：CalendarManager；  API声明：getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR | 类名：CalendarManager；  API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getCalendar(callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR | 类名：CalendarManager；  API声明：getCalendar(callback: AsyncCallback<Calendar>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getAllCalendars(): Promise<Calendar[]>;  差异内容：ohos.permission.READ\_CALENDAR | 类名：CalendarManager；  API声明：getAllCalendars(): Promise<Calendar[]>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager；  API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void;  差异内容：ohos.permission.READ\_CALENDAR | 类名：CalendarManager；  API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | api/@ohos.calendarManager.d.ts |
