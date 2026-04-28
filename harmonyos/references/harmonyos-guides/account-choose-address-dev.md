---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-choose-address-dev
title: 获取收货地址
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取收货地址
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f3d341f6ae4bba069177b40ffadb52f28f88f0ed9135fafb605e5d194e6ce250
---

## 场景介绍

当应用需要获取用户收货地址时，可使用Account Kit提供的获取收货地址的能力，引导用户添加或选择已有的收货地址，并最终获取用户的收货地址。以下对Account Kit提供的获取收货地址能力进行介绍，获取收货地址功能还可使用场景化控件[选择收货地址Button](scenario-fusion-button-ship-to.md)进行实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/D8uxBfP6Ssq1tNg3dztNbA/zh-cn_image_0000002583438801.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=B7182B26C16BCB30BEEB92E9E72B39BFD7E899E170414E6B0C57C862B33DA02A "点击放大")

## 约束与限制

1. 收货地址中的手机号信息仅支持输入中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）手机号、地址信息只支持填写中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
2. Wearable、TV设备暂不支持使用获取收货地址功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/JAYhjZ3pS1-_7UtRnJhQYQ/zh-cn_image_0000002552958756.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=D80FEDE15A78046F31E89149326A4CC940D14D77A0AACAE32061BDBB48A82345)

流程说明：

1. 用户需要使用收货地址时，应用程序调用选择收货地址API，打开华为账号收货地址管理页面。
2. 用户可以在收货地址管理页面添加新的收货地址或者选择已有收货地址，点击确认后，选择的收货地址将返回给应用。

## 接口说明

获取收货地址关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-choose-address.md)。

| 接口名 | 描述 |
| --- | --- |
| [chooseAddress](../harmonyos-references/account-choose-address.md#chooseaddress)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)): Promise<[AddressInfo](../harmonyos-references/account-choose-address.md#addressinfo)> | 拉起收货地址管理页面并返回用户所选择的收货地址。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

在进行代码开发前，请先确认以下准备工作是否完成：

1、是否完成[申请账号权限](account-config-permissions.md)，未申请通过调用获取收货地址API，将返回[1008100005 应用未申请对应permissions权限](../harmonyos-references/account-api-error-code.md#section1008100005-应用未申请对应permissions权限)错误码，无法获取收货地址。

说明

如果在权限申请前已完成“配置签名和指纹”，则需要重新[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)，并重新[手动配置签名信息](ide-signing.md#section297715173233)。

2、是否完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)，未配置调用获取收货地址API，将返回 [1008100004 应用指纹证书校验失败](../harmonyos-references/account-api-error-code.md#section1008100004-应用指纹证书校验失败)错误码，无法获取收货地址。

## 开发步骤

1. 导入[shippingAddress](../harmonyos-references/account-choose-address.md)模块及相关公共模块。

   ```
   1. import { shippingAddress } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[chooseAddress](../harmonyos-references/account-choose-address.md#chooseaddress)方法打开收货地址管理页面，引导用户添加或选择收货地址后，应用即可获取用户收货地址。

   ```
   1. // 执行请求
   2. try {
   3. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   4. shippingAddress.chooseAddress(this.getUIContext().getHostContext()).then((data: shippingAddress.AddressInfo) => {
   5. hilog.info(0x0000, 'testTag', 'Succeeded in choosing address.');
   6. const userName: string = data.userName;
   7. const mobileNumber: string = data.mobileNumber;
   8. const countryCode: string = data.countryCode;
   9. const provinceName: string = data.provinceName;
   10. const cityName: string = data.cityName;
   11. const districtName: string = data.districtName;
   12. const streetName: string = data.streetName;
   13. const detailedAddress: string = data.detailedAddress;
   14. // 开发者处理获取的收货地址信息
   15. }).catch((error: BusinessError) => {
   16. dealAllError(error);
   17. })
   18. } catch (error) {
   19. dealAllError(error);
   20. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError): void {
   3. hilog.error(0x0000, 'testTag', `Failed to chooseAddress. Code: ${error.code}, message: ${error.message}`);
   4. }
   ```
