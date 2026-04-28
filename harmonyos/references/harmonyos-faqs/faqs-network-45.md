---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-45
title: 如何判断使用的是移动蜂窝网络
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何判断使用的是移动蜂窝网络
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:10+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:1c33e5a96e5948fd5834c6df7f2eaad23e5e848eb080b55e786495675e68af7f
---

使用@kit.NetworkKit中的connection.getNetCapabilities接口获取网络能力信息。如果返回结果中bearerTypes的值为 0，表示移动蜂窝网络，否则表示其他网络。需要权限：ohos.permission.GET\_NETWORK\_INFO。

参考代码如下：

```
1. import { connection } from '@kit.NetworkKit';

3. // Check if the network is connected
4. connection.hasDefaultNet((error, data) => {
5. console.log('data: ' + data);
6. })
7. // Obtain network capability information
8. connection.getDefaultNet().then((netHandle) => {
9. connection.getNetCapabilities(netHandle, (error, data) => {
10. console.log(JSON.stringify(error));
11. console.log(JSON.stringify(data));
12. })
13. })
```

[SetNetType.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetNetType.ets#L21-L33)

**参考链接**

[connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)

[NetBearType](../harmonyos-references/js-apis-net-connection.md#netbeartype)
