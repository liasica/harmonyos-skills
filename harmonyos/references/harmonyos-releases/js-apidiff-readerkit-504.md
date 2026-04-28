---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-readerkit-504
title: Reader Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > API变更清单 > Reader Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0ccd373aed2791918d6669564c088d3e5fc867d17b266f8078bf8d8266ffa062
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： export declare namespace bookParser  差异内容： export declare namespace bookParser | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：bookParser；  API声明： class BookParserHandler  差异内容： class BookParserHandler | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getBookInfo(): BookInfo;  差异内容：public getBookInfo(): BookInfo; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getCatalogList(): CatalogItem[];  差异内容：public getCatalogList(): CatalogItem[]; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getSpineList(): SpineItem[];  差异内容：public getSpineList(): SpineItem[]; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getSpineItemContent(spineIndex: number): Promise<string>;  差异内容：public getSpineItemContent(spineIndex: number): Promise<string>; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getResourceContent(spineIndex: number, filePath: string): ArrayBuffer;  差异内容：public getResourceContent(spineIndex: number, filePath: string): ArrayBuffer; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getDomPosByCatalogHref(href: string): string;  差异内容：public getDomPosByCatalogHref(href: string): string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookParserHandler；  API声明：public getAbsoluteResourcePath(spineIndex: number): string;  差异内容：public getAbsoluteResourcePath(spineIndex: number): string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：bookParser；  API声明： interface SpineItem  差异内容： interface SpineItem | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：SpineItem；  API声明：idRef: string;  差异内容：idRef: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：SpineItem；  API声明：index: number;  差异内容：index: number; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：SpineItem；  API声明：href: string;  差异内容：href: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：SpineItem；  API声明：properties: string;  差异内容：properties: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：bookParser；  API声明： interface CatalogItem  差异内容： interface CatalogItem | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：catalogId: number;  差异内容：catalogId: number; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：catalogName: string;  差异内容：catalogName: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：catalogLevel?: number;  差异内容：catalogLevel?: number; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：playOrder?: number;  差异内容：playOrder?: number; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：idRef?: string;  差异内容：idRef?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：href?: string;  差异内容：href?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：CatalogItem；  API声明：resourceFile?: string;  差异内容：resourceFile?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：bookParser；  API声明： interface BookInfo  差异内容： interface BookInfo | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookTitle: string;  差异内容：bookTitle: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookCreator?: string;  差异内容：bookCreator?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookPublishDate?: string;  差异内容：bookPublishDate?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookLanguage?: string;  差异内容：bookLanguage?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookCoverImage?: string;  差异内容：bookCoverImage?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookCharset?: string;  差异内容：bookCharset?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：bookType?: string;  差异内容：bookType?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：isRtl?: boolean;  差异内容：isRtl?: boolean; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：renditionLayout?: string;  差异内容：renditionLayout?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：renditionOrientation?: string;  差异内容：renditionOrientation?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：BookInfo；  API声明：renditionSpread?: string;  差异内容：renditionSpread?: string; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：bookParser；  API声明：type CallbackRes<T, V> = (data: T) => V;  差异内容：type CallbackRes<T, V> = (data: T) => V; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：bookParser；  API声明：function getDefaultHandler(path: string): Promise<BookParserHandler>;  差异内容：function getDefaultHandler(path: string): Promise<BookParserHandler>; | api/@hms.core.readerservice.bookParser.d.ts |
| 新增API | NA | 类名：global；  API声明： declare struct ReadPageComponent  差异内容： declare struct ReadPageComponent | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReadPageComponent；  API声明：controller: readerCore.ReaderComponentController;  差异内容：controller: readerCore.ReaderComponentController; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReadPageComponent；  API声明：readerCallback: AsyncCallback<readerCore.ReaderComponentController>;  差异内容：readerCallback: AsyncCallback<readerCore.ReaderComponentController>; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReadPageComponent；  API声明：build(): void;  差异内容：build(): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： declare namespace readerCore  差异内容： declare namespace readerCore | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：readerCore；  API声明： interface ReaderSetting  差异内容： interface ReaderSetting | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：fontName: string;  差异内容：fontName: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：fontSize: number;  差异内容：fontSize: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：fontWeight: number;  差异内容：fontWeight: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：fontColor: string;  差异内容：fontColor: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：fontPath: string;  差异内容：fontPath: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：lineHeight: number;  差异内容：lineHeight: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：nightMode: boolean;  差异内容：nightMode: boolean; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：themeColor: string;  差异内容：themeColor: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：themeBgImg: string;  差异内容：themeBgImg: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：flipMode: string;  差异内容：flipMode: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：scaledDensity: number;  差异内容：scaledDensity: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：viewPortWidth: number;  差异内容：viewPortWidth: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderSetting；  API声明：viewPortHeight: number;  差异内容：viewPortHeight: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：readerCore；  API声明： class ReaderComponentController  差异内容： class ReaderComponentController | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public init(context: common.UIAbilityContext): Promise<void>;  差异内容：public init(context: common.UIAbilityContext): Promise<void>; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public startPlay(spineIndex: number, domPos: string): Promise<void>;  差异内容：public startPlay(spineIndex: number, domPos: string): Promise<void>; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public flipPage(isNext: boolean): void;  差异内容：public flipPage(isNext: boolean): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public setPageConfig(pageConfig: ReaderSetting): void;  差异内容：public setPageConfig(pageConfig: ReaderSetting): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public releaseBook(): void;  差异内容：public releaseBook(): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public registerBookParser(bookParserHandler: bookParser.BookParserHandler): void;  差异内容：public registerBookParser(bookParserHandler: bookParser.BookParserHandler): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public on(type: 'pageShow', callback: Callback<PageDataInfo>): void;  差异内容：public on(type: 'pageShow', callback: Callback<PageDataInfo>): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public off(type: 'pageShow', callback?: Callback<PageDataInfo>): void;  差异内容：public off(type: 'pageShow', callback?: Callback<PageDataInfo>): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public on(type: 'resourceRequest', callback: bookParser.CallbackRes<string, ArrayBuffer>): void;  差异内容：public on(type: 'resourceRequest', callback: bookParser.CallbackRes<string, ArrayBuffer>): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：ReaderComponentController；  API声明：public off(type: 'resourceRequest', callback?: bookParser.CallbackRes<string, ArrayBuffer>): void;  差异内容：public off(type: 'resourceRequest', callback?: bookParser.CallbackRes<string, ArrayBuffer>): void; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：readerCore；  API声明： class PageDatabaseBean  差异内容： class PageDatabaseBean | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDatabaseBean；  API声明：public nodeType: string;  差异内容：public nodeType: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDatabaseBean；  API声明：public dataId: string;  差异内容：public dataId: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：readerCore；  API声明： class PageDataInfo  差异内容： class PageDataInfo | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public pageHeaderContent: string;  差异内容：public pageHeaderContent: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public pageFooterContent: string;  差异内容：public pageFooterContent: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public startDomPos: string;  差异内容：public startDomPos: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public endDomPos: string;  差异内容：public endDomPos: string; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public state: PageState;  差异内容：public state: PageState; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public resourceIndex: number;  差异内容：public resourceIndex: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageDataInfo；  API声明：public pageOffset: number;  差异内容：public pageOffset: number; | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：readerCore；  API声明： enum PageState  差异内容： enum PageState | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageState；  API声明：PAGE\_WAITING = 1  差异内容：PAGE\_WAITING = 1 | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageState；  API声明：PAGE\_LOADING = 2  差异内容：PAGE\_LOADING = 2 | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageState；  API声明：PAGE\_ON\_SHOW = 3  差异内容：PAGE\_ON\_SHOW = 3 | api/@hms.core.readerservice.readerComponent.d.ets |
| 新增API | NA | 类名：PageState；  API声明：OPEN\_BOOK\_FAIL = 4  差异内容：OPEN\_BOOK\_FAIL = 4 | api/@hms.core.readerservice.readerComponent.d.ets |
| kit变更 | NA | ReaderKit | api/@hms.core.readerservice.bookParser.d.ts |
| kit变更 | NA | ReaderKit | api/@hms.core.readerservice.readerComponent.d.ets |
| kit变更 | NA | ReaderKit | kits/@kit.ReaderKit.d.ts |
