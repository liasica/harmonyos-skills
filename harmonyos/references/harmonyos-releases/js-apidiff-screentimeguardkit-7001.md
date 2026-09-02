---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-7001
title: Screen Time Guard Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Screen Time Guard Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:37fb133e3b3e59b3c3332f90051e0f3ec2dcb15e64ad89c72a3cdd24734a3e8d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：SYSCAP\_UNSUPPORTED\_STRATEGY\_TYPE = 1019000011  差异内容：SYSCAP\_UNSUPPORTED\_STRATEGY\_TYPE = 1019000011 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：interface GuardStrategyData  差异内容：interface GuardStrategyData | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategyData；  API声明：usageDuration: number;  差异内容：usageDuration: number; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function queryGuardStrategyData(strategyName: string): Promise<GuardStrategyData>;  差异内容：function queryGuardStrategyData(strategyName: string): Promise<GuardStrategyData>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
