---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-network-turbo
title: 多网并发网络加速
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 多网并发网络加速
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:3d7b5fbf7aa4208a0235f383576b7e2cdaf00f74d2bb0878ab31309e38b46efb
---

## 概述

网络数据传输是应用的核心功能场景之一，而传输的性能直接决定着用户体验——例如高清晰度视频/图片的加载、大文件的上传下载、设备间多文件的同步迁移等场景，有限的网络传输性能导致的卡顿、长时间等待往往会导致用户使用感受变差。针对此类性能敏感的场景，Network Boost Kit的[多网并发](networkboost-netmultipathguide.md)能力提供了网络加速的解决方案。

本文将介绍多网并发的机制原理与基本开发流程，并结合大文件分片传输和多文件并发传输两个实际应用场景介绍多网并发能力的适配方案。

## 实现原理

### 基本概念

多网并发是指通过系统接口同时建立并使用多个网络通路，例如同时使用Wi-Fi和流量，或者主卡和副卡的流量通路。通过多网并发，可以突破默认单网传输的带宽和速率限制，达到网络传输加速的效果。应用发起多网请求后，系统依据业务场景决定并发组合和实施相应的并发管控，并对并发做收益度量。使用多网并发功能的原则是应用申请（受限权限）、系统管控、最小化使用。

### 开发流程

