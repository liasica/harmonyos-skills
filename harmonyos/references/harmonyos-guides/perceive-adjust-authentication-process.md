---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/perceive-adjust-authentication-process
title: 感知和调整认证过程
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 用户身份认证开发指导 > 感知和调整认证过程
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:25+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8819d4d145aa85de852cda00d21dd47f67977df38e4f10ce176bf037d7cd5f54
---

从API version 20开始，在应用发起身份认证时，可通过接口调整认证过程，以及感知认证过程。

调整认证过程：应用发起认证时通过[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)参数的skipLockedBiometricAuth属性控制是否跳过已禁用的生物认证。

感知认证过程：通过[on('authTip')](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)接口注册回调来获取认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证失败结果。正确的顺序为先通过on注册回调，再通过[start](../harmonyos-references/js-apis-useriam-userauth.md#start10)发起认证，start成功发起认证后on注册的回调才会收到信息。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[@ohos.userIAM.userAuth (用户认证)](../harmonyos-references/js-apis-useriam-userauth.md)。

| 接口名称 | 功能描述 |
| --- | --- |
| AuthParam | 用户认证相关参数，包括挑战值、认证类型列表、认证等级等。  可通过skipLockedBiometricAuth参数控制是否跳过禁用的生物认证。  true表示生物认证冻结时自动跳过倒计时界面直接切换到其他方式的认证。  false表示不跳过；默认为false。 |
| on(type: 'authTip', callback: AuthTipCallback): void | 订阅身份认证过程中的提示信息。 |
| off(type: 'authTip', callback?: AuthTipCallback): void | 取消订阅认证过程中的提示信息。 |

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)（包括挑战值、认证类型[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)列表和认证等级[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)）、配置认证控件界面[WidgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)，调用[getUserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserauthinstance10)获取认证对象。
3. 调用[UserAuthInstance.on('authTip')](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)接口订阅身份认证过程中的提示信息。
4. 调用[UserAuthInstance.start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口发起认证，通过[AuthTipCallback](../harmonyos-references/js-apis-useriam-userauth.md#authtipcallback20)回调返回认证中间状态[AuthTipInfo](../harmonyos-references/js-apis-useriam-userauth.md#authtipinfo20)。
5. 认证成功后，调用[UserAuthInstance.off('authTip')](../harmonyos-references/js-apis-useriam-userauth.md#offauthtip20)接口取消订阅认证过程中的提示信息。

以跳过禁用的生物认证，订阅认证信息为例：

```
1. perceiveAndAdjustAuthentication() {
2. try {
3. const randData = getRandData();
4. if (!randData) {
5. return;
6. }
7. // 设置认证参数
8. const authParam: userAuth.AuthParam = {
9. challenge: randData,
10. authType: [userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT],
11. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
12. skipLockedBiometricAuth: true
13. };
14. // 配置认证界面
15. const widgetParam: userAuth.WidgetParam = {
16. title: resourceToString($r('app.string.title')),
17. };
18. // 获取认证对象
19. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
20. Logger.info('get userAuth instance successfully.');
21. // 订阅认证过程中的提示信息。
22. userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
23. try {
24. Logger.info('userAuthInstance callback.');
25. this.result[ResultIndex.PERCEIVE_ADJUST] = (`${authTipInfo.tipType}`);
26. // 认证完成后取消订阅
27. userAuthInstance.off('result');
28. } catch (error) {
29. const err: BusinessError = error as BusinessError;
30. Logger.error(`onResult failed, code: ${err?.code}, Message: ${err?.message}`);
31. }
32. });
33. // 开始认证
34. userAuthInstance.start();
35. // ...
36. // 取消订阅认证过程中的提示信息。
37. userAuthInstance.off('authTip');
38. Logger.info('off authTip successfully.');
39. // 取消认证
40. userAuthInstance.cancel();
41. Logger.info('auth cancel successfully.');
42. // ...
43. } catch (error) {
44. const err: BusinessError = error as BusinessError;
45. Logger.error(`auth failed, code is ${err?.code as number}, message is ${err?.message}`);
46. }
47. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L401-L455)

## 示例代码

* [感知和调整认证过程](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
