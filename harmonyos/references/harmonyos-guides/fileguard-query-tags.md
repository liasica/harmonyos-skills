---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-query-tags
title: 获取文件属性标签
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 获取文件属性标签
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de8d4b4a449fb59b6068bebbe0e61a88375ce8975eaea2280ff8703b13eed0f4
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

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口queryFileTag，获取文件属性标签。

   * 通过回调函数方式，获取文件属性标签。

     ```
     1. function queryFileTagCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test/test.txt';
     4. guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
     5. if (err) {
     6. console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
     7. return;
     8. }
     9. console.info(`Succeeded in querying file tag.`);
     10. });
     11. }
     ```
   * 通过Promise方式，获取文件属性标签。

     ```
     1. function queryFileTagPromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test/test.txt';
     4. guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
     5. console.info(`Succeeded in querying file tag.`);
     6. }).catch((err: BusinessError) => {
     7. console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
     8. });
     9. }
     ```
