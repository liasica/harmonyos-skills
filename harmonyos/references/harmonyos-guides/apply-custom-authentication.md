---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/apply-custom-authentication
title: 切换自定义认证
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 切换自定义认证
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:34+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4eb470c0415ad5f3ce2df46409727aa70deeb340570cc52dbd0dea641b0f723e
---

若开发者定义了自定义认证方式，则用户进行生物认证失败点击导航按钮时，统一用户认证框架会结束系统认证流程并通知调用者拉起自定义认证界面。

例如，在支付场景中，如果厂商自定义了支付密码认证的方式，当调用系统人脸或指纹认证失败后，用户可以选择切换支付密码认证。

支付密码认证不属于系统认证能力，因此业务在发起认证时需要传入导航键的显式信息，例如“使用支付密码”。这样，用户看到的认证界面便会包含一个“使用支付密码”的按钮。

当用户点击该按钮，发起认证的业务应用便会收到统一用户认证框架返回的一个特殊认证结果，提示业务系统认证结束，需要拉起业务自定义的认证界面。这样，用户在点击“使用支付密码”按钮后，便会看到系统认证控件消失，显示出业务自定义的支付密码认证界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/VI4cm_AbR56DlYiP67mDrg/zh-cn_image_0000002788467380.png?HW-CC-KV=V1&HW-CC-Date=20261114T004554Z&HW-CC-Expire=31536000000&HW-CC-Sign=78C5181A28346CABC7535719C402D36A11B76BCDD43760A86698B14DF6716AF2)

如图所示，框选区域为WidgetParam.navigationButtonText字段。开发者可配置此字段，引导用户从生物认证切换到应用自定义的业务密码认证。

**说明** 

锁屏口令认证与业务自定义认证只能二选一，不能同时存在。

| 认证类型 | 支持切换业务自定义认证方式。  （√表示支持，x表示不支持。） |
| --- | --- |
| 锁屏口令认证 | x |
| 人脸认证 | √ |
| 指纹认证 | √ |
| 人脸+指纹18+ | √ |
| 人脸+锁屏口令认证 | x |
| 指纹+锁屏口令认证 | x |
| 人脸+指纹+锁屏口令认证 | x |

## 开发示例

针对需要切换自定义认证方式的场景，发起认证请求的方式请参考[发起认证](start-authentication.md)，但传入的widgetParam必须包含navigationButtonText字段。

当前示例仅展示如何配置界面和选择切换到自定义认证界面。具体拉起的页面及对应页面的实现，请开发者自行实现，代码插入位置可参考注释提示。

```typescript
handleCustomAuthResult(userAuthInstance: userAuth.UserAuthInstance, exampleNumber: number) {
  // ...
    userAuthInstance.on('result', {
      onResult: (result: userAuth.UserAuthResult) => {
        // ...
          Logger.info('userAuthInstance callback');
          // ...
          if (result.result == userAuth.UserAuthResultCode.CANCELED_FROM_WIDGET ||
            result.result == userAuth.UserAuthResultCode.NOT_ENROLLED) {
            // 请开发者自行完成拉起自定义认证界面的实现
            // ...
          }
          // ...
      }
    });
    // 启动认证
    userAuthInstance.start();
    Logger.info('auth start successfully.');
    // ...
}

/*
 * apply-custom-authentication.md
 * 当前示例仅展示如何配置界面、选择切换到自定义认证界面，具体拉起的页面及对应页面的实现，请开发者自行实现
 * */
applyingCustomAuthentication() {
  try {
    const randData = getRandData();
    if (!randData) {
      return;
    }
    const authParam: userAuth.AuthParam = {
      challenge: randData,
      authType: [userAuth.UserAuthType.FACE],
      authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    };
    // 配置自定义认证，需设置导航键文本
    const widgetParam: userAuth.WidgetParam = {
      title: resourceToString($r('app.string.title')),
      navigationButtonText: resourceToString($r('app.string.navigationButtonText'))
    };
    // 获取认证对象
    const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
    Logger.info('get userAuth instance successfully.');
    // 订阅认证结果
    this.handleCustomAuthResult(userAuthInstance, ResultIndex.CUSTOMIZE);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
  }
}
```

## 示例代码

* 可参考[用户认证服务](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)示例代码。
