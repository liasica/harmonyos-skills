---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-print-file
title: 文件打印（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 打印 > 文件打印（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f141321a76724b5cbb76f377d10bcaa3cbc6f9daac4250363ac28df492c3cec
---

## HarmonyOS提供的两种打印方式

[方式一](native-print-file.md#通过接口拉起系统打印预览界面下发任务)：应用通过接口拉起系统打印预览界面。适合没有实现打印预览能力的应用。

[方式二](native-print-file.md#通过打印接口直接下发打印任务)：应用通过接口指定打印文件和选项直接下发打印任务，适合已经实现打印预览能力的应用。

**说明** 

使用打印服务，需[声明权限](declare-permissions.md)：ohos.permission.PRINT。

当不再使用打印服务时，需先调用OH\_Print\_UnregisterPrinterChangeListener()和OH\_Print\_StopPrinterDiscovery()取消事件订阅，再调用OH\_Print\_Release()释放打印客户端资源。

C/C++接口需要在NDK工程中使用，请参考[NDK开发导读](ndk-development-overview.md)。

### 引用NDK头文件

初始路径为entry/src/main/cpp/types/napi\_init.cpp # C++ 源码目录 NAPI 初始化入口（桥接 ArkTS 与 C++）。

```
#include "napi/native_api.h"
#include "BasicServicesKit/ohprint.h"
#include "hilog/log.h"
#include <string>
#include <fcntl.h>
#include <unistd.h>
#include <vector>

#undef LOG_TAG
#define LOG_TAG "print c/c++"
#define LOGE(...) OH_LOG_ERROR(LOG_APP, ##__VA_ARGS__)
#define LOGI(...) OH_LOG_INFO(LOG_APP, ##__VA_ARGS__)
```

初始路径为entry/src/main/ets/pages/Index.ets # ArkTS 源码目录主页面。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
import { Context } from '@kit.AbilityKit';

class HiLog {
  static info(...args: string[]): void {
    hilog.info(0x0, 'print c/c++ ', '%{public}s', `${args.join(' ')}`);
  }
}
```

### 在CMake脚本中添加动态链接库

初始路径为entry/src/main/cpp/types/CMakeLists.txt # C++ 源码目录 CMake 构建配置。

```cmake
target_link_libraries(entry PUBLIC
    libace_napi.z.so
    libhilog_ndk.z.so
    libohprint.so
)
```

### 绑定页面和打印服务生命周期

建议将打印服务初始化和释放与使用系统打印能力的页面的生命周期绑定。

封装C/C++接口。

```
static void PrinterDiscoveryCallback(Print_DiscoveryEvent event, const Print_PrinterInfo *printerInfo)
{
    // 发现打印设备事件，以设备Id作为唯一标识符
    if (printerInfo == nullptr) {
        LOGE("printerInfo is nullptr");
        return;
    }
    // 开发者需根据具体事件实现相关逻辑
    switch (event) {
        // 探测到一台打印设备，可能会重复上报
        case PRINTER_DISCOVERED:
            LOGI("do something, printer[%{public}s] discovered", printerInfo->printerId);
            break;
        // 打印设备从发现列表移除，仅上报一次
        case PRINTER_LOST:
            LOGI("do something, printer[%{public}s] lost", printerInfo->printerId);
            break;
        // 打印设备开始连接，由OH_Print_ConnectPrinter触发
        case PRINTER_CONNECTING:
            LOGI("do something, printer[%{public}s] on connecting", printerInfo->printerId);
            break;
        // 打印设备成功连接，由OH_Print_ConnectPrinter触发
        case PRINTER_CONNECTED:
            LOGI("do something, printer[%{public}s] connected", printerInfo->printerId);
            break;
        default:
            break;
    }
}
```

```
static void PrinterChangeCallback(Print_PrinterEvent event, const Print_PrinterInfo *printerInfo)
{
    // 以设备Id作为唯一标识符
    if (printerInfo == nullptr) {
        LOGE("printerInfo is nullptr");
        return;
    }
    // 开发者需根据具体事件实现相关逻辑
    switch (event) {
        // 打印设备新增到已添加设备列表
        case PRINTER_ADDED:
            LOGI("do something, printer[%{public}s] added", printerInfo->printerId);
            break;
        // 打印设备从已添加设备列表移除
        case PRINTER_DELETED:
            LOGI("do something, printer[%{public}s] deleted", printerInfo->printerId);
            break;
        // 打印设备状态变更
        case PRINTER_STATE_CHANGED:
            LOGI("do something, printer[%{public}s] state change to %{public}d",
                 printerInfo->printerId, printerInfo->printerState);
            break;
        // 打印设备基础属性变更
        case PRINTER_INFO_CHANGED:
            LOGI("do something, printer[%{public}s] info changed", printerInfo->printerId);
            break;
        default:
            break;
    }
}
```

```
static napi_value NativeInit(napi_env env, napi_callback_info info)
{
    // 初始化打印服务
    Print_ErrorCode ret = OH_Print_Init();
    LOGI("nativeInit, ret = %{public}d", ret);
    napi_value n_ret = nullptr;
    napi_get_boolean(env, !ret, &n_ret);
    if (ret == 0) {
        // 订阅已添加设备状态变更事件
        Print_ErrorCode error = OH_Print_RegisterPrinterChangeListener(PrinterChangeCallback);
        LOGI("OH_Print_RegisterPrinterChangeListener, error = %{public}d", error);
        // 订阅设备发现相关事件
        error = OH_Print_StartPrinterDiscovery(PrinterDiscoveryCallback);
        LOGI("OH_Print_StartPrinterDiscovery, error = %{public}d", error);
    }
    return n_ret;
}
```

```
static napi_value NativeRelease(napi_env env, napi_callback_info info)
{
    // 取消订阅已添加设备状态变更事件
    OH_Print_UnregisterPrinterChangeListener();
    // 取消订阅设备发现相关事件
    OH_Print_StopPrinterDiscovery();
    // 释放打印服务
    Print_ErrorCode ret = OH_Print_Release();
    LOGI("nativeRelease, ret = %{public}d", ret);
    napi_value n_ret = nullptr;
    napi_get_boolean(env, !ret, &n_ret);
    return n_ret;
}
```

```
// 添加napi接口声明
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "nativeInit", nullptr, NativeInit, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "nativeRelease", nullptr, NativeRelease, nullptr, nullptr, nullptr, napi_default, nullptr },
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```

应用侧在页面被拉起的生命周期初始化，在页面关掉时释放。

```typescript
// 页面展示到屏幕时，初始化打印服务
aboutToAppear(): void {
  testNapi.nativeInit();
}
// 页面离开屏幕时
aboutToDisappear(): void {
  testNapi.nativeRelease();
}
```

### 通过接口拉起系统打印预览界面下发任务

封装C/C++接口。

```
// WriteFile 由开发者实现，示例仅为简单的文件拷贝。根据当前用户修改后的打印参数，若需要更新打印文件可重新写入系统提供的fd中
static uint32_t WriteFile(uint32_t fd, const Print_PrintAttributes *oldAttrs, const Print_PrintAttributes *newAttrs)
{
    // 沙箱内合法路径
    const char* filePath = "/data/storage/el2/base/files/test.pdf";
    int32_t fileFd = open(filePath, O_RDONLY);
    if (fileFd == -1) {
        LOGE("open failed, errno=%{public}d", errno);
        return 1;
    }

    char buffer[4096];
    ssize_t bytesRead = -1;
    while ((bytesRead = read(fileFd, buffer, sizeof(buffer))) > 0) {
        if (write(fd, buffer, bytesRead) < bytesRead) {
            close(fileFd);
            return 1;
        }
    }
    close(fileFd);
    return 0;
}
```

```
// 系统打印预览界面回调，首次拉起或用户修改打印参数时的延迟文件写入回调。可以根据新参数适当修改打印文件
static void OnStartLayoutWriteCb(const char *jobId,
                                 uint32_t fd,
                                 const Print_PrintAttributes *oldAttrs,
                                 const Print_PrintAttributes *newAttrs,
                                 Print_WriteResultCallback writeCallback)
{
    // 将数据写入系统提供的fd中，每次回调的fd不一定相同，请不要保存此fd
    uint32_t retCode = WriteFile(fd, oldAttrs, newAttrs);
    // 通知打印系统文件写入完成，若需要异步写入数据，请保存好jobId
    // retCode取值：0-写入成功，1-写入异常，2-无需重新写入
    writeCallback(jobId, retCode);
}

// 打印文件写入完成后，系统打印预览界面会进行预览，此时用户可以点击"开始打印"下发任务
// 任务ID对应的打印状态变化的回调函数
static void OnJobStateChangedCb(const char *jobId, uint32_t state)
{
    // state取值：0-任务准备中，1-任务排队中， 2-任务打印中， 3-任务异常暂停， 4-任务结束， 100-任务未知异常
    LOGI("do something with OnJobStateChangedCb, jobId: %{public}s, jobState: %{public}u", jobId, state);
}
```

```
// 拉起系统打印预览界面
static napi_value NativeStartPrintByNative(napi_env env, napi_callback_info info)
{
    napi_value n_ret = nullptr;
    void *context = nullptr;
    size_t argc = 1;
    napi_value argv[1] = {nullptr};
    // 假设 napi_get_cb_info 和 napi_unwrap 均正常返回
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    napi_unwrap(env, argv[0], &context);

    // 调用打印接口以拉起系统打印预览界面
    std::string printJobName = "test";
    Print_PrintDocCallback printDocCallback = { OnStartLayoutWriteCb, OnJobStateChangedCb };
    Print_ErrorCode ret = OH_Print_StartPrintByNative(printJobName.c_str(), printDocCallback, context);
    napi_get_boolean(env, !ret, &n_ret);
    return n_ret;
}
```

```
// 添加napi接口声明
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "nativeStartPrintByNative",
            nullptr, NativeStartPrintByNative, nullptr, nullptr, nullptr, napi_default, nullptr },
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```

主页上新增一个按钮，单击调用C/C++的nativeStartPrintByNative接口拉起打印预览界面。

```typescript
Button('OH_Print_StartPrintByNative')
  .onClick(() => {
    HiLog.info("OH_Print_StartPrintByNative onClick");
    let ctx: Context | undefined = this.getUIContext().getHostContext();
    let ret: boolean = testNapi.nativeStartPrintByNative(ctx);
    HiLog.info(`nativeStartPrintByNative ret: ${JSON.stringify(ret)}`);
  })
