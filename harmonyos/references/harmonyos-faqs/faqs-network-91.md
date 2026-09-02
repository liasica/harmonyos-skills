---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-91
title: 客户端如何根据服务器返回的内容自定义设置http请求头字段
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 客户端如何根据服务器返回的内容自定义设置http请求头字段
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a28515df703cfb41331331fdfa7843ac835a66c1d67e39789683f543454e86b4
---

## 问题现象

在多个场景中，客户端需根据业务具体需求自定义设置http请求头字段，例如根据服务器返回的内容动态调整请求参数。这种情况下，客户端应如何自定义设置http请求头字段？

## 背景知识

[http数据请求](../atomic-guides/atomic-http-request.md)：应用通过http发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、TRACE、CONNECT方法。

## 解决方案

http请求的请求头为Object类型，本来就支持动态设置。

**说明** 

需要自定义类型来接收响应数据。

1. 客户端：向服务器发送GET请求，以对象（具体格式需与服务端对齐）为header参数询问服务端有哪些商品类型。

   ```ts
   get('goods', (data: Object) => {
     let goods: Goods = JSON.parse(data.toString());
     let type = goods.goods;
     console.info(type);
     // 依据服务器返回的商品类型再请求具体的商品列表。
     get(type!, (data: Object) => {
       let sorts: Shoes = JSON.parse(data.toString());
       this.shoes = sorts.shoes;
       let s: Clothing = JSON.parse(data.toString());
       this.clothing = s.clothing;
     });
   });
   ```
2. 服务端：随机返回当前服务器上存在的商品类型。

   ```ts
   if (type === "goods") {
     // 客户端请求商品类型时随机返回 clothing 或 shoes
     res.json({ "goods": Math.random() > 0.5 ? "clothing" : "shoes" })
   }
   ```
3. 客户端：依据服务端返回的商品类型请求商品列表。

   ```ts
   get(type!, (data: Object) => {
     let sorts: Shoes = JSON.parse(data.toString());
     this.shoes = sorts.shoes;
     let s: Clothing = JSON.parse(data.toString());
     this.clothing = s.clothing;
   });
   ```

完整示例参考如下：

客户端ArkTS代码：

```ts
import http from '@ohos.net.http';
import { BusinessError } from '@ohos.base';

interface Goods {
  goods: string;
}

interface Shoes {
  shoes: string[];
}

interface Clothing {
  clothing: string[];
}

let httpRequest = http.createHttp();
httpRequest.on('headersReceive', (header) => {
  console.info(`header: ${JSON.stringify(header)}`);
});

function get(type: string, f: (data: Object) => void) {
  httpRequest.request(
    // 服务器url，运行服务器的电脑连手机wifi时可直接用ip代替域名。
    'http://x.x.x.x:9588',
    {
      method: http.RequestMethod.GET,
      // header字段为Object，支持动态设置。
      header: {
        'type': type
      },
      connectTimeout: 10000, // 可选，默认为60000ms.
      readTimeout: 10000, // 可选，默认为60000ms.
    }, (err: BusinessError, data: http.HttpResponse) => {
    if (!err) {
      f(data.result);
    } else {
      console.error(`error code:${err.code}, error message:${err.message}`);
      // 取消订阅http响应头事件。
      httpRequest.off('headersReceive');
    }
  }
  );
}

@Entry
@Component
struct Index {
  private message: string = '获取商品';
  @State shoes: string[] | undefined = [];
  @State clothing: string[] | undefined = [];

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('get')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 先发请求询问有哪些商品类型，服务器随机返回shoes或clothing.
          get('goods', (data: Object) => {
            let goods: Goods = JSON.parse(data.toString());
            let type = goods.goods;
            console.info(type);
            // 依据服务器返回的商品类型再请求具体的商品列表。
            get(type!, (data: Object) => {
              let sorts: Shoes = JSON.parse(data.toString());
              this.shoes = sorts.shoes;
              let s: Clothing = JSON.parse(data.toString());
              this.clothing = s.clothing;
            });
          });
        });
      Text('获取的商品如下')
        .id('info')
        .alignRules({
          top: { anchor: 'get', align: VerticalAlign.Bottom },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .margin({ top: '5%' });
      Row() {
        ForEach(this.shoes, (item: string) => {
          Text(item);
        });
        ForEach(this.clothing, (item: string) => {
          Text(item);
        });
      }
      .id('shoes')
      .alignRules({
        top: { anchor: 'info', align: VerticalAlign.Bottom },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .backgroundColor(Color.Yellow)
      .margin({ top: '5%' });
    }
    .height('100%')
    .width('100%');
  }
}
```

服务器端js代码：

```java
const express = require('express');
const app = express();

/* GET home page. */
app.get('/', function (req, res, next) {
  let header = req.headers;
  console.log(JSON.stringify(header))
  let type = header.type;
  if (type === "goods") {
    // 客户端请求商品类型时随机返回 clothing 或 shoes
    res.json({ "goods": Math.random() > 0.5 ? "clothing" : "shoes" })
  }
  if (type === "clothing") {
    // 客户端请求clothing则返回clothing列表
    res.json({ "clothing": ["coat", "shirt", "jacket"] })
  }
  if (type === "shoes") {
    // 客户端请求shoes则返回shoes列表
    res.json({ "shoes": ["slippers", "sneakers", "high heels"] })
  }
  res.send('Home Page');
});

app.listen(9588, () => {
  console.info('服务器启动成功');
});

module.exports = app;
```

## 常见FAQ

Q：http请求报2300023错误。

A：[http请求报2300023错误常见排查思路](../harmonyos-references/errorcode-net-http.md#section2300023-向磁盘应用程序写入接收数据失败)。

Q：http请求如何下载比较大的数据？

A：如果接收超过5M的数据，需要在[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)的maxLimit中进行设置。

Q：http请求头字段的默认值是什么？

A：当请求方式为"POST"、"PUT"、"DELETE"或者""时，默认{'content-Type': 'application/json'}，否则默认{'content-Type': 'application/x-www-form-urlencoded'}。header等请求参数的类型与取值范围参见[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)。

Q：网络请求频繁2300028，如何排查？

A：TCP连接超时或读写超时，排查网络或服务器问题，例如网络是否稳定、信号强度是否较弱、服务器负载是否过高、处理速度是否正常等。

Q：网络请求是有数据长度限制吗？

A：expectDataType当指定其类型为Object时，最大长度为65536。

Q：HttpRequestOptions里面的method为GET时，extraData如果为Object，参数内容会拼接到url中进行发送。实际开发测试过程中，发现并没有拼接到url中。

A：Object的key-value作为string即可，如：extraData: {'start':'0','limit':'20'}。

## 总结

该方案中服务器端采用express搭建，新建项目后将index.js文件替换为demo中的服务器端代码即可运行，注意服务器ip地址的设置。
