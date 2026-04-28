---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-netcancle-arkts
title: 取消网络请求（ArkTS）
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 发起HTTP请求，获取响应 > 取消网络请求（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f77fa5a45525e72894fe7e2b5a3a2950f11949522c4dce6cbf2045e958ca5e28
---

在远场通信服务的框架中，没有明确指定任何request的情况下，通过调用session.cancel，可以取消所有正在进行的网络请求。当开发者需要取消特定的一个网络请求时，可以使用session.cancel方法，并传入需要取消的请求，以实现这一目标。这样，开发者们就能根据具体需求，灵活地管理和控制网络请求的执行。

## 约束与限制

取消网络请求能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-rcp.md#cancel)。

| 接口名 | 描述 |
| --- | --- |
| cancel(requestToCancel?: [Request](../harmonyos-references/remote-communication-rcp.md#request)| [Request](../harmonyos-references/remote-communication-rcp.md#request)[]): void | - 取消指定网络请求：传入需要取消的请求，返回值为空。  - 取消所有网络请求：无需传入参数，直接调用，返回值为空。 |

## 使用示例

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建会话并创建两个Request，分别发起请求，在请求完成后进行cancel操作。

   * 单独取消某个请求

     ```
     1. // 创建会话
     2. const session = rcp.createSession();
     3. // 创建request1、request2
     4. let request1 = new rcp.Request("https://www.example.com");
     5. let request2 = new rcp.Request("https://www.example.com");

     7. // 分别发起请求
     8. session.fetch(request1).then((response: rcp.Response) => {
     9. console.info(`The response1 code is ${response.statusCode}`);
     10. }).catch((err: BusinessError) => {
     11. console.error(`Request1 error code is ${err.code}, error data is ${err.data}`);
     12. })

     14. session.fetch(request2).then((response: rcp.Response) => {
     15. console.info(`The response2 code is ${response.statusCode}`);
     16. }).catch((err: BusinessError) => {
     17. console.error(`Request2 error code is ${err.code}, error data is ${err.data}`);
     18. })

     20. // 单独取消Request1、request2
     21. session.cancel(request1);
     22. session.cancel(request2);
     ```
   * 取消全部请求

     ```
     1. // 创建会话
     2. const session = rcp.createSession();
     3. // 创建request1、request2
     4. let request1 = new rcp.Request("https://www.example.com");
     5. let request2 = new rcp.Request("https://www.example.com");

     7. // 分别发起请求
     8. session.fetch(request1).then((response: rcp.Response) => {
     9. console.info(`The response1 code is ${response.statusCode}`);
     10. }).catch((err: BusinessError) => {
     11. console.error(`Request1 error code is ${err.code}, error data is ${err.data}`);
     12. })

     14. session.fetch(request2).then((response: rcp.Response) => {
     15. console.info(`The response2 code is ${response.statusCode}`);
     16. }).catch((err: BusinessError) => {
     17. console.error(`Request2 error code is ${err.code}, error data is ${err.data}`);
     18. })
     19. // 取消全部request
     20. session.cancel();
     ```
