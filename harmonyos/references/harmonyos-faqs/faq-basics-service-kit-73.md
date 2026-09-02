---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-73
title: request.downloadFile, on('fail')回调报错8(ERROR_UNKNOWN) 的处理方法
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > request.downloadFile, on('fail')回调报错8(ERROR_UNKNOWN) 的处理方法
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:17+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:29f3c1f4f21e6af20f3f9c434fabddfbd27d8ba6bf0580bebd457bd266844002
---

## 问题现象

使用 @ohos.request 模块进行上传或下载时，任务失败后无法定位具体原因：

* **场景1：** 下载接口 request.downloadFile

  在 on('fail') 回调的 err 参数中收到错误码 **8**（ERROR\_UNKNOWN），提示未知错误。
* **场景2：** 上传接口 request.uploadFile

  on('fail') 回调返回 Array<TaskState>，不是数字错误码，不会返回 ERROR\_UNKNOWN。
* **场景3：** 上传下载接口 request.agent.create

  on('failed') 回调仅通知任务失败，不直接返回错误码，需通过 request.agent.show 查询 TaskInfo.reason 获取具体原因（如 "DNS error"、"TCP error" 等）。上传和下载任务均适用。

**说明** 

ERROR\_UNKNOWN 是 DownloadTask.on('fail') 回调中返回的错误码，不会在调用 request.agent.create、request.downloadFile 或 request.uploadFile 时作为异常抛出。上传任务 UploadTask.on('fail') 返回的是 Array<TaskState>，不使用此错误码。

## 背景知识

OpenHarmony 上传下载模块提供文件上传和下载能力，支持两种调用方式：

| 调用方式 | 最低API版本 | 说明 |
| --- | --- | --- |
| request.uploadFile / request.downloadFile | API 12 | 轻量接口，仅支持应用缓存目录下的文件 |
| request.agent.create | API 12 | 代理任务接口，支持前后台模式、用户文件路径等更多配置 |

下载任务错误码（DownloadTask.on('fail') 回调的 err 参数，或 getTaskInfo 返回的 failedReason 字段）：

| 错误码 | 常量名 | 说明 |
| --- | --- | --- |
| 0 | ERROR\_CANNOT\_RESUME | 网络原因导致恢复下载失败 |
| 3 | ERROR\_FILE\_ERROR | 文件操作失败 |
| 5 | ERROR\_INSUFFICIENT\_SPACE | 存储空间不足 |
| 8 | ERROR\_UNKNOWN | 未知错误 |
| 9 | ERROR\_OFFLINE | 网络未连接 |
| 10 | ERROR\_UNSUPPORTED\_NETWORK\_TYPE | 网络类型不匹配 |

ERROR\_UNKNOWN 是兜底错误码，表示失败原因无法归类到上述已知错误码中。对于 request.agent.create 创建的上传或下载任务，还可通过 on('faultOccur') 回调（API 20+）直接获取 Faults 枚举值，精准定位故障类型，无需二次查询：

| 故障类型 | 值 | 说明 |
| --- | --- | --- |
| Faults.OTHERS | 0xFF | 其他故障 |
| Faults.DISCONNECTED | 0x00 | 网络断开连接 |
| Faults.TIMEOUT | 0x10 | 任务超时 |
| Faults.PROTOCOL | 0x20 | 协议错误（如 500、416 等） |
| Faults.PARAM | 0x30 | 参数错误（如 URL 格式错误） |
| Faults.FSIO | 0x40 | 文件系统 IO 错误 |
| Faults.DNS | 0x50 | DNS 解析错误 |
| Faults.TCP | 0x60 | TCP 连接错误 |
| Faults.SSL | 0x70 | SSL 连接错误（如证书错误） |
| Faults.REDIRECT | 0x80 | 重定向错误 |
| Faults.LOW\_SPEED | 0x90 | 任务速度过低 |

**说明** 

