---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-choose-address
title: shippingAddress (华为账号收货地址管理服务)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > shippingAddress (华为账号收货地址管理服务)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:834a45238dc76206f689c4b1af8a8faf81b00e7fb13353d3f849f9519a298bc9
---

本模块提供Account Kit的收货地址管理能力。应用可通过该能力获取到用户华为账号收货地址信息，包括详细地址、手机号等。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { shippingAddress } from '@kit.AccountKit';
```

## ShippingAddressErrorCode

PhonePC/2in1Tablet

该枚举定义了Account Kit收货地址管理服务错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | [1008100001](account-api-error-code.md#section1008100001-内部错误) | 内部错误。 |
| NETWORK\_ERROR | [1008100002](account-api-error-code.md#section1008100002-网络不可用) | 网络不可用。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1008100003](account-api-error-code.md#section1008100003-账号未登录) | 用户未登录华为账号。 |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1008100004](account-api-error-code.md#section1008100004-应用指纹证书校验失败) | 应用指纹证书校验失败。 |
| PERMISSION\_CHECK\_ERROR | [1008100005](account-api-error-code.md#section1008100005-应用未申请对应permissions权限) | 应用未申请对应permissions权限。 |
| USER\_CANCELED | [1008100006](account-api-error-code.md#section1008100006-用户未完成操作就退出了收货地址管理服务) | 用户未完成操作就退出了收货地址管理服务。 |
| UNSUPPORTED | [1008100007](account-api-error-code.md#section1008100007-已登录的华为账号不支持收货地址管理服务) | 已登录的华为账号不支持收货地址管理服务。 |

## AddressInfo

PhonePC/2in1Tablet

该类为收货地址管理服务响应的收货地址数据对象。应用可根据实际场景获取相关收货地址信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| userName | string | 是 | 否 | 用户名。长度限制2-20。 |
| mobileNumber | string | 是 | 否 | 手机号码。长度限制2-20。  **说明：**  当前仅支持输入中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）手机号。收货地址的明文手机号支持183\*\*\*\*\*\*58、+86183\*\*\*\*\*\*58、0086183\*\*\*\*\*\*58共3种格式。接口返回的手机号格式和用户输入的手机号格式保持一致。 |
| telNumber | string | 是 | 是 | 座机号码。长度限制1-256。用户未设置默认不返回。 |
| zipCode | string | 是 | 是 | 邮政编码。长度限制1-256。用户未设置默认不返回。 |
| countryCode | string | 是 | 否 | 国家码。长度限制1-256。 |
| provinceName | string | 是 | 否 | 省份名称。长度限制1-50。 |
| cityName | string | 是 | 否 | 城市名称。长度限制1-50。 |
| districtName | string | 是 | 否 | 地区名称。长度限制1-50。  **说明：** 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| streetName | string | 是 | 否 | 街道名称。长度限制1-50。 |
| detailedAddress | string | 是 | 否 | 详细地址。长度限制1-50。 |

## chooseAddress

PhonePC/2in1Tablet

chooseAddress(context: common.Context): Promise<AddressInfo>

调用该方法打开收货地址管理页面，使用Promise异步回调用户选择的收货地址。用于应用向Account Kit获取用户绑定的华为账号收货地址。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AddressInfo](account-choose-address.md#addressinfo)> | Promise对象，返回[AddressInfo](account-choose-address.md#addressinfo)对象可以获取收货地址的详细信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1008100001](account-api-error-code.md#section1008100001-内部错误) | Internal error. |
| [1008100002](account-api-error-code.md#section1008100002-网络不可用) | The network is unavailable. |
| [1008100003](account-api-error-code.md#section1008100003-账号未登录) | The user has not signed in with HUAWEI ID. |
| [1008100004](account-api-error-code.md#section1008100004-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1008100005](account-api-error-code.md#section1008100005-应用未申请对应permissions权限) | The app does not have the required permissions. |
| [1008100006](account-api-error-code.md#section1008100006-用户未完成操作就退出了收货地址管理服务) | The user quits the shipping address management service without finishing. |
| [1008100007](account-api-error-code.md#section1008100007-已登录的华为账号不支持收货地址管理服务) | The shipping address management service does not support the HUAWEI ID that is already signed in. |

**示例：**

```
1. import { shippingAddress } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 执行请求
6. try {
7. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
8. shippingAddress.chooseAddress(this.getUIContext().getHostContext()).then((data: shippingAddress.AddressInfo) => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in choosing address');
10. const userName: string = data.userName;
11. const mobileNumber: string = data.mobileNumber;
12. const countryCode: string = data.countryCode;
13. const provinceName: string = data.provinceName;
14. const cityName: string = data.cityName;
15. const districtName: string = data.districtName;
16. const streetName: string = data.streetName;
17. const detailedAddress: string = data.detailedAddress;
18. // 开发者处理获取的收货地址信息
19. }).catch((error: BusinessError) => {
20. dealAllError(error);
21. });
22. } catch (error) {
23. dealAllError(error);
24. }

26. // 错误处理
27. function dealAllError(error: BusinessError): void {
28. hilog.error(0x0000, 'testTag', `Failed to chooseAddress. Code: ${error.code}, message: ${error.message}`);
29. // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
30. if (error.code === shippingAddress.ShippingAddressErrorCode.ACCOUNT_NOT_LOGGED_IN) {
31. // 用户未登录华为账号，请登录华为账号并重试
32. } else if (error.code === shippingAddress.ShippingAddressErrorCode.NETWORK_ERROR) {
33. // 网络异常，请检查当前网络状态并重试
34. } else if (error.code === shippingAddress.ShippingAddressErrorCode.USER_CANCELED) {
35. // 用户取消选择收货地址
36. } else {
37. // 选择收货地址失败，请稍后重试
38. }
39. }
```
