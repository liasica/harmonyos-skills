---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-file
title: @system.file (文件存储)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > 已停止维护的接口 > @system.file (文件存储)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e66fb703f288012eb66a679f20b6eaf657c3a91519b5b1b7068491aefd975ac1
---

说明

* 模块维护策略：
  + 对于Lite Wearable设备类型，该模块长期维护，正常使用。
  + 对于支持该模块的其他设备类型，该模块从API Version 10开始不再维护，推荐使用新接口[@ohos.file.fs](js-apis-file-fs.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

WearableLite Wearable

```
1. import file from '@system.file';
```

## file.move

WearableLite Wearable

move(Object): void

将指定文件移动到其他指定位置。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.moveFile](js-apis-file-fs.md#fileiomovefile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 要移动的文件的uri。字符串最大长度为128，且不能包含“"\*+,:;<=>?[]|\x7F”等特殊符号。 |
| dstUri | string | 是 | 文件要移动到的位置的uri。字符串最大长度为128，且不能包含“"\*+,:;<=>?[]|\x7F”等特殊符号。 |
| success | Function | 否 | 接口调用成功的回调函数，返回文件要移动到的位置的uri。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. move() {
3. file.move({
4. srcUri: 'internal://app/myfiles1',
5. dstUri: 'internal://app/myfiles2',
6. success: function(uri) {
7. console.info('call success callback success');
8. },
9. fail: function(data, code) {
10. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
11. },
12. });
13. }
14. }
```

## file.copy

WearableLite Wearable

copy(Object): void

将指定文件拷贝并存储到指定位置。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.copyFile](js-apis-file-fs.md#fileiocopyfile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 要拷贝的文件的uri。 |
| dstUri | string | 是 | 文件要拷贝到的位置的uri。  不支持用应用资源路径或tmp类型的uri。 |
| success | Function | 否 | 接口调用成功的回调函数，返回文件要拷贝到的位置的uri。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. copy() {
3. file.copy({
4. srcUri: 'internal://app/file.txt',
5. dstUri: 'internal://app/file_copy.txt',
6. success: function(uri) {
7. console.info('call success callback success');
8. },
9. fail: function(data, code) {
10. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
11. },
12. });
13. }
14. }
```

## file.list

WearableLite Wearable

list(Object): void

获取指定路径下全部文件的列表。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 目录uri。字符串最大长度为128，且不能包含“"\*+,:;<=>?[]|\x7F”等特殊符号。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| fileList | Array<FileInfo> | 获取的文件列表，其中每个文件的信息的格式为：  {  uri:'file1',  lastModifiedTime:1589965924479,  length:10240,  type: 'file'  } |

