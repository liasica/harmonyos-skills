---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-getphonenumber
title: 快速验证手机号Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 快速验证手机号Button
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cceaa8cd5690d2801eeeb0f884e18ea0d3da64af6d3b64443519692dcfcce920
---

## 场景介绍

快速验证手机号Button功能用于帮助开发者向用户发起手机号申请，应用在满足《[常见类型移动互联网应用程序必要个人信息范围规定](http://www.cac.gov.cn/2021-03/22/c_1617990997054277.htm)》（对第三方网站的内容，华为公司不承担任何责任）中使用手机号的必要业务场景，经用户同意后，应用可获取手机号，为用户提供相应服务（详见快速验证[场景介绍](account-get-phonenumber.md#场景介绍)）。

运行示例代码单击“快速验证手机号”按钮，拉起验证页面（完整场景可参考[快速验证](account-get-phonenumber.md)）。

## 约束与限制

快速验证手机号Button支持Phone、Tablet和2in1设备，并且从5.1.0(18)版本开始，新增支持TV设备。

说明

应用/元服务仅在首次使用时需要用户进行授权，授权成功后，后续只验证授权手机号，不可修改。

## 前提条件

参见[开发前提](account-get-phonenumber.md#开发前提)。

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
   10. // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
   11. openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
   12. label: '快速验证手机号',
   13. // 调整按钮样式。
   14. styleOption: {
   15. styleConfig: new functionalButtonComponentManager.ButtonConfig()
   16. .fontSize(20)
   17. },
   18. },
   19. // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
   20. controller: new functionalButtonComponentManager.FunctionalButtonController()
   21. .onGetPhoneNumber((err, data) => {
   22. if (err) {
   23. // 错误日志处理。
   24. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
   25. return;
   26. }
   27. // 成功日志处理。
   28. hilog.info(0x0000, "testTag", "succeeded in authenticating");
   29. // 授权码处理。
   30. let authorizationCode = data.code;
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

   * openType参数填写"functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER"指定Button为快速验证手机号类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onGetPhoneNumber"。
   * 若成功调用，可通过回调函数中的临时登录凭证（Authorization Code）获取真实手机号，临时登录凭证时效5分钟，具体操作可参考[服务端开发](account-get-phonenumber.md#服务端开发)。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
