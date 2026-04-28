---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-ringtonekit-b035
title: Ringtone Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Ringtone Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:33+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a013624673e67aaa826b7293d10bcb7692fd07f925bb41d58c9e3f80ea1d0b4c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace ringtone  差异内容： declare namespace ringtone | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明： enum RingtoneType  差异内容： enum RingtoneType | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType；  API声明：CALL = 0  差异内容：CALL = 0 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType；  API声明：MESSAGE = 1  差异内容：MESSAGE = 1 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType；  API声明：NOTIFICATION = 2  差异内容：NOTIFICATION = 2 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType；  API声明：ALARM = 3  差异内容：ALARM = 3 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明：function getSupportedRingtoneTypes(): Array<RingtoneType>;  差异内容：function getSupportedRingtoneTypes(): Array<RingtoneType>; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明：function getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>;  差异内容：function getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明：function getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number;  差异内容：function getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback<RingtoneType>): void;  差异内容：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback<RingtoneType>): void; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise<RingtoneType>;  差异内容：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise<RingtoneType>; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone；  API声明： enum RingtoneErrors  差异内容： enum RingtoneErrors | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors；  API声明：ERROR\_INVALID\_PARAM = 401  差异内容：ERROR\_INVALID\_PARAM = 401 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors；  API声明：ERROR\_USER\_CANCELED = 1011600001  差异内容：ERROR\_USER\_CANCELED = 1011600001 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors；  API声明：ERROR\_FILE\_NOT\_FOUND = 1011600002  差异内容：ERROR\_FILE\_NOT\_FOUND = 1011600002 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors；  API声明：ERROR\_SHOW\_FAILED = 1011600003  差异内容：ERROR\_SHOW\_FAILED = 1011600003 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors；  API声明：ERROR\_CALL\_SYSTEM\_API\_FAILED = 1011600004  差异内容：ERROR\_CALL\_SYSTEM\_API\_FAILED = 1011600004 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors；  API声明：ERROR\_SYSTEM = 1011699999  差异内容：ERROR\_SYSTEM = 1011699999 | api/@hms.core.ringtone.d.ts |
