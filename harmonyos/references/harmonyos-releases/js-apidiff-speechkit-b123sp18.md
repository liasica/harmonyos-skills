---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-speechkit-b123sp18
title: Speech Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Speech Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1d3dac4f962c6c9896ec310a5c5122b26f71ee1b6d0bc2aee833a02f3445f11f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：TextReader；  API声明：function release(): Promise<void>;  差异内容：1010600012 | 类名：TextReader；  API声明：function release(): Promise<void>;  差异内容：1010600012,1010600020 | api/@hms.ai.textReader.d.ets |
| 错误码变更 | 类名：TextReader；  API声明：function playPrev(): void;  差异内容：1010600012,1010600017 | 类名：TextReader；  API声明：function playPrev(): void;  差异内容：1010600012,1010600018 | api/@hms.ai.textReader.d.ets |
| 错误码变更 | 类名：TextReader；  API声明：function playNext(): void;  差异内容：1010600012,1010600018 | 类名：TextReader；  API声明：function playNext(): void;  差异内容：1010600012,1010600019 | api/@hms.ai.textReader.d.ets |
| 权限变更 | 类名：TextReader；  API声明：function init(context: common.BaseContext, readParams: ReaderParam): Promise<void>;  差异内容：NA | 类名：TextReader；  API声明：function init(context: common.BaseContext, readParams: ReaderParam): Promise<void>;  差异内容：ohos.permission.KEEP\_BACKGROUND\_RUNNING. | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function start(readInfoList: ReadInfo[], articleId: string | undefined, startParams: StartParams): Promise<void>;  差异内容：function start(readInfoList: ReadInfo[], articleId: string | undefined, startParams: StartParams): Promise<void>; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function on(type: 'requestMore', callback: Callback<string>): void;  差异内容：function on(type: 'requestMore', callback: Callback<string>): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function resetParam(paramName: ResetParamType): void;  差异内容：function resetParam(paramName: ResetParamType): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function showMinibar(): void;  差异内容：function showMinibar(): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function hideMinibar(): void;  差异内容：function hideMinibar(): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function queryReadStateByCategoryId(categoryId: string): ReadState;  差异内容：function queryReadStateByCategoryId(categoryId: string): ReadState; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function on(type: 'readProgress', callback: Callback<ReadProgress>): void;  差异内容：function on(type: 'readProgress', callback: Callback<ReadProgress>): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function off(type: 'readProgress', callback?: Callback<ReadProgress>): void;  差异内容：function off(type: 'readProgress', callback?: Callback<ReadProgress>): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： enum ResetParamType  差异内容： enum ResetParamType | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ResetParamType；  API声明：BAR\_PARAM = 1  差异内容：BAR\_PARAM = 1 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ResetParamType；  API声明：ALL = 2  差异内容：ALL = 2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ResetParamType；  API声明：READ\_LIST = 3  差异内容：READ\_LIST = 3 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface Person  差异内容： interface Person | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：Person；  API声明：tone: number;  差异内容：tone: number; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：Person；  API声明：style: string;  差异内容：style: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：person?: Person;  差异内容：person?: Person; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：isMinibarNeeded?: boolean;  差异内容：isMinibarNeeded?: boolean; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：minibarParams?: MinibarParams;  差异内容：minibarParams?: MinibarParams; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：customFeatures?: CustomFeature[];  差异内容：customFeatures?: CustomFeature[]; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：displayTab?: DisplayTab;  差异内容：displayTab?: DisplayTab; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：reportProgressPeriod?: number;  差异内容：reportProgressPeriod?: number; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface StartParams  差异内容： interface StartParams | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：StartParams；  API声明：isMinibarHidden?: boolean;  差异内容：isMinibarHidden?: boolean; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：StartParams；  API声明：callbackParam?: string;  差异内容：callbackParam?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： enum DisplayTab  差异内容： enum DisplayTab | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：DisplayTab；  API声明：COVER\_AND\_CONTENT = 1  差异内容：COVER\_AND\_CONTENT = 1 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：DisplayTab；  API声明：CONTENT = 2  差异内容：CONTENT = 2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：DisplayTab；  API声明：COVER = 3  差异内容：COVER = 3 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface MinibarParams  差异内容： interface MinibarParams | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：MinibarParams；  API声明：defaultAlignment: BarAlignment;  差异内容：defaultAlignment: BarAlignment; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：MinibarParams；  API声明：bottom?: number;  差异内容：bottom?: number; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： enum BarAlignment  差异内容： enum BarAlignment | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：BarAlignment；  API声明：LEFT = 1  差异内容：LEFT = 1 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：BarAlignment；  API声明：RIGHT = 2  差异内容：RIGHT = 2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadInfo；  API声明：imageUrl?: string;  差异内容：imageUrl?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadInfo；  API声明：bodyInfoObject?: BodyInfo;  差异内容：bodyInfoObject?: BodyInfo; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadInfo；  API声明：categoryObject?: CategoryInfo;  差异内容：categoryObject?: CategoryInfo; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadInfo；  API声明：audioInfo?: AudioInfo[];  差异内容：audioInfo?: AudioInfo[]; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadInfo；  API声明：isFavorite?: boolean;  差异内容：isFavorite?: boolean; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface CategoryInfo  差异内容： interface CategoryInfo | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CategoryInfo；  API声明：id: string;  差异内容：id: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CategoryInfo；  API声明：name: string;  差异内容：name: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CategoryInfo；  API声明：image: PixelMap | string;  差异内容：image: PixelMap | string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：NotificationEvent；  API声明：categoryId?: string;  差异内容：categoryId?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：PanelEvent；  API声明：categoryId?: string;  差异内容：categoryId?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ListEventState；  API声明：categoryId?: string;  差异内容：categoryId?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadState；  API声明：categoryId?: string;  差异内容：categoryId?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadState；  API声明：isLastArticle?: boolean;  差异内容：isLastArticle?: boolean; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface CustomFeature  差异内容： interface CustomFeature | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CustomFeature；  API声明：type: CustomFeatureType;  差异内容：type: CustomFeatureType; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CustomFeature；  API声明：name: string;  差异内容：name: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CustomFeature；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CustomFeature；  API声明：callback?: Callback<string>;  差异内容：callback?: Callback<string>; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface BodyInfo  差异内容： interface BodyInfo | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：BodyInfo；  API声明：type: BodyInfoType;  差异内容：type: BodyInfoType; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：BodyInfo；  API声明：body?: string;  差异内容：body?: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： export enum BodyInfoType  差异内容： export enum BodyInfoType | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：BodyInfoType；  API声明：CONTENT = 1  差异内容：CONTENT = 1 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：BodyInfoType；  API声明：FILE\_PATH = 2  差异内容：FILE\_PATH = 2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface ReadProgress  差异内容： interface ReadProgress | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgress；  API声明：id: string;  差异内容：id: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgress；  API声明：categoryId: string;  差异内容：categoryId: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgress；  API声明：readProgressType: ReadProgressType;  差异内容：readProgressType: ReadProgressType; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgress；  API声明：person: Person;  差异内容：person: Person; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgress；  API声明：maxPercent: number;  差异内容：maxPercent: number; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： interface AudioInfo  差异内容： interface AudioInfo | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：format: string;  差异内容：format: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：duration: number;  差异内容：duration: number; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：size: number;  差异内容：size: number; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：person?: Person;  差异内容：person?: Person; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：url: string;  差异内容：url: string; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： export enum CustomFeatureType  差异内容： export enum CustomFeatureType | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CustomFeatureType；  API声明：SYSTEM = 1  差异内容：SYSTEM = 1 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：CustomFeatureType；  API声明：USER = 2  差异内容：USER = 2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明： export enum ReadProgressType  差异内容： export enum ReadProgressType | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgressType；  API声明：PROGRESS = 1  差异内容：PROGRESS = 1 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgressType；  API声明：PAUSE = 2  差异内容：PAUSE = 2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgressType；  API声明：STOP = 3  差异内容：STOP = 3 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReadProgressType；  API声明：COMPLETED = 4  差异内容：COMPLETED = 4 | api/@hms.ai.textReader.d.ets |
