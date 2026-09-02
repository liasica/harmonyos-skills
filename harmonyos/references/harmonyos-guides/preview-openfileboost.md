---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost
title: 文件打开加速（C/C++）
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 文件打开加速（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:77a9c2c4647564a6617b61b8a3ddce2397d1550f8afa7944e9503fc62ec3883b
---

从5.0.3(15)版本开始，新增文件打开加速功能。提供注册和取消注册接口，应用可以注册一系列回调，文件打开加速服务通过调用回调接口向应用推荐文件进行预加载动作。

从26.0.0版本开始，文件打开加速过程中，新增支持应用扫描文件并同步结果给加速服务，加速服务判断该文件是否具备加速条件。

从26.0.0版本起，新增动态参数配置功能，允许应用根据自身需求定制文件预加载策略（如文件后缀、大小范围）。同时，系统还提供文件打开加速服务可用性查询和文件操作事件上报功能，有助于提升预加载的准确性。

## 接口说明

具体API说明详见[文件打开加速接口文档](../harmonyos-references/openfileboost_preview.md)。

**表1** 文件预加载接口介绍（C API）

| 接口名 | 描述 |
| --- | --- |
| bool HMS\_Preview\_FileBoost\_IsSupported (void) | 查询当前设备是否支持文件打开加速功能。建议开发者在使用文件打开加速功能之前，先调用本接口检查当前设备是否支持文件打开加速功能。确认支持后再使用其他文件打开加速接口如HMS\_OpenFileBoost\_RegisterFilePreload、HMS\_Preview\_FileScanBoost\_RegisterFileScan等。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_RegisterFilePreload(  HMS\_OpenFileBoost\_QueryAppState queryAppState,  HMS\_OpenFileBoost\_OnFilePreload filePreload,  HMS\_OpenFileBoost\_OnFilePreload cancelFilePreload); | 向系统注册文件预加载回调。 |
| typedef OpenFileBoost\_AppState (\*HMS\_OpenFileBoost\_QueryAppState)(void); | 系统查询APP状态的回调函数定义。 |
| typedef OpenFileBoost\_CbErrCode (\*HMS\_OpenFileBoost\_OnFilePreload)(void\* fileInfo); | 系统向应用推荐或取消推荐预加载文件的回调函数定义。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo(  void\* fileInfo, int32\_t\* fd); | 在向应用推荐文件进行预加载或取消预加载的回调上下文中，应用通过调用该接口获取文件描述符信息。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo(  void\* fileInfo, char\* sandboxPath, int32\_t pathLen); | 在向应用推荐文件进行预加载或取消预加载的回调上下文中，应用通过调用该接口获取文件沙箱路径信息。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_UnregisterFilePreload(void); | 取消注册预加载回调。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_NotifyPreloadHit(  int32\_t fd, char\* sandboxPath, int32\_t pathLen); | 当用户打开预加载文件时，应用调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ScanOptionCreate (FileScanBoost\_ScanOption \*\*outOption) | 创建FileScanBoost\_ScanOption实例。 |
| void HMS\_Preview\_FileScanBoost\_ScanOptionDestroy (FileScanBoost\_ScanOption \*option) | 销毁FileScanBoost\_ScanOption实例。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ScanOptionAddSupportFile (FileScanBoost\_ScanOption \*option, const char \*suffix, uint32\_t suffixLen) | 向扫描选项添加支持的文件类型。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ScanResultCreate (FileScanBoost\_ScanResult \*\*outResult) | 创建FileScanBoost\_ScanResult实例。 |
| void HMS\_Preview\_FileScanBoost\_ScanResultDestroy (FileScanBoost\_ScanResult \*result) | 销毁FileScanBoost\_ScanResult实例。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ScanResultSetState (FileScanBoost\_ScanResult \*result, FileScanBoost\_ScanState state) | 在结果中设置扫描状态。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ScanResultSetMaxAtomicTime (FileScanBoost\_ScanResult \*result, int64\_t maxAtomicTime) | 在结果中设置最大原子时间。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ScanResultSetMemSize (FileScanBoost\_ScanResult \*result, int64\_t memSize) | 在结果中设置内存大小。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_RegisterFileScan (HMS\_Preview\_FileScanBoost\_OnFileScan fileScanCb, FileScanBoost\_ScanOption \*option) | 使用扩展名过滤方式注册多文件类型的回调函数。 在上一次注册结果注销之前，请勿重复注册。 重复注册将返回错误码FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED， 且仅首次注册的信息生效。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_UnregisterFileScan (void) | 移除已注册的文件扫描回调函数。 |
| FileScanBoost\_ErrCode HMS\_Preview\_FileScanBoost\_ReportScanResult (const char \*path, uint32\_t pathLen, FileScanBoost\_ScanResult \*result) | 报告文件扫描操作的完成结果。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_SupportFileCreate (const char \*suffix, uint32\_t suffixLen, uint64\_t lowerLimitKb, uint64\_t upperLimitKb, OpenFileBoost\_SupportFile \*\*outSupportFile) | 创建OpenFileBoost\_SupportFile。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_SupportFileDestroy (OpenFileBoost\_SupportFile \*supportFile) | 销毁OpenFileBoost\_SupportFile。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_OptionsCreate (OpenFileBoost\_Options \*\*outOptions) | 创建一个空的OpenFileBoost\_Options。 使用HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile添加文件。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile (OpenFileBoost\_Options \*options, const OpenFileBoost\_SupportFile \*supportFile) | 向OpenFileBoost\_Options添加支持预加载的文件类型列表。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_OptionsDestroy (OpenFileBoost\_Options \*options) | 销毁OpenFileBoost\_Options。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_RegisterFilePreloadWithOption (HMS\_OpenFileBoost\_QueryAppState queryAppState, HMS\_OpenFileBoost\_OnFilePreload filePreload, HMS\_OpenFileBoost\_OnFilePreload cancelFilePreload, OpenFileBoost\_Options \*options) | 注册预加载回调，允许应用传入支持预加载的文件信息。 |
| bool HMS\_Preview\_OpenFileBoost\_IsEnabled (void) | 查询应用加速特性是否使能。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_FileOperationInfoCreate (const char \*path, uint32\_t pathLen, const char \*operation, uint32\_t operationLen, OpenFileBoost\_FileOperationInfo \*\*outFileOperationInfo) | 创建OpenFileBoost\_FileOperationInfo。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_FileOperationInfoDestroy (OpenFileBoost\_FileOperationInfo \*fileOperationInfo) | 销毁OpenFileBoost\_FileOperationInfo。 |
| OpenFileBoost\_ErrCode HMS\_Preview\_OpenFileBoost\_NotifyFileOperation (OpenFileBoost\_FileOperationInfo \*fileOperationInfo) | 当用户对文件进行操作时，app调用该接口通知系统文件操作类型，这将有助于提高预加载文件预测的准确性。 |

