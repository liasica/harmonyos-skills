---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-invoice-title
title: 选择发票抬头Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 选择发票抬头Button
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48115c5b5d80b7b9341a9975c4abebc9749b5c06e64635d2ba3e5e24ce4a9132
---

## 场景介绍

选择发票抬头Button功能可以帮助开发者调用对应Button组件跳转发票抬头选择页面，供用户完成已保存发票抬头的选择。

运行示例代码单击“选择发票抬头”按钮，拉起选择发票抬头页面可选择已保存发票，也可单击“管理发票抬头”进入新增企业/个人发票抬头页面（完整场景请参考[获取发票抬头](account-select-invoice-title.md)）。

## 前提条件

参见[开发前提](account-select-invoice-title.md#开发前提)。

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
   10. // OpenType.CHOOSE_INVOICE_TITLE表示该按钮用于选择发票抬头。
   11. openType: functionalButtonComponentManager.OpenType.CHOOSE_INVOICE_TITLE,
   12. label: '选择发票抬头',
   13. // 调整按钮样式。
   14. styleOption: {
   15. bgColor: functionalButtonComponentManager.ColorType.DEFAULT,
   16. size: functionalButtonComponentManager.SizeType.DEFAULT,
   17. plain: false,
   18. disabled: false,
   19. loading: false,
   20. hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
   21. hoverStartTime: 0,
   22. hoverStayTime: 0,
   23. styleConfig: new functionalButtonComponentManager.ButtonConfig()
   24. .fontSize(20)
   25. },
   26. },
   27. // 当OpenType为CHOOSE_INVOICE_TITLE时，回调必须为onChooseInvoiceTitle。
   28. controller: new functionalButtonComponentManager.FunctionalButtonController()
   29. .onChooseInvoiceTitle((err, data) => {
   30. if (err) {
   31. // 错误日志处理。
   32. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
   33. return;
   34. }
   35. // 成功日志处理。
   36. hilog.info(0x0000, "testTag", "succeeded in obtaining invoice title");
   37. // 获取发票信息。
   38. let type: string = data.type;
   39. let title: string = data.title;
   40. let taxNumber: string = data.taxNumber;
   41. let companyAddress: string | undefined = data.companyAddress;
   42. let telephone: string | undefined = data.telephone;
   43. let bankName: string | undefined = data.bankName;
   44. let bankAccount: string | undefined = data.bankAccount;
   45. })
   46. })
   47. }
   48. .width('100%')
   49. }
   50. .height('100%')
   51. }
   52. }
   ```

   说明

   * openType参数填写"functionalButtonComponentManager.OpenType.CHOOSE\_INVOICE\_TITLE"指定Button为选择发票抬头类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onChooseInvoiceTitle"。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
