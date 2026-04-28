---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transport-delete
title: 交通卡删卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 接入交通卡 > 交通卡删卡
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:36901b1533002f4afc945fc2adea1aed118d6be6a868224a7b2f5d2136286d35
---

交通卡的删卡过程分为：卡片展示、生成删卡业务订单和发起删卡三个步骤，整体流程如下图，相关接口定义请参照[钱包服务API](../harmonyos-references/wallet-wallettransitcard.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/oTLmI0NvTj-_hMeO0PnQlA/zh-cn_image_0000002552959206.png?HW-CC-KV=V1&HW-CC-Date=20260427T235109Z&HW-CC-Expire=86400&HW-CC-Sign=96BCB32F0BF57390DA8F711D7697432A0F4E22E7B921A951CE90D4AF516FA6BD)

* 开发者的app启动后，可调用[getCardMetadataInDevice](../harmonyos-references/wallet-wallettransitcard.md#getcardmetadataindevice)接口获取指定设备上开发者的app可以访问的交通卡的信息以数组的方式返回。如返回的数组为空，则表示开发者的app在该设备上没有可访问的交通卡，无需显示卡片开通入口；如返回数组不为空，则按具体的交通卡信息做展示。
* 如果交通卡信息中包括卡号、余额信息，则表明该卡片在设备上已开通，显示卡片信息即可；否则可显示卡片的开通入口。
* 用户选择了要删除的交通卡后，开发者的app需向开发者的后台服务器发起删卡业务订单的生成请求。
* 开发者的app可调用[deleteTransitCard](../harmonyos-references/wallet-wallettransitcard.md#deletetransitcard)接口发起删卡处理过程。如删卡过程出现异常导致失败，开发者的app会收到相应的错误码，可参考[ArkTS API错误码](../harmonyos-references/wallet-error-code.md)。

## 开发步骤

1. 获取设备上已开通的交通卡列表。

   初始化TransitCardClient时，构造方法的第二个入参callerId是接口调用方ID。开发者可以联系钱包运营申请交通卡服务时获取。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletTransitCard } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

   10. async getCardMetadataInDevice() {
   11. this.transitCardClient.getCardMetadataInDevice(walletTransitCard.DeviceType.DEVICE_PHONE).then((result) => {
   12. console.info(`Succeeded in getting cardMetadataInDevice`);
   13. }).catch((err: BusinessError) => {
   14. console.error(`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}`);
   15. })
   16. }

   18. build() {
   19. // your application UI
   20. }
   21. }
   ```
2. 删除交通卡。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletTransitCard } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

   10. async deleteTransitCard() {
   11. // number of the enabled traffic card returned by the step 1
   12. const logicalCardNumber = 'logicalCardNumber';
   13. // the specifiedDeviceId returned by the step 1
   14. const specifiedDeviceId = 'specifiedDeviceId';
   15. // order ID generated after payment in a developer's app, which is implemented by the developer
   16. const serverOrderId = 'serverOrderId';
   17. this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
   18. console.info(`Succeeded in deleting TransitCard`);
   19. }).catch((err: BusinessError) => {
   20. console.error(`Failed to delete TransitCard, code:${err.code}, message:${err.message}`);
   21. })
   22. }

   24. build() {
   25. // your application UI
   26. }
   27. }
   ```
