---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-securecamera
title: 安全摄像头场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 可信应用服务 > 安全摄像头场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38145694b87cccc88457cafc6755961012d696f7432bdb802a373368fbd89727
---

## 场景介绍

在安全摄像头场景中，通过创建证明密钥、打开证明会话的方式，对安全摄像头捕捉到的图像数据进行签名，确保图像数据的真实性和完整性。

## 约束与限制

该特性需要设备支持安全摄像头功能。

开发者可以通过调用[getSupportedSceneModes](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedscenemodes11)方法，当返回值为camera.SceneMode.SECURE\_PHOTO，当前设备支持安全摄像头，返回其他值表示当前设备不支持安全摄像头。具体判断方法参考如下示例：

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // 获得安全摄像头
4. function getSecureCameraDevice(cameraManager: camera.CameraManager): camera.CameraDevice {
5. // 获得设备支持的摄像头列表
6. const cameraDevices = cameraManager.getSupportedCameras();
7. if (cameraDevices.length < 1) {
8. throw new Error('no camera devices');
9. }
10. // 获取前置镜头对象。当前安全摄像头仅支持前置镜头。
11. const frontCamera: camera.CameraDevice | undefined = cameraDevices.find((profile: camera.CameraDevice) => {
12. return profile.cameraPosition != camera.CameraPosition.CAMERA_POSITION_BACK;
13. });
14. if (frontCamera === undefined) {
15. throw new Error('no front cameras');
16. }
17. // 检查前置摄像头设备是否支持安全模式；若支持，即可使用该前置摄像头做后续安全摄像头操作。
18. const modes = cameraManager.getSupportedSceneModes(frontCamera);
19. if (modes.indexOf(camera.SceneMode.SECURE_PHOTO) === -1) {
20. throw new Error('current device not support secure camera');
21. }
22. return frontCamera;
23. }
```

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/l2EKIj6eSrS7jpi9eE0p2w/zh-cn_image_0000002552798738.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234254Z&HW-CC-Expire=86400&HW-CC-Sign=15D0CE304AC5D05076FB2C183D123C75231BBCB01E3113D5ABB99AC7D7A8406F)

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

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { trustedAppService } from '@kit.DeviceSecurityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 参考[安全相机开发指导](camera-secure-photo.md)，初始化安全相机。

   开发者需要完成：

   * 选择支持安全相机的设备。
   * 查询相机设备在安全模式下支持的输出能力。
   * 创建设备输入输出。
   * 打开安全设备（安全摄像头），并获取安全设备序列号。
3. 创建证明密钥和初始化证明会话。

   说明

   * 只有创建证明密钥成功后，才能初始化证明会话。
   * 证明密钥的有效期为7天，为了避免反复创建证明密钥，建议先调用初始化证明会话，如果初始化失败，再去销毁、创建证明密钥，然后重新初始化证明密钥。
   * 每次打开安全摄像头都需要获取设备序列号，只有初始化安全相机证明会话时需要传入有效值，其他场景传“0”即可。
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
   16. const userData = "trusted_app_service_demo"; // 示例值，实际值请自行生成，长度在16到127Bytes之间
   17. const deviceId = 7483679320805398131; // 示例值，实际值请通过Camera Kit获取
   18. const initProperties: Array<trustedAppService.AttestParam> = [
   19. {
   20. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
   21. value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
   22. },
   23. {
   24. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
   25. value: BigInt(deviceId)
   26. }
   27. ];
   28. const initOptions: trustedAppService.AttestOptions = {
   29. properties: initProperties
   30. };
   31. // 创建证明密钥并打开证明会话
   32. let certChainList: Array<string>;
   33. try {
   34. await trustedAppService.createAttestKey(createOptions);
   35. const result = await trustedAppService.initializeAttestContext(userData, initOptions);
   36. certChainList = result.certChains;
   37. } catch (err) {
   38. const error = err as BusinessError;
   39. console.error(`Failed to initialize attest context, message:${error.message}, code:${error.code}`);
   40. }
   ```
4. 参考[安全相机开发指导](camera-secure-photo.md)，完成安全相机会话的创建，配置输入、输出流，启动预览流和安全数据流。
5. 结束证明会话。

   ```
   1. // 结束证明会话的参数
   2. const finalProperties: Array<trustedAppService.AttestParam> = [
   3. {
   4. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
   5. value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
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

   如果需要销毁证明密钥，请在结束证明会话后，调用[destroyAttestKey](../harmonyos-references/devicesecurity-taas-api.md#destroyattestkey)接口。由于安全摄像头、安全地理位置和安全图像压缩、裁剪共用同一个证明密钥，销毁前需要保证安全地理位置功能未在使用该证明密钥。
