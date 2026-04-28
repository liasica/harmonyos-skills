---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statfs
title: @ohos.statfs (statfs)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > 已停止维护的接口 > @ohos.statfs (statfs)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:53ebc2c404a91ab46af6510c25c59c0d4d88657b6d044a7f94f6f536da2b83cb
---

该模块提供文件系统相关存储信息的功能，向应用程序提供获取文件系统总字节数、空闲字节数的ArkTS接口。

说明

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块从API version 9开始废弃，建议使用[@ohos.file.statvfs](js-apis-file-statvfs.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import statfs from '@ohos.statfs';
```

## Statfs.getFreeBytes

PhonePC/2in1TabletTVWearable

getFreeBytes(path:string):Promise<number>

异步方法获取指定文件系统空闲字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回空闲字节数 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let path = "/dev";
3. statfs.getFreeBytes(path).then((number: number) => {
4. console.info("getFreeBytes promise successfully:" + number);
5. }).catch((err: BusinessError) => {
6. console.error("getFreeBytes failed with error:" + JSON.stringify(err));
7. });
```

## Statfs.getFreeBytes

PhonePC/2in1TabletTVWearable

getFreeBytes(path:string, callback:AsyncCallback<number>): void

异步方法获取指定文件系统空闲字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 |
| callback | AsyncCallback<number> | 是 | 异步获取空闲字节数之后的回调 |

**示例：**

```
1. import common from '@ohos.app.ability.common';
2. import { BusinessError } from '@ohos.base';
3. let context = getContext(this) as common.UIAbilityContext;
4. let path = context.filesDir;
5. statfs.getFreeBytes(path, (err: BusinessError, freeBytes:Number) => {
6. if (err) {
7. console.error('getFreeBytes callback failed');
8. } else {
9. console.info('getFreeBytes callback success' + freeBytes);
10. }
11. });
```

## Statfs.getTotalBytes

PhonePC/2in1TabletTVWearable

getTotalBytes(path: string): Promise<number>

异步方法获取指定文件系统总字节数，以Promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回总字节数 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let path = "/dev";
3. statfs.getTotalBytes(path).then((number: number) => {
4. console.info("getTotalBytes promise successfully:" + number);
5. }).catch((err: BusinessError) => {
6. console.error("getTotalBytes failed with error:" + JSON.stringify(err));
7. });
```

## Statfs.getTotalBytes

PhonePC/2in1TabletTVWearable

getTotalBytes(path: string, callback: AsyncCallback<number>): void

异步方法获取指定文件系统总字节数，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 |
| callback | AsyncCallback<number> | 是 | 异步获取总字节数之后的回调 |

**示例：**

```
1. import common from '@ohos.app.ability.common';
2. import { BusinessError } from '@ohos.base';
3. let context = getContext(this) as common.UIAbilityContext;
4. let path = context.filesDir;
5. statfs.getTotalBytes(path, (err: BusinessError, totalBytes:Number) => {
6. if (err) {
7. console.error('getTotalBytes callback failed');
8. } else {
9. console.info('getTotalBytes callback success' + totalBytes);
10. }
11. });
```
