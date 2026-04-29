---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-invoicing
title: 开票
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 开票
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cfb8cc77c56438e7b975b6a0b6ca4069567d69b3cf7d583b48831eea64df5788
---

## 用户申请开发票

从6.1.0（23）开始，支持开发票功能。若用户购买应用内数字商品后需要申请开发票，可选择需要申请开票的订单后根据页面指引，提交开发票信息。

用户可按照以下步骤：

1. 选择“手机设置 > 华为账号 > 付款与账单 > 发票中心”，点击“开发票”，在需要开发票的订单后，点击“下一步”，进入“开发票”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/_tV1XumSRQahU0JreSOZoA/zh-cn_image_0000002558605788.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=939FC3B63B96905086A591ACF0D23BE68668551E4AD70A049827935418049E9B)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/JaaDy2QUThiNhUbYAZnNFA/zh-cn_image_0000002589325315.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=2B66CDEFB3F646198D0D5DFE609DDAC7A0874B137CCAB7BE7BF5494609687DA6)
2. 在“开发票”页面，选择发票类型、抬头类型，输入发票抬头、税号和电子邮箱，然后提交开发票申请，提交后等待即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/fZ4fUadrTI6PnZQsisitlA/zh-cn_image_0000002589245251.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=C6B005077EC27CC4C37BF857E09912F1D0A3C92E874B10B359465AC38F2F0ECE)

   用户提交开发票申请后，返回“发票中心”页面，在“我的发票”中查看所有订单的开发票状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/vTezagB-Sxeh1gwROh57Jg/zh-cn_image_0000002558765446.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=7A293C6D1BCD5119B2030B059FBF650E00D5FB0AED0A4CC9E03A5EE270647B04)

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
