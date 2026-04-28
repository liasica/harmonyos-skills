---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-file-list
title: 设置KIA文件列表
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置KIA文件列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb0c34265ab8b0e3d96a2d6d1ace9e7687d846ac99678f9a7eb672fa0d0a495a
---

## 场景介绍

Enterprise Data Guard Kit为应用提供设置KIA文件列表的能力，HarmonyOS系统根据管控策略对KIA文件列表中的文件实行管控。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [setKiaFilelist](../harmonyos-references/dataguard-fileguard.md#setkiafilelist)(filelist: string, callback: AsyncCallback<void>): void | 使用Callback方式设置KIA文件列表。 |
| [setKiaFilelist](../harmonyos-references/dataguard-fileguard.md#setkiafilelist-1)(filelist: string): Promise<void> | 使用Promise方式设置KIA文件列表。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，将KIA文件列表对象转为字符串，调用接口setKiaFilelist，设置KIA文件列表。

   * 通过回调函数方式，设置KIA文件列表。

     ```
     1. function setKiaFilelistCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let fileListStr: string =
     4. '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
     5. '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
     6. '"kia_keyword":["key1","key2","key3"],' +
     7. '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
     8. '"compress_suffix":[".rar", ".zip"],' +
     9. '"kia_update_type":0}';
     10. guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
     11. if (err) {
     12. console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
     13. } else {
     14. console.info(`Succeeded in setting the list of KIA file.`);
     15. }
     16. });
     17. }
     ```
   * 通过Promise方式，设置KIA文件列表。

     ```
     1. function setKiaFilelistPromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let fileListStr: string =
     4. '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
     5. '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
     6. '"kia_keyword":["key1","key2","key3"],' +
     7. '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
     8. '"compress_suffix":[".rar", ".zip"],' +
     9. '"kia_update_type":0}';
     10. guard.setKiaFilelist(fileListStr).then(() => {
     11. console.info(`Succeeded in setting the list of KIA file.`);
     12. }).catch((err: BusinessError) => {
     13. console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
     14. });
     15. }
     ```
