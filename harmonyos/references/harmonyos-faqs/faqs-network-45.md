---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-45
title: 如何判断使用的是移动蜂窝网络
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何判断使用的是移动蜂窝网络
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ecd3ebf223100ae26ab1cbaae947ea1130176fe02ccbc042c9bced104bf280b
---

使用@kit.NetworkKit中的connection.getNetCapabilities接口获取网络能力信息。如果返回结果中bearerTypes的值为 0，表示移动蜂窝网络，否则表示其他网络。需要权限：ohos.permission.GET\_NETWORK\_INFO。

参考代码如下：

```typescript
import { connection } from '@kit.NetworkKit';

// Check if the network is connected
connection.hasDefaultNet((error, data) => {
  console.log('data: ' + data);
})
// Obtain network capability information
connection.getDefaultNet().then((netHandle) => {
  connection.getNetCapabilities(netHandle, (error, data) => {
    console.log(JSON.stringify(error));
    console.log(JSON.stringify(data));
  })
})
```

**参考链接**

[connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)

[NetBearType](../harmonyos-references/js-apis-net-connection.md#netbeartype)
