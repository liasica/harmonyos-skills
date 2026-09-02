---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-pre-connect
title: 通过预建连接提升HTTP传输性能
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 提升HTTP传输性能 > 通过预建连接提升HTTP传输性能
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:43ff761a2763e8835f124f87e36dcf5a0d260a24219429b7051faf4601fb051f
---

## 概述

从6.1.1(24)版本开始，新增支持预建连接功能。

发起一次HTTP/HTTPS请求一般需要先和目标服务器完成TCP握手和TLS握手（仅HTTPS）。后续请求如果能够复用已完成握手的连接，则可以直接收发数据，从而节省握手的耗时。Remote Communication Kit支持HTTP预建连接的能力。应用可以发起一次不进行数据传输的请求，使后续请求不再需要建立连接。

需要满足以下条件才能复用连接：

* 使用同一个session
* 访问同一个域名
* 网络状态未改变（未发生切换网络、网络关闭等情况）

## 约束与限制

通过预建连接提升HTTP传输性能，支持Phone、PC/2in1、Tablet、Wearable、TV设备。

## 使用预建连接能力（ArkTS）

```typescript
import { rcp } from '@kit.RemoteCommunicationKit';

export async function startConnectionOnlyByRequest() {
  const session = rcp.createSession();
  const request = new rcp.Request('https://example.com', 'GET');
  request.connectOnly = true;

  const response = await session.fetch(request);
  console.info(`Request succeeded, statusCode is ${response.statusCode}`);

  // 此session可用于发起后续请求
}
```

**注意** 

当[Request](../harmonyos-references/remote-communication-rcp.md#request)的connectOnly属性被设置为true时，即使已有连接，此请求也一定会建立一条新的连接。

## 使用预建连接能力（C++）

```cpp
#include "RemoteCommunicationKit/rcp.h"
#include <stdio.h>
#include <thread>

void DataRequestCallback(void *userContext, Rcp_Response *response, uint32_t errCode) {
    printf("DataRequest callback, errCode: %u\n", errCode);
    if (response != nullptr) {
        printf("Data request succeeded, status code: %d\n", response->statusCode);
        response->destroyResponse(response);
    }
}

void dataTransRequest() {
    uint32_t errCode = 0;
    // 创建session
    Rcp_Session *session = HMS_Rcp_CreateSession(nullptr, &errCode);
    printf("create session end: %d\n", errCode);
    const char *kHttpServerAddress = "https://example.com";
    Rcp_Request *dataRequest = HMS_Rcp_CreateRequest(kHttpServerAddress);
    dataRequest->method = RCP_METHOD_GET;

    // 设置本次请求仅建立连接。
    errCode = HMS_Rcp_SetRequestConnectOnly(dataRequest, true);

    Rcp_ResponseCallbackObject callback = {DataRequestCallback, nullptr};

    errCode = HMS_Rcp_Fetch(session, dataRequest, &callback);
    printf("session fetch end: %d\n", errCode);

    // 等待结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
    std::this_thread::sleep_for(std::chrono::milliseconds(1000 * 1000 * 3));

    // 请求完成后，清理request
    HMS_Rcp_DestroyRequest(dataRequest);

    // 此session在被close前可用于发起后续请求
    errCode = HMS_Rcp_CloseSession(&session);
    printf("HMS_Rcp_CloseSession end errCode: %d\n", errCode);
}
```

**注意** 

请求被设置为仅建立连接后，即使已有连接，此请求也一定会建立一条新的连接。

只有通过[HMS\_Rcp\_Fetch](../harmonyos-references/remote-communication-overview.md#hms_rcp_fetch)接口发起的请求可以复用已有的连接；通过[HMS\_Rcp\_FetchSync](../harmonyos-references/remote-communication-overview.md#hms_rcp_fetchsync)接口发起的请求不支持连接复用。

## 通过DefaultSession使用连接复用能力

不同的session之间不支持连接复用。可以通过默认session在同一个session上方便地发起请求。通过[getDefaultSession](../harmonyos-references/remote-communication-rcp.md#getdefaultsession)（ArkTS）和[HMS\_Rcp\_GetDefaultSession](../harmonyos-references/remote-communication-overview.md#hms_rcp_getdefaultsession)（C API）获得的默认session在系统内实际上是同一个session。

**ArkTS：**

```typescript
import { rcp } from '@kit.RemoteCommunicationKit';

export async function startConnectionOnlyByRequest() {
  const defaultSession = rcp.getDefaultSession();
  const request = new rcp.Request('https://example.com', 'GET');
  request.connectOnly = true;

  const response = await defaultSession.fetch(request);
  console.info(`Request succeeded, statusCode is ${response.statusCode}`);

  // 可以在默认session上发起后续请求
}
```

**C++：**

```cpp
#include <stdio.h>
#include <thread>
#include "RemoteCommunicationKit/rcp.h"

Rcp_Session *defaultSession = nullptr;

void DataRequestCallback(void *userContext, Rcp_Response *response, uint32_t errCode) {
    printf("DataRequest callback, errCode: %u\n", errCode);
    if (response != nullptr) {
        printf("Data request succeeded, status code: %d\n", response->statusCode);
        response->destroyResponse(response);
    }
}

void dataTransRequest() {
    uint32_t errCode = 0;
    // 获得默认session
    errCode = HMS_Rcp_GetDefaultSession(&defaultSession);

    printf("create session end: %d\n", errCode);
    const char *kHttpServerAddress = "https://example.com";
    Rcp_Request *dataRequest = HMS_Rcp_CreateRequest(kHttpServerAddress);
    dataRequest->method = RCP_METHOD_GET;
  
    Rcp_ResponseCallbackObject callback = {DataRequestCallback, nullptr};
    errCode = HMS_Rcp_Fetch(defaultSession, dataRequest, &callback);
    printf("defaultSession fetch end: %d\n", errCode);
    // 等待结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
    std::this_thread::sleep_for(std::chrono::milliseconds(1000 * 1000 * 3));
    // 清理request
    HMS_Rcp_DestroyRequest(dataRequest);

    // 可以在默认session上发起后续请求

    // 当不再需要默认session时，使用HMS_Rcp_CloseSession释放对默认session的强引用
    errCode = HMS_Rcp_CloseSession(&defaultSession);
    printf("HMS_Rcp_CloseSession end errCode: %d\n", errCode);
}
```

**注意** 

系统内会自动维护一个默认session。应用的默认session会持有对系统内默认session的引用。当应用所有的默认session被回收后，系统内默认session将被关闭。

当应用再次获取默认session时，系统内会创建一个新的默认session。新创建的默认session无法复用之前的连接。如果需要默认session长期保持连接，应用应长期持有至少一个默认session对象。
