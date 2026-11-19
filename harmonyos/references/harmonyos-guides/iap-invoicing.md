---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-invoicing
title: 开票
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 开票
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:02+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:2f7661da716db08e61b5dd1e58bb27f0f3c6f8bbbbbb506961ba5d672c3c5788
---

## 用户申请开发票

从6.1.0(23)版本开始，支持开发票功能。若用户购买应用内数字商品后需要申请开发票，可选择需要申请开票的订单后根据页面指引，提交开发票信息。

用户可按照以下步骤：

1. 选择“手机设置 > 华为账号 > 付款与账单 > 发票中心”，点击“开发票”，在需要开发票的订单后，点击“下一步”，进入“开发票”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/CLUcJle4R0ev9CwwADs8AA/zh-cn_image_0000002791726376.png?HW-CC-KV=V1&HW-CC-Date=20261119T014808Z&HW-CC-Expire=31536000000&HW-CC-Sign=E52C0A0AE6C80D8B0984600F3D3895FD87B9671B573598C2F26F89AE8826A400)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nTOx08JeR1OIefLpTXXZUg/zh-cn_image_0000002791566404.png?HW-CC-KV=V1&HW-CC-Date=20261119T014808Z&HW-CC-Expire=31536000000&HW-CC-Sign=16584C43F2609D759F8778417C39217DFFE24886F25F385C9CE21ED7B78EDD09)
2. 在“开发票”页面，选择发票类型、抬头类型，输入发票抬头、税号和电子邮箱，然后提交开发票申请，提交后等待即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/W1jyzs0-QzesVJmNA-y_dw/zh-cn_image_0000002820526357.png?HW-CC-KV=V1&HW-CC-Date=20261119T014808Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF03423089DD95B86ADD05E44348079D921A7BE1DFAC6FCA0F193BF6CAFD550F)

   用户提交开发票申请后，返回“发票中心”页面，在“我的发票”中查看所有订单的开发票状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/ldx3Mv_dSlSHTpMSgyx2og/zh-cn_image_0000002820406357.png?HW-CC-KV=V1&HW-CC-Date=20261119T014808Z&HW-CC-Expire=31536000000&HW-CC-Sign=906B0B209FB2073E6D95CAE3E5FAD3CA46927F6655C82D04A37DE527AA3FD5F6)

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
