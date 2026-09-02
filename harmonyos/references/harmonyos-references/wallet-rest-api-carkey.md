---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-carkey
title: 数字车钥匙接口
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > 数字车钥匙接口
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:37532489b91922a0b563093912ca8ae91b448011016fe71c7b543b948b9d5895
---

## 预置模板

卡片模板的创建是接入流程的第一步，这一步可以通过http/https请求的方式向华为钱包云服务提供卡券样式的关键信息，如卡面主标题、副标题、logo、背景图片等，用于华为钱包钥匙页面的展示。

开发者可创建多个共享相同机构名和服务号但模板ID不同的模板。在申请车钥匙时，每张卡必须绑定唯一的模板ID，即一个模板可被多个车钥匙复用，而一个车钥匙仅能关联一个模板ID。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：DK业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/{cardType}/model

  cardType取值如下：

  key\_stdcar：汽车钥匙

  key\_stdbike：两轮车钥匙
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 发送端可接受的数据类型，取值为：application/json;charset=UTF-8。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | 创建Wallet Kit服务时注册的服务号，格式为：hwpass.stdcarkey.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义）。 |
| passStyleIdentifier | 是 | String | 模板ID，长度不超过64个字符，只能是字母、数字、“.”、“-”和“\_”。 |
| organizationName | 是 | String | 商户名称，最长64个字节，无具体格式要求，中英文均可。 |
| passVersion | 是 | String | Pass版本号，固定“10.0”。 |
| fields | 是 | fields | 卡券展示信息，包括appendFields和commonFields两部分。 |

| appendFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| isCreateWhiteCard | 是 | String | 是否为NFC卡的标记。  true：NFC卡。  false：非NFC卡。  固定取'true'。 |

| commonFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| logo | 是 | String | 卡面logo，128\*128px，背景要求透明，底图要求128px直径白色圆形，logo居于中心位置。 |
| backgroundImage | 是 | String | 卡面背景，1312\*820px，方形直角，请勿切圆角，图片的边框不可有白边。 |
| picUrl | 是 | String | 卡面（logo+背景），将卡面logo和卡面背景按照示例进行组合。1312\*820px，方形直角，请勿切圆角，图片的边框不可有白边；logo居于背景左上角，与背景左边和上边间距均为96px。 |
| merchantName | 是 | String | 卡面主标题，小于256个字节。 |
| name | 是 | String | 卡面副标题，小于256个字节。 |

### 请求示例

