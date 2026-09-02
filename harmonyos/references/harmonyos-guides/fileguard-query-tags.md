---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-query-tags
title: 获取文件属性标签
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 获取文件属性标签
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:84680ab492d35085cde4d736706ef8756b56bb40450c8b6d1bd42d1fac88d105
---

## 场景介绍

Enterprise Data Guard Kit为应用提供获取文件属性标签的能力，HarmonyOS系统根据管控策略和文件属性标签对文件实行管控。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [queryFileTag](../harmonyos-references/dataguard-fileguard.md#queryfiletag)(path: string, callback: AsyncCallback<[FileTagInfo](../harmonyos-references/dataguard-fileguard.md#filetaginfo)>): void | 使用Callback方式获取文件属性标签。 |
| [queryFileTag](../harmonyos-references/dataguard-fileguard.md#queryfiletag-1)(path: string): Promise<[FileTagInfo](../harmonyos-references/dataguard-fileguard.md#filetaginfo)> | 使用Promise方式获取文件属性标签。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[queryFileTag](../harmonyos-references/dataguard-fileguard.md#queryfiletag)，获取文件属性标签。

   * 通过回调函数方式，获取文件属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 获取文件属性标签。使用callback异步回调。
      */
     function queryFileTagCallback() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test/test1.txt';
       guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
           return;
         }
         hilog.info(DOMAIN, TAG,
           `Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
       });
     }
     ```
   * 通过Promise方式，获取文件属性标签。

     ```typescript
     const TAG: string = 'FileGuard_FileTag';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 获取文件属性标签。使用Promise异步回调。
      */
     function queryFileTagPromise() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test/test2.txt';
       guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
         hilog.info(DOMAIN, TAG,
           `Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
