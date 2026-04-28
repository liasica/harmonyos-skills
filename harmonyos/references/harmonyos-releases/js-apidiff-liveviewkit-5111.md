---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-liveviewkit-5111
title: Live View Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Live View Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d4ed2738f1a86ea9d0407e3840a805cff7f709f147c376d233d9cc0dafcb0f3e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：liveViewManager；  API声明：export interface ServiceButton  差异内容：export interface ServiceButton | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：ServiceButton；  API声明：name?: string;  差异内容：name?: string; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：ServiceButton；  API声明：clickAction?: WantAgent;  差异内容：clickAction?: WantAgent; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LayoutData；  API声明：isServiceButtonsDisplayed?: boolean;  差异内容：isServiceButtonsDisplayed?: boolean; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LayoutData；  API声明：serviceButtons?: Array<ServiceButton>;  差异内容：serviceButtons?: Array<ServiceButton>; | api/@hms.core.liveview.liveViewManager.d.ts |
