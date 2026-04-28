---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-partner-bindcard
title: 引导用户绑卡场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 引导用户绑卡场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75c9feaaa3552e3a9b9f36612a3380eb7ba110aec252fd55bc31916f87a6a8f7
---

## 场景介绍

从5.0.5(17)版本开始，新增支持引导用户绑卡场景。

支持拉起绑卡页面，结合商户营销活动，有效引导用户完成绑卡操作。例如商户针对银行卡开展某营销活动，需要引导用户拉起绑卡页面完成银行卡绑定。

支持商户模型：直连商户、平台类商户、服务商

引导用户绑卡页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/wn_9DtiORFq0iG3TZTeemA/zh-cn_image_0000002583479093.png?HW-CC-KV=V1&HW-CC-Date=20260427T235011Z&HW-CC-Expire=86400&HW-CC-Sign=3AF65239E98250FDFC6BBDC507B0CB16FCEDBBDC24C4F4FADAEF35116AB574F5)

## 提供绑卡跳转应用信息

开发者需与华为支付业务侧沟通（合作咨询可[点击此处](payment-service-support.md)）后提供以下应用信息：

| 应用信息 | 是否必选 | 说明 |
| --- | --- | --- |
| AppID | 是 | 应用的AppID（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“开发与服务”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“APP ID”的值）。 |

## 业务流程

开发者接入引导用户绑卡，具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/w-zJLq8rSx21HZ13pz1MmA/zh-cn_image_0000002552799444.png?HW-CC-KV=V1&HW-CC-Date=20260427T235011Z&HW-CC-Expire=86400&HW-CC-Sign=98E6D3979EF3F0FB01B242CBD0E0D79AA6BC8619E5AB7961740691E090E32367)

**场景1：用户取消绑卡**

1. 商户客户端调用[requestBindCard](../harmonyos-references/payment-paymentservice.md#paymentservicerequestbindcard)接口拉起用户绑卡页面。
2. Payment Kit客户端展示绑卡页面，商户客户端可根据用户不同处理场景完成后续流程。
3. 用户返回或取消绑卡。
4. Payment Kit客户端返回商户客户端并将绑卡结果一并返回，商户客户端根据绑卡结果完成后续业务处理。

**场景2：用户完成绑卡**

1. 商户客户端调用[requestBindCard](../harmonyos-references/payment-paymentservice.md#paymentservicerequestbindcard)接口拉起用户绑卡页面。
2. Payment Kit客户端展示绑卡页面，商户客户端可根据用户不同处理场景完成后续流程。
3. 用户通过绑卡页面完成绑卡操作，Payment Kit客户端会请求Payment Kit服务端处理绑卡。
4. Payment Kit服务端处理绑卡。
5. Payment Kit服务端将绑卡结果返回给Payment Kit客户端。
6. Payment Kit客户端展示绑卡结果页面。
7. 用户关闭绑卡页后，Payment Kit客户端返回商户客户端并将绑卡结果一并返回。
8. 商户客户端根据绑卡结果完成后续业务处理。

## 接口说明

拉起用户绑卡页面接口。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md#paymentservicerequestbindcard)。

| 接口名 | 描述 |
| --- | --- |
| requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult> | 拉起用户绑卡页面。 |

## 开发步骤

### 拉起绑卡页面（端侧开发）

商户客户端调用[requestBindCard](../harmonyos-references/payment-paymentservice.md#paymentservicerequestbindcard)接口拉起用户绑卡页面。

当接口通过.then()方法返回结果，则表示接口请求成功，通过.catch()方法返回异常表示请求失败。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/payment-error-code.md)。

示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestBindCardPromise() {
10. paymentService.requestBindCard(this.context)
11. .then((bindCardResult: paymentService.BindCardResult) => {
12. // succeeded in bind card
13. console.info(`succeeded in binding card. result: ${bindCardResult}`);
14. })
15. .catch((error: BusinessError) => {
16. // failed to bind card
17. console.error(`failed to binding card, error.code: ${error.code}, error.message: ${error.message}`);
18. });
19. }

21. build() {
22. Column() {
23. Button('requestBindCardPromise')
24. .type(ButtonType.Capsule)
25. .width('50%')
26. .margin(20)
27. .onClick(() => {
28. this.requestBindCardPromise();
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```
