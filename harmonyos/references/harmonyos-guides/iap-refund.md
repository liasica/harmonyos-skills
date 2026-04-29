---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a20eff0424aa0fd0f3af25a82759bec9b764c36b13ff91396ac31a1bac9e4c20
---

当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上审核退款订单，实现用户的退款。

说明

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/agc-help-manageaccount-0000001099996700.md#section151241455193313)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“APP”。 在应用列表中点击待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/C7sybL8cRrybwrWwOWArmw/zh-cn_image_0000002558605782.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=640944E887CDC1C44B71A857B28CB52EB97C7352DA16409AEE4EF6784948D5FA)
2. 在“运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/hRj-aih7T7ifsU70Ci2jzw/zh-cn_image_0000002589325309.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=D238390B7C937A22ED57469EA722B50836471D2136F03A4C0918C7F9564962B8)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在 “退款金额“下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/oMoGuvpLTICIRvP0PvIjbA/zh-cn_image_0000002589245245.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=4E116AA4047A2A5ED7EC28ABBCF73B89862470CAB9411A22046B27634D37477A)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/v1mvlnxISi2ocQLyrQ9ObQ/zh-cn_image_0000002558765440.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=9A230757592BB8CA89A7B00291B356E8CB41A01270781C8B7C5A9030FBD0DF55)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/rUpEZZ9xS1C9PLvA53JOJQ/zh-cn_image_0000002558605784.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=082C7D21C5BDE140004BFEC31025DB5B65BBE02B2A84756D61B78E9A93DA1251)

   **查询退款订单**：点击“已完成”页签，开发者可以查看所有已处理的退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/GGERJM5TQJCxmmxX4gy8yw/zh-cn_image_0000002589325311.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=CC155B00EB4960A6EA9AEBAF7F7E9AACBEFC9A999CFEB33C1045346DCCCE34AC)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/xhfVd1oHQ4q5P0yiEi6jQQ/zh-cn_image_0000002589245247.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=6F0A07C5D38C08A9590755D7F483E07F309E36FCF7EA616D4F69D20A87430EEC)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/AMCXuNfzSrWYI-bI4Gs3EQ/zh-cn_image_0000002558765442.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=1C856BA00382ACDF89E8FE4350538C5D321FFEF3245BE8D1E7781C7601EC1A75)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/KhzLbwCMQQmwpm0bKVAScg/zh-cn_image_0000002558605786.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=171B159BFC08EE0B8D8FC1C37D5E1619BE59F52455F72A47BB2699615783A5C3)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/1D6c-be3Rf662OeGWXJ4rQ/zh-cn_image_0000002589325313.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=86308F5FD9FA11A43B5C849316A2F0B6D616AB24351FEF5D9B468C5114FF517E)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/NKCx5K0ZRkOqnzB5lFZSMw/zh-cn_image_0000002589245249.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=275A687EA8B7B86218C58A189D4E31A206DAB52E3FCB8BA93D06F734751B558C)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/n_HcWJ_qSVaU1mCrqUQy3A/zh-cn_image_0000002558765444.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=41A23D767271469C81DCA4349D32B4281CC32EC455CDB163BAA1B69526417999)

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
