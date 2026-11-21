---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:29+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:ebb8a46299cd1e624df6ba152dd638a18d1e553c29938416867435fdaaf92d67
---

当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)上审核退款订单，实现用户的退款。

**说明** 

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/team-account-guide-0000002735960448.md#section1674403322314)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，点击“应用管理”，在左上角应用卡片处选择待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/8w8G-tyTT7Kd1O8rZhdGsg/zh-cn_image_0000002821837957.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=30642AA47C26B777A9808FE97F0E887555A743DB02B4BB6159D74580D826A1B3)
2. 在“推广运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/8tZZeW51SFitJyUFDoGZcg/zh-cn_image_0000002821757959.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=A685F3F06FA5D475C5DB66CC91E8E0FC2E25961DCF115AB99B959DDAE192E3F4)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在“退款金额”下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/elfTNIhZSWylxLbU_fETqg/zh-cn_image_0000002793038022.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C67F8F8486CB4BC3494941942B6A52E4E885C64092A214FE4ED8DA4DAE546A0)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/WoUKaoFHSniVNzNizhAlsw/zh-cn_image_0000002792878052.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=1299EA3145F9097A607D93D7289161FBD3262B8F45A45A76E7022E83D8EB1FB0)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/yfjx4togQsCOzNdB11qZvg/zh-cn_image_0000002821837959.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D6DE91572CC03364B3DEDA14EF246DA42F98826B473A5C3047C2B0CDCE851F2)

   **查询退款订单**：点击“已完成”页签，开发者可以按退款单的“申请时间”由新到旧或者由旧到新的排序，展示已处理的退款单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/MkTiiTrpSFexVIm_0_0jIQ/zh-cn_image_0000002821757961.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F9A9A43D897C8F8C5429E161EC1F71E86C3EC53814C54ABFA4E7E118793A866)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/qrau_nbCSyKCN4nwEi15rQ/zh-cn_image_0000002793038024.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5E866E9D36D6A3DFCBA7DC41A6DD29FD04E7764FC43D54E0CDD210323A89339)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/2Ja8JNKYR9SJsQyznMblhA/zh-cn_image_0000002792878054.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D92914B0EEA577F370E0E71D7B6ED9CB4A7CC573C11087CB1326BC05E0F2BD1)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Tf1LQmCnS5208K9X7KXgmA/zh-cn_image_0000002821837961.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9B2105C8BA9BF6D416F88C71380FBBDC2A9A7A7A15DF679EE8C284D48E8613E)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/gqz6hPPaSOqillCOOET2mw/zh-cn_image_0000002821757963.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=A89D37EC0C3A32677E8CC954B24119E7A68220AF4554F772DF2B568F15C73F54)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/8EtuKRNaTFOL56xU_GJgHg/zh-cn_image_0000002793038026.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=D53F4219C76F17B32E4A59667C0AC475C83F8CFF05566A7BBE47E1D3F9520E02)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/X8EWaJb0Swe0zOzpKccttw/zh-cn_image_0000002792878056.png?HW-CC-KV=V1&HW-CC-Date=20261121T011228Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5786E3093D3A74F9813BB887AF4FA301C3E37979BA315A63844EC2D5930ADB5)

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
