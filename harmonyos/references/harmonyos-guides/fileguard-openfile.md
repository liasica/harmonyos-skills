---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-openfile
title: 打开文件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 打开文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8240ad446bed3ee4cbceba17b4b1655f4e96b896426f6e09887cc6d428ce0ed5
---

## 场景介绍

普通应用无法直接访问公共路径下的文件，Enterprise Data Guard Kit为应用提供相关接口以获取文件描述符（fd）。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [openFile](../harmonyos-references/dataguard-fileguard.md#openfile)(path: string, callback: AsyncCallback<number>): void | 通过Callback方式打开指定路径下的文件，获取文件描述符（fd）。 |
| [openFile](../harmonyos-references/dataguard-fileguard.md#openfile-1)(path: string): Promise<number> | 使用Promise方式打开指定路径下的文件，获取文件描述符（fd）。 |
| [openFileWrite](../harmonyos-references/dataguard-fileguard.md#openfilewrite)(path: string, callback: AsyncCallback<number>): void | 在只写模式下，通过Callback方式打开用户个人数据目录下的文件，获取文件描述符（fd）。 |
| [openFileWrite](../harmonyos-references/dataguard-fileguard.md#openfilewrite-1)(path: string): Promise<number> | 在只写模式下，使用Promise方式打开用户个人数据目录下的文件，获取文件描述符（fd）。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[openFile](../harmonyos-references/dataguard-fileguard.md#openfile)，并且可选择以下一种方式打开文件，获取指定目录文件fd。

   * 通过回调函数方式，打开指定路径下的文件，获取文件fd。

     ```typescript
     const TAG: string = 'FileGuard_OpenFile';
     const DOMAIN: number = 0x0000;

     /**
      * 打开文件。使用callback异步回调。
      */
     function openFileCallback() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test/test1.txt';
       guard.openFile(path, (err: BusinessError, fd: number) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to open file. Code: ${err.code}, message: ${err.message}.`);
           return;
         }
         hilog.info(DOMAIN, TAG, `Succeeded in opening file. path: ${path}, fd: ${fd}.`);
       });
     }
     ```
   * 通过Promise方式，打开指定路径下的文件，获取文件fd。

     ```typescript
     const TAG: string = 'FileGuard_OpenFile';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 打开文件。使用Promise异步回调。
      */
     function openFilePromise() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test/test2.txt';
       guard.openFile(path).then((fd: number) => {
         hilog.info(DOMAIN, TAG, `Succeeded in opening file. path: ${path}, fd: ${fd}.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to open file. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
3. 只写模式下，打开用户个人数据目录下的文件，获取文件描述符。初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[openFileWrite](../harmonyos-references/dataguard-fileguard.md#openfilewrite)，并且可选择以下一种方式获取指定目录文件fd。

   * 通过回调函数方式，打开用户个人数据目录下的文件，获取文件fd。

     ```typescript
     const TAG: string = 'FileGuard_OpenFile';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 只写模式打开文件。使用callback异步回调。
      * @param accountId: 用户ID
      */
     function openFileWriteCallback(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
       guard.openFileWrite(path, (err: BusinessError, fd: number) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
           return;
         }
         hilog.info(DOMAIN, TAG, `Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
       });
     }
     ```
   * 通过Promise方式，打开用户个人数据目录下的文件，获取文件fd。

     ```typescript
     const TAG: string = 'FileGuard_OpenFile';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 只写模式打开文件。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     function openFileWritePromise(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
       guard.openFileWrite(path).then((fd: number) => {
         hilog.info(DOMAIN, TAG, `Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
