---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-filepreview
title: 文件预览
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 文件预览
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:051b7ada98392cca0db5b12a508c3183fc20ae5cd1d8bea548c22343970edd31
---

当前Preview Kit的文件预览能力采用拉起新窗口的方式来实现，在新的窗口中展示需要预览的文件，并按照统一设计的界面进行展示，如果开发者需要使用Preview Kit的文件预览能力，需要注意以下事项：

* 当前Preview Kit仅支持跳出应用进行文件的预览，暂不支持应用内预览。
* Office类型文档预览借助WPS提供的能力来实现，在预览文档类型文件时会存在“WPS提供技术支持”、“使用WPS Office打开”等相关字样。
* 当前Preview Kit暂不支持安全定制能力，包括禁止截录屏、屏蔽其他应用打开入口、屏蔽分享入口等安全预览能力。
* 当前Preview Kit需要调用方存在对应uri的转授权能力，从而让预览获得该文件的访问权限来正常读取文件，具体问题可以参考[Preview Kit常见问题2](preview-faq-2.md)。

## 接口说明

接口返回值有两种返回形式：callback和promise，promise和callback只是返回值方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/preview-arkts.md)。

**表1** Preview Kit的接口介绍

| 接口名 | 描述 |
| --- | --- |
| openPreview(context: Context, file: PreviewInfo, info?: DisplayInfo): Promise<void> | 打开预览功能。通过传入单个文件预览信息以及悬浮窗口属性信息，打开预览窗口。1秒内重复调用无效。使用Promise方式异步返回结果。 |
| openPreview(context: Context, file: PreviewInfo, info: DisplayInfo, callback: AsyncCallback<void>): void | 打开预览功能。通过传入单个文件预览信息以及悬浮窗口属性信息，打开预览窗口。1秒内重复调用无效。传入callback进行异步回调。 |
| openPreview(context: Context, files: Array<PreviewInfo>, index?: number): Promise<void> | 打开预览功能。通过传入多个文件预览信息以及选择展示的文件信息下标，打开预览窗口。1秒内重复调用无效。使用Promise方式异步返回结果。仅移动端可用。 |
| canPreview(context: Context, uri: string): Promise<boolean> | 根据文件的uri判断文件是否可预览。  - 当传入支持的文件类型（图片、视频、音频、文本、html）并且文件存在时，会返回true。  - 当传入不可预览的文件uri时，返回false。 |
| hasDisplayed(context: Context): Promise<boolean> | 判断预览窗口是否已经存在。预览窗口是单例的形式。  - 如果预览窗口已经打开过并且没关闭，那会返回true。  - 如果没打开或者打开后已关闭，那将返回false。 |
| closePreview(context: Context): Promise<void> | 关闭预览窗口，仅当预览窗口存在时起效。 |
| loadData(context: Context, file: PreviewInfo): Promise<void> | 加载预览文件信息。仅当预览窗口存在时生效。100毫秒内重复调用无效。  - 传入可预览文件时展示对应预览界面。  - 传入不可预览文件显示不支持预览界面。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 判断是否可以预览。

   ```typescript
   let uiContext = this.getUIContext().getHostContext() as Context;
   let uri = fileUri.getUriFromPath(uiContext.filesDir + '/1.txt');
   filePreview.canPreview(uiContext, uri).then((result) => { // 传入支持的文件类型且文件存在时会返回true
     hilog.info(0x0000, 'FilePreview',
       `Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
     // ...
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'FilePreview',
       `Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```
3. 调用openPreview，实现打开文件预览的功能。

   * 通过Promise方式打开文件

   ```typescript
   let uiContext = this.getUIContext().getHostContext() as Context;
   let displayInfo: filePreview.DisplayInfo = {
     x: 100,
     y: 100,
     width: 800,
     height: 800
   };
   let fileInfo: filePreview.PreviewInfo = {
     title: '1.txt',
     uri: fileUri.getUriFromPath(uiContext.filesDir + '/1.txt'),
     mimeType: 'text/plain'
   };
   filePreview.openPreview(uiContext, fileInfo, displayInfo).then(() => {
     hilog.info(0x0000, 'FilePreview', 'Succeeded in opening preview');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'FilePreview',
       `Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```

   * 通过CallBack回调函数方式打开文件

   ```typescript
   let uiContext = this.getUIContext().getHostContext() as Context;
   let displayInfo: filePreview.DisplayInfo = {
     x: 100,
     y: 100,
     width: 800,
     height: 800
   };
   let fileInfo: filePreview.PreviewInfo = {
     title: '1.txt',
     uri: fileUri.getUriFromPath(uiContext.filesDir + '/1.txt'),
     mimeType: 'text/plain'
   };
   filePreview.openPreview(uiContext, fileInfo, displayInfo, (err) => {
     if (err && err.code) {
       hilog.error(0x0000, 'FilePreview',
         `Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
       return;
     }
     hilog.info(0x0000, 'FilePreview', 'Succeeded in opening preview');
   });
   ```

   * 传入多个文件打开预览，仅移动端可用。

   ```typescript
   let uiContext = this.getUIContext().getHostContext() as Context;
   // ...
   let fileInfo: filePreview.PreviewInfo = {
     title: '1.txt',
     uri: fileUri.getUriFromPath(uiContext.filesDir + '/1.txt'),
     mimeType: 'text/plain'
   };
   let fileInfo1: filePreview.PreviewInfo = {
     title: '2.txt',
     uri: fileUri.getUriFromPath(uiContext.filesDir + '/2.txt'),
     mimeType: 'text/plain'
   };
   let files: filePreview.PreviewInfo[] = [];
   files.push(fileInfo);
   files.push(fileInfo1);
   // 多文件预览，当前仅移动端可用，PC/2in1设备不可用，返回801错误码
   filePreview.openPreview(uiContext, files, 0).then(() => {
     hilog.info(0x0000, 'FilePreview', 'Succeeded in opening preview');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'FilePreview',
       `Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```
4. （可选）如果已经打开过预览窗口，需要重新加载页面，需要调用loadData接口，加载文件。

   ```typescript
   let uiContext = this.getUIContext().getHostContext() as Context;
   let fileInfo: filePreview.PreviewInfo = {
     title: '2.txt',
     uri: fileUri.getUriFromPath(uiContext.filesDir + '/2.txt'),
     mimeType: 'text/plain'
   };
   filePreview.loadData(uiContext, fileInfo).then(() => { // 仅当预览窗口存在时起效
     hilog.info(0x0000, 'FilePreview', 'Succeeded in loading data.');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'FilePreview', `Failed to load data, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```
5. （可选）如果想要关闭预览窗口，需要调用closePreview。

   ```typescript
   let uiContext = this.getUIContext().getHostContext() as Context;
   filePreview.closePreview(uiContext).then(() => { // 仅当预览窗口存在时起效
     hilog.info(0x0000, 'FilePreview', 'Succeeded in closing preview');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'FilePreview',
       `Failed to close preview, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```
