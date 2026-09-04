---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transitcard-scene-update
title: 更新交通卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 交通卡 > 开发场景 > 更新交通卡
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f8a68240fdf857dd5e317990c8f1ec6044cbe3cb6ede2e8a5bd872e9cf81b714
---

更新交通卡的相关信息，从而保持卡数据与交通卡公司系统同步。

## 交互流程

交通卡的更新过程分为：卡片展示、生成更新业务订单和发起更新三个步骤，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/BWvfUTQ5SxKNiIroEWEauQ/zh-cn_image_0000002712245478.png)

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
2. 用户选择了要更新的交通卡后，开发者App需向开发者的后台服务器发起更新业务订单的生成请求。
3. 开发者App可调用[updateTransitCard](../harmonyos-references/wallet-wallettransitcard.md#updatetransitcard)接口发起更新处理过程。

   ```typescript
   async updateTransitCard(cardMetadataInDevice: walletTransitCard.CardMetadataInDevice) {
      try {
         const logicalCardNumber = cardMetadataInDevice.cardMetadata[0].logicalCardNumber;
         const specifiedDeviceId = cardMetadataInDevice.deviceId;
         await this.transitCardClient.updateTransitCard(logicalCardNumber, specifiedDeviceId, this.serverOrderId);
         console.info('Succeeded in updating');
      } catch (err) {
         console.error(`Failed to update, code:${err.code}, message:${err.message}`);
      }
   }
   ```
