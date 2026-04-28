---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-permissiononsetting
title: 权限设置Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 权限设置Button
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3321af534c690805410a7ee4e6582d149ad60812c10d8abeb73a8e04ab499f94
---

## 场景介绍

权限设置Button可以帮助开发者调用对应Button组件，二次拉起权限设置弹框。

运行示例代码单击“请求用户授权”按钮触发首次权限设置弹框，选择“不允许”后，单击“权限设置”按钮拉起二次授权页面。

## 约束与限制

权限设置Button支持Phone、Tablet和2in1设备，并且从5.1.0(18)版本开始，新增支持TV设备。

说明

仅支持UIAbility/UIExtensionAbility。

在调用此接口前，应用需要先调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)，如果用户在首次权限设置弹框时已授权，调用当前接口将无法拉起二次授权页面。

## 前提条件

* 调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口，用户在首次权限设置弹框时拒绝授权。
* 参见[开发准备](scenario-fusion-preparations.md)。

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 在容器中声明FunctionalButton，指定Button的openType，并设置对应的回调函数，代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. Row() {
   6. Column({ space: 3 }) {
   7. // 调用requestPermissionsFromUser接口Button。
   8. Button('请求用户授权')
   9. .fontSize(20)
   10. .onClick(() => {
   11. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   12. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   13. try {
   14. // 在module.json5文件中添加ohos.permission.READ_CALENDAR、ohos.permission.WRITE_CALENDAR权限。
   15. atManager.requestPermissionsFromUser(context,
   16. ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'],
   17. (err: BusinessError, data: PermissionRequestResult) => {
   18. if (err) {
   19. hilog.error(0x0000, "testTag", "failed in requesting Permissions from user : %{public}d %{public}s",
   20. err.code, err.message);
   21. } else {
   22. hilog.info(0x0000, "testTag", 'data permissions: %{public}s', data.permissions?.join(','));
   23. hilog.info(0x0000, "testTag", 'data authResults: %{public}s', data.authResults?.join(','));
   24. hilog.info(0x0000, "testTag", 'data dialogShownResults: %{public}s', data.dialogShownResults?.join(','));
   25. }
   26. })
   27. } catch (err) {
   28. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
   29. }
   30. })

   32. // 构建FunctionalButton组件实例。
   33. FunctionalButton({
   34. params: {
   35. // OpenType.PERMISSION_SETTING表示该按钮用于设置权限。
   36. openType: functionalButtonComponentManager.OpenType.PERMISSION_SETTING,
   37. label: '权限设置',
   38. permissionListParam: ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'],
   39. // 调整按钮样式。
   40. styleOption: {
   41. styleConfig: new functionalButtonComponentManager.ButtonConfig()
   42. .fontSize(20)
   43. },
   44. },
   45. // 当OpenType设置为PERMISSION_SETTING时，回调必须为onPermissionSetting。
   46. controller: new functionalButtonComponentManager.FunctionalButtonController().onPermissionSetting((err,
   47. data) => {
   48. if (err) {
   49. // 错误日志处理。
   50. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
   51. return;
   52. }
   53. // 成功日志处理。
   54. hilog.info(0x0000, "testTag", "succeeded in setting permission ");
   55. let result = data.permissionResult;
   56. result.forEach(res => {
   57. hilog.info(0x0000, "testTag", "data: %{public}s", String(res));
   58. })
   59. })
   60. })
   61. }
   62. .width('100%')
   63. }
   64. .height('100%')
   65. }
   66. }
   ```

   说明

   * openType参数填写"functionalButtonComponentManager.OpenType.PERMISSION\_SETTING"指定Button为权限设置类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onPermissionSetting"。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

     其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
