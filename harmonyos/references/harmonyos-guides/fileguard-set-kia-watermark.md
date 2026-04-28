---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-kia-watermark
title: 设置KIA文件水印图片
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置KIA文件水印图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7083abe58552783f3b64068a9ec20a016785e5990027c47289a27d9c46a23710
---

## 场景介绍

为应用提供设置KIA文件水印图片能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [setKiaWatermarkImage](../harmonyos-references/dataguard-fileguard.md#setkiawatermarkimage)(image: Uint8Array, info: string): Promise<void> | 使用Promise方式设置KIA文件水印图片。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[setKiaWatermarkImage](../harmonyos-references/dataguard-fileguard.md#setkiawatermarkimage)，设置KIA文件水印图片。

   ```
   1. async function testSetKiaWaterMarkImage() {
   2. try {
   3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   4. let imagePath: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.png';
   5. let fd: number = await guard.openFile(imagePath);
   6. let stat: fileIo.Stat = fileIo.statSync(fd);
   7. let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
   8. fileIo.readSync(fd, buffer);

   10. let image: Uint8Array = new Uint8Array(buffer);
   11. let info: string = new Date().toLocaleString();
   12. guard.setKiaWatermarkImage(image, info).then(() => {
   13. console.info(`Succeeded in setting the watermark image for Kia file.`);
   14. }).catch((err: BusinessError) => {
   15. console.error(`Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
   16. })
   17. } catch (e) {
   18. console.error(`[scanFileGuard] testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
   19. }
   20. }
   ```
