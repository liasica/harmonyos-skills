---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost-stateawareness
title: 文件打开加速状态感知
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 文件打开加速状态感知
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:918b1328777ad6279c1ae77fce518d6bcfc459b3a4338ce0df1f7b2896c6b400
---

从5.0.5(17)版本开始，如浏览器等支持下载文件的应用，可以接入文件预加载状态感知接口，动态感知文件预加载状态，通过UI（user interface）标识对加速文件进行显性化提示，进一步提升用户体验。

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

## 开发准备

需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.PCService.OpenFileBoost系统能力，当前仅在2in1设备上支持该能力。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { openFileBoost } from '@kit.PreviewKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 注册文件预加载状态感知回调函数。

   ```
   1. // 文件预加载状态变更的回调函数定义，若有文件预加载状态变更，则通过该回调函数通知
   2. function callback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
   3. if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADING) {
   4. // 预加载过程中，应用可以根据自己设计对应UX
   5. hilog.info(0x0000, 'testTag', `file is PRELOADING, suggest to show loading animation`);
   6. }
   7. if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADED) {
   8. // 预加载完成，应用可以通过UX显示提示用户加速完成
   9. hilog.info(0x0000, 'testTag', `file is PRELOADED, suggest to show loaded animation`);
   10. }
   11. if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.NOT_PRELOADED) {
   12. // 没有预加载，应用可以不显示任何额外UX
   13. hilog.info(0x0000, 'testTag', `file is UNPRELOADED, suggest do not show animation `);
   14. }
   15. }
   16. // 调用register函数可以注册预加载状态感知回调
   17. function register(): void {
   18. try {
   19. openFileBoost.on('filePreloadStateChanged', callback);
   20. } catch(error) {
   21. let code = (error as BusinessError).code;
   22. let message = (error as BusinessError).message;
   23. hilog.error(0x0000, 'testTag', `register filePreloadStateChanged failed, error code: ${code}, message: ${message}.`);
   24. }
   25. }
   ```
3. 调用addFile接口传入想要监听的文件的沙箱路径。典型场景比如应用下载某个文件完成，可将该文件路径注册进来，若文件后续状态变更，系统会通过2中的回调函数通知应用。

   ```
   1. // 为10MB_file.docx文件添加文件预加载状态监听
   2. function testAddFile(): void {
   3. try {
   4. const file:string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
   5. openFileBoost.addFile(file);
   6. } catch(error) {
   7. let code = (error as BusinessError).code;
   8. let message = (error as BusinessError).message;
   9. hilog.error(0x0000, 'testTag', `addFile failed, error code: ${code}, message: ${message}.`);
   10. }
   11. }
   ```
4. 通过addFile接口监听的文件个数有上限（50个文件），不再需要监听的文件可以通过removeFile接口取消监听。

   ```
   1. const file:string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
   2. try {
   3. openFileBoost.removeFile(file);
   4. } catch(error) {
   5. let code = (error as BusinessError).code;
   6. let message = (error as BusinessError).message;
   7. hilog.error(0x0000, 'testTag', `removeFile failed, error code: ${code}, message: ${message}.`);
   8. }
   ```
5. 如果不需要再监听任何文件的预加载状态变更，可注销预加载状态感知回调函数。如果传入具体的回调函数，则只取消该函数； 如果不传入具体的回调函数，则取消该进程的所有回调。

   ```
   1. // 假设之前在进程的不同业务逻辑中已经注册了callback1、callback2、callback3总共3个回调函数
   2. openFileBoost.on('filePreloadStateChanged', callback1);
   3. openFileBoost.on('filePreloadStateChanged', callback2);
   4. openFileBoost.on('filePreloadStateChanged', callback3);

   6. function testUnregister(): void {
   7. try {
   8. // 单独取消callback1的监听，传入callback1作为参数，后续不会再调用callback1的回调做通知
   9. openFileBoost.off('filePreloadStateChanged', callback1);
   10. // 取消所有callback的监听，不传第二个可选参数，后续不会再调用callback2和callback3做通知
   11. openFileBoost.off('filePreloadStateChanged');
   12. } catch(error) {
   13. let code = (error as BusinessError).code;
   14. let message = (error as BusinessError).message;
   15. hilog.error(0x0000, 'testTag', `off filePreloadStateChanged failed, error code: ${code}, message: ${message}.`);
   16. }
   17. }
   ```
6. 应用还可通过查询接口查询某个文件的实时的预加载状态，一般在应用刚启动时可以查询一遍相关文件的预加载状态。每次调用接口传入一个文件的沙箱路径。

   ```
   1. function testQuery(): void {
   2. try {
   3. const file:string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
   4. let statusInfo : openFileBoost.FilePreloadStatusInfo = openFileBoost.queryFilePreloadStatusInfo(file);
   5. hilog.info(0x0000, 'testTag', 'file, %{public}s, progress:%{public}d  preloadState:%{public}d',
   6. statusInfo.sandboxPath, statusInfo.progress, statusInfo.state);
   7. } catch(error) {
   8. let code = (error as BusinessError).code;
   9. let message = (error as BusinessError).message;
   10. hilog.error(0x0000, 'testTag', `query failed, error code: ${code}, message: ${message}.`);
   11. }
   12. }
   ```
