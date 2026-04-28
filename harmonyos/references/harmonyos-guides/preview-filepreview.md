---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-filepreview
title: 文件预览
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 文件预览
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51281c7eeba02223ae2b48905f65ee46b01da3a765ac0ef181e6a022b183fa19
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

   ```
   1. import { filePreview } from '@kit.PreviewKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 判断是否可以预览。

   ```
   1. let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
   2. let uiContext = this.getUIContext().getHostContext() as Context;
   3. filePreview.canPreview(uiContext, uri).then((result) => {    // 传入支持的文件类型且文件存在时会返回true
   4. console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
   5. }).catch((err: BusinessError) => {
   6. console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
   7. });
   ```
3. 调用openPreview，实现打开文件预览的功能。

   * 通过Promise方式打开文件

     ```
     1. let uiContext = this.getUIContext().getHostContext() as Context;
     2. let displayInfo: filePreview.DisplayInfo = {
     3. x: 100,
     4. y: 100,
     5. width: 800,
     6. height: 800
     7. };
     8. let fileInfo: filePreview.PreviewInfo = {
     9. title: '1.txt',
     10. uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
     11. mimeType: 'text/plain'
     12. };
     13. filePreview.openPreview(uiContext, fileInfo, displayInfo).then(() => {
     14. console.info('Succeeded in opening preview');
     15. }).catch((err: BusinessError) => {
     16. console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
     17. });
     ```
   * 通过CallBack回调函数方式打开文件

     ```
     1. let uiContext = this.getUIContext().getHostContext() as Context;
     2. let displayInfo: filePreview.DisplayInfo = {
     3. x: 100,
     4. y: 100,
     5. width: 800,
     6. height: 800
     7. };
     8. let fileInfo: filePreview.PreviewInfo = {
     9. title: '1.txt',
     10. uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
     11. mimeType: 'text/plain'
     12. };
     13. filePreview.openPreview(uiContext, fileInfo, displayInfo, (err) => {
     14. if (err && err.code) {
     15. console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
     16. return;
     17. }
     18. console.info('Succeeded in opening preview');
     19. });
     ```
   * 传入多个文件打开预览，仅移动端可用。

     ```
     1. let uiContext = this.getUIContext().getHostContext() as Context;
     2. let fileInfo: filePreview.PreviewInfo = {
     3. title: '1.txt',
     4. uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
     5. mimeType: 'text/plain'
     6. };
     7. let fileInfo1: filePreview.PreviewInfo = {
     8. title: '2.txt',
     9. uri: 'file://docs/storage/Users/currentUser/Documents/2.txt',
     10. mimeType: 'text/plain'
     11. };
     12. let files: Array<filePreview.PreviewInfo> = new Array();
     13. files.push(fileInfo);
     14. files.push(fileInfo1);
     15. filePreview.openPreview(uiContext, files, 0).then(() => {
     16. console.info('Succeeded in opening preview');
     17. }).catch((err: BusinessError) => {
     18. console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
     19. });
     ```
4. （可选）如果已经打开过预览窗口，需要重新加载页面，需要调用loadData接口，加载文件。

   ```
   1. let uiContext = this.getUIContext().getHostContext() as Context;
   2. let fileInfo: filePreview.PreviewInfo = {
   3. title: '2.txt',
   4. uri: 'file://docs/storage/Users/currentUser/Documents/2.txt',
   5. mimeType: 'text/plain'
   6. };
   7. filePreview.loadData(uiContext, fileInfo).then(() => {   // 仅当预览窗口存在时起效
   8. console.info('Succeeded in loading data.');
   9. }).catch((err: BusinessError) => {
   10. console.error(`Failed to load data, err.code = ${err.code}, err.message = ${err.message}`);
   11. });
   ```
5. （可选）如果想要关闭预览窗口，需要调用closePreview。

   ```
   1. let uiContext = this.getUIContext().getHostContext() as Context;
   2. filePreview.closePreview(uiContext).then(() => {   // 仅当预览窗口存在时起效
   3. console.info('Succeeded in closing preview');
   4. }).catch((err: BusinessError) => {
   5. console.error(`Failed to close preview, err.code = ${err.code}, err.message = ${err.message}`);
   6. });
   ```
