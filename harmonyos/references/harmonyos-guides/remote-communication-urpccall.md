---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-urpccall
title: 使用URPC进行远程程序调用
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > URPC场景 > 使用URPC进行远程程序调用
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0acedd03f5ae358aa0b945b8a1f4200145d856b26ced6be5ee0d95535cb27f2a
---

## 场景介绍

发送一个URPC请求，可以设置优先级等参数，返回来自远程服务器的URPC响应。当发起请求后，可以选择取消指定或正在进行的URPC请求。当完成请求后，需要关闭请求来释放与此URPC关联的资源。

## 约束与限制

* 使用URPC进行远程程序调用能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。
* 此功能需要配合部署远程服务器。如有需要，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)的方式与我们联系。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-urpcapi.md)。

| 接口名 | 描述 |
| --- | --- |
| call: (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise | 发送一个URPC请求，并返回来自服务器的URPC响应。使用Promise异步回调。 |
| cancel: (callingId?: number | number[]) => void | 取消指定或所有正在进行的URPC请求，返回值为空。 |
| destroy: () => void | 销毁UrpcStub实例 |

## 使用示例

### 创建urpcStub

1. 导入模块

   ```
   1. import { hilog } from "@kit.PerformanceAnalysisKit";
   2. import { urpc } from "@kit.RemoteCommunicationKit";
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义远程调用的类，作为调用方法的入参和返回值，示例如下：

   ```
   1. // 定义调用方法的入参类示例
   2. export class MediaTaskRequestMessage {
   3. RequestMessage: urpc.FlowbufElement<string>;

   5. constructor() {
   6. this.RequestMessage = {type: 'STRING', value: "", name: ""};
   7. }

   9. setRequestMessage(RequestMessage: string) {
   10. this.RequestMessage.value = RequestMessage;
   11. }

   13. getRequestMessage(): string {
   14. return this.RequestMessage.value;
   15. }

   17. }

   19. // 定义用于接收调用方法返回值的类示例
   20. export class MediaTaskResponseMessage {
   21. ResponseMessage: urpc.FlowbufElement<string>;

   23. constructor() {
   24. this.ResponseMessage = {type: 'STRING', value: "", name: ""};
   25. }

   27. setResponseMessage(ResponseMessage: string) {
   28. this.ResponseMessage.value = ResponseMessage;
   29. }

   31. getResponseMessage(): string {
   32. return this.ResponseMessage.value;
   33. }

   35. }
   ```
3. 创建Request对象和Response接收对象。

   ```
   1. let request = new MediaTaskRequestMessage();
   2. let response = new MediaTaskResponseMessage();
   ```
4. 配置连接信息，创建发起URPC调用的UrpcStub。

   ```
   1. // 提前部署好的远程服务器的ip地址和端口号
   2. let node: urpc.IpAndPort = {
   3. ip: '127.0.0.1',
   4. port: 8000
   5. }
   6. let connect: urpc.UrpcConnectConfiguration = {
   7. node: node,
   8. protocol: 'eat',
   9. }
   10. let config: urpc.UrpcInitConfiguration = {
   11. timeout: 3000,
   12. mode: 'client',
   13. connect: connect
   14. }
   15. const funcList:string[] = ["uploadFile"];
   16. let urpcStub = urpc.urpcStubCreate(config, funcList);
   ```

### 使用call收发网络请求

```
1. urpcStub.then(async (stub: urpc.UrpcStub) =>{
2. let upload_config: urpc.CallingOption = {
3. priority: 0
4. };
5. let urpcPromise = stub.call("uploadFile", request, response, upload_config);
6. urpcPromise.promise.then((resp: object) => {
7. hilog.info(0x000, "urpc", "resp: %{public}s", resp);
8. }).catch((err: BusinessError) => {
9. hilog.error(0x000, "urpc", "the error code is %d", err.code);
10. })
11. }).catch((error: BusinessError) => {
12. hilog.error(0x000, "urpc", "urpc call failed, error code is %d", error.code);
13. })
```

### （可选）使用cancel取消网络请求

当调用call发起一次urpc收发请求后，根据业务需要，不用接收响应时，可调用cancel取消指定callingId的请求；若不指定callingId，则取消UrpcStub发起的全部请求。

```
1. urpcStub.then(async (stub: urpc.UrpcStub) =>{
2. let upload_config: urpc.CallingOption = {
3. priority: 0
4. };
5. let urpcPromise = stub.call("uploadFile", request, response, upload_config);
6. stub.cancel(urpcPromise.callingId);
7. }).catch((error: BusinessError) => {
8. hilog.error(0x000, "urpc", "urpc cancel failed, error code is %d", error.code);
9. })
```

### 使用destroy关闭URPC

当完成所有urpc收发网络请求后，需调用destroy释放并销毁UrpcStub相关的资源。

```
1. urpcStub.then(async (stub: urpc.UrpcStub) =>{
2. stub.destroy();
3. }).catch((error: BusinessError) => {
4. hilog.error(0x000, "urpc", "urpc destroy failed, error code is %d", error.code);
5. })
```
