---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-carkey
title: 数字车钥匙接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 数字车钥匙接口
category: harmonyos-references
scraped_at: 2026-04-28T08:18:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4cfbd84cc235270bc474f2b412c365993c4c69ee5697711956617b67a5e4d0c4
---

## 预置模板

卡片模板的创建是接入流程的第一步，这一步您将会通过http/https请求的方式向华为钱包云服务提供卡券样式的关键信息，如卡面主标题、副标题、logo、背景图片等；用于华为钱包钥匙页面的展示。

您可以创建多个模板，它们有着相同的机构名和服务号，而模板ID不同；当您申请车钥匙时，每一张卡必须和唯一的模板ID关联；即一个模板可供多张钥匙使用，而一张钥匙只能使用一个模板ID。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：三方业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/key\_stdcar/model
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：Content-Type: application/json;charset=UTF-8 |
| Authorization | 是 | String | 将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值 |
| Accept | 是 | String | 取值为：Content-Type: application/json;charset=UTF-8 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | hwpass.stdcarkey.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义)  [创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)时注册的服务号，需要开发者到华为AGC网站申请。 |
| passStyleIdentifier | 是 | String | 自定义，模板ID，即modelId。在同一个appId下唯一。长度不超过64个字符，只能是字母、数字和（.）、（-）、（\_）。 |
| organizationName | 是 | String | 自定义，商户名称，最长64个字节，无具体格式要求，中英文均可。 |
| passVersion | 是 | String | 版本号，固定10.0  钱包对象版本，开发者可以依据此确定钱包对象的版本信息 |
| fields | 是 | fields | 自定义  卡券展示信息：**appendFields**和**commonFields** |

| appendFields参数 | value | label | 是否必须 | 描述 |
| --- | --- | --- | --- | --- |
| isCreateWhiteCard | true | NFCCardFlag | 是 | 用于表明是否是NFC卡的flag |

| commonFields参数 | value | label | 是否必须 | 描述 |
| --- | --- | --- | --- | --- |
| logo | https://开头的图片链接，具体地址车厂自定义 | / | 是 | 卡面logo  128\*128px，大小<=20kb，直角图片，无需切圆角 |
| backgroundImage | https://开头的图片链接，具体地址车厂自定义 | / | 是 | 卡面背景  1312\*820px，直角图片，无需切圆角 |
| picUrl | https://开头的图片链接，具体地址车厂自定义 | / | 是 | 带logo的卡面背景  1312\*820px，直角图片，无需切圆角 |
| merchantName | 车厂定义 | 卡面主标题 | 是 | 卡面主标题  小于256字节 |
| name | 车厂定义 | 卡面副标题 | 是 | 卡面副标题  小于256字节 |

### 请求示例

```
1. {
2. "passVersion": "10.0",
3. "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
4. "passStyleIdentifier": "DigitalCarKeyTestModel",
5. "organizationName": "Replace with your organization name",
6. "fields": {
7. "appendFields": [
8. {
9. "label": "NFCCardFlag",
10. "value": "true",
11. "key": "isCreateWhiteCard"
12. }
13. ],
14. "commonFields": [
15. {
16. "label": "卡面主标题",
17. "value": "我的车",
18. "key": "merchantName"
19. },
20. {
21. "label": "卡面副标题",
22. "value": "XXX车钥匙",
23. "key": "name"
24. },
25. {
26. "label": "",
27. "value": "https://xxx/xxx.png",
28. "key": "logo"
29. },
30. {
31. "label": "",
32. "value": "https://xxx/xxx.webp",
33. "key": "backgroundImage"
34. },
35. {
36. "label": "",
37. "value": "https://xxx/xxx.png",
38. "key": "picUrl"
39. }
40. ]
41. }
42. }
```

### 响应参数

模板预置成功，即http响应为200时，钱包云服务会将DK业务管理服务请求的数据原样返回，即和上面的请求体中的数据一致；其他错误情况，可见[REST API错误码](wallet-rest-api-error-code.md)。

### 调用示例

