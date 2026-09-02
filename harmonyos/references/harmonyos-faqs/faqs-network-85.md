---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-85
title: http请求通过MultiFormData分片上传报错
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求通过MultiFormData分片上传报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4fc831b1fbfc98d113e6a5dc8a9109eec76ec3e2d36044396e111eb660e67637
---

## 问题现象

通过http.MultiFormData[]上传失败，错误信息：

```screen
{"timestamp":1747124996117,"status":400,"error":"Bad Request","exception":"org.springframework.web.multipart.support.MissingServletRequestPartException","message":"Required request part 'chunk' is not present","path":"/upload/clip"}
```

## 背景知识

httpRequest实现分片上传需要服务器那边配合定义好协议传参，在[MultiFormData](../harmonyos-references/js-apis-http.md#multiformdata11)里添加相关参数。

## 问题定位

这是传参错误导致,错误示例如下:

```ts
uploadFile1(filePath: string) {
  let httpRequest = http.createHttp();
  let requestMultipart: http.MultiFormData[] = [];
  let formData: http.MultiFormData = {
    name: 'xxx.mp4',
    contentType: 'video/mp4',
    filePath: filePath,
    remoteFileName: 'xxx.mp4',
    data: {
      'vid': 'xxx',
      'fseq': 'xxx',
      'cmd5': 'xxx',
      'chunk': ''
    }
  };
  requestMultipart.push(formData);
  httpRequest.request(
    this.uploadUrl,
    {
      method: http.RequestMethod.POST,
      header: {
        'Content-Type': 'multipart/form-data',
        'APPID': 'xxx',
        'TOKEN': 'xxx',
        'VERSION': 'xxx',
      },
      multiFormDataList: requestMultipart,
    }, (err: BusinessError, data: http.HttpResponse) => {
    if (err) {
      console.error(`Failed to uploadFile. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded to uploadFile:  ${data}`);
  });
}
```

应把data数据放到requestMultipart中。

## 分析结论

数据结构不对导致服务器无法捕获引起错误，修改传参可解决处理。

## 修改建议

通过对象requestMultipart上传时需要把data数据拎出来单独push到requestMultipart对象里面才能收到。

```ts
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private uploadUrl: string = 'http://127.0.0.1:9588/'; //替换为实际服务器URL。

  uploadFile(filePath: string) {
    let httpRequest = http.createHttp();
    let requestMultipart: http.MultiFormData[] = [];
    let formData: http.MultiFormData = {
      name: 'share.txt', //数据名称。
      contentType: 'text/plain', //数据类型，自API 11开始支持该属性。
      filePath: filePath, //替换为实际文件路径。
      remoteFileName: 'share.txt', //上传到服务器保存为文件的名称。
    };
    requestMultipart.push(formData);

    httpRequest.request(
      this.uploadUrl,
      {
        method: http.RequestMethod.POST,
        header: {
          'Content-Type': 'multipart/form-data',
        },
        multiFormDataList: requestMultipart,
      }, (err: BusinessError, data: http.HttpResponse) => {
      if (err) {
        console.error(`Failed to uploadFile. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info(`Succeeded to uploadFile:  ${data.result}`);
    });
  }

  build() {
    Column({ space: 10 }) {
      Button('MultiFormData分片上传').onClick(() => {
        let context = this.getUIContext()?.getHostContext();
        if (!context) {
          return;
        }
        let filePath = context.filesDir + '/' + 'share.txt'; //文件沙箱路径，使用时替换实际文件路径。
        this.uploadFile(filePath);
      });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：使用requestInStream设置multiFormDataList上传文件，当remoteFileName的名字过长时会提示500，换成其他短文件名则不会出现问题。

A：使用multiFormDataList设置remoteFileName时，当文件名包含中文、空格、特殊符号或长度超过255字符，可能触发服务器端异常，需通过URL编码处理。

Q：multiFormDataList上传文件的filePath字段能使用fd吗？

A：filePath中需要传入一个文件路径，而fd://int的语法是以fd标识一个媒体资源，非文件路径。
