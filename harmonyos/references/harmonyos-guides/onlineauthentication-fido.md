---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-fido
title: FIDO免密身份认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > FIDO免密身份认证
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0e1fa70a79bbcb406e6371f0bf6ecc9c48dcc0e476392d968a052d17edcd27d6
---

## 场景介绍

* 开通FIDO免密身份认证功能，使用用户已有的生物特征开通FIDO免密身份认证能力。
* 使用FIDO免密身份认证功能，使用用户已开通的生物特征进行FIDO免密身份认证。
* 关闭FIDO免密身份认证功能，使用用户已开通的生物特征注销FIDO免密身份认证能力。

## 基本概念

在开发FIDO免密身份认证功能前，开发者应了解以下基本概念：

* FIDO协议

  FIDO（Fast Identity Online）是一套身份认证框架协议，它由FIDO联盟推出并持续维护。FIDO规范定义了一套在线身份认证的技术架构。
* UAF身份认证框架

  UAF（Universal Authentication Framework）意为通用身份认证框架，目的是通过生物识别（如指纹识别）和加密技术方式，为用户提供无密码的身份认证体验。

## 相关权限

获取生物识别权限：ohos.permission.ACCESS\_BIOMETRIC。

## 约束与限制

需满足以下条件，才能使用该功能。

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
* FIDO服务需要联网，以便提供完整的在线身份校验服务。应用在调用本服务API前，需将FIDO服务联网行为向用户明示，并且取得用户同意。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/tWYcHI6PQRWVCZVJksrVdQ/zh-cn_image_0000002583478407.png?HW-CC-KV=V1&HW-CC-Date=20260427T234309Z&HW-CC-Expire=86400&HW-CC-Sign=0A1640CC55BCAFBAB3570B16DA0040C930A864EFFB3412D41C05E21374778840)

## 接口说明

业务进行FIDO免密身份认证功能的开通、使用和关闭。

