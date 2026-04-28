---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-getplayerinfo
title: 获取玩家标识
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > REST API > 获取玩家标识
category: harmonyos-references
scraped_at: 2026-04-28T08:16:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be7374d9ce09db682407b481ea64b7b307aac536b0399b381c0d379445f56a0c
---

## 功能介绍

* 调用该接口，对已经获得的Access Token进行鉴权。
* 传入Access Token到华为服务器上获取玩家的gamePlayerId、teamPlayerId等信息。

## 场景描述

游戏已经获取到Access Token，要对其进行解析鉴权，通过Access Token到华为服务器上获取玩家的gamePlayerId、teamPlayerId等信息。

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
| method | 是 | String | 固定传入“external.hms.gs.getPlayerInfo”。 |
| accessToken | 是 | String | 游戏调用华为账号的[获取用户级凭证](account-api-obtain-user-token.md)接口获取到的Access Token。 |

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
10. method=external.hms.gs.getPlayerInfo&accessToken=******
```

## 响应参数

| 参数 | 是否必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| rtnCode | 是 | int | 服务端结果说明：  0：获取成功  -1：获取失败  2：accessToken无效  3001：参数错误 |
| acctInfo | 否 | LoginAcctInfo | 玩家标识信息，获取成功时返回。 |
| bindInfo | 是 | BindPlayerInfo | 与华为PlayerId绑定的游戏官方账号信息。 |
| errMsg | 否 | String | 异常场景下返回错误码的描述。 |

* LoginAcctInfo

  | 参数 | 是否必选 | 类型 | 描述 |
  | --- | --- | --- | --- |
  | gamePlayerAcct | 否 | PlayerAcct | gamePlayerId信息。转移场景默认返回gamePlayerId。 |
  | teamPlayerAcct | 否 | PlayerAcct | teamPlayerId信息。绑定场景默认返回teamPlayerId。 |

  + PlayerAcct

    | 参数 | 是否必选 | 类型 | 描述 |
    | --- | --- | --- | --- |
    | id | 是 | String | 玩家标识ID。 |
    | compatibleType | 是 | int | 兼容类型。  0：gamePlayerId与openId、playerId不兼容，即调用[getLocalPlayer](gameservice-gameplayer.md#gameplayergetlocalplayer)接口时，玩家首次登录游戏生成的玩家标识；teamPlayerId与unionId不兼容，即调用[unionLogin](gameservice-gameplayer.md#gameplayerunionlogin)接口时，玩家首次登录游戏未选择转移APK游戏数据生成的玩家标识。  1：gamePlayerId兼容playerId，即玩家首次登录游戏时选择转移APK游戏数据，且APK游戏使用了playerId作为玩家标识，Game Service Kit将playerId作为新的gamePlayerId。  2：gamePlayerId兼容openId，即玩家首次登录游戏时选择转移APK游戏数据，且APK游戏使用了openId作为玩家标识，Game Service Kit将openId作为新的gamePlayerId。 |
    | idType | 是 | int | 玩家标识ID类型。  1：gamePlayerId  2：teamPlayerId |
    | bindType | 是 | int | 是否可绑定游戏官方账号。  0：不可绑定  1：可绑定 |
* BindPlayerInfo

  | 参数 | 是否必选 | 类型 | 描述 |
  | --- | --- | --- | --- |
  | bindMode | 否 | int | 绑定模式：  0：开发者级别。  1：游戏级别。 |
  | thirdOpenId | 否 | String | 游戏官方账号ID。 |

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
9. "acctInfo": {
10. "gamePlayerAcct": {
11. "id": "B7******5E",
12. "compatibleType": 0,
13. "idType": 1,
14. "bindType": 0
15. }
16. },
17. "bindInfo":{
18. "bindMode": 0,
19. "thirdOpenId": "u_123***9ab"
20. },
21. "rtnCode": 0
22. }
```

## 调用示例

