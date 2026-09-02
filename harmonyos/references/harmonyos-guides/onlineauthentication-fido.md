---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-fido
title: FIDO免密认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > 免密认证 > FIDO免密认证
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5473592b0c9fa3eec4a8c6467c96a825376717d2fc47d9eef06ec443aad13d6a
---

## 场景介绍

* 开通FIDO免密认证功能，使用用户已有的生物特征开通FIDO免密认证能力。
* 使用FIDO免密认证功能，使用用户已开通的生物特征进行FIDO免密认证能力。
* 关闭FIDO免密认证功能，使用用户已开通的生物特征注销FIDO免密认证能力。

## 约束与限制

需满足以下条件，才能使用该功能。

* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```typescript
  import { BusinessError } from '@kit.BasicServicesKit';
  import { userAuth } from '@kit.UserAuthenticationKit';
  // ...
  function getAvailableStatus(){
    try {
      // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
      userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
      console.info('current auth trust level is supported');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
    }
  }
  ```
* FIDO服务需要联网，以便提供完整的在线身份校验服务。应用在调用本服务API前，需将FIDO服务联网行为向用户明示，并且取得用户同意。
* FIDO服务会将匿名化的指纹ID和面容ID等个人信息返回至应用，以提供绑定具体生物特征的免密认证能力。应用将个人信息上云前，需要向用户明示并且取得同意，详细请参考[个人数据处理说明](onlineauthentication-personal-data-processing-description.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/HNkNweIFRS2laiki5hRRGg/zh-cn_image_0000002706834310.png)

**注册流程说明：**

