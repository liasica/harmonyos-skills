---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-b061
title: Account Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta6引入的API > Account Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:21+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dfc03d99c5e04f0a8533dd194ba17a18e57685a53cafc170e85528d3b73d9a15
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AuthenticationErrorCode；  API声明：UNSUPPORTED = 1001500004  差异内容：UNSUPPORTED = 1001500004 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：AuthenticationErrorCode；  API声明：REQUEST\_RESTRICTED = 1001500005  差异内容：REQUEST\_RESTRICTED = 1001500005 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：authentication；  API声明： export interface ConsistencyRequest  差异内容： export interface ConsistencyRequest | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyRequest；  API声明：idType: IdType;  差异内容：idType: IdType; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyRequest；  API声明：idValue: string;  差异内容：idValue: string; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyRequest；  API声明：mobileNumber: string;  差异内容：mobileNumber: string; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：authentication；  API声明： export enum ConsistencyState  差异内容： export enum ConsistencyState | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyState；  API声明：CONSISTENT = 0  差异内容：CONSISTENT = 0 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyState；  API声明：INCONSISTENT\_WITH\_DEVICES = 1  差异内容：INCONSISTENT\_WITH\_DEVICES = 1 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyState；  API声明：INCONSISTENT = 2  差异内容：INCONSISTENT = 2 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：authentication；  API声明： export interface ConsistencyResult  差异内容： export interface ConsistencyResult | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyResult；  API声明：state: ConsistencyState;  差异内容：state: ConsistencyState; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：HuaweiIDProvider；  API声明：getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>;  差异内容：getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>; | api/@hms.core.authentication.d.ts |
