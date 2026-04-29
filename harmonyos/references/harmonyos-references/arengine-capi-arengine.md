---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine
title: AR Engine
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 模块 > AR Engine
category: harmonyos-references
scraped_at: 2026-04-29T14:05:09+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:7b7dc3fc3a651926746053bab69eb75273b14f2ac13ded8e8d9d2e2f8e34e07a
---

## 概述

PhoneTabletTV

本模块提供AR Engine（AR引擎服务）的AR增强现实能力相关接口。AR Engine的基础核心能力包含：环境识别与运动跟踪能力、图像识别与跟踪能力、人脸识别与跟踪能力和人体骨骼识别与跟踪能力。

**起始版本：** 5.0.0(12)

## 汇总

PhoneTabletTV

### 文件

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [ar\_engine\_core.h](arengine-header-file.md) | 本声明用于访问AR Engine（AR引擎服务）的API。提供AR（增强现实）能力的相关接口。AR的基础核心能力包含：环境识别与运动跟踪能力、图像识别与跟踪能力、人脸识别与跟踪能力和人体骨骼识别与跟踪能力。 |

### 结构体

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| struct [AREngine\_ARAugmentedImageSource](arengine-struct-araugmentedimagesource.md) | 图像数据。 |
| struct [AREngine\_ClipPlaneDistance](arengine-struct-clipplanedistance.md) | 裁剪平面距离数据。 |
| struct [AREngine\_ARSemanticDensePointData](arengine-struct-arsemanticdensepointdata.md) | 高精几何重建对象的稠密点云数据。 |
| struct [AREngine\_ARSemanticDenseCubeData](arengine-struct-arsemanticdensecubedata.md) | 高精几何重建对象的立方体数据。 |

