---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-36
title: ArkTS中HTTP请求如何以JSON形式进行传输
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > ArkTS中HTTP请求如何以JSON形式进行传输
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7e4ffb6d876e06359396a8145560227dbb940457822d6bd8e7bcf49a3722ca1a
---

HTTP协议消息头中，Content-Type表示媒体类型。

设置参数值为application/json。请求中的数据将以JSON形式传输。参考代码如下：

```typescript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;
  constructor(contentType: string) {
    this.contentType = contentType;
  }
}
let httpRequest = http.createHttp();
let promise = httpRequest.request("EXAMPLE_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});
```

**参考链接**

[request](../harmonyos-references/js-apis-http.md#request)
