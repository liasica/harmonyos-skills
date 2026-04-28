---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-getuserrisklevel
title: 获取用户风险等级
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 获取用户信息 > 获取用户风险等级
category: harmonyos-references
scraped_at: 2026-04-28T08:16:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2dfbf2bccb4fded6574e2ef0a74c460d5992a4cee19f5a462b4c4039cfec4856
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

当应用服务端需要[获取风险等级](../harmonyos-guides/account-get-risklevel-introduction.md)时，应用服务端向华为账号服务器调用该接口获取华为账号用户风险等级。

## 场景描述

应用已经通过授权码（Authorization Code）获取到Access Token后，应用获取用户风险等级。

## 使用约束

* 需确保调用端网络正常。
* 应用使用此功能之前，需要完成riskLevel（获取用户风险等级）的scope权限申请，在获取Authorization Code时携带riskLevel（获取用户风险等级）的scope，详见[开发前提](../harmonyos-guides/account-get-risklevel-byquicklogin.md#开发前提)。

说明

应用未申请riskLevel（获取用户风险等级）的scope权限，或获取Authorization Code时未携带riskLevel（获取用户风险等级）的scope，调用接口将返回错误，响应体中errCode=403。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为账号服务器
* **接口URL**：https://account.cloud.huawei.com/user/getuserrisklevel
* **数据格式**：

  请求消息：Content-Type: application/json;charset=utf-8

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-getuserrisklevel.md#示例代码)。 |

### Request Query Parameter

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| clientID | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client ID**参数。 |
| transactionID | 是 | String | 交易流水号，每个消息都需要带该字段；  生成规则：YYYYMMDDhhmmssxxxxxxxxxx，例如： 202502121546232352164151  其中：YYYYMMDDhhmmss：请求产生时间，14位；  xxxxxxxxxx：随机数，可变长，10至20位 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| accessToken | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。获取凭证时Authorization Code需包含riskLevel scope的授权。 |
| scene | 是 | String | 获取用户风险等级的业务场景  - registration：注册  - marketing：营销活动 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /user/getuserrisklevel?clientID=<clientID>&transactionID=<transactionID> HTTP/1.1
2. Host: account.cloud.huawei.com
3. Content-Type: application/json;charset=utf-8

5. {"accessToken":"<Access Token>", "scene":"<scene>"}
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。 |

### Response Body

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| errCode | 是 | Int | 错误码，调用成功时返回0，调用失败时返回对应错误码。 |
| errMsg | 是 | String | 错误描述，调用成功时返回空字符串，调用失败时返回对应描述。 |
| riskLevel | 否 | Int | 请求成功时才会返回风险等级（详见后文附表①）  0：未发现显著风险  1：低风险  2：中风险  3：高风险  4：风险未知 |
| riskTag | 否 | String[] | 风险标签（详见后文附表②） |

附表①: 风险等级含义与建议处置方案

| **等级** | **含义** | **建议处置方案** |
| --- | --- | --- |
| 0 | 未发现显著风险项。例如通过合法途径注册，正常使用华为手机，无批量操作、使用自动机、养号等异常行为的场景。 | 建议确认无风险后放通。 |
| 1 | 低风险。发现风险因素，结合总体评分后风险较低。 | 建议进行简单验证（如验证码、短信等），或人工审核。 |
| 2 | 中风险。发现风险因素，结合总体评分后风险中等。 | 建议根据业务场景采取一定措施规避伤害。例如，营销活动可降低高等级奖励的概率、打榜类活动对此类投票降低权重、登录注册要求二次验证等。 |
| 3 | 高风险。发现风险因素，结合总体评分后风险较高。 | 建议业务逻辑直接拦截。例如，红包类活动返回不中奖或最小额红包、打榜类活动不计算票数、登录/注册操作要求二次验证、高危业务可选择限制本次操作。 |
| 4 | 风险未知。暂无明确风险等级。 | 建议结合账号历史行为及业务场景做出最终决策。 |

附表②: 风险标签及解释

| **riskTag** | **名称** | **解释** |
| --- | --- | --- |
| spamMailbox | 绑定垃圾邮箱 | 疑似绑定垃圾邮箱 |
| riskPhoneNumber | 绑定卡商手机号 | 疑似绑定卡商手机号 |
| riskDevice | 使用风险设备 | 疑似使用自动机、群控等异常设备注册或登录 |
| ipCluster | IP聚集 | 疑似半年内存在IP的聚集性异常 |
| deviceCluster | 设备聚集 | 疑似半年内存在设备的聚集性异常 |
| batchBehavior | 批量操作 | 疑似半年内与大量垃圾账号存在批量协同行为轨迹 |
| illegalLogin | 非法登录 | 当前华为账号疑似通过非法手段登录 |
| activityFraud | 恶意行为-薅羊毛 | 疑似半年内在营销活动中存在薅羊毛的行为 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "errCode": 0,
6. "errMsg": "",
7. "riskLevel": 2,
8. "riskTag": [
9. "spamMailbox"
10. ]
11. }
```

### 请求失败时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "errCode": 403,
6. "errMsg": "no permission"
7. }
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```
1. import com.alibaba.fastjson2.JSONArray;
2. import com.alibaba.fastjson2.JSONObject;
3. import org.apache.http.client.methods.CloseableHttpResponse;
4. import org.apache.http.client.methods.HttpPost;
5. import java.io.IOException;
6. import java.util.HashMap;
7. import java.util.Map;
8. import java.util.Objects;

