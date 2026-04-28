---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-penkit-5111
title: Pen Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Pen Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c09d8083dd6385fb02adbb38b40c9c48eefb40d8c274f140939d46feacb4fff3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace stylusInteraction  差异内容：declare namespace stylusInteraction | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void;  差异内容：function on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void;  差异内容：function off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：export interface SqueezeEvent  差异内容：export interface SqueezeEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：SqueezeEvent；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void;  差异内容：function on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void;  差异内容：function off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：export interface DoubleTapEvent  差异内容：export interface DoubleTapEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：DoubleTapEvent；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.officeservice.stylusInteraction.d.ts  差异内容：Penkit | api/@hms.officeservice.stylusInteraction.d.ts |
