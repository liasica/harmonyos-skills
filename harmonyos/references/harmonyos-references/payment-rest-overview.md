---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-rest-overview
title: 公共说明
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 公共说明
category: harmonyos-references
scraped_at: 2026-09-02T15:03:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:05671231eff56539b10d826c478c122b76ffb6d7992d21eb82aaef5520940d1e
---

## HTTPS安全要求

* 所有的API请求必须使用HTTPS。
* 支持的TLS协议版本：1.2 / 1.3。
* 支持的加密套件列表：

  ```html
  TLS_CHACHA20_POLY1305_SHA256
  TLS_AES_128_GCM_SHA256
  TLS_AES_256_GCM_SHA384
  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  ```

## HTTP方法说明

当前Payment Kit对外接口涉及GET及POST两种HTTP METHOD。

* **GET**：对应于查询场景。适用于从服务器查询资源数据，如查询订单信息、查询签约信息等。
* **POST**：对应于新建/更新资源场景，如预下单、退款请求等。

## 数据格式

请求和响应报文统一使用JSON格式。

## 字符编码

Payment Kit所有请求默认支持UTF-8编码，如采用其他编码格式的报文可能导致验签失败、字段解析失败等问题。

HTTP METHOD方式为GET的接口请求，请求URL如涉及参数拼接，拼接后完整的请求URL不建议带特殊字符。如有需要，建议对URL中的特殊字符进行编码处理。URL特殊字符参考但不限于：“+”、“空格”、“?”，“%”，“#”，“&”、“=”。

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

   ```json
   "allocationType=DELAY_ORDER_ALLOCATION&callbackUrl=https://www.xxxxxx.com/hw/pay/callback&currency=CNY&mercNo=xxxxxx&mercOrderNo=xxxxxx&totalAmount=2&tradeSummary=杂志报刊"
   ```
