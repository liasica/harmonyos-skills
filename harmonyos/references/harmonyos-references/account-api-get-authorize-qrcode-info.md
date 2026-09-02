---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-authorize-qrcode-info
title: 获取二维码信息
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 开放接口调用凭证 > 扫码授权登录 > 获取二维码信息
category: harmonyos-references
scraped_at: 2026-09-02T15:02:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2e9f563095631bf8a5e7421460279153d20507daaac16a5bd81265370eaca5ea
---

## 功能介绍

应用调用该接口获取二维码信息。

## 场景描述

在Account Kit[扫码授权登录](../harmonyos-guides/account-authorize-by-qrcode.md)场景中，应用调用该接口获取二维码信息。完整接入流程详见[扫码授权登录](../harmonyos-guides/account-authorize-by-qrcode.md)。

## 使用约束

需确保调用端网络正常。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/oauth2/v3/device/code
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-authorize-qrcode-info.md#示例代码)。 |

### Request Body

| 参数名 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| client\_id | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的OAuth 2.0客户端ID（凭据）-Client ID参数。 |
| scope | 否 | String | 需要获取的用户信息，多个以空格分隔。scope示例如下：  - openid：获取用户OpenID、UnionID。  - profile：获取用户头像昵称。 |

## 请求示例

```http
POST /oauth2/v3/device/code HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

client_id=<client_id>&scope=openid profile
```

## 响应参数

### Response Header

| 参数名 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8 |

### Response Body

| 参数名 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| create\_time | 是 | Long | Unix时间戳，用户码的创建时间，二维码有效时间以这个时间为基准。 |
| device\_code | 是 | String | 设备码，可用于获取Access Token。 |
| expire\_in | 是 | Integer | 设备码的过期时间，单位：s。设备码超过该有效期后，将无法获取Access Token。 |
| interval | 是 | Integer | 设备码获取Access Token轮询间隔时间，单位：s。轮询次数不得超过expire\_in/interval。 |
| scan\_expire\_in | 是 | Integer | 用户码的到期时间，如果在这个时间内不扫码，用户码变为不可用，需要重新获取，单位：s。 |
| user\_code | 是 | String | 用户码，用于生成二维码。 |
| verification\_url | 是 | String | 用户码的校验URL，负责展示授权登录页面。 |

## 响应示例

### 请求成功时

```http
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "create_time": 1569813512,
    "device_code": "AgEAAN7qd*****U0TvQ",
    "expire_in": 1800,
    "interval": 3,
    "scan_expire_in": 120,
    "user_code": "ABCDEFGH",
    "verification_url": "https://oauth-login1.cloud.huawei.com/oauth2/v3/device"
}
```

### 请求失败时

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=utf-8

{
    "sub_error": 20042,
    "error_description": "invalid scope",
    "error": 1101
}
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```java
import com.alibaba.fastjson2.JSONObject;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.message.BasicNameValuePair;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * 获取二维码信息
 */
public class GetQrCodeInfoDemo {
    public static void main(String[] args) throws IOException {
        // 获取二维码信息的接口URL
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/device/code";
        // 替换为您的Client ID
        String clientId = "<Client ID>";
        // 替换为您实际需要获取的用户权限scope，多个以空格分隔
        String scope = "openid profile";
        JSONObject result = getQrCodeInfo(url, clientId, scope);
        // 解析获取create_time
        Long createTime = result.getLong("create_time");
        // 解析获取device_code
        String deviceCode = result.getString("device_code");
        // 解析获取expire_in
        Integer expireIn = result.getInteger("expire_in");
        // 解析获取interval
        Integer interval = result.getInteger("interval");
        // 解析获取user_code
        String userCode = result.getString("user_code");
        // 解析获取scan_expire_in
        Integer scanExpireIn = result.getInteger("scan_expire_in");
        // 解析获取verification_url
        String verificationUrl = result.getString("verification_url");
    }

    private static JSONObject getQrCodeInfo(String url, String clientId, String scope) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("client_id", clientId));
        request.add(new BasicNameValuePair("scope", scope));
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
        return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
    }
}
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 400 | 参数错误。 | 请根据**业务响应主错误码**以及**业务响应子错误码**进一步排查问题。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

| 业务响应主错误码 | 业务响应子错误码 | 描述 | 解决方法 |
| --- | --- | --- | --- |
| 1101 | 20002 | client\_id格式不正确。 | 检查client\_id是否满足正则：^[0-9]{1,64}$。 |
| 1101 | 20003 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1101 | 20041 | scope格式不正确或数量超过150个。 | - 检查scope参数是否满足正则：^[0-9a-zA-Z:/\\.\u0020]+$。  - 检查scope数量是否超过150个。 |
| 1101 | 20042 | 无效的scope。 | 入参scope存在伪造值，请参照参数说明，传入正确的参数。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1600 | 16001 | 生成设备码异常。 | 设备码编码时出现异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
