---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-avplayer-arkts-integration
title: 基于AVPlayer播放DRM节目(ArkTS)
breadcrumb: 指南 > 媒体 > DRM Kit（数字版权保护服务） > 基于AVPlayer播放DRM节目(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d2e3cfb0b65cccdf9d5c14b54ce0ebfcc07da9410b9c608483dbaef2d298a14a
---

开发者可以调用DRM Kit和Media Kit的ArkTS接口实现AVPlayer播放器，完成DRM节目播放。

## 开发步骤

1. 导入DRM Kit和Media Kit接口。

   ```typescript
   import { drm } from '@kit.DrmKit';
   import { media } from '@kit.MediaKit';
   ```
2. 导入BusinessError模块抛出Drm Kit接口的错误码。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. 调用[createAVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)，创建AVPlayer实例并设置DRM信息监听事件。

   ```typescript
   private playerHandle?: media.AVPlayer;

   async initPlayer(): Promise<void> {
     this.playerHandle = await media.createAVPlayer();
     this.playerHandle.on('mediaKeySystemInfoUpdate', async (mediaKeySystemInfo: drm.MediaKeySystemInfo[]) => {
       console.info('player has received drmInfo signal: ' + JSON.stringify(mediaKeySystemInfo));
       // 处理DRM信息，根据DRM信息中的uuid创建MediaKeySystem与MediaKeySession实例，并完成媒体密钥请求与处理。
       try {
         await this.processDrmInfo(mediaKeySystemInfo);
       } catch (err) {
         const e = err as BusinessError;
         console.error(`processDrmInfo failed, code: ${e.code}, message: ${e.message}`);
       }
     });
   }
   ```
4. 调用[createMediaKeySystem](../harmonyos-references/arkts-apis-drm-f.md#drmcreatemediakeysystem)和[createMediaKeySession](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#createmediakeysession-1)根据DRM信息中的uuid创建MediaKeySystem和MediaKeySession实例。

   ```typescript
   private mediaKeySystem?: drm.MediaKeySystem;
   private mediaKeySession?: drm.MediaKeySession;

   async processDrmInfo(mediaKeySystemInfo: drm.MediaKeySystemInfo[]): Promise<void> {
     const drmInfoArr: drm.MediaKeySystemInfo[] = mediaKeySystemInfo;
     for (let i = 0; i < drmInfoArr.length; i++) {
       console.info('drmInfoArr - uuid: ' + drmInfoArr[i].uuid);
       console.info('drmInfoArr - pssh: ' + drmInfoArr[i].pssh);
       const description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
       let solutionName: string = 'com.wiseplay.drm';
       for (let item of description) {
         if (drmInfoArr[i].uuid == item.uuid) {
           solutionName = item.name;
         }
       }
       // 实际开发中应从播放内容的轨道信息（如AVPlayer.getTrackDescription()）或已知媒体源获取mimeType。
       // drm.MediaKeySystemInfo不包含mimeType字段，无法直接从drmInfoArr[i]获取。
       const mimeType: string = 'video/mp4';
       const isSupported: boolean = drm.isMediaKeySystemSupported(solutionName, mimeType);
       if (isSupported) {
         this.mediaKeySystem = drm.createMediaKeySystem(solutionName);
         this.mediaKeySession = this.mediaKeySystem.createMediaKeySession();
         // 媒体密钥请求与处理。
         await this.processMediaKey(drmInfoArr[i].pssh, mimeType);
       }
     }
     // 媒体密钥请求与处理后，设置解密session。
     this.setDecryptionConfig();
   }
   ```
5. 调用[generateMediaKeyRequest](../harmonyos-references/arkts-apis-drm-mediakeysession.md#generatemediakeyrequest)生成媒体密钥请求，并调用[processMediaKeyResponse](../harmonyos-references/arkts-apis-drm-mediakeysession.md#processmediakeyresponse)处理媒体密钥响应。

   ```typescript
   async processMediaKey(pssh: Uint8Array, mimeType: string): Promise<void> {
     if (this.mediaKeySession === undefined) {
       return;
     }
     const initData: Uint8Array = new Uint8Array(pssh);
     const optionsData: drm.OptionsData[] = [{
       name: 'optionalDataName',
       value: 'optionalDataValue'
     }];
     try {
       const licenseRequest = await this.mediaKeySession.generateMediaKeyRequest(
         mimeType, initData, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE, optionsData);
       console.info('generateMediaKeyRequest success, type: ' + licenseRequest.mediaKeyRequestType);
       // 将媒体密钥请求返回的licenseRequest.data通过网络请求发送给DRM服务获取媒体密钥响应，并处理。
       const licenseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]); // 媒体密钥响应。
       await this.mediaKeySession.processMediaKeyResponse(licenseResponse);
     } catch (err) {
       const e = err as BusinessError;
       console.error(`generateMediaKeyRequest or processMediaKeyResponse failed, code: ${e.code}`);
     }
   }
   ```
6. 调用[requireSecureDecoderModule](../harmonyos-references/arkts-apis-drm-mediakeysession.md#requiresecuredecodermodule)和[setDecryptionConfig](../harmonyos-references/arkts-apis-media-avplayer.md#setdecryptionconfig11)，在处理媒体密钥响应成功后设置解密session。

   ```typescript
   setDecryptionConfig(): void {
     if (this.playerHandle === undefined || this.mediaKeySession === undefined) {
       return;
     }
     // 实际开发中应从轨道信息获取codec mime type（如video/avc），再传入requireSecureDecoderModule。
     const svp: boolean = this.mediaKeySession.requireSecureDecoderModule('video/avc');
     this.playerHandle.setDecryptionConfig(this.mediaKeySession, svp);
   }
   ```
7. 销毁AVPlayer实例并根据released事件监听销毁MediaKeySession和MediaKeySystem实例。

   ```typescript
   async releasePlayer(): Promise<void> {
     if (this.playerHandle === undefined) {
       return;
     }
     // 销毁AVPlayer实例，并根据released事件监听销毁MediaKeySession和MediaKeySystem实例。
     this.playerHandle.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
       if (state == 'released') {
         this.mediaKeySession?.destroy();
         this.mediaKeySystem?.destroy();
         this.mediaKeySession = undefined;
         this.mediaKeySystem = undefined;
         this.playerHandle = undefined;
         // ...
       }
     });
     await this.playerHandle.release();
   }
   ```
