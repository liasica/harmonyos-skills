---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-kia-watermark
title: 设置KIA文件水印图片
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置KIA文件水印图片
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:cc0647ff7c92e1575ad999747459bbcddb7a9a43109fcd0ff90d31fa70e0cd5b
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

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[setKiaWatermarkImage](../harmonyos-references/dataguard-fileguard.md#setkiawatermarkimage)，设置KIA文件水印图片。

   ```typescript
   const TAG: string = 'FileGuard_KIAWatermarkImage';
   const DOMAIN: number = 0x0000;

   /**
    * 设置KIA文件水印图片。使用Promise异步回调。
    */
   async function testSetKiaWaterMarkImage() {
     let fd: number = -1;
     try {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let imagePath: string = `/data/service/el2/test_water.png`;
       fd = await guard.openFile(imagePath);
       let stat: fileIo.Stat = fileIo.statSync(fd);
       let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
       fileIo.readSync(fd, buffer);

       let image: Uint8Array = new Uint8Array(buffer);
       let info: string = new Date().toLocaleString();
       guard.setKiaWatermarkImage(image, info).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in setting the watermark image for Kia file.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG,
           `Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
       })
     } catch (e) {
       hilog.error(DOMAIN, TAG, `testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
     } finally {
       if (fd !== -1) {
         fileIo.close(fd);
       }
     }
   }
   ```
