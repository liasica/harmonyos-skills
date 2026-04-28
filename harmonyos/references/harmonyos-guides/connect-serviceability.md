---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/connect-serviceability
title: 连接ServiceAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > ServiceAbility组件开发指导 > 连接ServiceAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4ff75f874b36ecc1714d8a083cebd5e4762751257b50dcd3a9e67d6101d5ef53
---

如果ServiceAbility需要与PageAbility或其他应用的ServiceAbility进行交互，则须创建用于连接的Connection。ServiceAbility支持其他Ability通过[connectAbility()](../harmonyos-references/js-apis-ability-featureability.md#featureabilityconnectability7)方法与其进行连接。PageAbility的connectAbility()方法定义在[featureAbility](../harmonyos-references/js-apis-ability-featureability.md)中，ServiceAbility的connectAbility()方法定义在[particleAbility](../harmonyos-references/js-apis-ability-particleability.md)中。连接ServiceAbility的规则详见[组件启动规则](component-startup-rules-fa.md)章节。在使用connectAbility()处理回调时，需要传入目标Service的[Want](../harmonyos-references/js-apis-app-ability-want.md)与[IAbilityConnection](../harmonyos-references/js-apis-inner-ability-connectoptions.md)的实例。[IAbilityConnection](../harmonyos-references/js-apis-inner-ability-connectoptions.md)提供了以下方法供开发者实现。

**表1** IAbilityConnection接口说明

| 接口名 | 描述 |
| --- | --- |
| onConnect() | 用于处理连接Service成功的回调。 |
| onDisconnect() | 用来处理Service异常死亡的回调。 |
| onFailed() | 用来处理连接Service失败的回调。 |

PageAbility创建连接本地ServiceAbility回调实例的代码以及连接本地ServiceAbility的示例代码如下：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import common from '@ohos.app.ability.common';
3. import Want from '@ohos.app.ability.Want';
4. import promptAction from '@ohos.promptAction';
5. import rpc from '@ohos.rpc';
6. import hilog from '@ohos.hilog';
```

```
1. const TAG: string = 'PageServiceAbility';
2. const domain: number = 0xFF00;

4. @Entry
5. @Component
6. struct PageServiceAbility {
7. // ...
8. build() {
9. Column() {
10. // ...
11. List({ initialIndex: 0 }) {
12. ListItem() {
13. Row() {
14. // ...
15. }
16. .onClick(() => {
17. let option: common.ConnectOptions = {
18. onConnect: (element, proxy) => {
19. hilog.info(domain, TAG, `onConnectLocalService onConnectDone element:` + JSON.stringify(element));
20. if (proxy === null) {
21. promptAction.showToast({
22. message: 'connect_service_failed_toast'
23. });
24. return;
25. }
26. let data = rpc.MessageParcel.create();
27. let reply = rpc.MessageParcel.create();
28. let option = new rpc.MessageOption();
29. data.writeInterfaceToken('connect.test.token');
30. proxy.sendRequest(0, data, reply, option);
31. promptAction.showToast({
32. message: 'connect_service_success_toast'
33. });
34. },
35. onDisconnect: (element) => {
36. hilog.info(domain, TAG, `onConnectLocalService onDisconnectDone element:${element}`);
37. promptAction.showToast({
38. message: 'disconnect_service_success_toast'
39. });
40. },
41. onFailed: (code) => {
42. hilog.info(domain, TAG, `onConnectLocalService onFailed errCode:${code}`);
43. promptAction.showToast({
44. message: 'connect_service_failed_toast'
45. });
46. }
47. };

49. let request: Want = {
50. bundleName: 'com.samples.famodelabilitydevelop',
51. abilityName: 'com.samples.famodelabilitydevelop.ServiceAbility',
52. };
53. let connId = featureAbility.connectAbility(request, option);
54. hilog.info(domain, TAG, `onConnectLocalService onFailed errCode:${connId}`);
55. })
56. }
57. // ...
58. }
59. // ...
60. }
61. // ...
62. }
63. }
```

同时，Service侧也需要在[onConnect()](../harmonyos-references/js-apis-inner-ability-connectoptions.md#onconnect)时返回[IRemoteObject](../harmonyos-references/js-apis-rpc.md#iremoteobject)，从而定义与Service进行通信的接口。onConnect()需要返回一个IRemoteObject对象。系统提供了IRemoteObject的默认实现，开发者可以通过继承[rpc.RemoteObject](../harmonyos-references/js-apis-rpc.md#remoteobject)来创建自定义的实现类。

Service侧把自身的实例返回给调用侧的示例代码如下：

```
1. import type Want from '@ohos.app.ability.Want';
2. import rpc from '@ohos.rpc';
3. import hilog from '@ohos.hilog';

5. const TAG: string = '[Sample_FAModelAbilityDevelop]';
6. const domain: number = 0xFF00;

8. class FirstServiceAbilityStub extends rpc.RemoteObject {
9. constructor(des: Object) {
10. if (typeof des === 'string') {
11. super(des);
12. } else {
13. return;
14. }
15. }

17. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
18. hilog.info(domain, TAG, 'ServiceAbility onRemoteRequest called');
19. if (code === 1) {
20. let string = data.readString();
21. hilog.info(domain, TAG, `ServiceAbility string=${string}`);
22. let result = Array.from(string).sort().join('');
23. hilog.info(domain, TAG, `ServiceAbility result=${result}`);
24. reply.writeString(result);
25. } else {
26. hilog.info(domain, TAG, 'ServiceAbility unknown request code');
27. }
28. return true;
29. }
30. }
31. // ...
```
