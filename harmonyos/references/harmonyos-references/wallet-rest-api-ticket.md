---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-ticket
title: 活动/景点门票接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 活动/景点门票接口
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1af7d420e94a82d718cc22b301e5f4a28de7a6d2a85653dd96cc201191bc5ffb
---

## 预置模板

卡片模板的创建是接入流程的第一步，这一步可以通过http/https请求的方式向华为钱包云服务提供卡券样式的关键信息，如卡面主标题、副标题、logo、背景图片等，用于华为钱包门票页面的展示。

开发者可创建多个共享相同机构名和服务号但模板ID不同的模板。在申请门票时，每张卡必须绑定唯一的模板ID，即一个模板可被多张门票复用，而一张门票仅能关联一个模板ID。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/{cardType}/model
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 响应的数据格式，取值为：application/json;charset=UTF-8。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | 创建Wallet Kit服务时注册的服务号，格式为：hwpass.xxx.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义）。 |
| passStyleIdentifier | 是 | String | 模板ID，长度不超过64个字符，只能是字母、数字、“.”、“-”和“\_”。 |
| organizationName | 是 | String | 商户名称，最长64个字节，无具体格式要求，中英文均可。 |
| passVersion | 是 | String | Pass版本号，固定“10.0”。 |
| fields | 是 | fields | 卡券展示信息，包括appendFields和commonFields两部分。 |

| appendFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| isCreateWhiteCard | 否 | String | 是否为NFC卡的标记。  true：NFC卡。  false：非NFC卡。 |

| commonFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| logo | 是 | String | 卡面logo，128\*128px，大小<=20kb，直角图片，无需切圆角。 |
| backgroundImage | 是 | String | 卡面背景  1312\*820px，直角图片，无需切圆角。 |
| picUrl | 是 | String | 带logo的卡面背景  1312\*820px，直角图片，无需切圆角。 |
| merchantName | 是 | String | 卡面主标题，小于256字节。 |
| name | 是 | String | 卡面副标题，小于256字节。 |

### 请求示例

```json
POST /hmspass/v2/key_ticket/model HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "passVersion": "10.0",
  "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
  "passStyleIdentifier": "keyTicketModelTest",
  "organizationName": "xxx",
  "fields": {
    "appendFields": [
      {
        "label": "NFCCardFlag",
        "value": "true",
        "key": "isCreateWhiteCard"
      }
    ],
    "commonFields": [
      {
        "label": "卡面主标题",
        "value": "门票",
        "key": "merchantName"
      },
      {
        "label": "卡面副标题",
        "value": "XXX门票",
        "key": "name"
      },
      {
        "label": "",
        "value": "https://xxx/xxx.png",
        "key": "logo"
      },
      {
        "label": "",
        "value": "https://xxx/xxx.webp",
        "key": "backgroundImage"
      },
      {
        "label": "",
        "value": "https://xxx/xxx.png",
        "key": "picUrl"
      }
    ]
  }
}
```

### 响应参数

模板预置成功，即http响应为200时，钱包云服务会将开发者业务管理服务请求的数据原样返回，即和请求体中的数据一致；其他错误情况，可见[REST API错误码](wallet-rest-api-error-code.md)。

### 调用示例

```java
public HwWalletObject invokeHwCreateKeyTicketClass(){
    HwWalletObject request=new HwWalletObject();
    request.setPassVersion("1.0");
    request.setPassTypeIdentifier("hwpass.keyticket.test");
    request.setPassStyleIdentifier("keyTicketModelTest");
    request.setOrganizationName("XXXX");
    Fields fields=new Fields();
    fields.setCountryCode("CN");
    List<ValueObject> commonFields=new ArrayList<>();
    ValueObject logo=new ValueObject();
    logo.setKey("logo");
    logo.setValue("https://www.huawei.com/XXX.png");
    commonFields.add(logo);
    fields.setCommonFields(commonFields);
    request.setFields(fields);
    HttpHeaders header=constructHttpHeaders();
    String baseUrl="https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass";
    String walletServerUrl=baseUrl+"/v2/key_ticket/model";
    HttpEntity<JSONObject> entity=new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)),header);
    ResponseEntity<JSONObject> exchange = REST_TEMPLATE.exchange(walletServerUrl,HttpMethod.POST,entity,JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(),HwWalletObject.class);
}
```

