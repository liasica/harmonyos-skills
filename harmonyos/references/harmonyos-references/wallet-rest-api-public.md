---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-public
title: 公共接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 公共接口
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44b133ed7405953669bf3ebed6604fa29873e9c36a1fe92ba592013f0bc19204
---

## 获取AccessToken

此接口用于获取访问token，向钱包云服务的每次https请求都需要传入访问的token，该token相当于一个访问许可，钱包云服务器收到其请求时会对其进行校验。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者业务管理服务->钱包云服务
* **接口URL**：https://oauth-login.cloud.huawei.com/oauth2/v3/token
* **数据格式**：

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/x-www-form-urlencoded。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| grant\_type | 是 | String | 填写为“client\_credentials”，表示为客户端模式。 |
| client\_id | 是 | String | 在[应用开发准备](../harmonyos-guides/application-dev-overview.md)中得到的客户端ID，可从“项目设置 > 常规 > 应用 > APP ID”获取。 |
| client\_secret | 是 | String | 在[应用开发准备](../harmonyos-guides/application-dev-overview.md)中给客户端ID分配的密钥，可从“项目设置 > 常规 > 应用 > Client Secret”获取。 |

### 请求示例

```http
POST /oauth2/v3/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials&client_id=<客户端ID>&client_secret=<客户端密钥>
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 响应的数据类型，取值为：application/json;charset=UTF-8。 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| token\_type | 是 | String | 固定字符串“Bearer”。 |
| access\_token | 是 | String | Access Token。 |
| expires\_in | 否 | Long | Access Token的过期时间，以秒为单位。默认60分钟过期。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "access_token": "<返回的Access Token>",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```

### 调用示例

```java
public static String getToken(String clientId, String clientSecret) {
    HttpHeaders header = new HttpHeaders();
    header.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

    MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
    map.add("grant_type", "client_credentials");
    map.add("client_id", clientId);
    map.add("client_secret", clientSecret);

    String tokenUrl = ConfigUtil.instants().getValue("gw.tokenUrl");

    HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(tokenUrl, HttpMethod.POST, entity, JSONObject.class);

    JSONObject response = exchange.getBody();
    if (response == null) {
        throw new NullPointerException("Get null token response.");
    }
    String accessToken = response.getString("access_token");
    if (Strings.isEmpty(accessToken)) {
        throw new NullPointerException("Get null access token.");
    }
    return accessToken;
}
```

## 设备认证

预个人化执行完成后，华为钱包App经由钱包云服务中转后请求认证设备，将applet身份公钥以及身份公钥的钱包服务器签名携带在请求体中，向开发者业务管理服务请求认证授权证书。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：https://{webServiceURL}/v1/passes/registrations
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

**说明** 

