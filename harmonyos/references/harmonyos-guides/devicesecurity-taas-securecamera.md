---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-securecamera
title: 安全摄像头场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 可信应用服务 > 安全摄像头场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:40f111861779d3d9a0433a89b2378b3ee00a28f70d98a037503a282e35003aa9
---

## 场景介绍

在安全摄像头场景中，通过创建证明密钥、打开证明会话的方式，对安全摄像头捕捉到的图像数据进行签名，确保图像数据的真实性和完整性。

## 约束与限制

该特性需要设备支持安全摄像头功能。

开发者可以通过调用[getSupportedSceneModes](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedscenemodes11)方法，当返回值为camera.SceneMode.SECURE\_PHOTO，当前设备支持安全摄像头，返回其他值表示当前设备不支持安全摄像头。具体判断方法参考如下示例：

```typescript
private getSecureCameraDevice(cameraManager: camera.CameraManager): camera.CameraDevice {
  // 获得设备支持的摄像头列表
  const cameraDevices = cameraManager.getSupportedCameras();
  if (cameraDevices.length < 1) {
    throw new Error('no camera devices');
  }
  // 获取前置镜头对象。当前安全摄像头仅支持前置镜头。
  const frontCamera: camera.CameraDevice | undefined = cameraDevices.find((profile: camera.CameraDevice) => {
    return profile.cameraPosition != camera.CameraPosition.CAMERA_POSITION_BACK;
  });
  if (frontCamera === undefined) {
    throw new Error('no front cameras');
  }
  // 检查前置摄像头设备是否支持安全模式；若支持，即可使用该前置摄像头做后续安全摄像头操作。
  const modes = cameraManager.getSupportedSceneModes(frontCamera);
  if (modes.indexOf(camera.SceneMode.SECURE_PHOTO) === -1) {
    throw new Error('current device not support secure camera');
  }
  return frontCamera;
}
```

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/7Z1XvgvmTvq_ayfGhsYkSQ/zh-cn_image_0000002706674354.jpg)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-taas-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [createAttestKey](../harmonyos-references/devicesecurity-taas-api.md#createattestkey)(options: AttestOptions): Promise<void> | 创建证明密钥。 |
| [initializeAttestContext](../harmonyos-references/devicesecurity-taas-api.md#initializeattestcontext)(userData: string, options: AttestOptions): Promise<AttestReturnResult> | 初始化证明会话。 |
| [finalizeAttestContext](../harmonyos-references/devicesecurity-taas-api.md#finalizeattestcontext)(options: AttestOptions): Promise<void> | 结束证明会话。 |
| [destroyAttestKey](../harmonyos-references/devicesecurity-taas-api.md#destroyattestkey)(): Promise<void> | 销毁证明密钥。 |

## 开发步骤

1. 导入camera模块、trustedAppService模块和相关依赖模块。

   ```typescript
   import { camera } from '@kit.CameraKit';
   import { trustedAppService } from '@kit.DeviceSecurityKit';
   import { image } from '@kit.ImageKit';
   import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
   import hilog from '@ohos.hilog';
   import { common } from '@kit.AbilityKit';
   import { util } from '@kit.ArkTS';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 参考[安全相机开发指导](camera-secure-photo.md)，初始化安全相机。

   开发者需要完成：

   * 选择支持安全相机的设备。
   * 查询相机设备在安全模式下支持的输出能力。
   * 创建设备输入输出。
   * 打开安全设备（安全摄像头），并获取安全设备序列号。
3. 创建证明密钥和初始化证明会话。

   **说明** 

   * 只有创建证明密钥成功后，才能初始化证明会话。
   * 证明密钥的有效期为7天，为了避免反复创建证明密钥，建议先调用初始化证明会话，如果初始化失败，再去销毁、创建证明密钥，然后重新初始化证明密钥。
   * 每次打开安全摄像头都需要获取设备序列号，只有初始化安全相机证明会话时需要传入有效值，其他场景传“0”即可。
   * 调用initializeAttestContext初始化证明会话时，userData的长度必须在16到127 Bytes之间。

   * 创建安全相机场景的证明密钥：

     ```typescript
     private async creatSecureCameraAttestKey(): Promise<void> {
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
   * 初始化安全相机场景的证明会话：

     ```typescript
     private async initSecureCameraAttestContext(cameraInput: camera.CameraInput): Promise<number> {
       try {
         // 初始化证明会话的参数
         const deviceId = await cameraInput.open(true);
         const initProperties: Array<trustedAppService.AttestParam> = [
           {
             tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
             value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
           },
           {
             tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
             value: BigInt(deviceId) // 实际值请通过Camera Kit获取
           }
         ];
         const initOptions: trustedAppService.AttestOptions = {
           properties: initProperties
         };
         let userData = 'trusted_app_service_default_userdata'; // 示例值，实际值请自行生成，长度在16到127 Bytes之间
         // 初始化证明会话
         const certChainResult = await trustedAppService.initializeAttestContext(userData, initOptions);
         if (certChainResult.certChains.length < 1) {
           throw new Error('empty returned cert chain');
         }
         // ...
         return 0;
       } catch (err) {
         const businessError = err as BusinessError;
         hilog.error(0x0000, 'TrustedAppService',
           `initializeAttestContext failed. errCode: ${businessError.code}, message: ${businessError.message}`);
         const finalNumericCode = Number(String(businessError.code ?? '').replace('n', '').trim());
         return Number.isNaN(finalNumericCode) ? -1 : finalNumericCode;
       }
     }
     ```
4. 参考[安全相机开发指导](camera-secure-photo.md)，完成安全相机会话的创建，配置输入、输出流，启动预览流和安全数据流。
5. 结束证明会话。

   ```typescript
   private async finalizeSecureCameraAttestContext(): Promise<void> {
     // 结束证明会话的参数
     const finalProperties: Array<trustedAppService.AttestParam> = [
       {
         tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
         value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
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

   如果需要销毁证明密钥，请在结束证明会话后，调用[destroyAttestKey](../harmonyos-references/devicesecurity-taas-api.md#destroyattestkey)接口。由于安全摄像头、安全地理位置和安全图像压缩、裁剪共用同一个证明密钥，销毁前需要保证其余功能未在使用该证明密钥。
