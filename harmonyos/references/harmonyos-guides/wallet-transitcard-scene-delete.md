---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transitcard-scene-delete
title: 删除交通卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 交通卡 > 开发场景 > 删除交通卡
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:33+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:2c36f8d2a4409f0975ac03f0e7d59c93418008605d833d7254d38808a005861e
---

删除钱包中的交通卡，同时取消与交通卡公司的关联关系。

## 交互流程

交通卡的删卡过程分为：卡片展示、生成删卡业务订单和发起删卡三个步骤，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/eeT00jN0QPC-QAfksgmiWw/zh-cn_image_0000002817507789.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBAA3DACBADA8114AC016A52CC9295633EA17569A8F371C4461D3E367306E8AB)

## 开发步骤

1. 开发者App启动后，可调用[getCardMetadataInDevice](../harmonyos-references/wallet-wallettransitcard.md#getcardmetadataindevice)接口获取指定设备上可访问的交通卡信息，并以数组形式返回。

   如返回的数组为空，则表示开发者App在该设备上没有可访问的交通卡，无需显示卡片开通入口；如返回数组不为空，则根据返回的[交通卡数据](../harmonyos-references/wallet-wallettransitcard.md#cardmetadataindevice)进行页面展示。

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
2. 如果交通卡信息中包括卡号、余额信息，则表明该卡片在设备上已开通，显示卡片信息即可；否则可显示卡片的开通入口。
3. 用户选择了要删除的交通卡后，开发者App需向开发者的后台服务器发起删卡业务订单的生成请求。
4. 开发者可调用[deleteTransitCard](../harmonyos-references/wallet-wallettransitcard.md#deletetransitcard)接口发起删卡处理过程。如删卡过程出现异常导致失败，开发者会收到相应的错误码。

   ```typescript
   async deleteTransitCard(cardMetadataInDevice: walletTransitCard.CardMetadataInDevice) {
      try {
         const logicalCardNumber = cardMetadataInDevice.cardMetadata[0].logicalCardNumber;
         const specifiedDeviceId = cardMetadataInDevice.deviceId;
         await this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, this.serverOrderId);
         console.info('Succeeded in deleting');
      } catch (err) {
         console.error(`Failed to delete, code:${err.code}, message:${err.message}`);
      }
   }
   ```
