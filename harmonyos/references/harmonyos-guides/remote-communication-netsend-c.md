---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-netsend-c
title: 发送网络请求（C++）
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 发起HTTP请求，获取响应 > 发送网络请求（C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11e89474fe61687c3f92cf98d48720d2a7a8cbc548d3dfb3defdfebab9c13268
---

## 约束与限制

发送网络请求能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 如何使用fetchsync发起网络请求

发送一个同步HTTP请求，也可以设置请求头和请求体等参数，并返回来自服务器的HTTP响应。常用于获取资源，支持通过拦截器来处理请求和响应。

### 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-overview.md#hms_rcp_fetchsync)。

| 接口名 | 描述 |
| --- | --- |
| [Rcp\_Response](../harmonyos-references/remote-communication-overview.md#rcp_response) \*HMS\_Rcp\_FetchSync([Rcp\_Session](../harmonyos-references/remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](../harmonyos-references/remote-communication-overview.md#rcp_request) \*request, uint32\_t \*errCode); | 发送一个HTTP请求，并直接返回来自服务器的HTTP响应。 |

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <stdio.h>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建Request对象。"https://www.example.com"请根据实际情况替换为想要请求的URL地址。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```
   1. const char *kHttpServerAddress = "https://www.example.com";
   2. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   ```
4. 创建会话。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```
   1. uint32_t errCode = 0;
   2. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ```
5. 发起请求，并处理返回结果。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```
   1. Rcp_Response *response = HMS_Rcp_FetchSync(session, request, &errCode);
   2. if (response != NULL) {
   3. printf("Response status: %d\n", response->statusCode);
   4. } else {
   5. printf("Fetch failed: errCode: %u\n", errCode);
   6. }
   ```
6. 清理response响应和request请求。最后关闭session。（实际使用时请将该代码块放入main函数或者其他函数区域内）。

   ```
   1. // 清理request
   2. HMS_Rcp_DestroyRequest(request);
   3. // 处理response，并清理response
   4. if (response != NULL) {
   5. response->destroyResponse(response);
   6. }
   7. // 关闭session
   8. errCode = HMS_Rcp_CloseSession(&session);
   9. // 处理errCode
   ```

## 如何使用fetch发起异步网络请求

发送一个异步HTTP请求，也可以设置请求头和请求体等参数，并返回来自服务器的HTTP响应。常用于获取资源，支持通过拦截器来处理请求和响应。

### 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-overview.md#hms_rcp_fetch)。

| 接口名 | 描述 |
| --- | --- |
| uint32\_t HMS\_Rcp\_Fetch([Rcp\_Session](../harmonyos-references/remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](../harmonyos-references/remote-communication-overview.md#rcp_request) \*request, const [Rcp\_ResponseCallbackObject](../harmonyos-references/remote-communication-overview.md#rcp_responsecallbackobject) \*responseCallback); | 发送一个HTTP请求，并返回来自服务器的HTTP响应。使用responseCallback异步回调。 |

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <cstring>
   3. #include <stdio.h>
   4. #include <unistd.h>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建Request对象。"https://www.example.com"请根据实际情况替换为想要请求的URL地址。（完整见步骤5）

   ```
   1. const char *kHttpServerAddress = "https://www.example.com";
   2. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   ```
4. 创建会话。（完整见步骤5）

   ```
   1. uint32_t errCode = 0;
   2. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   ```
5. 发起请求，并处理返回结果。最后关闭session。

   ```
   1. // 异步请求的响应处理回调，请用户自定义
   2. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode)
   3. {
   4. (void *)usrCtx;
   5. if (response != NULL) {
   6. printf("Response status: %d\n", response->statusCode);
   7. } else {
   8. printf("Fetch failed: errCode: %u\n", errCode);
   9. }
   10. // 注意清理响应
   11. if (response != NULL) {
   12. response->destroyResponse(response);
   13. }
   14. }

   16. int main() {
   17. const char *kHttpServerAddress = "https://www.example.com";
   18. // 请求配置
   19. Rcp_Configuration config;
   20. // 初始化配置参数
   21. (void)memset(&config, 0, sizeof(Rcp_Configuration));
   22. // 重新设置自动重定向
   23. config.transferConfiguration.autoRedirect = true;
   24. // 重新设置请求超时配置参数
   25. config.transferConfiguration.timeout.transferMs = 1000 * 10;
   26. config.transferConfiguration.timeout.connectMs = 1000 * 10;
   27. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   28. request->method = RCP_METHOD_GET;
   29. request->configuration = &config;
   30. uint32_t errCode = 0;
   31. // 创建session
   32. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   33. // 配置请求回调
   34. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   35. // 发起fetch请求
   36. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   37. // 等待fetch结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   38. usleep(1000 * 1000 * 3);
   39. printf("Fetch completed, errCode: %u\n", errCode);
   40. // 在退出前取消可能还在执行的requests
   41. errCode = HMS_Rcp_CancelSession(session);
   42. // 清理request
   43. HMS_Rcp_DestroyRequest(request);
   44. // 关闭session
   45. errCode = HMS_Rcp_CloseSession(&session);
   46. // 处理errCode
   47. return 0;
   48. }
   ```

## 如何使用get发送网络请求

发送一个带有默认HTTP参数的HTTP GET请求，并返回来自服务器的HTTP响应。采用异步回调的方式进行处理，提高应用的响应性和效率。常用于从服务器获取数据。

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <cstring>
   3. #include <stdio.h>
   4. #include <unistd.h>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建会话，会话发起get请求。“http://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   1. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode)
   2. {
   3. (void *)usrCtx;
   4. if (response != NULL) {
   5. printf("Response status: %d\n", response->statusCode);
   6. } else {
   7. printf("Fetch failed: errCode: %u\n", errCode);
   8. }
   9. // 注意清理响应
   10. if (response != NULL) {
   11. response->destroyResponse(response);
   12. }
   13. }

   15. int main() {
   16. const char *kHttpServerAddress = "http://www.example.com";
   17. // 请求配置
   18. Rcp_Configuration config;
   19. // 初始化配置参数
   20. (void)memset(&config, 0, sizeof(Rcp_Configuration));
   21. // 重新设置自动重定向
   22. config.transferConfiguration.autoRedirect = true;
   23. // 重新设置请求超时配置参数
   24. config.transferConfiguration.timeout.transferMs = 1000 * 10;
   25. config.transferConfiguration.timeout.connectMs = 1000 * 10;
   26. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   27. request->method = RCP_METHOD_GET;
   28. request->configuration = &config;
   29. uint32_t errCode = 0;
   30. // 创建session
   31. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   32. // 配置请求回调
   33. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   34. // 发起请求
   35. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   36. // 等待结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   37. usleep(1000 * 1000 * 3);
   38. printf("Fetch completed, errCode: %u\n", errCode);
   39. // 在退出前取消可能还在执行的requests
   40. errCode = HMS_Rcp_CancelSession(session);
   41. // 清理request
   42. HMS_Rcp_DestroyRequest(request);
   43. // 关闭session
   44. errCode = HMS_Rcp_CloseSession(&session);
   45. // 处理errCode
   46. return 0;
   47. }
   ```

## 如何使用post发送网络请求

发送一个带有默认HTTP参数的HTTP POST请求，并返回来自服务器的HTTP响应。使用异步回调。常用于向服务器提交数据。与GET请求不同，POST请求将参数包含在请求主体中，适用于创建新资源、提交表单数据或执行某些操作。

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <cstdlib>
   3. #include <cstring>
   4. #include <stdio.h>
   5. #include <unistd.h>
   6. #include <thread>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建会话，会话发起post请求。“http://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   1. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode)
   2. {
   3. (void *)usrCtx;
   4. if (response != NULL) {
   5. printf("Response status: %d\n", response->statusCode);
   6. } else {
   7. printf("Fetch failed: errCode: %u\n", errCode);
   8. }
   9. // 注意清理响应
   10. if (response != NULL) {
   11. response->destroyResponse(response);
   12. }
   13. }

   15. int main() {
   16. const char *kHttpServerAddress = "http://www.example.com";
   17. const char *content = "content";
   18. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   19. // 设置request参数
   20. request->method = RCP_METHOD_POST;
   21. request->content = (Rcp_RequestContent *)calloc(1, sizeof(Rcp_RequestContent));
   22. request->content->type = RCP_CONTENT_TYPE_STRING;
   23. request->content->data.contentStr.buffer = content;
   24. request->content->data.contentStr.length = strlen(content);
   25. // 请求配置
   26. Rcp_Configuration config;
   27. // 初始化配置参数
   28. (void)memset(&config, 0, sizeof(Rcp_Configuration));
   29. // 重新设置自动重定向
   30. config.transferConfiguration.autoRedirect = true;
   31. // 重新设置请求超时配置参数
   32. config.transferConfiguration.timeout.transferMs = 1000 * 10;
   33. config.transferConfiguration.timeout.connectMs = 1000 * 10;
   34. request->configuration = &config;
   35. uint32_t errCode = 0;
   36. // 创建session
   37. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   38. // 配置请求回调
   39. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   40. // 发起请求
   41. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   42. // 等待fetch结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   43. std::this_thread::sleep_for(std::chrono::milliseconds(1000 * 1000 * 3));
   44. printf("Fetch completed, errCode: %u\n", errCode);
   45. // 清理request->content
   46. free(request->content);
   47. // 清理request
   48. HMS_Rcp_DestroyRequest(request);
   49. // 关闭session
   50. errCode = HMS_Rcp_CloseSession(&session);
   51. // 处理errCode
   52. return 0;
   53. }
   ```

## 如何使用put发送网络请求

发送一个带有默认HTTP参数的HTTP PUT请求，并返回来自服务器的HTTP响应。使用异步回调。常用于向服务器更新资源。PUT请求将更新的数据发送到特定的URL，用于替换指定资源的全部内容。

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <cstdlib>
   3. #include <cstring>
   4. #include <stdio.h>
   5. #include <unistd.h>
   6. #include <thread>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建会话，会话发起put请求。“http://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   1. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode)
   2. {
   3. (void *)usrCtx;
   4. if (response != NULL) {
   5. printf("Response status: %d\n", response->statusCode);
   6. } else {
   7. printf("Fetch failed: errCode: %u\n", errCode);
   8. }
   9. // 注意清理响应
   10. if (response != NULL) {
   11. response->destroyResponse(response);
   12. }
   13. }

   15. int main() {
   16. const char *kHttpServerAddress = "http://www.example.com";
   17. const char *content = "content";
   18. // 创建request，并设置request的参数
   19. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   20. request->method = RCP_METHOD_PUT;
   21. request->content = (Rcp_RequestContent *)calloc(1, sizeof(Rcp_RequestContent));
   22. request->content->type = RCP_CONTENT_TYPE_STRING;
   23. request->content->data.contentStr.buffer = content;
   24. request->content->data.contentStr.length = strlen(content);
   25. // 请求配置
   26. Rcp_Configuration config;
   27. // 初始化配置参数
   28. (void)memset(&config, 0, sizeof(Rcp_Configuration));
   29. // 重新设置自动重定向
   30. config.transferConfiguration.autoRedirect = true;
   31. // 重新设置请求超时配置参数
   32. config.transferConfiguration.timeout.transferMs = 1000 * 10;
   33. config.transferConfiguration.timeout.connectMs = 1000 * 10;
   34. request->configuration = &config;
   35. uint32_t errCode = 0;
   36. // 创建session
   37. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   38. // 配置请求回调
   39. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   40. // 发起fetch请求
   41. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   42. // 等待结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   43. std::this_thread::sleep_for(std::chrono::milliseconds(1000 * 1000 * 3));
   44. printf("Fetch completed, errCode: %u\n", errCode);
   45. // 在退出前取消可能还在执行的requests
   46. errCode = HMS_Rcp_CancelSession(session);
   47. // 清理request content
   48. free(request->content);
   49. // 清理request
   50. HMS_Rcp_DestroyRequest(request);
   51. // 关闭session
   52. errCode = HMS_Rcp_CloseSession(&session);
   53. // 处理errCode
   54. return 0;
   55. }
   ```

## 如何使用head发送网络请求

发送一个带有默认HTTP参数的HTTP HEAD请求，并返回来自服务器的HTTP响应。使用异步回调。类似GET请求，但只返回响应头，不返回实体内容。可以获取资源的元信息，如文件大小、修改日期等。

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <cstring>
   3. #include <stdio.h>
   4. #include <unistd.h>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建会话，会话发起head请求。“http://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   1. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode)
   2. {
   3. (void *)usrCtx;
   4. if (response != NULL) {
   5. printf("Response status: %d\n", response->statusCode);
   6. } else {
   7. printf("Fetch failed: errCode: %u\n", errCode);
   8. }
   9. // 注意清理响应
   10. if (response != NULL) {
   11. response->destroyResponse(response);
   12. }
   13. }

   15. int main() {
   16. const char *kHttpServerAddress = "http://www.example.com/head";
   17. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   18. request->method = RCP_METHOD_HEAD;
   19. // 请求配置
   20. Rcp_Configuration config;
   21. // 初始化配置参数
   22. (void)memset(&config, 0, sizeof(Rcp_Configuration));
   23. // 重新设置自动重定向
   24. config.transferConfiguration.autoRedirect = true;
   25. // 重新设置请求超时配置参数
   26. config.transferConfiguration.timeout.transferMs = 1000 * 10;
   27. config.transferConfiguration.timeout.connectMs = 1000 * 10;
   28. request->configuration = &config;
   29. uint32_t errCode = 0;
   30. // 创建session
   31. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   32. // 配置请求回调
   33. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   34. // 发起fetch请求
   35. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   36. // 等待fetch结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   37. usleep(1000 * 1000 * 3);
   38. printf("Fetch completed, errCode: %u\n", errCode);
   39. // 在退出前取消可能还在执行的requests
   40. errCode = HMS_Rcp_CancelSession(session);
   41. // 清理request
   42. HMS_Rcp_DestroyRequest(request);
   43. // 关闭session
   44. errCode = HMS_Rcp_CloseSession(&session);
   45. // 处理errCode
   46. return 0;
   47. }
   ```

## 如何使用delete发送网络请求

发送一个带有默认HTTP参数的HTTP DELETE请求，并返回来自服务器的HTTP响应，用于从服务器删除资源，通过向指定URL发送DELETE请求，可以删除该URL上对应的资源。使用异步回调。

### 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <cstring>
   3. #include <stdio.h>
   4. #include <unistd.h>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建会话，会话发起delete请求。“http://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   1. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode)
   2. {
   3. (void *)usrCtx;
   4. if (response != NULL) {
   5. printf("Response status: %d\n", response->statusCode);
   6. } else {
   7. printf("Fetch failed: errCode: %u\n", errCode);
   8. }
   9. if (response != NULL) {
   10. response->destroyResponse(response);
   11. }
   12. }

   14. int main() {
   15. const char *kHttpServerAddress = "http://www.example.com/delete";
   16. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   17. request->method = RCP_METHOD_DELETE;
   18. // 请求配置
   19. Rcp_Configuration config;
   20. // 初始化配置参数
   21. (void)memset(&config, 0, sizeof(Rcp_Configuration));
   22. // 重新设置自动重定向
   23. config.transferConfiguration.autoRedirect = true;
   24. // 重新设置请求超时配置参数
   25. config.transferConfiguration.timeout.transferMs = 1000 * 10;
   26. config.transferConfiguration.timeout.connectMs = 1000 * 10;
   27. request->configuration = &config;
   28. uint32_t errCode = 0;
   29. // 创建session
   30. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   31. // 配置请求回调
   32. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   33. // 发起fetch请求
   34. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   35. // 等待fetch结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   36. usleep(1000 * 1000 * 3);
   37. printf("Fetch completed, errCode: %u\n", errCode);
   38. // 在退出前取消可能还在执行的requests
   39. errCode = HMS_Rcp_CancelSession(session);
   40. // 清理request
   41. HMS_Rcp_DestroyRequest(request);
   42. // 关闭session
   43. errCode = HMS_Rcp_CloseSession(&session);
   44. // 处理errCode
   45. return 0;
   46. }
   ```
