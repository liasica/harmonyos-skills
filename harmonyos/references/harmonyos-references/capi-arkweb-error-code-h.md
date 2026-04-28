---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h
title: arkweb_error_code.h
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 头文件 > arkweb_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6fb441ccf2ad3f1000194317917bb9fca3907033c4c8a798ac7a0deb882feff9
---

## 概述

PhonePC/2in1TabletTVWearable

声明ArkWeb NDK接口异常错误码。

**引用文件：** <web/arkweb\_error\_code.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | ArkWeb\_ErrorCode | 定义ArkWeb NDK接口异常错误码。 |
| [ArkWeb\_BlanklessErrorCode](capi-arkweb-error-code-h.md#arkweb_blanklesserrorcode) | ArkWeb\_BlanklessErrorCode | 定义无白屏加载的异常错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkWeb\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum ArkWeb_ErrorCode
```

**描述：**

定义ArkWeb NDK接口异常错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB\_SUCCESS = 0 | 成功。 |
| ARKWEB\_INIT\_ERROR = 17100001 | 初始化失败。 |
| ARKWEB\_ERROR\_UNKNOWN = 17100100 | 未知错误。 |
| ARKWEB\_INVALID\_PARAM = 17100101 | 参数无效。 |
| ARKWEB\_SCHEME\_REGISTER\_FAILED = 17100102 | 注册scheme的配置失败，应该在创建ArkWeb之前注册。 |
| ARKWEB\_INVALID\_URL = 17100103 | 无效的URL。 |
| ARKWEB\_INVALID\_COOKIE\_VALUE = 17100104 | 无效的cookie值。 |
| ARKWEB\_LIBRARY\_OPEN\_FAILURE = 17100105 | 打开动态链接库失败。  **起始版本：** 15 |
| ARKWEB\_LIBRARY\_SYMBOL\_NOT\_FOUND = 17100106 | 动态链接库中找不到所需的符号。  **起始版本：** 15 |
| ARKWEB\_COOKIE\_MANAGER\_NOT\_INITIALIZED = 17100107 | CookieManager未初始化。  **起始版本：** 20 |
| ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED = 17100108 | CookieManager初始化失败。  **起始版本：** 20 |
| ARKWEB\_COOKIE\_SAVE\_FAILED = 17100109 | 保存cookie失败。  **起始版本：** 20 |

### ArkWeb\_BlanklessErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum ArkWeb_BlanklessErrorCode
```

**描述：**

定义无白屏加载的异常错误码。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB\_BLANKLESS\_SUCCESS = 0 | 成功。 |
| ARKWEB\_BLANKLESS\_ERR\_UNKNOWN = -1 | 未知错误，内部状态错误等。 |
| ARKWEB\_BLANKLESS\_ERR\_INVALID\_ARGS = -2 | 参数不合法。 |
| ARKWEB\_BLANKLESS\_ERR\_CONTROLLER\_NOT\_INITED = -3 | WebViewController未绑定组件。 |
| ARKWEB\_BLANKLESS\_ERR\_KEY\_NOT\_MATCH = -4 | 未匹配到key值，对于OH\_NativeArkWeb\_SetBlanklessLoadingWithKey需与OH\_NativeArkWeb\_GetBlanklessInfoWithKey配套使用并且key值一致，否则返回该错误码。 |
| ARKWEB\_BLANKLESS\_ERR\_SIGNIFICANT\_CHANGE = -5 | 当相似度较低时，系统会判定为跳变太大，OH\_NativeArkWeb\_SetBlanklessLoadingWithKey接口启用插帧不成功。 |
| ARKWEB\_BLANKLESS\_ERR\_DEVICE\_NOT\_SUPPORT = 801 | 该设备不适用于此功能。 |
