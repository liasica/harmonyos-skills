---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-remotecommunicationkit-6002
title: Remote Communication Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Remote Communication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d3e705a31a6926b7e274995e40f0985f7248ed55841f6e7de9f9e4bbc356d70b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：rcp；  API声明：export interface ResponseSendable  差异内容：export interface ResponseSendable | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly requestId: string;  差异内容：readonly requestId: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly statusCode: number;  差异内容：readonly statusCode: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly headers: ResponseHeaders;  差异内容：readonly headers: ResponseHeaders; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly effectiveUrl?: string;  差异内容：readonly effectiveUrl?: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly body?: ArrayBuffer;  差异内容：readonly body?: ArrayBuffer; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly downloadedTo?: DownloadedTo;  差异内容：readonly downloadedTo?: DownloadedTo; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly debugInfo?: DebugInfo[];  差异内容：readonly debugInfo?: DebugInfo[]; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly timeInfo?: TimeInfo;  差异内容：readonly timeInfo?: TimeInfo; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly cookies?: ResponseCookie[];  差异内容：readonly cookies?: ResponseCookie[]; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly httpVersion?: HttpVersion;  差异内容：readonly httpVersion?: HttpVersion; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly reasonPhrase?: string;  差异内容：readonly reasonPhrase?: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseSendable；  API声明：readonly cacheInfo?: CacheInfo;  差异内容：readonly cacheInfo?: CacheInfo; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface CacheControl  差异内容：export interface CacheControl | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：expirationPolicy?: TimeLimitedExpirationPolicy;  差异内容：expirationPolicy?: TimeLimitedExpirationPolicy; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：keepCache?: boolean;  差异内容：keepCache?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：noCache?: boolean;  差异内容：noCache?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：noStore?: boolean;  差异内容：noStore?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：maxAge?: TimeInterval;  差异内容：maxAge?: TimeInterval; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：maxStale?: TimeInterval;  差异内容：maxStale?: TimeInterval; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：minFresh?: TimeInterval;  差异内容：minFresh?: TimeInterval; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：noTransform?: boolean;  差异内容：noTransform?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheControl；  API声明：onlyIfCached?: boolean;  差异内容：onlyIfCached?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface CacheInfo  差异内容：export interface CacheInfo | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheInfo；  API声明：originalRequestId: string;  差异内容：originalRequestId: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheInfo；  API声明：age: TimeInterval;  差异内容：age: TimeInterval; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type TimeLimitedExpirationPolicy = AbsoluteTimeExpirationPolicy | RelativeTimeExpirationPolicy | SlidingTimeExpirationPolicy;  差异内容：export type TimeLimitedExpirationPolicy = AbsoluteTimeExpirationPolicy | RelativeTimeExpirationPolicy | SlidingTimeExpirationPolicy; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type ExpirationPolicy = NeverExpirationPolicy | TimeLimitedExpirationPolicy;  差异内容：export type ExpirationPolicy = NeverExpirationPolicy | TimeLimitedExpirationPolicy; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface NeverExpirationPolicy  差异内容：export interface NeverExpirationPolicy | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：NeverExpirationPolicy；  API声明：kind: 'never';  差异内容：kind: 'never'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface AbsoluteTimeExpirationPolicy  差异内容：export interface AbsoluteTimeExpirationPolicy | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：AbsoluteTimeExpirationPolicy；  API声明：kind: 'absolute';  差异内容：kind: 'absolute'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：AbsoluteTimeExpirationPolicy；  API声明：time: Date;  差异内容：time: Date; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface RelativeTimeExpirationPolicy  差异内容：export interface RelativeTimeExpirationPolicy | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：RelativeTimeExpirationPolicy；  API声明：kind: 'relative';  差异内容：kind: 'relative'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：RelativeTimeExpirationPolicy；  API声明：time: TimeInterval;  差异内容：time: TimeInterval; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface SlidingTimeExpirationPolicy  差异内容：export interface SlidingTimeExpirationPolicy | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：SlidingTimeExpirationPolicy；  API声明：kind: 'sliding';  差异内容：kind: 'sliding'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：SlidingTimeExpirationPolicy；  API声明：time: TimeInterval;  差异内容：time: TimeInterval; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface TimeInterval  差异内容：export interface TimeInterval | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TimeInterval；  API声明：units: TimeIntervalUnits;  差异内容：units: TimeIntervalUnits; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TimeInterval；  API声明：value: number;  差异内容：value: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type TimeIntervalUnits = 'seconds' | 'minutes' | 'hours' | 'days';  差异内容：export type TimeIntervalUnits = 'seconds' | 'minutes' | 'hours' | 'days'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface CachedResponse  差异内容：export interface CachedResponse | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：timeStamp: Date;  差异内容：timeStamp: Date; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：originalRequestId: string;  差异内容：originalRequestId: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：statusCode: number;  差异内容：statusCode: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：headers: rcp.ResponseHeaders;  差异内容：headers: rcp.ResponseHeaders; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：body?: ArrayBuffer;  差异内容：body?: ArrayBuffer; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：effectiveUrl?: string;  差异内容：effectiveUrl?: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：httpVersion?: rcp.HttpVersion;  差异内容：httpVersion?: rcp.HttpVersion; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：reasonPhrase?: string;  差异内容：reasonPhrase?: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CachedResponse；  API声明：extra?: ArrayBuffer;  差异内容：extra?: ArrayBuffer; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface ResponseCacheKey  差异内容：export interface ResponseCacheKey | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCacheKey；  API声明：url: URLOrString;  差异内容：url: URLOrString; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCacheKey；  API声明：method: HttpMethod;  差异内容：method: HttpMethod; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCacheKey；  API声明：extra?: string;  差异内容：extra?: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface ResponseCacheRecord  差异内容：export interface ResponseCacheRecord | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCacheRecord；  API声明：expirationPolicy: ExpirationPolicy;  差异内容：expirationPolicy: ExpirationPolicy; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCacheRecord；  API声明：response: CachedResponse;  差异内容：response: CachedResponse; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCacheRecord；  API声明：key: ResponseCacheKey;  差异内容：key: ResponseCacheKey; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface CacheConfiguration  差异内容：export interface CacheConfiguration | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheConfiguration；  API声明：persistent: PersistentStorageConfiguration;  差异内容：persistent: PersistentStorageConfiguration; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheConfiguration；  API声明：inMemory?: InMemoryCacheConfiguration;  差异内容：inMemory?: InMemoryCacheConfiguration; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheConfiguration；  API声明：maxItems?: number;  差异内容：maxItems?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheConfiguration；  API声明：maxSize?: number;  差异内容：maxSize?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheConfiguration；  API声明：defaultExpirationPolicy?: TimeLimitedExpirationPolicy;  差异内容：defaultExpirationPolicy?: TimeLimitedExpirationPolicy; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type PersistentStorageConfiguration = FileSystemStorageConfiguration;  差异内容：export type PersistentStorageConfiguration = FileSystemStorageConfiguration; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface FileSystemStorageConfiguration  差异内容：export interface FileSystemStorageConfiguration | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：FileSystemStorageConfiguration；  API声明：kind: 'file-system';  差异内容：kind: 'file-system'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：FileSystemStorageConfiguration；  API声明：pathToFolder: string;  差异内容：pathToFolder: string; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface InMemoryCacheConfiguration  差异内容：export interface InMemoryCacheConfiguration | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：InMemoryCacheConfiguration；  API声明：maxItems?: number;  差异内容：maxItems?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：InMemoryCacheConfiguration；  API声明：maxSize?: number;  差异内容：maxSize?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface CacheState  差异内容：export interface CacheState | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheState；  API声明：size: number;  差异内容：size: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheState；  API声明：count: number;  差异内容：count: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：CacheState；  API声明：hitCount: number;  差异内容：hitCount: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export class ResponseCache  差异内容：export class ResponseCache | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：set(key: ResponseCacheKey, response: CachedResponse, expirationPolicy?: ExpirationPolicy): Promise<void>;  差异内容：set(key: ResponseCacheKey, response: CachedResponse, expirationPolicy?: ExpirationPolicy): Promise<void>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：get(key: ResponseCacheKey): Promise<ResponseCacheRecord>;  差异内容：get(key: ResponseCacheKey): Promise<ResponseCacheRecord>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：clear(): Promise<void>;  差异内容：clear(): Promise<void>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：getState(): Promise<CacheState>;  差异内容：getState(): Promise<CacheState>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：remove(key: ResponseCacheKey): Promise<boolean>;  差异内容：remove(key: ResponseCacheKey): Promise<boolean>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：ResponseCache；  API声明：removeMultiple(url: URLOrString, matchKind: URLMatchKind, method?: HttpMethod): Promise<boolean>;  差异内容：removeMultiple(url: URLOrString, matchKind: URLMatchKind, method?: HttpMethod): Promise<boolean>; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type URLMatchKind = 'exact' | 'as-substring';  差异内容：export type URLMatchKind = 'exact' | 'as-substring'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export function createResponse(request: Request, cachedResponse: CachedResponse, currentTime: Date): Response;  差异内容：export function createResponse(request: Request, cachedResponse: CachedResponse, currentTime: Date): Response; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export function createCachedResponse(response: Response, timeStamp?: Date): CachedResponse;  差异内容：export function createCachedResponse(response: Response, timeStamp?: Date): CachedResponse; | api/@hms.collaboration.rcp.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：Request；  API声明：cacheControl?: CacheControl;  差异内容：cacheControl?: CacheControl; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Session；  API声明：fetchForSendable(request: Request): Promise<ResponseSendable>;  差异内容：fetchForSendable(request: Request): Promise<ResponseSendable>; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Configuration；  API声明：cache?: ResponseCache;  差异内容：cache?: ResponseCache; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Response；  API声明：readonly cacheInfo?: CacheInfo;  差异内容：readonly cacheInfo?: CacheInfo; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SessionConfiguration；  API声明：cacheControl?: CacheControl;  差异内容：cacheControl?: CacheControl; | api/@hms.collaboration.rcp.d.ts |
