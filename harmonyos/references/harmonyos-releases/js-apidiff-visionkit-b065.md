---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-b065
title: Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:21+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:920a699eee93b6be8dcbc56446a66fddec606ef5380b11644fd9c02d85121d7b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 属性变更 | 类名：DocumentScanner；  API声明：onResult: (code: number, saveType: SaveOption, uris: string[]) => void;  差异内容：(code: number, saveType: SaveOption, uris: string[]) => void | 类名：DocumentScanner；  API声明：onResult: DocumentScannerResultCallback;  差异内容：DocumentScannerResultCallback | api/@hms.ai.DocumentScanner.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type DocumentScannerResultCallback = (code: number, saveType: SaveOption, uris: string[]) => void;  差异内容：declare type DocumentScannerResultCallback = (code: number, saveType: SaveOption, uris: string[]) => void; | api/@hms.ai.DocumentScanner.d.ets |
