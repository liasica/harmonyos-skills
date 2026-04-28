---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scankit-b123sp18
title: Scan Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Scan Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0844c7b29471907fec50161d652f607a838b1d582a00e628222e466d7a4cad0b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：customScan；  API声明：function init(options?: scanBarcode.ScanOptions): void;  差异内容：1000500001,401 | 类名：customScan；  API声明：function init(options?: scanBarcode.ScanOptions): void;  差异内容：1000500001,201,401 | api/@hms.core.scan.customScan.d.ts |
| 错误码变更 | 类名：customScan；  API声明：function start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void;  差异内容：1000500001,401 | 类名：customScan；  API声明：function start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void;  差异内容：1000500001,201,401 | api/@hms.core.scan.customScan.d.ts |
| 错误码变更 | 类名：customScan；  API声明：function start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>;  差异内容：1000500001,401 | 类名：customScan；  API声明：function start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>;  差异内容：1000500001,201,401 | api/@hms.core.scan.customScan.d.ts |
