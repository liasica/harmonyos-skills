---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-appgallerykit-5032
title: App Gallery Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > App Gallery Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:33+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e3ca43ebfda47166787063d224d68f79e24aa089a8a766c472782b1434ede4b4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace appInfoManager  差异内容： declare namespace appInfoManager | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager；  API声明： export interface DynamicIconInfo  差异内容： export interface DynamicIconInfo | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：DynamicIconInfo；  API声明：readonly iconUrl: string;  差异内容：readonly iconUrl: string; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：DynamicIconInfo；  API声明：readonly iconId: string;  差异内容：readonly iconId: string; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：DynamicIconInfo；  API声明：readonly enabled: boolean;  差异内容：readonly enabled: boolean; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager；  API声明：function queryDynamicIcons(): Promise<DynamicIconInfo[]>;  差异内容：function queryDynamicIcons(): Promise<DynamicIconInfo[]>; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager；  API声明：function selectDynamicIcon(iconId: string): Promise<void>;  差异内容：function selectDynamicIcon(iconId: string): Promise<void>; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager；  API声明：function disableDynamicIcon(): Promise<void>;  差异内容：function disableDynamicIcon(): Promise<void>; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| kit变更 | NA | AppGalleryKit | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
