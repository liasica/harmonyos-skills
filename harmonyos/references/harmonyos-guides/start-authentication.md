---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-authentication
title: 发起认证
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 用户身份认证开发指导 > 发起认证
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:25+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c7be6a60ab699f245a83d01efcc5c47cd58abf9bd026652e83c99af871db326f
---

应用发起身份认证请求，获取身份认证结果，以访问受保护的系统、服务或应用的功能和数据，包括用户个人数据。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[userAuth.getUserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserauthinstance10)。

| 接口名称 | 功能描述 |
| --- | --- |
| getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance | 获取UserAuthInstance对象，用于执行用户身份认证，并支持使用[统一用户认证控件](start-authentication.md#统一用户认证控件介绍)。 |
| on(type: 'result', callback: IAuthCallback): void | 订阅用户身份认证结果。 |
| off(type: 'result', callback?: IAuthCallback): void | 取消订阅用户身份认证结果。 |
| start(): void | 执行用户认证。 |

## 统一用户认证控件介绍

系统提供了统一用户认证控件供应用调用，使用统一用户认证控件的优势：

* 统一用户认证服务将通过该控件完成信息的识别和认证，再将认证结果返回给应用，整体过程安全可控，可以更好地保护用户的生物特征信息。
* 统一固定的UI组件样式，便于用户识别。

认证控件的样式如图所示，通过[WidgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)配置对应参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/lMHSDD6bSMSwzWALSUjT0w/zh-cn_image_0000002558764916.png?HW-CC-KV=V1&HW-CC-Date=20260429T053224Z&HW-CC-Expire=86400&HW-CC-Sign=B4DCF1CCD4C70A639BA3459457440C774F7A00DE3F429CE6D22CFFAEA6BB658E)

* 标注1：用户认证界面的标题（WidgetParam.title），不支持传空字串，最大长度为500字符。应用可在此配置符合场景的字符串，建议传入认证目的，例如用于支付、登录应用等。
* 标注2：当生物认证失败后，将显示一个按钮。点击该按钮，可以从生物认证切换到其他口令认证类型（AuthParam.authType）。

  开发者如需[切换自定义认证](apply-custom-authentication.md)，需要配置导航按键上显示的文本（WidgetParam.navigationButtonText），最大长度为60字符。API 10-17仅在单指纹、单人脸场景下支持配置。从API 18开始，增加支持人脸+指纹场景。

当前支持使用认证控件的认证类型包括：

