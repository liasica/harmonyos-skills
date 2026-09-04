---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transitcard-scene-open
title: 开通交通卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 交通卡 > 开发场景 > 开通交通卡
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:efbd77d1479c9a31fcfa0c17c36ea19100b77d90926ed521311a0c2abb2765dd
---

申请开通交通卡，将交通卡添加至钱包，实现公交、地铁等nfc刷卡能力。

## 交互流程

交通卡的开通过程分为：获取卡片开通入口、确认卡片是否支持添加、生成并支付订单和完成添卡四个步骤，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/9j9gBdZWTdKoKqhl3s47Pw/zh-cn_image_0000002712405436.png)

## 开发步骤

1. 开发者App启动后，可调用[getCardMetadataInDevice](../harmonyos-references/wallet-wallettransitcard.md#getcardmetadataindevice)接口获取指定设备上可访问的交通卡信息，并以数组形式返回。

   如返回的数组为空，则表示开发者App在该设备上没有可访问的交通卡，无需显示卡片开通入口；如返回数组不为空，则根据返回的[交通卡数据](../harmonyos-references/wallet-wallettransitcard.md#cardmetadataindevice)进行页面展示。

   如果交通卡信息中包括卡号、余额信息，则表明该卡片在设备上已开通，显示卡片信息即可；否则可显示卡片的开通入口。

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
2. 用户选择开通交通卡后，开发者调用[canAddTransitCard](../harmonyos-references/wallet-wallettransitcard.md#canaddtransitcard)接口，传入issuerId和指定设备Id。

   钱包会检查指定设备上目标卡片的开卡条件是否满足，如有条件不满足，会返回相应错误码，请按错误码类型给用户具体的错误提示。如条件满足则会返回开卡凭证数据addCardOpaqueData，数据长度为64个字符。

   ```typescript
   async canAddTransitCard(cardMetadataInDevice: walletTransitCard.CardMetadataInDevice) {
      try {
         const issuerId = cardMetadataInDevice.cardMetadata[0].issuerId;
         const specifiedDeviceId = cardMetadataInDevice.deviceId;
         const addCardOpaqueData = await this.transitCardClient.canAddTransitCard(issuerId, specifiedDeviceId);
         return addCardOpaqueData;
      } catch (err) {
         console.error(`Failed to check, code:${err.code}, message:${err.message}`);
         return '';
      }
   }
   ```
3. 在开卡条件检查通过获取到开卡凭证数据后，开发者App需要将用户的开卡和首充值的订单信息连同开卡凭证addCardOpaqueData一起提交给开发者的服务器生成开卡+首充的订单，addCardOpaqueData需和订单关联存储。

   开发者的服务器将订单提交给支付机构，在用户授权完成支付并收到支付机构的支付完成通知后，向卡公司的SP TSM服务器下发开卡+首充值的订单数据，其中需要包括addCardOpaqueData数据。
4. 在确认订单支付完成后，开发者调用[addTransitCard](../harmonyos-references/wallet-wallettransitcard.md#addtransitcard)接口，传入addCardOpaqueData和serverOrderId进行开卡。

   开卡过程会跳转到钱包App页面进行，开卡成功后返回到开发者App并携带卡片的基本数据，包括卡号和余额信息。开卡过程中如出现失败，钱包App会自动重试，如重试不成功，钱包App会自动发起回滚流程，向支付机构申请退款。

   ```typescript
   async addTransitCard(addCardOpaqueData: string) {
      try {
         const res = await this.transitCardClient.addTransitCard(addCardOpaqueData, this.serverOrderId);
         // 开卡成功，获取到卡片数据，可以用来展示对应交通卡的卡片，包含卡号及余额。
         console.info(`Succeeded in adding card, balance: ${res.balance}, cardNumber: ${res.cardNumber}, logicalCardNumber: ${res.logicalCardNumber}`);
      } catch (err) {
         console.error(`Failed to add card, code:${err.code}, message:${err.message}`);
      }
   }
   ```
