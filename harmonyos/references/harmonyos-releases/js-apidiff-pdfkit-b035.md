---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-b035
title: PDF Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > PDF Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a5e238c327e827ec8a06ffaf4244310c01fb3a66f2402ecdc86a3bafa800c780
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace pdfViewManager  差异内容： declare namespace pdfViewManager | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export enum SupportedAnnotationType  差异内容： export enum SupportedAnnotationType | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：FREE\_TEXT = 3  差异内容：FREE\_TEXT = 3 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：LINE = 4  差异内容：LINE = 4 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：SQUARE = 5  差异内容：SQUARE = 5 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：OVAL = 6  差异内容：OVAL = 6 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：POLYGON = 7  差异内容：POLYGON = 7 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：HIGHLIGHT = 9  差异内容：HIGHLIGHT = 9 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：UNDERLINE = 10  差异内容：UNDERLINE = 10 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SupportedAnnotationType；  API声明：STRIKETHROUGH = 12  差异内容：STRIKETHROUGH = 12 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export enum AnnotationEditType  差异内容： export enum AnnotationEditType | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationEditType；  API声明：ADD = 0  差异内容：ADD = 0 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationEditType；  API声明：MODIFY = 1  差异内容：MODIFY = 1 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationEditType；  API声明：DELETE = 2  差异内容：DELETE = 2 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class PageRects  差异内容： export class PageRects | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PageRects；  API声明：pageIndex: number;  差异内容：pageIndex: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PageRects；  API声明：rectArray: Array<pdfService.PdfRect>;  差异内容：rectArray: Array<pdfService.PdfRect>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class SelectedRects  差异内容： export class SelectedRects | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedRects；  API声明：isRotated: number;  差异内容：isRotated: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export enum RedirectType  差异内容： export enum RedirectType | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：RedirectType；  API声明：URI = 6  差异内容：URI = 6 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：RedirectType；  API声明：LAUNCH = 4  差异内容：LAUNCH = 4 | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class RedirectInfo  差异内容： export class RedirectInfo | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：RedirectInfo；  API声明：content: string;  差异内容：content: string; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：RedirectInfo；  API声明：actionType: RedirectType;  差异内容：actionType: RedirectType; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class SelectedAnnotation  差异内容： export class SelectedAnnotation | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedAnnotation；  API声明：readonly annotationIndex: number;  差异内容：readonly annotationIndex: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedAnnotation；  API声明：readonly pageIndex: number;  差异内容：readonly pageIndex: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedAnnotation；  API声明：readonly annotationType: SupportedAnnotationType;  差异内容：readonly annotationType: SupportedAnnotationType; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedAnnotation；  API声明：readonly color: number;  差异内容：readonly color: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedAnnotation；  API声明：readonly rect?: Array<pdfService.PdfRect>;  差异内容：readonly rect?: Array<pdfService.PdfRect>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：SelectedAnnotation；  API声明：readonly points?: Array<pdfService.PdfPoint>;  差异内容：readonly points?: Array<pdfService.PdfPoint>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class ScrollParam  差异内容： export class ScrollParam | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ScrollParam；  API声明：offsetX: number;  差异内容：offsetX: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ScrollParam；  API声明：offsetY: number;  差异内容：offsetY: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ScrollParam；  API声明：pdfWidth: number;  差异内容：pdfWidth: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ScrollParam；  API声明：pdfHeight: number;  差异内容：pdfHeight: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ScrollParam；  API声明：viewWidth: number;  差异内容：viewWidth: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ScrollParam；  API声明：viewHeight: number;  差异内容：viewHeight: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class TextSelectedParam  差异内容： export class TextSelectedParam | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：TextSelectedParam；  API声明：text: string;  差异内容：text: string; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：TextSelectedParam；  API声明：pdfRect: Array<SelectedRects>;  差异内容：pdfRect: Array<SelectedRects>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class ImageSelectedParam  差异内容： export class ImageSelectedParam | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ImageSelectedParam；  API声明：imageType: pdfService.ImageFormat;  差异内容：imageType: pdfService.ImageFormat; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ImageSelectedParam；  API声明：buffer?: ArrayBuffer;  差异内容：buffer?: ArrayBuffer; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ImageSelectedParam；  API声明：pdfRect?: pdfService.PdfRect;  差异内容：pdfRect?: pdfService.PdfRect; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：ImageSelectedParam；  API声明：pageIndex?: number;  差异内容：pageIndex?: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class AnnotationChangedParam  差异内容： export class AnnotationChangedParam | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationChangedParam；  API声明：color: number;  差异内容：color: number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationChangedParam；  API声明：annotationType: SupportedAnnotationType;  差异内容：annotationType: SupportedAnnotationType; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationChangedParam；  API声明：pageIndexArray: Array<number>;  差异内容：pageIndexArray: Array<number>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：AnnotationChangedParam；  API声明：controlType: AnnotationEditType;  差异内容：controlType: AnnotationEditType; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：pdfViewManager；  API声明： export class PdfController  差异内容： export class PdfController | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setViewOffset(offsetX: number, offsetY: number, refreshView: boolean): void;  差异内容：setViewOffset(offsetX: number, offsetY: number, refreshView: boolean): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPagePixelMap(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>;  差异内容：getPagePixelMap(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerScrollListener(listener: Callback<ScrollParam>): void;  差异内容：registerScrollListener(listener: Callback<ScrollParam>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：enablePageDrag(verticalEnabled: boolean, horizontalEnabled: boolean): void;  差异内容：enablePageDrag(verticalEnabled: boolean, horizontalEnabled: boolean): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：loadDocument(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>;  差异内容：loadDocument(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：releaseDocument(): void;  差异内容：releaseDocument(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setHighlightRects(rectArray: Array<PageRects>, color?: number): void;  差异内容：setHighlightRects(rectArray: Array<PageRects>, color?: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setHighlightText(pageIndex: number, textArray: string[], color: number): void;  差异内容：setHighlightText(pageIndex: number, textArray: string[], color: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setPageZoom(zoom: number): void;  差异内容：setPageZoom(zoom: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageZoom(): number;  差异内容：getPageZoom(): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setPageLayout(columnCount: pdfService.PageLayout): void;  差异内容：setPageLayout(columnCount: pdfService.PageLayout): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageLayout(): pdfService.PageLayout;  差异内容：getPageLayout(): pdfService.PageLayout; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setPageContinuous(isContinuous: boolean): void;  差异内容：setPageContinuous(isContinuous: boolean): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：isPageContinuous(): boolean;  差异内容：isPageContinuous(): boolean; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setPageFit(pageFit: pdfService.PageFit): void;  差异内容：setPageFit(pageFit: pdfService.PageFit): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageFit(): pdfService.PageFit;  差异内容：getPageFit(): pdfService.PageFit; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setPageSpacing(horizontal: number, vertical?: number): void;  差异内容：setPageSpacing(horizontal: number, vertical?: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageHorizontalSpacing(): number;  差异内容：getPageHorizontalSpacing(): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageVerticalSpacing(): number;  差异内容：getPageVerticalSpacing(): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageCount(): number;  差异内容：getPageCount(): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageIndex(): number;  差异内容：getPageIndex(): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：goToPage(pageIndex: number): void;  差异内容：goToPage(pageIndex: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setPageRotation(pageIndex: number, angle: pdfService.RotationAngle): void;  差异内容：setPageRotation(pageIndex: number, angle: pdfService.RotationAngle): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getPageRotation(pageIndex: number): pdfService.RotationAngle;  差异内容：getPageRotation(pageIndex: number): pdfService.RotationAngle; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void;  差异内容：enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：addMarkupAnnotation(annotationType: SupportedAnnotationType, selectedRects: Array<SelectedRects>, color: number): void;  差异内容：addMarkupAnnotation(annotationType: SupportedAnnotationType, selectedRects: Array<SelectedRects>, color: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：disableAnnotation(): void;  差异内容：disableAnnotation(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：deleteSelectedAnnotation(annotationIndex: number, pageIndex: number): void;  差异内容：deleteSelectedAnnotation(annotationIndex: number, pageIndex: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：updateMarkupAnnotation(annotationIndex: number, pageIndex: number, color: number): void;  差异内容：updateMarkupAnnotation(annotationIndex: number, pageIndex: number, color: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：saveDocument(path: string, onProgress?: Callback<number>): Promise<number>;  差异内容：saveDocument(path: string, onProgress?: Callback<number>): Promise<number>; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerSelectedRectsChangedListener(listener: Callback<Array<SelectedRects>>): void;  差异内容：registerSelectedRectsChangedListener(listener: Callback<Array<SelectedRects>>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerPageFitChangedListener(listener: Callback<pdfService.PageFit>): void;  差异内容：registerPageFitChangedListener(listener: Callback<pdfService.PageFit>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerPageChangedListener(listener: Callback<number>): void;  差异内容：registerPageChangedListener(listener: Callback<number>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerScaleChangedListener(listener: Callback<number>): void;  差异内容：registerScaleChangedListener(listener: Callback<number>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerTextSelectedListener(listener: Callback<TextSelectedParam>): void;  差异内容：registerTextSelectedListener(listener: Callback<TextSelectedParam>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerAnnotationSelectedListener(listener: Callback<SelectedAnnotation>): void;  差异内容：registerAnnotationSelectedListener(listener: Callback<SelectedAnnotation>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerImageSelectedListener(listener: Callback<ImageSelectedParam>): void;  差异内容：registerImageSelectedListener(listener: Callback<ImageSelectedParam>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerActionClickListener(listener: Callback<RedirectInfo>): void;  差异内容：registerActionClickListener(listener: Callback<RedirectInfo>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerAnnotationChangedListener(listener: Callback<AnnotationChangedParam>): void;  差异内容：registerAnnotationChangedListener(listener: Callback<AnnotationChangedParam>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：registerPageCountChangedListener(listener: Callback<number>): void;  差异内容：registerPageCountChangedListener(listener: Callback<number>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：searchKey(text: string, listener: Callback<number>): void;  差异内容：searchKey(text: string, listener: Callback<number>): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：clearSearch(): void;  差异内容：clearSearch(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：getSearchIndex(): number;  差异内容：getSearchIndex(): number; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfController；  API声明：setSearchIndex(pageIndex: number): void;  差异内容：setSearchIndex(pageIndex: number): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：global；  API声明： declare struct PdfView  差异内容： declare struct PdfView | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfView；  API声明：controller: pdfViewManager.PdfController;  差异内容：controller: pdfViewManager.PdfController; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfView；  API声明：pageLayout: pdfService.PageLayout;  差异内容：pageLayout: pdfService.PageLayout; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfView；  API声明：isContinuous: boolean;  差异内容：isContinuous: boolean; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfView；  API声明：showScroll: boolean;  差异内容：showScroll: boolean; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfView；  API声明：pageFit: pdfService.PageFit;  差异内容：pageFit: pdfService.PageFit; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfView；  API声明：build(): void;  差异内容：build(): void; | api/@hms.officeservice.PdfView.d.ets |
| 新增API | NA | 类名：PdfDocument；  API声明：getRootBookmarks(): Array<Bookmark>;  差异内容：getRootBookmarks(): Array<Bookmark>; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfPage；  API声明：getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap;  差异内容：getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfPage；  API声明：release(): void;  差异内容：release(): void; | api/@hms.officeservice.pdfservice.d.ts |
