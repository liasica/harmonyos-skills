---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-start-task
title: 启动文件扫描任务
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 启动文件扫描任务
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:be37a5b6b17b4ff6df82a628c9e3f100e384b64f85e20f01f9040edf3748618b
---

## 场景介绍

Enterprise Data Guard Kit为应用提供公共路径和指定目录的扫描能力，获取对应目录下的文件列表。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [startFileScanTask](../harmonyos-references/dataguard-fileguard.md#startfilescantask)(type: [CommonDirScanType](../harmonyos-references/dataguard-fileguard.md#commondirscantype), callback: [ScanFileCallback](../harmonyos-references/dataguard-fileguard.md#scanfilecallback), batchNum?: number): void | 通过Callback的方式，扫描公共目录并返回结果。 |
| [startFileScanTask](../harmonyos-references/dataguard-fileguard.md#startfilescantask-1)(path: string, callback: [ScanFileCallback](../harmonyos-references/dataguard-fileguard.md#scanfilecallback), batchNum?: number): void | 通过Callback的方式，扫描指定目录并返回结果。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，并且声明扫描结果回调函数。

   * 按照文件类型扫描公共空间文件，查看打印结果。

     ```typescript
     const TAG: string = 'FileGuard_Scan';
     const DOMAIN: number = 0x0000;

     /**
      * 启动公共目录文件扫描任务
      */
     function startFileScanTaskUnderCommonDir() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
         files.forEach((value: string) => {
           hilog.info(DOMAIN, TAG, `Succeeded in getting file: ${value}.`);
         })
       };
       let onCompleteScanTask: (count: number) => void = (count: number) => {
         hilog.info(DOMAIN, TAG, `Succeeded in getting count: ${count}.`);
       };
       let scanFileCallback: fileGuard.ScanFileCallback = {
         onReceiveFileList: onReceiveFileList,
         onTaskCompleted: onCompleteScanTask
       };
       guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
     }
     ```
   * 扫描公共空间指定路径下的文件，查看打印结果。

     ```typescript
     const TAG: string = 'FileGuard_Scan';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 启动指定目录文件扫描任务
      */
     function startFileScanTaskUnderSpecifiedDir() {
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let path: string = '/data/service/el2/test';
       let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
         files.forEach((value: string) => {
           hilog.info(DOMAIN, TAG, `Succeeded in getting file: ${value}.`);
         })
       };
       let onCompleteScanTask: (count: number) => void = (count: number) => {
         hilog.info(DOMAIN, TAG, `Succeeded in getting count: ${count}.`);
       };
       let scanFileCallback: fileGuard.ScanFileCallback = {
         onReceiveFileList: onReceiveFileList,
         onTaskCompleted: onCompleteScanTask
       };
       guard.startFileScanTask(path, scanFileCallback);
     }
     ```
