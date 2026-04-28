---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec
title: 对称密钥加解密算法规格
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密算法规格 > 对称密钥加解密算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:21+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9f9048a8725f25048880fda06710a5646d763a4386118c8043ad435bfffed65d
---

当前章节将说明系统目前支持的算法及其对应的规格。

对于每种算法采用支持的加密模式，将会在具体的每个算法规格中介绍。

## AES

算法库当前提供了[AES](crypto-sym-key-generation-conversion-spec.md#aes)加解密常用的7种加密模式：ECB、CBC、OFB、CFB、CTR、GCM和CCM。不同的加密模式适用的加解密参数不同，具体请参考[ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#paramsspec)。

由于AES为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。

由于需要填充至分组大小，所以实际算法库中的PKCS5和PKCS7都是以分组大小作为填充长度的，即AES加密填充至16字节。

说明

ECB、CBC加密模式，明文长度不是128位整数倍，必须使用填充方法补足。

CCM加密模式，必须指定附加验证数据aad且其长度必须大于等于1字节且小于等于2048字节。

当前支持以字符串参数完成AES加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

* 如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。

  举例说明：

  + 当需要分组模式为ECB、密钥长度为128bit、填充模式为PKCS7，其字符串参数为"AES128|ECB|PKCS7"。
  + 当需要分组模式为CFB、密钥长度为256bit、填充模式为NoPadding，其字符串参数为"AES256|CFB|NoPadding"。

  | 分组模式 | 密钥长度（bit） | 填充模式 | API版本 |
  | --- | --- | --- | --- |
  | ECB | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
  | CBC | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
  | CTR | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
  | OFB | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
  | CFB | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
  | GCM | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
  | CCM | [128|192|256] | [NoPadding|PKCS5|PKCS7] | 9+ |
* 从API版本10开始，支持对称加解密不带密钥长度的规格。加解密参数输入密钥类型时，支持不带长度，加解密运算取决于实际输入的密钥长度。

  举例说明，当需要分组模式为CFB、不带密钥长度、填充模式为NoPadding，其字符串参数为"AES|CFB|NoPadding"。

## DES

[DES](crypto-sym-key-generation-conversion-spec.md#des)算法的加密过程包含16轮相同的加密函数，每轮都使用不同的子密钥。子密钥是通过对原始密钥进行一系列的置换和移位操作生成的。在每一轮中，明文块被分为左右两部分，然后通过一系列的置换、替换和异或操作进行加密。

算法库当前提供了DES加解密常用的4种加密模式：ECB、CBC、OFB和CFB。不同的加密模式适用的加解密参数不同，具体请参考[ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#paramsspec)。

说明

ECB、CBC加密模式，明文长度不是64位整数倍，必须使用填充方法补足。

当前支持以字符串参数完成DES加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

* 如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。

  举例说明：

  + 当需要分组模式为ECB、密钥长度为64bit、填充模式为PKCS7，其字符串参数为"DES64|ECB|PKCS7"。
  + 当需要分组模式为OFB、密钥长度为64bit、填充模式为NoPadding，其字符串参数为"DES64|OFB|NoPadding"。

  | 分组模式 | 密钥长度（bit） | 填充模式 | API版本 |
  | --- | --- | --- | --- |
  | ECB | 64 | [NoPadding|PKCS5|PKCS7] | 20+ |
  | CBC | 64 | [NoPadding|PKCS5|PKCS7] | 20+ |
  | OFB | 64 | [NoPadding|PKCS5|PKCS7] | 20+ |
  | CFB | 64 | [NoPadding|PKCS5|PKCS7] | 20+ |
* 从API版本10开始，支持对称加解密不带密钥长度的规格。加解密参数输入密钥类型时，支持不带长度，加解密运算取决于实际输入的密钥长度。

  举例说明，当需要分组模式为CFB、不带密钥长度、填充模式为NoPadding，其字符串参数为"DES|CFB|NoPadding"。

## 3DES

[3DES](crypto-sym-key-generation-conversion-spec.md#section3des)算法的加解密过程分别是对明文/密文数据进行三次DES加密或解密，得到相应的密文或明文。

算法库当前提供了3DES加解密常用的4种加密模式：ECB、CBC、OFB和CFB。不同的加密模式适用的加解密参数不同，具体请参考[ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#paramsspec)。

由于DES为分组加密算法，分组长度为64位。在实际应用中，最后一组明文可能不足64位（8字节），此时可以通过不同的[填充模式](crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。

由于需要填充至分组大小，所以实际算法库中的PKCS5和PKCS7都是以分组大小作为填充长度的，即3DES加密填充至8字节。

说明

ECB、CBC加密模式，明文长度不是64位整数倍，必须使用填充方法补足。

当前支持以字符串参数完成3DES加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

* 如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。

  举例说明：

  + 当需要分组模式为ECB、密钥长度为192bit、填充模式为PKCS7，其字符串参数为"3DES192|ECB|PKCS7"。
  + 当需要分组模式为OFB、密钥长度为192bit、填充模式为NoPadding，其字符串参数为"3DES192|OFB|NoPadding"。

  | 分组模式 | 密钥长度（bit） | 填充模式 | API版本 |
  | --- | --- | --- | --- |
  | ECB | 192 | [NoPadding|PKCS5|PKCS7] | 9+ |
  | CBC | 192 | [NoPadding|PKCS5|PKCS7] | 9+ |
  | OFB | 192 | [NoPadding|PKCS5|PKCS7] | 9+ |
  | CFB | 192 | [NoPadding|PKCS5|PKCS7] | 9+ |
* 从API版本10开始，支持对称加解密不带密钥长度的规格。加解密参数输入密钥类型时，支持不带长度，加解密运算取决于实际输入的密钥长度。

  举例说明，当需要分组模式为CFB、不带密钥长度、填充模式为NoPadding，其字符串参数为"3DES|CFB|NoPadding"。

## SM4

算法库当前提供了[SM4](crypto-sym-key-generation-conversion-spec.md#sm4)加解密常用的7种加密模式：ECB、CBC、CTR、OFB、CFB、CFB128和GCM。不同的加密模式适用的加解密参数不同，具体请参考[ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#paramsspec)。

由于SM4为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。

由于需要填充至分组大小，所以实际算法库中的PKCS5和PKCS7都是以分组大小作为填充长度的，即SM4加密填充至16字节。

说明

ECB、CBC加密模式，明文长度不是128位整数倍，必须使用填充方法补足。

当前支持以字符串参数完成SM4加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

* 如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。SM4算法和密钥长度中间采用符号“\_”拼接。

  举例说明：

  + 当需要分组模式为ECB、密钥长度为128bit、填充模式为PKCS7，其字符串参数为"SM4\_128|ECB|PKCS7"。
  + 当需要分组模式为CFB、密钥长度为128bit、填充模式为NoPadding，其字符串参数为"SM4\_128|CFB|NoPadding"。
  + 当需要分组模式为GCM、密钥长度为128bit、填充模式为NoPadding，其字符串参数为"SM4\_128|GCM|NoPadding"。

  | 分组模式 | 密钥长度（bit） | 填充模式 | API版本 |
  | --- | --- | --- | --- |
  | ECB | 128 | [NoPadding|PKCS5|PKCS7] | 10+ |
  | CBC | 128 | [NoPadding|PKCS5|PKCS7] | 10+ |
  | CTR | 128 | [NoPadding|PKCS5|PKCS7] | 10+ |
  | OFB | 128 | [NoPadding|PKCS5|PKCS7] | 10+ |
  | CFB | 128 | [NoPadding|PKCS5|PKCS7] | 10+ |
  | CFB128 | 128 | [NoPadding|PKCS5|PKCS7] | 10+ |
  | GCM | 128 | [NoPadding|PKCS5|PKCS7] | 12+ |

## AES-WRAP

算法库提供AES-WRAP算法，该算法是一种基于[AES](crypto-sym-key-generation-conversion-spec.md#aes)的加密算法，用于安全地存储或传输对称密钥。它的主要目的是通过加密保护密钥，防止密钥在存储或传输过程中被泄露或篡改。

| 算法名称 | 字符串参数 | API版本 |
| --- | --- | --- |
| AES128\_WRAP | AES128\_WRAP | 22+ |
| AES256\_WRAP | AES256\_WRAP | 22+ |
| AES384\_WRAP | AES384\_WRAP | 22+ |

## 填充模式

分组加密算法有固定的分组长度，在实际应用中，最后一组明文的数据量可能无法达到固定的长度要求，此时可以通过不同的填充模式进行数据填充。填充模式有：

* NoPadding：不带填充。输入数据需要与分组长度匹配。
* PKCS5：填充字符由一个字节序列组成，而且每个字节填充的值与要填充的字节序列长度相同。PKCS5为8字节填充，即需将数据填充为八字节的倍数。
* PKCS7：填充方法和PKCS5一致。但PKCS7可以在1-255字节之间任意填充，PKCS5固定为8字节。

对于CFB、OFB、CTR、GCM、CCM这类将分组密码转化为流模式实现的模式，不需要填充，因此无论是否指定填充模式，都会按照NoPadding实现。

## ChaCha20

从API22开始，算法库支持该算法。

算法库当前提供了[ChaCha20](crypto-sym-key-generation-conversion-spec.md#chacha20)加解密，默认的ChaCha20加解密时需要传入IV。默认ChaCha20需要的加解密参数为[IvParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#ivparamsspec)。

常用的加密模式：Poly1305。Poly1305模式适用的加解密参数为[Poly1305ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#poly1305paramsspec22)。

由于ChaCha20是流算法，无需填充算法。

当前支持以字符串参数完成ChaCha20加解密，具体的“字符串参数”由“对称密钥类型”和“分组模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。

| 对称算法名 | 密钥长度（bit） | 字符串参数 | API版本 |
| --- | --- | --- | --- |
| ChaCha20 | 256 | ChaCha20 | 22+ |
| ChaCha20 | 256 | ChaCha20|Poly1305 | 22+ |
