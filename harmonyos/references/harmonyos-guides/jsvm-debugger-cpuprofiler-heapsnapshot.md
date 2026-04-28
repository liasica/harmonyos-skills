---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-debugger-cpuprofiler-heapsnapshot
title: JSVM-API调试&定位
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API调试&定位
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ff54040e1ac7904e18f18bb7e66d0d4fec3d547f3763850890c9049bb4016f26
---

JSVM，即标准JS引擎，是严格遵守ECMAScript规范的JavaScript代码执行引擎。详情参考：[JSVM](../harmonyos-references/capi-jsvm.md)。

基于JSVM的JS代码调试调优能力包括：Debugger、CPU Profiler、Heap Snapshot、Heap Statistics。涉及以下接口：

| 接口名 | 接口功能 |
| --- | --- |
| OH\_JSVM\_GetVM | 获取给定环境的虚拟机实例。 |
| OH\_JSVM\_GetHeapStatistics | 返回一组虚拟机堆的统计数据。 |
| OH\_JSVM\_StartCpuProfiler | 创建并启动一个CPU profiler。 |
| OH\_JSVM\_StopCpuProfiler | 停止CPU profiler并将结果输出到流。 |
| OH\_JSVM\_TakeHeapSnapshot | 获取当前堆快照并将其输出到流。 |
| OH\_JSVM\_OpenInspector | 在指定的主机和端口上激活inspector，将用来调试JS代码。 |
| OH\_JSVM\_OpenInspectorWithName | 基于传入的 pid 和 name 激活 inspector。 |
| OH\_JSVM\_CloseInspector | 尝试关闭剩余的所有inspector连接。 |
| OH\_JSVM\_WaitForDebugger | 等待主机与inspector建立socket连接，连接建立后程序将继续运行。执行Runtime.runIfWaitingForDebugger命令。 |

本文将介绍调试方法、CPU Profiler使用方法和Heap Snapshot使用方法。

## 调试能力使用方法

### 使用 OH\_JSVM\_OpenInspector

1. 在应用工程配置文件module.json中配置网络权限：

   ```
   1. "requestPermissions": [{
   2. "name": "ohos.permission.INTERNET",
   3. "reason": "$string:app_name",
   4. "usedScene": {
   5. "abilities": [
   6. "FromAbility"
   7. ],
   8. "when": "inuse"
   9. }
   10. }]
   ```
2. 为避免debugger过程中的暂停被误报为无响应异常，可以开启DevEco Studio的Debug模式，参考[debug启动调试](../harmonyos-guides-V5/ide-debug-arkts-debug-V5.md)（无需设置断点），或者可以在非主线程的其它线程中运行JSVM。

   ```
   1. // 在非主线程的其他线程中运行JSVM示例代码
   2. static napi_value RunTest(napi_env env, napi_callback_info info)
   3. {
   4. std::thread testJSVMThread(TestJSVM);
   5. testJSVMThread.detach();
   6. return  nullptr;
   7. }
   ```
3. 在执行JS代码之前，调用OH\_JSVM\_OpenInspector在指定的主机和端口上激活inspector，创建socket。例如OH\_JSVM\_OpenInspector(env, "localhost", 9225)，在端侧本机端口9225创建socket。
4. 调用OH\_JSVM\_WaitForDebugger，等待建立socket连接。
5. 检查端侧端口是否打开成功。hdc shell "netstat -anp | grep 9225"。结果为9225端口状态为“LISTEN"即可。
6. 转发端口。hdc fport tcp:9229 tcp:9225。转发开发者个人计算机侧端口9229到端侧端口9225。结果为"Forwardport result:OK"即可。
7. 在chrome浏览器地址栏输入"localhost:9229/json"，回车。获取端口连接信息。拷贝"devtoolsFrontendUrl"字段url内容到地址栏，回车，进入DevTools源码页，将看到在应用中通过OH\_JSVM\_RunScript执行的JS源码，此时暂停在第一行JS源码处。(注："devtoolsFrontendUrl"字段url只支持使用Chrome、Edge浏览器打开，不支持使用Firefox、Safari等浏览器打开。)
8. 用户可在源码页打断点，通过按钮发出各种调试命令控制JS代码执行，并查看变量。
9. 调用OH\_JSVM\_CloseInspector关闭inspector，结束socket连接。

**示例代码**

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

