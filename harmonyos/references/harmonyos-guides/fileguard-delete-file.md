---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-delete-file
title: 删除指定路径下的文件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 删除指定路径下的文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2e3e96e6c819fa542462e2e7335819c25a20180bb3f99766cdb5b741c7971916
---

## 场景介绍

Enterprise Data Guard Kit为应用提供对[用户个人数据目录](dataguard-introduction.md#访问限制)下指定路径文件的删除能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [deleteFile](../harmonyos-references/dataguard-fileguard.md#deletefile)(path: string, callback: AsyncCallback<void>): void | 使用Callback方式删除指定路径下的文件。 |
| [deleteFile](../harmonyos-references/dataguard-fileguard.md#deletefile-1)(path: string): Promise<void> | 使用Promise方式删除指定路径下的文件。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[deleteFile](../harmonyos-references/dataguard-fileguard.md#deletefile)，删除指定路径下的文件。

   * 通过回调函数方式，删除指定路径下的文件。

     ```typescript
     const TAG: string = 'FileGuard_DeleteFile';
     const DOMAIN: number = 0x0000;

     /**
      * 删除指定路径下的文件。使用callback异步回调。
      * @param accountId: 用户ID
      */
     function deleteFileCallback(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/ccc.txt`;
       guard.deleteFile(path, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
         } else {
           hilog.info(DOMAIN, TAG, `Succeeded in deleting file.`);
         }
       });
     }
     ```
   * 通过Promise方式，删除指定路径下的文件。

     ```typescript
     const TAG: string = 'FileGuard_DeleteFile';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 删除指定路径下的文件。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     function deleteFilePromise(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/ddd.txt`;
       guard.deleteFile(path).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in deleting file.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
