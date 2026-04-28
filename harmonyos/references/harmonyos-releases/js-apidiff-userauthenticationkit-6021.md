---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-6021
title: User Authentication Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > User Authentication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:eefea863ee10c1285c84279a210cd8617eb334e2cd4d45584d8dc5aa2fa9c33b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：userAuth；  API声明：const PERMANENT\_LOCKOUT\_DURATION: number = 0x7fffffff;  差异内容：const PERMANENT\_LOCKOUT\_DURATION: number = 0x7fffffff; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：interface AuthLockState  差异内容：interface AuthLockState | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthLockState；  API声明：isLocked: boolean;  差异内容：isLocked: boolean; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthLockState；  API声明：remainingAuthAttempts: number;  差异内容：remainingAuthAttempts: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthLockState；  API声明：lockoutDuration: number;  差异内容：lockoutDuration: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>;  差异内容：function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>; | api/@ohos.userIAM.userAuth.d.ts |
