---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-rest-receive
title: 归因结果回传
category: harmonyos-references
scraped_at: 2026-04-28T08:16:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e140db10902e3cb1c06fc199302d4ffb45cf09d0ccf6bad384ec5dd655d5173
---

## 功能介绍

应用归因服务将满足隐私要求的归因结果回传给开发者、获胜的分发平台以及分发平台配置的归因监测平台。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 华为应用归因端侧 -> （分发平台/开发者/归因监测平台）
* **接口URL：** 应用生态伙伴在归因云端管理台注册归因角色时填写的URL地址
* **数据格式：**

  请求消息： Content-Type: application/json

  响应消息： Content-Type: application/json

## 请求参数

**Request Body**

| 参数 | 参数类型 | 是否必选 | 是否参与签名 | 描述 |
| --- | --- | --- | --- | --- |
| ad\_tech\_id | String | 否 | 是 | 归因成功的分发平台id，分发平台向应用归因云侧注册角色时，由应用归因服务分配，长度固定为8个字符如果接收方为分发平台，该id即分发平台自身的id。  如果接收方为归因监测平台/开发者，该id为归因监测平台/开发者注册转化时指定分发平台列表中归因成功的分发平台id。 |
| campaign\_id | String | 否 | 是 | 本次转化归因到的营销任务id，仅当满足回传条件时携带。 |
| source\_id | String | 否 | 是 | 媒体应用id，长度不超过64个字符，仅当满足回传条件时携带。 |
| destination\_id | String | 否 | 是 | 开发者应用id，长度不超过64个字符 。  **说明：** 您的应用ID参考[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)获取。 |
| service\_tag | String | 否 | 否 | 业务标识。  回传分发平台时，为分发平台关注的业务信息，如创意、素材等；  回传开发者时，为开发者关注的业务信息，如激活、付费相关营销链接信息。  **说明：** 通过[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)方式向分发平台、开发者开放。 |
| business\_scene | number | 否 | 否 | 业务场景值，仅开发者满足回传条件时携带。  取值范围：[0,99]。  **说明：** 通过[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)方式向开发者开放。 |
| trigger\_data | number | 否 | 是 | 转化事件编码。  [标准转化事件](../harmonyos-guides/store-attribution-trigger-standard.md)取值范围：[1, 200]。  [自定义转化事件](../harmonyos-guides/store-attribution-trigger-custom.md)取值范围：[501, 600]。 |
| installation\_status | number | 否 | 否 | 应用安装状态。  **说明：** 通过[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)方式向应用生态伙伴（分发平台、开发者、归因监测平台）开放。 |
| nonce | String | 是 | 是 | 用于计算签名的随机数，不带"-"，由应用归因服务生成，每次归因结果回传，nonce唯一。 |
| timestamp | number | 是 | 是 | 回传发生的时间戳，建议校验时判断与当前时间相差不超过5min，unix时间戳，毫秒。 |
| signature | String | 是 | 否 | 签名值。接收方应使用应用归因服务提供的[公钥](../harmonyos-guides/store-attribution-receive.md#验签计算规则)，对该签名值进行验签，具体参考[验签计算规则](../harmonyos-guides/store-attribution-receive.md#验签计算规则)、[回传结果验签方法](store-rest-receive.md#回传结果验签方法)。 |
| adSourceTime | String | 是 | 否 | 回传获胜方来源登记营销事件发生时间。  **说明：** 通过[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)方式向应用生态伙伴（分发平台、开发者、归因监测平台）开放。 |
| transaction\_id | String | 是 | 否 | 本次回传的事务id，唯一，接收方可用于请求的幂等处理。 |

## 请求示例

```
1. POST https://xxxxxxxx/attribution/report-attribution
2. Content-Type: application/json
3. {
4. "ad_tech_id":"12345678",
5. "campaign_id":"50",
6. "source_id":"108****321",
7. "destination_id":"101****678",
8. "trigger_data":12,
9. "nonce":"17aa292c****4516****25150****195",
10. "timestamp":167****380,
11. "signature":"MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg==",
12. "transaction_id":"aa****aaaa"
13. }
```

## 响应参数

**Response Header**

| 参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| Content-Type | String | 是 | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| resultCode | String | 是 | 应用归因侧解析application/json类型响应，“0”表示成功，其他值失败。 |
| resultDesc | String | 是 | 结果描述。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "0",
5. "resultDesc": "Success."
6. }
```

## 回传结果验签方法

1. 您需要在pom.xml文件中引入最新版本的开源密码算法包[Bouncy Castle](https://www.bouncycastle.org/download/bouncy-castle-java/)。

   ```
   1. <dependency>
   2. <groupId>org.bouncycastle</groupId>
   3. <artifactId>bcprov-jdk18on</artifactId>
   4. <version>${last_version}</version>
   5. </dependency>
   6. <dependency>
   7. <groupId>commons-codec</groupId>
   8. <artifactId>commons-codec</artifactId>
   9. <version>${last_version}</version>
   10. </dependency>
   ```
2. 您可以使用以下代码对回传请求中签名值进行验签。

   ```
   1. import org.apache.commons.codec.binary.Base64;
   2. import org.bouncycastle.jce.provider.BouncyCastleProvider;
   3. import java.nio.charset.StandardCharsets;
   4. import java.security.InvalidKeyException;
   5. import java.security.KeyFactory;
   6. import java.security.NoSuchAlgorithmException;
   7. import java.security.PublicKey;
   8. import java.security.Security;
   9. import java.security.Signature;
   10. import java.security.SignatureException;
   11. import java.security.spec.InvalidKeySpecException;
   12. import java.security.spec.X509EncodedKeySpec;

   14. /**
   15. * 回传结果验签工具类
   16. *
   17. * @author ******
   18. * @since ****-**-**
   19. */
   20. public class PostbackResultVerifyUtil {
   21. private static String publicKey = "MIIBoj*****AAE=";
   22. private static final String RSA_ALGORITHM = "RSA";
   23. private static final String SHA256WithRSA_PSS_ALGORITHM = "SHA256WithRSA/PSS";

   25. /**
   26. * 回传结果验签调用方法
   27. *
   28. * @param content 签名内容拼接字段
   29. * @param signature 回传请求中的签名值
   30. * @return 验签结果
   31. * @throws NoSuchAlgorithmException NoSuchAlgorithmException
   32. * @throws InvalidKeySpecException InvalidKeySpecException
   33. * @throws InvalidKeyException InvalidKeyException
   34. * @throws SignatureException SignatureException
   35. */
   36. public boolean verify(String content,String signature)
   37. throws NoSuchAlgorithmException, InvalidKeySpecException, InvalidKeyException, SignatureException {
   38. byte[] plainContent = content.getBytes(StandardCharsets.UTF_8);
   39. byte[] signContent = decodeBase64(signature);
   40. Security.addProvider(new BouncyCastleProvider());
   41. PublicKey pubKey = getPublicKey(publicKey);
   42. Signature rsaSignature = Signature.getInstance(SHA256WithRSA_PSS_ALGORITHM);
   43. rsaSignature.initVerify(pubKey);
   44. rsaSignature.update(plainContent);
   45. return rsaSignature.verify(signContent);
   46. }

   48. private PublicKey getPublicKey(String key) throws NoSuchAlgorithmException, InvalidKeySpecException {
   49. X509EncodedKeySpec keySpec = new X509EncodedKeySpec(decodeBase64(key));
   50. KeyFactory keyFactory = KeyFactory.getInstance(RSA_ALGORITHM);
   51. return keyFactory.generatePublic(keySpec);
   52. }

   54. private byte[] decodeBase64(String base64Str) {
   55. return Base64.decodeBase64(base64Str.getBytes(StandardCharsets.UTF_8));
   56. }
   57. }
   ```

   说明

   回传结果验签调用方法verify(String content,String signature)中：

   content：签名内容拼接字段，拼接方式可参考[验签计算规则](../harmonyos-guides/store-attribution-receive.md#验签计算规则)。

   signature：回传请求中的签名值。
