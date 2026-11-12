---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-moduleinstall_c
title: 产品特性按需分发(C/C++)
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 产品特性按需分发 > 产品特性按需分发(C/C++)
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:19+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a3b02b8f40403fe98be357b891985e483885c02d6bb1009de6e7c7680b8a6255
---

26.0.0版本开始，新增暂停下载任务接口，支持用户暂停下载任务。

## 场景介绍

随着HarmonyOS应用的持续发展，应用的功能将越来越丰富，实际上80%的用户使用时长都会集中在20%的特性上，其余的功能可能也仅仅是面向部分用户。为了避免用户首次下载应用耗时过长，及过多占用用户空间，应用市场服务提供按需分发的能力，支持用户按需动态下载自己所需的增强特性。

## 基本概念

按需分发：一个应用程序被打包成多个安装包，安装包包含了所有的应用程序代码和静态资源。用户从应用市场下载的应用只包含基本功能的安装包，当用户需要使用增强功能时，相应安装包将会从服务器下载到设备上。

## 约束与限制

* 应用需要上架应用市场。
* 产品特性按需分发功能支持Phone、Tablet、PC/2in1设备。从5.1.1(19)版本开始，新增支持TV设备；并且从API版本26.0.1开始，新增支持Car设备。
* 使用按需分发前，需先将应用拆分为基础包与增强功能模块，详细操作请参考[模块管理](ide-module-management.md)。

## 接口说明

