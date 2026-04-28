---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-select-invoice-title
title: 获取发票抬头
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取发票抬头
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:04b16ebd04aff0f030c5be6c945bc1546d6b616673527637101085627d02e07e
---

## 场景介绍

当应用需要获取用户发票抬头时，可使用Account Kit提供的发票助手能力，打开发票抬头选择页面，帮助用户快速选择或管理发票抬头。以下对Account Kit提供的发票助手能力进行介绍，获取发票抬头功能还可使用场景化控件[选择发票抬头Button](scenario-fusion-button-invoice-title.md)进行实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/9XeBQZSwRTmhJMCMtVpE2Q/zh-cn_image_0000002583478757.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=D5FD0432951D4F80D8E5586DEB0AF6CD76A13AB48F9CE0C6AD6B4E9DCDCD7FEC "点击放大")

## 约束与限制

Wearable、TV设备暂不支持使用获取发票抬头功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Q9bCguPDTieLbSreLCohzw/zh-cn_image_0000002552799108.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=8171B6ABF5284D5A65A4AB82B919C49116BCC53490DEB3863FC1C96DCE8C3C5A)

流程说明：

1. 用户需要使用发票抬头时，应用程序调用选择发票抬头API，打开华为账号发票抬头选择页。
2. 用户可以在发票抬头选择页选择已有发票抬头或者跳转到发票抬头管理页进行增加，点击确认后可将选择的发票抬头返回给应用。

## 接口说明

获取发票抬头关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-invoiceassistant.md)。

| 接口名 | 描述 |
| --- | --- |
| [selectInvoiceTitle](../harmonyos-references/account-api-invoiceassistant.md#selectinvoicetitle)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)): Promise<[InvoiceTitle](../harmonyos-references/account-api-invoiceassistant.md#invoicetitle)> | 调用该方法打开发票抬头选择页面，使用Promise异步回调返回选择的发票抬头。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。此场景无需申请账号权限。

## 开发步骤

1. 导入[invoiceAssistant](../harmonyos-references/account-api-invoiceassistant.md)模块及相关公共模块。

   ```
   1. import { invoiceAssistant } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[selectInvoiceTitle](../harmonyos-references/account-api-invoiceassistant.md#selectinvoicetitle)方法选择发票抬头页面。

   ```
   1. // 执行请求
   2. if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
   3. try {
   4. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   5. invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
   6. .then((data: invoiceAssistant.InvoiceTitle) => {
   7. hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
   8. const type: string = data.type;
   9. const title: string = data.title;
   10. const taxNumber: string = data.taxNumber;
   11. const companyAddress: string = data.companyAddress;
   12. const telephone: string = data.telephone;
   13. const bankName: string = data.bankName;
   14. const bankAccount: string = data.bankAccount;

   16. // 开发者处理type, title, taxNumber, companyAddress, telephone, bankName, bankAccount
   17. // ...

   19. })
   20. .catch((error: BusinessError<Object>) => {
   21. dealAllError(error);
   22. })
   23. } catch (error) {
   24. dealAllError(error);
   25. }
   26. } else {
   27. hilog.info(0x0000, 'testTag',
   28. 'The current device does not support the invoking of the selectInvoiceTitle interface.');
   29. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError<Object>): void {
   3. hilog.error(0x0000, 'testTag', `Failed to selectInvoiceTitle. Code: ${error.code}, message: ${error.message}`);
   4. }
   ```
