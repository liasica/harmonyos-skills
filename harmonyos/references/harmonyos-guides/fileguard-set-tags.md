---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-tags
title: 设置文件属性标签
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置文件属性标签
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e9efe920755ff40c004972007d538bb8ed9f8fa7972cbee1e68b694b4abe31e4
---

## 场景介绍

Enterprise Data Guard Kit为应用提供对文件设置属性标签的能力，方便应用对管控文件进行标识、分类。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [setFileTag](../harmonyos-references/dataguard-fileguard.md#setfiletag)(path: string, level: [SecurityLevel](../harmonyos-references/dataguard-fileguard.md#securitylevel), tag: string, callback: AsyncCallback<void>): void | 使用Callback方式设置文件属性标签。 |
| [setFileTag](../harmonyos-references/dataguard-fileguard.md#setfiletag-1)(path: string, level: [SecurityLevel](../harmonyos-references/dataguard-fileguard.md#securitylevel), tag: string): Promise<void> | 使用Promise方式设置文件属性标签。 |
| [setFileCustomTag](../harmonyos-references/dataguard-fileguard.md#setfilecustomtag)(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void | 使用Callback方式设置文件自定义属性标签。 |
| [setFileCustomTag](../harmonyos-references/dataguard-fileguard.md#setfilecustomtag-1)(path: string, tagList: Array<string>): Promise<void> | 使用Promise方式设置文件自定义属性标签。 |
| [unsetFileCustomTag](../harmonyos-references/dataguard-fileguard.md#unsetfilecustomtag)(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void | 使用Callback方式取消设置文件自定义属性标签。 |
| [unsetFileCustomTag](../harmonyos-references/dataguard-fileguard.md#unsetfilecustomtag-1)(path: string, tagList: Array<string>): Promise<void> | 使用Promise方式取消设置文件自定义属性标签。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[setFileTag](../harmonyos-references/dataguard-fileguard.md#setfiletag)，设置文件属性标签。

   * 通过回调函数方式，设置文件属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     /**
      * 设置文件属性标签。使用callback异步回调。
      */
     function setFileTagCallback() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test/test1.txt';
       let tag: string = 'test1';
       guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
           return;
         }
         hilog.info(DOMAIN, TAG, `Succeeded in setting file tag.`);
       });
     }
     ```
   * 通过Promise方式，设置文件属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 设置文件属性标签。使用Promise异步回调。
      */
     function setFileTagPromise() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test/test2.txt';
       let tag: string = 'test2';
       guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in setting file tag.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
3. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[setFileCustomTag](../harmonyos-references/dataguard-fileguard.md#setfilecustomtag)，设置文件自定义属性标签。

   * 通过回调函数方式，设置文件自定义属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 设置文件自定义属性标签。使用callback异步回调。
      * @param accountId: 用户ID
      */
     function setFileCustomTagCallback(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test1.txt`;
       let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
       guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
         } else {
           hilog.info(DOMAIN, TAG, `Succeeded in setting file custom tag.`);
         }
       });
     }
     ```
   * 通过Promise方式，设置文件自定义属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 设置文件自定义属性标签。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     function setFileCustomTagPromise(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test2.txt`;
       let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
       guard.setFileCustomTag(path, tagList).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in setting file custom tag.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
4. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[unsetFileCustomTag](../harmonyos-references/dataguard-fileguard.md#unsetfilecustomtag)，取消文件自定义属性标签。

   * 通过回调函数方式，取消文件自定义属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 取消文件自定义属性标签。使用callback异步回调。
      * @param accountId: 用户ID
      */
     function unsetFileCustomTagCallback(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test1.txt`;
       let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
       guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
         } else {
           hilog.info(DOMAIN, TAG, `Succeeded in unsetting file custom tag.`);
         }
       });
     }
     ```
   * 通过Promise方式，取消文件自定义属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 取消文件自定义属性标签。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     function unsetFileCustomTagPromise(accountId: number) {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test2.txt`;
       let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
       guard.unsetFileCustomTag(path, tagList).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in unsetting file custom tag.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
