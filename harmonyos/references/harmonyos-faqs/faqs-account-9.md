---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-9
title: 华为一键登录如何同时获取匿名手机号和头像、昵称
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为一键登录如何同时获取匿名手机号和头像、昵称
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:0ce3bd048a526e991d91f3d202969b34588cc5b19c39cc4b3e21be09d3b6fa5f
---

## 问题现象

获取匿名手机号（quickLoginAnonymousPhone）只能与openid同时使用。在获取匿名手机号时如何同时获取头像和昵称？

## 背景知识

* 应用使用华为账号一键登录功能之前，需要完成quickLoginMobilePhone（华为账号一键登录）的scope权限申请，详情参见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。scope权限申请审批未完成或未通过，将报错[1001502014 应用未申请scopes或permissions权限](../harmonyos-guides/account-faq-2.md)。
* [createAuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest)：创建一个Account Kit授权请求对象，可通过属性值设置请求参数。作为应用使用华为账号登录场景的请求参数。
* [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)：该类为应用创建的授权请求对象，使用Account Kit请求授权以申请更多的用户信息，包括scopes、permissions等属性。作为向华为账号申请授权的请求对象，应用根据实际场景按需获取。

## 解决方案

获取华为账号绑定的匿名手机号是通过quickLoginAnonymousPhone，该scope只能与openid同时使用，而获取头像昵称是通过profile值获取，quickLoginAnonymousPhone和profile同时使用会报错：“1001500003不支持该scopes或permissions”。

若需要同时获取匿名化手机号和头像昵称，建议分2个方法调用，不会影响返回结果。示例代码如下：

```ts
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { authentication } from '@kit.AccountKit';

@Entry
@Component
struct Page {
  getPhotoName() {
    // 创建授权请求，并设置参数
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    // 获取头像昵称需要传如下scope
    authRequest.scopes = ['profile'];
    // 若开发者需要进行服务端开发，则需传如下permission获取authorizationCode
    authRequest.permissions = ['serviceauthcode'];
    // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
    authRequest.forceAuthorization = true;
    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 执行授权请求
    try {

      const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext() as Context);
      controller.executeRequest(authRequest).then((data) => {
        const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
        const state = authorizationWithHuaweiIDResponse.state;
        if (state != undefined && authRequest.state != state) {
          hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');

        const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse.data!;
        const avatarUri = authorizationWithHuaweiIDCredential.avatarUri; // 用户头像链接
        const nickName = authorizationWithHuaweiIDCredential.nickName; // 用户昵称
        const unionID = authorizationWithHuaweiIDCredential.unionID;
        const openID = authorizationWithHuaweiIDCredential.openID;
        const authorizationCode = authorizationWithHuaweiIDCredential.authorizationCode;

        hilog.info(0x0000, 'testTag',
          `获取到nickName、avatarUri、UnionID、OpenID、authorizationCode:${nickName}、${avatarUri}、${unionID}、${openID}、${authorizationCode}`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag',
          `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
    }
  }

  getQuickLoginAnonymousPhone() {
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    authRequest.scopes = ['quickLoginAnonymousPhone'];

    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 一键登录场景该参数只能设置为false
    authRequest.forceAuthorization = false;
    const controller = new authentication.AuthenticationController();
    try {
      controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
        // 获取到UnionID、OpenID、匿名手机号
        const unionID = response.data?.unionID;
        const openID = response.data?.openID;
        const authCode = response.data?.authorizationCode;
        hilog.info(0x0000, 'testTag', `获取到UnionID、OpenID、匿名手机号:${unionID}、${openID}、${authCode}`);
        const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
        if (anonymousPhone) {
          hilog.info(0x0000, 'testTag', 'Succeeded in authentication getQuickLoginAnonymousPhone.');
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in authentication. AnonymousPhone is empty.');
        // 未获取到匿名手机号需要跳转到应用自定义的登录页面
      })
        .catch((error: BusinessError) => {
          hilog.error(0x0000, 'testTag',
            `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);

        });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
    }
  }

  build() {
    Column() {
      // 应用使用华为账号一键登录功能之前，需要完成quickLoginMobilePhone（华为账号一键登录）的scope权限申请，详情参见配置scope权限:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-config-permissions
      Button('获取头像、昵称')
        .onClick(() => {
          this.getPhotoName();
        })
        .margin({ bottom: 10 });
      Button('获取匿名手机号')
        .onClick(() => {
          this.getQuickLoginAnonymousPhone();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：使用华为账号一键登录功能时，是以华为账号的UnionID/OpenID还是以手机号作为用户的主要标识？

A：推荐使用华为账号的UnionID/OpenID作为用户的主要标识，并将应用与华为账号绑定的手机号关联。华为账号的UnionID/OpenID不会发生变化，即使换绑手机号，仍然可以使用华为账号登录原来绑定的应用账号。

Q：Access Token和Refresh Token的有效时长是多久？

A：Access Token的有效时长是1个小时，Refresh Token的有效时长是180天。

Q：向用户申请获取昵称/头像授权是在华为账号一键登录前还是登录后？

A：同意获取昵称/头像授权包含在[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)内，用户同意[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)后才能进入华为账号一键登录流程。
