---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-b031
title: UI Design Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:44+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ee2fcc4d29ed07a6213511b7d8cbd0c870bbb97e1a613eaad449ded905f1cfe0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace hdsDrawable  差异内容： declare namespace hdsDrawable | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明：function getHdsLayeredIcon(bundleName: string, layeredDrawableDescriptor: LayeredDrawableDescriptor, size: number, hasBorder?: boolean): image.PixelMap;  差异内容：function getHdsLayeredIcon(bundleName: string, layeredDrawableDescriptor: LayeredDrawableDescriptor, size: number, hasBorder?: boolean): image.PixelMap; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明：function getHdsIcon(bundleName: string, pixelMap: image.PixelMap, size: number, mask: image.PixelMap, hasBorder?: boolean): image.PixelMap;  差异内容：function getHdsIcon(bundleName: string, pixelMap: image.PixelMap, size: number, mask: image.PixelMap, hasBorder?: boolean): image.PixelMap; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明：function getHdsIcons(icons: Array<Icon>, mask: image.PixelMap, options: Options): Promise<Array<ProcessedIcon>>;  差异内容：function getHdsIcons(icons: Array<Icon>, mask: image.PixelMap, options: Options): Promise<Array<ProcessedIcon>>; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明：function getHdsLayeredIcons(icons: Array<LayeredIcon>, options: Options): Promise<Array<ProcessedIcon>>;  差异内容：function getHdsLayeredIcons(icons: Array<LayeredIcon>, options: Options): Promise<Array<ProcessedIcon>>; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明： export interface LayeredIcon  差异内容： export interface LayeredIcon | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：LayeredIcon；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：LayeredIcon；  API声明：layeredDrawableDescriptor: LayeredDrawableDescriptor;  差异内容：layeredDrawableDescriptor: LayeredDrawableDescriptor; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明： export interface Icon  差异内容： export interface Icon | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：Icon；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：Icon；  API声明：pixelMap: image.PixelMap;  差异内容：pixelMap: image.PixelMap; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明： export interface ProcessedIcon  差异内容： export interface ProcessedIcon | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：ProcessedIcon；  API声明：readonly bundleName: string;  差异内容：readonly bundleName: string; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：ProcessedIcon；  API声明：readonly pixelMap: image.PixelMap;  差异内容：readonly pixelMap: image.PixelMap; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明： export interface Options  差异内容： export interface Options | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：Options；  API声明：size: number;  差异内容：size: number; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：Options；  API声明：hasBorder?: boolean;  差异内容：hasBorder?: boolean; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：Options；  API声明：parallelNumber?: number;  差异内容：parallelNumber?: number; | api/@hms.hds.hdsDrawable.d.ts |
