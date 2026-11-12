---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-module_install
title: module_install.h
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > C API > 头文件 > module_install.h
category: harmonyos-references
scraped_at: 2026-11-12T09:57:13+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a5ef0731bc3bf9b379afc970b2fd1bb997d8b7e4ed9f81e14170fc93925efdb0
---

## 概述

声明按需分发能力的API。

**引用文件：** <AppGalleryKit/module\_install.h>

**库：** libhmsmoduleinstall.so

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.3(15)

**相关模块：** [ModuleInstall](store-c-moduleinstall.md)

**废弃版本：** 26.0.1

**替代引用文件：** <AppGalleryKit/module\_install\_v2.h>

## 汇总

### 类型

| 名称 | 描述 |
| --- | --- |
| typedef struct [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) [ModuleInstall\_InstalledModule](store-c-moduleinstall.md#moduleinstall_installedmoduledeprecated) | 安装模块信息。 |
| typedef struct [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) [ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#moduleinstall_fetchmodulesresultdeprecated) | 安装模块结果。 |
| typedef struct [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) | 模块安装状态回调。 |
| typedef void [ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallbackdeprecated) | 监听回调函数。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| typedef enum [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) {  E\_NO\_ERROR = 0,  E\_PARAMS = 401,  E\_QUERY\_MODULE = 1006500001,  E\_REPEATED\_CALL = 1006500002,  E\_CONNECT\_SA = 1006500004,  E\_OFF\_WITHOUT\_ON = 1006500006,  E\_CONNECT\_SERVICE\_EXTENSION = 1006500007,  E\_WRITE\_PARAM = 1006500008,  E\_REQUEST\_SERVER = 1006500009,  E\_RESPONSE\_INVALID = 1006500010,  E\_INNER\_ERROR = 1006500011,  E\_INTERNAL\_COMMUNICATION = 1006500012,  E\_INVALID\_TASK\_ID = 1006500013  } | 枚举错误码。 |
| typedef enum [ModuleInstall\_InstallStatus](store-c-moduleinstall.md#moduleinstall_installstatusdeprecated) {  INSTALLED = 0,  NOT\_INSTALLED = 1  } | 枚举安装状态。 |
| typedef enum [ModuleInstall\_RequestCode](store-c-moduleinstall.md#moduleinstall_requestcodedeprecated) {  MODULE\_ALREADY\_EXISTS = -8,  MODULE\_UNAVAILABLE = -7,  INVALID\_REQUEST = -6,  NETWORK\_ERROR = -5,  INVOKER\_VERIFICATION\_FAILED = -4,  FOREGROUND\_REQUIRED = -3,  ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2,  FAILURE = -1,  SUCCESS = 0,  DOWNLOAD\_WAIT\_WIFI = 1  } | 枚举请求码。 |
| typedef enum [ModuleInstall\_TaskStatus](store-c-moduleinstall.md#moduleinstall_taskstatusdeprecated) {  CREATE\_TASK\_FAILED = -4,  HIGHER\_VERSION\_INSTALLED = -3,  TASK\_ALREADY\_EXISTS = -2,  TASK\_UNFOUND = -1,  TASK\_CREATED = 0,  DOWNLOADING = 1,  DOWNLOAD\_PAUSED = 2,  DOWNLOAD\_WAITING = 3,  DOWNLOAD\_SUCCESSFUL = 4,  DOWNLOAD\_FAILED = 5,  DOWNLOAD\_WAIT\_FOR\_WIFI = 6,  INSTALL\_WAITING = 20,  INSTALLING = 21,  INSTALL\_SUCCESSFUL = 22,  INSTALL\_FAILED = 23  } | 枚举任务状态。 |

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
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_ShowCellularDataConfirmation](store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationdeprecated)(const char \*taskId, unsigned int length, unsigned int showResult) | 向用户展示流量提醒弹窗。 |
| [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*[HMS\_ModuleInstall\_CreateStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_createstatuscallbackdeprecated)([ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#moduleinstall_onstatuscallbackdeprecated) \*onStatusCallback) | 创建下载进度监听回调。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_On](store-c-moduleinstall.md#hms_moduleinstall_ondeprecated)(const char \*bundleName, unsigned int length, unsigned int appIndex, unsigned int period, [ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*\*callback) | 下载进度监听。 |
| void [HMS\_ModuleInstall\_ReleaseStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_releasestatuscallbackdeprecated)([ModuleInstall\_StatusCallback](store-c-moduleinstall.md#moduleinstall_statuscallbackdeprecated) \*statusCallback) | 释放下载进度监听回调。 |
| [ModuleInstall\_ErrCode](store-c-moduleinstall.md#moduleinstall_errcodedeprecated) [HMS\_ModuleInstall\_Off](store-c-moduleinstall.md#hms_moduleinstall_offdeprecated)(const char \*bundleName, unsigned int length, unsigned int appIndex) | 取消下载进度监听。 |
