---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-hash
title: @ohos.file.hash (文件哈希处理)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.hash (文件哈希处理)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b87d9186088550ba8394dd205925add2845fc26201fbf67cacc16a4482f56456
---

该模块提供文件哈希处理能力，对文件内容进行哈希处理。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { hash } from '@kit.CoreFileKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. let context = this.context;
7. let pathDir = context.filesDir;
8. }
9. }
```

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：[应用上下文Context-获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。

## hash.hash

PhonePC/2in1TabletTVWearable

hash(path: string, algorithm: string): Promise<string>

计算文件的哈希值，使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回文件的哈希值。表示为十六进制数字串，所有字母均大写。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let filePath = pathDir + "/test.txt";
3. hash.hash(filePath, "sha256").then((str: string) => {
4. console.info("calculate file hash succeed:" + str);
5. }).catch((err: BusinessError) => {
6. console.error("calculate file hash failed with error message: " + err.message + ", error code: " + err.code);
7. });
```

## hash.hash

PhonePC/2in1TabletTVWearable

hash(path: string, algorithm: string, callback: AsyncCallback<string>): void

计算文件的哈希值，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |
| callback | AsyncCallback<string> | 是 | 异步计算文件哈希操作之后的回调函数（其中给定文件哈希值表示为十六进制数字串，所有字母均大写）。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let filePath = pathDir + "/test.txt";
3. hash.hash(filePath, "sha256", (err: BusinessError, str: string) => {
4. if (err) {
5. console.error("calculate file hash failed with error message: " + err.message + ", error code: " + err.code);
6. } else {
7. console.info("calculate file hash succeed:" + str);
8. }
9. });
```

## hash.createHash12+

PhonePC/2in1TabletTVWearable

createHash(algorithm: string): HashStream

创建并返回 HashStream 对象，该对象可用于使用给定的 algorithm 生成哈希摘要。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HashStream](js-apis-file-hash.md#hashstream12) | HashStream 类的实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 13900020 | Invalid argument. |
| 13900042 | Unknown error. |

**示例：**

```
1. // pages/xxx.ets
2. import { fileIo } from '@kit.CoreFileKit';

4. function hashFileWithStream() {
5. const filePath = pathDir + "/test.txt";
6. // 创建文件可读流
7. const rs = fileIo.createReadStream(filePath);
8. // 创建哈希流
9. const hs = hash.createHash('sha256');
10. rs.on('data', (emitData) => {
11. const data = emitData?.data;
12. hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
13. });
14. rs.on('close', async () => {
15. const hashResult = hs.digest();
16. const fileHash = await hash.hash(filePath, 'sha256');
17. console.info(`hashResult: ${hashResult}, fileHash: ${fileHash}`);
18. });
19. }
```

## HashStream12+

PhonePC/2in1TabletTVWearable

HashStream 类是用于创建数据的哈希摘要的实用工具。由 [createHash](js-apis-file-hash.md#hashcreatehash12) 接口获得。

### update12+

PhonePC/2in1TabletTVWearable

update(data: ArrayBuffer): void

使用给定的 data 更新哈希内容，可多次调用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 待计算哈希值的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 13900042 | Unknown error. |

**示例：**

```
1. // 创建哈希流
2. const hs = hash.createHash('sha256');
3. hs.update(new Uint8Array('1234567890'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
4. hs.update(new Uint8Array('abcdefg'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
5. const hashResult = hs.digest();
6. // 88A00F46836CD629D0B79DE98532AFDE3AEAD79A5C53E4848102F433046D0106
7. console.info(`hashResult: ${hashResult}`);
```

### digest12+

PhonePC/2in1TabletTVWearable

digest(): string

计算传递给哈希处理的所有数据的摘要。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回数据的哈希值。该哈希值表示为十六进制数字串，所有字母均大写。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 13900042 | Unknown error. |

**示例：**

```
1. // 创建哈希流
2. const hs = hash.createHash('sha256');
3. hs.update(new Uint8Array('1234567890'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
4. hs.update(new Uint8Array('abcdefg'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
5. const hashResult = hs.digest();
6. // 88A00F46836CD629D0B79DE98532AFDE3AEAD79A5C53E4848102F433046D0106
7. console.info(`hashResult: ${hashResult}`);
```