* 锁屏口令认证
* 人脸认证
* 指纹认证
* 人脸+锁屏口令认证
* 指纹+锁屏口令认证
* 人脸+指纹+锁屏口令认证
* 人脸+自定义导航按键
* 指纹+自定义导航按键
* 人脸+指纹+自定义导航按键18+

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)（包括挑战值、认证类型[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)列表和认证等级[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)）、配置认证控件界面[WidgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)，调用[getUserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserauthinstance10)获取认证对象。
3. 调用[UserAuthInstance.on('result')](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)接口订阅认证结果。
4. 调用[UserAuthInstance.start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口发起认证，通过[IAuthCallback](../harmonyos-references/js-apis-useriam-userauth.md#iauthcallback10)回调返回认证结果[UserAuthResult](../harmonyos-references/js-apis-useriam-userauth.md#userauthresult10)。当认证成功时返回认证通过类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)）和令牌信息（AuthToken）。

**示例1：**

发起用户认证，采用认证可信等级≥ATL3的人脸+指纹+锁屏口令认证，获取认证结果。

```
1. initiatingUserAuthentication1() {
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
12. };
13. // 配置认证界面
14. const widgetParam: userAuth.WidgetParam = {
15. title: resourceToString($r('app.string.title')),
16. };
17. // 获取认证对象
18. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
19. Logger.info('get userAuth instance successfully.');
20. // 订阅认证结果
21. userAuthInstance.on('result', {
22. onResult: (result: userAuth.UserAuthResult) => {
23. try {
24. Logger.info('userAuthInstance callback.');
25. this.result[ResultIndex.EXAMPLE_1] = (`${result.result}`);
26. // 可在认证结束或其他业务需要场景，取消订阅认证结果。
27. userAuthInstance.off('result');
28. } catch (error) {
29. const err: BusinessError = error as BusinessError;
30. Logger.error(`onResult failed, code: ${err?.code}, Message: ${err?.message}`);
31. }
32. }
33. });
34. // 启动认证
35. userAuthInstance.start();
36. Logger.info('auth start successfully.');
37. } catch (error) {
38. const err: BusinessError = error as BusinessError;
39. Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
40. }
41. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L120-L163)

**示例2：**

发起用户认证，采用认证可信等级≥ATL3的人脸+认证类型相关+复用设备解锁最大有效时长认证，获取认证结果。

```
1. initiatingUserAuthentication2() {
2. // 设置认证参数
3. let reuseUnlockResult: userAuth.ReuseUnlockResult = {
4. reuseMode: userAuth.ReuseMode.AUTH_TYPE_RELEVANT,
5. reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
6. };
7. try {
8. const randData = getRandData();
9. if (!randData) {
10. return;
11. }
12. const authParam: userAuth.AuthParam = {
13. challenge: randData,
14. authType: [userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT],
15. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
16. reuseUnlockResult: reuseUnlockResult,
17. };
18. // 配置认证界面
19. const widgetParam: userAuth.WidgetParam = {
20. title: resourceToString($r('app.string.title')),
21. };
22. // 获取认证对象
23. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
24. Logger.info('get userAuth instance successfully.');
25. // 订阅认证结果
26. userAuthInstance.on('result', {
27. onResult: (result: userAuth.UserAuthResult) => {
28. try {
29. Logger.info('userAuthInstance callback.');
30. this.result[ResultIndex.EXAMPLE_2] = (`${result.result}`);
31. // 可在认证结束或其他业务需要场景，取消订阅认证结果。
32. userAuthInstance.off('result');
33. } catch (error) {
34. const err: BusinessError = error as BusinessError;
35. Logger.error(`onResult failed, code: ${err?.code}, Message: ${err?.message}`);
36. }
37. }
38. });
39. // 启动认证
40. userAuthInstance.start();
41. Logger.info('auth start successfully.');
42. } catch (error) {
43. const err: BusinessError = error as BusinessError;
44. Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
45. }
46. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L170-L218)

**示例3：**

发起用户认证，采用认证可信等级≥ATL3的人脸+任意应用认证类型相关+复用任意应用最大有效时长认证，获取认证结果。

```
1. initiatingUserAuthentication3() {
2. // 设置认证参数
3. let reuseUnlockResult: userAuth.ReuseUnlockResult = {
4. reuseMode: userAuth.ReuseMode.CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT,
5. reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
6. };
7. try {
8. const randData = getRandData();
9. if (!randData) {
10. return;
11. }
12. const authParam: userAuth.AuthParam = {
13. challenge: randData,
14. authType: [userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT],
15. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
16. reuseUnlockResult: reuseUnlockResult,
17. };
18. // 配置认证界面
19. const widgetParam: userAuth.WidgetParam = {
20. title: resourceToString($r('app.string.title')),
21. };
22. // 获取认证对象
23. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
24. Logger.info('get userAuth instance successfully.');
25. // 订阅认证结果
26. userAuthInstance.on('result', {
27. onResult: (result: userAuth.UserAuthResult) => {
28. try {
29. Logger.info('userAuthInstance callback.');
30. this.result[ResultIndex.EXAMPLE_3] = (`${result.result}`);
31. // 可在认证结束或其他业务需要场景，取消订阅认证结果。
32. userAuthInstance.off('result');
33. } catch (error) {
34. const err: BusinessError = error as BusinessError;
35. Logger.error(`onResult failed, code: ${err?.code}, Message: ${err?.message}`);
36. }
37. }
38. });
39. // 启动认证
40. userAuthInstance.start();
41. Logger.info('auth start successfully.');
42. } catch (error) {
43. const err: BusinessError = error as BusinessError;
44. Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
45. }
46. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L225-L273)

**示例4：**

以模应用弹窗方式拉起身份认证控件对用户进行身份认证：

说明

在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

```
1. initiatingUserAuthentication4() {
2. // 设置认证参数
3. try {
4. const randData = getRandData();
5. if (!randData) {
6. return;
7. }
8. const authParam: userAuth.AuthParam = {
9. challenge: randData,
10. authType: [userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT],
11. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
12. };
13. // 配置认证界面
14. const widgetParam: userAuth.WidgetParam = {
15. title: resourceToString($r('app.string.title')),
16. uiContext: this.getUIContext().getHostContext()
17. };
18. // 获取认证对象
19. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
20. Logger.info('get userAuth instance successfully.');
21. // 订阅认证结果
22. userAuthInstance.on('result', {
23. onResult: (result: userAuth.UserAuthResult) => {
24. try {
25. Logger.info('userAuthInstance callback.');
26. this.result[ResultIndex.EXAMPLE_4] = (`${result.result}`);
27. // 可在认证结束或其他业务需要场景，取消订阅认证结果。
28. userAuthInstance.off('result');
29. } catch (error) {
30. const err: BusinessError = error as BusinessError;
31. Logger.error(`onResult failed, code: ${err?.code}, Message: ${err?.message}`);
32. }
33. }
34. });
35. // 启动认证
36. userAuthInstance.start();
37. Logger.info('auth start successfully.');
38. } catch (error) {
39. const err: BusinessError = error as BusinessError;
40. Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
41. }
42. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L280-L324)

## 示例代码

* [发起认证](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
