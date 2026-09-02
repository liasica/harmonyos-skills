---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-20
title: Request上传下载任务报错13400001
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > Request上传下载任务报错13400001
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2cbe760071fffd4940afcb5b7cd1efa8a9d3d1098428ba70ec1d9a95be2c9dbe
---

## 问题现象

使用@ohos.request模块进行文件上传下载时，调用request.agent.create或request.downloadFile抛出错误码**13400001**（EXCEPTION\_FILEIO），提示"Invalid file or file system error"。

典型日志：

```txt
err.code : 13400001, err.errInfo : GetFd File exists and other error
```

err.errInfo的内容可帮助判断具体原因。

## 背景知识

| 调用方式 | 最低API版本 | 说明 |
| --- | --- | --- |
| request.downloadFile | API 12 | 轻量下载接口，仅支持应用缓存目录下的文件 |
| request.uploadFile | API 12 | 轻量上传接口，仅支持应用缓存目录下的文件 |
| request.agent.create | API 12 | 代理任务接口，支持前后台模式、用户文件路径等更多配置 |

| 错误码 | 常量名 | 说明 |
| --- | --- | --- |
| 13400001 | EXCEPTION\_FILEIO | 文件 I/O 操作异常 |
| 13400002 | EXCEPTION\_FILEPATH | 文件路径异常 |
| 13400003 | EXCEPTION\_SERVICE | 服务异常 |

13400001侧重于文件I/O操作本身失败，13400002侧重于文件路径格式不合法。部分场景在request.downloadFile和request.agent.create中返回的错误码不同：**上传任务在request.uploadFile下，文件路径相关的错误（文件不存在、fopen 失败等）返回13400002而非13400001**，仅body临时文件创建失败、ACL授权失败等少数场景会返回13400001。

## 问题定位

根据日志中的err.errInfo信息，按以下步骤排查：

1. **检查下载目标文件是否已存在**
   * **输入**：下载任务配置，日志中err.errInfo包含GetFd File exists and other error
   * **操作**：确认下载目标文件是否已存在且未设置覆盖
   * **输出**：若文件已存在，request.agent.create返回13400001，request.downloadFile返回13400002

   设置overwrite: true，或创建任务前删除已有文件：

   ```ts
   import { fileIo } from '@kit.CoreFileKit';

   let filePath = context.cacheDir + '/download.zip';
   try {
     fileIo.unlinkSync(filePath);
   } catch (e) {
     // 文件不存在，忽略
   }

   let config: request.agent.Config = {
     action: request.agent.Action.DOWNLOAD,
     url: 'https://example.com/file.zip',
     saveas: 'download.zip',
     overwrite: true,
   };
   ```

   **说明** 

   request.downloadFile不支持overwrite参数，文件已存在时返回13400002。
2. **检查文件描述符（fd）及系统调用错误**
   * **输入**：日志中err.errInfo包含GetFd failed to open file errno <数字>（下载场景）或UploadBodyFiles failed to open file errno <数字>（上传场景，body临时文件创建失败）
   * **操作**：根据日志中的errno数值对照下表判断原因
   * **输出**：确定具体的系统级错误原因

   **说明** 

   下载场景的GetFd错误在request.downloadFile下同样返回13400001（不区分版本）。上传场景中，源文件fopen失败在request.uploadFile下返回13400002，仅body临时文件创建失败返回13400001。

   常见errno值：

   | errno常量 | 数值 | 含义 | 排查建议 |
   | --- | --- | --- | --- |
   | ENOENT | 2 | 文件或目录不存在 | 检查路径中的各级目录是否存在 |
   | EINTR | 4 | 系统调用被信号中断 | 偶发情况，可重试 |
   | EIO | 5 | 底层I/O错误 | 可能是存储设备故障，检查设备健康状态 |
   | EACCES | 13 | 权限不足 | 检查应用是否有目标路径的读写权限 |
   | ENOTDIR | 20 | 路径组件非目录 | 检查路径中是否有非目录的组件被当作目录使用 |
   | EISDIR | 21 | 路径是目录而非文件 | 检查saveas路径是否指向了目录 |
   | ENFILE | 23 | 系统级打开文件数超限 | 系统fd耗尽，需等待其他进程释放或重启设备 |
   | EMFILE | 24 | 进程级打开文件数超限 | 检查应用是否打开了过多文件，关闭不需要的文件描述符后重试 |
   | ENOSPC | 28 | 磁盘空间不足 | 清理磁盘空间后重试 |
   | EROFS | 30 | 只读文件系统 | 检查目标路径是否在只读分区上，改用应用沙箱可写目录 |
   | ENAMETOOLONG | 36 | 路径名过长 | 缩短文件路径或文件名 |
   | ELOOP | 40 | 符号链接循环 | 检查路径中是否存在循环的符号链接 |

   排查方法：根据日志中的errno数值对照上表判断原因。如遇未列出的errno值，可通过以下方式查阅：

   * errno -l：列出系统上所有errno常量及其数值和描述，例如输入errno 24可直接查看errno 24的含义。
   * man 2 open：查看open()系统调用手册，其中的ERRORS章节列出了所有可能的errno及触发条件。
