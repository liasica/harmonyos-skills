---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-1
title: 如何通过指纹登录
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 如何通过指纹登录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dfef835e036bb68096afef2595190abdd90e2d8d0a745a019a77ae8fb9705d57
---

## 问题现象

对于支持指纹验证的设备，如何实现指纹登录？

## 背景知识

* [User Authentication Kit](../harmonyos-guides/user-authentication-overview.md)提供了基于用户在设备本地注册的锁屏口令、人脸和指纹来认证用户身份的能力。
* [嵌入式用户身份认证控件](../harmonyos-references/ohos-useriam-userauthicon.md)。提供应用界面上展示的人脸、指纹认证图标，具体功能如下：
  1. 提供嵌入式的人脸、指纹认证控件图标，可被应用集成。
  2. 支持自定义图标的颜色和大小，但图标样式不可变更。
  3. 点击控件图标后将以系统弹窗的方式，拉起人脸、指纹认证控件。

## 解决方案

1. 在手机设置中录入个人指纹，完成指纹验证功能设置。
2. 在**对应模块的module.json5**文件中找到requestPermissions字段配置**ohos.permission.ACCESS\_BIOMETRIC**权限。

   ```json
   {
     "name": "ohos.permission.ACCESS_BIOMETRIC"
   },
   ```
3. [查询认证能力是否支持](../harmonyos-guides/obtain-supported-authentication-capabilities.md#开发步骤)，需要根据[错误码](../harmonyos-references/errorcode-useriam.md)的不同，给予用户不同的提示。

   ```ts
   // 查询认证能力是否支持。
   try {
     userAuth.getAvailableStatus(userAuth.UserAuthType.FINGERPRINT, userAuth.AuthTrustLevel.ATL3);
     console.info('current auth trust level is supported');
     this.isAvi = true;
   } catch (error) {
     const err: BusinessError = error as BusinessError;
     this.isAvi = false;
     console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
   }
   ```
4. 使用嵌入式用户身份认证控件。

   ```ts
   UserAuthIcon({
     authParam: this.authParam,
     widgetParam: this.widgetParam,
     iconHeight: 200,
     iconColor: this.isAvi ? Color.Blue : Color.Red,
     onIconClick: () => {
       console.info('The user clicked the icon.');
     },
     onAuthResult: (result: userAuth.UserAuthResult) => {
       console.info(`Get user auth result, result = ${JSON.stringify(result.result)}`);
       if (result.result === 12500000) {
         setTimeout(() => {
           this.isPassUserAuth = true;
         }, 1000);
       }
     }
   }).alignSelf(ItemAlign.Center);
   ```

完整示例参考如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct UserAuth {
  rand = cryptoFramework.createRandom();
  len: number = 16;
  randData: Uint8Array = this.rand?.generateRandomSync(this.len)?.data;
  authParam: userAuth.AuthParam = {
    challenge: this.randData,
    authType: [userAuth.UserAuthType.FINGERPRINT],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3
  };
  widgetParam: userAuth.WidgetParam = {
    title: '请进行身份认证'
  };
  @State isPassUserAuth: boolean = false;
  private isAvi: boolean = false;

  checkFinger() {
    // 查询认证能力是否支持。
    try {
      userAuth.getAvailableStatus(userAuth.UserAuthType.FINGERPRINT, userAuth.AuthTrustLevel.ATL3);
      console.info('current auth trust level is supported');
      this.isAvi = true;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      this.isAvi = false;
      console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
    }
  }

  aboutToAppear(): void {
    this.checkFinger();
  }

  build() {
    Row() {
      Column() {
        if (!this.isAvi) {
          Text('请录入指纹或者请确认设备支持指纹登录').fontSize(30).fontColor(Color.Red);
        } else {
          if (!this.isPassUserAuth) {
            UserAuthIcon({
              authParam: this.authParam,
              widgetParam: this.widgetParam,
              iconHeight: 200,
              iconColor: this.isAvi ? Color.Blue : Color.Red,
              onIconClick: () => {
                console.info('The user clicked the icon.');
              },
              onAuthResult: (result: userAuth.UserAuthResult) => {
                console.info(`Get user auth result, result = ${JSON.stringify(result.result)}`);
                if (result.result === 12500000) {
                  setTimeout(() => {
                    this.isPassUserAuth = true;
                  }, 1000);
                }
              }
            }).alignSelf(ItemAlign.Center);
          } else {
            Column() {
              Image($r('app.media.startIcon')).width(30);
              Text('主页').fontSize(30);
            }.width('100%');
          }
        }
      }.justifyContent(FlexAlign.Center);
    }.width('100%').height('100%').justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：HarmonyOS在不用User Authentication Kit的情况下，系统有没有提供自定义认证界面底层的认证逻辑开发相关能力？

A：User Authentication Kit（用户认证服务）提供了系统级多设备统一的、集多种认证方式于一体的系统级用户身份认证控件。HarmonyOS屏蔽不同认证因子的差异，实现调用锁屏口令、人脸、指纹认证的接口归一，并不提供单独的身份认证接口。若伙伴有自定义认证界面的需求，具体认证逻辑需自行实现。

Q：使用ArkUI-X进行跨平台开发，可否使用Authentication相关接口实现登录功能？

A：安全认证Authentication相关的接口实现登录功能，当前是不支持跨平台的，需改用标准登录。
