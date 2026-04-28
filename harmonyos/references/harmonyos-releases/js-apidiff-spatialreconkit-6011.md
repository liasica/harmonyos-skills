---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-spatialreconkit-6011
title: Spatial Recon Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Spatial Recon Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:33e4150255aae08d28aed9b01aff3cce3495542b51ebdc0aeb7596e5fa86a232
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace spatialRender  差异内容：declare namespace spatialRender | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface GSImportSettings  差异内容：export interface GSImportSettings | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSImportSettings；  API声明：uri: string;  差异内容：uri: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSImportSettings；  API声明：offset?: number;  差异内容：offset?: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface GSNode  差异内容：export interface GSNode | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export class GSPlugin  差异内容：export class GSPlugin | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static readonly PLUGIN\_ID: string;  差异内容：static readonly PLUGIN\_ID: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static readonly RETRO\_EFFECT\_ID: string;  差异内容：static readonly RETRO\_EFFECT\_ID: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static readonly COMIC\_EFFECT\_ID: string;  差异内容：static readonly COMIC\_EFFECT\_ID: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static readonly OBRA\_DINN\_EFFECT\_ID: string;  差异内容：static readonly OBRA\_DINN\_EFFECT\_ID: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static readonly COLOR\_EDITING\_EFFECT\_ID: string;  差异内容：static readonly COLOR\_EDITING\_EFFECT\_ID: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static loadGSNode(scene: Scene, params: GSImportSettings, parent?: Node): Promise<GSNode>;  差异内容：static loadGSNode(scene: Scene, params: GSImportSettings, parent?: Node): Promise<GSNode>; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface RetroEffect  差异内容：export interface RetroEffect | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffect；  API声明：colorNum: number;  差异内容：colorNum: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffect；  API声明：pixelSize: number;  差异内容：pixelSize: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffect；  API声明：blendEnabled: boolean;  差异内容：blendEnabled: boolean; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffect；  API声明：curve: number;  差异内容：curve: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface ComicEffect  差异内容：export interface ComicEffect | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ComicEffect；  API声明：lineThreshold: number;  差异内容：lineThreshold: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ComicEffect；  API声明：lineColor: Color;  差异内容：lineColor: Color; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface ObraDinnEffect  差异内容：export interface ObraDinnEffect | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffect；  API声明：noiseStrength: number;  差异内容：noiseStrength: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffect；  API声明：threshold: number;  差异内容：threshold: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffect；  API声明：foregroundColor: Color;  差异内容：foregroundColor: Color; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffect；  API声明：backgroundColor: Color;  差异内容：backgroundColor: Color; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface ColorEditingEffect  差异内容：export interface ColorEditingEffect | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffect；  API声明：exposure: number;  差异内容：exposure: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffect；  API声明：contrast: number;  差异内容：contrast: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffect；  API声明：temperature: number;  差异内容：temperature: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffect；  API声明：tint: number;  差异内容：tint: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffect；  API声明：saturation: number;  差异内容：saturation: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffect；  API声明：vibrance: number;  差异内容：vibrance: number; | api/@hms.graphics.spatialRender.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.graphics.spatialRender.d.ts  差异内容：SpatialReconKit | api/@hms.graphics.spatialRender.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.SpatialReconKit.d.ts  差异内容：SpatialReconKit | kits/@kit.SpatialReconKit.d.ts |