1. 开发前准备。

   多网并发能力在设备类型、网络状态及开发方案的选择上存在一定限制，具体接入要求可参考[多网发起和释放](networkboost-netmultipath-request-release.md)，开发者也可以在调试过程中通过[多网请求错误码](../harmonyos-references/networkboost-nethandover.md#nethandoverrequestmultipath)分析。
2. 发起多网并发。

   (1) 权限配置：应用使用多网并发等网络加速能力，连接迁移能力部分接口需要ohos.permission.LINKTURBO权限，权限配置方法参见[申请权限步骤](networkboost-preparations.md#申请权限步骤)。同时此权限为受限ACL权限需要特别配置和申请，具体操作步骤参考[配置签名](networkboost-preparations.md#配置签名)和[受限ACL权限申请](networkboost-preparations.md#受限acl权限申请)。

   (2) 发起流程：多网并发能力发起的核心步骤包括[netBoost.setSceneDesc()](../harmonyos-references/networkboost-netboost.md#netboostsetscenedesc)设置多网场景、[netHandover.getMultiPathQuotaStats()](../harmonyos-references/networkboost-nethandover.md#nethandovergetmultipathquotastats)查询多网配额、[netHandover.requestMultiPath()](../harmonyos-references/networkboost-nethandover.md#nethandoverrequestmultipath)请求发起多网以及[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#nethandoveronmultipathstatechange)多网状态监听，详细实现可参考[代码实现](networkboost-netmultipath-network-turbo.md#代码实现)中的多网发起与接入。
3. 获取多网NetHandle并绑定Socket。

   (1) 成功发起多网请求后，可以在[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#nethandoveronmultipathstatechange)回调中监听并获取到可用的[NetHandle](../harmonyos-references/js-apis-net-connection.md#nethandle)数据网络句柄对象。

   (2) 针对需要在多网路径上传输的数据，创建对应的TCP Socket（详见[TCPSocket](../harmonyos-references/js-apis-socket.md#tcpsocket)）/UDP Socket（详见[UDPSocket](../harmonyos-references/js-apis-socket.md#udpsocket)），通过[bindSocket()](../harmonyos-references/js-apis-net-connection.md#bindsocket9)方法将Socket对象绑定到NetHandle对应的网络上。
4. Socket发起网络传输任务。

   绑定网络后，TCP Socket/UDP Socket进行[数据传输](socket-connection.md#应用通过tcp-socket-server进行数据传输)时将会使用对应的网络通路，多个Socket使用不同的网络通路同时发起网络传输任务就可以起到多网并发的效果。

## 大文件分片传输

### 场景描述

当发布视频帖子、下载应用资源包时，应用本质上在进行大文件网络传输，通过将大文件分片可以充分发挥多网并发能力，将不同文件片段分配给不同网络通路同时传输，能极大地加快传输速度。

### 关键技术

1. [Network Boost Kit](network-boost-kit-guide.md)：多网能力的发起、监听、状态管理与绑定。
2. [@ohos.net.connection](../harmonyos-references/js-apis-net-connection.md)：网络连接管理，网络通路获取。
3. [Socket数据传输](socket-connection.md)：创建网络连接，执行网络传输任务。
4. [TaskPool](taskpool-introduction.md)：管理多线程网络并发任务。
5. [@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)：负责文件管理，包括文件分片、大小查询等。

### 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ZUNYRtY9ScCYUofaLqbszw/zh-cn_image_0000002706834358.png)

### 代码实现

1. 多网发起与接入。

   根据当前网络传输任务通过[netBoost.setSceneDesc()](../harmonyos-references/networkboost-netboost.md#netboostsetscenedesc)设置多网场景，帮助系统进行多网并发管控和业务时长分析，当前对于文件分片上传任务选择'upload'场景。

   ```ts
   /**
    * Enter or exit 'upload' scene.
    * @param enter true enter,false exit.
    * */
   export function setUploadSceneDesc(enter: boolean): boolean {
     try {
       let sceneDesc: netBoost.SceneDesc = {
         scene: 'upload',
         sceneEvent: enter ? netBoost.SceneEvent.SCENE_EVENT_ENTER : netBoost.SceneEvent.SCENE_EVENT_LEAVE
       };
       netBoost.setSceneDesc(sceneDesc);
       return true;
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, TAG, `[setUploadSceneDesc] Error:${error.code},${error.name}`);
       return false;
     }
   }
   ```

   通过[netHandover.getMultiPathQuotaStats()](../harmonyos-references/networkboost-nethandover.md#nethandovergetmultipathquotastats)获取当前多网配额，包括次数和时长等，应用可按需添加业务逻辑如提示用户剩余配额等。

   ```ts
   /**
    * Obtain multi-network quota information.
    * @returns multi-network quota.
    * */
   export function getMultiPathQuota(): netHandover.MultiPathQuota | undefined {
     try {
       let quota: netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
       return quota;
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, TAG, `[getMultiPathQuota] Error:${error.code},${error.name}`);
       return;
     }
   }
   ```

   通过[netHandover.requestMultiPath()](../harmonyos-references/networkboost-nethandover.md#nethandoverrequestmultipath)请求开启多网，支持Wi-Fi和蜂窝并发以及主卡和副卡并发，不支持开发者指定并发组合，并发组合由系统决定。

   ```ts
   /**
    * Request a multi-network path.
    * @returns Returns true on success, otherwise false.
    * */
   export function requestMultiPath(): Promise<boolean> {
     return new Promise((resolve) => {
       try {
         netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
           if (data && data.result === netHandover.MultiPathErrorResult.MULTIPATH_ERROR_NONE) {
             resolve(true);
           } else {
             resolve(false);
           }
         });
       } catch (err) {
         resolve(false);
         const error: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, TAG, `[requestMultiPath] Error:${error.code},${error.name}`);
       }
     })
   }
   ```

   多网请求成功后还需要使用[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#nethandoveronmultipathstatechange)监听多网状态，确认多网络通路的使能与可用情况，记录可用的NetHandle信息。

   ```ts
   /**
    * Enable multi-network listening.
    * @param netHandleChange The callback when the netHandle changes.
    */
   export function setOnMultiPathStateChange(netHandleChange: NetHandleChange) {
     try {
       netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
         if (data.multiPathState === netHandover.MultiPathState.MULTIPATH_CREATED &&
           data.netHandle.netId >= CommonConst.MIN_USEFUL_NET_ID) {
           netHandleChange?.onMultiNetSuccess(data.netHandle);
         } else if (data.multiPathState === netHandover.MultiPathState.MULTIPATH_CREATING) {
           hilog.info(DOMAIN, TAG, `[setOnMultiPathStateChange.multiPathStateChange] ${data.netHandle.netId} Creating`);
         } else {
           netHandleChange?.onMultiNetRelease(data.netHandle);
         }
       });
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, TAG, `[setOnMultiPathStateChange] Error:${error.code},${error.name}`);
     }
   }
   ```
2. 多网通路绑定Socket。

   封装网络查询函数，通过[connection.getAllNetsSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetallnetssync10)获取当前所有网络信息。由于网络传输任务一般放在子线程实现，而当前无法跨线程传递Socket对象和NetHandle对象，为了在子线程实现网络与Socket绑定需要获取所有网络信息，再通过之前请求多网后记录的NetHandle对象的ID找到指定网络在执行绑定操作；如果应用业务不涉及多线程问题可直接绑定上一步多网状态监听中获取到的NetHandle。

   ```ts
   /**
    * Get all netHandles.
    * @returns Returns all netHandles on success,otherwise returns undefined
    * */
   export function getAllNetHandles(): connection.NetHandle[] | undefined {
     try {
       let netHandles = connection.getAllNetsSync();
       const constNetHandles: connection.NetHandle[] = [];
       for (let i = 0; i < netHandles.length; i++) {
         hilog.info(DOMAIN, TAG, `[getAllNetHandles] success [${i}]>>>${netHandles[i].netId}`);
         if (netHandles[i].netId >= CommonConst.MIN_USEFUL_NET_ID) {
           constNetHandles.push(netHandles[i]);
         }
       }
       return constNetHandles;
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, TAG, `[getAllNetHandles] Error:${error.code},${error.name}`);
       return undefined;
     }
   }
   ```

   遍历获取到的所有网络，将多网状态监听中记录的可用网络通过bindSocket()绑定到Socket上，后续的TCP Socket进行网络传输任务时将会使用绑定的网络。

   ```ts
   /**
    * Binds the socket to the specified network path.
    * @param socketInstance  socket client.
    * @param netId netHandle Id.
    * @param port binds port.
    * */
   export async function bindSpecifiedNet(socketInstance: socket.TCPSocket, netId: number, port: number) {
     const netHandles = getAllNetHandles();
     if (netHandles) {
       for (let i = 0; i < netHandles.length; i++) {
         if (netHandles[i].netId === netId) {
           try {
             const connectionProperties = connection.getConnectionPropertiesSync(netHandles[i]);
             if (connectionProperties && connectionProperties.linkAddresses &&
               connectionProperties.linkAddresses.length > 0) {
               let netAddress: socket.NetAddress = {
                 address: connectionProperties.linkAddresses[0].address.address,
                 port: port
               };
               await socketInstance.bind(netAddress);
               await netHandles[i].bindSocket(socketInstance);
             } else {
               hilog.error(DOMAIN, TAG, `[socketBindNet] Get ConnectionProperties error`);
             }
           } catch (err) {
             const error: BusinessError = err as BusinessError;
             hilog.error(DOMAIN, TAG, `[socketBindNet] Error occurred:${error.code},${error.name}`);
           }
           break;
         }
       }
     } else {
       hilog.error(DOMAIN, TAG, `Net Empty`);
     }
   }
   ```
3. 文件分片处理。

   封装文件处理类，设置分片文件数据结构，包括当前文件片段数量、开始位置、分片大小、片段重试次数等信息。

   ```ts
   /**
    * File upload chunk info.
    * */
   export class FileUpChunk {
     chunkNumber: number = 1;
     startPosition: number = 0;
     chunkSize: number = 0;
     buffer: ArrayBuffer = new ArrayBuffer(0);
     retryTimes: number = 0;
   }
   ```

   提供方法根据文件大小计算分片规格，开发者可根据业务需要自行实现分片策略。

   ```ts
   function getChunkSize(fileSize: number): number {
     const MB = CommonConst.MIN_SLICE_FILE_SIZE;
     const fullMBs = Math.floor(fileSize / MB);
     let res = Math.max(1, Math.min(CommonConst.MAX_SLICE_FILE_COUNT, fullMBs));
     hilog.info(DOMAIN, TAG, `[getChunkSize] FileSize:${fileSize},ChunkSize:${res}`);
     return res;
   }
   ```

   通过[fileIo.statSync()](../harmonyos-references/js-apis-file-fs.md#fileiostatsync)获取待上传文件的大小等信息，按照计算出的分片规格对文件进行分片处理。

   ```ts
   /**
    * Splits the file into segments.
    * @param file An opened file
    * @returns Returns all segments of the file.
    */
   export function splitFile(file: fileIo.File): FileUpChunk[] {
     try {
       const fileStat = fileIo.statSync(file.fd);
       const fileSize = fileStat.size;
       const chunks: FileUpChunk[] = [];
       let chunkNumber = 1;
       const splitChunkSize = Math.floor(fileStat.size / getChunkSize(fileSize));
       for (let start = 0; start < fileSize; start += splitChunkSize) {
         const chunkSize = Math.min(splitChunkSize, fileSize - start);
         const chunk = new FileUpChunk();
         chunk.chunkNumber = chunkNumber++;
         chunk.startPosition = start;
         chunk.chunkSize = chunkSize;
         chunks.push(chunk);
       }
       hilog.info(DOMAIN, TAG, `[splitFile] success`);
       return chunks;
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       hilog.error(DOMAIN, TAG, `[splitFile] errror:${err.code},${err.name}`);
       return [];
     }
   }
   ```
4. 多Socket并发上传不同文件片段。

   封装分片文件上传类，提供初始化分片上传接口，通知服务端待上传文件片段对应的存储路径。此处代码片段仅供参考，开发者可以根据自己业务的实际实现方式调整通信格式、请求参数等。

   ```ts
   /**
    * Initializes the upload.
    * @param host Server host.
    * @param port Server port.
    * @param uploadFileName File save path.
    * @returns Returns a 'InitiateMultipartUpload' object if success,otherwise returns undefined.
    */
   @Concurrent
   async function initMultiPartUpload(host: string, port: number,
     uploadFileName: string): Promise<InitiateMultipartUpload | undefined> {
     const objectKey: string = uploadFileName;
     const path = `/${objectKey}?uploads`;
     const method = http.RequestMethod.POST;
     const date = new Date().toUTCString();

     // build request headers
     const headers = [
       `Host: ${host}`,
       `Date: ${date}`,
       `Content-Length: 0`,
       `Content-Type: application/xml`,
       `Connection: close`
     ];

     // build request info
     const request = `${method} ${path} HTTP/1.1\r\n` + headers.join('\r\n') + CommonConst.HEADER_BODY_DELIMITER;
     // request data by socket
     const value: socket.SocketMessageInfo | undefined = await getDataBySocket(host, port, request);
     // parse result
     if (value) {
       try {
         let responseStr = buffer.from(value.message).toString('utf-8');
         const uploadIdMatch = responseStr.match(/<UploadId>(.*?)<\/UploadId>/);
         if (uploadIdMatch && uploadIdMatch[1]) {
           // start build 'InitiateMultipartUpload' object
           let result = XmlUtils.xmlToObj(extractHttpBody(responseStr), true);
           if (result && result['initiateMultipartUploadResult']) {
             const json: object = result['initiateMultipartUploadResult'];
             if (json) {
               return {
                 bucket: json['bucket'],
                 key: json['key'],
                 uploadId: json['uploadId']
               } as InitiateMultipartUpload;
             }
             return undefined;
           } else {
             hilog.error(0x0000, 'FilePartsUploadManager',
               `[initiateMultipartUploadResult.onResult]: parse xml info error`);
             return undefined;
           }
         } else {
           hilog.error(0x0000, 'FilePartsUploadManager', `[initMultiPartUpload] onMessage ignore`);
           return undefined;
         }
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         hilog.error(0x0000, 'FilePartsUploadManager', `[uploadPart] buffer.from error:${err.code},${err.name}`);
         return undefined;
       }
     } else {
       return undefined;
     }
   }
   ```

   封装网络上传接口，包括创建TCP Socket实例并绑定到指定网络NetHandle、设置网络请求头等配置、通过[TCPSocket.send()](../harmonyos-references/js-apis-socket.md#send-2)方法发送请求至服务端并通过[TCPSocket.on('message')](../harmonyos-references/js-apis-socket.md#onmessage-1)监听响应。

   ```ts
   /**
    * Upload file segment.
    * @param host Server host.
    * @param port Server port.
    * @param initResult An 'InitiateMultipartUpload' object.
    * @param fileChunk File info to uploaded.
    * @param netId The ID of the netHandle to bind.
    * @returns Returns a 'UploadPartResult' object if success,otherwise returns undefined
    */
   @Concurrent
   async function uploadSegment(host: string, port: number, initResult: InitiateMultipartUpload, fileChunk: FileUpChunk,
     netId: number): Promise<UploadPartResult | undefined> {
     const socketInstance: socket.TCPSocket = socket.constructTCPSocketInstance();
     await bindSpecifiedNet(socketInstance, netId, CommonConst.SOCKET_BIND_UP_PORT);

     const path = `/${initResult.key}?partNumber=${fileChunk.chunkNumber}&uploadId=${initResult.uploadId}`;
     const method = http.RequestMethod.PUT;
     const date = new Date().toUTCString();
     // build request header
     const headers = [
       `Host: ${host}`,
       `Date: ${date}`,
       `Content-Length: ${fileChunk.chunkSize}`,
       `Content-Type: application/octet-stream`,
       `Connection: close`
     ];

     const requestHeader = `${method} ${path} HTTP/1.1\r\n` + headers.join('\r\n') + CommonConst.HEADER_BODY_DELIMITER;
     const headerBuffer = buffer.from(requestHeader, 'utf-8').buffer;

     // build request header and body
     const requestBuffer = new Uint8Array(headerBuffer.byteLength + fileChunk.buffer.byteLength);
     requestBuffer.set(new Uint8Array(headerBuffer), 0);
     requestBuffer.set(new Uint8Array(fileChunk.buffer), headerBuffer.byteLength);
     // get value from socket
     const value: socket.SocketMessageInfo | undefined =
       await getDataBySocket(host, port, requestBuffer.buffer, socketInstance);

     // parse value
     if (value) {
       try {
         let responseStr = buffer.from(value.message).toString('utf-8');
         // Get ETag
         const eTagMatch = responseStr.match(/ETag: "([^"]+)"/);
         if (eTagMatch && eTagMatch[1]) {
           return ({
             partNumber: fileChunk.chunkNumber,
             eTag: eTagMatch[1]
           } as UploadPartResult);
         } else {
           hilog.error(0x0000, 'FilePartsUploadManager',
             `[uploadPart] onMessage--> fileChunkId:${fileChunk.chunkNumber} upload Faild`);
           return undefined;
         }
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         hilog.error(0x0000, 'FilePartsUploadManager',
           `[uploadPart] buffer.from error:${err.code},${err.name},fileChunkId:${fileChunk.chunkNumber}`);
         return undefined;
       }
     } else {
       return undefined;
     }
   }
   ```

   通过网络上传接口封装文件片段传输方法，包括读取当前文件片段、为当前NetHandle创建子线程发起上传任务、根据文件分片信息更新上传进度、以及失败重试等逻辑。在当前片段传输完毕后循环调用此方法上传剩余片段，直至无片段剩余。

   ```ts
   /**
    * Upload file segment using assigned net.
    */
   private async uploadFileChunkWithNet(netHandle: connection.NetHandle) {
     if (this.abortUpload) {
       return;
     }
     if (this.fileChunks.length === 0) {
       hilog.info(DOMAIN, TAG, `[MultiNetworkUploader.uploadFileChunkWithNet] fileChunks empty`);
       this.checkUploadSuccess();
       return;
     }

     const fileChunk = this.fileChunks.shift()!;
     let fileChunkWithData = readFileChunkBuffer(this.file!, fileChunk);
     // start upload a file chunk
     if (fileChunkWithData) {
       const task =
         new taskpool.Task(uploadSegment, CommonConst.UP_HOST, CommonConst.HTTP_DEFAULT_PORT, this.initMultipartUpload!,
           fileChunkWithData, netHandle.netId);
       try {
         const uploadPartRes = await taskpool.execute(task);
         // upload success
         if (uploadPartRes) {
           this.uploadResult.push(uploadPartRes as UploadPartResult);
           this.uploadFileChunkWithNet(netHandle);
           this.onProgressUpdate(this.uploadResult.length / this.fileChunksSize);
         } else {
           this.retryUpload(fileChunk, netHandle);
           hilog.error(DOMAIN, TAG, `[uploadFileChunkWithNet] upload failed`);
         }
       } catch (error) {
         this.retryUpload(fileChunk, netHandle);
         const err: BusinessError = error as BusinessError;
         hilog.error(DOMAIN, TAG, `[uploadFileChunkWithNet] taskpool error occurred:${err.code},${err.name}`);
       }
     } else {
       this.retryUpload(fileChunk, netHandle);
       hilog.error(DOMAIN, TAG, `[uploadFileChunkWithNet] readFileChunkBuffer failed`);
     }
   }
   ```

   遍历NetHandle调用上传文件片段方法，为每个网络通路分配网络传输任务，实现多网络通路并发传输文件片段的效果。

   ```ts
   /**
    * Start upload file.
    */
   public startUpload() {
     if (!this.netHandles || this.netHandles.length === 0) {
       hilog.error(DOMAIN, TAG, `[MultiNetworkUploader.startUpload] netHandles is empty`);
       return;
     }

     if (!this.fileChunks || this.fileChunks.length === 0) {
       hilog.error(DOMAIN, TAG, `[MultiNetworkUploader.startUpload] fileChunks is empty`);
       return;
     }

     for (let i = 0; i < this.netHandles.length; i++) {
       this.uploadFileChunkWithNet(this.netHandles[i]);
     }
   }
   ```
5. 通知服务端整合分片文件。

   全部文件片段上传完毕后，通知服务端文件片段顺序，进行文件整合。

   ```ts
   /**
    *  Merge all file segments.
    * */
   private async mergeSegmentsOnServer() {
     fileIo.close(this.file?.fd).catch((error: BusinessError) => {
       hilog.error(DOMAIN, TAG, `[mergeSegmentsOnServer] Close file error:${error.code},${error.name}`);
     });
     this.uploadResult.sort((a, b) => a.partNumber - b.partNumber);
     const task = new taskpool.Task(completeMultiPartUploadRequest, CommonConst.UP_HOST, CommonConst.HTTP_DEFAULT_PORT,
       this.initMultipartUpload!,
       this.uploadResult);
     try {
       const res = await taskpool.execute(task);
       if (res) {
         this.onUploadSuccess();
       } else {
         this.onFailed();
       }
     } catch (error) {
       this.onFailed();
     }
   }
   ```
6. 释放资源。

   通过[netHandover.releaseMultiPath()](../harmonyos-references/networkboost-nethandover.md#nethandoverreleasemultipath)释放多网，注销相关的监听方法。

   ```ts
   /**
    * Stop multi net path.
    * */
   export function releaseMultiPath() {
     try {
       netHandover.releaseMultiPath();
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, TAG, `[releaseMultiPath] Error:${error.code},${error.name}`);
     }
   }

   // ...
   /**
    * Stop listening on multiple network paths.
    * */
   export function setOffMultiPathStateChange() {
     try {
       netHandover.off('multiPathStateChange');
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, TAG, `[setOffMultiPathStateChange] Error:${error.code},${error.name}`);
     }
   }
   ```

## 多文件并发传输

### 场景描述

当进行数据、文件同步，下载器下载资源时，往往会需要处理多个文件的传输任务，使用多网并发拓宽网络带宽，不同文件传输任务分配给不同网络通路并发传输，达到提升传输效率的效果。

多文件并发传输与大文件分片传输对多网能力的使用原理相同，整体流程都是通过拉起多网后获取到多个netHandle，同时创建多个TCP Socket和不同netHandle绑定，再通过多个TCP Socket建立连接并行发起传输任务，区别只在于分片传输每个连接传输的是文件片段，而本场景传输的是不同文件。此处以并发传输两个文件作为示例场景。

### 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Aa171RFkR3OolCVkDdVUUg/zh-cn_image_0000002736313463.png)

### 代码实现

多网接入和绑定部分与分片传输场景一致，此处不再赘述，仅提供关键差异部分代码:

封装文件下载类，提供下载文件方法，根据下载对象链接与网络netId新建线程，发起文件下载任务。

```ts
/**
 * Start download file.
 * */
public async startDownload() {
  if (this.downUrls) {
    this.isFileDownloading = true;
    const netId = this.netHandle ? this.netHandle.netId : -1;
    const task = new taskpool.Task(getFileSizeWithNet, this.downUrls, CommonConst.HTTP_DEFAULT_PORT, netId);
    try {
      const fileSize = await taskpool.execute(task) as number;
      if (fileSize > 0) {
        // notify download start
        this.onDownStart(fileSize);
        this.fileChunk.endPosition = fileSize;
        // start download the file using taskpool
        const downTask =
          new taskpool.Task(downloadFileChunkWithNet, this.downUrls, CommonConst.HTTP_DEFAULT_PORT, this.fileChunk,
            netId, this.downListener);
        const downRes = await taskpool.execute(downTask);
        if (downRes) {
          // notify download success
          this.onDownSuccess();
        } else {
          // download failed,retry again
          this.retryDownload();
        }
      } else {
        // download failed,retry again
        this.retryDownload();
        hilog.error(DOMAIN, TAG, `[startDownload] upload failed`);
      }
    } catch (error) {
      // download failed,retry again
      this.retryDownload();
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, `[startDownload] taskpool error occurred:${err.code},${err.name}`);
    }
  } else {
    hilog.warn(DOMAIN, TAG, `[startDownload] Url is null`);
    // download failed,retry again
    this.onDownFailed();
  }
}
```

使用默认网络下载第一个文件，刷新对应的下载进度。

```ts
/**
 * Downloads the first file using the specified netHandle.
 * @param netHandle The specified netHandle to access the server.
 * */
private startDownFirstFile(netHandle: connection.NetHandle) {
  this.firstFileDownloader = new FileDownloadManager(this.firstDownFileInfo!, netHandle);
  this.firstFileDownloader.onProgress = (downloaded: number, fileSize: number, progress: number) => {
    this.downFirstProgress = progress;
    this.downFirstProgressText = `${formatFileSize(downloaded)} / ${formatFileSize(fileSize)}`;
  }
  // download success
  this.firstFileDownloader.onSuccess = () => {
    this.firstFileDownloading = false;
    this.downBtnEnable = (!this.firstFileDownloading) && (!this.secondFileDownloading) && this.taskArray.length === 0;
    this.downFirstProgressColor = $r('sys.color.confirm');
    let res = this.taskArray.shift();
    this.downFirstFileResult = '';
    if (res) {
      this.startDownSecondFile(netHandle);
    } else {
      hilog.info(DOMAIN, TAG, `[startDownFirstFile]  File1 downloaded,no need to download File2`);
    }
  }
  // download failed
  this.firstFileDownloader.onError = () => {
    this.firstFileDownloading = false;
    this.downBtnEnable = (!this.firstFileDownloading) && (!this.secondFileDownloading);
    if (this.downFirstProgress === 0) {
      this.downFirstProgress = 0.01;
    }
    this.downFirstProgressColor = $r('sys.color.multi_color_08');
    this.taskArray.shift();
    this.downFirstFileResult = $r('app.string.down_failed');
  }
  // init downloading status
  this.firstFileDownloading = true;
  this.downFirstProgress = 0;
  this.downFirstProgressColor = $r('sys.color.comp_background_emphasize');
  this.downFirstFileResult = '';
  // start download
  this.firstFileDownloader.startDownload();
}
```

如果多网请求成功，在监听多网状态变更的回调中获取新的可用网络NetHandle，使用新网络NetHandle发起第二个文件的下载任务，达到并发下载的效果。

```ts
private netHandleChange: NetHandleChange = {
  onMultiNetSuccess: async (netHandle: connection.NetHandle): Promise<void> => {
    this.multiNetHandle = netHandle;
    let res = this.taskArray.shift();
    if (res) {
      this.startDownSecondFile(netHandle);
    } else {
      hilog.info(DOMAIN, TAG, `[netHandleChange] Multi-net enable,but no need to download file2`);
    }
  },

  onMultiNetRelease: async (netHandle: connection.NetHandle): Promise<void> => {
    this.multiNetHandle = undefined;
  }
}
```

## 示例代码

[基于多网并发能力实现网络加速](https://gitcode.com/harmonyos_samples/NetBoost)
