---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-moduleinstall
title: ModuleInstall
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > C API > 模块 > ModuleInstall
category: harmonyos-references
scraped_at: 2026-11-12T09:57:13+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0d1edfa5bb983641e59d0605c409fc237e92410642ef2d22810d6613775df9c7
---

## 概述

描述AppGallery kit提供按需分发能力。

**起始版本：** 5.0.3(15)

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [module\_install.h](store-c-module_install.md) | 声明按需分发能力提供的API。 |
| [module\_install\_v2.h](appgallery-c-module_install_v2.md) | 声明按需分发能力提供的API。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) | 安装模块信息。 |
| typedef struct [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) | 安装模块结果。 |
| typedef struct [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) | 模块安装状态回调。 |
| typedef void (\*[ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallbackdeprecated))(char \*bundleName, char \*eventInfo) | 监听回调函数。 |
| typedef struct [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) | 安装模块信息。 |
| typedef struct [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) | 安装模块结果。 |
| typedef struct [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) | 模块安装状态回调。 |
| typedef void (\*[HMS\_ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_onstatuscallback)) (char \*bundleName, char \*eventInfo) | 监听回调函数。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) {  E\_NO\_ERROR = 0,  E\_PARAMS = 401,  E\_QUERY\_MODULE = 1006500001,  E\_REPEATED\_CALL = 1006500002,  E\_CONNECT\_SA = 1006500004,  E\_OFF\_WITHOUT\_ON = 1006500006,  E\_CONNECT\_SERVICE\_EXTENSION = 1006500007,  E\_WRITE\_PARAM = 1006500008,  E\_REQUEST\_SERVER = 1006500009,  E\_RESPONSE\_INVALID = 1006500010,  E\_INNER\_ERROR = 1006500011,  E\_INTERNAL\_COMMUNICATION = 1006500012,  E\_INVALID\_TASK\_ID = 1006500013  } | 枚举错误码。 |
| [ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatusdeprecated) {  INSTALLED = 0,  NOT\_INSTALLED = 1  } | 枚举安装状态。 |
| [ModuleInstall\_RequestCode](store-c-moduleinstall.md#moduleinstall_requestcodedeprecated) {  MODULE\_ALREADY\_EXISTS = -8,  MODULE\_UNAVAILABLE = -7,  INVALID\_REQUEST = -6,  NETWORK\_ERROR = -5,  INVOKER\_VERIFICATION\_FAILED = -4,  FOREGROUND\_REQUIRED = -3,  ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2,  FAILURE = -1,  SUCCESS = 0,  DOWNLOAD\_WAIT\_WIFI = 1  } | 枚举请求码。 |
| [ModuleInstall\_TaskStatus](store-c-moduleinstall.md#moduleinstall_taskstatusdeprecated) {  CREATE\_TASK\_FAILED = -4,  HIGHER\_VERSION\_INSTALLED = -3,  TASK\_ALREADY\_EXISTS = -2,  TASK\_UNFOUND = -1,  TASK\_CREATED = 0,  DOWNLOADING = 1,  DOWNLOAD\_PAUSED = 2,  DOWNLOAD\_WAITING = 3,  DOWNLOAD\_SUCCESSFUL = 4,  DOWNLOAD\_FAILED = 5,  DOWNLOAD\_WAIT\_FOR\_WIFI = 6,  INSTALL\_WAITING = 20,  INSTALLING = 21,  INSTALL\_SUCCESSFUL = 22,  INSTALL\_FAILED = 23  } | 枚举任务状态。 |
| typedef enum [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) {  HMS\_MODULEINSTALL\_NO\_ERROR = 0,  HMS\_MODULEINSTALL\_PARAM\_INVALID = 401,  HMS\_MODULEINSTALL\_QUERY\_MODULE\_FAILED = 1006500001,  HMS\_MODULEINSTALL\_REPEATED\_CALL = 1006500002,  HMS\_MODULEINSTALL\_CONNECT\_SA\_FAILED= 1006500004,  HMS\_MODULEINSTALL\_OFF\_WITHOUT\_ON\_FAILED = 1006500006,  HMS\_MODULEINSTALL\_CONNECT\_SERVICE\_FAILED = 1006500007,  HMS\_MODULEINSTALL\_WRITE\_PARAM\_FAILED = 1006500008,  HMS\_MODULEINSTALL\_REQUEST\_SERVER\_FAILED = 1006500009,  HMS\_MODULEINSTALL\_RESPONSE\_INVALID\_FAILED = 1006500010,  HMS\_MODULEINSTALL\_INNER\_ERROR = 1006500011,  HMS\_MODULEINSTALL\_INTERNAL\_COMMUNICATION\_FAILED= 1006500012,  HMS\_MODULEINSTALL\_TASK\_ID\_INVALID = 1006500013  } | 枚举错误码。 |
| typedef enum [HMS\_ModuleInstall\_InstallStatus](store-c-moduleinstall.md#hms_moduleinstall_installstatus) {  HMS\_MODULEINSTALL\_STATUS\_INSTALLED = 0,  HMS\_MODULEINSTALL\_STATUS\_NOT\_INSTALLED = 1  } | 枚举安装状态。 |
| typedef enum [HMS\_ModuleInstall\_RequestCode](store-c-moduleinstall.md#hms_moduleinstall_requestcode) {  HMS\_MODULEINSTALL\_CODE\_MODULE\_ALREADY\_EXISTS = -8,  HMS\_MODULEINSTALL\_CODE\_MODULE\_UNAVAILABLE = -7,  HMS\_MODULEINSTALL\_CODE\_INVALID\_REQUEST = -6,  HMS\_MODULEINSTALL\_CODE\_NETWORK\_ERROR = -5,  HMS\_MODULEINSTALL\_CODE\_INVALID\_INVOKER = -4,  HMS\_MODULEINSTALL\_CODE\_FOREGROUND\_REQUIRED = -3,  HMS\_MODULEINSTALL\_CODE\_ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2,  HMS\_MODULEINSTALL\_CODE\_FAILURE = -1,  HMS\_MODULEINSTALL\_CODE\_SUCCESS = 0,  HMS\_MODULEINSTALL\_CODE\_DOWNLOAD\_WAIT\_WIFI = 1  } | 枚举请求码。 |
| typedef enum [HMS\_ModuleInstall\_TaskStatus](store-c-moduleinstall.md#hms_moduleinstall_taskstatus) {  HMS\_MODULEINSTALL\_TASK\_CREATE\_FAILED = -4,  HMS\_MODULEINSTALL\_TASK\_HIGHER\_VERSION\_INSTALLED = -3,  HMS\_MODULEINSTALL\_TASK\_ALREADY\_EXISTS= -2,  HMS\_MODULEINSTALL\_TASK\_UNFOUND = -1,  HMS\_MODULEINSTALL\_TASK\_CREATED = 0,  HMS\_MODULEINSTALL\_TASK\_DOWNLOADING = 1,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_PAUSED = 2,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_WAITING = 3,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_SUCCESSFUL = 4,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_FAILED = 5,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_WAIT\_FOR\_WIFI = 6,  HMS\_MODULEINSTALL\_TASK\_INSTALL\_WAITING = 20,  HMS\_MODULEINSTALL\_TASK\_INSTALLING = 21,  HMS\_MODULEINSTALL\_TASK\_INSTALL\_SUCCESSFUL = 22,  HMS\_MODULEINSTALL\_TASK\_INSTALL\_FAILED = 23  } | 枚举任务状态。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_GetInstalledModule](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduledeprecated)(const char \*moduleName, unsigned int length, [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*\*installedModule) | 查询模块是否安装。 |
| char \*[HMS\_ModuleInstall\_GetInstalledModuleName](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulenamedeprecated)(const [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*installedModule) | 获取模块名。 |
| int [HMS\_ModuleInstall\_GetInstalledModuleType](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletypedeprecated)(const [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*installedModule) | 获取模块类型。 |
| [ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatusdeprecated) [HMS\_ModuleInstall\_GetModuleInstallStatus](store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatusdeprecated)(const [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*installedModule) | 获取模块安装状态。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_FetchModules](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesdeprecated)(const char \*bundleName, unsigned int length, char \*\*moduleNames, unsigned int moduleNamesLength, [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*\*fetchModulesResult) | 请求下载模块。 |
| [ModuleInstall\_RequestCode](store-c-moduleinstall.md#moduleinstall_requestcodedeprecated) [HMS\_ModuleInstall\_GetFetchModulesRequestCode](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcodedeprecated)(const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载请求码。 |
| [ModuleInstall\_TaskStatus](store-c-moduleinstall.md#moduleinstall_taskstatusdeprecated) [HMS\_ModuleInstall\_GetFetchModulesTaskStatus](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatusdeprecated)( const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载任务状态。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesTaskId](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskiddeprecated)(const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载任务id。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesDesc](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdescdeprecated)(const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载描述。 |
| char \*[HMS\_ModuleInstall\_GetFetchModules](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdeprecated)(const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载模块名。 |
| int [HMS\_ModuleInstall\_GetFetchModulesTotalSize](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsizedeprecated)(const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载总大小。 |
| int [HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsizedeprecated)(const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult) | 获取模块下载已下载大小。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_CancelTask](store-c-moduleinstall.md#hms_moduleinstall_canceltaskdeprecated)(const char \*taskId, unsigned int length, unsigned int cancelResult) | 取消下载任务。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_PauseTask](store-c-moduleinstall.md#hms_moduleinstall_pausetaskdeprecated)(const char \*taskId) | 暂停下载任务。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_ShowCellularDataConfirmation](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationdeprecated)(const char \*taskId, unsigned int length, unsigned int showResult) | 展示流量弹窗。 |
| [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*[HMS\_ModuleInstall\_CreateStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_createstatuscallbackdeprecated)([ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallbackdeprecated) \*onStatusCallback) | 创建下载进度监听回调。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_On](store-c-moduleinstall.md#hms_moduleinstall_ondeprecated)(const char \*bundleName, unsigned int length, unsigned int appIndex, unsigned int period, [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*\*callback) | 下载进度监听。 |
| void [HMS\_ModuleInstall\_ReleaseStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_releasestatuscallbackdeprecated)([ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*statusCallback) | 释放下载进度监听回调。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_Off](store-c-moduleinstall.md#hms_moduleinstall_offdeprecated)(const char \*bundleName, unsigned int length, unsigned int appIndex) | 取消下载进度监听。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_GetInstalledModuleV2](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulev2)(const char \*moduleName, unsigned int length, [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*\*installedModule) | 查询模块是否安装。 |
| char \*[HMS\_ModuleInstall\_GetInstalledModuleNameV2](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulenamev2)(const [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule) | 获取模块名。 |
| int [HMS\_ModuleInstall\_GetInstalledModuleTypeV2](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletypev2)(const [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule) | 获取模块类型。 |
| [HMS\_ModuleInstall\_InstallStatus](store-c-moduleinstall.md#hms_moduleinstall_installstatus) [HMS\_ModuleInstall\_GetModuleInstallStatusV2](store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatusv2)(const [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule) | 获取模块安装状态。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_FetchModulesV2](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesv2)(const char \*bundleName, unsigned int length, char \*\*moduleNames, unsigned int moduleNamesLength, [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*\*fetchModulesResult) | 请求下载模块。 |
| [HMS\_ModuleInstall\_RequestCode](store-c-moduleinstall.md#hms_moduleinstall_requestcode) [HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcodev2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载请求码。 |
| [HMS\_ModuleInstall\_TaskStatus](store-c-moduleinstall.md#hms_moduleinstall_taskstatus) [HMS\_ModuleInstall\_GetFetchModulesTaskStatusV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatusv2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载任务状态。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesTaskIdV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskidv2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载任务id。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesDescV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdescv2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载描述。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesv2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载模块名。 |
| int [HMS\_ModuleInstall\_GetFetchModulesTotalSizeV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsizev2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载总大小。 |
| int [HMS\_ModuleInstall\_GetFetchModulesDownloadedSizeV2](store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsizev2)(const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载已下载大小。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_CancelTaskV2](store-c-moduleinstall.md#hms_moduleinstall_canceltaskv2)(const char \*taskId, unsigned int length, unsigned int cancelResult) | 取消下载任务。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_ShowCellularDataConfirmationV2](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationv2)(const char \*taskId, unsigned int length, unsigned int showResult) | 向用户展示流量提醒弹窗。 |
| [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*[HMS\_ModuleInstall\_CreateStatusCallbackV2](store-c-moduleinstall.md#hms_moduleinstall_createstatuscallbackv2)([HMS\_ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_onstatuscallback) \*onStatusCallback) | 创建下载进度监听回调。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_OnV2](store-c-moduleinstall.md#hms_moduleinstall_onv2)(const char \*bundleName, unsigned int length, unsigned int appIndex, unsigned int period, [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*\*callback) | 下载进度监听。 |
| void [HMS\_ModuleInstall\_ReleaseStatusCallbackV2](store-c-moduleinstall.md#hms_moduleinstall_releasestatuscallbackv2)([HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*statusCallback) | 释放监听下载进度的回调。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_OffV2](store-c-moduleinstall.md#hms_moduleinstall_offv2)(const char \*bundleName, unsigned int length, unsigned int appIndex) | 取消下载进度监听。 |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_PauseTaskV2](store-c-moduleinstall.md#hms_moduleinstall_pausetaskv2)(const char \*taskId) | 暂停下载任务。 |

## 类型定义说明

### ModuleInstall\_InstalledModule(deprecated)

```c
typedef struct ModuleInstall_InstalledModule ModuleInstall_InstalledModule
```

**描述**

安装模块信息。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_InstalledModule

### ModuleInstall\_FetchModulesResult(deprecated)

```c
typedef struct ModuleInstall_FetchModulesResult ModuleInstall_FetchModulesResult
```

**描述**

安装模块结果。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_FetchModulesResult

### ModuleInstall\_StatusCallback(deprecated)

```c
typedef struct ModuleInstall_StatusCallback ModuleInstall_StatusCallback
```

**描述**

模块安装状态回调。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_StatusCallback

### ModuleInstall\_OnStatusCallback(deprecated)

```c
typedef void (*ModuleInstall_OnStatusCallback)(char *bundleName, char *eventInfo)
```

**描述**

监听回调函数。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_OnStatusCallback

**参数：**

| 参数 | 描述 |
| --- | --- |
| char \*bundleName | 应用包名。 |
| char \*eventInfo | 监听回调信息。 |

### HMS\_ModuleInstall\_InstalledModule

```c
typedef struct HMS_ModuleInstall_InstalledModule HMS_ModuleInstall_InstalledModule
```

**描述**

安装模块信息。

**起始版本：** 26.0.1

### HMS\_ModuleInstall\_FetchModulesResult

```c
typedef struct HMS_ModuleInstall_FetchModulesResult HMS_ModuleInstall_FetchModulesResult
```

**描述**

安装模块结果。

**起始版本：** 26.0.1

### HMS\_ModuleInstall\_StatusCallback

```c
typedef struct HMS_ModuleInstall_StatusCallback HMS_ModuleInstall_StatusCallback
```

**描述**

模块安装状态回调。

**起始版本：** 26.0.1

### HMS\_ModuleInstall\_OnStatusCallback

```c
typedef void (*HMS_ModuleInstall_OnStatusCallback)(char *bundleName, char *eventInfo)
```

**描述**

监听回调函数。

**起始版本：** 26.0.1

**参数：**

| 参数 | 描述 |
| --- | --- |
| char \*bundleName | 应用包名。 |
| char \*eventInfo | 监听回调信息。 |

## 枚举类型说明

### ModuleInstall\_ErrCode(deprecated)

```c
enum ModuleInstall_ErrCode
```

**描述**

错误码枚举。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_ErrCode

| 枚举值 | 描述 |
| --- | --- |
| E\_NO\_ERROR = 0 | 成功。 |
| E\_PARAMS = 401 | 无效的参数。 |
| E\_QUERY\_MODULE = 1006500001 | 调用包管理模块接口异常。 |
| E\_REPEATED\_CALL = 1006500002 | 重复调用接口，输入相同。 |
| E\_CONNECT\_SA = 1006500004 | 服务异常。 |
| E\_OFF\_WITHOUT\_ON = 1006500006 | 未与[HMS\_ModuleInstall\_On](store-c-moduleinstall.md#hms_moduleinstall_ondeprecated)接口共同使用。 |
| E\_CONNECT\_SERVICE\_EXTENSION = 1006500007 | 服务连接失败。 |
| E\_WRITE\_PARAM = 1006500008 | 参数写入异常。 |
| E\_REQUEST\_SERVER = 1006500009 | 请求服务异常。 |
| E\_RESPONSE\_INVALID = 1006500010 | 响应参数无法解析。 |
| E\_INNER\_ERROR = 1006500011 | 内部错误。 |
| E\_INTERNAL\_COMMUNICATION = 1006500012 | 内部通信异常。  **起始版本：** 26.0.0 |
| E\_INVALID\_TASK\_ID = 1006500013 | 无效的任务id。  **起始版本：** 26.0.0 |

### ModuleInstall\_InstallStatus(deprecated)

```c
enum ModuleInstall_InstallStatus
```

**描述**

安装状态枚举。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_InstallStatus

| 枚举值 | 描述 |
| --- | --- |
| INSTALLED = 0 | 已安装。 |
| NOT\_INSTALLED = 1 | 未安装。 |

### ModuleInstall\_RequestCode(deprecated)

```c
enum ModuleInstall_RequestCode
```

**描述**

按需下载模块请求码枚举。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_RequestCode

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
| DOWNLOAD\_WAIT\_WIFI = 1 | 当前使用的是流量，开发者需要调用  [HMS\_ModuleInstall\_ShowCellularDataConfirmation](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationdeprecated)接口，提醒用户确认是否使用流量下载。 |

### ModuleInstall\_TaskStatus(deprecated)

```c
enum ModuleInstall_TaskStatus
```

**描述**

任务状态枚举。

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_TaskStatus

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

### HMS\_ModuleInstall\_ErrCode

```c
enum HMS_ModuleInstall_ErrCode
```

**描述**

错误码枚举。

**起始版本：** 26.0.1

| 枚举值 | 描述 |
| --- | --- |
| HMS\_MODULEINSTALL\_NO\_ERROR = 0 | 成功。 |
| HMS\_MODULEINSTALL\_PARAM\_INVALID = 401 | 无效的参数。 |
| HMS\_MODULEINSTALL\_QUERY\_MODULE\_FAILED = 1006500001 | 调用包管理模块接口异常。 |
| HMS\_MODULEINSTALL\_REPEATED\_CALL = 1006500002 | 重复调用接口，输入相同。 |
| HMS\_MODULEINSTALL\_CONNECT\_SA\_FAILED = 1006500004 | 服务异常。 |
| HMS\_MODULEINSTALL\_OFF\_WITHOUT\_ON\_FAILED = 1006500006 | 未与[HMS\_ModuleInstall\_OnV2](store-c-moduleinstall.md#hms_moduleinstall_onv2)接口共同使用。 |
| HMS\_MODULEINSTALL\_CONNECT\_SERVICE\_FAILED = 1006500007 | 服务连接失败。 |
| HMS\_MODULEINSTALL\_WRITE\_PARAM\_FAILED = 1006500008 | 参数写入异常。 |
| HMS\_MODULEINSTALL\_REQUEST\_SERVER\_FAILED = 1006500009 | 请求服务异常。 |
| HMS\_MODULEINSTALL\_RESPONSE\_INVALID\_FAILED = 1006500010 | 响应参数无法解析。 |
| HMS\_MODULEINSTALL\_INNER\_ERROR = 1006500011 | 内部异常。 |
| HMS\_MODULEINSTALL\_INTERNAL\_COMMUNICATION\_FAILED = 1006500012 | 内部通信异常。 |
| HMS\_MODULEINSTALL\_TASK\_ID\_INVALID = 1006500013 | 无效的任务id。 |

### HMS\_ModuleInstall\_InstallStatus

```c
enum HMS_ModuleInstall_InstallStatus
```

**描述**

安装状态枚举。

**起始版本：** 26.0.1

| 枚举值 | 描述 |
| --- | --- |
| HMS\_MODULEINSTALL\_STATUS\_INSTALLED = 0 | 已安装。 |
| HMS\_MODULEINSTALL\_STATUS\_NOT\_INSTALLED = 1 | 未安装。 |

### HMS\_ModuleInstall\_RequestCode

```c
enum HMS_ModuleInstall_RequestCode
```

**描述**

按需下载模块请求码枚举。

**起始版本：** 26.0.1

| 枚举值 | 描述 |
| --- | --- |
| HMS\_MODULEINSTALL\_CODE\_MODULE\_ALREADY\_EXISTS = -8 | 模块已存在。 |
| HMS\_MODULEINSTALL\_CODE\_MODULE\_UNAVAILABLE = -7 | 要下载的模块不存在或者模块不适配该设备。 |
| HMS\_MODULEINSTALL\_CODE\_INVALID\_REQUEST = -6 | 该请求无效，请求中包含的信息不准确。 |
| HMS\_MODULEINSTALL\_CODE\_NETWORK\_ERROR = -5 | 网络异常，请求失败。 |
| HMS\_MODULEINSTALL\_CODE\_INVALID\_INVOKER = -4 | 调用者信息异常。 |
| HMS\_MODULEINSTALL\_CODE\_FOREGROUND\_REQUIRED = -3 | 仅允许应用在前台时请求按需加载。 |
| HMS\_MODULEINSTALL\_CODE\_ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2 | 请求被拒绝，因为当前至少有一个请求正在下载。 |
| HMS\_MODULEINSTALL\_CODE\_FAILURE = -1 | 失败。 |
| HMS\_MODULEINSTALL\_CODE\_SUCCESS = 0 | 成功。 |
| HMS\_MODULEINSTALL\_CODE\_DOWNLOAD\_WAIT\_WIFI = 1 | 当前使用的是流量，开发者需要调用[HMS\_ModuleInstall\_ShowCellularDataConfirmationV2](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationv2)接口，提醒用户确认是否使用流量下载。 |

### HMS\_ModuleInstall\_TaskStatus

```c
enum HMS_ModuleInstall_TaskStatus
```

**描述**

任务状态枚举。

**起始版本：** 26.0.1

| 枚举值 | 描述 |
| --- | --- |
| HMS\_MODULEINSTALL\_TASK\_CREATE\_FAILED = -4 | 创建下载任务失败。 |
| HMS\_MODULEINSTALL\_TASK\_HIGHER\_VERSION\_INSTALLED = -3 | 本地存在相同或者更高版本。 |
| HMS\_MODULEINSTALL\_TASK\_ALREADY\_EXISTS = -2 | 本地存在相同或者更高版本。 |
| HMS\_MODULEINSTALL\_TASK\_UNFOUND = -1 | 下载任务不存在。 |
| HMS\_MODULEINSTALL\_TASK\_CREATED = 0 | 创建下载任务成功。 |
| HMS\_MODULEINSTALL\_TASK\_DOWNLOADING = 1 | 下载中。 |
| HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_PAUSED = 2 | 暂停中。 |
| HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_WAITING = 3 | 等待下载中。 |
| HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_SUCCESSFUL = 4 | 下载成功。 |
| HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_FAILED = 5 | 下载失败。 |
| HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_WAIT\_FOR\_WIFI = 6 | Wi-Fi预约。 |
| HMS\_MODULEINSTALL\_TASK\_INSTALL\_WAITING = 20 | 等待安装。 |
| HMS\_MODULEINSTALL\_TASK\_INSTALLING = 21 | 安装中。 |
| HMS\_MODULEINSTALL\_TASK\_INSTALL\_SUCCESSFUL = 22 | 安装完成。 |
| HMS\_MODULEINSTALL\_TASK\_INSTALL\_FAILED = 23 | 安装失败。 |

## 函数说明

### HMS\_ModuleInstall\_GetInstalledModule(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_GetInstalledModule(const char *moduleName, unsigned int length,
    ModuleInstall_InstalledModule **installedModule)
```

**描述**

查询模块是否安装。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetInstalledModuleV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*moduleName | 模块名。 |
| unsigned int length | 模块名长度，最大长度512。 |
| [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*\*installedModule | 模块信息。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_QUERY\_MODULE表示调用包管理模块接口异常。

### HMS\_ModuleInstall\_GetInstalledModuleName(deprecated)

```c
char *HMS_ModuleInstall_GetInstalledModuleName(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetInstalledModuleNameV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*installedModule | 模块信息。 |

**返回：**

返回模块名。

### HMS\_ModuleInstall\_GetInstalledModuleType(deprecated)

```c
int HMS_ModuleInstall_GetInstalledModuleType(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块类型。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetInstalledModuleTypeV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*installedModule | 模块信息。 |

**返回：**

返回模块类型, 取值参考：[bundleManager.ModuleType](js-apis-bundlemanager.md#moduletype)。当[ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatusdeprecated)=1时，默认返回0。

### HMS\_ModuleInstall\_GetModuleInstallStatus(deprecated)

```c
ModuleInstall_InstallStatus HMS_ModuleInstall_GetModuleInstallStatus(const ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块安装状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetModuleInstallStatusV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) \*installedModule | 模块信息。 |

**返回：**

模块安装状态，取值参考：[ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatusdeprecated)。

### HMS\_ModuleInstall\_FetchModules(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_FetchModules(const char *bundleName, unsigned int length, char **moduleNames, unsigned int moduleNamesLength, ModuleInstall_FetchModulesResult **fetchModulesResult)
```

**描述**

请求下载模块。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_FetchModulesV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*bundleName | 包名。 |
| unsigned int length | 包名长度，最大长度512。 |
| char \*\*moduleNames | 模块名数组。 |
| unsigned int moduleNamesLength | 模块名数组长度，最大长度512。 |
| [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*\*fetchModulesResult | 模块安装结果。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SA表示服务异常；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析；返回E\_INNER\_ERROR表示内部错误。

### HMS\_ModuleInstall\_GetFetchModulesRequestCode(deprecated)

```c
ModuleInstall_RequestCode HMS_ModuleInstall_GetFetchModulesRequestCode(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载请求码。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

按需下载模块请求码，取值参考: [ModuleInstall\_RequestCode](store-c-moduleinstall.md#moduleinstall_requestcodedeprecated)。

### HMS\_ModuleInstall\_GetFetchModulesTaskStatus(deprecated)

```c
ModuleInstall_TaskStatus HMS_ModuleInstall_GetFetchModulesTaskStatus(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesTaskStatusV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

模块下载任务状态，取值参考：[ModuleInstall\_TaskStatus](store-c-moduleinstall.md#moduleinstall_taskstatusdeprecated)。

### HMS\_ModuleInstall\_GetFetchModulesTaskId(deprecated)

```c
char *HMS_ModuleInstall_GetFetchModulesTaskId(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务id。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesTaskIdV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

任务id。

### HMS\_ModuleInstall\_GetFetchModulesDesc(deprecated)

```c
char *HMS_ModuleInstall_GetFetchModulesDesc(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载描述。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesDescV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载描述。

### HMS\_ModuleInstall\_GetFetchModules(deprecated)

```c
char* HMS_ModuleInstall_GetFetchModules(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块名。

### HMS\_ModuleInstall\_GetFetchModulesTotalSize(deprecated)

```c
int HMS_ModuleInstall_GetFetchModulesTotalSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载总大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesTotalSizeV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块总大小，单位是Byte。

### HMS\_ModuleInstall\_GetFetchModulesDownloadedSize(deprecated)

```c
int HMS_ModuleInstall_GetFetchModulesDownloadedSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载已下载大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_GetFetchModulesDownloadedSizeV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) \*fetchModulesResult | 模块安装结果。 |

**返回：**

已下载模块大小。

### HMS\_ModuleInstall\_CancelTask(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_CancelTask(const char *taskId, unsigned int length, unsigned int cancelResult)
```

**描述**

取消下载任务。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_CancelTaskV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*taskId | 任务id。 |
| unsigned int length | 任务id长度，最大长度512。 |
| unsigned int cancelResult | 取消下载结果。  0：成功。  1：失败。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析。

### HMS\_ModuleInstall\_PauseTask(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_PauseTask(const char *taskId)
```

**描述**

暂停下载任务。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.0

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_PauseTaskV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*taskId | 任务id。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_INVALID\_TASK\_ID表示无效的任务id；返回E\_INTERNAL\_COMMUNICATION表示内部通信异常。

### HMS\_ModuleInstall\_ShowCellularDataConfirmation(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_ShowCellularDataConfirmation(const char *taskId, unsigned int length, unsigned int showResult)
```

**描述**

展示流量弹窗。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_ShowCellularDataConfirmationV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*taskId | 任务id。 |
| unsigned int length | 任务id长度，最大长度512。 |
| unsigned int showResult | 展示流量弹窗结果。  0：成功。  1：失败。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_CONNECT\_SERVICE\_EXTENSION表示服务连接失败；返回E\_WRITE\_PARAM表示参数写入异常；返回E\_REQUEST\_SERVER表示请求服务异常；返回E\_RESPONSE\_INVALID表示响应参数无法解析。

### HMS\_ModuleInstall\_CreateStatusCallback(deprecated)

```c
ModuleInstall_StatusCallback *HMS_ModuleInstall_CreateStatusCallback(ModuleInstall_OnStatusCallback *onStatusCallback)
```

**描述**

创建下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_CreateStatusCallbackV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallbackdeprecated) \*onStatusCallback | 下载进度监听回调函数。 |

**返回：**

下载进度监听回调。

### HMS\_ModuleInstall\_On(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_On(const char *bundleName, unsigned int length, unsigned int appIndex, unsigned int period, ModuleInstall_StatusCallback **callback)
```

**描述**

下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_OnV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*bundleName | 包名。 |
| unsigned int length | 包名长度，最大长度512。 |
| unsigned int appIndex | 应用分身索引。 |
| unsigned int period | 监听周期。 |
| [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*\*callback | 下载进度监听回调。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_REPEATED\_CALL表示重复调用接口；返回E\_CONNECT\_SA表示服务异常。

### HMS\_ModuleInstall\_ReleaseStatusCallback(deprecated)

```c
void HMS_ModuleInstall_ReleaseStatusCallback(ModuleInstall_StatusCallback *statusCallback)
```

**描述**

释放下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_ReleaseStatusCallbackV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*statusCallback | 下载进度监听回调。 |

### HMS\_ModuleInstall\_Off(deprecated)

```c
ModuleInstall_ErrCode HMS_ModuleInstall_Off(const char *bundleName, unsigned int length, unsigned int appIndex)
```

**描述**

取消下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**废弃版本：** 26.0.1

**替代接口：** HMS\_ModuleInstall\_OffV2

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*bundleName | 包名。 |
| unsigned int length | 包名长度，最大长度512。 |
| unsigned int appIndex | 应用分身索引。 |

**返回：**

返回E\_NO\_ERROR表示成功；返回E\_PARAMS表示输入参数错误；返回E\_OFF\_WITHOUT\_ON表示未与监听接口共同使用；返回E\_CONNECT\_SA表示服务异常。

### HMS\_ModuleInstall\_GetInstalledModuleV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_GetInstalledModuleV2(const char *moduleName, unsigned int length,
    HMS_ModuleInstall_InstalledModule **installedModule)
```

**描述**

查询模块是否安装。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*moduleName | 模块名。 |
| unsigned int length | 模块名长度，最大长度512。 |
| [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*\*installedModule | 模块信息。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_PARAM\_INVALID表示输入参数错误；返回HMS\_MODULEINSTALL\_QUERY\_MODULE\_FAILED表示调用包管理模块接口异常。

### HMS\_ModuleInstall\_GetInstalledModuleNameV2

```c
char *HMS_ModuleInstall_GetInstalledModuleNameV2(const HMS_ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

返回模块名。

### HMS\_ModuleInstall\_GetInstalledModuleTypeV2

```c
int HMS_ModuleInstall_GetInstalledModuleTypeV2(const HMS_ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块类型。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

返回模块类型, 取值参考：[bundleManager.ModuleType](js-apis-bundlemanager.md#moduletype)。当[HMS\_ModuleInstall\_InstallStatus](store-c-moduleinstall.md#hms_moduleinstall_installstatus)=1时，默认返回0。

### HMS\_ModuleInstall\_GetModuleInstallStatusV2

```c
HMS_ModuleInstall_InstallStatus HMS_ModuleInstall_GetModuleInstallStatusV2(
    const HMS_ModuleInstall_InstalledModule *installedModule)
```

**描述**

获取模块安装状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule | 模块信息。 |

**返回：**

模块安装状态，取值参考：[HMS\_ModuleInstall\_InstallStatus](store-c-moduleinstall.md#hms_moduleinstall_installstatus)。

### HMS\_ModuleInstall\_FetchModulesV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_FetchModulesV2(const char *bundleName, unsigned int length,
    char **moduleNames, unsigned int moduleNamesLength, HMS_ModuleInstall_FetchModulesResult **fetchModulesResult)
```

**描述**

请求下载模块。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*bundleName | 包名。 |
| unsigned int length | 包名长度，最大长度512。 |
| char \*\*moduleNames | 模块名数组。 |
| unsigned int moduleNamesLength | 模块名数组长度，最大长度512。 |
| [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*\*fetchModulesResult | 模块安装结果。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_PARAM\_INVALID表示输入参数错误；返回HMS\_MODULEINSTALL\_CONNECT\_SA\_FAILED表示服务异常；返回HMS\_MODULEINSTALL\_CONNECT\_SERVICE\_FAILED表示服务连接失败；返回HMS\_MODULEINSTALL\_WRITE\_PARAM\_FAILED表示参数写入异常；返回HMS\_MODULEINSTALL\_REQUEST\_SERVER\_FAILED表示请求服务异常；返回HMS\_MODULEINSTALL\_RESPONSE\_INVALID\_FAILED表示响应参数无法解析；返回HMS\_MODULEINSTALL\_INNER\_ERROR表示内部错误。

### HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2

```c
HMS_ModuleInstall_RequestCode HMS_ModuleInstall_GetFetchModulesRequestCodeV2(
    const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载请求码。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

按需下载模块请求码，取值参考: [HMS\_ModuleInstall\_RequestCode](store-c-moduleinstall.md#hms_moduleinstall_requestcode)。

### HMS\_ModuleInstall\_GetFetchModulesTaskStatusV2

```c
HMS_ModuleInstall_TaskStatus HMS_ModuleInstall_GetFetchModulesTaskStatusV2(
    const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务状态。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

模块下载任务状态，取值参考：[HMS\_ModuleInstall\_TaskStatus](store-c-moduleinstall.md#hms_moduleinstall_taskstatus)。

### HMS\_ModuleInstall\_GetFetchModulesTaskIdV2

```c
char *HMS_ModuleInstall_GetFetchModulesTaskIdV2(const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载任务id。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

任务id。

### HMS\_ModuleInstall\_GetFetchModulesDescV2

```c
char *HMS_ModuleInstall_GetFetchModulesDescV2(const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载描述。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

模块下载结果描述。

### HMS\_ModuleInstall\_GetFetchModulesV2

```c
char *HMS_ModuleInstall_GetFetchModulesV2(const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载模块名。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块名。

### HMS\_ModuleInstall\_GetFetchModulesTotalSizeV2

```c
int HMS_ModuleInstall_GetFetchModulesTotalSizeV2(const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载总大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

下载模块总大小，单位是Byte。

### HMS\_ModuleInstall\_GetFetchModulesDownloadedSizeV2

```c
int HMS_ModuleInstall_GetFetchModulesDownloadedSizeV2(const HMS_ModuleInstall_FetchModulesResult *fetchModulesResult)
```

**描述**

获取模块下载已下载大小。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult | 模块安装结果。 |

**返回：**

已下载模块大小。

### HMS\_ModuleInstall\_CancelTaskV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_CancelTaskV2(const char *taskId, unsigned int length,
    unsigned int cancelResult)
```

**描述**

取消下载任务。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*taskId | 任务id。 |
| unsigned int length | 任务id长度，最大长度512。 |
| unsigned int cancelResult | 取消下载结果。  0：成功。  1：失败。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_PARAM\_INVALID表示输入参数错误；返回HMS\_MODULEINSTALL\_CONNECT\_SERVICE\_FAILED表示服务连接失败；返回HMS\_MODULEINSTALL\_WRITE\_PARAM\_FAILED表示参数写入异常；返回HMS\_MODULEINSTALL\_REQUEST\_SERVER\_FAILED表示请求服务异常；返回HMS\_MODULEINSTALL\_RESPONSE\_INVALID\_FAILED表示响应参数无法解析。

### HMS\_ModuleInstall\_PauseTaskV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_PauseTaskV2(const char *taskId)
```

**描述**

暂停下载任务。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*taskId | 任务id。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_TASK\_ID\_INVALID表示无效的任务id；返回HMS\_MODULEINSTALL\_INTERNAL\_COMMUNICATION\_FAILED表示内部通信异常。

### HMS\_ModuleInstall\_ShowCellularDataConfirmationV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_ShowCellularDataConfirmationV2(const char *taskId, unsigned int length,
    unsigned int showResult)
```

**描述**

向用户展示流量提醒弹窗。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*taskId | 任务id。 |
| unsigned int length | 任务id长度，最大长度512。 |
| unsigned int showResult | 展示流量弹窗结果。  0：成功。  1：失败。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_PARAM\_INVALID表示输入参数错误；返回HMS\_MODULEINSTALL\_CONNECT\_SERVICE\_FAILED表示服务连接失败；返回HMS\_MODULEINSTALL\_WRITE\_PARAM\_FAILED表示参数写入异常；返回HMS\_MODULEINSTALL\_REQUEST\_SERVER\_FAILED表示请求服务异常；返回HMS\_MODULEINSTALL\_RESPONSE\_INVALID\_FAILED表示响应参数无法解析。

### HMS\_ModuleInstall\_CreateStatusCallbackV2

```c
HMS_ModuleInstall_StatusCallback *HMS_ModuleInstall_CreateStatusCallbackV2(
    HMS_ModuleInstall_OnStatusCallback *onStatusCallback)
```

**描述**

创建下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| [HMS\_ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_onstatuscallback) \*onStatusCallback | 下载进度监听回调函数。 |

**返回：**

下载进度监听回调。

### HMS\_ModuleInstall\_OnV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_OnV2(const char *bundleName, unsigned int length, unsigned int appIndex,
    unsigned int period, HMS_ModuleInstall_StatusCallback **callback)
```

**描述**

下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*bundleName | 包名。 |
| unsigned int length | 包名长度，最大长度512。 |
| unsigned int appIndex | 应用分身索引。 |
| unsigned int period | 监听周期。 |
| [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*\*callback | 下载进度监听回调。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_PARAM\_INVALID表示输入参数错误；返回HMS\_MODULEINSTALL\_REPEATED\_CALL表示重复调用接口；返回HMS\_MODULEINSTALL\_CONNECT\_SA\_FAILED表示服务异常。

### HMS\_ModuleInstall\_ReleaseStatusCallbackV2

```c
void HMS_ModuleInstall_ReleaseStatusCallbackV2(HMS_ModuleInstall_StatusCallback *statusCallback)
```

**描述**

释放下载进度监听回调。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*statusCallback | 下载进度监听回调。 |

### HMS\_ModuleInstall\_OffV2

```c
HMS_ModuleInstall_ErrCode HMS_ModuleInstall_OffV2(const char *bundleName, unsigned int length, unsigned int appIndex)
```

**描述**

取消下载进度监听。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**参数：**

| 名称 | 描述 |
| --- | --- |
| const char \*bundleName | 包名。 |
| unsigned int length | 包名长度，最大长度512。 |
| unsigned int appIndex | 应用分身索引。 |

**返回：**

返回HMS\_MODULEINSTALL\_NO\_ERROR表示成功；返回HMS\_MODULEINSTALL\_PARAM\_INVALID表示输入参数错误；返回HMS\_MODULEINSTALL\_OFF\_WITHOUT\_ON\_FAILED表示未与监听接口共同使用；返回HMS\_MODULEINSTALL\_CONNECT\_SA\_FAILED表示服务异常。
