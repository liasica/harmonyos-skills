---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-70
title: connection如何获取网卡链路地址、DNS地址等信息
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > connection如何获取网卡链路地址、DNS地址等信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e9eb9d025cab137e5ac4a36ba52d92465cba4c73f4b008aaf00e65d4c50ba26c
---

使用[connection.getConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)获取netHandle对应网络的连接信息，包括网卡链路地址和DNS地址。需要权限：ohos.permission.INTERNET、ohos.permission.GET\_NETWORK\_INFO。参考代码如下：

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct GetConnectionProperties {
7. getConnectionProperties() {
8. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
9. connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
10. if (error) {
11. console.error(`Failed to get connection properties. Code:${error.code}, message:${error.message}`);
12. return;
13. }
14. console.info('Succeeded to get data: ' + JSON.stringify(data));
15. })
16. });
17. }

19. build() {
20. Column({ space: 10 }) {
21. Button('获取对应的网络连接信息')
22. .onClick(() => {
23. this.getConnectionProperties();
24. })
25. }
26. .alignItems(HorizontalAlign.Center)
27. .height('100%')
28. .width('100%')
29. }
30. }
```

[GetDns.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/GetDns.ets#L21-L50)
