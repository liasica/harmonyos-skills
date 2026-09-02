---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-park
title: 园区卡接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 园区卡接口
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5ae561c799bf9426536a924cbbfbe18bc0e1a6f42cb4d925be1e7db8e68f10a5
---

## 预置模板

卡片模板的创建是接入流程的第一步，这一步可以通过http/https请求的方式向华为钱包云服务提供卡券样式的关键信息，如卡面主标题、副标题、logo、背景图片等，用于华为钱包园区卡页面的展示。

开发者可创建多个共享相同机构名和服务号但模板ID不同的模板。在申请园区卡时，每张卡必须绑定唯一的模板ID，即一个模板可被多张园区卡复用，而一张园区卡仅能关联一个模板ID。

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
| isCreateWhiteCard | 是 | String | 是否为NFC卡的标记。  true：NFC卡。  false：非NFC卡。 |

| commonFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| logo | 是 | String | 卡面logo，128\*128px，大小<=20kb，直角图片，无需切圆角。 |
| backgroundImage | 是 | String | 卡面背景  1312\*820px，直角图片，无需切圆角。 |
| picUrl | 是 | String | 带logo的卡面背景  1312\*820px，直角图片，无需切圆角。 |
| merchantName | 是 | String | 卡面主标题，小于256字节。 |
| name | 是 | String | 卡面副标题，小于256字节。 |

### 请求示例

```json
POST /hmspass/v2/key_park/model HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "passVersion": "10.0",
  "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
  "passStyleIdentifier": "keyParkModelTest",
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
        "value": "园区一卡通",
        "key": "merchantName"
      },
      {
        "label": "卡面副标题",
        "value": "XXX园区卡",
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
public HwWalletObject invokeHwCreateKeyParkClass(){
    HwWalletObject request=new HwWalletObject();
    request.setPassVersion("1.0");
    request.setPassTypeIdentifier("hwpass.keypark.test");
    request.setPassStyleIdentifier("keyParkModelTest");
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
    String walletServerUrl=baseUrl+"/v2/key_parkcard/model";
    HttpEntity<JSONObject> entity=new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)),header);
    ResponseEntity<JSONObject> exchange = REST_TEMPLATE.exchange(walletServerUrl,HttpMethod.POST,entity,JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(),HwWalletObject.class);
}
```

## 申请园区卡

开发者向开发者服务器申请开通园区卡，开发者服务器将园区卡卡片信息添加至钱包云服务中。其中：开发者App->开发者服务之间的交互由开发者自行实现，本章主要侧重于开发者服务器->钱包云服务申请园区卡的过程，主要包括：申请卡片和生成JWE数据。

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
| organizationPassId | 是 | String | 园区卡卡片在开发者服务器中的卡号。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和serialNumber保持一致。 |
| serialNumber | 是 | String | 园区卡卡片在华为钱包服务器中的卡号，即instanceId。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和organizationPassId保持一致。 |
| fields | 是 | fields | 卡券展示信息，包括commonFields、status、localized部分。 |
| linkDevicePass | 是 | linkDevicePass | 链接设备参数，用于保存园区卡管理台服务器地址、公钥信息以及是否使能卡券的NFC能力。 |

| **status**参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| state | 是 | String | 状态值。取值如下：  - active：生效  - inactive：未激活  - completed：已使用  - expired：已过期 |
| effectTime | 否 | String | 生效时间，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。 |
| expireTime | 否 | String | 失效时间，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。如果超过此时间，卡券自动按照expired状态处理。 |

| localized参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| key | 否 | String | 国际化键名。无固定值，根据实际需要国际化的字段传入对应键名即可。 |
| value | 否 | String | 国际化文本，对应语言的显示内容。 |
| language | 否 | String | 语言代码，如zh-CN、en-US。 |

| commonFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| ownerPassTypeIdentifier | 是 | String | 服务号，格式为：hwpass.xxx.xxx.xxx。 |
| readerMatchValue | 是 | String | 园区卡标识，建议不超过20个字节，第一字节表示开发者标识，第二字节表示品牌/系列标识，后续的字节用于保证开发者内唯一性。字符只能包含0-9和A-F。 |
| deviceType | 是 | String | 当前园区卡开通的设备类型，Phone：手机，Wear：穿戴。 |
| personalizedData | 否 | Object | 开发者个性化数据。 |
| logo | 否 | String | 卡面logo，128\*128px，大小<=20kb，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| backgroundImage | 否 | String | 卡面背景，1312\*820px，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| picUrl | 否 | String | 带logo的卡面背景，1312\*820px，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| merchantName | 否 | String | 卡面主标题，小于256字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| name | 否 | String | 卡面副标题，小于256字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |

| linkDevicePass参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| webServiceURL | 是 | String | 开发者业务管理服务地址，用于开通激活过程中向开发者业务管理服务发起设备认证、获取个人化token以及获取个人化数据。 |
| token | 是 | String | 认证信息，开发者业务管理服务自行生成，没有格式要求，用于开通激活过程中钱包向开发者业务管理服务进行“[设备认证](wallet-rest-api-public.md#设备认证)”和“[获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)”请求头中携带的Authorization信息。 |
| serialNumber | 是 | String | 请和上述提及的serialNumber保持一致。 |
| passVersion | 否 | String | Pass版本，固定“10.0”。 |
| spPublickey | 是 | String | 开发者创建Wallet Kit服务生成的公钥。用于对开发者业务管理服务返回的“Applet个人化数据”进行验签。NFC卡片信息不会上传到钱包云服务器，所以终端设备需要这个参数来进行验签。 |
| nfcType | 是 | String | 是否开启NFC能力。  1：开启。  0：不开启。  固定取'1'。 |

### 请求示例

```json
POST /hmspass/v2/key_park/instance HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "organizationPassId": "5623489234",
  "passTypeIdentifier": "hwpass.type.parkcard.test",
  "passStyleIdentifier": "class_parkcard_Test",
  "serialNumber": "70001",
  "fields": {
    "status": {
      "state": "active",
      "effectTime": "2019-11-13T00:00:00.111Z",
      "expireTime": "2020-11-20T00:00:00.111Z"
    },
     "commonFields": [
       {
         "key": "merchantName",
         "value": "XX",
         "label": "merchantName"
       },
       {
         "key": "name",
         "value": "XX园区卡",
         "label": "name"
       },
       {
         "key": "backgroundImage",
         "value": "https://xxx/xxx.webp",
         "label": "backgroundImage"
       },
       {
         "key": "logo",
         "value": "https://xxx/xxx.png",
         "label": "logo"
       },
       {
         "key": "picUrl",
         "value": "https://xxx/xxx.png",
         "label": "picUrl"
       }
     ],
     "localized": [
       {
         "key": "merchantName",
         "value": "XX",
         "language": "zh-CN"
       }
     ]
   },
   "linkDevicePass": {
     "webServiceURL": "https://xxx/xxx",
     "token": "xxx",
     "serialNumber": "xxx",
     "passVersion": "10.0",
     "spPublickey": "xxx",
     "nfcType": "1"
   }
}
```

### 响应参数

返回结果中会携带预置模板中的信息一并返回。

### 调用示例

完整的调用示例，请参见[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)示例代码。

```java
public HwWalletObject invokeHwCreateKeyParkObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keypark.test");
    request.setPassStyleIdentifier("keyParkModelTest");
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
    String walletServerUrl = baseUrl + "/v2/key_parkcard/instance";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.POST, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```

### 生成JWE数据

华为钱包园区卡卡片的开通是基于JWE（JSON Web Encryption）方式。因此开发者业务管理服务向钱包云服务申请创建园区卡成功后，基于创建成功的园区卡serialNumber生成JWE数据，并将其返回给开发者客户端。JWE数据包含JWE Encrypted Key，iv，Ciphertext，signature，可参见如下步骤获取：

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

## 园区卡数据更新

更新园区卡卡片数据。

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

参见[申请园区卡](wallet-rest-api-park.md#申请园区卡)的请求体，如果是全量更新，与申请园区卡接口请求体相同。如果是局部更新，则只需传入需要变更的数据体。

### 请求示例

```json
PATCH /hmspass/v2/key_park/instance/100004 HTTP/1.1
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
public HwWalletObject invokeHwCreateKeyParkObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keypark.test");
    request.setPassStyleIdentifier("keyParkModelTest");
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
    // 100004仅为instanceId的示例值，实际使用时请替换为真实的instanceId。
    String walletServerUrl = baseUrl + "/v2/key_parkcard/instance/100004";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.PATCH, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```

## 申请二维码

通过此接口获取指定数量及类型的在线二维码，二维码有效期在接口返回值中指定。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：{webServiceURL}/v1/createAuthCode
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| signType | 是 | String | 签名方式。固定值：'SHA256WithRSA/PSS'。 |
| sign | 是 | String | 对整个消息体的签名值。 |
| signVersion | 否 | String | 本次签名使用的秘钥版本号，默认值为0。 |
| version | 是 | String | 接口版本号，固定值：'V1'。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| apiKey | 是 | String | 华为钱包发起请求时的标识，默认为HuaweiWallet，用于关联对应的公行验签。 |
| passType | 是 | String | 服务号，通知扫码结果时回传。 |
| serialNumber | 是 | String | Pass对象在发卡方的唯一键值，通知扫码结果时回传以便根据此值识别具体的卡券。 |
| userDeviceId | 是 | String | 账号设备唯一标识，申请二维码时传入，通知结果时回传，用于关联对应的设备。 |
| timestamp | 是 | String | 请求时间戳，格式 yyyyMMddHHmmss，校验请求消息送达时间为10分钟以内。 |
| transId | 是 | String | 请求唯一标识，为随机数。 |
| paymentType | 否 | String | 预留，传入时获取指定类型的二维码。 |
| qrCodeNumber | 否 | String | 单次获取的数量。 |
| queryInfo | 否 | Json | 其他信息，用于开发者基于此信息关联细化。 |

| QueryInfo参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| cardBusinessType | 否 | String | 卡片业务类型，Pass中包含此字段时传递。 |

### 请求示例

```json
POST /v1/createAuthCode HTTP/1.1
Content-Type: application/json;charset=UTF-8
signType: SHA256WithRSA/PSS
sign: u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExH********************g
signVersion: 0
version: V1
{
  "apiKey": "HuaweiWallet",
  "passType": "hwpass.xxx.xxx",
  "serialNumber": "xxx",
  "userDeviceId": "xxx",
  "timestamp": "202605056112022",
  "transId": "xxx",
  "paymentType": "xxx",
  "qrCodeNumber": "xxx",
  "queryInfo": {
    "cardBusinessType": "xxx"
  }
}
```

### 响应参数

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 响应结果码。200：成功、其他：失败。 |
| resultDesc | 是 | String | 返回值描述。success: 成功、其他：失败。 |
| supportPaymentType | 否 | String | 预留，规划用于返回支持的二维码类型，暂不启用，可提前约定通过PassType属性配置。 |
| qrCodeInfo | 是 | Json | 数组类型，二维码列表。 |

| QrCodeInfo参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| qrCode | 是 | String | 码值，用于呈现二维码。 |
| validTime | 是 | String | 二维码有效期，以分钟为单位。 |

### 调用示例

```java
public HwWalletObject applyAuthCode(@RequestBody ApplyAuthCodeRequest request, @RequestHeaders Map<String, String> headers) {
    String version = headerMaps.get("version");
    String signType = headerMaps.get("HMSSignType");
    String sign = headerMaps.get("HMSSign");
    String signContent = ToStringUtil.signString(request);
    String verifyHwClientSignPubKey = "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA5w4ii7rh2J6B371m02C+FBFgp9vZ8aS6nv5nBdAaMWpETj6bzZ1rFiGFF99o7qSbbh63cKgic0dARMed6HClOC5QGB7o16FwZGemrjN/z8/4dXc5OcUVs8BuebeJC4OvKTT7roQ7p9GuGgg1jrGgFkfC+nkWGt3ePE0tiXJfH5f341X1OyKHSjdF5N6QYM0m73+XxS1foq3IyyIHrjq4I9uH1QjpFOF+9jo35bAYcNUquONUd6J55gAc/Cztje6KfNmKBz24zwwoRkbXmNcaphK/t/z5N3FZsiS70GFv6iABXBR7j6ceaWzs24oQ2A1LuakXNN2ORnVnj8laSxlMpey5Ci+eicU+mL1ivixGDmDhCgT4u4tj4vvD/AV+z88nUR83muwZ3+J3ASBFZVaBrMeeX6o+8rn+iK+WvP5SLL2DLpffiMX0QqwA6C/RVW8KDh8Jq9yNkE0Uy81yVO0BJctY6t35d0fucLmwTa2YMSqV12dDfeMZjxMDhmJVDUD/AgMBAAE=";
    verifySignature(signContent, verifyHwSignPubKey, sign);
    String serialNumber = request.getSerialNumber();
    String userDeviceId = request.getUserDeviceId();
    ApplyAuthCodeResponse response = new ApplyAuthCodeResponse();
    response.setResultCode("200");
    response.setResultDesc("success");
    response.setSupportPaymentType("1");
    response.setCodeList(xxx);
    return response;
}
```

## 通知扫码结果

扫码后，SP Server通过此接口，推送签名后的扫码结果至钱包服务器。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者业务管理服务->钱包云服务
* **接口URL**：{webServiceURL}/hmspass/v1/scanResultNotify
* **数据格式**：

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/x-www-form-urlencoded。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 响应的数据格式，取值为：application/json;charset=UTF-8。 |
| signType | 是 | String | 签名方式。固定值：'SHA256WithRSA/PSS'。 |
| sign | 是 | String | 对整个消息体的签名值。 |
| signVersion | 否 | String | 本次签名使用的秘钥版本号，默认值为0。 |
| version | 是 | String | 接口版本号，固定值：'V1'。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| appId | 是 | String | 调用方身份标识，关联对应的公钥进行验签。 |
| passType | 是 | String | 服务号。 |
| serialNumber | 是 | String | Pass对象在发卡方的唯一键值，回调时以便发卡方根据此值识别具体的卡券。 |
| userDeviceId | 是 | String | 账号设备唯一标识，申请二维码时传入，通知结果时回传，用于关联对应的设备。 |
| timestamp | 是 | String | 请求时间戳，格式 yyyyMMddHHmmss，校验请求消息送达时间为10分钟以内。 |
| transId | 是 | String | 请求唯一标识，为随机数。 |
| notifyType | 是 | String | 通知类型。1：预留、2：扫码结果通知。 |
| qrCode | 是 | String | 码值，用于指定当前扫码结果关联的二维码。 |
| paymentInfo | 是 | Json | 扫码结果，notifyType取值为2时必填。 |

| paymentInfo参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| transAmount | 是 | String | 交易金额。 |
| discountAmount | 否 | String | 优惠信息。 |
| leftBalance | 否 | String | 余额，无此信息时可不传入。 |
| transTime | 是 | String | 交易实际发生时间，格式yyyyMMddHHmmss。 |
| merchantName | 是 | String | 交易商户名称。 |
| transDesc | 否 | String | 交易结果描述，默认为消费成功，预留。 |

### 请求示例

```json
POST /hmspass/v1/scanResultNotify HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
signType: SHA256WithRSA/PSS
sign: u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExH********************g
signVersion: 0
version: V1
{
  "appId": "xxx",
  "passType": "hwpass.xxx.xxx",
  "serialNumber": "xxx",
  "userDeviceId": "xxx",
  "timestamp": "202605056112022",
  "transId": "xxx",
  "notifyType": "xxx",
  "qrCode": "xxx",
  "paymentInfo": {
    "transAmount": "1",
    "discountAmount": "1",
    "leftBalance": "1",
    "transTime": "202605056112022",
    "merchantName": "xxx",
    "transDesc": "xxx",
  }
}
```

### 响应参数

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 响应结果码。200：成功、其他：失败。 |
| resultDesc | 是 | String | 返回值描述。success: 成功、其他：失败。 |

### 调用示例

```java
public HwWalletObject invokeHwScanResultNotify() {
    ScanResultNotifyRequest request = new ScanResultNotifyRequest();
    request.setPassTypeIdentifier("xxx");
    request.setSerialNumber("xxx");
    request.setPassVersion("xxx");
    request.setUserDeviceId("xxx");
    request.setTimestamp("2026-01-01 00:00:00.000");
    request.setTransId("202601010000000001234567");
    request.setNotifyType("2");
    PaymentInfo paymentInfo = new PaymentInfo();
    paymentInfo.setTransAmount("10");
    paymentInfo.setDiscountAmount("xxx");
    paymentInfo.setLeftBalance("20");
    paymentInfo.setTransTime("20260101000000");
    paymentInfo.setMerchantName("xxx");
    paymentInfo.setTransDesc("xxx");
    request.setPaymentInfo(paymentInfo);
    HttpHeaders header = constructHttpHeaders();
    String baseUrl = "https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass";
    String walletServerUrl = baseUrl + "/v1/scanResultNotify";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.POST, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), BaseResponse.class);
}
```
