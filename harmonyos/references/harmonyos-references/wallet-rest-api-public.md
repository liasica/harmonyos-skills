---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-public
title: 公共接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 公共接口
category: harmonyos-references
scraped_at: 2026-04-28T08:18:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb56cdff718c4cbb4eb44b9dc8c86681d09735fa478e1d379969d8b76bc3740d
---

## 获取AccessToken

此接口用于获取访问token，向钱包云服务的每次https请求都需要传入访问的token，该token相当于一个访问许可，钱包云服务器收到其请求时会对其进行校验。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：三方业务管理服务->钱包云服务
* **接口URL**：https://oauth-login.cloud.huawei.com/oauth2/v3/token
* **数据格式**：

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| grant\_type | 是 | String | 填写为“client\_credentials”，表示为客户端模式。 |
| client\_id | 是 | String | 在[应用开发准备](../harmonyos-guides/application-dev-overview.md)中得到的OAuth 2.0客户端ID，对于AppGallery Connect类应用，该值为应用的Client ID |
| client\_secret | 是 | String | 在[应用开发准备](../harmonyos-guides/application-dev-overview.md)中给客户端ID分配的密钥，对于AppGallery Connect类应用，该值为应用的Client Secret。 |

### 请求示例

```
1. grant_type=client_credentials&client_id=<客户端ID>&client_secret=<客户端密钥>
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| token\_type | 是 | String | 固定字符串“Bearer”。 |
| access\_token | 是 | String | Access Token。 |
| expires\_in | 否 | Long | Access Token的过期时间，以秒为单位。默认60分钟过期。 |

### 响应示例

```
1. {
2. "access_token": "<返回的Access Token>",
3. "expires_in": 3600,
4. "token_type": "Bearer"
5. }
```

### 调用示例

```
1. public static String getToken(String clientId, String clientSecret) {
2. HttpHeaders header = new HttpHeaders();
3. header.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

5. MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
6. map.add("grant_type", "client_credentials");
7. map.add("client_id", clientId);
8. map.add("client_secret", clientSecret);

10. String tokenUrl = ConfigUtil.instants().getValue("gw.tokenUrl");

12. HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, header);
13. ResponseEntity<JSONObject> exchange =
14. REST_TEMPLATE.exchange(tokenUrl, HttpMethod.POST, entity, JSONObject.class);

16. JSONObject response = exchange.getBody();
17. if (response == null) {
18. throw new NullPointerException("Get null token response.");
19. }
20. String accessToken = response.getString("access_token");
21. if (Strings.isEmpty(accessToken)) {
22. throw new NullPointerException("Get null access token.");
23. }
24. return accessToken;
25. }
```

## 设备认证

预个人化执行完成后，华为钱包App经由钱包云服务中转后请求认证设备，将applet身份公钥以及身份公钥的钱包服务器签名携带在请求体中，向三方业务管理服务请求三方业务管理服务认证授权证书。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->三方业务管理服务
* **接口URL**：https://{webServiceURL}/v1/passes/registrations
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

说明

webServiceURL为DK业务管理服务域名。

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |
| Authorization | 是 | String | [申请钥匙卡片](wallet-rest-api-carkey.md#申请钥匙卡片)时linkDevicePass参数中的token值，用于校验该请求是否合法。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 必选 | [创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 必选 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | passVersion | String | 可选 | 版本号，固定10.0。 |
| requestBody | userDeviceId | String | 必选 | 用户在当前设备上的唯一标识。 |
| requestBody | transId | String | 必选 | 随机数。 |
| signature | - | String | 必选 | Applet的身份私钥对requestBody的Hash值的签名。 |
| certificate | signature | String | 必选 | 钱包云服务使用钱包服务器私钥对publicKey的签名值。DK业务管理服务收到该请求后，需要使用钱包云服务公钥对其进行验签。 |
| certificate | publicKey | String | 必选 | Applet的身份公钥。 |

### 请求示例

```
1. {
2. "requestBody": {
3. "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
4. "passVersion": "10.0",
5. "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
6. "transId": "16198381994485116358",
7. "userDeviceId": "xxx"
8. },
9. "certificate": {
10. "publicKey": "xxx",
11. "signature": "xxx"
12. },
13. "signature": "xxx"
14. }
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

**Response Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | String | 必选 | 接口网络状态码。 |
| response | certificate | Certificate | 可选 | DK业务管理服务使用[创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)步骤5生成的私钥对publicKey进行签名后返回。 |

