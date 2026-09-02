---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cancel-authentication
title: 认证过程中取消认证
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 认证过程中取消认证
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad5d2fc493f658df7e291c0c0280817a50be1bef285acbd037fc523c4db048e7
---

统一用户认证框架提供了cancel接口，当应用在认证过程中，需要取消认证时可调用该接口。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[cancel](../harmonyos-references/js-apis-useriam-userauth.md#cancel10)。

此处仅展示了取消认证操作的接口，在取消认证前，需要先发起认证，发起认证的接口列表、详细说明可参考[发起认证](start-authentication.md)章节和API文档。

| 接口名称 | 功能描述 |
| --- | --- |
| cancel(): void | 取消本次认证操作。 |

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)（包括挑战值、认证类型[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)列表和认证等级[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)），获取认证对象[UserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthinstance10)，并调用[UserAuthInstance.start](../harmonyos-references/js-apis-useriam-userauth.md#start10)发起认证。此步骤详细说明可参考[发起认证](start-authentication.md)。
3. 使用已经成功发起认证的UserAuthInstance对象调用[UserAuthInstance.cancel](../harmonyos-references/js-apis-useriam-userauth.md#cancel10)接口取消本次认证。

示例代码为发起认证可信等级≥ATL3的人脸+锁屏口令认证后，取消认证请求：

```typescript
handleAuthResultAndCanceling(userAuthInstance: userAuth.UserAuthInstance, exampleNumber: number) {
  // ...
    // 启动认证
    userAuthInstance.start();
    Logger.info('auth start successfully.');
    // ...
      // 取消认证
      userAuthInstance.cancel();
      Logger.info('auth cancel successfully.');
      // ...
}

/*
 * cancel-authentication.md
 * 发起认证可信等级≥ATL3的人脸+锁屏密码认证后，取消认证请求
 * */
cancelingUserAuthentication() {
  try {
    const randData = getRandData();
    if (!randData) {
      return;
    }
    // 设置认证参数
    const authParam: userAuth.AuthParam = {
      challenge: randData,
      authType: [userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT],
      authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    };
    // 配置认证界面
    const widgetParam: userAuth.WidgetParam = {
      title: resourceToString($r('app.string.title')),
    };
    // 获取认证对象
    const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
    Logger.info('get userAuth instance successfully.');
    this.handleAuthResultAndCanceling(userAuthInstance, ResultIndex.CANCEL);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`auth failed, code is ${err?.code as number}, message is ${err?.message}`);
  }
}
```

## 示例代码

* [认证过程中取消认证](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)
