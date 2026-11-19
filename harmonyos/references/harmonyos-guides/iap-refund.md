---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:02+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:c0b1bc3f2d87893c6928bfef4591441f8fa6bcd32f52c1e846c8f64cdc175802
---

当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)上审核退款订单，实现用户的退款。

**说明** 

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/team-account-guide-0000002735960448.md#section1674403322314)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，点击“应用管理”，在左上角应用卡片处选择待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/6BifZJnaSVKygc1DpMBRCA/zh-cn_image_0000002791726370.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD43A8F12394844606CDA0C5315040957FC9D7516AF68495AE9BC50AF275AC4F)
2. 在“推广运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/x-VPScp-TvGmyuuv_JDcDg/zh-cn_image_0000002791566398.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=D214BF04C03A4EC767733B5A7B2886A6D7E1BCCCD2CFC5160432AB607F550DE0)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在“退款金额”下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/JbnYyNWsSBu8O9sINV4FPA/zh-cn_image_0000002820526351.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1EC0391DC7890703603BAA035B92516751376FDBE25DB5249082563650B075D)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/qseRlq_BQOCUilHhJwd_BQ/zh-cn_image_0000002820406351.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=6887800610D32C9DD3F46BB1BD7140B9DF6CC9F7FDC4941115BD65D8AC416161)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/kfXG-L8KR0S7ChK1ltd4pw/zh-cn_image_0000002791726372.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=D788BAC18151B6580A45256E782012BCDFC41EA35BCCD9AD19B43FFF14B2941D)

   **查询退款订单**：点击“已完成”页签，开发者可以按退款单的“申请时间”由新到旧或者由旧到新的排序，展示已处理的退款单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/GuUp5CZoQF2vKYgjFqsptA/zh-cn_image_0000002791566400.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDB6CEDCD6E7D3011DDAADE1EC4EA7B7FF9C30688C8357BDBD7137DC869FDE3C)

   退款订单状态如下：

   | **序号** | **退款订单状态** | **说明** |
   | --- | --- | --- |
   | 1 | 申请已拒绝 | 开发者驳回退款订单。 |
   | 2 | 申请已通过 | 开发者同意退款订单。 |
   | 3 | 退款成功 | 开发者同意退款，且华为操作退款成功。 |
   | 4 | 退款失败 | 开发者同意退款，且华为操作退款失败。 |
   | 5 | 超期未处理 | 开发者未按规定时间处理退款订单时，退款订单由华为运营进行审核。 |

## 用户申请退款

**说明** 

* 生态应用订单退款最低系统版本要求为6.16.10（检查版本可参考以下路径“系统设置-华为账号-付款与账单-更多设置-关于”）。
* 退款申请后到退款完成非实时，一般从发起申请退款到完成需要7个工作日左右。

若用户购买应用内数字商品后需要申请退款，可选择某笔订单后根据页面指引，提交退款信息。开发者审核完成后，用户可收到退款金额。

用户可按照以下步骤申请订单退款：

1. 在“手机设置 > 华为账号 > 付款与账单 > 购买记录”中点击待退款的订单，跳转至详情页面，点击“对订单有疑问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/VEAk3iKIQky910FXY0s6uw/zh-cn_image_0000002820526353.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=905B838CAF8B937F27E191AFAC2FD4F65D5E9174B02E783F95E9A3AF309047DB)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/djlb1Xs-QI-yptNfFMxf9g/zh-cn_image_0000002820406353.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2B3B41D2A340372377E7B4AC3EF8FBC76CF023ADDB278ADB2D3CAD910D96F06)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ekYS8qqUQ0Kaia9Tnm9C-A/zh-cn_image_0000002791726374.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D78A6926D957A2A851B482B1E8DA3AA983CB3DE860C8F66679488D498C599AE)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Hk7-Rik1S0CIoW4C3m18AA/zh-cn_image_0000002791566402.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=A54FDC0E3DCD69C3C2691C0F49946925BB292C949C823F0D0604E78ED8B5BCF1)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/FHnhmMD5Rsa-Gwng7D4HZA/zh-cn_image_0000002820526355.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E98718A32DCDEA3480DD5EC416BCD987E0573859765B337EDB9ABAED89FBE52)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/BmGbYAILTzurERHnwgj1uw/zh-cn_image_0000002820406355.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=C113C29532F954E26AD86732802F4ADD182DE04BC87DD4E676289ABCED4E9EFD)

## 应用内接入退款入口

**说明** 

* 仅支持非游戏类应用接入。
* 该退款入口仅支持应用本身所产生的订单的退款。

**拉起退款**

用户发起退款后，应用客户端向IAP Kit发送[createRefundRequest](../harmonyos-references/iap-iap.md#iapcreaterefundrequest)请求拉起退款页面，请求中需携带待退款的订单号（purchaseOrderId）。

**代码示例**

```typescript
import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import Logger from '../common/Logger';
// ...
  /**
   * 拉起退款界面
   */
  async createRefundRequest() {
    if (!this.purchaseOrderId) {
      Logger.error(TAG, `Failed to create refund request. Error params`);
      return;
    }
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    await iap.createRefundRequest(context, this.purchaseOrderId).then(() => {
      // 退款成功
      Logger.info(TAG, 'Succeeded in create refund request.');
      // ...
    }).catch((err: BusinessError) => {
      // 退款失败
      Logger.error(TAG, `Failed to create refund request. Code is ${err.code}, message is ${err.message}`);
      // ...
    });
  }
```