10. /**
11. * 获取用户风险等级
12. */
13. public class GetUserRiskLevelDemo {
14. public static void main(String[] args) throws IOException {
15. // 获取用户风险等级的接口URL
16. String url = "https://account.cloud.huawei.com/user/getuserrisklevel";
17. // 替换为实际的Client ID
18. String clientID = "<Client ID>";
19. // 替换为实际的transactionID
20. String transactionID = "<transactionID>";
21. // 替换为实际获取到的用户级凭证Access Token
22. String accessToken = "<Access Token>";
23. // 替换为实际的scene
24. String scene = "<scene>";
25. JSONObject result = getUserRiskLevel(url, clientID, transactionID, accessToken, scene);
26. // 解析获取errCode
27. Integer errCode = result.getInteger("errCode");
28. // 解析获取errMsg
29. String errMsg = result.getString("errMsg");
30. // 解析获取riskLevel
31. Integer riskLevel = result.getInteger("riskLevel");
32. // 解析获取riskTag
33. JSONArray riskTag = result.getJSONArray("riskTag");
34. }

36. private static JSONObject getUserRiskLevel(String url, String clientID, String transactionID,
37. String accessToken, String scene) throws IOException {
38. HttpPost httpPost = new HttpPost(url + "?" + "clientID=" + clientID + "&transactionID=" + transactionID);
39. Map<String, String> reqBody = new HashMap<>();
40. reqBody.put("accessToken", accessToken);
41. reqBody.put("scene", scene);
42. httpPost.setHeader("Content-Type", "application/json;charset=utf-8");
43. httpPost.setEntity(CallUtils.wrapJsonEntity(reqBody));
44. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost, (CloseableHttpResponse response, String rawBody) -> {
45. int statusCode = response.getStatusLine().getStatusCode();
46. // http状态码不是200，请求失败
47. if (statusCode != 200) {
48. return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
49. }
50. // http状态码为200，解析响应的body，判断业务错误码
51. JSONObject errorResponseBody = CallUtils.toJsonObject(rawBody);
52. // 错误码
53. Integer errCode = errorResponseBody.getInteger("errCode");
54. // errCode为0表示成功，非0表示失败
55. if (Objects.nonNull(errCode) && errCode != 0) {
56. return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
57. }
58. return null;
59. }));
60. }
61. }
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功（接口调用成功不等于业务处理成功，实际业务处理结果需要通过**Response Body**中的**errCode**进行判断）。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 415 | 不支持的媒体类型 | 请检查http请求的contentType是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

| errCode | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确  - 其他内部原因 | - 请检查传参是否正确，如无问题请尝试重新获取。  - 本接口请求数据格式为 application/json;charset=utf-8，在构造请求体时，请确保不对access\_token参数进行URLEncode处理，可参考[示例代码](account-api-getuserrisklevel.md#示例代码)组装参数。  - 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 403 | 无权访问 | 请前往AppGallery Connect（简称AGC）为应用申请开放权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。 |
| 503 | 触发系统流控。 | 请稍后重试。 |
| 70001201 | 请求参数错误 | 修改请求url或者请求体中的参数。 |
| 70001402 | 系统鉴权错误。 | 鉴权系统异常，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70020002 | 接口内部超时 | 稍后重试。 |
| 70001401 | 接口内部错误 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