## 约束限制

当前仅在PC/2in1和tablet设备上支持。

## 开发步骤

1. 申请文件打开加速服务的对应权限，在module.json5文件中添加文件预加载权限，注意ohos.permission.PRELOAD\_FILE为受限权限，具体可参考[申请使用受限权限](declare-permissions-in-acl.md) 。

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.PRELOAD_FILE"
     }
   ],
   ```
2. 添加对应的头文件。

   ```cpp
   #include "PreviewKit/open_file_boost.h"
   ```
3. 编写CMakeLists.txt，新增对文件打开加速功能的依赖。

   ```cmake
   find_library(
       OPEN_FILE_BOOST_LIBRARY
       NAMES libopen_file_boost.so
       PATHS ${CMAKE_FIND_ROOT_PATH}/lib/aarch64-linux-ohos
   )
   # ...
   target_link_libraries(entry PUBLIC ${OPEN_FILE_BOOST_LIBRARY})
   ```
4. 注册文件预加载回调，应用可传入支持预加载的文件信息，注册后系统在条件符合时调用回调向应用推荐文件。

   ```cpp
   static napi_value RegisterPreload(napi_env env, napi_callback_info info) {
       napi_value resp;
       napi_create_int32(env, 0, &resp);
       OH_LOG_INFO(LOG_APP, "Register file preload start.");
       // 创建选项
       OpenFileBoost_Options *options = nullptr;
       auto createCode = HMS_Preview_OpenFileBoost_OptionsCreate(&options);
       if (createCode != OPEN_FILE_BOOST_SUCCESS) {
           // 应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to create Options, code: %{public}d", createCode);
           napi_create_int32(env, -1, &resp);
           return resp;
       }
       // 创建文件类型
       OpenFileBoost_SupportFile *supportFile = nullptr;
       auto supportCode = HMS_Preview_OpenFileBoost_SupportFileCreate("xlsx", 4, 0, 100 * 1024 * 1024, &supportFile);
       if (supportCode != OPEN_FILE_BOOST_SUCCESS) {
           // 应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to create SupportFile, code: %{public}d", supportCode);
           // 销毁之前的创建
           HMS_Preview_OpenFileBoost_OptionsDestroy(options);
           napi_create_int32(env, -2, &resp);
           return resp;
       }
       // 添加文件类型到选项
       auto addCode = HMS_Preview_OpenFileBoost_OptionsAddSupportFile(options, supportFile);
       HMS_Preview_OpenFileBoost_SupportFileDestroy(supportFile);

       if (addCode != OPEN_FILE_BOOST_SUCCESS) {
           // 添加失败，应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to add support file, code: %{public}d", addCode);
           HMS_Preview_OpenFileBoost_OptionsDestroy(options);
           napi_create_int32(env, -3, &resp);
           return resp;
       }
       // 注册文件预加载回调，同时应用传递自己支持的文件后缀类型和文件大小上下限
       auto code = HMS_Preview_OpenFileBoost_RegisterFilePreloadWithOption(AppQueryAppStateCb, AppOnFilePreload,
                                                                           AppCancelFilePreload, options);
       HMS_Preview_OpenFileBoost_OptionsDestroy(options);

       if (code != OPEN_FILE_BOOST_SUCCESS) {
           // 注册失败，应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Register failed, ret :%{public}d", code);
           napi_create_int32(env, code, &resp);
           return resp;
       }

       OH_LOG_INFO(LOG_APP, "Register file preload successfully.");
       napi_create_int32(env, 0, &resp);
       return resp;
   }
   ```
5. 应用在当前回调上下文中同步解析预加载文件，或同步阻塞等待解析完毕后再返回，以便系统评估本次预加载文件的资源消耗。

   ```cpp
   // 查询应用当前状态的回调函数，系统在向应用推荐文件前会先调用状态查询回调函数向应用查询当前是否适合推荐
   OpenFileBoost_AppState AppQueryAppStateCb(void) {
       // 如果当前状态允许进行文件预加载则返回OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD，这里的state为代码示例，表示应用根据实际业务设置是否允许预加载
       int state = ConfigManager::getInstance().getAppState();
       OH_LOG_INFO(LOG_APP, "AppQueryAppStateCb, return state: %{public}d", state);
       return static_cast<OpenFileBoost_AppState>(state);
   }

   // 文件预加载回调
   OpenFileBoost_CbErrCode AppOnFilePreload(void *fileInfo) {
       OH_LOG_INFO(LOG_APP, "AppOnFilePreload called");

       int32_t fileDescriptor = 0;
       // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetFdFromPreloadFileInfo获取文件描述符
       OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
       if (ret != OPEN_FILE_BOOST_SUCCESS) {
           return OPEN_FILE_BOOST_CALLBACK_FAILURE;
       }

       char sandboxPath[MAX_BUFFER_LENGTH] = {0};
       // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo获取文件路径
       ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
       if (ret != OPEN_FILE_BOOST_SUCCESS) {
           return OPEN_FILE_BOOST_CALLBACK_FAILURE;
       }

       OH_LOG_INFO(LOG_APP, "Preload file: fd=%{public}d, path=%{public}s", fileDescriptor, sandboxPath);
       // 用户可保存文件描述符和文件路径，方便后续通知取消预加载时对文件取消预加载
       // 用户自定义具体的文件预加载逻辑
       {
           std::lock_guard<std::mutex> lock(g_preloadMutex);
           g_preloadTasks[std::string(sandboxPath)] = fileDescriptor;
       }
       ConfigManager::getInstance().addFileProcessTask(std::string(sandboxPath), fileDescriptor);

       int callbackResult = ConfigManager::getInstance().getPreloadCallbackResult();
       OH_LOG_INFO(LOG_APP, "AppOnFilePreload returning: %{public}d", callbackResult);
       return static_cast<OpenFileBoost_CbErrCode>(callbackResult);
   }

   // 取消预加载回调
   OpenFileBoost_CbErrCode AppCancelFilePreload(void *fileInfo) {
       OH_LOG_INFO(LOG_APP, "AppCancelFilePreload called");
       // 同样的方法获取文件描述符和沙箱路径
       int32_t fileDescriptor = 0;
       OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
       if (ret != OPEN_FILE_BOOST_SUCCESS) {
           return OPEN_FILE_BOOST_CALLBACK_FAILURE;
       }

       char sandboxPath[MAX_BUFFER_LENGTH] = {0};
       ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
       if (ret != OPEN_FILE_BOOST_SUCCESS) {
           return OPEN_FILE_BOOST_CALLBACK_FAILURE;
       }
       // 用户自定义具体的取消文件预加载逻辑
       OH_LOG_INFO(LOG_APP, "Cancel preload: fd=%{public}d, path=%{public}s", fileDescriptor, sandboxPath);

       std::string path(sandboxPath);
       std::lock_guard<std::mutex> lock(g_preloadMutex);
       auto it = g_preloadTasks.find(path);
       if (it != g_preloadTasks.end()) {
           g_preloadTasks.erase(it);
       }

       return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
   }
   ```
6. 如果用户打开了已经预加载的文件，应用需要调用HMS\_OpenFileBoost\_NotifyPreloadHit通知系统，系统会更改文件的预加载状态。

   ```cpp
   static napi_value NotifyPreloadHit(napi_env env, napi_callback_info info) {
       napi_value resp;

       std::lock_guard<std::mutex> lock(g_preloadMutex);
       if (g_preloadTasks.empty()) {
           OH_LOG_INFO(LOG_APP, "No preload tasks to notify");
           napi_create_int32(env, 0, &resp);
           return resp;
       }

       int notifyCount = 0;
       for (auto it = g_preloadTasks.begin(); it != g_preloadTasks.end(); ++it) {
           std::string notifyPath = it->first;
           std::vector<char> pathBuffer(notifyPath.size() + 1);
           std::copy(notifyPath.begin(), notifyPath.end(), pathBuffer.begin());
           pathBuffer[notifyPath.size()] = '\0';
           int fd = it->second;
           // 传入用户打开的已经预加载的文件描述符、文件路径和长度
           OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_NotifyPreloadHit(
               fd, pathBuffer.data(),static_cast<int32_t>(notifyPath.size()));
           if (ret == OPEN_FILE_BOOST_SUCCESS) {
               OH_LOG_INFO(LOG_APP, "Notify file(%{public}s) hit successfully.", notifyPath.c_str());
               notifyCount++;
           } else {
               // 通知失败，用户可自定义错误处理
               OH_LOG_ERROR(LOG_APP, "Notify file(%{public}s) failed, ret :%{public}d", notifyPath.c_str(), ret);
           }
       }

       g_preloadTasks.clear();
       OH_LOG_INFO(LOG_APP, "Notify %{public}d files hit successfully.", notifyCount);
       napi_create_int32(env, 0, &resp);
       return resp;
   }
   ```
7. 应用向系统查询加速开关特性是否可用。

   ```cpp
   static napi_value IsAccelerateEnabled(napi_env env, napi_callback_info info) {
       napi_value resp;

       bool isEnabled = HMS_Preview_OpenFileBoost_IsEnabled();
       if (isEnabled) {
           // 加速特性可用，应用可处理加速相关业务逻辑
           OH_LOG_INFO(LOG_APP, "Accelerate Enabled ");
       } else {
           // 加速特性不可用，应用可处理自身相关业务逻辑
           OH_LOG_INFO(LOG_APP, "Accelerate not Enabled");
       }

       napi_get_boolean(env, isEnabled, &resp);
       return resp;
   }
   ```
8. 应用向系统传递用户对文件的操作信息。

   ```cpp
   static napi_value NotifyFileOperation(napi_env env, napi_callback_info info) {
       napi_value resp;
       napi_create_int32(env, 0, &resp);

       size_t argc = 2;
       napi_value args[2] = {nullptr};
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       char filePath[MAX_BUFFER_LENGTH] = {0};
       char operationType[MAX_BUFFER_LENGTH] = {0};

       GetCharString(env, args[0], filePath);
       GetCharString(env, args[1], operationType);

       OH_LOG_INFO(LOG_APP, "NotifyFileOperation: path=%{public}s, operation=%{public}s", filePath, operationType);
       // 创建文件操作信息
       OpenFileBoost_FileOperationInfo *fileOpInfo = nullptr;
       OpenFileBoost_ErrCode ret = HMS_Preview_OpenFileBoost_FileOperationInfoCreate(
           filePath, static_cast<uint32_t>(strlen(filePath)), operationType, static_cast<uint32_t>(strlen(operationType)),
           &fileOpInfo);

       if (ret != OPEN_FILE_BOOST_SUCCESS) {
           // 创建失败，应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to create FileOperationInfo, code: %{public}d", ret);
           napi_create_int32(env, ret, &resp);
           return resp;
       }

       ret = HMS_Preview_OpenFileBoost_NotifyFileOperation(fileOpInfo);
       if (ret != OPEN_FILE_BOOST_SUCCESS) {
           // 传递失败，应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "NotifyFileOperation failed, ret :%{public}d", ret);
           HMS_Preview_OpenFileBoost_FileOperationInfoDestroy(fileOpInfo);
           napi_create_int32(env, ret, &resp);
           return resp;
       }

       HMS_Preview_OpenFileBoost_FileOperationInfoDestroy(fileOpInfo);
       OH_LOG_INFO(LOG_APP, "NotifyFileOperation successfully.");
       napi_create_int32(env, 0, &resp);
       return resp;
   }
   ```
9. 注册文件扫描回调，确保系统在扫描文件时可以调用回调向应用通知扫描任务。

   ```
   static napi_value RegisterFileScan(napi_env env, napi_callback_info info) {
       napi_value resp;
       napi_create_int32(env, 0, &resp);
       OH_LOG_INFO(LOG_APP, "Register file scan start.");
       // 创建扫描选项，添加应用支持的文件类型
       FileScanBoost_ScanOption *scanOption = nullptr;
       FileScanBoost_ErrCode res = HMS_Preview_FileScanBoost_ScanOptionCreate(&scanOption);
       if (res != FILE_SCAN_BOOST_SUCCESS) {
           // 应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to create ScanOption, code: %{public}d", res);
           napi_create_int32(env, -1, &resp);
           return resp;
       }

       res = HMS_Preview_FileScanBoost_ScanOptionAddSupportFile(scanOption, "xlsx", 4);
       if (res != FILE_SCAN_BOOST_SUCCESS) {
           // 应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to add .xlsx support, code: %{public}d", res);
           HMS_Preview_FileScanBoost_ScanOptionDestroy(scanOption);
           napi_create_int32(env, -2, &resp);
           return resp;
       }

       res = HMS_Preview_FileScanBoost_ScanOptionAddSupportFile(scanOption, "xls", 3);
       if (res != FILE_SCAN_BOOST_SUCCESS) {
           // 应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Failed to add .xls support, code: %{public}d", res);
           HMS_Preview_FileScanBoost_ScanOptionDestroy(scanOption);
           napi_create_int32(env, -3, &resp);
           return resp;
       }
       // 注册文件扫描回调
       res = HMS_Preview_FileScanBoost_RegisterFileScan(AppOnFileScan, scanOption);
       if (res != FILE_SCAN_BOOST_SUCCESS) {
           // 注册失败，应用可自定义错误处理
           OH_LOG_ERROR(LOG_APP, "Register file scan failed, ret :%{public}d", res);
           napi_create_int32(env, res, &resp);
           return resp;
       }
       // 扫描完成需销毁扫描选项
       HMS_Preview_FileScanBoost_ScanOptionDestroy(scanOption);
       OH_LOG_INFO(LOG_APP, "Register file scan successfully.");
       napi_create_int32(env, 0, &resp);
       return resp;
   }

   // 文件扫描回调函数，系统调用此回调发送扫描任务
   // 应用应在当前回调上下文中同步完成文件解析或同步阻塞等待解析完毕后再返回
   FileScanBoost_CbErrCode AppOnFileScan(int32_t fd, const char *path, uint32_t pathLen) {
       // 应用可在回调中实现具体文件解析逻辑
       // 返回FILE_SCAN_BOOST_CALLBACK_SUCCESS表示接受扫描任务
       // 返回其他值表示拒绝
       OH_LOG_INFO(LOG_APP, "AppOnFileScan called, fd=%{public}d, path=%{public}s", fd, path);

       {
           std::lock_guard<std::mutex> lock(g_scanMutex);
           g_scanTasks[std::string(path)] = fd;
       }
       ConfigManager::getInstance().addScanTask(std::string(path), fd);

       int callbackResult = ConfigManager::getInstance().getScanCallbackResult();
       OH_LOG_INFO(LOG_APP, "AppOnFileScan returning: %{public}d", callbackResult);
       return static_cast<FileScanBoost_CbErrCode>(callbackResult);
   }
   ```
10. 应用向系统传递扫描结果，确保文件扫描完成后，系统能收到文件扫描结果。

    ```cpp
    static napi_value ReportScanResult(napi_env env, napi_callback_info info) {
        napi_value resp;
        napi_create_int32(env, 0, &resp);

        std::lock_guard<std::mutex> lock(g_scanMutex);
        if (g_scanTasks.empty()) {
            OH_LOG_INFO(LOG_APP, "No scan tasks to report");
            napi_create_int32(env, 0, &resp);
            return resp;
        }

        int reportCount = 0;
        for (auto it = g_scanTasks.begin(); it != g_scanTasks.end();) {
            std::string reportPath = it->first;
            // 创建扫描结果
            FileScanBoost_ScanResult *scanResult = nullptr;
            FileScanBoost_ErrCode res = HMS_Preview_FileScanBoost_ScanResultCreate(&scanResult);
            if (res != FILE_SCAN_BOOST_SUCCESS) {
                // 应用可自定义错误处理
                OH_LOG_ERROR(LOG_APP, "Failed to create ScanResult, code: %{public}d", res);
                ++it;
                continue;
            }
            // 设置扫描状态
            int state = ConfigManager::getInstance().getScanResultState();
            res = HMS_Preview_FileScanBoost_ScanResultSetState(scanResult, static_cast<FileScanBoost_ScanState>(state));
            if (res != FILE_SCAN_BOOST_SUCCESS) {
                // 应用可自定义错误处理
                OH_LOG_INFO(LOG_APP, "ScanResultSetState error");
            }

            // 设置最大原子耗时（单位：ms）
            int64_t maxAtomicTime = ConfigManager::getInstance().getScanResultMaxAtomicTime();
            res = HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime(scanResult, maxAtomicTime);
            if (res != FILE_SCAN_BOOST_SUCCESS) {
                // 应用可自定义错误处理
                OH_LOG_INFO(LOG_APP, "ScanResultSetMaxAtomicTime error");
            }

            // 设置内存占用（单位：MB）
            int64_t memSize = ConfigManager::getInstance().getScanResultMemSize();
            res = HMS_Preview_FileScanBoost_ScanResultSetMemSize(scanResult, memSize);
            if (res != FILE_SCAN_BOOST_SUCCESS) {
                // 应用可自定义错误处理
                OH_LOG_INFO(LOG_APP, "ScanResultSetMemSize error");
            }

            // 向系统报告扫描结果
            res = HMS_Preview_FileScanBoost_ReportScanResult(reportPath.c_str(),
                                                             static_cast<uint32_t>(strlen(reportPath.c_str())), scanResult);

            if (res == FILE_SCAN_BOOST_SUCCESS) {
                // 报告失败，应用可自定义错误处理
                OH_LOG_INFO(LOG_APP, "ReportScanResult successfully for: %{public}s", reportPath.c_str());
                reportCount++;
            } else {
                OH_LOG_ERROR(LOG_APP, "ReportScanResult failed for %{public}s, ret :%{public}d", reportPath.c_str(), res);
            }

            // 扫描完成需销毁扫描结果
            HMS_Preview_FileScanBoost_ScanResultDestroy(scanResult);

            it = g_scanTasks.erase(it);
            ConfigManager::getInstance().removeScanTaskByPath(reportPath);
        }

        OH_LOG_INFO(LOG_APP, "Report %{public}d scan results successfully.", reportCount);
        napi_create_int32(env, 0, &resp);
        return resp;
    }
    ```
11. 应用注销文件扫描回调，确保应用将不再接收扫描任务通知。

    ```cpp
    static napi_value UnregisterFileScan(napi_env env, napi_callback_info info) {
        napi_value resp;
        napi_create_int32(env, 0, &resp);
        OH_LOG_INFO(LOG_APP, "UnRegister file scan start.");

        auto res = HMS_Preview_FileScanBoost_UnregisterFileScan();
        if (res != FILE_SCAN_BOOST_SUCCESS) {
            // 注销失败，应用可自定义错误处理
            OH_LOG_ERROR(LOG_APP, "UnRegister file scan failed, ret :%{public}d", res);
            napi_create_int32(env, res, &resp);
            return resp;
        }

        {
            std::lock_guard<std::mutex> lock(g_scanMutex);
            g_scanTasks.clear();
        }

        OH_LOG_INFO(LOG_APP, "UnRegister file scan successfully.");
        napi_create_int32(env, 0, &resp);
        return resp;
    }
    ```
