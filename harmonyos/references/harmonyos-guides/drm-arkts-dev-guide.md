---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-arkts-dev-guide
title: 数字版权保护(ArkTS)
breadcrumb: 指南 > 媒体 > DRM Kit（数字版权保护服务） > 数字版权保护(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:456ed01cea8cc2047962fdcd99d27e79bf3aac07da02dc67794090ac51236cdf
---

开发者可以调用DRM Kit的ArkTS接口实现DRM证书管理、DRM许可证管理、DRM节目授权、DRM节目解密等数字版权保护功能。

DRM Kit提供MediaKeySystem实现DRM证书管理、DRM许可证管理功能，并管理MediaKeySession实例；MediaKeySession实现DRM节目授权，并可支持Media Kit/AVCodec Kit实现DRM节目解密以实现DRM节目播放。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.drm](../harmonyos-references/arkts-apis-drm.md)。

1. 导入DRM Kit接口。

   ```typescript
   import { drm } from '@kit.DrmKit';
   ```
2. 导入BusinessError模块抛出DRM Kit接口的错误码。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. （可选）调用[getMediaKeySystems](../harmonyos-references/arkts-apis-drm-f.md#drmgetmediakeysystems12)，获取设备支持的DRM解决方案名称和唯一标识的列表。

   ```typescript
   const descriptions: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
   ```

   如果获取结果数组为空，说明该设备中不存在支持的DRM解决方案。
4. （可选）调用[isMediaKeySystemSupported](../harmonyos-references/arkts-apis-drm-f.md#drmismediakeysystemsupported)，查询设备是否支持对应DRM解决方案名称、媒体类型、安全保护级别的DRM解决方案。

   ```typescript
   const byName = drm.isMediaKeySystemSupported(DRM_SOLUTION_NAME);
   // ...
   const byMimeType = drm.isMediaKeySystemSupported(DRM_SOLUTION_NAME, MIME_TYPE);
   // ...
   const byLevel = drm.isMediaKeySystemSupported(
     DRM_SOLUTION_NAME, MIME_TYPE, drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
   // ...
   ```

   如果查询结果为false，说明该设备不支持对应的DRM解决方案。
5. 调用[createMediaKeySystem](../harmonyos-references/arkts-apis-drm-f.md#drmcreatemediakeysystem)，创建MediaKeySystem实例。

   ```typescript
   mediaKeySystem = drm.createMediaKeySystem(DRM_SOLUTION_NAME);
   ```

   如果创建失败则返回undefined，说明该设备不支持该DRM解决方案。
6. （可选）调用[on('keySystemRequired')](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#onkeysystemrequired)，设置MediaKeySystem状态监听事件。

   通过注册keySystemRequired回调函数监听设备DRM证书请求事件。该事件在需要设备DRM证书时触发，此时建议完成设备DRM证书请求与处理流程。

   ```typescript
   mediaKeySystem.on('keySystemRequired', (eventInfo: drm.EventInfo) => {
     console.info(`keySystemRequired extra:${eventInfo.extraInfo} data:${eventInfo.info}`);
     // 设备DRM证书请求与处理。
   });
   ```
7. （可选）调用[getCertificateStatus](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#getcertificatestatus)，获取设备DRM证书状态。

   ```typescript
   const certificateStatus = mediaKeySystem.getCertificateStatus();
   ```
8. （可选）调用[generateKeySystemRequest](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#generatekeysystemrequest)和[processKeySystemResponse](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#processkeysystemresponse)，生成设备DRM证书请求与处理设备DRM证书响应。

   如果设备DRM证书状态不是drm.CertificateStatus.CERT\_STATUS\_PROVISIONED，可以生成设备DRM证书请求，处理设备DRM证书响应。

   ```typescript
   const provisionRequest = await mediaKeySystem.generateKeySystemRequest();
   ```

   ```typescript
   // 将设备DRM证书请求返回的provisionRequest.data通过网络请求发送给DRM证书服务获取设备DRM证书响应，并处理。
   const provisionResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]); // 设备DRM证书响应。
   await mediaKeySystem.processKeySystemResponse(provisionResponse);
   ```
9. 调用[createMediaKeySession](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#createmediakeysession)，创建MediaKeySession实例。

   创建该DRM解决方案默认内容保护级别的MediaKeySession实例。

   ```typescript
   mediaKeySession = mediaKeySystem.createMediaKeySession();
   ```
10. （可选）设置MediaKeySession状态监听事件。

    监听MediaKeySession实例的事件，包括媒体密钥请求事件、媒体密钥过期事件、媒体密钥有效期更新事件、媒体密钥变换事件等。

    * 使用[on('keyRequired')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onkeyrequired)接口监听媒体密钥请求事件，此时建议完成媒体密钥请求与处理流程。

      ```typescript
      mediaKeySession.on('keyRequired', (eventInfo: drm.EventInfo) => {
        console.info(`keyRequired info:${eventInfo.info} extraInfo:${eventInfo.extraInfo}`);
        // 媒体密钥请求与处理。
      });
      ```
    * 使用[on('keyExpired')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onkeyexpired)接口监听媒体密钥过期事件。

      ```typescript
      mediaKeySession.on('keyExpired', (eventInfo: drm.EventInfo) => {
        console.info(`keyExpired info:${eventInfo.info} extraInfo:${eventInfo.extraInfo}`);
      });
      ```
    * 使用[on('expirationUpdate')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onexpirationupdate)接口监听媒体密钥有效期更新事件。

      ```typescript
      mediaKeySession.on('expirationUpdate', (eventInfo: drm.EventInfo) => {
        console.info(`expirationUpdate info:${eventInfo.info} extraInfo:${eventInfo.extraInfo}`);
      });
      ```
    * 使用[on('keysChange')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onkeyschange)接口监听媒体密钥变换事件。

      ```typescript
      mediaKeySession.on('keysChange', (keyInfo: drm.KeysInfo[], newKeyAvailable: boolean) => {
        for (let i = 0; i < keyInfo.length; i++) {
          console.info(`keysChange keyId:${keyInfo[i].keyId} value:${keyInfo[i].value}`);
        }
      });
      ```
11. （可选）调用[requireSecureDecoderModule](../harmonyos-references/arkts-apis-drm-mediakeysession.md#requiresecuredecodermodule)，查询是否需要安全解码。

    ```typescript
    const needSecureDecoder = mediaKeySession.requireSecureDecoderModule(MIME_TYPE);
    ```
12. 调用[generateMediaKeyRequest](../harmonyos-references/arkts-apis-drm-mediakeysession.md#generatemediakeyrequest)和[processMediaKeyResponse](../harmonyos-references/arkts-apis-drm-mediakeysession.md#processmediakeyresponse)，生成媒体密钥请求与处理媒体密钥响应。

    获取到DRM节目中的DRM信息时，可以生成媒体密钥请求，处理媒体密钥响应，以请求许可证完成DRM节目授权。

    ```typescript
    // 实际应用中initData应从媒体内容的PSSH box中提取。
    const initData = new Uint8Array([0x00, 0x01, 0x02, 0x03]);
    // 根据DRM解决方案要求设置可选数据的值。
    const optionalData: drm.OptionsData[] = [{
      name: 'optionalDataName',
      value: 'optionalDataValue'
    }];
    const mediaKeyRequest = await mediaKeySession.generateMediaKeyRequest(
      MIME_TYPE, initData, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE, optionalData);
    ```

    ```typescript
    // 将媒体密钥请求返回的mediaKeyRequest.data通过网络请求发送给DRM服务获取媒体密钥响应，并处理。
    const mediaKeyResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]); // 媒体密钥响应。
    const offlineMediaKeyId = await mediaKeySession.processMediaKeyResponse(mediaKeyResponse);
    ```
13. （可选）调用[restoreOfflineMediaKeys](../harmonyos-references/arkts-apis-drm-mediakeysession.md#restoreofflinemediakeys)，恢复离线媒体密钥。

    ```typescript
    await mediaKeySession.restoreOfflineMediaKeys(offlineMediaKeyId);
    ```
14. （可选）调用[checkMediaKeyStatus](../harmonyos-references/arkts-apis-drm-mediakeysession.md#checkmediakeystatus)，检查媒体密钥状态。

    ```typescript
    const keyStatus = mediaKeySession.checkMediaKeyStatus();
    ```
15. （可选）调用[getOfflineMediaKeyIds](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#getofflinemediakeyids)获取离线媒体密钥标识列表，调用[getOfflineMediaKeyStatus](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#getofflinemediakeystatus)获取离线媒体密钥状态，调用[clearOfflineMediaKeys](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#clearofflinemediakeys)删除离线媒体密钥。

    媒体密钥标识用于对离线媒体密钥的管理。

    ```typescript
    const offlineMediaKeyIds = mediaKeySystem.getOfflineMediaKeyIds();
    if (offlineMediaKeyIds.length > 0) {
      const offlineStatus = mediaKeySystem.getOfflineMediaKeyStatus(offlineMediaKeyIds[0]);
      mediaKeySystem.clearOfflineMediaKeys(offlineMediaKeyIds[0]);
    }
    ```
16. 销毁MediaKeySession实例。

    完成加密媒体解密，MediaKeySession实例不再使用时，销毁MediaKeySession实例。

    ```typescript
    mediaKeySession.destroy();
    ```
17. 销毁MediaKeySystem实例。

    完成DRM功能使用，MediaKeySystem实例不再使用，销毁MediaKeySystem实例。

    ```typescript
    mediaKeySystem.destroy();
    ```
