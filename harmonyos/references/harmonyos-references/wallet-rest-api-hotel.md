---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-hotel
title: 酒店房卡接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 酒店房卡接口
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:21e623110c51de464a4e9cc89b6cef873d34283be6313170cabe5eb8593159d1
---

## 预置模板

卡片模板的创建是接入流程的第一步，这一步可以通过http/https请求的方式向华为钱包云服务提供卡券样式的关键信息，如卡面主标题、副标题、logo、背景图片等，用于华为钱包酒店房卡页面的展示。

开发者可创建多个共享相同机构名和服务号但模板ID不同的模板。在申请酒店房卡时，每张卡必须绑定唯一的模板ID，即一个模板可被多张酒店房卡复用，而一张酒店房卡仅能关联一个模板ID。

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
POST /hmspass/v2/key_hotel/model HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "passVersion": "10.0",
  "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
  "passStyleIdentifier": "keyHotelModelTest",
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
        "value": "酒店房卡",
        "key": "merchantName"
      },
      {
        "label": "卡面副标题",
        "value": "XXX酒店房卡",
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
public HwWalletObject invokeHwCreateKeyHotelClass(){
    HwWalletObject request=new HwWalletObject();
    request.setPassVersion("1.0");
    request.setPassTypeIdentifier("hwpass.keyhotel.test");
    request.setPassStyleIdentifier("keyHotelModelTest");
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
    String walletServerUrl=baseUrl+"/v2/key_hotel/model";
    HttpEntity<JSONObject> entity=new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)),header);
    ResponseEntity<JSONObject> exchange = REST_TEMPLATE.exchange(walletServerUrl,HttpMethod.POST,entity,JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(),HwWalletObject.class);
}
```

## 申请酒店房卡

开发者向开发者服务器申请开通酒店房卡，开发者服务器将酒店房卡卡片信息添加至钱包云服务中。其中：开发者App->开发者服务之间的交互由开发者自行实现，本章主要侧重于开发者服务器->钱包云服务申请酒店房卡的过程，主要包括：申请卡片和生成JWE数据。

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
| organizationPassId | 是 | String | 酒店房卡卡片在开发者服务器中的卡号。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和serialNumber保持一致。 |
| serialNumber | 是 | String | 酒店房卡卡片在华为钱包服务器中的卡号，即instanceId。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和organizationPassId保持一致。 |
| fields | 是 | fields | 卡券展示信息，包括commonFields、timeList和status三部分。 |
| linkDevicePass | 是 | linkDevicePass | 链接设备参数，用于保存酒店房卡管理台服务器地址、公钥信息以及是否使能卡券的NFC能力。 |

| **timeList**参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| linkDevicePassExpireTime | 是 | List | 时间列表。 |

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
| readerMatchValue | 是 | String | 酒店房卡标识，建议不超过20个字节，第一字节表示开发者标识，第二字节表示品牌/系列标识，后续的字节用于保证开发者内唯一性。字符只能包含0-9和A-F。 |
| deviceType | 是 | String | 当前酒店房卡开通的设备类型，Phone：手机，Wear：穿戴。 |
| personalizedData | 否 | Object | 开发者个性化数据。 |
| logo | 否 | String | 卡面logo，128\*128px，大小<=20kb，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| backgroundImage | 否 | String | 卡面背景，1312\*820px，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| picUrl | 否 | String | 带logo的卡面背景，1312\*820px，直角图片，无需切圆角。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| merchantName | 否 | String | 卡面主标题，小于256字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| name | 否 | String | 卡面副标题，小于256字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| isShowQueryRoomNumber | 否 | String | 是否显示查询房间号。true：显示、false：不显示。 |

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
POST /hmspass/v2/key_hotel/instance HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "organizationPassId": "5623489234",
  "passTypeIdentifier": "hwpass.type.hotel.test",
  "passStyleIdentifier": "hwpass.type.hotel.test",
  "serialNumber": "70001",
  "fields": {
    "status": {
      "state": "active",
      "effectTime": "2019-11-13T00:00:00.111Z",
      "expireTime": "2020-11-20T00:00:00.111Z"
    },
    "barCode": {
      "text": "562348969211212",
      "type": "codabar",
      "value": "562348969211212",
      "encoding": "UTF-8"
    },
    "commonFields": [
      {
        "key": "cardNumber",
        "value": "12345678",
        "label": "cardNumber"
      }
    ],
    "appendFields": [
      {
        "key": "isCreateWhiteCard",
        "value": "true",
        "label": "NFCCardFlag"
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
public HwWalletObject invokeHwCreateKeyHotelObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keyhotel.test");
    request.setPassStyleIdentifier("keyHotelModelTest");
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
    String walletServerUrl = baseUrl + "/v2/key_hotel/instance";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.POST, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```

### 生成JWE数据

华为钱包酒店房卡卡片的开通是基于JWE（JSON Web Encryption）方式。因此开发者业务管理服务向钱包云服务申请创建酒店房卡成功后，基于创建成功的酒店房卡serialNumber生成JWE数据，并将其返回给开发者客户端。JWE数据包含JWE Encrypted Key，iv，Ciphertext，signature，可参见如下步骤获取：

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

## 酒店房卡数据更新

