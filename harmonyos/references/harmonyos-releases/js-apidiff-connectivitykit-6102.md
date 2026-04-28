---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6102
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta2引入的变更 > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9520024b5be8f167d0019654d01689613b16e684b316cd695184d539f81d806e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：tag；  API声明：function on(type: 'readerModeWithInterval', elementName: ElementName, discTech: number[], callback: Callback<TagInfo>, interval: number): void;  差异内容：function on(type: 'readerModeWithInterval', elementName: ElementName, discTech: number[], callback: Callback<TagInfo>, interval: number): void; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：tag；  API声明：function off(type: 'readerModeWithInterval', elementName: ElementName, callback?: Callback<TagInfo>): void;  差异内容：function off(type: 'readerModeWithInterval', elementName: ElementName, callback?: Callback<TagInfo>): void; | api/@ohos.nfc.tag.d.ts |
