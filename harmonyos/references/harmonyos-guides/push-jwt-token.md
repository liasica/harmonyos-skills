---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-jwt-token
title: 基于服务账号生成鉴权令牌
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > 基于服务账号生成鉴权令牌
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1edb6c4c29591a78319b8f50ad0089dbec96d7563937c39c1aede7b8c1759f05
---

## 概述

服务账号（Service Account）是一种可实现服务器与服务器之间接口鉴权的账号，在华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/api/myApi)上创建服务账号，您可根据返回的公私钥在业务应用中生成鉴权令牌，调用支持此类鉴权的华为公开API。

服务账号令牌为JWT（JSON Web Token）格式字符串，JWT数据格式包括三个部分：

* Header（头部）
* Payload（负载）
* Signature（签名）

这三个部分通过“.”进行连接，其中Signature为通过SHA256withRSA/PSS算法对Header与Payload拼接的字符串签名生成的字符串。

**示例**

```
1. eyJra*****JjNjBjMXXX.
2. eyJhd*****JodHRXXX.
3. BRNss*****7az5oU7-Zp5g9X2WJVXXX
```

更多JWT的相关知识请参见[Introduction to JSON Web Tokens](https://jwt.io/introduction/)。

## 开发步骤

1. 创建服务账号密钥文件。

   您需要在华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/api/myApi)上创建并下载推送服务API的服务账号密钥文件，凭证创建入口如下图所示，选择所在项目，创建“服务账号密钥“凭证。相关创建步骤请参见[API服务操作指南-服务账号密钥](../start/api-0000001062522591.md#section3554194116341)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/yXyq6GU9TQ6NPmhMX9vAGw/zh-cn_image_0000002583479129.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=3DC94A8BB9F7A36B6F1B4AC8AF083661377C6FCC385D99893E3EC9235A75F7F9)

   您申请后的服务账号密钥样例文件形式可参考（文件内容已经经过脱敏处理）：

   ```
   1. {
   2. "project_id": "*****",
   3. "key_id": "*****",
   4. "private_key": "-----BEGIN PRIVATE KEY-----\nMIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCKw6kJKtCh7qmMvp1u1dI27z2TKZrPOzHbQaXO/Eez0AWZ2EN+ouF496R3pfo7fQXC1XOT/YTbVC4DNZwWSMA54fu3/AOCY9Zzyi46OK*****==\n-----END PRIVATE KEY-----\n",
   5. "sub_account": "*****",
   6. "auth_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/authorize",
   7. "token_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
   8. "auth_provider_cert_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/certs",
   9. "client_cert_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/x509?client_id="
   10. }
   ```
2. 请确认以上密钥文件中的project\_id是否与您的应用所属项目一致。

   您的应用所属项目ID查看方法：登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/mN9iOSEVQkeA3QBc6so_pQ/zh-cn_image_0000002552799480.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=655B788A0A981CC7A327B8B776B781787CBCF144F7D1AB809AC955202733C650)
3. 生成JWT Header数据。

   根据服务账号密钥文件中的key\_id（对应示例中的kid）字段拼接以下JSON体，对JSON体进行BASE64编码。

   **示例**

   ```
   1. {
   2. "kid": "*****",
   3. "typ": "JWT",
   4. "alg": "PS256"
   5. }
   ```

   | 字段名 | 描述 |
   | --- | --- |
   | kid | 服务账号密钥文件中key\_id字段。 |
   | typ | 数据类型，固定为：JWT。 |
   | alg | 算法类型，固定为：PS256。 |
4. 生成JWT Payload数据。

   根据服务账号密钥文件中的sub\_account（对应示例中的iss）字段拼接以下JSON体，对JSON体进行BASE64编码。

   **示例**

   ```
   1. {
   2. "aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
   3. "iss": "*****",
   4. "exp": 1581410664,
   5. "iat": 1581407064
   6. }
   ```

   | 字段名 | 描述 |
   | --- | --- |
   | iss | 服务账号密钥文件中sub\_account字段，标识数据生成者。 |
   | aud | 固定为：https://oauth-login.cloud.huawei.com/oauth2/v3/token。 |
   | iat | JWT签发UTC时间戳，为自UTC时间1970年1月1日00:00:00起的秒数（您的服务器时间需要校准为标准时间）。 |
   | exp | JWT到期UTC时间戳，比iat晚3600秒。 |
