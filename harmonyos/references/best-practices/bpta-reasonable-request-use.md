---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-request-use
title: 后台上传下载合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台上传下载合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:46+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8546a038a021e16b2c289f77327d3a6bc5f0dcc50c3879078199de96a293937a
---

应用上传下载时，应使用系统服务，不要申请长时任务。

## 约束

NA

## 示例

### 上传

```
1. import { BusinessError, request } from '@kit.BasicServicesKit';

3. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
4. let context = uiContext!.getHostContext()!;

6. let uploadTask: request.UploadTask;
7. let uploadConfig: request.UploadConfig = {
8. url: 'http://www.example.com', //Replace the IP address of the real server manually
9. header: { 'Accept': '*/*' },
10. method: "POST",
11. files: [{
12. filename: "test",
13. name: "test",
14. uri: "internal://cache/test.jpg",
15. type: "jpg"
16. }],
17. data: [{ name: "name123", value: "123" }],
18. };
19. try {
20. //Upload request
21. request.uploadFile(context, uploadConfig, (err: BusinessError, data: request.UploadTask) => {
22. if (err) {
23. console.error(`Failedtorequesttheupload.Code:${err.code},message:${err.message}`);
24. return;
25. }
26. uploadTask = data;
27. });
28. } catch (err) {
29. console.error(`Failedtorequesttheupload.err:${JSON.stringify(err)}`);
30. }
```

[Upload.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/Upload.ets#L21-L50)

### 下载

```
1. import { BusinessError, request } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. try {
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. request.downloadFile(context, {
7. url: 'https://xxxx/xxxxx.hap', // IP address of the server to download the file
8. filePath: 'xxx/xxxxx.hap'
9. }, (err: BusinessError, data: request.DownloadTask) => {
10. if (err) {
11. console.error(`Failedtorequestthedownload.Code:${err.code},message:${err.message}`);
12. return;
13. }
14. let downloadTask: request.DownloadTask = data;
15. });
16. } catch (err) {
17. console.error(`Failedtorequestthedownload.err:${JSON.stringify(err)}`);
18. }
```

[Download.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/Download.ets#L21-L49)

有关上传下载相关接口的使用，详情可以参考[应用文件上传下载](../harmonyos-guides/app-file-upload-download.md)。
