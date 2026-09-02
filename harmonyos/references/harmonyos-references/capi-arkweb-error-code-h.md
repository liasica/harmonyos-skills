---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h
title: arkweb_error_code.h
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 头文件 > arkweb_error_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:688a510c8aed5f69b673e2bc5818d6ce136226b67fff578760e64c4b6c46194a
---

## 概述

声明ArkWeb NDK接口异常错误码，用于在ArkWeb相关接口调用失败时返回具体的错误信息，帮助开发者快速定位和解决问题。这些错误码覆盖了初始化、参数校验、URL处理、Cookie管理、库加载等常见异常场景。

**引用文件：** <web/arkweb\_error\_code.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | ArkWeb\_ErrorCode | 表示ArkWeb NDK接口操作的结果状态，用于判断接口调用是否成功。 |
| [ArkWeb\_BlanklessErrorCode](capi-arkweb-error-code-h.md#arkweb_blanklesserrorcode) | ArkWeb\_BlanklessErrorCode | 表示无白屏加载功能操作的结果状态，用于判断无白屏加载接口调用是否成功。 |

## 枚举类型说明

### ArkWeb\_ErrorCode

```c
enum ArkWeb_ErrorCode
```

**描述：**

定义ArkWeb NDK接口异常错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB\_SUCCESS = 0 | 成功。 |
| ARKWEB\_INIT\_ERROR = 17100001 | 初始化失败。请检查系统环境，确保依赖库已安装，重试初始化。 |
| ARKWEB\_ERROR\_UNKNOWN = 17100100 | 未知错误，请收集日志反馈。 |
| ARKWEB\_INVALID\_PARAM = 17100101 | 参数无效。请检查传入参数的格式、范围和类型是否符合接口要求。 |
| ARKWEB\_SCHEME\_REGISTER\_FAILED = 17100102 | 注册scheme的配置失败，应该在创建ArkWeb之前注册。 |
| ARKWEB\_INVALID\_URL = 17100103 | 无效的URL，请检查URL格式或协议支持。 |
| ARKWEB\_INVALID\_COOKIE\_VALUE = 17100104 | 无效的cookie值，请检查cookie格式与有效性。 |
| ARKWEB\_LIBRARY\_OPEN\_FAILURE = 17100105 | 打开动态链接库失败。请检查动态链接库文件是否存在、路径是否正确、以及是否有读取权限。  **起始版本：** 15 |
| ARKWEB\_LIBRARY\_SYMBOL\_NOT\_FOUND = 17100106 | 动态链接库中找不到所需的符号。  **起始版本：** 15 |
| ARKWEB\_COOKIE\_MANAGER\_NOT\_INITIALIZED = 17100107 | CookieManager未初始化。请先调用初始化接口完成CookieManager的初始化。  **起始版本：** 20 |
| ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED = 17100108 | CookieManager初始化失败，请检查系统能力与权限配置。  **起始版本：** 20 |
| ARKWEB\_COOKIE\_SAVE\_FAILED = 17100109 | 保存cookie失败。请检查存储空间是否充足、是否有写入权限，以及cookie值是否符合规范。  **起始版本：** 20 |

### ArkWeb\_BlanklessErrorCode

```c
enum ArkWeb_BlanklessErrorCode
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
