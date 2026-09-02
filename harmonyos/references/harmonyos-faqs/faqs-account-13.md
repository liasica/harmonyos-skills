---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-13
title: 华为账号一键登录无后端场景的接入方式
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为账号一键登录无后端场景的接入方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:83c6da1bda670db514da20e1887dd5223bb0c701fff2ff8e1a910a8903fd4cd7
---

## 问题现象

华为账号一键登录接入过程中，客户端获取到AuthorizationCode后，需要传到服务端，通过服务端调用华为账号接口获取用户信息。应用如果没有后端，是否还能接入华为账号一键登录？AuthorizationCode传到服务端调用华为账号接口这部分功能，是否可以在客户端直接实现？

## 背景知识

* Authorization Code：授权码，用户使用华为账号登录成功之后，可通过返回的凭据解析出授权码，通过授权码可获取Access Token、Refresh Token、ID Token等。
* Access Token：访问凭证，是访问被权限管控资源的应用级凭证。可使用Access Token调用获取用户信息接口获取用户信息。

## 解决方案

在HarmonyOS开发中，华为账号一键登录通常需要通过应用服务器来获取业务登录凭证，不建议直接在客户端获取。以下是具体原因：

1. 安全性考虑：防止敏感信息泄露：业务登录凭证（如Access Token）是敏感信息，直接在客户端获取和存储可能会增加被恶意获取的风险。
2. 业务逻辑的实现：用户关联和注册：服务器可以根据获取到的用户信息（如UnionID、OpenID、手机号等）完成用户关联、注册等业务逻辑。
3. 客户端的限制：无法处理复杂逻辑：客户端处理能力有限，不适合处理复杂的业务逻辑和安全策略。

* 综上所述，获取用户手机号等敏感信息时，不建议在客户端完成凭证交换，推荐在服务端实现。
* 如果只需要获取UnionID或OpenID作为本地用户标识，客户端可以直接通过华为账号授权获取，无需后端参与凭证交换。
* 如果开发者没有服务端又想获取用户手机号码信息，可以在客户端使用[rcp](../harmonyos-references/remote-communication-rcp.md)模拟服务端发送请求获取用户信息。代码如下：

```ts
import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rcp } from '@kit.RemoteCommunicationKit';

@Entry
@Component
struct Index {
  @State message: string = '';
  AuToken: string = '';
  accessToken: string = '';
  // 应用的Client ID
  clientId: string = '*****';
  // 应用的Client Secret
  clientSecret = '*****';

  build() {
    Column() {
      Text(this.message)
        .maxLines(10)
        .id('QuickGetPhoneNumber')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
      Button($r('app.string.GetACButton')).onClick(() => {
        this.getAuthCode();
      })
      Button($r('app.string.GetATButton')).onClick(() => {
        this.getFromServer();
      })
      Button($r('app.string.GetPhoneNumberButton')).onClick(() => {
        this.getPhoneNumber();
      })
    }
    .height('100%')
    .width('100%')
  }

  getAuthCode() {
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    // 获取手机号需要传如下scope，传参数之前需要先申请对应scope权限，否则会返回1001502014错误码
    authRequest.scopes = ['phone'];
    // 获取authorizationCode需传如下permission
    authRequest.permissions = ['serviceauthcode'];
    // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
    authRequest.forceAuthorization = true;
    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 执行请求
    try {
      // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
      const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
      controller.executeRequest(authRequest).then((data) => {
        const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
        const state = authorizationWithHuaweiIDResponse.state;
        if (state && authRequest.state !== state) {
          hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
        const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
        const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
        if (authorizationCode != undefined) {
          this.AuToken = authorizationCode;
          this.message = authorizationCode;
        }

        // 开发者处理authorizationCode
      }).catch((err: BusinessError) => {
        dealAllError(err);
      });
    } catch (error) {
      dealAllError(error);
    }
  }

  getFromServer() {
    let context = this.getUIContext().getHostContext();
    if (context == undefined) {
      console.error(`context is undefined`);
      return;
    }
    let headers: rcp.RequestHeaders = {
      'accept': context.resourceManager.getStringByNameSync('accept'),
      'content-type': context.resourceManager.getStringByNameSync('content_type')
    };
    const simpleForm = new rcp.Form({
      'client_id': this.clientId,
      'grant_type': context.resourceManager.getStringByNameSync('authorization_code'),
      'code': this.AuToken,
      'client_secret': this.clientSecret
    });
    let req = new rcp.Request(context.resourceManager.getStringByNameSync('getATURL'), 'POST', headers, simpleForm);
    req.content = simpleForm;
    try {
      // 创建会话。
      const session = rcp.createSession();
      // 会话发起请求。
      session.fetch(req).then((resp: rcp.Response) => {
        console.info(`Response succeeded: ${JSON.stringify(resp)}`);
        this.accessToken = JSON.parse(JSON.stringify(resp)).access_token as string;
        this.message = this.accessToken;
        session.close();
      }).catch((err: BusinessError) => {
        // 请求错误处理。
        console.error(`Response err: Code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err)}`);
        session.close();
      });
    } catch (err) {
      // 创建会话错误处理。
      console.error(`createSession err: Code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err)}`);
    }
  }

  getPhoneNumber() {
    let context = this.getUIContext().getHostContext();
    if (context == undefined) {
      console.error(`context is undefined`);
      return;
    }
    // 定义content，请根据实际情况选择
    let headers: rcp.RequestHeaders = {
      'content-type': context.resourceManager.getStringByNameSync('accept'),
    };
    const simpleForm = new rcp.Form({
      'access_token': this.accessToken
    });
    let req = new rcp.Request(context.resourceManager.getStringByNameSync('getPhoneURL'), 'POST', headers, simpleForm);
    req.content = simpleForm;
    try {
      // 创建会话。
      const session = rcp.createSession();
      // 会话发起请求。
      session.fetch(req).then((resp: rcp.Response) => {

        console.info(`Response succeeded: ${JSON.stringify(resp)}`);
        this.message = JSON.parse(JSON.stringify(resp)).mobileNumber as string;
        session.close();
      }).catch((err: BusinessError) => {
        // 请求错误处理。
        console.error(`Response err: Code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err)}`);
        session.close();
      });
    } catch (err) {
      // 创建会话错误处理。
      console.error(`createSession err: Code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err)}`);
    }
  }
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在应用快速验证手机号场景下，涉及UI交互时，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络异常，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请尝试使用其他方式登录
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```
