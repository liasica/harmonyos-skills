---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-localizationkit-6001
title: Localization Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Localization Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7fadce076787e5eb6587a53673ac606f595cb1415d343c09d7cd072fe552a475
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：System；  API声明：static getSystemLocale(): string;  差异内容：NA | 类名：System；  API声明：static getSystemLocale(): string;  差异内容：20 | api/@ohos.i18n.d.ts |
| API废弃版本变更 | 类名：I18NUtil；  API声明：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string;  差异内容：NA | 类名：I18NUtil；  API声明：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string;  差异内容：20 | api/@ohos.i18n.d.ts |
| API废弃版本变更 | 类名：i18n；  API声明：export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat;  差异内容：NA | 类名：i18n；  API声明：export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat;  差异内容：20 | api/@ohos.i18n.d.ts |
| API废弃版本变更 | 类名：i18n；  API声明：export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat;  差异内容：NA | 类名：i18n；  API声明：export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat;  差异内容：20 | api/@ohos.i18n.d.ts |
| API废弃版本变更 | 类名：i18n；  API声明：export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat;  差异内容：NA | 类名：i18n；  API声明：export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat;  差异内容：20 | api/@ohos.i18n.d.ts |
| API废弃版本变更 | 类名：LocaleOptions；  API声明：calendar?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：calendar?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：LocaleOptions；  API声明：collation?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：collation?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：LocaleOptions；  API声明：hourCycle?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：hourCycle?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：LocaleOptions；  API声明：numberingSystem?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：numberingSystem?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：LocaleOptions；  API声明：numeric?: boolean;  差异内容：NA | 类名：LocaleOptions；  API声明：numeric?: boolean;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：LocaleOptions；  API声明：caseFirst?: string;  差异内容：NA | 类名：LocaleOptions；  API声明：caseFirst?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：language: string;  差异内容：NA | 类名：Locale；  API声明：language: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：script: string;  差异内容：NA | 类名：Locale；  API声明：script: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：region: string;  差异内容：NA | 类名：Locale；  API声明：region: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：baseName: string;  差异内容：NA | 类名：Locale；  API声明：baseName: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：caseFirst: string;  差异内容：NA | 类名：Locale；  API声明：caseFirst: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：calendar: string;  差异内容：NA | 类名：Locale；  API声明：calendar: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：collation: string;  差异内容：NA | 类名：Locale；  API声明：collation: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：hourCycle: string;  差异内容：NA | 类名：Locale；  API声明：hourCycle: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：numberingSystem: string;  差异内容：NA | 类名：Locale；  API声明：numberingSystem: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：numeric: boolean;  差异内容：NA | 类名：Locale；  API声明：numeric: boolean;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：toString(): string;  差异内容：NA | 类名：Locale；  API声明：toString(): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：maximize(): Locale;  差异内容：NA | 类名：Locale；  API声明：maximize(): Locale;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Locale；  API声明：minimize(): Locale;  差异内容：NA | 类名：Locale；  API声明：minimize(): Locale;  差异内容：20 | api/@ohos.intl.d.ts |
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
| API废弃版本变更 | 类名：DateTimeFormat；  API声明：format(date: Date): string;  差异内容：NA | 类名：DateTimeFormat；  API声明：format(date: Date): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeFormat；  API声明：formatRange(startDate: Date, endDate: Date): string;  差异内容：NA | 类名：DateTimeFormat；  API声明：formatRange(startDate: Date, endDate: Date): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：DateTimeFormat；  API声明：resolvedOptions(): DateTimeOptions;  差异内容：NA | 类名：DateTimeFormat；  API声明：resolvedOptions(): DateTimeOptions;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：locale?: string;  差异内容：NA | 类名：NumberOptions；  API声明：locale?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：currency?: string;  差异内容：NA | 类名：NumberOptions；  API声明：currency?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：currencySign?: string;  差异内容：NA | 类名：NumberOptions；  API声明：currencySign?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：currencyDisplay?: string;  差异内容：NA | 类名：NumberOptions；  API声明：currencyDisplay?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：unit?: string;  差异内容：NA | 类名：NumberOptions；  API声明：unit?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：unitDisplay?: string;  差异内容：NA | 类名：NumberOptions；  API声明：unitDisplay?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：unitUsage?: string;  差异内容：NA | 类名：NumberOptions；  API声明：unitUsage?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：signDisplay?: string;  差异内容：NA | 类名：NumberOptions；  API声明：signDisplay?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：compactDisplay?: string;  差异内容：NA | 类名：NumberOptions；  API声明：compactDisplay?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：notation?: string;  差异内容：NA | 类名：NumberOptions；  API声明：notation?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：NumberOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：style?: string;  差异内容：NA | 类名：NumberOptions；  API声明：style?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：numberingSystem?: string;  差异内容：NA | 类名：NumberOptions；  API声明：numberingSystem?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：useGrouping?: boolean;  差异内容：NA | 类名：NumberOptions；  API声明：useGrouping?: boolean;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：minimumIntegerDigits?: number;  差异内容：NA | 类名：NumberOptions；  API声明：minimumIntegerDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：minimumFractionDigits?: number;  差异内容：NA | 类名：NumberOptions；  API声明：minimumFractionDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：maximumFractionDigits?: number;  差异内容：NA | 类名：NumberOptions；  API声明：maximumFractionDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：minimumSignificantDigits?: number;  差异内容：NA | 类名：NumberOptions；  API声明：minimumSignificantDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：maximumSignificantDigits?: number;  差异内容：NA | 类名：NumberOptions；  API声明：maximumSignificantDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：roundingPriority?: string;  差异内容：NA | 类名：NumberOptions；  API声明：roundingPriority?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：roundingIncrement?: number;  差异内容：NA | 类名：NumberOptions；  API声明：roundingIncrement?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberOptions；  API声明：roundingMode?: string;  差异内容：NA | 类名：NumberOptions；  API声明：roundingMode?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberFormat；  API声明：format(number: number): string;  差异内容：NA | 类名：NumberFormat；  API声明：format(number: number): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberFormat；  API声明：formatRange(startRange: number, endRange: number): string;  差异内容：NA | 类名：NumberFormat；  API声明：formatRange(startRange: number, endRange: number): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：NumberFormat；  API声明：resolvedOptions(): NumberOptions;  差异内容：NA | 类名：NumberFormat；  API声明：resolvedOptions(): NumberOptions;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：CollatorOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：usage?: string;  差异内容：NA | 类名：CollatorOptions；  API声明：usage?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：sensitivity?: string;  差异内容：NA | 类名：CollatorOptions；  API声明：sensitivity?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：ignorePunctuation?: boolean;  差异内容：NA | 类名：CollatorOptions；  API声明：ignorePunctuation?: boolean;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：collation?: string;  差异内容：NA | 类名：CollatorOptions；  API声明：collation?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：numeric?: boolean;  差异内容：NA | 类名：CollatorOptions；  API声明：numeric?: boolean;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：CollatorOptions；  API声明：caseFirst?: string;  差异内容：NA | 类名：CollatorOptions；  API声明：caseFirst?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Collator；  API声明：compare(first: string, second: string): number;  差异内容：NA | 类名：Collator；  API声明：compare(first: string, second: string): number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：Collator；  API声明：resolvedOptions(): CollatorOptions;  差异内容：NA | 类名：Collator；  API声明：resolvedOptions(): CollatorOptions;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：PluralRulesOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：type?: string;  差异内容：NA | 类名：PluralRulesOptions；  API声明：type?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：minimumIntegerDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：minimumIntegerDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：minimumFractionDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：minimumFractionDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：maximumFractionDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：maximumFractionDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：minimumSignificantDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：minimumSignificantDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRulesOptions；  API声明：maximumSignificantDigits?: number;  差异内容：NA | 类名：PluralRulesOptions；  API声明：maximumSignificantDigits?: number;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：PluralRules；  API声明：select(n: number): string;  差异内容：NA | 类名：PluralRules；  API声明：select(n: number): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatInputOptions；  API声明：localeMatcher?: string;  差异内容：NA | 类名：RelativeTimeFormatInputOptions；  API声明：localeMatcher?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatInputOptions；  API声明：numeric?: string;  差异内容：NA | 类名：RelativeTimeFormatInputOptions；  API声明：numeric?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatInputOptions；  API声明：style?: string;  差异内容：NA | 类名：RelativeTimeFormatInputOptions；  API声明：style?: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：locale: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：locale: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：style: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：style: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：numeric: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：numeric: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormatResolvedOptions；  API声明：numberingSystem: string;  差异内容：NA | 类名：RelativeTimeFormatResolvedOptions；  API声明：numberingSystem: string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormat；  API声明：format(value: number, unit: string): string;  差异内容：NA | 类名：RelativeTimeFormat；  API声明：format(value: number, unit: string): string;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormat；  API声明：formatToParts(value: number, unit: string): Array<object>;  差异内容：NA | 类名：RelativeTimeFormat；  API声明：formatToParts(value: number, unit: string): Array<object>;  差异内容：20 | api/@ohos.intl.d.ts |
| API废弃版本变更 | 类名：RelativeTimeFormat；  API声明：resolvedOptions(): RelativeTimeFormatResolvedOptions;  差异内容：NA | 类名：RelativeTimeFormat；  API声明：resolvedOptions(): RelativeTimeFormatResolvedOptions;  差异内容：20 | api/@ohos.intl.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat;  差异内容：export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat;  差异内容：export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleNumberFormat;  差异内容：export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleNumberFormat; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class ZoneRules  差异内容：export class ZoneRules | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ZoneRules；  API声明：public nextTransition(date?: number): ZoneOffsetTransition;  差异内容：public nextTransition(date?: number): ZoneOffsetTransition; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：i18n；  API声明：export class ZoneOffsetTransition  差异内容：export class ZoneOffsetTransition | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ZoneOffsetTransition；  API声明：public getMilliseconds(): number;  差异内容：public getMilliseconds(): number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ZoneOffsetTransition；  API声明：public getOffsetAfter(): number;  差异内容：public getOffsetAfter(): number; | api/@ohos.i18n.d.ts |
| 新增API | NA | 类名：ZoneOffsetTransition；  API声明：public getOffsetBefore(): number;  差异内容：public getOffsetBefore(): number; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：System；  API声明：static getSystemLocaleInstance(): Intl.Locale;  差异内容：static getSystemLocaleInstance(): Intl.Locale; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：System；  API声明：static setSystemLocaleInstance(locale: Intl.Locale): void;  差异内容：static setSystemLocaleInstance(locale: Intl.Locale): void; | api/@ohos.i18n.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TimeZone；  API声明：public getZoneRules(): ZoneRules;  差异内容：public getZoneRules(): ZoneRules; | api/@ohos.i18n.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：I18NUtil；  API声明：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string;  差异内容：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string; | 类名：I18NUtil；  API声明：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string;  差异内容：static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string; | api/@ohos.i18n.d.ts |
