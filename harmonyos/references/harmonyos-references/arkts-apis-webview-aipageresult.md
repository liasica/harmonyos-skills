---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-aipageresult
title: AIPageResult
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > AIPageResult
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f0a98ff965950355bad9bb95ce36714d8808f9bf31d206e81fc7df9d3cb2b46c
---

AIPageResult定义[executeAIPageCommand](arkts-apis-webview-webviewcontroller.md#executeaipagecommand)返回结果的通用格式与结果码取值，供[AIPageCommand](arkts-apis-webview-aipagecommand.md)和[AIPageInteraction](arkts-apis-webview-aipageinteraction.md)中的命令共享。

## CommandResult

[AIPageInteraction](arkts-apis-webview-aipageinteraction.md)中的scroll、select、uploadFile、setZoomLevel等命令返回如下JSON格式；[AIPageCommand](arkts-apis-webview-aipagecommand.md)中getZoomLevel的返回结果同样包含code和message字段，并追加zoomLevel字段。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| code | number | 执行结果码。取值请参见[命令执行结果码说明](arkts-apis-webview-aipageresult.md#命令执行结果码说明)。 |
| message | string | 执行结果描述。成功时为"success"；存在非阻塞警告时，追加"; warnings: "前缀及警告信息，格式为"success; warnings: <path1>: <reason1>, <path2>: <reason2>"；失败时为错误描述。 |

## 命令执行结果码说明

| 取值 | 说明 |
| --- | --- |
| 10 | 执行成功。 |
| 11 | 执行失败。 |
| 110 | JSON无效。 |
| 115 | xpath字段取值无效。 |
| 131 | 元素不存在。 |
| 132 | browser或host为空。 |
| 160 | 页面未就绪。 |
| 161 | 元素类型不匹配。 |
| 200 | 输入命令xpath字段无效。 |
| 201 | 输入命令value字段无效。 |
| 202 | 输入类型无效。 |
| 203 | 输入值格式无效。 |
| 204 | 输入事件类型不匹配。 |
| 250 | select命令xpath字段无效。 |
| 251 | select选项无效（indexes和values均未提供）。 |
| 252 | select索引越界。 |
| 253 | select值未找到。 |
| 254 | select不支持多选。 |
| 255 | select选项被禁用。 |
| 256 | select选项为空。 |
| 300 | 手势命令x字段无效。 |
| 301 | 手势命令y字段无效。 |
| 302 | 手势命令distance字段无效。 |
| 303 | 手势命令scale字段无效。 |
| 304 | 手势命令duration字段无效。 |
| 305 | 手势命令tapCount字段无效。 |
| 306 | 手势命令speed字段无效。 |
| 307 | 手势命令坐标字段无效。 |
| 350 | 命令下发失败。 |
| 351 | 命令通道未就绪。 |
| 352 | 命令执行失败。 |
| 353 | 命令响应解析错误。 |
| 370 | 文件路径无法解析。 |
| 371 | 文件路径为空。 |
| 372 | 文件列表为空。 |
| 390 | 不支持的命令。 |
| 391 | 缺少必要参数。 |
| 392 | 参数类型无效。 |
| 400 | 输入法处理器未找到。 |
| 401 | 未知命令名称（method字段取值无法识别）。 |
| 402 | 输入法未绑定。 |
| 420 | click/focus未提供params字段。 |
| 421 | click/focus未提供xpath/nodeid或其值为空字符串。 |
| 422 | click/focus定位字段解析后为空。 |
| 423 | click/focus Web实例不可用。 |
| 424 | click/focus未找到目标元素。 |
| 440 | type未提供params字段。 |
| 441 | type未提供xpath/nodeid。 |
| 442 | type未提供text参数。 |
| 443 | type提供了xpath但值为空。 |
| 444 | type Web实例不可用。 |
| 445 | type未找到目标元素。 |
| 460 | send\_keys未提供params字段。 |
| 461 | send\_keys未提供key字段。 |
| 462 | send\_keys的key为空字符串或无有效按键。 |
| 463 | send\_keys的key值无法识别。 |
| 480 | zoomLevel超出取值范围。 |
| 481 | zoomLevel取值非法（负数或零）。 |
| 482 | 缩放控制已被应用禁用。 |

**说明** 

* 元素定位字段缺失与为空的区分：未提供定位字段、或其值为空字符串，均返回对应命令的\*\_NODEID\_MISSING（如421/441）；提供了xpath但值为空，返回\*\_XPATH\_EMPTY（如443）。
* send\_keys的key字段：未提供key字段返回461；key为空字符串返回462；key值无法识别返回463。
