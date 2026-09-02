---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-69
title: 在不同存储路径下如何读取JSON文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 在不同存储路径下如何读取JSON文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:452fec3fe9494fa099111c86cfb71ff6857d0356ed2a35e7ae95b9e52eb026ed
---

## 问题现象

在APP开发中，需要使用JSON文件保存信息到本地或者服务器，如何在如下场景去读取JSON文件？

* 场景一：读取放在工程rawfile目录下的JSON文件。
* 场景二：读取放在本地沙箱目录下的JSON文件。
* 场景三：读取网络接口返回的JSON文件。

## 背景知识

* [util.json](../harmonyos-references/js-apis-json.md)：提供了将JSON文本转换为JSON对象或值，以及将对象转换为JSON文本等功能。
* [requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10-1)：根据URL地址和相关配置项，发起HTTP网络请求并返回流式响应，使用callback方式作为异步方法。
* [getRawFileContentSync](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontentsync10)：获取resources/rawfile目录下对应的rawfile文件内容，使用同步形式返回。
* [@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)：该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

## 解决方案

读取JSON文件主要是读取文件二进制数据转为JSON字符串或者直接读取JSON字符串，然后解析对象数据。

模拟JSON文件，放在rawfile目录下或者沙箱filesDir目录下，定义数据类型，示例代码如下：

```json
{
  "CityCodeList":  [
    {
      "districtGeocode":"110100",
      "district":"北京"
    },
    {
      "districtGeocode":"110101",
      "district":"东城"
    },
    {
      "districtGeocode":"110102",
      "district":"朝阳"
    }
  ]
}
```

```ts
// 定义数据类
export class CityCode {
  cityCodeList: Array<CityCodeBean> = [];
}

export class CityCodeBean {
  districtGeocode: string = '';
  district: string = '';
}
```

* 场景一：读取放在工程rawfile目录下的JSON文件，并解析为对象。

  通过getRawFileContentSync读取文件，返回二进制数据。转字符串后，通过JSON.parse解析为对象。示例代码如下：

  ```ts
  getRawFileJsonData() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let value: Uint8Array = context.resourceManager.getRawFileContentSync('testData.json');
    let citystr = buffer.from(value.buffer).toString();
    let cityObj: ESObject = JSON.parse(citystr);
    let cityInfoList: CityCode = cityObj;
    console.info('getRawFileJsonData：', JSON.stringify(cityInfoList));
  }
  ```
* 场景二：读取放在沙箱目录下的JSON文件，并解析为对象。

  通过[fs.readTextSync](../harmonyos-references/js-apis-file-fs.md#fileioreadtextsync)读取文件，返回字符串文本数据，通过JSON.parse解析为对象。示例代码如下：

  ```ts
  getLocationFileJsonData() {
    // 读取文件，解析为对象
    let context = this.getUIContext().getHostContext() as common.Context;
    let pathDir = context.filesDir;
    let filePath = pathDir + '/testData.json';// 需要先把测试数据放入沙箱filesDir目录下
    try {
      let cityStr = fs.readTextSync(filePath);
      let cityObj: ESObject = JSON.parse(cityStr);
      let cityInfoList: CityCode = cityObj;
      console.info('getLocationFileJsonData：', JSON.stringify(cityInfoList));
    } catch (e) {
      console.error('fs.readTextSync failed error is : ', JSON.stringify(e));
    }
  }
  ```
* 场景三：读取通过网络接口返回的JSON文件。

  先使用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10-1)获取文本，再通过httpRequest.on('dataReceive',()=>{})流式获取数据，httpRequest.on('dataEnd',()=>{})整合文本内容转化JSON数据。

  ```ts
  async httpGetJsonFile(): Promise<object> {
    return new Promise((resolve: Function) => {
      let res = new ArrayBuffer(0);
      let httpRequest = http.createHttp();
      httpRequest.on('dataReceive', (data: ArrayBuffer) => {
        const newRes = new ArrayBuffer(res.byteLength + data.byteLength);
        const resView = new Uint8Array(newRes);
        resView.set(new Uint8Array(res));
        resView.set(new Uint8Array(data), res.byteLength);
        res = newRes;
        console.info('res length: ', res.byteLength);
      });
      httpRequest.on('dataEnd', () => {
        try {
          let textDecoderOptions: util.TextDecoderOptions = {
            ignoreBOM: true
          };
          let decoder = util.TextDecoder.create('utf-8', textDecoderOptions);
          let str = decoder.decodeToString(new Uint8Array(res));
          console.info('test json read successful: ', str);
          let jsonStr = json.parse(str);
          resolve(jsonStr);
        } catch (err) {
          hilog.error(0x0000, 'testTag', `error: ${(err as BusinessError).code} ${(err as BusinessError).message}`);
        }
      });
      httpRequest.requestInStream('json文件的网络地址', // 后台服务器地址
        {
          method: http.RequestMethod.GET,
          header: {
            'Content-Type': 'application/json'
          },
          connectTimeout: 6000,
          readTimeout: 6000,
        }, (err, data) => {
          if (!err) {
            console.info('data: ', data);
          }
        }
      );
    });
  }
  ```

