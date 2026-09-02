---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-pauseresume
title: 实现请求暂停、恢复与断点续传
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 文件上传下载 > 实现请求暂停、恢复与断点续传
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:863cdc081f9a2d9f8136437c002c1f3335182636ff38a8a71f690a7d8e52e001
---

## 约束与限制

请求暂停、恢复与断点续传能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 请求暂停、恢复

### 场景介绍

Remote Communication Kit提供完善的功能支持，包括请求的暂停和恢复功能。这不仅涵盖接收暂停，还包括发送暂停。

### 使用实例

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   import { util } from '@kit.ArkTS';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义调试信息接口、调试信息源类型以及调试信息序列化函数，用于将调试信息序列化为StringifiedDebugInfo数组。函数首先根据infoSource的类型获取调试信息，然后使用TextDecoder将调试信息的data字段解码为字符串，并返回一个包含解码后的调试信息的数组。

   ```typescript
   // 定义请求的URL（请根据实际需求调整）
   const HTTP_SERVER_POST: string = 'https://example.com/anything';
   // 定义调试信息接口
   interface StringFeildDebugInfo {
     type: rcp.DebugEvent;
     data: string;
   };
   // 定义调试信息源类型
   type DebugInfoSource = undefined | rcp.DebugInfo[] | rcp.Response;

   // 定义调试信息序列化函数
   function debugInfoStringify(infoSource: DebugInfoSource): StringFeildDebugInfo[] {
     const debugInfo = Array.isArray(infoSource)
       ? (infoSource as rcp.DebugInfo[])
       : (infoSource as rcp.Response).debugInfo;

     if (!debugInfo) {
       return [];
     }

     const decoder = util.TextDecoder.create('utf-8');
     return debugInfo.map((i: rcp.DebugInfo): StringFeildDebugInfo => {
       return {
         type: i.type,
         data: decoder.decodeToString(new Uint8Array(i.data)).trim(),
       };
     });
   }
   ```
3. 获取发送暂停和恢复事件，用于从调试信息中筛选出发送暂停和恢复事件。

   ```typescript
   function getSendPausedEvents(debugInfo: DebugInfoSource) {
     return debugInfoStringify(debugInfo).filter((i) => i.data.startsWith('[[RCP]]: Pause sending'));
   }

   function getSendResumedEvents(debugInfo: DebugInfoSource) {
     return debugInfoStringify(debugInfo).filter((i) => i.data.startsWith('[[RCP]]: Resume sending'));
   }
   ```
4. 编写发起请求的函数。

   ```typescript
   const sendingPauseByTimeout = async (done: Function): Promise<void> => {
     try {
       const session = rcp.createSession();
       const request = new rcp.Request(HTTP_SERVER_POST);
       // 定义发送暂停策略，kind为'timeout'，timeoutMs为1ms
       const sendPolicy: rcp.SendingPausePolicy = {
         kind: 'timeout',
         timeoutMs: 1,
       };
       // 定义暂停策略，sending字段引用了上述定义的发送暂停策略
       const pausePolicy: rcp.PausePolicy = {
         sending: sendPolicy,
       };
       // 设置请求的配置，包括传输策略和跟踪信息
       request.configuration = {
         transfer: {
           pausePolicy: pausePolicy,
         },
         tracing: {
           infoToCollect: {
             textual: true,
           },
         },
       };
       // 定义请求体数据
       const data = 'TestData';
       // 设置请求头，'Content-Length字段表示请求体的长度
       request.headers = {
         'Content-Length': data.length.toString(),
       };
       // 定义布尔型标志变量用于控制请求体生成
       let isReadCompleted = false;
       // 设置请求方法为POST
       request.method = 'POST';
       // 定义请求体内容生成函数，如果read为true，则返回空的ArrayBuffer，否则生成包含请求体数据的ArrayBuffer
       request.content = (maxSize) => {
         if (isReadCompleted) {
           return new ArrayBuffer(0);
         }
         isReadCompleted = true;
         const buffer = new ArrayBuffer(data.length);
         util.TextEncoder.create('utf-8').encodeIntoUint8Array(data, new Uint8Array(buffer));
         return buffer;
       };

       // 发送请求并等待响应
       const response = await session.fetch(request)

       // 从响应的调试信息中获取发送暂停和恢复事件
       const pausedEvents = getSendPausedEvents(response);
       const resumedEvents = getSendResumedEvents(response);
       // ...

       // 关闭会话
       session.close();
       // 调用完成回调函数
       done();
     } catch (err) {
       console.error(`error code is ${err.code}, error data is ${err.data}`);
     }
   }
   ```

## 实现断点续传

