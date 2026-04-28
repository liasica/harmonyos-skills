---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-b065
title: Core Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Core Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:36c5208bd8fc7c58cf9fd47dc75bab6f214d564b6895df68816e10bc49f77237
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：faceComparator；  API声明：function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>;  差异内容：1008400001,1008400002,401 | 类名：faceComparator；  API声明：function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>;  差异内容：1008400001,1008400002,200,401 | api/@hms.ai.face.faceComparator.d.ts |
| 错误码变更 | 类名：faceDetector；  API声明：function detect(visionInfo: VisionInfo): Promise<Array<Face>>;  差异内容：1008800001,1008800002,401 | 类名：faceDetector；  API声明：function detect(visionInfo: VisionInfo): Promise<Array<Face>>;  差异内容：1008800001,1008800002,200,401 | api/@hms.ai.face.faceDetector.d.ts |
| 错误码变更 | 类名：subjectSegmentation；  API声明：function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>;  差异内容：1011000001,1011000002,401 | 类名：subjectSegmentation；  API声明：function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>;  差异内容：1011000001,1011000002,200,401 | api/@hms.ai.vision.subjectSegmentation.d.ts |
