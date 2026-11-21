---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-invoicing
title: 开票
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 开票
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:28+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:8fd3ddae83d47b6ddab5d97c4c60abf23f7b8d5145e0d6d33df6a1af91890cce
---

## 用户申请开发票

从6.1.0(23)版本开始，支持开发票功能。若用户购买应用内数字商品后需要申请开发票，可选择需要申请开票的订单后根据页面指引，提交开发票信息。

用户可按照以下步骤：

1. 选择“手机设置 > 华为账号 > 付款与账单 > 发票中心”，点击“开发票”，在需要开发票的订单后，点击“下一步”，进入“开发票”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/mKhFMbtMRwm8as3U8Vr0Eg/zh-cn_image_0000002821837963.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C349C051B072150DBDE9BDE1A5F682906E402B9E611B493D56A910B2782D6B6)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/nWOj_pwMTEu9gX4_QsWrUQ/zh-cn_image_0000002821757965.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=05A98D27F1E945D0BD0C01DA4173E9046F0F754B00146851F292749B58E65C6E)
2. 在“开发票”页面，选择发票类型、抬头类型，输入发票抬头、税号和电子邮箱，然后提交开发票申请，提交后等待即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/B2tPvMoQRxGbGjW8W44t8w/zh-cn_image_0000002793038028.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=432E2B1F0FF7A6FE022FDE217F7700BDFF3C4E20814EA8CAD4B06C438635449D)

   用户提交开发票申请后，返回“发票中心”页面，在“我的发票”中查看所有订单的开发票状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/vnngS-QvQOixHVjg1MjsYA/zh-cn_image_0000002792878058.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D96912D7E3877B20F579247A952B30C76E78735FD701A44DCC1DD03620B66FB)

## 应用内接入开发票入口

**拉起开发票页面**

用户发起申请开发票后，应用客户端向IAP Kit发送[showManagedInvoices](../harmonyos-references/iap-iap.md#iapshowmanagedinvoices)请求拉起开发票页面，请求中需携带待开发票的订单号（purchaseOrderId）。

**代码示例**

```typescript
import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import Logger from '../common/Logger';
// ...
  /**
   * 拉起开发票界面
   */
  async showManagedInvoices() {
    if (!this.purchaseOrderId) {
      Logger.error(TAG, `Failed to show invoice page. Error params`);
      return;
    }
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    await iap.showManagedInvoices(context, this.purchaseOrderId).then(() => {
      // 请求成功
      Logger.info(TAG, 'Succeeded in showing invoice page.');
      // ...
    }).catch((err: BusinessError) => {
      // 请求失败
      Logger.error(TAG, `Failed to show invoice page. Code is ${err.code}, message is ${err.message}`);
      // ...
    });
  }
```
