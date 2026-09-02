---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-6
title: 指纹登录功能实现以及指纹锁定
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 指纹登录功能实现以及指纹锁定
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:1486030fdf61767d6f61a187f32e09eae0503606978a178268dbbf862521fa7b
---

## 问题现象

出于安全考虑，想要通过监听指纹匹配错误5次后移动端应用内部主动关闭指纹登录功能，但是由于用户认证无法回调[中间态](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)，只可以回调[结果](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)，且指纹验证错误5次后锁定指纹认证，需要手动关闭指纹认证，回调结果为错误码12500003，导致无法精准判断指纹匹配错误5次。

## 背景知识

* [@ohos.userIAM.userAuth (用户认证)](../harmonyos-references/js-apis-useriam-userauth.md)：提供用户认证能力，应用于设备解锁、支付、应用登录等场景。本文主要使用了统一用户身份认证控件（UserAuthInstance）。
* [start](../harmonyos-references/js-apis-useriam-userauth.md#start10)：需要配置ohos.permission.ACCESS\_BIOMETRIC权限，开始认证。

## 解决方案

1. 指纹认证前提：设备具备指纹认证功能且录入个人指纹。
2. 在**对应模块的module.json5**文件中找到requestPermissions字段配置**ohos.permission.ACCESS\_BIOMETRIC**权限。

   ```json
   {
     "name": "ohos.permission.ACCESS_BIOMETRIC"
   },
   ```
3. [查询支持的认证能力](../harmonyos-guides/obtain-supported-authentication-capabilities.md)，需要根据[错误码](../harmonyos-references/errorcode-useriam.md)的不同，给予用户不同的提示：

   ```ts
   try {
     // 查询认证能力是否支持
     userIAM.getAvailableStatus(userAuthType, authTrustLevel);
   } catch (error) {
     console.error(TAG, 'auth catch error: ' + JSON.stringify(error));
     if (error['code'] && error['code'] == 12500010) { // 有：未禁用\无凭据
       callback(false, 12500010, `请先在本机系统中添加或设置指纹后才能使用此功能`);
     } else if (error['code'] && error['code'] == 12500005) { // 无：不支持
       callback(false, 12500005, `该设备不支持${tip}认证`);
     } else {
       callback(false, error['code'], `该设备不支持${tip}认证`); // 兜底
     }
     return;
   }
   ```
4. 设置[AuthParam](../harmonyos-references/js-apis-useriam-userauth.md#authparam10)中skipLockedBiometricAuth属性，可在指纹失败5次时返回12500009错误码，根据错误码跳过锁定的指纹认证，即可主动关闭。
5. 订阅认证结果并开始认证：

   ```ts
   userAuthInstance.on('result', {
     onResult(result) {
       console.info('userAuthInstance callback result = ' + JSON.stringify(result));
       let success: boolean = false;
       let msg: string = '';
       switch (result.result) {
         case userIAM.UserAuthResultCode.SUCCESS:
           success = true;
           msg = '认证成功';
           break;
         case userIAM.UserAuthResultCode.FAIL:
           msg = '认证失败';
           break;
         case userIAM.UserAuthResultCode.CANCELED:
           msg = '操作取消';
           break;
         case userIAM.UserAuthResultCode.TIMEOUT:
           msg = '操作超时';
           break;
         case userIAM.UserAuthResultCode.TYPE_NOT_SUPPORT:
           msg = '不支持的认证类型';
           break;
         case userIAM.UserAuthResultCode.TRUST_LEVEL_NOT_SUPPORT:
           msg = '不支持的认证等级';
           break;
         case userIAM.UserAuthResultCode.BUSY:
           msg = '忙碌状态';
           break;
         case userIAM.UserAuthResultCode.LOCKED:
           msg = '认证器已锁定';
           break;
         case userIAM.UserAuthResultCode.NOT_ENROLLED:
           msg = '用户未录入认证信息';
           break;
         case userIAM.UserAuthResultCode.CANCELED_FROM_WIDGET:
           msg = '当前的认证操作被用户从组件取消。返回这个错误码，表示使用应用自定义认证。';
         default:
           msg = '操作失败';
           break;
       }
       callback(success, result.result, msg);
     }
   });
   console.info('auth on success');
   // 开始认证
   userAuthInstance.start();
   ```

完整代码如下：

```ts
import userIAM from '@ohos.userIAM.userAuth';

/**
 * 认证类型
 */
export enum AuthType {
  FINGER,
  FACE
}

/**
 * 认证结果回调
 */
export type AuthCallback = (success: boolean, code: number, msg: string) => void;

// TAG
const TAG: string = 'UserAuthManager';
// 认证等级
const authTrustLevel: userIAM.AuthTrustLevel = userIAM.AuthTrustLevel.ATL1;
// widgetParam
const widgetParam: userIAM.WidgetParam = {
  title: '请验证已录入手机的指纹',
};

/**
 * 用户认证管理（指纹认证、人脸认证）
 */
export class UserAuthManager {
  /**
   * 用户指纹认证操作
   *
   * @param type 1：设置；2：登录
   */
  public static startUserAuth(type: AuthType, callback: AuthCallback) {

    let userAuthType: userIAM.UserAuthType = userIAM.UserAuthType.FINGERPRINT;
    let tip: string = '';

    switch (type) {
      case AuthType.FINGER:
        userAuthType = userIAM.UserAuthType.FINGERPRINT;
        tip = '指纹';
        break;
      case AuthType.FACE:
        userAuthType = userIAM.UserAuthType.FACE;
        tip = '人脸';
        break;
    }

    let authParam: userIAM.AuthParam = {
      challenge: new Uint8Array([49, 49, 49, 49, 49, 49]),
      authType: [userAuthType],
      authTrustLevel: authTrustLevel,
      skipLockedBiometricAuth: true
    };

    try {
      // 查询认证能力是否支持
      userIAM.getAvailableStatus(userAuthType, authTrustLevel);
    } catch (error) {
      console.error(TAG, 'auth catch error: ' + JSON.stringify(error));
      if (error['code'] && error['code'] == 12500010) { // 有：未禁用\无凭据
        callback(false, 12500010, `请先在本机系统中添加或设置指纹后才能使用此功能`);
      } else if (error['code'] && error['code'] == 12500005) { // 无：不支持
        callback(false, 12500005, `该设备不支持${tip}认证`);
      } else {
        callback(false, error['code'], `该设备不支持${tip}认证`); // 兜底
      }
      return;
    }

    try {
      // 获取认证对象
      let userAuthInstance = userIAM.getUserAuthInstance(authParam, widgetParam);
      console.info('get userAuth instance success');

      userAuthInstance.on('result', {
        onResult(result) {
          console.info('userAuthInstance callback result = ' + JSON.stringify(result));
          let success: boolean = false;
          let msg: string = '';
          switch (result.result) {
            case userIAM.UserAuthResultCode.SUCCESS:
              success = true;
              msg = '认证成功';
              break;
            case userIAM.UserAuthResultCode.FAIL:
              msg = '认证失败';
              break;
            case userIAM.UserAuthResultCode.CANCELED:
              msg = '操作取消';
              break;
            case userIAM.UserAuthResultCode.TIMEOUT:
              msg = '操作超时';
              break;
            case userIAM.UserAuthResultCode.TYPE_NOT_SUPPORT:
              msg = '不支持的认证类型';
              break;
            case userIAM.UserAuthResultCode.TRUST_LEVEL_NOT_SUPPORT:
              msg = '不支持的认证等级';
              break;
            case userIAM.UserAuthResultCode.BUSY:
              msg = '忙碌状态';
              break;
            case userIAM.UserAuthResultCode.LOCKED:
              msg = '认证器已锁定';
              break;
            case userIAM.UserAuthResultCode.NOT_ENROLLED:
              msg = '用户未录入认证信息';
              break;
            case userIAM.UserAuthResultCode.CANCELED_FROM_WIDGET:
              msg = '当前的认证操作被用户从组件取消。返回这个错误码，表示使用应用自定义认证。';
            default:
              msg = '操作失败';
              break;
          }
          callback(success, result.result, msg);
        }
      });
      console.info('auth on success');
      // 开始认证
      userAuthInstance.start();
      console.info('auth start success');
    } catch (error) {
      console.error('auth catch error: ' + JSON.stringify(error));
    }
  }
}

@Entry
@Component
struct Index {
  @State isPassUserAuth: boolean = false;
  @State isAuth: boolean = true; //此处根据需求可以持久化或者从服务端获取

  build() {
    Row() {
      if (!this.isPassUserAuth) {
        if (this.isAuth) {
          Column() {
            Button("指纹认证")
              .onClick(() => {
                UserAuthManager.startUserAuth(AuthType.FINGER, (suc, code, msg) => {
                  console.info(msg);
                  if (code === 12500009) {
                    this.isAuth = false;
                  }
                  this.isPassUserAuth = suc;
                });
              });
          };
        } else {
          Button("密码登录")
            .onClick(() => {
              // ...
            });
        }
      } else {
        Column() {
          Text('主页').fontSize(30);
        }.width('100%');
      }
    };
  }
}
```

## 常见FAQ

Q：如何获取指纹登录错误信息？

A：可使用[on](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)订阅身份认证过程中的提示信息，获得中间状态的枚举值[UserAuthTipCode](../harmonyos-references/js-apis-useriam-userauth.md#userauthtipcode20)。

Q：指纹认证是否有超时逻辑？

A：用户身份认证有超时逻辑，超时返回[UserAuthResultCode](../harmonyos-references/js-apis-useriam-userauth.md#userauthresultcode9)中的错误码12500004。不同的认证类型认证超时时间不同，不同的器件认证超时时间也不同默认超时时间不可更改。如果开发者想要自定义超时时间可参考[认证过程中取消认证](../harmonyos-guides/cancel-authentication.md)在系统超时取消认证即可。