3. 签名：调用给定算法对排序后的串完成签名。

   **SHA256WithRSA/PSS：** 具体可参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md#集成maven依赖)中RSAUtils.java类的signByRSAWithPSS方法。

   **SM2：** 具体可参考[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md#集成maven依赖)中Sm2Utils.java类中的sign方法。

   加签内容参考：

   ```txt
   POST请求：POST https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/preorder/create/app
   {
       "appId": "5765880207854262xxx",
       "callbackUrl": "https://www.xxx.com/hw_notify",
       "currency": "CNY",
       "mercNo": "101723200xxx",
       "mercOrderNo": "2405171027547xxx",
       "payload": "shop|h8ahnJA8xxRXVw",
       "totalAmount": 5,
       "tradeSummary": "test",
       "subOrders": [
         {
           "mercNo": "101723200xxx",
           "mercOrderNo": "abcxxx1"
         },
         {
           "mercNo": "101723201xxx",
           "mercOrderNo": "abcxxx2"
         }
       ]
   }
   加签内容：appId=5765880207854262xxx&callbackUrl=https://www.xxx.com/hw_notify&currency=CNY&mercNo=101723200xxx&mercOrderNo=2405171027547xxx&payload=shop|h8ahnJA8xxRXVw&subOrders=mercNo=101723200xxx&mercOrderNo=abcxxx1,mercNo=101723201xxx&mercOrderNo=abcxxx2&totalAmount=5&tradeSummary=test

   GET请求：GET https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/transactions/merc-orders/20240507000000041809599950090xxx?mercNo=101540000089&sdkVersion=1.0.0
   加签内容：/api/v2/aggr/transactions/merc-orders/20240507000000041809599950090xxx?mercNo=101540000089&sdkVersion=1.0.0
   ```

**注意** 

字段值设置为null时，字段可不参与签名，设置为空字符时，则必须参与签名。

### 常用语言SHA256WithRSA/PSS加签示例代码参考

**go语言**

加签实现示例代码：

```go
// 排序拼接示例
import (
    "encoding/base64"
    "encoding/hex"
    "encoding/json"
    "fmt"
    "sort"
    "strings"
)

// GenerateSignData 生成待签名字符串
// 步骤一：筛选，排除sign字段
// 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
func (s *SignatureUtils) GenerateSignData(params map[string]interface{}) string {
    return s.buildSignData(params)
}
// buildSignData 递归构建签名字符串
func (s *SignatureUtils) buildSignData(params interface{}) string {
    switch v := params.(type) {
    case map[string]interface{}:
        return s.buildMapSignData(v)
    case []interface{}:
        return s.buildArraySignData(v)
    default:
        return fmt.Sprintf("%v", v)
    }
}
// buildMapSignData 处理Map类型数据
func (s *SignatureUtils) buildMapSignData(params map[string]interface{}) string {
    // 排序key
    var keys []string
    for k := range params {
        // 排除sign字段
        if k == "sign" {
            continue
        }
        keys = append(keys, k)
    }
    sort.Strings(keys)
    var parts []string
    for _, key := range keys {
        value := params[key]
        // null值不参与签名
        if value == nil {
            continue
        }
        // 空字符串参与签名
        strValue := s.buildSignData(value)
        parts = append(parts, fmt.Sprintf("%s=%s", key, strValue))
    }
    return strings.Join(parts, "&")
}
// buildArraySignData 处理数组类型数据
func (s *SignatureUtils) buildArraySignData(arr []interface{}) string {
    var parts []string
    for _, item := range arr {
        if item == nil {
            continue
        }
        parts = append(parts, s.buildSignData(item))
    }
    return strings.Join(parts, ",")
}

// 加签示例
package main
import (
  "crypto"
  "crypto/rand"
  "crypto/rsa"
  "crypto/sha256"
  "crypto/x509"
  "encoding/base64"
  "fmt"
  "testing"
)
func signSha256WithRsaPSS(message, privateKeyStr string) (string, error) {
  privateKey, err := getPrivateKey(privateKeyStr)
  if err != nil {
    return "", err
  }
  hasher := sha256.New()
  hasher.Write([]byte(message))
  hashedMessage := hasher.Sum(nil)
  opts := rsa.PSSOptions{
    SaltLength: rsa.PSSSaltLengthEqualsHash,
    Hash:       crypto.SHA256,
  }
  signature, err := rsa.SignPSS(rand.Reader, privateKey, crypto.SHA256, hashedMessage, &opts)
  if err != nil {
    return "", err
  }
  return base64.StdEncoding.EncodeToString(signature), nil
}

func getPrivateKey(privateKeyStr string) (*rsa.PrivateKey, error) {
  decoded, err := base64.StdEncoding.DecodeString(privateKeyStr)
  if err != nil {
    return nil, err
  }
  privateKey, err := x509.ParsePKCS8PrivateKey(decoded)
  if err != nil {
    return nil, err
  }
  rsaPrivateKey, ok := privateKey.(*rsa.PrivateKey)
  if !ok {
  return nil, err
  }
  return rsaPrivateKey, nil
}

func TestRsaSign(t *testing.T) {
  signature, err := signSha256WithRsaPSS("加签排序拼接内容","私钥")
  fmt.Println(signature, err)
}
```

**JavaScript语言**

javascript可通过jsrsasign模块实现，如已安装node环境，可执行如下命令安装jsrsasign模块。

```shell
npm install jsrsasign
```

加签实现示例代码：

```javascript
// 排序拼接示例
/**
 * 递归构建签名字符串
 * @param {*} data 数据
 * @returns {string} 签名字符串
 */
buildSignData(data) {
    if (data === null || data === undefined) {
        return '';
    }
    if (typeof data === 'object' && !Array.isArray(data)) {
        return this.buildMapSignData(data);
    }
    if (Array.isArray(data)) {
        return this.buildArraySignData(data);
    }
    return String(data);
}
/**
 * 处理Map类型数据
 * @param {Object} params 参数对象
 * @returns {string} 签名字符串
 */
buildMapSignData(params) {
    // 排序key
    const keys = Object.keys(params)
        .filter(key => key !== 'sign') // 排除sign字段
        .sort();
    const parts = [];
    for (const key of keys) {
        const value = params[key];
        // null值不参与签名
        if (value === null || value === undefined) {
            continue;
        }
        // 空字符串参与签名
        const strValue = this.buildSignData(value);
        parts.push(`${key}=${strValue}`);
    }
    return parts.join('&');
}
/**
 * 处理数组类型数据
 * @param {Array} arr 数组
 * @returns {string} 签名字符串
 */
buildArraySignData(arr) {
    const parts = [];
    for (const item of arr) {
        if (item === null || item === undefined) {
            continue;
        }
        parts.push(this.buildSignData(item));
    }
    return parts.join(',');
}

// 加签示例
const jsrsasign = require('jsrsasign');
function signSha256WithRsaPSS(plainData, privateStr) {
  let rsa = new jsrsasign.RSAKey();
  // PEM 格式的私钥
  const priKey = `-----BEGIN PRIVATE KEY-----\n${privateStr}\n-----END PRIVATE KEY-----\n`;
  rsa = jsrsasign.KEYUTIL.getKey(priKey);
  const sig = new jsrsasign.KJUR.crypto.Signature({
    alg: 'SHA256withRSAandMGF1',
  });
  sig.init(rsa);
  sig.updateString(plainData);
  return jsrsasign.hextob64(sig.sign());
}
let signature = signSha256WithRsaPSS("加签排序拼接内容","私钥");
console.info(signature)
```

**python语言**

python可通过cryptography模块实现，可先执行如下命令安装cryptography模块：

```python
pip install cryptography
```

加签实现示例代码：

```python
# 排序拼接示例
def generate_sign_data(self, params):
    """
    生成待签名字符串
    步骤一：筛选，排除sign字段
    步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
    Args:
        params: 参数字典
    Returns:
        str: 待签名字符串
    """
    return self._build_sign_data(params)
def _build_sign_data(self, data):
    """
    递归构建签名字符串
    Args:
        data: 数据
    Returns:
        str: 签名字符串
    """
    if data is None:
        return ''
    if isinstance(data, dict):
        return self._build_map_sign_data(data)
    if isinstance(data, (list, tuple)):
        return self._build_array_sign_data(data)
    return str(data)
def _build_map_sign_data(self, params):
    """
    处理字典类型数据
    Args:
        params: 参数字典
    Returns:
        str: 签名字符串
    """
    # 排序key，排除sign字段
    keys = sorted([k for k in params.keys() if k != 'sign'])
    parts = []
    for key in keys:
        value = params[key]
        # None值不参与签名
        if value is None:
            continue
        # 空字符串参与签名
        str_value = self._build_sign_data(value)
        parts.append(f"{key}={str_value}")
    return '&'.join(parts)
def _build_array_sign_data(self, arr):
    """
    处理数组类型数据
    Args:
        arr: 数组
    Returns:
        str: 签名字符串
    """
    parts = []
    for item in arr:
        if item is None:
            continue
        parts.append(self._build_sign_data(item))
    return ','.join(parts)

# 加签示例
import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

def signSha256WithRsaPSS(private_key_str, message):
    # PEM 格式的私钥
    prikey_content = "-----BEGIN PRIVATE KEY-----\n" + private_key_str +"\n-----END PRIVATE KEY-----\n";
    private_key = load_pem_private_key(data=prikey_content.encode("utf-8"), password=None, backend=default_backend())

    # 使用 RSA-PSS 算法生成签名
    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

message = "加签排序拼接内容"
private_key_str = "私钥"
signature = signSha256WithRsaPSS(private_key_str, message)
print(signature)
```

**php语言**

php可通过phpseclib加密库实现，如已安装composer环境，可先通过以下命令导入phpseclib：

```php
composer require phpseclib/phpseclib
```

phpseclib2加签实现示例代码：

```php
// 排序拼接示例
class SignatureUtils
{
    /**
     * 生成待签名字符串
     * 步骤一：筛选，排除sign字段
     * 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
     *
     * @param array $params 参数数组
     * @return string 待签名字符串
     */
    public function generateSignData($params)
    {
        return $this->buildSignData($params);
    }
    /**
     * 递归构建签名字符串
     *
     * @param mixed $data 数据
     * @return string 签名字符串
     */
    private function buildSignData($data)
    {
        if ($data === null) {
            return '';
        }
        if (is_array($data)) {
            // 判断是否为关联数组（Map）
            if ($this->isAssocArray($data)) {
                return $this->buildMapSignData($data);
            } else {
                return $this->buildArraySignData($data);
            }
        }
        return (string)$data;
    }
    /**
     * 判断是否为关联数组
     *
     * @param array $arr 数组
     * @return bool
     */
    private function isAssocArray($arr)
    {
        if (empty($arr)) {
            return false;
        }
        return array_keys($arr) !== range(0, count($arr) - 1);
    }
    /**
     * 处理Map类型数据
     *
     * @param array $params 参数数组
     * @return string 签名字符串
     */
    private function buildMapSignData($params)
    {
        // 排序key，排除sign字段
        $keys = array_keys($params);
        $keys = array_filter($keys, function($key) {
            return $key !== 'sign';
        });
        sort($keys);
        $parts = [];
        foreach ($keys as $key) {
            $value = $params[$key];
            // null值不参与签名
            if ($value === null) {
                continue;
            }
            // 空字符串参与签名
            $strValue = $this->buildSignData($value);
            $parts[] = $key . '=' . $strValue;
        }
        return implode('&', $parts);
    }
    /**
     * 处理数组类型数据
     *
     * @param array $arr 数组
     * @return string 签名字符串
     */
    private function buildArraySignData($arr)
    {
        $parts = [];
        foreach ($arr as $item) {
            if ($item === null) {
                continue;
            }
            $parts[] = $this->buildSignData($item);
        }
        return implode(',', $parts);
    }
    /**
     * Base64转Hex
     *
     * @param string $base64String Base64字符串
     * @return string Hex字符串
     */
    private function base64ToHex($base64String)
    {
        $bytes = base64_decode($base64String);
        return bin2hex($bytes);
    }
    /**
     * 解析JSON字符串为数组
     *
     * @param string $jsonStr JSON字符串
     * @return array 数组
     */
    public function parseJSON($jsonStr)
    {
        return json_decode($jsonStr, true);
    }
    /**
     * 从JSON字符串生成待签名字符串
     *
     * @param string $jsonStr JSON字符串
     * @return string 待签名字符串
     */
    public function generateSignDataFromJSON($jsonStr)
    {
        $params = $this->parseJSON($jsonStr);
        return $this->generateSignData($params);
    }
    public function testExcludeSignField()
    {
        $params = [
            'appId' => '5765880207854262xxx',
            'callbackUrl' => 'https://www.xxx.com/hw_notify',
            'sign' => 'xxxxx', // sign字段应被排除
            'currency' => 'CNY'
        ];
        $signData = $this-> generateSignData($params);
        echo "[testExcludeSignField] Sign data without sign field: " . $signData . "\n";
    }
}

// 加签示例
<?php
require_once 'vendor/autoload.php';
use phpseclib\Crypt\RSA;

function signSha256WithRsaPSS($content, $privateKeyStr) {
    try {
        $privateKey = "-----BEGIN PRIVATE KEY-----\n" . $privateKeyStr ."\n-----END PRIVATE KEY-----";
        $signer = new \phpseclib\Crypt\RSA();
        $signer->loadKey($privateKey, $password = false);
        $signer->setHash('sha256');
        $signer->setSignatureMode(RSA::SIGNATURE_PSS);
        $signer->setMGFHash('sha256');
        $signature = $signer->sign($content);

        $sign = base64_encode($signature);
        return $sign;
    } catch (Exception $e) {
        echo $e->getMessage();
    }
    return null;
}
$data = "加签排序拼接内容";
$privateKeyStr = "私钥";
echo signSha256WithRsaPSS($data, $privateKeyStr)
?>
```

phpseclib3加签实现示例代码：

```php
<?php
require_once 'vendor/autoload.php';

use phpseclib3\Crypt\PublicKeyLoader;
use phpseclib3\Crypt\RSA;

function signSha256WithRsaPSS($data,$rsa_key){
    $key = "-----BEGIN PRIVATE KEY-----\n" . $rsa_key . "-----END PRIVATE KEY-----";
    $private = PublicKeyLoader::load($key, $password = false);
    $private = $private->withPadding(RSA::SIGNATURE_PSS);
    return base64_encode($private->sign($data));
}

$data = "加签排序拼接内容";
$privateKeyStr = "私钥";
echo signSha256WithRsaPSS($data, $privateKeyStr);
?>
```

**C#语言**

C#可通过BouncyCastle库来实现，如已安装 [.NET SDK](https://dotnet.microsoft.com/download)，可先执行如下命令添加BouncyCastle：

```cs
dotnet add package BouncyCastle
```

加签实现示例代码：

```cs
// 排序拼接示例
using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Linq;
namespace PaySignature
{
    /// <summary>
    /// 签名工具类
    /// </summary>
    public class SignatureUtils
    {
        /// <summary>
        /// 生成待签名字符串
        /// 步骤一：筛选，排除sign字段
        /// 步骤二：排序拼接，按key的ascii码顺序排序，使用&连接
        /// </summary>
        /// <param name="params">参数字典</param>
        /// <returns>待签名字符串</returns>
        public string GenerateSignData(Dictionary<string, object> parameters)
        {
            return BuildSignData(parameters);
        }
        /// <summary>
        /// 递归构建签名字符串
        /// </summary>
        /// <param name="data">数据</param>
        /// <returns>签名字符串</returns>
        private string BuildSignData(object data)
        {
            if (data == null)
            {
                return string.Empty;
            }
            if (data is Dictionary<string, object> dict)
            {
                return BuildMapSignData(dict);
            }
            if (data is List<object> list)
            {
                return BuildArraySignData(list);
            }
            return data.ToString();
        }
        /// <summary>
        /// 处理字典类型数据
        /// </summary>
        /// <param name="parameters">参数字典</param>
        /// <returns>签名字符串</returns>
        private string BuildMapSignData(Dictionary<string, object> parameters)
        {
            // 排序key，排除sign字段
            var keys = parameters.Keys
                .Where(k => k != "sign")
                .OrderBy(k => k, StringComparer.Ordinal)
                .ToList();
            var parts = new List<string>();
            foreach (var key in keys)
            {
                var value = parameters[key];
                // null值不参与签名
                if (value == null)
                {
                    continue;
                }
                // 空字符串参与签名
                var strValue = BuildSignData(value);
                parts.Add($"{key}={strValue}");
            }
            return string.Join("&", parts);
        }
        /// <summary>
        /// 处理数组类型数据
        /// </summary>
        /// <param name="arr">数组</param>
        /// <returns>签名字符串</returns>
        private string BuildArraySignData(List<object> arr)
        {
            var parts = new List<string>();
            foreach (var item in arr)
            {
                if (item == null)
                {
                    continue;
                }
                parts.Add(BuildSignData(item));
            }
            return string.Join(",", parts);
        }
        /// <summary>
        /// Base64转Hex
        /// </summary>
        /// <param name="base64String">Base64字符串</param>
        /// <returns>Hex字符串</returns>
        private string Base64ToHex(string base64String)
        {
            var bytes = Convert.FromBase64String(base64String);
            return BitConverter.ToString(bytes).Replace("-", "").ToLower();
        }
        /// <summary>
        /// 解析JSON字符串为字典
        /// </summary>
        /// <param name="jsonStr">JSON字符串</param>
        /// <returns>字典</returns>
        public Dictionary<string, object> ParseJSON(string jsonStr)
        {
            using var document = JsonDocument.Parse(jsonStr);
            var result = new Dictionary<string, object>();
            foreach (var element in document.RootElement.EnumerateObject())
            {
                result[element.Name] = ParseJsonElement(element.Value);
            }
            return result;
        }
        /// <summary>
        /// 解析JSON元素
        /// </summary>
        /// <param name="element">JSON元素</param>
        /// <returns>对象</returns>
        private object ParseJsonElement(JsonElement element)
        {
            switch (element.ValueKind)
            {
                case JsonValueKind.String:
                    return element.GetString();
                case JsonValueKind.Number:
                    if (element.TryGetInt32(out int intValue))
                        return intValue;
                    if (element.TryGetInt64(out long longValue))
                        return longValue;
                    return element.GetDouble();
                case JsonValueKind.True:
                    return true;
                case JsonValueKind.False:
                    return false;
                case JsonValueKind.Null:
                    return null;
                case JsonValueKind.Object:
                    var dict = new Dictionary<string, object>();
                    foreach (var prop in element.EnumerateObject())
                    {
                        dict[prop.Name] = ParseJsonElement(prop.Value);
                    }
                    return dict;
                case JsonValueKind.Array:
                    var list = new List<object>();
                    foreach (var item in element.EnumerateArray())
                    {
                        list.Add(ParseJsonElement(item));
                    }
                    return list;
                default:
                    return element.ToString();
            }
        }
        /// <summary>
        /// 从JSON字符串生成待签名字符串
        /// </summary>
        /// <param name="jsonStr">JSON字符串</param>
        /// <returns>待签名字符串</returns>
        public string GenerateSignDataFromJSON(string jsonStr)
        {
            var parameters = ParseJSON(jsonStr);
            return GenerateSignData(parameters);
        }
    }
}
// 测试
using Xunit;
using PaySignature;
namespace PaySignatureTest
{
    public class SignatureUtilsTest2
    {
        private readonly SignatureUtils _utils;
        public SignatureUtilsTest2()
        {
            _utils = new SignatureUtils();
        }
        /// <summary>
        /// 测试构造签名串
        /// </summary>
        [Fact]
        public void TestComplexNestedStructure()
        {
            var goods = new List<object>
            {
                new Dictionary<string, object>
                {
                    { "goodsId", "G001" },
                    { "goodsName", "商品1" },
                    { "quantity", 2 }
                },
                new Dictionary<string, object>
                {
                    { "goodsId", "G002" },
                    { "goodsName", "商品2" },
                    { "quantity", 3 }
                }
            };
            var parameters = new Dictionary<string, object>
            {
                { "appId", "5765880207854262xxx" },
                { "goods", goods },
                { "totalAmount", 100 }
            };
            var signData = _utils.GenerateSignData(parameters);
            Assert.Contains("appId=5765880207854262xxx", signData);
            Assert.Contains("goods=", signData);
            Console.WriteLine($"Sign data with complex structure: {signData}");
        }
    }
}

// 加签示例
using System.Text;
using Org.BouncyCastle.OpenSsl;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Security;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Crypto.Engines;
using Org.BouncyCastle.Crypto.Digests;
class SignProgram
{
    public static void Main(string[] args)
    {
        string res = RSASign("加签排序拼接内容","私钥");
        Console.WriteLine("result: " + res);
    }
    public static string RSASign(string datastr,string privateStr)
    {
        var priKey = "-----BEGIN PRIVATE KEY-----\n"+ privateStr +"\n-----END PRIVATE KEY-----\n";
        byte[] data = Encoding.UTF8.GetBytes(datastr);
        // 创建PSS签名器
        var signer = new PssSigner(new RsaEngine(), new Sha256Digest());
        AsymmetricKeyParameter rsaPrivateKey = null;
        using (var stringReader = new StringReader(priKey))
        {
            var pemReader = new PemReader(stringReader);
            rsaPrivateKey = pemReader.ReadObject() as AsymmetricKeyParameter;
        }
        signer.Init(true, new ParametersWithRandom(rsaPrivateKey, new SecureRandom()));
        signer.BlockUpdate(data, 0, data.Length);
        byte[] signature = signer.GenerateSignature();
        return Convert.ToBase64String(signature);
    }
}
```

## 验签规则

**验签场景：** 商户需要对来自Payment Kit服务器的信息做验签，验证签名信息身份来自Payment Kit服务器。商户服务器对华为支付服务器返回的回调通知请求参数和退款通知请求参数验签。

**验签算法：** SM2。

**开发步骤：** 确认验证签名的公钥证书、确认参与签名字段将待签名字段转换为“key=value”并以符号“&”拼接、使用验签方法验证签名。

1. 获取华为支付公钥，此处公钥证书为[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)获取的证书，可参见[下载华为支付证书](../harmonyos-guides/payment-certificates-config.md#下载华为支付证书)。
2. 获取参与签名的字段，转换为map并将map的“key-value”排序后以符号“&”拼接。
3. 使用SM2算法进行验签，具体参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](../harmonyos-guides/payment-server-connect.md)中VerifyTools.java类的verifySign方法。

**注意** 

因业务发展需要，接口字段可能发生变动，建议验签功能实现可扩展——即“先对回调通知的请求体进行验签处理，再转换成业务对象处理”，以确保在字段有变化时也可以正常验签。

### 常用语言SM2验签示例代码参考

**JavaScript语言**

javascript可通过sm-crypto模块实现，如已安装node环境，可执行如下命令安装：

```javascript
npm install sm-crypto
```

验签实现示例代码：

```javascript
const SmCrypto = require('sm-crypto');
function signSM2Verify(plainData, sign, publicStr) {
  let signHex1 = base64ToHex(sign)
  console.info("plainData: " + plainData)
  console.info("sign: " + sign)
  console.info("sign hex: " + signHex1)
  return SmCrypto.sm2.doVerifySignature(plainData, signHex1, publicStr, {
    hash: true,
    der: true
  })
}
function base64ToHex(base64String) {
  const buffer = Buffer.from(base64String, 'base64');
  return buffer.toString('hex');
}
let signSM2VerifyRes = signSM2Verify(
    "验签排序拼接内容",
    "验签sign",
    "验签公钥"
);
console.info(signSM2VerifyRes)
```

**go语言**

验签实现示例代码：

```go
// TestSM2Verify 测试：SM2验签（需要安装go get -u github.com/tjfoc/gmsm）
func ReadSM2PublicKeyFromHex(publicKeyStr string) (*sm2.PublicKey, error) {
    // 解码十六进制字符串
    pubKeyBytes, err := hex.DecodeString(publicKeyStr)
    if err != nil {
        return nil, fmt.Errorf("failed to decode hex: %v", err)
    }
    // 检查是否为非压缩格式 (0x04 开头)
    if len(pubKeyBytes) != 65 || pubKeyBytes[0] != 0x04 {
        return nil, fmt.Errorf("invalid SM2 public key format (expected 65 bytes, starting with 0x04)")
    }
    // 解析 X 和 Y 坐标（SM2 公钥长度为 65 字节：0x04 + 32字节X + 32字节Y）
    x := pubKeyBytes[1:33]  // X 坐标（32字节）
    y := pubKeyBytes[33:65] // Y 坐标（32字节）
    // 构造 SM2 公钥
    publicKey := &sm2.PublicKey{
        Curve: sm2.P256Sm2(), // SM2 曲线
            X:     new(big.Int).SetBytes(x),
            Y:     new(big.Int).SetBytes(y),
    }
    return publicKey, nil
}
func (s *SignatureUtils) VerifySM2(content, publicKeyStr, signData string) (bool, error) {
    // 将Base64签名转换为Hex格式
    signBytes, err := base64.StdEncoding.DecodeString(signData)
    if err != nil {
        return false, fmt.Errorf("decode sign data failed: %v", err)
    }
    signHex := hex.EncodeToString(signBytes)
    // 解析公钥
    publicKey, err := ReadSM2PublicKeyFromHex(publicKeyStr)
    if err != nil {
        return false, fmt.Errorf("parse public key failed: %v", err)
    }
    // 将Hex签名转换为字节数组
    signature, err := hex.DecodeString(signHex)
    if err != nil {
        return false, fmt.Errorf("decode signature hex failed: %v", err)
    }
    // SM2验签
    isVerified := publicKey.Verify([]byte(content), signature)
    if !isVerified {
        return false, fmt.Errorf("SM2 verification requires external library, please install: go get github.com/tjfoc/gmsm")
    }
    return true, nil
}
```

**python语言**

验签实现示例代码：

```python
import binascii
import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import load_der_private_key, load_der_public_key
from cryptography.hazmat.backends import default_backend
from pyasn1.codec.ber import decoder
class SignatureUtils:
    RS_LEN = 32
    def verify_sm2(self, content, public_key_str, sign_data):
        """
        SM2验签
        Args:
            content: 原文
            public_key_str: 公钥（Hex格式）
            sign_data: 签名（Base64格式）
        Returns:
            bool: 验签结果
        Raises:
            Exception: 需要引入SM2库
        """
        try:
            from gmssl import sm2, func
            
            # 将Base64签名转换为Hex格式
            sign_hex = self.base64_to_hex(sign_data)
            print(f'plainData: {content}')
            print(f'sign: {sign_data}')
            print(f'sign hex: {sign_hex}')
            # 创建SM2实例
            sm2_crypt = sm2.CryptSM2(
                public_key=self._preprocessing_public_key(public_key_str),
                private_key=None,
                asn1=True
            )
            # SM2验签
            is_verified = sm2_crypt.verify_with_sm3(sign_hex, content.encode())
            
            return is_verified
        except ImportError:
            raise Exception("SM2 verification requires gmssl library, please install: pip install gmssl")
        except Exception as e:
            raise Exception(f"SM2 verification failed: {str(e)}")
    def is_asn1_format_key(self, key_hex_str: str, is_public_key: bool = False) -> bool:
        """
        判断是否为asn1格式的密钥
        Args:
            key_hex_str: 十六进制密钥字符串
            is_public_key: 是否为公钥
        Returns:
            boolean
        """
        ken_len = len(binascii.unhexlify(key_hex_str))
        if is_public_key:
            return ken_len != self.RS_LEN * 2 and ken_len != self.RS_LEN * 2 + 1
        return ken_len != self.RS_LEN and ken_len != self.RS_LEN + 1
    @classmethod
    def covert_asn1_der_public_key(self, public_key: str) -> str:
        """
        将sm2的DER编码的ASN.1格式的公钥，转换成未编码的原始密钥
        Args:
            public_key: DER编码的ASN.1格式的公钥字符串。
        Returns:
            未编码的原始公钥，直接表示为一个65字节的十六进制字符串
        """
        asn1_obj, _ = decoder.decode(binascii.unhexlify(public_key))
        public_key_bytes = asn1_obj[1].asOctets()
        return public_key_bytes.hex()
    @classmethod
    def covert_asn1_der_private_key(self, private_key: str) -> str:
        """
        将ASN.1格式的私钥，转换成未编码的原始密钥
        Args:
            private_key: DER编码的ASN.1格式的私钥字符串
        Returns:
            返回BCEC格式的私钥
        """
        asn1_obj, _ = decoder.decode(binascii.unhexlify(private_key))
        # 提取私钥的大整数部分，这里是特别适配了华为支付java-sdk的逻辑，如果是其他格式的私钥，可能需要调整这部分
        private_key_sequence = decoder.decode(asn1_obj[2].asOctets())[0]
        private_value_bytes = private_key_sequence[1].asOctets()
        return private_value_bytes[:32].hex()  # 取32字节，为BCEC格式的标准长度
    @classmethod
    def _preprocessing_public_key(self, public_key):
        """公钥预处理"""
        if self.is_asn1_format_key(self, public_key, is_public_key=True):
            public_key = self.covert_asn1_der_public_key(public_key)
        # 手动去除前缀04，避免CryptSM2初始化时检查到04开头会使用lstrip方法，如果原公钥是以0开头，则起始的0会被误去除
        if public_key.startswith('04'):
            public_key = public_key[2:]
        return public_key
# 验证用例
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from signature import SignatureUtils
class TestSignatureUtils(unittest.TestCase):
    """签名工具类测试"""
    def setUp(self):
        """测试前准备"""
        self.utils = SignatureUtils()
    def test_sm2_verify(self):
        """测试：SM2验签（需要安装gmssl）"""
        # SM2测试数据
        plain_data = ''
        public_key_str = ''
        sign_data = '' # Base64格式的SM2签名，需要替换为真实数据
        try:
            # SM2验签
            verified = self.utils.verify_sm2(plain_data, public_key_str, sign_data)
            print(f'SM2 verification result: {verified}')
        except Exception as e:
            if 'gmssl' in str(e):
                self.skipTest('SM2 test skipped - gmssl not installed')
            else:
                raise
if __name__ == '__main__':
    unittest.main()
```

**php语言**

验签实现示例代码：

```php
# 使用三方库实现，安装命令：composer require lpilp/guomi
/**
* 测试：SM2验签（使用给定的示例数据）
*/
public function testSM2Verify()
{
    $plainData = '';
    $publicKeyStr = '';
    $signData = "";
    try {
        // SM2验签
        $verified = $this->sm2Verify($plainData, $signData, $publicKeyStr);
        $this->assertTrue($verified, "SM2 verification should succeed with given sample data");
    } catch (Exception $e) {
        $this->fail('SM2 verify failed: ' . $e->getMessage());
    }
}
public function sm2Verify(string $data, string $signature, string $publicKey): bool
{
    try {
        if (empty($data)) {
            throw new Exception('待验签数据不能为空');
        }
        if (empty($signature)) {
            throw new Exception('签名不能为空');
        }
        if (empty($publicKey)) {
            throw new Exception('公钥不能为空');
        }
        if (!class_exists('Rtgm\sm\RtSm2')) {
            throw new Exception('Rtgm\sm\RtSm2 类不存在，请检查composer依赖');
        }
        $signatureHex = bin2hex(base64_decode($signature));
        $sm2 = new RtSm2();
        $result = $sm2->verifySign($data, $signatureHex, $publicKey);
        echo'[sm2Verify] SM2验证结果: '.$result;
        return $result;
    } catch (Exception $e) {
        echo '[sm2Verify Error] SM2验证异常: ' . $e->getMessage();
        return false;
    }
}
```

**c#语言**

验签实现示例代码：

```cs
using Xunit;
using System.Text;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Utilities.Encoders;
using Org.BouncyCastle.Asn1.X9;
namespace PaySignatureTest
{
    public class SignatureUtilsTest3
    {
        /// <summary>
        /// 测试：SM2验签（需要引入BouncyCastle）命令：dotnet add package BouncyCastle
        /// </summary>
        [Fact]
        public void TestSM2Verify()
        {
            // SM2测试数据
            var plainData = "";
            var publicKeyStr = "";
            var signData = ""; // Base64格式的SM2签名，需要替换为真实数据
            // SM2验签
            var verified = verifySM2(plainData, publicKeyStr, signData);
            Console.WriteLine($"SM2 verification result: {verified}");
        }
        public bool verifySM2(string content, string publicKeyStr, string signData)
        {
            // 使用BouncyCastle库实现SM2验签
            // 将Base64签名转换为Hex格式
            var signBytes = Convert.FromBase64String(signData);
            var signHex = Hex.ToHexString(signBytes);
            Console.WriteLine($"plainData: {content}");
            Console.WriteLine($"sign: {signData}");
            Console.WriteLine($"sign hex: {signHex}");
            // 解析公钥
            var curve = ECNamedCurveTable.GetByName("sm2p256v1");
            var domain = new ECDomainParameters(curve.Curve, curve.G, curve.N, curve.H);
            var q = curve.Curve.DecodePoint(Hex.Decode(publicKeyStr));
            var publicKey = new ECPublicKeyParameters("EC", q, domain);
            // 解析签名
            var signer = new SM2Signer();
            signer.Init(false, publicKey);
            signer.BlockUpdate(Encoding.UTF8.GetBytes(content), 0, content.Length);
            var isVerified = signer.VerifySignature(Hex.Decode(signHex));
            return isVerified;
        }
    }
}
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

  ```html
  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
  TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
  TLS_DHE_DSS_WITH_AES_256_GCM_SHA384
  TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  TLS_AES_128_GCM_SHA256
  ```
