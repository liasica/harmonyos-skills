---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-select-invoice-title
title: 获取发票抬头
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取发票抬头
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0f15f0a82df8399c5c538fe438145cc72e7aa7e15c2b557e8a97b87083a87b3d
---

## 场景介绍

当应用需要获取用户发票抬头时，可使用Account Kit提供的发票助手能力，打开发票抬头选择页面，帮助用户快速选择或管理发票抬头。以下对Account Kit提供的发票助手能力进行介绍，获取发票抬头功能还可使用场景化控件[选择发票抬头Button](scenario-fusion-button-invoice-title.md)进行实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/_WkjfVMxQFyuXLes5QT-Mg/zh-cn_image_0000002706834768.png "点击放大")

## 约束与限制

Wearable、TV设备暂不支持使用获取发票抬头功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/yr6eSX6PStaUmADKsUQ0Bg/zh-cn_image_0000002736313875.png)

流程说明：

1. 用户需要使用发票抬头时，应用程序调用选择发票抬头API，打开华为账号发票抬头选择页。
2. 用户可以在发票抬头选择页选择已有发票抬头或者跳转到发票抬头管理页进行增加，点击确认后可将选择的发票抬头返回给应用。

## 接口说明

获取发票抬头关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-invoiceassistant.md)。

| 接口名 | 描述 |
| --- | --- |
| [selectInvoiceTitle](../harmonyos-references/account-api-invoiceassistant.md#selectinvoicetitle)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)): Promise<[InvoiceTitle](../harmonyos-references/account-api-invoiceassistant.md#invoicetitle)> | 调用该方法打开发票抬头选择页面，使用Promise异步回调返回选择的发票抬头。 |

**注意** 

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。此场景无需申请账号权限。

## 开发步骤

1. 导入[invoiceAssistant](../harmonyos-references/account-api-invoiceassistant.md)模块及相关公共模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { invoiceAssistant } from '@kit.AccountKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[selectInvoiceTitle](../harmonyos-references/account-api-invoiceassistant.md#selectinvoicetitle)方法选择发票抬头页面。

   ```typescript
   try {
     if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
       invoiceAssistant.selectInvoiceTitle(context).then((data: invoiceAssistant.InvoiceTitle) => {
         // ...
       }).catch((error: BusinessError) => {
         hilog.error(domainId, logTag,
           `Failed to selectInvoiceTitle. BusinessError errCode: ${error.code}, errMessage: ${error.message}`);
       });
     } else {
       hilog.error(domainId, logTag, 'The API is not supported on this device.');
     }
   } catch (error) {
     hilog.error(domainId, logTag,
       `Failed to selectInvoiceTitle. errCode: ${error.code}, errMessage: ${error.message}`);
   }
   ```