产品特性按需分发场景提供以下C接口，具体API说明详见[ModuleInstall](../harmonyos-references/store-c-moduleinstall.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_GetInstalledModuleV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulev2)(const char \*moduleName, unsigned int length, [HMS\_ModuleInstall\_InstalledModule](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*\*installedModule) | 查询模块是否安装。 |
| char \*[HMS\_ModuleInstall\_GetInstalledModuleNameV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulenamev2)(const [HMS\_ModuleInstall\_InstalledModule](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule) | 获取模块名。 |
| int [HMS\_ModuleInstall\_GetInstalledModuleTypeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletypev2)(const [HMS\_ModuleInstall\_InstalledModule](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule) | 获取模块类型。 |
| [HMS\_ModuleInstall\_InstallStatus](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_installstatus) [HMS\_ModuleInstall\_GetModuleInstallStatusV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatusv2)(const [HMS\_ModuleInstall\_InstalledModule](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_installedmodule) \*installedModule) | 获取模块安装状态。 |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_FetchModulesV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesv2)(const char \*bundleName, unsigned int length, char \*\*moduleNames, unsigned int moduleNamesLength, [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*\*fetchModulesResult) | 请求下载模块。 |
| [HMS\_ModuleInstall\_RequestCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_requestcode) [HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcodev2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载请求码。 |
| [HMS\_ModuleInstall\_TaskStatus](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_taskstatus) [HMS\_ModuleInstall\_GetFetchModulesTaskStatusV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatusv2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载任务状态。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesTaskIdV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskidv2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载任务id。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesDescV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdescv2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载描述。 |
| char \*[HMS\_ModuleInstall\_GetFetchModulesV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesv2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载模块名。 |
| int [HMS\_ModuleInstall\_GetFetchModulesTotalSizeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsizev2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载总大小。 |
| int [HMS\_ModuleInstall\_GetFetchModulesDownloadedSizeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsizev2)(const [HMS\_ModuleInstall\_FetchModulesResult](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesresult) \*fetchModulesResult) | 获取模块下载已下载大小。 |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_CancelTaskV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_canceltaskv2)(const char \*taskId, unsigned int length, unsigned int cancelResult) | 取消下载任务。 |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_ShowCellularDataConfirmationV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationv2)(const char \*taskId, unsigned int length, unsigned int showResult) | 展示流量弹窗。 |
| [HMS\_ModuleInstall\_StatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*[HMS\_ModuleInstall\_CreateStatusCallbackV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_createstatuscallbackv2)([HMS\_ModuleInstall\_OnStatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_onstatuscallback) \*onStatusCallback) | 创建下载进度监听回调。 |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_OnV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_onv2)(const char \*bundleName, unsigned int length, unsigned int appIndex, unsigned int period, [HMS\_ModuleInstall\_StatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*\*callback) | 下载进度监听。 |
| void [HMS\_ModuleInstall\_ReleaseStatusCallbackV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_releasestatuscallbackv2)([HMS\_ModuleInstall\_StatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_statuscallback) \*statusCallback) | 释放监听下载进度的回调。 |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_OffV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_offv2)(const char \*bundleName, unsigned int length, unsigned int appIndex) | 取消下载进度监听。 |
| [HMS\_ModuleInstall\_ErrCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_errcode) [HMS\_ModuleInstall\_PauseTaskV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_pausetaskv2)(const char \*taskId) | 暂停下载任务。 |

## 使用指导

应用要使用ModuleInstall提供的按需分发能力，需要添加对应的头文件。

### 在CMake脚本中链接动态库

```text
target_link_libraries(entry PUBLIC ${module_install_lib})
```

### 添加头文件

需要开发者引入[module\_install\_v2.h](../harmonyos-references/appgallery-c-module_install_v2.md)头文件后，才可以使用按需分发相关API。

**说明** 

从API版本26.0.1开始，头文件<AppGalleryKit/module\_install.h>已废弃，请使用替代头文件<AppGalleryKit/module\_install\_v2.h>。

```
#include "AppGalleryKit/module_install_v2.h"
```

## 获取模块安装信息

在使用按需分发能力之前，需要调用[HMS\_ModuleInstall\_GetInstalledModuleV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulev2)接口查询按需分发的模块是否安装，接口调用成功后，可以通过[HMS\_ModuleInstall\_GetInstalledModuleNameV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulenamev2)、[HMS\_ModuleInstall\_GetInstalledModuleTypeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletypev2)、[HMS\_ModuleInstall\_GetModuleInstallStatusV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatusv2)接口分别获取模块名称、模块类型、模块安装状态信息。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_GetInstalledModule、HMS\_ModuleInstall\_GetInstalledModuleName、HMS\_ModuleInstall\_GetInstalledModuleType、HMS\_ModuleInstall\_GetModuleInstallStatus接口已废弃，请分别使用HMS\_ModuleInstall\_GetInstalledModuleV2、HMS\_ModuleInstall\_GetInstalledModuleNameV2、HMS\_ModuleInstall\_GetInstalledModuleTypeV2、HMS\_ModuleInstall\_GetModuleInstallStatusV2接口替代。

```
char *moduleName;
HMS_ModuleInstall_InstalledModule *installedModule;
HMS_ModuleInstall_ErrCode ret =
    HMS_ModuleInstall_GetInstalledModuleV2(moduleName, strlen(moduleName), &installedModule);
if (ret == HMS_MODULEINSTALL_NO_ERROR) {
    char *installedModuleName = HMS_ModuleInstall_GetInstalledModuleNameV2(installedModule);
    int moduleType = HMS_ModuleInstall_GetInstalledModuleTypeV2(installedModule);
    int installStatus = HMS_ModuleInstall_GetModuleInstallStatusV2(installedModule);
}
if (installedModule != nullptr) {
    installedModule = nullptr;
}
```

## 按需加载模块

应用可以通过[HMS\_ModuleInstall\_FetchModulesV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesv2)按需加载模块，接口调用成功之后可以通过[HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcodev2)、[HMS\_ModuleInstall\_GetFetchModulesTaskStatusV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatusv2)、[HMS\_ModuleInstall\_GetFetchModulesTaskIdV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskidv2)、[HMS\_ModuleInstall\_GetFetchModulesDescV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdescv2)、[HMS\_ModuleInstall\_GetFetchModulesV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesv2)、[HMS\_ModuleInstall\_GetFetchModulesTotalSizeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsizev2)、[HMS\_ModuleInstall\_GetFetchModulesDownloadedSizeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsizev2)接口获取模块下载相关信息。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_FetchModules、HMS\_ModuleInstall\_GetFetchModulesRequestCode、HMS\_ModuleInstall\_GetFetchModulesTaskStatus、HMS\_ModuleInstall\_GetFetchModulesTaskId、HMS\_ModuleInstall\_GetFetchModulesDesc、HMS\_ModuleInstall\_GetFetchModules、HMS\_ModuleInstall\_GetFetchModulesTotalSize、HMS\_ModuleInstall\_GetFetchModulesDownloadedSize接口已废弃，请分别使用MS\_ModuleInstall\_FetchModulesV2、HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2、HMS\_ModuleInstall\_GetFetchModulesTaskStatusV2、HMS\_ModuleInstall\_GetFetchModulesTaskIdV2、HMS\_ModuleInstall\_GetFetchModulesDescV2、HMS\_ModuleInstall\_GetFetchModulesV2、HMS\_ModuleInstall\_GetFetchModulesTotalSizeV2、HMS\_ModuleInstall\_GetFetchModulesDownloadedSizeV2接口替代。

```
char *bundleName;
unsigned int arraySize = 1;
// ...
char **moduleNames = new char *[arraySize];
for (int i = 0; i < arraySize; i++) {
    moduleNames[i] = new char[256];
}
// ...
HMS_ModuleInstall_FetchModulesResult *fetchModulesResult;
HMS_ModuleInstall_ErrCode ret =
    HMS_ModuleInstall_FetchModulesV2(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
// ...
if (ret == HMS_MODULEINSTALL_NO_ERROR) {
    HMS_ModuleInstall_RequestCode code = HMS_ModuleInstall_GetFetchModulesRequestCodeV2(fetchModulesResult);
    HMS_ModuleInstall_TaskStatus taskStatus = HMS_ModuleInstall_GetFetchModulesTaskStatusV2(fetchModulesResult);
    char *taskId = HMS_ModuleInstall_GetFetchModulesTaskIdV2(fetchModulesResult);
    char *desc = HMS_ModuleInstall_GetFetchModulesDescV2(fetchModulesResult);
    char *modules = HMS_ModuleInstall_GetFetchModulesV2(fetchModulesResult);
    int totalSize = HMS_ModuleInstall_GetFetchModulesTotalSizeV2(fetchModulesResult);
    int downloadedSize = HMS_ModuleInstall_GetFetchModulesDownloadedSizeV2(fetchModulesResult);
    // ...
}
if (moduleNames != nullptr) {
    delete[] moduleNames;
    moduleNames = nullptr;
}
if (fetchModulesResult != nullptr) {
    delete fetchModulesResult;
    fetchModulesResult = nullptr;
}
```

## 暂停下载任务

调用[HMS\_ModuleInstall\_PauseTaskV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_pausetaskv2)接口暂停下载任务。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_PauseTask接口已废弃，请使用HMS\_ModuleInstall\_PauseTaskV2接口替代。

```
char *taskId; // 下载任务id
// ...
HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_PauseTaskV2(taskId);
if (ret == HMS_MODULEINSTALL_NO_ERROR) {
    // 暂停下载成功
}
```

## 恢复下载任务

使用[HMS\_ModuleInstall\_PauseTaskV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_pausetaskv2)接口暂停下载任务后，可通过调用[HMS\_ModuleInstall\_FetchModulesV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodulesv2)接口实现下载任务从中断处继续下载。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_PauseTask、HMS\_ModuleInstall\_FetchModules接口已废弃，请分别使用HMS\_ModuleInstall\_PauseTaskV2、HMS\_ModuleInstall\_FetchModulesV2接口替代。

```
#include <cstring>
#include "AppGalleryKit/module_install_v2.h"

// ...

// 暂停下载任务
void PauseTask() {
    char *taskId;
    HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_PauseTaskV2(taskId);
    if (ret == HMS_MODULEINSTALL_NO_ERROR) {
        // 暂停下载成功
    }
}

// 恢复下载任务
void FetchModules() {
    char *bundleName;
    int arraySize = 1;
    char **moduleNames = new char *[arraySize];
    for (int i = 0; i < arraySize; i++) {
        moduleNames[i] = new char[256];
    }
    HMS_ModuleInstall_FetchModulesResult *fetchModulesResult;
    HMS_ModuleInstall_ErrCode ret =
        HMS_ModuleInstall_FetchModulesV2(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
    if (ret == HMS_MODULEINSTALL_NO_ERROR) {
        HMS_ModuleInstall_TaskStatus taskStatus = HMS_ModuleInstall_GetFetchModulesTaskStatusV2(fetchModulesResult);
        char *taskId = HMS_ModuleInstall_GetFetchModulesTaskIdV2(fetchModulesResult);
        HMS_ModuleInstall_RequestCode code = HMS_ModuleInstall_GetFetchModulesRequestCodeV2(fetchModulesResult);
        if (code == HMS_MODULEINSTALL_CODE_DOWNLOAD_WAIT_WIFI) {
            int showResult;
            HMS_ModuleInstall_ErrCode ret =
                HMS_ModuleInstall_ShowCellularDataConfirmationV2(taskId, strlen(taskId), showResult);
        }
        char *desc = HMS_ModuleInstall_GetFetchModulesDescV2(fetchModulesResult);
        char *modules = HMS_ModuleInstall_GetFetchModulesV2(fetchModulesResult);
        int totalSize = HMS_ModuleInstall_GetFetchModulesTotalSizeV2(fetchModulesResult);
        int downloadedSize = HMS_ModuleInstall_GetFetchModulesDownloadedSizeV2(fetchModulesResult);
    }
    if (moduleNames != nullptr) {
        for (int i = 0; i < arraySize; i++) {
            delete[] moduleNames[i];
        }
        delete[] moduleNames;
        moduleNames = nullptr;
    }
    if (fetchModulesResult != nullptr) {
        delete fetchModulesResult;
        fetchModulesResult = nullptr;
    }
}
```

## 取消下载任务

调用[HMS\_ModuleInstall\_CancelTaskV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_canceltaskv2)接口取消下载任务。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_CancelTask接口已废弃，请使用HMS\_ModuleInstall\_CancelTaskV2接口替代。

```
char *taskId;     // 下载任务id
int cancelResult = 0; // 取消下载结果
// ...
HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_CancelTaskV2(taskId, strlen(taskId), cancelResult);
if (ret == HMS_MODULEINSTALL_NO_ERROR && cancelResult == 0) {
    // 取消下载成功
}
```

## 向用户展示流量弹窗

如果调用[HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcodev2)接口返回HMS\_MODULEINSTALL\_CODE\_DOWNLOAD\_WAIT\_WIFI时，需要调用[HMS\_ModuleInstall\_ShowCellularDataConfirmationV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmationv2)接口向用户展示流量弹窗。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_GetFetchModulesRequestCode、HMS\_ModuleInstall\_ShowCellularDataConfirmation接口已废弃，请分别使用HMS\_ModuleInstall\_GetFetchModulesRequestCodeV2、HMS\_ModuleInstall\_ShowCellularDataConfirmationV2接口替代。

```
char *taskId;   // 下载任务id
int showResult = 0; // 展示流量弹窗结果
// ...
HMS_ModuleInstall_ErrCode ret =
    HMS_ModuleInstall_ShowCellularDataConfirmationV2(taskId, strlen(taskId), showResult);
if (ret == HMS_MODULEINSTALL_NO_ERROR && showResult == 0) {
    // 展示流量弹窗成功
}
```

## 监听下载任务

### 定义回调函数以处理下载任务状态通知

```
void onEvent(char *bundleName, char *eventInfo) {
    // 回调处理
    // ...
}
```

### 初始化下载进度回调

应用可以通过[HMS\_ModuleInstall\_CreateStatusCallbackV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_createstatuscallbackv2)初始化下载进度回调。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_CreateStatusCallback接口已标记为废弃，请使用HMS\_ModuleInstall\_CreateStatusCallbackV2接口替代。

```
HMS_ModuleInstall_StatusCallback *statusCallback;
HMS_ModuleInstall_OnStatusCallback onStatusCallback = onEvent;
statusCallback = HMS_ModuleInstall_CreateStatusCallbackV2(&onStatusCallback);
```

### 监听下载进度

应用可以通过[HMS\_ModuleInstall\_OnV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_onv2)接口监听下载进度。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_On接口已废弃，请使用HMS\_ModuleInstall\_OnV2接口替代。

```
char *bundleName; // 应用包名
int appIndex;     // 应用分身索引
int period;       // 监听周期
// ...
HMS_ModuleInstall_ErrCode ret =
    HMS_ModuleInstall_OnV2(bundleName, strlen(bundleName), appIndex, period, &statusCallback);
```

## 取消监听下载任务

应用可以通过[HMS\_ModuleInstall\_OffV2](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_offv2)接口取消下载进度监听。

**说明** 

从API版本26.0.1开始，HMS\_ModuleInstall\_Off接口已废弃，请使用HMS\_ModuleInstall\_OffV2接口替代。

```
char *bundleName; // 应用包名
int appIndex;     // 应用分身索引
// ...
HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_OffV2(bundleName, strlen(bundleName), appIndex);
if (ret == HMS_MODULEINSTALL_NO_ERROR) {
    // 取消监听成功
}
```

## 完整示例

参考以下示例，完成应用按需分发过程。

```
#include <cstring>
#include "AppGalleryKit/module_install_v2.h"

void GetInstalledModule() {
    char *moduleName;
    HMS_ModuleInstall_InstalledModule *installedModule;
    HMS_ModuleInstall_ErrCode ret =
        HMS_ModuleInstall_GetInstalledModuleV2(moduleName, strlen(moduleName), &installedModule);
    if (ret == HMS_MODULEINSTALL_NO_ERROR) {
        char *installedModuleName = HMS_ModuleInstall_GetInstalledModuleNameV2(installedModule);
        int moduleType = HMS_ModuleInstall_GetInstalledModuleTypeV2(installedModule);
        int installStatus = HMS_ModuleInstall_GetModuleInstallStatusV2(installedModule);
    }
    if (installedModule != nullptr) {
        installedModule = nullptr;
    }
}

void ShowCellularDataConfirmation(char *taskId) {
    int showResult;
    HMS_ModuleInstall_ErrCode ret =
        HMS_ModuleInstall_ShowCellularDataConfirmationV2(taskId, strlen(taskId), showResult);
}

void CancelTask() {
    char *taskId;
    int cancelResult;
    HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_CancelTaskV2(taskId, strlen(taskId), cancelResult);
}

// 暂停下载任务
void PauseTask() {
    char *taskId;
    HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_PauseTaskV2(taskId);
    if (ret == HMS_MODULEINSTALL_NO_ERROR) {
        // 暂停下载成功
    }
}

// 恢复下载任务
void FetchModules() {
    char *bundleName;
    int arraySize = 1;
    char **moduleNames = new char *[arraySize];
    for (int i = 0; i < arraySize; i++) {
        moduleNames[i] = new char[256];
    }
    HMS_ModuleInstall_FetchModulesResult *fetchModulesResult;
    HMS_ModuleInstall_ErrCode ret =
        HMS_ModuleInstall_FetchModulesV2(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
    if (ret == HMS_MODULEINSTALL_NO_ERROR) {
        HMS_ModuleInstall_TaskStatus taskStatus = HMS_ModuleInstall_GetFetchModulesTaskStatusV2(fetchModulesResult);
        char *taskId = HMS_ModuleInstall_GetFetchModulesTaskIdV2(fetchModulesResult);
        HMS_ModuleInstall_RequestCode code = HMS_ModuleInstall_GetFetchModulesRequestCodeV2(fetchModulesResult);
        if (code == HMS_MODULEINSTALL_CODE_DOWNLOAD_WAIT_WIFI) {
            int showResult;
            HMS_ModuleInstall_ErrCode ret =
                HMS_ModuleInstall_ShowCellularDataConfirmationV2(taskId, strlen(taskId), showResult);
        }
        char *desc = HMS_ModuleInstall_GetFetchModulesDescV2(fetchModulesResult);
        char *modules = HMS_ModuleInstall_GetFetchModulesV2(fetchModulesResult);
        int totalSize = HMS_ModuleInstall_GetFetchModulesTotalSizeV2(fetchModulesResult);
        int downloadedSize = HMS_ModuleInstall_GetFetchModulesDownloadedSizeV2(fetchModulesResult);
    }
    if (moduleNames != nullptr) {
        for (int i = 0; i < arraySize; i++) {
            delete[] moduleNames[i];
        }
        delete[] moduleNames;
        moduleNames = nullptr;
    }
    if (fetchModulesResult != nullptr) {
        delete fetchModulesResult;
        fetchModulesResult = nullptr;
    }
}

void onEvent(char *bundleName, char *eventInfo) {
    // ...
}

void On() {
    char *bundleName;
    int appIndex;
    int period;
    HMS_ModuleInstall_StatusCallback *statusCallback;
    HMS_ModuleInstall_OnStatusCallback onStatusCallback = onEvent;
    statusCallback = HMS_ModuleInstall_CreateStatusCallbackV2(&onStatusCallback);
    HMS_ModuleInstall_ErrCode ret =
        HMS_ModuleInstall_OnV2(bundleName, strlen(bundleName), appIndex, period, &statusCallback);
}

void Off() {
    char *bundleName;
    int appIndex;
    HMS_ModuleInstall_ErrCode ret = HMS_ModuleInstall_OffV2(bundleName, strlen(bundleName), appIndex);
}
```
