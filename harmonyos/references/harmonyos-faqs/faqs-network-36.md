---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-36
title: ArkTS中HTTP请求如何以JSON形式进行传输
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > ArkTS中HTTP请求如何以JSON形式进行传输
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4b67f5e1c2e8aef4e6aa6fe800e891c8ecf2289f53c2146ecaf9d8f4df4fad11
---

HTTP协议消息头中，Content-Type表示媒体类型。

设置参数值为application/json。请求中的数据将以JSON形式传输。参考代码如下：

```
1. import { http } from '@kit.NetworkKit';

3. class Header {
4. public contentType: string;
5. constructor(contentType: string) {
6. this.contentType = contentType;
7. }
8. }
9. let httpRequest = http.createHttp();
10. let promise = httpRequest.request("EXAMPLE_URL", {
11. method: http.RequestMethod.GET,
12. connectTimeout: 60000,
13. readTimeout: 60000,
14. header: new Header('application/json')
15. });
```

[RequestJson.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/RequestJson.ets#L21-L35)

**参考链接**

[request](../harmonyos-references/js-apis-http.md#request)
