---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-6111
title: Multimodal Awareness Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Multimodal Awareness Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:b349d3103c5f1a8fb621efe8680a71a0bbc475e452f66cbb8ae0df6ceeaf30e4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：declare namespace userStatus  差异内容：NA | 类名：global；  API声明：declare namespace userStatus  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：userStatus；  API声明：export interface UserClassification  差异内容：NA | 类名：userStatus；  API声明：export interface UserClassification  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：UserClassification；  API声明：ageGroup?: UserAgeGroup;  差异内容：NA | 类名：UserClassification；  API声明：ageGroup?: UserAgeGroup;  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：UserClassification；  API声明：confidence?: float;  差异内容：NA | 类名：UserClassification；  API声明：confidence?: float;  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：userStatus；  API声明：export enum UserAgeGroup  差异内容：NA | 类名：userStatus；  API声明：export enum UserAgeGroup  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：UserAgeGroup；  API声明：OTHERS = 0  差异内容：NA | 类名：UserAgeGroup；  API声明：OTHERS = 0  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：UserAgeGroup；  API声明：CHILD = 1  差异内容：NA | 类名：UserAgeGroup；  API声明：CHILD = 1  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：userStatus；  API声明：function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void;  差异内容：NA | 类名：userStatus；  API声明：function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void;  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| API废弃版本变更 | 类名：userStatus；  API声明：function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void;  差异内容：NA | 类名：userStatus；  API声明：function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void;  差异内容：24 | api/@ohos.multimodalAwareness.userStatus.d.ts |
