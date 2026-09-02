---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-fastkit-7002
title: FAST Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > FAST Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d2639efe451024b7c8a10f57e842138d2abacead76954ae4c60dad85dbfa618a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace schedulingOptimization  差异内容：declare namespace schedulingOptimization | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：schedulingOptimization；  API声明：export enum SceneType  差异内容：export enum SceneType | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：APP\_LAUNCH = 1  差异内容：APP\_LAUNCH = 1 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：PAGE\_TRANSITION = 2  差异内容：PAGE\_TRANSITION = 2 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：PAGE\_LOAD = 3  差异内容：PAGE\_LOAD = 3 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：NETWORK\_FILE\_PROCESSING = 4  差异内容：NETWORK\_FILE\_PROCESSING = 4 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：LOCAL\_FILE\_PROCESSING = 5  差异内容：LOCAL\_FILE\_PROCESSING = 5 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：PAGE\_DRAWING = 6  差异内容：PAGE\_DRAWING = 6 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：ANIMATION = 7  差异内容：ANIMATION = 7 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：MEDIA\_PLAYBACK = 8  差异内容：MEDIA\_PLAYBACK = 8 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneType；  API声明：MEDIA\_ENCODING\_AND\_DECODING = 9  差异内容：MEDIA\_ENCODING\_AND\_DECODING = 9 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：schedulingOptimization；  API声明：export enum SceneState  差异内容：export enum SceneState | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneState；  API声明：END = 0  差异内容：END = 0 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：SceneState；  API声明：BEGIN = 1  差异内容：BEGIN = 1 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：schedulingOptimization；  API声明：export enum DurationType  差异内容：export enum DurationType | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：DurationType；  API声明：SHORT = 1  差异内容：SHORT = 1 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：DurationType；  API声明：MEDIUM = 2  差异内容：MEDIUM = 2 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：DurationType；  API声明：LONG = 3  差异内容：LONG = 3 | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：schedulingOptimization；  API声明：interface PerfHintConfig  差异内容：interface PerfHintConfig | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：PerfHintConfig；  API声明：sceneType: SceneType;  差异内容：sceneType: SceneType; | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：PerfHintConfig；  API声明：sceneState: SceneState;  差异内容：sceneState: SceneState; | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：PerfHintConfig；  API声明：durationType: DurationType;  差异内容：durationType: DurationType; | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：PerfHintConfig；  API声明：tids: number[];  差异内容：tids: number[]; | api/@hms.fast.schedulingOptimization.d.ts |
| 新增API | NA | 类名：schedulingOptimization；  API声明：function perfHint(config: PerfHintConfig): Promise<void>;  差异内容：function perfHint(config: PerfHintConfig): Promise<void>; | api/@hms.fast.schedulingOptimization.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.fast.schedulingOptimization.d.ts  差异内容：FASTKit | api/@hms.fast.schedulingOptimization.d.ts |
