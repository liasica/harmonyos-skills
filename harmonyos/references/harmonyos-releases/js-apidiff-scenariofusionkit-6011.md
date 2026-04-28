---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-6011
title: Scenario Fusion Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Scenario Fusion Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f238e5f59f859ee3141e32db02d722b5ef1cdc19264d48a7163dc4334e025b05
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：atomicService；  API声明：enum FollowResult  差异内容：enum FollowResult | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowResult；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowResult；  API声明：FAILED = 1  差异内容：FAILED = 1 | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：atomicService；  API声明：interface FollowComponentParams  差异内容：interface FollowComponentParams | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowComponentParams；  API声明：pubId: string;  差异内容：pubId: string; | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowComponentParams；  API声明：channelId?: string;  差异内容：channelId?: string; | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowComponentParams；  API声明：offset?: Position | Edges | LocalizedEdges;  差异内容：offset?: Position | Edges | LocalizedEdges; | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：atomicService；  API声明：interface FollowCompleteResult  差异内容：interface FollowCompleteResult | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowCompleteResult；  API声明：code: FollowResult;  差异内容：code: FollowResult; | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：atomicService；  API声明：interface FollowComponentCallback  差异内容：interface FollowComponentCallback | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：FollowComponentCallback；  API声明：onFollowComplete: AsyncCallback<FollowCompleteResult>;  差异内容：onFollowComplete: AsyncCallback<FollowCompleteResult>; | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
| 新增API | NA | 类名：atomicService；  API声明：function showFollowComponent(ctx: UIContext, params: FollowComponentParams, callback: FollowComponentCallback): Promise<void>;  差异内容：function showFollowComponent(ctx: UIContext, params: FollowComponentParams, callback: FollowComponentCallback): Promise<void>; | api/@hms.core.atomicserviceComponent.atomicservice.d.ets |
