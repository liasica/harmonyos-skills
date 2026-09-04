---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-real-name-preparations
title: （可选）用户身份验证服务接入准备
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > （可选）用户身份验证服务接入准备
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a4c656c862ea7702e17bf814add1a96d25bd1979b20da67c38886d6f1ed3510a
---

如不涉及身份验证服务接入，可跳过该章节。

## 开启用户身份验证服务权限开关

开发者可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“项目设置 > 开放能力管理”的“鸿蒙支付服务”中开启身份验证服务相关权限开关。

**说明** 

开启身份验证服务相关权限开关时，开发者需签署一份“开发者协议”，开发者同意协议并提交申请资料后需要等待审核（审核周期一般在1-3个工作日）通过后才能使用相关服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/MJWTVNBZSmWkwZQX07AoPQ/zh-cn_image_0000002712405310.png)

## 上传开发者公钥及下载华为公钥

开发者可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“鸿蒙支付服务 > 身份验证服务”菜单中的“公钥管理”页签下完成开发者证书的上传以及华为公钥证书下载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ffqXZ8fYRDy4LnReLapuMQ/zh-cn_image_0000002742124259.png)

证书使用如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/hlfgsTdKTBO8inVcV8yZTg/zh-cn_image_0000002712245352.png)

证书说明如下：