```

### 通过打印接口直接下发打印任务

封装C/C++接口，示例仅演示从已添加打印设备列表获取信息并下发任务。

```
// 下发打印任务
static napi_value NativeStartPrintJob(napi_env env, napi_callback_info info)
{
    napi_value n_ret = nullptr;
    napi_get_boolean(env, false, &n_ret);
    Print_ErrorCode ret = PRINT_ERROR_INVALID_PARAMETER;

    // 获取已添加打印机的列表
    Print_StringList pList = { 0 };
    ret = OH_Print_QueryPrinterList(&pList);
    if (ret != PRINT_ERROR_NONE) {
        OH_Print_ReleasePrinterList(&pList);
        return n_ret;
    }
    if (pList.count <= 0 || (!pList.list)) {
        OH_Print_ReleasePrinterList(&pList);
        return n_ret;
    }
    // 打印列表中所有的打印机Id
    for (uint32_t index = 0; index < pList.count; index++) {
        LOGI("pList->list[%{public}d]: %{public}s", index, pList.list[index]);
    }

    // 获取列表中第一台打印机属性
    const char *printerId = pList.list[0];
    Print_PrinterInfo *printerInfo = nullptr;
    ret = OH_Print_QueryPrinterInfo(printerId, &printerInfo);
    if (ret != PRINT_ERROR_NONE) {
        OH_Print_ReleasePrinterInfo(printerInfo);
        OH_Print_ReleasePrinterList(&pList);
        return n_ret;
    }
    // 打开要打印的文件，可以有多个，沙箱内合法路径
    const char* filePath = "/data/storage/el2/base/files/test.pdf";
    int32_t fd = open(filePath, O_RDONLY);
    if (fd == -1) {
        LOGE("open failed, errno=%{public}d", errno);
        ret = PRINT_ERROR_INVALID_PARAMETER;
        OH_Print_ReleasePrinterInfo(printerInfo);
        OH_Print_ReleasePrinterList(&pList);
        return n_ret;
    }
    std::vector<uint32_t> fdList = { static_cast<uint32_t>(fd) };
    // 本例子使用首选项 printerInfo->defaultValue 作为打印任务参数来下发任务
    Print_PrintJob printJob{ "jobName", fdList.data(), static_cast<uint32_t>(fdList.size()), printerInfo->printerId,
                             1, printerInfo->defaultValue.defaultPaperSource,
                             printerInfo->defaultValue.defaultMediaType, printerInfo->defaultValue.defaultPageSizeId,
                             printerInfo->defaultValue.defaultColorMode, printerInfo->defaultValue.defaultDuplexMode,
                             printerInfo->defaultValue.defaultResolution, printerInfo->defaultValue.defaultMargin,
                             true, printerInfo->defaultValue.defaultOrientation,
                             printerInfo->defaultValue.defaultPrintQuality, DOCUMENT_FORMAT_PDF,
                             printerInfo->defaultValue.otherDefaultValues, };
    ret = OH_Print_StartPrintJob(&printJob);
    close(fd);
    // 使用完打印机属性和添加列表后需要及时释放
    OH_Print_ReleasePrinterInfo(printerInfo);
    OH_Print_ReleasePrinterList(&pList);

    napi_get_boolean(env, !ret, &n_ret);
    return n_ret;
}
```

```
// 添加napi接口声明
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "nativeStartPrintJob", nullptr, NativeStartPrintJob, nullptr, nullptr, nullptr, napi_default, nullptr },
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```

主页上新增一个按钮，单击调用C/C++的nativeStartPrintJob直接下发任务。

```typescript
Button('OH_Print_StartPrintJob')
  .onClick(() => {
    HiLog.info('OH_Print_StartPrintJob onClick');
    let ret: boolean = testNapi.nativeStartPrintJob();
    HiLog.info(`OH_Print_StartPrintJob ret: ${JSON.stringify(ret)}`);
  })
```
