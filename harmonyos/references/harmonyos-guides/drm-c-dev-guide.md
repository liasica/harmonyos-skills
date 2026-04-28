---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/drm-c-dev-guide
title: 数字版权保护(C/C++)
breadcrumb: 指南 > 媒体 > DRM Kit（数字版权保护服务） > 数字版权保护(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:11+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:9566b45ba2026888abd2ea6f7b5ce09c84b238fa12b89509b285af99163a83ba
---

## 功能介绍

开发者可以调用DRM Kit的C/C++接口实现DRM证书管理、DRM许可证管理、DRM节目授权、DRM节目解密等数字版权保护功能。

DRM Kit提供MediaKeySystem实现DRM证书管理、DRM许可证管理功能，并管理MediaKeySession实例；MediaKeySession实现DRM节目授权，并可支持Media Kit或AVCodec Kit实现DRM节目解密以实现DRM节目播放。

## 开发步骤

详细的API说明请参考[Drm](../harmonyos-references/capi-drm.md)。

1. 导入DRM Kit接口。

   ```
   1. #include "multimedia/drm_framework/native_drm_common.h"
   2. #include "multimedia/drm_framework/native_drm_err.h"
   3. #include "multimedia/drm_framework/native_mediakeysession.h"
   4. #include "multimedia/drm_framework/native_mediakeysystem.h"
   ```
2. 在CMake脚本中链接动态库。

   ```
   1. target_link_libraries(PUBLIC libnative_drm.so)
   ```
3. 获取设备支持的DRM解决方案名称和唯一标识的列表。

   ```
   1. uint32_t count = 3; // count是当前设备实际支持的DRM插件的个数，用户根据实际情况设置。
   2. DRM_MediaKeySystemDescription descriptions[3];
   3. memset(descriptions, 0, sizeof(descriptions));
   4. Drm_ErrCode ret = OH_MediaKeySystem_GetMediaKeySystems(descriptions, &count);
   5. if (ret != DRM_ERR_OK) {
   6. printf("OH_MediaKeySystem_GetMediaKeySystems failed.");
   7. }
   ```
4. （可选）查询设备是否支持对应DRM解决方案名称、媒体类型、安全保护级别的DRM解决方案。

   ```
   1. bool isSupported = OH_MediaKeySystem_IsSupported3("com.wiseplay.drm", "video/mp4", CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
   2. if (isSupported != true) {
   3. printf("The device does not support the content protection level.");
   4. }
   ```
5. 创建MediaKeySystem实例。

   ```
   1. MediaKeySystem *mediaKeySystem = nullptr;
   2. ret = OH_MediaKeySystem_Create("com.wiseplay.drm", &mediaKeySystem);
   3. if (ret != DRM_ERR_OK || mediaKeySystem == nullptr) {
   4. printf("OH_MediaKeySystem_Create failed.");
   5. }
   ```
6. （可选）设置MediaKeySystem事件监听回调。

   ```
   1. static Drm_ErrCode SystemCallBackWithObj(MediaKeySystem *mediaKeySystem, DRM_EventType eventType,
   2. uint8_t *info, int32_t infoLen, char *extra)
   3. {
   4. printf("SystemCallBackWithObj enter");
   5. if (eventType == EVENT_PROVISION_REQUIRED) {
   6. // 设备DRM证书请求和处理。
   7. }
   8. return DRM_ERR_OK;
   9. }

   11. ret = OH_MediaKeySystem_SetCallback(mediaKeySystem, SystemCallBackWithObj);
   12. if (ret != DRM_ERR_OK) {
   13. printf("OH_MediaKeySystem_SetCallback failed.");
   14. }
   ```
7. （可选）获取设备DRM证书状态。

   ```
   1. DRM_CertificateStatus certStatus = CERT_STATUS_INVALID;
   2. // 检查设备DRM证书状态。
   3. ret = OH_MediaKeySystem_GetCertificateStatus(mediaKeySystem, &certStatus);
   4. if (ret == DRM_ERR_OK && certStatus != CERT_STATUS_PROVISIONED) {
   5. // 设备DRM证书请求和处理。
   6. }
   ```
8. （可选）生成设备DRM证书请求与处理设备DRM证书响应。

   ```
   1. #define MAX_DRM_PROVISION_BUF_SIZE 24576 // 24576: (2 * 12 * 1024)
   2. unsigned char request[MAX_DRM_PROVISION_BUF_SIZE] = { 0x00 };  // 设备DRM证书request最大长度为MAX_DRM_PROVISION_BUF_SIZE，按实际大小申请。
   3. int32_t requestLen = MAX_DRM_PROVISION_BUF_SIZE;
   4. // DRM服务URL的最大长度为2048。
   5. char defaultUrl[2048] = { 0x00 };
   6. int32_t defaultUrlLen = 2048;
   7. ret = OH_MediaKeySystem_GenerateKeySystemRequest(mediaKeySystem, request, &requestLen, defaultUrl,
   8. defaultUrlLen);
   9. if (ret != DRM_ERR_OK) {
   10. printf("OH_MediaKeySystem_GenerateKeySystemRequest failed.");
   11. }
   12. /*
   13. 应用通过网络请求，将设备DRM证书请求信息传到DRM服务获取设备DRM证书请求响应keySystemResponse，
   14. 再将设备DRM证书请求响应设置到设备上，请根据实际的数据和长度传入。
   15. */
   16. unsigned char keySystemResponse[MAX_DRM_PROVISION_BUF_SIZE] = {0x00};
   17. ret = OH_MediaKeySystem_ProcessKeySystemResponse(mediaKeySystem, keySystemResponse, sizeof(keySystemResponse));
   18. if (ret != DRM_ERR_OK) {
   19. printf("OH_MediaKeySystem_ProcessKeySystemResponse failed.");
   20. }
   ```
9. （可选）获取设备支持的最大内容保护级别。

   ```
   1. DRM_ContentProtectionLevel maxContentProtectionLevel = CONTENT_PROTECTION_LEVEL_UNKNOWN;
   2. ret = OH_MediaKeySystem_GetMaxContentProtectionLevel(mediaKeySystem, &maxContentProtectionLevel);
   3. if (ret != DRM_ERR_OK) {
   4. printf("OH_MediaKeySystem_GetMaxContentProtectionLevel failed.");
   5. }
   ```
10. 创建MediaKeySession实例。

    ```
    1. MediaKeySession *mediaKeySession = nullptr;
    2. DRM_ContentProtectionLevel contentProtectionLevel = CONTENT_PROTECTION_LEVEL_SW_CRYPTO; // 依据设备支持的内容保护级别设置。
    3. ret = OH_MediaKeySystem_CreateMediaKeySession(mediaKeySystem, &contentProtectionLevel, &mediaKeySession);
    4. if (ret != DRM_ERR_OK || mediaKeySession == nullptr) {
    5. printf("OH_MediaKeySystem_CreateMediaKeySession failed.");
    6. }
    ```
11. （可选）设置MediaKeySession事件监听回调。

    ```
    1. static Drm_ErrCode SessionEventCallBackWithObj(MediaKeySession *mediaKeySession, DRM_EventType eventType, uint8_t *info, int32_t infoLen, char *extra)
    2. {
    3. if (eventType == EVENT_KEY_REQUIRED) {
    4. // 媒体密钥请求与处理。
    5. }
    6. return DRM_ERR_OK;
    7. }

    9. static Drm_ErrCode SessionKeyChangeCallBackWithObj(MediaKeySession *mediaKeySession, DRM_KeysInfo *keysInfo, bool hasNewGoodKeys)
    10. {
    11. return DRM_ERR_OK;
    12. }

    14. OH_MediaKeySession_Callback sessionCallback = { SessionEventCallBackWithObj, SessionKeyChangeCallBackWithObj };
    15. ret = OH_MediaKeySession_SetCallback(mediaKeySession, &sessionCallback);
    16. if (ret != DRM_ERR_OK) {
    17. printf("OH_MediaKeySession_SetCallback failed.");
    18. }
    ```
12. （可选）查询是否需要安全解码。

    ```
    1. bool requireSecureDecoder;
    2. ret = OH_MediaKeySession_RequireSecureDecoderModule(mediaKeySession, "video/avc", &requireSecureDecoder);
    3. if (ret != DRM_ERR_OK) {
    4. printf("OH_MediaKeySession_RequireSecureDecoderModule failed.");
    5. }
    ```
13. 生成媒体密钥请求与处理媒体密钥响应，以请求许可证完成DRM节目授权。

    ```
    1. #define MAX_DRM_MEDIA_KEY_RESPONSE_BUF_SIZE 24576 // 24576: (2 * 12 * 1024)
    2. DRM_MediaKeyRequest mediaKeyRequest;
    3. DRM_MediaKeyRequestInfo info;
    4. // initData对应码流中的pssh数据，请按实际数据填入。
    5. unsigned char initData[512] = {0x00};
    6. memset(&info, 0, sizeof(DRM_MediaKeyRequestInfo));
    7. info.initDataLen = sizeof(initData);
    8. info.type = MEDIA_KEY_TYPE_ONLINE; // MEDIA_KEY_TYPE_ONLINE: 在线媒体密钥请求类型; MEDIA_KEY_TYPE_OFFLINE: 离线媒体密钥请求类型。
    9. memcpy(info.mimeType, (char *)"video/mp4", sizeof("video/mp4"));
    10. memcpy(info.initData, initData, sizeof(initData));
    11. memcpy(info.optionName[0], (char *)"optionalDataName", sizeof("optionalDataName"));
    12. memcpy(info.optionData[0], (char *)"optionalDataValue", sizeof("optionalDataValue"));
    13. info.optionsCount = 1;
    14. ret = OH_MediaKeySession_GenerateMediaKeyRequest(mediaKeySession, &info, &mediaKeyRequest);
    15. if (ret != DRM_ERR_OK) {
    16. printf("OH_MediaKeySession_GenerateMediaKeyRequest failed.");
    17. }
    18. /*
    19. 应用通过网络请求DRM服务，获取媒体密钥响应mediaKeyResponse，将响应传到OH_MediaKeySession_ProcessMediaKeyResponse，
    20. 若是离线媒体密钥响应处理，则返回离线媒体密钥标识mediaKeyId，请根据实际的数据和长度传入。
    21. */
    22. unsigned char mediaKeyId[128] = {0x00};
    23. int32_t mediaKeyIdLen = 128;
    24. // 媒体密钥响应长度最大为MAX_DRM_MEDIA_KEY_RESPONSE_BUF_SIZE，请按实际数据输入。
    25. unsigned char mediaKeyResponse[MAX_DRM_MEDIA_KEY_RESPONSE_BUF_SIZE] = {0x00};
    26. int32_t mediaKeyResponseLen = MAX_DRM_MEDIA_KEY_RESPONSE_BUF_SIZE;
    27. ret = OH_MediaKeySession_ProcessMediaKeyResponse(mediaKeySession, mediaKeyResponse,
    28. mediaKeyResponseLen, mediaKeyId, &mediaKeyIdLen);
    29. if (ret != DRM_ERR_OK) {
    30. printf("OH_MediaKeySession_ProcessMediaKeyResponse failed.");
    31. }
    ```
14. （可选）恢复离线媒体密钥。

    ```
    1. // 将指定媒体密钥标识的媒体密钥加载到当前会话。
    2. ret = OH_MediaKeySession_RestoreOfflineMediaKeys(mediaKeySession, mediaKeyId, mediaKeyIdLen);
    3. if (ret != DRM_ERR_OK) {
    4. printf("OH_MediaKeySession_RestoreOfflineMediaKeys failed.");
    5. }
    ```
15. （可选）检查媒体密钥状态。

    ```
    1. DRM_MediaKeyStatus mediaKeyStatus;
    2. ret = OH_MediaKeySession_CheckMediaKeyStatus(mediaKeySession, &mediaKeyStatus);
    3. if (ret != DRM_ERR_OK) {
    4. printf("OH_MediaKeySession_CheckMediaKeyStatus failed.");
    5. }
    ```
16. （可选）获取离线媒体密钥标识列表、获取离线媒体密钥状态与清除离线媒体密钥。

    ```
    1. DRM_OfflineMediakeyIdArray offlineMediaKeyIds;
    2. ret = OH_MediaKeySystem_GetOfflineMediaKeyIds(mediaKeySystem, &offlineMediaKeyIds);
    3. if (ret != DRM_ERR_OK) {
    4. printf("OH_MediaKeySystem_GetOfflineMediaKeyIds failed.");
    5. }
    6. DRM_OfflineMediaKeyStatus OfflineMediaKeyStatus = OFFLINE_MEDIA_KEY_STATUS_UNKNOWN;
    7. ret = OH_MediaKeySystem_GetOfflineMediaKeyStatus(mediaKeySystem, offlineMediaKeyIds.ids[0], offlineMediaKeyIds.idsLen[0], &OfflineMediaKeyStatus);
    8. if (ret != DRM_ERR_OK) {
    9. printf("OH_MediaKeySystem_GetOfflineMediaKeyStatus failed.");
    10. }
    11. ret = OH_MediaKeySystem_ClearOfflineMediaKeys(mediaKeySystem, offlineMediaKeyIds.ids[0], offlineMediaKeyIds.idsLen[0]);
    12. if (ret != DRM_ERR_OK) {
    13. printf("OH_MediaKeySystem_ClearOfflineMediaKeys failed.");
    14. }
    ```
17. 销毁MediaKeySession实例。

    ```
    1. ret = OH_MediaKeySession_Destroy(mediaKeySession);
    2. if (ret != DRM_ERR_OK) {
    3. printf("OH_MediaKeySession_Destroy failed.");
    4. }
    ```
18. 销毁MediaKeySystem实例。

    ```
    1. ret = OH_MediaKeySystem_Destroy(mediaKeySystem);
    2. if (ret != DRM_ERR_OK) {
    3. printf("OH_MediaKeySystem_Destroy failed.");
    4. }
    ```
