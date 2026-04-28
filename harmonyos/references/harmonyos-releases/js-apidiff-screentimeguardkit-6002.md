---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6002
title: Screen Time Guard Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Screen Time Guard Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e6c6502dfa506d7cd041aaee2487ba6b4f6b02169e302ae92a090faa1a429fa3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：appPicker；  API声明：function startAppPicker(context: common.Context, appSelection: AppInfo): Promise<string[]>;  差异内容：appSelection: AppInfo | 类名：appPicker；  API声明：function startAppPicker(context: common.Context, appSelection: guardService.AppInfo): Promise<string[]>;  差异内容：appSelection: guardService.AppInfo | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