更新酒店房卡卡片数据。

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

参见[申请酒店房卡](wallet-rest-api-hotel.md#申请酒店房卡)的请求体，如果是全量更新，与申请酒店房卡接口请求体相同。如果是局部更新，则只需传入需要变更的数据体。

### 请求示例

```json
PATCH /hmspass/v2/key_hotel/instance/100002 HTTP/1.1
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
public HwWalletObject invokeHwCreateKeyHotelObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keyhotel.test");
    request.setPassStyleIdentifier("keyHotelModelTest");
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
    // 100002仅为instanceId的示例值，实际使用时请替换为真实的instanceId。
    String walletServerUrl = baseUrl + "/v2/key_hotel/instance/100002";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.PATCH, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```

## 获取酒店个人化数据

华为钱包App经由钱包云服务中转后向开发者业务管理服务获取个人化数据。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：{webServiceURL}/v1/passes/requestHotelPersonalize
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 是 | 注册Wallet Kit服务时指定的服务号。 |
| requestBody | serialNumber | String | 是 | Pass对象在发卡方的唯一键值，回调时以便发卡方根据此值识别具体的卡片记录。 |
| requestBody | passVersion | String | 否 | 版本号，固定“10.0”。 |
| requestBody | userDeviceId | String | 是 | 用户在当前设备上的唯一标识。 |
| requestBody | transPublicKey | String | 是 | 用于加密返回的对称秘钥，用于对返回的数据做数字信封。 |
| requestBody | timestamp | String | 是 | 时间戳，参与签名，用于防重放攻击。格式yyyymmddHH24MissSSS。 |
| requestBody | updateFlag | String | 否 | 用于标识本次接口调用的意图，预留，默认为获取指定订单的酒店房卡数据。 |
| requestBody | orderNo | String | 否 | 订单号，Pass数据中存在时携带，取值不为空时参与签名；酒店系统返回匹配订单号的空发数据。 |
| signature | - | String | 是 | 钱包服务器对requestbody的Hash签名。 |

### 请求示例

```json
POST /v1/passes/requestHotelPersonalize HTTP/1.1
Content-Type: application/json;charset=UTF-8
{
  "requestBody": {
    "transPublicKey": "xxx",
    "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "858947076d58a5e66ee22b9ed1c43c4d",
    "userDeviceId": "xxx",
    "timestamp": "xxx",
    "updateFlag": "xxx",
    "orderNo": "xxx",
  },
  "signature": "xxx"
}
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 响应的数据类型，取值为：application/json;charset=UTF-8。 |

**Response Body**

| 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| httpStatus | String | 是 | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| resultCode | String | 是 | 0：空发写卡，需传入空发的个人化数据。1：仅开卡，不包含写卡的个人化数据，前台提示用户开卡完成，提示用户需要写卡后使用。 |
| encryptSessionKey | String | 否 | 酒店云侧管理服务使用请求中的transPublicKey加密生成的sessionKey。采用Base64编码，resultCode取值为0时必选。 |
| encryptDevicePass | String | 否 | 固定取值为空字符串：''。 |
| encryptAppletPersonalizeFields | String | 否 | 酒店云侧管理服务通过生成的sessionKey加密Applet的个人化参数密文。采用Base64编码，resultCode取值为0时必选。 |
| signature | String | 是 | 使用酒店云侧管理服务的私钥对response的Hash值进行签名。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "resultCode": "0",
  "encryptSessionKey": "xxx",
  "encryptDevicePass": "xxx",
  "encryptAppletPersonalizeFields": "xxx",
  "signature": "xxx"
}
```

## 酒店房卡检测更新

携带卡片唯一标识，申请检测用户信息是否有变化，由用户行为触发，每张卡片每日最多调用一次。若存在会员等级等信息变化，需通过酒店卡更新接口先更新完成，再应答结果，结果中包含是否有变化的检测结果。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：{webServiceURL}/v1/passes/detectChange
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 是 | 注册Wallet Kit服务时指定的服务号。 |
| requestBody | serialNumber | String | 是 | Pass对象在发卡方的唯一键值，回调时以便发卡方根据此值识别具体的卡片记录。 |
| requestBody | timestamp | String | 是 | 参与签名，用于防重放攻击，格式yyyymmddHH24MissSSS。 |
| requestBody | detectMode | String | 否 | 用于标识本次检测的数据范围。 |
| signature | - | String | 是 | 钱包服务器对requestbody的Hash签名。 |

### 请求示例

```json
POST /v1/passes/detectChange HTTP/1.1
Content-Type: application/json;charset=UTF-8
{
  "requestBody": {
    "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "timestamp": "xxx",
    "detectMode": "xxx",
  },
  "signature": "xxx"
}
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 响应的数据类型，取值为：application/json;charset=UTF-8。 |

**Response Body**

| 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| Httpstatus | String | 是 | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| resultCode | String | 是 | 0：空发写卡，需传入空发的个人化数据。1：仅开卡，不包含写卡的个人化数据，前台提示用户开卡完成，提示用户需要写卡后使用。 |
| signature | String | 是 | 使用酒店云侧管理服务的私钥对response的Hash值进行签名。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "resultCode": "0",
  "signature": "xxx"
}
```
