---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohscan-h
title: ohscan.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > ohscan.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2c74d986b8b9ded688f6f2398eafa6dc5f408626a268b316df4b5e3052c3ecb7
---

## 概述

声明用于发现和连接扫描仪、从扫描仪扫描图片、获取图片扫描进度和设置扫描仪参数等功能的 API，适用于需要在应用内集成扫描仪相关操作的场景。

**引用文件：** <BasicServicesKit/ohscan.h>

**库：** libohscan.so

**系统能力：** SystemCapability.Print.PrintFramework

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

## 汇总

### 结构体

| 名称 | typedef 关键字 | 描述 |
| --- | --- | --- |
| [Scan\_ScannerDevice](capi-oh-scan-scan-scannerdevice.md) | Scan\_ScannerDevice | 表示扫描仪设备信息 |
| [Scan\_PictureScanProgress](capi-oh-scan-scan-picturescanprogress.md) | Scan\_PictureScanProgress | 表示扫描仪扫描图片的进度 |
| [Scan\_ScannerOptions](capi-oh-scan-scan-scanneroptions.md) | Scan\_ScannerOptions | 表示一个扫描仪的所有参数选项 |

### 枚举

| 名称 | typedef 关键字 | 描述 |
| --- | --- | --- |
| [Scan\_ErrorCode](capi-ohscan-h.md#scan_errorcode) | Scan\_ErrorCode | 定义错误码 |

### 函数

| 名称 | typedef 关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Scan\_ScannerDiscoveryCallback)(Scan\_ScannerDevice\*\* devices, int32\_t deviceCount)](capi-ohscan-h.md#scan_scannerdiscoverycallback) | Scan\_ScannerDiscoveryCallback | 扫描仪设备发现回调，通过[OH\_Scan\_StartScannerDiscovery](capi-ohscan-h.md#oh_scan_startscannerdiscovery)注册。devices 指针指向的内存将在回调函数结束时释放。 |
| [int32\_t OH\_Scan\_Init()](capi-ohscan-h.md#oh_scan_init) | - | 此 API 检查并拉起扫描服务，初始化扫描客户端，并建立与扫描服务的连接。 |
| [int32\_t OH\_Scan\_StartScannerDiscovery(Scan\_ScannerDiscoveryCallback callback)](capi-ohscan-h.md#oh_scan_startscannerdiscovery) | - | 此 API 开始发现扫描仪，注册回调函数处理发现的扫描仪设备。 |
| [int32\_t OH\_Scan\_OpenScanner(const char\* scannerId)](capi-ohscan-h.md#oh_scan_openscanner) | - | 此 API 连接到扫描仪设备。 |
| [int32\_t OH\_Scan\_CloseScanner(const char\* scannerId)](capi-ohscan-h.md#oh_scan_closescanner) | - | 此 API 用于关闭已连接的扫描仪设备。 |
| [Scan\_ScannerOptions\* OH\_Scan\_GetScannerParameter(const char\* scannerId, int32\_t\* errorCode)](capi-ohscan-h.md#oh_scan_getscannerparameter) | - | 此 API 可用于获取扫描仪可设置的选项列表。返回的结构体指针指向的内存会在[OH\_Scan\_Exit](capi-ohscan-h.md#oh_scan_exit)时自动释放，每个扫描仪型号在内存中只会存储一份副本。 |
| [int32\_t OH\_Scan\_SetScannerParameter(const char\* scannerId, const int32\_t option, const char\* value)](capi-ohscan-h.md#oh_scan_setscannerparameter) | - | 此 API 可用于设置扫描仪的某个选项参数。传入的选项和值从[OH\_Scan\_GetScannerParameter](capi-ohscan-h.md#oh_scan_getscannerparameter)获取。 |
| [int32\_t OH\_Scan\_StartScan(const char\* scannerId, bool batchMode)](capi-ohscan-h.md#oh_scan_startscan) | - | 此 API 用于启动扫描仪的扫描任务。 |
| [int32\_t OH\_Scan\_CancelScan(const char\* scannerId)](capi-ohscan-h.md#oh_scan_cancelscan) | - | 此 API 用于取消扫描仪正在进行的扫描任务。 |
| [int32\_t OH\_Scan\_GetPictureScanProgress(const char\* scannerId, Scan\_PictureScanProgress\* prog)](capi-ohscan-h.md#oh_scan_getpicturescanprogress) | - | 此 API 可获取扫描仪扫描图片的进度。prog 参数必须传入非空值，扫描进度将写入 prog 指针指向的结构体。 |
| [int32\_t OH\_Scan\_Exit()](capi-ohscan-h.md#oh_scan_exit) | - | 此 API 可用于退出扫描服务，释放扫描框架内存，并注销扫描仪设备发现回调。 |

## 枚举类型说明

### Scan\_ErrorCode

```cpp
enum Scan_ErrorCode
```

**描述**

定义错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SCAN\_ERROR\_NONE = 0 | 操作成功 |
| SCAN\_ERROR\_NO\_PERMISSION = 201 | 权限验证失败，需申请接口所需权限 |
| SCAN\_ERROR\_INVALID\_PARAMETER = 401 | 参数无效。例如指针为空或字符串为空，请检查传入的参数是否合法 |
| SCAN\_ERROR\_GENERIC\_FAILURE = 24300101 | 通用内部错误，请稍后重试 |
| SCAN\_ERROR\_RPC\_FAILURE = 24300102 | RPC 通信错误，请检查扫描服务状态后重试 |
| SCAN\_ERROR\_SERVER\_FAILURE = 24300103 | 表示扫描过程中发生错误，请稍后重试 |
| SCAN\_ERROR\_UNSUPPORTED = 24300104 | 不支持的操作，请检查当前扫描仪是否支持该操作 |
| SCAN\_ERROR\_CANCELED = 24300105 | 操作已取消，请重新发起扫描 |
| SCAN\_ERROR\_DEVICE\_BUSY = 24300106 | 扫描仪繁忙，请稍后重试 |
| SCAN\_ERROR\_INVALID = 24300107 | 数据无效（包括打开时无设备），请检查扫描仪连接状态 |
| SCAN\_ERROR\_JAMMED = 24300108 | 文档进纸器卡纸，请清除卡纸后重试 |
| SCAN\_ERROR\_NO\_DOCS = 24300109 | 文档进纸器缺纸，请在进纸器中放入文档后重试 |
| SCAN\_ERROR\_COVER\_OPEN = 24300110 | 扫描仪盖板打开，请关闭盖板后重试 |
| SCAN\_ERROR\_IO\_ERROR = 24300111 | 扫描仪 I/O 错误，请检查扫描仪连接并重试 |
| SCAN\_ERROR\_NO\_MEMORY = 24300112 | 内存不足，请释放资源后重试 |

## 函数说明

### Scan\_ScannerDiscoveryCallback()

```cpp
typedef void (*Scan_ScannerDiscoveryCallback)(Scan_ScannerDevice** devices, int32_t deviceCount)
```

**描述**

扫描仪设备发现回调，通过[OH\_Scan\_StartScannerDiscovery](capi-ohscan-h.md#oh_scan_startscannerdiscovery)注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Scan\_ScannerDevice](capi-oh-scan-scan-scannerdevice.md)\*\* devices | 所有发现的扫描仪设备列表，devices 指针指向的内存将在回调函数结束时释放 |
| int32\_t deviceCount | 发现的扫描仪数量 |

### OH\_Scan\_Init()

```cpp
int32_t OH_Scan_Init()
```

**描述**

此 API 检查并拉起扫描服务，初始化扫描客户端，并建立与扫描服务的连接。应先调用此 API 初始化扫描服务，再调用其他扫描 API。在使用完毕后，需调用 [OH\_Scan\_Exit](capi-ohscan-h.md#oh_scan_exit) 释放资源。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描服务成功启动  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误 |

### OH\_Scan\_StartScannerDiscovery()

```cpp
int32_t OH_Scan_StartScannerDiscovery(Scan_ScannerDiscoveryCallback callback)
```

**描述**

此 API 开始发现扫描仪，注册回调函数处理发现的扫描仪设备。注册的回调将在调用 [OH\_Scan\_Exit](capi-ohscan-h.md#oh_scan_exit) 时注销。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Scan\_ScannerDiscoveryCallback](capi-ohscan-h.md#scan_scannerdiscoverycallback) callback | 扫描仪发现事件的[Scan\_ScannerDiscoveryCallback](capi-ohscan-h.md#scan_scannerdiscoverycallback)回调函数，不能为NULL |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示成功开始扫描仪搜索  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误 |

### OH\_Scan\_OpenScanner()

```cpp
int32_t OH_Scan_OpenScanner(const char* scannerId)
```

**描述**

此 API 连接到扫描仪设备。设备使用完毕后，可调用 [OH\_Scan\_CloseScanner](capi-ohscan-h.md#oh_scan_closescanner) 关闭。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 用于连接扫描仪的 ID，取值应为已发现的有效扫描仪设备 ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描仪成功连接  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误  [SCAN\_ERROR\_DEVICE\_BUSY](capi-ohscan-h.md#scan_errorcode) 表示扫描仪繁忙  [SCAN\_ERROR\_INVALID\_PARAMETER](capi-ohscan-h.md#scan_errorcode) 表示输入参数无效  [SCAN\_ERROR\_IO\_ERROR](capi-ohscan-h.md#scan_errorcode) 表示与扫描仪通信时发生错误  [SCAN\_ERROR\_NO\_MEMORY](capi-ohscan-h.md#scan_errorcode) 表示可用内存不足 |

### OH\_Scan\_CloseScanner()

```cpp
int32_t OH_Scan_CloseScanner(const char* scannerId)
```

**描述**

此 API 用于关闭已连接的扫描仪设备。一般在扫描仪使用完毕后调用此 API 关闭连接。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 用于断开扫描仪连接的 ID，取值应为已连接的有效扫描仪设备 ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描仪连接成功关闭  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误  [SCAN\_ERROR\_INVALID\_PARAMETER](capi-ohscan-h.md#scan_errorcode) 表示输入参数无效 |

### OH\_Scan\_GetScannerParameter()

```cpp
Scan_ScannerOptions* OH_Scan_GetScannerParameter(const char* scannerId, int32_t* errorCode)
```

**描述**

此 API 可用于获取扫描仪可设置的选项列表。返回的结构体指针指向的内存会在[OH\_Scan\_Exit](capi-ohscan-h.md#oh_scan_exit)时自动释放，每个扫描仪型号在内存中只会存储一份副本。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 用于获取扫描仪参数的 ID，取值应为已连接的有效扫描仪设备 ID。 |
| int32\_t\* errorCode | 不能为 NULL。如果执行成功，errorCode 返回[SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode)，否则返回特定的错误码，参考[Scan\_ErrorCode](capi-ohscan-h.md#scan_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Scan\_ScannerOptions\*](capi-oh-scan-scan-scanneroptions.md) | 成功时返回扫描仪参数选项结构体指针，可用于获取和设置扫描仪参数选项；失败时返回 NULL。 |

### OH\_Scan\_SetScannerParameter()

```cpp
int32_t OH_Scan_SetScannerParameter(const char* scannerId, const int32_t option, const char* value)
```

**描述**

此 API 可用于设置扫描仪的某个选项参数。传入的选项和值从[OH\_Scan\_GetScannerParameter](capi-ohscan-h.md#oh_scan_getscannerparameter)获取。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 此 ID 用于设置特定扫描仪的选项，取值应为已连接的有效扫描仪设备 ID。 |
| const int32\_t option | 要设置的选项编号。取值范围从0到 optionCount - 1，从[Scan\_ScannerOptions](capi-oh-scan-scan-scanneroptions.md)获取。 |
| const char\* value | 要设置的选项值，有效值从[Scan\_ScannerOptions](capi-oh-scan-scan-scanneroptions.md)的 ranges 中获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描仪参数设置成功  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误  [SCAN\_ERROR\_INVALID\_PARAMETER](capi-ohscan-h.md#scan_errorcode) 表示输入参数无效 |

### OH\_Scan\_StartScan()

```cpp
int32_t OH_Scan_StartScan(const char* scannerId, bool batchMode)
```

**描述**

此 API 用于启动扫描仪的扫描任务。成功初始化扫描服务，并连接扫描仪完成参数设置后，可以调用此 API 开始扫描。扫描过程中可调用 [OH\_Scan\_GetPictureScanProgress](capi-ohscan-h.md#oh_scan_getpicturescanprogress) 获取扫描进度，可调用 [OH\_Scan\_CancelScan](capi-ohscan-h.md#oh_scan_cancelscan) 取消扫描。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 此 ID 用于启动指定扫描仪的扫描任务，取值应为已连接的有效扫描仪设备 ID。 |
| bool batchMode | 是否以批处理模式启动扫描仪。true表示开启批处理模式，扫描仪可连续扫描多页文档（通常经文档进纸器连续进纸）；false表示关闭批处理模式，仅扫描单页。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描仪成功启动扫描任务  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误  [SCAN\_ERROR\_JAMMED](capi-ohscan-h.md#scan_errorcode) 表示文档进纸器卡纸  [SCAN\_ERROR\_NO\_DOCS](capi-ohscan-h.md#scan_errorcode) 表示文档进纸器缺纸  [SCAN\_ERROR\_COVER\_OPEN](capi-ohscan-h.md#scan_errorcode) 表示扫描仪盖板打开  [SCAN\_ERROR\_IO\_ERROR](capi-ohscan-h.md#scan_errorcode) 表示与扫描仪通信时发生错误  [SCAN\_ERROR\_NO\_MEMORY](capi-ohscan-h.md#scan_errorcode) 表示可用内存不足  [SCAN\_ERROR\_INVALID\_PARAMETER](capi-ohscan-h.md#scan_errorcode) 表示输入参数无效  [SCAN\_ERROR\_DEVICE\_BUSY](capi-ohscan-h.md#scan_errorcode) 表示扫描仪繁忙，应稍后重试操作 |

### OH\_Scan\_CancelScan()

```cpp
int32_t OH_Scan_CancelScan(const char* scannerId)
```

**描述**

此 API 用于取消扫描仪正在进行的扫描任务。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 此 ID 用于取消指定扫描仪的扫描任务，取值应为已连接的有效扫描仪设备 ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描仪成功取消扫描任务  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_INVALID\_PARAMETER](capi-ohscan-h.md#scan_errorcode) 表示输入参数无效  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误 |

### OH\_Scan\_GetPictureScanProgress()

```cpp
int32_t OH_Scan_GetPictureScanProgress(const char* scannerId, Scan_PictureScanProgress* prog)
```

**描述**

此 API 可获取扫描仪扫描图片的进度。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scannerId | 用于查询扫描仪图片扫描进度的 ID，取值应为已连接的有效扫描仪设备 ID。 |
| [Scan\_PictureScanProgress](capi-oh-scan-scan-picturescanprogress.md)\* prog | 扫描图片的[Scan\_PictureScanProgress](capi-oh-scan-scan-picturescanprogress.md)，必须传入非空值，扫描进度将写入 prog 指针指向的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描仪成功查询到扫描图片的进度  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_INVALID\_PARAMETER](capi-ohscan-h.md#scan_errorcode) 表示输入参数无效  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误  [SCAN\_ERROR\_JAMMED](capi-ohscan-h.md#scan_errorcode) 表示文档进纸器卡纸  [SCAN\_ERROR\_NO\_DOCS](capi-ohscan-h.md#scan_errorcode) 表示文档进纸器缺纸  [SCAN\_ERROR\_COVER\_OPEN](capi-ohscan-h.md#scan_errorcode) 表示扫描仪盖板打开  [SCAN\_ERROR\_IO\_ERROR](capi-ohscan-h.md#scan_errorcode) 表示与扫描仪通信时发生错误  [SCAN\_ERROR\_NO\_MEMORY](capi-ohscan-h.md#scan_errorcode) 表示可用内存不足  [SCAN\_ERROR\_DEVICE\_BUSY](capi-ohscan-h.md#scan_errorcode) 表示扫描仪繁忙，应稍后重试操作 |

### OH\_Scan\_Exit()

```cpp
int32_t OH_Scan_Exit()
```

**描述**

此 API 可用于退出扫描服务，释放扫描框架内存，并注销扫描仪设备发现回调。扫描服务退出后，将无法再调用其他扫描 API。

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [SCAN\_ERROR\_NONE](capi-ohscan-h.md#scan_errorcode) 表示扫描服务成功退出  [SCAN\_ERROR\_NO\_PERMISSION](capi-ohscan-h.md#scan_errorcode) 表示无权限使用此接口  [SCAN\_ERROR\_RPC\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示 RPC 通信错误  [SCAN\_ERROR\_SERVER\_FAILURE](capi-ohscan-h.md#scan_errorcode) 表示扫描过程中发生错误 |