on('faultOccur') 仅适用于 request.agent.create 创建的任务（API 20+），request.downloadFile / request.uploadFile 创建的 DownloadTask / UploadTask 不支持此回调。

## 问题定位

ERROR\_UNKNOWN 是兜底错误码，多种失败场景均会回退到此错误码。收到 ERROR\_UNKNOWN 后，建议优先通过 reason 或 Faults 定位具体原因，再根据具体原因针对性处理：

1. **通过 reason 或 Faults 定位具体原因**
   * **输入**：任务失败后的回调信息
   * **操作**：查询 request.agent.show 返回的 TaskInfo.reason 字段值，或 on('faultOccur') 返回的 Faults 枚举值
   * **输出**：确定具体的故障类型

   TaskInfo.reason 字段值与 Faults 枚举值的对应关系：

   | reason 字段值 | 对应 Faults | 说明 |
   | --- | --- | --- |
   | DNS error | Faults.DNS | DNS 解析失败 |
   | TCP error | Faults.TCP | TCP 连接错误 |
   | TSL/SSL error | Faults.SSL | SSL/TLS 握手错误 |
   | Http protocol error | Faults.PROTOCOL | HTTP 协议交互异常 |
   | The server is not support range request | Faults.PROTOCOL | 服务器不支持 Range 请求 |
   | Request error | Faults.OTHERS | 请求错误 |
   | There are some files upload failed | Faults.OTHERS | 上传文件失败 |
   | Build request error | Faults.OTHERS | 请求构造过程中出错 |
   | Failed because cannot get the file size from the server and the precise is setted true by user | Faults.PROTOCOL | 精确模式下无法从服务器获取文件大小 |
   | Continuous processing task time out | Faults.TIMEOUT | 任务执行时间超限 |
   | Account stopped | Faults.DISCONNECTED | 用户账号已停用 |
   | NetWork is offline and the app is background or terminate | Faults.DISCONNECTED | 网络断开且应用在后台或已终止 |
   | NetWork is offline and the account is stopped | Faults.DISCONNECTED | 网络断开且用户账号已停用 |
   | The app is background or terminate and the account is stopped | Faults.DISCONNECTED | 应用在后台或已终止且用户账号已停用 |
   | NetWork is offline and the app is background or terminate and the account is stopped | Faults.DISCONNECTED | 网络断开、应用在后台或已终止且用户账号已停用 |
   | Below low speed limit | Faults.LOW\_SPEED | 传输速度低于配置的最低速度阈值 |
   | Some other error occured | Faults.OTHERS | 其他未分类错误 |
   | unknown error | Faults.OTHERS | 无法识别的错误类型 |

   **说明** 

   reason 字段值为系统内部描述，不同版本可能存在差异。Faults 枚举值与 reason 字段值为近似映射，并非严格一一对应。
2. **检查网络连接状态**
   * **输入**：reason 为 "DNS error"/"TCP error"/"TSL/SSL error" 等，或 Faults 为 DNS/TCP/SSL 等
   * **操作**：确认设备网络连接状态，检查是否可访问目标 URL
   * **输出**：确定是否为网络层错误导致

   这是最常见的触发原因。DNS 解析失败、TCP 连接超时、SSL/TLS 握手失败等网络层错误均会回退到 ERROR\_UNKNOWN。

   解决方法：

   * 确认设备网络连接正常，可以访问目标 URL。
   * 如果使用 HTTPS，确认服务器证书有效且 TLS 版本兼容。
   * API version 12 及以下版本，系统仅支持串行地尝试连接域名相关 IP，不支持单个 IP 的连接时间控制。若 DNS 返回的首个 IP 被阻塞，可能会由于握手超时导致 ERROR\_UNKNOWN 错误。建议升级到 API version 13 及以上版本。
