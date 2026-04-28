---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-se-access-guide
title: 安全单元访问开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > NFC > 安全单元访问开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b26110be3a554df004827b2612c123ea8507570da6087904be31e3f9d9d592cc
---

## 简介

电子设备上可能存在一个或多个安全单元（SecureElement，简称SE），比如有eSE(Embedded SE)和SIM卡。安全单元的访问控制，通过GPAC（GlobalPlatform Access Control）规范实现。

## 场景介绍

应用程序可以通过接口访问安全单元，比如往安全单元里面写入数据，实现在电子设备上模拟一张NFC卡片的目的。该卡片数据可能存储在eSE安全单元，或在SIM卡安全单元上。安全单元上一般会预置有访问控制规则（GPAC规范），应用程序需要具备对应的权限，参考[安全单元接口](../harmonyos-references/js-apis-secureelement.md)，也就是通过安全单元的访问控制权限校验之后，才能正常访问安全单元。

## 接口说明

安全单元完整的API说明以及示例代码请参考：[安全单元接口](../harmonyos-references/js-apis-secureelement.md)。

实现安全单元的访问，需要使用到下面的接口。

| 接口名 | 支持版本 | 功能描述 |
| --- | --- | --- |
| createService(): Promise<SEService> | 从API version 12开始支持 | 建立一个可用于连接到系统中所有可用SE的新连接。 |
| getReaders(): Reader[] | 从API version 10开始支持 | 返回可用SE Reader的数组，包含该设备上支持的所有的安全单元。 |
| openSession(): Session | 从API version 10开始支持 | 在SE Reader实例上创建连接会话，返回Session实例。 |
| openLogicalChannel(aid: number[]): Promise<Channel> | 从API version 10开始支持 | 打开逻辑通道，返回逻辑Channel实例对象。 |
| transmit(command: number[]): Promise<number[]> | 从API version 10开始支持 | 向SE发送APDU数据 |
| close(): void | 从API version 10开始支持 | 关闭Channel。 |

## 主要场景开发步骤

### 应用程序访问安全单元

1. import需要的安全单元模块。
2. 判断设备是否支持安全单元能力。
3. 访问安全单元，实现数据的读取或写入。
4. 释放通道资源。

注意

* 从API version 9之后的应用开发新增支持[Stage模型](ability-terminology.md#stage模型)，作为目前主推并长期演进的模型。
* 由于SE的安全级别较高，必须将构建模式设置为release进行打包，否则应用将无法正常运行。

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

6. let seService: omapi.SEService;
7. let seReaders: omapi.Reader[];
8. let seSession: omapi.Session;
9. let seChannel: omapi.Channel;
10. let testSelectedAid: number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
11. let p2: number = 0x00;

13. export default class EntryAbility extends UIAbility {
14. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
15. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

17. // 判断设备是否支持安全单元能力
18. if (!canIUse("SystemCapability.Communication.SecureElement")) {
19. hilog.error(0x0000, 'testTag', 'secure element unavailable.');
20. return;
21. }
22. hilog.info(0x0000, 'testTag', 'secure element available.');
23. this.omaTest();
24. }

26. private async omaTest() {
27. // 创建安全单元service，用于访问安全单元
28. await omapi.createService().then((data) => {
29. if (data == undefined || !data.isConnected()) {
30. hilog.error(0x0000, 'testTag', 'secure element service disconnected.');
31. return;
32. }
33. seService = data;
34. hilog.info(0x0000, 'testTag', 'secure element service connected.');
35. }).catch((error: BusinessError) => {
36. hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
37. return;
38. });

40. // 获取设备上所有支持的readers，即所有的安全单元列表
41. try {
42. seReaders = seService.getReaders();
43. } catch (error) {
44. hilog.error(0x0000, 'testTag', 'getReaders error %{public}s', JSON.stringify(error));
45. }
46. if (seReaders == undefined || seReaders.length == 0) {
47. hilog.error(0x0000, 'testTag', 'no valid reader found.');
48. seService.shutdown();
49. return;
50. }

52. // 根据业务需求，选择一个安全单元来访问，比如选择eSE或SIM或SIM2，其中SIM2从API version 22开始支持
53. let reader: (omapi.Reader | undefined);
54. for (let i = 0; i < seReaders.length; ++i) {
55. let r = seReaders[i];
56. // 安全单元的Name来区分，比如是eSE或SIM或SIM2
57. if (r.getName() === 'SIM') {
58. reader = r;
59. break;
60. }
61. }
62. if (reader == undefined) {
63. hilog.error(0x0000, 'testTag', 'no valid sim reader.');
64. seService.shutdown();
65. return;
66. }
67. hilog.info(0x0000, 'testTag', 'reader is %{public}s', reader?.getName());

69. // 在选定的一个安全单元实例上，打开一个会话session
70. try {
71. seSession = reader?.openSession() as omapi.Session;
72. } catch (error) {
73. hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
74. }
75. if (seSession == undefined) {
76. hilog.error(0x0000, 'testTag', 'seSession invalid.');
77. seService.shutdown();
78. return;
79. }

81. // 通过会话session实例，创建逻辑通道或基础通道，一般选择逻辑通道访问，因为基础通道可能是受限的
82. try {
83. // testSelectedAid 根据实际业务，修改为打开逻辑通道的应用的aid值
84. seChannel = await seSession.openLogicalChannel(testSelectedAid, p2);
85. } catch (exception) {
86. hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
87. }

89. if (seChannel == undefined) {
90. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
91. seService.shutdown();
92. return;
93. }

95. // 使用通道发送APDU数据到安全单元，testApduData根据实际业务，修改为正确的业务数据值。所填充的APDU数据格式，需要符合APDU规范。
96. let testApduData = [0x01, 0x02, 0x03, 0x04];
97. try {
98. let response: number[] = await seChannel.transmit(testApduData);
99. hilog.info(0x0000, 'testTag', 'seChannel.transmit() response = %{public}s.', JSON.stringify(response));
100. } catch (exception) {
101. hilog.error(0x0000, 'testTag', 'seChannel.transmit() exception = %{public}s.', JSON.stringify(exception));
102. }

104. // 通道访问结束后，必须确保通道资源是关闭的
105. try {
106. seChannel.close();
107. } catch (exception) {
108. hilog.error(0x0000, 'testTag', 'seChannel.close() exception = %{public}s.', JSON.stringify(exception));
109. }

111. // 关闭服务资源，关闭应用程序和安全单元服务的绑定关系
112. seService.shutdown();
113. }
114. }
```
