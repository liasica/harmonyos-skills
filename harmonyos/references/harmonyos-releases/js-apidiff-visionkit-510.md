---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-510
title: Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3561fdc15f11ff12bc62858e3f16bac36e8ae83a96bfd961d7645cf77bcc68cc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'cursorMoveInText', callback: Callback<void>): void;  差异内容：on(type: 'cursorMoveInText', callback: Callback<void>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveInText', callback?: ErrorCallback): void;  差异内容：off(type: 'cursorMoveInText', callback?: ErrorCallback): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'cursorMoveOutText', callback: Callback<void>): void;  差异内容：on(type: 'cursorMoveOutText', callback: Callback<void>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveOutText', callback?: ErrorCallback): void;  差异内容：off(type: 'cursorMoveOutText', callback?: ErrorCallback): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Subject；  API声明：maskData?: Int32Array;  差异内容：maskData?: Int32Array; | api/@hms.ai.visionImageAnalyzer.d.ets |
