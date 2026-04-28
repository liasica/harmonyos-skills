---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-rest-overview
title: 公共说明
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 公共说明
category: harmonyos-references
scraped_at: 2026-04-28T08:17:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5498779594c6ce490297f7431a352cb6eeabe1d983b7a9a8e48ef87420ecf76d
---

## HTTPS安全要求

* 所有的API请求必须使用HTTPS。
* 支持的TLS协议版本：1.2 / 1.3。
* 支持的加密套件列表：

  ```
  1. TLS_CHACHA20_POLY1305_SHA256
  2. TLS_AES_128_GCM_SHA256
  3. TLS_AES_256_GCM_SHA384
  4. TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  5. TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  ```

## HTTP方法说明

当前Payment Kit对外接口涉及GET及POST两种HTTP METHOD。

* **GET**：对应于查询场景。适用于从服务器查询资源数据，如查询订单信息、查询签约信息等。
* **POST**：对应于新建/更新资源场景，如预下单、退款请求等。

## 数据格式

请求和响应报文统一使用JSON格式。

## 字符编码

Payment Kit所有请求默认支持UTF-8编码，如采用其他编码格式的报文可能导致验签失败、字段解析失败等问题。

HTTP METHOD方式为GET的接口请求，请求URL如涉及参数拼接，拼接后完整的请求URL不建议带特殊字符。如有需要，建议对URL中的特殊字符进行编码处理。URL特殊字符参考但不限于：+, 空格, ?, %, #, &, =

## 认证授权

