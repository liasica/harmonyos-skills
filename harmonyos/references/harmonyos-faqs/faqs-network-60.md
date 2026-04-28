---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-60
title: 如何解决网络连接状态变化的公共事件返回内容为"NetType":1的问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决网络连接状态变化的公共事件返回内容为"NetType":1的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:62a5219a33264ca06d2db3588a7da663a8a4d4f73be85a187077b7f5f0a9a74e
---

返回"NetType":1枚举值表示为NET\_CONN\_STATE\_IDLE网络空闲状态。

如果是监听网络变化，建议使用@ohos.net.connection的能力，请参考[@ohos.net.connection (网络连接管理)](../harmonyos-references/js-apis-net-connection.md)。

代码示例如下：

```
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

4. function  listen_network() {
5. let netSpecifier: connection.NetSpecifier = {
6. netCapabilities: {
7. //Assuming the current default network is WiFi, a cellular network connection needs to be created, and the network type can be specified as cellular network
8. bearerTypes: [connection.NetBearType.BEARER_CELLULAR, connection.NetBearType.BEARER_WIFI],
9. },
10. };
11. let conn = connection.createNetConnection(netSpecifier);

13. conn.register((err: BusinessError, data: void) => {
14. console.warn('register Network ' + JSON.stringify(err))
15. });

17. // Subscription event, network available
18. conn.on('netAvailable', ((data: connection.NetHandle) => {
19. console.warn('Network available, netId is ' + data.netId);
20. }));

22. // Subscription event, network available
23. conn.on('netCapabilitiesChange', ((data: connection.NetCapabilityInfo) => {
24. console.warn('Network netCapabilitiesChange bearerTypes ' + data.netCap.bearerTypes);
25. console.warn('Network netCapabilitiesChange networkCap ' + data.netCap.networkCap);
26. }));

28. // Subscription event, network unavailable
29. conn.on('netUnavailable', ((data: void) => {
30. console.warn('The network is unavailable, data is ' + JSON.stringify(data));
31. }));

33. // Subscription event, network disconnection
34. conn.on('netLost', ((data: connection.NetHandle) => {
35. console.warn('Network lost, netId is ' + data.netId);
36. }));
37. }

39. // After monitoring an event, it is necessary to obtain the network status through a network interface
40. function sub_network() {
41. console.warn('into sub_network')
42. // Public event monitoring code:
43. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
44. // Subscription message exception public event
45. events: ['usual.event.CONNECTIVITY_CHANGE']
46. }

48. // Create subscriber callback
49. commonEventManager.createSubscriber(subscribeInfo, (err: BusinessError, subscriber: commonEventManager.CommonEventSubscriber) => {
50. if (err) {
51. console.warn(`Failed to create netWorkSubscribeInfo. Code is ${err.code}, message is ${err.message}`);
52. return;
53. }
54. if (subscribeInfo && subscribeInfo != null) {
55. // Subscribe to public event callbacks
56. commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
57. if (err) {
58. console.warn(`Failed to netWorkSubscribe common event. Code is ${err.code}, message is ${err.message}`);
59. return;
60. }
61. console.warn('NET_CONNECTIVITY_CHANGE：' + JSON.stringify(data.parameters));

63. setTimeout(async () => {
64. connection.getDefaultNet((error, data) => {
65. console.log(JSON.stringify(error))
66. console.log(JSON.stringify(data))
67. }) }, 500);
68. // The log printed here is{'NetType':1,'moduleName':''}
69. })
70. }
71. })
72. }

74. @Entry
75. @Component
76. struct NetWork {
77. build() {
78. Row() {
79. Column() {
80. Button('Monitor the network').onClick(() => {
81. listen_network()
82. })
83. Button('Obtain the network status').onClick(() => {
84. sub_network()
85. })
86. }
87. .width('100%')
88. }
89. .height('100%')
90. }
91. }
```

[SetNetSpecifier.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetNetSpecifier.ets#L21-L111)
