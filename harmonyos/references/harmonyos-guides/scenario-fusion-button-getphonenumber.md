---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-getphonenumber
title: 快速验证手机号Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 快速验证手机号Button
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:1c1e1419cbc6d6aef0e757732fb106ebeb9e2e4d903a306002ddc7ea79476cc4
---

## 场景介绍

快速验证手机号Button功能用于帮助开发者向用户发起手机号申请，应用在满足《[常见类型移动互联网应用程序必要个人信息范围规定](http://www.cac.gov.cn/2021-03/22/c_1617990997054277.htm)》（对第三方网站的内容，华为公司不承担任何责任）中使用手机号的必要业务场景，经用户同意后，应用可获取手机号，为用户提供相应服务（详见获取手机号[场景介绍](account-get-phonenumber.md#场景介绍)）。

运行示例代码单击“快速验证手机号”按钮，拉起验证页面（完整场景可参考[获取手机号](account-get-phonenumber.md)）。

## 约束与限制

快速验证手机号Button支持Phone、Tablet和PC/2in1设备，并且从5.1.0(18)版本开始，新增支持TV设备。

**说明** 

应用/元服务仅在首次使用时需要用户进行授权，授权成功后，后续只验证授权手机号，不可修改。

## 前提条件

应用开发前提条件，参见[开发前提](account-get-phonenumber.md#开发前提)。

元服务应用开发前提条件，参见[开发前提](../atomic-guides/account-guide-atomic-get-phonenumber.md#开发前提)。

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```typescript
   import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在容器中声明FunctionalButton，指定Button的openType，并设置对应的回调函数，代码如下：

   ```typescript
   @Entry
   @Component
   struct Index {
     build() {
       Row() {
         Column() {
           // 构建FunctionalButton组件实例。
           FunctionalButton({
             params: {
               // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
               openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
               label: '快速验证手机号',
               // 调整按钮样式。
               styleOption: {
                 styleConfig: new functionalButtonComponentManager.ButtonConfig()
                   .fontSize(20)
               }
             },
             // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
             controller: new functionalButtonComponentManager.FunctionalButtonController()
               .onGetPhoneNumber((err, data) => {
                 if (err) {
                   // 错误日志处理。
                   hilog.error(0x0000, 'testTag', 'Failed to authenticate, error: %{public}d %{public}s', err.code, err.message);
                   return;
                 }
                 // 成功日志处理。
                 hilog.info(0x0000, 'testTag', 'succeeded in authenticating');
                 // 授权码处理。
                 let authorizationCode = data.code;
               })
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

   **说明** 

   * openType参数填写"functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER"指定Button为快速验证手机号类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onGetPhoneNumber"。
   * 若成功调用，可通过回调函数中的临时登录凭证（Authorization Code）获取真实手机号，临时登录凭证时效5分钟，具体操作可参考[服务端开发](account-get-phonenumber.md#服务端开发)。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
