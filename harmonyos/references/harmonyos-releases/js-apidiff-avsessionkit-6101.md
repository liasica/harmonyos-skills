---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-6101
title: AVSession Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c57d726532e119d6af3b1869abae28ad2d9b98bc80365067279192dd69e6676
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace avMusicTemplate  差异内容：declare namespace avMusicTemplate | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate;  差异内容：function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type NoParamAsyncCallback = () => Promise<void>;  差异内容：type NoParamAsyncCallback = () => Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryMainTabsEvent = () => Promise<MediaTab[]>;  差异内容：type QueryMainTabsEvent = () => Promise<MediaTab[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryMediaTabContentEvent = (tabId: string) => Promise<MediaTabContent>;  差异内容：type QueryMediaTabContentEvent = (tabId: string) => Promise<MediaTabContent>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryMediaEntityEvent = (params: QueryMediaEntityParam) => Promise<PageMediaEntity>;  差异内容：type QueryMediaEntityEvent = (params: QueryMediaEntityParam) => Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryCompilationEvent = (compilationId: string, pageIndex: number) => Promise<PageMediaEntity>;  差异内容：type QueryCompilationEvent = (compilationId: string, pageIndex: number) => Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryPlaylistEvent = (pageIndex: number, sort: Sort) => Promise<PageMediaEntity>;  差异内容：type QueryPlaylistEvent = (pageIndex: number, sort: Sort) => Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryCurrentSingleEvent = () => Promise<Single>;  差异内容：type QueryCurrentSingleEvent = () => Promise<Single>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryCompilationByKeywordEvent = (keyword: string) => Promise<Compilation[]>;  差异内容：type QueryCompilationByKeywordEvent = (keyword: string) => Promise<Compilation[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType, pageIndex: number) => Promise<PageMediaEntity>;  差异内容：type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType, pageIndex: number) => Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryRecommendMediaEntityListEvent = () => Promise<MediaEntity[]>;  差异内容：type QueryRecommendMediaEntityListEvent = () => Promise<MediaEntity[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryHotWordsEvent = () => Promise<string[]>;  差异内容：type QueryHotWordsEvent = () => Promise<string[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QuerySearchHistoryEvent = () => Promise<string[]>;  差异内容：type QuerySearchHistoryEvent = () => Promise<string[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ClearSearchHistoryEvent = () => Promise<OperResult>;  差异内容：type ClearSearchHistoryEvent = () => Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>;  差异内容：type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>;  差异内容：type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type HandleMemberPurchaseEvent = (info: MemberPurchaseInfo) => Promise<DialogInfo>;  差异内容：type HandleMemberPurchaseEvent = (info: MemberPurchaseInfo) => Promise<DialogInfo>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryMemberPurchaseEvent = (memberPurchaseType: MemberPurchaseType) => Promise<MemberPurchaseInfo[]>;  差异内容：type QueryMemberPurchaseEvent = (memberPurchaseType: MemberPurchaseType) => Promise<MemberPurchaseInfo[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>;  差异内容：type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type DownloadMediaEntityEvent = (controlType: DownloadControlType, mediaEntity: MediaEntity) => Promise<OperResult>;  差异内容：type DownloadMediaEntityEvent = (controlType: DownloadControlType, mediaEntity: MediaEntity) => Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type SettingsChangeEvent = (settingItem: SettingItem) => Promise<SettingItem>;  差异内容：type SettingsChangeEvent = (settingItem: SettingItem) => Promise<SettingItem>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>;  差异内容：type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type PlayForSearchEvent = (command: SearchPlayInfoType, args: SearchPlayInfo) => Promise<OperResult>;  差异内容：type PlayForSearchEvent = (command: SearchPlayInfoType, args: SearchPlayInfo) => Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>;  差异内容：type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type PlayMediaEntityEvent = (mediaEntity: MediaEntity) => Promise<void>;  差异内容：type PlayMediaEntityEvent = (mediaEntity: MediaEntity) => Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type FavoriteMediaEntityEvent = (actionType: MediaFavoriteType, mediaEntity: MediaEntity) => Promise<OperResult>;  差异内容：type FavoriteMediaEntityEvent = (actionType: MediaFavoriteType, mediaEntity: MediaEntity) => Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：class AVMusicTemplate  差异内容：class AVMusicTemplate | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：sessionId: string;  差异内容：sessionId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：sessionTag: string;  差异内容：sessionTag: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：startTemplate(): Promise<OperResult>;  差异内容：startTemplate(): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryMainTabs(callback: QueryMainTabsEvent): void;  差异内容：onQueryMainTabs(callback: QueryMainTabsEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryMainTabs(callback?: QueryMainTabsEvent): void;  差异内容：offQueryMainTabs(callback?: QueryMainTabsEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void;  差异内容：onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void;  差异内容：offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryMediaEntity(callback: QueryMediaEntityEvent): void;  差异内容：onQueryMediaEntity(callback: QueryMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryMediaEntity(callback?: QueryMediaEntityEvent): void;  差异内容：offQueryMediaEntity(callback?: QueryMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryCompilation(callback: QueryCompilationEvent): void;  差异内容：onQueryCompilation(callback: QueryCompilationEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryCompilation(callback?: QueryCompilationEvent): void;  差异内容：offQueryCompilation(callback?: QueryCompilationEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryPlaylist(callback: QueryPlaylistEvent): void;  差异内容：onQueryPlaylist(callback: QueryPlaylistEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryPlaylist(callback?: QueryPlaylistEvent): void;  差异内容：offQueryPlaylist(callback?: QueryPlaylistEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void;  差异内容：onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void;  差异内容：offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void;  差异内容：onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void;  差异内容：offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void;  差异内容：onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void;  差异内容：offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void;  差异内容：onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void;  差异内容：offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryHotWords(callback: QueryHotWordsEvent): void;  差异内容：onQueryHotWords(callback: QueryHotWordsEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryHotWords(callback?: QueryHotWordsEvent): void;  差异内容：offQueryHotWords(callback?: QueryHotWordsEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQuerySearchHistory(callback: QuerySearchHistoryEvent): void;  差异内容：onQuerySearchHistory(callback: QuerySearchHistoryEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void;  差异内容：offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onClearSearchHistory(callback: ClearSearchHistoryEvent): void;  差异内容：onClearSearchHistory(callback: ClearSearchHistoryEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offClearSearchHistory(callback?: ClearSearchHistoryEvent): void;  差异内容：offClearSearchHistory(callback?: ClearSearchHistoryEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onLogin(callback: LoginEvent): void;  差异内容：onLogin(callback: LoginEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offLogin(callback?: LoginEvent): void;  差异内容：offLogin(callback?: LoginEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onRequestDialogInfo(callback: RequestDialogInfoEvent): void;  差异内容：onRequestDialogInfo(callback: RequestDialogInfoEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offRequestDialogInfo(callback?: RequestDialogInfoEvent): void;  差异内容：offRequestDialogInfo(callback?: RequestDialogInfoEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void;  差异内容：onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void;  差异内容：offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void;  差异内容：onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void;  差异内容：offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onQueryCustomContent(callback: QueryCustomContentEvent): void;  差异内容：onQueryCustomContent(callback: QueryCustomContentEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offQueryCustomContent(callback?: QueryCustomContentEvent): void;  差异内容：offQueryCustomContent(callback?: QueryCustomContentEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void;  差异内容：onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void;  差异内容：offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onSettingsChange(callback: SettingsChangeEvent): void;  差异内容：onSettingsChange(callback: SettingsChangeEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offSettingsChange(callback?: SettingsChangeEvent): void;  差异内容：offSettingsChange(callback?: SettingsChangeEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onProblemAndAdvice(callback: ProblemAndAdviceEvent): void;  差异内容：onProblemAndAdvice(callback: ProblemAndAdviceEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void;  差异内容：offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onPlayForSearch(callback: PlayForSearchEvent): void;  差异内容：onPlayForSearch(callback: PlayForSearchEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offPlayForSearch(callback?: PlayForSearchEvent): void;  差异内容：offPlayForSearch(callback?: PlayForSearchEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onExecuteAction(callback: ExecuteActionEvent): void;  差异内容：onExecuteAction(callback: ExecuteActionEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offExecuteAction(callback?: ExecuteActionEvent): void;  差异内容：offExecuteAction(callback?: ExecuteActionEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onPlayMediaEntity(callback: PlayMediaEntityEvent): void;  差异内容：onPlayMediaEntity(callback: PlayMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offPlayMediaEntity(callback?: PlayMediaEntityEvent): void;  差异内容：offPlayMediaEntity(callback?: PlayMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void;  差异内容：onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void;  差异内容：offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setUserInfo(userInfo: UserInfo): Promise<void>;  差异内容：setUserInfo(userInfo: UserInfo): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>;  差异内容：setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setCurrentSingle(single: Single): Promise<void>;  差异内容：setCurrentSingle(single: Single): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setMediaEntities(entities: MediaEntity[]): Promise<void>;  差异内容：setMediaEntities(entities: MediaEntity[]): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>;  差异内容：setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setPlaylist(playlist: PageMediaEntity): Promise<void>;  差异内容：setPlaylist(playlist: PageMediaEntity): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>;  差异内容：setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setCustomElements(actionType: ActionType, customType: CustomType, customElement: CustomElement): Promise<void>;  差异内容：setCustomElements(actionType: ActionType, customType: CustomType, customElement: CustomElement): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setSettings(settingItems: SettingItem[]): Promise<void>;  差异内容：setSettings(settingItems: SettingItem[]): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：reportExecuteAction(actionType: string, params: string): Promise<void>;  差异内容：reportExecuteAction(actionType: string, params: string): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：setExtensionAbility(want: WantAgent): Promise<void>;  差异内容：setExtensionAbility(want: WantAgent): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：class AVMusicTemplateController  差异内容：class AVMusicTemplateController | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：sessionId: string;  差异内容：sessionId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：isDestroy: boolean;  差异内容：isDestroy: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryMainTabs(): Promise<MediaTab[]>;  差异内容：queryMainTabs(): Promise<MediaTab[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryMediaTabContent(tabId: string): Promise<MediaTabContent>;  差异内容：queryMediaTabContent(tabId: string): Promise<MediaTabContent>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>;  差异内容：queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>;  差异内容：queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>;  差异内容：queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryCurrentSingle(): Promise<Single>;  差异内容：queryCurrentSingle(): Promise<Single>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryCompilationByKeyword(keyword: string): Promise<Compilation[]>;  差异内容：queryCompilationByKeyword(keyword: string): Promise<Compilation[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>;  差异内容：queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryRecommendMediaEntityList(): Promise<MediaEntity[]>;  差异内容：queryRecommendMediaEntityList(): Promise<MediaEntity[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryHotWords(): Promise<string[]>;  差异内容：queryHotWords(): Promise<string[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：querySearchHistory(): Promise<string[]>;  差异内容：querySearchHistory(): Promise<string[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：clearSearchHistory(): Promise<OperResult>;  差异内容：clearSearchHistory(): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：updateSettings(settingItem: SettingItem): Promise<SettingItem>;  差异内容：updateSettings(settingItem: SettingItem): Promise<SettingItem>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：reportProblemAndAdvice(advice: string): Promise<OperResult>;  差异内容：reportProblemAndAdvice(advice: string): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>;  差异内容：login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>;  差异内容：requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>;  差异内容：handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>;  差异内容：queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：queryCustomContent(queryType: CustomType[]): Promise<CustomElement>;  差异内容：queryCustomContent(queryType: CustomType[]): Promise<CustomElement>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>;  差异内容：downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>;  差异内容：playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：executeAction(actionType: string, params: string): Promise<string>;  差异内容：executeAction(actionType: string, params: string): Promise<string>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：playMediaEntity(mediaEntity: MediaEntity): Promise<void>;  差异内容：playMediaEntity(mediaEntity: MediaEntity): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>;  差异内容：favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onUserInfoChange(callback: Callback<UserInfo>): void;  差异内容：onUserInfoChange(callback: Callback<UserInfo>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offUserInfoChange(callback?: Callback<UserInfo>): void;  差异内容：offUserInfoChange(callback?: Callback<UserInfo>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onDialogCommandChange(callback: ReportDialogCommandEvent): void;  差异内容：onDialogCommandChange(callback: ReportDialogCommandEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offDialogCommandChange(callback?: ReportDialogCommandEvent): void;  差异内容：offDialogCommandChange(callback?: ReportDialogCommandEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onCurrentSingleChange(callback: Callback<Single>): void;  差异内容：onCurrentSingleChange(callback: Callback<Single>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offCurrentSingleChange(callback?: Callback<Single>): void;  差异内容：offCurrentSingleChange(callback?: Callback<Single>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void;  差异内容：onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void;  差异内容：offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onTabContentChange(callback: ReportTabContentEvent): void;  差异内容：onTabContentChange(callback: ReportTabContentEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offTabContentChange(callback?: ReportTabContentEvent): void;  差异内容：offTabContentChange(callback?: ReportTabContentEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onPlaylistChange(callback: Callback<PageMediaEntity>): void;  差异内容：onPlaylistChange(callback: Callback<PageMediaEntity>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offPlaylistChange(callback?: Callback<PageMediaEntity>): void;  差异内容：offPlaylistChange(callback?: Callback<PageMediaEntity>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void;  差异内容：onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void;  差异内容：offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void;  差异内容：onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void;  差异内容：offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onSettingsChange(callback: Callback<SettingItem[]>): void;  差异内容：onSettingsChange(callback: Callback<SettingItem[]>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offSettingsChange(callback?: Callback<SettingItem[]>): void;  差异内容：offSettingsChange(callback?: Callback<SettingItem[]>): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onReportExecuteAction(callback: ReportExecuteActionEvent): void;  差异内容：onReportExecuteAction(callback: ReportExecuteActionEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offReportExecuteAction(callback?: ReportExecuteActionEvent): void;  差异内容：offReportExecuteAction(callback?: ReportExecuteActionEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void;  差异内容：onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void;  差异内容：offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ReportDialogCommandEvent = (type: DialogControlType, buttonInfo: DialogInfo) => void;  差异内容：type ReportDialogCommandEvent = (type: DialogControlType, buttonInfo: DialogInfo) => void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void;  差异内容：type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType, customElement: CustomElement) => void;  差异内容：type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType, customElement: CustomElement) => void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ReportExecuteActionEvent = (actionType: string, params: string) => void;  差异内容：type ReportExecuteActionEvent = (actionType: string, params: string) => void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ReportExecuteAbilityEvent = (want: WantAgent) => void;  差异内容：type ReportExecuteAbilityEvent = (want: WantAgent) => void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type MediaFavoriteType = 'addFavorite' | 'removeFavorite';  差异内容：type MediaFavoriteType = 'addFavorite' | 'removeFavorite'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type ActionType = 'add' | 'remove';  差异内容：type ActionType = 'add' | 'remove'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type CustomType = 'USER\_INFO' | 'TAB' | 'COMPILATION' | 'SETTINGS';  差异内容：type CustomType = 'USER\_INFO' | 'TAB' | 'COMPILATION' | 'SETTINGS'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type DownloadControlType = 'startDownload' | 'deleteDownload' | 'resumeDownload' | 'pauseDownload';  差异内容：type DownloadControlType = 'startDownload' | 'deleteDownload' | 'resumeDownload' | 'pauseDownload'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type LoginType = 'queryLoginInfo' | 'refreshLoginInfo' | 'cancel' | 'logout';  差异内容：type LoginType = 'queryLoginInfo' | 'refreshLoginInfo' | 'cancel' | 'logout'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type DialogActionType = 'open' | 'close' | 'refresh';  差异内容：type DialogActionType = 'open' | 'close' | 'refresh'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type DialogControlType = 'open' | 'close' | 'refresh' | 'toast';  差异内容：type DialogControlType = 'open' | 'close' | 'refresh' | 'toast'; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface OperResult  差异内容：interface OperResult | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：OperResult；  API声明：errorCode: number;  差异内容：errorCode: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：OperResult；  API声明：errorMsg?: string;  差异内容：errorMsg?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface MediaTab  差异内容：interface MediaTab | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaTab；  API声明：tabId: string;  差异内容：tabId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaTab；  API声明：tabName: string;  差异内容：tabName: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaTab；  API声明：tabIcon?: image.PixelMap;  差异内容：tabIcon?: image.PixelMap; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaTab；  API声明：extraDataJson?: string;  差异内容：extraDataJson?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface MediaTabContent  差异内容：interface MediaTabContent | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaTabContent；  API声明：tabId: string;  差异内容：tabId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaTabContent；  API声明：compilations: Compilation[];  差异内容：compilations: Compilation[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface CustomElement  差异内容：interface CustomElement | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：CustomElement；  API声明：userInfo?: UserInfo;  差异内容：userInfo?: UserInfo; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：CustomElement；  API声明：tabs?: MediaTab[];  差异内容：tabs?: MediaTab[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：CustomElement；  API声明：customCompilations?: Compilation[];  差异内容：customCompilations?: Compilation[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：CustomElement；  API声明：settings?: SettingItem[];  差异内容：settings?: SettingItem[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface Compilation  差异内容：interface Compilation | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Compilation；  API声明：id: string;  差异内容：id: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Compilation；  API声明：title: string;  差异内容：title: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Compilation；  API声明：hasMoreData: boolean;  差异内容：hasMoreData: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Compilation；  API声明：totalSize: number;  差异内容：totalSize: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Compilation；  API声明：memberMediaType: EntityType;  差异内容：memberMediaType: EntityType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Compilation；  API声明：topElements: MediaEntity[];  差异内容：topElements: MediaEntity[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface PageMediaEntity  差异内容：interface PageMediaEntity | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：pageIndex: number;  差异内容：pageIndex: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：pageSize: number;  差异内容：pageSize: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：hasMoreData: boolean;  差异内容：hasMoreData: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：totalSize: number;  差异内容：totalSize: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：memberMediaType: EntityType;  差异内容：memberMediaType: EntityType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：elements: MediaEntity[];  差异内容：elements: MediaEntity[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：sort?: Sort;  差异内容：sort?: Sort; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PageMediaEntity；  API声明：episodeRange?: EpisodeRange;  差异内容：episodeRange?: EpisodeRange; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface MediaEntity  差异内容：interface MediaEntity | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：mediaId: string;  差异内容：mediaId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：mediaType: EntityType;  差异内容：mediaType: EntityType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：parentId: string;  差异内容：parentId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：parentMediaType: EntityType;  差异内容：parentMediaType: EntityType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：title: string;  差异内容：title: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：desc?: string;  差异内容：desc?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：imageUrl: string;  差异内容：imageUrl: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MediaEntity；  API声明：playState: PlaybackState;  差异内容：playState: PlaybackState; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface MediaElement  差异内容：interface MediaElement | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface Banner  差异内容：interface Banner | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Banner；  API声明：isSupportOnePlay: boolean;  差异内容：isSupportOnePlay: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface Album  差异内容：interface Album | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Album；  API声明：singer: string;  差异内容：singer: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Album；  API声明：playCounts: string;  差异内容：playCounts: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Album；  API声明：favSubscribeData: FavoriteData;  差异内容：favSubscribeData: FavoriteData; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Album；  API声明：episodeCounts?: string;  差异内容：episodeCounts?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface Single  差异内容：interface Single | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：isVip: boolean;  差异内容：isVip: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：singer: string;  差异内容：singer: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：playInfo: PlayInfo;  差异内容：playInfo: PlayInfo; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：favSubscribeData: FavoriteData;  差异内容：favSubscribeData: FavoriteData; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：tags?: string[];  差异内容：tags?: string[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：settings?: SettingItem[];  差异内容：settings?: SettingItem[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：downloadStatus?: DownloadStatus;  差异内容：downloadStatus?: DownloadStatus; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Single；  API声明：downloadProgress?: number;  差异内容：downloadProgress?: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum DownloadStatus  差异内容：enum DownloadStatus | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DownloadStatus；  API声明：DOWNLOAD\_SUCCESS = 0  差异内容：DOWNLOAD\_SUCCESS = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DownloadStatus；  API声明：DOWNLOADING = 1  差异内容：DOWNLOADING = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DownloadStatus；  API声明：DOWNLOAD\_FAIL = 2  差异内容：DOWNLOAD\_FAIL = 2 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface Ranking  差异内容：interface Ranking | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Ranking；  API声明：topElements: MediaEntity[];  差异内容：topElements: MediaEntity[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface PlayInfo  差异内容：interface PlayInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：playCounts: string;  差异内容：playCounts: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportNext: boolean;  差异内容：isSupportNext: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportPrev: boolean;  差异内容：isSupportPrev: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportQuickForward: boolean;  差异内容：isSupportQuickForward: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportQuickBackward: boolean;  差异内容：isSupportQuickBackward: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：quickForwardStep: number;  差异内容：quickForwardStep: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：quickBackwardStep: number;  差异内容：quickBackwardStep: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportSkipHead: boolean;  差异内容：isSupportSkipHead: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportSkipTail: boolean;  差异内容：isSupportSkipTail: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportPlayMode: boolean;  差异内容：isSupportPlayMode: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportPlayRate: boolean;  差异内容：isSupportPlayRate: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：supportedPlayRate: string[];  差异内容：supportedPlayRate: string[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：currentPlayRate: string;  差异内容：currentPlayRate: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportSoundQuality: boolean;  差异内容：isSupportSoundQuality: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportSoundEffect: boolean;  差异内容：isSupportSoundEffect: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：totalDuration: number;  差异内容：totalDuration: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：currentPlayDuration: number;  差异内容：currentPlayDuration: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlayInfo；  API声明：isSupportProgress: boolean;  差异内容：isSupportProgress: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface FavoriteData  差异内容：interface FavoriteData | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：FavoriteData；  API声明：isSupportFav: boolean;  差异内容：isSupportFav: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：FavoriteData；  API声明：isFavorite: boolean;  差异内容：isFavorite: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：FavoriteData；  API声明：favCounts: string;  差异内容：favCounts: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface UserInfo  差异内容：interface UserInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：UserInfo；  API声明：userInfoId: string;  差异内容：userInfoId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：UserInfo；  API声明：nickName: string;  差异内容：nickName: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：UserInfo；  API声明：profilePicUrl: string;  差异内容：profilePicUrl: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：UserInfo；  API声明：tips: string;  差异内容：tips: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：UserInfo；  API声明：isLogin: boolean;  差异内容：isLogin: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：UserInfo；  API声明：isVip: boolean;  差异内容：isVip: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface MemberPurchaseInfo  差异内容：interface MemberPurchaseInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseInfo；  API声明：id: string;  差异内容：id: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseInfo；  API声明：diagramUrl: string;  差异内容：diagramUrl: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseInfo；  API声明：diagramData?: image.PixelMap;  差异内容：diagramData?: image.PixelMap; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseInfo；  API声明：diagramContent: string;  差异内容：diagramContent: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseInfo；  API声明：memberPurchaseType: MemberPurchaseType;  差异内容：memberPurchaseType: MemberPurchaseType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface QrCodeInfo  差异内容：interface QrCodeInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：id: string;  差异内容：id: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：price: string;  差异内容：price: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：titleName: string;  差异内容：titleName: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：detailName: string;  差异内容：detailName: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：tips: string;  差异内容：tips: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：icon?: image.PixelMap;  差异内容：icon?: image.PixelMap; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：content: string;  差异内容：content: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：codeData?: image.PixelMap;  差异内容：codeData?: image.PixelMap; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QrCodeInfo；  API声明：validPeriod: number;  差异内容：validPeriod: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SettingItem  差异内容：interface SettingItem | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingItem；  API声明：id: string;  差异内容：id: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingItem；  API声明：title: string;  差异内容：title: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingItem；  API声明：desc: string;  差异内容：desc: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingItem；  API声明：settingType?: SettingType;  差异内容：settingType?: SettingType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingItem；  API声明：settingValue?: string | boolean | SettingContent[] | WantAgent;  差异内容：settingValue?: string | boolean | SettingContent[] | WantAgent; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingItem；  API声明：mediaId: string;  差异内容：mediaId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SettingContent  差异内容：interface SettingContent | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingContent；  API声明：value: string;  差异内容：value: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingContent；  API声明：isSelected: boolean;  差异内容：isSelected: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingContent；  API声明：textTags?: string[];  差异内容：textTags?: string[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingContent；  API声明：imageTags?: image.PixelMap[];  差异内容：imageTags?: image.PixelMap[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface DialogActionInfo  差异内容：interface DialogActionInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogActionInfo；  API声明：dialogId: string;  差异内容：dialogId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogActionInfo；  API声明：isChecked: boolean;  差异内容：isChecked: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogActionInfo；  API声明：clickedBtnId: string;  差异内容：clickedBtnId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface DialogInfo  差异内容：interface DialogInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：dialogId: string;  差异内容：dialogId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：dialogType: DialogType;  差异内容：dialogType: DialogType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：title?: string;  差异内容：title?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：text?: string;  差异内容：text?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：buttons?: DialogButtonInfo[];  差异内容：buttons?: DialogButtonInfo[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：qrCodes?: QrCodeInfo[];  差异内容：qrCodes?: QrCodeInfo[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogInfo；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface DialogButtonInfo  差异内容：interface DialogButtonInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogButtonInfo；  API声明：buttonId: string;  差异内容：buttonId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogButtonInfo；  API声明：buttonText: string;  差异内容：buttonText: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogButtonInfo；  API声明：buttonType: ButtonType;  差异内容：buttonType: ButtonType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SearchPlayMusicItem  差异内容：interface SearchPlayMusicItem | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicItem；  API声明：entityId: string;  差异内容：entityId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicItem；  API声明：entityName?: string;  差异内容：entityName?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SearchPlayMusicInfo  差异内容：interface SearchPlayMusicInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicInfo；  API声明：items: SearchPlayMusicItem[];  差异内容：items: SearchPlayMusicItem[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicInfo；  API声明：displayName?: string;  差异内容：displayName?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicInfo；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicInfo；  API声明：playMusicOnly?: boolean;  差异内容：playMusicOnly?: boolean; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicInfo；  API声明：playMode?: string;  差异内容：playMode?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SearchPlayVideoInfo  差异内容：interface SearchPlayVideoInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayVideoInfo；  API声明：entityId: string;  差异内容：entityId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayVideoInfo；  API声明：episodeId?: string;  差异内容：episodeId?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayVideoInfo；  API声明：episodeNumber?: number;  差异内容：episodeNumber?: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayVideoInfo；  API声明：extras?: string;  差异内容：extras?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SearchPlayInfo  差异内容：interface SearchPlayInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfo；  API声明：musicInfo?: SearchPlayMusicInfo;  差异内容：musicInfo?: SearchPlayMusicInfo; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfo；  API声明：videoInfo?: SearchPlayVideoInfo;  差异内容：videoInfo?: SearchPlayVideoInfo; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface EpisodeRange  差异内容：interface EpisodeRange | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EpisodeRange；  API声明：start: number;  差异内容：start: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EpisodeRange；  API声明：end: number;  差异内容：end: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface QueryMediaEntityParam  差异内容：interface QueryMediaEntityParam | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QueryMediaEntityParam；  API声明：entityId: string;  差异内容：entityId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QueryMediaEntityParam；  API声明：pageIndex: number;  差异内容：pageIndex: number; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QueryMediaEntityParam；  API声明：type: EntityType;  差异内容：type: EntityType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QueryMediaEntityParam；  API声明：subEntityType?: EntityType;  差异内容：subEntityType?: EntityType; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QueryMediaEntityParam；  API声明：sort?: Sort;  差异内容：sort?: Sort; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：QueryMediaEntityParam；  API声明：episodeRange?: EpisodeRange;  差异内容：episodeRange?: EpisodeRange; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum SettingType  差异内容：enum SettingType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingType；  API声明：SWITCH = 0  差异内容：SWITCH = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingType；  API声明：LIST = 1  差异内容：LIST = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SettingType；  API声明：JUMP = 2  差异内容：JUMP = 2 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum DialogType  差异内容：enum DialogType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：INTERNET = 1  差异内容：INTERNET = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：FLOW = 2  差异内容：FLOW = 2 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：PAID = 3  差异内容：PAID = 3 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：VIP = 4  差异内容：VIP = 4 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：LOGIN = 5  差异内容：LOGIN = 5 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：ERROR = 6  差异内容：ERROR = 6 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：DialogType；  API声明：UNKNOWN = 7  差异内容：UNKNOWN = 7 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum ButtonType  差异内容：enum ButtonType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：ButtonType；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：ButtonType；  API声明：EMPHASIZE = 1  差异内容：EMPHASIZE = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum EntityType  差异内容：enum EntityType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：SINGLE = 1  差异内容：SINGLE = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：SINGER = 2  差异内容：SINGER = 2 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：ALBUM = 3  差异内容：ALBUM = 3 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：RANKING = 4  差异内容：RANKING = 4 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：BANNER = 5  差异内容：BANNER = 5 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：RADIO\_STATION = 6  差异内容：RADIO\_STATION = 6 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum PlaybackState  差异内容：enum PlaybackState | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_PREPARE = 0  差异内容：PLAYBACK\_STATE\_PREPARE = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_PLAY = 1  差异内容：PLAYBACK\_STATE\_PLAY = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_PAUSE = 2  差异内容：PLAYBACK\_STATE\_PAUSE = 2 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_STOP = 3  差异内容：PLAYBACK\_STATE\_STOP = 3 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_COMPLETED = 4  差异内容：PLAYBACK\_STATE\_COMPLETED = 4 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_ERROR = 5  差异内容：PLAYBACK\_STATE\_ERROR = 5 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：PlaybackState；  API声明：PLAYBACK\_STATE\_BUFFERING = 6  差异内容：PLAYBACK\_STATE\_BUFFERING = 6 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum MemberPurchaseType  差异内容：enum MemberPurchaseType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseType；  API声明：NORMAL = 'normal'  差异内容：NORMAL = 'normal' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：MemberPurchaseType；  API声明：BANNER = 'banner'  差异内容：BANNER = 'banner' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum AVMusicTemplateType  差异内容：enum AVMusicTemplateType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateType；  API声明：DEFAULT = 'smartCar'  差异内容：DEFAULT = 'smartCar' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum SearchPlayInfoType  差异内容：enum SearchPlayInfoType | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfoType；  API声明：PLAY\_MUSIC = 'playMusic'  差异内容：PLAY\_MUSIC = 'playMusic' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfoType；  API声明：PLAY\_VIDEO = 'playVideo'  差异内容：PLAY\_VIDEO = 'playVideo' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum Sort  差异内容：enum Sort | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Sort；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Sort；  API声明：ORDER = 1  差异内容：ORDER = 1 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：Sort；  API声明：REVERSE\_ORDER = 2  差异内容：REVERSE\_ORDER = 2 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：enum AVMusicTemplateErrorCode  差异内容：enum AVMusicTemplateErrorCode | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_CREATE\_AV\_MUSIC\_TEMPLATE\_FAILED = 35000001  差异内容：ERR\_CODE\_CREATE\_AV\_MUSIC\_TEMPLATE\_FAILED = 35000001 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_CREATE\_AV\_MUSIC\_TEMPLATE\_CONTROLLER\_FAILED = 35000002  差异内容：ERR\_CODE\_CREATE\_AV\_MUSIC\_TEMPLATE\_CONTROLLER\_FAILED = 35000002 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_TEMPLATE\_LISTENER\_NO\_EXIT = 35000003  差异内容：ERR\_CODE\_TEMPLATE\_LISTENER\_NO\_EXIT = 35000003 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_CONTROLLER\_CALLBACK\_NO\_EXIT = 35000004  差异内容：ERR\_CODE\_CONTROLLER\_CALLBACK\_NO\_EXIT = 35000004 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_AV\_MUSIC\_TEMPLATE\_NOT\_EXIST = 35000005  差异内容：ERR\_CODE\_AV\_MUSIC\_TEMPLATE\_NOT\_EXIST = 35000005 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_CONTROLLER\_NOT\_EXIST = 35000006  差异内容：ERR\_CODE\_CONTROLLER\_NOT\_EXIST = 35000006 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_CONTROLLER\_IS\_EXIST = 35000007  差异内容：ERR\_CODE\_CONTROLLER\_IS\_EXIST = 35000007 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_SERVICE\_NOT\_EXIST = 35000008  差异内容：ERR\_CODE\_SERVICE\_NOT\_EXIST = 35000008 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_SERVICE\_EXCEPTION = 35000009  差异内容：ERR\_CODE\_SERVICE\_EXCEPTION = 35000009 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_EXCEED\_MAX\_DATA\_SIZE = 35000010  差异内容：ERR\_CODE\_EXCEED\_MAX\_DATA\_SIZE = 35000010 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_WRITE\_RESULT\_EXCEPTION = 35000011  差异内容：ERR\_CODE\_WRITE\_RESULT\_EXCEPTION = 35000011 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateErrorCode；  API声明：ERR\_CODE\_AV\_MUSIC\_TEMPLATE\_ERROR = 35000012  差异内容：ERR\_CODE\_AV\_MUSIC\_TEMPLATE\_ERROR = 35000012 | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>;  差异内容：function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function createController(sessionId: string): Promise<AVSessionController>;  差异内容：function createController(sessionId: string): Promise<AVSessionController>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function isDesktopLyricSupported(): Promise<boolean>;  差异内容：function isDesktopLyricSupported(): Promise<boolean>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：interface DesktopLyricState  差异内容：interface DesktopLyricState | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DesktopLyricState；  API声明：isLocked: boolean;  差异内容：isLocked: boolean; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function onSessionCreate(callback: Callback<AVSessionDescriptor>): void;  差异内容：function onSessionCreate(callback: Callback<AVSessionDescriptor>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function onSessionDestroy(callback: Callback<AVSessionDescriptor>): void;  差异内容：function onSessionDestroy(callback: Callback<AVSessionDescriptor>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function onTopSessionChange(callback: Callback<AVSessionDescriptor>): void;  差异内容：function onTopSessionChange(callback: Callback<AVSessionDescriptor>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function offSessionCreate(callback?: Callback<AVSessionDescriptor>): void;  差异内容：function offSessionCreate(callback?: Callback<AVSessionDescriptor>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void;  差异内容：function offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function offTopSessionChange(callback?: Callback<AVSessionDescriptor>): void;  差异内容：function offTopSessionChange(callback?: Callback<AVSessionDescriptor>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：enableDesktopLyric(enable: boolean): Promise<void>;  差异内容：enableDesktopLyric(enable: boolean): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：setDesktopLyricVisible(visible: boolean): Promise<void>;  差异内容：setDesktopLyricVisible(visible: boolean): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：isDesktopLyricVisible(): Promise<boolean>;  差异内容：isDesktopLyricVisible(): Promise<boolean>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void;  差异内容：onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void;  差异内容：offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：setDesktopLyricState(state: DesktopLyricState): Promise<void>;  差异内容：setDesktopLyricState(state: DesktopLyricState): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：getDesktopLyricState(): Promise<DesktopLyricState>;  差异内容：getDesktopLyricState(): Promise<DesktopLyricState>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void;  差异内容：onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void;  差异内容：offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：interface AVSessionDescriptor  差异内容：interface AVSessionDescriptor | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionDescriptor；  API声明：sessionId: string;  差异内容：sessionId: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionDescriptor；  API声明：type: AVSessionType;  差异内容：type: AVSessionType; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionDescriptor；  API声明：sessionTag: string;  差异内容：sessionTag: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionDescriptor；  API声明：elementName: ElementName;  差异内容：elementName: ElementName; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionDescriptor；  API声明：isActive: boolean;  差异内容：isActive: boolean; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionDescriptor；  API声明：isTopSession: boolean;  差异内容：isTopSession: boolean; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：isDesktopLyricEnabled(): Promise<boolean>;  差异内容：isDesktopLyricEnabled(): Promise<boolean>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：onDesktopLyricEnabled(callback: Callback<boolean>): void;  差异内容：onDesktopLyricEnabled(callback: Callback<boolean>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：offDesktopLyricEnabled(callback?: Callback<boolean>): void;  差异内容：offDesktopLyricEnabled(callback?: Callback<boolean>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：setDesktopLyricVisible(visible: boolean): Promise<void>;  差异内容：setDesktopLyricVisible(visible: boolean): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：isDesktopLyricVisible(): Promise<boolean>;  差异内容：isDesktopLyricVisible(): Promise<boolean>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void;  差异内容：onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void;  差异内容：offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：setDesktopLyricState(state: DesktopLyricState): Promise<void>;  差异内容：setDesktopLyricState(state: DesktopLyricState): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：getDesktopLyricState(): Promise<DesktopLyricState>;  差异内容：getDesktopLyricState(): Promise<DesktopLyricState>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void;  差异内容：onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void;  差异内容：offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionErrorCode；  API声明：ERR\_CODE\_DESKTOP\_LYRIC\_NOT\_ENABLED = 6600110  差异内容：ERR\_CODE\_DESKTOP\_LYRIC\_NOT\_ENABLED = 6600110 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionErrorCode；  API声明：ERR\_CODE\_DESKTOP\_LYRIC\_NOT\_SUPPORTED = 6600111  差异内容：ERR\_CODE\_DESKTOP\_LYRIC\_NOT\_SUPPORTED = 6600111 | api/@ohos.multimedia.avsession.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimedia.avMusicTemplate.d.ts  差异内容：AVSessionKit | api/@ohos.multimedia.avMusicTemplate.d.ts |
