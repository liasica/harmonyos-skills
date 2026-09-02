---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-get-file-url
title: 获取文件URI
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 获取文件URI
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5d00728c71be397cda73d3ae961505d3f5f56b395ceaddf26c8966914d6abc2e
---

## 场景介绍

Enterprise Data Guard Kit为应用提供获取[用户个人数据目录](dataguard-introduction.md#访问限制)下文件路径信息的能力，该路径可被应用直接打开，从而辅助判断是否是KIA文件。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [getFileUri](../harmonyos-references/dataguard-fileguard.md#getfileuri)(path: string, callback: AsyncCallback<[FilePathInfo](../harmonyos-references/dataguard-fileguard.md#filepathinfo)>): void | 使用Callback方式获取文件路径信息。 |
| [getFileUri](../harmonyos-references/dataguard-fileguard.md#getfileuri-1)(path: string): Promise<[FilePathInfo](../harmonyos-references/dataguard-fileguard.md#filepathinfo)> | 使用Promise方式获取文件路径信息。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[getFileUri](../harmonyos-references/dataguard-fileguard.md#getfileuri)，获取文件URI。

   * 通过回调函数方式，获取文件URI。

     ```typescript
     const TAG: string = 'FileGuard_FileUri';
     const DOMAIN: number = 0x0000;

     /**
      * 获取文件URI。使用callback异步回调。
      * @param accountId: 用户ID
      */
     function getFileUriCallBack(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
       guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
         } else {
           hilog.info(DOMAIN, TAG, `Succeeded in getting file uri. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
         }
       });
     }
     ```
   * 通过Promise方式，获取文件URI。

     ```typescript
     const TAG: string = 'FileGuard_FileUri';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 获取文件URI。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     function getFileUriPromise(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/bbb.txt`;
       guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
         hilog.info(DOMAIN, TAG,
           `Succeeded in getting the uri of file. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to get the uri of file. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
