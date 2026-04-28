---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ba3af2d0b5696064b0b044a472a1a450313edb0e62190f6e0122a74381aa67b1
---

当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上审核退款订单，实现用户的退款。

说明

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/agc-help-manageaccount-0000001099996700.md#section151241455193313)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“APP”。 在应用列表中点击待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/d0F1xB5BR_WGkpJCz8hemw/zh-cn_image_0000002583478939.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=3A74DC1C0789F586C0F745285B205F43B662154586CD84864A06E7B9EA4476C3)
2. 在“运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/a77-C3HWQgqi8pvy-4IeEw/zh-cn_image_0000002552799290.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=F3CBBC8EEAF80D7A430D0088E2B4CDE053F2257141662E9E7A9266F6BFEF76DC)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在 “退款金额“下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ALRuGqvUQMmUQXFaj0Y3uQ/zh-cn_image_0000002583438985.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=F0FA295B2A3758C12D53619C147221366EED6FC2EF819BD40E3A3AF7BBDF2FA9)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/GUvap6DmSU-hydGgNpoFpg/zh-cn_image_0000002552958940.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=EA9BFF8226E593A067D1DCFEF4EB566AF3B419FDCE3C5E2E202C2C0CB568EBD4)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/BfWHfDo5TxyEA6bAz10VyQ/zh-cn_image_0000002583478941.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=1A0AD34EBC992AC84FBD98548B62E5477E00DEF65E49A574B5424DD56C2F0F9F)

   **查询退款订单**：点击“已完成”页签，开发者可以查看所有已处理的退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_mxHxrc6SFiM-EfDb_hx6w/zh-cn_image_0000002552799292.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=8EC208449677A422DFC0AFD687F01CD3FC6BFF80893EEFA620CADDAA7CEEDCF6)

   退款订单状态如下：

   | **序号** | **退款订单状态** | **说明** |
   | --- | --- | --- |
   | 1 | 申请已拒绝 | 开发者驳回退款订单。 |
   | 2 | 申请已通过 | 开发者同意退款订单。 |
   | 3 | 退款成功 | 开发者同意退款，且华为操作退款成功。 |
   | 4 | 退款失败 | 开发者同意退款，且华为操作退款失败。 |
   | 5 | 超期未处理 | 开发者未按规定时间处理退款订单时，退款订单由华为运营进行审核。 |

## 用户申请退款

说明

* 生态应用订单退款最低系统版本要求为6.16.10（检查版本可参考以下路径“系统设置-华为账号-付款与账单-更多设置-关于”）。
* 退款申请后到退款完成非实时，一般从发起申请退款到完成需要7个工作日左右。

若用户购买应用内数字商品后需要申请退款，可选择某笔订单后根据页面指引，提交退款信息。开发者审核完成后，用户可收到退款金额。

用户可按照以下步骤申请订单退款：

1. 在“手机设置 > 华为账号 > 付款与账单 > 购买记录”中点击待退款的订单，跳转至详情页面，点击“对订单有疑问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/_F14yLegRbKfg6PdH3bOLw/zh-cn_image_0000002583438987.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=2FF20D57C5BEA2D895438DDF89C96532B14778AC21535B0A032E7D5474A8D3E1)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/QpwyjpTgSjOde8rGY7pKpA/zh-cn_image_0000002552958942.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=8E62B5119E10DA275D0E00D289D272FB0A2F3F9B8B234611AFAE4FC9817E3C7B)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/B2isRieDSbCe8OJi10zo9A/zh-cn_image_0000002583478943.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=5E179103265C75444F85E565E00FBFC1290512D599A04A215DB8E01D86DDC2A9)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/OrmC2GQ0REe5eBcDv6ub8g/zh-cn_image_0000002552799294.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=3218C41FCEE121AC4FC29824CF306EA1808EFC76F8C6A7A0D3CBB5BF99FC0BE5)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9j_6wrQ5Tlqc4UgAB_uFyA/zh-cn_image_0000002583438989.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=DAFA5727E75E0F11008B0A9C294E5CF09D834DF13D6F6846B09CB357FB125FFE)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/DyLmNrDOQlmDzjC9Ug6kgA/zh-cn_image_0000002552958944.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=AA41F5B15D35F21C0E2BE8B261B56BDD9DD48ADED1DA7F9C22B1F5932A68754D)

## 应用内接入退款入口

说明

* 仅支持非游戏类应用接入。
* 该退款入口仅支持应用本身所产生的订单的退款。

**拉起退款**

用户发起退款后，应用客户端向IAP Kit发送[createRefundRequest](../harmonyos-references/iap-iap.md#iapcreaterefundrequest)请求拉起退款页面，请求中需携带待退款的订单号（purchaseOrderId）。

**代码示例**

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {

9. /**
10. * 拉起退款界面
11. */
12. createRefundRequest(context: common.UIAbilityContext) {
13. // 调用iap.createRefundRequest拉起退款，传入context和purchaseOrderId
14. let purchaseOrderId = '';
15. iap.createRefundRequest(context, purchaseOrderId).then(() => {
16. // 退款成功
17. console.info('Succeeded in creating refund request.');
18. // ...
19. }).catch((err: BusinessError) => {
20. // 退款失败
21. console.error(`Failed to create refund request. Code is ${err.code}, message is ${err.message}`);
22. // ...
23. });
24. }

26. build() {}
27. }
```