## 申请门票

开发者向开发者服务器申请开通门票，开发者服务器将门票卡片信息添加至钱包云服务中。其中：开发者App->开发者服务之间的交互由开发者自行实现，本章主要侧重于开发者服务器->钱包云服务申请门票的过程，主要包括：申请卡片和生成JWE数据。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/{cardType}/instance
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 响应的数据格式，取值为：application/json;charset=UTF-8。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | 创建Wallet Kit服务时注册的服务号，格式为：hwpass.xxx.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义）。 |
| passStyleIdentifier | 是 | String | 模板ID，长度不超过64个字符，只能是字母、数字、“.”、“-”和“\_”。 |
| organizationName | 是 | String | 预置模板中创建的商户名称，最长64个字节。 |
| organizationPassId | 是 | String | 门票卡片在开发者服务器中的卡号。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和serialNumber保持一致。 |
| serialNumber | 是 | String | 门票卡片在华为钱包服务器中的卡号，即instanceId。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和organizationPassId保持一致。 |
| fields | 是 | fields | 卡券展示信息，包括commonFields、appendFields、barCode、flexFields、status、localized部分。 |

| barCode参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| text | 否 | String | 二维码下方显示的描述或数字。 |
| type | 否 | String | 二维码类型，固定值：'qrCode'。 |
| value | 否 | String | 二维码码值。 |
| encoding | 否 | String | 编码格式，固定值：'UTF-8'。 |

| flexFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| primaryFields | 否 | List | 主要信息区字段列表，最多展示4条数据。每个主要信息区字段包含key、value、label。  每行展示规则：1个key居左对齐，2个key分别居左居右，3~4个key两侧居左居右、中间居中。  label和value值进行展示，label不支持换行，value最多2行超过截断。 |
| secondaryFields | 否 | List | 次要信息字段列表，最多展示4个。取label和value进行展示。每个元素包含key、value、label。门票常用key：seat（座位）、row（排）、section（区域）、gate（入口）、confirmationNumber（确认号）。 |

| **status**参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| state | 是 | String | 状态值。取值如下：  - active：生效  - inactive：未激活  - completed：已使用  - expired：已过期 |
| effectTime | 是 | String | 生效时间，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。 |
| expireTime | 是 | String | 失效时间，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。如果超过此时间，卡券自动按照expired状态处理。 |

| localized参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| key | 否 | String | 国际化键名。无固定值，根据实际需要国际化的字段传入对应键名即可。 |
| value | 否 | String | 国际化文本，对应语言的显示内容。 |
| language | 否 | String | 语言代码，如zh-CN、en-US。 |

| commonFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| ownerPassTypeIdentifier | 是 | String | 服务号，格式为：hwpass.xxx.xxx.xxx。 |
| readerMatchValue | 否 | String | 门票标识，建议不超过20个字节，第一字节表示开发者标识，第二字节表示品牌/系列标识，后续的字节用于保证开发者内唯一性。字符只能包含0-9和A-F。 |
| deviceType | 否 | String | 当前门票开通的设备类型，Phone：手机、Wear：穿戴。 |
| personalizedData | 否 | Object | 开发者个性化数据。 |
| logo | 否 | String | 卡面logo，128\*128px，大小<=20kb，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| backgroundImage | 否 | String | 卡面背景，1312\*820px，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| picUrl | 否 | String | 带logo的卡面背景，1312\*820px，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| merchantName | 否 | String | 卡面主标题，小于256字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| name | 否 | String | 卡面副标题，小于256字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| showQrCodeLink | 否 | String | 跳转开发者页面配置，json string格式。 |
| backgroundColor | 否 | String | 卡面背景颜色，如"#1A73E8"。 |
| maskColor | 否 | String | 遮罩颜色，如"#000000". |
| textColor | 否 | String | 文字颜色，如"#FFFFFF". |
| optionalIcon | 否 | String | 可选图标，小于64个字节。门票场景下可用来展示检票状态、入场标记等。 |

| showQrCodeLink参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| key | 是 | String | 跳转字段标识。 |
| value | 是 | String | 跳转字段值。 |

