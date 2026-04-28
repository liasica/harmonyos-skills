---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatial-recon-interface-h
title: spatial_recon_interface.h
breadcrumb: API参考 > 图形 > Spatial Recon Kit（空间建模服务） > C API > 头文件 > spatial_recon_interface.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0f1088c73a425ab7dada90dce53f50892c8c84598c5db01eab7df3199855edb
---

## 概述

3D空间重建任务设计模块，通过处理多视角图像输入来生成立体场景。

**引用文件：** <SpatialReconKit/spatial\_recon\_interface.h>

**库：** libspatial\_recon\_ndk.z.so

**系统能力：** SystemCapability.Graphics.SpatialRecon

**起始版本：** 6.1.0(23)

**相关模块：** [SpatialRecon](capi-spatialrecon.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HMS\_SpatialRecon\_ModelWriteInfo](capi-spatialrecon-hms-spatialrecon-modelwriteinfo.md) | - | 空间重建模型写入的结构体。 |
| [HMS\_SpatialRecon\_DataFrame](capi-spatialrecon-hms-spatialrecon-dataframe.md) | HMS\_SpatialRecon\_DataFrame | 定义HMS（Huawei Mobile Services）空间重建数据帧的结构体，包含用于空间重建的相机内参、姿态信息、时间戳和图像数据。 |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) | HMS\_SpatialRecon\_Session | 定义用于空间重建会话句柄的结构体，用于3D场景重建。 |
| [AREngine\_ARSession](capi-spatialrecon-arengine-arsession.md) | AREngine\_ARSession | 表示华为AR Engine中AR会话的不透明句柄。 |
| [AREngine\_ARFrame](capi-spatialrecon-arengine-arframe.md) | AREngine\_ARFrame | 定义一个结构体，用于存储AR Engine中捕获的单帧AR图像数据，包含特定时间戳下的相机图像、追踪状态、锚点及AR相关信息。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus | 表示空间重建操作状态的枚举。 |
| [HMS\_SpatialReconOutputFormat](capi-spatial-recon-interface-h.md#hms_spatialreconoutputformat) | HMS\_SpatialReconOutputFormat | 定义空间重建模型输出格式的枚举。 |
| [HMS\_SpatialReconRunningMode](capi-spatial-recon-interface-h.md#hms_spatialreconrunningmode) | HMS\_SpatialReconRunningMode | 空间重建运行模式类型。 |
| [HMS\_SpatialReconStage](capi-spatial-recon-interface-h.md#hms_spatialreconstage) | HMS\_SpatialReconStage | 3D重建流水线中的某特定阶段。此枚举定义了空间重建过程中从初始化到完成或终止的所有可能状态。 |
| [HMS\_SpatialReconModelType](capi-spatial-recon-interface-h.md#hms_spatialreconmodeltype) | HMS\_SpatialReconModelType | 空间重建模型类型的枚举。目前仅支持3DGS（3D Gaussian Splatting）模型类型。 |
| [HMS\_SpatialReconImageDataFormat](capi-spatial-recon-interface-h.md#hms_spatialreconimagedataformat) | HMS\_SpatialReconImageDataFormat | 空间重建图像数据格式。定义用于空间重建的图像数据格式的枚举，当前仅支持RGB格式。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*HMS\_SpatialReconCallbackFunc)(HMS\_SpatialReconStatus)](capi-spatial-recon-interface-h.md#hms_spatialreconcallbackfunc) | HMS\_SpatialReconCallbackFunc | 用于处理空间重建状态更新的回调函数类型定义。当系统提供关于空间重建过程的更新时，会调用此回调。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_IsSupport(HMS\_SpatialReconModelType type)](capi-spatial-recon-interface-h.md#hms_spatialrecon_issupport) | - | 查询当前设备是否支持指定的空间重建模型类型。该函数检查设备使用给定模型类型执行空间重建的能力。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_CreateSession(HMS\_SpatialReconModelType type, const char\* workPath, HMS\_SpatialRecon\_Session \*\*outSpatialReconSession)](capi-spatial-recon-interface-h.md#hms_spatialrecon_createsession) | - | 创建一个新的空间重建会话。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_DestroySession(HMS\_SpatialRecon\_Session \*spatialReconSession)](capi-spatial-recon-interface-h.md#hms_spatialrecon_destroysession) | - | 销毁一个空间重建会话并释放其资源。该函数终止空间重建会话并释放与其关联的所有内存和系统资源。调用此函数后，提供的会话指针将失效，不应再次使用。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_PushFrame(HMS\_SpatialRecon\_Session \*spatialReconSession, HMS\_SpatialRecon\_DataFrame \*inputFrame)](capi-spatial-recon-interface-h.md#hms_spatialrecon_pushframe) | - | 将空间重建数据帧推送到空间重建会话中进行处理。该函数将捕获的空间数据帧提交到重建会话中进行处理。会话使用此数据更新或完善其内部空间模型。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_PushARFrame(HMS\_SpatialRecon\_Session spatialReconSession, AREngine\_ARSession arSession, AREngine\_ARFrame \*arFrame)](capi-spatial-recon-interface-h.md#hms_spatialrecon_pusharframe) | - | 将AREngine会话中的AREngine帧推送到空间重建会话中。该函数将包含摄像头图像、姿态和AR跟踪数据的AREngine帧提交到空间重建会话中。它允许重建系统利用实时的AR跟踪信息（如摄像头姿态、特征点）来提升空间映射效果。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_StartSession(HMS\_SpatialRecon\_Session spatialReconSession, HMS\_SpatialRecon\_ModelWriteInfo writeInfo, HMS\_SpatialReconCallbackFunc onSpatialReconFinished)](capi-spatial-recon-interface-h.md#hms_spatialrecon_startsession) | - | 启动空间重建会话。该操作是异步执行的，完成状态通过回调函数报告。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_SetRunningMode(HMS\_SpatialRecon\_Session \*spatialReconSession, HMS\_SpatialReconRunningMode runningMode)](capi-spatial-recon-interface-h.md#hms_spatialrecon_setrunningmode) | - | 设置空间重建会话的运行模式。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_PauseSession(HMS\_SpatialRecon\_Session \*spatialReconSession)](capi-spatial-recon-interface-h.md#hms_spatialrecon_pausesession) | - | 暂停一个正在进行的空间重建会话。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_ResumeSession(HMS\_SpatialRecon\_Session \*spatialReconSession)](capi-spatial-recon-interface-h.md#hms_spatialrecon_resumesession) | - | 恢复一个被暂停的空间重建会话。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_GetProgress(HMS\_SpatialRecon\_Session spatialReconSession, float progress, HMS\_SpatialReconStage\* stage)](capi-spatial-recon-interface-h.md#hms_spatialrecon_getprogress) | - | 获取当前任务的进度。该函数查询正在进行的任务（即重建或保存）的进度比例，并通过指针变量返回结果。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_GetRefinedFrame(HMS\_SpatialRecon\_Session \*spatialReconSession, int iFrame, HMS\_SpatialRecon\_DataFrame \*outFrame)](capi-spatial-recon-interface-h.md#hms_spatialrecon_getrefinedframe) | - | 从空间重建会话中获取优化后的相机帧。该函数为指定帧索引提供经过重建处理后的优化相机内外参数。 |
| [HMS\_SpatialReconStatus HMS\_SpatialRecon\_SaveResultToFile(HMS\_SpatialRecon\_Session \*spatialReconSession, HMS\_SpatialRecon\_ModelWriteInfo \*writeInfo, HMS\_SpatialReconCallbackFunc onSaved)](capi-spatial-recon-interface-h.md#hms_spatialrecon_saveresulttofile) | - | 将空间重建结果保存到文件。该函数将处理后的空间重建数据导出到指定的文件格式。操作是异步执行的，完成状态通过回调函数报告。 |

## 枚举类型说明

### HMS\_SpatialReconStatus

```
1. enum HMS_SpatialReconStatus
```

**描述**

表示空间重建操作状态的枚举。

**起始版本：** 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL\_RECON\_STATUS\_SUCCESS = 0 | 空间重建成功。 |
| SPATIAL\_RECON\_STATUS\_EXCEEDS\_MAXIMUM = 1023700001 | 超过最大空间重建帧数。 |
| SPATIAL\_RECON\_STATUS\_DEVICE\_NOT\_SUPPORT = 801 | 当前设备不支持空间重建。 |
| SPATIAL\_RECON\_STATUS\_INVALID\_WORK\_PATH = 1023700002 | 输入的工作路径无效。 |
| SPATIAL\_RECON\_STATUS\_INVALID\_FRAME\_DATA = 1023700003 | 输入的帧数据无效。 |
| SPATIAL\_RECON\_STATUS\_STAGE\_NOT\_INITIALIZED = 1023700004 | 会话未初始化。 |
| SPATIAL\_RECON\_STATUS\_STAGE\_BUILDING = 1023700005 | 重建会话已开始。 |
| SPATIAL\_RECON\_STATUS\_STAGE\_NOT\_FINISHED = 1023700006 | 重建会话未完成。 |
| SPATIAL\_RECON\_STATUS\_FAILED = 1023700007 | 空间重建失败。 |

### HMS\_SpatialReconOutputFormat

```
1. enum HMS_SpatialReconOutputFormat
```

**描述**

定义空间重建模型输出格式的枚举。

**起始版本：** 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL\_RECON\_OUTPUT\_FORMAT\_PLY | PLY格式。 |
| SPATIAL\_RECON\_OUTPUT\_FORMAT\_MP4 | MPEG-4视频格式。 |

### HMS\_SpatialReconRunningMode

```
1. enum HMS_SpatialReconRunningMode
```

**描述**

空间重建运行模式类型。

说明

SpatialRecon会话支持前台和后台两种运行模式。当应用切换到后台或返回前台时，需要调用HMS\_SpatialReconRunningMode，允许系统针对每种运行模式优化功耗。

**起始版本：** 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL\_RECON\_RUNNING\_FOREGROUND\_MODE | 默认前台模式。当空间重建在前台执行时，系统会分配更多资源给重建任务，以确保更快的重建速度。 |
| SPATIAL\_RECON\_RUNNING\_BACKGROUND\_MODE | 后台模式。当空间重建在后台运行时，系统会优先处理前台应用的操作，重建速度相对较慢。 |

### HMS\_SpatialReconStage

```
1. enum HMS_SpatialReconStage
```

**描述**

3D重建流水线中的某特定阶段。此枚举定义了空间重建过程中从初始化到完成或终止的所有可能状态。

**起始版本：** 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL\_RECON\_STAGE\_INIT | 初始化阶段：正在准备资源和环境。 |
| SPATIAL\_RECON\_STAGE\_BUILDING | 重建阶段：正在处理数据并构建3D模型。 |
| SPATIAL\_RECON\_STAGE\_PAUSED | 重建过程已暂停。 |
| SPATIAL\_RECON\_STAGE\_FINISHED | 重建成功完成。 |
| SPATIAL\_RECON\_STAGE\_SAVING | 保存阶段：3D模型正被保存为文件。 |
| SPATIAL\_RECON\_STAGE\_UNKNOWN | 阶段未知或不确定。 |

### HMS\_SpatialReconModelType

```
1. enum HMS_SpatialReconModelType
```

**描述**

空间重建模型类型的枚举。目前仅支持3DGS（3D Gaussian Splatting）模型类型。

**起始版本：** 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL\_RECON\_MODEL\_TYPE\_GS | 用于场景重建的3DGS模型。 |

### HMS\_SpatialReconImageDataFormat

```
1. enum HMS_SpatialReconImageDataFormat
```

**描述**

空间重建图像数据格式。定义用于空间重建的图像数据格式的枚举，当前仅支持RGB格式。

**起始版本：** 6.1.0(23)

| 枚举项 | 描述 |
| --- | --- |
| SPATIAL\_RECON\_IMAGEDATA\_FORMAT\_RGB | RGB格式，一种基于红、绿、蓝的三通道色彩表示方法。 |

## 函数说明

### HMS\_SpatialReconCallbackFunc()

```
1. typedef void (*HMS_SpatialReconCallbackFunc)(HMS_SpatialReconStatus)
```

**描述**

用于处理空间重建状态更新的回调函数类型定义。当系统提供关于空间重建过程的更新时，会调用此回调。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | 空间重建过程的当前状态。HMS\_SpatialReconStatus用于标识重建结果的状态。 |

### HMS\_SpatialRecon\_IsSupport()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_IsSupport(HMS_SpatialReconModelType type)
```

**描述**

查询当前设备是否支持指定的空间重建模型类型。该函数检查设备使用给定模型类型执行空间重建的能力。

说明

支持状态可能因设备硬件、系统版本或当前环境条件而异。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialReconModelType](capi-spatial-recon-interface-h.md#hms_spatialreconmodeltype) type | 要检查支持性的空间重建模型类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus用于指示是否支持该模型类型。 |

### HMS\_SpatialRecon\_CreateSession()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_CreateSession(HMS_SpatialReconModelType type, const char* workPath, HMS_SpatialRecon_Session **outSpatialReconSession)
```

**描述**

创建一个新的空间重建会话。

说明

在不支持的设备上，会话对象将无法成功创建，函数将返回错误。可以先调用HMS\_SpatialRecon\_IsSupport来确认当前设备是否支持此能力。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialReconModelType](capi-spatial-recon-interface-h.md#hms_spatialreconmodeltype) type | 要使用的重建模型类型。这决定了重建会话的算法和能力。 |
| const char\* workPath | 文件系统路径，用于存储重建数据和临时文件，必须为已存在的目录。 |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*\*outSpatialReconSession | 输出参数，接收指向新创建的空间重建会话对象的指针。调用方负责管理此对象的生命周期，并且最终必须使用适当的清理函数销毁它。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus指示操作结果。 |

### HMS\_SpatialRecon\_DestroySession()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_DestroySession(HMS_SpatialRecon_Session *spatialReconSession)
```

**描述**

销毁一个空间重建会话并释放其资源。该函数终止空间重建会话并释放与其关联的所有内存和系统资源。调用此函数后，提供的会话指针将失效，不应再次使用。

注意

一旦销毁会话，将无法恢复。所有未保存的重建数据将会丢失。如果需要数据持久化，请在销毁前调用HMS\_SpatialRecon\_SaveResultToFile()进行保存。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向要销毁的空间重建会话的指针。该会话必须是先前创建的，如果为NULL，则函数无效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus表示操作的结果。 |

### HMS\_SpatialRecon\_PushFrame()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_PushFrame(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_DataFrame *inputFrame)
```

**描述**

将空间重建数据帧推送到空间重建会话中进行处理。该函数将捕获的空间数据帧提交到重建会话中进行处理。会话使用此数据更新或完善其内部空间模型。

说明

如果调用HMS\_SpatialRecon\_StartSession启动建模过程，则帧数据将无法成功推送。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。 |
| [HMS\_SpatialRecon\_DataFrame](capi-spatialrecon-hms-spatialrecon-dataframe.md) \*inputFrame | 指向包含传感器数据的空间重建数据帧的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | 状态码，表示操作的结果。 |

### HMS\_SpatialRecon\_PushARFrame()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_PushARFrame(HMS_SpatialRecon_Session *spatialReconSession, AREngine_ARSession* arSession, AREngine_ARFrame *arFrame)
```

**描述**

将AREngine会话中的AREngine帧推送到空间重建会话中。该函数将包含摄像头图像、姿态和AR跟踪数据的AREngine帧提交到空间重建会话中。它允许重建系统利用实时的AR跟踪信息（如摄像头姿态、特征点）来提升空间映射效果。

说明

如果调用HMS\_SpatialRecon\_StartSession启动建模过程，则帧数据将无法成功推送。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。 |
| [AREngine\_ARSession](capi-spatialrecon-arengine-arsession.md)\* arSession | 指向生成AREngine帧的AREngine会话的指针。 |
| [AREngine\_ARFrame](capi-spatialrecon-arengine-arframe.md) \*arFrame | 指向包含AR跟踪数据和摄像头图像的AREngine帧的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | 状态码，表示操作的结果。 |

### HMS\_SpatialRecon\_StartSession()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_StartSession(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_ModelWriteInfo* writeInfo, HMS_SpatialReconCallbackFunc onSpatialReconFinished)
```

**描述**

启动空间重建会话。该操作是异步执行的，完成状态通过回调函数报告。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。如果spatialReconSession为空，则函数将返回错误码。 |
| [HMS\_SpatialRecon\_ModelWriteInfo](capi-spatialrecon-hms-spatialrecon-modelwriteinfo.md)\* writeInfo | 指向模型写入配置信息的指针。包含保存重建输出的参数。如果writeInfo指针为空，则重建完成后不会执行写入操作，之后可以单独调用HMS\_SpatialRecon\_SaveResultToFile接口。 |
| [HMS\_SpatialReconCallbackFunc](capi-spatial-recon-interface-h.md#hms_spatialreconcallbackfunc) onSpatialReconFinished | 重建过程完成后将被调用的回调函数指针。回调函数可以设为NULL，此时不会触发回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus表示成功或特定错误的状态码。 |

### HMS\_SpatialRecon\_SetRunningMode()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_SetRunningMode(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialReconRunningMode runningMode)
```

**描述**

设置空间重建会话的运行模式。

说明

该函数必须在 HMS\_SpatialRecon\_StartSession() 之后调用，并且在重建完成之前调用。如果在非活动会话期间调用，则不会产生任何效果。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。 |
| [HMS\_SpatialReconRunningMode](capi-spatial-recon-interface-h.md#hms_spatialreconrunningmode) runningMode | 空间重建的期望运行模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus表示成功或特定错误的状态码。 |

### HMS\_SpatialRecon\_PauseSession()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_PauseSession(HMS_SpatialRecon_Session *spatialReconSession)
```

**描述**

暂停一个正在进行的空间重建会话。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | 状态码，表示操作的结果。如果不存在活动会话，则返回错误。 |

### HMS\_SpatialRecon\_ResumeSession()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_ResumeSession(HMS_SpatialRecon_Session *spatialReconSession)
```

**描述**

恢复一个被暂停的空间重建会话。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus表示操作的结果。如果会话未被暂停，则返回错误。 |

### HMS\_SpatialRecon\_GetProgress()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_GetProgress(HMS_SpatialRecon_Session *spatialReconSession, float* progress, HMS_SpatialReconStage* stage)
```

**描述**

获取当前任务的进度。该函数查询正在进行的任务（即重建或保存）的进度比例，并通过指针变量返回结果。

说明

一旦调用HMS\_SpatialRecon\_SaveResultToFile函数，会话将手动开始将3D模型保存到文件。返回的进度值将仅反映文件保存的进度，而不是整个进度。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话实例的指针。 |
| float\* progress | 指向一个浮点变量的指针，用于存储进度比例。该值范围为0.0f（0%）到1.0f（100%）。如果指针为NULL，则函数将返回错误码。 |
| [HMS\_SpatialReconStage](capi-spatial-recon-interface-h.md#hms_spatialreconstage)\* stage | 指向一个阶段变量的指针，用于存储阶段值。如果指针为NULL，则不会写入阶段值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus表示成功或特定错误的状态码。 |

### HMS\_SpatialRecon\_GetRefinedFrame()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_GetRefinedFrame(HMS_SpatialRecon_Session *spatialReconSession, int iFrame, HMS_SpatialRecon_DataFrame *outFrame)
```

**描述**

从空间重建会话中获取优化后的相机帧。该函数为指定帧索引提供经过重建处理后的优化相机内外参数。

说明

该函数不返回图像像素数据，imageData字段将被设置为null。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话句柄的指针。 |
| int iFrame | 要获取的帧的索引（从0开始）。 |
| [HMS\_SpatialRecon\_DataFrame](capi-spatialrecon-hms-spatialrecon-dataframe.md) \*outFrame | 输出参数，存储优化后的帧数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | HMS\_SpatialReconStatus表示操作成功或失败的状态码。 |

### HMS\_SpatialRecon\_SaveResultToFile()

```
1. HMS_SpatialReconStatus HMS_SpatialRecon_SaveResultToFile(HMS_SpatialRecon_Session *spatialReconSession, HMS_SpatialRecon_ModelWriteInfo *writeInfo, HMS_SpatialReconCallbackFunc onSaved)
```

**描述**

将空间重建结果保存到文件。该函数将处理后的空间重建数据导出到指定的文件格式。操作是异步执行的，完成状态通过回调函数报告。

说明

该函数只能在模型成功构建后调用；否则，将返回错误值。

**起始版本：** 6.1.0(23)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_SpatialRecon\_Session](capi-spatialrecon-hms-spatialrecon-session.md) \*spatialReconSession | 指向空间重建会话对象的指针。必须不为 NULL，并且应为有效且活跃的会话。 |
| [HMS\_SpatialRecon\_ModelWriteInfo](capi-spatialrecon-hms-spatialrecon-modelwriteinfo.md) \*writeInfo | 指向包含文件导出参数的结构体指针，如文件路径、格式和可选配置标志。必须不为NULL。 |
| [HMS\_SpatialReconCallbackFunc](capi-spatial-recon-interface-h.md#hms_spatialreconcallbackfunc) onSaved | 保存操作完成后将被调用的回调函数指针。如果不需要回调，可以设为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HMS\_SpatialReconStatus](capi-spatial-recon-interface-h.md#hms_spatialreconstatus) | 返回HMS\_SpatialReconStatus表示初始验证状态或即时错误（例如无效参数）。文件导出的实际结果通过回调函数传递。 |
