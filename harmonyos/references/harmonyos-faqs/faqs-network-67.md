---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-67
title: 如何监听判断VPN类型网络
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何监听判断VPN类型网络
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d0bd17d77504ebfe089acc4f5797f9a6f285f2d2c72295a8ea118eee85a94b89
---

VPN类型可使用getNetCapabilities方法获取到bearerTypes，当[bearerTypes](../harmonyos-references/js-apis-net-connection.md#netbeartype)的值是4时表示使用了VPN。需要权限：ohos.permission.INTERNET、ohos.permission.GET\_NETWORK\_INFO。

参考代码如下：

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. export struct JudeNetType {
7. getNetType() {
8. connection.getAllNets((error: BusinessError, allNets: connection.NetHandle[]) => {
9. if (error) {
10. console.error(`Failed to get getAllNets. Code: ${error.code}, message: ${error.message}`);
11. return;
12. }
13. for (let netHandle of allNets) {
14. connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
15. if (error) {
16. console.error(`Failed to get capabilities. Code: ${error.code}, message: ${error.message}`);
17. return;
18. }
19. if (data.bearerTypes[0] == connection.NetBearType.BEARER_VPN) {
20. console.info('The VPN network is connected');
21. }
22. })
23. }
24. });
25. }

27. build() {
28. Column({ space: 10 }) {
29. Button('Obtain the type of network connection').onClick(() => {
30. this.getNetType()
31. })
32. }.alignItems(HorizontalAlign.Center)
33. .height('100%')
34. .width('100%')
35. }
36. }
```

[OnNetVpn.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/OnNetVpn.ets#L21-L57)

参考文档：[网络连接管理](../harmonyos-references/js-apis-net-connection.md#netbeartype)
