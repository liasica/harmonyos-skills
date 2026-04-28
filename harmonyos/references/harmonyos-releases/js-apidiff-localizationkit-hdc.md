---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-localizationkit-hdc
title: Localization Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Localization Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8c1c1e39a3e7afe8bfc457a30db4cfc8d33b589622ecc654a0fe916abd875a4c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：ResourceManager；  API声明：getStringValue(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getStringValue(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getStringValue(resource: Resource): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getStringValue(resource: Resource): Promise<string>;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource, callback: \_AsyncCallback<Array<string>>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource, callback: \_AsyncCallback<Array<string>>): void;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource): Promise<Array<string>>;  差异内容：NA | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource): Promise<Array<string>>;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource): Promise<Uint8Array>;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource): Promise<Uint8Array>;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource): Promise<string>;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number, callback: \_AsyncCallback<string>): void;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getPluralStringValue(resource: Resource, num: number): Promise<string>;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getStringSync(resource: Resource): string;  差异内容：NA | 类名：ResourceManager；  API声明：getStringSync(resource: Resource): string;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getBoolean(resource: Resource): boolean;  差异内容：NA | 类名：ResourceManager；  API声明：getBoolean(resource: Resource): boolean;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API模型切换 | 类名：ResourceManager；  API声明：getNumber(resource: Resource): number;  差异内容：NA | 类名：ResourceManager；  API声明：getNumber(resource: Resource): number;  差异内容：stagemodelonly | api/@ohos.resourceManager.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare namespace i18n  差异内容：NA | 类名：global；  API声明： declare namespace i18n  差异内容：form | api/@ohos.i18n.d.ts |
| API卡片权限变更 | 类名：i18n；  API声明： export class System  差异内容：NA | 类名：i18n；  API声明： export class System  差异内容：form | api/@ohos.i18n.d.ts |
| API卡片权限变更 | 类名：System；  API声明：static getSystemLanguage(): string;  差异内容：NA | 类名：System；  API声明：static getSystemLanguage(): string;  差异内容：form | api/@ohos.i18n.d.ts |
| API卡片权限变更 | 类名：System；  API声明：static is24HourClock(): boolean;  差异内容：NA | 类名：System；  API声明：static is24HourClock(): boolean;  差异内容：form | api/@ohos.i18n.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare namespace intl  差异内容：NA | 类名：global；  API声明： declare namespace intl  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：intl；  API声明： export interface LocaleOptions  差异内容：NA | 类名：intl；  API声明： export interface LocaleOptions  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：LocaleOptions；  API声明：calendar?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：calendar?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：LocaleOptions；  API声明：collation?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：collation?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：LocaleOptions；  API声明：hourCycle?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：hourCycle?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：LocaleOptions；  API声明：numberingSystem?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：numberingSystem?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：LocaleOptions；  API声明：numeric?: boolean;  差异内容：NA | 类名：LocaleOptions；  API声明：numeric?: boolean;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：LocaleOptions；  API声明：caseFirst?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：caseFirst?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：intl；  API声明： export class Locale  差异内容：NA | 类名：intl；  API声明： export class Locale  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：language: string;  差异内容：NA | 类名：Locale；  API声明：language: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：script: string;  差异内容：NA | 类名：Locale；  API声明：script: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：region: string;  差异内容：NA | 类名：Locale；  API声明：region: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：baseName: string;  差异内容：NA | 类名：Locale；  API声明：baseName: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：caseFirst: string;  差异内容：NA | 类名：Locale；  API声明：caseFirst: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：calendar: string;  差异内容：NA | 类名：Locale；  API声明：calendar: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：collation: string;  差异内容：NA | 类名：Locale；  API声明：collation: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：hourCycle: string;  差异内容：NA | 类名：Locale；  API声明：hourCycle: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：numberingSystem: string;  差异内容：NA | 类名：Locale；  API声明：numberingSystem: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：numeric: boolean;  差异内容：NA | 类名：Locale；  API声明：numeric: boolean;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：toString(): string;  差异内容：NA | 类名：Locale；  API声明：toString(): string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：maximize(): Locale;  差异内容：NA | 类名：Locale；  API声明：maximize(): Locale;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：Locale；  API声明：minimize(): Locale;  差异内容：NA | 类名：Locale；  API声明：minimize(): Locale;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：intl；  API声明： export interface DateTimeOptions  差异内容：NA | 类名：intl；  API声明： export interface DateTimeOptions  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：locale?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：locale?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：dateStyle?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：dateStyle?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：timeStyle?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：timeStyle?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：hourCycle?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：hourCycle?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：timeZone?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：timeZone?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：numberingSystem?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：numberingSystem?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：hour12?: boolean;  差异内容：NA | 类名：DateTimeOptions；  API声明：hour12?: boolean;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：weekday?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：weekday?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：era?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：era?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：year?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：year?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：month?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：month?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：day?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：day?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：hour?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：hour?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：minute?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：minute?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：second?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：second?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：timeZoneName?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：timeZoneName?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：dayPeriod?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：dayPeriod?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：localeMatcher?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeOptions；  API声明：formatMatcher?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：formatMatcher?: string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：intl；  API声明： export class DateTimeFormat  差异内容：NA | 类名：intl；  API声明： export class DateTimeFormat  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeFormat；  API声明：format(date: Date): string;  差异内容：NA | 类名：DateTimeFormat；  API声明：format(date: Date): string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeFormat；  API声明：formatRange(startDate: Date, endDate: Date): string;  差异内容：NA | 类名：DateTimeFormat；  API声明：formatRange(startDate: Date, endDate: Date): string;  差异内容：form | api/@ohos.intl.d.ts |
| API卡片权限变更 | 类名：DateTimeFormat；  API声明：resolvedOptions(): DateTimeOptions;  差异内容：NA | 类名：DateTimeFormat；  API声明：resolvedOptions(): DateTimeOptions;  差异内容：form | api/@ohos.intl.d.ts |
| 新增API | NA | 类名：System；  API声明：static setAppPreferredLanguage(language: string): void;  差异内容：static setAppPreferredLanguage(language: string): void; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：I18NUtil；  API声明：static getTimePeriodName(hour: number, locale?: string): string;  差异内容：static getTimePeriodName(hour: number, locale?: string): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：I18NUtil；  API声明：static getBestMatchLocale(locale: string, localeList: string[]): string;  差异内容：static getBestMatchLocale(locale: string, localeList: string[]): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：I18NUtil；  API声明：static getThreeLetterLanguage(locale: string): string;  差异内容：static getThreeLetterLanguage(locale: string): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：I18NUtil；  API声明：static getThreeLetterRegion(locale: string): string;  差异内容：static getThreeLetterRegion(locale: string): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：Calendar；  API声明：add(field: string, amount: number): void;  差异内容：add(field: string, amount: number): void; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：Calendar；  API声明：getTimeInMillis(): number;  差异内容：getTimeInMillis(): number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：Calendar；  API声明：compareDays(date: Date): number;  差异内容：compareDays(date: Date): number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：TimeZone；  API声明：static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>;  差异内容：static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export enum NormalizerMode  差异内容： export enum NormalizerMode | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：NormalizerMode；  API声明：NFC = 1  差异内容：NFC = 1 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：NormalizerMode；  API声明：NFD = 2  差异内容：NFD = 2 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：NormalizerMode；  API声明：NFKC = 3  差异内容：NFKC = 3 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：NormalizerMode；  API声明：NFKD = 4  差异内容：NFKD = 4 | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export class Normalizer  差异内容： export class Normalizer | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：Normalizer；  API声明：static getInstance(mode: NormalizerMode): Normalizer;  差异内容：static getInstance(mode: NormalizerMode): Normalizer; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：Normalizer；  API声明：normalize(text: string): string;  差异内容：normalize(text: string): string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export interface HolidayInfoItem  差异内容： export interface HolidayInfoItem | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayInfoItem；  API声明：baseName: string;  差异内容：baseName: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayInfoItem；  API声明：year: number;  差异内容：year: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayInfoItem；  API声明：month: number;  差异内容：month: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayInfoItem；  API声明：day: number;  差异内容：day: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayInfoItem；  API声明：localNames?: Array<HolidayLocalName>;  差异内容：localNames?: Array<HolidayLocalName>; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export interface HolidayLocalName  差异内容： export interface HolidayLocalName | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayLocalName；  API声明：language: string;  差异内容：language: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayLocalName；  API声明：name: string;  差异内容：name: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export class HolidayManager  差异内容： export class HolidayManager | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayManager；  API声明：isHoliday(date?: Date): boolean;  差异内容：isHoliday(date?: Date): boolean; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：HolidayManager；  API声明：getHolidayInfoItemArray(year?: number): Array<HolidayInfoItem>;  差异内容：getHolidayInfoItemArray(year?: number): Array<HolidayInfoItem>; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export interface EntityInfoItem  差异内容： export interface EntityInfoItem | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：EntityInfoItem；  API声明：begin: number;  差异内容：begin: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：EntityInfoItem；  API声明：end: number;  差异内容：end: number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：EntityInfoItem；  API声明：type: string;  差异内容：type: string; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明： export class EntityRecognizer  差异内容： export class EntityRecognizer | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：EntityRecognizer；  API声明：findEntityInfo(text: string): Array<EntityInfoItem>;  差异内容：findEntityInfo(text: string): Array<EntityInfoItem>; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, density: number, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：getMediaContent(resource: Resource, density: number, callback: \_AsyncCallback<Uint8Array>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, density: number): Promise<Uint8Array>;  差异内容：getMediaContent(resource: Resource, density: number): Promise<Uint8Array>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContent(resId: number, density: number, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：getMediaContent(resId: number, density: number, callback: \_AsyncCallback<Uint8Array>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContent(resId: number, density: number): Promise<Uint8Array>;  差异内容：getMediaContent(resId: number, density: number): Promise<Uint8Array>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, density: number, callback: \_AsyncCallback<string>): void;  差异内容：getMediaContentBase64(resource: Resource, density: number, callback: \_AsyncCallback<string>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, density: number): Promise<string>;  差异内容：getMediaContentBase64(resource: Resource, density: number): Promise<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resId: number, density: number, callback: \_AsyncCallback<string>): void;  差异内容：getMediaContentBase64(resId: number, density: number, callback: \_AsyncCallback<string>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resId: number, density: number): Promise<string>;  差异内容：getMediaContentBase64(resId: number, density: number): Promise<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaByName(resName: string, density: number, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：getMediaByName(resName: string, density: number, callback: \_AsyncCallback<Uint8Array>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaByName(resName: string, density: number): Promise<Uint8Array>;  差异内容：getMediaByName(resName: string, density: number): Promise<Uint8Array>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaBase64ByName(resName: string, density: number, callback: \_AsyncCallback<string>): void;  差异内容：getMediaBase64ByName(resName: string, density: number, callback: \_AsyncCallback<string>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaBase64ByName(resName: string, density: number): Promise<string>;  差异内容：getMediaBase64ByName(resName: string, density: number): Promise<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getStringSync(resId: number, ...args: Array<string | number>): string;  差异内容：getStringSync(resId: number, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getStringSync(resource: Resource, ...args: Array<string | number>): string;  差异内容：getStringSync(resource: Resource, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getStringByNameSync(resName: string, ...args: Array<string | number>): string;  差异内容：getStringByNameSync(resName: string, ...args: Array<string | number>): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DEVICE\_TYPE\_2IN1 = 0x07  差异内容：DEVICE\_TYPE\_2IN1 = 0x07 | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：resourceManager；  API声明： export enum ColorMode  差异内容： export enum ColorMode | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ColorMode；  API声明：DARK = 0  差异内容：DARK = 0 | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ColorMode；  API声明：LIGHT = 1  差异内容：LIGHT = 1 | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：deviceType: DeviceType;  差异内容：deviceType: DeviceType; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：screenDensity: ScreenDensity;  差异内容：screenDensity: ScreenDensity; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：colorMode: ColorMode;  差异内容：colorMode: ColorMode; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：mcc: number;  差异内容：mcc: number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：mnc: number;  差异内容：mnc: number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：resourceManager；  API声明：export function getSystemResourceManager(): ResourceManager;  差异内容：export function getSystemResourceManager(): ResourceManager; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor;  差异内容：getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor;  差异内容：getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor;  差异内容：getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getRawFileList(path: string, callback: \_AsyncCallback<Array<string>>): void;  差异内容：getRawFileList(path: string, callback: \_AsyncCallback<Array<string>>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getRawFileList(path: string): Promise<Array<string>>;  差异内容：getRawFileList(path: string): Promise<Array<string>>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColor(resId: number, callback: \_AsyncCallback<number>): void;  差异内容：getColor(resId: number, callback: \_AsyncCallback<number>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColor(resId: number): Promise<number>;  差异内容：getColor(resId: number): Promise<number>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColor(resource: Resource, callback: \_AsyncCallback<number>): void;  差异内容：getColor(resource: Resource, callback: \_AsyncCallback<number>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColor(resource: Resource): Promise<number>;  差异内容：getColor(resource: Resource): Promise<number>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColorByName(resName: string, callback: \_AsyncCallback<number>): void;  差异内容：getColorByName(resName: string, callback: \_AsyncCallback<number>): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColorByName(resName: string): Promise<number>;  差异内容：getColorByName(resName: string): Promise<number>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColorSync(resId: number): number;  差异内容：getColorSync(resId: number): number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColorSync(resource: Resource): number;  差异内容：getColorSync(resource: Resource): number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getColorByNameSync(resName: string): number;  差异内容：getColorByNameSync(resName: string): number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：addResource(path: string): void;  差异内容：addResource(path: string): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：removeResource(path: string): void;  差异内容：removeResource(path: string): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getRawFdSync(path: string): RawFileDescriptor;  差异内容：getRawFdSync(path: string): RawFileDescriptor; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：closeRawFdSync(path: string): void;  差异内容：closeRawFdSync(path: string): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getRawFileListSync(path: string): Array<string>;  差异内容：getRawFileListSync(path: string): Array<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getRawFileContentSync(path: string): Uint8Array;  差异内容：getRawFileContentSync(path: string): Uint8Array; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentSync(resId: number, density?: number): Uint8Array;  差异内容：getMediaContentSync(resId: number, density?: number): Uint8Array; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentSync(resource: Resource, density?: number): Uint8Array;  差异内容：getMediaContentSync(resource: Resource, density?: number): Uint8Array; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentBase64Sync(resId: number, density?: number): string;  差异内容：getMediaContentBase64Sync(resId: number, density?: number): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaContentBase64Sync(resource: Resource, density?: number): string;  差异内容：getMediaContentBase64Sync(resource: Resource, density?: number): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getPluralStringValueSync(resId: number, num: number): string;  差异内容：getPluralStringValueSync(resId: number, num: number): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getPluralStringValueSync(resource: Resource, num: number): string;  差异内容：getPluralStringValueSync(resource: Resource, num: number): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getStringArrayValueSync(resId: number): Array<string>;  差异内容：getStringArrayValueSync(resId: number): Array<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getStringArrayValueSync(resource: Resource): Array<string>;  差异内容：getStringArrayValueSync(resource: Resource): Array<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getPluralStringByNameSync(resName: string, num: number): string;  差异内容：getPluralStringByNameSync(resName: string, num: number): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaByNameSync(resName: string, density?: number): Uint8Array;  差异内容：getMediaByNameSync(resName: string, density?: number): Uint8Array; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getMediaBase64ByNameSync(resName: string, density?: number): string;  差异内容：getMediaBase64ByNameSync(resName: string, density?: number): string; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getStringArrayByNameSync(resName: string): Array<string>;  差异内容：getStringArrayByNameSync(resName: string): Array<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getConfigurationSync(): Configuration;  差异内容：getConfigurationSync(): Configuration; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getDeviceCapabilitySync(): DeviceCapability;  差异内容：getDeviceCapabilitySync(): DeviceCapability; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getLocales(includeSystem?: boolean): Array<string>;  差异内容：getLocales(includeSystem?: boolean): Array<string>; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getSymbol(resId: number): number;  差异内容：getSymbol(resId: number): number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getSymbol(resource: Resource): number;  差异内容：getSymbol(resource: Resource): number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getSymbolByName(resName: string): number;  差异内容：getSymbolByName(resName: string): number; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：isRawDir(path: string): boolean;  差异内容：isRawDir(path: string): boolean; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getOverrideResourceManager(configuration?: Configuration): ResourceManager;  差异内容：getOverrideResourceManager(configuration?: Configuration): ResourceManager; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：getOverrideConfiguration(): Configuration;  差异内容：getOverrideConfiguration(): Configuration; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：ResourceManager；  API声明：updateOverrideConfiguration(configuration: Configuration): void;  差异内容：updateOverrideConfiguration(configuration: Configuration): void; | api/@ohos.resourceManager.d.ts |
| 新增API | NA | 类名：Resource；  API声明：params?: any[];  差异内容：params?: any[]; | api/global/resource.d.ts |
| 新增API | NA | 类名：Resource；  API声明：type?: number;  差异内容：type?: number; | api/global/resource.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace sendableResourceManager  差异内容： declare namespace sendableResourceManager | api/@ohos.sendableResourceManager.d.ets |
| 新增API | NA | 类名：sendableResourceManager；  API声明：export function resourceToSendableResource(resource: Resource): SendableResource;  差异内容：export function resourceToSendableResource(resource: Resource): SendableResource; | api/@ohos.sendableResourceManager.d.ets |
| 新增API | NA | 类名：sendableResourceManager；  API声明：export function sendableResourceToResource(resource: SendableResource): Resource;  差异内容：export function sendableResourceToResource(resource: SendableResource): Resource; | api/@ohos.sendableResourceManager.d.ets |
| 新增API | NA | 类名：sendableResourceManager；  API声明：export type Resource = \_Resource;  差异内容：export type Resource = \_Resource; | api/@ohos.sendableResourceManager.d.ets |
| 新增API | NA | 类名：sendableResourceManager；  API声明：export type SendableResource = \_SendableResource;  差异内容：export type SendableResource = \_SendableResource; | api/@ohos.sendableResourceManager.d.ets |
| 新增API | NA | 类名：global；  API声明： interface SendableResource  差异内容： interface SendableResource | api/global/sendableResource.d.ets |
| 新增API | NA | 类名：SendableResource；  API声明：bundleName: string;  差异内容：bundleName: string; | api/global/sendableResource.d.ets |
| 新增API | NA | 类名：SendableResource；  API声明：moduleName: string;  差异内容：moduleName: string; | api/global/sendableResource.d.ets |
| 新增API | NA | 类名：SendableResource；  API声明：id: number;  差异内容：id: number; | api/global/sendableResource.d.ets |
| 新增API | NA | 类名：SendableResource；  API声明：params?: collections.Array<string | number>;  差异内容：params?: collections.Array<string | number>; | api/global/sendableResource.d.ets |
| 新增API | NA | 类名：SendableResource；  API声明：type?: number;  差异内容：type?: number; | api/global/sendableResource.d.ets |