```
1. public void createStdCarKeyModel() {
2. JSONObject model = JSONObject.parseObject(ConfigUtil.readFile("StdCarKeyModel.json"));
3. HwWalletObjectUtil.validateModel(model);
4. String urlSegment = "/v2/key_stdcar/model";
5. JSONObject responseModel = serverApiService.postToWalletServer(urlSegment, JSONObject.toJSONString(model));
6. }
```

## 申请ICCE钥匙

车主APP向DK业务管理服务申请开通ICCE车钥匙，DK业务管理服务将车钥匙卡片信息添加至钱包云服务中；其中：车主APP->DK业务管理服务之间的交互由车厂自行实现，本章主要侧重于DK业务管理服务->钱包云服务申请ICCE车钥匙的过程，主要包括：申请钥匙卡片和生成JWE数据。

### 申请钥匙卡片

DK业务管理服务向华为钱包云服务请求创建车钥匙卡片。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：三方业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/key\_stdcar/instance
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：Content-Type: application/json;charset=UTF-8 |
| Authorization | 是 | String | 将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值 |
| Accept | 是 | String | Content-Type: application/json;charset=UTF-8 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | hwpass.stdcarkey.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义)  [创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)时注册的服务号，需要开发者到华为AGC网站申请。 |
| passStyleIdentifier | 是 | String | 自定义，注：示例代码中的默认值仅作说明，请勿直接使用  请使用“预置模板中创建的”模板ID，即modelId。在同一个appId下唯一。长度不超过64个字符，只能是字母、数字和（.）、（-）、（\_）。 |
| organizationName | 是 | String | 自定义，注：示例代码中的默认值仅作说明，请勿直接使用  请使用预置模板中创建的商户名称，最长64个字节。 |
| organizationPassId | 是 | String(64) | 自定义，注：示例代码中的默认值仅作说明，请勿直接使用  车钥匙卡片在开发者服务器中的卡号。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字（全大写）。当前和serialNumber保持一致 |
| serialNumber | 是 | String(64) | 自定义，注：示例代码中的默认值仅作说明，请勿直接使用  车钥匙卡片在华为钱包服务器中的卡号，即instanceId。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字（全大写）。当前和organizationPassId保持一致。 |
| fields | 是 | fields | 自定义  卡券展示信息：**commonFields**、**timeList**和**status** |
| linkDevicePass | 是 | linkDevicePass | 自定义**linkDevicePass**  此参数用于保存车钥匙管理台服务器地址、公钥信息以及是否使能卡券的NFC能力。 |

| **timeList**参数 | value | label | 是否必须 | 描述 |
| --- | --- | --- | --- | --- |
| linkDevicePassExpireTime | 自定义 | / | 是 | 时间列表 |

| **status**参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| state | 是 | String | 状态值。取值如下  - active：生效  - inactive：未激活  - completed：已使用  - expired：已过期 |
| effectTime | 是 | String | UTC格式，生效时间 |
| expireTime | 是 | String | UTC格式，失效时间，如果超过此事件，卡券自动按照expired状态处理 |

