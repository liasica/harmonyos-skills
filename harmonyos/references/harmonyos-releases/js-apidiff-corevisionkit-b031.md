---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-b031
title: Core Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Core Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9bf0ee60d17d491ae7bf1f91556adeb0183ab1833d0e689040c592d4face039c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace objectDetection  差异内容： declare namespace objectDetection | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：objectDetection；  API声明： interface VisionObject  差异内容： interface VisionObject | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：VisionObject；  API声明：boundingBox: visionBase.BoundingBox;  差异内容：boundingBox: visionBase.BoundingBox; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：VisionObject；  API声明：score: number;  差异内容：score: number; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：VisionObject；  API声明：labels: Array<number>;  差异内容：labels: Array<number>; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：VisionObject；  API声明：id: number;  差异内容：id: number; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：objectDetection；  API声明： class ObjectDetectionResponse  差异内容： class ObjectDetectionResponse | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：ObjectDetectionResponse；  API声明：objects: Array<VisionObject>;  差异内容：objects: Array<VisionObject>; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：objectDetection；  API声明： class ObjectDetector  差异内容： class ObjectDetector | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：ObjectDetector；  API声明：static create(): Promise<ObjectDetector>;  差异内容：static create(): Promise<ObjectDetector>; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：ObjectDetector；  API声明：process(request: visionBase.Request): Promise<ObjectDetectionResponse>;  差异内容：process(request: visionBase.Request): Promise<ObjectDetectionResponse>; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：ObjectDetector；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | api/@hms.ai.vision.objectDetection.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace skeletonDetection  差异内容： declare namespace skeletonDetection | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：skeletonDetection；  API声明： enum SkeletonPointType  差异内容： enum SkeletonPointType | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：NOSE = 0  差异内容：NOSE = 0 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_EYE = 1  差异内容：LEFT\_EYE = 1 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_EYE = 2  差异内容：RIGHT\_EYE = 2 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_EAR = 3  差异内容：LEFT\_EAR = 3 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_EAR = 4  差异内容：RIGHT\_EAR = 4 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_SHOULDER = 5  差异内容：LEFT\_SHOULDER = 5 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_SHOULDER = 6  差异内容：RIGHT\_SHOULDER = 6 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_ELBOW = 7  差异内容：LEFT\_ELBOW = 7 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_ELBOW = 8  差异内容：RIGHT\_ELBOW = 8 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_WRIST = 9  差异内容：LEFT\_WRIST = 9 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_WRIST = 10  差异内容：RIGHT\_WRIST = 10 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_HIP = 11  差异内容：LEFT\_HIP = 11 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_HIP = 12  差异内容：RIGHT\_HIP = 12 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_KNEE = 13  差异内容：LEFT\_KNEE = 13 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_KNEE = 14  差异内容：RIGHT\_KNEE = 14 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：LEFT\_ANKLE = 15  差异内容：LEFT\_ANKLE = 15 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPointType；  API声明：RIGHT\_ANKLE = 16  差异内容：RIGHT\_ANKLE = 16 | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：skeletonDetection；  API声明： interface SkeletonPoint  差异内容： interface SkeletonPoint | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPoint；  API声明：score: number;  差异内容：score: number; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPoint；  API声明：point: visionBase.Point;  差异内容：point: visionBase.Point; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonPoint；  API声明：type: SkeletonPointType;  差异内容：type: SkeletonPointType; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：skeletonDetection；  API声明： interface Skeleton  差异内容： interface Skeleton | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：Skeleton；  API声明：boundingBox: visionBase.BoundingBox;  差异内容：boundingBox: visionBase.BoundingBox; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：Skeleton；  API声明：score: number;  差异内容：score: number; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：Skeleton；  API声明：points: Array<SkeletonPoint>;  差异内容：points: Array<SkeletonPoint>; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：skeletonDetection；  API声明： class SkeletonDetectionResponse  差异内容： class SkeletonDetectionResponse | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonDetectionResponse；  API声明：skeletons: Array<Skeleton>;  差异内容：skeletons: Array<Skeleton>; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：skeletonDetection；  API声明： class SkeletonDetector  差异内容： class SkeletonDetector | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonDetector；  API声明：static create(): Promise<SkeletonDetector>;  差异内容：static create(): Promise<SkeletonDetector>; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonDetector；  API声明：process(request: visionBase.Request): Promise<SkeletonDetectionResponse>;  差异内容：process(request: visionBase.Request): Promise<SkeletonDetectionResponse>; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：SkeletonDetector；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | api/@hms.ai.vision.skeletonDetection.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace visionBase  差异内容： declare namespace visionBase | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： enum SceneMode  差异内容： enum SceneMode | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：SceneMode；  API声明：FOREGROUND = 1  差异内容：FOREGROUND = 1 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：SceneMode；  API声明：BACKGROUND = 2  差异内容：BACKGROUND = 2 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface ImageData  差异内容： interface ImageData | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：ImageData；  API声明：pixelMap: image.PixelMap;  差异内容：pixelMap: image.PixelMap; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：type InputData = ImageData | ImageData[];  差异内容：type InputData = ImageData | ImageData[]; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface BoundingBox  差异内容： interface BoundingBox | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：BoundingBox；  API声明：left: number;  差异内容：left: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：BoundingBox；  API声明：top: number;  差异内容：top: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：BoundingBox；  API声明：width: number;  差异内容：width: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：BoundingBox；  API声明：height: number;  差异内容：height: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface Point  差异内容： interface Point | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Point；  API声明：x: number;  差异内容：x: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Point；  API声明：y: number;  差异内容：y: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface Orientation  差异内容： interface Orientation | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：yaw: number;  差异内容：yaw: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：pitch: number;  差异内容：pitch: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：roll: number;  差异内容：roll: number; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： class Request  差异内容： class Request | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Request；  API声明：inputData: InputData;  差异内容：inputData: InputData; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Request；  API声明：scene?: SceneMode;  差异内容：scene?: SceneMode; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Request；  API声明：requestId?: string;  差异内容：requestId?: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： class Response  差异内容： class Response | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Response；  API声明：requestId?: string;  差异内容：requestId?: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： class Analyzer  差异内容： class Analyzer | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：Analyzer；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | api/@hms.ai.vision.visionBase.d.ts |
