---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-penkit-510
title: Pen kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Pen kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e32ffcf6b38aade1ccd48113c70daad18c0fbe5d16a5aa764fa9cd3bcab42780
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare type InitCallback = () => void;  差异内容：declare type InitCallback = () => void; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type ScaleCallback = (scale: number) => void;  差异内容：declare type ScaleCallback = (scale: number) => void; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HandwriteComponent；  API声明：defaultPenType?: PenType;  差异内容：defaultPenType?: PenType; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HandwriteComponent；  API声明：defaultPenInfo?: PenHspInfo[];  差异内容：defaultPenInfo?: PenHspInfo[]; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface PenHspInfo  差异内容：export interface PenHspInfo | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenHspInfo；  API声明：penType: PenType;  差异内容：penType: PenType; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenHspInfo；  API声明：penWidth: number;  差异内容：penWidth: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export enum PenType  差异内容：export enum PenType | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：PEN = 1  差异内容：PEN = 1 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：BALLPOINT\_PEN = 2  差异内容：BALLPOINT\_PEN = 2 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：PENCIL = 3  差异内容：PENCIL = 3 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：MARKER = 4  差异内容：MARKER = 4 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：HIGHLIGHTER\_BRUSH = 5  差异内容：HIGHLIGHTER\_BRUSH = 5 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：MOSAIC = 7  差异内容：MOSAIC = 7 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：RUBBER = 8  差异内容：RUBBER = 8 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：LASSO = 9  差异内容：LASSO = 9 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：PenType；  API声明：LASER = 10  差异内容：LASER = 10 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：imageFeaturePicker；  API声明：function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>;  差异内容：function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 函数变更 | 类名：HandwriteComponent；  API声明：onInit?: () => void;  差异内容：() => void | 类名：HandwriteComponent；  API声明：onInit?: InitCallback;  差异内容：InitCallback | api/@hms.stylus.HandwriteComponent.d.ets |
| 函数变更 | 类名：HandwriteComponent；  API声明：onScale?: (scale: number) => void;  差异内容：(scale: number) => void | 类名：HandwriteComponent；  API声明：onScale?: ScaleCallback;  差异内容：ScaleCallback | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export interface PenHspInfo  差异内容：NA | 类名：global；  API声明：  差异内容：export interface PenHspInfo | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export enum PenType  差异内容：NA | 类名：global；  API声明：  差异内容：export enum PenType | api/@hms.stylus.HandwriteComponent.d.ets |
