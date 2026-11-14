---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:22+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:dd5edc81ae3703b345c755c3c0cc37717bcef7bf23c6e2fd3bd279094e4b4d64
---

当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)上审核退款订单，实现用户的退款。

**说明** 

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/team-account-guide-0000002735960448.md#section1674403322314)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，点击“应用管理”，在左上角应用卡片处选择待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/KfpYo1HdTZG4smnc99l1rQ/zh-cn_image_0000002817427431.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=95D3814C95262E1A6B5D7C202B251ED2BA196F139FF3B3C99CB498F6BE4AAD66)
2. 在“推广运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/aUO9DOXTRLqqbLq-PilGiQ/zh-cn_image_0000002788468012.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=C44409744E5BA4F409032D9F08A43A928001174608092B11835BC7D0489DEB02)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在“退款金额”下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uANo1JLNQwKu2corxL3Cmw/zh-cn_image_0000002817507501.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDFA4B5EAC62BE3C8A583DFD5E0BACFB5AA9AAC49FA6C5BD8BB035334E6A1B6D)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eFXokmsiQrW7yPXjugqX2A/zh-cn_image_0000002788308070.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EA22610F457FCCEFCF54F28F90A0BB2801D5CFC72DF1B33D434E31F83A21177)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/3U6kIc5pTlS4q74DQG1UWw/zh-cn_image_0000002817427433.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=016802CCF03E13EB69C7C9C66B7BA9E11C869A91ADEAE4346C0DF6646E057650)

   **查询退款订单**：点击“已完成”页签，开发者可以按退款单的“申请时间”由新到旧或者由旧到新的排序，展示已处理的退款单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ZOwt1WBnS0SiPdWjlV7cOg/zh-cn_image_0000002788468014.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBE8C5F985A3C1CF8A1AF7C03C9845B5E650B78B76E9AF131055F1BB1B0A537A)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/z3NSauouSKeaaEpk_hI99w/zh-cn_image_0000002817507503.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5FF1F04B2800B49327A78019A93AB1198F8F8F428A89BE5384D140C5CEDBFBF)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/GNqTWA9nTXq7ERTrSczvhQ/zh-cn_image_0000002788308072.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2C335D935A372F73C9298595C2A432D17AE9A9CBE8433F67536C6F12FD19166)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/CtVu0KlYRjKIy6DFZQf54Q/zh-cn_image_0000002817427435.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=56CBE822E747AFC35FF238A44FC65F977814296654D0EA34E43A12BE9E0B5846)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/xVSl5ADgTsa8Z22h5Q9eQQ/zh-cn_image_0000002788468016.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E339CA108FE2E783FB05412272F485DAB3EA0B32C500B4B8707B438BB89718D)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/2BNfQTcqSi2uM2Px0hkVFA/zh-cn_image_0000002817507505.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2D7325BEFC3A6DD071BDB00A6A804B18D2CCEF47B02BEF1CC57FFD2CFC5964F)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/D9m2qMDfQLGKa3ODNcXSdQ/zh-cn_image_0000002788308074.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B7EA9931DC6684C289040323019A660AAF23B3058D60A6198D0CDB7C7636208)

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
