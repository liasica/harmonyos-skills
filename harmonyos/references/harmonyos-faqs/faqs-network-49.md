---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-49
title: 如何实现http并行下载
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何实现http并行下载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cadb09dd4d5f50d0dadbdf04c6f9a166a5a249e04e870e248972295aa0229f16
---

使用上传下载模块进行下载。最多支持4个任务同时下载。

参考代码如下：

```typescript
import { request } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Using AppStore to store UIContext in ExitAbility
const context = AppStorage.get("context") as UIContext;
let downloadTask: request.DownloadTask;
try {
  request.downloadFile(context.getHostContext(), { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    downloadTask = data;
  }).catch((err: BusinessError) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. err: ${JSON.stringify(err)}`);
}
```

**参考链接**

[@ohos.request (上传下载)](../harmonyos-references/js-apis-request.md)