```
1. Java
2. package okhttp.com.post;
3. import com.alibaba.fastjson.JSONObject;
4. import okhttp3.*;
5. import java.io.IOException;
6. public class GetTokenInfoTest {
7. private static Integer RETURN_CODE_SUCCEED = 0;
8. /**
9. * 接口本地调测使用
10. */
11. public static void main(String[] args) {
12. String method = "external.hms.gs.getPlayerInfo"; // 固定传入
13. String accessToken= "xxxx"; // 请使用游戏客户端调用账号获取到的AccessToken
14. getPlayerInfoService(method, accessToken);
15. }
16. /**
17. * 根据AccessToken获取玩家标识信息
18. *
19. * @param method 固定传入“external.hms.gs.getPlayerInfo”
20. * @param accessToken 游戏客户端调用账号获取到的AccessToken
21. */
22. private static void getPlayerInfoService(String method, String accessToken) {
23. OkHttpClient client = new OkHttpClient().newBuilder().build();
24. RequestBody mFormBody = new FormBody.Builder().add("method", method)
25. .add("accessToken", accessToken)
26. .build();
27. Request request = new Request.Builder().url("https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi")
28. .post(mFormBody)
29. .build();
30. try {
31. Response response = client.newCall(request).execute();
32. if (response.isSuccessful()) {
33. JSONObject object = JSONObject.parseObject(response.body().string());
34. if (RETURN_CODE_SUCCEED.equals(object.get("rtnCode")) && object.get("acctInfo") != null) {
35. JSONObject acctInfo = JSONObject.parseObject(object.get("acctInfo").toString());
36. if (acctInfo != null){
37. if (acctInfo.get("gamePlayerAcct") != null) {
38. JSONObject gamePlayerAcct = JSONObject.parseObject(acctInfo.get("gamePlayerAcct").toString());
39. System.out.println("gamePlayerId: " + gamePlayerAcct.get("id"));
40. System.out.println("gamePlayer compatibleType: " + gamePlayerAcct.get("compatibleType"));
41. }
42. if (acctInfo.get("teamPlayerAcct") != null) {
43. JSONObject teamPlayerAcct = JSONObject.parseObject(acctInfo.get("teamPlayerAcct").toString());
44. System.out.println("teamPlayerId: " + teamPlayerAcct.get("id"));
45. System.out.println("teamPlayer compatibleType: " + teamPlayerAcct.get("compatibleType"));
46. }
47. }
48. JSONObject bindInfo = JSONObject.parseObject(object.get("bindInfo").toString());
49. if (bindInfo != null) {
50. System.out.println("bindMode: " + bindInfo.get("bindMode"));
51. System.out.println("thirdOpenId: " + bindInfo.get("thirdOpenId"));
52. }
53. } else {
54. System.out.println("rtnCode: " + object.get("rtnCode"));
55. System.out.println("rtnMsg: " + object.get("errMsg"));
56. }
57. }
58. } catch (IOException e) {
59. e.printStackTrace();
60. }
61. }
62. }
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
13. // 固定传入“external.hms.gs.getPlayerInfo”
14. string method = "external.hms.gs.getPlayerInfo";
15. // 取自当前玩家的Player对象中获取到的Access Token
16. string accessToken = "xxxxx";
17. // 请求接口
18. requestgameInfo(method, accessToken);
19. }
20. static void requestgameInfo(string method, string accessToken)
21. {
22. var requestUrl = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi";
23. HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
24. request.Method = "post";
25. request.ContentType = "application/x-www-form-urlencoded";
26. StringBuilder data = new StringBuilder();
27. data.Append("method=" + HttpUtility.UrlEncode(method));
28. data.Append("&accessToken=" + HttpUtility.UrlEncode(accessToken));
29. byte[] byteData = Encoding.UTF8.GetBytes(data.ToString());
30. request.ContentLength = byteData.Length;
31. Stream postStream = request.GetRequestStream();
32. postStream.Write(byteData, 0, byteData.Length);
33. postStream.Close();
34. WebResponse response = request.GetResponse();
35. StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
36. string strJson = reader.ReadToEnd();
37. Console.WriteLine(strJson);
38. reader.Close();
39. response.Close();
40. }
41. }
42. }
```

```
1. PHP
2. class get_token_info
3. {
4. /**
5. * 根据AccessToken获取玩家信息
6. *
7. * @param string $method 固定传入“external.hms.gs.getPlayerInfo”
8. * @param string $accessToken 请使用客户端Player对象中的AccessToken
9. */
10. public function call_https(string $method, string $accessToken): void
11. {
12. $data = array("method" => $method, "accessToken" => $accessToken);
13. $curl = curl_init();
14. curl_setopt_array($curl, array(
15. CURLOPT_URL => 'https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi',
16. CURLOPT_RETURNTRANSFER => true,
17. CURLOPT_ENCODING => '',
18. CURLOPT_MAXREDIRS => 10,
19. CURLOPT_TIMEOUT => 0,
20. CURLOPT_FOLLOWLOCATION => true,
21. CURLOPT_CUSTOMREQUEST => 'POST',
22. CURLOPT_SSL_VERIFYHOST => false,
23. CURLOPT_SSL_VERIFYPEER => false,
24. CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
25. CURLOPT_POSTFIELDS => http_build_query($data),
26. CURLOPT_HTTPHEADER => array(
27. 'Content-Type: application/x-www-form-urlencoded'
28. ),
29. ));
30. $response = curl_exec($curl);
31. if (curl_error($curl)) {
32. throw new Exception(curl_error($curl));
33. }
34. curl_close($curl);
35. $result = json_decode($response, true);
36. var_dump($result);
37. }
38. }
39. $get_token_info = new get_token_info();
40. $method = "external.hms.gs.getPlayerInfo"; // 固定传入
41. $accessToken = "xxxxx"; // 请使用客户端Player对象中的AccessToken
42. $get_token_info->call_https($method, $accessToken);
```

```
1. Python
2. from typing import Any
3. import requests
4. import urllib.parse
5. class GetTokenInfoSolution:
6. def get_token_info(self, method, accessToken):
7. url = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi"
8. params: dict[str, Any] = {
9. 'method': method,
10. 'accessToken': accessToken
11. }
12. encodedParams = urllib.parse.urlencode(params)
13. headers = {
14. 'Content-Type': 'application/x-www-form-urlencoded'
15. }
16. response = requests.post(url, headers=headers, data=encodedParams)
17. print(response.text)
18. if __name__ == "__main__":
19. # 固定传入“external.hms.gs.getPlayerInfo”
20. input_method = 'external.hms.gs.getPlayerInfo'
21. # 请使用客户端Player对象中的AccessToken
22. input_accessToken = 'xxx'
23. function = GetTokenInfoSolution()
24. function.get_token_info(input_method, input_accessToken)
```
