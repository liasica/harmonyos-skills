---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-invoice-title
title: 选择发票抬头Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 选择发票抬头Button
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:3bcf9dac3f700f322e3cc92a287ae75f27061f76b0d2e3b9a0f4e0fe8381ed49
---

## 场景介绍

选择发票抬头Button功能可以帮助开发者调用对应Button组件跳转发票抬头选择页面，供用户完成已保存发票抬头的选择。

运行示例代码单击“选择发票抬头”按钮，拉起选择发票抬头页面可选择已保存发票，也可单击“管理发票抬头”进入新增企业/个人发票抬头页面（完整场景请参考[获取发票抬头](account-select-invoice-title.md)）。

## 前提条件

应用开发前提条件，参见[开发前提](account-select-invoice-title.md#开发前提)。

元服务应用开发前提条件，参见[开发前提](../atomic-guides/account-guide-atomic-select-invoice-title.md#开发前提)。

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
               // OpenType.CHOOSE_INVOICE_TITLE表示该按钮用于选择发票抬头。
               openType: functionalButtonComponentManager.OpenType.CHOOSE_INVOICE_TITLE,
               label: '选择发票抬头',
               // 调整按钮样式。
               styleOption: {
                 bgColor: functionalButtonComponentManager.ColorType.DEFAULT,
                 size: functionalButtonComponentManager.SizeType.DEFAULT,
                 plain: false,
                 disabled: false,
                 loading: false,
                 hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
                 hoverStartTime: 0,
                 hoverStayTime: 0,
                 styleConfig: new functionalButtonComponentManager.ButtonConfig()
                   .fontSize(20)
               }
             },
             // 当OpenType为CHOOSE_INVOICE_TITLE时，回调必须为onChooseInvoiceTitle。
             controller: new functionalButtonComponentManager.FunctionalButtonController()
               .onChooseInvoiceTitle((err, data) => {
                 if (err) {
                   // 错误日志处理。
                   hilog.error(0x0000, 'testTag', 'Failed to obtain invoice title, error: %{public}d %{public}s', err.code, err.message);
                   return;
                 }
                 // 成功日志处理。
                 hilog.info(0x0000, 'testTag', 'succeeded in obtaining invoice title');
                 // 获取发票信息。
                 let type: string = data.type;
                 let title: string = data.title;
                 let taxNumber: string = data.taxNumber;
                 let companyAddress: string | undefined = data.companyAddress;
                 let telephone: string | undefined = data.telephone;
                 let bankName: string | undefined = data.bankName;
                 let bankAccount: string | undefined = data.bankAccount;
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

   * openType参数填写"functionalButtonComponentManager.OpenType.CHOOSE\_INVOICE\_TITLE"指定Button为选择发票抬头类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onChooseInvoiceTitle"。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
