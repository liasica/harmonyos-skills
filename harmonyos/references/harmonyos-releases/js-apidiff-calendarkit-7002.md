---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-calendarkit-7002
title: Calendar Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Calendar Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7708377e0cc2752847acfb420ccf763b5415b4282e697058d0b972f4e188fe59
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：Calendar；  API声明：addEvent(event: Event): Promise<number>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：addEvent(event: Event): Promise<number>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：addEvent(event: Event, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：addEvent(event: Event, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：addEvents(events: Event[]): Promise<void>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：addEvents(events: Event[]): Promise<void>;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：addEvents(events: Event[], callback: AsyncCallback<void>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：addEvents(events: Event[], callback: AsyncCallback<void>): void;  差异内容：ohos.permission.WRITE\_CALENDAR or ohos.permission.WRITE\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：getEvents(callback: AsyncCallback<Event[]>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：getEvents(callback: AsyncCallback<Event[]>): void;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：Calendar；  API声明：queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR | 类名：Calendar；  API声明：queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>;  差异内容：ohos.permission.READ\_CALENDAR or ohos.permission.READ\_WHOLE\_CALENDAR [since 23] | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：Calendar；  API声明：openEventEditPage(id: number): Promise<void>;  差异内容：openEventEditPage(id: number): Promise<void>; | api/@ohos.calendarManager.d.ts |
