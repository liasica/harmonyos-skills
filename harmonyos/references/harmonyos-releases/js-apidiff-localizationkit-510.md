---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-localizationkit-510
title: Localization Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Localization Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:86e5ec6a99f0830788a096939aa69645a8d3f8c962541ac90bc1a59b4f6f2f2e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number, callback: \_AsyncCallback<string>): void;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number): Promise<string>;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringValue(resId: number, num: number, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValue(resId: number, num: number, callback: \_AsyncCallback<string>): void;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringValue(resId: number, num: number): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValue(resId: number, num: number): Promise<string>;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringByName(resName: string, num: number, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringByName(resName: string, num: number, callback: \_AsyncCallback<string>): void;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringByName(resName: string, num: number): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringByName(resName: string, num: number): Promise<string>;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringValueSync(resId: number, num: number): string;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValueSync(resId: number, num: number): string;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringValueSync(resource: Resource, num: number): string;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValueSync(resource: Resource, num: number): string;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getPluralStringByNameSync(resName: string, num: number): string;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringByNameSync(resName: string, num: number): string;  差异内容：18 | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export enum WeekDay  差异内容：export enum WeekDay | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：MON = 1  差异内容：MON = 1 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：TUE = 2  差异内容：TUE = 2 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：WED = 3  差异内容：WED = 3 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：THU = 4  差异内容：THU = 4 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：FRI = 5  差异内容：FRI = 5 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：SAT = 6  差异内容：SAT = 6 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：WeekDay；  API声明：SUN = 7  差异内容：SUN = 7 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export enum TemperatureType  差异内容：export enum TemperatureType | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TemperatureType；  API声明：CELSIUS = 1  差异内容：CELSIUS = 1 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TemperatureType；  API声明：FAHRENHEIT = 2  差异内容：FAHRENHEIT = 2 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TemperatureType；  API声明：KELVIN = 3  差异内容：KELVIN = 3 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat;  差异内容：export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat;  差异内容：export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class SimpleDateTimeFormat  差异内容：export class SimpleDateTimeFormat | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SimpleDateTimeFormat；  API声明：format(date: Date): string;  差异内容：format(date: Date): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat;  差异内容：export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class SimpleNumberFormat  差异内容：export class SimpleNumberFormat | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SimpleNumberFormat；  API声明：format(value: number): string;  差异内容：format(value: number): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class StyledNumberFormat  差异内容：export class StyledNumberFormat | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：StyledNumberFormat；  API声明：format(value: number): StyledString;  差异内容：format(value: number): StyledString; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface StyledNumberFormatOptions  差异内容：export interface StyledNumberFormatOptions | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：StyledNumberFormatOptions；  API声明：integer?: TextStyle;  差异内容：integer?: TextStyle; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：StyledNumberFormatOptions；  API声明：decimal?: TextStyle;  差异内容：decimal?: TextStyle; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：StyledNumberFormatOptions；  API声明：fraction?: TextStyle;  差异内容：fraction?: TextStyle; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：StyledNumberFormatOptions；  API声明：unit?: TextStyle;  差异内容：unit?: TextStyle; | api/@ohos.i18n.d.ts |
| 起始版本有变化 | 类名：Resource；  API声明：params?: any[];  差异内容：7 | 类名：Resource；  API声明：params?: any[];  差异内容：9 | api/global/resource.d.ts |
| 起始版本有变化 | 类名：Resource；  API声明：type?: number;  差异内容：7 | 类名：Resource；  API声明：type?: number;  差异内容：9 | api/global/resource.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：System；  API声明：static getTemperatureType(): TemperatureType;  差异内容：static getTemperatureType(): TemperatureType; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：System；  API声明：static getTemperatureName(type: TemperatureType): string;  差异内容：static getTemperatureName(type: TemperatureType): string; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：System；  API声明：static getFirstDayOfWeek(): WeekDay;  差异内容：static getFirstDayOfWeek(): WeekDay; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：I18NUtil；  API声明：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string;  差异内容：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NumberFormat；  API声明：formatRange(startRange: number, endRange: number): string;  差异内容：formatRange(startRange: number, endRange: number): string; | api/@ohos.intl.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResourceManager；  API声明：getIntPluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string;  差异内容：getIntPluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResourceManager；  API声明：getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;  差异内容：getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResourceManager；  API声明：getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string;  差异内容：getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResourceManager；  API声明：getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string;  差异内容：getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResourceManager；  API声明：getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;  差异内容：getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResourceManager；  API声明：getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string;  差异内容：getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NumberOptions；  API声明：roundingPriority?: string;  差异内容：roundingPriority?: string; | api/@ohos.intl.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NumberOptions；  API声明：roundingIncrement?: number;  差异内容：roundingIncrement?: number; | api/@ohos.intl.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NumberOptions；  API声明：roundingMode?: string;  差异内容：roundingMode?: string; | api/@ohos.intl.d.ts |
