---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-79
title: HTTP请求返回数据类型为JSON文件时如何读取data
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HTTP请求返回数据类型为JSON文件时如何读取data
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:73fcdac42bc66699255dbb521ae056b1774a1e0a7e92bae0c54b24815f50430f
---

## 问题现象

通过HTTP GET请求，可以正常调用并返回数据，但是当请求返回JSON格式内容时，无法直接读取，如何实现JSON文件响应数据的读取呢？

## 背景知识

* [JSON解析与生成](../harmonyos-references/js-apis-json.md)。
* HTTP请求返回文件可通过requestInStream获取文本，参考[发起HTTP流式传输请求](../harmonyos-guides/http-request.md#发起http流式传输请求)。

## 解决方案

开发前需要在module.json5中声明ohos.permission.INTERNET权限，使用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10-1)获取文本，再通过[on("dataReceive")](../harmonyos-references/js-apis-http.md#ondatareceive10)流式获取数据，[on("dataEnd")](../harmonyos-references/js-apis-http.md#ondataend10)整合文本内容转换为JSON数据。

```json
async httpTest(): Promise<object> {
  return new Promise((resolve: Function, reject: Function) => {
    let res: ArrayBuffer = new ArrayBuffer(0);
    let httpRequest: http.HttpRequest = http.createHttp();
    httpRequest.on('dataReceive', (data: ArrayBuffer) => {
      const newRes: ArrayBuffer = new ArrayBuffer(res.byteLength + data.byteLength);
      const resView: Uint8Array = new Uint8Array(newRes);
      resView.set(new Uint8Array(res));
      resView.set(new Uint8Array(data), res.byteLength);
      res = newRes;
      console.info(`res length: ${res.byteLength}`);
    });
    httpRequest.on('dataEnd', () => {
      try {
        let textDecoderOptions: util.TextDecoderOptions = {
          ignoreBOM: true
        };
        let decoder: util.TextDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
        let str: string = decoder.decodeToString(new Uint8Array(res));
        console.info(`test json read successful: ${str}`);
        let jsonStr = json.parse(str);
        resolve(jsonStr);
      } catch (err) {
        hilog.error(0x0000, 'testTag', `error: ${(err as BusinessError).code} ${(err as BusinessError).message}`);
        reject(err);
      }
    });
    httpRequest.requestInStream(
      'xx.xx.xx/xx.json', // 后台服务器地址
      {
        method: http.RequestMethod.GET,
        header: {
          'Content-Type': 'application/json'
        },
        connectTimeout: 6000,
        readTimeout: 6000,
      });
  });
}
```

## 总结

1. 读取本地JSON文件的方式：

   ```json
   readJsonFromRawFile(fileName: string): object | undefined  {
     try {
       let value: Uint8Array | undefined = this.getUIContext().getHostContext()?.resourceManager.getRawFileContentSync(fileName);
       return JSON.parse(buffer.from(value?.buffer).toString());
     } catch (error) {
       console.error(`error: ${JSON.stringify(error)}`);
     }
     return undefined;
   }
   ```
2. 读取HTTP请求返回的JSON文件的方式：

   先使用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10-1)获取文本，再通过[on("dataReceive")](../harmonyos-references/js-apis-http.md#ondatareceive10)流式获取数据，[on("dataEnd")](../harmonyos-references/js-apis-http.md#ondataend10)整合文本内容转换为JSON数据。

完整示例如下：

```json
import { hilog } from '@kit.PerformanceAnalysisKit';
import { buffer, util } from '@kit.ArkTS';
import json from '@ohos.util.json';
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State jsonObj: object | undefined = undefined;

  async httpTest(): Promise<object> {
    return new Promise((resolve: Function, reject: Function) => {
      let res: ArrayBuffer = new ArrayBuffer(0);
      let httpRequest: http.HttpRequest = http.createHttp();
      httpRequest.on('dataReceive', (data: ArrayBuffer) => {
        const newRes: ArrayBuffer = new ArrayBuffer(res.byteLength + data.byteLength);
        const resView: Uint8Array = new Uint8Array(newRes);
        resView.set(new Uint8Array(res));
        resView.set(new Uint8Array(data), res.byteLength);
        res = newRes;
        console.info(`res length: ${res.byteLength}`);
      });
      httpRequest.on('dataEnd', () => {
        try {
          let textDecoderOptions: util.TextDecoderOptions = {
            ignoreBOM: true
          };
          let decoder: util.TextDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
          let str: string = decoder.decodeToString(new Uint8Array(res));
          console.info(`test json read successful: ${str}`);
          let jsonStr = json.parse(str);
          resolve(jsonStr);
        } catch (err) {
          hilog.error(0x0000, 'testTag', `error: ${(err as BusinessError).code} ${(err as BusinessError).message}`);
          reject(err);
        }
      });
      httpRequest.requestInStream(
        'xx.xx.xx/xx.json', // 后台服务器地址
        {
          method: http.RequestMethod.GET,
          header: {
            'Content-Type': 'application/json'
          },
          connectTimeout: 6000,
          readTimeout: 6000,
        });
    });
  }

  readJsonFromRawFile(fileName: string): object | undefined  {
    try {
      let value: Uint8Array | undefined = this.getUIContext().getHostContext()?.resourceManager.getRawFileContentSync(fileName);
      return JSON.parse(buffer.from(value?.buffer).toString());
    } catch (error) {
      console.error(`error: ${JSON.stringify(error)}`);
    }
    return undefined;
  }

  build() {
    Column({ space: 24 }) {
      Button('读取JSON文件响应数据')
        .onClick(async () => {
          this.httpTest().then((jsonObj) => {
            this.jsonObj = jsonObj;
          });
        })
      Button('读取本地JSON文件')
        .onClick(() => {
          let fileName = 'xxx.json'; // 此处填写文件名，JSON文件需要放置到resources/rawfile目录下
          this.jsonObj = this.readJsonFromRawFile(fileName);
        })
      Column({ space: 16 }) {
        Text('JSON内容如下：')
          .fontSize(20)
        Text(JSON.stringify(this.jsonObj))
          .fontSize(16)
      }
    }
    .height('100%')
    .width('100%')
  }
}
```
