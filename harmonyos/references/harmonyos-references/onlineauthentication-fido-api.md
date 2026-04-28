---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-fido-api
title: FIDO
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > ArkTS API > FIDO
category: harmonyos-references
scraped_at: 2026-04-28T08:07:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:78b1ebaf6b596d0b4a6ef09b7132dfae82f4e77588098dc5d5d1e03ac3c51db3
---

本模块提供FIDO UAF本地免密认证能力，通过生物特征代替密码，支持免密登录，免密支付等业务场景，包括：

1、开通FIDO免密身份认证功能。

2、使用FIDO免密身份认证功能。

3、关闭FIDO免密身份认证功能。

支持的设备类型为：Phone, PC/2in1, Tablet

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1Tablet

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { UIContext } from '@kit.ArkUI'
3. import { common } from '@kit.AbilityKit';
4. import { fido } from '@kit.OnlineAuthenticationKit';
```

## ChannelBinding

PhonePC/2in1Tablet

传输通道的绑定参数，用于验证通道的安全性。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serverEndPoint | string | 否 | 是 | TLS服务器证书的base64url编码哈希值。长度由不同三方服务器限制，默认值为空。 |
| tlsServerCertificate | string | 否 | 是 | 如果FIDO UAF客户端使用了TLS服务器证书，则该证书必须设置为base64url、DER编码的格式。若不涉及，不可设置该字段。长度由不同三方服务器限制，默认值为空。 |
| tlsUnique | string | 否 | 是 | TLS通道Finished结构的base64url编码。若不涉及，不可设置该字段。长度由不同三方服务器限制，默认值为空。 |
| cidPubkey | string | 否 | 是 | base64url编码的序列化使用UTF-8编码的JwkKey结构。如果客户端TLS堆栈不向处理实体提供TLS ChannelID信息，则不可设置该字段。如果客户端TLS堆栈支持TLS ChannelID信息，但TLS (web)服务器尚未发出信号，则必须设置为“未使用”。长度由不同三方服务器限制，默认值为空。 |
| tokenBinding | string | 否 | 是 | base64url编码的序列化使用UTF-8编码的TokenBindingID结构。如果客户端TLS堆栈不向处理实体提供令牌绑定ID信息，则不可设置该字段。如果客户端TLS堆栈支持令牌绑定ID信息，但TLS (web)服务器尚未发出信号，则必须设置为“未使用”。长度由不同三方服务器限制，默认值为空。 |

## UAFMessage

PhonePC/2in1Tablet

UAF字典对象，包含原始的UAF协议消息和附加数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uafProtocolMessage | string | 否 | 否 | UAF协议消息。长度由不同三方服务器限制。注意其中若有challenge、transaction等字段，则包含上述字段的TA请求报文不可超过2048字节。 |
| additionalData | string | 否 | 是 | UAF附加数据。长度由不同三方服务器限制，默认值为空。该字段格式为json string，具体格式{"key": value}。  - 当key为isGuideToSetBiometrics，表示用户未设置生物特征的情况下，使用系统跳转能力引导用户去设置生物特征。value取值为true、false。  - true：使用系统跳转能力。  - false：不使用系统跳转能力。  当不传入isGuideToSetBiometrics，则表示不使用系统跳转能力。  **起始版本：** 6.0.0(20)  - 当key为navigationButtonText，表示支持开发者自定义认证方式，在用户生物认证失败并点击切换认证方式按钮时，提示用户拉起自定义的认证界面。  - 当value为任意文本时，表示开启自定义认证功能，此时传入的文本为切换认证方式按钮显示的文本。  当不传入navigationButtonText，则表示不使用自定义认证功能。  **起始版本：** 6.0.1(21)  - 当key为algorithmMode，表示支持开发者选择密码算法模式。  - 当前value取值支持传入'default'、'SM'。  - 'default'：使用FIDO标准默认支持的国际通用算法。  - 'SM'：FIDO已支持国密化，传入此值表示使用中国国密算法。  当不传入algorithmMode，则使用FIDO协议默认支持的国际通用算法。  **起始版本：** 6.1.0(23) |

**调用示例：**

```
1. // ...
2. let uafMessage: fido.UAFMessage = {
3. uafProtocolMessage: "", // uafProtocolMessage为从FIDO服务器获取的报文
4. additionalData: JSON.stringify({
5. isGuideToSetBiometrics: true,
6. navigationButtonText: 'Navigation Button',
7. algorithmMode: 'SM'
8. }) // 当不传入additionalData时，应将其替换为：additionalData: ""
9. };
10. // ...
```

## Version

PhonePC/2in1Tablet

UAF协议版本信息。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| major | number | 否 | 否 | 主要版本，默认值为1。 |
| minor | number | 否 | 否 | 次要版本，默认值为0。 |

## RgbPaletteEntry

PhonePC/2in1Tablet

RGB三元调色板。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| r | number | 否 | 否 | 红色样本值，取值为0~255。 |
| g | number | 否 | 否 | 绿色样本值，取值为0~255。 |
| b | number | 否 | 否 | 蓝色样本值，取值为0~255。 |

## DisplayPNGCharacteristicsDescriptor

PhonePC/2in1Tablet

PNG图片特征对象。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 图片宽度（dpi），长度满足uint32。 |
| height | number | 否 | 否 | 图片高度（dpi），长度满足uint32。 |
| bitDepth | number | 否 | 否 | 位深（bit），长度满足uint8。 |
| colorType | number | 否 | 否 | 颜色类型。0代表灰度，2代表真彩色，3代表索引颜色，4代表使用alpha的灰度，6代表使用alpha的真彩色。 |
| compression | number | 否 | 否 | 仅定义PNG压缩方法0（zlib），压缩方法的其他值保留。 |
| filter | number | 否 | 否 | 过滤方法。0代表None,1代表Sub，2代表Up，3代表Average，4代表Paeth。 |
| interlace | number | 否 | 否 | 交错方法。0代表空行方法，1代表Adam7方式。 |
| plte | Array<[RgbPaletteEntry](onlineauthentication-fido-api.md#rgbpaletteentry)> | 否 | 是 | 调色板条目。默认值为空。 |

## Authenticator

PhonePC/2in1Tablet

认证器对象，描述了一个可用认证器的相关信息。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 否 | 认证器名，长度由不同三方服务器限制。 |
| aaid | string | 是 | 否 | 认证器唯一标识，长度由不同三方服务器限制，CFCA为9个字符。 |
| description | string | 是 | 否 | 认证器描述，长度由不同三方服务器限制。 |
| supportedUAFVersions | Array<[Version](onlineauthentication-fido-api.md#version)> | 是 | 否 | 认证器支持的UAF协议版本。 |
| assertionScheme | string | 是 | 否 | 认证断言编码方式，长度由不同三方服务器限制，CFCA为8个字符。 |
| authenticationAlgorithm | number | 是 | 否 | 支持的鉴别算法。  目前支持ALG\_SIGN\_SECP256R1\_ECDSA\_SHA256\_RAW算法（0x0001）。 |
| attestationTypes | Array<number> | 是 | 否 | 支持的鉴别类型列表。  目前支持TAG\_ATTESTATION\_BASIC\_FULL(0x3E07)。 |
| userVerification | number | 是 | 否 | 用户认证方式。  2：指纹。  16：人脸。 |
| keyProtection | number | 是 | 否 | 秘钥保护类型。  目前支持KEY\_PROTECTION\_TEE 0x0004。 |
| matcherProtection | number | 是 | 否 | 认证设备保护类型。  目前支持MATCHER\_PROTECTION\_TEE 0x0002。 |
| attachmentHint | number | 是 | 否 | 认证设备连接方式。  目前支持ATTACHMENT\_HINT\_INTERNAL 0x0001。 |
| isSecondFactorOnly | boolean | 是 | 否 | 认证器是否仅能作为第二因子使用。  目前不支持，返回值为false。 |
| tcDisplay | number | 是 | 否 | 交易确认显示方式。  目前支持TRANSACTION\_CONFIRMATION\_DISPLAY\_ANY 0x0001。 |
| tcDisplayContentType | string | 是 | 否 | 交易确认显示支持的MIME内容类型。  目前支持text/plain。 |
| tcDisplayPNGCharacteristics | Array<[DisplayPNGCharacteristicsDescriptor](onlineauthentication-fido-api.md#displaypngcharacteristicsdescriptor)> | 是 | 否 | 交易确认显示支持的PNG集合。 |
| icon | string | 是 | 否 | 认证器的PNG图标。长度由不同PNG图片Base64编码长度限制。 |
| supportedExtensionIDs | Array<string> | 是 | 否 | UAF协议扩展标识符的支持列表。 |

## DiscoveryData

PhonePC/2in1Tablet

FIDO UAF客户端软件状态和可用的认证器数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedUAFVersions | Array<[Version](onlineauthentication-fido-api.md#version)> | 否 | 否 | 客户端支持的FIDO UAF协议版本列表。 |
| clientVendor | string | 否 | 否 | UAF客户端的供应商，CFCA长度为4个字符。 |
| clientVersion | [Version](onlineauthentication-fido-api.md#version) | 否 | 否 | FIDO UAF客户端版本。 |
| availableAuthenticators | Array<[Authenticator](onlineauthentication-fido-api.md#authenticator)> | 否 | 否 | 包含描述可使用UAF认证器的认证器结构数。 |

## discover

PhonePC/2in1Tablet

discover(context: common.Context): Promise<DiscoveryData>

发现设备的认证能力，返回当前设备软件支持的认证器数据。使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | ability的context。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<[DiscoveryData](onlineauthentication-fido-api.md#discoverydata)> | Promise对象。返回包含当前设备软件支持的认证器数据的对象。 |

**错误码:**

以下错误码的详细介绍请参见[FIDO免密认证错误码](onlineauthentication-error-code-fido.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Device type error. |
| 1005900015 | System Interruption. |
| 1005900016 | Unknown error. |

**调用示例：**

```
1. // ...
2. // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可
3. let uiContext = new UIContext();
4. let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
5. try {
6. let discoverData: fido.DiscoveryData = await fido.discover(context);
7. console.info("Succeeded in doing discover, discoverData:", discoverData);
8. // ...
9. } catch (error) {
10. const err: BusinessError = error as BusinessError;
11. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
12. // ...
13. }
14. // ...
```

## checkPolicy

PhonePC/2in1Tablet

checkPolicy(context: common.Context, uafRequest: UAFMessage): Promise<void>

检测用户策略的开启状态。使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | ability的context。 |
| uafRequest | [UAFMessage](onlineauthentication-fido-api.md#uafmessage) | 是 | 需要检测的策略和操作。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[FIDO免密认证错误码](onlineauthentication-error-code-fido.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Device type error. |
| 1005900005 | No authenticator matching the authenticator policy specified is available. |
| 1005900006 | A violation of the UAF protocol occurred. |
| 1005900015 | System Interruption. |
| 1005900016 | Unknown error. |

**调用示例：**

```
1. // ...
2. // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可
3. let uiContext = new UIContext();
4. let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
5. // 从FIDO服务器获取报文message
6. let uafMessage: fido.UAFMessage = {
7. uafProtocolMessage: "", // uafProtocolMessage为从FIDO服务器获取的报文
8. additionalData: ""
9. };
10. try {
11. await fido.checkPolicy(context, uafMessage);
12. console.info("Succeeded in doing checkPolicy.");
13. // ...
14. } catch (error) {
15. const err: BusinessError = error as BusinessError;
16. console.error(`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}`);
17. // ...
18. }
19. // ...
```

## processUAFOperation

PhonePC/2in1Tablet

processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding): Promise<UAFMessage>

用户UAF操作接口，处理UAF协议消息。使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | ability的context。 |
| uafRequest | [UAFMessage](onlineauthentication-fido-api.md#uafmessage) | 是 | FIDO客户端软件使用的[UAFMessage](onlineauthentication-fido-api.md#uafmessage)。 |
| channelBindings | [ChannelBinding](onlineauthentication-fido-api.md#channelbinding) | 否 | 传输通道的绑定参数，用于验证通道安全性，默认为空。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<[UAFMessage](onlineauthentication-fido-api.md#uafmessage)> | Promise对象。返回包含签名后响应数据的UAFMessage消息对象。 |

**错误码：**

以下错误码的详细介绍请参见[FIDO免密认证错误码](onlineauthentication-error-code-fido.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Device type error. |
| 1005900003 | User cancels. |
| 1005900005 | No authenticator matching the authenticator policy specified is available. |
| 1005900006 | A violation of the UAF protocol occurred. |
| 1005900007 | No Facet\_ID is registered. |
| 1005900009 | The authenticator denies access to the generated request. |
| 1005900014 | The user does not record biometric features or the authentication module is abnormal. |
| 1005900015 | System Interruption. |
| 1005900016 | Unknown error. |
| 1005900017 | Switched to the custom authentication process. |

**调用示例：**

```
1. // ...
2. // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可
3. let uiContext = new UIContext();
4. let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
5. // 从FIDO服务器获取报文message
6. let uafMessage: fido.UAFMessage = {
7. uafProtocolMessage: "", // uafProtocolMessage为从FIDO服务器获取的报文
8. additionalData: '{"navigationButtonText": "使用其他方式验证"}' // 这里是可选字段，如果需要开启自定义认证功能，请在此传入文本
9. };
10. let channelBinding: fido.ChannelBinding = {};
11. try {
12. let messageResp = await fido.processUAFOperation(context, uafMessage, channelBinding);
13. console.info("Succeeded in doing processUAFOperation.");
14. // ...
15. } catch (error) {
16. const err: BusinessError = error as BusinessError;
17. console.error(`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}`);
18. // ...
19. }
20. // ...
```

## notifyUAFResult

PhonePC/2in1Tablet

notifyUAFResult(context: common.Context, uafResponse: UAFMessage): Promise<void>

通知FIDO认证器FIDO免密身份认证功能的开启结果。使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | ability的context。 |
| uafResponse | [UAFMessage](onlineauthentication-fido-api.md#uafmessage) | 是 | UAF响应消息。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[FIDO免密认证错误码](onlineauthentication-error-code-fido.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Device type error. |
| 1005900006 | A violation of the UAF protocol occurred. |
| 1005900015 | System Interruption. |
| 1005900016 | Unknown error. |

**调用示例：**

```
1. // ...
2. // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可
3. let uiContext = new UIContext();
4. let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
5. // 从FIDO服务器获取报文message
6. let uafMessage: fido.UAFMessage = {
7. uafProtocolMessage: "", // uafProtocolMessage为从FIDO服务器获取的报文
8. additionalData: ""
9. };
10. try {
11. await fido.notifyUAFResult(context, uafMessage);
12. console.info("Succeeded in doing notifyUAFResult.");
13. // ...
14. } catch (error) {
15. const err: BusinessError = error as BusinessError;
16. console.error(`Failed to call notifyUAFResult. Code is ${err.code}, message is ${err.message}`);
17. // ...
18. }
19. // ...
```
