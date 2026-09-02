---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-cookiemanagerapi
title: ArkWeb_CookieManagerAPI
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_CookieManagerAPI
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d91b3031d52bb605f05c94060ef5e7bc5376648da743e3862c13f165694f1cc
---

```c
typedef struct {...} ArkWeb_CookieManagerAPI
```

## 概述

ArkWeb\_CookieManagerAPI是Cookie管理相关Native API结构体。该结构体提供了Cookie的读取、设置、清除和同步等操作能力，适用于需要在WebView组件中管理用户会话、跟踪用户首选项等场景，能够帮助开发者便捷地实现数据持久化和状态同步。

CookieManager相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取，调用前建议通过[ARKWEB\_MEMBER\_MISSING](capi-arkweb-type-h.md#宏定义)校验函数指针的可用性，避免SDK与设备ROM不匹配导致崩溃。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t size | 结构体的大小。 |

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [ArkWeb\_ErrorCode (\*fetchCookieSync)(const char\* url, bool incognito, bool includeHttpOnly, char\*\* cookieValue)](capi-web-arkweb-cookiemanagerapi.md#fetchcookiesync) | 获取指定URL对应的cookie值。 |
| [ArkWeb\_ErrorCode (\*configCookieSync)(const char\* url,const char\* cookieValue, bool incognito, bool includeHttpOnly)](capi-web-arkweb-cookiemanagerapi.md#configcookiesync) | 设置指定URL的cookie值。 |
| [bool (\*existCookies)(bool incognito)](capi-web-arkweb-cookiemanagerapi.md#existcookies) | 检查cookie是否存在。 |
| [void (\*clearAllCookiesSync)(bool incognito)](capi-web-arkweb-cookiemanagerapi.md#clearallcookiessync) | 清除所有cookies。 |
| [void (\*clearSessionCookiesSync)()](capi-web-arkweb-cookiemanagerapi.md#clearsessioncookiessync) | 清除所有会话cookies。 |

## 成员函数说明

### fetchCookieSync()

```c
ArkWeb_ErrorCode (*fetchCookieSync)(const char* url, bool incognito, bool includeHttpOnly, char** cookieValue)
```

**描述：**

获取指定URL对应的cookie值。用于用户登录状态维护、会话管理、个性化配置读取等场景。该方法需在UI线程调用，调用前建议校验函数指针的可用性。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* url | 要获取的cookie所属的URL，建议使用完整的URL。 |
| bool incognito | true表示获取隐私模式下WebView的内存cookie（应用退出后自动清除），false表示获取非隐私模式下的cookie（持久化存储）。 |
| bool includeHttpOnly | true表示标记为HTTP-Only属性的cookie也将包含在cookieValue中，false表示不包含。  **说明：** 读取HTTP-Only cookie应确保符合安全合规要求。 |
| char\*\* cookieValue | 输出参数，用于获取与URL对应的cookie值。内存由函数内部分配，调用方需在使用完毕后释放。返回值为字符串格式，包含所有匹配的cookie项，格式为name=value，其中name和value分别为cookie的名称和值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | 返回值错误码。  [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 获取cookie成功。  [ARKWEB\_INVALID\_URL](capi-arkweb-error-code-h.md#arkweb_errorcode) 无效的URL。可能原因：URL格式不正确、URL为空或不符合规范。  [ARKWEB\_INVALID\_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode) cookieValue参数无效。 |

### configCookieSync()

```c
ArkWeb_ErrorCode (*configCookieSync)(const char* url, const char* cookieValue, bool incognito, bool includeHttpOnly)
```

**描述：**

设置指定URL的cookie值。用于保存用户偏好设置、维持登录状态、会话信息保存等场景。该方法需在UI线程调用，调用前建议校验函数指针的可用性。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* url | 指定cookie所属的URL，建议填写完整的URL。 |
| const char\* cookieValue | 要设置的cookie的值。格式为name=value，其中name和value分别为cookie的名称和值。 |
| bool incognito | true表示在隐私模式下设置对应URL的cookie（应用退出后自动清除），false表示以非隐私模式设置对应URL的cookie（持久化存储）。 |
| bool includeHttpOnly | 是否包含或覆盖标记为HTTP-Only属性的cookie。如果为true，则标记为HTTP-Only属性的cookie也可以被包含在结果中或被覆盖；如果为false，则仅处理非HTTP-Only属性的cookie。  **说明：** 覆盖HTTP-Only cookie可能影响安全性，请确保符合业务安全要求。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | 返回值错误码。  [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 设置cookie成功。  [ARKWEB\_INVALID\_URL](capi-arkweb-error-code-h.md#arkweb_errorcode) 无效的URL。可能原因：URL格式不正确、URL为空或不符合规范。  [ARKWEB\_INVALID\_COOKIE\_VALUE](capi-arkweb-error-code-h.md#arkweb_errorcode) cookieValue参数无效。 |

### existCookies()

```c
bool (*existCookies)(bool incognito)
```

**描述：**

检查cookie是否存在。用于判断用户是否已登录、检查会话是否有效、验证身份状态等场景。该方法需在UI线程调用，调用前建议校验函数指针的可用性。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool incognito | true表示隐私模式下是否存在cookie，false表示非隐私模式下是否存在cookie。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true表示cookie存在，false表示cookie不存在。 |

### clearAllCookiesSync()

```c
void (*clearAllCookiesSync)(bool incognito)
```

**描述：**

清除所有cookies（包括持久化cookies和会话cookies）。用于用户退出登录、清除隐私数据、重置用户状态等场景。若仅需清除会话cookies，建议使用[clearSessionCookiesSync](capi-web-arkweb-cookiemanagerapi.md#clearsessioncookiessync)。该方法需在UI线程调用，调用前建议校验函数指针的可用性。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool incognito | true表示清除隐私模式下的所有cookies，false表示清除非隐私模式下的所有cookies。 |

### clearSessionCookiesSync()

```c
void (*clearSessionCookiesSync)()
```

**描述：**

清除所有会话cookies。用于清除临时会话数据、关闭所有会话、会话超时清理等场景。该方法需在UI线程调用，调用前建议校验函数指针的可用性。
