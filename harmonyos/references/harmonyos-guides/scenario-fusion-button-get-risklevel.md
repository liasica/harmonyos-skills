---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-get-risklevel
title: 获取手机号和风险等级Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 获取手机号和风险等级Button
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0f66d6363fdc349547a368133797f449b9b138fbbad07ecd92125cd8e29dab85
---

## 场景介绍

从6.0.2(22)开始，支持获取手机号和风险等级Button功能。

开发者可通过“获取手机号和风险等级Button”获取授权码（Authorization Code），进而获取用户的手机号和风险等级信息，用于对恶意账号进行风险控制，进一步增强应用的安全性。风险等级完整场景详见[获取风险等级](account-get-risklevel-on-demand-acquisition.md)。

## 约束与限制

获取手机号和风险等级Button支持Phone、Tablet、PC/2in1和TV设备。

## 前提条件

应用开发需要完成“获取您的手机号”权限申请和获取风险等级权限申请，分别参见[申请账号权限](account-config-permissions.md)和[开发前提](account-get-risklevel-on-demand-acquisition.md#开发前提)章节。

元服务应用开发需要完成“获取您的手机号”权限申请和获取风险等级权限申请，分别参见[申请账号权限](../atomic-guides/account-guide-atomic-permissions.md)和[开发前提](../atomic-guides/account-guide-atomic-get-risklevel.md#开发前提)章节。

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
               // OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL表示该按钮用于获取手机号和风险等级。
               openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL,
               label: '获取手机号和风险等级',
               // 调整按钮样式。
               styleOption: {
                 styleConfig: new functionalButtonComponentManager.ButtonConfig()
                   .fontSize(20)
               }
             },
             // 当OpenType为GET_PHONE_NUMBER_AND_RISK_LEVEL时，回调必须为onGetPhoneNumberAndRiskLevel。
             controller: new functionalButtonComponentManager.FunctionalButtonController()
               .onGetPhoneNumberAndRiskLevel((data) => {
                 if (data?.errCode) {
                   // 错误日志处理。
                   hilog.error(0x0000, 'testTag', 'Failed to authenticate, error: %{public}d %{public}s', data?.errCode, data?.errMsg);
                   return;
                 }
                 // 成功日志处理。
                 hilog.info(0x0000, 'testTag', 'succeeded in authentication');
                 // 授权码处理。
                 let authorizationCode = data?.code;
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

   * openType参数填写"functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL"指定Button为获取手机号和风险等级类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onGetPhoneNumberAndRiskLevel"。
   * 若成功调用，可通过回调函数中的授权码（Authorization Code）获取用户的手机号和风险等级。风险等级完整场景详见[获取风险等级](account-get-risklevel-on-demand-acquisition.md)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
