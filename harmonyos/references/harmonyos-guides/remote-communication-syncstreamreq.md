---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-syncstreamreq
title: 流式传输
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 实现流式请求 > 流式传输
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:38f7453652d6f770f430a631316cd8dbcea660de4bf979b7b6bf6274ba0dea7d
---

## 场景介绍

HTTP流式传输（Streaming）允许客户端与服务器之间以流的形式进行数据交互，而无需等待所有数据准备完毕，能显著提升用户体验。流式传输适用于大文件的上传下载、直播、实时数据更新等场景。

## 约束与限制

流式传输能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 基于缓冲区的流式传输

### 使用示例

1. 导入模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 利用rcp.NetworkInputQueue创建同步写队列对象实现同步写功能。

   ```typescript
   export const testNetworkInputQueue = () => {
     // 创建同步写队列对象
     const networkInputQueue = new rcp.NetworkInputQueue();
     // 模拟文件通过同步读写流上传场景，将文件写入到同步写队列 networkInputQueue 中
     let counter = 0;
     const interval = setInterval(() => {
       // 添加数据到同步写队列
       networkInputQueue.write('a counter ' + counter++);
       console.info(`networkInputQueue write`);
       if (counter === 10) {
         clearInterval(interval);
         // 关闭同步写队列
         networkInputQueue.close();
       }
     }, 1000);
     try {
       // 创建session
       const session = rcp.createSession();
       console.info(`Post start.`);
       // 发起请求，'https://httpbin.org/anything'是示例网址，相关数据在写入队列 networkInputQueue 的同时会同步进行上传
       session.post('https://httpbin.org/anything', networkInputQueue).then((response) => {
         // 结果状态码
         console.info(`Response status code is: ${response.statusCode}`);
         // ...
         if (response && response.statusCode === 200) {
           console.info(`Post succeeded! response: ${response.toString()}`);
         } else {
           console.error(`Post failed.`);
         }
         session.close();
       }).catch((err: BusinessError) => {
         console.error(`Post error code is ${err.code}, error data is ${err.data}`);
         // ...
         session.close();
       });
     } catch (err) {
       console.error(`create session error code is ${err.code}, error data is ${err.data}`);
       // ...
     }
   }
   ```
3. 利用rcp.NetworkOutputQueue创建同步读队列对象实现同步读功能。

   ```typescript
   export const testNetworkOutputQueue = () => {
     // 创建同步读队列对象
     const networkOutputQueue = new rcp.NetworkOutputQueue();
     // 创建session
     try {
       const session = rcp.createSession();
       // 配置请求流数据size
       const numOfChunks = 10;
       const chunkLength = 1000;
       const totalBytes = numOfChunks * chunkLength;
       // 发起请求，'https://httpbin.org/bytes/'是示例网址，响应数据会暂存在同步读队列networkOutputQueue中
       session.get('https://httpbin.org/bytes/' + totalBytes.toString(), networkOutputQueue).then((response) => {
         // ...
         if (response && response.statusCode === 200) {
           console.info(`get bytes succeeded.`);
         } else {
           console.error(`get bytes failed.`);
         }
         session.close();
       }).catch((err: BusinessError) => {
         console.error(`get bytes error code is ${err.code}, error data is ${err.data}`);
         // ...
         session.close();
       });
       // 在需要使用响应数据时，可按需从 `networkOutputQueue` 队列中循环读取，例如每隔 1000 毫秒读取一次，每次读取 1000 个字节的数据
       let totalGetLength = 0;
       const intervalId = setInterval(() => {
         // 读取数据后，开发者需根据具体业务场景进行后续处理
         const chunk = networkOutputQueue.read(chunkLength);
         totalGetLength += chunk.byteLength;
         console.info(`get bytes totalGetLength: ${totalGetLength}`);
         // 数据读取完成后，清除计时器
         if (totalGetLength === totalBytes) {
           clearInterval(intervalId);
           console.info(`get bytes finished.`);
         }
       }, 1000);
     } catch (err) {
       console.error(`create session error code is ${err.code}, error data is ${err.data}`);
       // ...
     }
   }
   ```

## 基于回调函数的流式传输

### 接口说明

