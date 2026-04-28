---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-print-file
title: 文件打印（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 打印 > 文件打印（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:25+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:40134e0322c7ab99fe8d8a5b960c9b12085d42ffe9bfdced6a5f6a1af34796dc
---

## HarmonyOS提供的两种打印方式

[方式一](native-print-file.md#步骤4-通过接口拉起系统打印预览界面下发任务)：应用通过接口拉起系统打印预览界面。适合没有实现打印预览能力的应用。

[方式二](native-print-file.md#步骤5-通过打印接口直接下发打印任务)：应用通过接口指定打印文件和选项直接下发打印任务，适合已经实现打印预览能力的应用。

说明

使用打印服务，需[声明权限](declare-permissions.md)：ohos.permission.PRINT。

当不再使用打印服务时，调用OH\_Print\_Release()释放打印客户端资源并取消事件订阅。

c++接口需要在NDK工程中使用，请参考[NDK开发导读](ndk-development-overview.md)。

### 步骤1. 引用NDK头文件

初始路径为entry/src/main/cpp/types/napi\_init.cpp # C++ 源码目录 NAPI 初始化入口（桥接 ArkTS 与 C++）。

```
1. #include "hilog/log.h"
2. #include "napi/native_api.h"
3. #include "BasicServicesKit/ohprint.h"

5. #undef LOG_TAG
6. #define LOG_TAG "print c/c++"
7. #define LOGE(...) OH_LOG_ERROR(LOG_APP, ##__VA_ARGS__)
8. #define LOGI(...) OH_LOG_INFO(LOG_APP, ##__VA_ARGS__)
```

初始路径为entry/src/main/ets/pages/Index.ets # ArkTS 源码目录主页面。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { testNapi } from 'libentry.so';
3. import { Context } from '@kit.AbilityKit';

5. class HiLog {
6. static info(...args:string[]): void {
7. hilog.info(0x0, "print c/c++ ", '%{public}s', `${args.join(' ')}`);
8. }
9. }
```

### 步骤2. 在CMake脚本中添加动态链接库

初始路径为entry/src/main/cpp/types/CMakeLists.txt # C++ 源码目录 CMake 构建配置。

```
1. target_link_libraries(entry PUBLIC
2. libace_napi.z.so
3. libhilog_ndk.z.so
4. libohprint.so
5. )
```

### 步骤3. 绑定页面和打印服务生命周期

建议将打印服务初始化和释放与使用系统打印能力的页面的生命周期绑定。

封装c++接口。

```
1. // napi_init.cpp

3. static void PrinterDiscoveryCallback(Print_DiscoveryEvent event, const Print_PrinterInfo *printerInfo)
4. {
5. // 发现打印设备事件，以设备Id作为唯一标识符
6. if (printerInfo == nullptr) {
7. LOGE("printerInfo is nullptr");
8. return;
9. }
10. // 开发者需根据具体事件实现相关逻辑
11. switch (event) {
12. // 探测到一台打印设备，可能会重复上报
13. case PRINTER_DISCOVERED:
14. LOGI("do something, printer[%{public}s] discovered", printerInfo->printerId);
15. break;
16. // 打印设备从发现列表移除，仅上报一次
17. case PRINTER_LOST:
18. LOGI("do something, printer[%{public}s] lost", printerInfo->printerId);
19. break;
20. // 打印设备开始连接，由OH_Print_ConnectPrinter触发
21. case PRINTER_CONNECTING:
22. LOGI("do something, printer[%{public}s] on connecting", printerInfo->printerId);
23. break;
24. // 打印设备成功连接，由OH_Print_ConnectPrinter触发
25. case PRINTER_CONNECTED:
26. LOGI("do something, printer[%{public}s] connected", printerInfo->printerId);
27. break;
28. default:
29. break;
30. }
31. }

33. static void PrinterChangeCallback(Print_PrinterEvent event, const Print_PrinterInfo *printerInfo)
34. {
35. // 以设备Id作为唯一标识符
36. if (printerInfo == nullptr) {
37. LOGE("printerInfo is nullptr");
38. return;
39. }
40. // 开发者需根据具体事件实现相关逻辑
41. switch (event) {
42. // 打印设备新增到已添加设备列表
43. case PRINTER_ADDED:
44. LOGI("do something, printer[%{public}s] added", printerInfo->printerId);
45. break;
46. // 打印设备从已添加设备列表移除
47. case PRINTER_DELETED:
48. LOGI("do something, printer[%{public}s] deleted", printerInfo->printerId);
49. break;
50. // 打印设备状态变更
51. case PRINTER_STATE_CHANGED:
52. LOGI("do something, printer[%{public}s] state change to %{public}d",
53. printerInfo->printerId, printerInfo->printerState);
54. break;
55. // 打印设备基础属性变更
56. case PRINTER_INFO_CHANGED:
57. LOGI("do something, printer[%{public}s] info changed", printerInfo->printerId);
58. break;
59. // 打印设备首选项属性
60. case PRINTER_PREFERENCE_CHANGED:
61. LOGI("do something, printer[%{public}s] preference changed", printerInfo->printerId);
62. break;
63. default:
64. break;
65. }
66. }

68. static napi_value NativeInit(napi_env env, napi_callback_info info)
69. {
70. // 初始化打印服务
71. Print_ErrorCode ret = OH_Print_Init();
72. LOGI("nativeInit, ret = %{public}d", ret);
73. napi_value n_ret = nullptr;
74. napi_get_boolean(env, !ret, &n_ret);
75. if (ret == 0) {
76. // 订阅已添加设备状态变更事件
77. Print_ErrorCode error = OH_Print_RegisterPrinterChangeListener(PrinterChangeCallback);
78. LOGI("OH_Print_RegisterPrinterChangeListener, ret = %{public}d", error);
79. // 订阅设备发现相关事件
80. error = OH_Print_StartPrinterDiscovery(PrinterDiscoveryCallback);
81. LOGI("OH_Print_StartPrinterDiscovery, ret = %{public}d", error);
82. }
83. return n_ret;
84. }

86. static napi_value NativeRelease(napi_env env, napi_callback_info info)
87. {
88. // 取消订阅已添加设备状态变更事件
89. OH_Print_UnregisterPrinterChangeListener();
90. // 取消订阅设备发现相关事件
91. OH_Print_StopPrinterDiscovery();
92. // 释放打印服务
93. Print_ErrorCode ret = OH_Print_Release();
94. LOGI("nativeInit, ret = %{public}d", ret);
95. napi_value n_ret = nullptr;
96. napi_get_boolean(env, !ret, &n_ret);
97. return n_ret;
98. }

100. // 添加napi接口声明
101. EXTERN_C_START
102. static napi_value Init(napi_env env, napi_value exports)
103. {
104. napi_property_descriptor desc[] = {
105. { "nativeInit", nullptr, NativeInit, nullptr, nullptr, nullptr, napi_default, nullptr },
106. { "nativeRelease", nullptr, NativeRelease, nullptr, nullptr, nullptr, napi_default, nullptr },
107. };
108. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
109. return exports;
110. }
111. EXTERN_C_END
```

应用侧在页面被拉起的生命周期初始化，在页面关掉时释放。

```
1. // Index.ets

3. @Entry
4. @Component
5. struct Index {
6. // 页面展示到屏幕时，初始化打印服务
7. aboutToAppear(): void {
8. testNapi.nativeInit();
9. }
10. // 页面离开到屏幕时
11. aboutToDisappear(): void {
12. testNapi.nativeRelease();
13. }
14. }
```

### 步骤4. 通过接口拉起系统打印预览界面下发任务

封装c++接口。

```
1. // napi_init.cpp

3. // WriteFile 由开发者实现，示例仅为简单的文件拷贝。根据当前用户修改后的打印参数，若需要更新打印文件可重新写入系统提供的fd中
4. static uint32_t WriteFile(uint32_t fd, const Print_PrintAttributes *oldAttrs, const Print_PrintAttributes *newAttrs){
5. // 沙箱内合法路径
6. const char* filePath = "/data/storage/el2/base/files/test.pdf";
7. int32_t fileFd = open(filePath, O_RDONLY);
8. if (fd == -1) {
9. LOGE("open failed, errno=%{public}d", errno);
10. return 1;
11. }

13. char buffer[4096];
14. ssize_t bytesRead = -1;;
15. while ((bytesRead = read(fileFd, buffer, sizeof(buffer))) > 0) {
16. if (write(fd, buffer, bytesRead) < bytesRead) {
17. close(fileFd);
18. return 1;
19. }
20. }
21. close(fileFd);
22. return 0;
23. }

25. // 系统打印预览界面回调，首次拉起或用户修改打印参数时的延迟文件写入回调。可以根据新参数适当修改打印文件
26. static void OnStartLayoutWriteCb(const char *jobId,
27. uint32_t fd,
28. const Print_PrintAttributes *oldAttrs,
29. const Print_PrintAttributes *newAttrs,
30. Print_WriteResultCallback writeCallback)
31. {
32. // 将数据写入系统提供的fd中，每次回调的fd不一定相同，请不要保存此fd
33. uint32_t retCode = WriteFile(fd, oldAttrs, newAttrs);
34. // 通知打印系统文件写入完成，若需要异步写入数据，请保存好jobId
35. // retCode取值：0-写入成功，1-写入异常，2-无需重新写入
36. writeCallback(jobId, retCode);
37. }

39. // 打印文件写入完成后，系统打印预览界面会进行预览，此时用户可以点击“开始打印”下发任务
40. // 任务ID对应的打印状态变化的回调函数
41. static void OnJobStateChangedCb(const char *jobId, uint32_t state)
42. {
43. // jobState取值：0-任务准备中，1-任务排队中， 2-任务打印中， 3-任务异常暂停， 4-任务结束， 100-任务未知异常
44. LOGI("dosomething with OnJobStateChangedCb, jobId: %{public}s, jobState: %{public}u", jobId, state);
45. }

47. // 下发打印任务
48. static napi_value NativeStartPrintByNative(napi_env env, napi_callback_info info) {
49. napi_value n_ret = nullptr;
50. void *context = nullptr;
51. size_t argc = 1;
52. napi_value argv[1] = {nullptr};
53. // 假设 napi_get_cb_info 和 napi_unwrap 均正常返回
54. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
55. napi_unwrap(env, argv[0], &context);

57. // 调用打印接口以拉起系统打印预览界面
58. std::string printJobName = "test";
59. Print_PrintDocCallback printDocCallback = { OnStartLayoutWriteCb, OnJobStateChangedCb };
60. Print_ErrorCode ret = OH_Print_StartPrintByNative(printJobName.c_str(), printDocCallback, context);
61. napi_get_boolean(env, !ret, &n_ret);
62. return n_ret;
63. }

65. // 添加napi接口声明
66. EXTERN_C_START
67. static napi_value Init(napi_env env, napi_value exports)
68. {
69. napi_property_descriptor desc[] = {
70. { "nativeStartPrintByNative", nullptr, NativeStartPrintByNative, nullptr, nullptr, nullptr, napi_default, nullptr },
71. };
72. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
73. return exports;
74. }
75. EXTERN_C_END
```

主页上新增一个按钮，单击调用c++的nativeStartPrintByNative接口拉起打印预览界面。

```
1. // Index.ets

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column() {
9. Button('OH_Print_StartPrintByNative')
10. .onClick(() => {
11. HiLog.info("OH_Print_StartPrintByNative onClick");
12. let ctx: Context | undefined = this.getUIContext().getHostContext();
13. let ret: boolean= testNapi.nativeStartPrintByNative(ctx);
14. HiLog.info(`nativeStartPrintByNative ret: ${JSON.stringify(ret)}`);
15. })
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }
```

### 步骤5. 通过打印接口直接下发打印任务

封装c++接口，示例仅演示从已添加打印设备列表获取信息并下发任务。

```
1. // napi_init.cpp

3. // 下发打印任务
4. static napi_value NativeStartPrintJob(napi_env env, napi_callback_info info) {
5. napi_value n_ret = nullptr;
6. napi_get_boolean(env, false, &n_ret);
7. Print_ErrorCode ret = PRINT_ERROR_INVALID_PARAMETER;

9. // 获取已添加打印机的列表
10. Print_StringList pList = { 0 };
11. ret = OH_Print_QueryPrinterList(&pList);
12. LOGI("OH_Print_QueryPrinterList ret = %{public}d", ret);
13. if (ret == PRINT_ERROR_NONE) {
14. return n_ret;
15. }
16. LOGI("pList->count: %{public}d", pList.count);
17. if (pList.count <= 0 || (!pList.list)) {
18. return n_ret;
19. }
20. // 打印列表中所有的打印机Id
21. for (uint32_t index = 0; index < pList.count; index++) {
22. LOGI("pList->list[%{public}d]： %{public}s", index, pList.list[index]);
23. }

25. // 获取列表中第一台打印机属性
26. const char *printerId = pList.list[0];
27. Print_PrinterInfo *printerInfo = nullptr;
28. ret = OH_Print_QueryPrinterInfo(printerId, &printerInfo);
29. if (ret == PRINT_ERROR_NONE) {
30. return n_ret;
31. }
32. // 打开要打印的文件，可以有多个，沙箱内合法路径
33. const char* filePath = "/data/storage/el2/base/files/test.pdf";
34. int32_t fd = open(filePath, O_RDONLY);
35. if (fd == -1) {
36. LOGE("open failed, errno=%{public}d", errno);
37. ret = PRINT_ERROR_INVALID_PARAMETER;
38. return n_ret;
39. }
40. std::vector<uint32_t> fdList = { static_cast<uint32_t>(fd) };
41. // 本例子使用首选项 printerInfo->defaultValue 作为打印任务参数来下发任务
42. Print_PrintJob* printJob = new Print_PrintJob{ "jobName",
43. fdList.data(),
44. static_cast<uint32_t>(fdList.size()),
45. printerInfo->printerId,
46. 1, // 打印份数
47. printerInfo->defaultValue.defaultPaperSource,
48. printerInfo->defaultValue.defaultMediaType,
49. printerInfo->defaultValue.defaultPageSizeId,
50. printerInfo->defaultValue.defaultColorMode,
51. printerInfo->defaultValue.defaultDuplexMode,
52. printerInfo->defaultValue.defaultResolution,
53. printerInfo->defaultValue.defaultMargin,
54. true,
55. printerInfo->defaultValue.defaultOrientation,
56. printerInfo->defaultValue.defaultPrintQuality,
57. DOCUMENT_FORMAT_PDF,
58. printerInfo->defaultValue.otherDefaultValues, };
59. ret = OH_Print_StartPrintJob(printJob);
60. close(fd);
61. // 使用完打印机属性和添加列表后需要及时释放
62. OH_Print_ReleasePrinterInfo(printerInfo);
63. OH_Print_ReleasePrinterList(&pList);

65. napi_get_boolean(env, !ret, &n_ret);
66. return n_ret;
67. }

69. // 添加napi接口声明
70. EXTERN_C_START
71. static napi_value Init(napi_env env, napi_value exports)
72. {
73. napi_property_descriptor desc[] = {
74. { "nativeStartPrintJob", nullptr, NativeStartPrintJob, nullptr, nullptr, nullptr, napi_default, nullptr },
75. };
76. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
77. return exports;
78. }
79. EXTERN_C_END
```

主页上新增一个按钮，单击调用c++的nativeStartPrintByNative直接发送任务。

```
1. // Index.ets

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column() {
9. Button('OH_Print_StartPrintJob')
10. .onClick(() => {
11. HiLog.info("OH_Print_StartPrintJob onClick");
12. let ret: boolean = testNapi.nativeStartPrintJob();
13. HiLog.info(`OH_Print_StartPrintJob ret: ${JSON.stringify(ret)}`);
14. })
15. }
16. .width('100%')
17. }
18. .height('100%')
19. }
20. }
```