| harmonyNext参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| type | 是 | Integer | 跳转目标类型，3：开发者App、4：元服务/快应用。 |
| jumpInfo | 否 | jsonString | 跳转目标信息，[Want](js-apis-app-ability-want.md)类型，包含bundleName、abilityName、action、moduleName、parameters等字段。 |

| jumpInfo参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| bundleName | 否 | String | 目标应用包名。 |
| abilityName | 否 | String | 目标Ability名称。 |
| action | 否 | String | Action动作。 |
| moduleName | 否 | String | 模块名称。 |
| parameters | 否 | jsonString | 附加参数，键值对形式。 |

### 请求示例

```json
POST /hmspass/v2/key_ticket/instance HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "organizationPassId": "The122",
  "passTypeIdentifier": "hwpass.xxx.xxx",
  "passStyleIdentifier": "TicketModel001",
  "serialNumber": "The122",
  "organizationName": "XX景区",
  "fields": {
    "status": {
      "state": "active",
      "effectTime": "2019-11-11T00:00:00.000Z",
      "expireTime": "2060-12-31T23:59:59.999Z"
    },
    "barCode": {
      "text": "xxx",
      "type": "qrCode",
      "value": "xxx",
      "encoding": "UTF-8"
    },
    "commonFields": [
      {
        "key": "merchantName",
        "value": "XX景区",
        "label": "merchantName"
      },
      {
        "key": "name",
        "value": "XX门票",
        "label": "name"
      },
      {
        "key": "logo",
        "value": "https://xxx/xxx.png",
        "label": "logo"
      },
      {
        "key": "backgroundImage",
        "value": "https://xxx/xxx.webp",
        "label": "backgroundImage"
      },
      {
        "key": "picUrl",
        "value": "https://xxx/xxx.png",
        "label": "picUrl"
      },
      {
        "key": "showQrCodeLink",
        "value": "{\"harmonyNext\":{\"type\":3,\"jumpInfo\":{\"bundleName\":\"com.xxx.xxx\",\"abilityName\":\"MainAbility\",\"action\":\"home\",\"moduleName\":\"entry\",\"parameters\":{\"scene\":\"scene\"}}}}"
      },
      {
        "key": "backgroundColor",
        "value": "#1A73E8",
        "label": "backgroundColor"
      },
      {
        "key": "maskColor",
        "value": "#000000",
        "label": "maskColor"
      },
      {
        "key": "textColor",
        "value": "#FFFFFF",
        "label": "textColor"
      }
    ],
    "appendFields": [
      {
        "key": "isCreateWhiteCard",
        "value": "false",
        "label": "NFCCardFlag"
      },
      {
        "key": "seat",
        "value": "A12",
        "label": "座位"
      },
      {
        "key": "gate",
        "value": "东门",
        "label": "入口"
      }
    ],
    "flexFields": {
      "primaryFields": [
        {
          "key": "ticketNumber",
          "value": "xxx",
          "label": "票号"
        }
      ],
      "secondaryFields": [
        {
          "key": "venueOfPerformance",
          "value": "XX",
          "label": "演出场所"
        }
      ],
      "supplementaryFields": [
        {
          "key": "ticketStatus",
          "value": "有效",
          "label": "门票状态"
        }
      ]
    },
    "localized": [
      {
        "key": "ticketNumberLabel",
        "value": "票号",
        "language": "zh-CN"
      },
      {
        "key": "ticketNumberLabel",
        "value": "Ticket No.",
        "language": "en-US"
      }
    ]
  }
}
```

### 响应参数

返回结果中会携带预置模板中的信息一并返回。

### 调用示例

完整的调用示例，请参见[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)示例代码。

```java
public HwWalletObject invokeHwCreateKeyTicketObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keyticket.test");
    request.setPassStyleIdentifier("keyTicketModelTest");
    request.setOrganizationPassId("20001");
    request.setSerialNumber("20001");
    Fields fields = new Fields();
    fields.setCountryCode("CN");
    List<ValueObject> commonFields = new ArrayList<>();
    ValueObject seatNumber = new ValueObject();
    seatNumber.setKey("seatNumber");
    seatNumber.setValue("12A");
    commonFields.add(seatNumber);
    fields.setCommonFields(commonFields);
    request.setFields(fields);
    HttpHeaders header = constructHttpHeaders();
    String baseUrl = "https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass";
    String walletServerUrl = baseUrl + "/v2/key_ticket/instance";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.POST, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```

