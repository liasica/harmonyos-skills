---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-unbindplayer
title: 解绑账号
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > REST API > 解绑账号
category: harmonyos-references
scraped_at: 2026-04-28T08:16:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e84d5039fdd7fd9918f2436da8646a1306342d18145e2bc642f6c1e6c44ea7d
---

## 功能介绍

调用此接口可以将游戏官方账号与华为teamPlayerId的解绑结果上报给华为游戏服务器。

## 场景描述

玩家选择华为账号登录游戏时，游戏需要将游戏官方账号与华为teamPlayerId绑定，并将绑定结果上报给华为游戏服务器。若需将游戏官方账号与华为teamPlayerId解绑，需将解绑结果上报给华为，此时客户端侧可通过Game Service Kit的[unbindPlayer](gameservice-gameplayer.md#gameplayerunbindplayer)接口实现，服务器侧则可通过本接口实现。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为游戏服务器
* **接口URL**：<https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi>
* **数据格式**：

  + 请求：Content-Type: application/x-www-form-urlencoded（表单方式）
  + 响应：Content-Type: application/json

## 请求参数

**body参数**

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| method | 是 | String | 固定传入“external.hms.gs.player.unbindPlayer”。  最大长度64个字符。 |
| appId | 否 | String | 游戏在AppGallery Connect中的APP ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。若解绑“游戏级别”类型，该参数必填。  最大长度32个字符。 |
| cpId | 是 | String | 游戏开发者在AppGallery Connect中的Developer ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  最大长度32个字符。 |
| teamPlayerId | 是 | String | HarmonyOS 5.0及以上游戏的玩家标识，通过调用[unionLogin](gameservice-gameplayer.md#gameplayerunionlogin)接口返回，  最大长度256个字符。 |
| ts | 是 | Long | 当前时间的时间戳，即当前时间距离GMT时间1970年1月1号0时0分0秒所差的毫秒数。 |
| sign | 是 | String | 用于华为游戏服务器对请求参数验签的签名字符串。  为防止请求被篡改，游戏需要根据[签名机制](gameservice-unbindplayer.md#签名机制)中的方法生成签名字符串，华为服务器在收到请求后会对签名字符串进行验签，验签成功后才会进行后续处理，否则将返回失败错误码。请求中除sign和method以外的所有Body参数均参与签名。  最大长度1024个字符。 |

## 请求示例

```
1. POST /gameservice/api/gbClientApi
2. Host: jos-open-api.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded
4. // 所有请求参数值均需要urlencode编码后再进行拼接
5. method=external.hms.gs.player.unbindPlayer&appId=135***568&cpId=123***21f&teamPlayerId=******&ts=1670841860308&sign=**************
```

## 响应参数

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| rtnCode | 是 | int | 服务端返回码。  -1：响应失败  0：解绑成功  1：验签失败  3001：参数错误  2031002：玩家账号信息错误  2031006：游戏信息错误  2031007：华为玩家账号已绑定其他游戏玩家账号 |
| errMsg | 否 | String | 异常场景下返回错误码的描述。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=UTF-8
3. {
4. "rtnCode":0
5. }
```

## 签名机制

为了确保HTTPS传输的安全性，防止请求参数被篡改，应用需要在调用接口时携带请求参数的签名字符串，用于华为服务器对请求参数进行校验。签名字符串的生成规则如下所示：

1. 将请求参数Body中除**sign**和**method**以外的参数，按参数名首字母的ASCII码将参数升序排序。若遇到相同首字母，则比较第二个字母，以此类推。

   注意

   **sign**和**method**参数不参与签名。
2. 添加依赖项。

   ```
   1. <dependencies>
   2. <dependency>
   3. <groupId>commons-codec</groupId>
   4. <artifactId>commons-codec</artifactId>
   5. <version>1.15</version> <!-- 请使用最新的稳定版本 -->
   6. </dependency>
   7. <dependency>
   8. <groupId>org.bouncycastle</groupId>
   9. <artifactId>bcprov-jdk18on</artifactId>
   10. <version>1.74</version> <!-- 请使用最新的稳定版本 -->
   11. </dependency>
   12. </dependencies>
   ```
3. 将所有参与签名的参数名和参数值的键值对以“&”字符连接成待签名字符串，例如“a=xxxxxx&b=xxxxxxx&c=xxxxxxxxxxx...”。其中，参数值需要进行urlencode。

   Java示例代码如下：

   ```
   1. // 组装body内除sign和method以外的参数，此处参数值仅为示例
   2. Map<String, String> paramsMap = new HashMap<>();
   3. paramsMap.put("appId", "appId");
   4. paramsMap.put("cpId", "cpId");
   5. paramsMap.put("teamPlayerId", "teamPlayerId");
   6. paramsMap.put("ts", "111111111");

   8. // 对参数进行字典序排序
   9. Map<String, String> tempMap = new TreeMap<>(paramsMap);
   10. StringBuffer base = new StringBuffer();

   12. // 拼接参数
   13. for (Map.Entry<String, String> entry : tempMap.entrySet()) {
   14. String key = entry.getKey();
   15. String value = entry.getValue();
   16. base.append(key).append('=').append(null == value ? '' : URLEncoder.encode(value, "UTF-8")).append('&');
   17. }

   19. if (base.length() > 0) {
   20. base.deleteCharAt(base.length() - 1);
   21. }
   ```
4. 将待签名字符串使用游戏私钥按照RSA算法（SHA256WithRSA/PSS）进行签名，将签名后的字符串经过Base64编码，得到的字符串即为签名字符串。

   说明

   * 游戏私钥获取请参见[获取游戏密钥](../harmonyos-guides/gameservice-key.md)。
   * 签名字符串需要进行urlencode后再拼接到请求中。

   Java示例代码如下：

   ```
   1. // 获取签名私钥，具体实现方法由开发者自行决定，此处仅为接口示例
   2. String privateKey = "xxxxxx";

   4. // 加签
   5. byte[] keyBytes = Base64.decodeBase64(privateKey);
   6. PKCS8EncodedKeySpec pkcs8KeySpec = new PKCS8EncodedKeySpec(keyBytes);
   7. KeyFactory keyFactory = KeyFactory.getInstance("RSA");
   8. PrivateKey privateK =  keyFactory.generatePrivate(pkcs8KeySpec);
   9. Signature signature = Signature.getInstance("SHA256withRSA/PSS", new BouncyCastleProvider());
   10. signature.initSign(privateK);
   11. signature.update(base.getBytes(StandardCharsets.UTF_8));
   12. String sign =  Base64.encodeBase64String(signature.sign());
   ```
