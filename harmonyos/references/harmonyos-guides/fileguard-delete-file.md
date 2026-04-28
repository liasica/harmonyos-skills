---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-delete-file
title: 删除指定路径下的文件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 删除指定路径下的文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb79fa894ed1590c759d1cccd7781cb7ca1e0d727df6c4bde051ea0fa3697182
---

## 场景介绍

Enterprise Data Guard Kit为应用提供对指定路径下文件的删除能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [deleteFile](../harmonyos-references/dataguard-fileguard.md#deletefile)(path: string, callback: AsyncCallback<void>): void | 使用Callback方式删除指定路径下的文件。 |
| [deleteFile](../harmonyos-references/dataguard-fileguard.md#deletefile-1)(path: string): Promise<void> | 使用Promise方式删除指定路径下的文件。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口deleteFile，删除扫描范围内的文件。

   * 通过回调函数方式，删除扫描范围内的文件。

     ```
     1. function deleteFileCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
     4. guard.deleteFile(path, (err: BusinessError) => {
     5. if (err) {
     6. console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
     7. } else {
     8. console.info(`Succeeded in deleting file.`);
     9. }
     10. });
     11. }
     ```
   * 通过Promise方式，删除扫描范围内的文件。

     ```
     1. function deleteFilePromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
     4. guard.deleteFile(path).then(() => {
     5. console.info(`Succeeded in deleting file.`);
     6. }).catch((err: BusinessError) => {
     7. console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
     8. });
     9. }
     ```
