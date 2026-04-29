---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-secimage-process
title: 安全图像压缩、裁剪场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 可信应用服务 > 安全图像压缩、裁剪场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:463f8744ffb233472c34d6a1e6a2408fdc70e967241c2648aee558427fb3130c
---

## 场景介绍

在安全图像支持压缩、裁剪场景中，通过创建证明密钥、打开证明会话的方式，对从[安全摄像头](devicesecurity-taas-securecamera.md)获取的图像数据进行压缩、裁剪处理并重新签名，降低安全摄像头的原始图像大小，同时也能确保图像数据的真实性和完整性。

## 约束与限制

该特性需要设备支持安全摄像头功能，其支持的设备范围与安全摄像头场景保持一致。开发者可以参考安全摄像头场景的[约束与限制](devicesecurity-taas-securecamera.md#约束与限制)，判断设备是否支持安全摄像头。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/y1UcAYIeT9iTP01JswFSXQ/zh-cn_image_0000002589324755.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053130Z&HW-CC-Expire=86400&HW-CC-Sign=C7D33E98A9329EC2B3CD8E337AE69F3491279CFAAC583AA9003908995418DEF0)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-taas-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [createAttestKey](../harmonyos-references/devicesecurity-taas-api.md#createattestkey)(options: AttestOptions): Promise<void> | 创建证明密钥。 |
| [initializeAttestContext](../harmonyos-references/devicesecurity-taas-api.md#initializeattestcontext)(userData: string, options: AttestOptions): Promise<AttestReturnResult> | 初始化证明会话。 |
| [finalizeAttestContext](../harmonyos-references/devicesecurity-taas-api.md#finalizeattestcontext)(options: AttestOptions): Promise<void> | 结束证明会话。 |
| [destroyAttestKey](../harmonyos-references/devicesecurity-taas-api.md#destroyattestkey)(): Promise<void> | 销毁证明密钥。 |
| [procSecImageTransform](../harmonyos-references/devicesecurity-taas-api.md#procsecimagetransform)(srcSecImage: ArrayBuffer, Options: SecImageProcOptions): Promise<SecImageBuffer> | 处理安全图像压缩、裁剪操作。 |

## 开发步骤

1. 参考[安全摄像头开发指导](devicesecurity-taas-securecamera.md)，获取安全图像。
2. 创建证明密钥和初始化证明会话。

   说明

   * 只有创建证明密钥成功后，才能初始化证明会话。
   * 证明密钥的有效期为7天，为了避免反复创建证明密钥，建议先调用初始化证明会话，如果初始化失败，再去销毁、创建证明密钥，然后重新初始化证明密钥。
   * 调用initializeAttestContext初始化证明会话时，userData的长度必须在16到127 Bytes之间。

   ```
   1. // 创建证明密钥的参数
   2. const createProperties: Array<trustedAppService.AttestParam> = [
   3. {
   4. tag: trustedAppService.AttestTag.ATTEST_TAG_ALGORITHM,
   5. value: trustedAppService.AttestKeyAlg.ATTEST_ALG_ECC
   6. },
   7. {
   8. tag: trustedAppService.AttestTag.ATTEST_TAG_KEY_SIZE,
   9. value: trustedAppService.AttestKeySize.ATTEST_ECC_KEY_SIZE_256
   10. }
   11. ];
   12. const createOptions: trustedAppService.AttestOptions = {
   13. properties: createProperties
   14. };
   15. // 初始化证明会话的参数
   16. const userData = "trusted_app_service_demo"; // 示例值，实际值请自行生成，长度在16到127 Bytes之间
   17. const initProperties: Array<trustedAppService.AttestParam> = [
   18. {
   19. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
   20. value: trustedAppService.AttestType.ATTEST_TYPE_SECIMAGE_PROCESS
   21. },
   22. {
   23. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
   24. value: BigInt(0) // 此参数在安全图像压缩、裁剪场景下不生效
   25. }
   26. ];
   27. const initOptions: trustedAppService.AttestOptions = {
   28. properties: initProperties
   29. };

   31. let certChainList: Array<string>;
   32. try {
   33. // 创建证明密钥
   34. await trustedAppService.createAttestKey(createOptions);
   35. // 初始化证明会话
   36. const result = await trustedAppService.initializeAttestContext(userData, initOptions);
   37. certChainList = result.certChains;
   38. } catch (err) {
   39. const error = err as BusinessError;
   40. console.error(`Failed to initialize attest context, message:${error.message}, code:${error.code}`);
   41. }
   ```
3. 请求对安全图像进行压缩、裁剪处理

   * 以压缩场景为例：

     ```
     1. const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

     3. let properties: Array<trustedAppService.SecImageProcParams> = [
     4. {
     5. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
     6. value: trustedAppService.SecImageProcOperation.SECIMAGE_COMPRESSION,
     7. },
     8. {
     9. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
     10. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
     11. },
     12. {
     13. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
     14. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_JPEG, // 安全图像压缩命令返回的图像格式为：JPEG 格式
     15. },
     16. {
     17. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_COMPRESSION_QUALITY,
     18. value: 90, // 实际使用请替换为业务场景需要的压缩质量
     19. },
     20. ];
     21. let procParams: trustedAppService.SecImageProcParamsArray = {
     22. properties: properties,
     23. };
     24. await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
     25. (returnResult: trustedAppService.SecImageBuffer): void => {
     26. let returnSecImageBuffer = returnResult.secImage;
     27. }
     28. ).catch(
     29. (error: BusinessError): void => {
     30. let err = error as BusinessError;
     31. hilog.error(0x0000, 'testTag', `Failed to process secureImage cropping, code:${err.code}, message:${err.message}`);
     32. }
     33. );
     ```
   * 以裁剪场景为例：

     ```
     1. const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

     3. let properties: Array<trustedAppService.SecImageProcParams> = [
     4. {
     5. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
     6. value: trustedAppService.SecImageProcOperation.SECIMAGE_CROPPING,
     7. },
     8. {
     9. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
     10. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
     11. },
     12. {
     13. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
     14. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像裁剪命令返回的图像格式为：YUV420 NV21 格式
     15. },
     16. {
     17. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_CROP_REGION,
     18. value: { x : 0, y ： 0, width : 320, height : 240 }, // 实际使用请替换为业务场景需要的裁剪区域范围
     19. },
     20. ];
     21. let procParams: trustedAppService.SecImageProcParamsArray = {
     22. properties: properties,
     23. };
     24. await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
     25. (returnResult: trustedAppService.SecImageBuffer): void => {
     26. let returnSecImageBuffer = returnResult.secImage;
     27. }
     28. ).catch(
     29. (error: BusinessError): void => {
     30. let err = error as BusinessError;
     31. hilog.error(0x0000, 'testTag', `Failed to process secureImage cropping, code:${err.code}, message:${err.message}`);
     32. }
     33. );
     ```
4. 结束证明会话。

   ```
   1. // 结束证明会话的参数
   2. const finalProperties: Array<trustedAppService.AttestParam> = [
   3. {
   4. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
   5. value: trustedAppService.AttestType.ATTEST_TYPE_SECIMAGE_PROCESS
   6. }
   7. ];
   8. const finalOptions: trustedAppService.AttestOptions = {
   9. properties: finalProperties,
   10. };
   11. // 结束证明会话
   12. try {
   13. await trustedAppService.finalizeAttestContext(finalOptions);
   14. } catch (err) {
   15. const error = err as BusinessError;
   16. console.error(`Failed to finalize attest context, message:${error.message}, code:${error.code}`);
   17. }
   ```

   如果需要销毁证明密钥，请在结束证明会话后，调用[destroyAttestKey](../harmonyos-references/devicesecurity-taas-api.md#destroyattestkey)接口。由于安全摄像头、安全地理位置和安全图像压缩、裁剪共用同一个证明密钥，销毁前需要保证其余场景功能未在使用该证明密钥。
