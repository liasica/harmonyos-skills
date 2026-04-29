---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transport-recharge
title: 交通卡充值
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 接入交通卡 > 交通卡充值
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc289f62ed1a8c20f47cd939ea05775609ebed838472cea5dbbaf256a8707326
---

交通卡的充值过程分为：卡片展示、生成并支付充值订单和发起充值三个步骤，整体流程如下图，相关接口定义请参照[钱包服务API](../harmonyos-references/wallet-wallettransitcard.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/XczEcfGDQSmqh_6APi0nBw/zh-cn_image_0000002558606050.png?HW-CC-KV=V1&HW-CC-Date=20260429T054045Z&HW-CC-Expire=86400&HW-CC-Sign=3E00DA97C3E9E08BDC37DB3C730C36947A677C7CD5C2A5712969C969A9C9C9A2)

* 开发者的app启动后，可调用[getCardMetadataInDevice](../harmonyos-references/wallet-wallettransitcard.md#getcardmetadataindevice)接口获取指定设备上开发者的app可以访问的交通卡的信息以数组的方式返回。如返回的数组为空，则表示开发者的app在该设备上没有可访问的交通卡，无需显示卡片开通入口；如返回数组不为空，则按具体的交通卡信息做展示。如果交通卡信息中包括卡号、余额信息，则表明该卡片在设备上已开通，显示卡片信息即可；否则可显示卡片的开通入口。
* 用户选择了给指定的交通卡充值时，开发者的app需向开发者的后台服务器发起充值订单的生成请求，并让用户完成支付。
* 开发者的app在查询到订单已支付完成后，可调用[rechargeTransitCard](../harmonyos-references/wallet-wallettransitcard.md#rechargetransitcard)接口发起将订单金额充值到卡内的处理过程。如果充值正常结束，开发者的app会收到充值成功的返回值并携带了新的余额；如果充值过程出现失败，在钱包app自行发起重试后仍然失败的情况下，钱包会发起订单退款的请求。在SP TSM或开发者的后台服务器确认订单状态是可退款的情况下，需调用对应支付渠道的订单撤销接口，将订单金额原路退回，这种情况下开发者的app会收到充值失败的错误码，可参考[ArkTS API错误码](../harmonyos-references/wallet-error-code.md)。

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
2. 交通卡充值。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletTransitCard } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

   10. async rechargeTransitCard() {
   11. // number of the enabled traffic card returned by the getCardMetadataInDevice interface
   12. const logicalCardNumber = 'logicalCardNumber';
   13. // the specifiedDeviceId returned by the getCardMetadataInDevice interface
   14. const specifiedDeviceId = 'specifiedDeviceId';
   15. // order ID generated after payment in a developer's app, which is implemented by the developer
   16. const serverOrderId = 'serverOrderId';
   17. this.transitCardClient.rechargeTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then((result) => {
   18. console.info(`Succeeded in recharging TransitCard`);
   19. }).catch((err: BusinessError) => {
   20. console.error(`Failed to recharge TransitCard, code:${err.code}, message:${err.message}`);
   21. })
   22. }

   24. build() {
   25. // your application UI
   26. }
   27. }
   ```
