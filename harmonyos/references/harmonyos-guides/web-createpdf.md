---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-createpdf
title: 使用Web组件保存前端页面为PDF
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 使用Web组件保存前端页面为PDF
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:26e70fecd776389640d720283d49a2691335bbaa8f9bca03049532b73e7f4cc7
---

从API version 14开始，支持使用Web组件的[createPdf](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#createpdf14)方法，为应用提供了保存前端页面为PDF的功能。

使用[createPdf](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#createpdf14)生成实例后，调用pdfArrayBuffer方法获取二进制数据流，再使用[fileIo](../harmonyos-references/js-apis-file-fs.md)方法将二进制数据流保存为PDF文件。用户可以将前端页面内容保存为PDF以便分享或保存。例如，生成报告、发票等，方便用户保存和传输。

说明

通过[pdfConfiguration](../harmonyos-references/arkts-apis-webview-i.md#pdfconfiguration14)的配置，可调整PDF每页大小、前端页面缩放比例等；推荐使用前端页面适配策略，通过CSS媒体查询（@media print）优化PDF排版。

## 需要权限

若涉及网络文档获取，需在module.json5中配置网络访问权限。具体添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.INTERNET"
4. }
5. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebCreatePdf/entry/src/main/module.json5#L64-L70)

## callback方式保存PDF

通过callback方式调用createPdf接口，获取到的result通过pdfArrayBuffer接口取得PDF二进制数据流，最后使用fileIo方法将二进制数据流保存为PDF文件。

```
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. controller: webview.WebviewController = new webview.WebviewController();
10. pdfConfig: webview.PdfConfiguration = {
11. width: 8.27,
12. height: 11.69,
13. marginTop: 0,
14. marginBottom: 0,
15. marginRight: 0,
16. marginLeft: 0,
17. shouldPrintBackground: true
18. };

20. build() {
21. Column() {
22. Button('SavePDF')
23. .onClick(() => {
24. // 触发PDF生成，需要确保页面渲染完成，可使用onPageEnd事件监听
25. this.controller.createPdf(
26. this.pdfConfig,
27. (error, result: webview.PdfData) => {
28. try {
29. // 获取到的result通过`pdfArrayBuffer`接口取得PDF二进制数据流，最后使用`fileIo`方法将二进制数据流保存为PDF文件
30. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
31. let filePath = context.filesDir + '/test.pdf';
32. let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
33. fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
34. console.info('createPDF write data to file succeed and size is:' + writeLen);
35. }).catch((err: BusinessError) => {
36. console.error('createPDF write data to file failed with error message: ' + err.message +
37. ', error code: ' + err.code);
38. }).finally(() => {
39. // 关闭file
40. fs.closeSync(file);
41. });
42. } catch (resError) {
43. console.error(
44. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
45. }
46. });
47. })
48. Web({ src: 'www.example.com', controller: this.controller })
49. }
50. }
51. }
```

[WebCreatePdfCallback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebCreatePdf/entry/src/main/ets/pages/WebCreatePdfCallback.ets#L16-L68)

## Promise方式保存PDF

通过Promise方式调用createPdf接口，获取到的result通过pdfArrayBuffer接口取得PDF二进制数据流，最后使用fileIo方法将二进制数据流保存为PDF文件。

```
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. controller: webview.WebviewController = new webview.WebviewController();
10. pdfConfig: webview.PdfConfiguration = {
11. width: 8.27,
12. height: 11.69,
13. marginTop: 0,
14. marginBottom: 0,
15. marginRight: 0,
16. marginLeft: 0,
17. shouldPrintBackground: true
18. };

20. build() {
21. Column() {
22. Button('SavePDF')
23. .onClick(() => {
24. // 触发PDF生成，需要确保页面渲染完成，可使用onPageEnd事件监听
25. this.controller.createPdf(this.pdfConfig)
26. .then((result: webview.PdfData) => {
27. try {
28. // 获取到的result通过`pdfArrayBuffer`接口取得PDF二进制数据流，最后使用`fileIo`方法将二进制数据流保存为PDF文件
29. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
30. let filePath = context.filesDir + '/test.pdf';
31. let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
32. fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
33. console.info('createPDF write data to file succeed and size is:' + writeLen);
34. }).catch((err: BusinessError) => {
35. console.error('createPDF write data to file failed with error message: ' + err.message +
36. ', error code: ' + err.code);
37. }).finally(() => {
38. // 关闭file
39. fs.closeSync(file);
40. });
41. } catch (resError) {
42. console.error(
43. `ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
44. }
45. })
46. })
47. Web({ src: 'www.example.com', controller: this.controller })
48. }
49. }
50. }
```

[WebCreatePdfPromise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebCreatePdf/entry/src/main/ets/pages/WebCreatePdfPromise.ets#L16-L67)