3. **检查服务器是否支持 Range 请求**
   * **输入**：reason 为 "The server is not support range request"，或 Faults 为 PROTOCOL，且下载任务配置了 begins 或 index 参数
   * **操作**：确认服务器是否支持 Range 请求
   * **输出**：若服务器不支持 Range 请求但配置了断点续传参数，则触发 ERROR\_UNKNOWN

   此场景仅适用于下载任务。

   常见错误写法：

   ```ts
   let config: request.agent.Config = {
     action: request.agent.Action.DOWNLOAD,
     url: 'https://example.com/file.zip',
     begins: 1024,
   };
   ```

   解决方法：如果服务器不支持 Range 请求，不要设置 begins 和 ends 参数，从起始位置完整下载。

## 分析结论

* **原因1：** 网络连接异常（DNS 解析失败、TCP 连接超时、SSL/TLS 握手失败等），是最常见的触发原因。
* **原因2：** 服务器不支持 Range 请求但配置了断点续传参数，仅适用于下载任务。
* **原因3：** 其他未分类错误，如请求构造失败、上传文件失败等。

定位具体原因的方式取决于使用的接口：

| 场景 | 定位方式 |
| --- | --- |
| 下载（request.downloadFile） | getTaskInfo 获取任务 ID → request.agent.show 查询 TaskInfo.reason |
| 上传（request.uploadFile） | on('fail') 回调返回 Array<TaskState>，通过 responseCode 和 message 获取失败信息 |
| 上传下载（request.agent.create） | request.agent.show 查询 TaskInfo.reason；API 20+ 还可使用 on('faultOccur') 回调直接获取 Faults 枚举值 |

## 修改建议

* **场景1：** 网络环境

  确保设备网络连接正常，HTTPS 场景确认服务器证书有效。
* **场景2：** 断点续传

  仅在确认服务器支持 Range 请求时，才配置 begins 和 ends 参数。
