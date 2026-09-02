---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-48
title: 如何实现http长连接
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何实现http长连接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:01fe555499ebeece5d83e50925593a9fc6733e210b07ccb9027fa06a2878c795
---

可使用定时HTTP请求模拟长连接。参考代码如下：

```screen
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
// 设置5秒轮询一次
setInterval(() => {
  httpRequest.request("EXAMPLE_URL", {
    method: http.RequestMethod.GET,
    connectTimeout: 60000,
    readTimeout: 60000
  }, (err, data) => {
    if (!err) {
      console.info('Received data:', JSON.stringify(data.result));
    } else {
      console.info('Polling error:', JSON.stringify(err));
    }
  })
}, 5000)
```
