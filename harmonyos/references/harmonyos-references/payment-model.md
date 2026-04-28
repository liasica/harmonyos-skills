---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-model
title: 数据模型说明
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > 数据模型说明
category: harmonyos-references
scraped_at: 2026-04-28T08:18:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f2863b56f3040aa20e299c5094f58a27325033a3213fe255d77408460d71364
---

## orderStr

SDK华为支付接口入参**订单支付信息**。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| app\_id | 否 | String | 应用ID。获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。  **说明：** 服务商模式接入，切换到商户应用/元服务拉起收银台时，需要把app\_id改成商户相应的appId，并在[平台类商户/服务商预下单](payment-agent-prepay.md)接口通过subAppId字段同步传递。 |
| merc\_no | 是 | String | 商户号。获取商户号请参见[查询商户号信息](../pay-docs/hwzf-shanghuhao-0000001725982508.md)。  **说明：** 请传递直连、平台/服务商商户号，需要和获取预支付ID商户号保持一致。 |
| prepay\_id | 是 | String | 预支付ID。使用[直连商户预下单](payment-prepay.md)/[平台类商户/服务商预下单](payment-agent-prepay.md)请求生成，有效期10分钟。 |
| timestamp | 是 | String | 当前时间戳，标准北京时间，时区为东八区，自1970年1月1日 0点0分0秒以来的毫秒数，13位。示例值：1666230721315。 |
| noncestr | 是 | String | 随机字符串，不长于32位。推荐随机数生成算法。  每笔订单都需重新生成。 |
| sign | 是 | String | 签名，使用除了sign字段以外的其他字段计算签名值。可参考[签名规则](payment-rest-overview.md#签名规则)。 |
| auth\_id | 是 | String | 商户证书编号。一个商户可配置多套证书，请妥善保管。获取可参见[准备证书](../harmonyos-guides/payment-certificates-config.md)。 |
| reserved | 否 | String | 扩展字段，jsonStr格式。参见[reserved](payment-model.md#reserved)说明。 |

SDK跳转三方支付接口入参**订单支付跳转信息**。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| nextAction | 是 | String | 指定三方支付方式。  - L：linkUrl  - S：scheme |
| linkUrl | 否 | String | 三方支付方式linkUrl类型的链接（按照三方支付平台接入要求获取）。根据nextAction指定支付方式传递。 |
| scheme | 否 | String | 三方支付方式scheme类型的链接（按照三方支付平台接入要求获取）。根据nextAction指定支付方式传递。 |
| clientToken | 是 | String | 客户端凭据。  拉起通用收银台接口[requestPayment](payment-paymentservice.md#paymentservicerequestpayment)、[cashierPicker](payment-paymentservice.md#paymentservicecashierpicker)响应中获取。 |

## reserved

orderStr扩展字段信息说明。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| sandbox\_flag | 否 | Boolean | 沙盒环境标识。是否使用沙盒环境进行调试，使用沙盒环境调试时必填。  - true：是  - false：否（默认） |

## extraInfo

SDK华为支付接口保留字段说明。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| selectPayType | 否 | String | 指定收银台展示的支付方式列表。多个支付方式通过竖线 “|” 分隔，支付方式为在申请[产品开通与配置](../harmonyos-guides/payment-common-pay-introduction.md#产品开通与配置)中提供的支付方式。  **说明：** 例如商户配置3个支付方式（微信支付wechat\_pay、支付宝ali\_pay、支付宝沙盒ali\_pay\_sandbox），开发者可传入 ：  1. wechat\_pay|ali\_pay（收银台展示微信支付、支付宝）  2. wechat\_pay|ali\_pay\_sandbox（收银台展示微信支付、支付宝沙盒） |

## payload

SDK华为支付接口预留信息字段payload说明。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| method | 否 | String | 备选支付方式。  AP: alternative Payment Type |

## contractStr

SDK签约接口入参说明。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| appId | 否 | String | 应用ID。获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。 |
| preSignNo | 是 | String | 预签约号，使用[直连商户预签约](payment-withhold-presign.md)/[平台类商户/服务商预签约](payment-partner-withhold-presign.md)请求生成，有效期10分钟。 |

## PayMercAuth

PayMercAuth JSON类型保存了商户鉴权信息，用于请求头入参。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| callerId | 是 | String | 商户号。获取商户号参见[查询商户号信息](../pay-docs/hwzf-shanghuhao-0000001725982508.md)。  **说明：** 请传递直连、平台/服务商商户号，和商户证书编号（authId）归属商户号保持一致。 |
| traceId | 是 | String | 与请求对应，需要保证每次请求唯一，建议时间戳+随机数。最大长度32。 |
| time | 是 | Long | 当前时间戳，以毫秒计，防止重复请求。 |
| authId | 是 | String | 商户证书编号。一个商户可配置多套证书，请妥善保管。获取可参见[准备证书](../harmonyos-guides/payment-certificates-config.md)。 |
| sessionKey | 否 | String | 使用SM2加密过的SM4密钥，涉及敏感参数传递场景（参见[敏感信息处理](../harmonyos-guides/payment-server-connect.md#敏感信息处理)）必传，否则无须传递。 |
| headerSign | 是 | String | PayMercAuth对象内入参的签名值（除headerSign外的所有字段），根据[签名规则](payment-rest-overview.md#签名规则)排序拼接后签名。 |
| bodySign | 是 | String | 请求Body参数签名，根据[签名规则](payment-rest-overview.md#签名规则)排序拼接后签名。  **说明：**  GET请求方式请对请求uri进行签名，如请求url为“https://www.xxxxxx.com/api/v2/aggr/transactions/merc-orders/202xxx?mercNo=1015xxx”，则签名内容为“/api/v2/aggr/transactions/merc-orders/202xxx?mercNo=1015xxx”。 |

## PayDevAuth

JSON类型数据，保存了开发者鉴权信息，用于请求头入参。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| clientId | 是 | String | 应用的OAuth 2.0客户端ID（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“我的项目”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“OAuth 2.0客户端ID（凭据）：Client ID”的值）。 |
| accessToken | 是 | String | 应用级的token。获取方式请参见[获取应用级凭证](payment-api-common-get-app-token.md)。 |
| traceId | 是 | String | 与请求对应，需要保证每次请求唯一，建议时间戳+随机数。最大长度32。 |
| time | 是 | Long | 当前时间戳，以毫秒计，防止重复请求。 |
| developerEncKeyId | 否 | String | 开发者加密公钥证书Id（获取方式请参见[上传开发者公钥](../harmonyos-guides/payment-real-name-preparations.md#上传开发者公钥及下载华为公钥)）。接口涉及敏感参数（接口字段中说明）请求场景必传，否则无须传递。  开发者指定华为侧使用对应的开发者加密公钥进行响应字段加密返回，开发者使用对应的私钥进行解密。 |
| petalpayEncKeyId | 否 | String | 华为加密公钥证书Id（获取方式请参见[下载华为公钥](../harmonyos-guides/payment-real-name-preparations.md#上传开发者公钥及下载华为公钥)）。接口涉及响应敏感参数（接口字段中说明）场景必传，否则无须传递。  开发者使用对应的华为加密公钥进行API接口请求中隐私字段加密，华为侧使用对应的私钥进行解密。 |
| developerSignKeyId | 是 | String | 开发者验签公钥证书Id（获取方式请参见[上传开发者公钥](../harmonyos-guides/payment-real-name-preparations.md#上传开发者公钥及下载华为公钥)）。开发者使用对应的私钥进行接口请求签名，华为侧使用对应的公钥进行验签。 |
| petalpaySignKeyId | 是 | String | 华为验签公钥证书Id（获取方式请参见[下载华为公钥](../harmonyos-guides/payment-real-name-preparations.md#上传开发者公钥及下载华为公钥)）。华为侧使用对应的华为加签私钥进行接口响应报文签名，开发者使用对应的公钥进行验签。 |
| bodySign | 是 | String | 请求Body参数签名。请求参数根据[签名规则](payment-rest-overview.md#section174821258151218)排序拼接后使用SM2方式签名。 |
| headerSign | 是 | String | 请求headerSign参数签名。PayDevAuth对象内入参的签名值（除headerSign外的所有字段）根据[签名规则](payment-rest-overview.md#section174821258151218)排序拼接后使用SM2方式签名。 |

## PromotionItem

营销信息缓存模型。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| promotionId | 否 | String | 营销活动类型Id。 |
| promotionType | 否 | String | 营销活动类型。  - PROMOTION：营销活动  - COUPON：优惠券  - VOUCHER：支付满减券  - CONSVOUCHER：消费金 |
| promotionAmount | 否 | Long | 优惠金额，单位：分。 |
| promotionStatus | 否 | String | 活动状态。  - PROMO\_FAILED：营销处理失败  - PROMO\_UNKNOW：营销状态未知  - PROMO\_SUCCESS：营销成功 |

## BillDownloadParam

账单下载地址信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| headers | 是 | [Map](payment-model.md#map) | 下载鉴权信息。 |
| method | 是 | String | 调用方法。 |
| downloadUrl | 是 | String | 文件下载url。 |

## Map

账单下载信息请求头相关字段

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| Authorization | 是 | String | 鉴权请求头。 |
| x-amz-content-sha256 | 是 | String | 签名计算方式。 |
| x-amz-client-request-id | 是 | String | 签名客户端请求id。 |
| x-amz-date | 是 | String | 签名日期标识。 |
| connection | 是 | String | 连接标识，标识此次请求使用的是长连接还是短连接。 |
| Host | 是 | String | 请求主机。 |
| user-agent | 是 | String | 代理标识，用来标识发起请求的用户代理信息。 |
| Content-Type | 是 | String | 资源类型。 |

## PayerIn

接口请求用户信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| userClientIp | 否 | String | 客户端下单时ip。 |
| credentialType | 否 | String | 证件类型。最大长度为2。  01：身份证（默认）  02：军官证  03：护照  04：户口簿  05：士兵证  06：港澳来往内地通行证  07：台湾同胞来往内地通行证  08：临时身份证  09：外国人居留证  10：警官证  15：港澳居民居住证  16：台湾居民居住证  99：其他 |
| credentialIdNo | 是 | String | 证件号。用于校验同名认证支付交易。  隐私字段，需参考[敏感信息处理](../harmonyos-guides/payment-server-connect.md#敏感信息处理)进行加密传递。  最大长度128。 |
| realName | 否 | String | 用户真实姓名。用于校验同名认证支付交易。  隐私字段，需参考[敏感信息处理](../harmonyos-guides/payment-server-connect.md#敏感信息处理)进行加密传递。  最大长度256。 |
| textType | 否 | String | 文本类型。最大长度为2。  01：身份证号、姓名、证件类型填写全文（默认）  02：身份证填写后六位，姓名、证件类型全文 |

## PayerOut

用户信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| openId | 否 | String | 用户在所属商户AppID下的唯一标识。 |
| spOpenId | 否 | String | 用户在所属合作伙伴商户AppID下的唯一标识。 |
| subOpenId | 否 | String | 用户在子商户AppID下的唯一标识。 |
| userClientIp | 否 | String | 客户端下单时ip。 |
| userClientIpMatched | 否 | Boolean | 订单创建与订单完成时IP是否一致。  - true：一致  - false：不一致 |

## ContractInfo

签约信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| planId | 是 | String | 协议模板ID。该模板ID是商户在向华为支付[提交代扣权限申请](../harmonyos-guides/payment-password-free-pay-overview.md)时由华为支付生成。 |
| mercContractCode | 是 | String | 商户签约协议号。商户请求签约时传入的签约协议号，商户侧须唯一。最大长度64。 |
| callbackUrl | 是 | String | 回调通知地址，通知URL必须为外网环境可直接访问的URL，要求为https地址。具体要求参考[通知回调接口说明](payment-rest-overview.md#通知回调接口说明)。最大长度为512 |

## GoodDetail

商品详情。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| quantity | 是 | Integer | 商品数量。 |
| unitPrice | 是 | Integer | 商品单价，单位为分。取值必须大于0。 |
| goodsName | 是 | String | 商品名称。最大长度为128。 |
| goodsId | 否 | String | 商品ID。最大长度为32。 |

## SubMercOrder

子订单信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| mercNo | 是 | String | 子单收款子商户号。  **说明：**  1. 子商户号必须是子单关联的主订单中传递商户号的子商户。  2. 子订单的商户号不能相同，同一子商户的订单可合并到一个子订单，不用拆分。 |
| tradeSummary | 是 | String | 交易的摘要。格式建议：“商户应用名称-商品描述”。最大长度128。 |
| totalAmount | 是 | Long | 订单金额，必须为大于0的整数值，单位：分。 |
| currency | 否 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| goodsDetail | 否 | List<[GoodDetail](payment-model.md#gooddetail)> | 订单详细信息列表。 |
| allocationType | 否 | String | 分账类型。  - NO\_ALLOCATION：不分账（默认）。  - DELAY\_ORDER\_ALLOCATION：延时分账。  **注意：** 使用该字段需联系开发者的商户对接人协助申请开通分账能力。分账相关操作参见[分账交易管理](../pay-docs/hwzf-dongjiefenzhang-0000001200646822.md)。 |
| payload | 否 | String | 商户预留信息，在查询和回调通知时会原样返回。最大长度255。 |

## SubOrderResult

子订单结果信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| sysTransOrderNo | 是 | String | 华为支付系统订单号。 |
| mercOrderNo | 是 | String | 商户订单号。 |
| orderStatus | 是 | String | 订单状态。  - TRX\_SUCCESS：交易成功  - TRX\_FAILED：交易失败  - TRX\_APPLY：交易处理中  - TRX\_PROC：交易处理中 |
| payload | 否 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |
| currency | 否 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| totalAmount | 否 | Long | 交易总金额，单位：分。 |
| payerAmount | 否 | Long | 实付金额，单位：分。 |
| promotionAmount | 否 | Long | 优惠金额，单位：分。 |
| finishTime | 否 | String | 合单支付子单支付完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。 |
| paymentTools | 否 | String | 支付方式。  - WECHAT\_MICROPAY：微信小程序支付  - AGMT：快捷  - ACCT：账户余额  - HUAWEIPAY：华为pay |
| promotionDetail | 否 | List<[PromotionItem](payment-model.md#promotionitem)> | 营销信息。 |

## payInfo

三方支付服务接口入参payInfo说明，json字符串的格式。参考示例如下：

```
1. // PayMethod.WECHAT_PAY：'{"appId":"***","partnerId":"***","prepayId":"***","packageValue":"***","nonceStr":"***","timeStamp":"***","sign":"***","extData":"***","token":"***"}'
2. // PayMethod.ALI_PAY：'{"orderInfo":"***", "token":"***"}'
3. // PayMethod.WECHAT_MINI_PROGRAM：'{"userName":"原始id", "path":"小程序启动路径", "miniProgramType":"小程序的类型，0-正式版 1-开发版 2-体验版 默认0", "extData":"***", "token":"***"}'
```

具体传递参数需开发者根据不同三方支付方式（[PayMethod](payment-third-payment-service.md#paymethod)）拉起收银台要求传递。

* PayMethod.WECHAT\_PAY传参参考[这里](https://pay.weixin.qq.com/doc/v3/merchant/4013070351)。
* PayMethod.ALI\_PAY传参参考[这里](https://opendocs.alipay.com/open/02e7gu?pathHash=f06f2b67#示例代码)。
* PayMethod.WECHAT\_MINI\_PROGRAM传参参考[这里](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Launching_a_Mini_Program/Android_Development_example.html)。

以下为华为支付要求传递参数：

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| token | 是 | string | 客户端凭证。拉起通用收银台时响应支付信息[PayResult](payment-paymentservice.md#payresult)(混合支付场景）/[PickerResult](payment-paymentservice.md#pickerresult)（纯外部支付场景）中返回。 |

## SelectPromotions

平台券信息请求信息。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| platCoupons | 否 | List<[PlatCoupon](payment-model.md#platcoupon)> | 平台券信息（可参见[查询用户可用券](payment-api-common-promotion-service-inquiry.md)接口获取）。 |

## PlatCoupon

平台券信息数据模型。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| platCouponNo | 是 | String | 平台券ID。 |
| openid | 是 | String | 用户ID。 |
| sceneParam | 是 | String | 券因子，jsonStr格式，可参见[sceneParams](payment-model.md#sceneparams)。  如平台券有订单金额限制示例：{"tradeOrderAmount": 200} |

## RequestSceneInfo

查询用户平台券信息。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| sceneId | 是 | String | 场景Id，唯一字符串，由商户自己生成，用于匹配响应结果。 |
| [sceneParams](payment-model.md#sceneparams) | 是 | Map<String, Object> | 场景扩展参数，用于匹配平台券的使用条件。部分参数可参考[设备信息](js-apis-device-info.md) |

## sceneParams

平台券场景参数。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| tradeOrderAmount | 是 | Integer | 订单金额，单位为分。 |
| bundleType | 是 | String | 包类型。示例：APP (HarmonyOS应用)、ATOMIC\_SERVICE(元服务) |
| bundleName | 否 | String | 包名。 |
| productModel | 否 | String | 产品模型。示例：ALN-AL00 |
| deviceType | 否 | String | 设备类型。详细请参考[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。示例：phone |
| osType | 是 | String | 系统类型枚举，可取值：  - HMOS: HarmonyOS操作系统 |

## ServCouponInfo

优惠券信息。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| couponCode | 是 | String | 优惠券编号。 |
| batchNo | 是 | String | 优惠券批次。 |
| couponType | 是 | String | 券批次类型，可选取值：  - NORMAL：固定面额满减券批次类型。 |
| effectiveTime | 是 | Long | 券可使用开始时间的时间戳。 |
| expireTime | 是 | Long | 用户领取到这张券的过期时间的时间戳。 |
| amount | 否 | Integer | 优惠金额（优惠券面额），单位分。 |
| displayInfo | 否 | [SimpleDisplayInfo](payment-model.md#simpledisplayinfo) | 优惠券简易展示信息。 |

## SimpleDisplayInfo

优惠券简易展示信息。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| couponDesc | 否 | String | 券描述。 |
| logoUrl | 否 | String | 品牌Logo的URL。 |

## SceneMatchedCouponNos

各场景匹配到的券号信息。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| sceneId | 否 | String | 场景Id。 |
| couponNos | 否 | List<String> | 优惠券编号列表。 |

## CouponSendRule

券发放规则。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| maxCoupons | 是 | Integer | 批次总限额，最大可发放券个数限制，最大值为1000000。  特殊规则：取值范围 0 ≤ value ≤ 1000000。  **说明**：新建批次时，如果couponCodeMode为MERCHANT\_UPLOAD，需要设置为0。 |
| maxCouponsPerUser | 是 | Integer | 用户限额，用户可领券数，最大值为100。  **说明**：新建批次时，如果couponCodeMode为HWPAY\_MODE或者MERCHANT\_API，要求用户限额小于等于批次总限额。 |
| maxCouponsByDay | 否 | Integer | 日限额，单天发放上限券数，最大值为1000000。  特殊规则：取值范围 1 ≤ value ≤ 1000000  **说明**：新建批次时，如果couponCodeMode为HWPAY\_MODE或者MERCHANT\_API，要求日限额小于等于批次总限额。 |
| sendEntrance | 是 | String | 投放商家券的位置。  PLATFORM\_PUSH：平台流量  MERC\_SELF\_CHANNEL：商家自有流量 |
| naturalPersonLimit | 否 | boolean | 自然人防刷即同证件号下的所有账户合并计算的限领次数。  - true：是  - false：否（默认）  **说明**：限领次数指的是参数字段“用户最大领取个数”填写的值，当前版本暂不支持。 |
| preventApiAbuse | 否 | boolean | 是否开启可疑账号拦截。  - true：是  - false：否（默认）  **说明**：如果选择“是”，则需要在发券消息中上报终端用户的设备信息，详情请查看[发放优惠券](ommon-promotion-service-merc-coup-ucoup-distribute.md)接口。 |

## CouponUseRuleMod

券核销相关规则。

| **参数** | **是否必选** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| useMethod | 是 | List<String> | 核销方式。  - FASTAPP：应用/元服务 |
| useAppId | 否 | List<String> | 核销方式为线上应用/元服务核销时必填。列表最大长度为8。每个元素最小长度为1，最大长度为32。 |

## SendCountInfo

批次已发放总量信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| totalSendNum | 否 | Integer | 批次已发放的券数量，满减、折扣、换购类型会返回该字段。 |
| totalSendAmount | 否 | Integer | 批次已发放的预算金额，满减券类型会返回该字段。 |
| todaySendNum | 否 | Integer | 批次当天已发放的券数量，设置了单天发放上限的满减、折扣、换购类型返回该字段。 |
| todaySendAmount | 否 | Integer | 批次当天已发放的预算金额，设置了单天发放上限的满减券类型返回该字段。 |

## DeviceInfo

用户的设备信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| deviceId | 否 | String | 设备标识，最大长度为128。 |
| deviceIdType | 否 | String | 设备标识类型，UDID、OAID等，最大长度为8。 |
| deviceModel | 否 | String | 设备型号，最大长度为32。 |
| riskToken | 否 | String | safetyDetect接口获取的riskToken，最大长度为512。 |
| clientIp | 否 | String | 领券时客户端IP信息，风控使用，最大长度为64。 |
| clientVersion | 否 | String | 领券时客户端版本信息，风控使用，最大长度为32。 |
| packageName | 否 | String | 领券时客户端应用的packageName，风控使用，最大长度为64。 |

## CouponNotice

通知消息的附加信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| receiveTime | 是 | String | 给用户发放优惠券的时间。格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。注意：要使用必须传准确的UTC时间。 |
| batchNo | 是 | String | 批次号。 |
| couponCodes | 否 | List<String> | 此批次下的券Code列表，用于创建批次时外部指定Code，或结果返回时返回券的Code。 |

## UploadFailReason

本次导入失败的code信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| couponCode | 是 | String | 商户通过API上传的券code。 |
| subCode | 否 | String | 对应券code上传失败的错误码。 |
| subMessage | 否 | String | 上传失败的错误信息描述。 |

## DiscountCoupon

折扣券使用规则。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| discountPercent | 是 | Integer | 折扣百分比，例如：86为八六折。 |
| transactionMinimum | 是 | Integer | 消费门槛，单位：分。  特殊规则：取值范围 1 ≤ value ≤ 10000000。 |

## CouponSendRuleMod

券分发规则。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| preventApiAbuse | 否 | boolean | 是否开启可疑账号拦截（如黑灰产账号）。  - true：是  - false：否（默认）  **说明**：不填默认“否”，如果选择“是”，则需要在发券消息中上报终端用户的设备信息，详情请查看发券接口。 |

## CouponUseRule

券核销相关规则。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| availableTime | 否 | [CouponAvailableTime](payment-model.md#couponavailabletime) | 优惠券的日期类核销条件。 |
| fixedNormalCoupon | 否 | [FixedNormalCoupon](payment-model.md#fixednormalcoupon) | 固定面额满减券使用规则。  **说明**：当优惠券类型（couponType）为满减券（NORMAL）时，该参数必传。 |
| discountCoupon | 否 | [DiscountCoupon](payment-model.md#discountcoupon) | 折扣券使用规则。  **说明**：当优惠券类型（couponType）为折扣券（DISCOUNT）时，该参数必传。 |
| exchangeCoupon | 否 | [ExchangeCoupon](payment-model.md#exchangecoupon) | 换购券使用规则。  **说明**：当优惠券类型（couponType）为换购券（EXCHANGE）时，该参数必传。 |
| useMethod | 是 | List<String> | 核销方式。  - FASTAPP：应用/元服务 |
| useAppId | 否 | List<String> | 核销方式为应用/元服务核销时必填。最大支持配置8个。每个appId的最小长度为1，最大长度为32。 |

## CouponInfo

待发券的批次信息和券码。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| couponCode | 是 | String | 优惠券编号。 |
| batchNo | 是 | String | 优惠券批次号。 |
| batchName | 是 | String | 优惠券批次名称。 |
| belongMerchant | 是 | String | 批次归属商户号。 |
| comment | 否 | String | 批次备注，用于自定义信息。字数上限为64个，一个中文汉字/英文字母/数字均占用一个字数。 |
| goodsName | 是 | String | 适用商品范围，字数上限为15个，一个中文汉字/英文字母/数字均占用一个字数。 |
| couponType | 是 | String | 批次类型。  - NORMAL：固定面额满减券批次  - DISCOUNT：折扣券批次  - EXCHANGE：换购券批次 |
| couponState | 是 | String | 商家券状态。  - SENDED：可用  - USED：已核销  - EXPIRED：已过期  - DEACTIVATED：已失效 |
| displayInfo | 否 | [CouponDisplayInfo](payment-model.md#coupondisplayinfo) | 优惠券展示信息。 |
| couponUseRule | 是 | [CouponUseRule](payment-model.md#couponuserule) | 券核销相关规则。 |
| availableStartTime | 是 | String | 券可使用开始时间。格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。 |
| expireTime | 是 | String | 用户领取到这张券的过期时间。格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。 |
| receiveTime | 是 | String | 用户领取到这张券的时间。 |
| distributeRequestNo | 是 | String | 发券时传入的唯一凭证。 |
| useRequestNo | 否 | String | 核销时传入的唯一凭证（如券已被核销，将返回此字段）。 |
| useTime | 否 | String | 券被核销的时间（如券已被核销，将返回此字段）。格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。 |
| lastRefundRequestNo | 否 | String | 最后一次回退时传入的唯一凭证（如券发生了退回，将返回此字段）。 |
| lastRefundTime | 否 | String | 最后一次券被回退的时间（如券发生了退回，将返回此字段），格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。 |
| deactivateRequestNo | 否 | String | 失效时传入的唯一凭证（如果一张券已失效，将返回此字段） |
| deactivateTime | 否 | String | 券被失效的时间（如果一张券已失效，将返回此字段）。格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。 |
| deactivateReason | 否 | String | 失效一张券的原因（如果一张券已失效，可能返回此字段）。 |

## CouponBatchDetailExtInfo

券批次查询响应。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| batchStatus | 是 | String | 批次当前状态。  - DEACTIVATED：已停用  - ACTIVATED：已激活  - EXPIRED：已过期 |
| batchNo | 是 | String | 券批次号。 |
| couponCodeCount | 否 | [CouponCodeCount](payment-model.md#couponcodecount) | 批次券code数量统计。 |
| sendCountInfo | 否 | [SendCountInfo](payment-model.md#sendcountinfo) | 批次已发放总量信息。 |
| batchName | 是 | String | 批次名称。 |
| belongMerchant | 是 | String | 批次归属商户号。注：  - 普通直连模式，该参数为直连商户号。  - 服务商模式，该参数为特约商户号。  - 平台商户模式，该参数为平台子商户号。 |
| comment | 否 | String | 批次描述信息。 |
| goodsName | 是 | String | 适用商品范围，用来描述批次在哪些商品可用。 |
| couponType | 是 | String | 优惠券类型。  - NORMAL：满减券  - DISCOUNT：折扣券  - EXCHANGE：换购券 |
| couponUseRule | 是 | [CouponUseRule](payment-model.md#couponuserule) | 券使用规则。 |
| couponSendRule | 是 | [CouponSendRule](payment-model.md#couponsendrule) | 券发放规则。 |
| displayInfo | 是 | [CouponDisplayInfo](payment-model.md#coupondisplayinfo) | 优惠券展示信息。 |
| couponCodeMode | 是 | String | 商户发放时接口指定券code。商户上传自定义code，发券时系统随机选取上传的券code。  - HWPAY\_MODE：自动分配券code，商户不需要预存code。  - MERCHANT\_API：调用发券接口时需指定券code。  - MERCHANT\_UPLOAD：需要调用上传预存code接口上传code，调用发券接口时无需指定code。 |
| notifyConfig | 否 | [NotifyConfig](payment-model.md#notifyconfig) | 通知回调配置。 |

## CurrentDayTime

当天可用时间。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| beginTime | 否 | Integer | 当天可用开始时间，单位：秒，1代表当天0点0分1秒。 |
| endTime | 否 | Integer | 当天可用结束时间，单位：秒，86399代表当天23点59分59秒。 |

## IrregularyTime

无规律的有效时间段。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| beginTime | 否 | String | 开始时间，格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。  注意：要使用必须传准确的UTC时间。 |
| endTime | 否 | String | 结束时间，格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。  注意：要使用必须传准确的UTC时间。 |

## FailResult

失败发券的结果信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| subCode | 是 | String | 失败的结果码。 |
| subMessage | 否 | String | 失败的结果描述信息。 |
| number | 否 | Integer | 失败的个数。 |
| batchNo | 是 | String | 批次号。 |
| couponCodes | 否 | List<String> | 此批次下的券Code列表，用于创建批次时外部指定Code，或结果返回时返回券的Code。 |

## CouponDisplayInfo

优惠券展示信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| merchantLogoUrl | 是 | String | 商户Logo的URL地址。最小长度为1，最大长度为256。 |
| merchantName | 是 | String | 商户简称。最小长度为1，最大长度为16。 |
| backgroundColor | 否 | String | 背景颜色，默认：#DF674F（红色），建议使用深色。最大长度为16。 |
| couponTitle | 否 | String | 优惠券标题，不填写时和券批次名称保持一致。最大长度为64。 |
| description | 否 | String | 使用须知，用于描述详细的活动规则。最大长度为5120。 |
| jumpUrl | 否 | String | 跳转连接，支持商家应用/元服务地址，不支持app地址，支持url、fastapp，如果不填写，则在华为平台（负一屏）不跳转。最大长度为1024。 |
| nextJumpUrl | 否 | String | HarmonyOS Next版本跳转连接，支持[元服务applinking地址](../atomic-guides/atomic-applinking.md)，不支持app地址，支持url、fastapp，如果不填写，则在华为平台（负一屏）不跳转。最大长度为1024。 |
| diversionName | 否 | String | 导流栏目显示名称。最大长度为16。 |

## ExchangeCoupon

换购券使用规则。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| exchangePrice | 是 | Integer | 单品换购价，单位：分。  特殊规则：取值范围 0 ≤ value ≤ 10000000。 |
| transactionMinimum | 是 | Integer | 消费门槛，单位：分。  特殊规则：取值范围 1 ≤ value ≤ 10000000。 |

## NotifyConfig

通知回调配置。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| notifyAppId | 否 | String | 事件通知APPID，最大长度为32。用于回调通知时，计算返回操作用户的openid（比如领券用户），商家私域发券时可以不填写。华为平台（负一屏）发券时如果不填写，则不通知商家发券结果。  **说明**：华为平台（负一屏）发券必须填写，并且填写完成之后不建议更改，因为更改后会导致openid发生变化。 |
| notifyUrl | 否 | String | 事件通知的URL地址，最大长度为256。用于商家私域发券时通知商家发券结果的地址，如果不填写，则不通知。回调地址必须是https开头。 |

## SendCouponInfo

待发券的批次信息和券码。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| sendNum | 是 | Integer | 该批次下一次发放的券数量，默认是1张。 |
| batchNo | 是 | String | 批次号。 |
| couponCodes | 否 | List<String> | 此批次下的券Code列表，用于创建批次时外部指定Code，或结果返回时返回券的Code。列表最大长度为10，每个元素最小长度为1，最大长度为32。 |

## CouponCodeCount

批次券code数量统计。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| totalCount | 是 | Integer | 该批次总共已上传的code总数 |
| availableCount | 是 | Integer | 该批次当前可用的code数 |

## FixedNormalCoupon

固定面额满减券使用规则。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| discountAmount | 是 | Integer | 优惠金额（优惠券面额）， 单位分。特殊规则：取值范围 1 ≤ value ≤ 10000000。 |
| transactionMinimum | 是 | Integer | 消费门槛，单位：分。  特殊规则：取值范围 1 ≤ value ≤ 10000000。 |

## BatchCoupons

成功发券的结果信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| batchNo | 是 | String | 批次号。 |
| couponCodes | 否 | List<String> | 此批次下的券Code列表，用于创建批次时外部指定Code，或结果返回时返回券的Code。 |

## CouponAvailableTime

优惠券的日期类核销条件。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| beginTime | 是 | String | 批次开始时间，长度为28，格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。  **说明**：  - 要使用必须传准确的UTC时间。  - 商家券有效期最长为1年。 |
| endTime | 是 | String | 批次结束时间，长度为28，格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。  **说明**：  - 要使用必须传准确的UTC时间。  - 商家券有效期最长为1年。  - 这个有效期也会影响用户收到的优惠券的有效期，由于券在卡包中展示时是精确到日期，建议endTime需要配置到截止日期的23:59:59。 |
| dayAfterReceive | 否 | Integer | 日期区间内，券生效后x天内有效。最小值为1，最大值为365。例如生效当天内有效填1，生效后2天内有效填2，以此类推。注意，用户在有效期开始前领取商家券，则从有效期第1天开始计算天数，用户在有效期内领取商家券，则从领取当天开始计算天数，无论用户何时领取商家券，商家券在活动有效期结束后均不可用。 |
| availableWeek | 否 | [AvailableWeek](payment-model.md#availableweek) | 固定周期有效时间段，可设置多个星期下的多个可用时间段，比如每周二10点到18点。 |
| irregularyTime | 否 | List<[IrregularyTime](payment-model.md#irregularytime)> | 无规律的有效时间段。 |
| waitDaysAfterReceive | 否 | Integer | 日期区间内，用户领券后需等待x天开始生效。最小值为0，最大值为365。例如领券后当天开始生效则无需填写，领券后第2天开始生效填1，以此类推。用户在有效期开始前领取商家券，则从有效期第1天开始计算天数，用户在有效期内领取商家券，则从领取当天开始计算天数。无论用户何时领取商家券，商家券在活动有效期结束后均不可用。 |

## AvailableWeek

固定周期有效时间段。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| weekDay | 否 | List<Integer> | 可用星期数，0代表周日，当填写dayTime时，该字段必填。 |
| dayTime | 否 | List<[CurrentDayTime](payment-model.md#currentdaytime)> | 当天可用时间段，最多不超过2个，具体定义参考CurrentDayTime结构定义。 |

## CouponDisplayInfoMod

优惠券展示信息。

| **参数** | **是否必填** | **参数类型** | **描述** |
| --- | --- | --- | --- |
| backgroundColor | 否 | String | 背景颜色，默认：#DF674F（红色），建议使用深色。最大长度为16。 |
| couponTitle | 否 | String | 优惠券标题，不填写时和券批次名称保持一致。最大长度为64。 |
| description | 否 | String | 使用须知，用于描述详细的活动规则。最大长度为5120。 |
| jumpUrl | 否 | String | 跳转连接，支持商家应用/元服务地址，不支持app地址，支持url、fastapp，如果不填写，则在华为平台（负一屏）不跳转。最大长度为1024。 |
| nextJumpUrl | 否 | String | HarmonyOS Next版本跳转连接，支持[元服务applinking地址](../atomic-guides/atomic-applinking.md)，不支持app地址，支持url、fastapp，如果不填写，则在华为平台（负一屏）不跳转。最大长度为1024。 |
| diversionName | 否 | String | 导流栏目显示名称。最大长度为16。 |
