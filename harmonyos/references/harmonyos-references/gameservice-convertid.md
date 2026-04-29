---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-convertid
title: 转换ID
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > REST API > 转换ID
category: harmonyos-references
scraped_at: 2026-04-29T14:07:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:15c822ac12783f21ae6860bf39df298c6acc8127c48f5d9b95d8b7084a196154
---

## 功能介绍

调用该接口，传入Access Token、APP ID、gamePlayerId到华为服务器上获取HarmonyOS 4及以下游戏的玩家playerId、openId、unionId信息。

## 场景描述

通过Access Token、APP ID、gamePlayerId信息到华为服务器上查询HarmonyOS 4及以下游戏的玩家playerId、openId、unionId信息。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为游戏服务器
* **接口URL**：<https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi>

  说明

  请使用TLS 1.2协议或以上版本。
* **数据格式**：

  + 请求：Content-Type: application/x-www-form-urlencoded（表单方式）
  + 响应：Content-Type: application/json

## 请求参数

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| method | 是 | String | 固定传入“external.hms.gs.player.transfer.convertId”。 |
| accessToken | 是 | String | 游戏调用华为账号的[获取用户级凭证](account-api-obtain-user-token.md)接口获取到的Access Token。 |
| appId | 是 | String | HarmonyOS 5.0及以上游戏的APP ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 |
| gamePlayerId | 是 | String | HarmonyOS 5.0及以上游戏的玩家标识，通过调用[unionLogin](gameservice-gameplayer.md#gameplayerunionlogin)接口返回。 |

## 请求示例

```
1. POST /gameservice/api/gbClientApi HTTP/1.1
2. Content-Type: application/x-www-form-urlencoded
3. User-Agent: PostmanRuntime/7.24.0
4. Accept: */*
5. Host: jos-open-api.cloud.huawei.com
6. Accept-Encoding: gzip, deflate, br
7. Connection: keep-alive
8. Content-Length: 717
9. // 所有请求参数值均需要urlencode编码后再进行拼接
10. method=external.hms.gs.player.transfer.convertId&accessToken=******&appId=xxxxxxx&gamePlayerId=xxxxxxx
```

## 响应参数

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| rtnCode | 是 | int | 服务端结果说明。  0：获取成功。  -1：获取失败。  2：accessToken无效。  3001：参数错误。表示缺失请求参数或格式错误。  3101：应用ID与鉴权应用不一致。 |
| playerId | 是 | String | 在HarmonyOS 4及以下系统，华为游戏服务器给华为账号封装处理后的对外开放的游戏玩家标识。 |
| openId | 是 | String | 在HarmonyOS 4及以下系统，由华为账号和应用唯一标识组合加密起来的玩家标识。 |
| unionId | 否 | String | 在HarmonyOS 4及以下系统，由华为账号和开发者账号组合加密起来的玩家标识。 |
| errMsg | 否 | String | 异常场景下返回错误码的描述。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Date: Tue, 19 May 2023 06:28:02 GMT
3. Content-Type: application/json; charset=utf-8
4. Transfer-Encoding: chunked
5. Connection: keep-alive
6. Content-Encoding: gzip
7. Server: elb
8. {
9. "playerId": "13423***9864303",
10. "openId": "43JIOdok743***980sd9453",
11. "unionId": "MDFiaNicx***JHIicHAlnRD",
12. "rtnCode": 0
13. }
```

## 调用示例

```
1. Java
2. package okhttp.com.post;
3. import com.alibaba.fastjson.JSONObject;
4. import okhttp3.*;
5. import java.io.IOException;

7. public class ConvertIdTest {
8. private static Integer RETURN_CODE_SUCCEED = 0;

10. /**
11. * 接口本地调测时使用
12. */
13. public static void main(String[] args) {
14. String method = "external.hms.gs.player.transfer.convertId"; // 固定传入“external.hms.gs.player.transfer.convertId”
15. String accessToken = "xxxxx"; // 请使用客户端Player对象中的Access Token
16. String appId = "xxxx"; // HarmonyOS 5.0及以上游戏的APP ID
17. String gamePlayerId = "xxxxx"; // 通过Access Token到华为服务器上获取到的玩家gamePlayerId
18. convertIdService(method, accessToken,appId, gamePlayerId);
19. }

21. private static void convertIdService(String method, String accessToken, String appId, String gamePlayerId) {
22. OkHttpClient client = new OkHttpClient().newBuilder().build();
23. RequestBody mFormBody = new FormBody.Builder().add("method", method)
24. .add("accessToken", accessToken)
25. .add("appId", appId)
26. .add("gamePlayerId", gamePlayerId)
27. .build();
28. Request request = new Request.Builder().url("https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi")
29. .post(mFormBody)
30. .build();
31. try {
32. Response response = client.newCall(request).execute();
33. if (response.isSuccessful()) {
34. JSONObject object = JSONObject.parseObject(response.body().string());
35. if (RETURN_CODE_SUCCEED.equals(object.get("rtnCode"))) {
36. System.out.println("playerId: " + object.get("playerId"));
37. System.out.println("openId: " + object.get("openId"));
38. System.out.println("unionId: " + object.get("unionId"));
39. } else {
40. System.out.println("rtnCode: " + object.get("rtnCode"));
41. System.out.println("rtnMsg: " + object.get("errMsg"));
42. }
43. }
44. } catch (IOException e) {
45. e.printStackTrace();
46. }
47. }
48. }
```

```
1. C#
2. using System;
3. using System.IO;
4. using System.Net;
5. using System.Text;
6. using System.Web;
7. namespace cXdemo
8. {
9. class Program
10. {
11. static void Main(string[] args)
12. {
13. // 固定传入“external.hms.gs.player.transfer.convertId”
14. string method = "external.hms.gs.player.transfer.convertId";
15. // 请使用客户端Player对象中的Access Token
16. string accessToken = "xxxxx";
17. // HarmonyOS 5.0及以上游戏的APP ID
18. string appId = "xxxx";
19. // 通过Access Token到华为服务器上获取到的玩家gamePlayerId
20. string gamePlayerId = "xxxxx";
21. // 请求接口
22. requestgameInfo(method, accessToken, appId, gamePlayerId);
23. }
24. static void requestgameInfo(string method, string accessToken, string appId, string gamePlayerId)
25. {
26. var requestUrl = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi";
27. HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
28. request.Method = "post";
29. request.ContentType = "application/x-www-form-urlencoded";
30. StringBuilder data = new StringBuilder();
31. data.Append("method=" + HttpUtility.UrlEncode(method));
32. data.Append("&accessToken=" + HttpUtility.UrlEncode(accessToken));
33. data.Append("&appId=" + HttpUtility.UrlEncode(appId));
34. data.Append("&gamePlayerId=" + HttpUtility.UrlEncode(gamePlayerId));
35. byte[] byteData = Encoding.UTF8.GetBytes(data.ToString());
36. request.ContentLength = byteData.Length;
37. Stream postStream = request.GetRequestStream();
38. postStream.Write(byteData, 0, byteData.Length);
39. postStream.Close();
40. WebResponse response = request.GetResponse();
41. StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
42. string strJson = reader.ReadToEnd();
43. Console.WriteLine(strJson);
44. reader.Close();
45. response.Close();
46. }
47. }
48. }
```

```
1. PHP
2. class convert_id
3. {
4. /**
5. * 根据AccessToken获取玩家信息
6. *
7. * @param string $method 固定传入“external.hms.gs.player.transfer.convertId”
8. * @param string $accessToken 请使用客户端Player对象中的Access Token
9. * @param string $appId HarmonyOS 5.0及以上游戏的APP ID
10. * @param string $gamePlayerId 通过Access Token到华为服务器上获取到的玩家gamePlayerId
11. */
12. public function call_https(string $method, string $accessToken, string $appId, string $gamePlayerId): void
13. {
14. $data = array("method" => $method, "accessToken" => $accessToken, "appId" => $appId, "gamePlayerId" => $gamePlayerId);
15. $curl = curl_init();
16. curl_setopt_array($curl, array(
17. CURLOPT_URL => 'https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi',
18. CURLOPT_RETURNTRANSFER => true,
19. CURLOPT_ENCODING => '',
20. CURLOPT_MAXREDIRS => 10,
21. CURLOPT_TIMEOUT => 0,
22. CURLOPT_FOLLOWLOCATION => true,
23. CURLOPT_CUSTOMREQUEST => 'POST',
24. CURLOPT_SSL_VERIFYHOST => false,
25. CURLOPT_SSL_VERIFYPEER => false,
26. CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
27. CURLOPT_POSTFIELDS => http_build_query($data),
28. CURLOPT_HTTPHEADER => array(
29. 'Content-Type: application/x-www-form-urlencoded'
30. ),
31. ));
32. $response = curl_exec($curl);
33. if (curl_error($curl)) {
34. throw new Exception(curl_error($curl));
35. }
36. curl_close($curl);
37. $result = json_decode($response, true);
38. var_dump($result);
39. }
40. }
41. $convert_id = new convert_id();
42. $method = "external.hms.gs.player.transfer.convertId"; // 固定传入“external.hms.gs.player.transfer.convertId”
43. $accessToken = "xxxxx"; // 请使用客户端Player对象中的Access Token
44. $appId = "xxxxx"; // HarmonyOS 5.0及以上游戏的APP ID
45. $gamePlayerId = "xxxxx"; // 通过Access Token到华为服务器上获取到的玩家gamePlayerId
46. $convert_id->call_https($method, $accessToken, $appId, $gamePlayerId);
```

```
1. Python
2. from typing import Any
3. import requests
4. import urllib.parse
5. class ConvertIdSolution:
6. def convert_id(self, method, accessToken, appId, gamePlayerId):
7. url = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi"
8. params: dict[str, Any] = {
9. 'method': method,
10. 'accessToken': accessToken,
11. 'appId': appId,
12. 'gamePlayerId': gamePlayerId
13. }
14. encodedParams = urllib.parse.urlencode(params)
15. headers = {
16. 'Content-Type': 'application/x-www-form-urlencoded'
17. }
18. response = requests.post(url, headers=headers, data=encodedParams)
19. print(response.text)
20. if __name__ == "__main__":
21. # 固定传入“external.hms.gs.player.transfer.convertId”
22. input_method = 'external.hms.gs.player.transfer.convertId'
23. # 请使用客户端Player对象中的Access Token
24. input_accessToken = 'xxx'
25. # HarmonyOS 5.0及以上游戏的APP ID
26. input_appId = 'xxx'
27. # 通过Access Token到华为服务器上获取到的玩家gamePlayerId
28. input_gamePlayerId = 'xxx'
29. function = ConvertIdSolution()
30. function.convert_id(input_method, input_accessToken, input_appId, input_gamePlayerId)
```
