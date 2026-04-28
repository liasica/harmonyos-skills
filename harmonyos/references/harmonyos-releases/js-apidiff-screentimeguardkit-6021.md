---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6021
title: Screen Time Guard Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Screen Time Guard Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:acdc7bf03fcf228021f097a1377b3e0157d0100b1d7afd04aaa6b5cc137bec07
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：appPicker；  API声明：function startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>;  差异内容：function startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：INVALID\_PARAM = 1019000009  差异内容：INVALID\_PARAM = 1019000009 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategyType；  API声明：INCLUSIVE\_DURATION\_TYPE = 3  差异内容：INCLUSIVE\_DURATION\_TYPE = 3 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
