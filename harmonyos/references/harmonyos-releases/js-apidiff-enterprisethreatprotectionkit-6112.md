---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisethreatprotectionkit-6112
title: Enterprise Threat Protection Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > Enterprise Threat Protection Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:14e1ec250230bcf059b682fdd3d839a6ac36ce98ba15113d06de8b6cddc29c3b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：virusRemediation；  API声明：function isolateThreatFile(path: string): Promise<string>;  差异内容：NA | 类名：virusRemediation；  API声明：function isolateThreatFile(path: string): Promise<string>;  差异内容：1023801001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation；  API声明：function restoreIsolatedFile(id: string): Promise<string>;  差异内容：NA | 类名：virusRemediation；  API声明：function restoreIsolatedFile(id: string): Promise<string>;  差异内容：1023801001,1023802003,1023803001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation；  API声明：function removeIsolatedFile(id: string): Promise<void>;  差异内容：NA | 类名：virusRemediation；  API声明：function removeIsolatedFile(id: string): Promise<void>;  差异内容：1023801001,1023803001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation；  API声明：function queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void;  差异内容：NA | 类名：virusRemediation；  API声明：function queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void;  差异内容：1023801001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation；  API声明：function openFile(path: string): Promise<number>;  差异内容：NA | 类名：virusRemediation；  API声明：function openFile(path: string): Promise<number>;  差异内容：1023801001,1023803001,1023804001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation；  API声明：function scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void;  差异内容：NA | 类名：virusRemediation；  API声明：function scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void;  差异内容：1023801001 | api/@hms.pcService.virusRemediation.d.ts |
