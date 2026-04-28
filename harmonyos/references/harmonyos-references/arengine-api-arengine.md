---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine
title: arEngine（AR增强现实能力）
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > ArkTS API > arEngine（AR增强现实能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:14:28+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bdf57e9eaccacc4dfefa3afa1f6538b6546d8e030450a0f9bbecd90ec43825c2
---

本模块提供AR Engine（AR引擎服务）的arEngine（AR增强现实能力）相关接口。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

## 导入模块

PhoneTabletTV

```
1. import { arEngine } from '@kit.AREngine';
```

## ARFeatureType

PhoneTabletTV

枚举，AR特性类别。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| ARENGINE\_FEATURE\_TYPE\_SLAM | 0 | 运动跟踪及平面识别特性。 |
| ARENGINE\_FEATURE\_TYPE\_DEPTH | 1 | 深度估计特性。 |
| ARENGINE\_FEATURE\_TYPE\_MESH | 2 | 环境Mesh识别特性。 |
| ARENGINE\_FEATURE\_TYPE\_IMAGE | 3 | 图像跟踪特性。 |
| ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE | 4 | 高精几何重建特性。 |
| ARENGINE\_FEATURE\_TYPE\_SEMANTIC | 5 | 平面及物体语义特性。 |
| ARENGINE\_FEATURE\_TYPE\_FACE | 6 | 人脸识别与跟踪特性。 |
| ARENGINE\_FEATURE\_TYPE\_BODY | 7 | 人体骨骼点识别与跟踪特性。 |

## ARAddAugmentedImageMode

PhoneTabletTV

