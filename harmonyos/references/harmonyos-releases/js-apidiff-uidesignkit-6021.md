---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-6021
title: UI Design Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:442ee3b6e5ba8349c1551d12357a0f0f37addaa954375fddf85c0d1acb52c74e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：global；  API声明：export declare enum HdsSceneType  差异内容：NA | 类名：global；  API声明：export declare enum HdsSceneType  差异内容：form | api/@hms.hds.HdsVisualComponent.d.ets |
| API卡片权限变更 | 类名：global；  API声明：declare type HdsSceneFinishCallback = () => void;  差异内容：NA | 类名：global；  API声明：declare type HdsSceneFinishCallback = () => void;  差异内容：form | api/@hms.hds.HdsVisualComponent.d.ets |
| API卡片权限变更 | 类名：global；  API声明：export class HdsSceneController  差异内容：NA | 类名：global；  API声明：export class HdsSceneController  差异内容：form | api/@hms.hds.HdsVisualComponent.d.ets |
| API卡片权限变更 | 类名：global；  API声明：export declare class HdsVisualComponentAttribute  差异内容：NA | 类名：global；  API声明：export declare class HdsVisualComponentAttribute  差异内容：form | api/@hms.hds.HdsVisualComponent.d.ets |
| API卡片权限变更 | 类名：HdsVisualComponentAttribute；  API声明：scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.ExpectedFrameRateRange): HdsVisualComponentAttribute;  差异内容：NA | 类名：HdsVisualComponentAttribute；  API声明：scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.ExpectedFrameRateRange): HdsVisualComponentAttribute;  差异内容：form | api/@hms.hds.HdsVisualComponent.d.ets |
| API卡片权限变更 | 类名：global；  API声明：export declare const HdsVisualComponent: HdsVisualComponentInterface;  差异内容：NA | 类名：global；  API声明：export declare const HdsVisualComponent: HdsVisualComponentInterface;  差异内容：form | api/@hms.hds.HdsVisualComponent.d.ets |
