---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6111
title: Screen Time Guard Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Screen Time Guard Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:b2eb3d3fe4536520367a85c0f910b71ec199d3b744861099277504c8862dd4a1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：guardService；  API声明：function requestUserAuth(context: common.UIAbilityContext, appConfig: AppConfig): Promise<void>;  差异内容：function requestUserAuth(context: common.UIAbilityContext, appConfig: AppConfig): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：SYSCAP\_UNSUPPORTED\_DEVICE = 1019000010  差异内容：SYSCAP\_UNSUPPORTED\_DEVICE = 1019000010 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：interface AppConfig  差异内容：interface AppConfig | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AppConfig；  API声明：isSupportAppUninstall: boolean;  差异内容：isSupportAppUninstall: boolean; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