**Certificate参数类型说明**

| certificate子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- |
| signature | String | 必选 | 钱包云服务使用钱包服务器私钥对publicKey的签名值。DK业务管理服务收到该请求后，需要使用钱包云服务公钥对其进行验签。 |
| publicKey | String | 必选 | Applet的身份公钥。 |

### 响应示例

```
1. {
2. "httpStatus": "0",
3. "response": {
4. "certificate": {
5. "signature": "xxx",
6. "publicKey": "xxx"
7. }
8. }
9. }
```

### 三方业务管理服务处理调用示例

完整的调用示例，请参见[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)示例代码。

```
1. public RegistrationsResponse dealWithRegisterRequest(String token, RegistrationsRequest request) {
2. RegistrationsResponse response = new RegistrationsResponse();
3. if (token == null) {
4. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
5. return response;
6. }
7. if (!ParamChecker.isValidRegistrationsRequest(request)) {
8. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
9. return response;
10. }
11. Certificate walletCertificate = request.getCertificate();
12. if (!verifyWalletCert(walletCertificate)) {
13. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
14. return response;
15. }

17. if (!ParamChecker.hashSignatureCheck(request.toJsonString(), request.getSignature(),
18. appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
19. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
20. return response;
21. }

23. String userDeviceId = request.getRequestBody().getUserDeviceId();
24. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_OK));
25. Response responseBody = new Response();
26. Certificate serverCert = PassData.getServerCert(appletAuthPublicKey);
27. responseBody.setCertificate(serverCert);
28. response.setResponse(responseBody);
29. deviceIdCertMap.put(userDeviceId, serverCert);
30. return response;
31. }
```

## 获取个人化数据Token

