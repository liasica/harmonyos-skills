---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-12
title: ID Token的使用场景与使用方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > ID Token的使用场景与使用方法
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:89eed20a508038ade2da323da050b9945ab397e9c138d61c61a73e8519f90aee
---

ID Token是OIDC（[OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html)）协议相对于OAuth 2.0协议扩展的一个用户身份凭证。

ID Token 是 JWT Token格式，意味着：

1. 用户的身份信息直接被编码进了ID Token，不需要额外请求其他的资源来获取用户信息。
2. ID Token 可以验证其是华为账号服务颁发的，携带华为账号签名信息，验证签名可证明其没有被篡改过。

## 使用场景

1. 应用无服务器，只有客户端，该场景下无法使用Authorization Code完成服务器侧的接口调用获取用户信息，需从ID Token中解析出用户信息；
2. 应用有服务器，希望在服务器侧解析ID Token对应字段，获取用户信息。

## 字段说明

ID Token是JWT Token格式数据，其中payload包含字段如下：

| 字段 | 参数类型 | 是否默认返回 | 描述 |
| --- | --- | --- | --- |
| iss | string | 是 | 固定值："https://accounts.huawei.com"。 |
| sub | string | 是 | 即用户的UnionID。同一个开发者下的所有应用，此参数均相同。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。 |
| aud | string | 是 | 接收ID Token的Client ID。 |
| exp | number | 是 | ID Token的过期时间戳（10位）。 |
| iat | number | 是 | ID Token的生成时间戳（10位）。 |
| at\_hash | string | 是 | Access Token的哈希值。 |
| azp | string | 是 | 生成ID Token的Client ID。 |
| openid | string | 是 | 用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。 |
| nonce | string | 否 | 防重放攻击随机值。详情请参考[LoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#loginwithhuaweiidrequest)或[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)的nonce字段说明。 |
| picture | string | 否 | 用户头像图片链接。该字段返回场景：[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中的scopes包含profile。 |
| display\_name | string | 否 | 华为账号对应的昵称，没有昵称则取匿名化的邮箱或手机号。该字段返回场景：  [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中的scopes包含profile。 |
| nickname | string | 否 | 华为账号对应的昵称。该字段返回场景：  [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中的scopes包含profile。 |

## 解析与验证

### **服务端解析与验证**

使用场景：有服务器应用。

对于有应用服务端的应用，推荐在服务端进行ID Token解析与验证，具体参考以下Maven工程依赖配置及Java示例代码。

Maven工程依赖：

```xml
<dependencies>
    <dependency>
        <groupId>com.alibaba.fastjson2</groupId>
        <artifactId>fastjson2</artifactId>
        <version>2.0.51</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk18on</artifactId>
        <version>1.74</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.6</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>com.auth0</groupId>
        <artifactId>jwks-rsa</artifactId>
        <version>0.8.2</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>com.auth0</groupId>
        <artifactId>java-jwt</artifactId>
        <version>3.8.1</version> <!--此处替换为您项目需要的版本-->
    </dependency>
</dependencies>
```

Java代码示例：

```java
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.JSONObject;
import com.auth0.jwk.InvalidPublicKeyException;
import com.auth0.jwk.Jwk;
import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTDecodeException;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.auth0.jwt.exceptions.TokenExpiredException;
import com.auth0.jwt.interfaces.DecodedJWT;
import org.apache.commons.codec.binary.Base64;
import org.apache.http.HttpEntity;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import java.security.Security;
import java.security.Signature;
import java.security.interfaces.RSAPublicKey;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class IDTokenParser {
    // 请替换为您的Client ID
    private final static String CLIENT_ID = "123456";
    private final static int MAX_PUBLIC_KEY_SIZE = 4;
    // 缓存jwt公钥信息
    private final Map<String, RSAPublicKey> keyId2PublicKey = new HashMap<>();
    /**
     * JWK JSON Web Key端点，开发者可以从该端点获取最近两天的JWK
     * 公钥在24小时内更新。确保以下ID Token在24小时内生成
     */
    private static final String CERT_URL = "https://oauth-login.cloud.huawei.com/oauth2/v3/certs";
    // ID Token的issuer
    public static final String ID_TOKEN_ISSUE = "https://accounts.huawei.com";
    public static final String ALG_RS256 = "RS256";
    public final static String ALG_PS256 = "PS256";
    public static void main(String[] args) throws Exception {
        // 由上述CLIENT_ID对应值生成的ID Token
        String idToken = "<ID Token>";
        IDTokenParser idTokenParser = new IDTokenParser();
        JSONObject idTokenInfo = idTokenParser.verifyAndParse(idToken);
        // 解析获取ID Token中的数据，例：解析获取iss
        String iss = idTokenInfo.getString("iss");
    }
    /**
     * 验证并解析ID Token
     * @param idToken idToken
     * @return ID Token携带的信息
     * @throws Exception 异常
     */
    public JSONObject verifyAndParse(String idToken) throws Exception {
        try {
            DecodedJWT decoder = JWT.decode(idToken);
            if (!decoder.getIssuer().equals(ID_TOKEN_ISSUE)) {
                // issuer校验不通过，抛出异常（异常类型可自行选择）
                throw new RuntimeException("issuer no match");
            }
            if (decoder.getAudience().size() > 0) {
                if (!decoder.getAudience().get(0).equals(CLIENT_ID)) {
                    // audience校验不通过，抛出异常（异常类型可自行选择）
                    throw new RuntimeException("audience no match");
                }
            }
            // 获取ID Token签名使用的算法
            String alg = decoder.getAlgorithm();
            if (ALG_RS256.equals(alg)) {
                Algorithm algorithm = Algorithm.RSA256(getRSAPublicKeyByKid(decoder.getKeyId()), null);
                JWTVerifier verifier = JWT.require(algorithm).build();
                JSONObject jsonObject = JSONObject.parseObject(new String(Base64.decodeBase64(decoder.getPayload())));
                // 验证签名
                verifier.verify(decoder);
                jsonObject.put("alg", decoder.getAlgorithm());
                jsonObject.put("typ", decoder.getType());
                jsonObject.put("kid", decoder.getKeyId());
                return jsonObject;
            } else if (ALG_PS256.equals(alg)) {
                PS256Algorithm algorithm = new PS256Algorithm(getRSAPublicKeyByKid(decoder.getKeyId()));
                boolean verifyResult = algorithm.verify(decoder.getHeader(), decoder.getPayload(),
                    decoder.getSignature());
                if (verifyResult) {
                    JSONObject jsonObject = JSONObject.parseObject(
                        new String(Base64.decodeBase64(decoder.getPayload())));
                    jsonObject.put("alg", decoder.getAlgorithm());
                    jsonObject.put("typ", decoder.getType());
                    jsonObject.put("kid", decoder.getKeyId());
                    return jsonObject;
                }
            }
            return null;
        } catch (JWTDecodeException e) {
            // ID Token解析失败，此场景常见于ID Token格式不正确
            throw new RuntimeException("ID Token decode failed");
        } catch (TokenExpiredException e) {
            // ID Token已过期
            throw new RuntimeException("ID Token expired");
        }
    }
    /**
     * 通过kid获取公钥信息，请缓存公钥信息，示例中采用map方式进行缓存，开发者可选择其它合适的方式进行缓存
     * @param keyId  keyId
     * @return 公钥信息
     * @throws InvalidPublicKeyException 异常
     */
    private RSAPublicKey getRSAPublicKeyByKid(String keyId) throws InvalidPublicKeyException {
        if (keyId2PublicKey.get(keyId) != null) {
            return keyId2PublicKey.get(keyId);
        }
        JSONArray keys = getJwks();
        if (keys == null) {
            return null;
        }
        if (keyId2PublicKey.size() > MAX_PUBLIC_KEY_SIZE) {
            keyId2PublicKey.clear();
        }
        for (int i = 0; i < keys.size(); i++) {
            String kid = keys.getJSONObject(i).getString("kid");
            String alg = keys.getJSONObject(i).getString("alg");
            if (ALG_RS256.equals(alg) || ALG_PS256.equals(alg)) {
                keyId2PublicKey.put(kid, getRsaPublicKeyByJwk(keys.getJSONObject(i)));
            }
        }
        return keyId2PublicKey.get(keyId);
    }
    /**
     * 从https://oauth-login.cloud.huawei.com/oauth2/v3/certs获取jwt公钥信息jwk
     * 因为jwk每天都会更新，所以需要缓存jwk
     * @return JSONObject 公钥信息数组
     */
    private static JSONArray getJwks() {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(CERT_URL);
        RequestConfig requestConfig = RequestConfig.custom()
            .setConnectTimeout(5000)
            .setConnectionRequestTimeout(5000)
            .setSocketTimeout(5000)
            .build();
        httpGet.setConfig(requestConfig);
        try {
            CloseableHttpResponse response = httpClient.execute(httpGet);
            HttpEntity entity = response.getEntity();
            String result = EntityUtils.toString(entity);
            return JSONObject.parseObject(result).getJSONArray("keys");
        } catch (Exception e) {
            return null;
        } finally {
            if (null != httpClient) {
                try {
                    httpClient.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
    /**
     * 通过jwk获取公钥信息
     * @return RSAPublicKey 公钥信息
     */
    private static RSAPublicKey getRsaPublicKeyByJwk(JSONObject jwkObject) throws InvalidPublicKeyException {
        Map<String, Object> additionalAttributes = new HashMap<>();
        additionalAttributes.put("n", jwkObject.getString("n"));
        additionalAttributes.put("e", jwkObject.getString("e"));
        List<String> operations = new ArrayList<>();
        Jwk jwk = new Jwk(jwkObject.getString("kid"), jwkObject.getString("kty"), jwkObject.getString("alg"),
            jwkObject.getString("use"), operations, null, null, null, additionalAttributes);
        return (RSAPublicKey) jwk.getPublicKey();
    }
    static class PS256Algorithm {
        private final RSAPublicKey publicKey;
        public PS256Algorithm(RSAPublicKey publicKey) {
            this.publicKey = publicKey;
        }
        public boolean verify(String header, String payload, String signature) throws JWTVerificationException {
            byte[] contentBytes = (header + '.' + payload).getBytes(StandardCharsets.UTF_8);
            byte[] signatureBytes = Base64.decodeBase64(signature);
            try {
                Security.addProvider(new BouncyCastleProvider());
                Signature sign = Signature.getInstance("SHA256WithRSA/PSS");
                sign.initVerify(publicKey);
                sign.update(contentBytes);
                return sign.verify(signatureBytes);
            } catch (GeneralSecurityException e) {
                throw new JWTVerificationException("JWT verify failed");
            }
        }
    }
}
```

### **客户端解析与验证**

使用场景：无服务器应用。

对于无服务器应用，可在客户端获取ID Token后，进行本地解析与验证，解析后可获取用户数据，并验证签名，具体参考如下ArkTS代码示例，将获取的ID Token作为方法入参，并将代码中的CLIENT\_ID替换为应用真实的Client ID：

```typescript
import { buffer } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { http } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

decodeBase64(data: string): string {
  return buffer.from(data, 'base64').toString('utf8');
}

// 解析ID Token并验证
decodeIdToken(idToken: string): void {
  const parts = idToken.split('.');
  if (parts.length !== 3) {
    return;
  }
  const idTokenObj: Record<string, Object> = {};
  // ID Token头部
  idTokenObj['header'] = JSON.parse(this.decodeBase64(parts[0]));
  // ID Token负载
  idTokenObj['payload'] = JSON.parse(this.decodeBase64(parts[1]));
  // ID Token签名
  idTokenObj['signature'] = parts[2];
  const header: Record<string, string> = idTokenObj['header'] as Record<string, string>;
  // 从负载中解析出nonce等数据
  const payLoad: Record<string, string> = idTokenObj['payload'] as Record<string, string>;
  const nonce: string = payLoad['nonce'];
  // nonce可用于与请求体属性中的nonce作一致性比对，防止重放攻击
  // 应用Client ID，使用前请替换
  const CLIENT_ID: string = '<应用Client ID>';
  const ID_TOKEN_ISSUE: string = 'https://accounts.huawei.com';
  const iss: string = payLoad['iss'];
  const aud: string = payLoad['aud'];
  if (iss !== ID_TOKEN_ISSUE) {
    // 验证失败，开发者处理失败场景
    hilog.error(0x0000, 'testTag', 'Failed to check iss');
    return;
  }
  if (aud !== CLIENT_ID) {
    // 验证失败，开发者处理失败场景
    hilog.error(0x0000, 'testTag', 'Failed to check aud');
    return;
  }
  // 验证签名
  this.checkSignature(idToken, header['kid'], header['alg']);
}

private stringToUint8Array(str: string): Uint8Array {
  const arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  const tmpUint8Array: Uint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

// 验签方法
private checkSignature(idToken: string, kid: string, alg: string) {
  if (!idToken) {
    return;
  }
  const parts = idToken.split('.');
  if (parts.length !== 3) {
    return;
  }
  const url = 'https://oauth-login.cloud.huawei.com/oauth2/v3/certs';
  // 创建http请求，应用需在module.json5文件中先申请“ohos.permission.INTERNET”网络权限，请求才能发送成功
  const httpRequest = http.createHttp();
  httpRequest.request(url, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', `Failed to httpRequest. Code: ${err.code}, message: ${err.message}`);
      httpRequest.destroy();
      return;
    }
    let nStr = '';
    let eStr = '';
    const keys: object[] = JSON.parse(data.result as string)['keys'];
    for (let item of keys) {
      if (kid === item['kid']) {
        nStr = item['n'];
        eStr = item['e'];
        break;
      }
    }
    const nBigInt = '0x' + buffer.from(nStr, 'base64url').toString('hex');
    const eBigInt = '0x' + buffer.from(eStr, 'base64url').toString('hex');
    const dsaCommonSpec: cryptoFramework.RSACommonParamsSpec = {
      algName: 'RSA',
      specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
      n: BigInt(nBigInt),
    }
    const rsaKeyPairSpec: cryptoFramework.RSAPubKeySpec = {
      algName: 'RSA',
      specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC,
      params: dsaCommonSpec,
      pk: BigInt(eBigInt),
    }
    try {
      const asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaKeyPairSpec);
      asyKeyGeneratorBySpec.generatePubKey((error, publicKey) => {
        if (error) {
          return;
        }
        if (publicKey === null) {
          return;
        }
        const idTokenSign = parts[2];
        const idTokenSignArr: cryptoFramework.DataBlob =
          { data: new Uint8Array(buffer.from(idTokenSign, 'base64url').buffer) };
        const idToken = parts[0] + '.' + parts[1];
        const idTokenArr: cryptoFramework.DataBlob = { data: this.stringToUint8Array(idToken) };
        const verifier = alg === 'PS256' ? cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1_SHA256') :
          cryptoFramework.createVerify('RSA2048|PKCS1|SHA256');
        verifier.init(publicKey, () => {
          verifier.verify(idTokenArr, idTokenSignArr, (data) => {
            // 打印验签结果，结果为true则验签通过
            hilog.info(0x0000, 'testTag', 'verify result is: %{public}s', data);
          });
        });
      })
    } catch (err) {
      hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${err.code}, message: ${err.message}`);
    }
    httpRequest.destroy();
  });
}
```
