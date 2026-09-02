---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-file-list
title: 设置KIA文件列表
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置KIA文件列表
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0d09770aaae6a07815682237262dfebcc7a672391fc05fd3b4a798f9ab990a10
---

## 场景介绍

Enterprise Data Guard Kit为应用提供设置KIA文件列表的能力，HarmonyOS系统根据管控策略对KIA文件列表中的文件实行管控。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [setKiaFilelist](../harmonyos-references/dataguard-fileguard.md#setkiafilelist)(filelist: string, callback: AsyncCallback<void>): void | 使用Callback方式设置KIA文件列表。 |
| [setKiaFilelist](../harmonyos-references/dataguard-fileguard.md#setkiafilelist-1)(filelist: string): Promise<void> | 使用Promise方式设置KIA文件列表。 |
| [isKia](../harmonyos-references/dataguard-fileguard.md#iskia)(path: string): boolean | 检查文件或文件夹是否是KIA。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，将KIA文件列表对象转为字符串，调用接口[setKiaFilelist](../harmonyos-references/dataguard-fileguard.md#setkiafilelist)，设置KIA文件列表。

   * 通过回调函数方式，设置KIA文件列表。

     ```typescript
     const TAG: string = 'FileGuard_KIAFileList';
     const DOMAIN: number = 0x0000;

     /**
      * 设置KIA文件列表。使用callback异步回调。
      * @param accountId: 用户ID
      */
     function setKiaFilelistCallback(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let fileListStr: string =
         `{"kia_filelist":["/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/3.txt",` +
           `"/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/4.txt"],` +
           `"kia_keyword":["key1","key2","key3"],` +
           `"kia_suffix":[".java", ".html", ".cpp", ".docx"],` +
           `"compress_suffix":[".rar", ".zip"],` +
           `"user_id":${accountId},` +
           `"kia_update_type":1}`;
       guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
         } else {
           hilog.info(DOMAIN, TAG, `Succeeded in setting the list of KIA file.`);
         }
       });
     }
     ```
   * 通过Promise方式，设置KIA文件列表。

     ```typescript
     const TAG: string = 'FileGuard_KIAFileList';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 设置KIA文件列表。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     function setKiaFilelistPromise(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let fileListStr: string =
         `{"kia_filelist":["/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/1.txt",` +
           `"/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/2.txt"],` +
           `"kia_keyword":["key1","key2","key3"],` +
           `"kia_suffix":[".java", ".html"],` +
           `"compress_suffix":[".rar"],` +
           `"user_id":${accountId},` +
           `"kia_update_type":0}`;
       guard.setKiaFilelist(fileListStr).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in setting the list of KIA file.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
3. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[isKia](../harmonyos-references/dataguard-fileguard.md#iskia)，检查该文件或文件夹是否是KIA。

   ```typescript
   const TAG: string = 'FileGuard_KIAFileList';
   const DOMAIN: number = 0x0000;

   // ...
   /**
    * 是否KIA文件
    * @param accountId: 用户ID
    */
   function isKia(accountId: number) {
     try {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/1.txt`;
       let isKiaResult: boolean = guard.isKia(path);
       hilog.info(DOMAIN, TAG, `Succeeded in determining whether the file is a KIA file. isKia: ${isKiaResult}`);
     } catch (e) {
       hilog.error(DOMAIN, TAG,
         `Failed to determine whether the file is a KIA file. Code: ${e.code}, message: ${e.message}.`);
     }
   }
   ```
