---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-server-error-code
title: REST API错误码
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > REST API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c08f3c5686252a6b35943fd419ebde9d28562e7a15e59d3335d1a05e66159079
---

## 获取用户级凭证

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/token

错误码信息：

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
| 1101 | 20085 | 在grant\_type参数传authorization\_code时，client\_secret传参为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20152 | code格式不正确。 | 检查code格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。  该错误码出现可能场景：  - code参数被篡改，导致格式不符。  - 请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body体进行URLEncode处理，可参考[示例代码](account-api-obtain-user-token.md#示例代码)组装参数。 |
| 1101 | 20154 | code解析得到的Client ID与入参client\_id不一致。 | 检查入参client\_id是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 1101 | 20155 | code过期，code只有5分钟有效期，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的code再重试。 |
| 1101 | 20156 | code已经被使用过。 | code只能用一次，请重新获取code再重试。 |
| 1101 | 20158 | code已失效。正常code有效期为5分钟，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的code。 | 请引导用户重新授权，获取新的code再重试。 |
| 1101 | 20171 | 在grant\_type参数传“device\_code”、“refresh\_token”或“client\_credentials”时，client\_secret传参为空。 | 请按照接口参数的要求，grant\_type参数请固定传“authorization\_code”，并且传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”authorization\_code“。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20151 | code为空。 | 请按照接口参数的要求，传入正确的code参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”authorization\_code“。 |
| 1103 | 20153 | 无效的code。 | 请检查code是否正确。 |
| 1203 | 12303 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1203 | 12304 | 无效的client\_secret。 | 入参client\_id和client\_secret不匹配导致，请检查参数。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 刷新用户级凭证

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/token

错误码信息：

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
| 1101 | 20041 | scope格式不正确或数量超过150个。 | - 检查scope参数是否满足正则：^[0-9a-zA-Z:/\\.\u0020]+$。  - 检查scope数量是否超过150个。 |
| 1101 | 20042 | 无效的scope。 | 入参scope存在伪造值，请参照参数说明，传入正确的参数。 |
| 1101 | 20154 | refresh\_token中的client\_id和入参不一致。 | 检查入参client\_id是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 1101 | 20171 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”refresh\_token“。 |
| 1101 | 20192 | refresh\_token格式不正确。 | refresh\_token参数格式需要满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”refresh\_token“。 |
| 1102 | 20191 | refresh\_token为空。 | 请按照接口参数的要求，传入正确的refresh\_token参数。 |
| 1203 | 11205 | refresh\_token已过期。refresh\_token的有效期为180天，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的refresh\_token。 |
| 1203 | 12303 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1203 | 12304 | 无效的client\_secret。 | 入参client\_id和client\_secret不匹配导致，请检查参数。 |
| 1203 | 31202 | refresh\_token解析失败。 | refresh\_token不是一个正确有效的数据，请检查refresh\_token参数。 |
| 1203 | 31204 | refresh\_token已失效。正常refresh\_token有效期为180天，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前使已颁发的refresh\_token失效。 | 请引导用户重新授权，获取新的refresh\_token。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取应用级凭证

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/token

错误码信息：

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
| 1101 | 12304 | client\_secret不正确。 | 请前往AppGallery Connect（简称AGC）确认client\_secret是否正确。 |
| 1101 | 20002 | client\_id格式不正确。 | 检查client\_id是否满足正则：^[0-9]{1,64}$。 |
| 1101 | 20003 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1101 | 20171 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”client\_credentials“。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”client\_credentials“。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 扫码授权登录-获取用户级凭证

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/token

错误码信息：

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
| 1101 | 20152 | code格式校验不通过。 | 检查code格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。  该错误码出现可能场景：  - code参数被篡改，导致格式不符。  - 请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body体进行URLEncode处理，可参考[示例代码](account-api-obtain-user-token-for-qrcode.md#示例代码)组装参数。 |
| 1101 | 20154 | code解析得到的Client ID与入参client\_id不一致。 | 检查入参client\_id是否与调用[获取二维码信息接口](account-api-get-authorize-qrcode-info.md#接口原型)时的入参client\_id一致。 |
| 1101 | 20171 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”device\_code“。 |
| 1101 | 20404 | 二维码的user\_code已到期。 | 请重新调用[获取二维码信息](account-api-get-authorize-qrcode-info.md)，生成新的二维码。 |
| 1101 | 20406 | 设备码已经成功获取到用户级凭证，无法再次使用。 | 请重新调用[获取二维码信息](account-api-get-authorize-qrcode-info.md)，生成新的二维码。 |
| 1101 | 20407 | 设备码获取用户级凭证轮询超过限制。 | 请重新调用[获取二维码信息](account-api-get-authorize-qrcode-info.md)，生成新的二维码。 |
| 1101 | 20408 | 设备码解析出来的scope校验不通过。 | 在调用[获取二维码信息](account-api-get-authorize-qrcode-info.md)时，请严格按照接口入参要求，传入指定的scope枚举值。 |
| 1101 | 20411 | 用户未扫码。 | 该场景属于正常错误，轮询过程中如出现该错误，请勿中断轮询。 |
| 1101 | 20412 | 用户已扫码，但未完成授权。 | 该场景属于正常错误，轮询过程中如出现该错误，请勿中断轮询。 |
| 1101 | 20414 | 用户已扫码，但是在授权页点击取消。 | 请重新调用[获取二维码信息](account-api-get-authorize-qrcode-info.md)，生成新的二维码。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20151 | code为空。 | 请按照接口参数的要求，传入正确的code参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”device\_code“。 |
| 1203 | 12303 | client\_id在系统不存在。 | 在grant\_type=device\_code场景下，检查client\_id参数在系统不存在。请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1203 | 12304 | 无效的client\_secret。 | 入参client\_id和client\_secret不匹配导致，请检查参数。 |
| 1600 | 16002 | 设备码解析失败。 | 入参code错误，该参数值可通过[获取二维码信息](account-api-get-authorize-qrcode-info.md)接口获取，取响应参数device\_code字段的值。 |
| 1600 | 16003 | 设备码过期。 | 请重新调用[获取二维码信息](account-api-get-authorize-qrcode-info.md)，生成新的二维码。 |
| 1203 | 56000 | 系统内部调用出现异常。 | 系统内部调用出现异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 56100 | 系统内部调用连接超时。 | 系统内部调用连接超时，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 56200 | 系统内部调用socket超时。 | 系统内部调用socket超时，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 57000 | 系统内部调用触发熔断。 | 服务内部调用触发熔断，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 解析凭证

接口URL：https://oauth-api.cloud.huawei.com/rest.php?nsp\_fmt=JSON&nsp\_svc=huawei.oauth2.user.getTokenInfo

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP\_STATUS**进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | access\_token已过期。access\_token的有效期为3600秒，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的access\_token。 |
| 102 | 无效的access\_token。 | access\_token参数无效，可能原因：请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body参数进行URLEncode处理，可参考[示例代码](account-api-get-token-info.md#示例代码)组装参数。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 501 | 服务分发异常。 | - 检查请求URL中nsp\_svc是否正确  - 若确认请求URL与文档一致，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1302 | 接口流控。 | 业务调用频率过高，请稍后重试。 |
| 31204 | access\_token已失效。正常access\_token有效期为3600秒，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的access\_token。 | 请引导用户重新授权，获取新的access\_token。 |

## 取消用户级凭证授权

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/revoke

错误码信息：

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
| 1101 | 20222 | token格式不正确。 | token格式不正确，可能原因：  - token参数为伪造的值。  - 请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body体进行URLEncode处理，可参考[示例代码](account-api-obtain-revoke-token.md#示例代码)组装参数。 |
| 1102 | 20221 | token为空。 | 请按照接口参数的要求，传入正确的token参数。 |
| 1203 | 11205 | token已过期。Access Token有效期为3600秒，Refresh Token有效期为180天，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的token并重试。 |
| 1203 | 17009 | 无效的token。 | 传入的token参数无效，请重新获取token。 |
| 1203 | 17010 | token验证失败。 | token不是一个正确有效的数据，请检查token参数。 |
| 1203 | 31202 | token解析失败。 | token不是一个正确有效的数据，请检查token参数。 |
| 1203 | 31204 | token已失效。正常Access Token有效期为3600秒，Refresh Token有效期为180天，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的Access Token和Refresh Token。 | 请引导用户重新授权，获取新的token并重试。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取二维码信息

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/device/code

错误码信息：

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

## 获取用户信息

接口URL：https://account.cloud.huawei.com/rest.php?nsp\_svc=GOpen.User.getInfo

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功（接口调用成功不等于业务处理成功，如**Response Header**中返回了**NSP\_STATUS**字段，说明业务处理报错，需要判断报错原因）。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确  - 其他内部原因 | - 请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-get-user-info-get-nickname-and-avatar.md#示例代码)组装参数。  - 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 105 | 参数错误 | 参考API文档的说明，调整参数传值。 |
| 403 | 访问无权限。 | 请前往AppGallery Connect（简称AGC）为应用申请开放权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 触发系统流控。 | 请稍后重试。 |
| 70001201 | 参数不合法 | 参考API文档的说明，调整参数传值。 |
| 70001402 | 系统鉴权错误。 | 鉴权系统异常，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70020002 | 内部网络错误。 | 内部网络错误，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70001401 | 系统内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 一键登录获取华为账号绑定号码和UnionID/OpenID

接口URL：https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Body**中的**resultCode（错误码）** 进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

| 错误码 | 描述 | 解决方法 |
| --- | --- | --- |
| 60010002 | 参数不合法。 | 请按照错误描述及接口[Request Body](account-api-get-user-info-quicklogin-by-code.md#request-body)参数说明检查入参。 |
| 60010012 | code参数不正确。 | code参数传值不正确，可能原因：伪造的无效code或code被篡改。 |
| 60010013 | clientSecret参数不正确。 | clientSecret参数传值不正确，参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client Secret**参数。 |
| 60180003 | code解析得到的Client ID与入参clientId不一致。 | code参数获取时的clientId与当前接口参数clientId不一致导致，请检查当前入参clientId是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 60180004 | code过期，code只有5分钟有效期，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的code再重试。 |
| 60180005 | code已经被使用过。 | code只能用一次，请重新获取code再重试。 |
| 60180006 | code已失效。正常code有效期为5分钟，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的code。 | 请引导用户重新授权，获取新的code再重试。 |
| 60180007 | code未授权华为账号一键登录权限。 | code未授权华为账号一键登录权限，可能原因如下：  - 在进行华为账号一键登录客户端功能开发时，登录按钮的[LoginWithHuaweiIDButtonParams.loginType](account-api-component-manager.md#loginwithhuaweiidbuttonparams)属性未设置为LoginType.QUICK\_LOGIN。  - 客户端传给服务器的Authorization Code，是通过华为账号一键登录预取号阶段获取到的Authorization Code。  - 客户端传给服务器的Authorization Code，不是华为账号一键登录场景获取到的。  以上可能原因的解决方法，请参考[60180007 服务端通过Authorization Code无法获取到华为账号一键登录手机号如何解决](../harmonyos-guides/account-faq-21.md)。 |
| 60180008 | 用户无手机号。 | 用户华为账号未绑定手机号，该异常场景应用需要展示其他登录方式。 |
| 60180009 | 手机号信息获取受限。 | 华为账号一键登录服务仅对中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户提供。 |
| 60010001 | 系统内部错误。 | 请稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取用户风险等级

接口URL：https://account.cloud.huawei.com/user/getuserrisklevel

错误码信息：

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
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期。  - access\_token格式不正确。  - 其他内部原因。 | - 请检查传参是否正确，如无问题请尝试重新获取。  - 本接口请求数据格式为 application/json;charset=utf-8，在构造请求体时，请确保不对access\_token参数进行URLEncode处理，可参考[示例代码](account-api-getuserrisklevel.md#示例代码)组装参数。  - 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 403 | 无权访问 | 请前往AppGallery Connect（简称AGC）为应用申请开放权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。 |
| 503 | 触发系统流控。 | 请稍后重试。 |
| 70001201 | 请求参数错误 | 修改请求url或者请求体中的参数。 |
| 70001402 | 系统鉴权错误。 | 鉴权系统异常，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70020002 | 接口内部超时 | 稍后重试。 |
| 70001401 | 接口内部错误 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取实名信息

接口URL：https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.getDetailInfo

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP\_STATUS**进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确 | - access\_token无效或已过期，请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-get-realname.md#示例代码)组装参数。 |
| 105 | 请求url中nsp\_svc参数错误。 | 请检查请求地址参数是否正确。 |
| 403 | 访问无权限。 | 请根据[使用约束](account-api-get-realname.md#使用约束)章节进行检查。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 接口流控。 | 业务调用频率过高，请稍后重试。 |
| 70001201 | 请求参数错误。 | 请根据错误描述信息确定错误参数并修正后重试。 |
| 70001401 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70009019 | 实名信息不存在 | 账号未实名，请先进行实名，或更换已实名账号，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 实名信息校验

接口URL：https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.verifyRealName

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP\_STATUS**进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确 | - access\_token无效或已过期，请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-verify-realname.md#示例代码)组装参数。 |
| 105 | 请求url中nsp\_svc参数错误。 | 请检查请求地址参数是否正确。 |
| 403 | 访问无权限。 | 请根据[使用约束](account-api-verify-realname.md#使用约束)章节进行检查。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 接口流控。 | 业务调用频率过高，请稍后重试。 |
| 70001201 | 请求参数错误。 | 请根据错误描述信息确定错误参数并修正后重试。 |
| 70001401 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70009019 | 实名信息不存在 | 账号未实名，请先进行实名，或更换已实名账号，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取用户年龄段标识

接口URL：https://account-realname-api.cloud.huawei.com/openrealname/v6/realname-info/get

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功（接口调用成功不等于业务处理成功，如**Response Body**中返回了**resultCode**字段，说明业务处理报错，需要判断报错原因）。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的HTTP请求method。 | 请检查HTTP请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Body中的resultCode字段，在处理成功时不会返回。

| resultCode | 描述 | 解决方法 |
| --- | --- | --- |
| 60010002 | 参数不合法。 | 请按照错误描述及接口[Request Body](account-api-get-realname-age-range-flag.md#request-body)参数说明检查入参。 |
| 60010003 | 鉴权信息不合法。 | 请检查Header中Authorization参数传值，可能是未传值或传值不正确。 |
| 60010014 | 会话失效。  可能原因:  - Access Token格式不正确  - Access Token无效或已过期 | 请检查Header中Authorization参数传值，确保获取凭证时Authorization Code包含realNameAgeRange scope的授权，详见[获取用户级凭证](account-api-obtain-user-token.md)。 |
| 61110001 | 触发系统流控。 | 请稍后重试。 |
| 61110002 | Access Token中的scope权限不满足。  可能原因:  - 应用未申请realNameAgeRange scope权限。  - 获取Authorization Code时没有携带realNameAgeRange scope。 | - 申请realNameAgeRange scope权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)  - 请检查Header中Authorization参数传值，确保获取凭证时Authorization Code包含realNameAgeRange scope的授权，详见[获取用户级凭证](account-api-obtain-user-token.md)。 |
| 61110003 | Access Token中的Client ID和入参clientId不一致。 | 请检查获取凭证时Authorization Code时携带的Client ID是否和body入参中的clientId保持一致。 |
| 60010001 | 系统内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 通过OpenID获取UnionID

接口URL：https://oauth-login.cloud.huawei.com/rest.php?nsp\_svc=huawei.oauth2.app.openIdToUnionId

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP\_STATUS**进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | access\_token已过期。access\_token有效期为3600秒，超过有效期后将无法继续使用。 | 请通过[获取应用级凭证](account-api-obtain-app-token.md)重新获取新的access\_token。 |
| 102 | 无效的access\_token。 | access\_token参数无效，可能原因：请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body参数进行URLEncode处理，可参考[示例代码](account-api-get-unionid.md#示例代码)组装参数。 |
| 403 | 无权限访问。 | 入参access\_token请通过[获取应用级凭证](account-api-obtain-app-token.md)获取，其他方式获取的access\_token不允许调用该接口。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 501 | 服务分发异常。 | - 检查请求URL中nsp\_svc是否正确  - 若确认请求URL与文档一致，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1302 | 接口流控。 | 业务调用频率过高，单应用调用并发请低于100TPS。 |
| 31204 | access\_token已失效。 | 通过[获取应用级凭证](account-api-obtain-app-token.md)获取的access\_token不会出现此错误。请严格按照接口入参要求，使用[获取应用级凭证](account-api-obtain-app-token.md)方式获取access\_token并重试。 |
| 150028 | open\_id参数非法。 | open\_id参数非法，可能原因：  - open\_id参数为空。  - open\_id参数格式错误，具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

## 通过Authorization Code获取GroupUnionID

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/token

错误码信息：

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
| 1101 | 20085 | 在grant\_type参数传authorization\_code时，client\_secret传参为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20152 | code格式不正确。 | 检查code格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。  该错误码出现可能场景：  - code参数被篡改，导致格式不符。  - 请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body体进行URLEncode处理，可参考[示例代码](account-api-get-groupunionid-code.md#示例代码)组装参数。 |
| 1101 | 20154 | code解析得到的Client ID与入参client\_id不一致。 | 检查入参client\_id是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 1101 | 20155 | code过期，code只有5分钟有效期，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的code再重试。 |
| 1101 | 20156 | code已经被使用过。 | code只能用一次，请重新获取code再重试。 |
| 1101 | 20158 | code已失效。正常code有效期为5分钟，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的code。 | 请引导用户重新授权，获取新的code再重试。 |
| 1101 | 20171 | 在grant\_type参数传“device\_code”、“refresh\_token”或“client\_credentials”时，client\_secret传参为空。 | 请按照接口参数的要求，grant\_type参数请固定传“authorization\_code”，并且传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”authorization\_code“。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20151 | code为空。 | 请按照接口参数的要求，传入正确的code参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”authorization\_code“。 |
| 1103 | 20153 | 无效的code。 | code被篡改或伪造的code导致，请排查code参数是否与获取到的code一致。 |
| 1203 | 12303 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1203 | 12304 | 无效的client\_secret。 | 入参client\_id和client\_secret不匹配导致，请检查参数。 |
| 1203 | 100301 | 参数处理异常。 | 参数处理异常，建议按照接口入参要求，检查参数是否符合规范。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 100502 | 开发者账号的关联主体账号组未查询到。 | 请参考[添加账号组成员](../start/aai-0000001265430513.md)，将应用的开发者账号加入关联主体账号组后重试。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 通过OpenID或UnionID获取GroupUnionID

接口URL：https://account-api.cloud.huawei.com/oauth2/v6/groupUnionId/batchGet

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Body**中的**resultCode（错误码）** 进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

| 错误码 | 描述 | 解决方法 |
| --- | --- | --- |
| 60010002 | 参数错误。 | 请按照响应描述中的提示，检查并修改[请求参数](account-api-get-groupunionid.md#请求参数)。 |
| 60010003 | 鉴权头Authorization校验不通过。 | 检查并修改[请求参数](account-api-get-groupunionid.md#请求参数)中Authorization参数。 |
| 60170001 | 开发者账号未加入关联主体账号组。 | 可通过[创建账号组](../start/cag-0000001265390541.md)创建关联主体账号组，然后在关联主体账号组中[添加账号组成员](../start/aai-0000001265430513.md)。 |
| 60010001 | 系统内部错误。 | 可重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取OpenID Connect配置公开信息

接口URL：https://oauth-login.cloud.huawei.com/.well-known/openid-configuration

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 获取验证ID Token的JWT公钥信息

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/certs

错误码信息：

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

## 验证ID Token有效性

接口URL：https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo

错误码信息：

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
| 1203 | 100305 | id\_token的header解析成功后的内容不是JSON格式。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1203 | 100306 | id\_token的payload解析成功后的内容不是JSON格式。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1203 | 150021 | id\_token的header解析失败。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1203 | 150022 | id\_token的payload解析失败。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1203 | 150023 | id\_token的signature解析失败。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1400 | 14004 | 无法通过其kid找到对应的JWT公钥相关信息。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1500 | 15003 | 无效的id\_token。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1500 | 15004 | id\_token验证失败。 | id\_token格式错误或者伪造的id\_token，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1500 | 15005 | id\_token的issuer验证失败。 | id\_token的issuer校验失败，请检查id\_token参数值是否为华为账号返回的原始值。 |
| 1500 | 15006 | id\_token已过期。 | 请重新获取新的id\_token。 |
| 1500 | 15007 | id\_token为空。 | 请按照接口参数的要求，传入正确的id\_token参数。 |
| 1500 | 15008 | id\_token格式不正确。 | 检查id\_token的格式是否满足正则：^[0-9a-zA-Z\_\-\.]+$。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
