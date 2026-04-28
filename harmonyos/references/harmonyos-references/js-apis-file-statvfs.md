---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-statvfs
title: @ohos.file.statvfs (文件系统空间统计)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.statvfs (文件系统空间统计)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c08c0e25e2e215bd3e94c2975bf59559d3f1890d431ba6fd929feeea04e3b4bc
---

该模块提供文件系统相关存储信息的功能：向应用程序提供获取文件系统总字节数、空闲字节数的ArkTS接口。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { statfs } from '@kit.CoreFileKit';
```

## statfs.getFreeSize

PhonePC/2in1TabletTVWearable

getFreeSize(path:string): Promise<number>

异步方法获取指定文件系统空闲字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回空闲字节数。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let path = context.filesDir;
7. statfs.getFreeSize(path).then((number: number) => {
8. console.info("getFreeSize succeed, Size: " + number);
9. }).catch((err: BusinessError) => {
10. console.error("getFreeSize failed with error message: " + err.message + ", error code: " + err.code);
11. });
```

## statfs.getFreeSize

PhonePC/2in1TabletTVWearable

getFreeSize(path:string, callback:AsyncCallback<number>): void

异步方法获取指定文件系统空闲字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径。 |
| callback | AsyncCallback<number> | 是 | 异步获取空闲字节数之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let path = context.filesDir;
7. statfs.getFreeSize(path, (err: BusinessError, number: number) => {
8. if (err) {
9. console.error("getFreeSize failed with error message: " + err.message + ", error code: " + err.code);
10. } else {
11. console.info("getFreeSize succeed, Size: " + number);
12. }
13. });
```

## statfs.getFreeSizeSync10+

PhonePC/2in1TabletTVWearable

getFreeSizeSync(path:string): number

以同步方法获取指定文件系统空闲字节数。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回空闲字节数。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let path = context.filesDir;
6. let number = statfs.getFreeSizeSync(path);
7. console.info("getFreeSizeSync succeed, Size: " + number);
```

## statfs.getTotalSize

PhonePC/2in1TabletTVWearable

getTotalSize(path: string): Promise<number>

异步方法获取指定文件系统总字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回总字节数。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let path = context.filesDir;
7. statfs.getTotalSize(path).then((number: number) => {
8. console.info("getTotalSize succeed, Size: " + number);
9. }).catch((err: BusinessError) => {
10. console.error("getTotalSize failed with error message: " + err.message + ", error code: " + err.code);
11. });
```

## statfs.getTotalSize

PhonePC/2in1TabletTVWearable

getTotalSize(path: string, callback: AsyncCallback<number>): void

异步方法获取指定文件系统总字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径。 |
| callback | AsyncCallback<number> | 是 | 异步获取总字节数之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let path = context.filesDir;
7. statfs.getTotalSize(path, (err: BusinessError, number: number) => {
8. if (err) {
9. console.error("getTotalSize failed with error message: " + err.message + ", error code: " + err.code);
10. } else {
11. console.info("getTotalSize succeed, Size: " + number);
12. }
13. });
```

## statfs.getTotalSizeSync10+

PhonePC/2in1TabletTVWearable

getTotalSizeSync(path: string): number

以同步方法获取指定文件系统总字节数。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回总字节数。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let path = context.filesDir;
6. let number = statfs.getTotalSizeSync(path);
7. console.info("getTotalSizeSync succeed, Size: " + number);
```
