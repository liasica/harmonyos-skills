---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-avplayer-arkts-integration
title: 基于AVPlayer播放DRM节目(ArkTS)
breadcrumb: 指南 > 媒体 > DRM Kit（数字版权保护服务） > 基于AVPlayer播放DRM节目(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7a41089e3710c891e17b573c19169aae866a65bfaca7b4c16d6f7827cb65d422
---

开发者可以调用DRM Kit和Media Kit的ArkTS接口实现AVPlayer播放器，完成DRM节目播放。

## 开发步骤

1. 导入DRM Kit和Media Kit接口。

   ```
   1. import { drm } from '@kit.DrmKit'
   2. import { media } from '@kit.MediaKit'
   ```
2. 导入BusinessError模块抛出Drm Kit接口的错误码。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit'
   ```
3. 调用[createAVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)，创建AVPlayer实例并设置DRM信息监听事件。

   ```
   1. let playerHandle: media.AVPlayer;
   2. async function initPlayer() {
   3. playerHandle = await media.createAVPlayer();
   4. playerHandle.on('mediaKeySystemInfoUpdate', async (mediaKeySystemInfo: drm.MediaKeySystemInfo[]) => {
   5. console.info('player has received drmInfo signal: ' + JSON.stringify(mediaKeySystemInfo))
   6. // 处理DRM信息。
   7. // 设置解密session。
   8. })
   9. }
   ```
4. 调用[createMediaKeySystem](../harmonyos-references/arkts-apis-drm-f.md#drmcreatemediakeysystem)和[createMediaKeySession](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#createmediakeysession)根据DRM信息中的uuid创建MediaKeySystem和MediaKeySession实例。

   ```
   1. let mediaKeySystem: drm.MediaKeySystem
   2. let mediaKeySession: drm.MediaKeySession
   3. let drmInfoArr: drm.MediaKeySystemInfo[] = mediaKeySystemInfo
   4. for (let i = 0; i < drmInfoArr.length; i++) {
   5. console.info('drmInfoArr - uuid: ' + drmInfoArr[i].uuid)
   6. console.info('drmInfoArr - pssh: ' + drmInfoArr[i].pssh)
   7. let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
   8. let solutionName: string = "com.wiseplay.drm"
   9. for (let item of description) {
   10. if (drmInfoArr[i].uuid == item.uuid) {
   11. solutionName = item.name
   12. }
   13. }
   14. let isSupported: boolean = drm.isMediaKeySystemSupported(solutionName, "video/mp4");
   15. if (isSupported) {
   16. mediaKeySystem = drm.createMediaKeySystem(solutionName);
   17. mediaKeySession = mediaKeySystem.createMediaKeySession();
   18. }
   19. // 媒体密钥请求与处理。
   20. }
   ```
5. 调用[generateMediaKeyRequest](../harmonyos-references/arkts-apis-drm-mediakeysession.md#generatemediakeyrequest)生成媒体密钥请求，并调用[processMediaKeyResponse](../harmonyos-references/arkts-apis-drm-mediakeysession.md#processmediakeyresponse)处理媒体密钥响应。

   ```
   1. let initData: Uint8Array = new Uint8Array(drmInfoArr[i].pssh);
   2. const optionsData: drm.OptionsData[] = [{
   3. name: "optionalDataName",
   4. value: "optionalDataValue"
   5. }]
   6. mediaKeySession.generateMediaKeyRequest("video/mp4", initData, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE, optionsData).then(async (licenseRequest) => {
   7. console.info("generateMediaKeyRequest success", licenseRequest.mediaKeyRequestType, licenseRequest.data, licenseRequest.defaultURL);
   8. // 将媒体密钥请求返回的licenseRequest.data通过网络请求发送给DRM服务获取媒体密钥响应，并处理。
   9. let licenseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
   10. mediaKeySession.processMediaKeyResponse(licenseResponse).then((mediaKeyId: Uint8Array) => {
   11. console.info("processMediaKeyResponse success");
   12. }).catch((err:BusinessError) =>{
   13. console.error("processMediaKeyResponse err end", err.code);
   14. });
   15. }).catch((err:BusinessError) =>{
   16. console.error("generateMediaKeyRequest err end", err.code);
   17. });
   ```
6. 调用[requireSecureDecoderModule](../harmonyos-references/arkts-apis-drm-mediakeysession.md#requiresecuredecodermodule)和[setDecryptionConfig](../harmonyos-references/arkts-apis-media-avplayer.md#setdecryptionconfig11)，在处理媒体密钥响应成功后设置解密session。

   ```
   1. let svp: boolean = mediaKeySession.requireSecureDecoderModule('video/avc');
   2. playerHandle.setDecryptionConfig(mediaKeySession, svp)
   ```
7. 销毁AVPlayer实例并根据released事件监听销毁MediaKeySession和MediaKeySystem实例。

   ```
   1. playerHandle.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
   2. if (state == 'released') {
   3. mediaKeySession.destroy();
   4. mediaKeySystem.destroy();
   5. } else if (state == 'releasing') {
   6. await playerHandle.release();
   7. }
   8. })
   ```
