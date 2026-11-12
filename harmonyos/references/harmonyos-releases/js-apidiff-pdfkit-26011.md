---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-26011
title: PDF Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > PDF Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:144e5f90680252dfee9a543ec0967d06c2faed8128da815ebfc62aec3ffbbd8c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：STAMP = 13  差异内容：STAMP = 13 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：INK = 15  差异内容：INK = 15 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明：export enum PenType  差异内容：export enum PenType | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PenType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明：export interface PenStyle  差异内容：export interface PenStyle | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PenStyle；  API声明：type?: PenType;  差异内容：type?: PenType; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PenStyle；  API声明：lineColor?: number;  差异内容：lineColor?: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PenStyle；  API声明：lineWidth?: number;  差异内容：lineWidth?: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PenStyle；  API声明：opacity?: number;  差异内容：opacity?: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明：export class HighlightRect  差异内容：export class HighlightRect | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：HighlightRect；  API声明：pageIndex: number;  差异内容：pageIndex: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：HighlightRect；  API声明：pdfRect: pdfService.PdfRect;  差异内容：pdfRect: pdfService.PdfRect; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：HighlightRect；  API声明：color: number;  差异内容：color: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setHighlightRectsWithColors(highlightRects: HighlightRect[]): void;  差异内容：setHighlightRectsWithColors(highlightRects: HighlightRect[]): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：enablePen(style?: PenStyle): void;  差异内容：enablePen(style?: PenStyle): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：disablePen(): void;  差异内容：disablePen(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：enableEraser(): void;  差异内容：enableEraser(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：disableEraser(): void;  差异内容：disableEraser(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：changePenStyle(style: PenStyle): void;  差异内容：changePenStyle(style: PenStyle): void; | api/@hms.officeservice.PdfView.d.ets |
