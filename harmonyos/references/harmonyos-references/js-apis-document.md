---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-document
title: @ohos.document (文件交互)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > 已停止维护的接口 > @ohos.document (文件交互)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:24f9709d96cd3318829aea10b3bbf893c8213e1751bfa46087149f3f4ad2b78a
---

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口从API version 9开始废弃。不建议使用以下接口，调用以下接口将抛出异常。

## 导入模块

PhonePC/2in1TabletTV

```
1. import document from '@ohos.document';
```

## document.choose(deprecated)

PhonePC/2in1TabletTV

choose(types?: string[]): Promise<string>

通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | string[] | 否 | 限定文件选择的类型 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 异步返回文件URI（注：当前返回错误码） |

**示例：**

```
1. let types: Array<string> = [];
2. document.choose(types);
```

## document.choose(deprecated)

PhonePC/2in1TabletTV

choose(callback:AsyncCallback<string>): void

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 异步获取对应文件URI（注：当前返回错误码） |

**示例：**

```
1. let uri: string = "";
2. document.choose((err: TypeError, uri: string) => {
3. //do something with uri
4. });
```

## document.choose(deprecated)

PhonePC/2in1TabletTV

choose(types:string[], callback:AsyncCallback<string>): void

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | string[] | 是 | 限定选择文件的类型 |
| callback | AsyncCallback<string> | 是 | 异步获取对应文件URI（注：当前返回错误码） |

**示例：**

```
1. let types: Array<string> = [];
2. let uri: string = "";
3. document.choose(types, (err: TypeError, uri: string) => {
4. //do something with uri
5. });
```

## document.show(deprecated)

PhonePC/2in1TabletTV

show(uri:string, type:string):Promise<void>

异步打开URI对应的文件，使用promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待打开的文件URI |
| type | string | 是 | 待打开文件的类型 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise回调返回void表示成功打开文件（注：当前返回错误码） |

**示例：**

```
1. let type: string = "";
2. let uri: string = "";
3. document.show(uri, type);
```

## document.show(deprecated)

PhonePC/2in1TabletTV

show(uri:string, type:string, callback:AsyncCallback<void>): void

异步打开URI对应的文件，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待打开的文件URI |
| type | string | 是 | 待打开文件的类型 |
| callback | AsyncCallback<void> | 是 | 异步打开uri对应文件（注：当前返回错误码） |

**示例：**

```
1. let type: string = "";
2. let uri: string = "";
3. document.show(uri, type, (err: TypeError) => {
4. //do something
5. });
```