三个场景的完整代码示例如下：

```ts
import { buffer, util } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';
import json from '@ohos.util.json';
import { http } from '@kit.NetworkKit';
import fs from '@ohos.file.fs';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 定义数据类
export class CityCode {
  cityCodeList: Array<CityCodeBean> = [];
}

export class CityCodeBean {
  districtGeocode: string = '';
  district: string = '';
}
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  // 读取文件，解析为对象
  aboutToAppear(): void {
    this.getRawFileJsonData();
    this.getLocationFileJsonData();
    this.httpGetJsonFile();
  }

  // 场景一：读取放在工程rawfile目录下的JSON文件，并解析为对象。
  getRawFileJsonData() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let value: Uint8Array = context.resourceManager.getRawFileContentSync('testData.json');
    let citystr = buffer.from(value.buffer).toString();
    let cityObj: ESObject = JSON.parse(citystr);
    let cityInfoList: CityCode = cityObj;
    console.info('getRawFileJsonData：', JSON.stringify(cityInfoList));
  }

  // 场景二：读取放在沙箱目录下的JSON文件，并解析为对象。
  getLocationFileJsonData() {
    // 读取文件，解析为对象
    let context = this.getUIContext().getHostContext() as common.Context;
    let pathDir = context.filesDir;
    let filePath = pathDir + '/testData.json';// 需要先把测试数据放入沙箱filesDir目录下
    try {
      let cityStr = fs.readTextSync(filePath);
      let cityObj: ESObject = JSON.parse(cityStr);
      let cityInfoList: CityCode = cityObj;
      console.info('getLocationFileJsonData：', JSON.stringify(cityInfoList));
    } catch (e) {
      console.error('fs.readTextSync failed error is : ', JSON.stringify(e));
    }
  }

  // 场景三：读取通过网络接口返回的JSON文件。
  async httpGetJsonFile(): Promise<object> {
    return new Promise((resolve: Function) => {
      let res = new ArrayBuffer(0);
      let httpRequest = http.createHttp();
      httpRequest.on('dataReceive', (data: ArrayBuffer) => {
        const newRes = new ArrayBuffer(res.byteLength + data.byteLength);
        const resView = new Uint8Array(newRes);
        resView.set(new Uint8Array(res));
        resView.set(new Uint8Array(data), res.byteLength);
        res = newRes;
        console.info('res length: ', res.byteLength);
      });
      httpRequest.on('dataEnd', () => {
        try {
          let textDecoderOptions: util.TextDecoderOptions = {
            ignoreBOM: true
          };
          let decoder = util.TextDecoder.create('utf-8', textDecoderOptions);
          let str = decoder.decodeToString(new Uint8Array(res));
          console.info('test json read successful: ', str);
          let jsonStr = json.parse(str);
          resolve(jsonStr);
        } catch (err) {
          hilog.error(0x0000, 'testTag', `error: ${(err as BusinessError).code} ${(err as BusinessError).message}`);
        }
      });
      httpRequest.requestInStream('json文件的网络地址', // 后台服务器地址
        {
          method: http.RequestMethod.GET,
          header: {
            'Content-Type': 'application/json'
          },
          connectTimeout: 6000,
          readTimeout: 6000,
        }, (err, data) => {
          if (!err) {
            console.info('data: ', data);
          }
        }
      );
    });
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
