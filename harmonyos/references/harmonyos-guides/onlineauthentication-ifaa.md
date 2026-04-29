---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-ifaa
title: IFAA免密身份认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > IFAA免密身份认证
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9d84fcb356113094cfaeb03bc51e3e51d125a5e3b2976731a84703af5bb70c26
---

## 场景介绍

* 开通：提供移动端开通生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已有的生物特征类型进行开通，会开通移动端对应生物特征类型的IFAA免密身份认证能力。
* 认证：提供移动端认证生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征进行认证，认证成功；使用未开通的生物特征进行认证，认证失败。
* 注销：提供移动端注销生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征类型进行注销，会注销移动端对应生物特征类型的IFAA免密身份认证能力。

## 基本概念

互联网金融身份认证联盟（IIFAA），全称为International Internet Finance Authentication Alliance，是一个生物识别框架，它由IIFAA联盟推出并持续维护。

## 相关权限

获取生物识别权限：ohos.permission.ACCESS\_BIOMETRIC。

## 约束与限制

* 开发者应用已接入IIFAA联盟，可以从IIFAA中心服务器获取签名数据。
* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { userAuth } from '@kit.UserAuthenticationKit';

  4. try {
  5. // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
  6. userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
  7. console.info('current auth trust level is supported');
  8. } catch (error) {
  9. const err: BusinessError = error as BusinessError;
  10. console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
  11. }
  ```
* 移动端设备使用此服务时需要处于联网状态。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/qV8_dAzgSNek6bdWT8O-tw/zh-cn_image_0000002558764906.png?HW-CC-KV=V1&HW-CC-Date=20260429T053151Z&HW-CC-Expire=86400&HW-CC-Sign=17DDA2EC060D4F206181DB82528784F81C197888521A7A52BABE795F4D209BD9)

## 接口说明

**表1** 开通、认证、注销的所需要的接口

| 接口名 | 描述 |
| --- | --- |
| [register](../harmonyos-references/onlineauthentication-ifaa-api.md#register)(registerData: Uint8Array): Promise<Uint8Array> | 开通指定用户的指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。 |
| [auth](../harmonyos-references/onlineauthentication-ifaa-api.md#auth)(authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array> | 使用指定用户的生物信息类型进行IFAA免密身份认证。 |
| [deregisterSync](../harmonyos-references/onlineauthentication-ifaa-api.md#deregistersync)(deregisterData: Uint8Array): void | 注销指定用户指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。 |
| [getAnonymousIdSync](../harmonyos-references/onlineauthentication-ifaa-api.md#getanonymousidsync)(userToken: Uint8Array): Uint8Array | 获取移动端设备标识ID。 |

## 开发步骤

1. 注册IFAA免密身份认证。

   ```
   1. import { ifaa } from '@kit.OnlineAuthenticationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array, 再使用ifaa.getAnonymousIdSync接口。此处new Uint8Array([0])需要替换为开发者定义的用户标识。
   5. let arg = new Uint8Array([0]);
   6. let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);

   8. // 开发者需使用getAnonIdResult从服务端获取签名后的开通数据
   9. // 开发者将开通数据（IIFAA协议的TLV格式）转换为Uint8Array, 再使用ifaa.register接口。此处new Uint8Array([0])需要替换为有效数据。
   10. let TLV_Register_fp = new Uint8Array([0]);
   11. let registerPromise: Promise<Uint8Array> = ifaa.register(TLV_Register_fp);
   12. registerPromise.then(registerResult => {
   13. console.info("Succeeded in doing register.");
   14. // 开通成功，开发者获取ifaa.register结果并处理。
   15. }).catch((err: BusinessError) =>{
   16. console.error(`Failed to call register. Code: ${err.code}, message: ${err.message}`);
   17. // 开通失败，开发者获取ifaa.register错误并处理。
   18. });
   ```
2. 使用IFAA免密身份认证进行认证。

   ```
   1. import { ifaa } from '@kit.OnlineAuthenticationKit';
   2. import { userAuth } from '@kit.UserAuthenticationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array, 再使用ifaa.getAnonymousIdSync接口。arg需要替换开发者自定义数据。
   6. let arg = new Uint8Array([0]);
   7. let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);

   9. // 开发者需使用getAnonIdResult从服务端获取签名后的认证数据

   11. // 获取此次免密支付的challenge
   12. let ifaaChallenge: Uint8Array = ifaa.preAuthSync();
   13. let authParam: userAuth.AuthParam = {
   14. challenge: ifaaChallenge,
   15. authType: [userAuth.UserAuthType.FINGERPRINT],
   16. authTrustLevel: userAuth.AuthTrustLevel.ATL4,
   17. };
   18. // 使用preAuthResult请求身份认证
   19. let userAuthInstance = userAuth.getUserAuthInstance(authParam,  {title: ' '});
   20. userAuthInstance.on('result', {
   21. async onResult (result) {
   22. let authToken = result.token;
   23. try {
   24. // 生物特征认证成功后，调用IFAA认证
   25. console.info("IFAA auth start");
   26. // 开发者将认证数据（IIFAA协议的TLV格式）转换为Uint8Array, 再使用ifaa.auth接口。此处new Uint8Array([0])需要替换为有效数据。
   27. let TLV_Auth_fp = new Uint8Array([0]);
   28. // 开发者根据业务需求选择同步/异步接口
   29. let authResult: Uint8Array = ifaa.authSync(authToken, TLV_Auth_fp);
   30. console.info("authSyn authResult" + authResult);
   31. // 开发者处理authResult
   32. } catch (error) {
   33. const err: BusinessError = error as BusinessError;
   34. console.error(`Failed to call auth. Code is ${err.code}, message is ${err.message}`);
   35. }
   36. }
   37. });
   38. userAuthInstance.start();
   ```
3. 注销IFAA免密身份认证。

   ```
   1. import { ifaa } from '@kit.OnlineAuthenticationKit'

   3. // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array, 再使用ifaa.getAnonymousIdSync接口。此处new Uint8Array([0])需要替换为开发者定义的用户标识。
   4. let arg = new Uint8Array([0]);
   5. let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);

   7. // 开发者需使用getAnonymousId的结果从服务端获取签名后的注销数据
   8. // 开发者将注销数据（IIFAA协议的TLV格式）转换为Uint8Array, 再使用ifaa.deregisterSync接口。此处new Uint8Array([0])需要替换为有效数据。
   9. let TLV_deregister_fp = new Uint8Array([0]);
   10. ifaa.deregisterSync(TLV_deregister_fp);
   ```

## 常见问题

现象描述：开通IFAA免密身份认证失败。

可能原因：移动端设备没有联网。

处理步骤：移动端设备连接WIFI或热点，再次尝试。
