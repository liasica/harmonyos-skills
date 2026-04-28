---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-6003
title: User Authentication Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > User Authentication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:23+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:aca617ae3270fcb1ef3be5bddd6603c6caf8dbd31b8679d84d5ab28f12d58a80
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：userAuth；  API声明：enum UserAuthTipCode  差异内容：enum UserAuthTipCode | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode；  API声明：COMPARE\_FAILURE = 1  差异内容：COMPARE\_FAILURE = 1 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode；  API声明：TIMEOUT = 2  差异内容：TIMEOUT = 2 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode；  API声明：TEMPORARILY\_LOCKED = 3  差异内容：TEMPORARILY\_LOCKED = 3 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode；  API声明：PERMANENTLY\_LOCKED = 4  差异内容：PERMANENTLY\_LOCKED = 4 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode；  API声明：WIDGET\_LOADED = 5  差异内容：WIDGET\_LOADED = 5 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode；  API声明：WIDGET\_RELEASED = 6  差异内容：WIDGET\_RELEASED = 6 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：interface AuthTipInfo  差异内容：interface AuthTipInfo | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthTipInfo；  API声明：tipType: UserAuthType;  差异内容：tipType: UserAuthType; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthTipInfo；  API声明：tipCode: UserAuthTipCode;  差异内容：tipCode: UserAuthTipCode; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：type AuthTipCallback = (authTipInfo: AuthTipInfo) => void;  差异内容：type AuthTipCallback = (authTipInfo: AuthTipInfo) => void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResultCode；  API声明：INVALID\_PARAMETERS = 12500008  差异内容：INVALID\_PARAMETERS = 12500008 | api/@ohos.userIAM.userAuth.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：UserAuthInstance；  API声明：on(type: 'authTip', callback: AuthTipCallback): void;  差异内容：on(type: 'authTip', callback: AuthTipCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：UserAuthInstance；  API声明：off(type: 'authTip', callback?: AuthTipCallback): void;  差异内容：off(type: 'authTip', callback?: AuthTipCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AuthParam；  API声明：skipLockedBiometricAuth?: boolean;  差异内容：skipLockedBiometricAuth?: boolean; | api/@ohos.userIAM.userAuth.d.ts |
