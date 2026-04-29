---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-netmanager-guidelines
title: 管理网络连接(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 连接网络 > 管理网络连接(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:075f6bfdc626eea4ffc6cf3b2798abfac41c9982e311bc2e0a1dda84d10762e7
---

## 场景介绍

NetConnection模块提供了常用网络信息查询的能力。

## 接口说明

NetConnection常用接口如下表所示，详细的接口说明请参考[net\_connection.h](../harmonyos-references/capi-net-connection-h.md)。

| 接口名 | 描述 |
| --- | --- |
| OH\_NetConn\_HasDefaultNet(int32\_t \*hasDefaultNet) | 检查默认数据网络是否被激活，判断设备是否有网络连接，以便在应用程序中采取相应的措施。 |
| OH\_NetConn\_GetDefaultNet(NetConn\_NetHandle \*netHandle) | 获得默认激活的数据网络。 |
| OH\_NetConn\_IsDefaultNetMetered(int32\_t \*isMetered) | 检查当前网络上的数据流量使用是否被计量。 |
| OH\_NetConn\_GetConnectionProperties(NetConn\_NetHandle \*netHandle, NetConn\_ConnectionProperties \*prop) | 获取netHandle对应的网络的连接信息。 |
| OH\_NetConn\_GetNetCapabilities (NetConn\_NetHandle \*netHandle, NetConn\_NetCapabilities \*netCapacities) | 获取netHandle对应的网络的能力信息。 |
| OH\_NetConn\_GetDefaultHttpProxy (NetConn\_HttpProxy \*httpProxy) | 获取网络默认的代理配置信息。 如果设置了全局代理，则会返回全局代理配置信息。如果进程已经绑定到指定netHandle对应的网络，则返回网络句柄对应网络的代理配置信息。在其他情况下，将返回默认网络的代理配置信息。 |
| OH\_NetConn\_GetAddrInfo (char \*host, char \*serv, struct addrinfo \*hint, struct addrinfo \*\*res, int32\_t netId) | 通过netId获取DNS结果。 |
| OH\_NetConn\_FreeDnsResult(struct addrinfo \*res) | 释放DNS结果内存。 |
| OH\_NetConn\_GetAllNets(NetConn\_NetHandleList \*netHandleList) | 获取所有处于连接状态的网络列表。 |
| OHOS\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver) | 注册自定义DNS解析器。  **弃用：** 从API version 13开始废弃。  **替代：** 推荐使用OH\_NetConn\_RegisterDnsResolver。 |
| OHOS\_NetConn\_UnregisterDnsResolver(void) | 取消注册自定义DNS解析器。  **弃用：** 从API version 13开始废弃。  **替代：** 推荐使用OH\_NetConn\_UnregisterDnsResolver。 |
| OH\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver) | 注册自定义DNS解析器。 |
| OH\_NetConn\_UnregisterDnsResolver(void) | 取消注册自定义DNS解析器。 |
| OH\_NetConn\_SetPacUrl(const char \*pacUrl) | 设置系统级代理自动配置(PAC)脚本地址。 |
| OH\_NetConn\_GetPacUrl(char \*pacUrl) | 获取系统级代理自动配置(PAC)脚本地址。 |
| OH\_NetConn\_QueryProbeResult(char \*destination, int32\_t duration, NetConn\_ProbeResultInfo \*probeResultInfo) | 查询探测结果。 |
| OH\_NetConn\_QueryTraceRoute(char \*destination, NetConn\_TraceRouteOption \*option, NetConn\_TraceRouteInfo \*traceRouteInfo) | 查询跟踪路由。 |

## 网络管理接口开发示例

### 开发步骤

使用本文档涉及接口获取网络相关信息时，需先创建Native C++工程，在源文件中将相关接口封装，再在ArkTS层对封装的接口进行调用，使用hilog或者console.log等手段选择打印在控制台或者生成设备日志。

本文以实现获取默认激活的数据网络为例，给出具体的开发指导。

其他接口开发请参考：[完整示例代码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case)。

### 添加开发依赖

**添加动态链接库**

CMakeLists.txt中添加以下lib:

```
1. libace_napi.z.so
2. libnet_connection.so
```

**头文件**

