---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-path-network-turbo
title: 多网并发网络加速
breadcrumb: 最佳实践 > 网络 > 多网并发网络加速
category: best-practices
scraped_at: 2026-04-28T08:20:23+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:2f9620b45f47d8b6af6215cb583514c9813e57fd9990694ee50c878188538cef
---

## 概述

网络数据传输是应用的核心功能场景之一，而传输的性能直接决定着用户体验——例如高清晰度视频/图片的加载、大文件的上传下载、设备间多文件的同步迁移等场景，有限的网络传输性能导致的卡顿、长时间等待往往会导致用户使用感受变差。针对此类性能敏感的场景，Network Boost Kit的[多网并发](../harmonyos-guides/networkboost-netmultipathguide.md)能力提供了网络加速的解决方案。

本文将介绍多网并发的机制原理与基本开发流程，并结合大文件分片传输和多文件并发传输两个实际应用场景介绍多网并发能力的适配方案。

## 实现原理

### 基本概念

多网并发是指通过系统接口同时建立并使用多个网络通路，例如同时使用Wi-Fi和流量，或者主卡和副卡的流量通路。通过多网并发，可以突破默认单网传输的带宽和速率限制，达到网络传输加速的效果。应用发起多网请求后，系统依据业务场景决定并发组合和实施相应的并发管控，并对并发做收益度量。使用多网并发功能的原则是应用申请（受限权限）、系统管控、最小化使用。

### 开发流程

