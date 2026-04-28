---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-get-risklevel
title: 获取手机号和风险等级Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 获取手机号和风险等级Button
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:13dac17dc06d2daaa2d5e692bcc2a1bad10ed5ffd1261e4e74550aa1f93a1fcb
---

## 场景介绍

从6.0.2(22)开始，支持获取手机号和风险等级Button功能。

开发者可通过“获取手机号和风险等级Button”获取授权码（Authorization Code），进而获取用户的手机号和风险等级信息，用于对恶意账号进行风险控制，进一步增强应用的安全性。风险等级完整场景详见[获取风险等级](account-get-risklevel-on-demand-acquisition.md)。

## 前提条件

需要完成手机号的scope权限申请和【获取风险等级】权限申请，请见[申请账号权限](account-config-permissions.md)和[开发前提](account-get-risklevel-on-demand-acquisition.md#开发前提)章节。

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在容器中声明FunctionalButton，指定Button的openType，并设置对应的回调函数，代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. Row() {
   6. Column() {
   7. // 构建FunctionalButton组件实例。
   8. FunctionalButton({
   9. params: {
   10. // OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL表示该按钮用于获取手机号和风险等级。
   11. openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL,
   12. label: '获取手机号和风险等级',
   13. // 调整按钮样式。
   14. styleOption: {
   15. styleConfig: new functionalButtonComponentManager.ButtonConfig()
   16. .fontSize(20)
   17. },
   18. },
   19. // 当OpenType为GET_PHONE_NUMBER_AND_RISK_LEVEL时，回调必须为onGetPhoneNumberAndRiskLevel。
   20. controller: new functionalButtonComponentManager.FunctionalButtonController()
   21. .onGetPhoneNumberAndRiskLevel((data) => {
   22. if (data?.errCode) {
   23. // 错误日志处理。
   24. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", data?.errCode, data?.errMsg);
   25. return;
   26. }
   27. // 成功日志处理。
   28. hilog.info(0x0000, "testTag", "succeeded in authentication");
   29. // 授权码处理。
   30. let authorizationCode = data?.code;
   31. })
   32. })
   33. }
   34. .width('100%')
   35. }
   36. .height('100%')
   37. }
   38. }
   ```

   说明

   * openType参数填写"functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL"指定Button为获取手机号和风险等级类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onGetPhoneNumberAndRiskLevel"。
   * 若成功调用，可通过回调函数中的授权码（Authorization Code）获取用户的手机号和风险等级。风险等级完整场景详见[获取风险等级](account-get-risklevel-on-demand-acquisition.md)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