```
1. #include "napi/native_api.h"
2. #include "network/netmanager/net_connection.h"
3. #include "network/netmanager/net_connection_type.h"
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case/entry/src/main/cpp/napi_init.cpp#L16-L20)

### 构建工程

1. 在源文件中编写调用该API的代码，并将结果封装成一个napi\_value类型的值返回给Node.js环境。

   ```
   1. // 获取默认网络的函数
   2. static napi_value GetDefaultNet(napi_env env, napi_callback_info info)
   3. {
   4. size_t argc = 1; // 期望接收一个函数
   5. napi_value args[1] = {nullptr}; // 存储接收到的参数
   6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   7. // ...
   8. int32_t param;
   9. napi_get_value_int32(env, args[0], &param); // 从 args[0] 获取整数值并存储到 param 中

   11. NetConn_NetHandle netHandle;
   12. if (param == 0) { // 如果参数是0
   13. param = OH_NetConn_GetDefaultNet(NULL);
   14. } else {
   15. param = OH_NetConn_GetDefaultNet(&netHandle);
   16. }

   18. napi_value result;
   19. napi_create_int32(env, param, &result);
   20. return result;
   21. }

   23. // 获取默认网络ID的函数
   24. static napi_value NetId(napi_env env, napi_callback_info info)
   25. {
   26. int32_t defaultNetId;
   27. NetConn_NetHandle netHandle;
   28. OH_NetConn_GetDefaultNet(&netHandle);
   29. defaultNetId = netHandle.netId; // 获取默认的 netId
   30. napi_value result;
   31. napi_create_int32(env, defaultNetId, &result);
   32. return result;
   33. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case/entry/src/main/cpp/napi_init.cpp#L43-L81)

   简要说明：这两个函数用于获取系统默认网络连接的相关信息。其中，GetDefaultNet是接收ArkTS端传入的测试参数，返回调用接口后对应的返回值，param可以自行调整；如果返回值为0，代表获取成功，401代表参数错误，201代表没有权限；而NetId函数则用于获取默认网络连接的ID。这些信息可以用于进一步的网络操作。
2. 将通过napi封装好的napi\_value类型对象初始化导出，通过外部函数接口，将以上两个函数暴露给JavaScript使用。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. // Information used to describe an exported attribute. Two properties are defined here: `GetDefaultNet` and `NetId`.
   5. napi_property_descriptor desc[] = {
   6. {"GetDefaultNet", nullptr, GetDefaultNet, nullptr, nullptr, nullptr, napi_default, nullptr},
   7. {"NetId", nullptr, NetId, nullptr, nullptr, nullptr, napi_default, nullptr},
   8. // ...
   9. };
   10. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   11. return exports;
   12. }
   13. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case/entry/src/main/cpp/napi_init.cpp#L318-L348)
3. 将上一步中初始化成功的对象通过RegisterEntryModule函数，使用napi\_module\_register函数将模块注册到Node.js中。

   ```
   1. static napi_module demoModule = {
   2. .nm_version = 1,
   3. .nm_flags = 0,
   4. .nm_filename = nullptr,
   5. .nm_register_func = Init,
   6. .nm_modname = "entry",
   7. .nm_priv = ((void *)0),
   8. .reserved = {0},
   9. };

   11. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case/entry/src/main/cpp/napi_init.cpp#L352-L364)
4. 在工程的index.d.ts文件中定义两个函数的类型。

   * GetDefaultNet函数接受一个数字参数code，返回一个数字类型的值。
   * NetId函数不接受参数，返回一个数字类型的值。

   ```
   1. export const GetDefaultNet: (code: number) => number;
   2. export const NetId: () => number;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case/entry/src/main/cpp/types/libentry/Index.d.ts#L15-L18)