1. 开发前准备

   多网并发能力在设备类型、网络状态及开发方案的选择上存在一定限制，具体接入要求可参考[多网发起和释放](../harmonyos-guides/networkboost-netmultipath-request-release.md)，开发者也可以在调试过程中通过[多网请求错误码](../harmonyos-references/networkboost-nethandover.md#section8508131819279)分析。
2. 发起多网并发

   (1) 权限配置：应用使用多网并发等网络加速能力，连接迁移能力部分接口需要ohos.permission.LINKTURBO权限，权限配置方法参见[申请权限步骤](../harmonyos-guides/networkboost-preparations.md#section1648815561221)。同时此权限为受限ACL权限需要特别配置和申请，具体操作步骤参考[配置签名](../harmonyos-guides/networkboost-preparations.md#section94731428358)和[受限ACL权限申请](../harmonyos-guides/networkboost-preparations.md#section13192154213515)。

   (2) 发起流程：多网并发能力发起的核心步骤包括[netBoost.setSceneDesc()](../harmonyos-references/networkboost-netboost.md#section13106021163)设置多网场景、[netHandover.getMultiPathQuotaStats()](../harmonyos-references/networkboost-nethandover.md#section47829529513)查询多网配额、[netHandover.requestMultiPath()](../harmonyos-references/networkboost-nethandover.md#section8508131819279)请求发起多网以及[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#section7919111205211)多网状态监听，详细实现可参考[多网发起与接入](bpta-multi-path-network-turbo.md#li4874151714524)。
3. 获取多网NetHandle并绑定Socket

   (1) 成功发起多网请求后，可以在[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#section7919111205211)回调中监听并获取到可用的[NetHandle](../harmonyos-references/js-apis-net-connection.md#nethandle)数据网络句柄对象。

   (2) 针对需要在多网路径上传输的数据，创建对应的[TCP Socket](../harmonyos-references/js-apis-socket.md#tcpsocket)/[UDP Socket](../harmonyos-references/js-apis-socket.md#udpsocket)，通过[bindSocket()](../harmonyos-references/js-apis-net-connection.md#bindsocket9)方法将Socket对象绑定到NetHandle对应的网络上。
4. Socket发起网络传输任务

   绑定网络后，TCP/UDP Socket进行[数据传输](../harmonyos-guides/socket-connection.md#应用通过tcp-socket-server进行数据传输)时将会使用对应的网络通路，多个Socket使用不同的网络通路同时发起网络传输任务就可以起到多网并发的效果。

## 大文件分片传输

### 场景描述

当发布视频帖子、下载应用资源包时，应用本质上在进行大文件网络传输，通过将大文件分片可以充分发挥多网并发能力，将不同文件片段分配给不同网络通路同时传输，能极大地加快传输速度。

### 关键技术

1. [Network Boost Kit](../harmonyos-guides/network-boost-kit-guide.md)：多网能力的发起、监听、状态管理与绑定。
2. [@ohos.net.connection](../harmonyos-references/js-apis-net-connection.md)：网络连接管理，网络通路获取。
3. [Socket数据传输](../harmonyos-guides/socket-connection.md)：创建网络连接，执行网络传输任务。
4. [TaskPool](../harmonyos-guides/taskpool-introduction.md)：管理多线程网络并发任务。
5. [@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)：负责文件管理，包括文件分片、大小查询等。

### 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/lJMnFdzbSAGg63o9GoX4lw/zh-cn_image_0000002456588494.png?HW-CC-KV=V1&HW-CC-Date=20260428T002022Z&HW-CC-Expire=86400&HW-CC-Sign=2F4705A657C740B34204FC72CD14FB9D05EC483824DECCD1C220339D8876015D "点击放大")

### 代码实现

1. 多网发起与接入

   根据当前网络传输任务通过[netBoost.setSceneDesc()](../harmonyos-references/networkboost-netboost.md#section13106021163)设置多网场景，帮助系统进行多网并发管控和业务时长分析，当前对于文件分片上传任务选择'upload'场景。

   ```
   1. /**
   2. * Enter or exit 'upload' scene.
   3. * @param enter true enter,false exit.
   4. * */
   5. export function setUploadSceneDesc(enter: boolean): boolean {
   6. try {
   7. let sceneDesc: netBoost.SceneDesc = {
   8. scene: 'upload',
   9. sceneEvent: enter ? netBoost.SceneEvent.SCENE_EVENT_ENTER : netBoost.SceneEvent.SCENE_EVENT_LEAVE
   10. };
   11. netBoost.setSceneDesc(sceneDesc);
   12. return true;
   13. } catch (err) {
   14. const error: BusinessError = err as BusinessError;
   15. hilog.error(DOMAIN, TAG, `[setUploadSceneDesc] Error:${error.code},${error.name}`);
   16. return false;
   17. }
   18. }
   ```

   [NetBoostManager.ets](https://gitcode.com/HarmonyOS_Samples/NetBoost/blob/master/entry/src/main/ets/net/NetBoostManager.ets#L44-L61)

   通过[netHandover.getMultiPathQuotaStats()](../harmonyos-references/networkboost-nethandover.md#section47829529513)获取当前多网配额，包括次数和时长等，应用可按需添加业务逻辑如提示用户剩余配额等。

   ```
   1. /**
   2. * Obtain multi-network quota information.
   3. * @returns multi-network quota.
   4. * */
   5. export function getMultiPathQuota(): netHandover.MultiPathQuota | undefined {
   6. try {
   7. let quota: netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
   8. return quota;
   9. } catch (err) {
   10. const error: BusinessError = err as BusinessError;
   11. hilog.error(DOMAIN, TAG, `[getMultiPathQuota] Error:${error.code},${error.name}`);
   12. return;
   13. }
   14. }
   ```

   [NetBoostManager.ets](https://gitcode.com/HarmonyOS_Samples/NetBoost/blob/master/entry/src/main/ets/net/NetBoostManager.ets#L176-L189)

   通过[netHandover.requestMultiPath()](../harmonyos-references/networkboost-nethandover.md#section8508131819279)请求开启多网，支持Wi-Fi和蜂窝并发以及主卡和副卡并发，不支持开发者指定并发组合，并发组合由系统决定。

   ```
   1. /**
   2. * Request a multi-network path.
   3. * @returns Returns true on success, otherwise false.
   4. * */
   5. export function requestMultiPath(): Promise<boolean> {
   6. return new Promise((resolve) => {
   7. try {
   8. netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
   9. if (data && data.result === netHandover.MultiPathErrorResult.MULTIPATH_ERROR_NONE) {
   10. resolve(true);
   11. } else {
   12. resolve(false);
   13. }
   14. });
   15. } catch (err) {
   16. resolve(false);
   17. const error: BusinessError = err as BusinessError;
   18. hilog.error(DOMAIN, TAG, `[requestMultiPath] Error:${error.code},${error.name}`);
   19. }
   20. })
   21. }
   ```

   [NetBoostManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/net/NetBoostManager.ets#L65-L85)

   多网请求成功后还需要使用[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#section7919111205211)监听多网状态，确认多网络通路的使能与可用情况，记录可用的NetHandle信息。

   ```
   1. /**
   2. * Enable multi-network listening.
   3. * @param netHandleChange The callback when the netHandle changes.
   4. */
   5. export function setOnMultiPathStateChange(netHandleChange: NetHandleChange) {
   6. try {
   7. netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
   8. if (data.multiPathState === netHandover.MultiPathState.MULTIPATH_CREATED &&
   9. data.netHandle.netId >= CommonConst.MIN_USEFUL_NET_ID) {
   10. netHandleChange?.onMultiNetSuccess(data.netHandle);
   11. } else if (data.multiPathState === netHandover.MultiPathState.MULTIPATH_CREATING) {
   12. hilog.info(DOMAIN, TAG, `[setOnMultiPathStateChange.multiPathStateChange] ${data.netHandle.netId} Creating`);
   13. } else {
   14. netHandleChange?.onMultiNetRelease(data.netHandle);
   15. }
   16. });
   17. } catch (err) {
   18. const error: BusinessError = err as BusinessError;
   19. hilog.error(DOMAIN, TAG, `[setOnMultiPathStateChange] Error:${error.code},${error.name}`);
   20. }
   21. }
   ```

   [NetBoostManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/net/NetBoostManager.ets#L139-L159)
2. 多网通路绑定Socket

   封装网络查询函数，通过[connection.getAllNetsSync()](../harmonyos-references/js-apis-net-connection.md#connectiongetallnetssync10)获取当前所有网络信息。由于网络传输任务一般放在子线程实现，而当前无法跨线程传递Socket对象和NetHandle对象，为了在子线程实现网络与Socket绑定需要获取所有网络信息，再通过之前请求多网后记录的NetHandle对象的ID找到指定网络在执行绑定操作；如果应用业务不涉及多线程问题可直接绑定上一步多网状态监听中获取到的NetHandle。

   ```
   1. /**
   2. * Get all netHandles.
   3. * @returns Returns all netHandles on success,otherwise returns undefined
   4. * */
   5. export function getAllNetHandles(): connection.NetHandle[] | undefined {
   6. try {
   7. let netHandles = connection.getAllNetsSync();
   8. const constNetHandles: connection.NetHandle[] = [];
   9. for (let i = 0; i < netHandles.length; i++) {
   10. hilog.info(DOMAIN, TAG, `[getAllNetHandles] success [${i}]>>>${netHandles[i].netId}`);
   11. if (netHandles[i].netId >= CommonConst.MIN_USEFUL_NET_ID) {
   12. constNetHandles.push(netHandles[i]);
   13. }
   14. }
   15. return constNetHandles;
   16. } catch (err) {
   17. const error: BusinessError = err as BusinessError;
   18. hilog.error(DOMAIN, TAG, `[getAllNetHandles] Error:${error.code},${error.name}`);
   19. return undefined;
   20. }
   21. }
   ```

   [NetConnectionManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/net/NetConnectionManager.ets#L44-L64)

   遍历获取到的所有网络，将多网状态监听中记录的可用网络通过bindSocket()绑定到Socket上，后续的TCP Socket进行网络传输任务时将会使用绑定的网络。

   ```
   1. /**
   2. * Binds the socket to the specified network path.
   3. * @param socketInstance  socket client.
   4. * @param netId netHandle Id.
   5. * @param port binds port.
   6. * */
   7. export async function bindSpecifiedNet(socketInstance: socket.TCPSocket, netId: number, port: number) {
   8. const netHandles = getAllNetHandles();
   9. if (netHandles) {
   10. for (let i = 0; i < netHandles.length; i++) {
   11. if (netHandles[i].netId === netId) {
   12. try {
   13. const connectionProperties = connection.getConnectionPropertiesSync(netHandles[i]);
   14. if (connectionProperties && connectionProperties.linkAddresses &&
   15. connectionProperties.linkAddresses.length > 0) {
   16. let netAddress: socket.NetAddress = {
   17. address: connectionProperties.linkAddresses[0].address.address,
   18. port: port
   19. };
   20. await socketInstance.bind(netAddress);
   21. await netHandles[i].bindSocket(socketInstance);
   22. } else {
   23. hilog.error(DOMAIN, TAG, `[socketBindNet] Get ConnectionProperties error`);
   24. }
   25. } catch (err) {
   26. const error: BusinessError = err as BusinessError;
   27. hilog.error(DOMAIN, TAG, `[socketBindNet] Error occurred:${error.code},${error.name}`);
   28. }
   29. break;
   30. }
   31. }
   32. } else {
   33. hilog.error(DOMAIN, TAG, `Net Empty`);
   34. }
   35. }
   ```

   [NetBoostManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/net/NetBoostManager.ets#L193-L227)
3. 文件分片处理

   封装文件处理类，设置分片文件数据结构，包括当前文件片段数量、开始位置、分片大小、片段重试次数等信息。

   ```
   1. /**
   2. * File upload chunk info.
   3. * */
   4. export class FileUpChunk {
   5. chunkNumber: number = 1;
   6. startPosition: number = 0;
   7. chunkSize: number = 0;
   8. buffer: ArrayBuffer = new ArrayBuffer(0);
   9. retryTimes: number = 0;
   10. }
   ```

   [FileUtils.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/utils/FileUtils.ets#L25-L34)

   提供方法根据文件大小计算分片规格，开发者可根据业务需要自行实现分片策略。

   ```
   1. function getChunkSize(fileSize: number): number {
   2. const MB = CommonConst.MIN_SLICE_FILE_SIZE;
   3. const fullMBs = Math.floor(fileSize / MB);
   4. let res = Math.max(1, Math.min(CommonConst.MAX_SLICE_FILE_COUNT, fullMBs));
   5. hilog.info(DOMAIN, TAG, `[getChunkSize] FileSize:${fileSize},ChunkSize:${res}`);
   6. return res;
   7. }
   ```

   [FileUtils.ets](https://gitcode.com/HarmonyOS_Samples/NetBoost/blob/master/entry/src/main/ets/utils/FileUtils.ets#L183-L189)

   通过[fs.statSync()](../harmonyos-references/js-apis-file-fs.md#fsstatsync)获取待上传文件的大小等信息，按照计算出的分片规格对文件进行分片处理。

   ```
   1. /**
   2. * Splits the file into segments.
   3. * @param file An opened file
   4. * @returns Returns all segments of the file.
   5. */
   6. export function splitFile(file: fileIo.File): FileUpChunk[] {
   7. try {
   8. const fileStat = fileIo.statSync(file.fd);
   9. const fileSize = fileStat.size;
   10. const chunks: FileUpChunk[] = [];
   11. let chunkNumber = 1;
   12. const splitChunkSize = Math.floor(fileStat.size / getChunkSize(fileSize));
   13. for (let start = 0; start < fileSize; start += splitChunkSize) {
   14. const chunkSize = Math.min(splitChunkSize, fileSize - start);
   15. const chunk = new FileUpChunk();
   16. chunk.chunkNumber = chunkNumber++;
   17. chunk.startPosition = start;
   18. chunk.chunkSize = chunkSize;
   19. chunks.push(chunk);
   20. }
   21. hilog.info(DOMAIN, TAG, `[splitFile] success`);
   22. return chunks;
   23. } catch (error) {
   24. const err: BusinessError = error as BusinessError;
   25. hilog.error(DOMAIN, TAG, `[splitFile] error:${err.code},${err.name}`);
   26. return [];
   27. }
   28. }
   ```

   [FileUtils.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/utils/FileUtils.ets#L152-L179)
4. 多Socket并发上传不同文件片段

   封装分片文件上传类，提供初始化分片上传接口，通知服务端待上传文件片段对应的存储路径。此处代码片段仅供参考，开发者可以根据自己业务的实际实现方式调整通信格式、请求参数等。

   ```
   1. /**
   2. * Initializes the upload.
   3. * @param host Server host.
   4. * @param port Server port.
   5. * @param uploadFileName File save path.
   6. * @returns Returns a 'InitiateMultipartUpload' object if success,otherwise returns undefined.
   7. */
   8. @Concurrent
   9. async function initMultiPartUpload(host: string, port: number,
   10. uploadFileName: string): Promise<InitiateMultipartUpload | undefined> {
   11. const objectKey: string = uploadFileName;
   12. const path = `/${objectKey}?uploads`;
   13. const method = http.RequestMethod.POST;
   14. const date = new Date().toUTCString();

   16. // build request headers
   17. const headers = [
   18. `Host: ${host}`,
   19. `Date: ${date}`,
   20. `Content-Length: 0`,
   21. `Content-Type: application/xml`,
   22. `Connection: close`
   23. ];

   25. // build request info
   26. const request = `${method} ${path} HTTP/1.1\r\n` + headers.join('\r\n') + CommonConst.HEADER_BODY_DELIMITER;
   27. // request data by socket
   28. const value: socket.SocketMessageInfo | undefined = await getDataBySocket(host, port, request);
   29. // parse result
   30. if (value) {
   31. try {
   32. let responseStr = buffer.from(value.message).toString('utf-8');
   33. const uploadIdMatch = responseStr.match(/<UploadId>(.*?)<\/UploadId>/);
   34. if (uploadIdMatch && uploadIdMatch[1]) {
   35. // start build 'InitiateMultipartUpload' object
   36. let result = XmlUtils.xmlToObj(extractHttpBody(responseStr), true);
   37. if (result && result['initiateMultipartUploadResult']) {
   38. const json: object = result['initiateMultipartUploadResult'];
   39. if (json) {
   40. return {
   41. bucket: json['bucket'],
   42. key: json['key'],
   43. uploadId: json['uploadId']
   44. } as InitiateMultipartUpload;
   45. }
   46. return undefined;
   47. } else {
   48. hilog.error(0x0000, 'FilePartsUploadManager',
   49. `[initiateMultipartUploadResult.onResult]: parse xml info error`);
   50. return undefined;
   51. }
   52. } else {
   53. hilog.error(0x0000, 'FilePartsUploadManager', `[initMultiPartUpload] onMessage ignore`);
   54. return undefined;
   55. }
   56. } catch (error) {
   57. const err: BusinessError = error as BusinessError;
   58. hilog.error(0x0000, 'FilePartsUploadManager', `[uploadPart] buffer.from error:${err.code},${err.name}`);
   59. return undefined;
   60. }
   61. } else {
   62. return undefined;
   63. }
   64. }
   ```

   [FilePartsUploadManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/viewmodel/upload/FilePartsUploadManager.ets#L32-L95)

   封装网络上传接口，包括创建TCP Socket实例并绑定到指定网络NetHandle、设置网络请求头等配置、通过[TCPSocket.send()](../harmonyos-references/js-apis-socket.md#send-2)方法发送请求至服务端并通过[TCPSocket.on('message')](../harmonyos-references/js-apis-socket.md#onmessage-1)监听响应。

   ```
   1. /**
   2. * Upload file segment.
   3. * @param host Server host.
   4. * @param port Server port.
   5. * @param initResult An 'InitiateMultipartUpload' object.
   6. * @param fileChunk File info to uploaded.
   7. * @param netId The ID of the netHandle to bind.
   8. * @returns Returns a 'UploadPartResult' object if success,otherwise returns undefined
   9. */
   10. @Concurrent
   11. async function uploadSegment(host: string, port: number, initResult: InitiateMultipartUpload, fileChunk: FileUpChunk,
   12. netId: number): Promise<UploadPartResult | undefined> {
   13. const socketInstance: socket.TCPSocket = socket.constructTCPSocketInstance();
   14. await bindSpecifiedNet(socketInstance, netId, CommonConst.SOCKET_BIND_UP_PORT);

   16. const path = `/${initResult.key}?partNumber=${fileChunk.chunkNumber}&uploadId=${initResult.uploadId}`;
   17. const method = http.RequestMethod.PUT;
   18. const date = new Date().toUTCString();
   19. // build request header
   20. const headers = [
   21. `Host: ${host}`,
   22. `Date: ${date}`,
   23. `Content-Length: ${fileChunk.chunkSize}`,
   24. `Content-Type: application/octet-stream`,
   25. `Connection: close`
   26. ];

   28. const requestHeader = `${method} ${path} HTTP/1.1\r\n` + headers.join('\r\n') + CommonConst.HEADER_BODY_DELIMITER;
   29. const headerBuffer = buffer.from(requestHeader, 'utf-8').buffer;

   31. // build request header and body
   32. const requestBuffer = new Uint8Array(headerBuffer.byteLength + fileChunk.buffer.byteLength);
   33. requestBuffer.set(new Uint8Array(headerBuffer), 0);
   34. requestBuffer.set(new Uint8Array(fileChunk.buffer), headerBuffer.byteLength);
   35. // get value from socket
   36. const value: socket.SocketMessageInfo | undefined =
   37. await getDataBySocket(host, port, requestBuffer.buffer, socketInstance);

   39. // parse value
   40. if (value) {
   41. try {
   42. let responseStr = buffer.from(value.message).toString('utf-8');
   43. // Get ETag
   44. const eTagMatch = responseStr.match(/ETag: "([^"]+)"/);
   45. if (eTagMatch && eTagMatch[1]) {
   46. return ({
   47. partNumber: fileChunk.chunkNumber,
   48. eTag: eTagMatch[1]
   49. } as UploadPartResult);
   50. } else {
   51. hilog.error(0x0000, 'FilePartsUploadManager',
   52. `[uploadPart] onMessage--> fileChunkId:${fileChunk.chunkNumber} upload failed`);
   53. return undefined;
   54. }
   55. } catch (error) {
   56. const err: BusinessError = error as BusinessError;
   57. hilog.error(0x0000, 'FilePartsUploadManager',
   58. `[uploadPart] buffer.from error:${err.code},${err.name},fileChunkId:${fileChunk.chunkNumber}`);
   59. return undefined;
   60. }
   61. } else {
   62. return undefined;
   63. }
   64. }
   ```

   [FilePartsUploadManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/viewmodel/upload/FilePartsUploadManager.ets#L99-L162)

   通过网络上传接口封装文件片段传输方法，包括读取当前文件片段、为当前NetHandle创建子线程发起上传任务、根据文件分片信息更新上传进度、以及失败重试等逻辑。在当前片段传输完毕后循环调用此方法上传剩余片段，直至无片段剩余。

   ```
   1. /**
   2. * Upload file segment using assigned net.
   3. */
   4. private async uploadFileChunkWithNet(netHandle: connection.NetHandle) {
   5. if (this.abortUpload) {
   6. return;
   7. }
   8. if (this.fileChunks.length === 0) {
   9. hilog.info(DOMAIN, TAG, `[MultiNetworkUploader.uploadFileChunkWithNet] fileChunks empty`);
   10. this.checkUploadSuccess();
   11. return;
   12. }

   14. const fileChunk = this.fileChunks.shift()!;
   15. let fileChunkWithData = readFileChunkBuffer(this.file!, fileChunk);
   16. // start upload a file chunk
   17. if (fileChunkWithData) {
   18. const task =
   19. new taskpool.Task(uploadSegment, CommonConst.UP_HOST, CommonConst.HTTP_DEFAULT_PORT, this.initMultipartUpload!,
   20. fileChunkWithData, netHandle.netId);
   21. try {
   22. const uploadPartRes = await taskpool.execute(task);
   23. // upload success
   24. if (uploadPartRes) {
   25. this.uploadResult.push(uploadPartRes as UploadPartResult);
   26. this.uploadFileChunkWithNet(netHandle);
   27. this.onProgressUpdate(this.uploadResult.length / this.fileChunksSize);
   28. } else {
   29. this.retryUpload(fileChunk, netHandle);
   30. hilog.error(DOMAIN, TAG, `[uploadFileChunkWithNet] upload failed`);
   31. }
   32. } catch (error) {
   33. this.retryUpload(fileChunk, netHandle);
   34. const err: BusinessError = error as BusinessError;
   35. hilog.error(DOMAIN, TAG, `[uploadFileChunkWithNet] taskpool error occurred:${err.code},${err.name}`);
   36. }
   37. } else {
   38. this.retryUpload(fileChunk, netHandle);
   39. hilog.error(DOMAIN, TAG, `[uploadFileChunkWithNet] readFileChunkBuffer failed`);
   40. }
   41. }
   ```

   [FilePartsUploadManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/viewmodel/upload/FilePartsUploadManager.ets#L316-L356)

   遍历NetHandle调用上传文件片段方法，为每个网络通路分配网络传输任务，实现多网络通路并发传输文件片段的效果。

   ```
   1. /**
   2. * Start upload file.
   3. */
   4. public startUpload() {
   5. if (!this.netHandles || this.netHandles.length === 0) {
   6. hilog.error(DOMAIN, TAG, `[MultiNetworkUploader.startUpload] netHandles is empty`);
   7. return;
   8. }

   10. if (!this.fileChunks || this.fileChunks.length === 0) {
   11. hilog.error(DOMAIN, TAG, `[MultiNetworkUploader.startUpload] fileChunks is empty`);
   12. return;
   13. }

   15. for (let i = 0; i < this.netHandles.length; i++) {
   16. this.uploadFileChunkWithNet(this.netHandles[i]);
   17. }
   18. }
   ```

   [FilePartsUploadManager.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/viewmodel/upload/FilePartsUploadManager.ets#L290-L307)
5. 通知服务端整合分片文件

   全部文件片段上传完毕后，通知服务端文件片段顺序，进行文件整合。

   ```
   1. /**
   2. *  Merge all file segments.
   3. * */
   4. private async mergeSegmentsOnServer() {
   5. fileIo.close(this.file?.fd).catch((error: BusinessError) => {
   6. hilog.error(DOMAIN, TAG, `[mergeSegmentsOnServer] Close file error:${error.code},${error.name}`);
   7. });
   8. this.uploadResult.sort((a, b) => a.partNumber - b.partNumber);
   9. const task = new taskpool.Task(completeMultiPartUploadRequest, CommonConst.UP_HOST, CommonConst.HTTP_DEFAULT_PORT,
   10. this.initMultipartUpload!,
   11. this.uploadResult);
   12. try {
   13. const res = await taskpool.execute(task);
   14. if (res) {
   15. this.onUploadSuccess();
   16. } else {
   17. this.onFailed();
   18. }
   19. } catch (error) {
   20. this.onFailed();
   21. }
   22. }
   ```

   [FilePartsUploadManager.ets](https://gitcode.com/HarmonyOS_Samples/NetBoost/blob/master/entry/src/main/ets/viewmodel/upload/FilePartsUploadManager.ets#L398-L419)
6. 释放资源

   通过[netHandover.releaseMultiPath()](../harmonyos-references/networkboost-nethandover.md#section196405414517)释放多网，注销相关的监听方法。

   ```
   1. /**
   2. * Stop multi net path.
   3. * */
   4. export function releaseMultiPath() {
   5. try {
   6. netHandover.releaseMultiPath();
   7. } catch (err) {
   8. const error: BusinessError = err as BusinessError;
   9. hilog.error(DOMAIN, TAG, `[releaseMultiPath] Error:${error.code},${error.name}`);
   10. }
   11. }

   13. // ...
   14. /**
   15. * Stop listening on multiple network paths.
   16. * */
   17. export function setOffMultiPathStateChange() {
   18. try {
   19. netHandover.off('multiPathStateChange');
   20. } catch (err) {
   21. const error: BusinessError = err as BusinessError;
   22. hilog.error(DOMAIN, TAG, `[setOffMultiPathStateChange] Error:${error.code},${error.name}`);
   23. }
   24. }
   ```

   [NetBoostManager.ets](https://gitcode.com/HarmonyOS_Samples/NetBoost/blob/master/entry/src/main/ets/net/NetBoostManager.ets#L89-L172)

## 多文件并发传输

### 场景描述

当进行数据、文件同步，下载器下载资源时，往往会需要处理多个文件的传输任务，使用多网并发拓宽网络带宽，不同文件传输任务分配给不同网络通路并发传输，达到提升传输效率的效果。

多文件并发传输与大文件分片传输对多网能力的使用原理相同，整体流程都是通过拉起多网后获取到多个netHandle，同时创建多个TCP Socket和不同netHandle绑定，再通过多个TCP Socket建立连接并行发起传输任务，区别只在于分片传输每个连接传输的是文件片段，而本场景传输的是不同文件。此处以并发传输两个文件作为示例场景。

### 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Fg-3znLYRlejOxWTA4GQRQ/zh-cn_image_0000002489628085.png?HW-CC-KV=V1&HW-CC-Date=20260428T002022Z&HW-CC-Expire=86400&HW-CC-Sign=346C0098A34590DE777C3EF9C23042B07BEB2E595D9625CBA2861D26D2A738E5 "点击放大")

### 代码实现

多网接入和绑定部分与分片传输场景一致，此处不再赘述，仅提供关键差异部分代码:

封装文件下载类，提供下载文件方法，根据下载对象链接与网络netId新建线程，发起文件下载任务。

```
1. /**
2. * Start download file.
3. * */
4. public async startDownload() {
5. if (this.downUrls) {
6. this.isFileDownloading = true;
7. const netId = this.netHandle ? this.netHandle.netId : -1;
8. const task = new taskpool.Task(getFileSizeWithNet, this.downUrls, CommonConst.HTTP_DEFAULT_PORT, netId);
9. try {
10. const fileSize = await taskpool.execute(task) as number;
11. if (fileSize > 0) {
12. // notify download start
13. this.onDownStart(fileSize);
14. this.fileChunk.endPosition = fileSize;
15. // start download the file using taskpool
16. const downTask =
17. new taskpool.Task(downloadFileChunkWithNet, this.downUrls, CommonConst.HTTP_DEFAULT_PORT, this.fileChunk,
18. netId, this.downListener);
19. const downRes = await taskpool.execute(downTask);
20. if (downRes) {
21. // notify download success
22. this.onDownSuccess();
23. } else {
24. // download failed,retry again
25. this.retryDownload();
26. }
27. } else {
28. // download failed,retry again
29. this.retryDownload();
30. hilog.error(DOMAIN, TAG, `[startDownload] download failed`);
31. }
32. } catch (error) {
33. // download failed,retry again
34. this.retryDownload();
35. const err: BusinessError = error as BusinessError;
36. hilog.error(DOMAIN, TAG, `[startDownload] taskpool error occurred:${err.code},${err.name}`);
37. }
38. } else {
39. hilog.warn(DOMAIN, TAG, `[startDownload] Url is null`);
40. // download failed,retry again
41. this.onDownFailed();
42. }
43. }
```

[FileDownManager.ets](https://gitcode.com/HarmonyOS_Samples/NetBoost/blob/master/entry/src/main/ets/viewmodel/download/FileDownManager.ets#L174-L216)

使用默认网络下载第一个文件，刷新对应的下载进度。

```
1. /**
2. * Downloads the first file using the specified netHandle.
3. * @param netHandle The specified netHandle to access the server.
4. * */
5. private startDownFirstFile(netHandle: connection.NetHandle) {
6. this.firstFileDownloader = new FileDownloadManager(this.firstDownFileInfo!, netHandle);
7. this.firstFileDownloader.onProgress = (downloaded: number, fileSize: number, progress: number) => {
8. this.downFirstProgress = progress;
9. this.downFirstProgressText = `${formatFileSize(downloaded)} / ${formatFileSize(fileSize)}`;
10. }
11. // download success
12. this.firstFileDownloader.onSuccess = () => {
13. this.firstFileDownloading = false;
14. this.downBtnEnable = (!this.firstFileDownloading) && (!this.secondFileDownloading) && this.taskArray.length === 0;
15. this.downFirstProgressColor = $r('sys.color.confirm');
16. let res = this.taskArray.shift();
17. this.downFirstFileResult = '';
18. if (res) {
19. this.startDownSecondFile(netHandle);
20. } else {
21. hilog.info(DOMAIN, TAG, `[startDownFirstFile]  File1 downloaded,no need to download File2`);
22. }
23. }
24. // download failed
25. this.firstFileDownloader.onError = () => {
26. this.firstFileDownloading = false;
27. this.downBtnEnable = (!this.firstFileDownloading) && (!this.secondFileDownloading);
28. if (this.downFirstProgress === 0) {
29. this.downFirstProgress = 0.01;
30. }
31. this.downFirstProgressColor = $r('sys.color.multi_color_08');
32. this.taskArray.shift();
33. this.downFirstFileResult = $r('app.string.down_failed');
34. }
35. // init downloading status
36. this.firstFileDownloading = true;
37. this.downFirstProgress = 0;
38. this.downFirstProgressColor = $r('sys.color.comp_background_emphasize');
39. this.downFirstFileResult = '';
40. // start download
41. this.firstFileDownloader.startDownload();
42. }
```

[DownloadPage.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/pages/DownloadPage.ets#L113-L154)

如果多网请求成功，在监听多网状态变更的回调中获取新的可用网络NetHandle，使用新网络NetHandle发起第二个文件的下载任务，达到并发下载的效果。

```
1. private netHandleChange: NetHandleChange = {
2. onMultiNetSuccess: async (netHandle: connection.NetHandle): Promise<void> => {
3. this.multiNetHandle = netHandle;
4. let res = this.taskArray.shift();
5. if (res) {
6. this.startDownSecondFile(netHandle);
7. } else {
8. hilog.info(DOMAIN, TAG, `[netHandleChange] Multi-net enable,but no need to download file2`);
9. }
10. },

12. onMultiNetRelease: async (netHandle: connection.NetHandle): Promise<void> => {
13. this.multiNetHandle = undefined;
14. }
15. }
```

[DownloadPage.ets](https://gitcode.com/harmonyos_samples/NetBoost/blob/master/entry/src/main/ets/pages/DownloadPage.ets#L67-L81)

## 常见问题

### 在进行多网并发传输时，如何判断当前使用的网络是Wi-Fi还是流量

请求多网成功后可以获取到多个可用的netHandle，通过[connection.getNetCapabilities()](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)方法查询网络信息，通过[NetBearType](../harmonyos-references/js-apis-net-connection.md#netbeartype)字段判断网络类型，其中BEARER\_CELLULAR是蜂窝网络，BEARER\_WIFI是Wi-Fi网络。在设计多网并发策略时可以通过网络类型和网络能力调整对应网络通路的网络任务。

### 如果使用多网并发能力超过剩余配额限制，会发生什么

配额（次数或时长）耗尽会限制使用，多网会自动释放，应用可以在[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#section7919111205211)中监听到多网退出回调。如果此时再请求多网会抛出错误码，应用可以在[netHandover.requestMultiPath()](../harmonyos-references/networkboost-nethandover.md#section8508131819279)的错误码中判断错误类型。应用配额以24小时的周期进行刷新。

## 示例代码

* [基于多网并发能力实现网络加速](https://gitcode.com/harmonyos_samples/NetBoost)
