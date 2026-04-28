---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-pauseresume
title: 实现请求暂停、恢复与断点续传
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 文件上传下载 > 实现请求暂停、恢复与断点续传
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e72fc2497acd7e19edcd634a436b78bd197d5e7164588616d109ff6d2bc4ab4a
---

## 约束与限制

请求暂停、恢复与断点续传能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 请求暂停、恢复

### 场景介绍

Remote Communication Kit提供完善的功能支持，包括请求的暂停和恢复功能。这不仅涵盖接收暂停，还包括发送暂停。

### 使用实例

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { util } from '@kit.ArkTS';
   ```
2. 定义调试信息接口、调试信息源类型以及调试信息序列化函数，用于将调试信息序列化为StringifiedDebugInfo数组。函数首先根据infoSource的类型获取调试信息，然后使用TextDecoder将调试信息的data字段解码为字符串，并返回一个包含解码后的调试信息的数组。

   ```
   1. const HTTP_SERVER_POST: string = "https://example.org/anything";
   2. // 定义调试信息接口
   3. interface StringifiedDebugInfo {
   4. type: rcp.DebugEvent;
   5. data: string;
   6. };
   7. // 定义调试信息源类型
   8. type DebugInfoSource = undefined | rcp.DebugInfo[] | rcp.Response;

   10. // 定义调试信息序列化函数
   11. function debugInfoStringify(infoSource: DebugInfoSource): StringifiedDebugInfo[] {
   12. const debugInfo = Array.isArray(infoSource)
   13. ? (infoSource as rcp.DebugInfo[])
   14. : (infoSource as rcp.Response).debugInfo;

   16. if (!debugInfo) {
   17. return [];
   18. }

   20. const decoder = util.TextDecoder.create('utf-8');
   21. return debugInfo.map((i: rcp.DebugInfo): StringifiedDebugInfo => {
   22. return {
   23. type: i.type,
   24. data: decoder.decodeToString(new Uint8Array(i.data)).trim(),
   25. };
   26. });
   27. }
   ```
3. 获取发送暂停和恢复事件，用于从调试信息中筛选出发送暂停和恢复事件。

   ```
   1. function getSendPausedEvents(debugInfo: DebugInfoSource) {
   2. return debugInfoStringify(debugInfo).filter((i) => i.data.startsWith('[[RCP]]: Pause sending'));
   3. }

   5. function getSendResumedEvents(debugInfo: DebugInfoSource) {
   6. return debugInfoStringify(debugInfo).filter((i) => i.data.startsWith('[[RCP]]: Resume sending'));
   7. }
   ```
4. 编写发起请求的函数。

   ```
   1. const SendingPauseByTimeout = async (done: Function): Promise<void> => {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request(HTTP_SERVER_POST);
   4. // 定义发送暂停策略，kind为'timeout'，timeoutMs为1ms
   5. const sendPolicy: rcp.SendingPausePolicy = {
   6. kind: 'timeout',
   7. timeoutMs: 1,
   8. };
   9. // 定义暂停策略，sending字段引用了上述定义的发送暂停策略
   10. const pausePolicy: rcp.PausePolicy = {
   11. sending: sendPolicy,
   12. };
   13. // 设置请求的配置，包括传输策略和跟踪信息
   14. request.configuration = {
   15. transfer: {
   16. pausePolicy: pausePolicy,
   17. },
   18. tracing: {
   19. infoToCollect: {
   20. textual: true,
   21. },
   22. },
   23. };
   24. // 定义请求体数据
   25. const data = 'TestData';
   26. // 设置请求头，'Content-Length'字段表示请求体的长度
   27. request.headers = {
   28. 'Content-Length': data.length.toString(),
   29. };
   30. // 定义布尔型标志变量用于控制请求体生成
   31. let isReadCompleted = false;
   32. // 设置请求方法为POST
   33. request.method = 'POST';
   34. // 定义请求体内容生成函数，如果read为true，则返回空的ArrayBuffer，否则生成包含请求体数据的ArrayBuffer
   35. request.content = (maxSize) => {
   36. if (isReadCompleted) {
   37. return new ArrayBuffer(0);
   38. }
   39. isReadCompleted = true;
   40. const buffer = new ArrayBuffer(data.length);
   41. util.TextEncoder.create('utf-8').encodeIntoUint8Array(data, new Uint8Array(buffer));
   42. return buffer;
   43. };

   45. // 发送请求并等待响应
   46. const response = await session.fetch(request)

   48. // 从响应的调试信息中获取发送暂停和恢复事件
   49. const pausedEvents = getSendPausedEvents(response);
   50. const resumedEvents = getSendResumedEvents(response);

   52. // 关闭会话
   53. session.close();
   54. // 调用完成回调函数
   55. done();
   56. }
   ```

## 实现断点续传

### 场景介绍

在需要接续数据请求的场景中，用户可以通过定义[TransferRange](../harmonyos-references/remote-communication-rcp.md#transferrange)对象的from和to属性来控制数据的截取范围。下载的内容可以被准确地截取并拼接到目标文件中，确保数据的完整性和一致性，开发者可以灵活地管理和恢复下载过程。

### 使用示例

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建session，定义请求URL，并对request进行配置，同时定义变量以记录下载文件的总大小。

   ```
   1. // 创建会话
   2. let session: rcp.Session | null = rcp.createSession();
   3. // 定义服务器地址
   4. const kHttpServerAddress = "http://www.example.com/fetch";
   5. // 创建请求
   6. const request = new rcp.Request(kHttpServerAddress, "GET");
   7. // 定义变量记录下载文件的大小
   8. let totalSize = 0;
   9. // 定义一个存储上次传输位置的变量
   10. let lastTransferPosition = 0;
   ```
3. 编写一个函数以获取要下载的文件大小。有多种方法可以获取下载文件的大小，请根据实际需求选择合适的方法。在本例中，通过从响应数据的header中的content-range字段来获取下载文件的总大小。

   ```
   1. /**
   2. * 获取要下载文件的大小
   3. *
   4. * @returns 文件的大小
   5. */
   6. async function getTotalSize(): Promise<number> {
   7. request.transferRange = { from: 0, to: 1 };
   8. try {
   9. let rep = await session?.fetch(request);
   10. if (rep) {
   11. // 从响应数据的header的content-range字段中提取出文件的大小
   12. let contentRange = rep.headers['content-range'];
   13. let sizeStr = contentRange ? contentRange.substring(contentRange.indexOf('\/') + 1, contentRange.length) : '0';
   14. totalSize = Number(sizeStr);
   15. }
   16. } catch (err) {
   17. console.error(`getTotalSize error code is ${err.code}, error data is ${err.data}`);
   18. }
   19. console.info(`getTotalSize totalSize: ${totalSize.toString()}`);
   20. return totalSize;
   21. }
   ```
4. 编写一个依据传输范围下载文件的函数。

   ```
   1. /**
   2. * 根据传输范围下载文件
   3. *
   4. * @param from - 传输范围的起始位置
   5. * @param to - 传输范围的结束位置
   6. */
   7. function downloadTransfer(from: number, to: number) {
   8. // 设置请求的数据传输范围
   9. request.transferRange = { from: from, to: to };
   10. session?.fetch(request).then((rep) => {
   11. if (rep.body) {
   12. // 处理响应，可以在此处将文件保存到本地
   13. console.info(`Response succeeded: ${JSON.stringify(rep.headers)}`);
   14. // 下次传输的起始位置 = 上次的位置 + 本次传输数据的长度
   15. lastTransferPosition += rep.body.byteLength;
   16. if (lastTransferPosition < totalSize) {
   17. // 计算下一次传输范围的结束位置
   18. const nextTo = Math.min(lastTransferPosition + 100, totalSize);
   19. // 递归调用继续下载下一段数据
   20. downloadTransfer(lastTransferPosition, nextTo);
   21. } else {
   22. console.info("Response succeeded, completed.");
   23. }
   24. }
   25. }).catch((err: BusinessError) => {
   26. console.error(`Continue transfer error: code is ${err.code}, message is ${err.message}`);
   27. });
   28. }
   ```
5. 使用以下方式开始下载。

   ```
   1. /**
   2. * 开始下载
   3. */
   4. async function startDownload() {
   5. if (!session) {
   6. session = rcp.createSession();
   7. }
   8. // 传输位置归零
   9. lastTransferPosition = 0;
   10. // 获取要下载文件的总大小
   11. totalSize = await getTotalSize();
   12. // 计算传输范围的结束位置
   13. const nextTo = Math.min(lastTransferPosition + 100, totalSize);
   14. // 开始下载
   15. downloadTransfer(lastTransferPosition, nextTo);
   16. }
   ```
6. 使用以下方式暂停下载。

   ```
   1. /**
   2. * 暂停下载
   3. */
   4. function pauseDownload() {
   5. // 取消下载请求
   6. session?.cancel(request);
   7. }
   ```
7. 使用以下方式继续下载。

   ```
   1. /**
   2. * 继续下载
   3. */
   4. function resumeDownload() {
   5. // 计算传输范围的结束位置
   6. const nextTo = Math.min(lastTransferPosition + 100, totalSize);
   7. // 开始下载
   8. downloadTransfer(lastTransferPosition, nextTo);
   9. }
   ```
8. 使用以下方式停止下载。

   ```
   1. /**
   2. * 停止下载
   3. */
   4. function stopDownload() {
   5. // 取消下载请求
   6. session?.cancel(request);
   7. // 关闭session
   8. session?.close();
   9. session = null;
   10. }
   ```