### 场景介绍

在需要接续数据请求的场景中，用户可以通过定义[TransferRange](../harmonyos-references/remote-communication-rcp.md#transferrange)对象的from和to属性来控制数据的截取范围。下载的内容可以被准确地截取并拼接到目标文件中，确保数据的完整性和一致性，开发者可以灵活地管理和恢复下载过程。

### 使用示例

1. 导入模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   import { util } from '@kit.ArkTS';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建session，定义请求URL，并对request进行配置，同时定义变量以记录下载文件的总大小。

   ```typescript
   // 创建会话
   let session: rcp.Session | null = rcp.createSession();
   // 定义服务器地址
   const kHttpServerAddress = 'http://www.example.com/fetch';
   // 创建请求
   const request = new rcp.Request(kHttpServerAddress, 'GET');
   // 定义变量记录下载文件的大小
   let totalSize = 0;
   // 定义一个存储上次传输位置的变量
   let lastTransferPosition = 0;
   ```
3. 编写一个函数以获取要下载的文件大小。有多种方法可以获取下载文件的大小，请根据实际需求选择合适的方法。在本例中，通过从响应数据的header中的content-range字段来获取下载文件的总大小。

   ```typescript
   /**
    * 获取要下载文件的大小
    *
    * @returns 文件的大小
    */
   async getTotalSize(): Promise<number> {
     if (this.request == null || this.session == null) {
       return this.totalSize;
     }
     this.request.transferRange = { from: 0, to: 1 };
     try {
       let rep = await this.session?.fetch(this.request);
       if (rep) {
         // 从响应数据的header的content-range字段中提取出文件的大小
         let contentRange = rep.headers['content-range'];
         let sizeStr = contentRange ? contentRange.substring(contentRange.indexOf('\/') + 1, contentRange.length) : '0';
         this.totalSize = Number(sizeStr);
       }
     } catch (err) {
       console.error(`getTotalSize error code is ${err.code}, error data is ${err.data}`);
     }
     console.info(`getTotalSize totalSize: ${this.totalSize.toString()}`);
     return this.totalSize;
   }
   ```
4. 编写一个依据传输范围下载文件的函数。

   ```typescript
   /**
    * 根据传输范围下载文件
    *
    * @param from - 传输范围的起始位置
    * @param to - 传输范围的结束位置
    */
   downloadTransfer(from: number, to: number) {
     if (this.request == null || this.session == null) {
       return;
     }
     // ...
     // 设置请求的数据传输范围
     this.request.transferRange = { from: from, to: to };
     this.session?.fetch(this.request).then((rep) => {
       if (rep.body) {
         // 处理响应，可以在此处将文件保存到本地
         console.info(`Response succeeded: ${JSON.stringify(rep.headers)}`);
         // 下次传输的起始位置 = 上次的位置 + 本次传输数据的长度
         this.lastTransferPosition += rep.body.byteLength;
         if (this.lastTransferPosition < this.totalSize) {
           // 计算下一次传输范围的结束位置
           const nextTo = Math.min(this.lastTransferPosition + 100, this.totalSize);
           // 递归调用继续下载下一段数据
           this.downloadTransfer(this.lastTransferPosition, nextTo);
         } else {
           console.info('Response succeeded, completed.');
         }
         // ...
       }
     }).catch((err: BusinessError) => {
       console.error(`Continue transfer error: code is ${err.code}, message is ${err.message}`);
     });
   }
   ```
5. 使用以下方式开始下载。

   ```typescript
   if (!session) {
     session = rcp.createSession();
   }
   // 传输位置归零
   lastTransferPosition = 0;
   // 获取要下载文件的总大小
   await this.getTotalSize();
   // 计算传输范围的结束位置
   const nextTo = Math.min(lastTransferPosition + 100, totalSize);
   // 开始下载
   this.downloadTransfer(lastTransferPosition, nextTo);
   ```
6. 使用以下方式暂停下载。

   ```typescript
   /**
    * 暂停下载
    */
   async pauseDownload() {
     // ...
     // 取消下载请求
     this.session?.cancel(this.request);
   }
   ```
7. 使用以下方式继续下载。

   ```typescript
   /**
    * 继续下载
    */
   async resumeDownload() {
     // 计算传输范围的结束位置
     const nextTo = Math.min(this.lastTransferPosition + 100, this.totalSize);
     // 开始下载
     this.downloadTransfer(this.lastTransferPosition, nextTo);
   }
   ```
8. 使用以下方式停止下载。

   ```typescript
   // 取消下载请求
   this.session?.cancel(this.request);
   // 关闭session
   this.session?.close();
   this.session = null;
   ```