### 生成JWE数据

华为钱包门票卡片的开通是基于JWE（JSON Web Encryption）方式。因此开发者业务管理服务向钱包云服务申请创建门票成功后，基于创建成功的门票serialNumber生成JWE数据，并将其返回给开发者客户端。JWE数据包含JWE Encrypted Key，iv，Ciphertext，signature，可参见如下步骤获取：

1. 生成一个随机的CEK（Content Encryption Key）。
2. 使用RSA-OAEP加密算法，用钱包服务器给的公钥加密CEK，生成JWE Encrypted Key。
3. 生成JWE初始化向量。
4. 使用AES GCM加密算法对明文部分进行加密生成密文Ciphertext，算法会随之生成128位的认证标记Authentication Tag。对以上部分分别进行base64编码。
5. 使用开发者创建Wallet Kit服务生成的私钥对以上部分进行签名从而获取Signature。

完整的调用示例，请参见[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)示例代码。

```java
public static String generateJwe(String jwePrivateKey, String payload) {
    Map<String, String> jweHeader = getHeader();
    String jweHeaderEncode = getEncodeHeader(jweHeader);
    String sessionKey = generateSecureRandomFactor(16);
    String sessionKeyPublicKey = "MIIBojA****";
    String encryptedKeyEncode = getEncryptedKey(sessionKey, sessionKeyPublicKey);
    byte[] iv = AesUtil.getIvByte(12);
    String ivHexStr = new String(Hex.encodeHex(iv, false));
    String ivEncode = Base64.encodeBase64URLSafeString(ivHexStr.getBytes(StandardCharsets.UTF_8));
    String cipherTextEncode = getCipherText(payload, sessionKey, iv);
    String signature = getSignature(jwePrivateKey, sessionKey, payload, jweHeaderEncode, ivEncode);
    StringBuilder stringBuilder = new StringBuilder().append(jweHeaderEncode)
        .append(".")
        .append(encryptedKeyEncode)
        .append(".")
        .append(ivEncode)
        .append(".")
        .append(cipherTextEncode)
        .append(".")
        .append(signature);
    return stringBuilder.toString();
}
```

## 门票数据更新

更新门票卡片数据。

### 接口原型

* **承载协议**：HTTPS
* **请求方式**：PUT：全量更新；PATCH：局部更新
* **接口方向**：开发者业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/{cardType}/instance/{instanceId}
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 响应的数据格式，取值为：application/json;charset=UTF-8。 |

**Request Body**

参见[申请门票](wallet-rest-api-ticket.md#申请门票)的请求体，如果是全量更新，与申请门票接口请求体相同。如果是局部更新，则只需传入需要变更的数据体。

### 请求示例

```json
PATCH /hmspass/v2/key_ticket/instance/100005 HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "fields": {
    "commonFields": [
      {
        "value": "xxxx",
        "key": "personalizedData"
      }
    ]
  }
}
```

### 响应参数

http响应为200时表示成功。其他错误情况，可见[REST API错误码](wallet-rest-api-error-code.md)。

### 调用示例

```java
public HwWalletObject invokeHwCreateKeyTicketObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keyticket.test");
    request.setPassStyleIdentifier("keyTicketModelTest");
    request.setOrganizationPassId("20001");
    request.setSerialNumber("20001");
    Fields fields = new Fields();
    fields.setCountryCode("CN");
    List<ValueObject> commonFields = new ArrayList<>();
    ValueObject seatNumber = new ValueObject();
    seatNumber.setKey("seatNumber");
    seatNumber.setValue("12A");
    commonFields.add(seatNumber);
    fields.setCommonFields(commonFields);
    request.setFields(fields);
    HttpHeaders header = constructHttpHeaders();
    String baseUrl = "https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass";
    // 100005仅为instanceId的示例值，实际使用时请替换为真实的instanceId。
    String walletServerUrl = baseUrl + "/v2/key_ticket/instance/100005";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.PATCH, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```