3. **检查文件保存路径是否有效**
   * **输入**：日志中err.errInfo包含path error
   * **操作**：检查saveas路径是否有效且附带文件名
   * **输出**：空路径或仅含前缀（如internal://cache/）会导致13400001

   ```ts
   // 错误：internal://cache/ 后没有文件名，或 saveas 为空
   saveas: 'internal://cache/'
   saveas: ''

   // 正确：附带文件名
   saveas: 'internal://cache/file.zip'
   ```

   **说明** 

   internal://cache/前缀对应应用的cacheDir目录。使用request.agent.create时，saveas也可直接使用沙箱绝对路径，如context.cacheDir + '/file.zip'。
4. **检查上传文件是否存在且可读**
   * **输入**：日志中err.errInfo 包含 path error: path: /data/storage/...
   * **操作**：确认上传源文件是否存在且为普通文件（非目录）
   * **输出**：若文件不存在，request.agent.create返回13400001，request.uploadFile返回13400002

   上传前确认文件存在：

   ```ts
   import { fileIo } from '@kit.CoreFileKit';

   let filePath = context.cacheDir + '/test.txt';
   try {
     let stat = fileIo.statSync(filePath);
     console.info(`File exists, size: ${stat.size}`);
   } catch (e) {
     console.error('Upload file does not exist, please check the path.');
     return;
   }
   ```
5. **检查应用是否有文件访问权限**
   * **输入**：日志中err.errInfo包含permission fail
   * **操作**：检查应用对目标路径是否有读写权限
   * **输出**：无权限时文件操作失败并返回13400001

   常见场景：

   * 下载文件保存到应用沙箱外的路径，无写入权限。
   * 上传来自用户目录（如file://docs/、file://media/）的文件，无读取权限。

   解决方法：下载保存到应用沙箱目录（cacheDir、filesDir等）；上传用户文件时确保已获取相应权限，并使用UIAbilityContext。
6. **检查证书路径是否有效**
   * **输入**：下载URL使用HTTPS且配置了certsPath，日志中err.errInfo包含bad certs\_path
   * **操作**：检查证书目录是否存在且包含有效证书文件
   * **输出**：证书目录不存在或路径无效时触发13400001

   解决方法：确保certsPath指向存在的目录，且目录中包含有效的证书文件。
7. **检查磁盘空间是否充足**
   * **输入**：日志中err.errInfo包含open fail，且文件路径和权限均无问题
   * **操作**：检查设备可用存储空间
   * **输出**：磁盘空间不足导致文件创建或写入失败时触发13400001

   解决方法：下载前检查可用存储空间，或在任务失败回调中提示用户清理空间后重试。

## 分析结论

* **原因1：**下载目标文件已存在，日志特征File exists and other error，发生频率高。
* **原因2：**fd/errno错误（fd耗尽、只读文件系统等），日志特征GetFd failed to open file errno <数字>，发生频率高。
* **原因3：**文件保存路径无效（空路径或仅含前缀），日志特征path error，发生频率中。
* **原因4：**上传文件不存在，日志特征path error: path: ...，发生频率中。
* **原因5：**文件访问权限不足，日志特征permission fail，发生频率低。
* **原因6：**证书路径无效，日志特征bad certs\_path，发生频率低。
* **原因7：**磁盘空间不足，日志特征open fail，发生频率低。

## 修改建议

* **场景1：**下载任务

  确保saveas路径有效且附带文件名，按需设置overwrite: true，下载前检查磁盘空间。
* **场景2：**上传任务

  确保源文件存在且可读，使用正确的路径前缀（internal://cache/或沙箱绝对路径）。
* **场景3：**错误处理

  捕获13400001后根据err.errInfo判断具体原因。若信息包含errno，解析数值后对照问题定位第2步的errno表给出针对性提示。建议同时兼容13400002，因为上传任务在request.uploadFile下多数文件错误返回13400002。

## 常见FAQ

Q：不同接口的13400001错误有什么区别？

A：部分场景在request.uploadFile / request.downloadFile中返回13400002，request.agent.create中返回13400001。例如：下载文件已存在且不允许覆盖时，request.downloadFile返回13400002，request.agent.create返回13400001；上传文件不存在或无法打开时，request.uploadFile返回13400002，request.agent.create返回13400001。建议错误处理中同时兼容这两个错误码。

Q：request.uploadFile会返回13400001吗？

A：会，但场景有限。上传源文件不存在、fopen失败等核心场景在request.uploadFile下返回13400002；仅body临时文件创建失败（UploadBodyFiles failed to open file errno）、文件路径ACL授权失败、证书目录权限失败等场景会返回13400001。

Q：日志中err.errInfo包含errno数值，如何解读？

A：errno数值对应系统错误码，常见如：errno 24（EMFILE）表示进程级fd超限，需关闭不需要的文件描述符后重试；errno 23（ENFILE）表示系统级fd超限，需等待其他进程释放或重启设备；errno 30（EROFS）表示只读文件系统，需改用应用沙箱可写目录。完整对照见问题定位第2步errno表。

Q：日志中err.errInfo显示open fail，但文件路径和权限都没问题，可能是什么原因？

A：可能是磁盘空间不足导致文件创建失败，建议检查设备可用存储空间。此外，其他进程占用该文件也可能导致打开失败。
