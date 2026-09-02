---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-4
title: 解决用户认证回调中onResult内部不能调用外部方法的问题
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 解决用户认证回调中onResult内部不能调用外部方法的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ba15644d8748400accfa0366a9cc65465251efdb07d426c1f70a29e221583889
---

## 问题现象

[UserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthinstance10)开启对认证结果'result'的监听，在回调方法中，onResult内部不能通过this.func()调用组件内的自定义方法。

```ts
this.userAuthInstance.on('result', {
  onResult(result) {
  // 判断用户认证是否成功
    if (result.result === 12500000) {
      // 此处不能通过`this.func()`调用组件内的自定义方法
    } else {
      console.error(result.result.toString())
    }
  }
});
```

## 背景知识

为了解决上述问题，可以[使用Emitter进行线程间通信](../harmonyos-guides/itc-with-emitter.md)。用户认证成功后在onResult内部发送指定事件，在外部订阅该事件，执行对应的方法。

Emitter用于在同一进程内不同线程或相同线程间发送和处理事件，本示例使用到了发送事件、单次订阅事件。

1. [emitter.emit](../harmonyos-references/js-apis-emitter.md#emitteremit11)：发送指定事件。
2. [emitter.on](../harmonyos-references/js-apis-emitter.md#emitteron11)：持续订阅指定事件，并在接收到该事件时，执行对应的回调处理函数。
3. [emitter.off](../harmonyos-references/js-apis-emitter.md#emitteroff11)：取消事件ID为eventId的所有订阅。

本示例涉及用户指纹认证，需要申请权限[ohos.permission.ACCESS\_BIOMETRIC](../harmonyos-guides/permissions-for-all.md#ohospermissionaccess_biometric)，允许应用使用生物特征识别能力进行身份认证。

## 解决方案

1. 定义两个事件：onAuthFingerprint用户认证的事件，getAuthFingerprintResult获取到用户认证结果的事件。

   定义一个用户认证的类BiometricUtil，在构造函数中开启监听onAuthFingerprint事件。在接收到该事件后，执行this.onAuthFingerprint(data)方法，在该方法中发送getAuthFingerprintResult事件。
2. 在用户认证结果回调的onResult内部通过emitter线程间通信，当用户认证成功后，发送onAuthFingerprint事件，触发步骤1的流程。
3. 在用户点击按钮调用认证时，监听获取认证返回结果的事件getAuthFingerprintResult，并调用用户验证方法：new BiometricUtil().startAuthFingerprint()。

完整代码如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { emitter } from '@kit.BasicServicesKit';

@Entry
@Component
struct Biometric {
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Button('指纹认证调用')
        .fontSize(12)
        .onClick(() => {
          // 订阅监听事件
          emitter.on('getAuthFingerprintResult', (emitterData: emitter.EventData) => {
            if (emitterData.data !== undefined && emitterData.data.data !== undefined) {
              let data = emitterData.data.data as string;
              this.uiContext.showAlertDialog({
                message: data
              });
              emitter.off('getAuthFingerprintResult');
            }
          });
          // 执行指纹验证方法
          new BiometricUtil().startAuthFingerprint();
        });
    }.width('100%')
    .height('100%');
  }
}

class BiometricUtil {
  // 用于定义初始化方法中转站
  constructor() {
    emitter.on('onAuthFingerprint', (emitterData: emitter.EventData) => {
      if (emitterData.data !== undefined && emitterData.data.data !== undefined) {
        let data = emitterData.data.data as string;
        this.onAuthFingerprint(data);
        emitter.off('onAuthFingerprint');
      }
    });
  }

  startAuthFingerprint() {
    try {
      if (canIUse('SystemCapability.UserIAM.UserAuth.Core')) {
        userAuth.getAvailableStatus(userAuth.UserAuthType.FINGERPRINT, userAuth.AuthTrustLevel.ATL3);
        let randData: Uint8Array = cryptoFramework.createRandom().generateRandomSync(16).data;
        let authParam: userAuth.AuthParam = {
          challenge: randData,
          authType: [userAuth.UserAuthType.FINGERPRINT],
          authTrustLevel: userAuth.AuthTrustLevel.ATL3,
        };
        let widgetParam: userAuth.WidgetParam = {
          title: '请使用指纹认证',
        };
        let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
        // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
        userAuthInstance.on('result', {
          onResult(result) {
            // 判断用户认证是否成功
            if (result.result === userAuth.UserAuthResultCode.SUCCESS) {
              let eventData: emitter.EventData = {
                data: { 'data': '认证成功' }
              };
              // 成功后调用中转站方法
              emitter.emit('onAuthFingerprint', eventData);
            } else {
              console.error(`Authentication failed: ${result.result}`);
            }
          }
        });
        userAuthInstance.start();
      }
    } catch (error) {
      console.error(`Authentication catch error. code is ${error.code}, message is ${error.message}`);
      let eventData: emitter.EventData = {
        data: { 'data': this.getErrorMsg(error.code) }
      };
      // 成功后调用中转站方法
      emitter.emit('onAuthFingerprint', eventData);
    }
  }

  onAuthFingerprint(data: string) {
    let eventData: emitter.EventData = {
      data: { 'data': data }
    };
    emitter.emit('getAuthFingerprintResult', eventData);
  }

  getErrorMsg(code: number): string {
    switch (code) {
      case 12500005:
        return '认证类型不支持';
      case 12500006:
        return '认证等级不支持';
      case 12500010:
        return '未录入指纹认证凭据';
      case 12500013:
        return '密码过期请重新设置';
      default:
        return '认证发生错误';
    }
  }
}
```
