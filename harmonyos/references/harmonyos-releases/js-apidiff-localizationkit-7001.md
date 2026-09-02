---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-localizationkit-7001
title: Localization Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Localization Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:e4b1b71b8d8d537cd89896bc772012caa8b9292e590321ffae0acbbd5c64e5dd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：I18NUtil；  API声明：static convertCanonicalLocaleIdentifier(locale: string): string;  差异内容：static convertCanonicalLocaleIdentifier(locale: string): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：I18NUtil；  API声明：static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string;  差异内容：static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：Unicode；  API声明：static detectEncoding(bytes: Uint8Array): EncodingInfo;  差异内容：static detectEncoding(bytes: Uint8Array): EncodingInfo; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface EncodingInfo  差异内容：export interface EncodingInfo | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：EncodingInfo；  API声明：encodingName: string;  差异内容：encodingName: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：EncodingInfo；  API声明：confidence: number;  差异内容：confidence: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TimeZone；  API声明：public isDaylightSavingTime(date: Date): boolean;  差异内容：public isDaylightSavingTime(date: Date): boolean; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TimeZone；  API声明：static setAppDefaultTimeZoneById(zoneID: string): void;  差异内容：static setAppDefaultTimeZoneById(zoneID: string): void; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TimeZone；  API声明：static getAppDefaultTimeZone(): TimeZone;  差异内容：static getAppDefaultTimeZone(): TimeZone; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class SymbolDateTimeFormat  差异内容：export class SymbolDateTimeFormat | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolDateTimeFormat；  API声明：public format(date?: Date | number): string;  差异内容：public format(date?: Date | number): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolDateTimeFormat；  API声明：public formatRange(startDate: Date | number | bigint, endDate: Date | number | bigint): string;  差异内容：public formatRange(startDate: Date | number | bigint, endDate: Date | number | bigint): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolDateTimeFormat；  API声明：public formatRangeToParts(startDate: Date | number | bigint, endDate: Date | number | bigint): Intl.DateTimeRangeFormatPart[];  差异内容：public formatRangeToParts(startDate: Date | number | bigint, endDate: Date | number | bigint): Intl.DateTimeRangeFormatPart[]; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolDateTimeFormat；  API声明：public formatToParts(date?: Date | number): Intl.DateTimeFormatPart[];  差异内容：public formatToParts(date?: Date | number): Intl.DateTimeFormatPart[]; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolDateTimeFormat；  API声明：public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions;  差异内容：public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface SymbolDateTimeFormatOptions  差异内容：export interface SymbolDateTimeFormatOptions | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolDateTimeFormatOptions；  API声明：amPMSymbol?: string[] | undefined;  差异内容：amPMSymbol?: string[] | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface ResolvedSymbolDateTimeFormatOptions  差异内容：export interface ResolvedSymbolDateTimeFormatOptions | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolDateTimeFormatOptions；  API声明：amPMSymbol?: string[];  差异内容：amPMSymbol?: string[]; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class SymbolNumberFormat  差异内容：export class SymbolNumberFormat | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormat；  API声明：public format(value: number | bigint): string;  差异内容：public format(value: number | bigint): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormat；  API声明：public formatRange(startRange: number, endRange: number): string;  差异内容：public formatRange(startRange: number, endRange: number): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormat；  API声明：public formatToParts(value?: number | bigint): Intl.NumberFormatPart[];  差异内容：public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormat；  API声明：public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[];  差异内容：public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormat；  API声明：public resolvedOptions(): ResolvedSymbolNumberFormatOptions;  差异内容：public resolvedOptions(): ResolvedSymbolNumberFormatOptions; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface SymbolNumberFormatOptions  差异内容：export interface SymbolNumberFormatOptions | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormatOptions；  API声明：zero?: string | undefined;  差异内容：zero?: string | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormatOptions；  API声明：nan?: string | undefined;  差异内容：nan?: string | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormatOptions；  API声明：minusSign?: string | undefined;  差异内容：minusSign?: string | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormatOptions；  API声明：plusSign?: string | undefined;  差异内容：plusSign?: string | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormatOptions；  API声明：infinity?: string | undefined;  差异内容：infinity?: string | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：SymbolNumberFormatOptions；  API声明：groupingSeparator?: string | undefined;  差异内容：groupingSeparator?: string | undefined; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface ResolvedSymbolNumberFormatOptions  差异内容：export interface ResolvedSymbolNumberFormatOptions | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolNumberFormatOptions；  API声明：zero?: string;  差异内容：zero?: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolNumberFormatOptions；  API声明：nan?: string;  差异内容：nan?: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolNumberFormatOptions；  API声明：minusSign?: string;  差异内容：minusSign?: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolNumberFormatOptions；  API声明：plusSign?: string;  差异内容：plusSign?: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolNumberFormatOptions；  API声明：infinity?: string;  差异内容：infinity?: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResolvedSymbolNumberFormatOptions；  API声明：groupingSeparator?: string;  差异内容：groupingSeparator?: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class ISO8601DateTimeFormat  差异内容：export class ISO8601DateTimeFormat | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ISO8601DateTimeFormat；  API声明：public format(date: Date): string;  差异内容：public format(date: Date): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface ISO8601DateTimeFormatOptions  差异内容：export interface ISO8601DateTimeFormatOptions | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ISO8601DateTimeFormatOptions；  API声明：dateFormat?: 'calendar' | 'ordinal' | 'week';  差异内容：dateFormat?: 'calendar' | 'ordinal' | 'week'; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ISO8601DateTimeFormatOptions；  API声明：timePrecision?: 'dateOnly' | 'hours' | 'minutes' | 'seconds' | 'milliSeconds';  差异内容：timePrecision?: 'dateOnly' | 'hours' | 'minutes' | 'seconds' | 'milliSeconds'; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ISO8601DateTimeFormatOptions；  API声明：separatorStyle?: 'extended' | 'basic';  差异内容：separatorStyle?: 'extended' | 'basic'; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ISO8601DateTimeFormatOptions；  API声明：timeZone?: TimeZone;  差异内容：timeZone?: TimeZone; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ISO8601DateTimeFormatOptions；  API声明：displayTimeZone?: boolean;  差异内容：displayTimeZone?: boolean; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar;  差异内容：export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class ChineseCalendar  差异内容：export class ChineseCalendar | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendar；  API声明：public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void;  差异内容：public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendar；  API声明：public static checkLeapMonth(gregorianYear: number, cyclicalYear: number, month: number): boolean;  差异内容：public static checkLeapMonth(gregorianYear: number, cyclicalYear: number, month: number): boolean; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export interface ChineseCalendarTime  差异内容：export interface ChineseCalendarTime | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：gregorianYear: number;  差异内容：gregorianYear: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：cyclicalYear: number;  差异内容：cyclicalYear: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：month: number;  差异内容：month: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：date: number;  差异内容：date: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：isLeapMonth?: boolean;  差异内容：isLeapMonth?: boolean; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：hour?: number;  差异内容：hour?: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：minute?: number;  差异内容：minute?: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ChineseCalendarTime；  API声明：second?: number;  差异内容：second?: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getResourceName(resId: number): string;  差异内容：getResourceName(resId: number): string; | api/@ohos.resourceManager.d.ts |
