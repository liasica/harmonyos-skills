---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-urpccall
title: 使用URPC进行远程程序调用
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > URPC场景 > 使用URPC进行远程程序调用
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:cfe73a9d0c147ed93701ea3ab77324bc4f05a5892126f255ee710097b397e802
---

## 场景介绍

发送URPC请求，可以设置优先级等参数，返回来自远程服务器的URPC响应。当发起请求后，可以选择取消指定或正在进行的URPC请求。当完成请求后，需要关闭请求来释放与此URPC关联的资源。

## 约束与限制

* 使用URPC进行远程程序调用能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。
* 此功能需要配合部署远程服务器。如有需要，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)的方式与我们联系。

## 使用示例

### 创建urpcStub

1. 导入模块

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { urpc } from '@kit.RemoteCommunicationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { describe, beforeAll, beforeEach, afterEach, afterAll, it, expect } from '@ohos/hypium';
   ```
2. 定义远程调用的类，作为调用方法的入参和返回值，示例如下：

   ```typescript
   // 定义调用方法的入参类示例
   export class MediaTaskRequestMessage {
     RequestMessage: urpc.FlowbufElement<string>;

     constructor() {
       this.RequestMessage = {type: 'STRING', value: '', name: ''};
     }

     setRequestMessage(RequestMessage: string) {
       this.RequestMessage.value = RequestMessage;
     }

     getRequestMessage(): string {
       return this.RequestMessage.value;
     }

   }

   // 定义用于接收调用方法返回值的类示例
   export class MediaTaskResponseMessage {
     ResponseMessage: urpc.FlowbufElement<string>;

     constructor() {
       this.ResponseMessage = {type: 'STRING', value: '', name: ''};
     }

     setResponseMessage(ResponseMessage: string) {
       this.ResponseMessage.value = ResponseMessage;
     }

     getResponseMessage(): string {
       return this.ResponseMessage.value;
     }

   }
   ```
3. 创建Request对象和Response接收对象。

   ```typescript
   let request = new MediaTaskRequestMessage();
   let response = new MediaTaskResponseMessage();
   ```
4. 配置连接信息，创建发起URPC调用的UrpcStub。

   ```typescript
   // 提前部署好的远程服务器的ip地址和端口号，下面IP地址仅作为示意
   let node: urpc.IpAndPort = {
     ip: '192.168.1.1',
     port: 8000
   }
   let connect: urpc.UrpcConnectConfiguration = {
     node: node,
     protocol: 'eat',
   }
   let config: urpc.UrpcInitConfiguration = {
     timeout: 3000,
     mode: 'client',
     connect: connect
   }
   const funcList:string[] = ['uploadFile'];
   let urpcStub = urpc.urpcStubCreate(config, funcList);
   ```

### 使用call收发网络请求

```typescript
urpcStub.then(async (stub: urpc.UrpcStub) =>{
  let upload_config: urpc.CallingOption = {
    priority: 0
  };
  let urpcPromise = stub.call('uploadFile', request, response, upload_config);
  urpcPromise.promise.then((resp: object) => {
    hilog.info(0x000, 'urpc', 'resp: %{public}s', resp);
  }).catch((err: BusinessError) => {
    hilog.error(0x000, 'urpc', 'the error code is %d', err.code);
  })
}).catch((error: BusinessError) => {
  hilog.error(0x000, 'urpc', 'urpc call failed, error code is %d', error.code);
})
```

### （可选）使用cancel取消网络请求

当调用call发起一次urpc收发请求后，根据业务需要，不用接收响应时，可调用cancel取消指定callingId的请求；若不指定callingId，则取消UrpcStub发起的全部请求。

```typescript
urpcStub.then(async (stub: urpc.UrpcStub) =>{
  let upload_config: urpc.CallingOption = {
    priority: 0
  };
  let urpcPromise = stub.call('uploadFile', request, response, upload_config);
  stub.cancel(urpcPromise.callingId);
}).catch((error: BusinessError) => {
  hilog.error(0x000, 'urpc', 'urpc cancel failed, error code is %d', error.code);
})
```

### 使用destroy关闭URPC

当完成所有urpc收发网络请求后，需调用destroy释放并销毁UrpcStub相关的资源。

```typescript
urpcStub.then(async (stub: urpc.UrpcStub) =>{
  stub.destroy();
}).catch((error: BusinessError) => {
  hilog.error(0x000, 'urpc', 'urpc destroy failed, error code is %d', error.code);
})
```
