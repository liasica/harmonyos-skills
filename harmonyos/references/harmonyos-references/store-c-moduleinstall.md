---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-moduleinstall
title: ModuleInstall
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > C API > 模块 > ModuleInstall
category: harmonyos-references
scraped_at: 2026-04-28T08:16:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c5381512b1a129c4b9f6a4597d60b8a9c36983b9b3a118b25b8e0d672e48386
---

## 概述

PhonePC/2in1TabletTV

描述AppGallery kit提供按需分发能力。

**起始版本：** 5.0.2(14)

## 汇总

PhonePC/2in1TabletTV

### 文件

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [module\_install.h](store-c-module_install.md) | 声明按需分发能力提供的API。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmodule) [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmodule) | 安装模块信息。 |
| typedef struct [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) | 安装模块结果。 |
| typedef struct [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallback) [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallback) | 模块安装状态回调。 |
| typedef void (\*[ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallback))(char \*bundleName, char \*eventInfo) | 监听回调函数。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcode) | 枚举错误码。 |
| [ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatus) | 枚举安装状态。 |
| [ModuleInstall\_RequestCode](store-c-moduleinstall.md#moduleinstall_requestcode) | 枚举请求码。 |
| [ModuleInstall\_TaskStatus](store-c-moduleinstall.md#moduleinstall_taskstatus) | 枚举任务状态。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HMS\_ModuleInstall\_GetInstalledModule](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodule) | 查询模块是否安装。 |
| [HMS\_ModuleInstall\_GetInstalledModuleName](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulename) | 获取模块名。 |
| [HMS\_ModuleInstall\_GetInstalledModuleType](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletype) | 获取模块类型。 |
| [HMS\_ModuleInstall\_GetModuleInstallStatus](store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatus) | 获取模块安装状态。 |
| [HMS\_ModuleInstall\_FetchModules](store-c-moduleinstall.md#hms_moduleinstall_fetchmodules) | 请求下载模块。 |
| [HMS\_ModuleInstall\_GetFetchModulesRequestCode](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcode) | 获取模块下载请求码。 |
| [HMS\_ModuleInstall\_GetFetchModulesTaskStatus](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatus) | 获取模块下载任务状态。 |
| [HMS\_ModuleInstall\_GetFetchModulesTaskId](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskid) | 获取模块下载任务id。 |
| [HMS\_ModuleInstall\_GetFetchModulesDesc](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdesc) | 获取模块下载描述。 |
| [HMS\_ModuleInstall\_GetFetchModules](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodules) | 获取模块下载模块名。 |
| [HMS\_ModuleInstall\_GetFetchModulesTotalSize](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsize) | 获取模块下载总大小。 |
| [HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsize) | 获取模块下载已下载大小。 |
| [HMS\_ModuleInstall\_CancelTask](store-c-moduleinstall.md#hms_moduleinstall_canceltask) | 取消下载任务。 |
| [HMS\_ModuleInstall\_ShowCellularDataConfirmation](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmation) | 展示流量弹窗。 |
| [HMS\_ModuleInstall\_CreateStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_createstatuscallback) | 创建下载进度监听回调。 |
| [HMS\_ModuleInstall\_On](store-c-moduleinstall.md#hms_moduleinstall_on) | 下载进度监听。 |
| [HMS\_ModuleInstall\_ReleaseStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_releasestatuscallback) | 释放下载进度监听回调。 |
| [HMS\_ModuleInstall\_Off](store-c-moduleinstall.md#hms_moduleinstall_off) | 取消下载进度监听。 |

## 类型定义说明

PhonePC/2in1TabletTV

### ModuleInstall\_InstalledModule

PhonePC/2in1TabletTV

```
1. typedef struct ModuleInstall_InstalledModule ModuleInstall_InstalledModule
```

**描述**

安装模块信息。

**起始版本：** 5.0.2(14)

### ModuleInstall\_FetchModulesResult

PhonePC/2in1TabletTV

```
1. typedef struct ModuleInstall_FetchModulesResult ModuleInstall_FetchModulesResult
```

**描述**

安装模块结果。

**起始版本：** 5.0.2(14)

### ModuleInstall\_StatusCallback

PhonePC/2in1TabletTV

```
1. typedef struct ModuleInstall_StatusCallback ModuleInstall_StatusCallback
```

**描述**

模块安装状态回调。

**起始版本：** 5.0.2(14)

### ModuleInstall\_OnStatusCallback

PhonePC/2in1TabletTV

```
1. typedef void (*ModuleInstall_OnStatusCallback)(char *bundleName, char *eventInfo)
```

**描述**

监听回调函数。

**起始版本：** 5.0.2(14)

## 枚举类型说明

PhonePC/2in1TabletTV

### ModuleInstall\_ErrCode

PhonePC/2in1TabletTV

```
1. enum ModuleInstall_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| E\_NO\_ERROR = 0 | 成功。 |
| E\_PARAMS = 401 | 无效的参数。 |
| E\_QUERY\_MODULE = 1006500001 | 调用包管理模块接口异常。 |
| E\_REPEATED\_CALL = 1006500002 | 重复调用接口，输入相同。 |
| E\_CONNECT\_SA = 1006500004 | 服务异常。 |
| E\_OFF\_WITHOUT\_ON = 1006500006 | 未与[HMS\_ModuleInstall\_On](store-c-moduleinstall.md#hms_moduleinstall_on)接口共同使用。 |
| E\_CONNECT\_SERVICE\_EXTENSION = 1006500007 | 服务连接失败。 |
| E\_WRITE\_PARAM = 1006500008 | 参数写入异常。 |
| E\_REQUEST\_SERVER = 1006500009 | 请求服务异常。 |
| E\_RESPONSE\_INVALID = 1006500010 | 响应参数无法解析。 |
| E\_INNER\_ERROR = 1006500011 | 内部错误。 |

### ModuleInstall\_InstallStatus

PhonePC/2in1TabletTV

```
1. enum ModuleInstall_InstallStatus
```

**描述**

枚举安装状态。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| INSTALLED = 0 | 已安装。 |
| NOT\_INSTALLED = 1 | 未安装。 |

### ModuleInstall\_RequestCode

PhonePC/2in1TabletTV

```
1. enum ModuleInstall_RequestCode
```

**描述**

枚举按需下载模块请求码。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| MODULE\_ALREADY\_EXISTS = -8 | 模块已存在。 |
| MODULE\_UNAVAILABLE = -7 | 要下载的模块不存在或者模块不适配该设备。 |
| INVALID\_REQUEST = -6 | 该请求无效，请求中包含的信息不准确。 |
| NETWORK\_ERROR = -5 | 网络异常，请求失败。 |
| INVOKER\_VERIFICATION\_FAILED = -4 | 调用者信息异常。 |
| FOREGROUND\_REQUIRED = -3 | 仅允许应用在前台时请求按需加载。 |
| ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2 | 请求被拒绝，因为当前至少有一个请求正在下载。 |
| FAILURE = -1 | 失败。 |
| SUCCESS = 0 | 成功。 |
| DOWNLOAD\_WAIT\_WIFI = 1 | 当前使用的是流量，开发者需要调用  [HMS\_ModuleInstall\_ShowCellularDataConfirmation](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmation)接口，提醒用户确认是否使用流量下载。 |

### ModuleInstall\_TaskStatus

PhonePC/2in1TabletTV

```
1. enum ModuleInstall_TaskStatus
```

**描述**

枚举任务状态。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| CREATE\_TASK\_FAILED = -4 | 创建下载任务失败。 |
| HIGHER\_VERSION\_INSTALLED = -3 | 本地存在相同或者更高版本。 |
| TASK\_ALREADY\_EXISTS = -2 | 下载任务已存在。 |
| TASK\_UNFOUND = -1 | 下载任务不存在。 |
| TASK\_CREATED = 0 | 创建下载任务成功。 |
| DOWNLOADING = 1 | 下载中。 |
| DOWNLOAD\_PAUSED = 2 | 暂停中。 |
| DOWNLOAD\_WAITING = 3 | 等待下载中。 |
| DOWNLOAD\_SUCCESSFUL = 4 | 下载成功。 |
| DOWNLOAD\_FAILED = 5 | 下载失败。 |
| DOWNLOAD\_WAIT\_FOR\_WIFI = 6 | Wi-Fi预约。 |
| INSTALL\_WAITING = 20 | 等待安装。 |
| INSTALLING = 21 | 安装中。 |
| INSTALL\_SUCCESSFUL = 22 | 安装完成。 |
| INSTALL\_FAILED = 23 | 安装失败。 |

## 函数说明

PhonePC/2in1TabletTV

### HMS\_ModuleInstall\_GetInstalledModule

PhonePC/2in1TabletTV

```
1. ModuleInstall_ErrCode HMS_ModuleInstall_GetInstalledModule(const char *moduleName, unsigned int length,
2. ModuleInstall_InstalledModule **installedModule)
```

**描述**

查询模块是否安装。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| char \*moduleName | 模块名。 |
| int length | 模块名长度，最大长度512。 |
| [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmodule) \*\*installedModule | 模块信息。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_QUERY\_MODULE表示调用包管理模块接口异常。

### HMS\_ModuleInstall\_GetInstalledModuleName

PhonePC/2in1TabletTV

```
1. char *HMS_ModuleInstall_GetInstalledModuleName(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

返回模块名。

### HMS\_ModuleInstall\_GetInstalledModuleType

PhonePC/2in1TabletTV

```
1. int HMS_ModuleInstall_GetInstalledModuleType(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块类型。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

返回模块类型, 取值参考：[bundleManager.ModuleType](js-apis-bundlemanager.md#moduletype)。当[ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatus)=1时，默认返回0。

### HMS\_ModuleInstall\_GetModuleInstallStatus

PhonePC/2in1TabletTV

```
1. ModuleInstall_InstallStatus HMS_ModuleInstall_GetModuleInstallStatus(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块安装状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

模块安装状态，取值参考：[ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatus)。

### HMS\_ModuleInstall\_FetchModules

PhonePC/2in1TabletTV

```
1. ModuleInstall_ErrCode HMS_ModuleInstall_FetchModules(const char *bundleName, unsigned int length, char **moduleNames, unsigned int moduleNamesLength, ModuleInstall_FetchModulesResult **fetchModulesResult)
```

**描述**

请求下载模块。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| char \*bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| char \*\*moduleNames | 模块名数组。 |
| int moduleNamesLength | 模块名数组长度，最大长度512。 |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*\*fetchModulesResult | 模块安装结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SA表示服务异常；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析；返回E\_INNER\_ERROR表示内部错误。

### HMS\_ModuleInstall\_GetFetchModulesRequestCode

PhonePC/2in1TabletTV

```
1. ModuleInstall_RequestCode HMS_ModuleInstall_GetFetchModulesRequestCode(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载请求码。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

按需下载模块请求码，取值参考: [ModuleInstall\_RequestCode](store-c-moduleinstall.md#moduleinstall_requestcode)。

### HMS\_ModuleInstall\_GetFetchModulesTaskStatus

PhonePC/2in1TabletTV

```
1. ModuleInstall_TaskStatus HMS_ModuleInstall_GetFetchModulesTaskStatus(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

模块下载任务状态，取值参考：[ModuleInstall\_TaskStatus](store-c-moduleinstall.md#moduleinstall_taskstatus)。

### HMS\_ModuleInstall\_GetFetchModulesTaskId

PhonePC/2in1TabletTV

```
1. char *HMS_ModuleInstall_GetFetchModulesTaskId(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务id。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

任务id。

### HMS\_ModuleInstall\_GetFetchModulesDesc

PhonePC/2in1TabletTV

```
1. char *HMS_ModuleInstall_GetFetchModulesDesc(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载描述。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载描述。

### HMS\_ModuleInstall\_GetFetchModules

PhonePC/2in1TabletTV

```
1. char* HMS_ModuleInstall_GetFetchModules(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块名。

### HMS\_ModuleInstall\_GetFetchModulesTotalSize

PhonePC/2in1TabletTV

```
1. int HMS_ModuleInstall_GetFetchModulesTotalSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载总大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块总大小。

### HMS\_ModuleInstall\_GetFetchModulesDownloadedSize

PhonePC/2in1TabletTV

```
1. int HMS_ModuleInstall_GetFetchModulesDownloadedSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载已下载大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

已下载模块大小。

### HMS\_ModuleInstall\_CancelTask

PhonePC/2in1TabletTV

```
1. ModuleInstall_ErrCode HMS_ModuleInstall_CancelTask(const char *taskId, unsigned int length, unsigned int cancelResult)
```

**描述**

取消下载任务。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| char \*taskId | 任务id。 |
| int length | 任务id长度，最大长度512。 |
| int cancelResult | 取消下载结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析；

### HMS\_ModuleInstall\_ShowCellularDataConfirmation

PhonePC/2in1TabletTV

```
1. ModuleInstall_ErrCode HMS_ModuleInstall_ShowCellularDataConfirmation(const char *taskId, unsigned int length, unsigned int showResult)
```

**描述**

展示流量弹窗。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| char \*taskId | 任务id。 |
| int length | 任务id长度，最大长度512。 |
| int showResult | 展示流量弹窗结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析。

### HMS\_ModuleInstall\_CreateStatusCallback

PhonePC/2in1TabletTV

```
1. ModuleInstall_StatusCallback *HMS_ModuleInstall_CreateStatusCallback(ModuleInstall_OnStatusCallback *onStatusCallback)
```

**描述**

创建下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallback) \*onStatusCallback | 下载进度监听回调函数。 |

**返回：**

下载进度监听回调。

### HMS\_ModuleInstall\_On

PhonePC/2in1TabletTV

```
1. ModuleInstall_ErrCode HMS_ModuleInstall_On(const char *bundleName, unsigned int length, unsigned int appIndex, unsigned int period, ModuleInstall_StatusCallback **callback)
```

**描述**

下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| char \*bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| int appIndex | 应用分身索引。 |
| int period | 监听周期。 |
| [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallback) \*\*callback | 下载进度监听回调。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_REPEATED\_CALL表示重复调用接口；返回E\_CONNECT\_SA表示服务异常。

### HMS\_ModuleInstall\_ReleaseStatusCallback

PhonePC/2in1TabletTV

```
1. void HMS_ModuleInstall_ReleaseStatusCallback(ModuleInstall_StatusCallback *statusCallback)
```

**描述**

释放下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallback) \*statusCallback | 下载进度监听回调。 |

### HMS\_ModuleInstall\_Off

PhonePC/2in1TabletTV

```
1. ModuleInstall_ErrCode HMS_ModuleInstall_Off(const char *bundleName, unsigned int length, unsigned int appIndex)
```

**描述**

取消下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 描述 |
| --- | --- |
| char \*bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| int appIndex | 应用分身索引。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_OFF\_WITHOUT\_ON表示未与监听接口共同使用；返回E\_CONNECT\_SA表示服务异常。
