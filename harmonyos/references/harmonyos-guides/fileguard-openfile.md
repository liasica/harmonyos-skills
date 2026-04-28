---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-openfile
title: 打开文件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 打开文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:365a02e20ba621616123a259cf5507ed179c3055898e2fd16fcd2e82ae8576bf
---

## 场景介绍

普通应用无法直接访问公共路径下的文件，Enterprise Data Guard Kit为应用提供相关接口以获取文件描述符（fd）。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [openFile](../harmonyos-references/dataguard-fileguard.md#openfile)(path: string, callback: AsyncCallback<number>): void | 通过Callback方式获取指定路径下文件的文件描述符（fd）。 |
| [openFile](../harmonyos-references/dataguard-fileguard.md#openfile-1)(path: string): Promise<number> | 使用Promise方式获取指定路径下文件的文件描述符（fd）。 |
| [openFileWrite](../harmonyos-references/dataguard-fileguard.md#openfilewrite)(path: string, callback: AsyncCallback<number>): void | 在只写模式下，通过Callback方式获取指定路径下文件的文件描述符（fd）。 |
| [openFileWrite](../harmonyos-references/dataguard-fileguard.md#openfilewrite-1)(path: string): Promise<number> | 在只写模式下，使用Promise方式获取指定路径下文件的文件描述符（fd）。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口openFile或者openFileWrite，并且可选择以下一种方式获取指定目录文件fd。

   * 通过回调函数方式，获取文件fd。

     ```
     1. function openFileCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test/test.txt';
     4. guard.openFile(path, (err: BusinessError, fd: number) => {
     5. if (err) {
     6. console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
     7. return;
     8. }
     9. console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
     10. });
     11. }
     ```
   * 通过Promise方式，获取文件fd。

     ```
     1. function openFilePromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test/test.txt';
     4. guard.openFile(path).then((fd: number) => {
     5. console.info(`Succeeded in opening file. path: ${path} , fd: ${fd}.`);
     6. }).catch((err: BusinessError) => {
     7. console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
     8. });
     9. }
     ```
