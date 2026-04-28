---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6012
title: ArkUI
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Release引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5edbb6b8dfa7bef0121c604339f6c1d719b7023890841013cad9b829d00f924a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：RenderNode；  API声明：get shapeClip(): ShapeClip;  差异内容：SystemCapability.ArkUI.ArkUI.clip | 类名：RenderNode；  API声明：get shapeClip(): ShapeClip;  差异内容：SystemCapability.ArkUI.ArkUI.Full | api/arkui/RenderNode.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void;  差异内容：NA | 类名：CommonMethod；  API声明：onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T;  差异内容：T | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ContentTransitionEffect  差异内容：declare class ContentTransitionEffect | component/common.d.ts |
| 新增API | NA | 类名：ContentTransitionEffect；  API声明：static get IDENTITY(): ContentTransitionEffect;  差异内容：static get IDENTITY(): ContentTransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：ContentTransitionEffect；  API声明：static get OPACITY(): ContentTransitionEffect;  差异内容：static get OPACITY(): ContentTransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：contentTransition(transition: ContentTransitionEffect): ImageAttribute;  差异内容：contentTransition(transition: ContentTransitionEffect): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：PosterOptions；  API声明：contentTransitionEffect?: ContentTransitionEffect;  差异内容：contentTransitionEffect?: ContentTransitionEffect; | component/video.d.ts |
