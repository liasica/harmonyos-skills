---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arengine-6101
title: AR Engine
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > AR Engine
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e54caf865b92ba5d351a42359b8023662f11119218b746f4cc7e5e429fd4f5ea
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ARType；  API声明：BODY = 0x02  差异内容：BODY = 0x02 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARType；  API声明：FACE = 0x10  差异内容：FACE = 0x10 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARTrackableType；  API声明：FACE = 0x50000002  差异内容：FACE = 0x50000002 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFrame；  API声明：acquireBodySkeleton(): Array<ARBody>;  差异内容：acquireBodySkeleton(): Array<ARBody>; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：class ARFaceAnchor  差异内容：class ARFaceAnchor | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFaceAnchor；  API声明：getFace(): ARFace;  差异内容：getFace(): ARFace; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARConfig；  API声明：cameraLensFacing?: ARCameraLensFacing;  差异内容：cameraLensFacing?: ARCameraLensFacing; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARConfig；  API声明：multiFaceMode?: ARMultiFaceMode;  差异内容：multiFaceMode?: ARMultiFaceMode; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARConfig；  API声明：maxDetectedBodyNum?: number;  差异内容：maxDetectedBodyNum?: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：enum ARFeatureType  差异内容：enum ARFeatureType | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_SLAM = 0  差异内容：ARENGINE\_FEATURE\_TYPE\_SLAM = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_DEPTH = 1  差异内容：ARENGINE\_FEATURE\_TYPE\_DEPTH = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_MESH = 2  差异内容：ARENGINE\_FEATURE\_TYPE\_MESH = 2 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_IMAGE = 3  差异内容：ARENGINE\_FEATURE\_TYPE\_IMAGE = 3 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE = 4  差异内容：ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE = 4 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_SEMANTIC = 5  差异内容：ARENGINE\_FEATURE\_TYPE\_SEMANTIC = 5 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_FACE = 6  差异内容：ARENGINE\_FEATURE\_TYPE\_FACE = 6 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFeatureType；  API声明：ARENGINE\_FEATURE\_TYPE\_BODY = 7  差异内容：ARENGINE\_FEATURE\_TYPE\_BODY = 7 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：enum ARBlendShapeType  差异内容：enum ARBlendShapeType | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_BLINK\_LEFT = 0  差异内容：EYE\_BLINK\_LEFT = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_DOWN\_LEFT = 1  差异内容：EYE\_LOOK\_DOWN\_LEFT = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_IN\_LEFT = 2  差异内容：EYE\_LOOK\_IN\_LEFT = 2 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_OUT\_LEFT = 3  差异内容：EYE\_LOOK\_OUT\_LEFT = 3 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_UP\_LEFT = 4  差异内容：EYE\_LOOK\_UP\_LEFT = 4 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_SQUINT\_LEFT = 5  差异内容：EYE\_SQUINT\_LEFT = 5 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_WIDE\_LEFT = 6  差异内容：EYE\_WIDE\_LEFT = 6 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_BLINK\_RIGHT = 7  差异内容：EYE\_BLINK\_RIGHT = 7 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_DOWN\_RIGHT = 8  差异内容：EYE\_LOOK\_DOWN\_RIGHT = 8 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_IN\_RIGHT = 9  差异内容：EYE\_LOOK\_IN\_RIGHT = 9 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_OUT\_RIGHT = 10  差异内容：EYE\_LOOK\_OUT\_RIGHT = 10 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_LOOK\_UP\_RIGHT = 11  差异内容：EYE\_LOOK\_UP\_RIGHT = 11 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_SQUINT\_RIGHT = 12  差异内容：EYE\_SQUINT\_RIGHT = 12 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：EYE\_WIDE\_RIGHT = 13  差异内容：EYE\_WIDE\_RIGHT = 13 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：JAW\_FORWARD = 14  差异内容：JAW\_FORWARD = 14 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：JAW\_LEFT = 15  差异内容：JAW\_LEFT = 15 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：JAW\_RIGHT = 16  差异内容：JAW\_RIGHT = 16 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：JAW\_OPEN = 17  差异内容：JAW\_OPEN = 17 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_FUNNEL = 18  差异内容：MOUTH\_FUNNEL = 18 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_PUCKER = 19  差异内容：MOUTH\_PUCKER = 19 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_LEFT = 20  差异内容：MOUTH\_LEFT = 20 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_RIGHT = 21  差异内容：MOUTH\_RIGHT = 21 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_SMILE\_LEFT = 22  差异内容：MOUTH\_SMILE\_LEFT = 22 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_SMILE\_RIGHT = 23  差异内容：MOUTH\_SMILE\_RIGHT = 23 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_FROWN\_LEFT = 24  差异内容：MOUTH\_FROWN\_LEFT = 24 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_FROWN\_RIGHT = 25  差异内容：MOUTH\_FROWN\_RIGHT = 25 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_DIMPLE\_LEFT = 26  差异内容：MOUTH\_DIMPLE\_LEFT = 26 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_DIMPLE\_RIGHT = 27  差异内容：MOUTH\_DIMPLE\_RIGHT = 27 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_STRETCH\_LEFT = 28  差异内容：MOUTH\_STRETCH\_LEFT = 28 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_STRETCH\_RIGHT = 29  差异内容：MOUTH\_STRETCH\_RIGHT = 29 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_ROLL\_LOWER = 30  差异内容：MOUTH\_ROLL\_LOWER = 30 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_ROLL\_UPPER = 31  差异内容：MOUTH\_ROLL\_UPPER = 31 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_SHRUG\_LOWER = 32  差异内容：MOUTH\_SHRUG\_LOWER = 32 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_SHRUG\_UPPER = 33  差异内容：MOUTH\_SHRUG\_UPPER = 33 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_UPPER\_UP = 34  差异内容：MOUTH\_UPPER\_UP = 34 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_LOWER\_DOWN = 35  差异内容：MOUTH\_LOWER\_DOWN = 35 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：MOUTH\_LOWER\_OUT = 36  差异内容：MOUTH\_LOWER\_OUT = 36 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：BROW\_DOWN\_LEFT = 37  差异内容：BROW\_DOWN\_LEFT = 37 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：BROW\_DOWN\_RIGHT = 38  差异内容：BROW\_DOWN\_RIGHT = 38 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：BROW\_INNER\_UP = 39  差异内容：BROW\_INNER\_UP = 39 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：BROW\_OUTER\_UP\_LEFT = 40  差异内容：BROW\_OUTER\_UP\_LEFT = 40 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：BROW\_OUTER\_UP\_RIGHT = 41  差异内容：BROW\_OUTER\_UP\_RIGHT = 41 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：CHEEK\_PUFF = 42  差异内容：CHEEK\_PUFF = 42 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：CHEEK\_SQUINT\_LEFT = 43  差异内容：CHEEK\_SQUINT\_LEFT = 43 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：CHEEK\_SQUINT\_RIGHT = 44  差异内容：CHEEK\_SQUINT\_RIGHT = 44 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：FROWN\_NOSE\_MOUTH\_UP = 45  差异内容：FROWN\_NOSE\_MOUTH\_UP = 45 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_IN = 46  差异内容：TONGUE\_IN = 46 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_OUT\_SLIGHT = 47  差异内容：TONGUE\_OUT\_SLIGHT = 47 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_LEFT = 48  差异内容：TONGUE\_LEFT = 48 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_RIGHT = 49  差异内容：TONGUE\_RIGHT = 49 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_UP = 50  差异内容：TONGUE\_UP = 50 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_DOWN = 51  差异内容：TONGUE\_DOWN = 51 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_LEFT\_UP = 52  差异内容：TONGUE\_LEFT\_UP = 52 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_LEFT\_DOWN = 53  差异内容：TONGUE\_LEFT\_DOWN = 53 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_RIGHT\_UP = 54  差异内容：TONGUE\_RIGHT\_UP = 54 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：TONGUE\_RIGHT\_DOWN = 55  差异内容：TONGUE\_RIGHT\_DOWN = 55 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：LEFT\_EYEBALL\_LEFT = 56  差异内容：LEFT\_EYEBALL\_LEFT = 56 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：LEFT\_EYEBALL\_RIGHT = 57  差异内容：LEFT\_EYEBALL\_RIGHT = 57 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：LEFT\_EYEBALL\_UP = 58  差异内容：LEFT\_EYEBALL\_UP = 58 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：LEFT\_EYEBALL\_DOWN = 59  差异内容：LEFT\_EYEBALL\_DOWN = 59 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：RIGHT\_EYEBALL\_LEFT = 60  差异内容：RIGHT\_EYEBALL\_LEFT = 60 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：RIGHT\_EYEBALL\_RIGHT = 61  差异内容：RIGHT\_EYEBALL\_RIGHT = 61 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：RIGHT\_EYEBALL\_UP = 62  差异内容：RIGHT\_EYEBALL\_UP = 62 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapeType；  API声明：RIGHT\_EYEBALL\_DOWN = 63  差异内容：RIGHT\_EYEBALL\_DOWN = 63 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：enum ARAnimojiTriangleLabel  差异内容：enum ARAnimojiTriangleLabel | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_NON\_FACE = -1  差异内容：LABEL\_NON\_FACE = -1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_FACE\_OTHER = 0  差异内容：LABEL\_FACE\_OTHER = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_LOWER\_LIP = 1  差异内容：LABEL\_LOWER\_LIP = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_UPPER\_LIP = 2  差异内容：LABEL\_UPPER\_LIP = 2 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_LEFT\_EYE = 3  差异内容：LABEL\_LEFT\_EYE = 3 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_RIGHT\_EYE = 4  差异内容：LABEL\_RIGHT\_EYE = 4 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_LEFT\_BROW = 5  差异内容：LABEL\_LEFT\_BROW = 5 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_RIGHT\_BROW = 6  差异内容：LABEL\_RIGHT\_BROW = 6 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_BROW\_CENTER = 7  差异内容：LABEL\_BROW\_CENTER = 7 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARAnimojiTriangleLabel；  API声明：LABEL\_NOSE = 8  差异内容：LABEL\_NOSE = 8 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：enum ARCameraLensFacing  差异内容：enum ARCameraLensFacing | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARCameraLensFacing；  API声明：REAR = 0  差异内容：REAR = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARCameraLensFacing；  API声明：FRONT = 1  差异内容：FRONT = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：enum ARMultiFaceMode  差异内容：enum ARMultiFaceMode | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARMultiFaceMode；  API声明：MULTIFACE\_DISABLE = 0x300  差异内容：MULTIFACE\_DISABLE = 0x300 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARMultiFaceMode；  API声明：MULTIFACE\_ENABLE = 0x800  差异内容：MULTIFACE\_ENABLE = 0x800 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：class ARFace  差异内容：class ARFace | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFace；  API声明：getGeometry(): ARGeometry;  差异内容：getGeometry(): ARGeometry; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFace；  API声明：getBlendShapes(): ARBlendShapes;  差异内容：getBlendShapes(): ARBlendShapes; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFace；  API声明：getLandmark(): ARLandmark;  差异内容：getLandmark(): ARLandmark; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：class ARGeometry  差异内容：class ARGeometry | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：readonly verticesSize: number;  差异内容：readonly verticesSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：readonly triangleIndicesCount: number;  差异内容：readonly triangleIndicesCount: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：readonly texCoordSize: number;  差异内容：readonly texCoordSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：readonly indicesSize: number;  差异内容：readonly indicesSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：readonly triangleLabelsSize: number;  差异内容：readonly triangleLabelsSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：getVertices(): ArrayBuffer;  差异内容：getVertices(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：getTexCoord(): ArrayBuffer;  差异内容：getTexCoord(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：getIndices(): ArrayBuffer;  差异内容：getIndices(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：getTriangleLabels(): ArrayBuffer;  差异内容：getTriangleLabels(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARGeometry；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：class ARBlendShapes  差异内容：class ARBlendShapes | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapes；  API声明：readonly count: number;  差异内容：readonly count: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapes；  API声明：getData(): ArrayBuffer;  差异内容：getData(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapes；  API声明：getTypes(): Array<ARBlendShapeType>;  差异内容：getTypes(): Array<ARBlendShapeType>; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBlendShapes；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：class ARLandmark  差异内容：class ARLandmark | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARLandmark；  API声明：readonly count: number;  差异内容：readonly count: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARLandmark；  API声明：getVertices2D(): ArrayBuffer;  差异内容：getVertices2D(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARLandmark；  API声明：getVertices3D(): ArrayBuffer;  差异内容：getVertices3D(): ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARLandmark；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：enum ARBodyLandmarkType  差异内容：enum ARBodyLandmarkType | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：NECK = 1  差异内容：NECK = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_SHOULDER = 2  差异内容：RIGHT\_SHOULDER = 2 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_ELBOW = 3  差异内容：RIGHT\_ELBOW = 3 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_WRIST = 4  差异内容：RIGHT\_WRIST = 4 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_SHOULDER = 5  差异内容：LEFT\_SHOULDER = 5 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_ELBOW = 6  差异内容：LEFT\_ELBOW = 6 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_WRIST = 7  差异内容：LEFT\_WRIST = 7 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_HIP = 8  差异内容：RIGHT\_HIP = 8 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_KNEE = 9  差异内容：RIGHT\_KNEE = 9 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_ANKLE = 10  差异内容：RIGHT\_ANKLE = 10 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_HIP = 11  差异内容：LEFT\_HIP = 11 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_KNEE = 12  差异内容：LEFT\_KNEE = 12 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_ANKLE = 13  差异内容：LEFT\_ANKLE = 13 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：MID\_HIP = 14  差异内容：MID\_HIP = 14 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_EAR = 15  差异内容：RIGHT\_EAR = 15 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：RIGHT\_EYE = 16  差异内容：RIGHT\_EYE = 16 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：NOSE = 17  差异内容：NOSE = 17 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_EYE = 18  差异内容：LEFT\_EYE = 18 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：LEFT\_EAR = 19  差异内容：LEFT\_EAR = 19 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmarkType；  API声明：SPINE = 20  差异内容：SPINE = 20 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：interface ARBodyLandmark2D  差异内容：interface ARBodyLandmark2D | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmark2D；  API声明：x: number;  差异内容：x: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmark2D；  API声明：y: number;  差异内容：y: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmark2D；  API声明：confidence: number;  差异内容：confidence: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmark2D；  API声明：type: ARBodyLandmarkType;  差异内容：type: ARBodyLandmarkType; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBodyLandmark2D；  API声明：isValid: boolean;  差异内容：isValid: boolean; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine；  API声明：class ARBody  差异内容：class ARBody | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBody；  API声明：readonly trackId: number;  差异内容：readonly trackId: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBody；  API声明：readonly timeStamp: number;  差异内容：readonly timeStamp: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARBody；  API声明：getLandmarks2D(): Array<ARBodyLandmark2D>;  差异内容：getLandmarks2D(): Array<ARBodyLandmark2D>; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arViewController；  API声明：enum LandmarkType  差异内容：enum LandmarkType | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：LandmarkType；  API声明：LEFT\_EYE = 0  差异内容：LEFT\_EYE = 0 | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：LandmarkType；  API声明：LEFT\_SIDE\_OF\_MOUTH = 1  差异内容：LEFT\_SIDE\_OF\_MOUTH = 1 | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：LandmarkType；  API声明：RIGHT\_EYE = 2  差异内容：RIGHT\_EYE = 2 | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：LandmarkType；  API声明：RIGHT\_SIDE\_OF\_MOUTH = 3  差异内容：RIGHT\_SIDE\_OF\_MOUTH = 3 | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：LandmarkType；  API声明：TIP\_OF\_NOSE = 4  差异内容：TIP\_OF\_NOSE = 4 | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：LandmarkType；  API声明：CENTER\_OF\_FACE = 5  差异内容：CENTER\_OF\_FACE = 5 | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：loadAsset(resourcePath: ResourceStr, landmark: LandmarkType): Promise<void>;  差异内容：loadAsset(resourcePath: ResourceStr, landmark: LandmarkType): Promise<void>; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：removeAsset(landmark: LandmarkType): Promise<void>;  差异内容：removeAsset(landmark: LandmarkType): Promise<void>; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：clearResource(): Promise<void>;  差异内容：clearResource(): Promise<void>; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：setBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType, weight: number): boolean;  差异内容：setBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType, weight: number): boolean; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：getBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType): number | null;  差异内容：getBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType): number | null; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：transformPose(position: Vec3, rotation: Quaternion): arEngine.ARPose | null;  差异内容：transformPose(position: Vec3, rotation: Quaternion): arEngine.ARPose | null; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：arViewController；  API声明：function isARTypeSupported(type: arEngine.ARFeatureType): boolean;  差异内容：function isARTypeSupported(type: arEngine.ARFeatureType): boolean; | api/@hms.core.ar.arview.d.ets |
