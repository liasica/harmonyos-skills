---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-teamplayerid
title: 批量转换teamPlayerId
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > REST API > 批量转换teamPlayerId
category: harmonyos-references
scraped_at: 2026-04-28T08:16:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e8741f6509b02c32ffcd192c0863c8809ae05558a400618584b293d3517e7588
---

## 功能介绍

华为开发者联盟上的游戏从一个账号转移到另一个账号进行维护，该游戏资产归属于转入方。

转出方/转入方可以调用此接口，向华为服务器批量提交转让前游戏关联的玩家标识teamPlayerId等信息，批量获取游戏转让后对应的teamPlayerId等信息。

## 接口约束

* 调用此接口前，请确保转出方/转入方已完成[游戏转移](../app/game-center-transferring-0000001194325290.md)，否则均将无权转换teamPlayerId。
* 单次接口请求最多可以获取1000条teamPlayerId数据。
* 请勿频繁调用此接口，调用的时间间隔请控制在3秒以上。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为游戏服务器
* **接口URL**：

  + 中国站点：<https://connect-api.cloud.huawei.com/api/jas/open/players/player-accounts/team-player/convert>

    说明

    调用[获取Token](../AppGallery-connect-References/agcapi-obtain_token-0000001158365043.md)接口时使用的域名需与本接口域名保持一致，例如本接口使用“connect-api.cloud.huawei.com”，则调用[获取Token](../AppGallery-connect-References/agcapi-obtain_token-0000001158365043.md)接口需使用“https://connect-api.cloud.huawei.com/api/jas/open/players/player-accounts/team-player/convert”。
* **数据格式**：

  + 请求：Content-Type: application/json
  + 响应：Content-Type: application/json

## 请求参数

### Header

