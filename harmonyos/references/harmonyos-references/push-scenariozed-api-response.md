---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response
title: 响应参数
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 场景化消息 > 响应参数
category: harmonyos-references
scraped_at: 2026-04-29T14:09:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f018baa427a42e65e93c929d182b6d40371a79e462171af87cce29f938e397b2
---

## Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| code | 是 | String | 响应码。 |
| msg | 是 | String | 响应码描述。 |
| requestId | 是 | String | 请求标识。 |

## 响应示例

**响应成功示例：**

```
1. {
2. "code": "80000000",
3. "msg": "Success",
4. "requestId": "157*******006"
5. }
```

**响应失败示例：**

```
1. {
2. "code": "80100003",
3. "msg": "Illegal payload, badge addNum value ranges from 1 to 99",
4. "requestId": "1690*******1701"
5. }
```

## HTTP响应码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 400 | 参数错误。 | 请检查业务响应码并根据业务响应码进一步排查问题。 |
| 401 | 鉴权失败。 | 请检查HTTP头中Authorization参数。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 流量控制。 | · 平均分配发送速度。  · 平均分布推送时间段，不要集中发送。 |

## 业务响应码

说明

通过业务响应码定位问题之前，请优先检查[消息推送接口](push-scenariozed-api-request-struct.md)URL（https://push-api.cloud.huawei.com/**v3**/**[projectId]**/messages:send）是否正确：

* 请使用的v3版本的推送接口URL，不用使用v1或v2版本的推送接口URL，详情请参见[场景化消息中的请求URL版本问题](../harmonyos-guides/push-faq-8.md)。
* 请检查推送接口地址中的projectId，确保与您当前应用所属的项目保持一致，若不一致请更新推送接口URL中的projectId，并重新[生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)，应用重新[获取Push Token](../harmonyos-guides/push-get-token.md)，再进行消息推送。

### 80000000 成功

**错误信息**

Success.

**错误描述**

发送成功。

**可能原因**

发送成功。

**处理步骤**

不涉及。

### 80100000 部分Token发送成功

**错误信息**

Check Parameter Partial Success.

**错误描述**

部分Token发送成功。

**可能原因**

