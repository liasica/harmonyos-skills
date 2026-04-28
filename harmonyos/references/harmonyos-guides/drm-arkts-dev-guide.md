---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-arkts-dev-guide
title: 数字版权保护(ArkTS)
breadcrumb: 指南 > 媒体 > DRM Kit（数字版权保护服务） > 数字版权保护(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:11+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:92e94e29d35eef86172de7d7a7581e364802cf5ac76ee943548dae2d8e3f757f
---

开发者可以调用DRM Kit的ArkTS接口实现DRM证书管理、DRM许可证管理、DRM节目授权、DRM节目解密等数字版权保护功能。

DRM Kit提供MediaKeySystem实现DRM证书管理、DRM许可证管理功能，并管理MediaKeySession实例；MediaKeySession实现DRM节目授权，并可支持Media Kit或Media Kit/AVCodec Kit实现DRM节目解密以实现DRM节目播放。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.drm(数字版权保护)](../harmonyos-references/arkts-apis-drm.md)。

1. 导入DRM Kit接口。

   ```
   1. import { drm } from '@kit.DrmKit';
   ```
2. 导入BusinessError模块抛出Drm Kit接口的错误码。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. （可选）调用[getMediaKeySystems](../harmonyos-references/arkts-apis-drm-f.md#drmgetmediakeysystems12)，获取设备支持的DRM解决方案名称和唯一标识的列表。

   ```
   1. let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
   ```

   如果获取结果数组为空，说明该设备中不存在支持的DRM解决方案。
4. （可选）调用[isMediaKeySystemSupported](../harmonyos-references/arkts-apis-drm-f.md#drmismediakeysystemsupported)，查询设备是否支持对应DRM解决方案名称、媒体类型、安全保护级别的DRM解决方案。

   ```
   1. let isSupported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/mp4", drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
   ```

   如果查询结果为false，说明该设备不支持对应的DRM解决方案。
5. 调用[createMediaKeySystem](../harmonyos-references/arkts-apis-drm-f.md#drmcreatemediakeysystem)，创建MediaKeySystem实例。

   ```
   1. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
   ```

   如果创建失败则返回undefined，说明该设备不支持该DRM解决方案。
6. （可选）调用[on('keySystemRequired')](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#onkeysystemrequired)，设置MediaKeySystem状态监听事件。

   通过注册keySystemRequired回调函数监听设备DRM证书请求事件。该事件在需要设备DRM证书时触发，此时建议完成设备DRM证书请求与处理流程。

   ```
   1. mediaKeySystem.on('keySystemRequired', (eventInfo: drm.EventInfo) => {
   2. console.info('keySystemRequired' + 'extra:' + eventInfo.extraInfo + ' data:' + eventInfo.info);
   3. // 设备DRM证书请求与处理。
   4. });
   ```
7. （可选）调用[getCertificateStatus](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#getcertificatestatus)，获取设备DRM证书状态。

   ```
   1. let certificateStatus: drm.CertificateStatus = mediaKeySystem.getCertificateStatus();
   ```
8. （可选）调用[generateKeySystemRequest](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#generatekeysystemrequest)和[processKeySystemResponse](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#processkeysystemresponse)，生成设备DRM证书请求与处理设备DRM证书响应。

   如果设备DRM证书状态不是drm.CertificateStatus.CERT\_STATUS\_PROVISIONED，可以生成设备DRM证书请求，处理设备DRM证书响应。

   ```
   1. if(certificateStatus != drm.CertificateStatus.CERT_STATUS_PROVISIONED) {
   2. mediaKeySystem.generateKeySystemRequest().then(async (drmRequest: drm.ProvisionRequest) => {
   3. console.info("generateKeySystemRequest success", drmRequest.data, drmRequest.defaultURL);
   4. }).catch((err:BusinessError) =>{
   5. console.error("generateKeySystemRequest err end", err.code);
   6. });
   7. } else {
   8. console.info("The certificate already exists.");
   9. }
   10. // 将设备DRM证书请求返回的drmRequest.data通过网络请求发送给DRM证书服务获取设备DRM证书响应，并处理。
   11. let provisionResponseByte = new Uint8Array([0x00, 0x00, 0x00, 0x00]); // 设备DRM证书响应。
   12. mediaKeySystem.processKeySystemResponse(provisionResponseByte).then(() => {
   13. console.info("processKeySystemResponse success");
   14. }).catch((err:BusinessError) =>{
   15. console.error("processKeySystemResponse err end", err.code);
   16. });
   ```
9. 调用[createMediaKeySession](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#createmediakeysession)，创建MediaKeySession实例。

   创建该DRM解决方案默认内容保护级别的MediaKeySession实例。

   ```
   1. let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
   ```
10. （可选）设置MediaKeySession状态监听事件。

    监听MediaKeySession实例的事件，包括媒体密钥请求事件、媒体密钥过期事件、媒体密钥有效期更新事件、媒体密钥变换事件等。

    * 使用[on('keyRequired')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onkeyrequired)接口监听媒体密钥请求事件，此时建议完成媒体密钥请求与处理流程。

      ```
      1. mediaKeySession.on('keyRequired', (eventInfo: drm.EventInfo) => {
      2. console.info('keyRequired' + 'info:' + eventInfo.info + ' extraInfo:' + eventInfo.extraInfo);
      3. // 媒体密钥请求与处理。
      4. });
      ```
    * 使用[on('keyExpired')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onkeyexpired)接口监听媒体密钥过期事件。

      ```
      1. mediaKeySession.on('keyExpired', (eventInfo: drm.EventInfo) => {
      2. console.info('keyExpired' + 'info:' + eventInfo.info + ' extraInfo:' + eventInfo.extraInfo);
      3. });
      ```
    * 使用[on('expirationUpdate')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onexpirationupdate)接口监听媒体密钥有效期更新事件。

      ```
      1. mediaKeySession.on('expirationUpdate', (eventInfo: drm.EventInfo) => {
      2. console.info('expirationUpdate' + 'info:' + eventInfo.info + ' extraInfo:' + eventInfo.extraInfo);
      3. });
      ```
    * 使用[on('keysChange')](../harmonyos-references/arkts-apis-drm-mediakeysession.md#onkeyschange)接口监听媒体密钥变换事件。

      ```
      1. mediaKeySession.on('keysChange', (keyInfo : drm.KeysInfo[], newKeyAvailable:boolean) => {
      2. for(let i = 0; i < keyInfo.length; i++){
      3. console.info('keysChange' + 'info:' + keyInfo[i].keyId + ' extraInfo:' + keyInfo[i].value);
      4. }
      5. });
      ```
11. （可选）调用[requireSecureDecoderModule](../harmonyos-references/arkts-apis-drm-mediakeysession.md#requiresecuredecodermodule)，查询是否需要安全解码。

    ```
    1. try {
    2. let status: boolean = mediaKeySession.requireSecureDecoderModule("video/avc");
    3. } catch (err) {
    4. let error = err as BusinessError;
    5. console.error(`requireSecureDecoderModule ERROR: ${error}`);
    6. }
    ```
12. 调用[generateMediaKeyRequest](../harmonyos-references/arkts-apis-drm-mediakeysession.md#generatemediakeyrequest)和[processMediaKeyResponse](../harmonyos-references/arkts-apis-drm-mediakeysession.md#processmediakeyresponse)，生成媒体密钥请求与处理媒体密钥响应。

    获取到DRM节目中的DRM信息时，可以生成媒体密钥请求，处理媒体密钥响应，以请求许可证完成DRM节目授权。

    ```
    1. // 根据DRM解决方案要求，基于DRM信息中的pssh生成initData。
    2. let initData = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
    3. // 根据DRM解决方案要求设置可选数据的值。
    4. let optionalData:drm.OptionsData[] = [{
    5. name: "optionalDataName",
    6. value: "optionalDataValue"
    7. }];
    8. // 在线媒体密钥请求和响应。
    9. mediaKeySession.generateMediaKeyRequest("video/mp4", initData, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE, optionalData).then(async (licenseRequest: drm.MediaKeyRequest) => {
    10. console.info("generateMediaKeyRequest success", licenseRequest.mediaKeyRequestType, licenseRequest.data, licenseRequest.defaultURL);
    11. // 将媒体密钥请求返回的licenseRequest.data通过网络请求发送给DRM服务获取媒体密钥响应，并处理。
    12. let licenseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]); // 媒体密钥响应。
    13. mediaKeySession.processMediaKeyResponse(licenseResponse).then((mediaKeyId: Uint8Array) => {
    14. console.info("processMediaKeyResponse success");
    15. }).catch((err:BusinessError) =>{
    16. console.error("processMediaKeyResponse err end", err.code);
    17. });
    18. }).catch((err:BusinessError) =>{
    19. console.error("generateMediaKeyRequest err end", err.code);
    20. });
    21. // 离线媒体密钥请求和响应。
    22. let offlineMediaKeyId: Uint8Array;
    23. mediaKeySession.generateMediaKeyRequest("video/mp4", initData, drm.MediaKeyType.MEDIA_KEY_TYPE_OFFLINE, optionalData).then((licenseRequest: drm.MediaKeyRequest) => {
    24. console.info("generateMediaKeyRequest success", licenseRequest.mediaKeyRequestType, licenseRequest.data, licenseRequest.defaultURL);
    25. // 将媒体密钥请求返回的licenseRequest.data通过网络请求发送给DRM服务获取媒体密钥响应，并处理。
    26. let licenseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]); // 媒体密钥响应。
    27. mediaKeySession.processMediaKeyResponse(licenseResponse).then((mediaKeyId: Uint8Array) => {
    28. offlineMediaKeyId = new Uint8Array(mediaKeyId);
    29. console.info("processMediaKeyResponse success");
    30. }).catch((err:BusinessError) =>{
    31. console.error("processMediaKeyResponse err end", err.code);
    32. });
    33. }).catch((err:BusinessError) =>{
    34. console.error("generateMediaKeyRequest err end", err.code);
    35. });
    ```
13. （可选）调用[restoreOfflineMediaKey](../harmonyos-references/arkts-apis-drm-mediakeysession.md#restoreofflinemediakeys)，恢复离线媒体密钥。

    ```
    1. mediaKeySession.restoreOfflineMediaKeys(offlineMediaKeyId).then(() => {
    2. console.info("restoreOfflineMediaKeys success.");
    3. }).catch((err: BusinessError) => {
    4. console.error(`restoreOfflineMediaKeys: ERROR: ${err}`);
    5. });
    ```
14. （可选）调用[checkMediaKeyStatus](../harmonyos-references/arkts-apis-drm-mediakeysession.md#checkmediakeystatus)，检查媒体密钥状态。

    ```
    1. let mediaKeyStatus: drm.MediaKeyStatus[]
    2. try {
    3. mediaKeyStatus = mediaKeySession.checkMediaKeyStatus()
    4. } catch (err) {
    5. let error = err as BusinessError;
    6. console.error(`checkMediaKeyStatus: ERROR: ${error}`);
    7. }
    ```
15. （可选）调用[getOfflineMediaKeyIds](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#getofflinemediakeyids)获取离线媒体密钥标识列表，调用[getOfflineMediaKeyStatus](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#getofflinemediakeystatus)获取离线媒体密钥状态，调用[clearOfflineMediaKeys](../harmonyos-references/arkts-apis-drm-mediakeysystem.md#clearofflinemediakeys)删除离线媒体密钥。

    媒体密钥标识用于对离线媒体密钥的管理。

    ```
    1. let offlineMediaKeyIds: Uint8Array[] = mediaKeySystem.getOfflineMediaKeyIds();
    2. try {
    3. let offlineMediaKeyStatus: drm.OfflineMediaKeyStatus = mediaKeySystem.getOfflineMediaKeyStatus(offlineMediaKeyIds[0]);
    4. } catch (err) {
    5. let error = err as BusinessError;
    6. console.error(`getOfflineMediaKeyStatus ERROR: ${error}`);
    7. }
    8. try {
    9. mediaKeySystem.clearOfflineMediaKeys(offlineMediaKeyIds[0]);
    10. } catch (err) {
    11. let error = err as BusinessError;
    12. console.error(`clearOfflineMediaKeys ERROR: ${error}`);
    13. }
    ```
16. 销毁MediaKeySession实例。

    完成加密媒体解密，MediaKeySession实例不再使用时，销毁MediaKeySession实例。

    ```
    1. // MediaKeySession实例使用完需要进行资源释放。
    2. mediaKeySession.destroy();
    ```
17. 销毁MediaKeySystem实例。

    完成DRM功能使用，MediaKeySystem实例不再使用，销毁MediaKeySystem实例。

    ```
    1. // MediaKeySystem实例使用完需要进行资源释放。
    2. mediaKeySystem.destroy();
    ```