| 证书 | 获取方式 | 内容说明及使用场景 |
| --- | --- | --- |
| **华为加密公钥** | [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)的“鸿蒙支付服务>身份验证服务>公钥管理”下载 | 华为支付服务器使用SM2加密算法生成的证书公钥。  **使用场景：** 开发者可用对应的公钥证书对请求开放API接口的隐私字段进行加密，华为支付服务器使用配对的私钥证书对隐私字段进行解密。 |
| **华为签名公钥** | [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)的“鸿蒙支付服务>身份验证服务>公钥管理”下载 | 华为支付服务器使用SM2加密算法生成的证书公钥。  **使用场景：** 华为支付服务器使用配对的私钥证书对响应报文进行加签， 开发者用于对开放API接口响应报文验签使用，具体验签方式请参见[验签规则](../harmonyos-references/payment-rest-overview.md#验签规则)。 |
| **开发者公钥**（**加密**） | 开发者生成 | 开发者使用SM2加密算法生成的证书公钥。需登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“鸿蒙支付服务>身份验证服务>公钥管理”上传（公钥类型为加密）。  **使用场景：** 开发者上传后生成证书Id（developerEncKeyId），开发者请求开放API接口时可通过[PayDevAuth](../harmonyos-references/payment-model.md#paydevauth)请求头传递，指定给华为支付服务器用于对开放API接口响应的隐私字段加密。 |
| **开发者公钥（签名）** | 开发者生成 | 开发者使用SM2加密算法生成的证书公钥。需登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“鸿蒙支付服务>身份验证服务>公钥管理”上传（公钥类型为签名）。  **使用场景：** 开发者上传后生成证书Id（developerSignKeyId），开发者请求开放API接口时可通过[PayDevAuth](../harmonyos-references/payment-model.md#paydevauth)请求头传递，指定给华为支付服务器用于对开放API接口请求报文进行验签。 |

### SM2公私钥对生成示例代码参考

**注意** 

* 只支持ASN.1格式的SM2公私钥对（以下示例代码为服务端生成示例）。如需在应用端生成ASN.1格式SM2公私钥对（公钥91字节，私钥51字节）可参考：

1. [随机生成非对称密钥对(ArkTS)](crypto-generate-asym-key-pair-randomly.md)（应用端生成的公私钥对可能无法在服务端使用）。
2. 参考[数据编码格式差异](crypto-development-practice.md#数据编码格式差异)将生成的秘钥对转成16进制hex格式。

* 生成的SM2公私钥对，还请先自测验证加解密是否正常，正常后再正式对外使用，避免生成错误的公私钥对，阻塞后续业务进度。

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.util.encoders.Hex;
import org.junit.Test;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.spec.ECGenParameterSpec;
import java.util.HashMap;

public class GenerateSm2KeyPairTest2 {
  public static void main(String[] args) {
    try {
      // 获取sm2公私钥
      String jsonObject = getSm2SecretKey();
      // 可打印生成公私钥信息，例如：log.info(jsonObject);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  /**
   * 生成SM2的ASN.1格式的公私钥
   *
   * @return SM2的ASN.1格式的公私钥
   */
  public static String getSm2SecretKey() {
    try {
      KeyPair keyPair = generateSm2KeyPair();
      String privateKeyStr = Hex.toHexString(keyPair.getPrivate().getEncoded());
      String publicKeyStr = Hex.toHexString(keyPair.getPublic().getEncoded());
      HashMap<String, String> result = new HashMap<>();
      result.put("Sm2PrivateKey", privateKeyStr);
      result.put("Sm2PublicKey", publicKeyStr);
      return result.toString();
    } catch (Exception e) {
      return null;
    }
  }

  /**
   * SM2算法生成ASN.1格式的公私钥对
   *
   * @return 密钥对信息
   */
  public static KeyPair generateSm2KeyPair() throws Exception {
    try {
      final ECGenParameterSpec sm2Spec = new ECGenParameterSpec("sm2p256v1");
      // 获取一个椭圆曲线类型的密钥对生成器
      final KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC", new BouncyCastleProvider());
      SecureRandom random = new SecureRandom();
      // 使用SM2的算法区域初始化密钥生成器
      kpg.initialize(sm2Spec, random);
      // 获取密钥对
      KeyPair keyPair = kpg.generateKeyPair();
      return keyPair;
    } catch (Exception e) {
      throw new SecurityException("generateSm2KeyPair failed.");
    }
  }
}
```

### SM2加密示例代码参考

```java
import lombok.extern.slf4j.Slf4j;
import org.bouncycastle.asn1.ASN1ObjectIdentifier;
import org.bouncycastle.asn1.gm.GMNamedCurves;
import org.bouncycastle.asn1.x509.AlgorithmIdentifier;
import org.bouncycastle.asn1.x509.SubjectPublicKeyInfo;
import org.bouncycastle.asn1.x9.X9ECParameters;
import org.bouncycastle.asn1.x9.X9ObjectIdentifiers;
import org.bouncycastle.crypto.engines.SM2Engine;
import org.bouncycastle.crypto.params.ECDomainParameters;
import org.bouncycastle.crypto.params.ECPublicKeyParameters;
import org.bouncycastle.crypto.params.ParametersWithRandom;
import org.bouncycastle.math.ec.ECPoint;
import org.bouncycastle.util.encoders.Hex;

import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;

@Slf4j
public class SM2EncTest {
  public static void main(String[] args) {
    encrypt("16进制编码的SM2公钥", "待加密数据");
  }

  public static String encrypt(String pubKey, String data) {
    SM2Engine sm2Engine = new SM2Engine(SM2Engine.Mode.C1C3C2);
    if (data == null || data.isEmpty()) {
      return data;
    }
    byte[] in = data.getBytes(StandardCharsets.UTF_8);
    return Hex.toHexString(encrypt(pubKey, in, sm2Engine));
  }

  private static byte[] encrypt(String pubKey, byte[] in, SM2Engine sm2Engine) {
    try {
      byte[] bPubKey = Hex.decode(pubKey);
      byte[] coding = getCoding(bPubKey);
      X9ECParameters x9ECParameters = GMNamedCurves.getByName("sm2p256v1");
      ECDomainParameters ecDomainParameters = new ECDomainParameters(x9ECParameters.getCurve(),
              x9ECParameters.getG(), x9ECParameters.getN());
      ECPoint pukPoint = x9ECParameters.getCurve().decodePoint(coding);
      ECPublicKeyParameters publicKeyParameters = new ECPublicKeyParameters(pukPoint, ecDomainParameters);
      sm2Engine.init(true, new ParametersWithRandom(publicKeyParameters, new SecureRandom()));
      return sm2Engine.processBlock(in, 0, in.length);
    } catch (Exception e) {
        log.error("exception: ", e);
        throw new SecurityException(e);
    }
  }

  private static byte[] getCoding(byte[] publicKey) {
    if (publicKey.length != 64 && publicKey.length != 65) {
      AlgorithmIdentifier aid = new AlgorithmIdentifier(
              X9ObjectIdentifiers.id_ecPublicKey, new ASN1ObjectIdentifier("1.2.156.10197.1.301"));
      SubjectPublicKeyInfo info = SubjectPublicKeyInfo.getInstance(publicKey);
      if (!aid.equals(info.getAlgorithm())) {
        throw new SecurityException("encoded not valid");
      } else {
        byte[] coding = info.getPublicKeyData().getBytes();
        if (coding.length != 65) {
          throw new SecurityException("encoded not valid");
        } else {
          return coding;
        }
      }
    } else {
      if (publicKey.length == 64) {
        byte[] bytes = new byte[65];
        bytes[0] = 4;
        System.arraycopy(publicKey, 0, bytes, 1, 64);
        publicKey = bytes;
      }
      return (byte[]) publicKey.clone();
    }
  }
}
```

### SM2解密示例代码参考

```java
import lombok.extern.slf4j.Slf4j;
import org.bouncycastle.asn1.ASN1Integer;
import org.bouncycastle.asn1.ASN1OctetString;
import org.bouncycastle.asn1.ASN1Primitive;
import org.bouncycastle.asn1.ASN1Sequence;
import org.bouncycastle.asn1.ASN1Set;
import org.bouncycastle.asn1.ASN1TaggedObject;
import org.bouncycastle.asn1.gm.GMNamedCurves;
import org.bouncycastle.asn1.sec.ECPrivateKey;
import org.bouncycastle.asn1.x509.AlgorithmIdentifier;
import org.bouncycastle.asn1.x9.X9ECParameters;
import org.bouncycastle.crypto.engines.SM2Engine;
import org.bouncycastle.crypto.params.ECDomainParameters;
import org.bouncycastle.crypto.params.ECPrivateKeyParameters;
import org.bouncycastle.util.encoders.Hex;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.util.Enumeration;

@Slf4j
public class SM2DecTest {
  public static void main(String[] args) {
    String data = decrypt("16进制编码解密私钥", "密文");
    System.out.println(data);
  }

  private static String decrypt(String priKey, String cipherData) {
    SM2Engine sm2Engine = new SM2Engine(SM2Engine.Mode.C1C3C2);
    if (cipherData == null || cipherData.isEmpty()) {
      throw new SecurityException("cipher data is empty when decrypt data");
    }
    if (priKey == null || priKey.isEmpty()) {
      throw new SecurityException("pri key is empty when decrypt data");
    }
    try {
      X9ECParameters x9ECParameters = GMNamedCurves.getByName("sm2p256v1");
      ECDomainParameters ecDomainParameters = new ECDomainParameters(x9ECParameters.getCurve(),
              x9ECParameters.getG(), x9ECParameters.getN());
      byte[] bPriKey = Hex.decode(priKey);
      byte[] enContent = Hex.decode(cipherData);
      BigInteger privateKeyD;
      if (bPriKey.length != 32 && bPriKey.length != 33) {
        privateKeyD = getDInt(bPriKey);
      } else {
        privateKeyD = new BigInteger(bPriKey);
      }
      ECPrivateKeyParameters privateKeyParameters = new ECPrivateKeyParameters(privateKeyD, ecDomainParameters);
      sm2Engine.init(false, privateKeyParameters);
      return new String(sm2Engine.processBlock(enContent, 0, enContent.length), StandardCharsets.UTF_8);
    } catch (Exception e) {
        log.error("exception: ", e);
        throw new SecurityException(e);
    }
  }

  private static BigInteger getDInt(byte[] bytesKey) throws IOException {
    ASN1Sequence sequence = ASN1Sequence.getInstance(bytesKey);
    Enumeration e = sequence.getObjects();
    BigInteger version = ((ASN1Integer) e.nextElement()).getValue();
    if (version.intValue() != 0) {
      throw new IllegalArgumentException("wrong version for private key info");
    }
    AlgorithmIdentifier algId = AlgorithmIdentifier.getInstance(e.nextElement());
    ASN1OctetString privKey = ASN1OctetString.getInstance(e.nextElement());
    ASN1Set attributes;
    if (e.hasMoreElements()) {
      attributes = ASN1Set.getInstance((ASN1TaggedObject) e.nextElement(), false);
    }
    ASN1Primitive primitive = ASN1Primitive.fromByteArray(privKey.getOctets());
    ECPrivateKey privateKey = ECPrivateKey.getInstance(primitive);
    return privateKey.getKey();
  }
}
```
