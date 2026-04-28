---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-netclose-arkts
title: 关闭会话（ArkTS）
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 发起HTTP请求，获取响应 > 关闭会话（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b5bf25ade85ef4b3a005559c95592f11dad47b955b00c84bd7eaad2021c0797
---

当一个HTTP请求完成，即数据已经成功发送并收到确认，或者在某些情况下，由于超时或其他错误原因，通信尝试失败，此时应立即调用相应的“关闭会话”或“释放资源”方法。这一操作的主要目的是：

* 释放资源：在通信过程中，系统会分配各种资源，包括内存、网络带宽、处理器时间等，以支持数据的发送和接收。一旦通信结束，这些资源应被及时释放。
* 清理状态：关闭会话还涉及清理与特定会话相关的所有内部状态信息，如缓存、连接状态标志等。这有助于保持系统的清晰性和可预测性，避免潜在的资源泄漏或状态冲突。
* 优化性能：及时释放资源有助于提高系统的整体性能。例如，通过快速释放网络带宽，可以减少延迟，提高后续通信的效率。
* 错误恢复：在遇到通信错误时，正确的关闭会话操作可以帮助系统更快地从错误状态中恢复，避免资源锁定或死锁情况的发生。

在请求结束后，及时关闭会话并释放相关资源是保持系统健康和高效运行的关键步骤。这不仅有助于优化资源利用，还能提高系统的稳定性和可靠性。

## 约束与限制

关闭会话能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-rcp.md#close)。

| 接口名 | 描述 |
| --- | --- |
| close(): void | 关闭会话。返回为空。 |

## 使用示例

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建会话，会话发起请求后关闭会话。

   ```
   1. // 1、创建会话
   2. const session = rcp.createSession();
   3. // 2、创建Request，"http://www.example.com"请根据实际情况替换为想要请求的URL地址。
   4. let req = new rcp.Request("http://www.example.com/fetch", "GET");
   5. // 3、利用fetch发起网络请求
   6. session.fetch(req).then((response) => {
   7. // 4、对响应的处理，此处为示例，只做打印处理
   8. console.info(`Response succeeded: ${response}`);
   9. }).catch((err: BusinessError) => {
   10. // 5、请求错误处理
   11. console.error(`Response error code is ${err.code}, error data is ${err.data}`);
   12. });
   13. session.close();
   ```
