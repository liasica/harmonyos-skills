---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scankit-b031
title: Scan Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Scan Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:71d5f7719c7e7f7278c18082e60da28c4045be32be66979bf760018ea68e3cf2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：scanBarcode；  API声明：function startScanForResult(context: common.Context, callback: AsyncCallback<ScanResult>): void;  差异内容：1000500001,401 | 类名：scanBarcode；  API声明：function startScanForResult(context: common.Context, callback: AsyncCallback<ScanResult>): void;  差异内容：1000500001,1000500002,401 | api/@hms.core.scan.scanBarcode.d.ts |
| 错误码变更 | 类名：scanBarcode；  API声明：function startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void;  差异内容：1000500001,401 | 类名：scanBarcode；  API声明：function startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void;  差异内容：1000500001,1000500002,401 | api/@hms.core.scan.scanBarcode.d.ts |
| 错误码变更 | 类名：scanBarcode；  API声明：function startScanForResult(context: common.Context, options?: ScanOptions): Promise<ScanResult>;  差异内容：1000500001,401 | 类名：scanBarcode；  API声明：function startScanForResult(context: common.Context, options?: ScanOptions): Promise<ScanResult>;  差异内容：1000500001,1000500002,401 | api/@hms.core.scan.scanBarcode.d.ts |
| 新增API | NA | 类名：generateBarcode；  API声明：function createBarcode(content: ArrayBuffer, options: CreateOptions): Promise<image.PixelMap>;  差异内容：function createBarcode(content: ArrayBuffer, options: CreateOptions): Promise<image.PixelMap>; | api/@hms.core.scan.generateBarcode.d.ts |
| 新增API | NA | 类名：customScan；  API声明：function rescan(): void;  差异内容：function rescan(): void; | api/@hms.core.scan.customScan.d.ts |
| 新增API | NA | 类名：ScanErrorCode；  API声明：SCAN\_SERVICE\_CANCELED = 1000500002  差异内容：SCAN\_SERVICE\_CANCELED = 1000500002 | api/@hms.core.scan.scanCore.d.ts |