具体API说明详见[接口文档](../harmonyos-references/remote-communication-rcp.md#uploadfromstream)。

| 接口名 | 描述 |
| --- | --- |
| uploadFromStream(url: [URLOrString](../harmonyos-references/remote-communication-rcp.md#urlorstring), uploadFrom: [UploadFromStream](../harmonyos-references/remote-communication-rcp.md#uploadfromstream-2)): Promise<[Response](../harmonyos-references/remote-communication-rcp.md#response)> | 从流中上传。 |
| downloadToStream(url: [URLOrString](../harmonyos-references/remote-communication-rcp.md#urlorstring), downloadTo: [DownloadToStream](../harmonyos-references/remote-communication-rcp.md#downloadtostream-2)): Promise<[Response](../harmonyos-references/remote-communication-rcp.md#response)> | 下载到流中。 |

### 使用示例

1. 导入模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义FdReadStream实现rcp.ReadStream接口，从流中读取数据。

   ```typescript
   class FdReadStream implements rcp.ReadStream {
     public readonly fd: number;

     constructor(fd: number) {
       this.fd = fd;
     }

     async read(buffer: ArrayBuffer): Promise<number> {
       return fileIo.read(this.fd, buffer);
     }
   }
   ```
3. 调用uploadFromStream接口以流的形式上传数据。

   ```typescript
   export function testUploadFromStream(uploadFilePath: string) {
     try {
       // 创建session
       const session = rcp.createSession();
       // 根据传入的上传文件的路径打开文件
       const file = fileIo.openSync(uploadFilePath, fileIo.OpenMode.READ_ONLY);
       // 文件读取流
       const fileStream = new rcp.UploadFromStream(new FdReadStream(file.fd));
       // 以流的形式上传数据,'https://httpbin.org/anything'是示例网址
       session.uploadFromStream('https://httpbin.org/anything', fileStream).then((resp) => {
         console.info(`testUploadFromStream response: ${JSON.stringify(resp.statusCode)}`);
         // ...
         if (resp && resp.statusCode === 200) {
           console.info(`testUploadFromStream succeeded.`);
         } else {
           console.error(`testUploadFromStream failed.`);
         }
       }).catch((err: BusinessError) => {
         console.error(`testUploadFromStream error code is ${err.code}, error data is ${err.data}`);
         // ...
         fileIo.closeSync(file.fd);
         session.close();
       }).finally(() => {
         // 完成后关闭文件和session
         fileIo.closeSync(file.fd);
         session.close();
       });
     } catch (err) {
       console.error(`testUploadFromStream error code is ${err.code}, error data is ${err.data}`);
       // ...
     }
   }
   ```
4. 定义FdWriteStream实现WriteStream接口，将数据写入流中。

   ```typescript
   class FdWriteStream implements rcp.WriteStream {
     public readonly fd: number;

     constructor(fd: number) {
       this.fd = fd;
     }

     async write(buffer: ArrayBuffer): Promise<number | void> {
       return fileIo.write(this.fd, buffer);
     }
   }
   ```
5. 调用downloadToStream接口，以流的形式下载数据。

   ```typescript
   export function testDownloadToStream(downloadToPath: string) {
     try {
       // 创建session
       const session = rcp.createSession();
       // 根据传入的下载文件保存路径打开文件
       const file = fileIo.openSync(downloadToPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.WRITE_ONLY);
       // 文件写入流
       const fileStream = { kind: 'stream', stream: new FdWriteStream(file.fd) } as rcp.DownloadToStream;
       // 以流的形式下载数据,'https://httpbin.org/bytes/10000'是示例网址
       session.downloadToStream('https://httpbin.org/bytes/10000', fileStream)
         .then((resp) => {
           console.info(`testDownloadToStream response: ${JSON.stringify(resp.statusCode)}`);
           // ...
           if (resp && resp.statusCode === 200) {
             console.info(`testDownloadToStream succeeded.`);
           } else {
             console.error(`testDownloadToStream failed.`);
           }
         })
         .catch((err: BusinessError) => {
           console.error(`testDownloadToStream error code is ${err.code}, error data is ${err.data}`);
           // ...
           fileIo.close(file.fd);
           session.close();
         })
         .finally(() => {
           // 完成后关闭文件和session
           fileIo.closeSync(file.fd);
           session.close();
         });
     } catch (err) {
       console.error(`testDownloadToStream error code is ${err.code}, error data is ${err.data}`);
       // ...
     }
   }
   ```
