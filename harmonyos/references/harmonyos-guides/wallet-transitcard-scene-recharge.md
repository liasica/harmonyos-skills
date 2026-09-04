---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transitcard-scene-recharge
title: 充值交通卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 交通卡 > 开发场景 > 充值交通卡
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:37dc0ae470d8804a39e77d5a2e61cf44673bf45c5c843ceb4358167866df32fe
---

用户为钱包中的交通卡充值，恢复或增加卡内余额，无需排队购票，方便公交、地铁出行。

## 交互流程

交通卡的充值过程分为：卡片展示、生成并支付充值订单和发起充值三个步骤，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/YKcedy_tSGmOdJ-Nf7joWA/zh-cn_image_0000002742124385.png)

## 开发步骤

1. 开发者App启动后，可调用[getCardMetadataInDevice](../harmonyos-references/wallet-wallettransitcard.md#getcardmetadataindevice)接口获取指定设备上可访问的交通卡信息，并以数组形式返回。

   如返回的数组为空，则表示开发者App在该设备上没有可访问的交通卡，无需显示卡片开通入口；如返回数组不为空，则根据返回的[交通卡数据](../harmonyos-references/wallet-wallettransitcard.md#cardmetadataindevice)进行页面展示。如果交通卡信息中包括卡号、余额信息，则表明该卡片在设备上已开通，显示卡片信息即可；否则可显示卡片的开通入口。

   ```typescript
   async getCardMetadataInDevice() {
      try {
         // 如果是手机设备，数组只有一个元素。如果是穿戴设备，会根据连接的穿戴设备数返回对应数量的数组元素。
         const cardMetadataInDeviceList = await this.transitCardClient.getCardMetadataInDevice(this.deviceType);
         console.info(`Succeeded in getting cardMetadataInDevice, card length is ${cardMetadataInDeviceList.length}`);
         return cardMetadataInDeviceList;
      } catch (err) {
         console.error(`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}`);
         return [];
      }
   }
   ```
2. 用户选择了给指定的交通卡充值时，开发者App需向开发者的后台服务器发起充值订单的生成请求，并引导用户完成支付。
3. 开发者App在查询到订单已支付完成后，调用[rechargeTransitCard](../harmonyos-references/wallet-wallettransitcard.md#rechargetransitcard)接口，发起将订单金额充值到卡内的处理过程。

   如果充值正常结束，开发者App会收到充值成功的返回值并携带新的余额；如果充值过程出现失败，在钱包App自行发起重试后仍然失败的情况下，钱包会发起订单退款的请求。若SP TSM或开发者服务器器确认订单可退款，需调用支付渠道的订单撤销接口，将订单金额原路退回。

   ```typescript
   async rechargeTransitCard(cardMetadataInDevice: walletTransitCard.CardMetadataInDevice) {
      try {
         const logicalCardNumber = cardMetadataInDevice.cardMetadata[0].logicalCardNumber;
         const specifiedDeviceId = cardMetadataInDevice.deviceId;
         const balance = await this.transitCardClient.rechargeTransitCard(logicalCardNumber, specifiedDeviceId, this.serverOrderId);
         // 充值成功，返回当前余额。
         console.info(`Succeeded in recharging, balance: ${balance}`);
      } catch (err) {
         console.error(`Failed to recharge, code:${err.code}, message:${err.message}`);
      }
   }
   ```
