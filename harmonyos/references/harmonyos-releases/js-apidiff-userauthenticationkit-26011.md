---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-26011
title: User Authentication Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > User Authentication Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d19028b2b83fc082d18b8335fcd8f8bdfe15a3abb2669f4d7b3eff2d5f25bbde
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：userAuth；  API声明：enum UserRecognitionStatus  差异内容：enum UserRecognitionStatus | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionStatus；  API声明：UNCERTAIN = 0  差异内容：UNCERTAIN = 0 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionStatus；  API声明：MISMATCH = 1  差异内容：MISMATCH = 1 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionStatus；  API声明：MATCH = 2  差异内容：MATCH = 2 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：interface UserRecognitionResult  差异内容：interface UserRecognitionResult | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionResult；  API声明：status: UserRecognitionStatus;  差异内容：status: UserRecognitionStatus; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionResult；  API声明：userId: number;  差异内容：userId: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionResult；  API声明：userInfo: string;  差异内容：userInfo: string; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionResult；  API声明：authTrustLevel?: AuthTrustLevel;  差异内容：authTrustLevel?: AuthTrustLevel; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：type UserRecognitionResultCallback = (result: UserRecognitionResult) => void;  差异内容：type UserRecognitionResultCallback = (result: UserRecognitionResult) => void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：interface UserRecognitionMgr  差异内容：interface UserRecognitionMgr | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionMgr；  API声明：getUserRecognitionResult(): Promise<UserRecognitionResult>;  差异内容：getUserRecognitionResult(): Promise<UserRecognitionResult>; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionMgr；  API声明：onUserRecognitionChange(callback: UserRecognitionResultCallback): void;  差异内容：onUserRecognitionChange(callback: UserRecognitionResultCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserRecognitionMgr；  API声明：offUserRecognitionChange(callback?: UserRecognitionResultCallback): void;  差异内容：offUserRecognitionChange(callback?: UserRecognitionResultCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：function getUserRecognitionMgr(): UserRecognitionMgr | null;  差异内容：function getUserRecognitionMgr(): UserRecognitionMgr | null; | api/@ohos.userIAM.userAuth.d.ts |