* **认证(Authentication)**：认证操作确认调用者身份，防抵赖和数据篡改。所有对商户开放接口均需要商户在请求头中传递[PayMercAuth](payment-model.md#paymercauth)字段，在开放网关认证通过后方可进行后续流程。
* **授权(Authorization)**：授权确保给定接口仅特定调用者才有权限调用。部分接口仅特定商户申请开通后方可使用。

## 签名规则

**签名场景：** 商户云侧请求的请求头中参数签名。

**签名算法：** SHA256WithRSA/PSS 或者 SM2。

**开发步骤：**

1. 筛选：排除请求JSON字符串中sign字段，只保留sign以外的其他字段。
2. 排序拼接：按key值的ASCII码顺序排序，并使用&拼接，列表场景使用符号“=”连接。

   具体可参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md#集成maven依赖)中SignStringUtil.java类的signString方法，排序拼接结果示例如下：

   ```
   1. "allocationType=DELAY_ORDER_ALLOCATION&callbackUrl=https://www.xxxxxx.com/hw/pay/callback&currency=CNY&mercNo=xxxxxx&mercOrderNo=xxxxxx&totalAmount=2&tradeSummary=杂志报刊"
   ```
3. 签名：调用给定算法对排序后的串完成签名。

   **SHA256WithRSA/PSS：** 具体可参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md#集成maven依赖)中RSAUtils.java类的signByRSAWithPSS方法。

   **SM2：** 具体可参考[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md#集成maven依赖)中Sm2Utils.java类中的sign方法。

   加签内容参考：

   ```
   1. POST请求：POST https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/preorder/create/app
   2. {
   3. "appId": "5765880207854262xxx",
   4. "callbackUrl": "https://www.xxx.com/hw_notify",
   5. "currency": "CNY",
   6. "mercNo": "101723200xxx",
   7. "mercOrderNo": "2405171027547xxx",
   8. "payload": "shop|h8ahnJA8xxRXVw",
   9. "totalAmount": 5,
   10. "tradeSummary": "test",
   11. "subOrders": [
   12. {
   13. "mercNo": "101723200xxx",
   14. "mercOrderNo": "abcxxx1"
   15. },
   16. {
   17. "mercNo": "101723201xxx",
   18. "mercOrderNo": "abcxxx2"
   19. }
   20. ]
   21. }
   22. 加签内容：appId=5765880207854262xxx&callbackUrl=https://www.xxx.com/hw_notify&currency=CNY&mercNo=101723200xxx&mercOrderNo=2405171027547xxx&payload=shop|h8ahnJA8xxRXVw&subOrders=mercNo=101723200xxx&mercOrderNo=abcxxx1,mercNo=101723201xxx&mercOrderNo=abcxxx2&totalAmount=5&tradeSummary=test

   24. GET请求：GET https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/transactions/merc-orders/20240507000000041809599950090xxx?mercNo=101540000089&sdkVersion=1.0.0
   25. 加签内容：/api/v2/aggr/transactions/merc-orders/20240507000000041809599950090xxx?mercNo=101540000089&sdkVersion=1.0.0
   ```

注意

字段值设置为null时，字段可不参与签名，设置为空字符时，则必须参与签名。

### 常用语言SHA256WithRSA/PSS加签示例代码参考

**go语言**

加签实现示例代码：

```
1. // 排序拼接示例
2. import (
3. "encoding/base64"
4. "encoding/hex"
5. "encoding/json"
6. "fmt"
7. "sort"
8. "strings"
9. )

11. // GenerateSignData 生成待签名字符串
12. // 步骤一：筛选，排除sign字段
13. // 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
14. func (s *SignatureUtils) GenerateSignData(params map[string]interface{}) string {
15. return s.buildSignData(params)
16. }
17. // buildSignData 递归构建签名字符串
18. func (s *SignatureUtils) buildSignData(params interface{}) string {
19. switch v := params.(type) {
20. case map[string]interface{}:
21. return s.buildMapSignData(v)
22. case []interface{}:
23. return s.buildArraySignData(v)
24. default:
25. return fmt.Sprintf("%v", v)
26. }
27. }
28. // buildMapSignData 处理Map类型数据
29. func (s *SignatureUtils) buildMapSignData(params map[string]interface{}) string {
30. // 排序key
31. var keys []string
32. for k := range params {
33. // 排除sign字段
34. if k == "sign" {
35. continue
36. }
37. keys = append(keys, k)
38. }
39. sort.Strings(keys)
40. var parts []string
41. for _, key := range keys {
42. value := params[key]
43. // null值不参与签名
44. if value == nil {
45. continue
46. }
47. // 空字符串参与签名
48. strValue := s.buildSignData(value)
49. parts = append(parts, fmt.Sprintf("%s=%s", key, strValue))
50. }
51. return strings.Join(parts, "&")
52. }
53. // buildArraySignData 处理数组类型数据
54. func (s *SignatureUtils) buildArraySignData(arr []interface{}) string {
55. var parts []string
56. for _, item := range arr {
57. if item == nil {
58. continue
59. }
60. parts = append(parts, s.buildSignData(item))
61. }
62. return strings.Join(parts, ",")
63. }

65. // 加签示例
66. package main
67. import (
68. "crypto"
69. "crypto/rand"
70. "crypto/rsa"
71. "crypto/sha256"
72. "crypto/x509"
73. "encoding/base64"
74. "fmt"
75. "testing"
76. )
77. func signSha256WithRsaPSS(message, privateKeyStr string) (string, error) {
78. privateKey, err := getPrivateKey(privateKeyStr)
79. if err != nil {
80. return "", err
81. }
82. hasher := sha256.New()
83. hasher.Write([]byte(message))
84. hashedMessage := hasher.Sum(nil)
85. opts := rsa.PSSOptions{
86. SaltLength: rsa.PSSSaltLengthEqualsHash,
87. Hash:       crypto.SHA256,
88. }
89. signature, err := rsa.SignPSS(rand.Reader, privateKey, crypto.SHA256, hashedMessage, &opts)
90. if err != nil {
91. return "", err
92. }
93. return base64.StdEncoding.EncodeToString(signature), nil
94. }

96. func getPrivateKey(privateKeyStr string) (*rsa.PrivateKey, error) {
97. decoded, err := base64.StdEncoding.DecodeString(privateKeyStr)
98. if err != nil {
99. return nil, err
100. }
101. privateKey, err := x509.ParsePKCS8PrivateKey(decoded)
102. if err != nil {
103. return nil, err
104. }
105. rsaPrivateKey, ok := privateKey.(*rsa.PrivateKey)
106. if !ok {
107. return nil, err
108. }
109. return rsaPrivateKey, nil
110. }

112. func TestRsaSign(t *testing.T) {
113. signature, err := signSha256WithRsaPSS("加签排序拼接内容","私钥")
114. fmt.Println(signature, err)
115. }
```

**JavaScript语言**

javascript可通过jsrsasign模块实现，如已安装node环境，可执行如下命令安装jsrsasign模块。

```
1. npm install jsrsasign
```

加签实现示例代码：

```
1. // 排序拼接示例
2. /**
3. * 递归构建签名字符串
4. * @param {*} data 数据
5. * @returns {string} 签名字符串
6. */
7. buildSignData(data) {
8. if (data === null || data === undefined) {
9. return '';
10. }
11. if (typeof data === 'object' && !Array.isArray(data)) {
12. return this.buildMapSignData(data);
13. }
14. if (Array.isArray(data)) {
15. return this.buildArraySignData(data);
16. }
17. return String(data);
18. }
19. /**
20. * 处理Map类型数据
21. * @param {Object} params 参数对象
22. * @returns {string} 签名字符串
23. */
24. buildMapSignData(params) {
25. // 排序key
26. const keys = Object.keys(params)
27. .filter(key => key !== 'sign') // 排除sign字段
28. .sort();
29. const parts = [];
30. for (const key of keys) {
31. const value = params[key];
32. // null值不参与签名
33. if (value === null || value === undefined) {
34. continue;
35. }
36. // 空字符串参与签名
37. const strValue = this.buildSignData(value);
38. parts.push(`${key}=${strValue}`);
39. }
40. return parts.join('&');
41. }
42. /**
43. * 处理数组类型数据
44. * @param {Array} arr 数组
45. * @returns {string} 签名字符串
46. */
47. buildArraySignData(arr) {
48. const parts = [];
49. for (const item of arr) {
50. if (item === null || item === undefined) {
51. continue;
52. }
53. parts.push(this.buildSignData(item));
54. }
55. return parts.join(',');
56. }

58. // 加签示例
59. const jsrsasign = require('jsrsasign');
60. function signSha256WithRsaPSS(plainData, privateStr) {
61. let rsa = new jsrsasign.RSAKey();
62. // PEM 格式的私钥
63. const priKey = `-----BEGIN PRIVATE KEY-----\n${privateStr}\n-----END PRIVATE KEY-----\n`;
64. rsa = jsrsasign.KEYUTIL.getKey(priKey);
65. const sig = new jsrsasign.KJUR.crypto.Signature({
66. alg: 'SHA256withRSAandMGF1',
67. });
68. sig.init(rsa);
69. sig.updateString(plainData);
70. return jsrsasign.hextob64(sig.sign());
71. }
72. let signature = signSha256WithRsaPSS("加签排序拼接内容","私钥");
73. console.info(signature)
```

**python语言**

python可通过cryptography模块实现，可先执行如下命令安装cryptography模块：

```
1. pip install cryptography
```

加签实现示例代码：

```
1. // 排序拼接示例
2. def generate_sign_data(self, params):
3. """
4. 生成待签名字符串
5. 步骤一：筛选，排除sign字段
6. 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
7. Args:
8. params: 参数字典
9. Returns:
10. str: 待签名字符串
11. """
12. return self._build_sign_data(params)
13. def _build_sign_data(self, data):
14. """
15. 递归构建签名字符串
16. Args:
17. data: 数据
18. Returns:
19. str: 签名字符串
20. """
21. if data is None:
22. return ''
23. if isinstance(data, dict):
24. return self._build_map_sign_data(data)
25. if isinstance(data, (list, tuple)):
26. return self._build_array_sign_data(data)
27. return str(data)
28. def _build_map_sign_data(self, params):
29. """
30. 处理字典类型数据
31. Args:
32. params: 参数字典
33. Returns:
34. str: 签名字符串
35. """
36. # 排序key，排除sign字段
37. keys = sorted([k for k in params.keys() if k != 'sign'])
38. parts = []
39. for key in keys:
40. value = params[key]
41. # None值不参与签名
42. if value is None:
43. continue
44. # 空字符串参与签名
45. str_value = self._build_sign_data(value)
46. parts.append(f"{key}={str_value}")
47. return '&'.join(parts)
48. def _build_array_sign_data(self, arr):
49. """
50. 处理数组类型数据
51. Args:
52. arr: 数组
53. Returns:
54. str: 签名字符串
55. """
56. parts = []
57. for item in arr:
58. if item is None:
59. continue
60. parts.append(self._build_sign_data(item))
61. return ','.join(parts)

63. // 加签示例
64. import base64

66. from cryptography.hazmat.primitives import hashes
67. from cryptography.hazmat.primitives.asymmetric import padding
68. from cryptography.hazmat.backends import default_backend
69. from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

71. def signSha256WithRsaPSS(private_key_str, message):
72. # PEM 格式的私钥
73. prikey_content = "-----BEGIN PRIVATE KEY-----\n" + private_key_str +"\n-----END PRIVATE KEY-----\n";
74. private_key = load_pem_private_key(data=prikey_content.encode("utf-8"), password=None, backend=default_backend())

76. # 使用 RSA-PSS 算法生成签名
77. signature = private_key.sign(
78. message.encode("utf-8"),
79. padding.PSS(
80. mgf=padding.MGF1(hashes.SHA256()),
81. salt_length=padding.PSS.DIGEST_LENGTH
82. ),
83. hashes.SHA256()
84. )
85. return base64.b64encode(signature).decode('utf-8')

87. message = "加签排序拼接内容"
88. private_key_str = "私钥"
89. signature = signSha256WithRsaPSS(private_key_str, message)
90. print(signature)
```

**php语言**

php可通过phpseclib加密库实现，如已安装composer环境，可先通过以下命令导入phpseclib：

```
1. composer require phpseclib/phpseclib
```

phpseclib2加签实现示例代码：

```
1. // 排序拼接示例
2. class SignatureUtils
3. {
4. /**
5. * 生成待签名字符串
6. * 步骤一：筛选，排除sign字段
7. * 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
8. *
9. * @param array $params 参数数组
10. * @return string 待签名字符串
11. */
12. public function generateSignData($params)
13. {
14. return $this->buildSignData($params);
15. }
16. /**
17. * 递归构建签名字符串
18. *
19. * @param mixed $data 数据
20. * @return string 签名字符串
21. */
22. private function buildSignData($data)
23. {
24. if ($data === null) {
25. return '';
26. }
27. if (is_array($data)) {
28. // 判断是否为关联数组（Map）
29. if ($this->isAssocArray($data)) {
30. return $this->buildMapSignData($data);
31. } else {
32. return $this->buildArraySignData($data);
33. }
34. }
35. return (string)$data;
36. }
37. /**
38. * 判断是否为关联数组
39. *
40. * @param array $arr 数组
41. * @return bool
42. */
43. private function isAssocArray($arr)
44. {
45. if (empty($arr)) {
46. return false;
47. }
48. return array_keys($arr) !== range(0, count($arr) - 1);
49. }
50. /**
51. * 处理Map类型数据
52. *
53. * @param array $params 参数数组
54. * @return string 签名字符串
55. */
56. private function buildMapSignData($params)
57. {
58. // 排序key，排除sign字段
59. $keys = array_keys($params);
60. $keys = array_filter($keys, function($key) {
61. return $key !== 'sign';
62. });
63. sort($keys);
64. $parts = [];
65. foreach ($keys as $key) {
66. $value = $params[$key];
67. // null值不参与签名
68. if ($value === null) {
69. continue;
70. }
71. // 空字符串参与签名
72. $strValue = $this->buildSignData($value);
73. $parts[] = $key . '=' . $strValue;
74. }
75. return implode('&', $parts);
76. }
77. /**
78. * 处理数组类型数据
79. *
80. * @param array $arr 数组
81. * @return string 签名字符串
82. */
83. private function buildArraySignData($arr)
84. {
85. $parts = [];
86. foreach ($arr as $item) {
87. if ($item === null) {
88. continue;
89. }
90. $parts[] = $this->buildSignData($item);
91. }
92. return implode(',', $parts);
93. }
94. /**
95. * Base64转Hex
96. *
97. * @param string $base64String Base64字符串
98. * @return string Hex字符串
99. */
100. private function base64ToHex($base64String)
101. {
102. $bytes = base64_decode($base64String);
103. return bin2hex($bytes);
104. }
105. /**
106. * 解析JSON字符串为数组
107. *
108. * @param string $jsonStr JSON字符串
109. * @return array 数组
110. */
111. public function parseJSON($jsonStr)
112. {
113. return json_decode($jsonStr, true);
114. }
115. /**
116. * 从JSON字符串生成待签名字符串
117. *
118. * @param string $jsonStr JSON字符串
119. * @return string 待签名字符串
120. */
121. public function generateSignDataFromJSON($jsonStr)
122. {
123. $params = $this->parseJSON($jsonStr);
124. return $this->generateSignData($params);
125. }
126. public function testExcludeSignField()
127. {
128. $params = [
129. 'appId' => '5765880207854262xxx',
130. 'callbackUrl' => 'https://www.xxx.com/hw_notify',
131. 'sign' => 'xxxxx', // sign字段应被排除
132. 'currency' => 'CNY'
133. ];
134. $signData = $this-> generateSignData($params);
135. echo "[testExcludeSignField] Sign data without sign field: " . $signData . "\n";
136. }
137. }

139. // 加签示例
140. <?php
141. require_once 'vendor/autoload.php';
142. use phpseclib\Crypt\RSA;

144. function signSha256WithRsaPSS($content, $privateKeyStr) {
145. try {
146. $privateKey = "-----BEGIN PRIVATE KEY-----\n" . $privateKeyStr ."\n-----END PRIVATE KEY-----";
147. $signer = new \phpseclib\Crypt\RSA();
148. $signer->loadKey($privateKey, $password = false);
149. $signer->setHash('sha256');
150. $signer->setSignatureMode(RSA::SIGNATURE_PSS);
151. $signer->setMGFHash('sha256');
152. $signature = $signer->sign($content);

154. $sign = base64_encode($signature);
155. return $sign;
156. } catch (Exception $e) {
157. echo $e->getMessage();
158. }
159. return null;
160. }
161. $data = "加签排序拼接内容";
162. $privateKeyStr = "私钥";
163. echo signSha256WithRsaPSS($data, $privateKeyStr)
164. ?>
```

phpseclib3加签实现示例代码：

```
1. <?php
2. require_once 'vendor/autoload.php';

4. use phpseclib3\Crypt\PublicKeyLoader;
5. use phpseclib3\Crypt\RSA;

7. function signSha256WithRsaPSS($data,$rsa_key){
8. $key = "-----BEGIN PRIVATE KEY-----\n" . $rsa_key . "-----END PRIVATE KEY-----";
9. $private = PublicKeyLoader::load($key, $password = false);
10. $private = $private->withPadding(RSA::SIGNATURE_PSS);
11. return base64_encode($private->sign($data));
12. }

14. $data = "加签排序拼接内容";
15. $privateKeyStr = "私钥";
16. echo signSha256WithRsaPSS($data, $privateKeyStr);
17. ?>
```

**C#语言**

C#可通过BouncyCastle库来实现，如已安装 [.NET SDK](https://dotnet.microsoft.com/download)，可先执行如下命令添加BouncyCastle：

```
1. dotnet add package BouncyCastle
```

加签实现示例代码：

```
1. // 排序拼接示例
2. using System;
3. using System.Collections.Generic;
4. using System.Security.Cryptography;
5. using System.Text;
6. using System.Text.Json;
7. using System.Linq;
8. namespace PaySignature
9. {
10. /// <summary>
11. /// 签名工具类
12. /// </summary>
13. public class SignatureUtils
14. {
15. /// <summary>
16. /// 生成待签名字符串
17. /// 步骤一：筛选，排除sign字段
18. /// 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
19. /// </summary>
20. /// <param name="params">参数字典</param>
21. /// <returns>待签名字符串</returns>
22. public string GenerateSignData(Dictionary<string, object> parameters)
23. {
24. return BuildSignData(parameters);
25. }
26. /// <summary>
27. /// 递归构建签名字符串
28. /// </summary>
29. /// <param name="data">数据</param>
30. /// <returns>签名字符串</returns>
31. private string BuildSignData(object data)
32. {
33. if (data == null)
34. {
35. return string.Empty;
36. }
37. if (data is Dictionary<string, object> dict)
38. {
39. return BuildMapSignData(dict);
40. }
41. if (data is List<object> list)
42. {
43. return BuildArraySignData(list);
44. }
45. return data.ToString();
46. }
47. /// <summary>
48. /// 处理字典类型数据
49. /// </summary>
50. /// <param name="parameters">参数字典</param>
51. /// <returns>签名字符串</returns>
52. private string BuildMapSignData(Dictionary<string, object> parameters)
53. {
54. // 排序key，排除sign字段
55. var keys = parameters.Keys
56. .Where(k => k != "sign")
57. .OrderBy(k => k, StringComparer.Ordinal)
58. .ToList();
59. var parts = new List<string>();
60. foreach (var key in keys)
61. {
62. var value = parameters[key];
63. // null值不参与签名
64. if (value == null)
65. {
66. continue;
67. }
68. // 空字符串参与签名
69. var strValue = BuildSignData(value);
70. parts.Add($"{key}={strValue}");
71. }
72. return string.Join("&", parts);
73. }
74. /// <summary>
75. /// 处理数组类型数据
76. /// </summary>
77. /// <param name="arr">数组</param>
78. /// <returns>签名字符串</returns>
79. private string BuildArraySignData(List<object> arr)
80. {
81. var parts = new List<string>();
82. foreach (var item in arr)
83. {
84. if (item == null)
85. {
86. continue;
87. }
88. parts.Add(BuildSignData(item));
89. }
90. return string.Join(",", parts);
91. }
92. /// <summary>
93. /// Base64转Hex
94. /// </summary>
95. /// <param name="base64String">Base64字符串</param>
96. /// <returns>Hex字符串</returns>
97. private string Base64ToHex(string base64String)
98. {
99. var bytes = Convert.FromBase64String(base64String);
100. return BitConverter.ToString(bytes).Replace("-", "").ToLower();
101. }
102. /// <summary>
103. /// 解析JSON字符串为字典
104. /// </summary>
105. /// <param name="jsonStr">JSON字符串</param>
106. /// <returns>字典</returns>
107. public Dictionary<string, object> ParseJSON(string jsonStr)
108. {
109. using var document = JsonDocument.Parse(jsonStr);
110. var result = new Dictionary<string, object>();
111. foreach (var element in document.RootElement.EnumerateObject())
112. {
113. result[element.Name] = ParseJsonElement(element.Value);
114. }
115. return result;
116. }
117. /// <summary>
118. /// 解析JSON元素
119. /// </summary>
120. /// <param name="element">JSON元素</param>
121. /// <returns>对象</returns>
122. private object ParseJsonElement(JsonElement element)
123. {
124. switch (element.ValueKind)
125. {
126. case JsonValueKind.String:
127. return element.GetString();
128. case JsonValueKind.Number:
129. if (element.TryGetInt32(out int intValue))
130. return intValue;
131. if (element.TryGetInt64(out long longValue))
132. return longValue;
133. return element.GetDouble();
134. case JsonValueKind.True:
135. return true;
136. case JsonValueKind.False:
137. return false;
138. case JsonValueKind.Null:
139. return null;
140. case JsonValueKind.Object:
141. var dict = new Dictionary<string, object>();
142. foreach (var prop in element.EnumerateObject())
143. {
144. dict[prop.Name] = ParseJsonElement(prop.Value);
145. }
146. return dict;
147. case JsonValueKind.Array:
148. var list = new List<object>();
149. foreach (var item in element.EnumerateArray())
150. {
151. list.Add(ParseJsonElement(item));
152. }
153. return list;
154. default:
155. return element.ToString();
156. }
157. }
158. /// <summary>
159. /// 从JSON字符串生成待签名字符串
160. /// </summary>
161. /// <param name="jsonStr">JSON字符串</param>
162. /// <returns>待签名字符串</returns>
163. public string GenerateSignDataFromJSON(string jsonStr)
164. {
165. var parameters = ParseJSON(jsonStr);
166. return GenerateSignData(parameters);
167. }
168. }
169. }
170. // 测试
171. using Xunit;
172. using PaySignature;
173. namespace PaySignatureTest
174. {
175. public class SignatureUtilsTest2
176. {
177. private readonly SignatureUtils _utils;
178. public SignatureUtilsTest2()
179. {
180. _utils = new SignatureUtils();
181. }
182. /// <summary>
183. /// 测试构造签名串
184. /// </summary>
185. [Fact]
186. public void TestComplexNestedStructure()
187. {
188. var goods = new List<object>
189. {
190. new Dictionary<string, object>
191. {
192. { "goodsId", "G001" },
193. { "goodsName", "商品1" },
194. { "quantity", 2 }
195. },
196. new Dictionary<string, object>
197. {
198. { "goodsId", "G002" },
199. { "goodsName", "商品2" },
200. { "quantity", 3 }
201. }
202. };
203. var parameters = new Dictionary<string, object>
204. {
205. { "appId", "5765880207854262xxx" },
206. { "goods", goods },
207. { "totalAmount", 100 }
208. };
209. var signData = _utils.GenerateSignData(parameters);
210. Assert.Contains("appId=5765880207854262xxx", signData);
211. Assert.Contains("goods=", signData);
212. Console.WriteLine($"Sign data with complex structure: {signData}");
213. }
214. }
215. }

217. // 加签示例
218. using System.Text;
219. using Org.BouncyCastle.OpenSsl;
220. using Org.BouncyCastle.Crypto;
221. using Org.BouncyCastle.Crypto.Parameters;
222. using Org.BouncyCastle.Security;
223. using Org.BouncyCastle.Crypto.Signers;
224. using Org.BouncyCastle.Crypto.Engines;
225. using Org.BouncyCastle.Crypto.Digests;
226. class SignProgram
227. {
228. public static void Main(string[] args)
229. {
230. string res = RSASign("加签排序拼接内容","私钥");
231. Console.WriteLine("result: " + res);
232. }
233. public static string RSASign(string datastr,string privateStr)
234. {
235. var priKey = "-----BEGIN PRIVATE KEY-----\n"+ privateStr +"\n-----END PRIVATE KEY-----\n";
236. byte[] data = Encoding.UTF8.GetBytes(datastr);
237. // 创建PSS签名器
238. var signer = new PssSigner(new RsaEngine(), new Sha256Digest());
239. AsymmetricKeyParameter rsaPrivateKey = null;
240. using (var stringReader = new StringReader(priKey))
241. {
242. var pemReader = new PemReader(stringReader);
243. rsaPrivateKey = pemReader.ReadObject() as AsymmetricKeyParameter;
244. }
245. signer.Init(true, new ParametersWithRandom(rsaPrivateKey, new SecureRandom()));
246. signer.BlockUpdate(data, 0, data.Length);
247. byte[] signature = signer.GenerateSignature();
248. return Convert.ToBase64String(signature);
249. }
250. }
```

## 验签规则

**验签场景：** 商户需要对来自Payment Kit服务器的信息做验签，验证签名信息身份来自Payment Kit服务器。商户服务器对华为支付服务器返回的回调通知请求参数和退款通知请求参数验签。

**验签算法：** SM2。

**开发步骤：** 确认验证签名的公钥证书、确认参与签名字段将待签名字段转换为“key=value”并以符号“&”拼接、使用验签方法验证签名。

1. 获取华为支付公钥，此处公钥证书为[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)获取的证书，可参见[下载华为支付证书](../harmonyos-guides/payment-certificates-config.md#下载华为支付证书)。
2. 获取参与签名的字段，转换为map并将map的“key-value”排序后以符号“&”拼接。
3. 使用SM2算法进行验签，具体参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md)中VerifyTools.java类的verifySign方法。

注意

因业务发展需要，接口字段可能发生变动，建议验签功能实现可扩展——即“先对回调通知的请求体进行验签处理，再转换成业务对象处理”，以确保在字段有变化时也可以正常验签。

### 常用语言SM2验签示例代码参考

**JavaScript语言**

javascript可通过sm-crypto模块实现，如已安装node环境，可执行如下命令安装：

```
1. npm install sm-crypto
```

验签实现示例代码：

```
1. const SmCrypto = require('sm-crypto');
2. function signSM2Verify(plainData, sign, publicStr) {
3. let signHex1 = base64ToHex(sign)
4. console.info("plainData: " + plainData)
5. console.info("sign: " + sign)
6. console.info("sign hex: " + signHex1)
7. return SmCrypto.sm2.doVerifySignature(plainData, signHex1, publicStr, {
8. hash: true,
9. der: true
10. })
11. }
12. function base64ToHex(base64String) {
13. const buffer = Buffer.from(base64String, 'base64');
14. return buffer.toString('hex');
15. }
16. let signSM2VerifyRes = signSM2Verify(
17. "验签排序拼接内容",
18. "验签sign",
19. "验签公钥"
20. );
21. console.info(signSM2VerifyRes)
```

**go语言**

验签实现示例代码：

```
1. // TestSM2Verify 测试：SM2验签（需要安装go get -u github.com/tjfoc/gmsm）
2. func ReadSM2PublicKeyFromHex(publicKeyStr string) (*sm2.PublicKey, error) {
3. // 解码十六进制字符串
4. pubKeyBytes, err := hex.DecodeString(publicKeyStr)
5. if err != nil {
6. return nil, fmt.Errorf("failed to decode hex: %v", err)
7. }
8. // 检查是否为非压缩格式 (0x04 开头)
9. if len(pubKeyBytes) != 65 || pubKeyBytes[0] != 0x04 {
10. return nil, fmt.Errorf("invalid SM2 public key format (expected 65 bytes, starting with 0x04)")
11. }
12. // 解析 X 和 Y 坐标（SM2 公钥长度为 65 字节：0x04 + 32字节X + 32字节Y）
13. x := pubKeyBytes[1:33]  // X 坐标（32字节）
14. y := pubKeyBytes[33:65] // Y 坐标（32字节）
15. // 构造 SM2 公钥
16. publicKey := &sm2.PublicKey{
17. Curve: sm2.P256Sm2(), // SM2 曲线
18. X:     new(big.Int).SetBytes(x),
19. Y:     new(big.Int).SetBytes(y),
20. }
21. return publicKey, nil
22. }
23. func (s *SignatureUtils) VerifySM2(content, publicKeyStr, signData string) (bool, error) {
24. // 将Base64签名转换为Hex格式
25. signBytes, err := base64.StdEncoding.DecodeString(signData)
26. if err != nil {
27. return false, fmt.Errorf("decode sign data failed: %v", err)
28. }
29. signHex := hex.EncodeToString(signBytes)
30. // 解析公钥
31. publicKey, err := ReadSM2PublicKeyFromHex(publicKeyStr)
32. if err != nil {
33. return false, fmt.Errorf("parse public key failed: %v", err)
34. }
35. // 将Hex签名转换为字节数组
36. signature, err := hex.DecodeString(signHex)
37. if err != nil {
38. return false, fmt.Errorf("decode signature hex failed: %v", err)
39. }
40. // SM2验签
41. isVerified := publicKey.Verify([]byte(content), signature)
42. if !isVerified {
43. return false, fmt.Errorf("SM2 verification requires external library, please install: go get github.com/tjfoc/gmsm")
44. }
45. return true, nil
46. }
```

**python语言**

验签实现示例代码：

```
1. import binascii
2. import json
3. import base64
4. from cryptography.hazmat.primitives import hashes
5. from cryptography.hazmat.primitives.asymmetric import padding, rsa
6. from cryptography.hazmat.primitives.serialization import load_der_private_key, load_der_public_key
7. from cryptography.hazmat.backends import default_backend
8. from pyasn1.codec.ber import decoder
9. class SignatureUtils:
10. RS_LEN = 32
11. def verify_sm2(self, content, public_key_str, sign_data):
12. """
13. SM2验签
14. Args:
15. content: 原文
16. public_key_str: 公钥（Hex格式）
17. sign_data: 签名（Base64格式）
18. Returns:
19. bool: 验签结果
20. Raises:
21. Exception: 需要引入SM2库
22. """
23. try:
24. from gmssl import sm2, func

26. # 将Base64签名转换为Hex格式
27. sign_hex = self.base64_to_hex(sign_data)
28. print(f'plainData: {content}')
29. print(f'sign: {sign_data}')
30. print(f'sign hex: {sign_hex}')
31. # 创建SM2实例
32. sm2_crypt = sm2.CryptSM2(
33. public_key=self._preprocessing_public_key(public_key_str),
34. private_key=None,
35. asn1=True
36. )
37. # SM2验签
38. is_verified = sm2_crypt.verify_with_sm3(sign_hex, content.encode())

40. return is_verified
41. except ImportError:
42. raise Exception("SM2 verification requires gmssl library, please install: pip install gmssl")
43. except Exception as e:
44. raise Exception(f"SM2 verification failed: {str(e)}")
45. def is_asn1_format_key(self, key_hex_str: str, is_public_key: bool = False) -> bool:
46. """
47. 判断是否为asn1格式的密钥
48. Args:
49. key_hex_str: 十六进制密钥字符串
50. is_public_key: 是否为公钥
51. Returns:
52. boolean
53. """
54. ken_len = len(binascii.unhexlify(key_hex_str))
55. if is_public_key:
56. return ken_len != self.RS_LEN * 2 and ken_len != self.RS_LEN * 2 + 1
57. return ken_len != self.RS_LEN and ken_len != self.RS_LEN + 1
58. @classmethod
59. def covert_asn1_der_public_key(self, public_key: str) -> str:
60. """
61. 将sm2的DER编码的ASN.1格式的公钥，转换成未编码的原始密钥
62. Args:
63. public_key: DER编码的ASN.1格式的公钥字符串。
64. Returns:
65. 未编码的原始公钥，直接表示为一个65字节的十六进制字符串
66. """
67. asn1_obj, _ = decoder.decode(binascii.unhexlify(public_key))
68. public_key_bytes = asn1_obj[1].asOctets()
69. return public_key_bytes.hex()
70. @classmethod
71. def covert_asn1_der_private_key(self, private_key: str) -> str:
72. """
73. 将ASN.1格式的私钥，转换成未编码的原始密钥
74. Args:
75. private_key: DER编码的ASN.1格式的私钥字符串
76. Returns:
77. 返回BCEC格式的私钥
78. """
79. asn1_obj, _ = decoder.decode(binascii.unhexlify(private_key))
80. # 提取私钥的大整数部分，这里是特别适配了华为支付java-sdk的逻辑，如果是其他格式的私钥，可能需要调整这部分
81. private_key_sequence = decoder.decode(asn1_obj[2].asOctets())[0]
82. private_value_bytes = private_key_sequence[1].asOctets()
83. return private_value_bytes[:32].hex()  # 取32字节，为BCEC格式的标准长度
84. @classmethod
85. def _preprocessing_public_key(self, public_key):
86. """公钥预处理"""
87. if self.is_asn1_format_key(self, public_key, is_public_key=True):
88. public_key = self.covert_asn1_der_public_key(public_key)
89. # 手动去除前缀04，避免CryptSM2初始化时检查到04开头会使用lstrip方法，如果原公钥是以0开头，则起始的0会被误去除
90. if public_key.startswith('04'):
91. public_key = public_key[2:]
92. return public_key
93. # 验证用例
94. sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
95. from signature import SignatureUtils
96. class TestSignatureUtils(unittest.TestCase):
97. """签名工具类测试"""
98. def setUp(self):
99. """测试前准备"""
100. self.utils = SignatureUtils()
101. def test_sm2_verify(self):
102. """测试：SM2验签（需要安装gmssl）"""
103. # SM2测试数据
104. plain_data = ''
105. public_key_str = ''
106. sign_data = '' # Base64格式的SM2签名，需要替换为真实数据
107. try:
108. # SM2验签
109. verified = self.utils.verify_sm2(plain_data, public_key_str, sign_data)
110. print(f'SM2 verification result: {verified}')
111. except Exception as e:
112. if 'gmssl' in str(e):
113. self.skipTest('SM2 test skipped - gmssl not installed')
114. else:
115. raise
116. if __name__ == '__main__':
117. unittest.main()
```

**php语言**

验签实现示例代码：

```
1. # 使用三方库实现，安装命令：composer require lpilp/guomi
2. /**
3. * 测试：SM2验签（使用给定的示例数据）
4. */
5. public function testSM2Verify()
6. {
7. $plainData = '';
8. $publicKeyStr = '';
9. $signData = "";
10. try {
11. // SM2验签
12. $verified = $this->sm2Verify($plainData, $signData, $publicKeyStr);
13. $this->assertTrue($verified, "SM2 verification should succeed with given sample data");
14. } catch (Exception $e) {
15. $this->fail('SM2 verify failed: ' . $e->getMessage());
16. }
17. }
18. public function sm2Verify(string $data, string $signature, string $publicKey): bool
19. {
20. try {
21. if (empty($data)) {
22. throw new Exception('待验签数据不能为空');
23. }
24. if (empty($signature)) {
25. throw new Exception('签名不能为空');
26. }
27. if (empty($publicKey)) {
28. throw new Exception('公钥不能为空');
29. }
30. if (!class_exists('Rtgm\sm\RtSm2')) {
31. throw new Exception('Rtgm\sm\RtSm2 类不存在，请检查composer依赖');
32. }
33. $signatureHex = bin2hex(base64_decode($signature));
34. $sm2 = new RtSm2();
35. $result = $sm2->verifySign($data, $signatureHex, $publicKey);
36. echo'[sm2Verify] SM2验证结果: '.$result;
37. return $result;
38. } catch (Exception $e) {
39. echo '[sm2Verify Error] SM2验证异常: ' . $e->getMessage();
40. return false;
41. }
42. }
```

**c#语言**

验签实现示例代码：

```
1. using Xunit;
2. using System.Text;
3. using Org.BouncyCastle.Crypto.Parameters;
4. using Org.BouncyCastle.Crypto.Signers;
5. using Org.BouncyCastle.Utilities.Encoders;
6. using Org.BouncyCastle.Asn1.X9;
7. namespace PaySignatureTest
8. {
9. public class SignatureUtilsTest3
10. {
11. /// <summary>
12. /// 测试：SM2验签（需要引入BouncyCastle）命令：dotnet add package BouncyCastle
13. /// </summary>
14. [Fact]
15. public void TestSM2Verify()
16. {
17. // SM2测试数据
18. var plainData = "";
19. var publicKeyStr = "";
20. var signData = ""; // Base64格式的SM2签名，需要替换为真实数据
21. // SM2验签
22. var verified = verifySM2(plainData, publicKeyStr, signData);
23. Console.WriteLine($"SM2 verification result: {verified}");
24. }
25. public bool verifySM2(string content, string publicKeyStr, string signData)
26. {
27. // 使用BouncyCastle库实现SM2验签
28. // 将Base64签名转换为Hex格式
29. var signBytes = Convert.FromBase64String(signData);
30. var signHex = Hex.ToHexString(signBytes);
31. Console.WriteLine($"plainData: {content}");
32. Console.WriteLine($"sign: {signData}");
33. Console.WriteLine($"sign hex: {signHex}");
34. // 解析公钥
35. var curve = ECNamedCurveTable.GetByName("sm2p256v1");
36. var domain = new ECDomainParameters(curve.Curve, curve.G, curve.N, curve.H);
37. var q = curve.Curve.DecodePoint(Hex.Decode(publicKeyStr));
38. var publicKey = new ECPublicKeyParameters("EC", q, domain);
39. // 解析签名
40. var signer = new SM2Signer();
41. signer.Init(false, publicKey);
42. signer.BlockUpdate(Encoding.UTF8.GetBytes(content), 0, content.Length);
43. var isVerified = signer.VerifySignature(Hex.Decode(signHex));
44. return isVerified;
45. }
46. }
47. }
```

## 通知回调接口说明

* 对于回调通知，如果Payment Kit未收到application/json类型响应的数据，或收到应答数据不是{"resultCode":"000000","resultDesc":"Success."} ，Payment Kit会通过一定的周期定期重新发起通知，但不保证通知最终能成功。
* 相同通知可能多次重复发送给商户服务器，商户服务器需要正确实现以应对重复请求，处理建议：

  + 在商户服务器收到通知进行业务处理前先检查对应业务状态，对于未处理过的场景才进行业务处理。已处理的场景则直接返回成功。
  + 在业务处理时，合理设计同步机制防止并发问题。
* 如果在预期时间内未收到Payment Kit的回调请求，请排查提供的callbackUrl网络是否连通。如排除网络连通性问题，请调用同步查询接口确认订单状态。排查建议：

  + 确认callbackUrl为商户系统真实地址，保证url中的域名或IP是外网可以正常访问的。不能填写localhost、127.0.0.1、192.168.x.x、10.xx.xx.xx等。
  + callbackUrl必须为https://开头的完整地址。
* 对于收到的异步回调请求，请务必进行验签处理并在验签通过后进行后续业务流程。否则可能因为信息泄露导致对商户潜在的攻击，造成资金损失。
* 因商户自身系统实现问题导致的业务异常，资金损失，由商户自行承担。
* 如商户对支付回调地址有IP防火墙策略限制，需要对以下网段开通允许名单，后续有变动时会在此处更新。

  + 124.70.118.0/24
  + 139.159.166.0/24
* 商户系统收到回调通知时，需要在**3秒内**返回应答响应，否则华为支付会认为通知失败，会触发重试机制。
* 商户系统收到异步通知并返回{"resultCode":"000000","resultDesc":"Success."}时，服务器异步通知参数callbackId才会失效。同一个异步通知请求的多次重试callbackId是不变的。

**接口约束**

* 请勿将开发者的服务器的IP允许清单设置成用于限制华为的出口IP地址。IP允许清单本身并不能提高安全性且会给业务发展带来约束，在消息层面已有更安全的RSA签名机制条件下，没有存在价值。若开发者不遵守此约定带来的后果将由开发者自行承担。
* 地址必须支持HTTPS协议且具有合法商用证书，否则无法正常接收通知消息。
* 支持的TLS协议版本：1.2 / 1.3。
* 支持的加密套件列表：

  ```
  1. TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  2. TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
  3. TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
  4. TLS_DHE_DSS_WITH_AES_256_GCM_SHA384
  5. TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  6. TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
  7. TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  8. TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  9. TLS_AES_128_GCM_SHA256
  ```
