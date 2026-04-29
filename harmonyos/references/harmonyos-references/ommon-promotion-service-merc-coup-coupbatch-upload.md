---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-upload
title: 上传券预存Code
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 券批次 > 上传券预存Code
category: harmonyos-references
scraped_at: 2026-04-29T14:08:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1bcff6965e6abba93993605c8f9cb48c17bc12e08472443fd457b558b4d2d944
---

## 功能介绍

商家券的code码支持商户自定义。如商家已有自己的优惠券系统，可直接使用自定义模式。即商家预先向华为支付上传券code，当券在发放时，华为支付自动从已导入的code中随机取值（不能指定），派发给用户。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/couponbatch/codeupload
* **数据格式：**

  请求消息：Content-Type: application/json

  响应消息：Content-Type: application/json

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Body**

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| requestNo | 是 | String | 请求号，由商户随机生成，不同请求要求唯一。最小长度为1，最大长度为64。  **说明**：用于保证幂等。对不同请求，requestNo的值要求不一样。对于相同请求，值要求一样，比如超时场景，可通过requestNo一样进行重试。 |
| batchNo | 是 | String | 批次号。 |
| codeList | 是 | List<String> | 券code列表。列表最大数量为200。每个元素最小长度为1，最大长度为32。 |

## **请求示例**

```
1. POST api/merchantgrow/v1/merchantcoupon/couponbatch/codeupload HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+KYaq1j*********************z0UcN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TI*********************vFexUasPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
4. {
5. "requestNo": "20000008",
6. "batchNo": "PV1202602041321081919089024***",
7. "codeList": ["C1", "C2", "C3", "C1"]
8. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，"000000"表示成功，其他表示见错误码。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名信息，除“sign”字段以外的其他字段参与签名。 |
| signType | 否 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| certNo | 否 | String | 签名所使用的证书编号。 |
| batchNo | 是 | String | 批次号。 |
| totalCount | 是 | Integer | 本次上传操作，去重后实际上传的code数目。 |
| successCount | 是 | Integer | 本次上传操作上传成功个数。 |
| successCodes | 否 | List<String> | 本次新增上传成功的code信息。  单个券code长度为【1，32】，条目个数限制为【1，200】。 |
| successTime | 是 | String | 上传操作完成时间。格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。注意：要使用必须传准确的UTC时间。 |
| failCount | 否 | Integer | 本次上传操作上传失败的code数。 |
| failCodes | 否 | List<[UploadFailReason](payment-model.md#uploadfailreason)> | 本次导入失败的code信息，请参照错误信息，修改后重试。 |
| existCodes | 否 | List<String> | 历史已存在的code列表，本次不会重复导入。  **说明**：单个券code长度为【1，32】，条目个数限制为【1，200】。 |
| duplicateCodes | 否 | List<String> | 本次重复导入的code会被自动过滤，仅保留一个做导入，如满足要求则成功。如不满足要求，则失败。请参照报错提示修改重试。  **说明**：单个券code长度为【1，32】，条目个数限制为【1，200】。 |

## **响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign":"MEQCIEIWzdpziRyTi8vhwWHFuDdxfsiw********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "batchNo": "PV12345",
8. "existCodes": [],
9. "failCount": 0,
10. "duplicateCodes": [
11. "C1"
12. ],
13. "totalCount": 3,
14. "successCodes": [
15. "C1",
16. "C2",
17. "C3"
18. ],
19. "successTime": "2024-03-23T16:26:20.318+0800",
20. "successCount": 3
21. }
```

## 错误码

**resultCode**非400000的错误码请看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | **解决方案** |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用, 请稍后重试 | 稍候重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | INVALID\_MERC\_NO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | CHECK\_MERC\_STATUS | 商户状态校验失败 | 请检查商户状态是否正常。 |
| 400000 | COUPON\_BATCH\_NOT\_EXIST | 未找到待发券批次 | 确认券批次是否已创建，券批次号传递是否正确。 |
| 400000 | COUPON\_BATCH\_INVALID\_STATUS | 批次已过期或暂停 | 确认券批次状态或重新创建券批次。 |