```json
POST /hmspass/v2/key_stdcar/model HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "passVersion": "10.0",
  "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
  "passStyleIdentifier": "DigitalCarKeyTestModel",
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
        "value": "我的车",
        "key": "merchantName"
      },
      {
        "label": "卡面副标题",
        "value": "XXX车钥匙",
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

模板预置成功，即http响应为200时，钱包云服务会将DK业务管理服务请求的数据原样返回，即和请求体中的数据一致；其他错误情况，可见[REST API错误码](wallet-rest-api-error-code.md)。

### 调用示例

```java
public void createStdCarKeyModel() {
    JSONObject model = JSONObject.parseObject(ConfigUtil.readFile("StdCarKeyModel.json"));
    HwWalletObjectUtil.validateModel(model);
    String urlSegment = "/v2/key_stdcar/model";
    JSONObject responseModel = serverApiService.postToWalletServer(urlSegment, JSONObject.toJSONString(model));
}
```

## 申请ICCE钥匙

车主App向DK业务管理服务申请开通ICCE车钥匙，DK业务管理服务将车钥匙卡片信息添加至钱包云服务中。其中：车主App->DK业务管理服务之间的交互由车厂自行实现，本章主要侧重于DK业务管理服务->钱包云服务申请ICCE车钥匙的过程，主要包括：申请钥匙卡片和生成JWE数据。

DK业务管理服务向华为钱包云服务请求创建车钥匙卡片。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：DK业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/{cardType}/instance

  cardType取值如下：

  key\_stdcar：汽车钥匙

  key\_stdbike：两轮车钥匙
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 发送端可接受的数据类型，取值为：application/json;charset=UTF-8。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | 服务号，格式为：hwpass.stdcarkey.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义）。 |
| passStyleIdentifier | 是 | String | 模板ID，长度不超过64个字符，只能是字母、数字、“.”、“-”和“\_”。 |
| organizationName | 是 | String | 预置模板中创建的商户名称，最长64个字节。 |
| organizationPassId | 是 | String | 车钥匙卡片在开发者服务器中的卡号，长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和serialNumber保持一致。 |
| serialNumber | 是 | String | 车钥匙卡片在华为钱包服务器中的卡号，即instanceId。在同一个appId下唯一。长度16个字节，为保证唯一性，请勿手动输入，建议使用代码随机生成，只能是字母、数字，当前和organizationPassId保持一致。 |
| fields | 是 | fields | 卡券展示信息，包括commonFields和status两部分。 |
| linkDevicePass | 是 | linkDevicePass | 链接设备参数，用于保存车钥匙管理台服务器地址、公钥信息以及是否使能卡券的NFC能力。 |

| **status**参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| state | 是 | String | 状态值。取值如下：  - active：生效  - expired：删除 |
| effectTime | 是 | String | 生效时间，UTC格式。 |
| expireTime | 是 | String | 失效时间，UTC格式。如果超过此时间，卡券自动按照expired状态处理。 |

| commonFields参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| bleServiceUuid | 是 | String | 车厂蓝牙设备的SERVICE\_UDID，用于手机发现车端蓝牙模块开启的车钥匙服务；请使用蓝牙标准规范：如0000xxxx-0000-1000-8000-00805f9b34fb。 |
| ownerPassTypeIdentifier | 是 | String | 主服务号，取值如下：  hwpass.stdcarkey.std：汽车钥匙  hwpass.stdbike.std：两轮车钥匙。 |
| readerMatchValue | 是 | String | 车钥匙标识，建议不超过20个字节（第一字节：车厂标识，第二字节：品牌/系列标识，后续字节保证在车厂内唯一）, 只能包含0-9，A-F。 |
| bleTargetPackage | 是 | String | 车主App的包名，用于钱包在特定场景下拉起车主App。 |
| bleMacAddress | 是 | String | 车端蓝牙设备的mac地址，用于华为手机扫描车端蓝牙模块、向车端蓝牙发起Gatt连接等。请注意格式合法性，如：01:23:45:67:89:0A。 |
| sleL2ID | 否 | String | 车端星闪设备的mac地址，用于华为手机扫描车端星闪模块、向车端星闪发起数传连接等。格式如下：01:23:45:67:89:0A。 |
| bleFeature | 是 | String | 支持蓝牙车钥匙的标识，固定hwpass.carkey.ble。 |
| deviceType | 是 | String | 当前钥匙开通的设备类型，Phone：手机，Wear：穿戴。 |
| keyHolderType | 是 | String | 当前钥匙持有者的性质，如Owner：车主、Share：分享。 |
| vehicleId | 是 | String | 车辆vin码，不超过20个字节。 |
| personalizedData | 否 | String | 车厂个性化数据，可用于储存车辆标定数据等，申请ICCE车钥匙时下发给钱包。  车钥匙使用过程中，车端在完成认证流程之后可以通过0206指令从钱包车钥匙获取该信息。 |
| supportFunctionType | 否 | String | 车钥匙的能力集。长度固定为8的字符串，按照二进制解析（1：支持、0：不支持），从低位到高位取值如下：  bit0：是否支持NFC。  bit1：是否支持车控。  bit2：是否支持蓝牙无感。  bit3：是否支持UWB测距。  bit4：是否支持远程网络车控。  bit5：是否支持星闪无感。  bit6：预留。  bit7：预留。 |
| logo | 否 | String | 卡面logo，128\*128px，背景要求透明，底图要求128px直径白色圆形，logo居于中心位置。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| backgroundImage | 否 | String | 卡面背景，1312\*820px，方形直角，请勿切圆角，图片的边框不可有白边。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| picUrl | 否 | String | 卡面（logo+背景），将卡面logo和卡面背景按照示例进行组合。1312\*820px，方形直角，请勿切圆角，图片的边框不可有白边；logo居于背景左上角，与背景左边和上边间距均为96px。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| merchantName | 否 | String | 卡面主标题，小于256个字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |
| name | 否 | String | 卡面副标题，小于256个字节。  如果此处携带该参数，则会覆盖对应模板中的相应字段数据。 |

| linkDevicePass参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| webServiceURL | 是 | String | DK业务管理服务地址，用于开通激活过程中向DK业务管理服务发起设备认证、获取个人化token以及获取个人化数据。 |
| token | 是 | String | 认证信息，DK业务管理服务自行生成，没有格式要求，用于开通激活过程中钱包向DK业务管理服务进行“[设备认证](wallet-rest-api-public.md#设备认证)”和“[获取个人化数据Token](wallet-rest-api-public.md#获取个人化数据token)”请求头中携带的Authorization信息。 |
| serialNumber | 是 | String | 卡片标识。 |
| passVersion | 否 | String | Pass版本，固定“10.0”。 |
| spPublickey | 是 | String | DK业务管理服务生成的RSA2048公私钥对中的公钥，申请ICCE车钥匙时下发给钱包。  在后续开通过程中，钱包使用该公钥从DK业务管理服务获取个人化数据的返回值进行验签。  NFC卡片信息不会上传到钱包云服务器，所以终端设备需要这个参数来进行验签。 |
| nfcType | 是 | String | 是否开启NFC能力。  1：开启。  0：不开启。  固定值取'1'。 |

### 请求示例

```json
POST /hmspass/v2/key_stdcar/instance HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Bearer bKyECwrVGw********************e
Accept: application/json;charset=UTF-8
{
  "organizationName": "xxx",
  "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
  "passStyleIdentifier": "DigitalCarKeyTestModel",
  "organizationPassId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "fields": {
    "status": {
      "state": "active",
      "effectTime": "2020-04-06T00:00:00.111Z",
      "expireTime": "2030-04-06T00:00:00.111Z"
    },
    "commonFields": [
      {
        "value": "hwpass.carkey.ble",
        "key": "bleFeature"
      },
      {
        "value": "01:23:45:67:89:AB",
        "key": "bleMacAddress"
      },
      {
        "value": "01:23:45:67:89:AB",
        "key": "sleL2ID"
      },
      {
        "label": "readerId",
        "value": "CAD34B258391C097",
        "key": "readerMatchValue"
      },
      {
        "label": "主卡服务号",
        "value": "hwpass.stdcarkey.std",
        "key": "ownerPassTypeIdentifier"
      },
      {
        "value": "0000xxxx-0000-1000-8000-00805f9b34fb",
        "key": "bleServiceUuid"
      },
      {
        "value": "xxx",
        "key": "bleTargetPackage"
      },
      {
        "value": "Phone",
        "key": "deviceType"
      },
      {
        "value": "Owner",
        "key": "keyHolderType"
      },
      {
        "value": "xxx",
        "key": "vehicleId"
      },
      {
        "value": "xxx",
        "key": "personalizedData"
      },
      {
        "value": "00000111",
        "key": "supportFunctionType"
      }
    ]
  },
  "linkDevicePass": {
    "webServiceURL": "https://xxx",
    "nfcType": "1",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "passVersion": "10.0",
    "spPublickey": "xxx",
    "token": "xxx"
  }
}
```

### 响应参数

返回结果中会携带预置模板中的信息一并返回。

### 调用示例

完整的调用示例，请参见[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)示例代码。

```java
public void addStdCarKeyInstance() {
    JSONObject instance = JSONObject.parseObject(ConfigUtil.readFile("StdCarKeyInstance.json"));
    HwWalletObjectUtil.validateInstance(instance);
    String urlSegment = "/v2/key_stdcar/instance";
    JSONObject responseInstance =
        serverApiService.postToWalletServer(urlSegment, JSONObject.toJSONString(instance));

    if (responseInstance.containsKey("serialNumber")) {
        String serialNumber = responseInstance.getString("serialNumber");
        JweTest test = new JweTest();
        test.generateThinJWEToBindUser(serialNumber);
    }
}
```

### 生成JWE数据

华为钱包车钥匙卡片的开通是基于JWE（JSON Web Encryption）方式。因此DK业务管理服务向钱包云服务申请创建车钥匙成功后，基于创建成功的车钥匙serialNumber生成JWE数据，并将其返回给车主App。JWE数据包含JWE Encrypted Key，iv，Ciphertext，signature，可参见如下步骤获取：

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

## 车钥匙数据更新

更新数字车钥匙卡片数据。

### 接口原型

* **承载协议**：HTTPS
* **请求方式**：PUT：全量更新；PATCH：局部更新
* **接口方向**：DK业务管理服务->钱包云服务
* **接口URL**：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/{cardType}/instance/{instanceId}

  cardType取值如下：

  key\_stdcar：汽车钥匙

  key\_stdbike：两轮车钥匙
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Authorization | 是 | String | 认证信息，将[获取AccessToken](wallet-rest-api-public.md#获取accesstoken)获取到的“access\_token”的值拼接在字符串“Bearer”之后，以空格符相隔，组成“Authorization”参数的值。 |
| Accept | 是 | String | 发送端可接受的数据类型，取值为：application/json;charset=UTF-8。 |

**Request Body**

参见[申请ICCE车钥匙](wallet-rest-api-carkey.md#申请icce钥匙)的请求体，如果是全量更新，与申请ICCE车钥匙接口请求体相同。如果是局部更新，则只需传入需要变更的数据体。

### 请求示例

```json
PATCH /hmspass/v2/key_stdcar/instance/100000 HTTP/1.1
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
public HwWalletObject invokeHwCreateKeyCarKeyObject() {
    HwWalletObject request = new HwWalletObject();
    request.setPassTypeIdentifier("hwpass.keycarkey.test");
    request.setPassStyleIdentifier("keyCarKeyModelTest");
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
    // 100000仅为instanceId的示例值，实际使用时请替换为真实的instanceId。
    String walletServerUrl = baseUrl + "/v2/key_stdcar/instance/100000";
    HttpEntity<JSONObject> entity = new HttpEntity<>(JSONObject.parseObject(JSONObject.toJSONString(request)), header);
    ResponseEntity<JSONObject> exchange =
        REST_TEMPLATE.exchange(walletServerUrl, HttpMethod.PATCH, entity, JSONObject.class);
    return JSONObject.parseObject(exchange.getBody().toJSONString(), HwWalletObject.class);
}
```

## 上传车端数据到DK服务器

车端可通过钱包提供的通道上传自定义数据，用于获取DK服务器存储的钥匙状态、权限信息等云端数据，钱包作为中间桥梁透传交互数据，提供完整的业务闭环渠道。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->DK业务管理服务
* **接口URL**：开发者在华为钱包管理台网站上提供的回调地址
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Accept | 是 | String | 发送端可接受的数据类型，取值为：identity。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| passTypeIdentifier | 是 | String | 服务号，格式为：hwpass.stdcarkey.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义）。 |
| serialNumber | 是 | String | Pass对象在发卡方的唯一键值，回调时以便发卡方根据此值识别具体的卡券记录。 |
| payload | 是 | String | 车端请求报文中的整个body部分，如03040102xxxx。 |
| signature | 是 | String | 钱包服务器使用signByRSAWithPSS方式对请求体的签名。 |

### 请求示例

```json
POST /api/callback HTTP/1.1
Content-Type: application/json;charset=UTF-8
Accept: identity
{
    "requestBody": {
      "passTypeIdentifier": "hwpass.xxx.xxx.xxx",
      "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "payload": "10101"
    },
    "signature": "xxx"
}
```

### 响应参数

| 父节点参数 | 子节点参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | 否 | String | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| response | payload | 否 | String | SP验证请求后，返回的数据。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "response": {
    "payload": "xxx"
  }
}
```

