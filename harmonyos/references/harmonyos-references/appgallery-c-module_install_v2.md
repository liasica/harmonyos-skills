---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-c-module_install_v2
title: module_install_v2.h
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > C API > 头文件 > module_install_v2.h
category: harmonyos-references
scraped_at: 2026-11-12T09:57:13+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2f6a575be45eaccc07a4e15a953146c228bac5b0b1334c76407ad0b21e84382f
---

## 概述

声明按需分发能力的API。

**引用文件：** <AppGalleryKit/module\_install\_v2.h>

**库：** libhmsmoduleinstall.so

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 26.0.1

**相关模块：** [ModuleInstall](store-c-moduleinstall.md)

## 汇总

### 类型

| 名称 | 描述 |
| --- | --- |
| typedef struct [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) [HMS\_ModuleInstall\_InstalledModule](store-c-moduleinstall.md#hms_moduleinstall_installedmodule) | 安装模块信息。 |
| typedef struct [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) [HMS\_ModuleInstall\_FetchModulesResult](store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) | 安装模块结果。 |
| typedef struct [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) [HMS\_ModuleInstall\_StatusCallback](store-c-moduleinstall.md#hms_moduleinstall_statuscallback) | 模块安装状态回调。 |
| typedef void (\*[HMS\_ModuleInstall\_OnStatusCallback](store-c-moduleinstall.md#hms_moduleinstall_onstatuscallback))(char \*bundleName, char \*eventInfo) | 监听回调函数。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| typedef enum [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) {  HMS\_MODULEINSTALL\_NO\_ERROR = 0,  HMS\_MODULEINSTALL\_PARAM\_INVALID = 401,  HMS\_MODULEINSTALL\_QUERY\_MODULE\_FAILED = 1006500001,  HMS\_MODULEINSTALL\_REPEATED\_CALL = 1006500002,  HMS\_MODULEINSTALL\_CONNECT\_SA\_FAILED= 1006500004,  HMS\_MODULEINSTALL\_OFF\_WITHOUT\_ON\_FAILED = 1006500006,  HMS\_MODULEINSTALL\_CONNECT\_SERVICE\_FAILED = 1006500007,  HMS\_MODULEINSTALL\_WRITE\_PARAM\_FAILED = 1006500008,  HMS\_MODULEINSTALL\_REQUEST\_SERVER\_FAILED = 1006500009,  HMS\_MODULEINSTALL\_RESPONSE\_INVALID\_FAILED = 1006500010,  HMS\_MODULEINSTALL\_INNER\_ERROR = 1006500011,  HMS\_MODULEINSTALL\_INTERNAL\_COMMUNICATION\_FAILED= 1006500012,  HMS\_MODULEINSTALL\_TASK\_ID\_INVALID = 1006500013  } | 枚举错误码。 |
| typedef enum [HMS\_ModuleInstall\_InstallStatus](store-c-moduleinstall.md#hms_moduleinstall_installstatus) {  HMS\_MODULEINSTALL\_STATUS\_INSTALLED = 0,  HMS\_MODULEINSTALL\_STATUS\_NOT\_INSTALLED = 1  } | 枚举安装状态。 |
| typedef enum [HMS\_ModuleInstall\_RequestCode](store-c-moduleinstall.md#hms_moduleinstall_requestcode) {  HMS\_MODULEINSTALL\_CODE\_MODULE\_ALREADY\_EXISTS = -8,  HMS\_MODULEINSTALL\_CODE\_MODULE\_UNAVAILABLE = -7,  HMS\_MODULEINSTALL\_CODE\_INVALID\_REQUEST = -6,  HMS\_MODULEINSTALL\_CODE\_NETWORK\_ERROR = -5,  HMS\_MODULEINSTALL\_CODE\_INVALID\_INVOKER = -4,  HMS\_MODULEINSTALL\_CODE\_FOREGROUND\_REQUIRED = -3,  HMS\_MODULEINSTALL\_CODE\_ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2,  HMS\_MODULEINSTALL\_CODE\_FAILURE = -1,  HMS\_MODULEINSTALL\_CODE\_SUCCESS = 0,  HMS\_MODULEINSTALL\_CODE\_DOWNLOAD\_WAIT\_WIFI = 1  } | 枚举请求码。 |
| typedef enum [HMS\_ModuleInstall\_TaskStatus](store-c-moduleinstall.md#hms_moduleinstall_taskstatus) {  HMS\_MODULEINSTALL\_TASK\_CREATE\_FAILED = -4,  HMS\_MODULEINSTALL\_TASK\_HIGHER\_VERSION\_INSTALLED = -3,  HMS\_MODULEINSTALL\_TASK\_ALREADY\_EXISTS= -2,  HMS\_MODULEINSTALL\_TASK\_UNFOUND = -1,  HMS\_MODULEINSTALL\_TASK\_CREATED = 0,  HMS\_MODULEINSTALL\_TASK\_DOWNLOADING = 1,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_PAUSED = 2,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_WAITING = 3,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_SUCCESSFUL = 4,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_FAILED = 5,  HMS\_MODULEINSTALL\_TASK\_DOWNLOAD\_WAIT\_FOR\_WIFI = 6,  HMS\_MODULEINSTALL\_TASK\_INSTALL\_WAITING = 20,  HMS\_MODULEINSTALL\_TASK\_INSTALLING = 21,  HMS\_MODULEINSTALL\_TASK\_INSTALL\_SUCCESSFUL = 22,  HMS\_MODULEINSTALL\_TASK\_INSTALL\_FAILED = 23  } | 枚举任务状态。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [HMS\_ModuleInstall\_ErrCode](store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_GetInstalledModuleV2](store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulev2)(const char \*moduleName, unsigned int length, HMS\_ModuleInstall\_InstalledModule \*\*installedModule) | 查询模块是否安装。 |
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