枚举，添加图片模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NORMAL | 0 | 正常模式。  当添加的图片数量超过默认的最多图片数量（50）时，AR Engine会报告错误，错误信息见[1009200011](arengine-error-code.md#section1009200011-添加的图片数量超过最大数量)。 |
| UPDATE | 1 | 更新模式。  当添加的图片数量超过默认的最多图片数量（50）时，AR Engine会删除原有的最旧数据，以添加新的图片。 |

## ARAddAugmentedImageReason

PhoneTabletTV

枚举，添加图像失败原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NONE | 0 | 无失败原因，图像成功添加。 |
| SIZE\_NOT\_MATCH | 1 | 图像尺寸不正确。  **说明：** 图像尺寸评价从宽高比、分辨率两个维度进行。建议宽高比、分辨率的评价为Unfit以上。 |
| LIGHT\_ANOMALY | 2 | 图像亮度过亮或过暗。 |
| FEATURE\_LIMIT | 3 | 图像颜色单一，如纯色图片。 |
| OTHER | 4 | 其他原因，如图片有反光、光斑，重复性内容等。 |

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

## ARAnimojiTriangleLabel

PhoneTabletTV

枚举，人脸Mesh三角面标签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| LABEL\_NON\_FACE | -1 | 不是脸部部位。 |
| LABEL\_FACE\_OTHER | 0 | 脸部非关键部位。 |
| LABEL\_LOWER\_LIP | 1 | 下嘴唇。 |
| LABEL\_UPPER\_LIP | 2 | 上嘴唇。 |
| LABEL\_LEFT\_EYE | 3 | 左眼睛。 |
| LABEL\_RIGHT\_EYE | 4 | 右眼睛。 |
| LABEL\_LEFT\_BROW | 5 | 左眉毛。 |
| LABEL\_RIGHT\_BROW | 6 | 右眉毛。 |
| LABEL\_BROW\_CENTER | 7 | 眉心。 |
| LABEL\_NOSE | 8 | 鼻子。 |

## ARBlendShapeType

PhoneTabletTV

枚举，微表情类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| EYE\_BLINK\_LEFT | 0 | 左眼闭合。 |
| EYE\_LOOK\_DOWN\_LEFT | 1 | 左上眼皮微下垂。 |
| EYE\_LOOK\_IN\_LEFT | 2 | 左眼内部眼皮向左扩。 |
| EYE\_LOOK\_OUT\_LEFT | 3 | 左眼睑向左扩。 |
| EYE\_LOOK\_UP\_LEFT | 4 | 左眼上眼皮微上抬。 |
| EYE\_SQUINT\_LEFT | 5 | 左下眼睑上抬。 |
| EYE\_WIDE\_LEFT | 6 | 左眼瞪大眼。 |
| EYE\_BLINK\_RIGHT | 7 | 闭右眼。 |
| EYE\_LOOK\_DOWN\_RIGHT | 8 | 右上眼皮微下垂。 |
| EYE\_LOOK\_IN\_RIGHT | 9 | 右眼内部眼皮向右扩。 |
| EYE\_LOOK\_OUT\_RIGHT | 10 | 右眼睑向右扩。 |
| EYE\_LOOK\_UP\_RIGHT | 11 | 右眼上眼皮微上抬 |
| EYE\_SQUINT\_RIGHT | 12 | 右下眼睑上抬。 |
| EYE\_WIDE\_RIGHT | 13 | 右眼瞪大眼。 |
| JAW\_FORWARD | 14 | 下巴朝前。 |
| JAW\_LEFT | 15 | 下巴朝左 |
| JAW\_RIGHT | 16 | 下巴朝右。 |
| JAW\_OPEN | 17 | 张嘴。 |
| MOUTH\_FUNNEL | 18 | O型嘴。 |
| MOUTH\_PUCKER | 19 | 噘嘴。 |
| MOUTH\_LEFT | 20 | 嘴巴向左。 |
| MOUTH\_RIGHT | 21 | 嘴巴向右。 |
| MOUTH\_SMILE\_LEFT | 22 | 左嘴角向左 |
| MOUTH\_SMILE\_RIGHT | 23 | 右嘴角向右歪。 |
| MOUTH\_FROWN\_LEFT | 24 | 左嘴角下拉 |
| MOUTH\_FROWN\_RIGHT | 25 | 右嘴角下拉。 |
| MOUTH\_DIMPLE\_LEFT | 26 | 左酒窝上抬。 |
| MOUTH\_DIMPLE\_RIGHT | 27 | 右酒窝上抬。 |
| MOUTH\_STRETCH\_LEFT | 28 | 嘴角向左拉。 |
| MOUTH\_STRETCH\_RIGHT | 29 | 嘴角向右拉。 |
| MOUTH\_ROLL\_LOWER | 30 | 下嘴唇向内抿嘴。 |
| MOUTH\_ROLL\_UPPER | 31 | 抿上嘴唇。 |
| MOUTH\_SHRUG\_LOWER | 32 | 撅下嘴唇。 |
| MOUTH\_SHRUG\_UPPER | 33 | 撅上嘴唇。 |
| MOUTH\_UPPER\_UP | 34 | 嘴唇上翻。 |
| MOUTH\_LOWER\_DOWN | 35 | 下嘴唇朝下。 |
| MOUTH\_LOWER\_OUT | 36 | 下嘴唇朝外。 |
| BROW\_DOWN\_LEFT | 37 | 左侧眉毛朝下。 |
| BROW\_DOWN\_RIGHT | 38 | 右侧眉毛朝下。 |
| BROW\_INNER\_UP | 39 | 双侧眉毛抬眉。 |
| BROW\_OUTER\_UP\_LEFT | 40 | 左眉外侧向上抬 |
| BROW\_OUTER\_UP\_RIGHT | 41 | 右眉外侧向上抬。 |
| CHEEK\_PUFF | 42 | 鼓腮。 |
| CHEEK\_SQUINT\_LEFT | 43 | 左脸颊上抬。 |
| CHEEK\_SQUINT\_RIGHT | 44 | 右脸颊上抬。 |
| FROWN\_NOSE\_MOUTH\_UP | 45 | 鼻子上抬。 |
| TONGUE\_IN | 46 | 舌头在嘴里上下位置。 |
| TONGUE\_OUT\_SLIGHT | 47 | 舌头直伸。 |
| TONGUE\_LEFT | 48 | 舌头朝左。 |
| TONGUE\_RIGHT | 49 | 舌头朝右。 |
| TONGUE\_UP | 50 | 舌头朝上。 |
| TONGUE\_DOWN | 51 | 舌头朝下。 |
| TONGUE\_LEFT\_UP | 52 | 舌头朝左上。 |
| TONGUE\_LEFT\_DOWN | 53 | 舌头朝左下。 |
| TONGUE\_RIGHT\_UP | 54 | 舌头朝右上。 |
| TONGUE\_RIGHT\_DOWN | 55 | 舌头朝右下。 |
| LEFT\_EYEBALL\_LEFT | 56 | 左眼球向左。 |
| LEFT\_EYEBALL\_RIGHT | 57 | 左眼球向右。 |
| LEFT\_EYEBALL\_UP | 58 | 左眼球向上。 |
| LEFT\_EYEBALL\_DOWN | 59 | 左眼球向下。 |
| RIGHT\_EYEBALL\_LEFT | 60 | 右眼球向左。 |
| RIGHT\_EYEBALL\_RIGHT | 61 | 右眼球向右。 |
| RIGHT\_EYEBALL\_UP | 62 | 右眼球向上。 |
| RIGHT\_EYEBALL\_DOWN | 63 | 右眼球向下。 |

## ARCameraLensFacing

PhoneTabletTV

枚举，摄像机镜头的朝向。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| REAR | 0 | 后置摄像头。 |
| FRONT | 1 | 前置摄像头。 |

## ARDepthMode

PhoneTabletTV

枚举，深度模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DISABLED | 0 | 关闭深度模式。 |
| AUTOMATIC | 1 | 开启深度模式。  AR Engine会自动尝试从多种深度源获取深度信息。  **说明：** 通常有两种深度源，运动算法和硬件深度传感器 (Time of Flight，简称ToF)。目前仅支持使用主RGB相机所获取的运动深度数据。 |

## ARFocusMode

PhoneTabletTV

枚举，对焦模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| FIXED | 0 | 固定焦点模式。 |
| AUTO | 1 | 自动对焦模式。 |

## ARImageFormat

PhoneTabletTV

枚举，图像数据格式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| UNKNOWN | 0 | 无效的图像格式。 |
| YUV\_420\_888 | 2 | YUV\_420\_888格式，适用于处理高分辨率的图像数据。YUV\_420\_888格式由三个数据缓冲区组成：Y分量（平面）的索引为0，U分量为1，V分量为2。Y分量与U/V分量互不相交。也就是说，Y分量的像素步长（Pixel Stride）始终为1。U分量和V分量则具有相同的行步长（Row Stride）和像素步长。 |
| Y\_8 | 3 | Y\_8格式，适用于对图像数据要求较低的精度或存储空间的场景。Y\_8格式由一个数据缓冲区组成，其平面索引（Index）为0。该数据缓冲区的数据类型为8位无符号整数。 |
| Y\_16 | 4 | Y\_16格式，适用于对图像数据精度要求较高的场景。Y\_16格式由一个数据缓冲区组成，其平面索引为0。该数据缓冲区的数据类型为16位无符号整数。 |

## ARMeshMode

PhoneTabletTV

枚举，网格模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DISABLED | 0 | 网格模式关闭。  AR Engine不会处理或显示网格数据。 |
| ENABLE | 1 | 网格模式开启。  AR Engine会尝试处理和显示网格数据。 |

## ARMultiFaceMode

PhoneTabletTV

枚举，多人脸检测模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| MULTIFACE\_DISABLE | 0x300 | 多人脸模式关闭。 |
| MULTIFACE\_ENABLE | 0x800 | 多人脸模式开启。 |

## ARBodyLandmarkType

PhoneTabletTV

枚举，人体关键点类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NECK | 1 | 颈部 |
| RIGHT\_SHOULDER | 2 | 右肩 |
| RIGHT\_ELBOW | 3 | 右肘 |
| RIGHT\_WRIST | 4 | 右腕 |
| LEFT\_SHOULDER | 5 | 左肩 |
| LEFT\_ELBOW | 6 | 左肘 |
| LEFT\_WRIST | 7 | 左腕 |
| RIGHT\_HIP | 8 | 右髋部 |
| RIGHT\_KNEE | 9 | 右膝 |
| RIGHT\_ANKLE | 10 | 右脚踝 |
| LEFT\_HIP | 11 | 左髋部 |
| LEFT\_KNEE | 12 | 左膝 |
| LEFT\_ANKLE | 13 | 左脚踝 |
| MID\_HIP | 14 | 中髋部 |
| RIGHT\_EAR | 15 | 右耳 |
| RIGHT\_EYE | 16 | 右眼 |
| NOSE | 17 | 鼻子 |
| LEFT\_EYE | 18 | 左眼 |
| LEFT\_EAR | 19 | 左耳 |
| SPINE | 20 | 脊柱 |

## ARPlaneFindingMode

PhoneTabletTV

枚举，平面检测模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DISABLED | 0 | 禁用平面检测。 |
| HORIZONTAL | 1 | 只检测水平面，如地板和桌子。 |
| VERTICAL | 2 | 只检测竖直平面，如墙壁。 |
| HORIZONTAL\_AND\_VERTICAL | 3 | 同时检测水平面和竖直平面。 |

## ARPlaneType

PhoneTabletTV

枚举，平面类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| FACING\_HORIZONTAL\_UPWARD | 0 | 朝上的水平面，如地面和桌面平台。 |
| FACING\_HORIZONTAL\_DOWNWARD | 1 | 朝下的水平面，如天花板。 |
| FACING\_VERTICAL | 2 | 垂直的水平面，如墙壁。 |
| FACING\_INVALID | 3 | 无效或不支持的平面类型。  这可能是由于环境变化、光线条件或其他因素导致。 |

## ARPointOrientationMode

PhoneTabletTV

枚举，朝向模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INITIALIZED\_TO\_IDENTITY | 0 | 与世界坐标系的朝向一致，但会稍作调整。 |
| ESTIMATED\_SURFACE\_NORMAL | 1 | 朝向由估计的平面法向量决定。  点的方向将与平面的方向一致，适用于需要根据平面特征来确定点方向的应用场景。 |

## ARPoseMode

PhoneTabletTV

枚举，创建世界坐标系的方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| GRAVITY | 0 | 由重力确定。  世界坐标系的Y轴与重力方向一致，原点为设备所在的原始位置。参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |
| GRAVITY\_AND\_HEADING | 1 | 由重力和指南针确定。  世界坐标系的Y轴与重力方向一致，X轴指向指南针北向，原点为设备所在的原始位置。参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。  **说明：** 该选项当前仅支持省电模式，请将[ARPowerMode](arengine-api-arengine.md#arpowermode)置为POWER\_SAVING以启动该选项。 |

## ARPoseType

PhoneTabletTV

枚举，位姿类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| IDENTITY | 0 | 默认状态，即没有任何旋转或平移。 |
| ROTATE\_90 | 1 | 顺时针旋转90度。 |
| ROTATE\_180 | 2 | 顺时针旋转180度。 |
| ROTATE\_270 | 3 | 顺时针旋转270度。 |

## ARPowerMode

PhoneTabletTV

枚举，电源功耗模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NORMAL | 0 | 正常模式。  AR Engine在性能和电源消耗之间保持平衡。 |
| POWER\_SAVING | 1 | 节能模式。  AR Engine优先减少电源消耗。这可能会降低一些性能，以换取更长的电池寿命。 |
| PERFORMANCE\_FIRST | 2 | 性能优先模式。  AR Engine优先考虑性能，提供更高的处理能力和更快的响应时间。这可能会增加电源消耗。 |
| BOOST | 3 | 仅输出设备姿态信息模式。  AR Engine仅输出设备的位姿信息，电源消耗低于正常模式。在此模式下，[ARPlaneFindingMode](arengine-api-arengine.md#arplanefindingmode)等与平面相关的设置不起作用。 |
| ULTRA\_POWER\_SAVING | 11 | 超级节能模式。  AR Engine进一步优化电源消耗，提供比节能模式更低的电源消耗，这可能会损失更多的性能。 |

## ARSemanticDenseMode

PhoneTabletTV

枚举，高精几何重建识别模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.0.0(20)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DISABLED | 0 | 关闭高精几何重建识别模式。 |
| NORMAL | 1 | 正常模式，仅开启稠密点云识别。 |
| CUBE\_VOLUME | 2 | 基于高精几何重建的立方体体积测量模式。 |
| CUBE\_SPACE | 3 | 基于高精几何重建的立方体空间容积测量模式。 |

## ARSemanticMode

PhoneTabletTV

枚举，语义模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NONE | 0 | 不使用语义。 |
| PLANE | 1 | 使用平面语义模式。 |

## ARSemanticPlaneLabel

PhoneTabletTV

枚举，当前平面识别到的语义类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| UNKNOWN | 0 | 未知平面类型。 |
| WALL | 1 | 墙面。 |
| FLOOR | 2 | 地面。 |
| SEAT | 3 | 座位，如椅子或凳子。 |
| TABLE | 4 | 桌子。 |
| CEILING | 5 | 天花板。 |
| DOOR | 6 | 门。 |
| WINDOW | 7 | 窗户。 |
| BED | 8 | 床。 |
| PLANE\_SPACE | 9 | 平面空间。  **起始版本：** 6.0.0(20) |
| CUBE\_VOLUME | 10 | 立方体体积。  **起始版本：** 6.0.0(20) |
| CUBE\_SPACE | 11 | 立方体空间容积。  **起始版本：** 6.0.0(20) |

## ARTrackingState

PhoneTabletTV

枚举，可追踪对象的追踪状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| TRACKING | 0 | 正在追踪。 |
| PAUSED | 1 | 暂停追踪。 |
| STOPPED | 2 | 停止追踪。 |

## ARTrackingStateReason

PhoneTabletTV

枚举，追踪失败的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NONE | 0 | 未知原因。  这可能是由于系统暂时无法识别可追踪对象，但仍在尝试追踪。 |
| EXCESSIVE\_MOTION | 1 | 目标移动过快。  可追踪对象（如平面、点、图像等）移动速度过快，导致AR Engine无法准确识别和跟踪。 |
| INSUFFICIENT\_FEATURES | 2 | 视觉特征不足。  可追踪对象的视觉特征不够丰富，如纹理不明显、颜色过于单一等，导致AR Engine无法准确识别和跟踪。 |

## ARTrackableType

PhoneTabletTV

枚举，可追踪对象类型，如平面、点等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| BASE | 0x41520100 | 基本的可追踪对象类型，AR Engine默认类型。 |
| PLANE | 0x41520101 | 平面类型的可追踪对象。 |
| POINT | 0x41520102 | 点类型的可追踪对象。 |
| AUGMENTED\_IMAGE | 0x41520104 | 增强型图像类型的可追踪对象。 |
| FACE | 0x50000002 | 人脸类型的可追踪对象。  **起始版本：** 6.1.0(23) |
| INVALID | 0 | 无效的可追踪对象类型。 |

## ARType

PhoneTabletTV

枚举，AR能力类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| WORLD | 0x01 | 环境追踪能力。 |
| BODY | 0x02 | 人体跟踪与骨骼关键点识别能力。  **起始版本：** 6.1.0(23) |
| FACE | 0x10 | 人脸追踪能力。  **起始版本：** 6.1.0(23) |
| IMAGE | 0x80 | 图像识别能力。 |

## Distortion

PhoneTabletTV

type Distortion = [number, number, number, number, number]

类型别名，用于表示一个包含五个数字的数组，为相机的畸变系数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字，相机内参，取值范围无限制。  其中Distortion [0]~Distortion [2]表示k1，k2，k3（径向畸变系数），Distortion [3]~Distortion [4]是切向畸变系数。 |

## ARAugmentedImageDatabase

PhoneTabletTV

增强图像数据库对象。

用于表示增强图像数据库的相关操作，如序列化、反序列化、添加图像、获取图像数量等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

### ARAugmentedImageDatabase.deserialize

PhoneTabletTV

deserialize(buffer: ArrayBuffer): Promise<void>

将增强图像数据库数据反序列化为一个新的增强图像数据库对象。使用Promise异步回调。

说明

这个操作是耗时的，建议在后台线程中运行。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 增强图像数据库的ArrayBuffer数据。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |
| 1009200008 | Resource exhausted. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let buffer: ArrayBuffer = new ArrayBuffer(0);
4. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
5. await imageDatabase.deserialize(buffer);
```

### ARAugmentedImageDatabase.serialize

PhoneTabletTV

serialize(): Promise<ArrayBuffer>

将增强图像数据库数据序列化为一个缓冲区。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回ArrayBuffer对象。  ArrayBuffer是一个缓冲区，这个缓冲区包含了增强图像数据库的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
4. await imageDatabase.serialize();
```

### ARAugmentedImageDatabase.addImage

PhoneTabletTV

addImage(name: string, pixelMap: image.PixelMap, widthInMeters: number): Promise<ARAddAugmentedImageResult>

将图像添加到图像数据库中，并输出相应图像的索引（Index）。开发者可以通过[ARAugmentedImageDatabase.getCapacity](arengine-api-arengine.md#araugmentedimagedatabasegetcapacity)获取可添加图像的最大数量，通过[ARConfig.addAugmentedImageMode](arengine-api-arengine.md#arconfig)接口来设置调用此接口后的行为。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 图像名称。  不允许为空，255个字符以内，超过255个的字符将会被丢弃。 |
| pixelMap | [image.PixelMap](js-apis-sendableimage.md#pixelmap) | 是 | 图像的信息。 |
| widthInMeters | number | 是 | 图像中对象的实际物理宽度。  无限制，单位为m。默认值是A4纸张的大小。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ARAddAugmentedImageResult](arengine-api-arengine.md#araddaugmentedimageresult)> | Promise对象，返回ARAddAugmentedImageResult对象。  ARAddAugmentedImageResult是一个表示添加增强图像结果的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |
| 1009200008 | Resource exhausted. |
| 1009200011 | The number of images added exceeds the maximum. |
| 1009200012 | Attempted to add an image with insufficient quality to the image database. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { arEngine } from '@kit.AREngine';

4. let color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4
5. let opts: image.InitializationOptions = {
6. editable: true,
7. pixelFormat: image.PixelMapFormat.RGBA_8888,
8. size: { height: 4, width: 6 }
9. }
10. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
11. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
12. await imageDatabase.addImage('xx', pixelMap, 0.3);
```

### ARAugmentedImageDatabase.getImageCount

PhoneTabletTV

getImageCount(): number

获取图像数据库中图像的数量。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 返回图像的数量。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
4. imageDatabase.getImageCount();
```

### ARAugmentedImageDatabase.getCapacity

PhoneTabletTV

getCapacity(): number

获取通过调用[ARAugmentedImageDatabase.addImage](arengine-api-arengine.md#araugmentedimagedatabaseaddimage)接口所能添加的图像最大数量。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 返回可添加图像的最大数量。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
4. imageDatabase.getCapacity();
```

### ARAugmentedImageDatabase.getImageAddMode

PhoneTabletTV

getImageAddMode(): ARAddAugmentedImageMode

获取图片添加模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARAddAugmentedImageMode](arengine-api-arengine.md#araddaugmentedimagemode) | 返回图片的添加模式。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
4. imageDatabase.getImageAddMode();
```

### ARAugmentedImageDatabase.setImageAddMode

PhoneTabletTV

setImageAddMode(mode: ARAddAugmentedImageMode): void

设置图片添加模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ARAddAugmentedImageMode](arengine-api-arengine.md#araddaugmentedimagemode) | 是 | 添加图片模式。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
4. imageDatabase.setImageAddMode(arEngine.ARAddAugmentedImageMode.UPDATE);
```

### ARAugmentedImageDatabase.release

PhoneTabletTV

release(): Promise<void>

释放增强图像数据库对象[ARAugmentedImageDatabase](arengine-api-arengine.md#araugmentedimagedatabase)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
4. await imageDatabase.release();
```

## ARCameraIntrinsics

PhoneTabletTV

相机内参。

包括fx、fy、cx、cy和畸变参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fx | number | 是 | 否 | 相机在x轴上的焦距。  可取任意值。 |
| fy | number | 是 | 否 | 相机在y轴上的焦距。  可取任意值。 |
| cx | number | 是 | 否 | 相机在x轴上的主点。  可取任意值。 |
| cy | number | 是 | 否 | 相机在y轴上的主点。  可取任意值。 |
| distortion | [Distortion](arengine-api-arengine.md#distortion) | 是 | 否 | 相机畸变参数。 |

## ARConfig

PhoneTabletTV

[ARSession](arengine-api-arengine.md#arsession)的功能配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ARType](arengine-api-arengine.md#artype) | 否 | 否 | AR能力类型。 |
| planeFindingMode | [ARPlaneFindingMode](arengine-api-arengine.md#arplanefindingmode) | 否 | 是 | 平面检测模式。  默认为HORIZONTAL\_AND\_VERTICAL。 |
| powerMode | [ARPowerMode](arengine-api-arengine.md#arpowermode) | 否 | 是 | 电源功耗模式。  默认为NORMAL。 |
| focusMode | [ARFocusMode](arengine-api-arengine.md#arfocusmode) | 否 | 是 | 对焦模式。  默认为FIXED。 |
| semanticMode | [ARSemanticMode](arengine-api-arengine.md#arsemanticmode) | 否 | 是 | 语义模式。  默认为NONE。 |
| maxMapSize | number | 否 | 是 | 存储地图数据的最大内存大小，单位为MB。可设定范围100MB~16GB，默认800MB。  建议根据设备的内存容量设置内存大小。超出硬件限制可能会导致意外错误。 |
| poseMode | [ARPoseMode](arengine-api-arengine.md#arposemode) | 否 | 是 | 创建世界坐标系的方式。  默认为GRAVITY。 |
| depthMode | [ARDepthMode](arengine-api-arengine.md#ardepthmode) | 否 | 是 | 深度模式。  默认为DISABLED。 |
| meshMode | [ARMeshMode](arengine-api-arengine.md#armeshmode) | 否 | 是 | 网格模式。  默认为DISABLED。 |
| addAugmentedImageMode | [ARAddAugmentedImageMode](arengine-api-arengine.md#araddaugmentedimagemode) | 否 | 是 | 添加图片模式。  默认为NORMAL。 |
| semanticDenseMode | [ARSemanticDenseMode](arengine-api-arengine.md#arsemanticdensemode) | 否 | 是 | 高精几何重建识别模式。  默认DISABLED。  **起始版本：** 6.0.0(20) |
| cameraLensFacing | [ARCameraLensFacing](arengine-api-arengine.md#arcameralensfacing) | 否 | 是 | 相机镜头朝向配置项。当cameraLensFacing配置为FRONT时，type配置为[ARType](arengine-api-arengine.md#artype).FACE或[ARType](arengine-api-arengine.md#artype).BODY才生效。  默认为REAR。  **起始版本：** 6.1.0(23) |
| multiFaceMode | [ARMultiFaceMode](arengine-api-arengine.md#armultifacemode) | 否 | 是 | 多人脸模式配置项。  默认为MULTIFACE\_DISABLE。  **起始版本：** 6.1.0(23) |
| maxDetectedBodyNum | number | 否 | 是 | 当类型为ARType.Body 时，需要检测的人体数量最大值。  默认为1，最大为2，超过2默认为2。  **起始版本：** 6.1.0(23) |

## ARPointCloud

PhoneTabletTV

可跟踪的3D点云集合。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 是 | 否 | 当前特征点云检测时的时间戳。  以ns为单位。 |
| points | Array<number> | 是 | 否 | 表示点云中所有点的坐标以及坐标对应的置信度数组。 |

## ARSemanticDenseCubeData

PhoneTabletTV

高精几何重建对象的立方体数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 当前立方体的ID。 |
| vertexSize | number | 是 | 否 | 当前立方体的顶点数量。 |
| vertexData | Array<number> | 是 | 否 | 当前立方体的顶点数据。  对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。 |
| confidence | number | 是 | 否 | 当前立方体的置信度。取值为0，1，2。 |
| label | [ARSemanticPlaneLabel](arengine-api-arengine.md#arsemanticplanelabel) | 是 | 否 | 当前立方体的语义标签。 |

## ARSemanticDensePointData

PhoneTabletTV

高精几何重建对象的稠密点云数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | ArrayBuffer | 是 | 否 | 稠密点云数据所有点的id数组。  **说明：** 该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |
| position | ArrayBuffer | 是 | 否 | 稠密点云数据所有点的坐标，以及它们的置信度数组，格式为[x0, y0, z0, c0, x1, y1, z1, c1, x2, ...]。  **说明：** 该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |
| color | ArrayBuffer | 是 | 否 | 稠密点云数据所有点的颜色，以 rgba 格式表示，格式为 [r0, g0, b0, a0, r1, g1, b1, a1, r2,...]。  **说明：** 该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |

## ARSession

PhoneTabletTV

管理AR Engine的系统状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

### ARSession.getFrame

PhoneTabletTV

getFrame(): ARFrame

获取AR Engine处理后的一帧数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARFrame](arengine-api-arengine.md#arframe) | 返回AR Engine处理后的一帧数据。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. class ARViewCallbackImpl extends arViewController.ARViewCallback {
5. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
6. // ...
7. }

9. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
10. // ...
11. }

13. async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
14. if (!ctx.session) {
15. // 如果没有创建session则退出，关于如何创建session请参考开发指南
16. return;
17. }

19. let arSession: arEngine.ARSession = ctx.session;
20. let frame: arEngine.ARFrame = arSession.getFrame();
21. await frame.release();
22. }
23. }
```

### ARSession.createAnchor

PhoneTabletTV

createAnchor(pose: ARPose): ARAnchor

创建一个用于连续跟踪的锚点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| pose | [ARPose](arengine-api-arengine.md#arpose) | 是 | 用于创建锚点的位姿对象。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARAnchor](arengine-api-arengine.md#aranchor) | 返回一个锚点对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { Quaternion, Vec3 } from '@kit.ArkGraphics3D';
2. import { arEngine } from '@kit.AREngine';

4. let r: Quaternion = {
5. x: 0,
6. y: 0,
7. z: 0,
8. w: 0
9. }
10. let t: Vec3 = { x: 0, y: 0, z: 0 };
11. let pose: arEngine.ARPose = arEngine.createARPose(r, t);
12. // arSession创建参考ARSession.getFrame接口示例代码
13. arSession.createAnchor(pose);
```

### ARSession.detachAnchor

PhoneTabletTV

detachAnchor(anchor: ARAnchor): void

停止追踪并解绑锚点。

说明

由于此函数并没有释放锚点[ARAnchor](arengine-api-arengine.md#aranchor)，开发者需要通过调用[ARAnchor.release](arengine-api-arengine.md#aranchorrelease)来释放锚点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchor | [ARAnchor](arengine-api-arengine.md#aranchor) | 是 | 要解绑的锚点对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let pose: arEngine.ARPose = arSession.getFrame().getCamera().getPose();
5. let anchor: arEngine.ARAnchor = arSession.createAnchor(pose);
6. arSession.detachAnchor(anchor);
```

### ARSession.getAllAnchors

PhoneTabletTV

getAllAnchors(): Array<ARAnchor>

获取所有状态的锚点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARAnchor](arengine-api-arengine.md#aranchor)> | 返回一个锚点对象组成的数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200008 | Resource exhausted. |

**示例：**

```
1. // arSession创建参考ARSession.getFrame接口示例代码
2. arSession.getAllAnchors();
```

### ARSession.getAllTrackables

PhoneTabletTV

getAllTrackables(type: ARTrackableType): Array<ARTrackable>

获取指定类型的所有可追踪对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | [ARTrackableType](arengine-api-arengine.md#artrackabletype) | 是 | 可追踪对象的类型。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARTrackable](arengine-api-arengine.md#artrackable)> | 返回一个可追踪对象组成的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |
| 1009200008 | Resource exhausted. |

**示例：**

```
1. // arSession创建参考ARSession.getFrame接口示例代码
2. arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
```

### ARSession.openFlash

PhoneTabletTV

openFlash(): Promise<boolean>

打开设备的闪光灯。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示设备的闪光灯已开启，返回false表示设备闪光灯未开启。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. // arSession创建参考ARSession.getFrame接口示例代码
2. await arSession.openFlash();
```

### ARSession.closeFlash

PhoneTabletTV

closeFlash(): Promise<boolean>

关闭设备的闪光灯。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示设备的闪光灯已关闭，返回false表示设备闪光灯未关闭。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. // arSession创建参考ARSession.getFrame接口示例代码
2. await arSession.closeFlash();
```

### ARSession.release

PhoneTabletTV

release(): Promise<void>

释放管理AR Engine系统状态对象[ARSession](arengine-api-arengine.md#arsession)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. // arSession创建参考ARSession.getFrame接口示例代码
2. await arSession.release();
```

## ImageComponent

PhoneTabletTV

图像组件的基本结构参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rowStride | number | 是 | 否 | 图像中两个连续像素行起始位置之间的字节数。行间距始终大于0。 |
| pixelStride | number | 是 | 否 | 图像中两个连续像素起始点之间的字节数。像素间距始终大于0。 |
| buffer | ArrayBuffer | 是 | 否 | 当前帧的平面数据缓冲区对象。  **说明：** 该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |

## ARAddAugmentedImageResult

PhoneTabletTV

添加增强图像的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 图像唯一索引，取值范围0~49。 |
| state | number | 否 | 否 | 添加增强图像的结果状态。成功为0，否则为1009200001。 |
| stateReason | [ARAddAugmentedImageReason](arengine-api-arengine.md#araddaugmentedimagereason) | 否 | 否 | 添加图像失败的原因。 |

## ARAnchor

PhoneTabletTV

锚点对象。

锚点描述与可追踪对象相关联的空间位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 锚点的索引，取值范围0~49。 |
| trackingState | [ARTrackingState](arengine-api-arengine.md#artrackingstate) | 是 | 否 | 可追踪对象的追踪状态。 |

### ARAnchor.getPose

PhoneTabletTV

getPose(): ARPose

获取锚点在世界坐标系中的位姿信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPose](arengine-api-arengine.md#arpose) | 返回位姿对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
5. anchors[0].getPose();
```

### ARAnchor.detach

PhoneTabletTV

detach(): void

停止追踪并解绑锚点。

说明

这个函数不会释放锚点，开发者需要通过调用[ARAnchor.release](arengine-api-arengine.md#aranchorrelease)方法来释放锚点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
5. anchors[0].detach();
```

### ARAnchor.release

PhoneTabletTV

release(): Promise<void>

释放锚点对象[ARAnchor](arengine-api-arengine.md#aranchor)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
5. await anchors[0].release();
```

## ARAugmentedImage

PhoneTabletTV

增强图像对象。

这个类继承自[ARTrackable](arengine-api-arengine.md#artrackable)类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| extendX | number | 是 | 否 | 表示在X轴上估计的物理图像宽度，单位为m。如果图像的追踪状态为PAUSED或STOPPED，返回的宽度信息是最后一次追踪的宽度。如果图像从未被追踪，返回0。 |
| extendZ | number | 是 | 否 | 表示在Z轴上估计的物理图像宽度，单位为m。如果图像的追踪状态为PAUSED或STOPPED，返回的宽度信息是最后一次追踪的宽度。如果图像从未被追踪，返回0。 |
| index | number | 是 | 否 | 表示增强图像在增强图像数据库中的图像索引，数值范围1~50，为图像在数据库中的唯一标识符。 |
| name | string | 是 | 否 | 表示增强图像的图像名称，最大为255Byte，该值可能不唯一。 |

## ARBlendShapes

PhoneTabletTV

用于管理人脸微表情，包含若干个表情参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 是 | 否 | 表示微表情的个数，最小为0，最大为64。 |

### ARBlendShapes.getData

PhoneTabletTV

getData(): ArrayBuffer

获取所有的表情参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 微表情数据。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
7. faceBlendShapes.getData();
```

### ARBlendShapes.getTypes

PhoneTabletTV

getTypes(): Array<ARBlendShapeType>

获取所有表情参数类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARBlendShapeType](arengine-api-arengine.md#arblendshapetype)> | 微表情的类型。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
7. faceBlendShapes.getTypes();
```

### ARBlendShapes.release

PhoneTabletTV

release(): Promise<void>

释放[ARBlendShapes](arengine-api-arengine.md#arblendshapes)对象。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
7. faceBlendShapes.release();
```

## ARLandmark

PhoneTabletTV

用于管理人脸关键点对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 是 | 否 | 表示人脸关键点的个数，固定为84。 |

### ARLandmark.getVertices2D

PhoneTabletTV

getVertices2D(): ArrayBuffer

获取人脸关键点的2D位姿信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 2D位姿信息。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceLandmark: arEngine.ARLandmark = face.getLandmark();
7. faceLandmark.getVertices2D();
```

### ARLandmark.getVertices3D

PhoneTabletTV

getVertices3D(): ArrayBuffer

获取人脸关键点的3D位姿信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 3D位姿信息。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceLandmark: arEngine.ARLandmark = face.getLandmark();
7. faceLandmark.getVertices3D();
```

### ARLandmark.release

PhoneTabletTV

release(): Promise<void>

释放[ARLandmark](arengine-api-arengine.md#arlandmark)对象。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceLandmark: arEngine.ARLandmark = face.getLandmark();
7. await faceLandmark.release();
```

## ARCamera

PhoneTabletTV

当前帧的摄像机信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [ARTrackingState](arengine-api-arengine.md#artrackingstate) | 是 | 否 | 可追踪对象的追踪状态。 |
| stateReason | [ARTrackingStateReason](arengine-api-arengine.md#artrackingstatereason) | 是 | 否 | 追踪失败的原因。 |
| viewMatrix | [Matrix4](js-apis-arkui-graphics.md#matrix4) | 是 | 否 | 摄像机在最新帧中的视图矩阵。 |

### ARCamera.getPose

PhoneTabletTV

getPose(): ARPose

获取摄像机在世界空间中的位姿。

位姿信息可参考[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。

位姿信息仅在状态返回TRACKING时才可使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPose](arengine-api-arengine.md#arpose) | 返回一个位姿对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let camera: arEngine.ARCamera = frame.getCamera();
6. camera.getPose();
```

### ARCamera.getDisplayOrientedPose

PhoneTabletTV

getDisplayOrientedPose(): ARPose

获取面向显示屏的虚拟摄像机在世界空间中的位姿。

位姿信息可参考[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。

位姿信息仅在状态返回TRACKING时才可使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPose](arengine-api-arengine.md#arpose) | 返回一个位姿对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let camera: arEngine.ARCamera = frame.getCamera();
6. camera.getDisplayOrientedPose();
```

### ARCamera.getProjectionMatrix

PhoneTabletTV

getProjectionMatrix(near: number, far: number): Matrix4

获取用于在相机图像上渲染虚拟内容的投影矩阵。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| near | number | 是 | 相机坐标系统中的近裁剪平面的距离，单位为m，值必须大于0。 |
| far | number | 是 | 相机坐标系统中的远裁剪平面的距离，单位为m，值必须大于0且大于near。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [Matrix4](js-apis-arkui-graphics.md#matrix4) | 返回一个Matrix4对象。  Matrix4是一个包含16个浮点数的数组，表示OpenGL中的列主旋转变换矩阵。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let camera: arEngine.ARCamera = frame.getCamera();
6. camera.getProjectionMatrix(0, 1);
```

### ARCamera.getImageIntrinsics

PhoneTabletTV

getImageIntrinsics(): ARCameraIntrinsics

获取离线相机的内参对象。

该对象可用于获取相机的焦距、图像尺寸、主点和畸变参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARCameraIntrinsics](arengine-api-arengine.md#arcameraintrinsics) | 返回一个相机内参对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let camera: arEngine.ARCamera = frame.getCamera();
6. camera.getImageIntrinsics();
```

## ARFace

PhoneTabletTV

用于人脸跟踪时返回人脸跟踪的结果。

这个类继承自[ARTrackable](arengine-api-arengine.md#artrackable)类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

### ARFace.getGeometry

PhoneTabletTV

getGeometry(): ARGeometry

获取人脸拓扑结构对象，即人脸Mesh对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARGeometry](arengine-api-arengine.md#argeometry) | 人脸拓扑结构对象，即人脸Mesh对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. face.getGeometry();
```

### ARFace.getBlendShapes

PhoneTabletTV

getBlendShapes(): ARBlendShapes

获取人脸微表情对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARBlendShapes](arengine-api-arengine.md#arblendshapes) | 人脸微表情对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. face.getBlendShapes();
```

### ARFace.getLandmark

PhoneTabletTV

getLandmark(): ARLandmark

获取人脸关键点对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARLandmark](arengine-api-arengine.md#arlandmark) | 人脸关键点对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. face.getLandmark();
```

## ARFaceAnchor

PhoneTabletTV

一个人脸类型的锚点对象。

这个类继承自[ARAnchor](arengine-api-arengine.md#aranchor)类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

### ARFaceAnchor.getFace

PhoneTabletTV

getFace(): ARFace

获取人脸跟踪的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARFace](arengine-api-arengine.md#arface) | 人脸跟踪的结果。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. // 该方法在ARViewCallback中使用
5. async onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): Promise<void> {
6. let faceAnchor: arEngine.ARFaceAnchor = anchor as arEngine.ARFaceAnchor;
7. let face: arEngine.ARFace = faceAnchor.getFace();
8. await face.release();
9. }
```

## ARBodyLandmark2D

PhoneTabletTV

人体骨骼关键点信息基本结构参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 骨骼关键点x坐标。 |
| y | number | 否 | 否 | 骨骼关键点y坐标。 |
| confidence | number | 否 | 否 | 骨骼关键点置信度。取值范围[0,1]。 |
| type | [ARBodyLandmarkType](arengine-api-arengine.md#arbodylandmarktype) | 否 | 否 | 骨骼关键点点类型。 |
| isValid | boolean | 否 | 否 | 骨骼关键点是否有效。true：有效，false：无效。 |

## ARBody

PhoneTabletTV

用于人体跟踪时返回跟踪结果，包含人体骨骼关键点数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trackId | number | 是 | 否 | 表示当前人体骨骼关键点ID。 |
| timeStamp | number | 是 | 否 | 当前帧的时间戳，单位ns |

### ARBody.getLandmarks2D

PhoneTabletTV

getLandmarks2D(): Array<ARBodyLandmark2D>

获取人体骨骼关键点信息，包括关键点坐标、类型、置信度等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARBodyLandmark2D](arengine-api-arengine.md#arbodylandmark2d)> | 返回人体骨骼关键点信息数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. const frame: arEngine.ARFrame = arSession.getFrame();
5. const arbodys: arEngine.ARBody[] = frame.acquireBodySkeleton();
6. if (arbodys.length > 0) {
7. arbodys[0].getLandmarks2D();
8. }
```

## ARFrame

PhoneTabletTV

AR Engine处理的一帧数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 是 | 否 | 表示当前帧的时间戳。  以ns为单位。 |
| pointCloud | [ARPointCloud](arengine-api-arengine.md#arpointcloud) | 是 | 否 | 表示当前帧中可追踪的3D点云集合。 |

### ARFrame.getCamera

PhoneTabletTV

getCamera(): ARCamera

获取当前帧的相机对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARCamera](arengine-api-arengine.md#arcamera) | 返回当前帧的相机对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.getCamera();
```

### ARFrame.getUpdatedTrackables

PhoneTabletTV

getUpdatedTrackables(type: ARTrackableType): Array<ARTrackable>

获取更新后的指定类型的可追踪对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | [ARTrackableType](arengine-api-arengine.md#artrackabletype) | 是 | 可追踪对象类型。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARTrackable](arengine-api-arengine.md#artrackable)> | 返回一个可追踪对象组成的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.getUpdatedTrackables(arEngine.ARTrackableType.BASE);
```

### ARFrame.hitTest

PhoneTabletTV

hitTest(x: number, y: number): Array<ARHitResult>

根据相机投射光线，获取预览区域中的像素坐标（pixelX和pixelY）来确定射线方向，然后检测这个射线在平面或点云中是否有交点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| x | number | 是 | 表示预览区域中的像素的X坐标。  该值由设备显示分辨率大小确定。 |
| y | number | 是 | 表示预览区域中的像素的Y坐标。  该值由设备显示分辨率大小确定。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARHitResult](arengine-api-arengine.md#arhitresult)> | 返回一个命中检测结果对象组成的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |
| 1009200008 | Resource exhausted. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.hitTest(0, 0);
```

### ARFrame.acquireSceneMesh

PhoneTabletTV

acquireSceneMesh(): ARSceneMesh

获取当前帧的场景网格数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARSceneMesh](arengine-api-arengine.md#arscenemesh) | 返回环境网格数据的集合。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200008 | Resource exhausted. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.acquireSceneMesh();
```

### ARFrame.acquireDepthImage16Bits

PhoneTabletTV

acquireDepthImage16Bits(): ARImage

获取当前帧对应的深度图像对象。

深度图像是索引0处的单个16位平面。每个像素包含到相机平面的距离，以mm为单位，可表示的深度范围在0mm~65535mm之间，即约65m。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARImage](arengine-api-arengine.md#arimage) | 返回相机视频流帧对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.acquireDepthImage16Bits();
```

### ARFrame.acquireDepthConfidenceImage

PhoneTabletTV

acquireDepthConfidenceImage(): ARImage

获取当前帧的深度置信度图像。

置信度值为0、1和2，0表示估计深度值的置信度最低，1表示估计深度值置信度中等，2表示估计深度值置信度最高，深度置信度图像的宽高与深度图像一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARImage](arengine-api-arengine.md#arimage) | 返回相机视频流帧对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.acquireDepthConfidenceImage();
```

### ARFrame.acquireSemanticDense

PhoneTabletTV

acquireSemanticDense(): ARSemanticDenseData

获取高精几何重建对象数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARSemanticDenseData](arengine-api-arengine.md#arsemanticdensedata) | 返回当前帧的高精几何重建对象数据。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.acquireSemanticDense();
```

### ARFrame.acquireBodySkeleton

PhoneTabletTV

acquireBodySkeleton(): Array<ARBody>

获取人体对象，该对象包含人体骨骼关键点信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARBody](arengine-api-arengine.md#arbody)> | 返回人体对象组成的数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. frame.acquireBodySkeleton();
```

### ARFrame.release

PhoneTabletTV

release(): Promise<void>

释放帧数据对象[ARFrame](arengine-api-arengine.md#arframe)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. await frame.release();
```

## ARGeometry

PhoneTabletTV

用于描述人脸拓扑结构，即人脸Mesh。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verticesSize | number | 是 | 否 | 表示顶点数组的大小。 |
| triangleIndicesCount | number | 是 | 否 | 表示三角形索引的数量。 |
| texCoordSize | number | 是 | 否 | 表示纹理坐标数组的大小。 |
| indicesSize | number | 是 | 否 | 表示索引数组的大小。 |
| triangleLabelsSize | number | 是 | 否 | 表示三角形标签数组的大小。 |

### ARGeometry.getVertices

PhoneTabletTV

getVertices(): ArrayBuffer

获取人脸Mesh顶点数组。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 人脸Mesh顶点数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceGeometry: arEngine.ARGeometry = face.getGeometry();
7. faceGeometry.getVertices();
```

### ARGeometry.getTexCoord

PhoneTabletTV

getTexCoord(): ArrayBuffer

获取人脸Mesh纹理坐标点数组。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 人脸Mesh纹理坐标点数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceGeometry: arEngine.ARGeometry = face.getGeometry();
7. faceGeometry.getTexCoord();
```

### ARGeometry.getIndices

PhoneTabletTV

getIndices(): ArrayBuffer

获取人脸Mesh三角面下标数组

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 人脸Mesh三角面下标数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceGeometry: arEngine.ARGeometry = face.getGeometry();
7. faceGeometry.getIndices();
```

### ARGeometry.getTriangleLabels

PhoneTabletTV

getTriangleLabels(): ArrayBuffer

获取人脸Mesh三角面标签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 人脸Mesh三角面标签。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceGeometry: arEngine.ARGeometry = face.getGeometry();
7. faceGeometry.getTriangleLabels();
```

### ARGeometry.release

PhoneTabletTV

release(): Promise<void>

释放[ARGeometry](arengine-api-arengine.md#argeometry)对象。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = session.getAllTrackables(arEngine.ARTrackableType.FACE);
5. let face: arEngine.ARFace = trackables[0] as arEngine.ARFace;
6. let faceGeometry: arEngine.ARGeometry = face.getGeometry();
7. await faceGeometry.release();
```

## ARHitResult

PhoneTabletTV

命中检测结果对象，描述单个可跟踪对象的命中检测结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| distance | number | 是 | 否 | 从相机到命中位置的距离，单位为m，其值范围0~65535。 |

### ARHitResult.getHitPose

PhoneTabletTV

getHitPose(): ARPose

获取交点位姿。

位姿信息可参考[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。

如果[ARPointOrientationMode](arengine-api-arengine.md#arpointorientationmode)是ESTIMATED\_SURFACE\_NORMAL，则 X+ 是射线的垂直向量，也就是平面的平行向量，Y+ 是平面的法向量，Z+ 是平面的平行向量，大致指向相机。

如果[ARPointOrientationMode](arengine-api-arengine.md#arpointorientationmode)是INITIALIZED\_TO\_IDENTITY，则坐标的旋转不会随着平面的角度变化而变化。X+ 是射线的垂直向量，指向右侧（从设备的视角），Y+ 指向上方，Z+ 大致指向相机。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPose](arengine-api-arengine.md#arpose) | 返回一个位姿对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
6. hitResult[0].getHitPose();
```

### ARHitResult.getTrackable

PhoneTabletTV

getTrackable(): ARTrackable

获取被命中的可追踪对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARTrackable](arengine-api-arengine.md#artrackable) | 返回可被追踪的对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
6. hitResult[0].getTrackable();
```

### ARHitResult.createAnchor

PhoneTabletTV

createAnchor(): ARAnchor

在交点（intersection）处创建一个锚点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARAnchor](arengine-api-arengine.md#aranchor) | 返回一个锚点对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
6. hitResult[0].createAnchor();
```

### ARHitResult.release

PhoneTabletTV

release(): Promise<void>

释放命中检测结果对象[ARHitResult](arengine-api-arengine.md#arhitresult)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
6. await hitResult[0].release();
```

## ARImage

PhoneTabletTV

相机视频流帧对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| format | [ARImageFormat](arengine-api-arengine.md#arimageformat) | 是 | 否 | 图像数据格式。 |
| width | number | 是 | 否 | 当前帧的图像宽度，以Pixel为单位。其数值范围与设备相机像素有关。 |
| height | number | 是 | 否 | 当前帧的图像高度，以Pixel为单位。其数值范围与设备相机像素有关。 |
| imageTimestamp | number | 是 | 否 | 图像的时间戳，以ns为单位。 |
| planes | Array<[ImageComponent](arengine-api-arengine.md#imagecomponent)> | 是 | 否 | 图像组件的基本结构参数列表。 |

### ARImage.release

PhoneTabletTV

release(): Promise<void>

释放相机视频流帧对象[ARImage](arengine-api-arengine.md#arimage)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let image: arEngine.ARImage = frame.acquireDepthImage16Bits();
6. await image.release();
```

## ARPlane

PhoneTabletTV

平面对象，描述被检测到的可跟踪平面信息。

这个类继承自[ARTrackable](arengine-api-arengine.md#artrackable)类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| planeType | [ARPlaneType](arengine-api-arengine.md#arplanetype) | 否 | 否 | 平面类型。 |
| extendX | number | 否 | 否 | 平面边界矩形沿平面局部坐标系X轴的长度，以m为单位，数值范围无限制。 |
| extendZ | number | 否 | 否 | 平面边界矩形沿平面局部坐标系Z轴的长度，以m为单位，数值范围无限制。 |
| label | [ARSemanticPlaneLabel](arengine-api-arengine.md#arsemanticplanelabel) | 否 | 否 | 当前平面识别到的语义类型。 |

### ARPlane.getPolygonXZ

PhoneTabletTV

getPolygonXZ(): ArrayBuffer

获取检测到的平面2D顶点数组。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 返回一个ArrayBuffer缓冲区对象，这个对象包含顶点坐标的数组。表示平面局部坐标系X-Z平面的坐标。  **说明：** 该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
5. let plane = trackables[0] as arEngine.ARPlane;
6. plane.getPolygonXZ();
```

### ARPlane.getSubsumedBy

PhoneTabletTV

getSubsumedBy(): ARPlane

获取平面的父平面（当平面与另一个平面合并时会生成父平面）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPlane](arengine-api-arengine.md#arplane) | 返回一个平面对象，表示父平面。如果没有父平面，将返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
5. let plane: arEngine.ARPlane = trackables[0] as arEngine.ARPlane;
6. plane.getSubsumedBy();
```

### ARPlane.isPoseInExtents

PhoneTabletTV

isPoseInExtents(pose: ARPose): boolean

检查给定位姿是否在平面的边界矩形内。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| pose | [ARPose](arengine-api-arengine.md#arpose) | 是 | 位姿对象。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 返回true表示位姿在平面的边界矩形内，false表示位姿不在平面的边界矩形内。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
5. let pose: arEngine.ARPose = trackables[0].getPose();
6. let plane: arEngine.ARPlane = trackables[0] as arEngine.ARPlane;
7. plane.isPoseInExtents(pose);
```

### ARPlane.isPoseInPolygon

PhoneTabletTV

isPoseInPolygon(pose: ARPose): boolean

检查给定位姿是否在平面的边界多边形内。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| pose | [ARPose](arengine-api-arengine.md#arpose) | 是 | 位姿对象。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 返回true表示位姿在平面的边界多边形内，false表示位姿不在平面的边界多边形内。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
5. let pose: arEngine.ARPose = trackables[0].getPose();
6. let plane: arEngine.ARPlane = trackables[0] as arEngine.ARPlane;
7. plane.isPoseInPolygon(pose);
```

## ARPlaneAnchor

PhoneTabletTV

一个平面类型的锚点对象。

这个类继承自[ARAnchor](arengine-api-arengine.md#aranchor)类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

### ARPlaneAnchor.getPlane

PhoneTabletTV

getPlane(): ARPlane

获取平面。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPlane](arengine-api-arengine.md#arplane) | 返回平面对象，描述被检测到的可跟踪平面信息。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';
3. // 该方法在ARViewCallback中使用
4. async onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): Promise<void> {
5. let planeAnchor: arEngine.ARPlaneAnchor = anchor as arEngine.ARPlaneAnchor;
6. let plane: arEngine.ARPlane = planeAnchor.getPlane();
7. await plane.release();
8. }
```

## ARPoint

PhoneTabletTV

可被追踪的3D点云对象。

这个类继承自[ARTrackable](arengine-api-arengine.md#artrackable)类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| orientationMode | [ARPointOrientationMode](arengine-api-arengine.md#arpointorientationmode) | 是 | 否 | 朝向模式。 |

## ARPose

PhoneTabletTV

位姿对象。

代表从一个坐标系到另一个坐标系的不可改变刚性变换，如平移或旋转。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rotation | [Quaternion](js-apis-inner-scene-types.md#quaternion) | 是 | 否 | 来自位姿对象的姿势数据，包括旋转分量。 |
| translation | [Vec3](js-apis-inner-scene-types.md#vec3) | 是 | 否 | 来自位姿对象的姿势数据，包括平移组件。 |

### ARPose.getMatrix

PhoneTabletTV

getMatrix(): Matrix4

将位姿数据转换为一个4x4的矩阵。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [Matrix4](js-apis-arkui-graphics.md#matrix4) | 返回一个包含16个浮点数的数组，按照列主序（column-major order）存储。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let camera: arEngine.ARCamera = frame.getCamera();
6. let pose: arEngine.ARPose = camera.getPose();
7. pose.getMatrix();
```

### ARPose.release

PhoneTabletTV

release(): Promise<void>

释放位姿对象[ARPose](arengine-api-arengine.md#arpose)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let camera: arEngine.ARCamera = frame.getCamera();
6. let pose: arEngine.ARPose = camera.getPose();
7. await pose.release();
```

## ARSceneMesh

PhoneTabletTV

环境网格数据集合。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verticesSize | number | 是 | 否 | 场景网格中的顶点数量。  最小为0，无上限。 |
| triangleIndicesSize | number | 是 | 否 | 场景网格中的三角形索引数量。最小为0，无上限。 |

### ARSceneMesh.getVertices

PhoneTabletTV

getVertices(): ArrayBuffer

获取场景网格中的顶点坐标数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 返回一个ArrayBuffer缓冲区对象。这个缓冲区包含了顶点在平面局部坐标系X-Z平面的坐标。  **说明：** 该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
6. sceneMesh.getVertices();
```

### ARSceneMesh.getVertexNormals

PhoneTabletTV

getVertexNormals(): ArrayBuffer

获取场景网格中的顶点法线坐标数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 返回一个ArrayBuffer缓冲区对象。这个缓冲区包含了顶点在平面局部坐标系X-Z平面的坐标。  **说明：** 该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
6. sceneMesh.getVertexNormals();
```

### ARSceneMesh.getTriangleIndices

PhoneTabletTV

getTriangleIndices(): ArrayBuffer

获取场景网格中的三角形索引数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| ArrayBuffer | 返回一个ArrayBuffer缓冲区对象。这个缓冲区包含了顶点在平面局部坐标系X-Z平面的坐标。  **说明：** 该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](../harmonyos-guides/arengine-arraybuffer-info.md)。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
6. sceneMesh.getTriangleIndices();
```

### ARSceneMesh.release

PhoneTabletTV

release(): Promise<void>

释放环境网格数据对象[ARSceneMesh](arengine-api-arengine.md#arscenemesh)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
6. await sceneMesh.release();
```

## ARSemanticDenseData

PhoneTabletTV

表示高精几何重建对象数据的集合。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 是 | 否 | 高精几何重建对象数据的时间戳。以ns为单位。 |
| pointDataSize | number | 是 | 否 | 高精几何重建对象数据中稠密点云数量的大小。最小为0，最大为10000。 |
| cubeDataSize | number | 是 | 否 | 高精几何重建对象数据中立方体数量的大小。最小为0，最大为1。 |

### ARSemanticDenseData.acquirePointData

PhoneTabletTV

acquirePointData(): ARSemanticDensePointData

高精几何重建对象数据中稠密点云数据信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARSemanticDensePointData](arengine-api-arengine.md#arsemanticdensepointdata) | 返回所有高精几何重建对象数据中稠密点云数据信息。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
6. semanticData.acquirePointData();
```

### ARSemanticDenseData.acquireCubeData

PhoneTabletTV

acquireCubeData(): Array<ARSemanticDenseCubeData>

高精几何重建对象数据中立方体数据信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARSemanticDenseCubeData](arengine-api-arengine.md#arsemanticdensecubedata)> | 返回一个高精几何重建对象数据的立方体数据信息的列表。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
6. semanticData.acquireCubeData();
```

### ARSemanticDenseData.release

PhoneTabletTV

release(): Promise<void>

释放高精几何重建对象数据[ARSemanticDenseData](arengine-api-arengine.md#arsemanticdensedata)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.0.0(20)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let frame: arEngine.ARFrame = arSession.getFrame();
5. let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
6. await semanticData.release();
```

## ARTrackable

PhoneTabletTV

可追踪的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ARTrackableType](arengine-api-arengine.md#artrackabletype) | 是 | 否 | 可追踪对象类型。 |
| state | [ARTrackingState](arengine-api-arengine.md#artrackingstate) | 是 | 否 | 可追踪对象的追踪状态。 |

### ARTrackable.getPose

PhoneTabletTV

getPose(): ARPose

获取追踪对象的位姿信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPose](arengine-api-arengine.md#arpose) | 返回可追踪对象的位姿信息。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
5. trackables[0].getPose();
```

### ARTrackable.getAnchors

PhoneTabletTV

getAnchors(): Array<ARAnchor>

获取可跟踪对象的锚点信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[ARAnchor](arengine-api-arengine.md#aranchor)> | 返回一个锚点对象组成的数组。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
5. trackables[0].getAnchors();
```

### ARTrackable.createAnchor

PhoneTabletTV

createAnchor(pose: ARPose): ARAnchor

使用可追踪对象的位姿信息创建一个锚点对象。这个锚点将与当前可追踪对象绑定。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| pose | [ARPose](arengine-api-arengine.md#arpose) | 是 | 位姿对象。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARAnchor](arengine-api-arengine.md#aranchor) | 返回一个锚点对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
5. let pose: arEngine.ARPose = trackables[0].getPose();
6. trackables[0].createAnchor(pose);
```

### ARTrackable.release

PhoneTabletTV

release(): Promise<void>

释放被追踪对象[ARTrackable](arengine-api-arengine.md#artrackable)占用的内存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. // arSession创建参考ARSession.getFrame接口示例代码
4. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
5. await trackables[0].release();
```

## arEngine.createARAugmentedImageDatabase

PhoneTabletTV

createARAugmentedImageDatabase(): Promise<ARAugmentedImageDatabase>

创建一个增强型图像数据库。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ARAugmentedImageDatabase](arengine-api-arengine.md#araugmentedimagedatabase)> | Promise对象，返回ARAugmentedImageDatabase对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine } from '@kit.AREngine';

3. await arEngine.createARAugmentedImageDatabase();
```

## arEngine.createARPose

PhoneTabletTV

createARPose(rotation: Quaternion, translation: Vec3): ARPose

在AR Engine中创建和初始化一个新的[ARPose](arengine-api-arengine.md#arpose)对象并返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | [Quaternion](js-apis-inner-scene-types.md#quaternion) | 是 | 表示旋转组件的数据。这个参数是Quaternion类型，通常是一个包含四个元素的数组，为四元数，用于表示和操作3D旋转。 |
| translation | [Vec3](js-apis-inner-scene-types.md#vec3) | 是 | 表示平移组件的数据。这个参数是Vec3类型，通常是一个包含三个元素的数组，表示3D向量的x、y和z分量，用于表示物体的平移位置。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [ARPose](arengine-api-arengine.md#arpose) | 返回创建的位姿对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters, for example, the input parameter is empty or invalid. |
| 1009200001 | Failure. |

**示例：**

```
1. import { Quaternion, Vec3 } from '@kit.ArkGraphics3D';
2. import { arEngine } from '@kit.AREngine';

4. let r: Quaternion = {
5. x: 0,
6. y: 0,
7. z: 0,
8. w: 0
9. };
10. let t: Vec3 = { x: 0, y: 0, z: 0 };
11. arEngine.createARPose(r, t);
```
