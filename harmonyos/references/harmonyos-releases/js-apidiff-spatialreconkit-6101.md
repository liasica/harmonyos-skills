---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-spatialreconkit-6101
title: Spatial Recon Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Spatial Recon Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af5ee5c4ee07ca898d8ac8a89e06f42b90b83e19b1d2ec45a950839d9088c5a2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global；  API声明：declare namespace spatialRender  差异内容：NA | 类名：global；  API声明：declare namespace spatialRender  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export interface GSImportSettings  差异内容：NA | 类名：spatialRender；  API声明：export interface GSImportSettings  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：GSImportSettings；  API声明：uri: string;  差异内容：NA | 类名：GSImportSettings；  API声明：uri: string;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：GSImportSettings；  API声明：offset?: number;  差异内容：NA | 类名：GSImportSettings；  API声明：offset?: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export interface GSNode  差异内容：NA | 类名：spatialRender；  API声明：export interface GSNode  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export class GSPlugin  差异内容：NA | 类名：spatialRender；  API声明：export class GSPlugin  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：GSPlugin；  API声明：static loadGSNode(scene: Scene, params: GSImportSettings, parent?: Node): Promise<GSNode>;  差异内容：NA | 类名：GSPlugin；  API声明：static loadGSNode(scene: Scene, params: GSImportSettings, parent?: Node): Promise<GSNode>;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export interface RetroEffect  差异内容：NA | 类名：spatialRender；  API声明：export interface RetroEffect  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：RetroEffect；  API声明：colorNum: number;  差异内容：NA | 类名：RetroEffect；  API声明：colorNum: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：RetroEffect；  API声明：pixelSize: number;  差异内容：NA | 类名：RetroEffect；  API声明：pixelSize: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：RetroEffect；  API声明：blendEnabled: boolean;  差异内容：NA | 类名：RetroEffect；  API声明：blendEnabled: boolean;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：RetroEffect；  API声明：curve: number;  差异内容：NA | 类名：RetroEffect；  API声明：curve: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export interface ComicEffect  差异内容：NA | 类名：spatialRender；  API声明：export interface ComicEffect  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ComicEffect；  API声明：lineThreshold: number;  差异内容：NA | 类名：ComicEffect；  API声明：lineThreshold: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ComicEffect；  API声明：lineColor: Color;  差异内容：NA | 类名：ComicEffect；  API声明：lineColor: Color;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export interface ObraDinnEffect  差异内容：NA | 类名：spatialRender；  API声明：export interface ObraDinnEffect  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ObraDinnEffect；  API声明：noiseStrength: number;  差异内容：NA | 类名：ObraDinnEffect；  API声明：noiseStrength: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ObraDinnEffect；  API声明：threshold: number;  差异内容：NA | 类名：ObraDinnEffect；  API声明：threshold: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ObraDinnEffect；  API声明：foregroundColor: Color;  差异内容：NA | 类名：ObraDinnEffect；  API声明：foregroundColor: Color;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ObraDinnEffect；  API声明：backgroundColor: Color;  差异内容：NA | 类名：ObraDinnEffect；  API声明：backgroundColor: Color;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：spatialRender；  API声明：export interface ColorEditingEffect  差异内容：NA | 类名：spatialRender；  API声明：export interface ColorEditingEffect  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ColorEditingEffect；  API声明：exposure: number;  差异内容：NA | 类名：ColorEditingEffect；  API声明：exposure: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ColorEditingEffect；  API声明：contrast: number;  差异内容：NA | 类名：ColorEditingEffect；  API声明：contrast: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ColorEditingEffect；  API声明：temperature: number;  差异内容：NA | 类名：ColorEditingEffect；  API声明：temperature: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ColorEditingEffect；  API声明：tint: number;  差异内容：NA | 类名：ColorEditingEffect；  API声明：tint: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ColorEditingEffect；  API声明：saturation: number;  差异内容：NA | 类名：ColorEditingEffect；  API声明：saturation: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| API模型切换 | 类名：ColorEditingEffect；  API声明：vibrance: number;  差异内容：NA | 类名：ColorEditingEffect；  API声明：vibrance: number;  差异内容：stagemodelonly | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static get PLUGIN\_ID(): string;  差异内容：static get PLUGIN\_ID(): string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static get RETRO\_EFFECT\_ID(): string;  差异内容：static get RETRO\_EFFECT\_ID(): string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static get COMIC\_EFFECT\_ID(): string;  差异内容：static get COMIC\_EFFECT\_ID(): string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static get OBRA\_DINN\_EFFECT\_ID(): string;  差异内容：static get OBRA\_DINN\_EFFECT\_ID(): string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static get COLOR\_EDITING\_EFFECT\_ID(): string;  差异内容：static get COLOR\_EDITING\_EFFECT\_ID(): string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export enum RetroEffectParams  差异内容：export enum RetroEffectParams | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffectParams；  API声明：COLOR\_NUM = 'colorNum'  差异内容：COLOR\_NUM = 'colorNum' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffectParams；  API声明：PIXEL\_SIZE = 'pixelSize'  差异内容：PIXEL\_SIZE = 'pixelSize' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffectParams；  API声明：BLEND\_ENABLED = 'blendEnabled'  差异内容：BLEND\_ENABLED = 'blendEnabled' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：RetroEffectParams；  API声明：CURVE = 'curve'  差异内容：CURVE = 'curve' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export enum ComicEffectParams  差异内容：export enum ComicEffectParams | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ComicEffectParams；  API声明：LINE\_THRESHOLD = 'lineThreshold'  差异内容：LINE\_THRESHOLD = 'lineThreshold' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ComicEffectParams；  API声明：LINE\_COLOR = 'lineColor'  差异内容：LINE\_COLOR = 'lineColor' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export enum ObraDinnEffectParams  差异内容：export enum ObraDinnEffectParams | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffectParams；  API声明：NOISE\_STRENGTH = 'noiseStrength'  差异内容：NOISE\_STRENGTH = 'noiseStrength' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffectParams；  API声明：THRESHOLD = 'threshold'  差异内容：THRESHOLD = 'threshold' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffectParams；  API声明：FOREGROUND\_COLOR = 'foregroundColor'  差异内容：FOREGROUND\_COLOR = 'foregroundColor' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ObraDinnEffectParams；  API声明：BACKGROUND\_COLOR = 'backgroundColor'  差异内容：BACKGROUND\_COLOR = 'backgroundColor' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export enum ColorEditingEffectParams  差异内容：export enum ColorEditingEffectParams | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffectParams；  API声明：EXPOSURE = 'exposure'  差异内容：EXPOSURE = 'exposure' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffectParams；  API声明：CONTRAST = 'contrast'  差异内容：CONTRAST = 'contrast' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffectParams；  API声明：TEMPERATURE = 'temperature'  差异内容：TEMPERATURE = 'temperature' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffectParams；  API声明：TINT = 'tint'  差异内容：TINT = 'tint' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffectParams；  API声明：SATURATION = 'saturation'  差异内容：SATURATION = 'saturation' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：ColorEditingEffectParams；  API声明：VIBRANCE = 'vibrance'  差异内容：VIBRANCE = 'vibrance' | api/@hms.graphics.spatialRender.d.ts |
| 删除API | 类名：GSPlugin；  API声明：static readonly PLUGIN\_ID: string;  差异内容：static readonly PLUGIN\_ID: string; | NA | api/@hms.graphics.spatialRender.d.ts |
| 删除API | 类名：GSPlugin；  API声明：static readonly RETRO\_EFFECT\_ID: string;  差异内容：static readonly RETRO\_EFFECT\_ID: string; | NA | api/@hms.graphics.spatialRender.d.ts |
| 删除API | 类名：GSPlugin；  API声明：static readonly COMIC\_EFFECT\_ID: string;  差异内容：static readonly COMIC\_EFFECT\_ID: string; | NA | api/@hms.graphics.spatialRender.d.ts |
| 删除API | 类名：GSPlugin；  API声明：static readonly OBRA\_DINN\_EFFECT\_ID: string;  差异内容：static readonly OBRA\_DINN\_EFFECT\_ID: string; | NA | api/@hms.graphics.spatialRender.d.ts |
| 删除API | 类名：GSPlugin；  API声明：static readonly COLOR\_EDITING\_EFFECT\_ID: string;  差异内容：static readonly COLOR\_EDITING\_EFFECT\_ID: string; | NA | api/@hms.graphics.spatialRender.d.ts |