### 宏定义

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [ARENGINE\_AABB\_POINT\_SIZE](arengine-capi-arengine.md#arengine_aabb_point_size) = 6 | 包围盒坐标集数组大小。 |
| [ARENGINE\_DISTORTION\_COUNT](arengine-capi-arengine.md#arengine_distortion_count) = 5 | 相机畸变参数的个数。 |
| [ARENGINE\_POSE\_RAW\_SIZE](arengine-capi-arengine.md#arengine_pose_raw_size) = 7 | 位姿数据数组大小。 |
| [ARENGINE\_VIEW\_MATRIX\_SIZE](arengine-capi-arengine.md#arengine_view_matrix_size) = 16 | 变换矩阵数组大小。 |

### 类型定义

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) | 锚点对象。 |
| typedef struct [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) | 锚点对象列表。 |
| typedef struct [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) | 跟踪图像对象。 |
| typedef struct [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) | 跟踪图像数据库对象。 |
| typedef struct [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) | 当前帧对应的相机信息。 |
| typedef struct [AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) [AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) | 相机的配置信息。 |
| typedef struct [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) | 相机内参。 |
| typedef struct [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) | 用于配置[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)的能力项（使用哪些能力、模式等）。 |
| typedef struct [AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface) [AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface) | 跟踪的人脸对象。 |
| typedef struct [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) | 人脸拓扑结构对象。 |
| typedef struct [AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) [AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) | 人脸微表情对象。 |
| typedef struct [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) | AR Engine处理的一帧数据。 |
| typedef struct [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) | 命中检测结果对象。 |
| typedef struct [AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) [AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) | 命中检测结果列表。 |
| typedef struct [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) | 相机视频流帧对象。 |
| typedef struct [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) | 平面对象。 |
| typedef struct [AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint) [AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint) | 点对象。 |
| typedef struct [AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) [AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) | 可跟踪的3D点云的集合。 |
| typedef struct [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) | 位姿对象。 |
| typedef struct [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) | 环境mesh数据的集合。 |
| typedef struct [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) | 表示高精几何重建对象数据的集合。 |
| typedef struct [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) | 管理AR Engine的系统状态。 |
| typedef struct [AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget) [AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget) | 物体对象。 |
| typedef struct [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) | 可跟踪对象，如点、平面等。 |
| typedef struct [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) | 可跟踪对象列表。 |
| typedef void (\*[HMS\_AREngine\_PhotoAvailableCallback](arengine-capi-arengine.md#hms_arengine_photoavailablecallback))([OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md) \*photoBuffer) | 输出拍照流图像回调。 |
| typedef struct [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) | 人体对象。 |

### 枚举

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [AREngine\_FeatureType](arengine-capi-arengine.md#arengine_featuretype) {  ARENGINE\_FEATURE\_TYPE\_SLAM = 0,  ARENGINE\_FEATURE\_TYPE\_DEPTH = 1,  ARENGINE\_FEATURE\_TYPE\_MESH = 2,  ARENGINE\_FEATURE\_TYPE\_IMAGE = 3,  ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE = 4,  ARENGINE\_FEATURE\_TYPE\_SEMANTIC = 5,  ARENGINE\_FEATURE\_TYPE\_FACE = 6,  ARENGINE\_FEATURE\_TYPE\_BODY = 7  } | AR特性类别。 |
| [AREngine\_ARAddAugmentedImageReason](arengine-capi-arengine.md#arengine_araddaugmentedimagereason) {  ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_NONE = 0,  ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_SIZE\_NOT\_MATCH = 1,  ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_LIGHT\_ANOMALY = 2,  ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_FEATURE\_LIMIT = 3,  ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_OTHER = 4  } | 跟踪失败的可能原因。 |
| [AREngine\_ARAnimojiBlendShape](arengine-capi-arengine.md#arengine_aranimojiblendshape) {  ARENGINE\_ARANIMOJI\_EYE\_BLINK\_LEFT = 0,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_DOWN\_LEFT = 1,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_IN\_LEFT = 2,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_OUT\_LEFT = 3,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_UP\_LEFT = 4,  ARENGINE\_ARANIMOJI\_EYE\_SQUINT\_LEFT = 5,  ARENGINE\_ARANIMOJI\_EYE\_WIDE\_LEFT = 6,  ARENGINE\_ARANIMOJI\_EYE\_BLINK\_RIGHT = 7,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_DOWN\_RIGHT = 8,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_IN\_RIGHT = 9,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_OUT\_RIGHT = 10,  ARENGINE\_ARANIMOJI\_EYE\_LOOK\_UP\_RIGHT = 11,  ARENGINE\_ARANIMOJI\_EYE\_SQUINT\_RIGHT = 12,  ARENGINE\_ARANIMOJI\_EYE\_WIDE\_RIGHT = 13,  ARENGINE\_ARANIMOJI\_JAW\_FORWARD = 14,  ARENGINE\_ARANIMOJI\_JAW\_LEFT = 15,  ARENGINE\_ARANIMOJI\_JAW\_RIGHT = 16,  ARENGINE\_ARANIMOJI\_JAW\_OPEN = 17,  ARENGINE\_ARANIMOJI\_MOUTH\_FUNNEL = 18,  ARENGINE\_ARANIMOJI\_MOUTH\_PUCKER = 19,  ARENGINE\_ARANIMOJI\_MOUTH\_LEFT = 20,  ARENGINE\_ARANIMOJI\_MOUTH\_RIGHT = 21,  ARENGINE\_ARANIMOJI\_MOUTH\_SMILE\_LEFT = 22,  ARENGINE\_ARANIMOJI\_MOUTH\_SMILE\_RIGHT = 23,  ARENGINE\_ARANIMOJI\_MOUTH\_FROWN\_LEFT = 24,  ARENGINE\_ARANIMOJI\_MOUTH\_FROWN\_RIGHT = 25,  ARENGINE\_ARANIMOJI\_MOUTH\_DIMPLE\_LEFT = 26,  ARENGINE\_ARANIMOJI\_MOUTH\_DIMPLE\_RIGHT = 27,  ARENGINE\_ARANIMOJI\_MOUTH\_STRETCH\_LEFT = 28,  ARENGINE\_ARANIMOJI\_MOUTH\_STRETCH\_RIGHT = 29,  ARENGINE\_ARANIMOJI\_MOUTH\_ROLL\_LOWER = 30,  ARENGINE\_ARANIMOJI\_MOUTH\_ROLL\_UPPER = 31,  ARENGINE\_ARANIMOJI\_MOUTH\_SHRUG\_LOWER = 32,  ARENGINE\_ARANIMOJI\_MOUTH\_SHRUG\_UPPER = 33,  ARENGINE\_ARANIMOJI\_MOUTH\_UPPER\_UP = 34,  ARENGINE\_ARANIMOJI\_MOUTH\_LOWER\_DOWN = 35,  ARENGINE\_ARANIMOJI\_MOUTH\_LOWER\_OUT = 36,  ARENGINE\_ARANIMOJI\_BROW\_DOWN\_LEFT = 37,  ARENGINE\_ARANIMOJI\_BROW\_DOWN\_RIGHT = 38,  ARENGINE\_ARANIMOJI\_BROW\_INNER\_UP = 39,  ARENGINE\_ARANIMOJI\_BROW\_OUTER\_UP\_LEFT = 40,  ARENGINE\_ARANIMOJI\_BROW\_OUTER\_UP\_RIGHT = 41,  ARENGINE\_ARANIMOJI\_CHEEK\_PUFF = 42,  ARENGINE\_ARANIMOJI\_CHEEK\_SQUINT\_LEFT = 43,  ARENGINE\_ARANIMOJI\_CHEEK\_SQUINT\_RIGHT = 44,  ARENGINE\_ARANIMOJI\_FROWN\_NOSE\_MOUTH\_UP = 45,  ARENGINE\_ARANIMOJI\_TONGUE\_IN = 46,  ARENGINE\_ARANIMOJI\_TONGUE\_OUT\_SLIGHT = 47,  ARENGINE\_ARANIMOJI\_TONGUE\_LEFT = 48,  ARENGINE\_ARANIMOJI\_TONGUE\_RIGHT = 49,  ARENGINE\_ARANIMOJI\_TONGUE\_UP = 50,  ARENGINE\_ARANIMOJI\_TONGUE\_DOWN = 51,  ARENGINE\_ARANIMOJI\_TONGUE\_LEFT\_UP = 52,  ARENGINE\_ARANIMOJI\_TONGUE\_LEFT\_DOWN = 53,  ARENGINE\_ARANIMOJI\_TONGUE\_RIGHT\_UP = 54,  ARENGINE\_ARANIMOJI\_TONGUE\_RIGHT\_DOWN = 55,  ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_LEFT = 56,  ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_RIGHT = 57,  ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_UP = 58,  ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_DOWN = 59,  ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_LEFT = 60,  ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_RIGHT = 61,  ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_UP = 62,  ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_DOWN = 63  } | 微表情类型。 |
| [AREngine\_ARAnimojiTriangleLabel](arengine-capi-arengine.md#arengine_aranimojitrianglelabel) {  ARENGINE\_TRIANGLE\_LABEL\_NON\_FACE = -1,  ARENGINE\_TRIANGLE\_LABEL\_FACE\_OTHER = 0,  ARENGINE\_TRIANGLE\_LABEL\_LOWER\_LIP = 1,  ARENGINE\_TRIANGLE\_LABEL\_UPPER\_LIP = 2,  ARENGINE\_TRIANGLE\_LABEL\_LEFT\_EYE = 3,  ARENGINE\_TRIANGLE\_LABEL\_RIGHT\_EYE = 4,  ARENGINE\_TRIANGLE\_LABEL\_LEFT\_BROW = 5,  ARENGINE\_TRIANGLE\_LABEL\_RIGHT\_BROW = 6,  ARENGINE\_TRIANGLE\_LABEL\_BROW\_CENTER = 7,  ARENGINE\_TRIANGLE\_LABEL\_NOSE = 8  } | 人脸三角形面片标签。 |
| [AREngine\_ARCameraLensFacing](arengine-capi-arengine.md#arengine_arcameralensfacing) {  ARENGINE\_CAMERA\_FACING\_REAR = 0,  ARENGINE\_CAMERA\_FACING\_FRONT = 1  } | 配置摄像机镜头的朝向。 |
| [AREngine\_ARConfidenceLevel](arengine-capi-arengine.md#arengine_arconfidencelevel) {  ARENGINE\_DEPTH\_CONFIDENCE\_LOW = 0,  ARENGINE\_DEPTH\_CONFIDENCE\_MEDIUM = 1,  ARENGINE\_DEPTH\_CONFIDENCE\_HIGH = 2  } | 深度置信度。 |
| [AREngine\_ARDepthMode](arengine-capi-arengine.md#arengine_ardepthmode) {  ARENGINE\_DEPTH\_MODE\_DISABLED = 0,  ARENGINE\_DEPTH\_MODE\_AUTOMATIC = 1  } | 深度模式。 |
| [AREngine\_ARFocusMode](arengine-capi-arengine.md#arengine_arfocusmode) {  ARENGINE\_FOCUS\_MODE\_FIXED = 0,  ARENGINE\_FOCUS\_MODE\_AUTO = 1  } | 对焦模式。 |
| [AREngine\_ARImageDatabaseMode](arengine-capi-arengine.md#arengine_arimagedatabasemode) {  ARENGINE\_ADD\_NORMAL = 0,  ARENGINE\_ADD\_AUTO = 1  } | 用于跟踪的特征库图像添加方式。 |
| [AREngine\_ARImageFormat](arengine-capi-arengine.md#arengine_arimageformat) {  ARENGINE\_IMAGE\_UNKNOWN = 0,  ARENGINE\_IMAGE\_YUV\_420\_888 = 2,  ARENGINE\_IMAGE\_Y\_8 = 3,  ARENGINE\_IMAGE\_Y\_16 = 4  } | 图像数据格式。 |
| [AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode) {  ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW = 0,  ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO = 1  } | 设置图片数据流模式，默认情况下系统设置为ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW。 |
| [AREngine\_ARMeshMode](arengine-capi-arengine.md#arengine_armeshmode) {  ARENGINE\_MESH\_MODE\_DISABLED = 0,  ARENGINE\_MESH\_MODE\_ENABLE=1  } | Mesh启用模式。 |
| [AREngine\_ARMultiFaceMode](arengine-capi-arengine.md#arengine_armultifacemode) {  ARENGINE\_MULTIFACE\_DISABLE = 0x300,  ARENGINE\_MULTIFACE\_ENABLE = 0x800  } | 多人脸检测模式。当多人脸检测模式开启时[HMS\_AREngine\_ARSession\_GetAllTrackables](arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)返回的可跟踪对象数量最大为3，当多人脸检测模式关闭时HMS\_AREngine\_ARSession\_GetAllTrackables返回的可跟踪对象数量最大为1。 |
| [AREngine\_ARPlaneFindingMode](arengine-capi-arengine.md#arengine_arplanefindingmode) {  ARENGINE\_PLANE\_FINDING\_MODE\_DISABLED = 0,  ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL = 1,  ARENGINE\_PLANE\_FINDING\_MODE\_VERTICAL = 2,  ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL\_AND\_VERTICAL = 3  } | 平面搜索模式。 |
| [AREngine\_ARPlaneType](arengine-capi-arengine.md#arengine_arplanetype) {  ARENGINE\_PLANE\_FACING\_HORIZONTAL\_UPWARD = 0,  ARENGINE\_PLANE\_FACING\_HORIZONTAL\_DOWNWARD = 1,  ARENGINE\_PLANE\_FACING\_VERTICAL = 2,  ARENGINE\_PLANE\_FACING\_INVALID = 3  } | 平面类型。 |
| [AREngine\_ARPointOrientationMode](arengine-capi-arengine.md#arengine_arpointorientationmode) {  ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY = 0,  ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL = 1  } | 朝向模式。 |
| [AREngine\_ARPoseMode](arengine-capi-arengine.md#arengine_arposemode) {  ARENGINE\_POSE\_MODE\_GRAVITY = 0,  ARENGINE\_POSE\_MODE\_GRAVITY\_HEADING = 1  } | AR Engine输出的相机位姿对齐格式。 |
| [AREngine\_ARPoseType](arengine-capi-arengine.md#arengine_arposetype) {  ARENGINE\_POSE\_TYPE\_IDENTITY = 0,  ARENGINE\_POSE\_TYPE\_ROTATE\_90 = 1,  ARENGINE\_POSE\_TYPE\_ROTATE\_180 = 2,  ARENGINE\_POSE\_TYPE\_ROTATE\_270 = 3  } | 位姿类型。 |
| [AREngine\_ARPowerMode](arengine-capi-arengine.md#arengine_arpowermode) {  ARENGINE\_POWER\_MODE\_NORMAL = 0,  ARENGINE\_POWER\_MODE\_POWER\_SAVING = 1,  ARENGINE\_POWER\_MODE\_PERFORMANCE\_FIRST = 2,  ARENGINE\_POWER\_MODE\_BOOST = 3 ,  ARENGINE\_POWER\_MODE\_ULTRA\_POWER\_SAVING = 11  } | 电源功耗模式。 |
| [AREngine\_ARPreviewMode](arengine-capi-arengine.md#arengine_arpreviewmode) {  ARENGINE\_PREVIEW\_MODE\_ENABLED = 0,  ARENGINE\_PREVIEW\_MODE\_DISABLED = 1  } | 预览模式。 |
| [AREngine\_ARSemanticDenseMode](arengine-capi-arengine.md#arengine_arsemanticdensemode) {  ARENGINE\_SEMANTIC\_DENSE\_MODE\_DISABLED = 0,  ARENGINE\_SEMANTIC\_DENSE\_MODE\_NORMAL = 1,  ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_VOLUME = 2,  ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_SPACE = 3  } | 高精几何重建识别模式。 |
| [AREngine\_ARSemanticMode](arengine-capi-arengine.md#arengine_arsemanticmode) {  ARENGINE\_SEMANTIC\_MODE\_NONE = 0,  ARENGINE\_SEMANTIC\_MODE\_PLANE = 1,  ARENGINE\_SEMANTIC\_MODE\_TARGET = 2  } | 语义模式。 |
| [AREngine\_ARSemanticPlaneLabel](arengine-capi-arengine.md#arengine_arsemanticplanelabel) {  ARENGINE\_PLANE\_UNKNOWN = 0,  ARENGINE\_PLANE\_WALL = 1,  ARENGINE\_PLANE\_FLOOR = 2,  ARENGINE\_PLANE\_SEAT = 3,  ARENGINE\_PLANE\_TABLE = 4,  ARENGINE\_PLANE\_CEILING = 5,  ARENGINE\_PLANE\_DOOR = 6,  ARENGINE\_PLANE\_WINDOW = 7,  ARENGINE\_PLANE\_BED = 8,  ARENGINE\_PLANE\_SPACE = 9,  ARENGINE\_CUBE\_VOLUME = 10,  ARENGINE\_CUBE\_SPACE = 11  } | 当前平面识别到的语义类型。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) {  ARENGINE\_SUCCESS = 0,  ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED = 201,  ARENGINE\_ERROR\_INVALID\_ARGUMENT = 401,  ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED = 801,  ARENGINE\_ERROR\_FATAL = 1009200001,  ARENGINE\_ERROR\_SESSION\_PAUSED = 1009200002,  ARENGINE\_ERROR\_SESSION\_NOT\_PAUSED = 1009200003,  ARENGINE\_ERROR\_NOT\_TRACKING = 1009200004,  ARENGINE\_ERROR\_TEXTURE\_NOT\_SET = 1009200005,  ARENGINE\_ERROR\_MISSING\_GL\_CONTEXT = 1009200006,  ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION = 1009200007,  ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED = 1009200008,  ARENGINE\_ERROR\_NOT\_AVAILABLE = 1009200009,  ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE = 1009200010,  ARENGINE\_ERROR\_IMAGE\_EXCEED\_NUM\_LIMIT = 1009200011,  ARENGINE\_ERROR\_IMAGE\_INSUFFICIENT\_QUALITY = 1009200012,  ARENGINE\_ERROR\_IMAGE\_INVALID\_DATABASE = 1009200013,  ARENGINE\_ERROR\_IMAGE\_ADD\_IMAGE\_TRACKING\_STATE = 1009200014,  ARENGINE\_ERROR\_NATIVEBUFFER\_CREATE\_FAILED = 1009200015,  ARENGINE\_ERROR\_NATIVEBUFFER\_WRITE\_FAILED = 1009200016,  ARENGINE\_CAMERA\_SERVICE\_FATAL\_ERROR = 1009200017  } | 接口返回错误码。 |
| [AREngine\_ARTargetShapeLabel](arengine-capi-arengine.md#arengine_artargetshapelabel) {  ARENGINE\_TARGET\_SHAPE\_UNKNOWN = 0,  ARENGINE\_TARGET\_SHAPE\_CUBE = 1,  ARENGINE\_TARGET\_SHAPE\_CIRCLE = 2,  ARENGINE\_TARGET\_SHAPE\_RECTANGLE = 3  } | 识别到的物体形状。 |
| [AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype) {  ARENGINE\_TRACKABLE\_BASE = 0x41520100,  ARENGINE\_TRACKABLE\_PLANE = 0x41520101,  ARENGINE\_TRACKABLE\_POINT = 0x41520102,  ARENGINE\_TRACKABLE\_AUGMENTED\_IMAGE = 0x41520104,  ARENGINE\_TRACKABLE\_BODY = 0x50000001,  ARENGINE\_TRACKABLE\_FACE = 0x50000002,  ARENGINE\_TRACKABLE\_TARGET = 0x50000008,  ARENGINE\_TRACKABLE\_INVALID = 0  } | 可跟踪对象类型，如平面、点等。 |
| [AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate) {  ARENGINE\_TRACKING\_STATE\_TRACKING = 0,  ARENGINE\_TRACKING\_STATE\_PAUSED = 1,  ARENGINE\_TRACKING\_STATE\_STOPPED = 2  } | 可跟踪对象的跟踪状态。 |
| [AREngine\_ARTrackingStateReason](arengine-capi-arengine.md#arengine_artrackingstatereason) {  ARENGINE\_TRACKING\_STATE\_REASON\_NONE = 0,  ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION = 1,  ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES = 2  } | 可能的跟踪失败原因。 |
| [AREngine\_ARType](arengine-capi-arengine.md#arengine_artype) {  ARENGINE\_TYPE\_WORLD = 0x01,  ARENGINE\_TYPE\_BODY = 0x02,  ARENGINE\_TYPE\_FACE = 0x10,  ARENGINE\_TYPE\_IMAGE = 0x80  } | AR能力类型。 |
| [AREngine\_ARUpdateMode](arengine-capi-arengine.md#arengine_arupdatemode) {  ARENGINE\_UPDATE\_MODE\_BLOCKING = 0,  ARENGINE\_UPDATE\_MODE\_LATEST = 1  } | 调用[HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)方法后数据更新模式。 |
| [AREngine\_ARBodySkeletonType](arengine-capi-arengine.md#arengine_arbodyskeletontype) {  ARENGINE\_ARBODY\_SKELETON\_NECK = 1,  ARENGINE\_ARBODY\_SKELETON\_R\_SHO = 2,  ARENGINE\_ARBODY\_SKELETON\_R\_ELBOW = 3,  ARENGINE\_ARBODY\_SKELETON\_R\_WRIST = 4,  ARENGINE\_ARBODY\_SKELETON\_L\_SHO = 5,  ARENGINE\_ARBODY\_SKELETON\_L\_ELBOW = 6,  ARENGINE\_ARBODY\_SKELETON\_L\_WRIST = 7,  ARENGINE\_ARBODY\_SKELETON\_R\_HIP = 8,  ARENGINE\_ARBODY\_SKELETON\_R\_KNEE = 9,  ARENGINE\_ARBODY\_SKELETON\_R\_ANKLE = 10,  ARENGINE\_ARBODY\_SKELETON\_L\_HIP = 11,  ARENGINE\_ARBODY\_SKELETON\_L\_KNEE = 12,  ARENGINE\_ARBODY\_SKELETON\_L\_ANKLE = 13,  ARENGINE\_ARBODY\_SKELETON\_HIP\_MID = 14,  ARENGINE\_ARBODY\_SKELETON\_R\_EAR = 15,  ARENGINE\_ARBODY\_SKELETON\_R\_EYE = 16,  ARENGINE\_ARBODY\_SKELETON\_NOSE = 17,  ARENGINE\_ARBODY\_SKELETON\_L\_EYE = 18,  ARENGINE\_ARBODY\_SKELETON\_L\_EAR = 19,  ARENGINE\_ARBODY\_SKELETON\_SPINE = 20  } | 骨骼点类型。 |

### 函数

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)([AREngine\_FeatureType](arengine-capi-arengine.md#arengine_featuretype) type) | 判断当前设备支不支持AR特性的使用。  **说明：** 在进行正式开发前，可通过此接口来判断AR特性是否能够正常运行在当前设备。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAnchor\_Detach](arengine-capi-arengine.md#hms_arengine_aranchor_detach)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*anchor) | 通知AR Engine停止跟踪并解绑一个锚点。  **说明：** 由于此函数并没有释放锚点[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)，开发者需要通过调用 [HMS\_AREngine\_ARAnchor\_Release](arengine-capi-arengine.md#hms_arengine_aranchor_release)来释放锚点。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAnchor\_GetPose](arengine-capi-arengine.md#hms_arengine_aranchor_getpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*anchor, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 获取指定锚点在世界坐标系中的位姿信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAnchor\_GetTrackingState](arengine-capi-arengine.md#hms_arengine_aranchor_gettrackingstate)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*anchor, [AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate) \*outTrackingState) | 获取指定锚点位姿的追踪状态。 |
| void [HMS\_AREngine\_ARAnchor\_Release](arengine-capi-arengine.md#hms_arengine_aranchor_release)([AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*anchor) | 释放指定锚点对象的内存。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAnchorList\_AcquireItem](arengine-capi-arengine.md#hms_arengine_aranchorlist_acquireitem)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) \*anchorList, int32\_t index, [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*\*outAnchor) | 从锚点对象列表中获取指定位置的锚点信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAnchorList\_Create](arengine-capi-arengine.md#hms_arengine_aranchorlist_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) \*\*outAnchorList) | 创建一个锚点对象列表。 |
| void [HMS\_AREngine\_ARAnchorList\_Destroy](arengine-capi-arengine.md#hms_arengine_aranchorlist_destroy)([AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) \*anchorList) | 释放一个锚点对象列表。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAnchorList\_GetSize](arengine-capi-arengine.md#hms_arengine_aranchorlist_getsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) \*anchorList, int32\_t \*outSize) | 获取锚点对象列表中包含锚点的数量。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImage\_AcquireName](arengine-capi-arengine.md#hms_arengine_araugmentedimage_acquirename)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) \*augmentedImage, char \*augmentedImageName, uint32\_t \*outNameLength) | 返回跟踪图像的名称。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_araugmentedimage_getcenterpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) \*augmentedImage, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 获取跟踪图像中心点在世界坐标系中的位姿信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImage\_GetExtendX](arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendx)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) \*augmentedImage, float \*outExtendX) | 以图像的中心点为坐标原点，获取X轴上的估计值。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendz)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) \*augmentedImage, float \*outExtendZ) | 以图像的中心点为坐标原点，获取Z轴上的估计值。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImage\_GetIndex](arengine-capi-arengine.md#hms_arengine_araugmentedimage_getindex)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage) \*augmentedImage, uint32\_t \*outIndex) | 获取跟踪图像数据库中跟踪图像的索引。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_addimage)([AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database, const [AREngine\_ARAugmentedImageSource](arengine-struct-araugmentedimagesource.md) \*image, uint32\_t \*outIndex, [AREngine\_ARAddAugmentedImageReason](arengine-capi-arengine.md#arengine_araddaugmentedimagereason) \*outReason) | 将图像添加到图像数据库并输出对应图像的索引。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_create)([AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*\*outDatabase) | 创建一个空的跟踪图像数据库。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_deserialize)(const uint8\_t \*buffer, const uint64\_t bufSize, [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*\*outDatabase) | 反序列化特征数据库。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_Destroy](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_destroy)([AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database) | 释放图像数据库对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetAddMode](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_getaddmode)(const [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database, [AREngine\_ARImageDatabaseMode](arengine-capi-arengine.md#arengine_arimagedatabasemode) \*outAddMode) | 获取添加跟踪图像模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_setaddmode)(const [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database, [AREngine\_ARImageDatabaseMode](arengine-capi-arengine.md#arengine_arimagedatabasemode) addMode) | 设置添加跟踪图像模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_getcapacity)(const [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database, uint32\_t \*outCapacity) | 获取可以添加的最大图像数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_getimagecount)(const [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database, uint32\_t \*outImageCount) | 获取数据库中存储的图像数量。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_serialize)(const [AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase) \*database, uint8\_t \*\*outBuffer, uint64\_t \*outBufSize) | 序列化特征数据库。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](arengine-capi-arengine.md#hms_arengine_arcamera_getdisplayorientedpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetImageIntrinsics](arengine-capi-arengine.md#hms_arengine_arcamera_getimageintrinsics)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*outIntrinsics) | 获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetPose](arengine-capi-arengine.md#hms_arengine_arcamera_getpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetProjectionMatrix](arengine-capi-arengine.md#hms_arengine_arcamera_getprojectionmatrix)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, [AREngine\_ClipPlaneDistance](arengine-struct-clipplanedistance.md) clipPlaneDistance, float \*outDestColMajor4x4, int32\_t destColMajor4x4Num) | 获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetTrackingState](arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstate)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, [AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate) \*outTrackingState) | 获取相机的当前追踪状态。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetTrackingStateReason](arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstatereason)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, [AREngine\_ARTrackingStateReason](arengine-capi-arengine.md#arengine_artrackingstatereason) \*outTrackingStateReason) | 获取相机的当前追踪状态为[ARENGINE\_TRACKING\_STATE\_PAUSED](arengine-capi-arengine.md#arengine_artrackingstate)时的原因。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCamera\_GetViewMatrix](arengine-capi-arengine.md#hms_arengine_arcamera_getviewmatrix)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera, float \*outColMajor4x4, int32\_t colMajor4x4Num) | 获取最新帧中相机的视图矩阵。 |
| void [HMS\_AREngine\_ARCamera\_Release](arengine-capi-arengine.md#hms_arengine_arcamera_release)([AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*camera) | 释放对相机的引用。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraConfig\_Create](arengine-capi-arengine.md#hms_arengine_arcameraconfig_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) \*\*outCameraConfig) | 创建一个相机配置对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetCameraLensFacing](arengine-capi-arengine.md#hms_arengine_arconfig_getcameralensfacing)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARCameraLensFacing](arengine-capi-arengine.md#arengine_arcameralensfacing) \*outFacing) | 获取相机镜头朝向。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetMultiFaceMode](arengine-capi-arengine.md#hms_arengine_arconfig_getmultifacemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARMultiFaceMode](arengine-capi-arengine.md#arengine_armultifacemode) \*outFaceMode) | 获取多人脸检测模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetCameraLensFacing](arengine-capi-arengine.md#hms_arengine_arconfig_setcameralensfacing)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARCameraLensFacing](arengine-capi-arengine.md#arengine_arcameralensfacing) facing) | 设置相机镜头朝向，参见[AREngine\_ARCameraLensFacing](arengine-capi-arengine.md#arengine_arcameralensfacing)。facing设置为ARENGINE\_CAMERA\_FACING\_FRONT时，需要调用[HMS\_AREngine\_ARConfig\_SetARType](arengine-capi-arengine.md#hms_arengine_arconfig_setartype)将AR能力类型设置为ARENGINE\_TYPE\_FACE或ARENGINE\_TYPE\_BODY才生效。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetMultiFaceMode](arengine-capi-arengine.md#hms_arengine_arconfig_setmultifacemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARMultiFaceMode](arengine-capi-arengine.md#arengine_armultifacemode) faceMode) | 设置多人脸检测模式。 |
| void [HMS\_AREngine\_ARCameraConfig\_Destroy](arengine-capi-arengine.md#hms_arengine_arcameraconfig_destroy)([AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) \*cameraConfig) | 释放相机配置对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraConfig\_GetImageDimensions](arengine-capi-arengine.md#hms_arengine_arcameraconfig_getimagedimensions)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight) | 从相机配置对象中获取相机送到CPU处理的图像尺寸。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraConfig\_GetTextureDimensions](arengine-capi-arengine.md#hms_arengine_arcameraconfig_gettexturedimensions)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight) | 从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraIntrinsics\_Create](arengine-capi-arengine.md#hms_arengine_arcameraintrinsics_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*\*outIntrinsics) | 创建一个相机内参对象。 |
| void [HMS\_AREngine\_ARCameraIntrinsics\_Destroy](arengine-capi-arengine.md#hms_arengine_arcameraintrinsics_destroy)([AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*intrinsics) | 释放指定的相机内参对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraIntrinsics\_GetDistortion](arengine-capi-arengine.md#hms_arengine_arcameraintrinsics_getdistortion)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*intrinsics, float \*outDistortion, int32\_t distortionNum) | 获取相机的畸变系数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraIntrinsics\_GetFocalLength](arengine-capi-arengine.md#hms_arengine_arcameraintrinsics_getfocallength)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*intrinsics, float \*outFocalX, float \*outFocalY) | 获取指定相机的焦距，焦距以Pixel为单位。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraIntrinsics\_GetImageDimensions](arengine-capi-arengine.md#hms_arengine_arcameraintrinsics_getimagedimensions)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*intrinsics, int32\_t \*outWidth, int32\_t \*outHeight) | 获取相机图像的尺寸，包括宽度和高度，以Pixel为单位。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARCameraIntrinsics\_GetPrincipalPoint](arengine-capi-arengine.md#hms_arengine_arcameraintrinsics_getprincipalpoint)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics) \*intrinsics, float \*outPrincipalX, float \*outPrincipalY) | 获取指定相机的主轴点，主点位置以Pixel为单位表示。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_Create](arengine-capi-arengine.md#hms_arengine_arconfig_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*\*outConfig) | 创建具有适当默认配置的配置对象。 |
| void [HMS\_AREngine\_ARConfig\_Destroy](arengine-capi-arengine.md#hms_arengine_arconfig_destroy)([AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config) | 释放指定的配置对象的内存空间。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetARType](arengine-capi-arengine.md#hms_arengine_arconfig_getartype)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARType](arengine-capi-arengine.md#arengine_artype) \*type) | 获取当前使用的AR能力类型。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetARType](arengine-capi-arengine.md#hms_arengine_arconfig_setartype)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARType](arengine-capi-arengine.md#arengine_artype) type) | 设置当前要使用的AR能力类型。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetCameraPreviewMode](arengine-capi-arengine.md#hms_arengine_arconfig_getcamerapreviewmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPreviewMode](arengine-capi-arengine.md#arengine_arpreviewmode) \*outMode) | 获取当前的预览模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetCameraPreviewMode](arengine-capi-arengine.md#hms_arengine_arconfig_setcamerapreviewmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPreviewMode](arengine-capi-arengine.md#arengine_arpreviewmode) mode) | 设置预览模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetDepthMode](arengine-capi-arengine.md#hms_arengine_arconfig_getdepthmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARDepthMode](arengine-capi-arengine.md#arengine_ardepthmode) \*outDepthMode) | 获取当前的深度模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetDepthMode](arengine-capi-arengine.md#hms_arengine_arconfig_setdepthmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARDepthMode](arengine-capi-arengine.md#arengine_ardepthmode) depthMode) | 设置深度模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetFocusMode](arengine-capi-arengine.md#hms_arengine_arconfig_getfocusmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARFocusMode](arengine-capi-arengine.md#arengine_arfocusmode) \*focusMode) | 获取当前配置的相机对焦模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetFocusMode](arengine-capi-arengine.md#hms_arengine_arconfig_setfocusmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARFocusMode](arengine-capi-arengine.md#arengine_arfocusmode) focusMode) | 设置当前所需的相机对焦模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetMaxMapSize](arengine-capi-arengine.md#hms_arengine_arconfig_getmaxmapsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, uint64\_t \*maxMapSize) | 获取地图数据使用的最大内存大小。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetMaxMapSize](arengine-capi-arengine.md#hms_arengine_arconfig_setmaxmapsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, uint64\_t maxMapSize) | 设置地图数据最大使用内存大小。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetMeshMode](arengine-capi-arengine.md#hms_arengine_arconfig_getmeshmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARMeshMode](arengine-capi-arengine.md#arengine_armeshmode) \*outMeshMode) | 获取当前mesh模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetMeshMode](arengine-capi-arengine.md#hms_arengine_arconfig_setmeshmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARMeshMode](arengine-capi-arengine.md#arengine_armeshmode) meshMode) | 设置mesh模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetPlaneFindingMode](arengine-capi-arengine.md#hms_arengine_arconfig_getplanefindingmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPlaneFindingMode](arengine-capi-arengine.md#arengine_arplanefindingmode) \*planeFindingMode) | 获取当前配置的平面识别模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetPlaneFindingMode](arengine-capi-arengine.md#hms_arengine_arconfig_setplanefindingmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPlaneFindingMode](arengine-capi-arengine.md#arengine_arplanefindingmode) planeFindingMode) | 设置当前所需的平面识别模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetPoseMode](arengine-capi-arengine.md#hms_arengine_arconfig_getposemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPoseMode](arengine-capi-arengine.md#arengine_arposemode) \*poseMode) | 获取相机输出的位姿坐标系对齐模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetPoseMode](arengine-capi-arengine.md#hms_arengine_arconfig_setposemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPoseMode](arengine-capi-arengine.md#arengine_arposemode) poseMode) | 设置相机输出的位姿坐标系对齐模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetPowerMode](arengine-capi-arengine.md#hms_arengine_arconfig_getpowermode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPowerMode](arengine-capi-arengine.md#arengine_arpowermode) \*powerMode) | 获取当前配置的功耗模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetPowerMode](arengine-capi-arengine.md#hms_arengine_arconfig_setpowermode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARPowerMode](arengine-capi-arengine.md#arengine_arpowermode) powerMode) | 设置功耗模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetPreviewSize](arengine-capi-arengine.md#hms_arengine_arconfig_setpreviewsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, uint32\_t width, uint32\_t height) | 设置预览画面尺寸。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetSemanticDenseMode](arengine-capi-arengine.md#hms_arengine_arconfig_getsemanticdensemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARSemanticDenseMode](arengine-capi-arengine.md#arengine_arsemanticdensemode) \*outSemanticDenseMode) | 获取已设置的高精几何重建模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetSemanticDenseMode](arengine-capi-arengine.md#hms_arengine_arconfig_setsemanticdensemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARSemanticDenseMode](arengine-capi-arengine.md#arengine_arsemanticdensemode) semanticDenseMode) | 设置当前所需的高精几何重建模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetSemanticMode](arengine-capi-arengine.md#hms_arengine_arconfig_getsemanticmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARSemanticMode](arengine-capi-arengine.md#arengine_arsemanticmode) \*mode) | 获取已设置成功的语义识别模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetSemanticMode](arengine-capi-arengine.md#hms_arengine_arconfig_setsemanticmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARSemanticMode](arengine-capi-arengine.md#arengine_arsemanticmode) mode) | 设置当前所需的语义识别模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetUpdateMode](arengine-capi-arengine.md#hms_arengine_arconfig_getupdatemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARUpdateMode](arengine-capi-arengine.md#arengine_arupdatemode) \*updateMode) | 获取当前配置的预览更新模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetUpdateMode](arengine-capi-arengine.md#hms_arengine_arconfig_setupdatemode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARUpdateMode](arengine-capi-arengine.md#arengine_arupdatemode) updateMode) | 设置预览更新模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetPhotoStreamSize](arengine-capi-arengine.md#hms_arengine_arconfig_setphotostreamsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, uint32\_t width, uint32\_t height) | 当[AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode)为ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO时，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetImageStreamMode](arengine-capi-arengine.md#hms_arengine_arconfig_setimagestreammode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode) mode) | 设置图像流模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_GetImageStreamMode](arengine-capi-arengine.md#hms_arengine_arconfig_getimagestreammode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, [AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode) outMode) | 获取图像流模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFace\_AcquireBlendShapes](arengine-capi-arengine.md#hms_arengine_arface_acquireblendshapes)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface) \*face, [AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) \*\*outBlendshapes) | 获取人脸微表情对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFace\_AcquireGeometry](arengine-capi-arengine.md#hms_arengine_arface_acquiregeometry)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface) \*face, [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*\*outGeometry) | 获取人脸拓扑结构对象，即人脸Mesh对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFace\_AcquireViewMatrix](arengine-capi-arengine.md#hms_arengine_arface_acquireviewmatrix)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface) \*face, float \*outColMajor4x4, int32\_t colMajor4x4Num) | 获取当前人脸的面视图矩阵。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFace\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_arface_getcenterpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface) \*face, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 获取人脸Mesh中心的位姿。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceBlendShapes\_AcquireData](arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_acquiredata)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) \*blendshapes, const float \*\*outData) | 获取微表情数据的集合。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceBlendShapes\_AcquireTypes](arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_acquiretypes)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) \*blendshapes, const [AREngine\_ARAnimojiBlendShape](arengine-capi-arengine.md#arengine_aranimojiblendshape) \*\*types) | 获取所有微表情参数类型数组。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceBlendShapes\_GetCount](arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_getcount)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) \*blendshapes, int32\_t \*outSize) | 获取微表情参数个数。 |
| void [HMS\_AREngine\_ARFaceBlendShapes\_Release](arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_release)([AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes) \*blendshapes) | 释放blendShapes对象，即由[HMS\_AREngine\_ARFace\_AcquireBlendShapes](arengine-capi-arengine.md#hms_arengine_arface_acquireblendshapes)创建的对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_AcquireIndices](arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquireindices)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, const int32\_t \*\*data) | 获取人脸Mesh三角面下标数组。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_AcquireTexCoord](arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquiretexcoord)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, const float \*\*outData) | 获取人脸Mesh纹理坐标点数组。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_AcquireTriangleLabels](arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquiretrianglelabels)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, const [AREngine\_ARAnimojiTriangleLabel](arengine-capi-arengine.md#arengine_aranimojitrianglelabel) \*\*data) | 获取人脸Mesh三角面标签。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_AcquireVertices](arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquirevertices)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, const float \*\*outData) | 获取人脸Mesh顶点数组。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_GetIndicesSize](arengine-capi-arengine.md#hms_arengine_arfacegeometry_getindicessize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, int32\_t \*outSize) | 获取人脸Mesh三角面下标数组大小。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_GetTexCoordSize](arengine-capi-arengine.md#hms_arengine_arfacegeometry_gettexcoordsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, int32\_t \*outSize) | 获取人脸Mesh纹理坐标点数组大小。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_GetTriangleCount](arengine-capi-arengine.md#hms_arengine_arfacegeometry_gettrianglecount)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, int32\_t \*outSize) | 获取人脸Mesh三角面个数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_GetTriangleLabelsSize](arengine-capi-arengine.md#hms_arengine_arfacegeometry_gettrianglelabelssize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, int32\_t \*outSize) | 获取人脸Mesh三角面标签个数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFaceGeometry\_GetVerticesSize](arengine-capi-arengine.md#hms_arengine_arfacegeometry_getverticessize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry, int32\_t \*outSize) | 获取人脸Mesh顶点数组大小。 |
| void [HMS\_AREngine\_ARFaceGeometry\_Release](arengine-capi-arengine.md#hms_arengine_arfacegeometry_release)([AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry) \*geometry) | 释放当前人脸几何体对象，即由 [HMS\_AREngine\_ARFace\_AcquireGeometry](arengine-capi-arengine.md#hms_arengine_arface_acquiregeometry)创建的对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireCamera](arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera) \*\*outCamera) | 获取当前帧的相机参数对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireCameraImage](arengine-capi-arengine.md#hms_arengine_arframe_acquirecameraimage)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*\*outImage) | 获取相机的当前帧的图像。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage](arengine-capi-arengine.md#hms_arengine_arframe_acquirecameraphotoimage)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [HMS\_AREngine\_PhotoAvailableCallback](arengine-capi-arengine.md#hms_arengine_photoavailablecallback) photoCallback) | 获取当前帧的拍照流图片。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthconfidenceimage)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*\*outConfidenceImage) | 获取当前帧的深度置信度图像。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthimage16bits)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*\*outDepthImage); | 获取当前帧的深度图像。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquirePointCloud](arengine-capi-arengine.md#hms_arengine_arframe_acquirepointcloud)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) \*\*outPointCloud) | 返回当前帧的点云数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireSceneMesh](arengine-capi-arengine.md#hms_arengine_arframe_acquirescenemesh)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*\*outSceneMesh) | 获取当前帧的mesh信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](arengine-capi-arengine.md#hms_arengine_arframe_acquiresemanticdensedata)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) \*\*outSemanticDenseData); | 获取当前帧的高精几何重建对象数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_Create](arengine-capi-arengine.md#hms_arengine_arframe_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*\*outFrame) | 创建一个新的[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到\*outFrame中。 |
| void [HMS\_AREngine\_ARFrame\_Destroy](arengine-capi-arengine.md#hms_arengine_arframe_destroy)([AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame) | 删除当前[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged](arengine-capi-arengine.md#hms_arengine_arframe_getdisplaygeometrychanged)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, int32\_t \*outGeometryChangeState) | 获取显示（长宽和旋转）是否发生变化。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_GetTimestamp](arengine-capi-arengine.md#hms_arengine_arframe_gettimestamp)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, int64\_t \*outTimestampNs) | 获取当前帧对应的时间戳信息，单位为ns。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_GetUpdatedTrackables](arengine-capi-arengine.md#hms_arengine_arframe_getupdatedtrackables)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, [AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype) filterType, [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) \*outTrackableList) | 获取[HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)更新后发生变化的指定类型的可跟踪对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_HitTest](arengine-capi-arengine.md#hms_arengine_arframe_hittest)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, float pixelX, float pixelY, [AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) \*hitResultList) | 从摄像头发射一条射线，该射线的方向由预览区上的点（pixelX，pixelY）确定，（pixelX，pixelY）可以通过XComponent的[DispatchTouchEvent](ent-native-xcomponent-oh-nativexcomponent-callback.md#dispatchtouchevent)事件获取。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords](arengine-capi-arengine.md#hms_arengine_arframe_transformdisplayuvcoords)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*frame, int32\_t elementSize, const float \*uvsIn, float \*uvsOut) | 调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResult\_AcquireNewAnchor](arengine-capi-arengine.md#hms_arengine_arhitresult_acquirenewanchor)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*hitResult, [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*\*outAnchor) | 在碰撞命中位置创建一个新的锚点。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResult\_AcquireTrackable](arengine-capi-arengine.md#hms_arengine_arhitresult_acquiretrackable)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*hitResult, [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*\*outTrackable) | 获取被命中的可追踪对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResult\_Create](arengine-capi-arengine.md#hms_arengine_arhitresult_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*\*outHitResult) | 创建一个空的命中检测结果对象。 |
| void [HMS\_AREngine\_ARHitResult\_Destroy](arengine-capi-arengine.md#hms_arengine_arhitresult_destroy)([AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*hitResult) | 释放命中检测结果对象使用的内存。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResult\_GetDistance](arengine-capi-arengine.md#hms_arengine_arhitresult_getdistance)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*hitResult, float \*outDistance) | 返回从相机到命中位置的距离，以m为单位。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResult\_GetHitPose](arengine-capi-arengine.md#hms_arengine_arhitresult_gethitpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*hitResult, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 获取交点的位姿。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResultList\_Create](arengine-capi-arengine.md#hms_arengine_arhitresultlist_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) \*\*outHitResultList) | 创建一个命中检测结果对象列表。 |
| void [HMS\_AREngine\_ARHitResultList\_Destroy](arengine-capi-arengine.md#hms_arengine_arhitresultlist_destroy)([AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) \*hitResultList) | 释放命中检测结果对象列表，以及其中的所有命中检测结果对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResultList\_GetItem](arengine-capi-arengine.md#hms_arengine_arhitresultlist_getitem)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) \*hitResultList, int32\_t index, [AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult) \*outHitResult) | 在命中检测结果列表中获取指定索引的命中检测结果对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARHitResultList\_GetSize](arengine-capi-arengine.md#hms_arengine_arhitresultlist_getsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist) \*hitResultList, int32\_t \*outSize) | 获取命中检测结果对象列表中包含的对象数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetFormat](arengine-capi-arengine.md#hms_arengine_arimage_getformat)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, [AREngine\_ARImageFormat](arengine-capi-arengine.md#arengine_arimageformat) \*outFormat) | 获取当前帧的图像格式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetHeight](arengine-capi-arengine.md#hms_arengine_arimage_getheight)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int32\_t \*outHeight) | 获取当前帧的图像数据的高度。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetWidth](arengine-capi-arengine.md#hms_arengine_arimage_getwidth)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int32\_t \*outWidth) | 获取当前帧的图像数据的宽度。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetNativeBuffer](arengine-capi-arengine.md#hms_arengine_arimage_getnativebuffer)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, [OH\_NativeBuffer](capi-oh-nativebuffer.md) \*\*outNativeBuffer); | 获取当前帧图像对象的NativeBuffer数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetPlaneCount](arengine-capi-arengine.md#hms_arengine_arimage_getplanecount)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int32\_t \*outCount) | 获取当前帧图像的平面数量。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetPlaneData](arengine-capi-arengine.md#hms_arengine_arimage_getplanedata)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int32\_t planeIndex, const uint8\_t \*\*outData, int32\_t \*outLength) | 获取当前帧图像的平面数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetPlanePixelStride](arengine-capi-arengine.md#hms_arengine_arimage_getplanepixelstride)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int32\_t planeIndex, int32\_t \*outPixelStride) | 获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetPlaneRowStride](arengine-capi-arengine.md#hms_arengine_arimage_getplanerowstride)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int32\_t planeIndex, int32\_t \*outRowStride) | 获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARImage\_GetTimestamp](arengine-capi-arengine.md#hms_arengine_arimage_gettimestamp)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image, int64\_t \*outTimestamp) | 获取图像的时间戳。 |
| void [HMS\_AREngine\_ARImage\_Release](arengine-capi-arengine.md#hms_arengine_arimage_release)([AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage) \*image) | 释放当前帧的图像对象，由[HMS\_AREngine\_ARFrame\_AcquireCameraImage](arengine-capi-arengine.md#hms_arengine_arframe_acquirecameraimage)创建的对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_AcquireSubsumedBy](arengine-capi-arengine.md#hms_arengine_arplane_acquiresubsumedby)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*\*outSubsumedBy) | 获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetExtentX](arengine-capi-arengine.md#hms_arengine_arplane_getextentx)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, float \*outExtentX) | 获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetExtentZ](arengine-capi-arengine.md#hms_arengine_arplane_getextentz)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, float \*outExtentZ) | 获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetLabel](arengine-capi-arengine.md#hms_arengine_arplane_getlabel)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, [AREngine\_ARSemanticPlaneLabel](arengine-capi-arengine.md#arengine_arsemanticplanelabel) \*label) | 获取平面的语义类型，如桌面、地板等。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetPolygon](arengine-capi-arengine.md#hms_arengine_arplane_getpolygon)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, float \*outPolygonXz, int32\_t polygonSize) | 获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetPolygonSize](arengine-capi-arengine.md#hms_arengine_arplane_getpolygonsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, int32\_t \*outPolygonSize) | 获取检测到平面的二维顶点数组大小。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_GetType](arengine-capi-arengine.md#hms_arengine_arplane_gettype)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, [AREngine\_ARPlaneType](arengine-capi-arengine.md#arengine_arplanetype) \*outPlaneType) | 获取平面的类型。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_IsPoseInExtents](arengine-capi-arengine.md#hms_arengine_arplane_isposeinextents)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, const [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose, int32\_t \*outPoseInExtents) | 判断位姿是否位于平面的矩形范围内。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPlane\_IsPoseInPolygon](arengine-capi-arengine.md#hms_arengine_arplane_isposeinpolygon)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*plane, const [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose, int32\_t \*outPoseInPolygon) | 判断位姿是否位于平面的多边形范围内。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPoint\_GetOrientationMode](arengine-capi-arengine.md#hms_arengine_arpoint_getorientationmode)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint) \*point, [AREngine\_ARPointOrientationMode](arengine-capi-arengine.md#arengine_arpointorientationmode) \*outOrientationMode) | 获取输入点的朝向模式。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPoint\_GetPose](arengine-capi-arengine.md#hms_arengine_arpoint_getpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint) \*point, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outPose) | 获取输入点的位姿信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPointCloud\_GetData](arengine-capi-arengine.md#hms_arengine_arpointcloud_getdata)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) \*pointCloud, const float \*\*outPointCloudData) | 获取点云中所有点的坐标及置信度数组。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPointCloud\_GetNumberOfPoints](arengine-capi-arengine.md#hms_arengine_arpointcloud_getnumberofpoints)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) \*pointCloud, int32\_t \*outNumberOfPoints) | 获取点云中所有点的坐标及置信度数组大小。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPointCloud\_GetTimestamp](arengine-capi-arengine.md#hms_arengine_arpointcloud_gettimestamp)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) \*pointCloud, int64\_t \*outTimestampNs) | 获取检测到当前特征点云的时间，以ns为单位。 |
| void [HMS\_AREngine\_ARPointCloud\_Release](arengine-capi-arengine.md#hms_arengine_arpointcloud_release)([AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud) \*pointCloud) | 释放点云对象使用的内存。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPose\_Create](arengine-capi-arengine.md#hms_arengine_arpose_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const float \*poseRaw, const uint32\_t poseRawSize, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*\*outPose) | 分配并初始化一个新的位姿对象。 |
| void [HMS\_AREngine\_ARPose\_Destroy](arengine-capi-arengine.md#hms_arengine_arpose_destroy)([AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose) | 释放位姿对象使用的内存。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPose\_GetMatrix](arengine-capi-arengine.md#hms_arengine_arpose_getmatrix)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose, float \*outMatrixColMajor4x4, int32\_t matrixColMajor4x4Size) | 将位姿数据转换成4X4的矩阵。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARPose\_GetPoseRaw](arengine-capi-arengine.md#hms_arengine_arpose_getposeraw)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose, float \*outPoseRaw, int32\_t poseRawSize) | 从位姿对象提取位姿数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlist)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*sceneMesh, int32\_t \*outData, int32\_t dataSize) | 获取mesh面片的索引集合。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*sceneMesh, int32\_t \*outSize) | 获取mesh面片的索引个数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquirevertexlist)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*sceneMesh, float \*outData, int32\_t dataSize) | 获取mesh的顶点集合。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSceneMesh\_AcquireVertexNormalList](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquirevertexnormallist)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*sceneMesh, float \*outData, int32\_t dataSize) | 获取mesh面片的法向量集合。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireverticessize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*sceneMesh, int32\_t \*outSize) | 获取mesh的顶点个数。 |
| void [HMS\_AREngine\_ARSceneMesh\_Release](arengine-capi-arengine.md#hms_arengine_arscenemesh_release)([AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh) \*SceneMesh) | 释放当前帧的mesh信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) \*semanticDenseData, [AREngine\_ARSemanticDenseCubeData](arengine-struct-arsemanticdensecubedata.md) \*\*outCubeData) | 获取识别到的高精几何重建对象数据中的立方体数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedatasize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) \*semanticDenseData, int64\_t \*outSize) | 获取识别到的高精几何重建对象数据中的立方体数量。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSemanticDense\_AcquirePointData](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirepointdata)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) \*semanticDenseData, [AREngine\_ARSemanticDensePointData](arengine-struct-arsemanticdensepointdata.md) \*\*outPointData) | 获取识别到的高精几何重建对象数据中的稠密点云数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSemanticDense\_AcquirePointDataSize](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirepointdatasize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) \*semanticDenseData, int64\_t \*outSize) | 获取识别到的高精几何重建对象数据中的稠密点云数量。 |
| void [HMS\_AREngine\_ARSemanticDense\_Release](arengine-capi-arengine.md#hms_arengine_arsemanticdense_release)([AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata) \*semanticDenseData) | 释放高精几何重建对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_AcquireNewAnchor](arengine-capi-arengine.md#hms_arengine_arsession_acquirenewanchor)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose, [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*\*outAnchor) | 创建一个持续跟踪的锚点。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Configure](arengine-capi-arengine.md#hms_arengine_arsession_configure)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config) | 配置[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)会话。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Create](arengine-capi-arengine.md#hms_arengine_arsession_create)(void \*env, void \*applicationContext, [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*\*outSessionPointer) | 创建一个新的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)会话。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Create\_Human\_Perception](arengine-capi-arengine.md#hms_arengine_arsession_create_human_perception)(void \*env, void \*applicationContext, [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*\*outSessionPointer) | 创建一个新的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)人体追踪会话。 |
| void [HMS\_AREngine\_ARSession\_Destroy](arengine-capi-arengine.md#hms_arengine_arsession_destroy)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session) | 释放[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)会话使用的资源。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_GetCameraConfig](arengine-capi-arengine.md#hms_arengine_arsession_getcameraconfig)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig) \*outCameraConfig) | 获取相机配置信息。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_GetAllAnchors](arengine-capi-arengine.md#hms_arengine_arsession_getallanchors)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) \*outAnchorList) | 获取所有锚点，包括[AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate)中包含的所有状态下的锚点。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_GetAllTrackables](arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype) filterType, [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) \*outTrackableList) | 获取所有指定类型的可跟踪对象集合。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Pause](arengine-capi-arengine.md#hms_arengine_arsession_pause)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session) | 暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Resume](arengine-capi-arengine.md#hms_arengine_arsession_resume)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session) | 开始运行[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)，或者在调用[HMS\_AREngine\_ARSession\_Pause](arengine-capi-arengine.md#hms_arengine_arsession_pause)以后恢复[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)的运行状态。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_SetCameraGLTexture](arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, uint32\_t textureId) | 设置可用于存储相机预览流数据的OpenGL纹理。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_SetDisplayGeometry](arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARPoseType](arengine-capi-arengine.md#arengine_arposetype) rotation, int32\_t width, int32\_t height) | 设置显示的高和宽，以Pixel为单位。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Stop](arengine-capi-arengine.md#hms_arengine_arsession_stop)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session) | 停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe) \*outFrame) | 更新AR Engine的计算结果。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTarget\_GetAxisAlignedBoundingBox](arengine-capi-arengine.md#hms_arengine_artarget_getaxisalignedboundingbox)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget) \*target, float \*outAabb, int32\_t aabbSize) | 获取语义物体最小外接包围盒坐标，坐标格式为（xmin，ymin，zmin，xmax，ymax，zmax)。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTarget\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_artarget_getcenterpose)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget) \*target, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*outARPose) | 获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTarget\_GetRadius](arengine-capi-arengine.md#hms_arengine_artarget_getradius)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget) \*target, float \*radius) | 获取语义物体的球体半径。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTarget\_GetShapeType](arengine-capi-arengine.md#hms_arengine_artarget_getshapetype)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget) \*target, [AREngine\_ARTargetShapeLabel](arengine-capi-arengine.md#arengine_artargetshapelabel) \*shape) | 获取语义物体的形状类型。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackable\_AcquireNewAnchor](arengine-capi-arengine.md#hms_arengine_artrackable_acquirenewanchor)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*trackable, [AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose) \*pose, [AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor) \*\*outAnchor) | 通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackable\_GetAnchors](arengine-capi-arengine.md#hms_arengine_artrackable_getanchors)([AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*trackable, [AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist) \*outAnchorList) | 获取绑定到输入可跟踪对象的锚点对象列表。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackable\_GetTrackingState](arengine-capi-arengine.md#hms_arengine_artrackable_gettrackingstate)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*trackable, [AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate) \*outTrackingState) | 获取当前可跟踪对象的跟踪状态。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackable\_GetType](arengine-capi-arengine.md#hms_arengine_artrackable_gettype)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*trackable, [AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype) \*outTrackableType) | 获取可跟踪对象的类型。 |
| void [HMS\_AREngine\_ARTrackable\_Release](arengine-capi-arengine.md#hms_arengine_artrackable_release)([AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*trackable) | 释放可跟踪对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackableList\_AcquireItem](arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) \*trackableList, int32\_t index, [AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable) \*\*outTrackable) | 从可跟踪列表中获取指定index的对象。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackableList\_Create](arengine-capi-arengine.md#hms_arengine_artrackablelist_create)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) \*\*outTrackableList) | 创建一个可跟踪对象列表。 |
| void [HMS\_AREngine\_ARTrackableList\_Destroy](arengine-capi-arengine.md#hms_arengine_artrackablelist_destroy)([AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) \*trackableList) | 释放可跟踪对象列表，以及它持有的所有锚点引用。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARTrackableList\_GetSize](arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist) \*trackableList, int32\_t \*outSize) | 获取此列表中的可跟踪对象的数量。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonConfidence](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconfidence)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, const float \*\*outConfidence) | 获取人体对象每个骨骼点检测的置信度。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonConnection](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnection)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, const [AREngine\_ARBodySkeletonType](arengine-capi-arengine.md#arengine_arbodyskeletontype) \*\*outSkeletonConnection) | 获取人体对象骨骼点之间的链接关系数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonConnectionSize](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnectionsize)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, int32\_t \*outConnectionCount) | 获取人体对象骨骼点之间的链接关系总数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonTypes](arengine-capi-arengine.md#hms_arengine_arbody_getskeletontypes)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, const [AREngine\_ARBodySkeletonType](arengine-capi-arengine.md#arengine_arbodyskeletontype) \*\*outSkeletonTypes) | 获取识别出的人体对象骨骼点类型。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonPointCount](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointcount)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, int32\_t \*outPointCount) | 获取人体对象的骨骼点个数。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonPointData2D](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointdata2d)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, const float \*\*outSkeletonPointData2D) | 当运行2D骨骼跟踪算法时，返回人体骨骼点的坐标数据。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetSkeletonPointIsValid](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointisvalid)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, const int32\_t \*\*outSkeletonPointIsValid) | 获取人体对象骨骼点的坐标是否有效，返回有效性数组。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetBodyTrackId](arengine-capi-arengine.md#hms_arengine_arbody_getbodytrackid)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, const int32\_t \*outBodyTrackId) | 获取指定人体对象的标识。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARBody\_GetBodyTimeStamp](arengine-capi-arengine.md#hms_arengine_arbody_getbodytimestamp)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, const [AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody) \*body, int64\_t \*timeStamp) | 获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。 |
| [AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus) [HMS\_AREngine\_ARConfig\_SetBodyDetectedNum](arengine-capi-arengine.md#hms_arengine_arconfig_setbodydetectednum)(const [AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession) \*session, [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig) \*config, int32\_t maxNum) | 设置追踪人数。 |

## 宏定义说明

PhoneTabletTV

### ARENGINE\_AABB\_POINT\_SIZE

PhoneTabletTV

```
1. const static int32_t ARENGINE_AABB_POINT_SIZE = 6
```

**描述**

包围盒坐标集数组大小。

**起始版本：** 5.0.0(12)

### ARENGINE\_DISTORTION\_COUNT

PhoneTabletTV

```
1. const static int32_t ARENGINE_DISTORTION_COUNT = 5
```

**描述**

相机畸变参数的个数。

**起始版本：** 5.0.0(12)

### ARENGINE\_POSE\_RAW\_SIZE

PhoneTabletTV

```
1. const static int32_t ARENGINE_POSE_RAW_SIZE = 7
```

**描述**

位姿数据数组大小。

**起始版本：** 5.0.0(12)

### ARENGINE\_VIEW\_MATRIX\_SIZE

PhoneTabletTV

```
1. const static int32_t ARENGINE_VIEW_MATRIX_SIZE = 16
```

**描述**

变换矩阵数组大小。

**起始版本：** 5.0.0(12)

## 类型定义说明

PhoneTabletTV

### AREngine\_ARAnchor

PhoneTabletTV

```
1. typedef struct AREngine_ARAnchor AREngine_ARAnchor
```

**描述**

锚点对象。

描述与可跟踪对象关联的空间位置。

**起始版本：** 5.0.0(12)

### AREngine\_ARAnchorList

PhoneTabletTV

```
1. typedef struct AREngine_ARAnchorList AREngine_ARAnchorList
```

**描述**

锚点对象列表。

包含一系列锚点对象。

**起始版本：** 5.0.0(12)

### AREngine\_ARAugmentedImage

PhoneTabletTV

```
1. typedef struct AREngine_ARAugmentedImage AREngine_ARAugmentedImage
```

**描述**

跟踪图像对象。

**起始版本：** 5.1.0(18)

### AREngine\_ARAugmentedImageDatabase

PhoneTabletTV

```
1. typedef struct AREngine_ARAugmentedImageDatabase AREngine_ARAugmentedImageDatabase
```

**描述**

跟踪图像数据库对象。

**起始版本：** 5.1.0(18)

### AREngine\_ARCamera

PhoneTabletTV

```
1. typedef struct AREngine_ARCamera AREngine_ARCamera
```

**描述**

当前帧对应的相机信息。

**起始版本：** 5.0.0(12)

### AREngine\_ARCameraConfig

PhoneTabletTV

```
1. typedef struct AREngine_ARCameraConfig AREngine_ARCameraConfig
```

**描述**

相机的配置信息。

如CPU图像的尺寸，GPU纹理的尺寸。

**起始版本：** 5.0.0(12)

### AREngine\_ARCameraIntrinsics

PhoneTabletTV

```
1. typedef struct AREngine_ARCameraIntrinsics AREngine_ARCameraIntrinsics
```

**描述**

相机内参。

包括fx；fy；cx；cy；畸变参数。

**起始版本：** 5.0.0(12)

### AREngine\_ARConfig

PhoneTabletTV

```
1. typedef struct AREngine_ARConfig AREngine_ARConfig
```

**描述**

用于配置[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)的能力项（使用哪些能力、模式等）。

**起始版本：** 5.0.0(12)

### AREngine\_ARFace

PhoneTabletTV

```
1. typedef struct AREngine_ARFace AREngine_ARFace
```

**描述**

跟踪的人脸对象。

**起始版本：** 6.1.0(23)

### AREngine\_ARFaceGeometry

PhoneTabletTV

```
1. typedef struct AREngine_ARFaceGeometry AREngine_ARFaceGeometry
```

**描述**

人脸拓扑结构对象。

**起始版本：** 6.1.0(23)

### AREngine\_ARFaceBlendShapes

PhoneTabletTV

```
1. typedef struct AREngine_ARFaceBlendShapes AREngine_ARFaceBlendShapes
```

**描述**

人脸微表情对象。

**起始版本：** 6.1.0(23)

### AREngine\_ARFaceLandmark

PhoneTabletTV

```
1. typedef struct AREngine_ARFaceLandmark AREngine_ARFaceLandmark
```

**描述**

人脸关键点对象。

**起始版本：** 6.1.0(23)

### AREngine\_ARFrame

PhoneTabletTV

```
1. typedef struct AREngine_ARFrame AREngine_ARFrame
```

**描述**

AR Engine处理的一帧数据。

**起始版本：** 5.0.0(12)

### AREngine\_ARHitResult

PhoneTabletTV

```
1. typedef struct AREngine_ARHitResult AREngine_ARHitResult
```

**描述**

命中检测结果对象。

描述单个可跟踪对象的命中检测结果。

**起始版本：** 5.0.0(12)

### AREngine\_ARHitResultList

PhoneTabletTV

```
1. typedef struct AREngine_ARHitResultList AREngine_ARHitResultList
```

**描述**

命中检测结果列表。

包含一系列命中检测的结果对象。

**起始版本：** 5.0.0(12)

### AREngine\_ARImage

PhoneTabletTV

```
1. typedef struct AREngine_ARImage AREngine_ARImage
```

**描述**

相机视频流帧对象。

**起始版本：** 5.0.0(12)

### AREngine\_ARPlane

PhoneTabletTV

```
1. typedef struct AREngine_ARPlane AREngine_ARPlane
```

**描述**

平面对象。

描述被检测到的可跟踪平面信息。

**起始版本：** 5.0.0(12)

### AREngine\_ARPoint

PhoneTabletTV

```
1. typedef struct AREngine_ARPoint AREngine_ARPoint
```

**描述**

点对象。

描述被检测到的可跟踪点数据。

**起始版本：** 5.0.0(12)

### AREngine\_ARPointCloud

PhoneTabletTV

```
1. typedef struct AREngine_ARPointCloud AREngine_ARPointCloud
```

**描述**

可跟踪的3D点云的集合。

**起始版本：** 5.0.0(12)

### AREngine\_ARPose

PhoneTabletTV

```
1. typedef struct AREngine_ARPose AREngine_ARPose
```

**描述**

位姿对象。

描述从一个坐标系到另一个坐标系的不可变的刚体变换，例如平移或旋转。

详细可参考[世界坐标系与位姿示意](../harmonyos-guides/arengine-get-pose-conversion.md#世界坐标系与位姿示意)。

**起始版本：** 5.0.0(12)

### AREngine\_ARSceneMesh

PhoneTabletTV

```
1. typedef struct AREngine_ARSceneMesh AREngine_ARSceneMesh
```

**描述**

环境mesh数据的集合。

**起始版本：** 5.1.0(18)

### AREngine\_ARSemanticDenseData

PhoneTabletTV

```
1. typedef struct AREngine_ARSemanticDenseData AREngine_ARSemanticDenseData
```

**描述**

表示高精几何重建对象数据的集合。

**起始版本：** 6.0.0(20)

### AREngine\_ARSession

PhoneTabletTV

```
1. typedef struct AREngine_ARSession AREngine_ARSession
```

**描述**

管理AR Engine的系统状态。

**起始版本：** 5.0.0(12)

### AREngine\_ARTarget

PhoneTabletTV

```
1. typedef struct AREngine_ARTarget AREngine_ARTarget
```

**描述**

物体对象。

描述被检测到的可跟踪语义目标信息，例如语义平面。

**起始版本：** 5.0.0(12)

### AREngine\_ARTrackable

PhoneTabletTV

```
1. typedef struct AREngine_ARTrackable AREngine_ARTrackable
```

**描述**

可跟踪对象，如点、平面等。

应用获取到此对象后，如需对此对象进行具体操作，如通过[HMS\_AREngine\_ARPlane\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose)接口获取平面的中心点位置， 通过[HMS\_AREngine\_ARPoint\_GetPose](arengine-capi-arengine.md#hms_arengine_arpoint_getpose)接口获取点的位姿信息等， 可以根据可跟踪对象类型（通过[HMS\_AREngine\_ARTrackable\_GetType](arengine-capi-arengine.md#hms_arengine_artrackable_gettype)接口获取）转换成相应的对象， 如[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)，[AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint)等，转换方式可参考： [AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*arPlane = reinterpret\_cast<[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane) \*>(trackable)。

**起始版本：** 5.0.0(12)

### AREngine\_ARTrackableList

PhoneTabletTV

```
1. typedef struct AREngine_ARTrackableList AREngine_ARTrackableList
```

**描述**

可跟踪对象列表。

**起始版本：** 5.0.0(12)

### HMS\_AREngine\_PhotoAvailableCallback

PhoneTabletTV

```
1. typedef void (*HMS_AREngine_PhotoAvailableCallback)(OH_NativeBuffer *photoBuffer)
```

**描述**

输出拍照流图像回调。

**起始版本：** 6.0.2(22)

### AREngine\_ARBody

PhoneTabletTV

```
1. typedef struct AREngine_ARBody AREngine_ARBody
```

**描述**

人体对象。

**起始版本：** 6.1.0(23)

## 枚举类型说明

PhoneTabletTV

### AREngine\_FeatureType

PhoneTabletTV

```
1. enum AREngine_FeatureType
```

**描述**

AR特性类别。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_FEATURE\_TYPE\_SLAM | 运动跟踪及平面识别特性。 |
| ARENGINE\_FEATURE\_TYPE\_DEPTH | 深度估计特性。 |
| ARENGINE\_FEATURE\_TYPE\_MESH | 环境Mesh识别特性。 |
| ARENGINE\_FEATURE\_TYPE\_IMAGE | 图像跟踪特性。 |
| ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE | 高精几何重建特性。 |
| ARENGINE\_FEATURE\_TYPE\_SEMANTIC | 平面语义及物体语义特性。 |
| ARENGINE\_FEATURE\_TYPE\_FACE | 人脸识别与跟踪特性。 |
| ARENGINE\_FEATURE\_TYPE\_BODY | 人体骨骼点识别与跟踪特性。 |

### AREngine\_ARAddAugmentedImageReason

PhoneTabletTV

```
1. enum AREngine_ARAddAugmentedImageReason
```

**描述**

跟踪失败的可能原因。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_NONE | 添加的图像符合质量要求。 |
| ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_SIZE\_NOT\_MATCH | 尝试将质量不足（尺寸不匹配）的图像添加到图像数据库。  **说明：** 图像尺寸评价从宽高比、分辨率两个维度进行。建议宽高比、分辨率的评价为Unfit以上。 |
| ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_LIGHT\_ANOMALY | 尝试将质量不足（太亮或太暗）的图像添加到图像数据库中。 |
| ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_FEATURE\_LIMIT | 尝试将质量不足（图像颜色比较单一）的图像添加到图像数据库中。 |
| ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_OTHER | 尝试将质量不足（其他场景，如图片有反光、光斑，重复性内容等）添加到图像数据库中。 |

* 宽高比：

  图像宽度与高度之比，如：640\*480分辨率的图像，其宽高比为1.33，对应评价Excellent。

  | 图像宽高比 | 评价 |
  | --- | --- |
  | [6, ∞) | Invalid |
  | [4, 6) | Bad |
  | [2.5, 4) | Unfit |
  | [2, 2.5) | Fit |
  | [1.5, 2) | Good |
  | [1, 1.5) | Excellent |
* 分辨率：

  以640\*480为基准，按比例计算。如：选取图像分辨率为320\*240，以基准分辨率计算其比值为0.5，对应评价Fit。

  | 图像分辨率比值 | 评价 |
  | --- | --- |
  | [0, 0.2] | Invalid |
  | (0.2, 0.3] | Bad |
  | (0.35, 0.45] | Unfit |
  | (0.45, 0.7] | Fit |
  | (0.7, 0.9] | Good |
  | (0.9, ∞) | Excellent |

### AREngine\_ARAnimojiBlendShape

PhoneTabletTV

```
1. enum AREngine_ARAnimojiBlendShape
```

**描述**

微表情类型。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_ARANIMOJI\_EYE\_BLINK\_LEFT | 左眼闭合。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_DOWN\_LEFT | 左上眼皮微下垂。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_IN\_LEFT | 左眼内部眼皮向左扩。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_OUT\_LEFT | 左眼睑向左扩。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_UP\_LEFT | 左眼上眼皮微上抬。 |
| ARENGINE\_ARANIMOJI\_EYE\_SQUINT\_LEFT | 左下眼睑上抬。 |
| ARENGINE\_ARANIMOJI\_EYE\_WIDE\_LEFT | 左眼瞪大眼。 |
| ARENGINE\_ARANIMOJI\_EYE\_BLINK\_RIGHT | 闭右眼。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_DOWN\_RIGHT | 右上眼皮微下垂。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_IN\_RIGHT | 右眼内部眼皮向右扩。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_OUT\_RIGHT | 右眼睑向右扩。 |
| ARENGINE\_ARANIMOJI\_EYE\_LOOK\_UP\_RIGHT | 右眼上眼皮微上抬。 |
| ARENGINE\_ARANIMOJI\_EYE\_SQUINT\_RIGHT | 右下眼睑上抬。 |
| ARENGINE\_ARANIMOJI\_EYE\_WIDE\_RIGHT | 右眼瞪大眼。 |
| ARENGINE\_ARANIMOJI\_JAW\_FORWARD | 下巴朝前。 |
| ARENGINE\_ARANIMOJI\_JAW\_LEFT | 下巴朝左。 |
| ARENGINE\_ARANIMOJI\_JAW\_RIGHT | 下巴朝右。 |
| ARENGINE\_ARANIMOJI\_JAW\_OPEN | 张嘴。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_FUNNEL | O型嘴。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_PUCKER | 噘嘴。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_LEFT | 嘴巴向左。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_RIGHT | 嘴巴向右。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_SMILE\_LEFT | 左嘴角向左歪。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_SMILE\_RIGHT | 右嘴角向右歪。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_FROWN\_LEFT | 左嘴角下拉。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_FROWN\_RIGHT | 右嘴角下拉。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_DIMPLE\_LEFT | 左酒窝上抬。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_DIMPLE\_RIGHT | 右酒窝上抬。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_STRETCH\_LEFT | 嘴角向左拉。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_STRETCH\_RIGHT | 嘴角向右拉。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_ROLL\_LOWER | 下嘴唇向内抿嘴。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_ROLL\_UPPER | 抿上嘴唇。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_SHRUG\_LOWER | 撅下嘴唇。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_SHRUG\_UPPER | 撅上嘴唇。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_UPPER\_UP | 嘴唇上翻。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_LOWER\_DOWN | 下嘴唇朝下。 |
| ARENGINE\_ARANIMOJI\_MOUTH\_LOWER\_OUT | 下嘴唇朝外。 |
| ARENGINE\_ARANIMOJI\_BROW\_DOWN\_LEFT | 左侧眉毛朝下。 |
| ARENGINE\_ARANIMOJI\_BROW\_DOWN\_RIGHT | 右侧眉毛朝下。 |
| ARENGINE\_ARANIMOJI\_BROW\_INNER\_UP | 双侧眉毛抬眉。 |
| ARENGINE\_ARANIMOJI\_BROW\_OUTER\_UP\_LEFT | 左眉外侧向上抬。 |
| ARENGINE\_ARANIMOJI\_BROW\_OUTER\_UP\_RIGHT | 右眉外侧向上抬。 |
| ARENGINE\_ARANIMOJI\_CHEEK\_PUFF | 鼓腮。 |
| ARENGINE\_ARANIMOJI\_CHEEK\_SQUINT\_LEFT | 左脸颊上抬。 |
| ARENGINE\_ARANIMOJI\_CHEEK\_SQUINT\_RIGHT | 右脸颊上抬。 |
| ARENGINE\_ARANIMOJI\_FROWN\_NOSE\_MOUTH\_UP | 鼻子上抬。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_IN | 舌头在嘴里上下位置。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_OUT\_SLIGHT | 舌头直伸。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_LEFT | 舌头朝左。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_RIGHT | 舌头朝右。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_UP | 舌头朝上。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_DOWN | 舌头朝下。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_LEFT\_UP | 舌头朝左上。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_LEFT\_DOWN | 舌头朝左下。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_RIGHT\_UP | 舌头朝右上。 |
| ARENGINE\_ARANIMOJI\_TONGUE\_RIGHT\_DOWN | 舌头朝右下。 |
| ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_LEFT | 左眼球向左。 |
| ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_RIGHT | 左眼球向右。 |
| ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_UP | 左眼球向上。 |
| ARENGINE\_ARANIMOJI\_LEFT\_EYEBALL\_DOWN | 左眼球向下。 |
| ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_LEFT | 右眼球向左。 |
| ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_RIGHT | 右眼球向右。 |
| ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_UP | 右眼球向上。 |
| ARENGINE\_ARANIMOJI\_RIGHT\_EYEBALL\_DOWN | 右眼球向下。 |

### AREngine\_ARAnimojiTriangleLabel

PhoneTabletTV

```
1. enum AREngine_ARAnimojiTriangleLabel
```

**描述**

人脸三角形面片标签。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_TRIANGLE\_LABEL\_NON\_FACE | 不是脸部位。 |
| ARENGINE\_TRIANGLE\_LABEL\_FACE\_OTHER | 脸部非关键部位。 |
| ARENGINE\_TRIANGLE\_LABEL\_LOWER\_LIP | 下嘴唇。 |
| ARENGINE\_TRIANGLE\_LABEL\_UPPER\_LIP | 上嘴唇。 |
| ARENGINE\_TRIANGLE\_LABEL\_LEFT\_EYE | 左眼睛。 |
| ARENGINE\_TRIANGLE\_LABEL\_RIGHT\_EYE | 右眼睛。 |
| ARENGINE\_TRIANGLE\_LABEL\_LEFT\_BROW | 左眉毛。 |
| ARENGINE\_TRIANGLE\_LABEL\_RIGHT\_BROW | 右眉毛。 |
| ARENGINE\_TRIANGLE\_LABEL\_BROW\_CENTER | 眉心。 |
| ARENGINE\_TRIANGLE\_LABEL\_NOSE | 鼻子。 |

### AREngine\_ARCameraLensFacing

PhoneTabletTV

```
1. enum AREngine_ARCameraLensFacing
```

**描述**

配置摄像机镜头的朝向。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_CAMERA\_FACING\_REAR | 后置摄像头。 |
| ARENGINE\_CAMERA\_FACING\_FRONT | 前置摄像头。 |

### AREngine\_ARConfidenceLevel

PhoneTabletTV

```
1. enum AREngine_ARConfidenceLevel
```

**描述**

深度置信度。

**起始版本：** 5.0.5(17)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_DEPTH\_CONFIDENCE\_LOW | 该深度图像的置信度较低。 |
| ARENGINE\_DEPTH\_CONFIDENCE\_MEDIUM | 该深度图像的置信度中等。 |
| ARENGINE\_DEPTH\_CONFIDENCE\_HIGH | 该深度图像的置信度很高。 |

### AREngine\_ARDepthMode

PhoneTabletTV

```
1. enum AREngine_ARDepthMode
```

**描述**

深度模式。

**起始版本：** 5.0.5(17)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_DEPTH\_MODE\_DISABLED | 不提供深度图像信息。 |
| ARENGINE\_DEPTH\_MODE\_AUTOMATIC | AR Engine会自动尝试从多种深度源获取深度信息。  **说明：** 通常有两种深度源，运动算法和硬件深度传感器 (Time of Flight，简称ToF)。目前仅支持使用主RGB相机所获取的运动深度数据。 |

### AREngine\_ARFocusMode

PhoneTabletTV

```
1. enum AREngine_ARFocusMode
```

**描述**

对焦模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_FOCUS\_MODE\_FIXED | 固定焦点对焦模式。 |
| ARENGINE\_FOCUS\_MODE\_AUTO | 自动对焦模式。 |

### AREngine\_ARImageDatabaseMode

PhoneTabletTV

```
1. enum AREngine_ARImageDatabaseMode
```

**描述**

用于跟踪的特征库图像添加方式。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_ADD\_NORMAL | 正常添加模式。 |
| ARENGINE\_ADD\_AUTO | 循环删除模式。 |

### AREngine\_ARImageFormat

PhoneTabletTV

```
1. enum AREngine_ARImageFormat
```

**描述**

图像数据格式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_IMAGE\_UNKNOWN | 无效的图片格式。 |
| ARENGINE\_IMAGE\_YUV\_420\_888 | YUV\_420\_888格式，适用于处理高分辨率的图像数据。YUV\_420\_888格式由三个数据缓冲区组成：Y分量（平面）的索引为0，U分量为1，V分量为2。Y分量与U/V分量互不相交。也就是说，Y分量的像素步长（Pixel Stride）始终为1。U分量和V分量则具有相同的行步长（Row Stride）和像素步长。 |
| ARENGINE\_IMAGE\_Y\_8 | Y\_8格式，适用于对图像数据要求较低的精度或存储空间的场景。Y\_8格式由一个数据缓冲区组成，其平面索引（Index）为0。该数据缓冲区的数据类型为8位无符号整数。  **起始版本：** 5.0.5(17) |
| ARENGINE\_IMAGE\_Y\_16 | Y\_16格式，适用于对图像数据精度要求较高的场景。Y\_16格式由一个数据缓冲区组成，其平面索引为0。该数据缓冲区的数据类型为16位无符号整数。  **起始版本：** 5.0.5(17) |

### AREngine\_ARImageStreamMode

PhoneTabletTV

```
1. enum AREngine_ARImageStreamMode
```

**描述**

设置图片数据流模式，默认情况下系统设置为ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW | 预览流模式，可通过HMS\_AREngine\_ARFrame\_AcquireCameraImage接口获取预览流图像。 |
| ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO | 拍照流加预览流模式，可通过HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage接口获取拍照流图像。 |

### AREngine\_ARMeshMode

PhoneTabletTV

```
1. enum AREngine_ARMeshMode
```

**描述**

Mesh启用模式。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_MESH\_MODE\_DISABLED | 网格模式关闭  AR Engine不会处理或显示网格数据。 |
| ARENGINE\_MESH\_MODE\_ENABLED | 网格模式开启  AR Engine会尝试处理或显示网格数据。 |

### AREngine\_ARMultiFaceMode

PhoneTabletTV

```
1. enum AREngine_ARMultiFaceMode
```

**描述**

多人脸检测模式。默认关闭多人脸检测模式。当多人脸检测模式开启时[HMS\_AREngine\_ARSession\_GetAllTrackables](arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)返回的可跟踪对象数量最大为3，当多人脸检测模式关闭时HMS\_AREngine\_ARSession\_GetAllTrackables返回的可跟踪对象数量最大为1。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_MULTIFACE\_DISABLE | 多人脸检测模式关闭。 |
| ARENGINE\_MULTIFACE\_ENABLE | 多人脸检测模式开启。 |

### AREngine\_ARPlaneFindingMode

PhoneTabletTV

```
1. enum AREngine_ARPlaneFindingMode
```

**描述**

平面搜索模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_PLANE\_FINDING\_MODE\_DISABLED | 禁用平面检测。 |
| ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL | 只检测水平面，如地板和桌子。 |
| ARENGINE\_PLANE\_FINDING\_MODE\_VERTICAL | 只检测竖直平面，如墙壁。 |
| ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL\_AND\_VERTICAL | 同时检测水平面和竖直平面。 |

### AREngine\_ARPlaneType

PhoneTabletTV

```
1. enum AREngine_ARPlaneType
```

**描述**

平面类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_PLANE\_FACING\_HORIZONTAL\_UPWARD | 朝上的水平面（例如地面和桌面平台）。 |
| ARENGINE\_PLANE\_FACING\_HORIZONTAL\_DOWNWARD | 朝下的水平面（例如天花板）。 |
| ARENGINE\_PLANE\_FACING\_VERTICAL | 垂直的水平面（例如墙壁）。 |
| ARENGINE\_PLANE\_FACING\_INVALID | 无效或不支持的平面类型。这可能是由于环境变化、光线条件或其他因素导致。 |

### AREngine\_ARPointOrientationMode

PhoneTabletTV

```
1. enum AREngine_ARPointOrientationMode
```

**描述**

朝向模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY | 与世界坐标系的朝向一致，但会稍作调整。 |
| ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL | 朝向由估计的平面法向量决定。 |

### AREngine\_ARPoseMode

PhoneTabletTV

```
1. enum AREngine_ARPoseMode
```

**描述**

AR Engine输出的相机位姿对齐格式。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_POSE\_MODE\_GRAVITY | 输出的位姿信息（通过[HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](arengine-capi-arengine.md#hms_arengine_arcamera_getdisplayorientedpose)、[HMS\_AREngine\_ARCamera\_GetPose](arengine-capi-arengine.md#hms_arengine_arcamera_getpose)接口返回）为重力坐标系对齐的数据。参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |
| ARENGINE\_POSE\_MODE\_GRAVITY\_HEADING | 输出的位姿信息（通过[HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](arengine-capi-arengine.md#hms_arengine_arcamera_getdisplayorientedpose)、[HMS\_AREngine\_ARCamera\_GetPose](arengine-capi-arengine.md#hms_arengine_arcamera_getpose)接口返回）为北向ENU坐标系对齐的数据。参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。  **说明：** 该选项当前仅支持省电模式，请调用[HMS\_AREngine\_ARConfig\_SetPowerMode](arengine-capi-arengine.md#hms_arengine_arconfig_setpowermode)将功耗模式设置为ARENGINE\_POWER\_MODE\_ULTRA\_POWER\_SAVING以启动该选项。 |

### AREngine\_ARPoseType

PhoneTabletTV

```
1. enum AREngine_ARPoseType
```

**描述**

位姿类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_POSE\_TYPE\_IDENTITY | 默认状态，即没有任何旋转或平移。 |
| ARENGINE\_POSE\_TYPE\_ROTATE\_90 | 顺时针旋转90度。 |
| ARENGINE\_POSE\_TYPE\_ROTATE\_180 | 顺时针旋转180度。 |
| ARENGINE\_POSE\_TYPE\_ROTATE\_270 | 顺时针旋转270度。 |

### AREngine\_ARPowerMode

PhoneTabletTV

```
1. enum AREngine_ARPowerMode
```

**描述**

电源功耗模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_POWER\_MODE\_NORMAL | 正常模式，AR Engine在性能和电源消耗之间保持平衡。 |
| ARENGINE\_POWER\_MODE\_POWER\_SAVING | 节能模式，AR Engine优先减少电源消耗。这可能会降低一些性能，以换取更长的电池寿命。 |
| ARENGINE\_POWER\_MODE\_PERFORMANCE\_FIRST | 性能优先模式，AR Engine优先考虑性能，提供更高的处理能力和更快的响应时间。这可能会增加电源消耗。 |
| ARENGINE\_POWER\_MODE\_BOOST | 仅输出设备姿态信息模式。功耗低于 ARENGINE\_POWER\_MODE\_NORMAL模式下的功耗。在此模式下，与平面相关的设置（如：[HMS\_AREngine\_ARConfig\_SetPlaneFindingMode](arengine-capi-arengine.md#hms_arengine_arconfig_setplanefindingmode)）不生效。 |
| ARENGINE\_POWER\_MODE\_ULTRA\_POWER\_SAVING | 超级节能模式，AR Engine进一步优化电源消耗，提供比节能模式更低的电源消耗，这可能会损失更多的性能。 |

### AREngine\_ARPreviewMode

PhoneTabletTV

```
1. enum AREngine_ARPreviewMode
```

**描述**

预览模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_PREVIEW\_MODE\_ENABLED | 开启相机预览。 |
| ARENGINE\_PREVIEW\_MODE\_DISABLED | 关闭相机预览，如：VR模式，不需要相机预览流。 在此模式下，通过[HMS\_AREngine\_ARSession\_SetCameraGLTexture](arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture)接口设置的OpenGL纹理 将不会被更新。 |

### AREngine\_ARSemanticDenseMode

PhoneTabletTV

```
1. enum AREngine_ARSemanticDenseMode
```

**描述**

高精几何重建识别模式。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_SEMANTIC\_DENSE\_MODE\_DISABLED | 关闭高精几何重建识别模式。 |
| ARENGINE\_SEMANTIC\_DENSE\_MODE\_NORMAL | 正常模式，仅开启稠密点云识别。 |
| ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_VOLUME | 基于高精几何重建的立方体体积测量模式。 |
| ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_SPACE | 基于高精几何重建的立方体空间容积测量模式。 |

### AREngine\_ARSemanticMode

PhoneTabletTV

```
1. enum AREngine_ARSemanticMode
```

**描述**

语义模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_SEMANTIC\_MODE\_NONE | 不使用语义。 |
| ARENGINE\_SEMANTIC\_MODE\_PLANE | 使用平面语义。 |
| ARENGINE\_SEMANTIC\_MODE\_TARGET | 使用物体语义。 |

### AREngine\_ARSemanticPlaneLabel

PhoneTabletTV

```
1. enum AREngine_ARSemanticPlaneLabel
```

**描述**

当前平面识别到的语义类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_PLANE\_UNKNOWN | 未知类型。 |
| ARENGINE\_PLANE\_WALL | 墙面。 |
| ARENGINE\_PLANE\_FLOOR | 地面。 |
| ARENGINE\_PLANE\_SEAT | 座椅。 |
| ARENGINE\_PLANE\_TABLE | 桌子。 |
| ARENGINE\_PLANE\_CEILING | 天花板。 |
| ARENGINE\_PLANE\_DOOR | 门。 |
| ARENGINE\_PLANE\_WINDOW | 窗户。 |
| ARENGINE\_PLANE\_BED | 床。 |
| ARENGINE\_PLANE\_SPACE | 平面空间。  **起始版本：** 6.0.0(20) |
| ARENGINE\_CUBE\_VOLUME | 立方体体积。  **起始版本：** 6.0.0(20) |
| ARENGINE\_CUBE\_SPACE | 立方体空间。  **起始版本：** 6.0.0(20) |

### AREngine\_ARStatus

PhoneTabletTV

```
1. enum AREngine_ARStatus
```

**描述**

接口返回错误码。

用于表示一个接口的调用状态。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED | 权限未授予状态。如相机权限未授予。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED | 不可用：设备不兼容状态。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_SESSION\_PAUSED | 会话已暂停状态。 |
| ARENGINE\_ERROR\_SESSION\_NOT\_PAUSED | 会话未暂停状态。 |
| ARENGINE\_ERROR\_NOT\_TRACKING | 未跟踪状态。 |
| ARENGINE\_ERROR\_TEXTURE\_NOT\_SET | 未设置纹理状态。 |
| ARENGINE\_ERROR\_MISSING\_GL\_CONTEXT | 缺少GL上下文状态。 |
| ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION | 不支持的配置状态。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |
| ARENGINE\_ERROR\_NOT\_AVAILABLE | 服务不可用状态。 |
| ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE | 相机不可用状态。 |
| ARENGINE\_ERROR\_IMAGE\_EXCEED\_NUM\_LIMIT | 添加的图片数量超过最大数量。  **起始版本：** 5.1.0(18) |
| ARENGINE\_ERROR\_IMAGE\_INSUFFICIENT\_QUALITY | 将质量不足的图像添加到图像数据库中。  **起始版本：** 5.1.0(18) |
| ARENGINE\_ERROR\_IMAGE\_INVALID\_DATABASE | 没有有效的图像数据库。  **起始版本：** 5.1.0(18) |
| ARENGINE\_ERROR\_IMAGE\_ADD\_IMAGE\_TRACKING\_STATE | 跟踪状态正在运行时无法添加图片。  **起始版本：** 5.1.0(18) |
| ARENGINE\_ERROR\_NATIVEBUFFER\_CREATE\_FAILED | 创建NativeBuffer失败。  **起始版本：** 6.0.0(20) |
| ARENGINE\_ERROR\_NATIVEBUFFER\_WRITE\_FAILED | 无法写入NativeBuffer。  **起始版本：** 6.0.0(20) |
| ARENGINE\_CAMERA\_SERVICE\_FATAL\_ERROR | 相机服务异常。  **起始版本：** 6.0.2(22) |

### AREngine\_ARTargetShapeLabel

PhoneTabletTV

```
1. enum AREngine_ARTargetShapeLabel
```

**描述**

识别到的物体形状。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_TARGET\_SHAPE\_UNKNOWN | 未知形状。 |
| ARENGINE\_TARGET\_SHAPE\_CUBE | 立方体形状。可以识别规则物体的包围框。 |
| ARENGINE\_TARGET\_SHAPE\_CIRCLE | 圆形形状。 |
| ARENGINE\_TARGET\_SHAPE\_RECTANGLE | 矩形形状。 |

### AREngine\_ARTrackableType

PhoneTabletTV

```
1. enum AREngine_ARTrackableType
```

**描述**

可跟踪对象类型，如平面、点等。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_TRACKABLE\_BASE | 基础可跟踪对象类型，可作为默认的[AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype)类型。 |
| ARENGINE\_TRACKABLE\_PLANE | 平面类可跟踪对象类型。 |
| ARENGINE\_TRACKABLE\_POINT | 点类可跟踪对象类型。 |
| ARENGINE\_TRACKABLE\_AUGMENTED\_IMAGE | 增强图像类型的可跟踪对象。  **起始版本：** 5.1.0(18) |
| ARENGINE\_TRACKABLE\_BODY | 人体追踪对象。  **起始版本：** 6.1.0(23) |
| ARENGINE\_TRACKABLE\_FACE | 人脸追踪对象。  **起始版本：** 6.1.0(23) |
| ARENGINE\_TRACKABLE\_TARGET | 物体类可跟踪对象类型。 |
| ARENGINE\_TRACKABLE\_INVALID | 无效的可跟踪对象类型。 |

### AREngine\_ARTrackingState

PhoneTabletTV

```
1. enum AREngine_ARTrackingState
```

**描述**

可跟踪对象的跟踪状态。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_TRACKING\_STATE\_TRACKING | 正在追踪。 |
| ARENGINE\_TRACKING\_STATE\_PAUSED | 暂停追踪。 |
| ARENGINE\_TRACKING\_STATE\_STOPPED | 停止追踪。 |

### AREngine\_ARTrackingStateReason

PhoneTabletTV

```
1. enum AREngine_ARTrackingStateReason
```

**描述**

可能的跟踪失败原因。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_TRACKING\_STATE\_REASON\_NONE | 未知原因。这可能是由于系统暂时无法识别可追踪对象，但仍在尝试追踪。 |
| ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION | 目标移动过快。可追踪对象（如平面、点、图像等）移动速度过快，导致AR Engine无法准确识别和跟踪。 |
| ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES | 视觉特征不足（如弱纹理）。可追踪对象的视觉特征不够丰富，如纹理不明显、颜色过于单一等，导致AR Engine无法准确识别和跟踪。 |

### AREngine\_ARType

PhoneTabletTV

```
1. enum AREngine_ARType
```

**描述**

AR能力类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_TYPE\_WORLD | 环境识别与运动跟踪能力。 |
| ARENGINE\_TYPE\_BODY | 人体骨骼识别与跟踪能力。  **起始版本：** 6.1.0(23) |
| ARENGINE\_TYPE\_FACE | 人脸识别与跟踪能力。  **起始版本：** 6.1.0(23) |
| ARENGINE\_TYPE\_IMAGE | 图像识别与跟踪跟踪能力。  **起始版本：** 5.1.0(18) |

### AREngine\_ARUpdateMode

PhoneTabletTV

```
1. enum AREngine_ARUpdateMode
```

**描述**

调用[HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)方法后数据更新模式。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_UPDATE\_MODE\_BLOCKING | [HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)方法在新的帧可用时才返回。 |
| ARENGINE\_UPDATE\_MODE\_LATEST | [HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)方法立刻返回（如果没有新的帧，返回上一帧）。 |

### AREngine\_ARBodySkeletonType

PhoneTabletTV

```
1. enum AREngine_ARBodySkeletonType
```

**描述**

人体骨骼点类型。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE\_ARBODY\_SKELETON\_NECK | 颈部。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_SHO | 右肩。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_ELBOW | 右肘。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_WRIST | 右腕。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_SHO | 左肩。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_ELBOW | 左肘。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_WRIST | 左腕。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_HIP | 右髋部。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_KNEE | 右膝。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_ANKLE | 右脚踝。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_HIP | 左髋部。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_KNEE | 左膝。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_ANKLE | 左脚踝。 |
| ARENGINE\_ARBODY\_SKELETON\_HIP\_MID | 中髋部。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_EAR | 右耳。 |
| ARENGINE\_ARBODY\_SKELETON\_R\_EYE | 右眼。 |
| ARENGINE\_ARBODY\_SKELETON\_NOSE | 鼻子。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_EYE | 左眼。 |
| ARENGINE\_ARBODY\_SKELETON\_L\_EAR | 左耳。 |
| ARENGINE\_ARBODY\_SKELETON\_SPINE | 脊柱。 |

## 函数说明

PhoneTabletTV

### HMS\_AREngine\_CheckSupported

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_CheckSupported(AREngine_FeatureType type)
```

**描述**

判断AREngine中的某个特性是否在该设备上能够使用。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| type | AR特性类别[AREngine\_FeatureType](arengine-capi-arengine.md#arengine_featuretype)对象。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED | 当前设备不支持。 |

### HMS\_AREngine\_ARAnchor\_Detach

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAnchor_Detach(AREngine_ARSession *session, AREngine_ARAnchor *anchor)
```

**描述**

通知AR Engine停止跟踪并解绑一个锚点。

但是该函数并不会释放该锚点，这需要通过[HMS\_AREngine\_ARAnchor\_Release](arengine-capi-arengine.md#hms_arengine_aranchor_release)单独来实现。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| anchor | 待解绑的锚点对象，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARAnchor\_GetPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAnchor_GetPose(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARPose *outPose)
```

**描述**

获取指定锚点在世界坐标系中的位姿信息。

当每次调用[HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)的时候，[HMS\_AREngine\_ARAnchor\_GetPose](arengine-capi-arengine.md#hms_arengine_aranchor_getpose)返回的位姿信息可能会发生变化。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| anchor | 待检索位姿的锚点，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |
| outPose | 返回锚点对应的位姿对象，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARAnchor\_GetTrackingState

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAnchor_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARTrackingState *outTrackingState)
```

**描述**

获取指定锚点位姿的追踪状态。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| anchor | 待获取追踪状态的锚点，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |
| outTrackingState | 返回锚点当前位姿的追踪状态，参见[AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARAnchor\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARAnchor_Release(AREngine_ARAnchor *anchor)
```

**描述**

释放指定锚点对象的内存。

释放前需要先通知AR Engine停止跟踪并解绑锚点，参见[HMS\_AREngine\_ARAnchor\_Detach](arengine-capi-arengine.md#hms_arengine_aranchor_detach)。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| anchor | 待释放的锚点对象，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |

### HMS\_AREngine\_ARAnchorList\_AcquireItem

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAnchorList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t index, AREngine_ARAnchor **outAnchor)
```

**描述**

从锚点对象列表中获取指定位置的锚点信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| anchorList | 被检索的锚点对象列表，参见[AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist)。 |
| index | 需要获取的锚点在锚点对象列表中的位置，最小为0，最大为49。 |
| outAnchor | 待返回的锚点信息，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAnchorList\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAnchorList_Create(const AREngine_ARSession *session, AREngine_ARAnchorList **outAnchorList)
```

**描述**

创建一个锚点对象列表。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outAnchorList | 待创建的锚点对象列表引用，参见[AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARAnchorList\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARAnchorList_Destroy(AREngine_ARAnchorList *anchorList)
```

**描述**

释放一个锚点对象列表。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| anchorList | 待释放的锚点列表对象，参见[AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist)。 |

### HMS\_AREngine\_ARAnchorList\_GetSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAnchorList_GetSize(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t *outSize)
```

**描述**

获取锚点对象列表中包含锚点的数量。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| anchorList | 锚点对象列表，参见[AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist)。 |
| outSize | 返回锚点对象列表中锚点的数量。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImage\_AcquireName

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImage_AcquireName(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, char *augmentedImageName, uint32_t *outNameLength)
```

**描述**

返回跟踪图像的名称。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| augmentedImage | 图像类型的可追踪对象，参见[AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage)。 |
| augmentedImageName | 图像名称，不允许为空，255个字符以内，超过255个字符的部分将被自动截断。 |
| outNameLength | 返回图像名称长度。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImage\_GetCenterPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, AREngine_ARPose *outPose)
```

**描述**

获取跟踪图像中心点在世界坐标系中的位姿信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| augmentedImage | 图像类型的可追踪对象，参见[AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage)。 |
| outPose | 返回跟踪图像的位姿，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImage\_GetExtendX

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendX(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendX)
```

**描述**

以图像的中心点为坐标原点，获取X轴上的估计值。

返回物理图像的长度，单位为m。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| augmentedImage | 图像类型的可追踪对象，参见[AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage)。 |
| outExtendX | 返回X轴上物理图像的估计长度，以m为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImage\_GetExtendZ

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendZ(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendZ)
```

**描述**

以图像的中心点为坐标原点，获取Z轴上的估计值。

返回物理图像的宽度，单位为m。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| augmentedImage | 图像类型的可追踪对象，参见[AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage)。 |
| outExtendZ | 返回Z轴上物理图像的估计宽度，以m为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImage\_GetIndex

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetIndex(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, uint32_t *outIndex)
```

**描述**

获取跟踪图像数据库中跟踪图像的索引。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| augmentedImage | 图像类型的可追踪对象，参见[AREngine\_ARAugmentedImage](arengine-capi-arengine.md#arengine_araugmentedimage)。 |
| outIndex | 返回图像的索引。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_AddImage(AREngine_ARAugmentedImageDatabase *database, const AREngine_ARAugmentedImageSource *image, uint32_t *outIndex, AREngine_ARAddAugmentedImageReason *outReason)
```

**描述**

将图像添加到图像数据库并输出对应图像的索引。开发者可以通过[HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_getcapacity)获取可添加图像的最大数量，通过[HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_setaddmode)接口来设置调用此接口后的行为。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |
| image | 图像信息，参见[AREngine\_ARAugmentedImageSource](arengine-struct-araugmentedimagesource.md)。 |
| outIndex | 返回添加图像的索引。 |
| outReason | 返回添加图片失败的原因，参见[AREngine\_ARAddAugmentedImageReason](arengine-capi-arengine.md#arengine_araddaugmentedimagereason)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |
| ARENGINE\_ERROR\_IMAGE\_EXCEED\_NUM\_LIMIT | 添加的图片数量超过最大数量。  **起始版本：** 5.1.0(18) |
| ARENGINE\_ERROR\_IMAGE\_INSUFFICIENT\_QUALITY | 将质量不足的图像添加到图像数据库中。  **起始版本：** 5.1.0(18) |

### HMS\_AREngine\_ARAugmentedImageDatabase\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Create(AREngine_ARAugmentedImageDatabase **outDatabase)
```

**描述**

创建一个空的跟踪图像数据库。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| outDatabase | 返回指向要创建的图像库的指针，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Deserialize(const uint8_t *buffer, const uint64_t bufSize, AREngine_ARAugmentedImageDatabase **outDatabase)
```

**描述**

反序列化特征数据库。

用户可以将上次生成的或者保存的buffer数据反序列化为特征数据库后直接使用。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| buffer | 跟踪图像数据库缓冲区。 |
| bufSize | 跟踪图像数据库缓冲区大小。 |
| outDatabase | 返回跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_Destroy

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Destroy(AREngine_ARAugmentedImageDatabase *database)
```

**描述**

释放图像数据库对象。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_GetAddMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode *outAddMode)
```

**描述**

获取添加跟踪图像模式。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |
| outAddMode | 返回添加跟踪图像模式。参见[AREngine\_ARImageDatabaseMode](arengine-capi-arengine.md#arengine_arimagedatabasemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_SetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode addMode)
```

**描述**

设置添加跟踪图像模式。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |
| addMode | 添加跟踪图像模式。参见[AREngine\_ARImageDatabaseMode](arengine-capi-arengine.md#arengine_arimagedatabasemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetCapacity(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outCapacity)
```

**描述**

获取通过调用[HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_addimage)接口所能添加的图像最大数量。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |
| outCapacity | 返回最大图像数，默认为50。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetImageCount(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outImageCount)
```

**描述**

获取数据库中存储的图像数量。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |
| outImageCount | 返回图像数量。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Serialize(const AREngine_ARAugmentedImageDatabase *database, uint8_t **outBuffer, uint64_t *outBufSize)
```

**描述**

序列化特征数据库。

在添加完图片后，可以将特征库序列化为buffer，开发者可以保存此buffer以供下次使用。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见[AREngine\_ARAugmentedImageDatabase](arengine-capi-arengine.md#arengine_araugmentedimagedatabase)。 |
| outBuffer | 返回跟踪图像数据库缓冲区。 |
| outBufSize | 返回跟踪图像数据库缓冲区大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetDisplayOrientedPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose)
```

**描述**

设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。

该位姿是OpenGL相机的位姿，其中X轴正方向为右，Y轴正方向为上，Z轴负方向为相机的观察方向。相机位置即物理相机位置，而相机X轴与Y轴指向受屏幕方向（考虑显示旋转）的影响。

该位姿信息应该在[HMS\_AREngine\_ARCamera\_GetTrackingState](arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstate)返回[ARENGINE\_TRACKING\_STATE\_TRACKING](arengine-capi-arengine.md#arengine_artrackingstate)状态的时候才能使用。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| outPose | 返回虚拟相机在世界空间中的位姿，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCamera\_GetImageIntrinsics

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetImageIntrinsics(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARCameraIntrinsics *outIntrinsics)
```

**描述**

获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| outIntrinsics | 返回相机物理内参对象，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARCamera\_GetPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose)
```

**描述**

设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。

其中X轴正方向为右，Y轴正方向为上，Z轴负方向为相机的观察方向。相机位置即物理相机位置，而相机X轴与Y轴指向不受屏幕方向（考虑显示旋转）的影响。

该位姿信息应该在[HMS\_AREngine\_ARCamera\_GetTrackingState](arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstate)返回[ARENGINE\_TRACKING\_STATE\_TRACKING](arengine-capi-arengine.md#arengine_artrackingstate)状态的时候才能使用。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| outPose | 物理相机在世界空间中的位姿，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCamera\_GetProjectionMatrix

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetProjectionMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ClipPlaneDistance clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num)
```

**描述**

获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| clipPlaneDistance | OpenGL裁剪平面距离，参见[AREngine\_ClipPlaneDistance](arengine-struct-clipplanedistance.md)。 |
| outDestColMajor4x4 | 返回一个由16个浮点数组成的数组，其中的数据表示OpenGL中以列为主的均匀变换矩阵。 |
| destColMajor4x4Num | 数组大小：[ARENGINE\_VIEW\_MATRIX\_SIZE](arengine-capi-arengine.md#arengine_view_matrix_size)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARCamera\_GetTrackingState

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingState *outTrackingState)
```

**描述**

获取相机的当前追踪状态。

只有当该状态为[ARENGINE\_TRACKING\_STATE\_TRACKING](arengine-capi-arengine.md#arengine_artrackingstate)时，相机的位姿才可用。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| outTrackingState | 返回当前相机的追踪状态，参见[AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCamera\_GetTrackingStateReason

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingStateReason(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingStateReason *outTrackingStateReason)
```

**描述**

获取相机的当前追踪状态为[ARENGINE\_TRACKING\_STATE\_PAUSED](arengine-capi-arengine.md#arengine_artrackingstate)时的原因。

当相机的当前追踪状态为[ARENGINE\_TRACKING\_STATE\_TRACKING](arengine-capi-arengine.md#arengine_artrackingstate)时，该函数返回[ARENGINE\_TRACKING\_STATE\_REASON\_NONE](arengine-capi-arengine.md#arengine_artrackingstatereason)。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| outTrackingStateReason | 返回跟踪失败的原因，参见[AREngine\_ARTrackingStateReason](arengine-capi-arengine.md#arengine_artrackingstatereason)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCamera\_GetViewMatrix

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCamera_GetViewMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, float *outColMajor4x4, int32_t colMajor4x4Num)
```

**描述**

获取最新帧中相机的视图矩阵。

此矩阵执行了[HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](arengine-capi-arengine.md#hms_arengine_arcamera_getdisplayorientedpose)提供的Pose的逆变换，即从世界坐标系转为相机坐标系。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| camera | Session对应的相机，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |
| outColMajor4x4 | 返回一个由16个浮点数组成的数组，其中的数据表示OpenGL中以列为主的均匀变换矩阵。 |
| colMajor4x4Num | 数组大小。数组大小定义大于等于[ARENGINE\_VIEW\_MATRIX\_SIZE](arengine-capi-arengine.md#arengine_view_matrix_size)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCamera\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARCamera_Release(AREngine_ARCamera *camera)
```

**描述**

释放对相机的引用。

当调用了[HMS\_AREngine\_ARFrame\_AcquireCamera](arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera)时，需要相应的调用[HMS\_AREngine\_ARCamera\_Release](arengine-capi-arengine.md#hms_arengine_arcamera_release)。

当没有[HMS\_AREngine\_ARFrame\_AcquireCamera](arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera)时，调用该方法无效。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| camera | 待释放的相机引用，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |

### HMS\_AREngine\_ARCameraConfig\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraConfig_Create(const AREngine_ARSession *session, AREngine_ARCameraConfig **outCameraConfig)
```

**描述**

创建一个相机配置对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outCameraConfig | 返回一个指向新分配的相机配置对象地址的指针，参见[AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARConfig\_GetCameraLensFacing

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraLensFacing(const AREngine_ARSession *session,const AREngine_ARConfig *config, AREngine_ARCameraLensFacing *outFacing)
```

**描述**

获取相机镜头朝向。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向包含目标配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outFacing | 相机镜头朝向，参见[AREngine\_ARCameraLensFacing](arengine-capi-arengine.md#arengine_arcameralensfacing)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetMultiFaceMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode *outFaceMode)
```

**描述**

获取多人脸检测模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向包含目标配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outFaceMode | 多人脸检测模式，参见[AREngine\_ARMultiFaceMode](arengine-capi-arengine.md#arengine_armultifacemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetCameraLensFacing

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraLensFacing(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARCameraLensFacing facing)
```

**描述**

设置相机镜头朝向。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向包含目标配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| facing | 设置相机镜头朝向，参见[AREngine\_ARCameraLensFacing](arengine-capi-arengine.md#arengine_arcameralensfacing)。facing设置为ARENGINE\_CAMERA\_FACING\_FRONT时，需要调用[HMS\_AREngine\_ARConfig\_SetARType](arengine-capi-arengine.md#hms_arengine_arconfig_setartype)将AR能力类型设置为ARENGINE\_TYPE\_FACE或ARENGINE\_TYPE\_BODY才生效。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetMultiFaceMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode faceMode)
```

**描述**

设置多人脸检测模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向包含目标配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| faceMode | 多人脸检测模式，参见[AREngine\_ARMultiFaceMode](arengine-capi-arengine.md#arengine_armultifacemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCameraConfig\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARCameraConfig_Destroy(AREngine_ARCameraConfig *cameraConfig)
```

**描述**

释放相机配置对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| cameraConfig | 待释放的指向相机配置对象的指针，参见[AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig)。 |

### HMS\_AREngine\_ARCameraConfig\_GetImageDimensions

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight)
```

**描述**

从相机配置对象中获取相机送到CPU处理的图像尺寸。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| cameraConfig | 指向相机配置对象的指针，参见[AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig)。 |
| outWidth | 返回图像的宽度，以Pixel为单位。 |
| outHeight | 返回图像的高度，以Pixel为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCameraConfig\_GetTextureDimensions

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetTextureDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight)
```

**描述**

从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| cameraConfig | 指向相机配置对象的指针，参见[AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig)。 |
| outWidth | 返回图像纹理的宽度，以Pixel为单位。 |
| outHeight | 返回图像纹理的高度，以Pixel为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCameraIntrinsics\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_Create(const AREngine_ARSession *session, AREngine_ARCameraIntrinsics **outIntrinsics)
```

**描述**

创建一个相机内参对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outIntrinsics | 返回一个指向新分配的相机内参对象地址的指针，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARCameraIntrinsics\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARCameraIntrinsics_Destroy(AREngine_ARCameraIntrinsics *intrinsics)
```

**描述**

释放指定的相机内参对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| intrinsics | 待释放的相机内参对象，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |

### HMS\_AREngine\_ARCameraIntrinsics\_GetDistortion

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetDistortion(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outDistortion, int32_t distortionNum)
```

**描述**

获取相机的畸变系数。

包含5个分量，其中outDistortion[0]~outDistortion [2]表示k1，k2，k3（径向畸变系数），outDistortion [3]~outDistortion [4]是切向畸变系数。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| intrinsics | 指向相机内参对象的指针，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |
| outDistortion | 返回相机畸变参数数组。 |
| distortionNum | 相机畸变参数的个数，参见[ARENGINE\_DISTORTION\_COUNT](arengine-capi-arengine.md#arengine_distortion_count)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCameraIntrinsics\_GetFocalLength

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetFocalLength(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outFocalX, float *outFocalY)
```

**描述**

获取指定相机的焦距，焦距以Pixel为单位。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| intrinsics | 指向相机内参对象的指针，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |
| outFocalX | 返回相机内参矩阵x(u)方向的像素焦距。 |
| outFocalY | 返回相机内参矩阵y(v)方向的像素焦距。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCameraIntrinsics\_GetImageDimensions

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, int32_t *outWidth, int32_t *outHeight)
```

**描述**

获取相机图像的尺寸，包括宽度和高度，以Pixel为单位。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| intrinsics | 指向相机内参对象的指针，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |
| outWidth | 返回相机图像的宽度，以Pixel为单位。 |
| outHeight | 返回相机图像的高度，以Pixel为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARCameraIntrinsics\_GetPrincipalPoint

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outPrincipalX, float *outPrincipalY)
```

**描述**

获取指定相机的主轴点，主点位置以Pixel为单位表示。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| intrinsics | 指向相机内参对象的指针，参见[AREngine\_ARCameraIntrinsics](arengine-capi-arengine.md#arengine_arcameraintrinsics)。 |
| outPrincipalX | 返回相机X方向的主轴点坐标。 |
| outPrincipalY | 返回相机Y方向的主轴点坐标。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_Create(const AREngine_ARSession *session, AREngine_ARConfig **outConfig)
```

**描述**

创建具有适当默认配置的配置对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outConfig | 返回一个指向新分配的配置对象地址的指针，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARConfig\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARConfig_Destroy(AREngine_ARConfig *config)
```

**描述**

释放指定的配置对象的内存空间。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待释放的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |

### HMS\_AREngine\_ARConfig\_GetARType

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetARType(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARType *type)
```

**描述**

获取当前使用的AR能力类型。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| type | 返回AR Engine当前使用的能力类型，参见[AREngine\_ARType](arengine-capi-arengine.md#arengine_artype)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetCameraPreviewMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode *outMode)
```

**描述**

获取当前的预览模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outMode | 返回相机预览模式，参见[AREngine\_ARPreviewMode](arengine-capi-arengine.md#arengine_arpreviewmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetDepthMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetDepthMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARDepthMode *outDepthMode)
```

**描述**

获取当前的深度模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.5(17)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outDepthMode | 返回当前深度模式，参见[AREngine\_ARDepthMode](arengine-capi-arengine.md#arengine_ardepthmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetFocusMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetFocusMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARFocusMode *focusMode)
```

**描述**

获取当前配置的相机对焦模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| focusMode | 返回当前对焦模式，参见[AREngine\_ARFocusMode](arengine-capi-arengine.md#arengine_arfocusmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetMaxMapSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetMaxMapSize(const AREngine_ARSession *session, const AREngine_ARConfig *config, uint64_t *maxMapSize)
```

**描述**

获取地图数据使用的最大内存大小。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

在执行[HMS\_AREngine\_ARSession\_Configure](arengine-capi-arengine.md#hms_arengine_arsession_configure)后，可通过此接口获取当前设置的地图数据最大使用内存大小。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| maxMapSize | 返回目前生效的地图数据最大使用内存大小，单位MB。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetMeshMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetMeshMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMeshMode *outMeshMode)
```

**描述**

获取当前mesh模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outMeshMode | 返回mesh模式，参见[AREngine\_ARMeshMode](arengine-capi-arengine.md#arengine_armeshmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetPlaneFindingMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetPlaneFindingMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPlaneFindingMode *planeFindingMode)
```

**描述**

获取当前配置的平面识别模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| planeFindingMode | 返回当前平面识别模式，参见[AREngine\_ARPlaneFindingMode](arengine-capi-arengine.md#arengine_arplanefindingmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetPoseMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetPoseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPoseMode *poseMode)
```

**描述**

获取相机输出的位姿坐标系对齐模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| poseMode | 相机位姿模式，参见[AREngine\_ARPoseMode](arengine-capi-arengine.md#arengine_arposemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetPowerMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetPowerMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPowerMode *powerMode)
```

**描述**

获取当前配置的功耗模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| powerMode | 返回当前功耗模式，参见[AREngine\_ARPowerMode](arengine-capi-arengine.md#arengine_arpowermode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetSemanticDenseMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticDenseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticDenseMode *outSemanticDenseMode)
```

**描述**

获取已设置的高精几何重建模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outSemanticDenseMode | 返回当前高精几何重建模式，参见[AREngine\_ARSemanticDenseMode](arengine-capi-arengine.md#arengine_arsemanticdensemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetSemanticMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticMode *mode)
```

**描述**

获取已设置成功的语义识别模式。

该方法在[HMS\_AREngine\_ARConfig\_SetSemanticMode](arengine-capi-arengine.md#hms_arengine_arconfig_setsemanticmode)后调用有效。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| mode | 返回当前语义模式，参见[AREngine\_ARSemanticMode](arengine-capi-arengine.md#arengine_arsemanticmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetUpdateMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetUpdateMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARUpdateMode *updateMode)
```

**描述**

获取当前配置的预览更新模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| updateMode | 返回当前预览更新模式，参见[AREngine\_ARUpdateMode](arengine-capi-arengine.md#arengine_arupdatemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetARType

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetARType(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARType type)
```

**描述**

设置当前要使用的AR能力类型。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| type | AR Engine支持的能力类型，参见[AREngine\_ARType](arengine-capi-arengine.md#arengine_artype)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION | 不支持的配置状态。 |

### HMS\_AREngine\_ARConfig\_SetCameraPreviewMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode mode)
```

**描述**

设置预览模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| mode | 相机预览模式，参见[AREngine\_ARPreviewMode](arengine-capi-arengine.md#arengine_arpreviewmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetDepthMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetDepthMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARDepthMode depthMode)
```

**描述**

设置深度模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.5(17)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| depthMode | 深度图像模式，参见[AREngine\_ARDepthMode](arengine-capi-arengine.md#arengine_ardepthmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetFocusMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetFocusMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARFocusMode focusMode)
```

**描述**

设置当前所需的相机对焦模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| focusMode | 对焦模式，参见[AREngine\_ARFocusMode](arengine-capi-arengine.md#arengine_arfocusmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetMaxMapSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetMaxMapSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint64_t maxMapSize)
```

**描述**

设置地图数据最大使用内存大小。

若配置的地图数据最大使用内存范围不合法，则配置最接近用户配置的有效值，默认最大使用内存大小800MB。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| maxMapSize | 地图数据最大使用内存大小，单位MB，范围：100MB~16G。 若设备内存占用超过设备硬件限制，可能出现不可预知错误，需要应用侧自行评估设置的内存大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetMeshMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetMeshMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode meshMode)
```

**描述**

设置mesh模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| meshMode | mesh模式，参见[AREngine\_ARMeshMode](arengine-capi-arengine.md#arengine_armeshmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetPlaneFindingMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetPlaneFindingMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPlaneFindingMode planeFindingMode)
```

**描述**

设置当前所需的平面识别模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| planeFindingMode | 平面识别模式，参见[AREngine\_ARPlaneFindingMode](arengine-capi-arengine.md#arengine_arplanefindingmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetPoseMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetPoseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPoseMode poseMode)
```

**描述**

设置相机输出的位姿坐标系对齐模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| poseMode | 相机位姿模式，参见[AREngine\_ARPoseMode](arengine-capi-arengine.md#arengine_arposemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetPowerMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetPowerMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPowerMode powerMode)
```

**描述**

设置功耗模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| powerMode | 功耗模式，参见[AREngine\_ARPowerMode](arengine-capi-arengine.md#arengine_arpowermode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetPreviewSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetPreviewSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height)
```

**描述**

设置预览画面尺寸。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| width | 预览画面的宽，以Pixel为单位。可调用[OH\_CameraManager\_GetSupportedCameraOutputCapability](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)查看。 |
| height | 预览画面的高，以Pixel为单位。可调用[OH\_CameraManager\_GetSupportedCameraOutputCapability](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)查看。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetSemanticDenseMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticDenseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticDenseMode semanticDenseMode)
```

**描述**

设置当前所需的高精几何重建模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| semanticDenseMode | 高精几何重建模式，参见[AREngine\_ARSemanticDenseMode](arengine-capi-arengine.md#arengine_arsemanticdensemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetSemanticMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticMode mode)
```

**描述**

设置当前所需的语义识别模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| mode | 语义模式，参见[AREngine\_ARSemanticMode](arengine-capi-arengine.md#arengine_arsemanticmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetUpdateMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetUpdateMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARUpdateMode updateMode)
```

**描述**

设置预览更新模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| updateMode | 预览更新模式，参见[AREngine\_ARUpdateMode](arengine-capi-arengine.md#arengine_arupdatemode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetPhotoStreamSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetPhotoStreamSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height)
```

**描述**

当[AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode)为ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO时，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| width | 拍照流图像分辨率的宽，以Pixel为单位。可调用[OH\_CameraManager\_GetSupportedCameraOutputCapability](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)查询设备支持的数值。 |
| height | 拍照流图像分辨率的宽，以Pixel为单位。可调用[OH\_CameraManager\_GetSupportedCameraOutputCapability](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)查询设备支持的数值。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetImageStreamMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetImageStreamMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode mode)
```

**描述**

设置图像流模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| mode | 图像流模式，参见[AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_GetImageStreamMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_GetImageStreamMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARImageStreamMode *outMode)
```

**描述**

获取图像流模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| outMode | 图像流模式，参见[AREngine\_ARImageStreamMode](arengine-capi-arengine.md#arengine_arimagestreammode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFace\_AcquireBlendShapes

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFace_AcquireBlendShapes(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceBlendShapes **outBlendshapes)
```

**描述**

获取人脸微表情对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| face | 当前人脸对象，参见[AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface)。 |
| outBlendshapes | 当前人脸的微表情对象，参见[AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFace\_AcquireGeometry

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFace_AcquireGeometry(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceGeometry **outGeometry)
```

**描述**

获取人脸拓扑结构对象，即人脸Mesh对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| face | 当前人脸对象，参见[AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface)。 |
| outGeometry | 当前人脸的拓扑结构对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFace\_AcquireLandmark

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFace_AcquireLandmark(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceLandmark **outLandmark)
```

**描述**

获取人脸关键点对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| face | 当前人脸对象，参见[AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface)。 |
| outLandmark | 当前人脸的关键点对象，参见[AREngine\_ARFaceLandmark](arengine-capi-arengine.md#arengine_arfacelandmark)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFace\_AcquireViewMatrix

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFace_AcquireViewMatrix(const AREngine_ARSession *session, const AREngine_ARFace *face, float *outColMajor4x4, int32_t colMajor4x4Num)
```

**描述**

获取当前人脸的面视图矩阵。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| face | 当前人脸对象，参见[AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface)。 |
| outColMajor4x4 | 当前人脸的视角视图矩阵数据。由16个浮点数组成的数组，表示OpenGL中的列主序统一变换矩阵。 |
| colMajor4x4Num | outColMajor4x4 的大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFace\_GetCenterPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFace_GetCenterPose(const AREngine_ARSession *session,const AREngine_ARFace *face, AREngine_ARPose *outPose)
```

**描述**

获取人脸Mesh中心的位姿。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| face | 当前人脸对象，参见[AREngine\_ARFace](arengine-capi-arengine.md#arengine_arface)。 |
| outPose | 人脸的中心位姿信息，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceBlendShapes\_AcquireData

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_AcquireData(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, const float **outData)
```

**描述**

获取微表情数据的集合。

**起始版本：** 6.1.0(23)

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| blendshapes | 当前人脸的微表情对象，参见[AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes)。 |
| outData | 人脸微表情参数的集合。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceBlendShapes\_AcquireTypes

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_AcquireTypes(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, const AREngine_ARAnimojiBlendShape **types)
```

**描述**

获取所有微表情参数类型数组。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| blendshapes | 当前人脸的微表情对象，参见[AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes)。 |
| types | 人脸微表情类型集合，参见[AREngine\_ARAnimojiBlendShape](arengine-capi-arengine.md#arengine_aranimojiblendshape)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceBlendShapes\_GetCount

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_GetCount(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, int32_t *outSize)
```

**描述**

获取微表情参数个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| blendshapes | 当前人脸的微表情对象，参见[AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes)。 |
| outSize | 人脸微表情参数个数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceBlendShapes\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARFaceBlendShapes_Release(AREngine_ARFaceBlendShapes *blendshapes)
```

**描述**

释放blendShapes对象，即由[HMS\_AREngine\_ARFace\_AcquireBlendShapes](arengine-capi-arengine.md#hms_arengine_arface_acquireblendshapes)创建的对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| blendshapes | 当前人脸微表情对象，参见[AREngine\_ARFaceBlendShapes](arengine-capi-arengine.md#arengine_arfaceblendshapes)。 |

### HMS\_AREngine\_ARFaceGeometry\_AcquireIndices

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireIndices(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t **data)
```

**描述**

获取人脸Mesh三角面下标数组。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| data | 三角形索引集合。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_AcquireTexCoord

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireTexCoord(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const float **outData)
```

**描述**

获取人脸Mesh纹理坐标点数组。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outData | 人脸Mesh纹理坐标集。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_AcquireTriangleLabels

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const AREngine_ARAnimojiTriangleLabel **data)
```

**描述**

获取人脸Mesh三角面标签。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| data | 三角形面标签的集合，参见[AREngine\_ARAnimojiTriangleLabel](arengine-capi-arengine.md#arengine_aranimojitrianglelabel)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_AcquireVertices

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireVertices(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const float **outData)
```

**描述**

获取人脸Mesh顶点数组。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outData | 顶点集合，格式为 [x0, y0, z0, x1, y1, z1,...]。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_GetIndicesSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetIndicesSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

**描述**

获取人脸Mesh三角面下标数组大小。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outSize | 三角形索引数组的大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_GetTexCoordSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTexCoordSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

**描述**

获取人脸Mesh纹理坐标点数组大小。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outSize | 纹理坐标数组的大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_GetTriangleCount

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTriangleCount(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

**描述**

获取人脸Mesh三角面个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outSize | 三角形面数量。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_GetTriangleLabelsSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

**描述**

获取人脸Mesh三角面标签个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outSize | 三角面标签的个数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_GetVerticesSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetVerticesSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

**描述**

获取人脸Mesh顶点数组大小。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |
| outSize | 人脸Mesh顶点数量。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceGeometry\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARFaceGeometry_Release(AREngine_ARFaceGeometry *geometry)
```

**描述**

释放当前人脸几何体对象，即由 [HMS\_AREngine\_ARFace\_AcquireGeometry](arengine-capi-arengine.md#hms_arengine_arface_acquiregeometry)创建的对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| geometry | 当前人脸Mesh对象，参见[AREngine\_ARFaceGeometry](arengine-capi-arengine.md#arengine_arfacegeometry)。 |

### HMS\_AREngine\_ARFaceLandmark\_AcquireVertices2D

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceLandmark_AcquireVertices2D(const AREngine_ARSession *session, const AREngine_ARFaceLandmark *landmark, const float **outData)
```

**描述**

获取人脸关键点的2D位姿信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| landmark | 当前人脸的关键点对象，参见[AREngine\_ARFaceLandmark](arengine-capi-arengine.md#arengine_arfacelandmark)。 |
| outData | 人脸关键点2D位姿信息。 |

### HMS\_AREngine\_ARFaceLandmark\_AcquireVertices3D

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceLandmark_AcquireVertices3D(const AREngine_ARSession *session, const AREngine_ARFaceLandmark *landmark, const float **outData)
```

**描述**

获取人脸关键点的3D位姿信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| landmark | 当前人脸的关键点对象，参见[AREngine\_ARFaceLandmark](arengine-capi-arengine.md#arengine_arfacelandmark)。 |
| outData | 人脸关键点3D位姿信息。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceLandmark\_GetCount

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFaceLandmark_GetCount(const AREngine_ARSession *session, const AREngine_ARFaceLandmark *landmark, int32_t *outSize)
```

**描述**

获取人脸关键点个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| landmark | 当前人脸的关键点对象，参见[AREngine\_ARFaceLandmark](arengine-capi-arengine.md#arengine_arfacelandmark)。 |
| outSize | 人脸关键点个数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFaceLandmark\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARFaceLandmark_Release(AREngine_ARFaceLandmark *landmark)
```

**描述**

释放landmark对象，即由[HMS\_AREngine\_ARFace\_AcquireLandmark](arengine-capi-arengine.md#hms_arengine_arface_acquirelandmark)创建的对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| landmark | 当前人脸的关键点对象，参见[AREngine\_ARFaceLandmark](arengine-capi-arengine.md#arengine_arfacelandmark)。 |

### HMS\_AREngine\_ARFrame\_AcquireCamera

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCamera(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARCamera **outCamera)
```

**描述**

获取当前帧的相机参数对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outCamera | 返回当前帧对应的相机参数对象，参见[AREngine\_ARCamera](arengine-capi-arengine.md#arengine_arcamera)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFrame\_AcquireCameraImage

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outImage)
```

**描述**

获取相机的当前帧的图像。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outImage | 返回当前帧的图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION | 不支持的配置状态。 |

### HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraPhotoImage(const AREngine_ARSession *session, const AAREngine_ARFrame*frame, HMS_AREngine_PhotoAvailableCallback photoCallback)
```

**描述**

获取当前帧的拍照流图片。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| photoCallback | 输出拍照流图片的回调，参见[HMS\_AREngine\_PhotoAvailableCallback](arengine-capi-arengine.md#hms_arengine_photoavailablecallback)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION | 不支持的配置状态。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE | 相机不可用状态。 |
| ARENGINE\_CAMERA\_SERVICE\_FATAL\_ERROR | 相机服务异常。 |

### HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outConfidenceImage)
```

**描述**

获取当前帧的深度置信度图像。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.5(17)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outConfidenceImage | 返回当前帧深度置信度图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthImage16Bits(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outDepthImage)
```

**描述**

获取当前帧的深度图像。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.5(17)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outDepthImage | 返回当前帧深度图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFrame\_AcquirePointCloud

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquirePointCloud(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARPointCloud **outPointCloud)
```

**描述**

返回当前帧的点云数据。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outPointCloud | 返回当前帧的点云对象，参见[AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFrame\_AcquireSceneMesh

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSceneMesh(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSceneMesh **outSceneMesh)
```

**描述**

获取当前帧的mesh信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outSceneMesh | 返回当前帧的mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSemanticDenseData(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSemanticDenseData **outSemanticDenseData)
```

**描述**

获取当前帧的高精几何重建对象数据。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outSemanticDenseData | 返回当前帧的高精几何重建对象数据，参见[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFrame\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_Create(const AREngine_ARSession *session, AREngine_ARFrame **outFrame)
```

**描述**

创建一个新的[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到\*outFrame中。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outFrame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARFrame\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARFrame_Destroy(AREngine_ARFrame *frame)
```

**描述**

删除当前[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| frame | 待销毁的当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |

### HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_GetDisplayGeometryChanged(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t *outGeometryChangeState)
```

**描述**

获取显示（长宽和旋转）是否发生变化。

如果发生变化，需要重新调用[HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords](arengine-capi-arengine.md#hms_arengine_arframe_transformdisplayuvcoords)获取正确的纹理贴图坐标。 返回值outGeometryChangeState为0，代表未发生变化，否则为发生了变化。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outGeometryChangeState | 返回显示（长宽和旋转）是否发生变化。0代表未发生变化，否则为发生了变化。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFrame\_GetTimestamp

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int64_t *outTimestampNs)
```

**描述**

获取当前帧对应的时间戳信息，单位为ns。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| outTimestampNs | 返回时间戳信息。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFrame\_GetUpdatedTrackables

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_GetUpdatedTrackables(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARTrackableType filterType, AREngine_ARTrackableList * outTrackableList)
```

**描述**

获取[HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)更新后发生变化的指定类型的可跟踪对象。

可跟踪对象类型参见[AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype)。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| filterType | 待返回的可跟踪对象类型，参见[AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype)。 |
| outTrackableList | 返回可跟踪对象列表，参见[AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARFrame\_HitTest

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_HitTest(const AREngine_ARSession *session, const AREngine_ARFrame *frame, float pixelX, float pixelY, AREngine_ARHitResultList *hitResultList)
```

**描述**

从摄像头发射一条射线，该射线的方向由预览区上的点（pixelX，pixelY）确定，（pixelX，pixelY）可以通过XComponent的[DispatchTouchEvent](ent-native-xcomponent-oh-nativexcomponent-callback.md#dispatchtouchevent)事件获取。

射线与系统跟踪的平面或者是点云中的点碰撞（点云正常识别），从而产生交点，形成碰撞结果。按照交点与设备的距离从近到远进行排序，存放在列表中。(pixelX，pixelY)是像素在预览区上坐标。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| pixelX | x轴坐标，通过[XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)获取。 |
| pixelY | y轴坐标，通过[XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)获取。 |
| hitResultList | 碰撞结果列表，参见[AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARFrame_TransformDisplayUvCoords(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t elementSize, const float *uvsIn, float *uvsOut)
```

**描述**

调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。

若[HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged](arengine-capi-arengine.md#hms_arengine_arframe_getdisplaygeometrychanged)返回的outGeometryChangeState不为0，或者使用[HMS\_AREngine\_ARSession\_SetDisplayGeometry](arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry)设置了新的显示大小则需要调用该方法更新纹理映射坐标，否则不需要更新。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| frame | 当前帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |
| elementSize | 待转换的纹理坐标数量，必须是2的倍数（uv坐标），最小为0。 |
| uvsIn | 原始输入uv坐标值。数组大小为 elementSize，不能为nullptr。 |
| uvsOut | 调整后的uv坐标值。数组大小为 elementSize，不能为nullptr。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARHitResult\_AcquireNewAnchor

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARHitResult *hitResult, AREngine_ARAnchor **outAnchor)
```

**描述**

在碰撞命中位置创建一个新的锚点。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| hitResult | 命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |
| outAnchor | 返回新创建的锚点对象，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARHitResult\_AcquireTrackable

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireTrackable(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARTrackable **outTrackable)
```

**描述**

获取被命中的可追踪对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| hitResult | 命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |
| outTrackable | 返回被命中的可追踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARHitResult\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResult_Create(const AREngine_ARSession *session, AREngine_ARHitResult **outHitResult)
```

**描述**

创建一个空的命中检测结果对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outHitResult | 待创建的命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARHitResult\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARHitResult_Destroy(AREngine_ARHitResult *hitResult)
```

**描述**

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| hitResult | 待释放的命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |

### HMS\_AREngine\_ARHitResult\_GetDistance

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResult_GetDistance(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, float *outDistance)
```

**描述**

返回从相机到命中位置的距离，以m为单位。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| hitResult | 命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |
| outDistance | 返回相机到命中对象的距离。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARHitResult\_GetHitPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResult_GetHitPose(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARPose *outPose)
```

**描述**

获取交点的位姿。

其平移向量是交点在世界坐标系的坐标，其旋转分量根据碰撞点的不同类型（平面交点、点云交点）而有不同的定义。

1. 当射线与平面碰撞时，局部坐标系为：X+垂直于射线，平行于跟踪平面；Y+是跟踪平面的法向量；Z+平行于平面，大致指向摄像头。
2. 当射线与点云中的点碰撞时，系统会尝试用点击区域的点云估计一个平面。

   1. 如果[HMS\_AREngine\_ARPoint\_GetOrientationMode](arengine-capi-arengine.md#hms_arengine_arpoint_getorientationmode)接口返回[ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL](arengine-capi-arengine.md#arengine_arpointorientationmode)，则X+垂直于射线，平行于跟踪平面，Y+是跟踪平面的法向量，Z+平行于平面，大致指向摄像头。
   2. 如果返回 [ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY](arengine-capi-arengine.md#arengine_arpointorientationmode)，则坐标的方向不会随平面的角度发生变化，X+垂直于射线且指向右侧（从设备的角度观察），Y+向上，Z+大致指向摄像头，具体参见朝向模式定义。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| hitResult | 命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |
| outPose | 返回交点的位姿，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARHitResultList\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResultList_Create(const AREngine_ARSession *session, AREngine_ARHitResultList **outHitResultList)
```

**描述**

创建一个命中检测结果对象列表。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outHitResultList | 待创建的命中检测结果对象列表，参见[AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARHitResultList\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARHitResultList_Destroy(AREngine_ARHitResultList *hitResultList)
```

**描述**

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| hitResultList | 待释放的命中检测结果对象列表，参见[AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist)。 |

### HMS\_AREngine\_ARHitResultList\_GetItem

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResultList_GetItem(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t index, AREngine_ARHitResult *outHitResult)
```

**描述**

在命中检测结果列表中获取指定索引的命中检测结果对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| hitResultList | 命中检测结果对象列表，参见[AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist)。 |
| index | 待获取的命中检测结果对象索引。 |
| outHitResult | 待获取的命中检测结果对象，参见[AREngine\_ARHitResult](arengine-capi-arengine.md#arengine_arhitresult)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARHitResultList\_GetSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARHitResultList_GetSize(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t *outSize)
```

**描述**

获取命中检测结果对象列表中包含的对象数。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| hitResultList | 命中检测结果对象列表，参见[AREngine\_ARHitResultList](arengine-capi-arengine.md#arengine_arhitresultlist)。 |
| outSize | 返回列表大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARImage\_GetFormat

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetFormat(const AREngine_ARSession *session, const AREngine_ARImage *image, AREngine_ARImageFormat *outFormat)
```

**描述**

获取当前帧的图像格式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 输入图像数据，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| outFormat | 返回当前帧的图像格式。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetHeight

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetHeight(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outHeight)
```

**描述**

获取当前帧的图像数据的高度。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| outHeight | 返回当前帧的图像的高度，以Pixel为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetNativeBuffer

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetNativeBuffer(const AREngine_ARSession *session, const AREngine_ARImage *image, OH_NativeBuffer **outNativeBuffer)
```

**描述**

获取当前帧图像对象的NativeBuffer数据。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| outNativeBuffer | 返回当前帧图像的NativeBuffer数据。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_NATIVEBUFFER\_CREATE\_FAILED | 创建NativeBuffer失败。 |
| ARENGINE\_ERROR\_NATIVEBUFFER\_WRITE\_FAILED | 无法写入NativeBuffer。 |

### HMS\_AREngine\_ARImage\_GetPlaneCount

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneCount(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outCount)
```

**描述**

获取当前帧图像的平面数量。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| outCount | 返回当前帧图像的平面数量。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetPlaneData

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneData(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength)
```

**描述**

获取当前帧图像的平面数据。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| planeIndex | 平面的索引。介于0和n-1，其中n是该图像的平面数。 |
| outData | 返回当前图像数据指针。 |
| outLength | 返回当前图像的长度，以Byte为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetPlanePixelStride

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetPlanePixelStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outPixelStride)
```

**描述**

获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| planeIndex | 平面的索引。介于0和n-1，其中n是该图像的平面数。 |
| outPixelStride | 返回图像的步幅，以Byte为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetPlaneRowStride

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneRowStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outRowStride)
```

**描述**

获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| planeIndex | 平面的索引。介于0和n-1，其中n是该图像的平面数。 |
| outRowStride | 返回图像的行跨距，以Byte为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetTimestamp

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARImage *image, int64_t *outTimestamp)
```

**描述**

获取图像的时间戳。

时间戳通常是单调递增的，以ns为单位。时间戳的具体含义和时基取决于提供图像的源。 来自不同来源的图像的时间戳可能具有不同的时基，因此不应该相互比较。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| outTimestamp | 返回图像的时间戳，以ns为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_GetWidth

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARImage_GetWidth(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outWidth)
```

**描述**

获取当前帧的图像数据的宽度。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| image | 当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |
| outWidth | 返回当前帧的图像的宽度，以Pixel为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARImage\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARImage_Release(AREngine_ARImage *image)
```

**描述**

释放当前帧的图像对象，由[HMS\_AREngine\_ARFrame\_AcquireCameraImage](arengine-capi-arengine.md#hms_arengine_arframe_acquirecameraimage)创建的对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| image | 待释放的当前帧图像对象，参见[AREngine\_ARImage](arengine-capi-arengine.md#arengine_arimage)。 |

### HMS\_AREngine\_ARPlane\_AcquireSubsumedBy

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_AcquireSubsumedBy(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlane **outSubsumedBy)
```

**描述**

获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outSubsumedBy | 返回指定平面的父平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetCenterPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPose *outPose)
```

**描述**

获取从平面的局部坐标系到世界坐标系转换的位姿信息。

平面局部坐标系（右手坐标系）为：原点在包裹平面矩形的中心，矩形更长的边方向为X轴，短边方向为Z轴，Y+为平面法向量。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outPose | 返回平面的局部坐标系到世界坐标系转换的位姿信息，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetExtentX

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentX(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentX)
```

**描述**

获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outExtentX | 返回平面的矩形边界沿平面局部坐标系X轴的长度，以m为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetExtentZ

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentZ(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentZ)
```

**描述**

获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outExtentZ | 返回平面的矩形边界沿平面局部坐标系Z轴的长度，以m为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetLabel

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetLabel(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARSemanticPlaneLabel *label)
```

**描述**

获取平面的语义类型，如桌面、地板等。

使用时需要使用[HMS\_AREngine\_ARConfig\_SetSemanticMode](arengine-capi-arengine.md#hms_arengine_arconfig_setsemanticmode)启用语义识别模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| label | 返回当前平面的语义类型，参见[AREngine\_ARSemanticPlaneLabel](arengine-capi-arengine.md#arengine_arsemanticplanelabel)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetPolygon

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outPolygonXz, int32_t polygonSize)
```

**描述**

获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。

这些值均在平面局部坐标系的x-z平面中定义，须经[HMS\_AREngine\_ARPlane\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose)转换到世界坐标系中。

在垂直平面中返回的值也是局部坐标系中的坐标[x1，z1，x2，z2，….]，需要使用[HMS\_AREngine\_ARPlane\_GetCenterPose](arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose)转换到世界坐标系。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outPolygonXz | 返回检测到平面的二维顶点数组。 |
| polygonSize | 二维顶点数组大小，通过[HMS\_AREngine\_ARPlane\_GetPolygonSize](arengine-capi-arengine.md#hms_arengine_arplane_getpolygonsize)接口获取。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetPolygonSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygonSize(const AREngine_ARSession *session, const AREngine_ARPlane *plane, int32_t *outPolygonSize)
```

**描述**

获取检测到平面的二维顶点数组大小。

配合[HMS\_AREngine\_ARPlane\_GetPolygon](arengine-capi-arengine.md#hms_arengine_arplane_getpolygon)接口使用。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outPolygonSize | 返回二维顶点数组大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_GetType

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_GetType(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlaneType *outPlaneType)
```

**描述**

获取平面的类型。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| outPlaneType | 返回平面的类型，参见[AREngine\_ARPlaneType](arengine-capi-arengine.md#arengine_arplanetype)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_IsPoseInExtents

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInExtents(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInExtents)
```

**描述**

判断位姿是否位于平面的矩形范围内。

如果传入的位姿（通过[HMS\_AREngine\_ARHitResult\_GetHitPose](arengine-capi-arengine.md#hms_arengine_arhitresult_gethitpose)获取）位于平面的矩形范围内，则返回非0值。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| pose | 位姿信息，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |
| outPoseInExtents | 返回位姿是否位于平面的矩形范围内，0表示不在范围内，非0表示在范围内。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPlane\_IsPoseInPolygon

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInPolygon)
```

**描述**

判断位姿是否位于平面的多边形范围内。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| plane | 待处理的平面对象，参见[AREngine\_ARPlane](arengine-capi-arengine.md#arengine_arplane)。 |
| pose | 位姿信息，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |
| outPoseInPolygon | 返回位姿是否位于平面的多边形范围内，0表示不在范围内，非0表示在范围内。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPoint\_GetOrientationMode

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPoint_GetOrientationMode(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPointOrientationMode *outOrientationMode)
```

**描述**

获取输入点的朝向模式。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| point | 输入点对象，参见[AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint)。 |
| outOrientationMode | 返回输入点的朝向模式，参见[AREngine\_ARPointOrientationMode](arengine-capi-arengine.md#arengine_arpointorientationmode)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPoint\_GetPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPoint_GetPose(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPose *outPose)
```

**描述**

获取输入点的位姿信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| point | 输入点对象，参见[AREngine\_ARPoint](arengine-capi-arengine.md#arengine_arpoint)。 |
| outPose | 返回输入点的位姿信息，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPointCloud\_GetData

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPointCloud_GetData(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, const float **outPointCloudData)
```

**描述**

获取点云中所有点的坐标及置信度数组。

其坐标值都在世界坐标系下，使用右手坐标系表示。点云对象可以通过[HMS\_AREngine\_ARFrame\_AcquirePointCloud](arengine-capi-arengine.md#hms_arengine_arframe_acquirepointcloud)获取。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| pointCloud | 点云对象，参见[AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud)。 |
| outPointCloudData | 返回点云中所有点的坐标及置信度数组。数据格式为[x0，y0，z0，c0，x1，y1，z1，c1，x2...]。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPointCloud\_GetNumberOfPoints

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPointCloud_GetNumberOfPoints(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int32_t *outNumberOfPoints)
```

**描述**

获取点云中所有点的坐标及置信度数组大小。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

与[HMS\_AREngine\_ARPointCloud\_GetData](arengine-capi-arengine.md#hms_arengine_arpointcloud_getdata)配合使用。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| pointCloud | 点云对象，参见[AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud)。 |
| outNumberOfPoints | 返回点云中所有点的坐标及置信度数组大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPointCloud\_GetTimestamp

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPointCloud_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int64_t *outTimestampNs)
```

**描述**

获取检测到当前特征点云的时间，以ns为单位。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| pointCloud | 点云对象，参见[AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud)。 |
| outTimestampNs | 返回检测到当前特征点云的时间。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPointCloud\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARPointCloud_Release(AREngine_ARPointCloud *pointCloud)
```

**描述**

释放点云对象使用的内存。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| pointCloud | 待释放的点云对象，参见[AREngine\_ARPointCloud](arengine-capi-arengine.md#arengine_arpointcloud)。 |

### HMS\_AREngine\_ARPose\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPose_Create(const AREngine_ARSession *session, const float *poseRaw, const uint32_t poseRawSize, AREngine_ARPose **outPose)
```

**描述**

分配并初始化一个新的位姿对象。

可以设置poseRaw为空，来创建未初始化的位姿对象，随后调用[HMS\_AREngine\_ARPoint\_GetPose](arengine-capi-arengine.md#hms_arengine_arpoint_getpose)、[HMS\_AREngine\_ARAnchor\_GetPose](arengine-capi-arengine.md#hms_arengine_aranchor_getpose)等为位姿对象赋值。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| poseRaw | 位姿数据，包括平移分量与旋转分量，数组大小为7，poseRaw[0]~poseRaw[3]为旋转分量quaternion，poseRaw[4]~poseRaw[6]为平移分量(x，y，z)。 |
| poseRawSize | 数组大小。取值范围：大于等于[ARENGINE\_POSE\_RAW\_SIZE](arengine-capi-arengine.md#arengine_pose_raw_size)。 |
| outPose | 返回新创建的位姿对象，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARPose\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARPose_Destroy(AREngine_ARPose *pose)
```

**描述**

释放位姿对象使用的内存。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| pose | 待释放的位姿对象，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

### HMS\_AREngine\_ARPose\_GetMatrix

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPose_GetMatrix(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size)
```

**描述**

将位姿数据转换成4X4的矩阵。

outMatrixColMajor4x4为存放数组，其中的数据按照列优先存储，该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| pose | 位姿对象，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |
| outMatrixColMajor4x4 | 返回一个大小为16的float数组，数据按照列优先存储。 |
| matrixColMajor4x4Size | 数组大小。数组大小定义为：[ARENGINE\_VIEW\_MATRIX\_SIZE](arengine-capi-arengine.md#arengine_view_matrix_size)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARPose\_GetPoseRaw

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARPose_GetPoseRaw(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outPoseRaw, int32_t poseRawSize)
```

**描述**

从位姿对象提取位姿数据。

包括平移分量与旋转分量，数组大小为7，poseRaw[0]~poseRaw[3]为旋转分量quaternion，poseRaw[4]~poseRaw[6]为平移分量(x，y，z)。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| pose | 位姿对象，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |
| outPoseRaw | 返回位姿数据。 |
| poseRawSize | 数组大小。数组大小定义为：[ARENGINE\_POSE\_RAW\_SIZE](arengine-capi-arengine.md#arengine_pose_raw_size)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSceneMesh\_AcquireIndexList

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outData, int32_t dataSize)
```

**描述**

获取mesh面片的索引集合。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| sceneMesh | 当前帧的Mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |
| outData | 返回mesh面片的索引集合。 |
| dataSize | mesh面片的索引个数，参见[HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexListSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize)
```

**描述**

获取mesh面片的索引个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| sceneMesh | 当前帧的Mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |
| outSize | 返回mesh面片的索引个数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSceneMesh\_AcquireVertexList

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize)
```

**描述**

获取mesh的顶点集合。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| sceneMesh | 当前帧的Mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |
| outData | 返回mesh顶点集合，数组内容为每个顶点的世界坐标展开，例如[x1, y1,z1, x2, y2, z2, ...] 。 |
| dataSize | mesh面片的顶点个数，参见[HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireverticessize)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSceneMesh\_AcquireVertexNormalList

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexNormalList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize)
```

**描述**

获取mesh面片的法向量集合。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| sceneMesh | 当前帧的Mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |
| outData | 返回mesh面片的法线向量集合，数组内容为每个面片法线向量的世界坐标展开，例如[x1,y1,z1, x2, y2, z2, ...]。 |
| dataSize | mesh面片的索引个数，参见[HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVerticesSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize)
```

**描述**

获取mesh的顶点个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| sceneMesh | 当前帧的Mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |
| outSize | 返回mesh的顶点个数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSceneMesh\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *sceneMesh)
```

**描述**

释放当前帧的mesh信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| sceneMesh | 当前帧的Mesh信息，参见[AREngine\_ARSceneMesh](arengine-capi-arengine.md#arengine_arscenemesh)。 |

### HMS\_AREngine\_ARSemanticDense\_AcquireCubeData

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, AREngine_ARSemanticDenseCubeData **outCubeData)
```

**描述**

获取识别到的高精几何重建对象数据中的立方体数据。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| semanticDenseData | 高精几何重建对象数据集合，参见[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)。 |
| outCubeData | 返回高精几何重建对象数据中立方体的数据，参见[AREngine\_ARSemanticDenseCubeData](arengine-struct-arsemanticdensecubedata.md)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, int64_t *outSize)
```

**描述**

获取识别到的高精几何重建对象数据中的立方体数量。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| semanticDenseData | 高精几何重建对象数据集合，参见[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)。 |
| outSize | 返回[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)对象中立方体数量的大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSemanticDense\_AcquirePointData

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, AREngine_ARSemanticDensePointData **outPointData)
```

**描述**

获取识别到的高精几何重建对象数据中的稠密点云数据。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| semanticDenseData | 高精几何重建对象数据集合，参见[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)。 |
| outPointData | 返回高精几何重建对象数据中稠密点云的数据，参见[AREngine\_ARSemanticDensePointData](arengine-struct-arsemanticdensepointdata.md)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSemanticDense\_AcquirePointDataSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, int64_t *outSize)
```

**描述**

获取识别到的高精几何重建对象数据中的稠密点云数量。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| semanticDenseData | 稠密点云的数据集合，参见[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)。 |
| outSize | 返回[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)对象中稠密点云数量的大小。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSemanticDense\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARSemanticDense_Release(AREngine_ARSemanticDenseData *semanticDenseData)
```

**描述**

释放高精几何重建对象。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| semanticDenseData | 释放高精几何重建对象，参见[AREngine\_ARSemanticDenseData](arengine-capi-arengine.md#arengine_arsemanticdensedata)。 |

### HMS\_AREngine\_ARSession\_AcquireNewAnchor

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_AcquireNewAnchor(AREngine_ARSession *session, const AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor)
```

**描述**

创建一个持续跟踪的锚点。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| pose | 创建锚点时使用的pose对象，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |
| outAnchor | 被创建的锚点对象，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_NOT\_TRACKING | 未跟踪状态。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARSession\_Configure

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Configure(AREngine_ARSession *session, const AREngine_ARConfig *config)
```

**描述**

配置[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)会话。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 需要配置到设备上的配置对象，参见 [AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_SESSION\_NOT\_PAUSED | 会话未暂停状态。 |

### HMS\_AREngine\_ARSession\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Create(void *env, void *applicationContext, AREngine_ARSession **outSessionPointer)
```

**描述**

创建一个新的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)会话。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中返回801错误码，可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**需要权限：** ohos.permission.CAMERA 和 ohos.permission.GYROSCOPE 和 ohos.permission.ACCELEROMETER

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| env | 当前APP的JNI运行环境信息。 |
| applicationContext | 与应用对应的Context。 |
| outSessionPointer | 被创建的会话对象，参见[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED | 权限未授予状态。如相机权限未授予。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED | 不可用：设备不兼容状态。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARSession\_Create\_Human\_Perception

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Create_Human_Perception(void *env, void *applicationContext, REngine_ARSession **outSessionPointer)
```

**描述**

创建一个新的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)人体追踪会话。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**需要权限：** ohos.permission.CAMERA

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| env | 当前APP的JNI运行环境信息。 |
| applicationContext | 与应用对应的Context。 |
| outSessionPointer | 被创建的会话对象，参见[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED | 权限未授予状态。如相机权限未授予。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED | 不可用：设备不兼容状态。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARSession\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARSession_Destroy(AREngine_ARSession *session)
```

**描述**

释放[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)会话使用的资源。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |

### HMS\_AREngine\_ARSession\_GetAllAnchors

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_GetAllAnchors(const AREngine_ARSession *session, AREngine_ARAnchorList *outAnchorList)
```

**描述**

获取所有锚点，包括[AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate)中包含的所有状态下的锚点。

应用处理时需要仅绘制[ARENGINE\_TRACKING\_STATE\_TRACKING](arengine-capi-arengine.md#arengine_artrackingstate)状态的锚点，删除[ARENGINE\_TRACKING\_STATE\_STOPPED](arengine-capi-arengine.md#arengine_artrackingstate)状态的锚点。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outAnchorList | 返回所有的锚点对象列表，参见[AREngine\_ARAnchorList](arengine-capi-arengine.md#arengine_aranchorlist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSession\_GetAllTrackables

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_GetAllTrackables(const AREngine_ARSession *session, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList)
```

**描述**

获取所有指定类型的可跟踪对象集合。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| filterType | 当前指定的可跟踪对象类型，参见[AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype)。 |
| outTrackableList | 返回指定类型的可跟踪对象集合，参见 [AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSession\_GetCameraConfig

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_GetCameraConfig(const AREngine_ARSession *session, AREngine_ARCameraConfig *outCameraConfig)
```

**描述**

获取相机配置信息。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outCameraConfig | 返回相机配置信息，参见[AREngine\_ARCameraConfig](arengine-capi-arengine.md#arengine_arcameraconfig)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSession\_Pause

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Pause(AREngine_ARSession *session)
```

**描述**

暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARSession\_Resume

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Resume(AREngine_ARSession *session)
```

**描述**

开始运行[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)，或者在调用[HMS\_AREngine\_ARSession\_Pause](arengine-capi-arengine.md#hms_arengine_arsession_pause)以后恢复[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)的运行状态。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE | 相机不可用状态。 |

### HMS\_AREngine\_ARSession\_SetCameraGLTexture

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_SetCameraGLTexture(AREngine_ARSession *session, uint32_t textureId)
```

**描述**

设置可用于存储相机预览流数据的OpenGL纹理。

应用调用[HMS\_AREngine\_ARSession\_Update](arengine-capi-arengine.md#hms_arengine_arsession_update)后，AR Engine会更新相机预览到纹理中。

纹理使用时需指定为GL\_TEXTURE\_EXTERNAL\_OES，如：glBindTexture(GL\_TEXTURE\_EXTERNAL\_OES, textureId)。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| textureId | 相机预览数据流的OpenGL textureId，大于0。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSession\_SetDisplayGeometry

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_SetDisplayGeometry(AREngine_ARSession *session, AREngine_ARPoseType rotation, int32_t width, int32_t height)
```

**描述**

设置显示的高和宽，以Pixel为单位。

该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| rotation | 显示旋转常量，值为[AREngine\_ARPoseType](arengine-capi-arengine.md#arengine_arposetype)中定义的枚举值。 |
| width | 显示的宽度，以Pixel为单位。其最大数值受设备屏幕像素限制，可通过[XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)获取。 |
| height | 显示的高度，以Pixel为单位。其最大数值受设备屏幕像素限制，可通过[XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)获取。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARSession\_Stop

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Stop(AREngine_ARSession *session)
```

**描述**

停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。

调用后，如果要再次启动，需要新建[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |

### HMS\_AREngine\_ARSession\_Update

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARSession_Update(AREngine_ARSession *session, AREngine_ARFrame *outFrame)
```

**描述**

更新AR Engine的计算结果。

应用应在需要获取最新的数据时调用此接口，如相机发生移动以后，使用此接口可以获取新的锚点坐标、平面坐标、相机获取的图像帧等。

如果[HMS\_AREngine\_ARConfig\_GetUpdateMode](arengine-capi-arengine.md#hms_arengine_arconfig_getupdatemode)为[ARENGINE\_UPDATE\_MODE\_BLOCKING](arengine-capi-arengine.md#arengine_arupdatemode)状态，那么该函数会阻塞至有新的帧可用。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outFrame | 返回更新后的帧对象，参见[AREngine\_ARFrame](arengine-capi-arengine.md#arengine_arframe)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_FATAL | 失败状态。 |
| ARENGINE\_ERROR\_SESSION\_PAUSED | 会话已暂停状态。 |
| ARENGINE\_ERROR\_MISSING\_GL\_CONTEXT | 缺少GL上下文状态。 |
| ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE | 相机不可用状态。 |
| ARENGINE\_ERROR\_IMAGE\_INVALID\_DATABASE | 没有有效的图像数据库。  **起始版本：** 5.1.0(18) |

### HMS\_AREngine\_ARTarget\_GetAxisAlignedBoundingBox

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *outAabb, int32_t aabbSize)
```

**描述**

获取语义物体最小外接包围盒坐标，坐标格式为(xmin，ymin，zmin，xmax，ymax，zmax)。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| target | 待处理的目标语义对象，参见[AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget)。 |
| outAabb | 返回当前目标语义识别物体的最小外接包围盒坐标集。 |
| aabbSize | 数组大小为：[ARENGINE\_AABB\_POINT\_SIZE](arengine-capi-arengine.md#arengine_aabb_point_size)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTarget\_GetCenterPose

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTarget_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARPose *outARPose)
```

**描述**

获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| target | 待处理的目标语义对象，参见[AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget)。 |
| outARPose | 返回目标语义对象的局部坐标系到世界坐标系转换的位姿，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTarget\_GetRadius

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTarget_GetRadius(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *radius)
```

**描述**

获取语义物体的球体半径。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| target | 待处理的目标语义对象，参见[AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget)。 |
| radius | 返回当前目标语义物体的球体半径，以m为单位。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTarget\_GetShapeType

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTarget_GetShapeType(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARTargetShapeLabel *shape)
```

**描述**

获取语义物体的形状类型。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| target | 待处理的目标语义对象，参见[AREngine\_ARTarget](arengine-capi-arengine.md#arengine_artarget)。 |
| shape | 返回当前目标语义识别到的物体形状类型，参见 [AREngine\_ARTargetShapeLabel](arengine-capi-arengine.md#arengine_artargetshapelabel)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTrackable\_AcquireNewAnchor

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackable_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARTrackable *trackable, AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor)
```

**描述**

通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| trackable | 可跟踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |
| pose | 可跟踪对象的位姿信息，参见[AREngine\_ARPose](arengine-capi-arengine.md#arengine_arpose)。 |
| outAnchor | 新创建的锚点对象，参见[AREngine\_ARAnchor](arengine-capi-arengine.md#arengine_aranchor)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_NOT\_TRACKING | 未跟踪状态。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARTrackable\_GetAnchors

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackable_GetAnchors(AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARAnchorList *outAnchorList)
```

**描述**

获取绑定到输入可跟踪对象的锚点对象列表。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| trackable | 可跟踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |
| outAnchorList | 返回锚点对象列表，此列表必须使用[HMS\_AREngine\_ARAnchorList\_Create](arengine-capi-arengine.md#hms_arengine_aranchorlist_create)创建。如果使用已经创建的列表，则此列表将被重新赋值。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTrackable\_GetTrackingState

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackable_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackingState *outTrackingState)
```

**描述**

获取当前可跟踪对象的跟踪状态。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| trackable | 可跟踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |
| outTrackingState | 返回可跟踪对象的跟踪状态，参见[AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTrackable\_GetType

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackable_GetType(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackableType *outTrackableType)
```

**描述**

获取可跟踪对象的类型。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| trackable | 可跟踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |
| outTrackableType | 返回可跟踪对象的类型，参见[AREngine\_ARTrackableType](arengine-capi-arengine.md#arengine_artrackabletype)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTrackable\_Release

PhoneTabletTV

```
1. void HMS_AREngine_ARTrackable_Release(AREngine_ARTrackable *trackable)
```

**描述**

释放可跟踪对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| trackable | 待释放的可跟踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |

### HMS\_AREngine\_ARTrackableList\_AcquireItem

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackableList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t index, AREngine_ARTrackable **outTrackable)
```

**描述**

从可跟踪列表中获取指定index的对象。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| trackableList | 被检索的可跟踪对象的列表，参见[AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist)。 |
| index | 可跟踪对象在可跟踪对象列表中的位置。最大值不超过[HMS\_AREngine\_ARTrackableList\_GetSize](arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)。 |
| outTrackable | 返回目标可跟踪对象，参见[AREngine\_ARTrackable](arengine-capi-arengine.md#arengine_artrackable)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARTrackableList\_Create

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackableList_Create(const AREngine_ARSession *session, AREngine_ARTrackableList **outTrackableList)
```

**描述**

创建一个可跟踪对象列表。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| outTrackableList | 待创建的可跟踪对象列表，参见[AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED | 资源耗尽状态。 |

### HMS\_AREngine\_ARTrackableList\_Destroy

PhoneTabletTV

```
1. void HMS_AREngine_ARTrackableList_Destroy(AREngine_ARTrackableList *trackableList)
```

**描述**

释放可跟踪对象列表，以及它持有的所有锚点引用。

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| trackableList | 待释放的可跟踪对象列表，参见[AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist)。 |

### HMS\_AREngine\_ARTrackableList\_GetSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARTrackableList_GetSize(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t *outSize)
```

**描述**

获取此列表中的可跟踪对象的数量。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| trackableList | 可跟踪对象列表，参见[AREngine\_ARTrackableList](arengine-capi-arengine.md#arengine_artrackablelist)。 |
| outSize | 返回可跟踪对象列表中可跟踪对象的数量。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonConfidence

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConfidence(const AREngine_ARSession *session, const AREngine_ARBody *body, const float **outConfidence)
```

**描述**

获取人体对象每个骨骼点检测的置信度。置信度数组大小为骨骼点个数，且与[HMS\_AREngine\_ARBody\_GetSkeletonTypes](arengine-capi-arengine.md#hms_arengine_arbody_getskeletontypes)返回的骨骼类型顺序一致，每一个元素为[0，1]范围的置信度值。置信度趋于1，代表识别的骨骼点越准确。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待识别骨骼点置信度的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outConfidence | 骨骼点置信度。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonConnection

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConnection(const AREngine_ARSession *session, const AREngine_ARBody *body, const AREngine_ARBodySkeletonType **outSkeletonConnection)
```

**描述**

获取人体对象骨骼点之间的链接关系数据。一个链接关系表示为两个骨骼点的类型。如返回值为[ARENGINE\_ARBODY\_SKELETON\_R\_WRIST，ARENGINE\_ARBODY\_SKELETON\_R\_ELBOW，...]，表示右手腕与右手肘相连成为一条骨骼。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待识别骨骼点链接关系数据的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outSkeletonConnection | 骨骼点之间的链接关系，参见[AREngine\_ARBodySkeletonType](arengine-capi-arengine.md#arengine_arbodyskeletontype)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonConnectionSize

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConnectionSize(const AREngine_ARSession *session, const AREngine_ARBody *body, int32_t *outConnectionCount)
```

**描述**

获取人体对象骨骼点之间的链接关系总数。该函数一般与[HMS\_AREngine\_ARBody\_GetSkeletonConnection](arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnection)对应使用。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待获取骨骼点链接关系总数的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outConnectionCount | 骨骼点之间的链接关系总数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonTypes

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonTypes(const AREngine_ARSession *session, const AREngine_ARBody *body, const AREngine_ARBodySkeletonType **outSkeletonTypes)
```

**描述**

获取识别出的人体对象骨骼点类型。骨骼点类型可参见[AREngine\_ARBodySkeletonType](arengine-capi-arengine.md#arengine_arbodyskeletontype)。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待获取骨骼点类型的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outSkeletonTypes | 人体对象中识别出的骨骼点类型，参见[AREngine\_ARBodySkeletonType](arengine-capi-arengine.md#arengine_arbodyskeletontype)。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonPointCount

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointCount(const AREngine_ARSession *session, const AREngine_ARBody *body, int32_t *outPointCount)
```

**描述**

获取人体对象中识别出的骨骼点个数。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待获取骨骼点数的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outPointCount | 人体对象中识别出的骨骼点个数。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonPointData2D

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointData2D(const AREngine_ARSession *session, const AREngine_ARBody *body, const float **outSkeletonPointData2D)
```

**描述**

当运行2D骨骼跟踪算法时，返回人体骨骼点的2D坐标数据。返回值的格式为 [x0，y0，x1，y1，…]的数组。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outSkeletonPointData2D | 人体骨骼点的2D坐标。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetSkeletonPointIsValid

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointIsValid(const AREngine_ARSession *session, const AREngine_ARBody *body, const int32_t **outSkeletonPointIsValid)
```

**描述**

获取人体对象骨骼点的坐标是否有效，返回有效性数组。值为0说明骨骼点坐标数据无效，1说明骨骼点坐标数据有效。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待获取坐标有效性数组的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outSkeletonPointIsValid | 坐标有效性数组。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetBodyTrackId

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetBodyTrackId(const AREngine_ARSession *session, const AREngine_ARBody *body, const int32_t *outBodyTrackId)
```

**描述**

获取指定人体对象的标识。当识别出多个Body时，每个Body有个标识，可以通过该接口获取指定人体对象的标识。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待获取标识的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| outBodyTrackId | 人体对象对应的标识。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARBody\_GetBodyTimeStamp

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARBody_GetBodyTimeStamp(const AREngine_ARSession *session, const AREngine_ARBody *body, int64_t *timeStamp)
```

**描述**

获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| body | 待获取检测时间点的人体对象，参见[AREngine\_ARBody](arengine-capi-arengine.md#arengine_arbody)。 |
| timeStamp | 人体对象的检测时间点。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

### HMS\_AREngine\_ARConfig\_SetBodyDetectedNum

PhoneTabletTV

```
1. AREngine_ARStatus HMS_AREngine_ARConfig_SetBodyDetectedNum(const AREngine_ARSession *session, AREngine_ARConfig *config, int32_t maxNum)
```

**描述**

设置追踪人数。

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[HMS\_AREngine\_CheckSupported](arengine-capi-arengine.md#hms_arengine_checksupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)对象。 |
| config | 指向待获取配置信息的配置对象，参见[AREngine\_ARConfig](arengine-capi-arengine.md#arengine_arconfig)。 |
| maxNum | 追踪人数，当前支持1或2，默认为1，若设置的追踪人数超过2，则按2处理。 |

**返回：**

接口执行状态，参见[AREngine\_ARStatus](arengine-capi-arengine.md#arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE\_SUCCESS | 成功状态。 |
| ARENGINE\_ERROR\_INVALID\_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
