---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-510
title: PDF Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > PDF Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:13+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:597fa637cfa8b29f8bcaa3849c5b36ef4a9f5563aae7ad21e19639fcd624bcec
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pdfService；  API声明：export class PdfAction  差异内容：export class PdfAction | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfAction；  API声明：type: PdfActionType;  差异内容：type: PdfActionType; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService；  API声明：export class PdfActionGoTo  差异内容：export class PdfActionGoTo | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfActionGoTo；  API声明：destInfo: DestInfo;  差异内容：destInfo: DestInfo; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService；  API声明：export class PdfActionHyperlink  差异内容：export class PdfActionHyperlink | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfActionHyperlink；  API声明：hyperlink: string;  差异内容：hyperlink: string; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService；  API声明：export enum PdfActionType  差异内容：export enum PdfActionType | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfActionType；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfActionType；  API声明：GOTO = 1  差异内容：GOTO = 1 | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfActionType；  API声明：HYPERLINK = 2  差异内容：HYPERLINK = 2 | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService；  API声明：export class PixelOptions  差异内容：export class PixelOptions | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PixelOptions；  API声明：isGray?: boolean;  差异内容：isGray?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PixelOptions；  API声明：drawAnnotations?: boolean;  差异内容：drawAnnotations?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PixelOptions；  API声明：isTransparent?: boolean;  差异内容：isTransparent?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PdfAnnotationInfo；  API声明：action?: PdfAction;  差异内容：action?: PdfAction; | api/@hms.officeservice.pdfservice.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PdfPage；  API声明：getAreaPixelMapWithOptions(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap;  差异内容：getAreaPixelMapWithOptions(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap; | api/@hms.officeservice.pdfservice.d.ts |