| commonFields参数 | value | label | 是否必须 | 描述 |
| --- | --- | --- | --- | --- |
| bleServiceUuid | 由车厂定义 | / | 是 | 车厂蓝牙设备的SERVICE\_UDID，用于手机发现车端蓝牙模块开启的车钥匙服务；请使用蓝牙标准规范：如0000xxxx-0000-1000-8000-00805f9b34fb；如需自行定义，请联系ICCE确认 |
| ownerPassTypeIdentifier | 固定值 | 主卡服务号 | 是 | hwpass.stdcarkey.std：归属ICCE车钥匙类别 |
| readerMatchValue | 由车厂定义 | readerId | 是 | 车钥匙标识，建议字节：不超过20字节（第一字节：车厂标识，第二字节：品牌/系列标识，后续字节保证在车厂内唯一）, 只能包含0-9，A-F |
| bleTargetPackage | 由车厂定义 | / | 是 | 车厂app的包名，用于钱包在特定场景下拉起车厂app，注：请提供应用安装后的全包名，即应用的applicationId, 如com.huawei.wallet |
| bleTargetActivity | 由车厂定义 | / | 是 | 车厂app的activity，供钱包在特定场景下拉起车厂app；注：全路径名称，不带文件后缀，如com.huawei.xxx.xxx.ShowCarDetailActivity |
| bleTargetService | 由车厂定义 | / | 是 | 车厂app的service，供钱包在特定场景下拉起车厂app，注：全路径名称，不带文件后缀名，如com.huawei.xxx.xxx.BleICCEService |
| bleMacAddress | 由车厂定义 | / | 是 | 车端蓝牙设备的mac地址，用于华为手机扫描车端蓝牙模块、向车端蓝牙发起Gatt连接等。请注意格式合法性，如：01:23:45:67:89:0A；注：字符必须全大写 |
| bleFeature | 固定值 | / | 是 | hwpass.carkey.ble：标识支持蓝牙车钥匙 |
| deviceType | 设备类型 | / | 是 | 当前钥匙开通的设备类型，如手机：Phone，穿戴：Wear |
| keyHolderType | 钥匙持有者性质 | / | 是 | 当前钥匙持有者的性质，如车主：Owner，分享：Share |
| vehicleId | 由车厂定义 | / | 是 | 车辆vin码，不超过20个字节 |
| personalizedData | 由车厂定义 | / | 否 | 车厂个性化数据，可用于储存车辆标定数据等 |
| logo | https://开头的图片链接，具体地址车厂自定义 | / | 否 | 卡面logo；128\*128px，大小<=20kb，直角图片，无需切圆角  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| backgroundImage | https://开头的图片链接，具体地址车厂自定义 | / | 否 | 卡面背景；1312\*820px，直角图片，无需切圆角  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| picUrl | https://开头的图片链接，具体地址车厂自定义 | / | 否 | 带logo的卡面背景；1312\*820px，直角图片，无需切圆角  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| merchantName | 车厂定义 | 卡面主标题 | 否 | 卡面主标题；小于256字节  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| name | 车厂定义 | 卡面副标题 | 否 | 卡面副标题；小于256字节  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |

| linkDevicePass参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| webServiceURL | 是 | String | DK业务管理服务地址，用于开通激活过程中向DK业务管理服务发起设备认证、获取个人化token以及获取个人化数据。 |
| token | 是 | String | DK业务管理服务自行生成，没有格式要求，用于开通激活过程中钱包向DK业务管理服务进行“[设备认证](wallet-rest-api-public.md#设备认证)”和“[获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)”请求头中携带的Authorization信息。 |
| serialNumber | 是 | String | 请和上述提及的serialNumber保持一致 |
| passVersion | 否 | String | DevicePass卡券包版本，固定10.0 |
| spPublickey | 是 | String | 开发者[创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)步骤5生成的公钥。用于对DK业务管理服务返回的“Applet个人化数据”进行验签。NFC卡片信息不会上传到钱包云服务器，所以终端设备需要这个参数来进行验签。 |
| nfcType | 是 | String | 固定值"1"，表示开启NFC能力。如果这个值不是"1"，当前个人化实例的NFC能力会被关闭。 |

### 请求示例

```
1. {
2. "organizationName": "Replace with your organization name",
3. "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
4. "passStyleIdentifier": "DigitalCarKeyTestModel",
5. "organizationPassId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
6. "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
7. "fields": {
8. "timeList": [
9. {
10. "value": "timeListValue",
11. "key": "linkDevicePassExpireTime"
12. }
13. ],
14. "status": {
15. "state": "active",
16. "effectTime": "2020-04-06T00:00:00.111Z",
17. "expireTime": "2030-04-06T00:00:00.111Z"
18. },
19. "commonFields": [
20. {
21. "value": "xxx.CarActivity",
22. "key": "bleTargetActivity"
23. },
24. {
25. "value": "hwpass.carkey.ble",
26. "key": "bleFeature"
27. },
28. {
29. "value": "01:23:45:67:89:AB",
30. "key": "bleMacAddress"
31. },
32. {
33. "label": "readerId",
34. "value": "CAD34B258391C097",
35. "key": "readerMatchValue"
36. },
37. {
38. "label": "主卡服务号",
39. "value": "hwpass.stdcarkey.std",
40. "key": "ownerPassTypeIdentifier"
41. },
42. {
43. "value": "0000xxxx-0000-1000-8000-00805f9b34fb",
44. "key": "bleServiceUuid"
45. },
46. {
47. "value": "xxx",
48. "key": "bleTargetPackage"
49. },
50. {
51. "value": "xxx",
52. "key": "bleTargetService"
53. },
54. {
55. "value": "Phone",
56. "key": "deviceType"
57. },
58. {
59. "value": "Owner",
60. "key": "keyHolderType"
61. },
62. {
63. "value": "xxx",
64. "key": "vehicleId"
65. }
66. ]
67. },
68. "linkDevicePass": {
69. "webServiceURL": "https://xxx",
70. "nfcType": "1",
71. "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
72. "passVersion": "10.0",
73. "spPublickey": "xxx",
74. "token": "xxx"
75. }
76. }
```

### 响应参数

返回结果中会携带预置模板中的信息一并返回。

### 调用示例

完整的调用示例，请参见[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)示例代码。

```
1. public void addStdCarKeyInstance() {
2. JSONObject instance = JSONObject.parseObject(ConfigUtil.readFile("StdCarKeyInstance.json"));
3. HwWalletObjectUtil.validateInstance(instance);
4. String urlSegment = "/v2/key_stdcar/instance";
5. JSONObject responseInstance =
6. serverApiService.postToWalletServer(urlSegment, JSONObject.toJSONString(instance));

8. if (responseInstance.containsKey("serialNumber")) {
9. String serialNumber = responseInstance.getString("serialNumber");
10. JweTest test = new JweTest();
11. test.generateThinJWEToBindUser(serialNumber);
12. }
13. }
```

### 生成JWE数据

华为钱包车钥匙卡片的开通是基于JWE（JSON Web Encryption）方式。因此DK业务管理服务向钱包云服务申请创建车钥匙成功后，基于创建成功的车钥匙serialNumber生成JWE数据，并将其返回给车厂app，如下所示：

JWE串包含JWE Encrypted Key，iv，Ciphertext，signature；可参见如下步骤：

1. 生成一个随机的Content Encryption Key（CEK）。
2. 使用RSA-OAEP加密算法，用钱包服务器给的公钥加密CEK，生成JWE Encrypted Key。
3. 生成JWE初始化向量。
4. 使用AES GCM加密算法对明文部分进行加密生成密文Ciphertext，算法会随之生成一128位的认证标记Authentication Tag。对以上部分分别进行base64编码。
5. Signature是使用开发者[创建Wallet Kit服务](../harmonyos-guides/wallet-preparations.md)步骤5生成的私钥对以上部分进行的签名。

### 调用示例

完整的调用示例，请参见[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)示例代码。

```
1. public static String generateJwe(String jwePrivateKey, String payload) {
2. Map<String, String> jweHeader = getHeader();
3. String jweHeaderEncode = getEncodeHeader(jweHeader);
4. String sessionKey = generateSecureRandomFactor(16);
5. String sessionKeyPublicKey = "MIIBojA****"; // 填入真实的公钥值
6. String encryptedKeyEncode = getEncryptedKey(sessionKey, sessionKeyPublicKey);
7. byte[] iv = AesUtil.getIvByte(12);
8. String ivHexStr = new String(Hex.encodeHex(iv, false));
9. String ivEncode = Base64.encodeBase64URLSafeString(ivHexStr.getBytes(StandardCharsets.UTF_8));
10. String cipherTextEncode = getCipherText(payload, sessionKey, iv);
11. String signature = getSignature(jwePrivateKey, sessionKey, payload, jweHeaderEncode, ivEncode);
12. StringBuilder stringBuilder = new StringBuilder().append(jweHeaderEncode)
13. .append(".")
14. .append(encryptedKeyEncode)
15. .append(".")
16. .append(ivEncode)
17. .append(".")
18. .append(cipherTextEncode)
19. .append(".")
20. .append(signature);
21. return stringBuilder.toString();
22. }
```
