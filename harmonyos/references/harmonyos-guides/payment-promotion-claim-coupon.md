---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-promotion-claim-coupon
title: 领券场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 运营工具 > 平台券 > 领券场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:04ddfd768a7c7c0cb69a3a49c46cfd951d2f359ff8a400af990474cec77ba198
---

## 场景介绍

从6.1.0(23)版本开始，新增支持领券场景。

如图1所示，当存在领券活动并且用户可参与时，在应用底部展示活动“领取”按钮，同时也支持用户关闭领券入口。用户点击“领取”按钮后，展示图2中的领券组件。

如图2所示，在领券组件中，用户可点击“领取”按钮领券，领券成功时组件会将按钮刷成“去使用”。

如图3所示，用户点击“去使用”按钮后商户可跳转至商品选择页。

支持商户模型：直连商户、平台类商户、服务商

领券场景展示效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/uMfB3IipQs-ZtBCWZ0dEog/zh-cn_image_0000002736434273.png)

## 接入流程

| 步骤 | 说明 |
| --- | --- |
| 开发准备 | 根据[端侧应用配置](payment-config-app-identity-info.md)完成开发准备。 |
| 接入活动入口组件 | 根据领券场景[开发步骤](payment-promotion-claim-coupon.md#开发步骤)完成接入。 |

## 业务流程

关于领券场景的业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/lTRGmEcST96ew26U0dWxvg/zh-cn_image_0000002706835122.png)

1. 用户进入商户服务。
2. 商户客户端调用Payment Kit客户端的[startPromotionEntryDialog](../harmonyos-references/payment-promotionservice.md#startpromotionentrydialog)拉起活动入口组件。
3. Payment Kit客户端判断是否已签署华为支付隐私协议，如果没签署过，后续流程将会结束，需要用户自行签署华为支付隐私协议。
4. Payment Kit客户端向服务端查询活动信息。
5. Payment Kit服务端根据用户信息查询可参与的活动并返回活动信息给Payment Kit客户端。
6. Payment Kit客户端根据活动信息展示活动入口组件。
7. 用户点击活动入口组件中的“领取”按钮。
8. Payment Kit客户端向服务端查询营销信息。
9. Payment Kit服务端返回营销信息。
10. Payment Kit客户端根据营销信息展示领券组件。
11. 用户点击领券组件中的“领取”按钮。
12. Payment Kit客户端调服务端接口给用户发券。
13. Payment Kit服务端给客户端返回发券结果。
14. Payment Kit客户端根据发券结果刷新领券组件。
15. 用户在领券组件上点击“去使用”按钮。
16. 返回商品选择页。

## 接口说明

领券场景需要拉起活动入口组件，涉及接口如下，更详细信息详见[API接口文档](../harmonyos-references/payment-promotionservice.md#startpromotionentrydialog)。

| 接口名 | 描述 |
| --- | --- |
| startPromotionEntryDialog(mercNo: string, offset?: number): Promise<UserAction>; | 拉起活动入口组件。 |

## 开发步骤

### 拉起活动入口组件（端侧开发）

针对领券场景，商户服务需要先拉起活动入口组件引导用户领券。示例代码如下：

```typescript
import { promotionService } from '@kit.PaymentKit';

@Component
struct StartPromotionEntryDialogDemo {
  controller: promotionService.PromotionComponentController =
    new promotionService.PromotionComponentController(this.getUIContext());
  build() {
    Column() {
      Button('拉起活动入口组件')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(async () => {
          try {
            // 拉起活动入口组件
            let userAction = await this.controller.startPromotionEntryDialog('100000000000', 10);
            // 点击关闭、去使用后会分别返回doNothing、useButtonClicked为true
            console.info(`userAction ${JSON.stringify(userAction)}`);
          } catch (e) {
            console.error(`startUserSelectCouponsPopup error ${JSON.stringify(e)}`);
          }
        })
    }
  }
}
```
