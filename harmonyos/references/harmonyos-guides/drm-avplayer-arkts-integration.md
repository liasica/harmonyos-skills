---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-avplayer-arkts-integration
title: 基于AVPlayer播放DRM节目(ArkTS)
breadcrumb: 指南 > 媒体 > DRM Kit（数字版权保护服务） > 基于AVPlayer播放DRM节目(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:17+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:13608d23e1a645f180a6ef1e2a1652f2b7c72fcdddfd4b6838e9dd31f1e27069
---

开发者可以调用DRM Kit和Media Kit的ArkTS接口实现AVPlayer播放器，完成DRM节目播放。

## 开发步骤

1. 导入DRM Kit和Media Kit接口。

   ```ts
   import { drm } from '@kit.DrmKit'
   import { media } from '@kit.MediaKit'
   ```
2. 导入BusinessError模块抛出Drm Kit接口的错误码。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit'
   ```
3. 调用[createAVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)，创建AVPlayer实例并设置DRM信息监听事件。

   ```ts
   let playerHandle: media.AVPlayer;
   async function initPlayer() {
   playerHandle = await media.createAVPlayer();
   playerHandle.on('mediaKeySystemInfoUpdate', async (mediaKeySystemInfo: drm.MediaKeySystemInfo[]) => {
   console.info('player has received drmInfo signal: ' + JSON.stringify(mediaKeySystemInfo))
   // 处理DRM信息。
   // 设置解密session。
   })
   }
   ```
4. 调用[createMediaKeySystem](../harmonyos-references/arkts-apis-drm-f.md#drmcreatemediakeysystem)和[createMediaKeySession](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#createmediakeysession)根据DRM信息中的uuid创建MediaKeySystem和MediaKeySession实例。

   ```ts
   let mediaKeySystem: drm.MediaKeySystem
   let mediaKeySession: drm.MediaKeySession
   let drmInfoArr: drm.MediaKeySystemInfo[] = mediaKeySystemInfo
   for (let i = 0; i < drmInfoArr.length; i++) {
     console.info('drmInfoArr - uuid: ' + drmInfoArr[i].uuid)
     console.info('drmInfoArr - pssh: ' + drmInfoArr[i].pssh)
     let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
     let solutionName: string = "com.wiseplay.drm"
     for (let item of description) {
       if (drmInfoArr[i].uuid == item.uuid) {
         solutionName = item.name
         }
       }
       let isSupported: boolean = drm.isMediaKeySystemSupported(solutionName, "video/mp4");
       if (isSupported) {
         mediaKeySystem = drm.createMediaKeySystem(solutionName);
         mediaKeySession = mediaKeySystem.createMediaKeySession();
     }
     // 媒体密钥请求与处理。
   }
   ```
5. 调用[generateMediaKeyRequest](../harmonyos-references/arkts-apis-drm-mediakeysession.md#generatemediakeyrequest)生成媒体密钥请求，并调用[processMediaKeyResponse](../harmonyos-references/arkts-apis-drm-mediakeysession.md#processmediakeyresponse)处理媒体密钥响应。

   ```ts
   let initData: Uint8Array = new Uint8Array(drmInfoArr[i].pssh);
   const optionsData: drm.OptionsData[] = [{
     name: "optionalDataName",
     value: "optionalDataValue"
   }]
   mediaKeySession.generateMediaKeyRequest("video/mp4", initData, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE, optionsData).then(async (licenseRequest) => {
     console.info("generateMediaKeyRequest success", licenseRequest.mediaKeyRequestType, licenseRequest.data, licenseRequest.defaultURL);
     // 将媒体密钥请求返回的licenseRequest.data通过网络请求发送给DRM服务获取媒体密钥响应，并处理。
     let licenseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
     mediaKeySession.processMediaKeyResponse(licenseResponse).then((mediaKeyId: Uint8Array) => {
       console.info("processMediaKeyResponse success");
     }).catch((err:BusinessError) =>{
       console.error("processMediaKeyResponse err end", err.code);
     });
   }).catch((err:BusinessError) =>{
     console.error("generateMediaKeyRequest err end", err.code);
   });
   ```
6. 调用[requireSecureDecoderModule](../harmonyos-references/arkts-apis-drm-mediakeysession.md#requiresecuredecodermodule)和[setDecryptionConfig](../harmonyos-references/arkts-apis-media-avplayer.md#setdecryptionconfig11)，在处理媒体密钥响应成功后设置解密session。

   ```ts
   let svp: boolean = mediaKeySession.requireSecureDecoderModule('video/avc');
   playerHandle.setDecryptionConfig(mediaKeySession, svp)
   ```
7. 销毁AVPlayer实例并根据released事件监听销毁MediaKeySession和MediaKeySystem实例。

   ```ts
   playerHandle.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
      if (state == 'released') {
         mediaKeySession.destroy();
         mediaKeySystem.destroy();
      }
   })
   ```
