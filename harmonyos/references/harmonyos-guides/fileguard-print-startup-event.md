---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-print-startup-event
title: 订阅或取消订阅打印服务启动事件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 订阅或取消订阅打印服务启动事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d68752aa5a87d4ec98560d335919d808bcb89fde92fa842811f8ff3e8e653943
---

从6.1.1(24)版本开始，新增订阅或取消订阅打印服务启动事件接口，帮助用户获取打印服务启动时机，便于及时注册水印回调，从而启用打印水印功能。

## 场景介绍

应用需注册打印服务提供的水印注册函数以实现打印水印功能。由于打印服务并非常驻进程，应用可通过监听提供的onPrintStartup回调函数，获取打印服务启动的时机；在接收到回调后，即可向打印服务[注册水印回调](../harmonyos-references/js-apis-print.md#printregisterwatermarkcallback24)，从而完成水印功能的启用。同时，调用[onPrintStartup](../harmonyos-references/dataguard-fileguard.md#onprintstartup)回调本身也作为打印水印功能的使能标志，调用[offPrintStartup](../harmonyos-references/dataguard-fileguard.md#offprintstartup)则会关闭打印水印功能。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [onPrintStartup](../harmonyos-references/dataguard-fileguard.md#onprintstartup)(callback: Callback<void>): void | 订阅打印服务启动事件。 |
| [offPrintStartup](../harmonyos-references/dataguard-fileguard.md#offprintstartup)(callback?: Callback<void>): void | 取消订阅打印服务启动事件。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { print } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { pdfService } from '@kit.PDFKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[onPrintStartup](../harmonyos-references/dataguard-fileguard.md#onprintstartup)，订阅打印服务启动事件。

   ```typescript
   const TAG: string = 'FileGuard_PrintStartUp';
   const DOMAIN: number = 0x0000;

   /**
    * 订阅打印服务启动事件
    * 打印服务启动时触发回调，用于注册水印回调
    */
   function testOnPrintStartup() {
     try {
       hilog.info(DOMAIN, TAG, `onPrintStartup start.`);
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       guard.onPrintStartup(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in listening print-startup.`);
         registerWatermark();
       });
     } catch (err) {
       hilog.error(DOMAIN, TAG, `Failed to listen print-startup. Code: ${err.code}, message: ${err.message}.`);
     }
   }

   function registerWatermark() {
     try {
       print.registerWatermarkCallback(watermarkCallback);
       hilog.info(DOMAIN, TAG, `Succeeded in registering Watermark.`);
     } catch (err) {
       hilog.error(DOMAIN, TAG, `Failed to register Watermark. Code: ${err.code}, message: ${err.message}.`);
     }
   }

   let watermarkCallback: print.WatermarkCallback = (jobId: string, fd: number) => {
     hilog.info(DOMAIN, TAG, `Watermark triggered. jobId=${jobId}, fd=${fd}`);
     const tempDir: string = AppStorage.get('tempDir') as string;
     const tempPath: string = `${tempDir}/watermark_${jobId}.pdf`;
     const outPath: string = `${tempDir}/watermark_${jobId}_out.pdf`;
     hilog.info(DOMAIN, TAG, `Watermark tempDir: ${tempDir}, tempPath: ${tempPath}, outPath: ${outPath}.`);

     try {
       // Copy file to sandbox: fd passed by print service is only valid for this operation.
       // PDF library requires file path to load document, cannot operate fd directly.
       const destFd = fileIo.openSync(tempPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
       fileIo.copyFileSync(fd, destFd.fd);
       // Release file handle: close immediately after copy to avoid handle leak
       fileIo.closeSync(destFd);

       const pdfDoc = new pdfService.PdfDocument();
       if (pdfDoc.loadDocument(tempPath) !== pdfService.ParseResult.PARSE_SUCCESS) {
         throw new Error('PDF parse failed');
       }

       const watermarkInfo = new pdfService.TextWatermarkInfo();
       watermarkInfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
       watermarkInfo.content = 'WATERMARK';
       watermarkInfo.textSize = 48;
       watermarkInfo.opacity = 0.3;
       watermarkInfo.rotation = -45;
       watermarkInfo.isOnTop = true;
       watermarkInfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_VCENTER;
       watermarkInfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_VCENTER;

       pdfDoc.addWatermark(watermarkInfo, 0, pdfDoc.getPageCount() - 1, true, true);
       pdfDoc.saveDocument(outPath);

       // Read processed file and write back to fd: open as read-only, copy content to original fd.
       // fd no longer needed after this, print service will read the processed file content.
       const srcFd = fileIo.openSync(outPath, fileIo.OpenMode.READ_ONLY);
       fileIo.copyFileSync(srcFd.fd, fd);
       // Release file handle: close source file handle after read completes
       fileIo.closeSync(srcFd);

       // Cleanup temp files: print service has finished reading, delete to free storage
       fileIo.unlinkSync(tempPath);
       fileIo.unlinkSync(outPath);

       print.notifyWatermarkComplete(jobId, print.WatermarkHandleResult.WATERMARK_HANDLE_SUCCESS);
       hilog.info(DOMAIN, TAG, `Watermark success. jobId=${jobId}`);
     } catch (err) {
       hilog.error(DOMAIN, TAG, `Watermark failed. jobId=${jobId},  Code: ${err.code}, message: ${err.message}.`);
       print.notifyWatermarkComplete(jobId, print.WatermarkHandleResult.WATERMARK_HANDLE_FAILURE);
     } finally {
       // Important: close fd after callback to avoid handle leak.
       fileIo.close(fd);
     }
   }
   ```
3. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[offPrintStartup](../harmonyos-references/dataguard-fileguard.md#offprintstartup)，取消订阅打印服务启动事件。

   ```typescript
   const TAG: string = 'FileGuard_PrintStartUp';
   const DOMAIN: number = 0x0000;

   // ...
   /**
    * 取消订阅打印服务启动事件
    */
   function testOffPrintStartup() {
     try {
       hilog.info(DOMAIN, TAG, `offPrintStartup start.`);
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       guard.offPrintStartup(() => {
         unregisterWatermark();
       });
     } catch (e) {
       hilog.error(DOMAIN, TAG, `Failed to cancel listen print-startup.`);
     }
   }

   function unregisterWatermark() {
     try {
       print.unregisterWatermarkCallback();
       hilog.info(DOMAIN, TAG, `Succeeded in unregistering Watermark.`);
     } catch (err) {
       hilog.error(DOMAIN, TAG, `Failed to unregister Watermark. Code: ${err.code}, message: ${err.message}.`);
     }
   }
   ```
