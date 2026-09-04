---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost-stateawareness
title: 文件打开加速状态感知（已废弃）
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 文件打开加速状态感知（已废弃）
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:17+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:0680fbaf138e2035b803c4860be3c4afdd7dccfa24cc41e8751d3483120d7a6a
---

从5.0.5(17)版本开始，如浏览器等支持下载文件的应用，可以接入文件预加载状态感知接口，动态感知文件预加载状态，通过UI（user interface）标识对加速文件进行显性化提示，进一步提升用户体验。

从26.0.0版本开始，文件打开加速状态感知能力已废弃。

## 接口说明

具体API说明详见[预加载状态感知接口文档](../harmonyos-references/preview-arkts-openfileboost-api.md)。

**表1** 文件预加载状态感知接口介绍（ArkTS API）

| 接口名 | 描述 |
| --- | --- |
| on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void | 文件预加载状态回调，应用通过注册回调函数获取文件预加载的状态变化。 |
| off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void | 文件预加载状态注销回调，通过注销回调函数取消获取文件预加载的状态变化。 |
| addFile(file: string): void | 监听一个文件的预加载状态，传入文件路径开始监听该文件的预加载状态。后续该文件状态有变化通过'filePreloadStateChanged'事件回调应用。  注意需要先调用openFileBoost.on('filePreloadStateChanged')接口后再调用该接口添加文件。  当前支持加速的文件类型见[文件打开加速支持的文件类型](preview-introduction.md#文件打开加速支持的文件类型)， 不支持的文件类型默认为未预加载状态，不需要调用该接口监听文件预加载状态变更。 |
| removeFile(file: string): void | 取消监听一个文件的预加载状态，取消后文件的预加载状态变化不会通过回调再通知业务。 |
| queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo | 查询文件预加载状态，传入文件路径，通过返回值返回该文件当前的预加载状态。 |

## 约束限制

支持的设备类型：PC/2in1，从26.0.0版本开始，新增支持tablet设备。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { openFileBoost } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 注册文件预加载状态感知回调函数。

   ```typescript
   // 文件预加载状态变更的回调函数定义，若有文件预加载状态变更，则通过该回调函数通知
   function callback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
     if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADING) {
       // 预加载过程中，应用可以根据自己设计对应UX
       console.info(`file is PRELOADING, suggest to show loading animation`);
     }
     if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADED) {
       // 预加载完成，应用可以通过UX显示提示用户加速完成
       console.info(`file is PRELOADED, suggest to show loaded animation`);
     }
     if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.NOT_PRELOADED) {
       // 没有预加载，应用可以不显示任何额外UX
       console.info(`file is UNPRELOADED, suggest do not show animation `);
     }
   }
   // 注册预加载状态感知回调
   openFileBoost.on('filePreloadStateChanged', callback);
   ```
3. 调用addFile接口传入想要监听的文件的沙箱路径。典型场景比如应用下载某个文件完成，可将该文件路径注册进来，若文件后续状态变更，系统会通过2中的回调函数通知应用。

   ```typescript
   // 为10MB_file.docx文件添加文件预加载状态监听
   const file: string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
   openFileBoost.addFile(file);
   ```
4. 通过addFile接口监听的文件个数有上限（50个文件），不再需要监听的文件可以通过removeFile接口取消监听。

   ```typescript
   const file: string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
   openFileBoost.removeFile(file);
   ```
5. 如果不需要再监听任何文件的预加载状态变更，可注销预加载状态感知回调函数。如果传入具体的回调函数，则只取消该函数； 如果不传入具体的回调函数，则取消该进程的所有回调。

   ```typescript
   // 假设之前在进程的不同业务逻辑中已经注册了callback1、callback2、callback3总共3个回调函数
   openFileBoost.on('filePreloadStateChanged', callback1);
   openFileBoost.on('filePreloadStateChanged', callback2);
   openFileBoost.on('filePreloadStateChanged', callback3);

   // 单独取消callback1的监听，传入callback1作为参数，后续不会再调用callback1的回调做通知
   openFileBoost.off('filePreloadStateChanged', callback1);
   // 取消所有callback的监听，不传第二个可选参数，后续不会再调用callback2和callback3做通知
   openFileBoost.off('filePreloadStateChanged');
   ```
6. 应用还可通过查询接口查询某个文件的实时的预加载状态，一般在应用刚启动时可以查询一遍相关文件的预加载状态。每次调用接口传入一个文件的沙箱路径。

   ```typescript
   const file: string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
   let statusInfo: openFileBoost.FilePreloadStatusInfo = openFileBoost.queryFilePreloadStatusInfo(file);
   console.info('file, %{public}s, progress:%{public}d  preloadState:%{public}d',
     statusInfo.sandboxPath, statusInfo.progress, statusInfo.state);
   ```
