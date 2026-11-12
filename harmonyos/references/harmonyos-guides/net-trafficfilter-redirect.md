---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-trafficfilter-redirect
title: 重定向网络流量(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 管理网络 > 重定向网络流量(C/C++)
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:45+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9f5135869ffd637855449fa181df7f2377304ad3546ee1f8541515a718535f6b
---

## 场景介绍

网络流量重定向能力通过内核网络协议栈拦截并改写TCP报文的目的地址，将匹配规则的流量转发到指定的代理服务器。典型应用场景包括：

* 企业网络审计：将指定应用或指定目的地址的出站TCP流量重定向到审计代理。
* 内容过滤代理：在网关或终端侧透明拦截HTTP/HTTPS流量并转发到内容安全代理。
* VPN透明代理：将需要代理的应用流量无感知地引流到本地或远程代理服务。

**说明** 

流量重定向能力需要系统权限支持，应用需在module.json5中声明ohos.permission.kernel.TRAFFIC\_FILTER权限，并在原生侧调用C API。

## 约束与限制

**权限约束**

应用必须声明ohos.permission.kernel.TRAFFIC\_FILTER权限。

## 开发步骤

使用本文档涉及接口创建并使用流量重定向时，需先创建Native C++工程，在源文件中封装相关接口，然后在ArkTS层调用封装好的接口，使用hilog或console.info等方法将日志打印到控制台或生成设备日志。

### 添加开发依赖

**添加动态链接库**

在CMakeLists.txt的target\_link\_libraries中添加以下共享库：

```txt
libace_napi.z.so
libhilog_ndk.z.so
libnet_trafficfilter.so
```

**头文件**

```
#include <cstdint>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <arpa/inet.h>

#include "napi/native_api.h"
#include "hilog/log.h"
#include "network/netmanager_ext/net_trafficfilter.h"
```

### 实现流量重定向

在开始实现前，请确保已完成以下前置条件：

* 已创建Native C++工程。
* 已在module.json5的requestPermissions项中声明ohos.permission.kernel.TRAFFIC\_FILTER权限。

1. 在源文件中编写调用该API的代码，实现重定向器的创建。

   使用[OH\_TrafficFilter\_CreateRedirector](../harmonyos-references/capi-net-trafficfilter-h.md#oh_trafficfilter_createredirector)接口创建流量重定向实例。group\_id用于标识重定向器分组，priority控制规则优先级。

   ```
   // 流量重定向器创建：解析JS入参并调用OH_TrafficFilter_CreateRedirector创建实例
   constexpr int BUFFER_SIZE = 128;
   constexpr size_t IP_ADDR_BUF_LEN = 16;
   constexpr size_t IPV4_ADDR_LEN = 4;
   constexpr uint32_t DEFAULT_GROUP_ID = 1001;
   constexpr uint32_t DEFAULT_PRIORITY = 100;
   constexpr uint32_t DEFAULT_PACKET_COPY_LEN = 0xFFFF;
   constexpr uint32_t DEFAULT_NFQUEUE_MAXLEN = 1024;
   constexpr uint32_t DEFAULT_NFQUEUE_FLAGS = 1;
   constexpr uint32_t PROTOCOL_TCP = OH_TRAFFICFILTER_PROTO_TCP;
   constexpr uint16_t DEFAULT_HTTP_PORT = 80;
   constexpr uint16_t DEFAULT_PROXY_PORT = 8080;
   constexpr uint16_t HTTPS_PORT = 443;
   constexpr uint16_t PORT_MIN_VALUE = 0;
   constexpr uint16_t PORT_MAX_VALUE = 65535;
   constexpr uint32_t UID_ANY = 4294967295u;
   constexpr size_t INTERFACE_NAME_MAX_LEN = 31;
   constexpr uint8_t IPV4_DEFAULT_PREFIX = 24;
   constexpr uint8_t IPV6_DEFAULT_PREFIX = 64;
   constexpr uint8_t IPV4_PREFIX_MAX = 32;
   constexpr uint8_t IPV6_PREFIX_MAX = 128;
   constexpr uint32_t LOG_DOMAIN_DEFAULT = 0x0000;
   constexpr size_t ARRAY_BRACKET_PAIR_LEN = 2;
   constexpr size_t ARRAY_CONTENT_START_OFFSET = 1;

   // JS入参索引定义
   constexpr int ARG_IDX_GROUP_ID = 0;
   constexpr int ARG_IDX_PRIORITY = 1;
   constexpr int ARG_IDX_PACKET_COPY_LEN = 2;
   constexpr int ARG_IDX_NFQUEUE_MAXLEN = 3;
   constexpr int ARG_IDX_NFQUEUE_FLAGS = 4;
   constexpr int REQUIRED_ARG_COUNT = 5;

   // 全局重定向器实例指针
   OH_TrafficFilter_Redirector* g_redirector = nullptr;

   static napi_value CreateRedirectorNapi(napi_env env, napi_callback_info info)
   {
       // 获取JS调用时传入的参数个数与参数值
       size_t argc = ARG_IDX_NFQUEUE_FLAGS + 1;
       napi_value args[ARG_IDX_NFQUEUE_FLAGS + 1] = {nullptr};

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 使用默认值初始化参数，若JS端传入则覆盖
       uint32_t groupId = DEFAULT_GROUP_ID;
       uint32_t priority = DEFAULT_PRIORITY;
       uint32_t packetCopyLen = DEFAULT_PACKET_COPY_LEN;
       uint32_t nfqueueMaxlen = DEFAULT_NFQUEUE_MAXLEN;
       uint32_t nfqueueFlags = DEFAULT_NFQUEUE_FLAGS;

       if (argc > ARG_IDX_GROUP_ID) {
           napi_get_value_uint32(env, args[ARG_IDX_GROUP_ID], &groupId);
       }
       if (argc > ARG_IDX_PRIORITY) {
           napi_get_value_uint32(env, args[ARG_IDX_PRIORITY], &priority);
       }
       if (argc > ARG_IDX_PACKET_COPY_LEN) {
           napi_get_value_uint32(env, args[ARG_IDX_PACKET_COPY_LEN], &packetCopyLen);
       }
       if (argc > ARG_IDX_NFQUEUE_MAXLEN) {
           napi_get_value_uint32(env, args[ARG_IDX_NFQUEUE_MAXLEN], &nfqueueMaxlen);
       }
       if (argc > ARG_IDX_NFQUEUE_FLAGS) {
           napi_get_value_uint32(env, args[ARG_IDX_NFQUEUE_FLAGS], &nfqueueFlags);
       }

   // ...

       // 调用系统API创建流量重定向实例
       int32_t ret = OH_TrafficFilter_CreateRedirector(groupId, priority, &g_redirector);

       // 构造结果字符串并返回给JS
       char msg[BUFFER_SIZE * 2];

       napi_value result;
       napi_create_string_utf8(env, msg, strlen(msg), &result);
       return result;
   }
   ```
2. 添加重定向规则。规则中可配置源/目的IP、端口、接口、UID范围以及代理服务器地址。

   使用[OH\_TrafficFilter\_AddRedirectRule](../harmonyos-references/capi-net-trafficfilter-h.md#oh_trafficfilter_addredirectrule)接口向重定向器添加规则。OH\_TrafficFilter\_RedirectRule中protocol固定为TCP，hookPoint（Netfilter钩子点）仅支持PREROUTING和OUTPUT，proxy\_ip与proxy\_port指定代理服务器地址。

   ```
   // 添加重定向规则：解析JSON字符串并调用系统API将规则加入重定向器
   static napi_value AddRedirectRuleNapi(napi_env env, napi_callback_info info)
   {
       // 获取JS调用参数
       size_t argc = 1;
       napi_value args[1] = {nullptr};

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 校验ruleJson参数是否传入
       if (argc <= 0) {
           char msg[] = "ERROR: ruleJson parameter required";
           napi_value result;
           napi_create_string_utf8(env, msg, strlen(msg), &result);
           return result;
       }

       // 读取JSON字符串长度并分配缓冲区
       size_t jsonLen = 0;
       napi_get_value_string_utf8(env, args[0], nullptr, 0, &jsonLen);
       char* jsonStr = new char[jsonLen + 1];
       napi_get_value_string_utf8(env, args[0], jsonStr, jsonLen + 1, &jsonLen);
       std::string json(jsonStr);
       delete[] jsonStr;

       // 将JSON字符串解析为OH_TrafficFilter_RedirectRule结构体
       OH_TrafficFilter_RedirectRule rule;
       int32_t parseRet = BuildRedirectRuleFromJson(json, rule);
       if (parseRet != OH_TRAFFICFILTER_OK) {
           char msg[BUFFER_SIZE];
           napi_value result;
           napi_create_string_utf8(env, msg, strlen(msg), &result);
           return result;
       }

       // 调用系统API向重定向器添加规则
       int32_t ret = OH_TrafficFilter_AddRedirectRule(g_redirector, &rule);

       // 构造结果字符串并返回给JS
       char msg[BUFFER_SIZE * 2];
       napi_value result;
       napi_create_string_utf8(env, msg, strlen(msg), &result);
       return result;
   }
   ```
3. 清除规则并销毁重定向器。

   测试完成后，建议先清除规则，再销毁重定向器，释放相关资源。

   * 使用[OH\_TrafficFilter\_ClearRedirectRule](../harmonyos-references/capi-net-trafficfilter-h.md#oh_trafficfilter_clearredirectrule)清除所有重定向规则。
   * 使用[OH\_TrafficFilter\_DestroyRedirector](../harmonyos-references/capi-net-trafficfilter-h.md#oh_trafficfilter_destroyredirector)销毁重定向器。

   ```
   static napi_value ClearRedirectRuleNapi(napi_env env, napi_callback_info info)
   {
       if (g_redirector == nullptr) {
           char msg[] = "ERROR: No redirector exists";
           napi_value result;
           napi_create_string_utf8(env, msg, strlen(msg), &result);
           return result;
       }

       int32_t ret = OH_TrafficFilter_ClearRedirectRule(g_redirector);

       char msg[BUFFER_SIZE * 2];
       napi_value result;
       napi_create_string_utf8(env, msg, strlen(msg), &result);
       return result;
   }
   ```

   ```
   static napi_value DestroyRedirectorNapi(napi_env env, napi_callback_info info)
   {
       if (g_redirector != nullptr) {
           OH_TrafficFilter_DestroyRedirector(g_redirector);
           g_redirector = nullptr;

           char msg[] = "SUCCESS: Redirector destroyed";
           napi_value result;
           napi_create_string_utf8(env, msg, strlen(msg), &result);
           return result;
       }
       char msg[] = "WARNING: No redirector to destroy";
       napi_value result;
       napi_create_string_utf8(env, msg, strlen(msg), &result);
       return result;
   }
   ```
4. 初始化并导出通过N-API封装的napi\_value类型对象，通过外部函数接口将函数提供给JavaScript调用。

   ```
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "createRedirector", nullptr, CreateRedirectorNapi, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "destroyRedirector", nullptr, DestroyRedirectorNapi, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "addRedirectRule", nullptr, AddRedirectRuleNapi, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "clearRedirectRule", nullptr, ClearRedirectRuleNapi, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "getRuleTemplate", nullptr, GetRuleTemplateNapi, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "queryProcess", nullptr, QueryProcessNapi, nullptr, nullptr, nullptr, napi_default, nullptr }
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END
   ```
5. 将上一步中初始化成功的对象通过RegisterEntryModule函数，使用napi\_module\_register函数将模块注册到Node.js中。

   ```
   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "entry",
       .nm_priv = nullptr,
       .reserved = { 0 },
   };

   extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   {
       napi_module_register(&demoModule);
   }
   ```

### 查询连接所属进程

[OH\_TrafficFilter\_QueryProcess](../harmonyos-references/capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess) 可根据五元组（源IP、目的IP、源端口、目的端口、协议）查询发起该连接的进程信息，常用于在重定向前识别流量归属。

```
// 查询连接所属进程：根据五元组信息查询发起该连接的进程
struct QueryArgs {
    std::string srcIp;      // 源IP地址
    std::string dstIp;      // 目的IP地址
    uint32_t srcPort = 0;   // 源端口
    uint32_t dstPort = 0;   // 目的端口
    uint32_t protocol = PROTOCOL_TCP; // 协议类型
};

static std::string ParseQueryArgsFromNapi(napi_env env, const napi_value args[], QueryArgs& queryArgs)
{
    // 从 JS参数中解析五元组（源/目的IP、端口、协议）
    int ardIdxDstIp = 2;
    int argIdxDstPort = 3;
    int argIdxProtocol = 4;
    size_t srcIpLen = 0;
    size_t dstIpLen = 0;

    // 获取源IP与目的IP字符串长度
    napi_get_value_string_utf8(env, args[0], nullptr, 0, &srcIpLen);
    napi_get_value_string_utf8(env, args[ardIdxDstIp], nullptr, 0, &dstIpLen);

    std::vector<char> srcIpBuf(srcIpLen + 1);
    std::vector<char> dstIpBuf(dstIpLen + 1);

    napi_get_value_string_utf8(env, args[0], srcIpBuf.data(), srcIpBuf.size(), &srcIpLen);
    napi_get_value_string_utf8(env, args[ardIdxDstIp], dstIpBuf.data(), dstIpBuf.size(), &dstIpLen);

    queryArgs.srcIp = srcIpBuf.data();
    queryArgs.dstIp = dstIpBuf.data();

    // 获取源端口、目的端口与协议类型
    napi_get_value_uint32(env, args[1], &queryArgs.srcPort);
    napi_get_value_uint32(env, args[argIdxDstPort], &queryArgs.dstPort);
    napi_get_value_uint32(env, args[argIdxProtocol], &queryArgs.protocol);

    // 校验端口范围与协议类型是否合法
    if (queryArgs.srcPort > PORT_MAX_VALUE || queryArgs.dstPort > PORT_MAX_VALUE) {
        return "ERROR: Invalid port value";
    }

    if (queryArgs.protocol != OH_TRAFFICFILTER_PROTO_TCP && queryArgs.protocol != OH_TRAFFICFILTER_PROTO_UDP) {
        return "ERROR: Invalid protocol value (must be TCP=6 or UDP=17)";
    }

    return "";
}

static std::string BuildQueryConnectionInfo(
    napi_env env,
    const napi_value args[],
    OH_TrafficFilter_ConnectionInfo& connectionInfo)
{
    // 根据五元组构建OH_TrafficFilter_ConnectionInfo结构体
    QueryArgs queryArgs;
    std::string error = ParseQueryArgsFromNapi(env, args, queryArgs);
    if (!error.empty()) {
        return error;
    }

    OH_LOG_INFO(LOG_APP,
        "QueryProcessNapi - srcIp=%{public}s, srcPort=%{public}u, dstIp=%{public}s, "
        "dstPort=%{public}u, protocol=%{public}u",
        queryArgs.srcIp.c_str(), queryArgs.srcPort,
        queryArgs.dstIp.c_str(), queryArgs.dstPort, queryArgs.protocol);

    memset(&connectionInfo, 0, sizeof(connectionInfo));
    connectionInfo.size = sizeof(OH_TrafficFilter_ConnectionInfo);

    // 解析源IP并按地址族填充
    connectionInfo.srcIp.family = DetectIPFamilyFromAddr(queryArgs.srcIp);
    if (!ParseIPAddressByFamily(queryArgs.srcIp, connectionInfo.srcIp.family,
        connectionInfo.srcIp.addr)) {
        return "ERROR: Invalid source IP address";
    }
    connectionInfo.srcPort = static_cast<uint16_t>(queryArgs.srcPort);

    connectionInfo.dstIp.family = DetectIPFamilyFromAddr(queryArgs.dstIp);
    if (!ParseIPAddressByFamily(queryArgs.dstIp, connectionInfo.dstIp.family,
        connectionInfo.dstIp.addr)) {
        return "ERROR: Invalid destination IP address";
    }
    connectionInfo.dstPort = static_cast<uint16_t>(queryArgs.dstPort);

    connectionInfo.protocol = static_cast<uint8_t>(queryArgs.protocol);
    return "";
}

static napi_value CreateQueryResponseNapi(
    napi_env env,
    int32_t ret,
    const OH_TrafficFilter_ProcessInfo& processInfo)
{
    char response[BUFFER_SIZE * 2];
    if (ret == OH_TRAFFICFILTER_OK) {
        OH_LOG_INFO(LOG_APP,
            "QueryProcessNapi - Process found: pid=%{public}u, uid=%{public}u",
            processInfo.pid, processInfo.uid);
    } else if (ret == OH_TRAFFICFILTER_ERROR_NOT_FOUND) {
        OH_LOG_ERROR(LOG_APP, "QueryProcessNapi - Process not found");
    } else if (ret == OH_TRAFFICFILTER_ERROR_INVALID_PARAM) {
        OH_LOG_ERROR(LOG_APP, "QueryProcessNapi - Invalid parameters");
    } else {
        OH_LOG_ERROR(LOG_APP, "QueryProcessNapi - Query failed with ret=%{public}d", ret);
    }

    napi_value result;
    napi_create_string_utf8(env, response, strlen(response), &result);
    return result;
}

static napi_value QueryProcessNapi(napi_env env, napi_callback_info info)
{
    // 查询连接所属进程的主入口
    size_t argc = REQUIRED_ARG_COUNT;
    napi_value args[REQUIRED_ARG_COUNT] = {nullptr};

    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    auto CreateStringResult = [env](const char* msg) -> napi_value {
        napi_value result;
        napi_create_string_utf8(env, msg, strlen(msg), &result);
        return result;
    };

    // 校验必需参数个数
    if (argc < REQUIRED_ARG_COUNT) {
        return CreateStringResult("ERROR: Missing required parameters");
    }

    // 构建连接信息结构体
    OH_TrafficFilter_ConnectionInfo connectionInfo;
    std::string error = BuildQueryConnectionInfo(env, args, connectionInfo);
    if (!error.empty()) {
        return CreateStringResult(error.c_str());
    }

    // 清零并设置进程信息结构体大小
    OH_TrafficFilter_ProcessInfo processInfo;
    memset(&processInfo, 0, sizeof(processInfo));
    processInfo.size = sizeof(OH_TrafficFilter_ProcessInfo);

    // 调用系统 API 查询进程信息
    int32_t ret = OH_TrafficFilter_QueryProcess(&connectionInfo, &processInfo);

    return CreateQueryResponseNapi(env, ret, processInfo);
}
```

## 调测验证

1. 连接设备，使用DevEco Studio打开搭建好的工程。
2. 运行工程，进入重定向管理页面。
3. 点击**Create Redirector**按钮创建重定向实例。
4. 配置目标IP、目标端口、代理IP和代理端口，点击**Add Redirect Rule**添加规则。
5. 在设备上触发匹配规则的TCP流量（例如访问目标IP的80端口），验证流量被重定向到代理服务器。
6. 如需查询连接归属进程，点击**Query Process**并输入五元组信息。
7. 测试完成后，先点击**Clear Redirect Rule**清除规则，再点击**Destroy Redirector**释放资源。
