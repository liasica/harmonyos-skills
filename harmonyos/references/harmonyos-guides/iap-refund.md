---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:20+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:74780fc05612366a53bb0384e1ee74841ca411efef36ce26450aa9a3725bf050
---

当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上审核退款订单，实现用户的退款。

**说明** 

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/agc-help-manageaccount-0000001099996700.md#section151241455193313)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“APP”。 在应用列表中点击待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/3St_453US3y3fl3yvqvSUQ/zh-cn_image_0000002717611810.png)
2. 在“运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZcRRKWBNRJClkXiVjeO5Qw/zh-cn_image_0000002747291763.png)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在 “退款金额“下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/qkScwYc_RPic29LVyScqqQ/zh-cn_image_0000002747211679.png)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/TYNUTF-KSfCRLDDTn1Bviw/zh-cn_image_0000002717771744.png)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/CPmFmm-hR1m5Z8iAFme_fA/zh-cn_image_0000002717611812.png)

   **查询退款订单**：点击“已完成”页签，开发者可以查看所有已处理的退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/-IcA6IzMQBeRY9Mmfu3oPQ/zh-cn_image_0000002747291765.png)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/SzqK1lsGSUaalCWmKt_M5A/zh-cn_image_0000002747211681.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/oi2JOUXgQj2zc97sXJEjHg/zh-cn_image_0000002717771746.png)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/H38WcEhwSQWuBgt3qdUOJg/zh-cn_image_0000002717611814.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/6oJmIXF0QrCM89ydXBASgg/zh-cn_image_0000002747291767.png)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/zCr4rbt1SQScvqUZttrK1A/zh-cn_image_0000002747211683.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/HXneP9iXRIK4b7vFMhCtog/zh-cn_image_0000002717771748.png)

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