webServiceURL为开发者业务管理服务域名。

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | [申请ICCE钥匙](wallet-rest-api-carkey.md#申请icce钥匙)时linkDevicePass参数中的token值，用于校验该请求是否合法。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 是 | 创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 是 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | passVersion | String | 否 | 版本号，固定“10.0”。 |
| requestBody | userDeviceId | String | 是 | 用户在当前设备上的唯一标识。 |
| requestBody | transId | String | 是 | 请求唯一标识，为随机数。 |
| requestBody | openId | String | 否 | 华为账号的openId，用于发卡方关联华为账号。 |
| signature | - | String | 是 | Applet的身份私钥对requestBody的SHA256 Hash值的签名。签名算法：SHA256withECDSA（园区卡）或SHA256WithRSAandMGF1（其他卡类型）。 |
| certificate | signature | String | 是 | 钱包云服务使用钱包服务器私钥对publicKey的签名值。开发者业务管理服务收到该请求后，需要使用钱包云服务公钥对其进行验签。 |
| certificate | publicKey | String | 是 | Applet的身份公钥。 |

### 请求示例

```json
POST /v1/passes/registrations HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
{
  "requestBody": {
    "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "16198381994485116358",
    "userDeviceId": "xxx",
    "openId": "xxx"
  },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
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

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | String | 是 | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| response | certificate | Certificate | 否 | 开发者业务管理服务使用创建Wallet Kit服务时生成的私钥对publicKey进行签名后返回。 |

**Certificate参数类型说明**

| certificate子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| signature | String | 是 | 钱包云服务使用钱包服务器私钥对publicKey的签名值。开发者业务管理服务收到该请求后，需要使用钱包云服务公钥对其进行验签。 |
| publicKey | String | 是 | Applet的身份公钥。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "response": {
    "certificate": {
      "signature": "xxx",
      "publicKey": "xxx"
    }
  }
}
```

### 开发者业务管理服务处理调用示例

完整的调用示例，请参见[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)示例代码。

```java
public RegistrationsResponse dealWithRegisterRequest(String token, RegistrationsRequest request) {
    RegistrationsResponse response = new RegistrationsResponse();
    if (token == null) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
        return response;
    }
    if (!ParamChecker.isValidRegistrationsRequest(request)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
        return response;
    }
    Certificate walletCertificate = request.getCertificate();
    if (!verifyWalletCert(walletCertificate)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
        return response;
    }

    if (!ParamChecker.hashSignatureCheck(request.toJsonString(), request.getSignature(),
            appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
        return response;
    }

    String userDeviceId = request.getRequestBody().getUserDeviceId();
    response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_OK));
    Response responseBody = new Response();
    Certificate serverCert = PassData.getServerCert(appletAuthPublicKey);
    responseBody.setCertificate(serverCert);
    response.setResponse(responseBody);
    deviceIdCertMap.put(userDeviceId, serverCert);
    return response;
}
```

## 获取个人化数据Token

华为钱包App经由钱包云服务中转后向开发者业务管理服务平台获取token（个人化数据请求报文里参与计算hash）。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：https://{webServiceURL}/v1/passes/requestPersonalizeToken
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | [申请ICCE钥匙](wallet-rest-api-carkey.md#申请icce钥匙)时linkDevicePass参数中的token值，用于校验该请求是否合法。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 是 | 创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 是 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | passVersion | String | 否 | 版本号，固定“10.0”。 |
| requestBody | userDeviceId | String | 是 | 用户在当前设备上的唯一标识。 |
| requestBody | transId | String | 是 | 请求唯一标识，为随机数。 |
| signature | - | String | 是 | Applet的身份私钥对requestBody的SHA256 Hash值的签名。签名算法：SHA256withECDSA（园区卡）或SHA256WithRSAandMGF1（其他卡类型）。 |
| certificate | signature | String | 是 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate的签名。  开发者业务管理服务使用创建Wallet Kit服务时生成的私钥对Applet的身份公钥签名信息。 |
| certificate | publicKey | String | 是 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate里的Applet的身份公钥。 |

### 请求示例

```json
POST /v1/passes/requestPersonalizeToken HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
{
  "requestBody": {
    "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "16198381994485116358",
    "userDeviceId": "xxx"
  },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
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

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | String | 是 | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| response | token | String | 是 | 个人化token。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "response": {
    "token": "sp.token.1619838979341"
  }
}
```

### 开发者业务管理服务处理调用示例

完整的调用示例，请参见[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)示例代码。

```java
public RequestTokenResponse dealWithTokenRequest(RequestTokenRequest request) {
    RequestTokenResponse response = new RequestTokenResponse();
    String userDeviceId = request.getRequestBody().getUserDeviceId();
    Certificate spCertFromRequest = request.getCertificate();
    if (CommonUtils.isStringEmpty(userDeviceId) || !ParamChecker.checkSpServerCertificate(spCertFromRequest)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
        return response;
    }
    Certificate cachedCert = deviceIdCertMap.get(userDeviceId);
    if (cachedCert == null) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
        return response;
    }
    if (!ParamChecker.hashSignatureCheck(request.toJsonString(), request.getSignature(),
            appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
        return response;
    }
    response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_OK));
    Response responseBody = new Response();
    String personalizeToken = PassData.getPersonalizeToken();
    responseBody.setToken(personalizeToken);
    deviceIdTokenMap.put(userDeviceId, personalizeToken);
    response.setResponse(responseBody);
    return response;
}
```

## 获取个人化数据

华为钱包App经由钱包云服务中转后向开发者业务管理服务获取个人化数据。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：https://{webServiceURL}/v1/passes/requestPersonalize
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | [获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)返回的token值，用于校验该请求是否合法。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | cardSEId | String | 是 | Applet唯一标识，可以用于车端秘钥分散 |
| requestBody | passTypeIdentifier | String | 是 | 创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 是 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | passVersion | String | 否 | 版本号，固定“10.0”。 |
| requestBody | userDeviceId | String | 是 | 用户在当前设备上的唯一标识。 |
| requestBody | personalizePublicKey | String | 是 | Applet的个人化公钥，用于加密个人化字段值。 |
| requestBody | personalizeCert | String | 是 | Applet身份私钥对个人化公钥personalizePublicKey的签名。 |
| requestBody | personalizeCertType | String | 是 | 固定值，默认为私钥签名。 |
| requestBody | transPublicKey | String | 是 | 用于加密返回的对称秘钥，用于对返回的数据做数字信封。 |
| requestBody | transId | String | 是 | 事务流水，用于拼接返回的对称秘钥。 |
| signature | - | String | 是 | Applet的身份私钥对requestBody的SHA256 Hash值的签名。[获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)作为其中requestbody一个key参与Hash值计算。签名算法：SHA256withECDSA（园区卡）或SHA256WithRSAandMGF1（其他卡类型）。 |
| certificate | signature | String | 是 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate的签名。  开发者业务管理服务使用创建Wallet Kit服务时生成的私钥对Applet的身份公钥签名信息。 |
| certificate | publicKey | String | 是 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate里的Applet的身份公钥。 |

### 请求示例

```json
POST /v1/passes/requestPersonalize HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
{
  "requestBody": {
    "cardSEId": "xxxxxxxxxxxxxxxx",
    "personalizeCert": "xxx",
    "personalizeCertType": "",
    "personalizePublicKey": "xxx",
    "transPublicKey": "xxx",
    "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "858947076d58a5e66ee22b9ed1c43c4d",
    "userDeviceId": "xxx"
  },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
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

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | String | 是 | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| response | encryptSessionKey | String | 是 | 开发者业务管理服务使用请求中的transPublicKey加密生成的sessionKey。采用Base64编码，加密前的字段说明：开发者生成AES128的aesKey和aesIv，用于加密生成encryptAppletPersonalizeFields和encryptDevicePass。使用请求中transPublicKey字段加密transId+aesKey+aesIv，对结果进行base64编码即得到encryptSessionKey。加密算法: RSA/ECB/OAEPWithSHA-256AndMGF1Padding。 |
| response | encryptDevicePass | String | 否 | 空字符串"" |
| response | encryptAppletPersonalizeFields | String | 是 | 用于蓝牙/NFC刷卡时的认证以及数据加解密操作。开发者业务管理服务通过生成的sessionKey加密Applet的个人化参数密文。采用Base64编码 |
| signature | - | String | 是 | 使用开发者业务管理服务的私钥对response的Hash值进行签名，生成的签名值。私钥请和开卡过程中下发的linkDevicePass参数中的spPublicKey保持一对。 |

| encryptAppletPersonalizeFields子节点参数 | 类型 | 是否必选 | 存储格式 | 描述 |
| --- | --- | --- | --- | --- |
| temp\_key | String | 是 | - | aesKey（AES128的key），长度16个字节，用于加密CardId，cardPrivateInfo信息。temp\_key：aesKey明文之前拼接一个固定的十六进制字符前缀"34810233"后，使用Applet个人化公钥appletPublicKey对其进行加密。加密算法RSA/NONE/OAEPWithSHA1AndMGF1Padding。 |
| temp\_iv | String | 是 | - | aesIv（AES128的iv），长度16个字节，用于applet解密写卡数据。temp\_iv：aesIv使用Applet个人化公钥appletPublicKey加密。加密算法RSA/NONE/OAEPWithSHA1AndMGF1Padding。 |
| card\_id | String | 是 | 9F3B + Lc + CardId | 发卡方发放的卡片唯一标识，长度16个字节。TLV格式存储：T=9F3B，Lc=10，V=CardId；加密方式：明文数据补800...00到16个字节整数倍，使用aesKey，aesIv对整个TLV加密，并转换成十六进制字符串。CBC模式加密，加密算法：AES/CBC/NoPadding。 |
| card\_key | String | 是 | - | 发卡方发放的卡片密钥，16个字节，一张卡支持1个秘钥，计算SessionKey时使用。使用"34010133"作为前缀拼接后加密；使用Applet个人化公钥appletPublicKey对拼接后的十六进制字符进行加密。加密算法RSA/NONE/OAEPWithSHA1AndMGF1Padding。 |
| card\_info | String | 是 | 9F05 + Lc + CardInfo1 + 9F31 + Lc + CardAuthParameter | 发卡方发放的卡片私有信息，允许在AUTH认证之前读取（GetProcessData步骤），TLV格式存储（多个TLV数据拼接）。加密方式：TLV明文数据补800...00到16个字节整数倍，使用aesKey，aesIv加密后的结果，并转换成十六进制字符串。CBC模式加密，加密算法：AES/CBC/NoPadding。Card Info1最长150个字节，如果长度超出127，则Lc需要使用两个字节标识，第一字节固定为81，例如正好150个字节则Lc为8196。CardAuthParameter最长30个字节。 |
| card\_privateInfo | String | 是 | - | 发卡方发放的卡片私有信息，如卡片有效期、权限等信息，在AUTH认证之后读取，开发者自行解析。加密方式：数据明文后补800...00到16个字节整数倍，使用aesKey，aesIv加密后的结果，并转换成十六进制字符串。CBC模式加密，加密算法：AES/CBC/NoPadding。 |
| card\_key\_iv | String | 是 | Lc + CardKeyIV | 交易流程协商的SessionKey使用（需要同步下发到车端），16个字节，如您无需使用此值，请传入全0。 |

**说明** 

园区卡的encryptAppletPersonalizeFields数据使用ECDH密钥协商 + AES-GCM加密方式，ECDH密钥派生过程如下：

1. 开发者业务管理服务生成ECC256临时密钥对（secp256r1曲线），获取临时公钥eccPK和临时私钥。
2. 开发者业务管理服务使用临时私钥与请求中的personalizePublicKey（Applet个人化公钥）进行ECDH协商，得到sharedSecret。
3. 开发者业务管理服务采用KDF算法派生AES密钥，具体过程为：对sharedSecret、0x00000001和eccShareInfo拼接后的数据进行SHA-256哈希运算，取计算结果的前16个字节作为AES-128密钥使用。
4. Applet侧使用自身ECC私钥与eccParam中的eccPK进行ECDH协商，结合eccShareInfo通过相同KDF派生出相同的aesKey。

| 园区卡encryptAppletPersonalizeFields子节点参数 | 类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| card\_id | String | 是 | AES-GCM加密后的CardId。明文为16个字节的CardId，加密算法：AES/GCM/NoPadding，密钥为ECDH协商派生的aesKey，IV为随机生成的12字节。加密结果格式：L（1个字节，值0x0C）+ IV（12个字节）+ 密文 + GCM Tag（16个字节），十六进制编码。 |
| card\_key | String | 是 | AES-GCM加密后的卡片密钥。明文为4个字节前缀（18010133）+ 16个字节CMAC（cardSEId, cardKeyRoot），加密算法：AES/GCM/NoPadding，密钥为ECDH协商派生的aesKey，IV为随机生成的12个字节。加密结果格式同card\_id。 |
| card\_privateInfo | String | 是 | AES-GCM加密后的卡片私有信息。明文为TLV格式的私有信息（如身份证号、serialNumber、人脸密钥等），加密算法：AES/GCM/NoPadding，密钥为ECDH协商派生的aesKey，IV为随机生成的12个字节。加密结果格式同card\_id。 |
| ecc\_param | String | 是 | ECDH参数，用于Applet端派生相同的aesKey。格式：C341 + eccPK（65个字节未压缩公钥，由04前缀 + 32个字节X坐标 + 32个字节Y坐标组成）+ C410 + eccShareInfo（16个字节随机数）。Applet使用自身ECC私钥与eccPK进行ECDH协商，再结合eccShareInfo通过KDF（SHA-256）派生aesKey。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "response": {
    "encryptDevicePass": "xxx",
    "encryptAppletPersonalizeFields": "xxx",
    "encryptSessionKey": "xxx"
  },
  "signature": "xxx"
}
```

### 开发者业务管理服务处理调用示例

完整的调用示例，请参见[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)示例代码。

```java
public PersonalizeResponse dealWithPersonalizeDataRequest(String token, PersonalizeRequest request) {
    PersonalizeResponse response = new PersonalizeResponse();
    RequestBody requestBody = request.getRequestBody();
    String userDeviceId = requestBody.getUserDeviceId();
    Certificate spCertFromRequest = request.getCertificate();
    String cachedToken = deviceIdTokenMap.remove(userDeviceId);
    if (cachedToken == null || !cachedToken.equals(token)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
        return response;
    }
    if (CommonUtils.isStringEmpty(userDeviceId) || !ParamChecker.checkSpServerCertificate(spCertFromRequest)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
        return response;
    }

    Certificate cachedCert = deviceIdCertMap.get(userDeviceId);
    if (cachedCert == null) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
        return response;
    }
    if (!ParamChecker.hashSignatureCheck(request.toJsonString(token), request.getSignature(),
            appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
        return response;
    }
    String personalizePKSign = requestBody.getPersonalizeCert();
    byte[] srcBytes = DataConvertUtil.base64Decode(requestBody.getPersonalizePublicKey());
    if (!DataConvertUtil.checkSign(srcBytes, personalizePKSign,
            appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
        response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
        return response;
    }
    response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_OK));
    PassDataResponse passData = getDevicePassData(requestBody);
    response.setResponse(passData);
    String passDataStr = passData.toJsonString();
    String passHashValue = DataConvertUtil.encodeSHA256(passDataStr);
    String signature = DataConvertUtil.signData(passHashValue, Constants.SERVER_SECRET_KEY);
    response.setSignature(signature);
    return response;
}
```

## NFC相关事件回调通知接口

用户进行华为钱包NFC能力相关操作时，华为钱包服务器调用此API通知开发者服务器。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：开发者在华为AGC网站上提供的NFC回调地址
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| HMSSignType | 是 | String | 签名方式，固定值：'SHA256WithRSA/PSS'。 |
| HMSSign | 是 | String | 签名值 |
| Version | 是 | String | 回调接口版本号，固定值：V2。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| eventId | 是 | String | 事件ID。若钱包服务器多次重试发送回调通知，开发者服务器可以用此参数去重。 |
| eventTime | 是 | String | 事件发生时间（UTC时间）："yyyy-MM-dd'T'HH:mm:ss:SSS'Z'" |
| eventType | 是 | String | 事件类型：  RECEIVE\_CARD：用户领取NFC卡券。  DELETE\_CARD：删除NFC卡券。  SWIPE\_CARD：用户使用NFC卡券刷卡。 |
| passNumber | 是 | String | 卡券号，即serialNumber。 |
| passTypeIdentifier | 是 | String | 开发者在AGC网站注册的服务号。 |
| sceneType | 是 | String | 场景类型：  USER\_OPERATION\_DELETE\_CARD：用户在华为钱包App里删卡，或用户在华为钱包App退出华为账号触发删卡。  RESTORE\_FACTORY\_SETTINGS：用户恢复手机出厂设置触发删卡。  REMOTE\_DELETE\_CARD：华为服务器删卡，如用户挂失场景。  THIRD\_PARTY\_DELETE\_CARD：开发者删卡。 |
| pushToken | 是 | String | 账号及设备关联的唯一标识。 |
| noticeToken | 是 | String | NFC事件对应的标识，用于调用用户使用NFC能力后推送消息接口。此标识有效时间为3分钟。 |

### 请求示例

```json
POST /api/callback HTTP/1.1
HMSSignType: SHA256WithRSA/PSS
HMSSign: u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExH********************g
Version: V2
{
  "requestBody": {
    "eventId": "0a1f133471c4102c8171f845919906f3",
    "eventTime": "2020-04-27T07:40:24.259Z",
    "eventType": "DELETE_CARD",
    "passNumber": "40001",
    "passTypeIdentifier": "hwpass.com.partner.examplepasstype"
 },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
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

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| returnCode | 是 | String | 响应码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| returnDesc | 是 | String | 错误描述 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "returnCode": "0",
  "returnDesc": "success",
}
```

### 调用示例

```java
@Data
public class CallbackRequest {
    // 事件id，随机值
      private String eventId;
    // 模板id
    private String modelId;
    // 卡实例id
       private String instanceId;
    // 事件发生时间
       private String eventTime;
    // 事件类型，RECEIVE_CARD/DELETE_CARD/TASK_RESULT_NOTIFY
    private String eventType;
    // 服务号
       private String passTypeIdentifier;
    // 场景类型
       private String sceneType;
}
// 开发者接收Wallet Kit云侧回调请求
public HwWalletObject getHwCallback(@RequestBody CallbackRequest request, @RequestHeaders Map<String, String> headers) {
    // 获取请求头签名信息
    String version = headerMaps.get("version");
       String signType = headerMaps.get("HMSSignType");
       String sign = headerMaps.get("HMSSign");
    // 对请求体进行验签
    String signContent = ToStringUtil.signString(request);
    String verifyHwSignPubKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1+b2/q6KEJfvI65xJLXhPMT8YRUO618zsgaW4pNGZ+r/mwfFC1EOZbcBp7sV0IaxSWeMy0WNyJPSh/JltuiC1R93hfA0Kh3DlaRWaDgJz9VC1b+aPjUOx+uqndOEFiZcKGGnM60YPXfyo7xCDH76/WsWR0G4Ov6MoYQ76RAUT0t+G0oumYGgdLYwx5hJ1ywDKPXszj7A/mKHtWJKiylPIhUK2mLwKR8Y/+3dLNuNomvb7miVgeBFiriwGS1FolQMu433zEugAqRgsiasZAKfVK1BChPmiC812IMS1UPhz1wwpXzzkjQ1YQUGjnbHpooKobeCyctKKgF27F84egpzsQIDAQAB";
    verifySignature(signContent, verifyHwSignPubKey, sign);
    // 获取华为侧回调请求体信息，包括eventType、instanceId
       String eventType = request.getEventType();
       String instanceId = request.getInstanceId();
       // 开发者视自己业务情况进行业务逻辑处理，根据事件类型对相应卡进行状态更新等操作

       // 响应成功
       BaseResponse response = new BaseResponse();
       response.setReturnCode(“0”);
       response.setReturnDesc(“success”);
       return response;
}
// 签名验签过程中对请求体字段按序排列生成待签名明文字符串工具类
public class ToStringUtil {
    public static String signString(Object obj) {
        if (obj == null) {
            return StringUtils.EMPTY;
        }
        if (obj instanceof Map) {
            return signStringFromMap((Map<?, ?>) obj);
        }
        return signStringFromObject(obj);
    }

    private static String signStringFromMap(Map<?, ?> map) {
        if (map == null || map.isEmpty()) {
            return StringUtils.EMPTY;
        }
        String result = map.entrySet().stream()
                .filter(entry -> !isEmptyValue(entry.getValue()))
                .sorted(Comparator.comparing(e -> String.valueOf(e.getKey())))
                .map(entry -> entry.getKey() + "=" + convertValueToString(entry.getValue()))
                .collect(Collectors.joining("&"));
        return result;
    }

    private static String signStringFromObject(Object obj) {
        Class<?> clazz = obj.getClass();
        List<Field> fields = Arrays.asList(clazz.getDeclaredFields());
        String result = fields.stream()
                .filter(field -> {
                    field.setAccessible(true);
                    try {
                        Object value = field.get(obj);
                        return !isEmptyValue(value);
                    } catch (Exception e) {
                        return false;
                    }
                })
                .sorted(Comparator.comparing(Field::getName))
                .map(field -> {
                    try {
                        field.setAccessible(true);
                        Object value = field.get(obj);
                        return field.getName() + "=" + convertValueToString(value);
                    } catch (Exception e) {
                        return null;
                    }
                })
                .filter(Objects::nonNull)
                .collect(Collectors.joining("&"));
        return result;
    }

    private static boolean isEmptyValue(Object value) {
        if (value == null) {
            return true;
        }
        if (value instanceof String) {
            return StringUtils.isEmpty((String) value);
        }
        return false;
    }

    private static String convertValueToString(Object value) {
        if (value == null) {
            return StringUtils.EMPTY;
        }
        if (value instanceof Map) {
            return signStringFromMap((Map<?, ?>) value);
        }
        if (value instanceof List) {
            return ((List<?>) value).stream()
                    .map(ToStringUtil::convertValueToString)
                    .collect(Collectors.joining(","));
        }
        return String.valueOf(value);
    }
}
// 使用SHA256WithRSA/PSS算法进行签名验签工具类
public class RsaUtil {
    private static final String SIGN_ALGORITHMS256 = "SHA256WithRSA/PSS";
    private static final BouncyCastleProvider BOUNCY_CASTLE_PROVIDER = new BouncyCastleProvider();
    static {
        if (Security.getProvider("BC") == null) {
            Security.addProvider(new BouncyCastleProvider());
        }
    }

    public static String sign(String content, String privateKey) {
        String charset = "utf-8";
        try {
            PKCS8EncodedKeySpec privatePKCS8 = new PKCS8EncodedKeySpec(Base64.getDecoder().decode(privateKey));
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");
            PrivateKey priKey = keyFactory.generatePrivate(privatePKCS8);

            java.security.Signature signatureObj = java.security.Signature.getInstance(SIGN_ALGORITHMS256);
            signatureObj.initSign(priKey);
            signatureObj.update(content.getBytes(charset));

            byte[] signed = signatureObj.sign();
            return Base64.getEncoder().encodeToString(signed);
        } catch (Exception e) {
            throw new IllegalArgumentException("Get signature failed. Error: " + e.getMessage());
        }
    }

    public static String encrypt(byte[] bytes, String publicKey, String algorithm) throws Exception {
        Key key = getPublicKey(publicKey);
        Cipher cipher = Cipher.getInstance(algorithm, BOUNCY_CASTLE_PROVIDER);
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] b1 = cipher.doFinal(bytes);
        return Base64.getEncoder().encodeToString(b1);
    }

    public static PublicKey getPublicKey(String key) throws Exception {
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(Base64.getDecoder().decode(key));
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePublic(keySpec);
    }

    public static boolean verifySignature(String content, String publicKey, String sign) throws Exception {
        PublicKey key = getPublicKey(publicKey);
        Signature signature = Signature.getInstance(SIGN_ALGORITHMS256);
        signature.initVerify(key);
        signature.update(content.getBytes());
        return signature.verify(Base64.getDecoder().decode(sign.getBytes()));
    }
}
```

## 检测更新

用户打开钱包进入卡详情或刷卡页选中卡时，会主动触发开发者服务器检测更新，开发者服务器检测安检信息/会员等级等数据是否发生变化并返回结果。

自动触发机制会结合时间因子，例如出行类卡券的时间因子：出发前48小时。

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
| signType | 是 | String | 签名算法类型，取值为SHA256withRSA/PSS。 |
| sign | 是 | String | 签名值，使用开发者服务器私钥对请求体进行签名。 |
| signVersion | 否 | String | 签名版本，固定值：'0'。 |
| version | 是 | String | 接口版本，固定值：'V1'。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| apiKey | 是 | String | 请求的唯一标识。 |
| requestNo | 否 | String | 请求流水号。 |
| passType | 是 | String | 服务号，格式为：hwpass.xxx.xxx.xxx。 |
| serialNumber | 是 | String | 卡券唯一标识。 |
| timestamp | 是 | String | 时间戳。 |
| detectMode | 否 | String | 检测模式，固定值：'detectChange'。 |

### 请求示例

```json
{
  "apiKey": "xxx",
  "passType": "hwpass.xxx.xxx",
  "serialNumber": "xxxxxxxxxxxxxxxx",
  "timestamp": "1619838199448",
  "detectMode": "detectChange"
}
```

### 响应参数

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 结果码。0：成功，其他值表示失败。 |
| resultDesc | 是 | String | 结果描述。 |
| detectResult | 是 | String | 检测更新结果。0：无变化、1：存在变化。 |
| signature | 是 | String | 签名值，使用开发者服务器私钥对响应体进行签名。 |

### 响应示例

```json
{
  "resultCode": "0",
  "resultDesc": "success",
  "detectResult": "1",
  "signature": "xxx"
}
```

## 账号关联

建立华为账号与开发者账号的映射关系，后续用户新创建的卡券将自动推送至钱包，无需再次手动添加。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->开发者业务管理服务
* **接口URL**：{webServiceURL}/v1/synchHwOpenId
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| signType | 是 | String | 签名算法类型，取值为SHA256withRSA/PSS。 |
| sign | 是 | String | 签名值，使用开发者服务器私钥对请求体进行签名。 |
| signVersion | 否 | String | 签名版本，固定值：'0'。 |
| version | 是 | String | 接口版本，固定值：'V1'。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| apiKey | 是 | String | 请求的唯一标识。 |
| requestNo | 否 | String | 请求流水号。 |
| hwOpenId | 是 | String | 华为侧openId，用户在华为账号体系中的唯一标识。 |
| spOpenId | 是 | String | 开发者openId，用户在开发者账号体系中的唯一标识。 |

### 请求示例

```json
{
  "apiKey": "xxx",
  "requestNo": "202107011234567890",
  "hwOpenId": "hw_openid_xxx",
  "spOpenId": "sp_openid_xxx"
}
```

### 响应参数

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 结果码。0：成功，其他值表示失败。 |
| resultDesc | 是 | String | 结果描述。 |

### 响应示例

```json
{
  "resultCode": "0",
  "resultDesc": "success"
}
```