**表1** FIDO免密身份认证接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| [discover](../harmonyos-references/onlineauthentication-fido-api.md#discover)(context: common.Context): Promise<[DiscoveryData](../harmonyos-references/onlineauthentication-fido-api.md#discoverydata)> | 发现设备的认证能力，返回当前设备软件支持的认证器数据。 |
| [checkPolicy](../harmonyos-references/onlineauthentication-fido-api.md#checkpolicy)(context: common.Context, uafRequest: [UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)): Promise<void> | 检测用户策略的开启状态。 |
| [processUAFOperation](../harmonyos-references/onlineauthentication-fido-api.md#processuafoperation)(context: common.Context, uafRequest: [UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage), channelBindings?: [ChannelBinding](../harmonyos-references/onlineauthentication-fido-api.md#channelbinding)): Promise<[UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)> | 用户UAF操作接口，处理UAF协议消息。 |
| [notifyUAFResult](../harmonyos-references/onlineauthentication-fido-api.md#notifyuafresult)(context: common.Context, uafResponse: [UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)): Promise<void> | 开通结果通知接口。 |

## 开发步骤

1. 需要业务方自行根据FIDO标准协议部署FIDO服务器。
2. 导入相关模块。

   ```
   1. import { fido } from '@kit.OnlineAuthenticationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. 开通FIDO免密身份认证。

   1. 初始化认证器信息。

      ```
      1. @Entry
      2. @Component
      3. struct FidoInvokePage {
      4. private uiContext = this.getUIContext().getHostContext();

      6. private async invokeDiscover() {
      7. try {
      8. // 初始化认证器信息
      9. let discoverData = await fido.discover(this.uiContext);
      10. // 业务处理discoverData
      11. } catch (error) {
      12. const err: BusinessError = error as BusinessError;
      13. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
      14. // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
      15. }
      16. }

      18. build() {
      19. // 业务UI界面
      20. }
      21. }
      ```
   2. 访问FIDO服务端，获取策略检查报文，检查用户开通状态。

      ```
      1. // uafMessage为FIDO服务端获取的策略检查报文
      2. let uafAuthMessage: fido.UAFMessage = {
      3. /*
      4. * 策略检查报文格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"","serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":[[{"aaid":["001B#1001"],"keyIDs":["test keyIDs"],"authenticationAlgorithms":[1]}]]}}]
      5. */
      6. uafProtocolMessage: uafMessage, // 从服务端获取的检查策略报文
      7. additionalData: "" // 附加信息（可选）
      8. };
      9. let isRegistered: boolean = true;
      10. try {
      11. // 检查是否已经开启FIDO认证
      12. await fido.checkPolicy(this.uiContext, uafAuthMessage);
      13. } catch (error) {
      14. isRegistered = false;
      15. const err: BusinessError = error as BusinessError;
      16. console.error(`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}`);
      17. // 业务根据错误码判断状态，进行相应处理
      18. }
      19. if (isRegistered) {
      20. console.info("has registered, no need to register again.");
      21. // 已注册，业务根据需要执行后续流程
      22. }
      ```
   3. 访问FIDO服务端，获取注册报文，调用processUAFOperation接口进行FIDO注册。

      ```
      1. // regMessage为从FIDO服务端获取的注册报文
      2. let uafRegMessage: fido.UAFMessage = {
      3. /*
      4. * 注册报文格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Reg","appID":"","serverData":"test server data"},"challenge":"test challenge","username":"test user name","policy":{"accepted":[[{"aaid":["001B#1001"],"attachmentHint":1,"authenticationAlgorithms":[1],"authenticatorVersion":1}]]}}]
      5. */
      6. uafProtocolMessage: regMessage, // 从服务端获取的注册报文
      7. additionalData: "" // 附加信息（可选）
      8. };
      9. // 传递通道绑定参数（可选）
      10. let channelBinding: fido.ChannelBinding = {};
      11. try {
      12. // 调用processUAFOperation接口进行FIDO注册
      13. let messageResp = await fido.processUAFOperation(this.uiContext, uafRegMessage, channelBinding);
      14. } catch (error) {
      15. const err: BusinessError = error as BusinessError;
      16. console.error(`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}`);
      17. // 业务根据错误码判断异常类型，进行相应处理
      18. }
      ```
   4. 发送注册响应报文至FIDO服务端进行验证并获取注册结果报文。

      ```
      1. // notifyMessage为从FIDO服务端获取的注册结果报文
      2. let notifyMessage:string = "";
      3. let notifyUafMessage: fido.UAFMessage = {
      4. /*
      5. * 响应报文格式: {"authenticatorsSucceeded":[{"description":"Attention completed successfully.","aaid":"001B#1001","keyID":"test keyID"}]}
      6. */
      7. uafProtocolMessage: notifyMessage, // 从服务端获取的注册结果报文
      8. additionalData: "" // 附加信息（可选）
      9. };
      ```
   5. 调用notifyUAFResult进行注册结果通知。

      ```
      1. try {
      2. // 调用notifyUAFResult进行注册结果通知
      3. fido.notifyUAFResult(this.uiContext, notifyUafMessage).then(notify => {
      4. console.info("Succeeded in doing notifyUAFResult.");
      5. })
      6. } catch (error) {
      7. const err: BusinessError = error as BusinessError;
      8. console.error(`Failed to call notifyUAFResult. Code is ${err.code}, message is ${err.message}`);
      9. // 业务根据错误码判断异常类型，进行相应处理
      10. }
      ```
4. 使用FIDO免密身份认证。

   1. 初始化认证器信息（如果已执行过初始化操作，则无需重复执行）。

      ```
      1. // 获取当前界面的context
      2. try {
      3. // 调用discover方法初始化认证器信息
      4. let discoverData = await fido.discover(this.uiContext);
      5. } catch (error) {
      6. const err: BusinessError = error as BusinessError;
      7. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
      8. // 业务根据错误码判断异常类型，进行相应处理
      9. }
      ```
   2. 访问FIDO服务端，获取策略检查报文，检查用户开启状态。

      ```
      1. // uafMessage为从FIDO服务器获取的策略检查报文
      2. let uafAuthMessage: fido.UAFMessage = {
      3. /*
      4. * 策略检查报文格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"","serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":[[{"aaid":["001B#1001"],"keyIDs":["test keyIDs"],"authenticationAlgorithms":[1]}]]}}]
      5. */
      6. uafProtocolMessage: uafMessage, // 从服务端获取的检查策略报文
      7. additionalData: "" // 附加信息（可选）
      8. };
      9. let isRegistered: boolean = true;
      10. try {
      11. // 检查是否已经开启FIDO认证
      12. await fido.checkPolicy(this.uiContext, uafAuthMessage);
      13. } catch (error) {
      14. isRegistered = false;
      15. const err: BusinessError = error as BusinessError;
      16. console.error(`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}`);
      17. // 业务根据错误码判断状态，进行相应处理
      18. }
      19. if (isRegistered) {
      20. console.info("has registered, no need to register again.");
      21. // 已注册，业务根据需要执行后续流程
      22. }
      ```
   3. 访问FIDO服务端，获取认证报文，调用processUAFOperation接口进行FIDO认证。

      ```
      1. // regMessage为从FIDO服务器获取的认证报文
      2. let uafRegMessage: fido.UAFMessage = {
      3. /*
      4. * 认证报文格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"","serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":[[{"aaid":["001B#1001"],"keyIDs":["test keyIDs"],"authenticationAlgorithms":[1]}]]}}]
      5. */
      6. uafProtocolMessage: regMessage, // 从服务端获取的认证报文
      7. additionalData: "" // 附加信息（可选）
      8. };
      9. // 传递通道绑定参数（可选）
      10. let channelBinding: fido.ChannelBinding = {};
      11. try {
      12. // 调用processUAFOperation接口进行FIDO认证
      13. let messageResp = await fido.processUAFOperation(this.uiContext, uafRegMessage, channelBinding);
      14. } catch (error) {
      15. const err: BusinessError = error as BusinessError;
      16. console.error(`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}`);
      17. // 业务根据错误码判断异常类型，进行相应处理
      18. }
      19. // 发送认证响应报文至FIDO服务端进行验证并返回认证结果
      ```
5. 关闭FIDO免密身份认证。

   1. 初始化认证器信息（如果已执行过初始化操作，则无需重复执行）。

      ```
      1. try {
      2. // 调用discover方法初始化认证器信息
      3. let discoverData = await fido.discover(this.uiContext);
      4. } catch (error) {
      5. const err: BusinessError = error as BusinessError;
      6. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
      7. // 业务根据错误码判断异常类型，进行相应处理
      8. }
      ```
   2. 访问FIDO服务端，获取注销报文，调用processUAFOperation接口进行FIDO注销。

      ```
      1. // deregMessage为从FIDO服务器获取的注销报文
      2. let uafRegMessage: fido.UAFMessage = {
      3. /*
      4. * 注销报文格式:  [{"header":{"upv":{"major":1,"minor":0},"op":"Dereg","appID":""},"authenticators":[{"aaid":"001B#1001","keyID":"test keyID"}]}]
      5. */
      6. uafProtocolMessage: deregMessage, // 从服务端获取的注销报文
      7. additionalData: "" // 附加信息（可选）
      8. };
      9. // 传递通道绑定参数（可选）
      10. let channelBinding: fido.ChannelBinding = {};
      11. try {
      12. // 调用processUAFOperation接口进行FIDO注销
      13. let messageResp = await fido.processUAFOperation(this.uiContext, uafRegMessage, channelBinding);
      14. } catch (error) {
      15. const err: BusinessError = error as BusinessError;
      16. console.error(`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}`);
      17. // 业务根据错误码判断异常类型，进行相应处理
      18. }
      19. // 发送认证响应报文至FIDO服务端进行验证并返回认证结果
      ```