5. 在index.ets文件中对上述封装好的接口进行调用。

   ```
   1. import testNetManager from 'libentry.so';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. enum ReturnCode {
   5. SUCCESS = 0, // 操作成功
   6. MISSING_PERMISSION = 201, // 缺少权限
   7. PARAMETER_ERROR = 401, // 参数错误
   8. }

   10. // ...
   11. @Entry
   12. @Component
   13. struct Index {
   14. @State message: string = ''; // 用于展示日志消息
   15. // ...

   17. build() {
   18. Column() { // 显示 Logger 输出的日志
   19. // ...
   20. Text(this.message)
   21. .fontSize(16)
   22. .fontColor(Color.Black)
   23. .margin({ bottom: 10 })
   24. .id('test-message') // 为测试消息设置 ID，便于测试获取内容

   26. Button($r('app.string.GetDefaultNet'))
   27. .onClick(() => {
   28. this.GetDefaultNet();
   29. })
   30. // ...

   32. Button($r('app.string.CodeNumber'))
   33. .onClick(() => {
   34. this.CodeNumber();
   35. })
   36. // ...
   37. }.width('100%').height('100%').justifyContent(FlexAlign.Center);
   38. }

   40. GetDefaultNet() {
   41. let netId = testNetManager.NetId();
   42. // ...
   43. hilog.info(0x0000, 'testTag', 'The defaultNetId is [' + netId + ']');
   44. // ...
   45. }

   47. CodeNumber() {
   48. let testParam = 1;
   49. // ...
   50. let codeNumber = testNetManager.GetDefaultNet(testParam);
   51. switch (codeNumber) {
   52. case ReturnCode.SUCCESS:
   53. hilog.info(0x0000, 'testTag', 'Test success. [' + codeNumber + ']');
   54. // ...
   55. break;
   56. case ReturnCode.MISSING_PERMISSION:
   57. hilog.info(0x0000, 'testTag', 'Missing permissions. [' + codeNumber + ']');
   58. // ...
   59. break;
   60. case ReturnCode.PARAMETER_ERROR:
   61. hilog.info(0x0000, 'testTag', 'Parameter error. [' + codeNumber + ']');
   62. // ...
   63. break;
   64. default:
   65. hilog.info(0x0000, 'testTag', 'Unexpected result: [' + codeNumber + ']');
   66. // ...
   67. break;
   68. }
   69. // ...
   70. }
   71. // ...
   72. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case/entry/src/main/ets/pages/Index.ets#L17-L463)
6. 配置CMakeLists.txt，本模块需要用到的共享库是libnet\_connection.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。

   注意

   如图所示，在add\_library中的entry是工程自动生成的modname。若要做修改，需和步骤3中.nm\_modname保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/XCDccINZQhuSL4YWCC5Bmg/zh-cn_image_0000002589324793.png?HW-CC-KV=V1&HW-CC-Date=20260429T053242Z&HW-CC-Expire=86400&HW-CC-Sign=A7319ECCCAB1A31815ABCE136FA866E7CD0B6E3DAFAB13FA6E2D86DBA42B5190)

经过以上步骤，整个工程的搭建已经完成，接下来就可以连接设备运行工程进行日志查看了。

## 测试步骤

1. 连接设备，使用DevEco Studio打开搭建好的工程。
2. 运行工程，设备上会弹出以下所示图片。

   * 点击GetDefaultNet时获取的是默认网络ID。
   * 点击codeNumber时获取的是接口返回的响应状态码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/eunWMD63R7OlEaFYia8jTA/zh-cn_image_0000002589244731.png?HW-CC-KV=V1&HW-CC-Date=20260429T053242Z&HW-CC-Expire=86400&HW-CC-Sign=92EE3902D35D1BCAC679DFBEF68FE668066F76B708F7026A7CBDC89ACF2DEC60)
3. 点击GetDefaultNet按钮，控制台会打印日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/6LhijtvyQp2T1pnRgiHgzA/zh-cn_image_0000002558764926.png?HW-CC-KV=V1&HW-CC-Date=20260429T053242Z&HW-CC-Expire=86400&HW-CC-Sign=D93E68BE5B476E90FDA24A375CD8D66E452B2D9DC9B0FCBE7612A6BF09B8C4D8)
4. 点击codeNumber按钮，控制台会打印相应的响应状态码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/laUlanftS2iQWeIVbZl2bg/zh-cn_image_0000002558605270.png?HW-CC-KV=V1&HW-CC-Date=20260429T053242Z&HW-CC-Expire=86400&HW-CC-Sign=2F416BF9C137FA9B717BFE03DAC91C06D6163E945637DCB883FE044659E4CF1A)
