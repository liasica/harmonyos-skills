---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-71
title: 如何判断当前网络的IP地址版本是多少
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何判断当前网络的IP地址版本是多少
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d67465b1f80caf273d0452e5ffe710559c573d75707f2598fa0b216b6473fd78
---

使用[NetAddress](../harmonyos-references/js-apis-net-connection.md#netaddress)类获取当前网络的地址信息，NetAddress类的family属性用于指定IP地址的版本，family属性的值为1表示IPv4，为2表示IPv6 。

示例代码如下：

```
1. import { connection } from '@kit.NetworkKit';

3. @Entry
4. @Component
5. struct Index {
6. getNetworkFamily() {
7. try {
8. let netHandle = connection.getDefaultNetSync();
9. let connectionProperties = connection.getConnectionPropertiesSync(netHandle);
10. if (connectionProperties !== undefined) {
11. let linkAddressesArray = connectionProperties.linkAddresses;
12. if (linkAddressesArray !== undefined && linkAddressesArray instanceof Array && linkAddressesArray.length > 0) {
13. for (let i = 0; i < linkAddressesArray.length; i++) {
14. let address: connection.NetAddress = linkAddressesArray[i].address;
15. if (address !== undefined) {
16. console.info("Succeeded to get address: " + JSON.stringify(address))
17. if (address.family === 1) {
18. console.info('Current network IP address version is ipv4')
19. } else if (address.family === 2) {
20. console.info('Current network IP address version is ipv6')
21. }
22. }
23. }
24. }
25. }
26. } catch (e) {
27. console.error(`Get exception: ${e}`);
28. }
29. }

31. build() {
32. Column({ space: 10 }) {
33. Button('获取当前网络IP地址版本')
34. .onClick(() => {
35. this.getNetworkFamily();
36. })
37. }
38. .alignItems(HorizontalAlign.Center)
39. .height('100%')
40. .width('100%')
41. }
42. }
```

[GetNetworkFamily](https://gitcode.com/harmonyos_samples/faqsnippets/blob/9599520cea2cd471e1e3ed244c5fc384697af3e6/NetworkKit/entry/src/main/ets/pages/GetNetworkFamily#L21-L62)
