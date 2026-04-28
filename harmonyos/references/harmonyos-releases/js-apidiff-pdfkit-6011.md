---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-6011
title: PDF Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > PDF Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:be8db2a0569e5e08f110475472975ba1dd8c676f29b0b301763ecc8267f0ed32
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pdfService；  API声明：export interface SearchResultData  差异内容：export interface SearchResultData | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchResultData；  API声明：pageIndex: number;  差异内容：pageIndex: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchResultData；  API声明：rects: PdfRect[];  差异内容：rects: PdfRect[]; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchResultData；  API声明：contextString: string;  差异内容：contextString: string; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService；  API声明：export interface SearchOptions  差异内容：export interface SearchOptions | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions；  API声明：startIndex?: number;  差异内容：startIndex?: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions；  API声明：endIndex?: number;  差异内容：endIndex?: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions；  API声明：isMatchWholeWord?: boolean;  差异内容：isMatchWholeWord?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions；  API声明：isMatchCase?: boolean;  差异内容：isMatchCase?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions；  API声明：contextStringLength?: number;  差异内容：contextStringLength?: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService；  API声明：export type SearchKeyCallback = (results: SearchResultData[]) => boolean;  差异内容：export type SearchKeyCallback = (results: SearchResultData[]) => boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PdfDocument；  API声明：searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise<void>;  差异内容：searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise<void>; | api/@hms.officeservice.pdfservice.d.ts |
