---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-liveviewkit-6003
title: Live View Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Live View Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:18+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:406c468a788e7377fb31182a9bff974183aa770957cd9ca2450fc2921c4e70bf
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：liveViewManager；  API声明：export enum BackgroundType  差异内容：export enum BackgroundType | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：BackgroundType；  API声明：SYS\_BACKGROUND\_UNDEFINED = 0  差异内容：SYS\_BACKGROUND\_UNDEFINED = 0 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：BackgroundType；  API声明：SYS\_BACKGROUND\_FLIGHT\_MOON = 100  差异内容：SYS\_BACKGROUND\_FLIGHT\_MOON = 100 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：BackgroundType；  API声明：SYS\_BACKGROUND\_FLIGHT\_SUNSET = 101  差异内容：SYS\_BACKGROUND\_FLIGHT\_SUNSET = 101 | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PrimaryData；  API声明：backgroundType?: BackgroundType;  差异内容：backgroundType?: BackgroundType; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CapsuleData；  API声明：tailIcon?: string | image.PixelMap;  差异内容：tailIcon?: string | image.PixelMap; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CapsuleData；  API声明：isTailIconDisplayed?: boolean;  差异内容：isTailIconDisplayed?: boolean; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ProgressCapsule；  API声明：content?: string;  差异内容：content?: string; | api/@hms.core.liveview.liveViewManager.d.ts |
