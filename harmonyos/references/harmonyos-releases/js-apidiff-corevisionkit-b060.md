---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-b060
title: Core Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta5引入的API > Core Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:def80e6855f253c315cba22c3506f5e6bcc66ed892ae07f25c0498fa8d1e9d39
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：SkeletonDetector；  API声明：static create(): Promise<SkeletonDetector>;  差异内容：SystemCapability.AI.Vision.ObjectDetection | 类名：SkeletonDetector；  API声明：static create(): Promise<SkeletonDetector>;  差异内容：SystemCapability.AI.Vision.SkeletonDetection | api/@hms.ai.vision.skeletonDetection.d.ts |
| 错误码变更 | 类名：faceComparator；  API声明：function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>;  差异内容：1008400001,1008400002,200,401 | 类名：faceComparator；  API声明：function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>;  差异内容：1008400001,1008400002,401 | api/@hms.ai.face.faceComparator.d.ts |
| 错误码变更 | 类名：faceDetector；  API声明：function detect(visionInfo: VisionInfo): Promise<Array<Face>>;  差异内容：1008800001,1008800002,200,401 | 类名：faceDetector；  API声明：function detect(visionInfo: VisionInfo): Promise<Array<Face>>;  差异内容：1008800001,1008800002,401 | api/@hms.ai.face.faceDetector.d.ts |
| 错误码变更 | 类名：subjectSegmentation；  API声明：function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>;  差异内容：1011000001,1011000002,200,401 | 类名：subjectSegmentation；  API声明：function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>;  差异内容：1011000001,1011000002,401 | api/@hms.ai.vision.subjectSegmentation.d.ts |