华为钱包APP经由钱包云服务中转后向三方业务管理服务平台获取token（个人化数据请求报文里参与计算hash）。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->三方业务管理服务
* **接口URL**：https://{webServiceURL}/v1/passes/requestPersonalizeToken
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |
| Authorization | 是 | String | [申请钥匙卡片](wallet-rest-api-carkey.md#申请钥匙卡片)时linkDevicePass参数中的token值，用于校验该请求是否合法。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 必选 | [创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 必选 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | passVersion | String | 可选 | 版本号，固定10.0。 |
| requestBody | userDeviceId | String | 必选 | 用户在当前设备上的唯一标识。 |
| requestBody | transId | String | 必选 | 随机数。 |
| signature | - | String | 必选 | Applet的身份私钥对requestBody的Hash值的签名。 |
| certificate | signature | String | 必选 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate的签名。  DK业务管理服务使用[创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)步骤5生成的私钥对Applet的身份公钥签名信息。 |
| certificate | publicKey | String | 必选 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate里的Applet的身份公钥。 |

### 请求示例

```
1. {
2. "requestBody": {
3. "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
4. "passVersion": "10.0",
5. "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
6. "transId": "16198381994485116358",
7. "userDeviceId": "xxx"
8. },
9. "certificate": {
10. "publicKey": "xxx",
11. "signature": "xxx"
12. },
13. "signature": "xxx"
14. }
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

**Response Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | String | 必选 | 接口网络状态码。 |
| response | token | String | 必选 | 个人化token。 |

### 响应示例

```
1. {
2. "httpStatus": "0",
3. "response": {
4. "token": "sp.token.1619838979341"
5. }
6. }
```

### 三方业务管理服务处理调用示例

完整的调用示例，请参见[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)示例代码。

```
1. public RequestTokenResponse dealWithTokenRequest(RequestTokenRequest request) {
2. RequestTokenResponse response = new RequestTokenResponse();
3. String userDeviceId = request.getRequestBody().getUserDeviceId();
4. Certificate spCertFromRequest = request.getCertificate();
5. if (CommonUtils.isStringEmpty(userDeviceId) || !ParamChecker.checkSpServerCertificate(spCertFromRequest)) {
6. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
7. return response;
8. }
9. Certificate cachedCert = deviceIdCertMap.get(userDeviceId);
10. if (cachedCert == null) {
11. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
12. return response;
13. }
14. if (!ParamChecker.hashSignatureCheck(request.toJsonString(), request.getSignature(),
15. appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
16. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
17. return response;
18. }
19. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_OK));
20. Response responseBody = new Response();
21. String personalizeToken = PassData.getPersonalizeToken();
22. responseBody.setToken(personalizeToken);
23. deviceIdTokenMap.put(userDeviceId, personalizeToken);
24. response.setResponse(responseBody);
25. return response;
26. }
```

## 获取个人化数据

华为钱包APP经由钱包云服务中转后向三方业务管理服务获取个人化数据。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->三方业务管理服务
* **接口URL**：https://{webServiceURL}/v1/passes/requestPersonalize
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |
| Authorization | 是 | String | [获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)返回的token值，用于校验该请求是否合法。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | cardSEId | String | 必选 | Applet唯一标识，可以用于车端秘钥分散 |
| requestBody | passTypeIdentifier | String | 必选 | [创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 必选 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | passVersion | String | 可选 | 版本号，固定10.0。 |
| requestBody | userDeviceId | String | 必选 | 用户在当前设备上的唯一标识。 |
| requestBody | personalizePublicKey | String | 必选 | Applet的个人化公钥，用于加密个人化字段值。 |
| requestBody | personalizeCert | String | 必选 | Applet身份私钥对个人化公钥personalizePublicKey的签名。 |
| requestBody | personalizeCertType | String | 必选 | 固定值，默认为私钥签名。 |
| requestBody | transPublicKey | String | 必选 | 用于加密返回的对称秘钥，用于对返回的数据做数字信封。 |
| requestBody | transId | String | 必选 | 事务流水，用于拼接返回的对称秘钥。 |
| signature | - | String | 必选 | Applet的身份私钥对requestBody的Hash值的签名。[获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)作为其中requestbody一个key参与Hash值计算。 |
| certificate | signature | String | 必选 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate的签名。  DK业务管理服务使用[创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)步骤5生成的私钥对Applet的身份公钥签名信息。 |
| certificate | publicKey | String | 必选 | 在[设备认证](wallet-rest-api-public.md#设备认证)接口返回的certificate里的Applet的身份公钥。 |

### 请求示例

```
1. {
2. "requestBody": {
3. "cardSEId": "xxxxxxxxxxxxxxxx",
4. "personalizeCert": "xxx",
5. "personalizeCertType": "",
6. "personalizePublicKey": "xxx",
7. "transPublicKey": "xxx",
8. "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
9. "passVersion": "10.0",
10. "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
11. "transId": "858947076d58a5e66ee22b9ed1c43c4d",
12. "userDeviceId": "xxx"
13. },
14. "certificate": {
15. "publicKey": "xxx",
16. "signature": "xxx"
17. },
18. "signature": "xxx"
19. }
```

### 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

**Response Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否可选 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | String | 必选 | 接口网络状态码。 |
| response | encryptSessionKey | String | 必选 | DK业务管理服务使用请求中的transPublicKey加密生成的sessionKey。采用Base64编码，加密前的字段说明：三方生成AES128的aesKey和aesIv，用于加密生成encryptAppletPersonalizeFields和encryptDevicePass。使用请求中transPublicKey字段加密transId+aesKey+aesIv，对结果进行base64编码即得到encryptSessionKey。加密算法: RSA/ECB/OAEPWithSHA-256AndMGF1Padding。 |
| response | encryptDevicePass | String | 可选 | 空字符串"" |
| response | encryptAppletPersonalizeFields | String | 必选 | 用于蓝牙/NFC刷卡时的认证以及数据加解密操作。DK业务管理服务通过生成的sessionKey加密Applet的个人化参数密文。采用Base64编码 |
| signature | - | String | 必选 | DK业务管理服务使用[创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)步骤5生成的私钥对response的Hash值进行签名。 |

| encryptAppletPersonalizeFields子节点参数 | 类型 | 是否可选 | 存储格式 | 描述 |
| --- | --- | --- | --- | --- |
| temp\_key | String | 必选 | - | aesKey(AES128的key)，长度16字节，用于加密CardId，cardPrivateInfo信息。temp\_key：aesKey明文之前拼接一个固定的十六进制字符前缀"34810233"后，使用Applet个人化公钥appletPublicKey对其进行加密。加密算法RSA/NONE/OAEPWithSHA1AndMGF1Padding。 |
| temp\_iv | String | 必选 | - | aesIv(AES128的iv)，长度16字节，用于applet解密写卡数据。temp\_iv：aesIv使用Applet个人化公钥appletPublicKey加密。加密算法RSA/NONE/OAEPWithSHA1AndMGF1Padding。 |
| card\_id | String | 必选 | 9F3B + Lc + CardId | CardId即发卡方发放的卡片唯一标识（和"生成钥匙卡片"中的serialNumber保持一致），长度16字节。使用TLV格式存储：T=9F3B，Lc=10，V=CardId；加密方式：使用aesKey，aesIv对整个TLV加密，并转换成十六进制字符串。CBC模式加密，加密算法：AES/CBC/NoPadding。 |
| card\_key | String | 必选 | - | 发卡方发放的卡片密钥，16字节，一张卡支持1个秘钥，计算SessionKey时使用。使用"34010133"作为前缀拼接后加密；使用Applet个人化公钥appletPublicKey对拼接后的十六进制字符进行加密。加密算法RSA/NONE/OAEPWithSHA1AndMGF1Padding。 |
| card\_info | String | 必选 | 9F05 + Lc + CardInfo1 + 9F31 + Lc + CardAuthParameter | 发卡方发放的卡片私有信息，允许在AUTH认证之前读取（GetProcessData步骤），TLV格式存储（多个TLV数据拼接）。加密方式：TLV明文数据补800...00到16字节整数倍，使用aesKey，aesIv加密后的结果，并转换成十六进制字符串。CBC模式加密，加密算法：AES/CBC/NoPadding。 |
| card\_privateInfo | String | 必选 | - | 发卡方发放的卡片私有信息，如卡片有效期、权限等信息，在AUTH认证之后读取（ReadBinary步骤），三方自行解析。加密方式：数据明文后补800...00到16字节整数倍，使用aesKey，aesIv加密后的结果，并转换成十六进制字符串。CBC模式加密，加密算法：AES/CBC/NoPadding。 |
| card\_key\_iv | String | 必选 | Lc + CardKeyIV | 交易流程协商的SessionKey使用（需要同步下发到车端），16字节，如您无需使用此值，请传入全0。 |

### 响应示例

```
1. {
2. "httpStatus": "0",
3. "response": {
4. "encryptDevicePass": "xxx",
5. "encryptAppletPersonalizeFields": "xxx",
6. "encryptSessionKey": "xxx"
7. },
8. "signature": "xxx"
9. }
```

### 三方业务管理服务处理调用示例

完整的调用示例，请参见[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)示例代码。

```
1. public PersonalizeResponse dealWithPersonalizeDataRequest(String token, PersonalizeRequest request) {
2. PersonalizeResponse response = new PersonalizeResponse();
3. RequestBody requestBody = request.getRequestBody();
4. String userDeviceId = requestBody.getUserDeviceId();
5. Certificate spCertFromRequest = request.getCertificate();
6. String cachedToken = deviceIdTokenMap.remove(userDeviceId);
7. if (cachedToken == null || !cachedToken.equals(token)) {
8. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
9. return response;
10. }
11. if (CommonUtils.isStringEmpty(userDeviceId) || !ParamChecker.checkSpServerCertificate(spCertFromRequest)) {
12. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
13. return response;
14. }

16. Certificate cachedCert = deviceIdCertMap.get(userDeviceId);
17. if (cachedCert == null) {
18. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_PARAM_ERROR));
19. return response;
20. }
21. if (!ParamChecker.hashSignatureCheck(request.toJsonString(token), request.getSignature(),
22. appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
23. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
24. return response;
25. }
26. String personalizePKSign = requestBody.getPersonalizeCert();
27. byte[] srcBytes = DataConvertUtil.base64Decode(requestBody.getPersonalizePublicKey());
28. if (!DataConvertUtil.checkSign(srcBytes, personalizePKSign,
29. appletAuthPublicKey, DataConvertUtil.SIGN_MODE_SHA256_RSA_MGF1)) {
30. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_SIGN_ERROR));
31. return response;
32. }
33. response.setHttpStatus(String.valueOf(Constants.RESULT_CODE_OK));
34. PassDataResponse passData = getDevicePassData(requestBody);
35. response.setResponse(passData);
36. String passDataStr = passData.toJsonString();
37. String passHashValue = DataConvertUtil.encodeSHA256(passDataStr);
38. String signature = DataConvertUtil.signData(passHashValue, Constants.SERVER_SECRET_KEY);
39. response.setSignature(signature);
40. return response;
41. }
```
