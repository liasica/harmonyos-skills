---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-request-use
title: 后台上传下载合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台上传下载合理使用
category: best-practices
scraped_at: 2026-10-16T07:06:48+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:c73a9e914e0a07cdb9f1126a2d8e93992473e7fe3f05fccfc99d686b8a42cf05
---

应用上传下载时，应使用系统服务，不要申请长时任务。

## 约束

不涉及

## 示例

### 上传

```typescript
import { BusinessError, request } from '@kit.BasicServicesKit';

const uiContext: UIContext | undefined = AppStorage.get('uiContext');
let context = uiContext!.getHostContext()!;

let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', //Replace the IP address of the real server manually
  header: { 'Accept': '*/*' },
  method: "POST",
  files: [{
    filename: "test",
    name: "test",
    uri: "internal://cache/test.jpg",
    type: "jpg"
  }],
  data: [{ name: "name123", value: "123" }],
};
try {
  //Upload request
  request.uploadFile(context, uploadConfig, (err: BusinessError, data: request.UploadTask) => {
    if (err) {
      console.error(`Failedtorequesttheupload.Code:${err.code},message:${err.message}`);
      return;
    }
    uploadTask = data;
  });
} catch (err) {
  console.error(`Failedtorequesttheupload.err:${JSON.stringify(err)}`);
}
```

### 下载

```typescript
import { BusinessError, request } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      request.downloadFile(context, {
        url: 'https://xxxx/xxxxx.hap', // IP address of the server to download the file
        filePath: 'xxx/xxxxx.hap'
      }, (err: BusinessError, data: request.DownloadTask) => {
        if (err) {
          console.error(`Failedtorequestthedownload.Code:${err.code},message:${err.message}`);
          return;
        }
        let downloadTask: request.DownloadTask = data;
      });
    } catch (err) {
      console.error(`Failedtorequestthedownload.err:${JSON.stringify(err)}`);
    }
```

有关上传下载相关接口的使用，详情可以参考[应用文件上传下载](../harmonyos-guides/app-file-upload-download.md)。
