---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-7002
title: PDF Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > PDF Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6675bf70d6123530b547ccfb6ab06aa173e86e961ebcd92867b4a21187d53cfd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pdfViewManager；  API声明：export enum PresetRenderMode  差异内容：export enum PresetRenderMode | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PresetRenderMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PresetRenderMode；  API声明：DARKMODE = 1  差异内容：DARKMODE = 1 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明：export interface Point  差异内容：export interface Point | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：Point；  API声明：x: number;  差异内容：x: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：Point；  API声明：y: number;  差异内容：y: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明：export interface ViewRect  差异内容：export interface ViewRect | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ViewRect；  API声明：left: number;  差异内容：left: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ViewRect；  API声明：top: number;  差异内容：top: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ViewRect；  API声明：right: number;  差异内容：right: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ViewRect；  API声明：bottom: number;  差异内容：bottom: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageIndexFromViewPoint(viewPoint: Point): number;  差异内容：getPageIndexFromViewPoint(viewPoint: Point): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：viewRectToPDFRect(pageIndex: number, viewRect: ViewRect): pdfService.PdfRect;  差异内容：viewRectToPDFRect(pageIndex: number, viewRect: ViewRect): pdfService.PdfRect; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：viewPointToPDFPoint(pageIndex: number, viewPoint: Point): pdfService.PdfPoint;  差异内容：viewPointToPDFPoint(pageIndex: number, viewPoint: Point): pdfService.PdfPoint; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：pdfRectToViewRect(pageIndex: number, pdfRect: pdfService.PdfRect): ViewRect;  差异内容：pdfRectToViewRect(pageIndex: number, pdfRect: pdfService.PdfRect): ViewRect; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：pdfPointToViewPoint(pageIndex: number, pdfPoint: pdfService.PdfPoint): Point;  差异内容：pdfPointToViewPoint(pageIndex: number, pdfPoint: pdfService.PdfPoint): Point; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setRenderMode(renderMode: PresetRenderMode): void;  差异内容：setRenderMode(renderMode: PresetRenderMode): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：loadDocumentFromMemory(data: ArrayBuffer, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>;  差异内容：loadDocumentFromMemory(data: ArrayBuffer, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>; | api/@hms.officeservice.PdfView.d.ets |
