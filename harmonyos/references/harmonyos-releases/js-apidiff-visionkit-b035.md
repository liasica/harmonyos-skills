---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-b035
title: Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:33+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ef5940f85b7ad355b55cff6fb414e9a1bf5cf84cf836a7617dda154705eb6e0d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace visionImageAnalyzer  差异内容： declare namespace visionImageAnalyzer | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： class VisionImageAnalyzerController  差异内容： class VisionImageAnalyzerController | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：setImageAnalyzerVisibility(visibility: ImageAnalyzerVisibility): void;  差异内容：setImageAnalyzerVisibility(visibility: ImageAnalyzerVisibility): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：setAIButtonPosition(position: Rect): void;  差异内容：setAIButtonPosition(position: Rect): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：setAIButtonVisibility(visible: boolean): void;  差异内容：setAIButtonVisibility(visible: boolean): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：setCustomTextMenuItems(menus: Menu[]): void;  差异内容：setCustomTextMenuItems(menus: Menu[]): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：startSubjectAnalyzer(): void;  差异内容：startSubjectAnalyzer(): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：setCustomSubjectMenuItems(menus: Menu[]): void;  差异内容：setCustomSubjectMenuItems(menus: Menu[]): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：setSelectedSubjects(subjectIds: number[]): void;  差异内容：setSelectedSubjects(subjectIds: number[]): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：getSelectedSubjects(): Promise<Subject[] | null>;  差异内容：getSelectedSubjects(): Promise<Subject[] | null>; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：getSubject(point: visionBase.Point): Promise<Subject | null>;  差异内容：getSubject(point: visionBase.Point): Promise<Subject | null>; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：getSubjectsImage(subjectIds: number[]): Promise<PixelMap | null>;  差异内容：getSubjectsImage(subjectIds: number[]): Promise<PixelMap | null>; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：startObjectSearch(): Promise<boolean>;  差异内容：startObjectSearch(): Promise<boolean>; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：stopObjectSearch(): void;  差异内容：stopObjectSearch(): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'aiButtonStatusChange', callback: Callback<AIButtonStatus>): void;  差异内容：on(type: 'aiButtonStatusChange', callback: Callback<AIButtonStatus>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'aiButtonStatusChange', callback?: Callback<AIButtonStatus>): void;  差异内容：off(type: 'aiButtonStatusChange', callback?: Callback<AIButtonStatus>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'imageAnalyzerVisibilityChange', callback: Callback<ImageAnalyzerVisibility>): void;  差异内容：on(type: 'imageAnalyzerVisibilityChange', callback: Callback<ImageAnalyzerVisibility>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'imageAnalyzerVisibilityChange', callback?: Callback<ImageAnalyzerVisibility>): void;  差异内容：off(type: 'imageAnalyzerVisibilityChange', callback?: Callback<ImageAnalyzerVisibility>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'textAnalysis', callback: Callback<string>): void;  差异内容：on(type: 'textAnalysis', callback: Callback<string>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'textAnalysis', callback?: Callback<string>): void;  差异内容：off(type: 'textAnalysis', callback?: Callback<string>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'selectedTextChange', callback: Callback<string>): void;  差异内容：on(type: 'selectedTextChange', callback: Callback<string>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'selectedTextChange', callback?: Callback<string>): void;  差异内容：off(type: 'selectedTextChange', callback?: Callback<string>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'subjectAnalysis', callback: Callback<Subject[]>): void;  差异内容：on(type: 'subjectAnalysis', callback: Callback<Subject[]>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'subjectAnalysis', callback?: Callback<Subject[]>): void;  差异内容：off(type: 'subjectAnalysis', callback?: Callback<Subject[]>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'selectedSubjectsChange', callback: Callback<Subject[]>): void;  差异内容：on(type: 'selectedSubjectsChange', callback: Callback<Subject[]>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'selectedSubjectsChange', callback?: Callback<Subject[]>): void;  差异内容：off(type: 'selectedSubjectsChange', callback?: Callback<Subject[]>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：on(type: 'analyzerFailed', callback: ErrorCallback): void;  差异内容：on(type: 'analyzerFailed', callback: ErrorCallback): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：off(type: 'analyzerFailed', callback?: ErrorCallback): void;  差异内容：off(type: 'analyzerFailed', callback?: ErrorCallback): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： enum ImageAnalyzerVisibility  差异内容： enum ImageAnalyzerVisibility | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerVisibility；  API声明：SHOWN = 0  差异内容：SHOWN = 0 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerVisibility；  API声明：HIDDEN = 1  差异内容：HIDDEN = 1 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： enum AIButtonStatus  差异内容： enum AIButtonStatus | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：AIButtonStatus；  API声明：SELECTED = 0  差异内容：SELECTED = 0 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：AIButtonStatus；  API声明：UNSELECTED = 1  差异内容：UNSELECTED = 1 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：AIButtonStatus；  API声明：HIDDEN = 2  差异内容：HIDDEN = 2 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： enum SelectedStatus  差异内容： enum SelectedStatus | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：SelectedStatus；  API声明：SELECTED = 0  差异内容：SELECTED = 0 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：SelectedStatus；  API声明：UNSELECTED = 1  差异内容：UNSELECTED = 1 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： interface Subject  差异内容： interface Subject | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Subject；  API声明：id: number;  差异内容：id: number; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Subject；  API声明：image: PixelMap;  差异内容：image: PixelMap; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Subject；  API声明：boundingBox: Rect;  差异内容：boundingBox: Rect; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： interface Rect  差异内容： interface Rect | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Rect；  API声明：left?: number;  差异内容：left?: number; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Rect；  API声明：top?: number;  差异内容：top?: number; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Rect；  API声明：right?: number;  差异内容：right?: number; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Rect；  API声明：bottom?: number;  差异内容：bottom?: number; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： interface Menu  差异内容： interface Menu | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Menu；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：Menu；  API声明：action: Callback<string | Subject[]>;  差异内容：action: Callback<string | Subject[]>; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：CardRecognition；  API声明：cardRecognitionConfig?: CardRecognitionConfig;  差异内容：cardRecognitionConfig?: CardRecognitionConfig; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global；  API声明： declare interface CardRecognitionConfig  差异内容： declare interface CardRecognitionConfig | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionConfig；  API声明：defaultShootingMode?: ShootingMode;  差异内容：defaultShootingMode?: ShootingMode; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionConfig；  API声明：isPhotoSelectionSupported?: boolean;  差异内容：isPhotoSelectionSupported?: boolean; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionConfig；  API声明：cardContentConfig?: CardContentConfig;  差异内容：cardContentConfig?: CardContentConfig; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global；  API声明： declare enum ShootingMode  差异内容： declare enum ShootingMode | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：ShootingMode；  API声明：AUTO = 0  差异内容：AUTO = 0 | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：ShootingMode；  API声明：MANUAL = 1  差异内容：MANUAL = 1 | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global；  API声明： declare interface CardContentConfig  差异内容： declare interface CardContentConfig | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardContentConfig；  API声明：bankCard?: BankCardConfig;  差异内容：bankCard?: BankCardConfig; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global；  API声明： declare interface BankCardConfig  差异内容： declare interface BankCardConfig | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：BankCardConfig；  API声明：isBankNumberDialogShown?: boolean;  差异内容：isBankNumberDialogShown?: boolean; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：InteractiveLivenessConfig；  API声明：isPrivacyMode?: boolean;  差异内容：isPrivacyMode?: boolean; | api/@hms.ai.interactiveLiveness.d.ts |
