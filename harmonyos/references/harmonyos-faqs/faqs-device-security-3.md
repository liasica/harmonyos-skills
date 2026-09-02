---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-3
title: 如何解决校验设备token时报错“InvalidDeviceToken”的问题
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 如何解决校验设备token时报错“InvalidDeviceToken”的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:1fffb22f6099993617a48af74101bc276104f7a5a73f801f75bbfcd2a1ccf2ea
---

## 问题现象

应用设备检测场景中，使用checkDeviceToken API校验设备Token时，如何解决报错InvalidDeviceToken的问题。

## 背景知识

[checkDeviceToken](../harmonyos-references/devicesecurity-deviceverify-checkdevicetoken.md)返回的错误码有以下几种：

| 错误码 | 描述 |
| --- | --- |
| OK | 请求处理成功。 |
| InvalidDeviceToken | deviceToken缺失或不合法。 |
| DeviceTokenExpired | deviceToken过期。 |
| InvalidTimeStamp | timeStamp缺失或不合法。 |
| InternalServerError | 服务器内部错误。 |
| InvalidBundleName | bundleName缺失或不合法。 |

## 解决方案

针对deviceToken缺失或者不合法问题，要从deviceToken生成和请求发送过程进行分析。

* deviceToken生成过程：
  1. 检查是否已“[开通Device Security服务](../harmonyos-guides/devicesecurity-deviceverify-activateservice.md)”中的应用设备状态检测能力并[申请调试Profile](../app/agc-help-debug-cert-0000002283256797.md)。
  2. 检查生成deviceToken代码是否合理，参考以下示例代码：

     ```ts
     import { deviceCertificate } from '@kit.DeviceSecurityKit';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';

     const TAG = "DeviceCertificateJsTest";

     @Entry
     @Component
     struct Index {
       private message: string = '获取设备Token';

       build() {
         RelativeContainer() {
           Text(this.message)
             .id('getDeviceToken')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               this.getDeviceToken();
             })
         }
         .height('100%')
         .width('100%')
       }

       /**
        * 获取设备的token
        * @returns
        */
       getDeviceToken(): string {
         let res = "";
         try {
           deviceCertificate.getDeviceToken().then((token) => {
             hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
             console.info('token：' + token);
           }).catch((err: BusinessError) => {
             hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
           });
         } catch (err) {
           let error: BusinessError = err as BusinessError;
           hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
         }
         return res;
       }
     }
     ```
  3. 检查deviceToken参数类型，deviceToken类型参数需要定义为String类型。
  4. 检查deviceToken生成时间，防止失效。deviceToken由Device Security Kit加密生成，每次调用生成Token均不一样，有效期1小时。

* 请求发送过程：
  1. 检查是否正确获取服务账号令牌，服务账号令牌获取指导详情请参见[基于服务账号生成鉴权令牌](../harmonyos-guides/devicesecurity-deviceverify-token.md)。
  2. 检查消息体构造是否正确。请求构造过程需要构造请求消息体时，消息体需要在外层包一层data结构。详情参考如[请求示例](../harmonyos-references/devicesecurity-deviceverify-checkdevicetoken.md#请求示例)。
