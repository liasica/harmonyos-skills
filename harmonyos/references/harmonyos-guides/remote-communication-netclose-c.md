---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-netclose-c
title: 关闭会话（C++）
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 发起HTTP请求，获取响应 > 关闭会话（C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:312bf9e4983251d900817052562b1b891ae1817add890232be9654edc6c027e4
---

当一个远场通信请求完成，即数据已经成功发送并收到确认，或者在某些情况下，由于超时或其他错误原因，通信尝试失败，此时应立即调用相应的“关闭会话”或“释放资源”方法。这一操作的主要目的是：

* 释放资源：在通信过程中，系统会分配各种资源，包括内存、网络带宽、处理器时间等，以支持数据的发送和接收。一旦通信结束，这些资源应被及时释放，以便它们可以被重新用于其他任务或通信。
* 清理状态：关闭会话还涉及清理与特定会话相关的所有内部状态信息，如缓存、连接状态标志等。这有助于保持系统的清晰性和可预测性，避免潜在的资源泄漏或状态冲突。
* 优化性能：及时释放资源有助于提高系统的整体性能。例如，通过快速释放网络带宽，可以减少延迟，提高后续通信的效率。
* 错误恢复：在遇到通信错误时，正确的关闭会话操作可以帮助系统更快地从错误状态中恢复，避免资源锁定或死锁情况的发生。

在请求结束后，及时关闭会话并释放相关资源是保持系统健康和高效运行的关键步骤。这不仅有助于优化资源利用，还能提高系统的稳定性和可靠性。

## 约束与限制

关闭会话能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-overview.md#hms_rcp_closesession)。

| 接口名 | 描述 |
| --- | --- |
| uint32\_t HMS\_Rcp\_CloseSession([Rcp\_Session](../harmonyos-references/remote-communication-overview.md#rcp_session) \*\*session); | 关闭会话。 |

## 使用示例

1. CPP侧导入模块。

   ```
   1. #include "RemoteCommunicationKit/rcp.h"
   2. #include <stdio.h>
   3. #include <unistd.h>
   ```
2. CMakeLists.txt中添加以下lib。（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```
   1. librcp_c.so
   ```
3. 创建会话，会话发起请求后关闭会话。“http://www.example.com”请根据实际情况替换为想要请求的URL地址。等待响应返回后，销毁request并关闭session。

   ```
   1. void ResponseCallback(void *usrCtx, Rcp_Response *response, uint32_t errCode) {
   2. (void *)usrCtx;
   3. if (response != NULL) {
   4. printf("Response status: %d\n", response->statusCode);
   5. } else {
   6. printf("Fetch failed: errCode: %u\n", errCode);
   7. }
   8. if (response != NULL) {
   9. response->destroyResponse(response);
   10. }
   11. }

   13. int main() {
   14. const char *kHttpServerAddress = "http://www.example.com";
   15. Rcp_Request *request = HMS_Rcp_CreateRequest(kHttpServerAddress);
   16. request->method = RCP_METHOD_GET;
   17. uint32_t errCode = 0;
   18. // 创建session
   19. Rcp_Session *session = HMS_Rcp_CreateSession(NULL, &errCode);
   20. // 配置请求回调
   21. Rcp_ResponseCallbackObject responseCallback = {ResponseCallback, NULL};
   22. // 发起fetch请求
   23. errCode = HMS_Rcp_Fetch(session, request, &responseCallback);
   24. // 等待fetch结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
   25. usleep(1000 * 1000 * 3);
   26. printf("Fetch completed, errCode: %u\n", errCode);
   27. // 在退出前取消可能还在执行的requests
   28. errCode = HMS_Rcp_CancelSession(session);
   29. // 关闭session
   30. errCode = HMS_Rcp_CloseSession(&session);
   31. // 清理request
   32. HMS_Rcp_DestroyRequest(request);
   33. return 0;
   34. }
   ```