```
1. #include "ark_runtime/jsvm.h"

3. #include <string>

5. using namespace std;

7. // 待调试的JS源码
8. static string srcDebugger = R"JS(
9. const concat = (...args) => args.reduce((a, b) => a + b);
10. var dialogue = concat('"What ', 'is ', 'your ', 'name ', '?"');
11. dialogue = concat(dialogue, ' --', '"My ', 'name ', 'is ', 'Bob ', '."');
12. )JS";

14. // 开启debugger
15. static void EnableInspector(JSVM_Env env) {
16. // 在指定的主机和端口上激活inspector，创建socket。
17. OH_JSVM_OpenInspector(env, "localhost", 9225);
18. // 等待建立socket连接。
19. OH_JSVM_WaitForDebugger(env, true);
20. }

22. // 关闭debugger
23. static void CloseInspector(JSVM_Env env) {
24. // 关闭inspector，结束socket连接。
25. OH_JSVM_CloseInspector(env);
26. }

28. static void RunScript(JSVM_Env env) {
29. JSVM_HandleScope handleScope;
30. OH_JSVM_OpenHandleScope(env, &handleScope);

32. JSVM_Value jsSrc;
33. OH_JSVM_CreateStringUtf8(env, srcDebugger.c_str(), srcDebugger.size(), &jsSrc);

35. JSVM_Script script;
36. OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);

38. JSVM_Value result;
39. OH_JSVM_RunScript(env, script, &result);

41. OH_JSVM_CloseHandleScope(env, handleScope);
42. }

44. void TestJSVM() {
45. JSVM_InitOptions initOptions{};
46. OH_JSVM_Init(&initOptions);

48. JSVM_VM vm;
49. OH_JSVM_CreateVM(nullptr, &vm);
50. JSVM_VMScope vmScope;
51. OH_JSVM_OpenVMScope(vm, &vmScope);

53. JSVM_Env env;
54. OH_JSVM_CreateEnv(vm, 0, nullptr, &env);
55. // 执行JS代码之前打开debugger。
56. EnableInspector(env);
57. JSVM_EnvScope envScope;
58. OH_JSVM_OpenEnvScope(env, &envScope);

60. // 执行JS代码。
61. RunScript(env);

63. OH_JSVM_CloseEnvScope(env, envScope);
64. // 执行JS代码之后关闭debugger。
65. CloseInspector(env);
66. OH_JSVM_DestroyEnv(env);
67. OH_JSVM_CloseVMScope(vm, vmScope);
68. OH_JSVM_DestroyVM(vm);
69. }
```

### 使用 OH\_JSVM\_OpenInspectorWithName

1. 在应用工程配置文件module.json中配置网络权限：

   ```
   1. "requestPermissions": [{
   2. "name": "ohos.permission.INTERNET",
   3. "reason": "$string:app_name",
   4. "usedScene": {
   5. "abilities": [
   6. "FromAbility"
   7. ],
   8. "when": "inuse"
   9. }
   10. }]
   ```
2. 为避免debugger过程中的暂停被误报为无响应异常，可以[开启DevEco Studio的Debug模式](../harmonyos-guides-V5/ide-debug-arkts-debug-V5.md)（无需设置断点），或者可以在非主线程的其他线程中运行JSVM。
3. 打开 inspector 端口，连接 devtools 用于调试，其流程如下：在执行JS代码之前，调用OH\_JSVM\_OpenInspector在指定的主机和端口上激活inspector，创建socket。例如OH\_JSVM\_OpenInspectorWithName(env, 123, "test")，创建 tcp socket 及其对应的 unixdomain 端口。
4. 调用OH\_JSVM\_WaitForDebugger，等待建立socket连接。
5. 检查端侧端口是否打开成功。hdc shell "cat /proc/net/unix | grep jsvm"。结果出现可用的 unix 端口即可，如：jsvm\_devtools\_remote\_9229\_123，其中 9229 为 tcp 端口号，123 为对应的 pid。
6. 转发端口。hdc fport tcp:9229 tcp:9229。转发开发者个人计算机侧端口9229到端侧端口9229。结果为"Forwardport result:OK"即可。
7. 在 chrome 浏览器地址栏输入 "localhost:9229/json"，回车。获取端口连接信息。打开Chrome开发者工具，拷贝"devtoolsFrontendUrl"字段url内容到地址栏，回车，进入DevTools源码页，将看到在应用中通过OH\_JSVM\_RunScript执行的JS源码，此时暂停在第一行JS源码处。(注："devtoolsFrontendUrl"字段url只支持使用Chrome、Edge浏览器打开，不支持使用Firefox、Safari等浏览器打开。)
8. 用户可在源码页打断点，通过按钮发出各种调试命令控制JS代码执行，并查看变量。
9. 调用OH\_JSVM\_CloseInspector关闭inspector，结束socket连接。

**代码示例**

对应的 enable inspector 替换为下面的即可

