---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-faq-0002
title: request上传下载参数校验问题排查
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 常见问题 > request上传下载参数校验问题排查
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:08+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:b8b549d415f8c90a7ca1c88c6cbf7da344aea150813adde6a3bd36b24e127f1c
---

**Q：报错“the parameters check fails this is fail path”如何解决？**

**A：**

```ts
public static timelineReceivedResult(path: string): void {
  if (!path) {
    console.error('Invoke empty file path')
    return;
  }
  let filename = path.substring(path.lastIndexOf("/") + 1);
  let uri = fileUri.getUriFromPath(path);
  let header = new Map<Object, string>();
  let files: Array<request.File> = [
    {
      filename: filename,
      name: 'test',
      uri: uri,
      type: 'txt'
    }
  ]
  let data: Array<request.RequestData> = []; // { name: 'name', value: 'value' }
  let uploadConfig: request.UploadConfig = {
    url: 'http://xx.xx.xx.xx:8800',
    header: header,
    method: 'POST',
    files: files,
    data: data
  }

  // Upload the local application file to the web server.
  try {
    request.uploadFile(context, uploadConfig)
      .then((uploadTask: request.UploadTask) => {
        uploadTask.on('complete', (taskStates: Array<request.TaskState>) => {
          for (let i = 0; i < taskStates.length; i++) {
            console.info(`upload complete taskState: ${JSON.stringify(taskStates[i])}`);
          }
        });
      })
      .catch((err: BusinessError) => {
        console.error(`Invoke uploadFile failed, code is ${err.code}, message is ${err.message}`);
      })
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`Invoke uploadFile failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

当参数检查失败时，系统会进入错误处理路径。

请尝试在cache里上传，当前仅支持“internal”协议，对应在cache目录下。

参考链接：[@ohos.request (上传下载)](../harmonyos-references/js-apis-request.md)。

**Q：[request](../harmonyos-references/js-apis-request.md)上传文件后通过[on('headerReceive')](../harmonyos-references/js-apis-request.md#onheaderreceive7)获取headerReceive内容：**

```json
{ "headers": {},"body": "{"code ":0,"msg ":"操作成功","data ":{"name ":"file.png ","url ":"","path ":""}}"}
```

使用JSON序列化解析，报错Error message:Unexpected Object in JSON：

```ts
let headerObject: RequestUploadHeaderInterface = JSON.parse(headersStr)
```

如何解决？

**A：**通过JSON校验工具可以看出，需要序列化的内容不是正规的JSON字符串，若在已知响应内容的情况下，通过属性名的字符串形式获取body对象的属性，再用JSON序列化，如：JSON.parse(headersStr["body"])。