## 获取配对码

计算配对码返回给钱包App。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->DK业务管理服务
* **接口URL**：{webServiceURL}/v1/passes/requestPairCode
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 请求的数据类型，取值为：application/json;charset=UTF-8。 |
| Accept | 是 | String | 发送端可接受的数据类型，取值为：identity。 |

**Request Body**

| 父节点参数 | 子节点参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- | --- |
| requestBody | passTypeIdentifier | String | 是 | 创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 |
| requestBody | serialNumber | String | 是 | 车钥匙卡片在华为钱包云服务器中的卡号，回调时以便发卡方根据此值识别具体的卡券记录。 |
| requestBody | transPublicKey | String | 是 | 用于加密返回的对称秘钥，用于对返回的数据做数字信封。 |
| requestBody | userDeviceId | String | 是 | 用户在当前设备上的唯一标识。 |
| requestBody | transId | String | 是 | 请求唯一标识，为随机数。 |
| requestBody | vehicleType | String | 否 | 车辆标识类型，mac：车端蓝牙MAC地址、vin：车辆VIN码、readerId：NFC读头标识。默认值为mac。 |
| requestBody | vehicleId | String | 是 | 车辆标识，用于匹配对应的车辆。 |
| requestBody | vehicleBroadcast | String | 是 | 扫描到的车端广播报文，byte[]数组转十六进制字符。 |
| requestBody | connectionType | String | 否 | 支持的传入类型，0200：NFC、0201：NFC+BLE、0202：UWB、0203：SLE。默认值为0202。 |
| requestBody | timestamp | String | 是 | 请求时间戳，格式 yyyyMMddHHmmssSSS，校验请求消息送达时间为5分钟以内。 |
| requestBody | timeZone | String | 否 | 默认东八区，非国内需要传入时区，国内传空。 |
| severSignature | - | String | 是 | 钱包服务器使用私钥对请求体的签名值，签名算法：SHA256WithRSA/PSS。 |