```
1. // 开启debugger
2. static void EnableInspector(JSVM_Env env) {
3. // 在指定的主机和端口上激活inspector，创建socket。
4. OH_JSVM_OpenInspectorWithName(env, 123, "test");
5. // 等待建立socket连接。
6. OH_JSVM_WaitForDebugger(env, true);
7. }
```

### 使用 Chrome inspect 页面进行调试

除了使用上述打开"devtoolsFrontendUrl"字段url的方法调试代码之外，也可以直接通过Chrome浏览器的 chrome://inspect/#devices 页面进行调试。方法如下：

1. Chrome浏览器中打开 chrome://inspect/#devices，勾选以下内容：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/gDz8uTEwR42trPz_hPyYtg/zh-cn_image_0000002552799726.png?HW-CC-KV=V1&HW-CC-Date=20260427T235424Z&HW-CC-Expire=86400&HW-CC-Sign=705A0C2FDAEAE43BC3C8A834FE5AD72AE49F9FC7FA6B71D00EFB695DAC41EF74)
2. 执行端口转发命令：hdc fport [开发者个人计算机侧端口号] [端侧端口号]

   例如：hdc fport tcp:9227 tcp:9226
3. 点击Port forwarding按钮，左侧输入开发者个人计算机侧端口，右侧输入端侧端口号，点击done。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/kBjOkoRZT4CueWw0NVogcA/zh-cn_image_0000002583439421.png?HW-CC-KV=V1&HW-CC-Date=20260427T235424Z&HW-CC-Expire=86400&HW-CC-Sign=89EF8164E89F9100030203324FA5A26A9B8545054DE7B20D9583B5D77D2A1B47)
4. 点击Configure按钮，输入开发者个人计算机侧的端口号，如localhost:9227。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/qQGGR0d5Q5SNMDQao_bizg/zh-cn_image_0000002552959376.png?HW-CC-KV=V1&HW-CC-Date=20260427T235424Z&HW-CC-Expire=86400&HW-CC-Sign=DA23CFAB965A7788A0DB04992C4F2153E6CAF3C1FF54B3C5E58078B256BD8AAE)
5. 稍等片刻，会在target下出现调试的内容，点击inspect即可调试。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/maEd4LpARo6RXe5LeQwlzg/zh-cn_image_0000002583479377.png?HW-CC-KV=V1&HW-CC-Date=20260427T235424Z&HW-CC-Expire=86400&HW-CC-Sign=22D207C1FCE75E5987C58EF2D97824449D29A802D4784F84C102861322FD47E8)

### 使用 websocket 端口进行调试

除了使用上述打开 "devtoolsFrontendUrl" 字段url的方法通过网页端 chrome devtools 调试代码之外，如果读者了解如何使用 CDP 协议代替网页端 devtools 功能，也可以通过连接 inspector 提供的 websocket 端口进行调试。

其中连接 websocket 的方法为，根据前面提供的网页端调试步骤，在做完端口映射之后（如映射到 9229 端口），在 chrome 浏览器地址栏输入 "localhost:9229/json"，回车，获取"webSocketDebuggerUrl" 字段所对应的 url，然后使用标准的 websocket 客户端连接这个 url 即可发送 CDP 调试协议进行调试。需要注意的是，当前版本 inspector 提供的websocket 端口仅支持接收 Text Frame, Ping Frame 和 Connection Close Frame，所有其他类型的帧都会被视为错误帧而导致 websocket 连接中断。

