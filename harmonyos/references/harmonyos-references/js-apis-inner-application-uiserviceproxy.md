---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiserviceproxy
title: UIServiceProxy
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > UIServiceProxy
category: harmonyos-references
scraped_at: 2026-04-28T07:58:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:81225128784b98baa5287720cc8cab44b9fe64e811faab0a0f58ddab4924cb58
---

UIServiceProxy提供代理能力，可以从UIServiceExtension客户端发送数据到服务端。

说明

* 本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## UIServiceProxy.sendData

PhonePC/2in1TabletTVWearable

sendData(data: Record<string, Object>): void

给UIServiceExtension服务端发送数据。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从 API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 待发送给UIServiceExtension服务端的数据。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = '[Extension] ';

6. @Entry
7. @Component
8. struct UIServiceExtensionAbility {
9. comProxy: common.UIServiceProxy | null = null;
10. dataCallBack: common.UIServiceExtensionConnectCallback = {
11. onData: (data: Record<string, Object>) => {
12. console.info(`${TAG} dataCallBack received data: ${JSON.stringify(data)}.`);
13. },
14. onDisconnect: () => {
15. console.info(`${TAG} dataCallBack onDisconnect.`);
16. this.comProxy = null;
17. }
18. }

20. build() {
21. Scroll() {
22. Column() {
23. // 创建一个连接UIServiceExtension的按钮
24. Button('connectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
25. .margin({
26. top: 5,
27. left: 10,
28. right: 10,
29. bottom: 5
30. })
31. .alignRules({
32. center: { anchor: '__container__', align: VerticalAlign.Center },
33. middle: { anchor: '__container__', align: HorizontalAlign.Center }
34. })
35. .onClick(() => {
36. this.myConnectUIServiceExtensionAbility()
37. });
38. }
39. .width('100%')
40. }
41. .height('100%')
42. }

44. // 自定义连接UIServiceExtension的函数
45. myConnectUIServiceExtensionAbility() {
46. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
47. let startWant: Want = {
48. deviceId: '',
49. bundleName: 'com.acts.myapplication',
50. abilityName: 'UiServiceExtensionAbility'
51. };

53. try {
54. // 连接UIServiceExtension
55. context.connectUIServiceExtensionAbility(startWant, this.dataCallBack)
56. .then((proxy: common.UIServiceProxy) => {
57. console.info(TAG + `try to connectUIServiceExtensionAbility ${proxy}}`);
58. this.comProxy = proxy;
59. let formData: Record<string, string> = {
60. 'PATH': '/tmp/aaa.jpg'
61. };
62. try {
63. console.info(`${TAG} sendData.`);
64. // 给UIServiceExtension发送数据
65. this.comProxy.sendData(formData);
66. } catch (err) {
67. let code = (err as BusinessError).code;
68. let message = (err as BusinessError).message;
69. console.error(`${TAG} sendData failed, code is ${code}, message is ${message}.`);
70. }
71. }).catch((err: Error) => {
72. let code = (err as BusinessError).code;
73. let message = (err as BusinessError).message;
74. console.error(`${TAG} connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.`);
75. });
76. } catch (err) {
77. let code = (err as BusinessError).code;
78. let message = (err as BusinessError).message;
79. console.error(`${TAG} connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.`);
80. }
81. }
82. }
```
