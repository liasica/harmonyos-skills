---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-identifysensitivecontent
title: @ohos.security.identifySensitiveContent (识别敏感内容)
breadcrumb: API参考 > 系统 > 安全 > Data Protection Kit（数据保护服务） > ArkTS API > @ohos.security.identifySensitiveContent (识别敏感内容)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:abd05203a8382f925032a1497207486cb04431ad98bfecbd8eaaafd9d9f2ecff
---

识别敏感内容功能的实现是通过输入的[扫描策略](js-apis-identifysensitivecontent.md#policy)来检测指定文件中的敏感信息。

说明

本模块首批接口从API version 21开始支持。后续版本的新增接口采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { identifySensitiveContent } from '@kit.DataProtectionKit';
```

## identifySensitiveContent.scanFile

PhonePC/2in1TabletTV

scanFile(filePath: string, identifyPolicies:Array<Policy>): Promise<Array<MatchResult>>

根据设置的策略，识别指定文件中的敏感内容。结果通过Promise方式异步返回。

**需要权限**：ohos.permission.ENTERPRISE\_DATA\_IDENTIFY\_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 识别的文件路径。 |
| identifyPolicies | Array<[Policy](js-apis-identifysensitivecontent.md#policy)> | 是 | 识别的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[MatchResult](js-apis-identifysensitivecontent.md#matchresult)>> | Promise对象。返回敏感内容识别的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DLP服务错误码](errorcode-dlp.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 801 | Capability not supported. |
| 19110001 | Parameter error.Possible causes:1. Incorrect policy format. 2. Invalid parameter range. |
| 19110002 | Sensitive file content identification timed out. |
| 19110003 | The file is not supported. Possible causes:1. The file path does not exist. 2. The file type is not supported. 3. The file permission is not supported. |
| 19110004 | A system error has occurred. |

**示例：**

```
1. import { identifySensitiveContent } from '@kit.DataProtectionKit';

3. let filepath = "file://docs/storage/Users/currentUser/Desktop/test.txt";
4. let policies: Array<identifySensitiveContent.Policy> = [
5. {"sensitiveLabel":"1", "keywords":[], "regex":""}
6. ];
7. try {
8. identifySensitiveContent.scanFile(filepath, policies).then(records => {
9. console.info('scanFile finish');
10. }).catch((err:Error) => {
11. console.error('error message', err.message);
12. })
13. } catch (err) {
14. console.error('error message', err.message);
15. }
```

## Policy

PhonePC/2in1TabletTV

定义敏感内容识别策略。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensitiveLabel | string | 否 | 否 | 表示识别策略的标签。最大30字节。 |
| keywords | Array<string> | 否 | 否 | 表示关键字集合。Array最大50，每个元素最大30字节。 |
| regex | string | 否 | 否 | 表示正则表达式内容。最大512字节。  在输入字符串时，需检查某些特殊字符（如反斜杠 \、双引号 "、换行符等），不会被自动转义，确保字符串的输入效果。 |

## MatchResult

PhonePC/2in1TabletTV

显示敏感内容的识别结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensitiveLabel | string | 是 | 否 | 表示识别策略的标签。 |
| matchContent | string | 是 | 否 | 表示匹配内容。 |
| matchNumber | number | 是 | 否 | 表示识别内容的总数。 |
