---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/apply-custom-authentication
title: 切换自定义认证
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 用户身份认证开发指导 > 切换自定义认证
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef1081d557ed437a3b41a073e26a223bac323c1224a9d4715351fade9445f769
---

若开发者定义了自定义认证方式，则用户进行生物认证失败点击导航按钮时，统一用户认证框架会结束系统认证流程并通知调用者拉起自定义认证界面。

例如，在支付场景中，如果厂商自定义了支付密码认证的方式，当调用系统人脸或指纹认证失败后，用户可以选择切换支付密码认证。

支付密码认证不属于系统认证能力，因此业务在发起认证时需要传入导航键的显式信息，例如“使用支付密码”。这样，用户看到的认证界面便会包含一个“使用支付密码”的按钮。

当用户点击该按钮，发起认证的业务应用便会收到统一用户认证框架返回的一个特殊认证结果，提示业务系统认证结束，需要拉起业务自定义的认证界面。这样，用户在点击“使用支付密码”按钮后，便会看到系统认证控件消失，显示出业务自定义的支付密码认证界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-hiUV7hpRkKLhs7Tl9Ymzw/zh-cn_image_0000002583438463.png?HW-CC-KV=V1&HW-CC-Date=20260427T234337Z&HW-CC-Expire=86400&HW-CC-Sign=5FFF75F324C1123681C3991D9050CE78CECA0634A4F919810785260EE2353254)

如图所示，框选区域为WidgetParam.navigationButtonText字段。开发者可配置此字段，引导用户从生物认证切换到应用自定义的业务密码认证。

说明

锁屏口令认证与业务自定义认证只能二选一，不能同时存在。

| 认证类型 | 支持切换业务自定义认证方式。  （√表示支持，x表示不支持。） |
| --- | --- |
| 锁屏口令认证 | × |
| 人脸认证 | √ |
| 指纹认证 | √ |
| 人脸+指纹18+ | √ |
| 人脸+锁屏口令认证 | × |
| 指纹+锁屏口令认证 | × |
| 人脸+指纹+锁屏口令认证 | × |

## 开发示例

针对需要切换自定义认证方式的场景，发起认证请求的方式请参考[发起认证](start-authentication.md)，但传入的widgetParam必须包含navigationButtonText字段。

当前示例仅展示如何配置界面和选择切换到自定义认证界面。具体拉起的页面及对应页面的实现，请开发者自行实现，代码插入位置可参考注释提示。

```
1. handleCustomAuthResult(userAuthInstance: userAuth.UserAuthInstance, exampleNumber: number) {
2. // ...
3. userAuthInstance.on('result', {
4. onResult: (result: userAuth.UserAuthResult) => {
5. // ...
6. Logger.info('userAuthInstance callback');
7. // ...
8. if (result.result == userAuth.UserAuthResultCode.CANCELED_FROM_WIDGET ||
9. result.result == userAuth.UserAuthResultCode.NOT_ENROLLED) {
10. // 请开发者自行完成拉起自定义认证界面的实现
11. // ...
12. }
13. // ...
14. }
15. });
16. // 启动认证
17. userAuthInstance.start();
18. Logger.info('auth start successfully');
19. // ...
20. }

22. /*
23. * apply-custom-authentication.md
24. * 当前示例仅展示如何配置界面、选择切换到自定义认证界面，具体拉起的页面及对应页面的实现，请开发者自行实现
25. * */
26. applyingCustomAuthentication() {
27. try {
28. const randData = getRandData();
29. if (!randData) {
30. return;
31. }
32. const authParam: userAuth.AuthParam = {
33. challenge: randData,
34. authType: [userAuth.UserAuthType.FACE],
35. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
36. };
37. // 配置自定义认证，需设置导航键文本
38. const widgetParam: userAuth.WidgetParam = {
39. title: resourceToString($r('app.string.title')),
40. navigationButtonText: resourceToString($r('app.string.navigationButtonText'))
41. };
42. // 获取认证对象
43. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
44. Logger.info('get userAuth instance successfully');
45. // 订阅认证结果
46. this.handleCustomAuthResult(userAuthInstance, ResultIndex.CUSTOMIZE);
47. } catch (error) {
48. const err: BusinessError = error as BusinessError;
49. Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
50. }
51. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L457-L540)

## 示例代码

* [切换自定义认证](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
