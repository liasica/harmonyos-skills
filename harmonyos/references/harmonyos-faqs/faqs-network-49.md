---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-49
title: 如何实现http并行下载
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何实现http并行下载
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0a2f8ecc8d694b03524a9c6bd8ee5f4b9affdddb0a751b53ae02964bdf99238e
---

使用上传下载模块进行下载。最多支持4个任务同时下载。

参考代码如下：

```
1. import { request } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // Using AppStore to store UIContext in ExitAbility
5. const context = AppStorage.get("context") as UIContext;
6. let downloadTask: request.DownloadTask;
7. try {
8. request.downloadFile(context.getHostContext(), { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
9. downloadTask = data;
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
12. })
13. } catch (err) {
14. console.error(`Failed to request the download. err: ${JSON.stringify(err)}`);
15. }
```

[HttpParallelDownload.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/HttpParallelDownload.ets#L21-L35)

**参考链接**

[@ohos.request (上传下载)](../harmonyos-references/js-apis-request.md)
