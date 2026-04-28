---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-5
title: 如何获取网络类型：Wi-Fi，3G，4G等
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何获取网络类型：Wi-Fi，3G，4G等
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a8589f2004767101d04efa6fc0f1d2a076dd9a82b39a1ebaa0c40d36bb0ab46e
---

先通过[getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)去获取网络的类型，判断默认网络是Wi-Fi还是蜂窝。

如果是Wi-Fi，则直接确认网络类型是Wi-Fi。如果是在蜂窝连接情况下，可以调用[radio.getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)获取指定SIM卡槽对应的注册网络信号强度信息列表，返回[SignalInformation](../harmonyos-references/js-apis-radio.md#signalinformation)对象的数组，其中，返回的signalType代表[网络类型NetworkType](../harmonyos-references/js-apis-radio.md#networktype)，signalType的值对应网络类型如下：

* GSM：2G
* CDMA：2G
* WCDMA：3G
* TDSCDMA：3G
* LTE：4G

具体可参考如下示例代码：

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { radio } from '@kit.TelephonyKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Column() {
10. Button('获取网络类型')
11. .type(ButtonType.Normal)
12. .width(200)
13. .height(200)
14. .onClick(() => {
15. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
16. if (netHandle.netId == 0) {
17. // When there is currently no connected network, the obtained netHandler's netid is 0, which belongs to an abnormal scenario.
18. // Here, some processing mechanisms can be added according to the actual situation.
19. return;
20. }
21. // Obtain the capability information of the network corresponding to netHandle
22. connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
23. if (error) {
24. console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
25. return;
26. }
27. console.info("Succeeded to get data: " + JSON.stringify(data));
28. if (data.bearerTypes[0] == 1) {
29. // console.info("Wi Fi network");
30. } else if (data.bearerTypes[0] == 0) {
31. // console.info("Cellular Network");
32. let slotId: number = 0; // Slot ID, -0: Slot 1, -1: Slot 2
33. radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
34. if (err) {
35. console.error(`getSignalInformation failed, callback: err->${JSON.stringify(err)}`);
36. return;
37. }
38. console.info(`getSignalInformation success, callback: data->${JSON.stringify(data)}`);
39. // Return an array of SignalInformation objects, where the returned signalType represents the network type NetworkType
40. });
41. }
42. })
43. }).catch((error: BusinessError) => {
44. console.error('error: ' + JSON.stringify(error));
45. });
46. })
47. }
48. .width('100%')
49. .height('100%')
50. .alignItems(HorizontalAlign.Center)
51. .justifyContent(FlexAlign.Center)
52. }
53. }
```

[GetNetCapabilities.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ConnectivityKit/entry/src/main/ets/pages/GetNetCapabilities.ets#L21-L73)