CDP 协议可以参考 chrome 的[官方文档](https://chromedevtools.github.io/devtools-protocol/)

## CPU Profiler及Heap Snapshot使用方法

### CPU Profiler接口使用方法

1. 在执行JS代码之前，调用OH\_JSVM\_StartCpuProfiler开始采样并返回JSVM\_CpuProfiler。
2. 在执行JS代码后，调用OH\_JSVM\_StopCpuProfiler，传入1中返回的JSVM\_CpuProfiler，传入输出流回调及输出流指针。数据将会写入指定的输出流中。
3. 输出数据为JSON字符串。可存入.cpuprofile文件中。该文件类型可导入Chrome浏览器-DevTools-JavaScript Profiler工具中解析成性能分析视图。

### Heap Snapshot接口使用方法

1. 为分析某段JS代码的堆对象创建情况，可在执行JS代码前后，分别调用一次OH\_JSVM\_TakeHeapSnapshot。传入输出流回调及输出流指针。数据将会写入指定的输出流中。
2. 输出数据可存入.heapsnapshot文件中。该文件类型可导入Chrome浏览器-DevTools-Memory工具中解析成内存分析视图。

### 示例代码

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

```
1. #include "ark_runtime/jsvm.h"

3. #include <fstream>
4. #include <iostream>

6. using namespace std;

8. // 待调优的JS代码。
9. static string srcProf = R"JS(
10. function sleep(delay) {
11. var start = (new Date()).getTime();
12. while ((new Date()).getTime() - start < delay) {
13. continue;
14. }
15. }

17. function work3() {
18. sleep(300);
19. }

21. function work2() {
22. work3();
23. sleep(200);
24. }

26. function work1() {
27. work2();
28. sleep(100);
29. }

31. work1();
32. )JS";

34. // 数据输出流回调，用户自定义，处理返回的调优数据，此处以写入文件为例。
35. static bool OutputStream(const char *data, int size, void *streamData) {
36. auto &os = *reinterpret_cast<ofstream *>(streamData);
37. if (data) {
38. os.write(data, size);
39. } else {
40. os.close();
41. }
42. return true;
43. }

45. static JSVM_CpuProfiler ProfilingBegin(JSVM_VM vm) {
46. // 文件输出流，保存调优数据，/data/storage/el2/base/files为沙箱路径。以包名为com.example.helloworld为例。
47. // 实际文件会保存到/data/app/el2/100/base/com.example.helloworld/files/heap-snapshot-begin.heapsnapshot。
48. ofstream heapSnapshot("/data/storage/el2/base/files/heap-snapshot-begin.heapsnapshot",
49. ios::out | ios::binary | ios::trunc);
50. // 执行JS前获取一次Heap Snapshot数据。
51. OH_JSVM_TakeHeapSnapshot(vm, OutputStream, &heapSnapshot);
52. JSVM_CpuProfiler cpuProfiler;
53. // 开启CPU Profiler。
54. OH_JSVM_StartCpuProfiler(vm, &cpuProfiler);
55. return cpuProfiler;
56. }

58. // 关闭调优数据采集工具
59. static void ProfilingEnd(JSVM_VM vm, JSVM_CpuProfiler cpuProfiler) {
60. // 文件输出流，保存调优数据，/data/storage/el2/base/files为沙箱路径。以包名为com.example.helloworld为例。
61. // 实际文件会保存到/data/app/el2/100/base/com.example.helloworld/files/cpu-profile.cpuprofile。
62. ofstream cpuProfile("/data/storage/el2/base/files/cpu-profile.cpuprofile",
63. ios::out | ios::binary | ios::trunc);
64. // 关闭CPU Profiler，获取数据。
65. OH_JSVM_StopCpuProfiler(vm, cpuProfiler, OutputStream, &cpuProfile);
66. ofstream heapSnapshot("/data/storage/el2/base/files/heap-snapshot-end.heapsnapshot",
67. ios::out | ios::binary | ios::trunc);
68. // 执行JS后再获取一次Heap Snapshot数据，与执行前数据作对比，以分析内存问题或者进行内存调优。
69. OH_JSVM_TakeHeapSnapshot(vm, OutputStream, &heapSnapshot);
70. }

72. static JSVM_Value RunScriptWithStatistics(JSVM_Env env, JSVM_CallbackInfo info) {
73. JSVM_VM vm;
74. OH_JSVM_GetVM(env, &vm);

76. // 开始调优。
77. auto cpuProfiler = ProfilingBegin(vm);

79. JSVM_HandleScope handleScope;
80. OH_JSVM_OpenHandleScope(env, &handleScope);

82. JSVM_Value jsSrc;
83. OH_JSVM_CreateStringUtf8(env, srcProf.c_str(), srcProf.size(), &jsSrc);

85. JSVM_Script script;
86. OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);

88. JSVM_Value result;
89. // 执行JS代码。
90. OH_JSVM_RunScript(env, script, &result);

92. OH_JSVM_CloseHandleScope(env, handleScope);

94. // 结束调优。
95. ProfilingEnd(vm, cpuProfiler);
96. return nullptr;
97. }
98. static JSVM_CallbackStruct param[] = {
99. {.data = nullptr, .callback = RunScriptWithStatistics},
100. };
101. static JSVM_CallbackStruct *method = param;
102. // runScriptWithStatistics方法别名，供JS调用
103. static JSVM_PropertyDescriptor descriptor[] = {
104. {"runScriptWithStatistics", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
105. };
```

样例测试JS

```
1. const char *srcCallNative = R"JS(runScriptWithStatistics();)JS";
```

预计的输出结果：

```
1. 在对应鸿蒙设备内生成两个文件用于后续调优：
2. heap-snapshot-end.heapsnapshot,
3. cpu-profile.cpuprofile
4. 文件功能见上文接口使用方法介绍
```
