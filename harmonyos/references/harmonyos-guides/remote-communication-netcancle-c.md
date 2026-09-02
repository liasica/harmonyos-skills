---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-netcancle-c
title: 取消网络请求（C++）
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 发起HTTP请求，获取响应 > 取消网络请求（C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:cb15c6f8669a4d1dd9da026283a95e0a1fa64553f8c1d7ac87c1750052c0ab88
---

在远场通信服务的框架中，使用HMS\_Rcp\_CancelSession方法可以取消传入session的所有正在进行的网络请求。如果开发者需要取消特定的一个网络请求，可以使用HMS\_Rcp\_CancelRequest方法，并传入需要取消的请求，以实现这一目标。开发者们可以根据具体需求，灵活地管理和控制网络请求的执行。总之，HMS\_Rcp\_CancelRequest方法的灵活运用，不仅能够优化网络资源的使用，还能提升应用程序的用户体验。

## 约束与限制

取消网络请求能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-overview.md#hms_rcp_cancelrequest)。

| 接口名 | 描述 |
| --- | --- |
| uint32\_t HMS\_Rcp\_CancelRequest([Rcp\_Session](../harmonyos-references/remote-communication-overview.md#rcp_session) \*session, const [Rcp\_Request](../harmonyos-references/remote-communication-overview.md#rcp_request) \*request); | 取消指定或所有正在进行的会话请求。 |

## 使用示例

1. CPP侧导入模块。

   ```cpp
   #include "RemoteCommunicationKit/rcp.h"
   #include <cstdlib>
   #include <cstring>
   #include <cstdio>
   #include <thread>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```cpp
   librcp_c.so
   ```
3. 创建会话，会话发起请求，并在使用fetch请求后，使用HMS\_Rcp\_CancelRequest取消网络请求。销毁request并关闭session。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。

   ```
   const char *kHttpServerAddress = "http://www.example.com/delete";
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   request->method = RCP_METHOD_DELETE;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   // 发起fetch请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   // 取消请求，处理errCode
   errCode = HMS_Rcp_CancelRequest(session, request);
   napi_value value = nullptr;
   napi_create_int32(env, errCode, &value);
   napi_resolve_deferred(env, ctx->deferred, value);
   // 在退出前取消可能还在执行的requests
   errCode = HMS_Rcp_CancelSession(session);
   // 清理request
   HMS_Rcp_DestroyRequest(request);
   // 关闭session
   errCode = HMS_Rcp_CloseSession(&session);
   ```
