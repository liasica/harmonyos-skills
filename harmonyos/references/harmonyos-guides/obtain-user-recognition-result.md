---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-user-recognition-result
title: 查询和订阅用户识别结果
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 查询和订阅用户识别结果
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e1f2f0384c82941a5dff90c81fd4cf36fab6b434af9ca02e8c49252ee950b125
---

从API版本26.0.1开始，系统支持用户识别。系统持续识别当前使用者。应用可查询最新识别结果或订阅识别结果变化，用于判断当前使用者是否与已登录的系统用户匹配。

## 接口说明

具体参数、返回值、错误码等描述，请参考[UserRecognitionMgr](../harmonyos-references/js-apis-useriam-userauth.md#userrecognitionmgr)。

| 接口名称 | 功能描述 |
| --- | --- |
| getUserRecognitionMgr(): UserRecognitionMgr | null | 获取UserRecognitionMgr实例，用于查询和订阅用户识别结果。 |
| getUserRecognitionResult(): Promise<UserRecognitionResult> | 获取最新的用户识别结果。 |
| onUserRecognitionChange(callback: UserRecognitionResultCallback): void | 订阅用户识别结果变化事件。 |
| offUserRecognitionChange(callback?: UserRecognitionResultCallback): void | 取消订阅用户识别结果变化事件。 |

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_USER\_PASSIVE\_RECOGNITION。

   该权限授权方式为system\_grant，在module.json5中声明即可获取。
2. 调用[getUserRecognitionMgr](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserrecognitionmgr)获取实例。
3. 调用[getUserRecognitionResult](../harmonyos-references/js-apis-useriam-userauth.md#getuserrecognitionresult)获取最新识别结果，或调用[onUserRecognitionChange](../harmonyos-references/js-apis-useriam-userauth.md#onuserrecognitionchange)订阅变化事件。

```typescript
async obtainingUserRecognitionResult(): Promise<string> {
  try {
    // 获取实例
    let mgr = userAuth.getUserRecognitionMgr();
    if (!mgr) {
      Logger.error('the device does not support user recognition.');
      return 'the device does not support user recognition.';
    }
    // 获取最新识别结果
    let result = await mgr.getUserRecognitionResult();
    Logger.info(`status: ${result.status}, userId: ${result.userId}`);
    // 订阅识别结果变化
    let callback: userAuth.UserRecognitionResultCallback = (recognitionResult: userAuth.UserRecognitionResult) => {
      Logger.info(`status: ${recognitionResult.status}, userId: ${recognitionResult.userId}`);
    };
    mgr.onUserRecognitionChange(callback);
    // 取消订阅
    mgr.offUserRecognitionChange(callback);
    return `status: ${result.status}, userId: ${result.userId}`;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    const errMessage: string = `getUserRecognitionResult failed, Code: ${err?.code}, message: ${err?.message}`;
    Logger.error(errMessage);
    return errMessage;
  }
}
```

## 示例代码

* 可参考[用户认证服务](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)示例代码。