| 参数名称 | 是否必选 | 类型 | 参数说明 |
| --- | --- | --- | --- |
| client\_id | 是 | String | 用于鉴权的客户端ID，获取方法参考[创建API客户端](../AppGallery-connect-Guides/agcapi-getstarted-0000001111845114.md#section103mcpsimp)。 |
| Authorization | 是 | String | 认证信息，格式为“Authorization: Bearer ${access\_token}”。access\_token为[获取Token](../AppGallery-connect-References/agcapi-obtain_token-0000001158365043.md)中获取的access\_token。 |
| appId | 是 | String | 游戏APP ID，获取方法参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 |

### Body

请求Body中使用JSON格式携带更相关信息，参数如下表所示。

| 参数名称 | 是否必选 | 类型 | 参数说明 |
| --- | --- | --- | --- |
| srcCpId | 是 | Long | 游戏转出方的开发者Developer ID，获取方法参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 |
| dstCpId | 是 | Long | 游戏转入方的开发者Developer ID，获取方法参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 |
| teamPlayerIds | 是 | List<String> | 转让前，游戏的玩家标识teamPlayerId列表，列表数量至少1条，至多不超过1000条。  建议开发者做好去重工作，确保teamPlayerId列表不要有重复的信息。 |

## 请求示例

```
1. POST  HTTP/1.1
2. Host: connect-api.cloud.huawei.com
3. Content-Type: application/json
4. client_id: 41******7168
5. appId: "*****"
6. Authorization: Bearer ******
7. {
8. "srcCpId": 4130****71055,
9. "dstCpId": 4008****74585,
10. "teamPlayerIds":[
11. "**********",
12. "**********",
13. "**********"
14. ]
15. }
```

## 响应参数

| 参数名称 | 是否必选 | 类型 | 参数说明 |
| --- | --- | --- | --- |
| ret | 是 | JosRet | 包含返回码及描述信息的JSON字符串，格式为{"code":retcode, "msg": "description"}，retcode为返回码，description为返回码描述信息。 |
| data | 是 | List<ConvertTeamPlayerIdItem> | 单次接口请求任务的查询结果。 |

* JosRet

  | 参数名称 | 是否必选 | 类型 | 参数说明 |
  | --- | --- | --- | --- |
  | code | 是 | int | 单次接口请求任务的结果返回码：  0：请求成功。  -1：请求失败。  3002：鉴权错误。 |
  | msg | 否 | String | 失败时的描述信息。 |
* ConvertTeamPlayerIdItem

  | 参数名称 | 是否必选 | 类型 | 参数说明 |
  | --- | --- | --- | --- |
  | srcCpId | 是 | Long | 游戏转出方的开发者Developer ID。 |
  | srcTeamPlayerId | 是 | String | 转让前，游戏的玩家标识teamPlayerId。 |
  | dstCpId | 是 | Long | 游戏转入方的开发者Developer ID。 |
  | dstTeamPlayerId | 是 | String | 转让后，游戏的玩家标识teamPlayerId。 |
  | errCode | 是 | int | 查询单个teamPlayerId的结果返回码：  0：成功。  -1：失败。 |

## 响应示例

```
1. {
2. "ret": {
3. "code": 0,
4. "msg": "string"
5. },
6. "data": [
7. {
8. "srcCpId": 4330****71055,
9. "srcTeamPlayerId": "******",
10. "dstCpId": 4130****71055,
11. "dstTeamPlayerId": "*****",
12. "errCode": 0
13. }
14. ]
15. }
```

## 调用示例

```
1. Java
2. /**
3. * 批量转换teamPlayerId
4. *
5. * @param domain 请根据您的服务器部署地就近选择对应站点的URL，与获取token时使用的domain保持一致
6. * @param client_id 用于鉴权的客户端ID
7. * @param token post认证请求的token
8. * @param teamPlayerIds 需要查询的teamPlayerId列表
9. * @param appId 游戏appId
10. */
11. private static void batchGetOpenIds(String domain, String client_id, String token, List<String> teamPlayerIds, String appId) {
12. try {
13. // 接口URL，domain请根据您的服务器部署地就近选择对应站点的URL且与获取token时使用的domain保持一致
14. HttpPost post = new HttpPost(domain + "/api/jas/open/players/player-accounts/team-player/convert");
15. // 构造消息头
16. post.setHeader("Authorization", "Bearer " + token);
17. post.setHeader("client_id", client_id);
18. post.setHeader("appId", appId);
19. // 构造消息实体
20. JSONObject keyString = new JSONObject();
21. keyString.put("srcCpId", srcCpId);
22. keyString.put("dstCpId", dstCpId);
23. keyString.put("teamPlayerId", teamPlayerIds); // 原主体的teamPlayerId
24. StringEntity entity = new StringEntity(keyString.toString(), Charset.forName("UTF-8"));
25. entity.setContentEncoding("UTF-8");
26. // 发送Json格式的数据请求
27. entity.setContentType("application/json");
28. post.setEntity(entity);
29. CloseableHttpClient httpClient = HttpClients.createDefault();
30. HttpResponse response = httpClient.execute(post);
31. int statusCode = response.getStatusLine().getStatusCode();
32. if (statusCode == HttpStatus.SC_OK) {
33. BufferedReader br =
34. new BufferedReader(new InputStreamReader(response.getEntity().getContent(), Consts.UTF_8));
35. String result = br.readLine();
36. System.out.println(result);
37. JSONObject object = JSON.parseObject(result);
38. }
39. post.releaseConnection();
40. httpClient.close();
41. } catch (Exception e) {
42. System.out.println(e.getMessage());
43. }
44. }
```

```
1. C#
2. /**
3. * 批量转换teamPlayerId
4. *
5. * @param domain 请根据您的服务器部署地就近选择对应站点的URL，与获取token时使用的domain保持一致
6. * @param clientId 用于鉴权的客户端ID
7. * @param token post认证请求的token
8. * @param teamPlayerIds 转让前游戏的玩家标识teamPlayerId列表
9. * @param appId 游戏appId
10. * @Param srcCpId 游戏转出方的开发者Developer ID
11. * @Param dstCpId 游戏转入方的开发者Developer ID
12. */
13. static void convertTeamPlayerId(string domain, string clientId, string token, List<string> teamPlayerIds, string appId, long srcCpId, long dstCpId)
14. {
15. try
16. {
17. // 接口URL，domain请根据您的服务器部署地就近选择对应站点的URL且与获取token时使用的domain保持一致
18. var requestUrl = domain + "/api/jas/open/players/player-accounts/team-player/convert";
19. HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
20. request.Method = "post";
21. request.ContentType = "application/json";
22. request.Headers.Add("client_id", clientId);
23. request.Headers.Add("Authorization", "Bearer " + token);
24. request.Headers.Add("appId", appId);
25. Dictionary<string, object> dic = new Dictionary<string, object>
26. {
27. {"srcCpId", srcCpId},
28. {"dstCpId", dstCpId},
29. {"teamPlayerIds", teamPlayerIds}
30. };
31. string sendData = JsonConvert.SerializeObject(dic, Formatting.Indented);
32. Console.WriteLine(sendData);
33. byte[] byteData = Encoding.GetEncoding("utf-8").GetBytes(sendData);
34. request.ContentLength = byteData.Length;
35. Stream postStream = request.GetRequestStream();
36. postStream.Write(byteData, 0, byteData.Length);
37. postStream.Close();
38. WebResponse response = request.GetResponse();
39. StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
40. string strJson = reader.ReadToEnd();
41. Console.WriteLine(strJson);
42. reader.Close();
43. response.Close();
44. }
45. catch (Exception e)
46. {
47. Console.WriteLine(e.ToString());
48. }
49. }
```

```
1. PHP
2. /**
3. * 批量转换teamPlayerId
4. *
5. * @param string $domain 请根据您的服务器部署地就近选择对应站点的URL，与获取token时使用的domain保持一致
6. * @param string $client_id 用于鉴权的客户端ID
7. * @param string $token post认证请求的token
8. * @param array $teamPlayerIds 转让前游戏的玩家标识teamPlayerId列表
9. * @param string $appId 游戏appid
10. * @Param long $srcCpId 游戏转出方的开发者Developer ID
11. * @Param long $dstCpId 游戏转入方的开发者Developer ID
12. * @throws Exception
13. */
14. public function batch_convert_teamPlayerIds(string $domain, string $client_id, string $token, array $teamPlayerIds, string $appId, long $srcCpId, long $dstCpId)
15. {
16. $curl = curl_init();
17. $data = array("teamPlayerIds" => $teamPlayerIds, "srcCpId" => $srcCpId, "dstCpId" => $dstCpId);
18. curl_setopt_array($curl, array(
19. CURLOPT_URL => $domain . '/api/jas/open/players/player-accounts/team-player/convert',
20. CURLOPT_RETURNTRANSFER => true,
21. CURLOPT_ENCODING => '',
22. CURLOPT_MAXREDIRS => 10,
23. CURLOPT_TIMEOUT => 0,
24. CURLOPT_FOLLOWLOCATION => true,
25. CURLOPT_SSL_VERIFYHOST => false,
26. CURLOPT_SSL_VERIFYPEER => false,
27. CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
28. CURLOPT_CUSTOMREQUEST => 'POST',
29. CURLOPT_POSTFIELDS => json_encode($data),
30. CURLOPT_HTTPHEADER => array(
31. 'client_id: ' . $client_id,
32. 'Authorization: Bearer ' . $token,
33. 'Content-Type: application/json',
34. 'appId: ' . $appId
35. ),
36. ));
37. $response = curl_exec($curl);
38. if (curl_error($curl)) {
39. throw new Exception(curl_error($curl));
40. }
41. curl_close($curl);
42. $result = json_decode($response, true);
43. var_dump($result);
44. }
```

```
1. Python
2. from getToken import *
3. class BatchConvertTeamPlayerIdsSolution:
4. @staticmethod
5. def batch_convert_team_player_ids(domain, client_id, access_token, team_player_id, app_id, src_cp_id, dst_cp_id):
6. url = domain + '/api/jas/open/players/player-accounts/team-player/convert'
7. data = {"teamPlayerIds": team_player_id, "srcCpId": src_cp_id， "dstCpId": dst_cp_id}
8. payload = json.dumps(data)
9. headers = {
10. 'client_id': client_id,
11. 'Authorization': 'Bearer ' + access_token,
12. 'Content-Type': 'application/json',
13. 'appId': app_id
14. }
15. response = requests.request("POST", url, headers=headers, data=payload)
16. print(response.text)
17. if __name__ == "__main__":
18. # 请根据您的服务器部署地就近选择对应站点的URL，这里以中国站点域名为例
19. input_domain = 'https://connect-api.cloud.huawei.com'
20. # 客户端ID
21. input_client_id = 'xxxxxxx'
22. # 客户端密钥
23. input_client_secret = 'xxxxxxxx'
24. # 获取token
25. token_function = GetToken()
26. input_access_token = token_function.get_token(input_domain, input_client_id, input_client_secret)
27. # 游戏appId
28. input_app_id = 'xxxxx'
29. # 需要转换的teamPlayerIds列表，单次最大不要超过1000个，这里以2个为例
30. input_player_Ids = ['xxxxxxx', 'xxxxxx']
31. # 游戏转出方的开发者Developer ID
32. input_src_cp_id = 111111
33. # 游戏转入方的开发者Developer ID
34. input_dst_cp_id = 222222
35. batch_function = BatchGetOpenIdsSolution()
36. batch_function.batch_convert_team_player_ids(input_domain, input_client_id, input_access_token, input_player_Ids, input_app_id, input_src_cp_id, input_dst_cp_id)
```
