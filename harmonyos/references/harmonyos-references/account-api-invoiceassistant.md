---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-invoiceassistant
title: invoiceAssistant (华为账号发票助手服务)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > invoiceAssistant (华为账号发票助手服务)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5479e236c36d4c42e3800d28e6fb7bb241b2a3a16f8d006bf7daadfac05e78d4
---

本模块提供Account Kit的发票助手能力。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { invoiceAssistant } from '@kit.AccountKit';
```

## InvoiceAssistantErrorCode

PhonePC/2in1Tablet

该枚举定义了Account Kit发票助手服务相关接口的错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HuaweiID.InvoiceAssistant

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| USER\_CANCELED | [1010060001](account-api-error-code.md#section1010060001-用户取消发票服务) | 用户取消发票助手服务。 |
| SYSTEM\_ERROR | [1010060002](account-api-error-code.md#section1010060002-系统内部错误) | 系统内部错误。 |
| APP\_NOT\_AUTHORIZED | [1010060003](account-api-error-code.md#section1010060003-应用指纹证书校验失败) | 应用指纹证书校验失败。 |
| FREQUENT\_CALLS | [1010060004](account-api-error-code.md#section1010060004-调用过于频繁) | 接口调用过于频繁。 |
| NETWORK\_ERROR | [1010060005](account-api-error-code.md#section1010060005-网络连接错误) | 网络连接错误。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1010060006](account-api-error-code.md#section1010060006-账号未登录) | 用户未登录华为账号。 |
| INVOICE\_TITLE\_EXISTS | [1010060007](account-api-error-code.md#section1010060007-发票抬头已存在) | 发票抬头信息已存在。 |
| UNSUPPORTED | [1010060008](account-api-error-code.md#section1010060008-华为账号不支持发票服务) | 已登录的华为账号不支持发票助手服务。 |

## InvoiceTitle

PhonePC/2in1Tablet

该类为发票助手服务响应的发票抬头数据对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HuaweiID.InvoiceAssistant

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 抬头类型，0-个人 1-企业。 |
| title | string | 否 | 否 | 抬头名称。 |
| taxNumber | string | 否 | 否 | 纳税人识别号。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| companyAddress | string | 否 | 否 | 公司地址。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| telephone | string | 否 | 否 | 公司电话。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| bankName | string | 否 | 否 | 公司银行名称。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| bankAccount | string | 否 | 否 | 公司银行账户。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |

## selectInvoiceTitle

PhonePC/2in1Tablet

selectInvoiceTitle(context: common.Context): Promise<InvoiceTitle>

调用该方法打开发票抬头选择页面，并返回用户选择的发票抬头。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HuaweiID.InvoiceAssistant

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[InvoiceTitle](account-api-invoiceassistant.md#invoicetitle)> | Promise对象，返回[InvoiceTitle](account-api-invoiceassistant.md#invoicetitle)对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1010060001](account-api-error-code.md#section1010060001-用户取消发票服务) | The operation was canceled by the user. |
| [1010060002](account-api-error-code.md#section1010060002-系统内部错误) | System internal error. |
| [1010060003](account-api-error-code.md#section1010060003-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1010060004](account-api-error-code.md#section1010060004-调用过于频繁) | Too frequent API calls. |
| [1010060005](account-api-error-code.md#section1010060005-网络连接错误) | Network connection error. |
| [1010060006](account-api-error-code.md#section1010060006-账号未登录) | The HUAWEI ID is not signed in. |
| [1010060007](account-api-error-code.md#section1010060007-发票抬头已存在) | Failed to create a invoice title because the title already exists. |
| [1010060008](account-api-error-code.md#section1010060008-华为账号不支持发票服务) | The invoice service does not support the logged HUAWEI ID. |

**示例：**

```
1. import { invoiceAssistant } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 执行请求
6. if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
7. try {
8. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
9. invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
10. .then((data: invoiceAssistant.InvoiceTitle) => {
11. hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
12. const type: string = data.type;
13. const title: string = data.title;
14. const taxNumber: string = data.taxNumber;
15. const companyAddress: string = data.companyAddress;
16. const telephone: string = data.telephone;
17. const bankName: string = data.bankName;
18. const bankAccount: string = data.bankAccount;

20. // 开发者处理type, title, taxNumber, companyAddress, telephone, bankName, bankAccount
21. // ...

23. })
24. .catch((error: BusinessError<Object>) => {
25. dealAllError(error);
26. });
27. } catch (error) {
28. dealAllError(error);
29. }
30. } else {
31. hilog.info(0x0000, 'testTag',
32. 'The current device does not support the invoking of the selectInvoiceTitle interface.');
33. }

35. // 错误处理
36. function dealAllError(error: BusinessError<Object>): void {
37. hilog.error(0x0000, 'testTag', `Failed to authorize. Code: ${error.code}, message: ${error.message}`);
38. }
```
