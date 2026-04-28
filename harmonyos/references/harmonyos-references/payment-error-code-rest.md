---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-error-code-rest
title: REST API错误码
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > REST API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:18:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b02e6b5c9b5d85275363d7343ecc3376775adddda21c97f4c785e37b6e7c1fd8
---

说明

若问题仍无法解决，请选择[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 公共错误码说明

Payment Kit开放网关会对开发者的应用/元服务接口的非业务类型调用返回错误码。

| 返回码 | 结果描述 | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- | --- |
| 000000 | Success | - | - | 不涉及。 |
| 100000 | 权限不足 | INSUFFICIENT\_PERMISSION | 商户权限受限 | 在商户平台检查并配置该产品权限。 |
| 200000 | 缺少必选参数 | MISSING\_AUTH\_HEADER | 缺少鉴权参数 | 在请求头中构建并传入对应的鉴权信息。 |
| 200000 | 缺少必选参数 | MISSING\_TRACER\_ID | 缺少tracerId参数 | 检查请求参数，每次请求传入唯一的traceId。 |
| 200000 | 缺少必选参数 | MISSING\_HEADER\_SIGN | 缺少headSign参数 | 检查请求参数，传入headerSign。 |
| 200000 | 缺少必选参数 | MISSING\_CALLER\_ID | 缺少callerId参数 | 检查请求参数，传入callerId，对应于商户号。 |
| 200000 | 缺少必选参数 | MISSING\_BODY\_SIGN | 缺少bodySign参数 | 检查请求参数，传入bodySign。 |
| 200000 | 缺少必选参数 | MISSING\_AUTH\_ID | 缺少authId参数 | 检查请求参数，传入商户对应的authId。 |
| 200000 | 缺少必选参数 | MISSING\_TIME | 缺少时间戳参数 | 检查请求参数，传入当前时间戳信息。 |
| 200000 | 缺少必选参数 | MISS\_ACCESS\_TOKEN | 缺少accessToken参数 | 检查请求头参数MISS\_ACCESS\_TOKEN是否正确传递。 |
| 200000 | 缺少必选参数 | MISS\_PETAL\_PAY\_SIGN\_KEY\_ID | 缺失petalpaySignKeyId参数 | 检查请求头参数petalpaySignKeyId是否正确传递。 |
| 200000 | 缺少必选参数 | MISS\_PETAL\_PAY\_ENC\_KEY\_ID | 缺失petalpayEncKeyId参数 | 检查请求头参数petalpayEncKeyId是否正确传递。 |
| 200000 | 缺少必选参数 | MISS\_DEVELOPER\_SIGN\_KEY\_ID | 缺失developerSignKeyId参数 | 检查请求头参数developerSignKeyId是否正确传递。 |
| 200001 | 非法的参数 | INVALID\_AUTH\_HEADER | 鉴权信息无效 | 检查请求头，传入正确的鉴权信息。 |
| 200001 | 非法的参数 | INVALID\_TRACER\_ID | tracerId参数无效 | 检查请求参数，传入正确的traceId。 |
| 200001 | 非法的参数 | INVALID\_AUTH\_ID | authId参数无效 | 检查请求参数，传入正确的authId。 |
| 200001 | 非法的参数 | INVALID\_TIME | 时间戳参数无效 | 检查请求参数，传入正确的时间戳。 |
| 200001 | 非法的参数 | INVALID\_SESSION\_KEY | sessionKey参数无效 | 检查请求参数，传入正确的sessionKey。 |
| 200001 | 非法的参数 | INVALID\_PUB\_KEY | 商户公钥无效 | 检查请求参数，确认已生成并上传公钥。 |
| 200001 | 非法的参数 | INVALID\_DUPLICATE\_REQUEST | 无效的重复请求 | 检查请求参数，每次请求需要生成新的traceId。 |
| 200001 | 非法的参数 | INVALID\_PARAMETER | 参数无效 | 检查请求参数，传入正确的参数。 |
| 200001 | 非法的参数 | INVALID\_CALLER\_ID | callerId参数无效 | 检查鉴权请求头callerId字段传递是否正确（如类型、特殊字符、长度等）。 |
| 200001 | 非法的参数 | INVALID\_PAY\_DEV\_AUTH | invalid payDevAuth header | 检查鉴权请求头payDevAuth 是否正确传递。 |
| 200001 | 非法的参数 | UNSUPPORTED\_PETAL\_PAY\_ENC\_KEY\_ID | unsupported PetalPayEncKeyId | 检查鉴权参数PetalPayEncKeyId是否正确传递。  检查接口入参敏感字段加密所用公钥是否匹配。 |
| 200001 | 非法的参数 | UNSUPPORTED\_PETAL\_PAY\_SIGN\_KEY\_ID | unsupported PetalPaySignKeyId | 检查鉴权参数PetalPaySignKeyId是否正确传递。 |
| 200001 | 非法的参数 | UNSUPPORTED\_DEVELOPER\_SIGN\_KEY\_ID | unsupported developerSignKeyId | 检查鉴权参数developerSignKeyId是否正确传递。  检查请求加签所用公钥是否匹配。 |
| 200002 | 签名错误 | INVALID\_SIGNATURE | 无效签名 | 检查请求参数，按说明完成签名并传入正确的签名参数。 |
| 300000 | 调用频率受限 | CALL\_FREQUENCY\_LIMITED | API调用次数超限 | 降低请求并发量。 |
| 500000 | 服务不可用 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |

## 业务错误码

响应的错误码示例，具体请参考业务接口（**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)）