### 请求示例

```json
POST /v1/passes/requestPairCode HTTP/1.1
Content-Type: application/json;charset=UTF-8
Accept: identity
{
    "requestBody": {
      "passTypeIdentifier": "xxx",
      "serialNumber": "xxx",
      "transPublicKey": "xxx",
      "transId": "xxx",
      "vehicleType": "xxx",
      "vehicleId": "xxx",
      "vehicleBroadcast": "xxx",
      "connectionType": "xxx",
      "timestamp": "xxx",
      "timeZone": "",
    },
    "severSignature": "xxx"
}
```

### 响应参数

| 父节点参数 | 子节点参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- | --- |
| Httpstatus | - | 是 | String | 接口网络状态码，参考[REST API错误码](wallet-rest-api-error-code.md)进行处理。 |
| response | encryptPairCode | 是 | String | SP Server通过生成的16个字节临时对称密钥key和iv加密配对码信息。对称加密算法使用AES-128-GCM，采用Base64编码。 |
| response | encryptSessionKey | 否 | String | SP Server生成AES128的16个字节临时对称密钥key和iv，按照transId+key+iv拼接即为sessionKey，用于加密生成encryptPairCode。  使用请求中transPublicKey字段加密sessionKey即为encryptSessionKey，RSA算法: RSA/ECB/OAEPWithSHA-256AndMGF1Padding，对结果进行base64编码即可。 |
| signature | - | 否 | String | SP Server对response的Hash值进行签名。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "httpStatus": "0",
  "response": {
    "encryptPairCode": "xxx",
    "encryptSessionKey": "xxx",
  }
}
```

## 车钥匙迁移

用户更换移动设备后，车钥匙自动迁移至新设备，无须重新线下配对，保障用户持续使用数字车钥匙的便捷体验。

### 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：钱包云服务->DK业务管理服务
* **接口URL**：{webServiceURL}/v2/passes/transfer
* **数据格式**：

  请求消息：Content-Type: application/json;charset=UTF-8

  响应消息：Content-Type: application/json;charset=UTF-8

### 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| signType | 是 | String | 签名方式，固定值：'SHA256WithRSA/PSS'。 |
| sign | 是 | String | 对整个消息体的签名值。 |
| signVersion | 否 | String | 本次签名使用的秘钥版本号，默认值为0。 |
| version | 是 | String | 接口版本号，固定值：'V2'。 |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| requestNo | 是 | String | 请求流水号，单次请求的唯一标识。 |
| passData | 是 | String | 原始的Pass数据。 |
| userDeviceId | 是 | String | 用户在当前设备上的唯一标识。 |
| deviceCategory | 是 | String | 设备类型，phone: 手机、wear: 穿戴，默认值为phone。 |
| deviceModel | 是 | String | 设备名，用于展示可开通的设备名称。 |
| deviceModelNumber | 是 | String | 设备型号编码，用于获取匹配的标定数据。 |
| capabilitySetInfo | 否 | String | 能力集信息，同步返回是否支持NFC/BLE/UWB/SLE。0200：NFC、0201：NFC+BLE、0202：UWB、0203：SLE。 |
| openId | 否 | String | 华为账号OpenId，开通时传入，用于车企后台发卡的车钥匙关联华为账号OpenId。兼容处理：存量钥匙未关联openId，放通不校验。 |
| transferScene | 否 | String | 迁移场景，预留字段，包括克隆以及其他批量/主动添卡场景。phoneClone：克隆、userOperation：其他。 |
| timestamp | 是 | String | 时间戳。 |

### 请求示例

```json
POST /v2/passes/transfer HTTP/1.1
Content-Type: application/json;charset=UTF-8
signType: SHA256WithRSA/PSS
sign: u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExH********************g
signVersion: 0
version: V2
{
    "requestNo": "xxx",
    "passData": "xxx",
    "userDeviceId": "xxx",
    "deviceCategory": "xxx",
    "deviceModel": "xxx",
    "deviceModelNumber": "xxx",
    "capabilitySetInfo": "xxx",
    "openId": "xxx",
    "transferScene": "xxx",
    "timestamp": ""
}
```

### 响应参数

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| returnCode | 是 | String | 响应结果码。0：成功；1010：原钥匙已经删除；1011：openId不一致，迁移失败。 |
| returnDesc | 是 | String | 返回值描述。success: 成功、其他：失败。 |
| jweData | 否 | String | jwe数据，响应结果码为0时必选，否则可空。 |

### 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "returnCode": "0",
  "returnDesc": "success",
  "jweData": "xxx",
}
```
