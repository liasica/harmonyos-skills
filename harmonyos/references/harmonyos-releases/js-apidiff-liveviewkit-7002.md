---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-liveviewkit-7002
title: Live View Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Live View Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f9267a8225ea1f6260b91c8be403e1e68559d56f81996e07dadec616d7f8f77a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：liveViewManager；  API声明：function startLiveView(liveView: LiveView): Promise<LiveViewResult>;  差异内容：NA | 类名：liveViewManager；  API声明：function startLiveView(liveView: LiveView): Promise<LiveViewResult>;  差异内容：1003500021 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增错误码 | 类名：liveViewManager；  API声明：function updateLiveView(liveView: LiveView): Promise<LiveViewResult>;  差异内容：NA | 类名：liveViewManager；  API声明：function updateLiveView(liveView: LiveView): Promise<LiveViewResult>;  差异内容：1003500021 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增错误码 | 类名：liveViewManager；  API声明：function stopLiveView(liveView: LiveView): Promise<LiveViewResult>;  差异内容：NA | 类名：liveViewManager；  API声明：function stopLiveView(liveView: LiveView): Promise<LiveViewResult>;  差异内容：1003500021 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增错误码 | 类名：liveViewManager；  API声明：function startLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>;  差异内容：NA | 类名：liveViewManager；  API声明：function startLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>;  差异内容：1003500021 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增错误码 | 类名：liveViewManager；  API声明：function stopLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>;  差异内容：NA | 类名：liveViewManager；  API声明：function stopLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>;  差异内容：1003500021 | api/@hms.core.liveview.liveViewManager.d.ts |
| 属性变更 | 类名：PrimaryData；  API声明：layoutData?: ProgressLayout | PickupLayout | FlightLayout | ScoreLayout | NavigationLayout;  差异内容：ProgressLayout,PickupLayout,FlightLayout,ScoreLayout,NavigationLayout | 类名：PrimaryData；  API声明：layoutData?: ProgressLayout | PickupLayout | FlightLayout | ScoreLayout | NavigationLayout | CustomLayout;  差异内容：ProgressLayout,PickupLayout,FlightLayout,ScoreLayout,NavigationLayout,CustomLayout | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface CardInfo  差异内容：export interface CardInfo | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增API | NA | 类名：CardInfo；  API声明：pagePath: string;  差异内容：pagePath: string; | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增API | NA | 类名：CardInfo；  API声明：storage?: LocalStorage;  差异内容：storage?: LocalStorage; | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class LiveViewCardExtensionAbility  差异内容：export default class LiveViewCardExtensionAbility | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveViewCardExtensionAbility；  API声明：public context: LiveViewCardExtensionContext;  差异内容：public context: LiveViewCardExtensionContext; | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增API | NA | 类名：LiveViewCardExtensionAbility；  API声明：public onRender(param: Record<string, string>): CardInfo;  差异内容：public onRender(param: Record<string, string>): CardInfo; | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class LiveViewCardExtensionContext  差异内容：export default class LiveViewCardExtensionContext | api/@hms.core.liveview.LiveViewCardExtensionContext.d.ts |
| 新增API | NA | 类名：LiveView；  API声明：shareUrl?: string;  差异内容：shareUrl?: string; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：LayoutType；  API声明：LAYOUT\_TYPE\_CUSTOM = 100  差异内容：LAYOUT\_TYPE\_CUSTOM = 100 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：export interface CustomLayout  差异内容：export interface CustomLayout | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：CustomLayout；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：CustomLayout；  API声明：abilityParameters?: Record<string, string>;  差异内容：abilityParameters?: Record<string, string>; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.liveview.LiveViewCardExtensionAbility.d.ts  差异内容：LiveViewKit | api/@hms.core.liveview.LiveViewCardExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.liveview.LiveViewCardExtensionContext.d.ts  差异内容：LiveViewKit | api/@hms.core.liveview.LiveViewCardExtensionContext.d.ts |
