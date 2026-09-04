---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/compaion-device-authentication
title: 伴随设备认证
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 伴随设备认证
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:071efcfe5133a87481b7db89f45cf323871c9f8c2daf54b087f90d4434e40e06
---

从API版本26.0.0开始，用户认证服务新增伴随设备认证方式。用户可通过佩戴的伴随设备完成身份认证。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[@ohos.userIAM.userAuth (用户认证)](../harmonyos-references/js-apis-useriam-userauth.md)。

| 接口名称 | 功能描述 |
| --- | --- |
| getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance | 获取UserAuthInstance对象，用于执行用户身份认证。发起伴随设备认证时，[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)的authType需指定为[UserAuthType.COMPANION\_DEVICE](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)。 |
| on(type: 'result', callback: IAuthCallback): void | 订阅用户身份认证结果。 |
| off(type: 'result', callback?: IAuthCallback): void | 取消订阅用户身份认证结果。 |
| start(): void | 执行用户认证。 |

## 伴随设备无感认证

发起伴随设备认证前需先在主设备上“设置->生物识别与密码->协同认证”页面添加伴随设备。具体流程如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/8PKj7HvQTmCiLB670OZWTQ/zh-cn_image_0000002742123475.png)

**说明** 

发起伴随设备认证时，[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)的authType只能指定为[UserAuthType.COMPANION\_DEVICE](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)，不能与PIN、FACE、FINGERPRINT同时指定。

## 开发准备

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)（包括挑战值、认证类型[UserAuthType.COMPANION\_DEVICE](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)和认证等级[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)）、配置认证控件界面[WidgetParam](../harmonyos-references/js-apis-useriam-userauth.md#widgetparam10)，调用[getUserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserauthinstance10)获取认证对象。
3. 调用[UserAuthInstance.on('result')](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)接口订阅认证结果。
4. 调用[UserAuthInstance.start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口发起认证，通过[IAuthCallback](../harmonyos-references/js-apis-useriam-userauth.md#iauthcallback10)回调返回认证结果[UserAuthResult](../harmonyos-references/js-apis-useriam-userauth.md#userauthresult10)。当认证成功时返回认证通过类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)）和令牌信息（AuthToken）。

**示例**

发起伴随设备认证，采用认证可信等级≥ATL2的伴随设备认证，获取认证结果。

```typescript
companionDeviceAuthentication() {
  try {
    const randData = getRandData();
    if (!randData) {
      return;
    }
    // 设置认证参数
    const authParam: userAuth.AuthParam = {
      challenge: randData,
      authType: [userAuth.UserAuthType.COMPANION_DEVICE],
      authTrustLevel: userAuth.AuthTrustLevel.ATL2,
    };
    // 配置认证界面
    const widgetParam: userAuth.WidgetParam = {
      title: resourceToString($r('app.string.title')),
    };
    // 获取认证对象
    const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
    Logger.info('get userAuth instance successfully.');
    // 订阅认证结果
    userAuthInstance.on('result', {
      onResult: (result: userAuth.UserAuthResult) => {
        try {
          Logger.info('userAuthInstance callback.');
          this.result[ResultIndex.EXAMPLE_1] = (`${result.result}`);
          // 可在认证结束或其他业务需要场景，取消订阅认证结果。
          userAuthInstance.off('result');
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          Logger.error(`onResult failed, code: ${err?.code}, Message: ${err?.message}`);
        }
      }
    });
    // 启动认证
    userAuthInstance.start();
    Logger.info('auth start successfully.');
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`auth failed, code is ${err?.code}, message is ${err?.message}`);
  }
}
```

## 示例代码

* [伴随设备认证](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/UserAuthentication)