1. noPushTypeRight：未申请请求头中push-type对应场景的权益。
2. noRight：生成Push Token的应用不属于请求url中projectId对应的项目。
3. atomicUnableSendUnsubscribedMsg：元服务不支持本次请求中对应的消息场景。
4. tokenFormatError：Token格式错误。
5. countryNotSupport：国家不支持。
6. tokenPlatformNotSupport：不支持三方代理Token。
7. disableSendHuaweiMsgBecauseOfPenalty：应用被违规处罚。
8. differentImgVerifyPolicy：图片风控使用的[push-type](push-image-control.md#请求参数)与推送时的[push-type](push-scenariozed-api-request-struct.md#request-header)不一致。
9. appinfoError：应用未创建。
10. noRightToSendThisLiveNotificationEvent：没有申请对应实况窗场景的权益。

**处理步骤**

请根据响应消息中的提示，排查失败的Token是否存在以下情况：

1. noPushTypeRight：请开通请求头中push-type对应场景的权益，语音播报消息（push-type为2）权益申请可参考[申请推送语音播报消息权益](../harmonyos-guides/push-apply-right.md#申请推送语音播报消息权益)，应用内通话消息（push-type为10）权益申请可参考[申请推送应用内通话消息权益](../harmonyos-guides/push-apply-right.md#申请推送应用内通话消息权益)。
2. noRight：请检查生成Push Token的应用是否属于请求url中projectId对应的项目，即确保请求URL（https://push-api.cloud.huawei.com/v3/**[projectId]**/messages:send）中的**projectId**与[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站中该应用所属的“项目ID”一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/E6u256QjQVqmsNdExA_uww/zh-cn_image_0000002558607776.png?HW-CC-KV=V1&HW-CC-Date=20260429T060909Z&HW-CC-Expire=86400&HW-CC-Sign=80930A289A64C615A222B54E93BEEC0725A32256EE3448BB17D035C6163A22FA)
3. atomicUnableSendUnsubscribedMsg：元服务**仅支持**发送授权订阅消息、卡片刷新消息，请排查消息体内容。
4. tokenFormatError：请检查Push Token格式是否错误，并重新[申请Push Token](../harmonyos-guides/push-get-token.md)。
5. countryNotSupport：请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
6. tokenPlatformNotSupport：请重新[申请Push Token](../harmonyos-guides/push-get-token.md)。
7. disableSendHuaweiMsgBecauseOfPenalty：请在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上检查并处理违规后再尝试发送消息。
8. differentImgVerifyPolicy：请确保图片风控使用的[push-type](push-image-control.md#请求参数)与推送时的[push-type](push-scenariozed-api-request-struct.md#request-header)一致。
9. appinfoError：请在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上检查应用是否创建，如果应用已成功创建，请稍后重试。
10. noRightToSendThisLiveNotificationEvent： 请参见[开通实况窗权益](../harmonyos-guides/liveview-formal-authority.md)完成权益的申请。

响应示例：

```
1. {
2. "code": "80100000",
3. "msg": "{\"illegalTokens\":{\"tokenFormatError\":[\"MAAALgE4G98BAAAAst*******jg\"]},\"success\":1,\"failure\":1}",
4. "requestId": "1690*******1701"
5. }
```

### 80100001 请求参数部分错误

**错误信息**

Check Parameter Error.

**错误描述**

请求参数部分错误。

**可能原因**

请求参数部分错误。

**处理步骤**

请根据响应消息中的提示，检查并修改请求[参数内容](push-scenariozed-api-request-param.md)。

### 80100003 消息结构体错误

**错误信息**

Illegal payload, {errorTips}.

**错误描述**

消息结构体错误。

**可能原因**

消息结构体错误。

**处理步骤**

请根据响应消息中的提示，检查并修改[请求体结构](push-scenariozed-api-request-struct.md)。

### 80100004 消息设置的过期时间小于当前时间导致

**错误信息**

Illegal expire time.

**错误描述**

消息设置的过期时间小于当前时间导致。

**可能原因**

消息设置的过期时间小于当前时间导致。

**处理步骤**

请根据响应消息中的提示，检查并修改消息字段[ttl](push-scenariozed-api-request-param.md#pushoptions)。

### 80100022 消息携带图片未验签

**错误信息**

Anti-Spam: image not verify.

**错误描述**

消息携带图片未验签。

**可能原因**

消息图片未经过风控验证。

**处理步骤**

请根据响应消息中的提示，检查消息图片是否正常经过风控验证，对下发的图片进行[风控校验](push-image-control.md)。

### 80200001 认证错误

**错误信息**

Authentication Error.

**错误描述**

认证错误。

**可能原因**

1. 发送消息时未添加Authorization参数或Authorization的值为空。
2. 用于申请JWT Token的Project Id和推送消息的Project Id不一致。
3. Authorization参数中的JWT Token与实际应用不匹配。
4. 未使用v3版本接口发送REST API请求。
5. HarmonyOS 5及以上系统版本推送不再支持Oauth2.0开放鉴权，请使用[JWT（JSON Web Tokens）](../harmonyos-guides/push-jwt-token.md)鉴权。

**处理步骤**

请根据响应消息中的提示，排查请求头中Authorization参数鉴权失败是否存在以下情况：

1. 请检查发送消息时是否添加Authorization参数或Authorization的值为空。
2. 请参考[鉴权令牌生成步骤](../harmonyos-guides/push-jwt-token.md#开发步骤)中的步骤二，检查推送请求URL（https://push-api.cloud.huawei.com/**v3**/[projectId]/messages:send）中的projectId，确保与您当前应用所属的项目保持一致。
3. 请检查Authorization参数中的JWT Token与实际应用是否匹配，详情参见[基于服务账号生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)。
4. 请使用v3版本的请求URL（https://push-api.cloud.huawei.com/**v3**/[projectId]/messages:send）发送REST API请求。
5. 使用[JWT（JSON Web Tokens）](../harmonyos-guides/push-jwt-token.md)方式生成令牌后再推送消息。

### 80200005 JWT Token过期

**错误信息**

Jwt token expired.

**错误描述**

JWT Token过期。

**可能原因**

JWT Token过期。

**处理步骤**

请根据响应消息中的提示，重新生成JWT Token后再推送消息，请参见[基于服务账号生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)。

### 80300002 当前应用无权限下发推送消息

**错误信息**

No permission to send message to these tmIDs.

**错误描述**

当前应用无权限下发推送消息。

**可能原因**

1. 推送服务未开通。
2. 推送服务已开通，但推送请求URL中的projectId与当前应用所属的项目不一致。

**处理步骤**

1. 请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，查看推送服务是否已开通，请参见[开通推送服务](../harmonyos-guides/push-config-setting.md)。
2. 请参考[鉴权令牌生成步骤](../harmonyos-guides/push-jwt-token.md#开发步骤)中的步骤二，检查推送请求URL（https://push-api.cloud.huawei.com/**v3**/[projectId]/messages:send）中的projectId，确保与您当前应用所属的项目保持一致。

请确保当前应用所属的项目已开通了推送服务，并基于该项目重新[生成鉴权令牌](../harmonyos-guides/push-jwt-token.md)，并重新尝试推送消息。

### 80300007 所有Token都是无效的

**错误信息**

All the tokens are invalid.

**错误描述**

所有Token都是无效的。

**可能原因**

1. noPushTypeRight：未申请请求头中push-type对应场景的权益。
2. noRight：生成Push Token的应用不属于请求url中projectId对应的项目。或终端设备从HarmonyOS 4及以下版本（简称HarmonyOS）升级到HarmonyOS 5及以上版本（简称HarmonyOS NEXT）后，Push Token未重新获取或请求URL版本未更新至V3版本。
3. atomicUnableSendUnsubscribedMsg：元服务不支持本次请求中对应的消息场景。
4. tokenFormatError：Token格式错误。
5. countryNotSupport：国家不支持。
6. tokenPlatformNotSupport：不支持三方代理Token。
7. disableSendHuaweiMsgBecauseOfPenalty：应用被违规处罚。
8. differentImgVerifyPolicy：图片风控使用的[push-type](push-image-control.md#请求参数)与推送时的[push-type](push-scenariozed-api-request-struct.md#request-header)不一致。
9. appinfoError：应用未创建。
10. notSupportPlayVoice：推送自分类类型为PLAY\_VOICE（语音播报）的语音播报消息时，请求头中push-type传入错误。
11. noRightToSendThisLiveNotificationEvent：没有申请对应实况窗场景的权益。

**处理步骤**

请根据响应消息中的提示，排查失败的Token是否存在以下情况

1. noPushTypeRight：请开通请求头中对应push-type场景的权益，语音播报消息（push-type为2）权益申请可参考[申请推送语音播报消息权益](../harmonyos-guides/push-apply-right.md#申请推送语音播报消息权益)，应用内通话消息（push-type为10）权益申请可参考[申请推送应用内通话消息权益](../harmonyos-guides/push-apply-right.md#申请推送应用内通话消息权益)。
2. noRight：请检查生成Push Token的应用是否属于请求url中projectId对应的项目，即确保请求URL（https://push-api.cloud.huawei.com/v3/**[projectId]**/messages:send）中的**projectId**与[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站中该应用所属的“项目ID”一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/K72SpuejSmKSsiMB4qq6wA/zh-cn_image_0000002589327303.png?HW-CC-KV=V1&HW-CC-Date=20260429T060909Z&HW-CC-Expire=86400&HW-CC-Sign=2E9AFC246EC3627A98C5A8D8C2DEA82319A54E41794674ADA41AA03180426A40)

   若终端设备升级至HarmonyOS NEXT版本后，需重新生成对应的Push Token（建议您在应用启动时调用getToken()接口，若设备的Push Token发生变化，及时上报到您的应用服务器更新Push Token）。并使用[请求体参数说明](push-scenariozed-api-request-param.md)、V3版本的请求URL（https://push-api.cloud.huawei.com**/v3**/[projectId]/messages:send）发送REST API请求。
3. atomicUnableSendUnsubscribedMsg：元服务**仅支持**发送授权订阅消息、卡片刷新消息，请排查消息体内容。
4. tokenFormatError：请检查Push Token格式是否错误，并重新[申请Push Token](../harmonyos-guides/push-get-token.md)。
5. countryNotSupport：请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
6. tokenPlatformNotSupport：请重新[申请Push Token](../harmonyos-guides/push-get-token.md)。
7. disableSendHuaweiMsgBecauseOfPenalty：请在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上检查并处理违规后再尝试发送消息。
8. differentImgVerifyPolicy：请确保图片风控使用的[push-type](push-image-control.md#请求参数)与推送时的[push-type](push-scenariozed-api-request-struct.md#request-header)一致。
9. appinfoError：请在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上检查应用是否创建，如果应用已成功创建，请稍后重试。
10. notSupportPlayVoice：若应用需要推送自分类类型为PLAY\_VOICE（语音播报）的消息时，需使用语音播报消息进行推送，即请求头中push-type传入2，表示[语音播报消息](../harmonyos-guides/push-send-extend-noti.md#开发步骤)。
11. noRightToSendThisLiveNotificationEvent： 请参见[开通实况窗权益](../harmonyos-guides/liveview-formal-authority.md)完成权益的申请。

响应示例：

```
1. {
2. "code": "80300007",
3. "msg": "{\"failure\":2,\"illegalTokens\":{\"noRight\":[\"MAAALgE4G98BAAAAst*******jg\",\"MAAALgE4G98BAAAAst*******re\"]}}",
4. "requestId": "1690*******1701"
5. }
```

### 80300008 消息体大小超过4096Bytes（不包括Push Token）

**错误信息**

Push message size is too long.

**错误描述**

消息体大小超过4096Bytes（不包括Push Token）。

**可能原因**

请求消息体大小超过4096Bytes（不包括Push Token）

**处理步骤**

请根据响应消息中的提示，减小消息体后重新发送消息。

### 80300010 消息体中的Token数量超过系统设置的默认值

**错误信息**

token count should within {0} and {1}.

**错误描述**

消息体中的Token数量超过系统设置的默认值。

**可能原因**

1. 卡片刷新消息单次发送消息仅能携带1个Token。
2. 其余场景单次发送消息最多携带1000个Token。

**处理步骤**

请根据响应消息中的提示，请减少Token数量后分批发送消息。

### 80300029 测试消息请求流量限制

**错误信息**

When send test message, the api request exceed limit.

**错误描述**

测试消息请求流量限制。

**可能原因**

测试消息发送过于频繁。

**处理步骤**

请根据响应消息中的提示，稍后再发送。

### 80300030 测试消息单次携带Token数量超过系统设置的默认值

**错误信息**

When send test message, token count exceed limit.

**错误描述**

测试消息单次携带Token数量超过系统设置的默认值。

**可能原因**

1. 卡片刷新消息单次发送测试消息仅能携带1个Token。
2. 其余场景单次发送测试消息最多携带10个Token。

**处理步骤**

请根据响应消息中的提示，减少Token数量后再发送消息。

### 80300036 JWT有效期超过1天

**错误信息**

JWT expire period over threshold.

**错误描述**

JWT有效期超过1天。

**可能原因**

JWT有效期超过1天。

**处理步骤**

请根据响应消息中的提示，重新生成有效期小于1天的JWT Token后再推送消息。

### 80300037 由于存在违规处罚导致无法发送推送消息

**错误信息**

Disable send huawei msg because of penalty.

**错误描述**

由于存在违规处罚导致无法发送推送消息。

**可能原因**

由于存在违规处罚导致无法发送推送消息。

**处理步骤**

请根据响应消息中的提示，先在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上处理违规后再尝试发送消息。

### 81000001 系统内部错误

**错误信息**

Inner Error.

**错误描述**

系统内部错误。

**可能原因**

其他未知错误。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
