---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-environment
title: @ohos.file.environment (目录环境能力)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.environment (目录环境能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3c4704e14cf5eb7a6a5f676c7a8c34e2432213b968e9b050e240c75befe74cac
---

该模块提供环境目录能力，获取内存存储根目录、公共文件根目录的ArkTS接口。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { Environment } from '@kit.CoreFileKit';
```

## Environment.getUserDownloadDir

PC/2in1

getUserDownloadDir(): string

获取当前用户预授权下载目录的沙箱路径。

**系统能力**：SystemCapability.FileManagement.File.Environment.FolderObtain

**设备行为差异**：该接口在2in1中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前用户预授权下载目录的沙箱路径。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function getUserDownloadDirExample() {
3. try {
4. let path = Environment.getUserDownloadDir();
5. console.info(`Succeeded in getUserDownloadDir, path is ${path}`);
6. } catch (err) {
7. console.error(`Failed to getUserDownloadDir. Code: ${err.code}, message: ${err.message}`);
8. }
9. }
```

## Environment.getUserDesktopDir

PC/2in1

getUserDesktopDir(): string

获取当前用户预授权桌面目录的沙箱路径。

**系统能力**：SystemCapability.FileManagement.File.Environment.FolderObtain

**设备行为差异**：该接口在2in1中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前用户预授权桌面目录的沙箱路径。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function getUserDesktopDirExample() {
3. try {
4. let path = Environment.getUserDesktopDir();
5. console.info(`Succeeded in getUserDesktopDir, path is ${path}`);
6. } catch (err) {
7. console.error(`Failed to getUserDesktopDir. Code: ${err.code}, message: ${err.message}`);
8. }
9. }
```

## Environment.getUserDocumentDir

PC/2in1

getUserDocumentDir(): string

获取当前用户预授权文档目录的沙箱路径。

**系统能力**：SystemCapability.FileManagement.File.Environment.FolderObtain

**设备行为差异**：该接口在2in1中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前用户预授权文档目录的沙箱路径。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function getUserDocumentDirExample() {
3. try {
4. let path = Environment.getUserDocumentDir();
5. console.info(`Succeeded in getUserDocumentDir, path is ${path}`);
6. } catch (err) {
7. console.error(`Failed to getUserDocumentDir. Code: ${err.code}, message: ${err.message}`);
8. }
9. }
```
