---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-calendarkit-510
title: Calendar Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Calendar Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:72357dabfa3bf9607e028f80851a944c1e0783c28d305523d20aea0a34521bfd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：calendarManager；  API声明：export enum AttendeeType  差异内容：export enum AttendeeType | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeType；  API声明：REQUIRED = 1  差异内容：REQUIRED = 1 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeType；  API声明：OPTIONAL = 2  差异内容：OPTIONAL = 2 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeType；  API声明：RESOURCE = 3  差异内容：RESOURCE = 3 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：calendarManager；  API声明：export enum AttendeeStatus  差异内容：export enum AttendeeStatus | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeStatus；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeStatus；  API声明：TENTATIVE = 1  差异内容：TENTATIVE = 1 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeStatus；  API声明：ACCEPTED = 2  差异内容：ACCEPTED = 2 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeStatus；  API声明：DECLINED = 3  差异内容：DECLINED = 3 | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：AttendeeStatus；  API声明：UNRESPONSIVE = 4  差异内容：UNRESPONSIVE = 4 | api/@ohos.calendarManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Calendar；  API声明：queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>;  差异内容：queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>; | api/@ohos.calendarManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Event；  API声明：instanceStartTime?: number;  差异内容：instanceStartTime?: number; | api/@ohos.calendarManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Event；  API声明：instanceEndTime?: number;  差异内容：instanceEndTime?: number; | api/@ohos.calendarManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Attendee；  API声明：type?: AttendeeType;  差异内容：type?: AttendeeType; | api/@ohos.calendarManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Attendee；  API声明：status?: AttendeeStatus;  差异内容：status?: AttendeeStatus; | api/@ohos.calendarManager.d.ts |
