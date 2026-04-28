---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-launchapp
title: 打开APP Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 打开APP Button
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c35dee8eee10c64c857a46ecc166c418080c21c09de06ad708a6495a8bc80c43
---

## 场景介绍

打开APP功能可以帮助调用对应Button组件打开另一个应用。

运行示例代码单击“打开APP”按钮，出现提示弹窗，单击“允许”，跳转至新的应用页面。

说明

弹窗是否弹出以及弹窗效果与跳转目标APP相关。

## 约束与限制

打开APP Button支持Phone、Tablet和2in1设备，并且从5.1.0(18)版本开始，新增支持TV设备。

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
   10. // OpenType.LAUNCH_APP表示该按钮用于启动应用。
   11. openType: functionalButtonComponentManager.OpenType.LAUNCH_APP,
   12. label: '打开APP',
   13. // 当OpenType为functionButtonComponentManager.OpenType.LAUNCH_APP时，appParam为必填项。
   14. appParam: {
   15. bundleName: "xxx",
   16. abilityName: "xxx"
   17. },
   18. // 调整按钮样式。
   19. styleOption: {
   20. styleConfig: new functionalButtonComponentManager.ButtonConfig()
   21. .fontSize(20)
   22. },
   23. },
   24. // 当OpenType设置为LAUNCH_APP时，回调函数必须是onLaunchAPP。
   25. controller: new functionalButtonComponentManager.FunctionalButtonController().onLaunchApp((err) => {
   26. if (err) {
   27. // 错误日志处理。
   28. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
   29. return;
   30. }
   31. // 处理成功。成功时不会返回任何值。
   32. hilog.info(0x0000, "testTag", "succeeded in launching app");
   33. })
   34. })
   35. }
   36. .width('100%')
   37. }
   38. .height('100%')
   39. }
   40. }
   ```

   说明

   * openType参数填写"functionalButtonComponentManager.OpenType.LAUNCH\_APP"指定Button为打开APP类型。
   * openType为"functionalButtonComponentManager.OpenType.LAUNCH\_APP"时，appParam参数必填。
   * "bundleName"为包名，"abilityName"为Ability名称。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onLaunchApp"。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