**表1** FileInfo

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| uri | string | 文件的 uri。 |
| lastModifiedTime | number | 文件上一次保存时的时间戳，显示从1970/01/01 00:00:00 GMT到当前时间的毫秒数。 |
| length | number | 文件的大小，单位为Byte。 |
| type | string | 文件的类型，可选值为：  - dir：目录；  - file：文件。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. list() {
3. file.list({
4. uri: 'internal://app/pic',
5. success: function(data) {
6. console.info(JSON.stringify(data.fileList));
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## file.get

WearableLite Wearable

get(Object): void

获取指定本地文件的信息。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.stat](js-apis-file-fs.md#fileiostat)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 文件的uri。 |
| recursive | boolean | 否 | 是否进行递归获取子目录文件列表，true为进行该操作，缺省为false。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| uri | string | 文件的uri。 |
| length | number | 文件长度，单位为Byte。 |
| lastModifiedTime | number | 文件保存时的时间戳，从1970/01/01 00:00:00到当前时间的毫秒数。 |
| type | string | 文件类型，可选值为：  - dir：目录；  - file：文件。 |
| subFiles | Array | 文件列表。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. get() {
3. file.get({
4. uri: 'internal://app/file',
5. success: function(data) {
6. console.info(data.uri);
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## file.delete

WearableLite Wearable

delete(Object): void

删除本地文件。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.unlink](js-apis-file-fs.md#fileiounlink)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 删除文件的uri，不能是应用资源路径。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误。 |
| 300 | I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. delete() {
3. file.delete({
4. uri: 'internal://app/my_file',
5. success: function() {
6. console.info('call delete success.');
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## file.writeText

WearableLite Wearable

writeText(Object): void

写文本内容到指定文件。仅支持文本文档读写。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.write](js-apis-file-fs.md#fileiowrite)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 本地文件uri，如果文件不存在会创建文件。 |
| text | string | 是 | 写入的字符串。 |
| encoding | string | 否 | 编码格式，默认为UTF-8。 |
| append | boolean | 否 | 是否追加模式，默认为false。true为追加，false为不追加。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误。 |
| 300 | I/O错误。 |

**示例：**

```
1. export default {
2. writeText() {
3. file.writeText({
4. uri: 'internal://app/test.txt',
5. text: 'Text that just for test.',
6. success: function() {
7. console.info('call writeText success.');
8. },
9. fail: function(data, code) {
10. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
11. },
12. });
13. }
14. }
```

## file.writeArrayBuffer

WearableLite Wearable

writeArrayBuffer(Object): void

写Buffer内容到指定文件。仅支持文本文档读写。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.write](js-apis-file-fs.md#fileiowrite)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 本地文件uri，如果文件不存在会创建文件。 |
| buffer | Uint8Array | 是 | 写入的Buffer。 |
| position | number | 否 | 文件开始写入数据的位置的偏移量，单位为Byte，默认为0。 |
| append | boolean | 否 | 是否追加模式，默认为false。当设置为true时，position参数无效。true为追加，false为不追加。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |

**示例：**

```
1. export default {
2. writeArrayBuffer() {
3. file.writeArrayBuffer({
4. uri: 'internal://app/test',
5. buffer: new Uint8Array(8),// buffer为Uint8Array类型
6. success: function() {
7. console.info('call writeArrayBuffer success.');
8. },
9. fail: function(data, code) {
10. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
11. },
12. });
13. }
14. }
```

## file.readText

WearableLite Wearable

readText(Object): void

从指定文件中读取文本内容。仅支持文本文档读写。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.readText](js-apis-file-fs.md#fileioreadtext)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 本地文件uri。 |
| encoding | string | 否 | 编码格式，缺省为UTF-8。 |
| position | number | 否 | 读取的起始位置，单位为Byte，默认值为文件的起始位置。 |
| length | number | 否 | 读取的长度，单位为Byte，默认值为4096。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| text | string | 读取到的文本内容。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |
| 302 | 要读取的文件内容超过4KB。 |

**示例：**

```
1. export default {
2. readText() {
3. file.readText({
4. uri: 'internal://app/text.txt',
5. success: function(data) {
6. console.info('call readText success: ' + data.text);
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## file.readArrayBuffer

WearableLite Wearable

readArrayBuffer(Object): void

从指定文件中读取Buffer内容。仅支持文本文档读写。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.read](js-apis-file-fs.md#fileioread)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 本地文件uri。 |
| position | number | 否 | 读取的起始位置，单位为Byte，缺省为文件的起始位置。 |
| length | number | 否 | 需要读取的长度，单位为Byte，缺省则读取到文件结尾。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

success返回值：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| buffer | Uint8Array | 读取到的文件内容。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. readArrayBuffer() {
3. file.readArrayBuffer({
4. uri: 'internal://app/test',
5. position: 10,
6. length: 200,
7. success: function(data) {
8. console.info('call readArrayBuffer success: ' + data.buffer);
9. },
10. fail: function(data, code) {
11. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
12. },
13. });
14. }
15. }
```

## file.access

WearableLite Wearable

access(Object): void

判断指定文件或目录是否存在。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.access](js-apis-file-fs.md#fileioaccess)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 目录或文件uri。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O 错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. access() {
3. file.access({
4. uri: 'internal://app/test',
5. success: function() {
6. console.info('call access success.');
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## file.mkdir

WearableLite Wearable

mkdir(Object): void

创建指定目录。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.mkdir](js-apis-file-fs.md#fileiomkdir)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 目录的uri路径。 |
| recursive | boolean | 否 | 是否递归创建该目录的上级目录，缺省为false。true为递归创建，false是不递归创建。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O 错误。 |

**示例：**

```
1. export default {
2. mkdir() {
3. file.mkdir({
4. uri: 'internal://app/test_directory',
5. success: function() {
6. console.info('call mkdir success.');
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## file.rmdir

WearableLite Wearable

rmdir(Object): void

删除指定目录。

说明

除Lite Wearable外，从API version 10开始废弃，请使用[fileIo.rmdir](js-apis-file-fs.md#fileiormdir)替代。

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 目录的uri路径。 |
| recursive | boolean | 否 | 是否递归删除子文件和子目录，缺省为false。true为递归删除，false为不递归删除。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 202 | 出现参数错误。 |
| 300 | 出现I/O 错误。 |
| 301 | 文件或目录不存在。 |

**示例：**

```
1. export default {
2. rmdir() {
3. file.rmdir({
4. uri: 'internal://app/test_directory',
5. success: function() {
6. console.info('call rmdir success.');
7. },
8. fail: function(data, code) {
9. console.error('call fail callback fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```
