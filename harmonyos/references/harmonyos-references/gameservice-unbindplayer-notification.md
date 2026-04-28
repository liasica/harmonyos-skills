---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-unbindplayer-notification
title: 解绑账号通知
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > REST API > 解绑账号通知
category: harmonyos-references
scraped_at: 2026-04-28T08:16:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e9924ee73b45d8fa7c47ca1112381caca94006fad4f6611eaecb0c7bb75f785
---

## 功能介绍

华为游戏服务器调用此接口向开发者服务器发送关键事件通知，并提醒开发者解绑账号。

## 场景描述

在AppGallery Connect[配置回调地址](../harmonyos-guides/gameservice-address.md)后，华为游戏服务器将在玩家注销华为账号后提醒开发者解绑账号。若开发者服务器返回结果为非成功响应，华为游戏服务器将周期性发送本次关键事件的通知，建议开发者服务端在收到通知后立即返回成功响应，避免堆积通知消息。

说明

为保证可靠性，系统具备补偿机制，所以可能出现重发的通知比预期的多。

## 接口约束

* 不建议开发者服务器限制IP，否则华为游戏服务器的出口IP发生变化后，可能会引起服务中断。
* 需提前在AppGallery Connect中配置回调地址，地址要求支持HTTPS协议，且具有合法商用证书。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：华为游戏服务器 -> 开发者服务器
* **性能指标**：TPS>50
* **最大响应时间**：<1s
* **接口URL**：在AppGallery Connect配置的回调地址。
* **数据格式**：

  + 请求消息：Content-Type: application/json
  + 响应消息：Content-Type: application/json

## 请求参数

**body参数**

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| appIds | 否 | List<String> | 待解绑游戏的APP ID列表：  - 若是开发者级别绑定，则为绑定发起的APP。  - 若是游戏级别绑定，则为绑定涉及的APP。 |
| teamPlayerId | 是 | String | 华为teamPlayerId。  最大长度256个字符。 |
| sign | 是 | String | 华为服务器在发送请求时对除sign以外的所有Body参数使用SHA256WithRSA/PSS算法进行了签名，并在sign参数中返回签名后的字符串。  开发者需获取验签公钥，并根据加密算法使用公钥对签名字符串进行验签，验签方法参见[验签机制](gameservice-unbindplayer-notification.md#验签机制)。  **说明**：本参数在"utf-8" urlencode后发送。如果使用的是Java中request的getParameter()方法，则无需进行urlencode。 |

## 请求示例

```
1. POST {接口url}
2. Host: xxx
3. Content-Type: application/json
4. {
5. "appIds": ["109***688", "691***237"],
6. "teamPlayerId": "E5B*****************E9B",
7. "sign": "J0Eslg0p***tKR37AB"
8. }
```

## 响应参数

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| result | 是 | int | 服务端返回码。  0：成功  1：验签失败  2：超时  3：业务信息错误  94：系统错误  95：IO 错误  96：错误的url  97：错误的响应  98：参数错误  99：其他错误 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=UTF-8
3. {
4. "result": 0
5. }
```

## 验签机制

1. 获取请求中的签名字符串，即sign参数。
2. 将请求参数Body中除sign以外的参数，按参数名首字母的ASCII码将参数升序排序。若遇到相同首字母，则比较第二个字母，以此类推。
3. 排序完成之后，将所有参与签名的参数值进行urlencode之后以“&”字符连接成字符串，例如“a=xxxxxx&b=xxxxxxx&c=xxxxxx”，此字符串便是待验签字符串。
4. 将待验签字符串使用游戏公钥按照RSA算法（SHA256WithRSA/PSS）进行签名，并与sign参数中的签名字符串进行一致性验证。

   说明

   游戏公钥获取请参见[获取游戏密钥](../harmonyos-guides/gameservice-key.md)。

   Java示例代码如下：

   ```
   1. // List、Map等基本类型的导包均由JDK自带，其它导包由业务侧自定义导入
   2. // 组装body内的参数，此处参数值仅为示例
   3. List<String> appIds =  Arrays.asList("appId1","appId2");
   4. Map<String, String> paramsMap = new HashMap<>();
   5. paramsMap.put("appIds", StringUtils.join(appIds, ","));
   6. paramsMap.put("teamPlayerId", "teamPlayerId");

   8. // 对参数进行字典序排序
   9. Map<String, String> tempMap = new TreeMap<>(paramsMap);
   10. // 拼接参数
   11. StringBuffer base = new StringBuffer();
   12. for (Map.Entry<String, String> entry : tempMap.entrySet()) {
   13. String key = entry.getKey();
   14. String value = entry.getValue();
   15. base.append(key).append('=').append(null == value ? "" : URLEncoder.encode(value, "UTF-8")).append('&');
   16. }
   17. String signStr = "";
   18. if (base.length() > 0) {
   19. signStr = base.deleteCharAt(base.length() - 1).toString();
   20. }

   22. // 获取验签公钥，具体实现方法由开发者自行决定，此处仅为接口示例
   23. String publicKey = "xxx";
   24. String sign = "sign";

   26. // 验签
   27. byte[] keyBytes = Base64.decodeBase64(publicKey);
   28. X509EncodedKeySpec pkcs8KeySpec = new X509EncodedKeySpec(keyBytes);
   29. KeyFactory keyFactory = KeyFactory.getInstance("RSA");
   30. PublicKey publicK = keyFactory.generatePublic(pkcs8KeySpec);
   31. Signature signature = Signature.getInstance("SHA256WithRSA/PSS", new BouncyCastleProvider());
   32. signature.initVerify(publicK);
   33. signature.update(signStr.getBytes("UTF-8"));
   34. signature.verify(Base64.decodeBase64(sign));
   ```
