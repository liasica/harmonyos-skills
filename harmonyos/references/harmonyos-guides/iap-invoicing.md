---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-invoicing
title: 开票
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 开票
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a59ca4d76e707d02f3125b868f51211c17791d7a25c5a27c1f02a1f0f3c733e6
---

## 用户申请开发票

从6.1.0（23）开始，支持开发票功能。若用户购买应用内数字商品后需要申请开发票，可选择需要申请开票的订单后根据页面指引，提交开发票信息。

用户可按照以下步骤：

1. 选择“手机设置 > 华为账号 > 付款与账单 > 发票中心”，点击“开发票”，在需要开发票的订单后，点击“下一步”，进入“开发票”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/03462lBnRBK2pCcTv7LtUw/zh-cn_image_0000002583478945.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=7356DD23323A62CA3BB47ACCAEDAB21E8A16E36C1C344F6C42C450A2D641ABD9)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/9TTProaMTRqCUP4dsMyPbg/zh-cn_image_0000002552799296.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=902916E04B09667050A0040556FBAF6D056EA94897E01D894011BE35E1A3C6CB)
2. 在“开发票”页面，选择发票类型、抬头类型，输入发票抬头、税号和电子邮箱，然后提交开发票申请，提交后等待即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/DcW8IZY6Tlaz4JfpOzFEXA/zh-cn_image_0000002583438991.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=58EAAFBA28730B8FE0DA280CFF06940A4B5D57DCFF37AD6E048A8E1DB6CC4308)

   用户提交开发票申请后，返回“发票中心”页面，在“我的发票”中查看所有订单的开发票状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ONLPWt4IRJqxjF7jW16J2Q/zh-cn_image_0000002552958946.png?HW-CC-KV=V1&HW-CC-Date=20260427T234928Z&HW-CC-Expire=86400&HW-CC-Sign=624332E42D5699BF8B5EE6A8DD5768659CD83F9563EC32786A1E13B4A61015D9)

## 应用内接入开发票入口

**拉起开发票页面**

用户发起申请开发票后，应用客户端向IAP Kit发送[showManagedInvoices](../harmonyos-references/iap-iap.md#iapshowmanagedinvoices)请求拉起开发票页面，请求中需携带待开发票的订单号（purchaseOrderId）。

**代码示例**

```
1. import { iap } from '@kit.IAPKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct IapTest {
8. /**
9. * 拉起开发票界面
10. */
11. showManagedInvoices() {
12. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. // 调用iap.showManagedInvoices拉起开发票页面，传入context和purchaseOrderId
14. let purchaseOrderId = '';
15. iap.showManagedInvoices(context, purchaseOrderId).then(() => {
16. // 请求成功
17. console.info('Succeeded in showing invoice page.');
18. // ...
19. }).catch((err: BusinessError) => {
20. // 请求失败
21. console.error(`Failed to show invoice page. Code is ${err.code}, message is ${err.message}`);
22. // ...
23. });
24. }
25. build() {
26. }
27. }
```