5. 生成JWT Token。

   将完成BASE64编码后的Header字符串与Payload字符串，通过“.”进行连接，您可在业务应用中，通过服务账号密钥文件中的private\_key（华为不进行存储，请您妥善保管），使用SHA256withRSA/PSS算法对拼接的字符串签名。

   至此，您已经完成服务账号鉴权令牌JWT Token的生成。

## 调用推送服务REST API

您的应用调用推送服务REST API时，需要把已获得的服务账号鉴权令牌放在Authorization头部来进行鉴权。请使用v3版本调用推送服务REST API。

**示例**

```
1. POST "https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send"
2. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
3. push-type:0
```

说明

Authorization格式：Bearer后面拼接空格，再拼接获取的鉴权信息。

接口版本：请使用V3版本调用推送服务REST API。

场景化消息[请求体](../harmonyos-references/push-scenariozed-api-request-struct.md)中，接口URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；接口URL版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

## 示例代码

为了方便您生成服务账号鉴权令牌，我们提供了Java语言的示例代码，请按照说明替换参数运行。

如果您使用其他开发语言，请选择对应的[JWT开源组件](https://jwt.io/libraries)进行开发。

其中鉴权令牌生成步骤如下：

1. 完成上述[开发步骤](push-jwt-token.md#开发步骤)中的步骤1创建服务账号密钥文件后，从华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/api/myApi)上创建并下载推送服务API的服务账号密钥文件（.json文件），格式如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/aTV2nmU7SwmPxDni2zi_wA/zh-cn_image_0000002583439175.png?HW-CC-KV=V1&HW-CC-Date=20260427T235031Z&HW-CC-Expire=86400&HW-CC-Sign=5D1812BA161FB1EE26482885F7617E57D1A26D2FEEEAC1257FE6C8F3CABFAE9B)
2. 以上json文件复制至工程中，参考如下代码进行解析（以private.json为例，本示例基于io.jsonwebtoken:jjwt 0.11.5版本开发，该库各版本API差异较大，请根据实际依赖版本自行适配）。

Java：

```
1. /* 推荐的java版本为java8，maven依赖如下：
2. <dependency>
3. <groupId>com.fasterxml.jackson.core</groupId>
4. <artifactId>jackson-databind</artifactId>
5. <version>2.16.2</version>
6. </dependency>
7. <dependency>
8. <groupId>io.jsonwebtoken</groupId>
9. <artifactId>jjwt-api</artifactId>
10. <version>0.11.5</version>
11. </dependency>
12. <dependency>
13. <groupId>io.jsonwebtoken</groupId>
14. <artifactId>jjwt-impl</artifactId>
15. <version>0.11.5</version>
16. <scope>runtime</scope>
17. </dependency>
18. <dependency>
19. <groupId>io.jsonwebtoken</groupId>
20. <artifactId>jjwt-jackson</artifactId>
21. <version>0.11.5</version>
22. <scope>runtime</scope>
23. </dependency>
24. <dependency>
25. <groupId>org.bouncycastle</groupId>
26. <artifactId>bcprov-jdk18on</artifactId>
27. <version>1.78.1</version>
28. <scope>runtime</scope>
29. </dependency>
30. */

32. import com.fasterxml.jackson.databind.JsonNode;
33. import com.fasterxml.jackson.databind.ObjectMapper;

35. import io.jsonwebtoken.*;
36. import io.jsonwebtoken.lang.Maps;

38. import java.io.File;
39. import java.io.IOException;
40. import java.net.URL;
41. import java.nio.charset.StandardCharsets;
42. import java.security.KeyFactory;
43. import java.security.NoSuchAlgorithmException;
44. import java.security.PrivateKey;
45. import java.security.interfaces.RSAPrivateKey;
46. import java.security.spec.InvalidKeySpecException;
47. import java.security.spec.PKCS8EncodedKeySpec;
48. import java.util.Base64;
49. import java.util.Map;

51. public class JsonWebTokenFactory {

53. // 实际开发时请将公网地址存储在配置文件或数据库
54. private static final String AUD = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";

56. public static String createJwt() throws NoSuchAlgorithmException, InvalidKeySpecException, IOException, NullPointerException {
57. // 读取配置文件
58. ObjectMapper mapper = new ObjectMapper();
59. // 上述private.json文件放置于工程的src/main/resources路径下
60. URL url = JsonWebTokenFactory.class.getClassLoader().getResource("private.json");
61. if (url == null) {
62. throw new NullPointerException("File not exist");
63. }
64. JsonNode rootNode = mapper.readTree(new File(url.getPath()));

66. RSAPrivateKey privateKey = (RSAPrivateKey) generatePrivateKey(rootNode.get("private_key").asText()
67. .replace("-----BEGIN PRIVATE KEY-----", "")
68. .replace("-----END PRIVATE KEY-----", "")
69. .replaceAll("\\s", ""));
70. long iat = System.currentTimeMillis() / 1000;
71. long exp = iat + 3600;

73. Map<String, Object> header = Maps.<String, Object>of(JwsHeader.KEY_ID, rootNode.get("key_id").asText())
74. .and(JwsHeader.TYPE, JwsHeader.JWT_TYPE)
75. .and(JwsHeader.ALGORITHM, SignatureAlgorithm.PS256.getValue())
76. .build();

78. Map<String, Object> payload = Maps.<String, Object>of(Claims.ISSUER, rootNode.get("sub_account").asText())
79. .and(Claims.ISSUED_AT, iat)
80. .and(Claims.EXPIRATION, exp)
81. .and(Claims.AUDIENCE, AUD)
82. .build();

84. return Jwts.builder()
85. .setHeader(header)
86. .setPayload(new ObjectMapper().writeValueAsString(payload))
87. .signWith(privateKey, SignatureAlgorithm.PS256)
88. .compact();
89. }

91. private static PrivateKey generatePrivateKey(String base64Key) throws NoSuchAlgorithmException, InvalidKeySpecException {
92. PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(Base64.getDecoder().decode(base64Key.getBytes(StandardCharsets.UTF_8)));
93. KeyFactory keyFactory = KeyFactory.getInstance("RSA");
94. return keyFactory.generatePrivate(keySpec);
95. }

97. public static void main(String[] args) {
98. try {
99. // 获取鉴权令牌
100. String jwt = createJwt();
101. } catch (NoSuchAlgorithmException e) {
102. // 异常处理流程1
103. } catch (InvalidKeySpecException e) {
104. // 异常处理流程2
105. } catch (IOException e) {
106. // 异常处理流程3
107. } catch (NullPointerException e) {
108. // 异常处理流程4
109. }
110. }
111. }
```

Node.js：

```
1. // 依赖：npm i jsonwebtoken
2. const jwt = require('jsonwebtoken');
3. const fs = require('fs');
4. let privateJson;
5. try {
6. // readFileSync首个参数修改为private.json的实际路径
7. const data = fs.readFileSync('private.json', 'utf8');
8. privateJson = JSON.parse(data);
9. // 自定义Header
10. const header = {
11. alg: 'PS256', // 建议使用PS256算法
12. kid: privateJson?.key_id,
13. typ: 'JWT'    // 类型为JWT
14. };
15. // 创建JWT载荷
16. const payload = {
17. iss: privateJson?.sub_account,
18. aud: 'https://oauth-login.cloud.huawei.com/oauth2/v3/token', // 实际开发时请将公网地址存储在配置文件或数据库
19. iat: Math.floor(Date.now() / 1000),
20. exp: Math.floor(Date.now() / 1000) + 3600
21. };
22. const private_key = privateJson?.private_key;
23. // 将字符串中的 \\n 替换成真正的换行符 \n，再按换行符分割为数组
24. const lines = private_key.replace(/\\n/g, '\n').split('\n');
25. // 取前三行
26. const firstThreeLines = lines.slice(0, 3);
27. // 重新拼接成一个三行的字符串：
28. const PRIVATE_KEY = firstThreeLines.join('\n');
29. // 获取鉴权令牌
30. const token = jwt.sign(payload, PRIVATE_KEY, { algorithm: 'PS256', header: header });
31. } catch (error) {
32. console.error("处理文件时出错:", error);
33. }
```

Go：

```
1. // 依赖：go get github.com/golang-jwt/jwt/v5

3. package main

5. import (
6. "encoding/json"
7. "encoding/pem"
8. "errors"
9. "fmt"
10. "github.com/golang-jwt/jwt/v5"
11. "log"
12. "os"
13. "strings"
14. "time"
15. )

17. type ServiceAccountKey struct {
18. KeyID      string `json:"key_id"`
19. SubAccount string `json:"sub_account"`
20. PrivateKey string `json:"private_key"`
21. }

23. func main() {
24. // 替换为实际JSON文件路径，此处以本文件同级目录为例
25. signedToken, err := generateJWTToken("private.json")
26. if err != nil {
27. log.Fatalf("Failed to generate JWT token: %v", err)
28. }

30. // signedToken为鉴权令牌，调用推送服务REST API时放在Authorization头部来进行鉴权。
31. sendMessage(signedToken)
32. }

34. func sendMessage(token string) {
35. // 自行实现业务流程
36. }

38. func generateJWTToken(keyFile string) (string, error) {
39. saKey, err := loadServiceAccountKey(keyFile)
40. if err != nil {
41. return "", err
42. }

44. formattedPrivateKey, err := formatPrivateKey(saKey.PrivateKey)
45. if err != nil {
46. return "", err
47. }

49. privateKey, err := jwt.ParseRSAPrivateKeyFromPEM([]byte(formattedPrivateKey))
50. if err != nil {
51. return "", fmt.Errorf("failed to parse private key: %w", err)
52. }

54. token, err := buildJWTToken(saKey.KeyID, saKey.SubAccount)
55. if err != nil {
56. return "", err
57. }

59. return token.SignedString(privateKey)
60. }

62. // buildJWTToken 构造 JWT token 对象
63. func buildJWTToken(keyID, subAccount string) (*jwt.Token, error) {
64. now := time.Now().UTC()
65. iat := now.Unix()
66. exp := iat + 3600 // token 过期时间：一小时后

68. claims := jwt.MapClaims{
69. // 实际开发时请将公网地址存储在配置文件或数据库
70. "aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
71. "iss": subAccount,
72. "exp": exp,
73. "iat": iat,
74. }

76. token := jwt.NewWithClaims(jwt.SigningMethodPS256, claims)

78. // 设置 header
79. token.Header["kid"] = keyID
80. token.Header["typ"] = "JWT"
81. token.Header["alg"] = "PS256"

83. return token, nil
84. }

86. // loadServiceAccountKey 从 JSON 文件加载服务账号密钥
87. func loadServiceAccountKey(filename string) (*ServiceAccountKey, error) {
88. data, err := os.ReadFile(filename)
89. if err != nil {
90. return nil, fmt.Errorf("failed to read key file: %w", err)
91. }

93. var saKey ServiceAccountKey
94. if err := json.Unmarshal(data, &saKey); err != nil {
95. return nil, fmt.Errorf("failed to parse key file: %w", err)
96. }

98. if saKey.KeyID == "" || saKey.SubAccount == "" || saKey.PrivateKey == "" {
99. return nil, errors.New("invalid service account key file: missing required fields")
100. }

102. return &saKey, nil
103. }

105. // formatPrivateKey 格式化私钥字符串为 PEM 格式
106. func formatPrivateKey(privateKeyStr string) (string, error) {
107. trimmed := strings.TrimSpace(privateKeyStr)

109. // 如果已经是 PEM 格式，则直接返回
110. if strings.HasPrefix(trimmed, "-----BEGIN PRIVATE KEY-----") &&
111. strings.HasSuffix(trimmed, "-----END PRIVATE KEY-----") {
112. return trimmed, nil
113. }

115. block, _ := pem.Decode([]byte(trimmed))
116. if block == nil {
117. return "", errors.New("failed to decode PEM block")
118. }

120. pemBytes := pem.EncodeToMemory(block)
121. if pemBytes == nil {
122. return "", errors.New("failed to encode private key to PEM format")
123. }

125. return string(pemBytes), nil
126. }
```

Python：

```
1. # 依赖：pip install PyJWT cryptography

3. import jwt
4. import json
5. import time
6. from cryptography.hazmat.primitives import serialization

8. def load_private_key_from_json(json_file_path):
9. """
10. 从JSON文件中加载私钥信息
11. :param json_file_path: JSON文件路径
12. :return: (key_id, sub_account, private_key_pem)
13. """
14. with open(json_file_path, 'r') as f:
15. data = json.load(f)

17. # 获取KID和ISS
18. key_id = data.get('key_id')
19. sub_account = data.get('sub_account')

21. # 将私钥转换为PEM格式
22. private_key_str = data.get('private_key')
23. private_key_pem = serialization.load_pem_private_key(
24. private_key_str.encode(),
25. password=None
26. )

28. return key_id, sub_account, private_key_pem

30. def generate_jwt_token(json_file_path):
31. # 从JSON文件加载信息
32. kid, iss, private_key = load_private_key_from_json(json_file_path)

34. # 当前时间和过期时间（示例中使用固定值，实际应根据需求计算）
35. iat = int(time.time())
36. exp = iat + 3600

38. # 构造Header
39. header = {
40. "kid": kid,
41. "typ": "JWT",
42. "alg": "PS256"
43. }

45. # 构造Payload
46. payload = {
47. # 实际开发时请将公网地址存储在配置文件或数据库
48. "aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
49. "iss": iss,
50. "exp": exp,
51. "iat": iat
52. }

54. # 生成JWT Token
55. token = jwt.encode(
56. payload=payload,
57. key=private_key,
58. algorithm='PS256',
59. headers=header
60. )

62. return token

64. def send_message(jwt_token):
65. # 自行实现业务流程
66. pass

68. if __name__ == "__main__":
69. json_file = "private.json"  # 替换为实际JSON文件路径，此处以本文件同级目录为例

71. try:
72. # jwt_token 为鉴权令牌，调用推送服务REST API时放在Authorization头部来进行鉴权。
73. jwt_token = generate_jwt_token(json_file)
74. send_message(jwt_token)
75. except Exception as e:
76. print(f"Error generating JWT token: {str(e)}")
```

PHP：

```
1. <?php
2. // 依赖：composer require lcobucci/jwt:^5.4.2
3. // 依赖：composer require lcobucci/jwt-rsassa-pss
4. // php: ~8.2.0 || ~8.3.0 || ~8.4.0
5. require 'vendor/autoload.php';

7. use Lcobucci\JWT\Configuration;
8. use Lcobucci\JWT\Signer\RsaPss\Sha256;
9. use Lcobucci\JWT\Signer\Key\InMemory;

11. class ServiceAccount
12. {
13. public string $keyId;
14. public string $subAccount;
15. public string $privateKey;
16. public string $tokenURI;

18. public function __construct(string $keyId, string $subAccount, string $privateKey, string $tokenURI)
19. {
20. $this->keyId = $keyId;
21. $this->subAccount = $subAccount;
22. $this->privateKey = $privateKey;
23. $this->tokenURI = $tokenURI;
24. }
25. }

27. function loadServiceAccount(string $filePath): ServiceAccount
28. {
29. if (!file_exists($filePath)) {
30. throw new RuntimeException("配置文件不存在: $filePath");
31. }

33. $json = file_get_contents($filePath);
34. $config = json_decode($json, true);
35. if (json_last_error() !== JSON_ERROR_NONE) {
36. throw new RuntimeException("JSON解析错误: " . json_last_error_msg());
37. }

39. // 验证必要字段
40. $requiredKeys = ['key_id', 'sub_account', 'private_key', 'token_uri'];
41. foreach ($requiredKeys as $key) {
42. if (!isset($config[$key])) {
43. throw new RuntimeException("配置缺少必要字段: $key");
44. }
45. }

47. // 处理私钥中的换行符
48. $privateKey = str_replace('\n', "\n", $config['private_key']);

50. return new ServiceAccount(
51. $config['key_id'],
52. $config['sub_account'],
53. $privateKey,
54. $config['token_uri']
55. );
56. }

58. function sendMessage()
59. {
60. // 自行实现业务流程
61. }

63. function generateJWTToken(ServiceAccount $serviceAccount)
64. {
65. $now = new DateTimeImmutable();
66. $expire = $now->modify("+3600 seconds");

68. $configuration = Configuration::forSymmetricSigner(
69. new Sha256(),
70. InMemory::plainText($serviceAccount->privateKey)
71. );

73. return $configuration->builder()
74. ->withHeader('alg', 'PS256') // 指定PS256算法
75. ->withHeader('typ', 'JWT')   // JWT类型
76. ->withHeader('kid', $serviceAccount->keyId) // 密钥ID
77. ->issuedBy($serviceAccount->subAccount) // iss
78. ->permittedFor($serviceAccount->tokenURI) // aud
79. ->issuedAt($now) // iat
80. ->expiresAt($expire) // exp
81. ->getToken($configuration->signer(), $configuration->signingKey())
82. ->toString();
83. }

85. function main()
86. {
87. try {
88. // 替换为JSON文件实际路径，此处以与本文件同级目录为例
89. $filePath = 'private.json';
90. $serviceAccount = loadServiceAccount($filePath);
91. $signedToken = generateJWTToken($serviceAccount);

93. // signedToken为鉴权令牌，调用推送服务REST API时放在Authorization头部来进行鉴权。
94. sendMessage($signedToken);
95. } catch (Exception $e) {
96. error_log("Error: " . $e->getMessage());
97. exit(1);
98. }
99. }

101. main();
102. ?>
```
