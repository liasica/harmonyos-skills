---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-secimage-process
title: 安全图像压缩、裁剪场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 可信应用服务 > 安全图像压缩、裁剪场景
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1d2fc2d1be16d6bdb4cecb1bfd445cb1a06754f51b8146c8f7d1174fea28d6f8
---

## 场景介绍

在安全图像支持压缩、裁剪场景中，通过创建证明密钥、打开证明会话的方式，对从[安全摄像头](devicesecurity-taas-securecamera.md)获取的图像数据进行压缩、裁剪处理并重新签名，降低安全摄像头的原始图像大小，同时也能确保图像数据的真实性和完整性。

## 约束与限制

该特性需要设备支持安全摄像头功能，其支持的设备范围与安全摄像头场景保持一致。开发者可以参考安全摄像头场景的[约束与限制](devicesecurity-taas-securecamera.md#约束与限制)，判断设备是否支持安全摄像头。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/nwgFN0yKT_CZf8rMCgn0vA/zh-cn_image_0000002712244528.jpg)

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

1. 导入trustedAppService模块和相关依赖模块。

   ```typescript
   import { trustedAppService } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import hilog from '@ohos.hilog';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { util } from '@kit.ArkTS';
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 参考[安全摄像头开发指导](devicesecurity-taas-securecamera.md)，获取安全图像。
3. 创建证明密钥和初始化证明会话。

   **说明** 

   * 只有创建证明密钥成功后，才能初始化证明会话。
   * 证明密钥的有效期为7天，为了避免反复创建证明密钥，建议先调用初始化证明会话，如果初始化失败，再去销毁、创建证明密钥，然后重新初始化证明密钥。
   * 调用initializeAttestContext初始化证明会话时，userData的长度必须在16到127 Bytes之间。

   * 创建安全图像压缩、裁剪场景的证明密钥：

     ```typescript
     private async creatSecureImageProcAttestKey(): Promise<void> {
       // 创建证明密钥的参数
       const createProperties: Array<trustedAppService.AttestParam> = [
         {
           tag: trustedAppService.AttestTag.ATTEST_TAG_ALGORITHM,
           value: trustedAppService.AttestKeyAlg.ATTEST_ALG_ECC
         },
         {
           tag: trustedAppService.AttestTag.ATTEST_TAG_KEY_SIZE,
           value: trustedAppService.AttestKeySize.ATTEST_ECC_KEY_SIZE_256
         }
       ];
       const createOptions: trustedAppService.AttestOptions = {
         properties: createProperties
       };
       // 创建证明密钥
       try {
         await trustedAppService.createAttestKey(createOptions);
         hilog.info(0x0000, 'TrustedAppService', 'createAttestKey successfully');
       } catch (error) {
         const err = error as BusinessError;
         hilog.error(0x0000, 'trustedappservice', `createattestkey failed, errCode: ${err.code}, errMsg: ${err.message}`);
         throw new Error(err.message);
       }
     }
     ```
   * 初始化安全图像压缩、裁剪场景的证明会话：

     ```typescript
     private async initSecureImageProcAttestContext(): Promise<number> {
       try {
         // 初始化证明会话的参数
         const deviceId = 0;
         const initProperties: Array<trustedAppService.AttestParam> = [
           {
             tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
             value: trustedAppService.AttestType.ATTEST_TYPE_SECIMAGE_PROCESS
           },
           {
             tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
             value: BigInt(deviceId) // 此参数在安全图像压缩、裁剪场景下不生效
           }
         ];
         const initOptions: trustedAppService.AttestOptions = {
           properties: initProperties
         };
         let userData = 'trusted_app_service_default_userdata'; // 示例值，实际值请自行生成，长度在16到127 Bytes之间
         // 初始化话证明会话
         const certChainResult = await trustedAppService.initializeAttestContext(userData, initOptions);
         if (certChainResult.certChains.length < 1) {
           throw new Error('empty returned cert chain');
         }
         // ...
         return 0;
       } catch (err) {
         const businessError = err as BusinessError;
         hilog.error(0x0000, 'TrustedAppService',
           `initializeAttestContext failed. errCode: ${businessError.code}, errMsg: ${businessError.message}`);
         const finalNumericCode = Number(String(businessError.code ?? '').replace('n', '').trim());
         return Number.isNaN(finalNumericCode) ? -1 : finalNumericCode;
       }
     }
     ```
4. 请求对安全图像进行压缩、裁剪处理

   * 以压缩场景为例：

     ```typescript
     private async procSecImageCompression(compressQuality: number, srcSecureImage: ArrayBuffer): Promise<ArrayBuffer> {
       try {
         let properties: Array<trustedAppService.SecImageProcParams> = [
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
             value: trustedAppService.SecImageProcOperation.SECIMAGE_COMPRESSION,
           },
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
             value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
           },
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
             value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_JPEG, // 安全图像压缩命令返回的图像格式为：JPEG 格式
           },
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_COMPRESSION_QUALITY,
             value: compressQuality, // 实际使用请替换为业务场景需要的压缩质量
           },
         ];
         const procParams: trustedAppService.SecImageProcParamsArray = {
           properties: properties
         };
         // srcSecureImage：实际使用请替换为Camera Kit获取到的安全图像buffer
         return (await trustedAppService.procSecImageTransform(srcSecureImage, procParams)).secImage;
       } catch (err) {
         const businessError = err as BusinessError;
         hilog.error(0x0000, 'TrustedAppService',
           `procSecImageTransform failed, code: ${businessError.code}, msg: ${businessError.message}`);
         throw new Error(businessError.message);
       }
     }
     ```
   * 以裁剪场景为例：

     ```typescript
     private async procSecImageCropping(cropRegion: trustedAppService.CropRegion,
       srcSecureImage: ArrayBuffer): Promise<ArrayBuffer> {
       try {
         let properties: Array<trustedAppService.SecImageProcParams> = [
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
             value: trustedAppService.SecImageProcOperation.SECIMAGE_CROPPING,
           },
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
             value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
           },
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
             value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像裁剪命令返回的图像格式为：YUV420 NV21 格式
           },
           {
             tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_CROP_REGION,
             value: {
               // 实际使用请替换为业务场景需要的裁剪区域范围
               x: cropRegion.x,
               y: cropRegion.y,
               width: cropRegion.width,
               height: cropRegion.height
             },
           },
         ];
         let procParams: trustedAppService.SecImageProcParamsArray = {
           properties: properties,
         };
         // srcSecureImage：实际使用请替换为Camera Kit获取到的安全图像buffer
         return (await trustedAppService.procSecImageTransform(srcSecureImage, procParams)).secImage;
       } catch (err) {
         const businessError = err as BusinessError;
         hilog.error(0x0000, 'TrustedAppService',
           `procSecImageTransform failed, code: ${businessError.code}, msg: ${businessError.message}`);
         throw new Error(businessError.message);
       }
     }
     ```
5. 结束证明会话。

   ```typescript
   private async finalizeSecureImageProcAttestContext(): Promise<void> {
     // 结束证明会话的参数
     const finalProperties: Array<trustedAppService.AttestParam> = [
       {
         tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
         value: trustedAppService.AttestType.ATTEST_TYPE_SECIMAGE_PROCESS
       }
     ];
     const finalOptions: trustedAppService.AttestOptions = {
       properties: finalProperties,
     };
     // 结束证明会话
     try {
       await trustedAppService.finalizeAttestContext(finalOptions);
     } catch (err) {
       const error = err as BusinessError;
       hilog.error(0x0000, 'TrustedAppService',
         'Failed to finalize attest context, code:${error.code}, message:${error.message}');
     }
   }
   ```

   如果需要销毁证明密钥，请在结束证明会话后，调用[destroyAttestKey](../harmonyos-references/devicesecurity-taas-api.md#destroyattestkey)接口。由于安全摄像头、安全地理位置和安全图像压缩、裁剪共用同一个证明密钥，销毁前需要保证其余场景功能未在使用该证明密钥。
