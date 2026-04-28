---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-5111
title: Device Security Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f522ee3d14d6d2312467f6480e21eb89fbc69e6f6f70340ff4c89da15ae824cc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：antifraudPicker；  API声明：interface AntifraudAppOptions  差异内容：interface AntifraudAppOptions | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：AntifraudAppOptions；  API声明：maxSelectNumber?: number;  差异内容：maxSelectNumber?: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明：interface AntifraudAppResult  差异内容：interface AntifraudAppResult | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：AntifraudAppResult；  API声明：appInfo: SingleAntifraudAppInfo[];  差异内容：appInfo: SingleAntifraudAppInfo[]; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明：interface SingleAntifraudAppInfo  差异内容：interface SingleAntifraudAppInfo | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：applicationName: string;  差异内容：applicationName: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：versionCode: number;  差异内容：versionCode: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：versionName: string;  差异内容：versionName: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：installTime: number;  差异内容：installTime: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：appId: string;  差异内容：appId: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：label: string;  差异内容：label: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudAppInfo；  API声明：installSource: string;  差异内容：installSource: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明：function selectFraudApp(context: common.Context, options?: AntifraudAppOptions): Promise<AntifraudAppResult>;  差异内容：function selectFraudApp(context: common.Context, options?: AntifraudAppOptions): Promise<AntifraudAppResult>; | api/@hms.security.antifraudPicker.d.ts |
