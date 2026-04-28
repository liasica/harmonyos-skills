---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nner-application-uiserviceextensionconnectcallback
title: UIServiceExtensionConnectCallback
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > UIServiceExtensionConnectCallback
category: harmonyos-references
scraped_at: 2026-04-28T07:58:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ace13262259b26617be5e7b3f1e96a6e71a6b553d41055ea6cceff7644d15263
---

UIServiceExtensionConnectCallback是UIServiceExtension连接回调接口类，提供UIServiceExtension连接回调数据能力。

说明

* 本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## UIServiceExtensionConnectCallback.onData

PhonePC/2in1TabletTVWearable

onData(data: Record<string, Object>): void

接收UIServiceExtension连接的回调数据。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从 API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 接收UIServiceExtension连接回调数据。 |

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
23. // 创建一个按钮，点击按钮后连接UIServiceExtensionAbility
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

44. myConnectUIServiceExtensionAbility() {
45. // 获取上下文
46. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
47. let startWant: Want = {
48. deviceId: '',
49. bundleName: 'com.acts.myapplication',
50. abilityName: 'UiServiceExtensionAbility'
51. };

53. try {
54. // 连接到UIServiceExtensionAbility
55. context.connectUIServiceExtensionAbility(startWant, this.dataCallBack)
56. .then((proxy: common.UIServiceProxy) => {
57. console.info(TAG + `try to connectUIServiceExtensionAbility ${proxy}`);
58. this.comProxy = proxy;
59. let formData: Record<string, string> = {
60. 'PATH': '/tmp/aaa.jpg'
61. };
62. try {
63. console.info(`${TAG} sendData.`);
64. this.comProxy.sendData(formData);
65. } catch (err) {
66. let code = (err as BusinessError).code;
67. let message = (err as BusinessError).message;
68. console.error(`${TAG} sendData failed, code is ${code}, message is ${message}.`);
69. }
70. }).catch((err: Error) => {
71. let code = (err as BusinessError).code;
72. let message = (err as BusinessError).message;
73. console.error(`${TAG} connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.`);
74. });
75. } catch (err) {
76. let code = (err as BusinessError).code;
77. let message = (err as BusinessError).message;
78. console.error(`${TAG} connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.`);
79. }
80. }
81. }
```

## UIServiceExtensionConnectCallback.onDisconnect

PhonePC/2in1TabletTVWearable

onDisconnect(): void

成功断开UIServiceExtension连接的回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从 API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = '[Extension] ';

6. @Entry
7. @Component
8. struct UIServiceExtensionAbility {
9. comProxy: common.UIServiceProxy | null = null;
10. // 连接时的回调接口
11. dataCallBack: common.UIServiceExtensionConnectCallback = {
12. onData: (data: Record<string, Object>) => {
13. console.info(`${TAG} dataCallBack received data: ${JSON.stringify(data)}.`);
14. },
15. onDisconnect: () => {
16. // 连接断链后的触发
17. console.info(`${TAG} dataCallBack onDisconnect.`);
18. this.comProxy = null;
19. }
20. }

22. build() {
23. Scroll() {
24. Column() {
25. // 创建一个按钮，点击后断开已连接的UIServiceExtensionAbility
26. Button('disConnectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
27. .margin({
28. top: 5,
29. left: 10,
30. right: 10,
31. bottom: 5
32. })
33. .alignRules({
34. center: { anchor: '__container__', align: VerticalAlign.Center },
35. middle: { anchor: '__container__', align: HorizontalAlign.Center }
36. })
37. .onClick(() => {
38. this.myConnectUIServiceExtensionAbility()
39. });
40. }
41. .width('100%')
42. }
43. .height('100%')
44. }

46. myConnectUIServiceExtensionAbility() {
47. // 获取上下文
48. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
49. // 断开连接的UIServiceExtensionAbility
50. try {
51. // this.comProxy在连接成功后保存
52. context.disconnectUIServiceExtensionAbility(this.comProxy).then(() => {
53. console.info(`${TAG} disconnectUIServiceExtensionAbility success.`);
54. }).catch((err: Error) => {
55. let code = (err as BusinessError).code;
56. let message = (err as BusinessError).message;
57. console.error(`${TAG} disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.`);
58. });
59. } catch (err) {
60. let code = (err as BusinessError).code;
61. let message = (err as BusinessError).message;
62. console.error(`${TAG} disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.`);
63. }
64. }
65. }
```
