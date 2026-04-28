---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-6002
title: Multimodal Awareness Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Multimodal Awareness Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:31+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6f2be92ec1bd9e294241210ad278016d6a3402a32953990e20626d4a5e804f43
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：ohos.permission.ACTIVITY\_MOTION | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace userStatus  差异内容：declare namespace userStatus | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus；  API声明：export interface UserClassification  差异内容：export interface UserClassification | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserClassification；  API声明：ageGroup?: UserAgeGroup;  差异内容：ageGroup?: UserAgeGroup; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserClassification；  API声明：confidence?: float;  差异内容：confidence?: float; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus；  API声明：export enum UserAgeGroup  差异内容：export enum UserAgeGroup | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserAgeGroup；  API声明：OTHERS = 0  差异内容：OTHERS = 0 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserAgeGroup；  API声明：CHILD = 1  差异内容：CHILD = 1 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus；  API声明：function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void;  差异内容：function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus；  API声明：function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void;  差异内容：function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：motion；  API声明：export enum HoldingHandStatus  差异内容：export enum HoldingHandStatus | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus；  API声明：NOT\_HELD = 0  差异内容：NOT\_HELD = 0 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus；  API声明：LEFT\_HAND\_HELD = 1  差异内容：LEFT\_HAND\_HELD = 1 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus；  API声明：RIGHT\_HAND\_HELD = 2  差异内容：RIGHT\_HAND\_HELD = 2 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus；  API声明：BOTH\_HANDS\_HELD = 3  差异内容：BOTH\_HANDS\_HELD = 3 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus；  API声明：UNKNOWN\_STATUS = 16  差异内容：UNKNOWN\_STATUS = 16 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion；  API声明：function on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void;  差异内容：function on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void; | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion；  API声明：function off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void;  差异内容：function off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void; | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimodalAwareness.userStatus.d.ts  差异内容：MultimodalAwarenessKit | api/@ohos.multimodalAwareness.userStatus.d.ts |
