---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-netsend-c
title: 发送网络请求（C++）
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 发起HTTP请求，获取响应 > 发送网络请求（C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:eba5e4e84417582a490fb31b1127dbdec6cd5363a3d7d61c1881edce5563aad5
---

## 约束与限制

发送网络请求能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 如何使用fetchsync发起网络请求

发送同步HTTP请求，可设置请求头和请求体等参数，并返回来自服务器的HTTP响应。常用于获取资源，支持通过拦截器来处理请求和响应。

### 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-overview.md#hms_rcp_fetchsync)。

| 接口名 | 描述 |
| --- | --- |
| [Rcp\_Response](../harmonyos-references/remote-communication-overview.md#rcp_response) \*HMS\_Rcp\_FetchSync([Rcp\_Session](../harmonyos-references/remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](../harmonyos-references/remote-communication-overview.md#rcp_request) \*request, uint32\_t \*errCode); | 发送HTTP请求，并直接返回来自服务器的HTTP响应。 |

### 使用示例

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
3. 创建Request对象。"https://www.example.com"请根据实际情况替换为想要请求的URL地址。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```
   const char *kHttpServerAddress = "https://www.example.com";
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   ```
4. 创建会话。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```cpp
   uint32_t errCode = 0;
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ```
5. 发起请求，并处理返回结果。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```
   Rcp_Response *response = HMS_Rcp_FetchSync(session, request, &errCode);
   if (response != NULL) {
       printf("Response status: %d\n", response->statusCode);
       // ...
   } else {
       printf("FetchSync failed: errCode: %u\n", errCode);
       // ...
   }
   ```
6. 清理response响应和request请求。最后关闭session。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```cpp
   // 清理request
   HMS_Rcp_DestroyRequest(request);
   // 处理response，并清理response
   if (response != NULL) {
       response->destroyResponse(response);
   }
   // 关闭session
   errCode = HMS_Rcp_CloseSession(&session);
   // 处理errCode
   ```

## 如何使用fetch发起异步网络请求

发送异步HTTP请求，可设置请求头和请求体等参数，并返回来自服务器的HTTP响应。常用于获取资源，支持通过拦截器来处理请求和响应。

### 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-overview.md#hms_rcp_fetch)。

| 接口名 | 描述 |
| --- | --- |
| uint32\_t HMS\_Rcp\_Fetch([Rcp\_Session](../harmonyos-references/remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](../harmonyos-references/remote-communication-overview.md#rcp_request) \*request, const [Rcp\_ResponseCallbackObject](../harmonyos-references/remote-communication-overview.md#rcp_responsecallbackobject) \*responseCallback); | 发送HTTP请求，并返回来自服务器的HTTP响应。使用responseCallback异步回调。 |

### 使用示例

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
3. 创建会话，会话发起Fetch请求。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```cpp
   // 创建request
   const char *kHttpServerAddress = "https://www.example.com";
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   ctx->request = request;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ctx->session = session;
   // 请求配置
   Rcp_Configuration config;
   // 初始化配置参数
   (void)memset(&config, 0, sizeof(Rcp_Configuration));
   // 重新设置自动重定向
   config.transferConfiguration.autoRedirect = true;
   // 重新设置请求超时配置参数
   config.transferConfiguration.timeout.transferMs = 1000 * 10;
   config.transferConfiguration.timeout.connectMs = 1000 * 10;
   request->method = RCP_METHOD_GET;
   request->configuration = &config;
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, ctx};
   // 发起请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   ```

## 如何使用get发送网络请求

发送带有默认HTTP参数的HTTP GET请求，并返回来自服务器的HTTP响应。采用异步回调的方式进行处理，提高应用的响应性和效率。常用于从服务器获取数据。

### 使用示例

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
3. 创建会话，会话发起get请求。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```cpp
   const char *kHttpServerAddress = "https://www.example.com";
   // 请求配置
   Rcp_Configuration config;
   // 初始化配置参数
   (void)memset(&config, 0, sizeof(Rcp_Configuration));
   // 重新设置自动重定向
   config.transferConfiguration.autoRedirect = true;
   // 重新设置请求超时配置参数
   config.transferConfiguration.timeout.transferMs = 1000 * 10;
   config.transferConfiguration.timeout.connectMs = 1000 * 10;
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   ctx->request = request;
   request->method = RCP_METHOD_GET;
   request->configuration = &config;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ctx->session = session;
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, ctx};
   // 发起请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   ```

## 如何使用post发送网络请求

发送带有默认HTTP参数的HTTP POST请求，并返回来自服务器的HTTP响应。使用异步回调。常用于向服务器提交数据。与GET请求不同，POST请求将参数包含在请求主体中，适用于创建新资源、提交表单数据或执行某些操作。

### 使用示例

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
3. 创建会话，会话发起post请求。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   // 创建request
   const char *kHttpServerAddress = "http://www.example.com";
   const char *content = "content";
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   // 设置request参数
   request->method = RCP_METHOD_POST;
   request->content = (Rcp_RequestContent *)calloc(1, sizeof(Rcp_RequestContent));
   request->content->type = RCP_CONTENT_TYPE_STRING;
   request->content->data.contentStr.buffer = content;
   request->content->data.contentStr.length = strlen(content);
   ctx->request = request;
   // 请求配置
   Rcp_Configuration config;
   // 初始化配置参数
   (void)memset(&config, 0, sizeof(Rcp_Configuration));
   // 重新设置自动重定向
   config.transferConfiguration.autoRedirect = true;
   // 重新设置请求超时配置参数
   config.transferConfiguration.timeout.transferMs = 1000 * 10;
   config.transferConfiguration.timeout.connectMs = 1000 * 10;
   request->configuration = &config;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ctx->session = session;
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, ctx};
   // 发起请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   ```

## 如何使用put发送网络请求

发送带有默认HTTP参数的HTTP PUT请求，并返回来自服务器的HTTP响应。使用异步回调。常用于向服务器更新资源。PUT请求将更新的数据发送到特定的URL，用于替换指定资源的全部内容。

### 使用示例

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
3. 创建会话，会话发起put请求。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   const char *kHttpServerAddress = "http://www.example.com";
   const char *content = "content";
   // 创建request，并设置request的参数
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   request->method = RCP_METHOD_PUT;
   request->content = (Rcp_RequestContent *)calloc(1, sizeof(Rcp_RequestContent));
   request->content->type = RCP_CONTENT_TYPE_STRING;
   request->content->data.contentStr.buffer = content;
   request->content->data.contentStr.length = strlen(content);
   ctx->request = request;
   // 请求配置
   Rcp_Configuration config;
   // 初始化配置参数
   (void)memset(&config, 0, sizeof(Rcp_Configuration));
   // 重新设置自动重定向
   config.transferConfiguration.autoRedirect = true;
   // 重新设置请求超时配置参数
   config.transferConfiguration.timeout.transferMs = 1000 * 10;
   config.transferConfiguration.timeout.connectMs = 1000 * 10;
   request->configuration = &config;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ctx->session = session;
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, ctx};
   // 发起fetch请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   ```

## 如何使用head发送网络请求

发送带有默认HTTP参数的HTTP HEAD请求，并返回来自服务器的HTTP响应。使用异步回调。类似GET请求，但只返回响应头，不返回实体内容。可以获取资源的元信息，如文件大小、修改日期等。

### 使用示例

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
3. 创建会话，会话发起head请求。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   const char *kHttpServerAddress = "http://www.example.com/head";
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   request->method = RCP_METHOD_HEAD;
   // 请求配置
   Rcp_Configuration config;
   // 初始化配置参数
   (void)memset(&config, 0, sizeof(Rcp_Configuration));
   // 重新设置自动重定向
   config.transferConfiguration.autoRedirect = true;
   // 重新设置请求超时配置参数
   config.transferConfiguration.timeout.transferMs = 1000 * 10;
   config.transferConfiguration.timeout.connectMs = 1000 * 10;
   request->configuration = &config;
   ctx->request = request;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ctx->session = session;
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, ctx};
   // 发起fetch请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   ```

## 如何使用delete发送网络请求

发送带有默认HTTP参数的HTTP DELETE请求，并返回来自服务器的HTTP响应，用于从服务器删除资源，通过向指定URL发送DELETE请求，可以删除该URL上对应的资源。使用异步回调。

### 使用示例

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
3. 创建会话，会话发起delete请求。“https://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   const char *kHttpServerAddress = "http://www.example.com/delete";
   Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   request->method = RCP_METHOD_DELETE;
   // 请求配置
   Rcp_Configuration config;
   // 初始化配置参数
   (void)memset(&config, 0, sizeof(Rcp_Configuration));
   // 重新设置自动重定向
   config.transferConfiguration.autoRedirect = true;
   // 重新设置请求超时配置参数
   config.transferConfiguration.timeout.transferMs = 1000 * 10;
   config.transferConfiguration.timeout.connectMs = 1000 * 10;
   request->configuration = &config;
   ctx->request = request;
   uint32_t errCode = 0;
   // 创建session
   Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ctx->session = session;
   // 配置请求回调
   Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, ctx};
   // 发起fetch请求
   errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   ```
