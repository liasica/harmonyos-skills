---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-tags
title: 设置文件属性标签
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置文件属性标签
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dba99dc7962d97e1496d4aa669672aa3c1abf3aeca4c789d8c049c732489ffcc
---

## 场景介绍

Enterprise Data Guard Kit为应用提供对文件设置属性标签的能力，方便应用对管控文件进行标识、分类。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [setFileTag](../harmonyos-references/dataguard-fileguard.md#setfiletag)(path: string, level: [SecurityLevel](../harmonyos-references/dataguard-fileguard.md#securitylevel), tag: string, callback: AsyncCallback<void>): void | 使用Callback方式设置文件属性标签。 |
| [setFileTag](../harmonyos-references/dataguard-fileguard.md#setfiletag-1)(path: string, level: [SecurityLevel](../harmonyos-references/dataguard-fileguard.md#securitylevel), tag: string): Promise<void> | 使用Promise方式设置文件属性标签。 |
| [setFileCustomTag](../harmonyos-references/dataguard-fileguard.md#setfilecustomtag)(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; | 使用Callback方式设置文件自定义属性标签。 |
| [setFileCustomTag](../harmonyos-references/dataguard-fileguard.md#setfilecustomtag-1)(path: string, tagList: Array<string>): Promise<void>; | 使用Promise方式设置文件自定义属性标签。 |
| [unsetFileCustomTag](../harmonyos-references/dataguard-fileguard.md#unsetfilecustomtag)(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; | 使用Callback方式取消设置文件自定义属性标签。 |
| [unsetFileCustomTag](../harmonyos-references/dataguard-fileguard.md#unsetfilecustomtag-1)(path: string, tagList: Array<string>): Promise<void>; | 使用Promise方式取消设置文件自定义属性标签。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口setFileTag或setFileCustomTag，设置文件属性标签，自定义属性标签可通过unsetFileCustomTag取消设置。

   * 通过回调函数方式，设置文件属性标签。

     ```
     1. function setFileTagCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test/test.txt';
     4. let tag: string = 'test';
     5. guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
     6. if (err) {
     7. console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
     8. return;
     9. }
     10. console.info(`Succeeded in setting file tag.`);
     11. });
     12. }
     ```
   * 通过Promise方式，设置文件属性标签。

     ```
     1. function setFileTagPromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let path: string = '/data/service/el2/test/test.txt';
     4. let tag: string = 'test';
     5. guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
     6. console.info(`Succeeded in setting file tag.`);
     7. }).catch((err: BusinessError) => {
     8. console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
     9. });
     10. }
     ```
