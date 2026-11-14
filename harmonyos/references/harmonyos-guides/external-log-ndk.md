---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/external-log-ndk
title: external_log日志清理（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > 通用日志 > external_log日志 > external_log日志清理（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:45+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:3ff6481f0f5cae220f9e8c35c5e62942654cc07da08540aa07298cae1ca19688
---

从API版本26.0.1开始提供了external\_log日志管理者注册接口，确保故障日志沙箱目录容量达到阈值时通知应用清理删除文件。

## 接口说明

API接口的使用说明，包括参数使用限制和取值范围，请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_RegExternalLogCapacityReachedCallback(OH\_HiAppEvent\_ExternalLogCapacityReachedCallback callback) | 注册external\_log日志文件管理者。 |

## 注册external\_log日志管理者开发指导

### 步骤一：新建工程及编译配置

1. 将示例工程依赖的jsoncpp库文件复制到新建工程中。

   打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，并点击“下载当前目录”，下载EventSub工程文件。

   新建一个Native C++工程。从解压后的EventSub文件夹中拷贝jsoncpp库文件（entry/libs和entry/src/main/cpp/thirdparty整个目录）到新建的工程中，得到的目录结构如下：

   ```text
   entry
   ├── libs        // 自行创建文件夹,放入相关的三方库
   └── src
       ├── main
       │   ├── cpp
       │   │   ├── CMakeLists.txt       // 导入so链接
       │   │   ├── napi_init.cpp        // 功能函数，观察者定义
       │   │   ├── thirdparty    // 自行创建文件夹,放入相关的三方库
       │   │   │   └── jsoncpp
       │   │   └── types
       │   │       └── libentry
       │   │           ├── Index.d.ts        // 定义ArkTS接口
       │   │           └── oh-package.json5
       │   ├── ets
       │   │   ├── entryability
       │   │   │   └── EntryAbility.ets    // 新增接口调用
       │   │   ├── entrybackupability
       │   │   │   └── EntryBackupAbility.ets
       │   │   └── pages
       │   │       └── Index.ets        // 主页
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://codeload.github.com/open-source-parsers/jsoncpp/tar.gz/refs/tags/1.9.6)。
2. 编辑“CMakeLists.txt”文件，添加所需的源文件和动态库。

   ```text
   set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   # 检查是否存在entry/build目录
   execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
       WORKING_DIRECTORY ${DEST_DIR})

   add_library(entry SHARED napi_init.cpp)
   // ...
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖的文件并定义LOG\_TAG：

   ```
   #include "napi/native_api.h"
   // 根据工程中三方库jsoncpp的位置适配引用json.h的路径
   #include "../../../build/jsoncpp-1.9.6/include/json/json.h"
   #include "hiappevent/hiappevent.h"
   #include "hiappevent/hiappevent_param.h"
   #include "hilog/log.h"

   #undef LOG_TAG
   #define LOG_TAG "testTag"
   ```

### 步骤二：注册external\_log日志管理者

1. 编辑“napi\_init.cpp”文件，定义注册external\_log日志管理者相关方法：

   ```
   // 定义回调函数
   void OnExternalLogCapacityReached(OH_HiAppEvent_ExternalLog* externalLogArr, uint32_t arrLen)
   {
       OH_LOG_INFO(LogType::LOG_APP, "[ExternalLogMgr_c] onCapacityReached triggered, log count: %{public}u", arrLen);
       for (uint32_t i = 0; i < arrLen; i++) {
           OH_HiAppEvent_ExternalLog* log = &externalLogArr[i];
           OH_LOG_INFO(LogType::LOG_APP, "[ExternalLogMgr_c] filePath: %{public}s, %{public}lld, %{public}ld,"
               "kb event: %{public}d", log->filePath, log->generationTs, log->fileSize, log->event);
           // 应用自行决定删除故障文件 删除返回的前5个文件
           if (i < 5) {
               remove(log->filePath);
               OH_LOG_INFO(LogType::LOG_APP, "[ExternalLogMgr_c] remove file %{public}s", log->filePath);
           }
       }
   }

   // 注册external_log日志管理者
   static napi_value RegisterExternalLogMgr(napi_env env, napi_callback_info info)
   {
       int ret = OH_HiAppEvent_RegExternalLogCapacityReachedCallback(OnExternalLogCapacityReached);
       if (ret == HIAPPEVENT_SUCCESS) {
           OH_LOG_INFO(LogType::LOG_APP, "[ExternalLogMgr_c] RegExternalLogMgr succeeded");
       } else {
           OH_LOG_INFO(LogType::LOG_APP, "[ExternalLogMgr_c] RegExternalLogMgr failed, ret %{public}d", ret);
       }

       return {};
   }
   ```
2. 编辑“napi\_init.cpp”文件，通过RegisterExternalLogMgr()方法，将注册external\_log日志管理者为ArkTS接口：

   ```
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           // ...
           { "registerExternalLogMgr", nullptr, RegisterExternalLogMgr, nullptr, nullptr, nullptr, napi_default, nullptr },
           // ...
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```
3. 编辑“index.d.ts”文件，定义ArkTS接口：

   ```typescript
   export const registerExternalLogMgr: () => void;
   ```
4. 编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：

   ```typescript
   import testNapi from 'libentry.so';
   ```

   ```ts
   // 在onCreate()函数中添加C API接口调用
   // 启动时，注册external_log日志管理者
   testNapi.registerExternalLogMgr();
   ```

### 步骤三：添加订阅

应用订阅故障事件，这里以[订阅崩溃事件（C/C++）](hiappevent-watcher-crash-events-ndk.md)为例。

## 调测验证

1. 点击DevEco Studio界面中的运行按钮，运行应用工程，启动应用。
2. 搜索关键字“ExternalLogMgr\_c”，在HiLog窗口查看注册external\_log日志管理者的日志：

   ```text
   [ExternalLogMgr_c] RegExternalLogMgr succeeded
   ```
3. 连续触发应用崩溃事件，使external\_log目录达到阈值。搜索关键字“ExternalLogMgr\_c”，在HiLog窗口查看external\_log目录达到阈值回调的日志：

   ```text
   [ExternalLogMgr_c] onCapacityReached triggered, log count: 13
   [ExternalLogMgr_c] filePath: /data/storage/el2/log/hiappevent/APP_CRASH_1788402790404_27596_0.log, 1788402790404, 183 kb event: 2
   [ExternalLogMgr_c] remove file /data/storage/el2/log/hiappevent/APP_CRASH_1788402790404_27596_0.log
   ...
   [ExternalLogMgr_c] filePath: /data/storage/el2/log/hiappevent/APP_CRASH_1788399327280_26303_0.log, 1788399327280, 515 kb event: 1
   [ExternalLogMgr_c] remove file /data/storage/el2/log/hiappevent/APP_CRASH_1788399327280_26303_0.log
   ...
   [ExternalLogMgr_c] filePath: /data/storage/el2/log/hiappevent/APP_CRASH_1788402913687_48668_0.log, 1788402913687, 518 kb event: 1
   ```
