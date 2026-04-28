---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-promotion-select-coupon
title: 选券场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 运营工具 > 平台券 > 选券场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c133f32f6ca965d43e3463b5b2878c083921aac2ac90460a6b866225718a2e16
---

## 场景介绍

从6.1.0(23)版本开始，新增支持选券场景。

当用户在商家服务选好商品后进入订单结算页，可选券组件切换优惠券，让用户选择可用平台券进行下单。

如下图所示，首先商户应用会调用云侧接口选择1张10元优惠券，然后点击优惠券弹出选券组件，选择1张6元优惠券，最后商户应用将优惠券渲染成6元。

支持商户模型：直连商户、平台类商户、服务商

选券场景效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/f4AX1FFsRpOsF67NeBwarg/zh-cn_image_0000002552799450.png?HW-CC-KV=V1&HW-CC-Date=20260427T235012Z&HW-CC-Expire=86400&HW-CC-Sign=62FFB28A42B2888941A5BB67A458FBADF732F8A3298971176025504F86DAF049)

## 接入流程

| 步骤 | 说明 |
| --- | --- |
| 开发准备 | 根据[端侧应用配置](payment-config-app-identity-info.md)完成开发准备。 |
| 接入选券组件 | 根据选券场景[开发步骤](payment-promotion-select-coupon.md#开发步骤)完成接入。 |

## 业务流程

关于选券场景的业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Q9zY90PdScO355NygpAwfg/zh-cn_image_0000002583439145.png?HW-CC-KV=V1&HW-CC-Date=20260427T235012Z&HW-CC-Expire=86400&HW-CC-Sign=62CA1C057F2D5A52FF8D061BCA72F9B28C6D0B1A0CE523AB08CB964CE1EABF52)

1. 用户选好商品后进入商家服务结算页。
2. 商户客户端请求商户服务端查询用户可用券。
3. 商户服务端请求华为支付服务端[查询用户可用券](../harmonyos-references/payment-api-common-promotion-service-inquiry.md)。
4. 华为支付服务端返回用户可用券给商户服务端。
5. 商户服务端给商户客户端返回券信息。
6. 商户客户端展示优惠券列表中的第1张券。
7. 用户点击优惠券进行选券。
8. 商户客户端根据订单信息请求服务端，服务端参考[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)构造[OrderContext](../harmonyos-references/payment-promotionservice.md#ordercontext) 签名信息。
9. 商户服务端返回签名信息。
10. 客户端根据签名信息组装好拉起选券组件的请求体，调用Payment Kit客户端[startUserChooseCouponsPopup](../harmonyos-references/payment-promotionservice.md#startuserchoosecouponspopup)接口拉起选券组件。
11. Payment Kit客户端收到调用后，判断用户是否已签署过华为支付隐私协议，如果没签署则不走后续流程。
12. 向服务端查询用户可用券。
13. Payment Kit服务端返回用户可用券信息
14. Payment Kit客户端利用可用券信息展示出选券组件。
15. 用户选券并点击确认按钮。
16. Payment Kit客户端给商户客户端返回券信息。
17. 商户客户端请求商户服务服务端创建订单。
18. 商户服务端请求[直连商户预下单](../harmonyos-references/payment-prepay.md)或[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)接口，通过selectPromotionInfo参数传递平台券信息进行核销。

## 接口说明

选券场景需要拉起选券组件，涉及接口如下，更详细信息详见[API接口文档](../harmonyos-references/payment-promotionservice.md#startpromotionentrydialog)。

| 接口名 | 描述 |
| --- | --- |
| startUserChooseCouponsPopup(context: common.Context, orderContext: OrderContext): Promise<CouponDetail[]> | 拉起选券组件。 |

## 开发步骤

### 查询用户可用券（服务端开发）

在拉起选券组件前，商户根据[查询用户可用券](../harmonyos-references/payment-api-common-promotion-service-inquiry.md)接口查询用户可用券，如果用户无可用券可不拉起选券组件。业务接口请求示例代码可参考[业务接口请求](payment-server-connect.md#业务接口请求)。

### 拉起选券组件（端侧开发）

针对选券场景，商户服务需要先选券组件引导用户选券。示例代码如下：

```
1. import { promotionService } from "@kit.PaymentKit";

3. @Component
4. export struct StartUserChooseCouponsPopupDemo {
5. build() {
6. Column() {
7. Button('选券页面')
8. .type(ButtonType.Capsule)
9. .width('50%')
10. .margin(20)
11. .onClick(() => {
12. let req: promotionService.OrderContext = {
13. // 商户号
14. mercNo: '100000000000',
15. // 订单金额，单位为分
16. tradeOrderAmount: 15,
17. // 商品编码
18. goodsCodes: ['goodsCode0', 'goodsCode1'],
19. // 商户证书ID
20. authId: '123',
21. // 签名内容调云侧接口获取
22. sign: 'MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ=='
23. }
24. console.error(`req ${JSON.stringify(req)}`);
25. promotionService.startUserChooseCouponsPopup(this.getUIContext().getHostContext()!, req).then(res => {
26. console.error(`startUserChooseCouponsPopup res ${JSON.stringify(res)}.`);
27. }).catch((e: BusinessError) => {
28. console.error(`startUserSelectCouponsPopup error ${JSON.stringify(e)}`);
29. })
30. })
31. }
32. }
33. }
```

### 使用平台券（服务端开发）

商家可以在创建订单时，请求[直连商户预下单](../harmonyos-references/payment-prepay.md)或[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)接口，通过selectPromotionInfo参数传递平台券信息进行核销。
