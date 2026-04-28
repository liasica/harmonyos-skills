---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-moduleinstall_c
title: 产品特性按需分发(C/C++)
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 产品特性按需分发 > 产品特性按需分发(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9c8e16c2e1c6d75ac0199df9ea861309411124283c87352d51f5d1f72957a644
---

## 场景介绍

随着HarmonyOS应用的持续发展，应用的功能将越来越丰富，实际上80%的用户使用时长都会集中在20%的特性上，其余的功能可能也仅仅是面向部分用户。为了避免用户首次下载应用耗时过长，及过多占用用户空间，应用市场服务提供按需分发的能力，支持用户按需动态下载自己所需的增强特性。

## 基本概念

按需分发：一个应用程序被打包成多个安装包，安装包包含了所有的应用程序代码和静态资源。用户从应用市场下载的应用只包含基本功能的安装包，当用户需要使用增强功能时，相应安装包将会从服务器下载到设备上。

## 约束与限制

* 应用需要上架应用市场。
* 产品特性按需分发功能支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。

## 接口说明

产品特性按需分发场景提供以下C接口，具体API说明详见[ModuleInstall](../harmonyos-references/store-c-moduleinstall.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_ModuleInstall\_GetInstalledModule](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodule) | 查询模块是否安装。 |
| [HMS\_ModuleInstall\_GetInstalledModuleName](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulename) | 获取模块名。 |
| [HMS\_ModuleInstall\_GetInstalledModuleType](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletype) | 获取模块类型。 |
| [HMS\_ModuleInstall\_GetModuleInstallStatus](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatus) | 获取模块安装状态。 |
| [HMS\_ModuleInstall\_FetchModules](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodules) | 请求下载模块。 |
| [HMS\_ModuleInstall\_GetFetchModulesRequestCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcode) | 获取模块下载请求码。 |
| [HMS\_ModuleInstall\_GetFetchModulesTaskStatus](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatus) | 获取模块下载任务状态。 |
| [HMS\_ModuleInstall\_GetFetchModulesTaskId](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskid) | 获取模块下载任务id。 |
| [HMS\_ModuleInstall\_GetFetchModulesDesc](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdesc) | 获取模块下载描述。 |
| [HMS\_ModuleInstall\_GetFetchModules](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodules) | 获取模块下载模块名。 |
| [HMS\_ModuleInstall\_GetFetchModulesTotalSize](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsize) | 获取模块下载总大小。 |
| [HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsize) | 获取模块下载已下载大小。 |
| [HMS\_ModuleInstall\_CancelTask](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_canceltask) | 取消下载任务。 |
| [HMS\_ModuleInstall\_ShowCellularDataConfirmation](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmation) | 展示流量弹窗。 |
| [HMS\_ModuleInstall\_CreateStatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_createstatuscallback) | 创建下载进度监听回调。 |
| [HMS\_ModuleInstall\_On](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_on) | 下载进度监听。 |
| [HMS\_ModuleInstall\_ReleaseStatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_releasestatuscallback) | 释放下载进度监听回调。 |
| [HMS\_ModuleInstall\_Off](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_off) | 取消下载进度监听。 |

## 使用指导

应用要使用ModuleInstall提供的按需分发能力，需要添加对应的头文件。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libhmsmoduleinstall.so)
```

### 添加头文件

需要开发者引入[module\_install.h](../harmonyos-references/store-c-module_install.md)头文件后，才可以使用按需分发相关API。

```
1. #include "AppGalleryKit/module_install.h"
```

## 获取模块安装信息

在使用按需分发能力之前，需要调用[HMS\_ModuleInstall\_GetInstalledModule](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodule)接口查询按需分发的模块是否安装，接口调用成功后，可以通过[HMS\_ModuleInstall\_GetInstalledModuleName](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmodulename)、[HMS\_ModuleInstall\_GetInstalledModuleType](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getinstalledmoduletype)、[HMS\_ModuleInstall\_GetModuleInstallStatus](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getmoduleinstallstatus)接口分别获取模块名称、模块类型、模块安装状态信息。

```
1. char *moduleName;
2. ModuleInstall_InstalledModule *installedModule;
3. ModuleInstall_ErrCode ret = HMS_ModuleInstall_GetInstalledModule(moduleName, strlen(moduleName), &installedModule);
4. if (ret == E_NO_ERROR) {
5. char *installedModuleName = HMS_ModuleInstall_GetInstalledModuleName(installedModule);
6. int moduleType = HMS_ModuleInstall_GetInstalledModuleType(installedModule);
7. int installStatus = HMS_ModuleInstall_GetModuleInstallStatus(installedModule);
8. }
9. if (installedModule != nullptr) {
10. delete installedModule;
11. installedModule = nullptr;
12. }
```

## 按需加载模块

应用可以通过[HMS\_ModuleInstall\_FetchModules](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_fetchmodules)按需加载模块，接口调用成功之后可以通过[HMS\_ModuleInstall\_GetFetchModulesRequestCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcode)、[HMS\_ModuleInstall\_GetFetchModulesTaskStatus](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskstatus)、[HMS\_ModuleInstall\_GetFetchModulesTaskId](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskid)、[HMS\_ModuleInstall\_GetFetchModulesDesc](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdesc)、[HMS\_ModuleInstall\_GetFetchModules](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodules)、[HMS\_ModuleInstall\_GetFetchModulesTotalSize](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestotalsize)、[HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesdownloadedsize)接口获取模块下载相关信息。

```
1. char *bundleName;
2. int arraySize = 1;
3. char** moduleNames = new char*[arraySize];
4. for (int i = 0; i < arraySize; i++) {
5. moduleNames[i] = new char[256];
6. }
7. ModuleInstall_FetchModulesResult *fetchModulesResult;
8. ModuleInstall_ErrCode ret = HMS_ModuleInstall_FetchModules(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
9. if (ret == E_NO_ERROR) {
10. ModuleInstall_RequestCode code = HMS_ModuleInstall_GetFetchModulesRequestCode(fetchModulesResult);
11. ModuleInstall_TaskStatus taskStatus = HMS_ModuleInstall_GetFetchModulesTaskStatus(fetchModulesResult);
12. char *taskId = HMS_ModuleInstall_GetFetchModulesTaskId(fetchModulesResult);
13. char *desc = HMS_ModuleInstall_GetFetchModulesDesc(fetchModulesResult);
14. char *modules = HMS_ModuleInstall_GetFetchModules(fetchModulesResult);
15. int totalSize = HMS_ModuleInstall_GetFetchModulesTotalSize(fetchModulesResult);
16. int downloadedSize = HMS_ModuleInstall_GetFetchModulesDownloadedSize(fetchModulesResult);
17. }
18. if (moduleNames != nullptr) {
19. delete[] moduleNames;
20. moduleNames = nullptr;
21. }
22. if (fetchModulesResult != nullptr) {
23. delete fetchModulesResult;
24. fetchModulesResult = nullptr;
25. }
```

## 取消下载任务

如果需要取消下载，应用可以调用[HMS\_ModuleInstall\_CancelTask](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_canceltask)接口取消下载任务，其中taskId是调用[HMS\_ModuleInstall\_GetFetchModulesTaskId](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulestaskid)接口返回的taskId。

```
1. char *taskId; // 下载任务id
2. int cancelResult; // 取消下载结果
3. ModuleInstall_ErrCode ret = HMS_ModuleInstall_CancelTask(taskId, strlen(taskId), cancelResult);
4. if (ret == E_NO_ERROR && cancelResult == 0) {
5. // 取消下载成功
6. }
```

## 展示流量弹窗

如果调用[HMS\_ModuleInstall\_GetFetchModulesRequestCode](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_getfetchmodulesrequestcode)接口返回DOWNLOAD\_WAIT\_WIFI时，需要调用[HMS\_ModuleInstall\_ShowCellularDataConfirmation](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_showcellulardataconfirmation)接口展示流量弹窗。

```
1. char *taskId; // 下载任务id
2. int showResult; // 展示流量弹窗结果
3. ModuleInstall_ErrCode ret = HMS_ModuleInstall_ShowCellularDataConfirmation(taskId, strlen(taskId), showResult);
4. if (ret == E_NO_ERROR && showResult == 0) {
5. // 展示流量弹窗成功
6. }
```

## 监听下载任务

### 定义监听下载回调函数

```
1. void onEvent(char *bundleName, char *eventInfo) {
2. // 回调处理
3. }
```

### 初始化下载进度回调

应用可以通过[HMS\_ModuleInstall\_CreateStatusCallback](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_createstatuscallback)初始化下载进度回调。

```
1. ModuleInstall_StatusCallback *statusCallback;
2. ModuleInstall_OnStatusCallback onStatusCallback = onEvent;
3. statusCallback = HMS_ModuleInstall_CreateStatusCallback(&onStatusCallback);
```

### 监听下载进度

应用可以通过[HMS\_ModuleInstall\_On](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_on)接口监听下载进度。

```
1. char *bundleName; // 应用包名
2. int appIndex; // 应用分身索引
3. int period; // 监听周期
4. ModuleInstall_ErrCode ret = HMS_ModuleInstall_On(bundleName, strlen(bundleName), appIndex, period, &statusCallback);
```

## 取消监听下载任务

应用可以通过[HMS\_ModuleInstall\_Off](../harmonyos-references/store-c-moduleinstall.md#hms_moduleinstall_off)接口取消下载进度监听。

```
1. char *bundleName; // 应用包名
2. int appIndex; // 应用分身索引
3. ModuleInstall_ErrCode ret = HMS_ModuleInstall_Off(bundleName, strlen(bundleName), appIndex);
4. if (ret == E_NO_ERROR) {
5. // 取消监听成功
6. }
```

## 完整示例

参考以下示例，完成应用按需分发过程。

```
1. #include <cstring>
2. #include "AppGalleryKit/module_install.h"

4. void GetInstalledModule() {
5. char *moduleName;
6. ModuleInstall_InstalledModule *installedModule;
7. ModuleInstall_ErrCode ret = HMS_ModuleInstall_GetInstalledModule(moduleName, strlen(moduleName), &installedModule);
8. if (ret == E_NO_ERROR) {
9. char *installedModuleName = HMS_ModuleInstall_GetInstalledModuleName(installedModule);
10. int moduleType = HMS_ModuleInstall_GetInstalledModuleType(installedModule);
11. int installStatus = HMS_ModuleInstall_GetModuleInstallStatus(installedModule);
12. }
13. if (installedModule != nullptr) {
14. delete installedModule;
15. installedModule = nullptr;
16. }
17. }

19. void ShowCellularDataConfirmation(char *taskId) {
20. int showResult;
21. ModuleInstall_ErrCode ret = HMS_ModuleInstall_ShowCellularDataConfirmation(taskId, strlen(taskId), showResult);
22. }

24. void FetchModules() {
25. char *bundleName;
26. int arraySize = 1;
27. char **moduleNames = new char *[arraySize];
28. for (int i = 0; i < arraySize; i++) {
29. moduleNames[i] = new char[256];
30. }
31. ModuleInstall_FetchModulesResult *fetchModulesResult;
32. ModuleInstall_ErrCode ret = HMS_ModuleInstall_FetchModules(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
33. if (ret == E_NO_ERROR) {
34. ModuleInstall_TaskStatus taskStatus = HMS_ModuleInstall_GetFetchModulesTaskStatus(fetchModulesResult);
35. char *taskId = HMS_ModuleInstall_GetFetchModulesTaskId(fetchModulesResult);
36. ModuleInstall_RequestCode code = HMS_ModuleInstall_GetFetchModulesRequestCode(fetchModulesResult);
37. if (code == DOWNLOAD_WAIT_WIFI) {
38. ShowCellularDataConfirmation(taskId);
39. }
40. char *desc = HMS_ModuleInstall_GetFetchModulesDesc(fetchModulesResult);
41. char *modules = HMS_ModuleInstall_GetFetchModules(fetchModulesResult);
42. int totalSize = HMS_ModuleInstall_GetFetchModulesTotalSize(fetchModulesResult);
43. int downloadedSize = HMS_ModuleInstall_GetFetchModulesDownloadedSize(fetchModulesResult);
44. }

46. if (moduleNames != nullptr) {
47. delete[] moduleNames;
48. moduleNames = nullptr;
49. }

51. if (fetchModulesResult != nullptr) {
52. delete fetchModulesResult;
53. fetchModulesResult = nullptr;
54. }
55. }

57. void CancelTask() {
58. char *taskId;
59. int cancelResult;
60. ModuleInstall_ErrCode ret = HMS_ModuleInstall_CancelTask(taskId, strlen(taskId), cancelResult);
61. }

63. void onEvent(char *bundleName, char *eventInfo) {}

65. void On() {
66. char *bundleName;
67. int appIndex;
68. int period;
69. ModuleInstall_StatusCallback *statusCallback;
70. ModuleInstall_OnStatusCallback onStatusCallback = onEvent;
71. statusCallback = HMS_ModuleInstall_CreateStatusCallback(&onStatusCallback);
72. ModuleInstall_ErrCode ret = HMS_ModuleInstall_On(bundleName, strlen(bundleName), appIndex, period, &statusCallback);
73. }

75. void Off() {
76. char *bundleName;
77. int appIndex;
78. ModuleInstall_ErrCode ret = HMS_ModuleInstall_Off(bundleName, strlen(bundleName), appIndex);
79. }
```
