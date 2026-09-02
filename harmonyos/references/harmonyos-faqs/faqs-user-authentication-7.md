---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-7
title: 实现生物认证功能
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 实现生物认证功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:60b0691c2271d1f5c157292fa047bfd8a372630951362accf1a1e69066343a40
---

## 问题现象

如何实现生物认证，并根据认证结果回调进行处理。

## 背景知识

* 身份认证包含锁屏口令、指纹识别及人脸识别三种方式，系统提供了统一的用户认证控件供应用调用，以实现[生物认证](../harmonyos-guides/devicesecurity-trustedauth-enablebio.md)功能。
* [ohos.userIAM.userAuth (用户认证)](../harmonyos-references/js-apis-useriam-userauth.md)提供用户认证能力，应用于设备解锁、支付、应用登录等场景。
* [UserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthinstance10)用于执行用户身份认证，并支持使用统一用户身份认证控件。

  其中API10的[on](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)接口注册监听是订阅用户身份认证的结果；API20的[on](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)接口注册监听是订阅用户身份认证中间状态。

## 解决方案

实现生物认证开发步骤如下：

1. 申请权限：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)（包括挑战值、认证类型[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)列表和认证等级[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)）、配置认证控件界面[WidgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)，调用[getUserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserauthinstance10)获取认证对象。
3. 调用[on](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)接口订阅认证结果。
4. 调用[start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口发起认证，通过[IAuthCallback](../harmonyos-references/js-apis-useriam-userauth.md#iauthcallback10)回调返回认证结果[UserAuthResult](../harmonyos-references/js-apis-useriam-userauth.md#userauthresult10)。当认证成功时返回认证通过类型（UserAuthType）和令牌信息（AuthToken）。

实际开发代码参考如下：

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct UserAuth {
  build() {
    Column() {
      Button('身份认证')
        .onClick(() => {
          try {
            const rand = cryptoFramework.createRandom();
            const len: number = 16; // Generate a 16-byte random number.
            const randData: Uint8Array = rand?.generateRandomSync(len)?.data;
            // 设置认证参数。
            const authParam: userAuth.AuthParam = {
              challenge: randData,
              authType: [userAuth.UserAuthType.PIN, userAuth.UserAuthType.FINGERPRINT],
              authTrustLevel: userAuth.AuthTrustLevel.ATL3,
            };
            // 配置认证界面。
            const widgetParam: userAuth.WidgetParam = {
              title: '请进行身份认证',
            };
            // 获取认证对象。
            const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
            hilog.info(0x0000, 'UserAuth', 'get userAuth instance success');
            // 订阅认证结果。
            userAuthInstance.on('result', {
              onResult(result) {
                hilog.info(0x0000, 'UserAuth', `userAuthInstance callback result: ${JSON.stringify(result)}`);
                // 可在认证结束或其他业务需要场景，取消订阅认证结果。
                userAuthInstance.off('result');
              }
            });
            hilog.info(0x0000, 'UserAuth', 'auth on success');
            userAuthInstance.start();
            hilog.info(0x0000, 'UserAuth', 'auth start success');
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            hilog.error(0x0000, 'UserAuth', `auth catch error. Code is ${err?.code}, message is ${err?.message}`);
          }
        });
    };
  }
}
```

## 常见FAQ

Q：添加了权限申请，代码也没有问题，依然报错是什么原因？

A：生物认证功能需要提前录入凭据，检查对应认证类型的凭据是否已经录入，未录入则进行录入。

Q：认证最大次数是否可以设置？

A：用户认证最大失败次数是设备、系统自身设置无法进行自定义。

Q：应用在调用生物认证功能时，只能收到认证成功和取消的回调，不能收到认证失败FAIL=12500001的回调或异常？

A：在生物认证过程中，不会返回中间过程的结果。中间错误，只会体现在交互界面上，而不会体现在认证结果回调上。

Q：指纹验证失败如何触发回调事件？在API10的[on](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)接口注册了回调，只有验证成功和取消指纹验证才会触发该回调，验证失败场景不会触发。

A：

* API10的[on](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)接口提供的是带界面的身份认证接口，onResult只会返回界面消失后最终的认证结果，中间认证结果（如认证失败尝试）是不返回的。
* 为让生态感知中间认证结果，API20增加了[on](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)的监听接口。同时用户也可以使用[自定义认证](../harmonyos-guides/apply-custom-authentication.md)，进行生物认证失败点击导航按钮时，统一身份认证框架会结束系统认证流程并通知调用者拉起自定义认证界面。

Q：面容解锁可以无限连续尝试？

A：目前人脸识别是在识别到人脸时才会启动人脸验证，如果验证失败会累计失败次数，达最大次数会进行禁用，但如果是识别超时，因为未识别到人脸，不会累计验证失败次数，就可以无限尝试。

Q：为什么authType设置为[userAuth.UserAuthType.FINGERPRINT, userAuth.UserAuthType.FACE]报错误码401？

A：需要在WidgetParam中配置navigationButtonText参数，该参数从API 18开始，增加支持人脸+指纹场景。参考[WidgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)：用户认证界面配置相关参数。

Q：AuthTrustLevel设置为ATL4时，错误码12500006，AuthTrustLevel的含义是什么呢，该如何解决？

A：[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)是指期望达到的认证可信等级。典型操作需要的身份认证所需等级，以及身份认证可信等级的划分请参见[认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。

错误码12500006表示认证信任等级不支持，原因及处理步骤请参考官网文档[12500006 认证信任等级不支持](../harmonyos-references/errorcode-useriam.md#section12500006-认证信任等级不支持)。

Q：应用支付需要人脸认证，为了保证所有手机都能使用，能否把AuthTrustLevel设置统一后，让接口自动降级去检测？

A：不能，支付有安全认证等级要求，只能用其他方式比如：指纹认证。

Q：同一个指纹，认证结果[UserAuthResult](../harmonyos-references/js-apis-useriam-userauth.md#userauthresult10)中的token是否一致？

A：不一致，使用[官方指南](../harmonyos-guides/start-authentication.md)中的示例demo，将入参challenge的值固定，返回结果也是用户认证结果（result）一致，而令牌信息（token）不一致。
