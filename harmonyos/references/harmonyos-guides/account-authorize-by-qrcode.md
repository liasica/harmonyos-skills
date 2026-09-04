---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-authorize-by-qrcode
title: 扫码授权登录
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 登录 > 扫码授权登录
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:01+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:dba575000acf3e975b9ac086f2c2f642444f705c52c14951d59daeb6c606690a
---

## 场景介绍

对于在缺乏便捷触控界面或输入受限的设备上登录应用的场景，推荐使用扫码授权登录方式接入Account Kit。用户使用已登录华为账号的设备（例如：Phone、Tablet等）扫描应用二维码并完成授权后，应用即可获取用户标识UnionID/OpenID等信息，实现扫码授权登录。

## 业务流程

扫码授权登录的整体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/6uKFWsamRaGjSBKSe2b5sw/zh-cn_image_0000002742123917.png)

### 步骤说明

1. 展示二维码阶段（序号1-5）

   1. 用户选择华为账号扫码授权方式登录，应用调用华为账号服务器获取二维码信息。
   2. 应用根据华为账号服务器返回的二维码信息生成二维码图片。
2. 等待用户扫码授权登录阶段（序号6-9）

   1. 应用将获取到的设备码传给应用服务端，应用服务端使用设备码轮询[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)。
   2. 针对轮询[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)响应的结果，应用请自行进行处理。
3. 用户扫码授权登录阶段（序号10-21）

   1. 用户使用已登录华为账号的设备（例如：Phone、Tablet等）扫描应用二维码并完成授权。此时应用服务端轮询[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)获取到Access Token，再使用Access Token调用[获取用户信息接口](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#接口原型)获取用户UnionID、OpenID等信息。
   2. 应用服务端将业务登录凭证SessionId、UnionID/OpenID传给应用，应用获取到UnionID/OpenID可用于判断华为账号是否登录。
   3. 应用对用户标识UnionID/OpenID、业务登录凭证SessionId信息进行安全认证后完成扫码授权登录。

## 接口说明

扫码授权登录流程涉及关键接口如下所示：

| 接口名称 | 描述 |
| --- | --- |
| [获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型) | 应用通过调用该接口获取二维码信息。 |
| [扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型) | 通过轮询该接口，获取用户级凭证。 |
| [获取用户信息接口](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#接口原型) | 在获取到用户级凭证后，通过该接口获取用户UnionID/OpenID等信息。 |

## 开发步骤

### 获取二维码信息

应用调用华为账号的[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)获取二维码信息。

**请求消息示例**

请通过POST方式调用，示例如下：

```http
POST /oauth2/v3/device/code HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

client_id=<client_id>&scope=openid profile
```

**响应消息示例**

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

请求参数、响应参数及错误码等信息详见[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)。

### 生成二维码

应用根据响应中的verification\_url和user\_code生成二维码并展示。

**二维码URL内容如下**

```text
https://oauth-login1.cloud.huawei.com/oauth2/v3/device?user_code=<user_code>
```

应用可以通过[QRCode](../harmonyos-references/ts-basic-components-qrcode.md)来生成二维码并在应用内展示，等待用户扫码。

**说明** 

[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)返回的user\_code存在有效期（以接口响应结果中的scan\_expire\_in字段实际值为准），如果用户未在此时间内扫码，需要重新调用[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)生成新的二维码。

### 轮询获取用户级凭证

应用服务端轮询调用[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)（轮询间隔时间可参考[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)响应结果中的interval字段值），直到轮询次数超过限制、设备码超过有效期或成功获取Access Token为止。

**请求消息示例**

请通过POST方式调用，示例如下：

```http
POST /oauth2/v3/token HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

grant_type=device_code&code=<device_code>&client_id=<client_id>&client_secret=<client_secret>
```

**响应消息示例**

用户未扫码时

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "sub_error": 20411,
    "error_description": "user code not scan",
    "error": 1101
}
```

用户已扫码并完成授权时

```http
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "access_token": "DgEAAN7qd*****U0TvQ/eXpE4x+gvhoYh5/UuzL",
    "refresh_token": "DgECAL++vCn******NQ/UOL8+wm0jJi+o4NI793H",
    "expires_in": 3600,
    "id_token": "eyJraW*****ifQ.eyJhdF9oYX*****Q2fQ.TT05lFYe*****vDwb_Gj1ccR59yyB2Ig",
    "scope": "openid profile",
    "token_type": "Bearer",
    "open_id": "AQAxrBzThFv*****lv9tV_4rMCc"
}
```

请求参数、响应参数及错误码等信息详见[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)。

**说明** 

[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)返回的device\_code存在有效期（以接口响应结果中的expire\_in字段实际值为准），超时后需要重新调用[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)生成新的二维码。

应用服务端在轮询[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)时，同一个设备码轮询次数不得超过[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)响应结果中的expire\_in/interval的值，轮询超过限制后请求会被拒绝，需要重新调用[获取二维码信息接口](../harmonyos-references/account-api-get-authorize-qrcode-info.md#接口原型)生成新的二维码。

### 用户扫码授权登录

1. 用户使用已登录华为账号的设备（例如：Phone、Tablet等）扫描应用的二维码，弹出授权页面，显示应用名称、图标及申请的权限列表，用户点击允许后完成授权流程。
2. 在用户完成授权后，此时应用服务端轮询[扫码授权登录-获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token-for-qrcode.md#接口原型)获取到Access Token，再使用Access Token调用[获取用户信息接口](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#接口原型)获取用户UnionID、OpenID等信息。
3. 应用服务端将业务登录凭证SessionId、UnionID/OpenID传给应用，应用获取到UnionID/OpenID可用于判断华为账号是否登录。
4. 应用对用户标识UnionID/OpenID、业务登录凭证SessionId信息进行安全认证后完成扫码授权登录。

**说明** 

若Access Token过期，可以使用Refresh Token调用[刷新用户级凭证](../harmonyos-references/account-api-obtain-refresh-token.md)获取新的Access Token。
