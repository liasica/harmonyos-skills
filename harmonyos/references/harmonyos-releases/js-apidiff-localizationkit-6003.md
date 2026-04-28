---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-localizationkit-6003
title: Localization Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Localization Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:47fad9ac2bc9ce448d43ebd6bf96eb7eba4502cd369f3c43226e845199507c6a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API跨平台权限变更 | 类名：System；  API声明：static setAppPreferredLanguage(language: string): void;  差异内容：NA | 类名：System；  API声明：static setAppPreferredLanguage(language: string): void;  差异内容：crossplatform | api/@ohos.i18n.d.ts |
| API跨平台权限变更 | 类名：System；  API声明：static getAppPreferredLanguage(): string;  差异内容：NA | 类名：System；  API声明：static getAppPreferredLanguage(): string;  差异内容：crossplatform | api/@ohos.i18n.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export interface LocaleOptions  差异内容：NA | 类名：intl；  API声明：export interface LocaleOptions  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export class Locale  差异内容：NA | 类名：intl；  API声明：export class Locale  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export interface DateTimeOptions  差异内容：NA | 类名：intl；  API声明：export interface DateTimeOptions  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：locale?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：locale?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：dateStyle?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：dateStyle?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：timeStyle?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：timeStyle?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：hourCycle?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：hourCycle?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：timeZone?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：timeZone?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：numberingSystem?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：numberingSystem?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：hour12?: boolean;  差异内容：NA | 类名：DateTimeOptions；  API声明：hour12?: boolean;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：weekday?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：weekday?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：era?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：era?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：year?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：year?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：month?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：month?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：day?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：day?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：hour?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：hour?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：minute?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：minute?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：second?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：second?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：timeZoneName?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：timeZoneName?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：dayPeriod?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：dayPeriod?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeOptions；  API声明：formatMatcher?: string;  差异内容：NA | 类名：DateTimeOptions；  API声明：formatMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export class DateTimeFormat  差异内容：NA | 类名：intl；  API声明：export class DateTimeFormat  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeFormat；  API声明：format(date: Date): string;  差异内容：NA | 类名：DateTimeFormat；  API声明：format(date: Date): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeFormat；  API声明：formatRange(startDate: Date, endDate: Date): string;  差异内容：NA | 类名：DateTimeFormat；  API声明：formatRange(startDate: Date, endDate: Date): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeFormat；  API声明：resolvedOptions(): DateTimeOptions;  差异内容：NA | 类名：DateTimeFormat；  API声明：resolvedOptions(): DateTimeOptions;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export interface PluralRulesOptions  差异内容：NA | 类名：intl；  API声明：export interface PluralRulesOptions  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：PluralRulesOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：type?: string;  差异内容：NA | 类名：PluralRulesOptions；  API声明：type?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：minimumIntegerDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：minimumIntegerDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：minimumFractionDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：minimumFractionDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：maximumFractionDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：maximumFractionDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：minimumSignificantDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：minimumSignificantDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：maximumSignificantDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：maximumSignificantDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export class PluralRules  差异内容：NA | 类名：intl；  API声明：export class PluralRules  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRules；  API声明：select(n: number): string;  差异内容：NA | 类名：PluralRules；  API声明：select(n: number): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export interface RelativeTimeFormatInputOptions  差异内容：NA | 类名：intl；  API声明：export interface RelativeTimeFormatInputOptions  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatInputOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：RelativeTimeFormatInputOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatInputOptions；  API声明：numeric?: string;  差异内容：NA | 类名：RelativeTimeFormatInputOptions；  API声明：numeric?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatInputOptions；  API声明：style?: string;  差异内容：NA | 类名：RelativeTimeFormatInputOptions；  API声明：style?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export interface RelativeTimeFormatResolvedOptions  差异内容：NA | 类名：intl；  API声明：export interface RelativeTimeFormatResolvedOptions  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：locale: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：locale: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：style: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：style: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：numeric: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：numeric: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：numberingSystem: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：numberingSystem: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：intl；  API声明：export class RelativeTimeFormat  差异内容：NA | 类名：intl；  API声明：export class RelativeTimeFormat  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormat；  API声明：format(value: number, unit: string): string;  差异内容：NA | 类名：RelativeTimeFormat；  API声明：format(value: number, unit: string): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormat；  API声明：formatToParts(value: number, unit: string): Array<object>;  差异内容：NA | 类名：RelativeTimeFormat；  API声明：formatToParts(value: number, unit: string): Array<object>;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormat；  API声明：resolvedOptions(): RelativeTimeFormatResolvedOptions;  差异内容：NA | 类名：RelativeTimeFormat；  API声明：resolvedOptions(): RelativeTimeFormatResolvedOptions;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：resourceManager；  API声明：export function getSystemResourceManager(): ResourceManager;  差异内容：NA | 类名：resourceManager；  API声明：export function getSystemResourceManager(): ResourceManager;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringValue(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getStringValue(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringValue(resource: Resource): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getStringValue(resource: Resource): Promise<string>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource, callback: \_AsyncCallback<Array<string>>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource, callback: \_AsyncCallback<Array<string>>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource): Promise<Array<string>>;  差异内容：NA | 类名：ResourceManager；  API声明：getStringArrayValue(resource: Resource): Promise<Array<string>>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, density: number, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, density: number, callback: \_AsyncCallback<Uint8Array>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource): Promise<Uint8Array>;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource): Promise<Uint8Array>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, density: number): Promise<Uint8Array>;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContent(resource: Resource, density: number): Promise<Uint8Array>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, callback: \_AsyncCallback<string>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, density: number, callback: \_AsyncCallback<string>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, density: number, callback: \_AsyncCallback<string>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource): Promise<string>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, density: number): Promise<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64(resource: Resource, density: number): Promise<string>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringSync(resource: Resource): string;  差异内容：NA | 类名：ResourceManager；  API声明：getStringSync(resource: Resource): string;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringSync(resource: Resource, ...args: Array<string | number>): string;  差异内容：NA | 类名：ResourceManager；  API声明：getStringSync(resource: Resource, ...args: Array<string | number>): string;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getBoolean(resource: Resource): boolean;  差异内容：NA | 类名：ResourceManager；  API声明：getBoolean(resource: Resource): boolean;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getNumber(resource: Resource): number;  差异内容：NA | 类名：ResourceManager；  API声明：getNumber(resource: Resource): number;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;  差异内容：NA | 类名：ResourceManager；  API声明：getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;  差异内容：NA | 类名：ResourceManager；  API声明：getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor;  差异内容：NA | 类名：ResourceManager；  API声明：getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getColor(resource: Resource, callback: \_AsyncCallback<number>): void;  差异内容：NA | 类名：ResourceManager；  API声明：getColor(resource: Resource, callback: \_AsyncCallback<number>): void;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getColor(resource: Resource): Promise<number>;  差异内容：NA | 类名：ResourceManager；  API声明：getColor(resource: Resource): Promise<number>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getColorSync(resource: Resource): number;  差异内容：NA | 类名：ResourceManager；  API声明：getColorSync(resource: Resource): number;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContentSync(resource: Resource, density?: number): Uint8Array;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentSync(resource: Resource, density?: number): Uint8Array;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getMediaContentBase64Sync(resource: Resource, density?: number): string;  差异内容：NA | 类名：ResourceManager；  API声明：getMediaContentBase64Sync(resource: Resource, density?: number): string;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getStringArrayValueSync(resource: Resource): Array<string>;  差异内容：NA | 类名：ResourceManager；  API声明：getStringArrayValueSync(resource: Resource): Array<string>;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：ResourceManager；  API声明：getSymbol(resource: Resource): number;  差异内容：NA | 类名：ResourceManager；  API声明：getSymbol(resource: Resource): number;  差异内容：20 | api/@ohos.resourceManager.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：localeMatcher?: string;  差异内容：20 | 类名：CollatorOptions；  API声明：localeMatcher?: string;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：usage?: string;  差异内容：20 | 类名：CollatorOptions；  API声明：usage?: string;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：sensitivity?: string;  差异内容：20 | 类名：CollatorOptions；  API声明：sensitivity?: string;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：ignorePunctuation?: boolean;  差异内容：20 | 类名：CollatorOptions；  API声明：ignorePunctuation?: boolean;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：collation?: string;  差异内容：20 | 类名：CollatorOptions；  API声明：collation?: string;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：numeric?: boolean;  差异内容：20 | 类名：CollatorOptions；  API声明：numeric?: boolean;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：caseFirst?: string;  差异内容：20 | 类名：CollatorOptions；  API声明：caseFirst?: string;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Collator；  API声明：compare(first: string, second: string): number;  差异内容：20 | 类名：Collator；  API声明：compare(first: string, second: string): number;  差异内容：NA | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Collator；  API声明：resolvedOptions(): CollatorOptions;  差异内容：20 | 类名：Collator；  API声明：resolvedOptions(): CollatorOptions;  差异内容：NA | api/@ohos.intl.d.ts |
| 函数变更 | 类名：PhoneNumberFormat；  API声明：isValidNumber(number: string): boolean;  差异内容：number: string | 类名：PhoneNumberFormat；  API声明：isValidNumber(phoneNumber: string): boolean;  差异内容：phoneNumber: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：PhoneNumberFormat；  API声明：format(number: string): string;  差异内容：number: string | 类名：PhoneNumberFormat；  API声明：format(phoneNumber: string): string;  差异内容：phoneNumber: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：PhoneNumberFormat；  API声明：getLocationName(number: string, locale: string): string;  差异内容：number: string, locale: string | 类名：PhoneNumberFormat；  API声明：getLocationName(phoneNumber: string, locale: string): string;  差异内容：phoneNumber: string, locale: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isDigit(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isDigit(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isSpaceChar(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isSpaceChar(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isWhitespace(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isWhitespace(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isRTL(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isRTL(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isIdeograph(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isIdeograph(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isLetter(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isLetter(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isLowerCase(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isLowerCase(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：isUpperCase(char: string): boolean;  差异内容：char: string | 类名：Character；  API声明：isUpperCase(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Character；  API声明：getType(char: string): string;  差异内容：char: string | 类名：Character；  API声明：getType(ch: string): string;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isDigit(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isDigit(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isSpaceChar(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isSpaceChar(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isWhitespace(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isWhitespace(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isRTL(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isRTL(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isIdeograph(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isIdeograph(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isLetter(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isLetter(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isLowerCase(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isLowerCase(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static isUpperCase(char: string): boolean;  差异内容：char: string | 类名：Unicode；  API声明：static isUpperCase(ch: string): boolean;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：Unicode；  API声明：static getType(char: string): string;  差异内容：char: string | 类名：Unicode；  API声明：static getType(ch: string): string;  差异内容：ch: string | api/@ohos.i18n.d.ts |
| 函数变更 | 类名：NumberFormat；  API声明：format(number: number): string;  差异内容：number: number | 类名：NumberFormat；  API声明：format(num: number): string;  差异内容：num: number | api/@ohos.intl.d.ts |
| 新增API | NA | 类名：resourceManager；  API声明：export function getSysResourceManager(): ResourceManager;  差异内容：export function getSysResourceManager(): ResourceManager; | api/@ohos.resourceManager.d.ts |