* **场景3：** 错误处理

  收到 ERROR\_UNKNOWN 后，根据上述定位方式获取具体失败原因并针对性处理。request.downloadFile 接口示例（on('fail') → getTaskInfo → request.agent.show）：

  ```ts
  import { request } from '@kit.BasicServicesKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let downloadTask: request.DownloadTask = await request.downloadFile(context, {
    url: 'https://example.com/file.zip',
    filePath: context.cacheDir + '/file.zip',
  });

  downloadTask.on('fail', async (err: number) => {
    if (err === request.ERROR_UNKNOWN) {
      try {
        let downloadInfo = await downloadTask.getTaskInfo();
        let taskInfo = await request.agent.show(String(downloadInfo.downloadId));
        console.error(`Download failed, reason: ${taskInfo.reason}`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(`Failed to get task detail, code: ${error.code}`);
      }
    } else {
      console.error(`Download failed with error code: ${err}`);
    }
  });
  ```

  request.agent.create 接口示例（API 20+ 推荐使用 on('faultOccur')，API 12-19 使用 on('failed') + request.agent.show。上传和下载任务均适用）：

  ```ts
  import { request } from '@kit.BasicServicesKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  async downloadWithErrorHandling(
    url: string,
    fileName: string,
    context: common.UIAbilityContext
  ) {
    let config: request.agent.Config = {
      action: request.agent.Action.DOWNLOAD,
      url: url,
      saveas: fileName,
      overwrite: true,
      gauge: true,
    };

    try {
      let task = await request.agent.create(context, config);

      task.on('completed', () => {
        console.info('Download completed');
        request.agent.remove(task.tid);
      });

      task.on('failed', async (progress: request.agent.Progress) => {
        try {
          let taskInfo = await request.agent.show(task.tid);
          console.error(`Download failed, reason: ${taskInfo.reason}`);
        } catch (e) {
          let err = e as BusinessError;
          console.error(`Show task info failed, code: ${err.code}`);
        }
        request.agent.remove(task.tid);
      });

      task.on('faultOccur', (faults: request.agent.Faults) => {
        switch (faults) {
          case request.agent.Faults.DNS:
            console.error('Download failed: DNS resolution error');
            break;
          case request.agent.Faults.TCP:
            console.error('Download failed: TCP connection error');
            break;
          case request.agent.Faults.SSL:
            console.error('Download failed: SSL/TLS error');
            break;
          case request.agent.Faults.PROTOCOL:
            console.error('Download failed: Protocol error');
            break;
          case request.agent.Faults.TIMEOUT:
            console.error('Download failed: Task timeout');
            break;
          case request.agent.Faults.LOW_SPEED:
            console.error('Download failed: Transfer speed below threshold');
            break;
          case request.agent.Faults.DISCONNECTED:
            console.error('Download failed: Network disconnected');
            break;
          default:
            console.error(`Download failed: Other fault (${faults})`);
            break;
        }
        request.agent.remove(task.tid);
      });

      task.start((err: BusinessError) => {
        if (err) {
          console.error(`Start failed, code: ${err.code}, message: ${err.message}`);
        }
      });
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Create task failed, code: ${err.code}, message: ${err.message}`);
    }
  }
  ```

  **说明** 

  on('faultOccur') 和 on('failed') 可以同时注册，两者都会在任务失败时触发。API 20+ 推荐使用 on('faultOccur') 直接获取故障类型；API 12-19 仅支持 on('failed')，需通过 request.agent.show 二次查询。

## 常见FAQ

Q：下载失败回调返回 ERROR\_UNKNOWN (8)，如何获取具体原因？

A：根据使用的接口选择不同方式：

* **下载**（request.downloadFile）：通过 getTaskInfo 获取任务 ID，再使用 request.agent.show 查询 TaskInfo.reason。
* **上传**（request.uploadFile）：on('fail') 回调返回 Array<TaskState>，通过 responseCode 和 message 获取失败信息。UploadTask 没有 getTaskInfo 方法，无法使用 request.agent.show。
* **上传下载**（request.agent.create）：可通过 request.agent.show 查询 TaskInfo.reason；API 20+ 还可使用 on('faultOccur') 回调直接获取 Faults 枚举值，无需二次查询。上传和下载任务均适用。

Q：上传任务失败时也会返回 ERROR\_UNKNOWN 吗？

A：不会。UploadTask.on('fail') 回调返回的是 Array<TaskState>，不是数字错误码，因此不会返回 ERROR\_UNKNOWN。request.uploadFile 上传任务只能通过 TaskState.responseCode 和 TaskState.message 获取失败信息；request.agent.create 上传任务可通过 request.agent.show 查询 TaskInfo.reason，或通过 on('faultOccur')（API 20+）获取 Faults 枚举值来定位。

Q：on('faultOccur') 和 on('failed') 有什么区别？

A：两者都是 request.agent.Task 对象的事件，都会在任务失败时触发。区别在于：on('failed') 回调参数为 Progress 对象，不包含错误码，需通过 request.agent.show 二次查询；on('faultOccur') 回调参数直接为 Faults 枚举值，可精准区分故障类型，无需二次查询。两者都仅适用于 request.agent.create 创建的任务，on('faultOccur') 从 API 20 开始支持。

Q：API version 12 及以下版本频繁出现 ERROR\_UNKNOWN，可能是什么原因？

A：API version 12 及以下版本，系统仅支持串行地尝试连接域名相关 IP，不支持单个 IP 的连接时间控制。若 DNS 返回的首个 IP 被阻塞，可能会由于握手超时导致 ERROR\_UNKNOWN 错误。建议升级到 API version 13 及以上版本。

Q：配置了断点续传后下载报 ERROR\_UNKNOWN，如何解决？

A：请确认服务器是否支持 Range 请求。如果服务器不支持 Range 请求，不要设置 begins 和 ends 参数，从起始位置完整下载。API 20+ 中此场景会触发 on('faultOccur') 回调并返回 Faults.PROTOCOL。