| 返回码 | 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | PAY\_ORDER\_NOT\_EXIST | 支付订单号不存在 | 检查入参订单号是否正确。 |
| 400000 | MERC\_ORDER\_NOT\_EXIST | 商户订单号不存在 | 检查入参订单号是否正确。 |
| 400000 | INVALID\_MERCNO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | REJECTED\_BY\_RISK\_CONTROL | 风控拒绝 | 咨询华为支付团队，[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。 |
| 400000 | NO\_MATCH\_MATCHING\_PRODUCT | 未匹配到商户产品 | 检查商户产品是否配置正确。 |
| 400000 | CHECK\_ORDER\_STATUS | 订单状态异常 | 请检查是否使用相同订单重复下单。 |
| 400000 | BANK\_CARD\_NOT\_SUPPORT | 银行卡不支持 | 更换其他银行卡重试。 |
| 400000 | CHECK\_ACCOUNT\_STATUS | 支付账号异常 | 请检查支付账号状态。 |
| 400000 | CHECK\_MERC\_STATUS | 商户状态异常 | 请检查商户状态是否正常。 |
| 400000 | MERC\_NOT\_SUPPORT\_REFUND | 商户不支持退款 | 请检查商户是否具有退款权限。 |
| 400000 | CHECK\_AMOUNT\_INVALID | 金额校验失败 | 检查传入金额是否合法。 |
| 400000 | CHECK\_ACCOUNT\_BALANCE | 账户余额不足 | 查看商户账户余额。 |
| 400000 | RETRY\_TOO\_MANY | 重试次数超限，请换单重试 | 换单重新请求。 |
| 400000 | NOT\_SETTLEMENT\_DATE | 非结算日，账单未生成 | 请修改入参日期重试。 |
| 400000 | INVALID\_APPID | appId不匹配 | 检查appId是否正确且已经绑定商户号。 |
| 400000 | BILL\_SWITCH\_NOT\_TURN\_ON | 账单开关没有打开 | 前往“[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)”的“功能设置”中开启相应的账单开关。 |
| 400000 | INVALID\_SUB\_MERCNO | 权限异常，请求传递的子商户号不是验签商户的子商户 | 请检查子商户号是否和验签商户正确关联。 |
| 400000 | ORDER\_CONCURRENT\_ERROR | 订单并发错误 | 解决方案：  1. 一笔普通收单多次退款，时间间隔要在1分钟以上。  2. 合单多笔子单退款，时间间隔要在1分钟以上。 |
| 400000 | NOT\_SUPPORTED\_OPERATION | 不支持的操作 | 请确认操作是否允许，如无法确认可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。 |
| 400000 | RESTRICTED\_USER\_ACCOUNT | 用户账户受限 | 请确认用户账户状态是否正常。 |
| 400000 | RESTRICTED\_USER\_TRANSACTION | 用户交易受限 | 请确认用户状态是否正常。 |
| 400000 | RESTRICTED\_MERCHANT\_TRANSACTION | 商户交易受限 | 请检查商户支付账号状态是否正常。 |
| 400000 | CHECK\_CONTRACT\_STATUS | 签约号无效 | 1. 请确认是否存在签约关系。  2. 检查签约号输入是否正确。 |
| 400000 | NOT\_IN\_VALIDITY\_PERIOD | 不在有效期内 | 请检查订单是否已过期，不再支持操作。 |
| 400000 | PAYMENT\_ACCOUNT\_NOT\_ENABLE | 支付账户未开通 | 请检查是否开通支付账户。 |
| 400000 | CUST\_NOT\_EXIST | 用户不存在或已销户 | 请确认操作的华为账号状态是否正常或已销户。 |
| 400000 | OPERATION\_NOT\_AUTHORIZED | 操作未授权 | 服务商代特约商户发起退款需要申请授权。 |
| 400000 | RESTRICTED\_TRANSACTION | 交易受限 | 交易存在风险，无法正常交易，请确认。无法确认可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。 |
| 400000 | WITHHOLD\_OVER\_TIMES | 代扣次数超限 | 请间隔四小时后再重试。 |
| 400000 | INVALID\_PAYMENT\_TYPE | 用户无有效支付方式 | 请检查用户是否存在可用支付方式。 |
| 400000 | CHECK\_TRANSACTION\_ORDER\_STATUS | 交易订单状态异常 | 请检查是否使用相同的商户订单号重复预下单。 |
| 400000 | NEED\_CHANGE\_ORDER | 请换单重试 | 更换商户订单号重试。 |
| 400000 | ORDER\_NOT\_SUPPORT | 订单不支持 | 确认操作是否正确，  无法确认可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。 |
| 400000 | COUPON\_INCORRECT\_MERCHANT\_RELATION | 批次创建商户和归属商户无归属关系 | 请检查批次创建商户和归属商户是否有归属关系。 |
| 400000 | COUPON\_INVALID\_NOTIFY\_URL | 回调地址仅支持https协议地址 | 请检查回调地址是否为https协议地址。 |
| 400000 | COUPON\_BATCH\_NOT\_EXIST | 未找到待发券批次 | 确认券批次是否已创建，券批次号传递是否正确。 |
| 400000 | COUPON\_BATCH\_INVALID\_STATUS | 批次已过期或暂停 | 确认券批次状态或重新创建券批次。 |
| 400000 | COUPON\_BATCH\_UPDATING | 批次正在更新中，无法处理新的更新请求 | 确认批次更新状态，等待批次更新完成。 |
| 400000 | COUPON\_NOT\_MATCH\_SEND\_RULE | 不满足发券条件 | 请确认用户是否满足发券条件（如用户已注销等）。 |
| 400000 | COUPON\_EXCEED\_SEND\_LIMIT\_PER\_REQUEST | 超过单个请求发放上限 | 请确认单个请求发放上限。 |
| 400000 | COUPON\_NOT\_EXIST | 未找到相关优惠券 | 查询用户优惠券信息，确认是否存在优惠券。 |
| 400000 | COUPON\_INVALID\_STATUS | 优惠券状态不正确 | 查询用户优惠券状态，确认是否正常。 |
| 400000 | INSUFFICIENT\_PERMISSION | 商户权限受限 | 在商户平台检查并配置该产品权限。 |