1. 应用客户端调用[discover](../harmonyos-references/onlineauthentication-fido-api.md#fidodiscover)接口初始化认证器，获取可用的认证器数据。
2. 应用客户端向应用服务端请求策略检查报文，获取报文数据。
3. 应用客户端调用[checkPolicy](../harmonyos-references/onlineauthentication-fido-api.md#fidocheckpolicy)接口检查用户开通状态。
4. 应用客户端向应用服务端请求注册报文，获取报文数据。
5. 应用客户端调用[processUAFOperation](../harmonyos-references/onlineauthentication-fido-api.md#fidoprocessuafoperation)接口注册FIDO，获取响应报文。
6. 应用客户端将注册响应报文上报至应用服务端，应用服务端验证后返回注册结果。
7. 应用客户端调用[notifyUAFResult](../harmonyos-references/onlineauthentication-fido-api.md#fidonotifyuafresult)接口通知注册结果。

**认证流程说明：**

1. 应用客户端调用[discover](../harmonyos-references/onlineauthentication-fido-api.md#fidodiscover)接口初始化认证器信息，获取可用的认证器数据。
2. 应用客户端向应用服务端请求策略检查报文，获取报文数据。
3. 应用客户端调用[checkPolicy](../harmonyos-references/onlineauthentication-fido-api.md#fidocheckpolicy)接口检查用户开通状态。
4. 应用客户端向应用服务端请求认证报文，获取认证报文数据。
5. 应用客户端调用[processUAFOperation](../harmonyos-references/onlineauthentication-fido-api.md#fidoprocessuafoperation)接口进行FIDO认证，获取认证响应报文。
6. 应用客户端将认证响应报文上报至应用服务端，应用服务端验证后返回认证结果。

**关闭流程说明：**

1. 应用客户端调用[discover](../harmonyos-references/onlineauthentication-fido-api.md#fidodiscover)接口初始化认证器数据，获取可用的认证器数据。
2. 应用客户端向应用服务端获取注销报文。
3. 应用客户端调用[processUAFOperation](../harmonyos-references/onlineauthentication-fido-api.md#fidoprocessuafoperation)接口进行FIDO注销，获取注销响应报文。
4. 应用客户端将注销响应报文上报至应用服务端，应用服务端删除数据后返回结果。

## 接口说明

以下是FIDO免密认证功能开通、认证、注销的所需要的接口，具体API说明详见[接口文档](../harmonyos-references/onlineauthentication-fido-api.md#fidodiscover)。

| 接口名 | 描述 |
| --- | --- |
| [discover](../harmonyos-references/onlineauthentication-fido-api.md#fidodiscover)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md#context)): Promise<[DiscoveryData](../harmonyos-references/onlineauthentication-fido-api.md#discoverydata)> | 发现设备的认证能力，返回当前设备软件支持的认证器数据。使用Promise异步回调。 |
| [checkPolicy](../harmonyos-references/onlineauthentication-fido-api.md#fidocheckpolicy)(context: common.Context, uafRequest: [UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)): Promise<void> | 检测用户策略的开启状态。使用Promise异步回调。 |
| [processUAFOperation](../harmonyos-references/onlineauthentication-fido-api.md#fidoprocessuafoperation)(context: common.Context, uafRequest: [UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage), channelBindings?: [ChannelBinding](../harmonyos-references/onlineauthentication-fido-api.md#channelbinding)): Promise<[UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)> | 用户UAF操作接口，处理UAF协议消息。使用Promise异步回调。 |
| [notifyUAFResult](../harmonyos-references/onlineauthentication-fido-api.md#fidonotifyuafresult)(context: common.Context, uafResponse: [UAFMessage](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)): Promise<void> | 通知FIDO认证器FIDO免密认证功能的开启结果。使用Promise异步回调。 |

## 开发步骤

1. 需要业务方自行根据FIDO标准协议部署FIDO服务器。
2. 导入相关模块。

   ```typescript
   import { fido } from '@kit.OnlineAuthenticationKit';
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. 开通FIDO免密认证。

   1. 初始化认证器信息。

      ```typescript
      @Entry
      @Component
      struct Index {
        private uiContext: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // ...
        private async discover() {
          try {
            // 初始化认证器信息
            let discoverData = await fido.discover(this.uiContext);
            console.info('Succeeded in discover, supportedUAFVersions:', discoverData.supportedUAFVersions,
              'clientVendor:', discoverData.clientVendor, 'clientVersion:', discoverData.clientVersion,
              'availableAuthenticators:', discoverData.availableAuthenticators);
            // 业务处理discoverData
            // ...
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
            // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
            // ...
          }
        }
        // ...
        build() {
          // ...
        }
      }
      ```
   2. 访问FIDO服务端，获取策略检查报文，检查用户开通状态。

      ```typescript
      private async checkPolicy(policyMessage: string) {
        let policyUafMessage: fido.UAFMessage = {
          /*
           * 策略检查报文policyMessage格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"",
           * "serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":[[{"aaid":["001B#1001"],
           * "keyIDs":["test keyIDs"],"authenticationAlgorithms":[1]}]]}}]
           */
          uafProtocolMessage: policyMessage, // 从FIDO服务端获取的检查策略报文
          additionalData: '' // 附加信息（可选）
        };
        try {
          // 检查是否已经开启FIDO认证
          await fido.checkPolicy(this.uiContext, policyUafMessage).then(() => {
            console.info('Succeeded in doing checkPolicy.');
            // ...
          })
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}`);
          // 业务根据错误码判断状态，进行相应处理
          // ...
        }
      }
      ```
   3. 访问FIDO服务端，获取注册报文，调用processUAFOperation接口进行FIDO注册。

      ```typescript
      private async register(regMessage: string) {
        try {
          let regUafMessage: fido.UAFMessage = {
            /*
             * 注册报文regMessage格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Reg","appID":"",
             * "serverData":"test server data"},"challenge":"test challenge","username":"test user name",
             * "policy":{"accepted":[[{"aaid":["001B#1001"],"attachmentHint":1,"authenticationAlgorithms":[1],
             * "authenticatorVersion":1}]]}}]
             */
            uafProtocolMessage: regMessage, // 从FIDO服务端获取的注册报文
            additionalData: '' // 附加信息（可选）
          };
          // 传连接通道参数（可选）
          let channelBinding: fido.ChannelBinding = {};
          // 调用processUAFOperation接口进行FIDO注册
          let messageResp: fido.UAFMessage =
            await fido.processUAFOperation(this.uiContext, regUafMessage, channelBinding);
          console.info('Succeeded in register, uafProtocolMessage:',
            messageResp.uafProtocolMessage, 'additionalData:', messageResp.additionalData);
          // ...
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(`Failed to register. Code is ${err.code}, message is ${err.message}`);
          // 业务根据错误码判断异常类型，进行相应处理
          // ...
        }
      }
      ```
   4. 发送注册响应报文至FIDO服务端进行验证并获取注册结果报文。

      ```typescript
      let notifyUafMessage: fido.UAFMessage = {
        /*
         * 响应报文notifyMessage格式: {"authenticatorsSucceeded":[{"description":"Attention completed successfully.",
         * "aaid":"001B#1001","keyID":"test keyID"}]}
         */
        uafProtocolMessage: notifyMessage, // 从FIDO服务端获取的注册结果报文
        additionalData: '' // 附加信息（可选）
      };
      ```
   5. 调用notifyUAFResult进行注册结果通知。

      ```typescript
      try {
        // 调用notifyUAFResult进行结果通知
        await fido.notifyUAFResult(this.uiContext, notifyUafMessage).then(() => {
          console.info('Succeeded in doing notifyUAFResult.');
        });
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to call notifyUAFResult. Code is ${err.code}, message is ${err.message}`);
        // 业务根据错误码判断异常类型，进行相应处理
      }
      ```
4. 使用FIDO免密认证。

   1. 初始化认证器信息（如果已执行过初始化操作，则无需重复执行）。

      ```typescript
      @Entry
      @Component
      struct Index {
        private uiContext: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // ...
        private async discover() {
          try {
            // 初始化认证器信息
            let discoverData = await fido.discover(this.uiContext);
            console.info('Succeeded in discover, supportedUAFVersions:', discoverData.supportedUAFVersions,
              'clientVendor:', discoverData.clientVendor, 'clientVersion:', discoverData.clientVersion,
              'availableAuthenticators:', discoverData.availableAuthenticators);
            // 业务处理discoverData
            // ...
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
            // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
            // ...
          }
        }
        // ...
        build() {
          // ...
        }
      }
      ```
   2. 访问FIDO服务端，获取策略检查报文，检查用户开启状态。

      ```typescript
      private async checkPolicy(policyMessage: string) {
        let policyUafMessage: fido.UAFMessage = {
          /*
           * 策略检查报文policyMessage格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"",
           * "serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":[[{"aaid":["001B#1001"],
           * "keyIDs":["test keyIDs"],"authenticationAlgorithms":[1]}]]}}]
           */
          uafProtocolMessage: policyMessage, // 从FIDO服务端获取的检查策略报文
          additionalData: '' // 附加信息（可选）
        };
        try {
          // 检查是否已经开启FIDO认证
          await fido.checkPolicy(this.uiContext, policyUafMessage).then(() => {
            console.info('Succeeded in doing checkPolicy.');
            // ...
          })
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}`);
          // 业务根据错误码判断状态，进行相应处理
          // ...
        }
      }
      ```
   3. 访问FIDO服务端，获取认证报文，调用processUAFOperation接口进行FIDO认证。

      ```typescript
      private async authenticate(authMessage: string) {
        try {
          let authUafMessage: fido.UAFMessage = {
            /*
             * 认证报文authMessage格式: [{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"",
             * "serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":[[{"aaid":["001B#1001"],
             * "keyIDs":["test keyIDs"],"authenticationAlgorithms":[1]}]]}}]
             */
            uafProtocolMessage: authMessage, // 从FIDO服务端获取的认证报文
            additionalData: '' // 附加信息（可选）
          };
          // 传递通道绑定参数（可选）
          let channelBinding: fido.ChannelBinding = {};
          let messageResp: fido.UAFMessage = await fido.processUAFOperation(this.uiContext, authUafMessage, channelBinding);
          console.info('Succeeded in authenticate, uafProtocolMessage:',
            messageResp.uafProtocolMessage, 'additionalData:', messageResp.additionalData);
          // ...
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(`Failed to authenticate. Code is ${err.code}, message is ${err.message}`);
          // 业务根据错误码判断状态，进行相应处理
          // ...
        }
        // 发送认证响应报文至FIDO服务端进行验证并返回认证结果
      }
      ```
5. 关闭FIDO免密认证。

   1. 初始化认证器信息（如果已执行过初始化操作，则无需重复执行）。

      ```typescript
      @Entry
      @Component
      struct Index {
        private uiContext: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // ...
        private async discover() {
          try {
            // 初始化认证器信息
            let discoverData = await fido.discover(this.uiContext);
            console.info('Succeeded in discover, supportedUAFVersions:', discoverData.supportedUAFVersions,
              'clientVendor:', discoverData.clientVendor, 'clientVersion:', discoverData.clientVersion,
              'availableAuthenticators:', discoverData.availableAuthenticators);
            // 业务处理discoverData
            // ...
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
            // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
            // ...
          }
        }
        // ...
        build() {
          // ...
        }
      }
      ```
   2. 访问FIDO服务端，获取注销报文，调用processUAFOperation接口进行FIDO注销。

      ```typescript
      private async deRegister(deRegMessage: string) {
        try {
          let deRegUafMessage: fido.UAFMessage = {
            /*
             * 注销报文deRegmessage格式:  [{"header":{"upv":{"major":1,"minor":0},"op":"Dereg","appID":""},
             * "authenticators":[{"aaid":"001B#1001","keyID":"test keyID"}]}]
             */
            uafProtocolMessage: deRegMessage, // 从FIDO服务端获取的注销报文
            additionalData: '' // 附加信息（可选）
          };
          // 传递通道绑定参数（可选）
          let channelBinding: fido.ChannelBinding = {};
          let messageResp: fido.UAFMessage =
            await fido.processUAFOperation(this.uiContext, deRegUafMessage, channelBinding);
          console.info('Succeeded in deRegister, uafProtocolMessage:',
            messageResp.uafProtocolMessage, 'additionalData:', messageResp.additionalData);
          // ...
        } catch (error) {
          // ...
          const err: BusinessError = error as BusinessError;
          console.error(`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}`);
          // 业务根据错误码判断异常类型，进行相应处理
        }
        // 发送认证响应报文至FIDO服务端进行验证并返回认证结果
      }
      ```
