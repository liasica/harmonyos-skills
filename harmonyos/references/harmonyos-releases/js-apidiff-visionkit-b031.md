---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-b031
title: Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:45+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0b26e8aa0f00b83d5cf6cc9cf193dce961169ff7320cff1473dec23181f7759d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：interactiveLiveness；  API声明：function startLivenessDetection(config: InteractiveLivenessConfig, callback: AsyncCallback<InteractiveLivenessResult | undefined>): Promise<boolean>;  差异内容：function startLivenessDetection(config: InteractiveLivenessConfig, callback: AsyncCallback<InteractiveLivenessResult | undefined>): Promise<boolean>; | api/@hms.ai.interactiveLiveness.d.ts |
| 新增API | NA | 类名：InteractiveLivenessConfig；  API声明：challenge?: string;  差异内容：challenge?: string; | api/@hms.ai.interactiveLiveness.d.ts |
| 新增API | NA | 类名：InteractiveLivenessConfig；  API声明：speechSwitch?: boolean;  差异内容：speechSwitch?: boolean; | api/@hms.ai.interactiveLiveness.d.ts |
| 新增API | NA | 类名：InteractiveLivenessResult；  API声明：securedImageBuffer?: ArrayBuffer;  差异内容：securedImageBuffer?: ArrayBuffer; | api/@hms.ai.interactiveLiveness.d.ts |
| 新增API | NA | 类名：InteractiveLivenessResult；  API声明：certificate?: Array<string>;  差异内容：certificate?: Array<string>; | api/@hms.ai.interactiveLiveness.d.ts |
