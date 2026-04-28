---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream
title: @ohos.util.stream (数据流基类stream)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.stream (数据流基类stream)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cae9ef22b3cd02f2d223c6eca070e9bff33ee7aff2d2f17fd0759034117244c5
---

本模块提供基本流类型的处理能力，支持数据分块读取或写入，避免一次性加载整个数据到内存。

包括可写流（[Writable](js-apis-stream.md#writable)）、可读流（[Readable](js-apis-stream.md#readable)）、双工流（[Duplex](js-apis-stream.md#duplex)）和转换流（[Transform](js-apis-stream.md#transform)）。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { stream  } from '@kit.ArkTS';
```

## Writable

PhonePC/2in1TabletTVWearable

可写入数据的流。可写流允许将数据写入到目标中，这个目标可以是文件、HTTP 响应、标准输出、另一个流等。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| writableObjectMode | boolean | 是 | 否 | 指定可写流是否以对象模式工作。true表示流被配置为对象模式，false表示流处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。 |
| writableHighWatermark | number | 是 | 否 | 定义可写流缓冲区数据量的水位线大小。当前版本不支持开发者自定义修改水位线大小。调用[write()](js-apis-stream.md#write)写入数据后，若缓冲区数据量达到该值，[write()](js-apis-stream.md#write)会返回false。默认值为16 \* 1024字节。 |
| writable | boolean | 是 | 否 | 表示可写流是否处于可写状态。true表示流当前是可写的，false表示流当前不再接受写入操作。 |
| writableLength | number | 是 | 否 | 表示可写流缓冲区中待写入的字节数。 |
| writableCorked | number | 是 | 否 | 表示可写流cork状态计数。值大于0时，可写流处于强制写入缓冲区状态；值为0时，该状态解除。使用[cork()](js-apis-stream.md#cork)方法时计数加一，使用[uncork()](js-apis-stream.md#uncork)方法时计数减一，使用[end()](js-apis-stream.md#end)方法时计数清零。 |
| writableEnded | boolean | 是 | 否 | 表示当前可写流的[end()](js-apis-stream.md#end)是否被调用，该状态不代表数据已经全部写入。true表示[end()](js-apis-stream.md#end)已被调用，false表示[end()](js-apis-stream.md#end)未被调用。 |
| writableFinished | boolean | 是 | 否 | 表示当前可写流是否处于写入完成状态。true表示当前流已处于写入完成状态，false表示当前流的写入操作可能还在进行中。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Writable的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let writableStream = new stream.Writable();
```

### write

PhonePC/2in1TabletTVWearable

write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean

将数据写入流的缓冲区中。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 否 | 需要写入的数据。默认值为undefined。当前版本不支持null、undefined和空字符串。 |
| encoding | string | 否 | 字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 否 | 回调函数。默认不调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可写流的缓冲区中是否还有空间。true表示缓冲区还有空间，false表示流的内部缓冲区数据量已达到设定水位线，不建议继续写入以避免内存溢出。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200035 | The doWrite method has not been implemented. |
| 10200036 | The stream has been ended. |
| 10200037 | The callback is invoked multiple times consecutively. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. console.info("Writable chunk is", chunk); // Writable chunk is test
8. callback();
9. }
10. }

12. let writableStream = new TestWritable();
13. writableStream.write('test', 'utf8');
```

### end

PhonePC/2in1TabletTVWearable

end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable

结束可写流的写入操作。如果属性writableCorked的值大于0，会置零该值并输出缓冲区剩余数据。如果传入chunk参数，则根据实际运行情况，通过write或者doWrite将其作为最后一块数据写入。其中通过doWrite写入时，encoding参数的合法性检查依赖doWrite。end单独使用（不使用write）并传入chunk参数的情况下，必然通过doWrite写入。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 否 | 需要写入的数据。默认为undefined。 |
| encoding | string | 否 | 字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 否 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Writable](js-apis-stream.md#writable) | 返回当前可写流对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200035 | The doWrite method has not been implemented. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. console.info("Writable chunk is", chunk);
8. callback();
9. }
10. // Writable chunk is test
11. // Writable chunk is finish
12. }

14. let writableStream = new TestWritable();
15. writableStream.write('test', 'utf8');
16. writableStream.end('finish', 'utf8', () => {
17. console.info("Writable is end"); // Writable is end
18. });
```

### setDefaultEncoding

PhonePC/2in1TabletTVWearable

setDefaultEncoding(encoding?: string): boolean

设置可写流的默认字符编码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 设置默认字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否设置成功。true表示成功，false表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. callback();
8. }
9. }

11. let writableStream = new TestWritable();
12. let result = writableStream.setDefaultEncoding('utf8');
13. console.info("Writable is result", result); // Writable is result true
```

### cork

PhonePC/2in1TabletTVWearable

cork(): boolean

使后续写入的数据强制写入缓冲区，优化连续写入操作的性能。使用后属性writableCorked的值会加一。建议和[uncork()](js-apis-stream.md#uncork)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置cork状态是否成功。true表示成功，false表示失败。 |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. callback();
8. }
9. }

11. let writableStream = new TestWritable();
12. let result = writableStream.cork();
13. console.info("Writable cork result", result); // Writable cork result true
```

### uncork

PhonePC/2in1TabletTVWearable

uncork(): boolean

解除cork状态，解除后刷新缓冲区数据并写入目标位置。使用后属性writableCorked的值会减一，如果该值降为0，则解除cork状态，否则流依然处于cork状态。建议和[cork()](js-apis-stream.md#cork)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回解除cork状态是否成功。true表示成功，false表示失败。 |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. callback();
8. }
9. }

11. let writableStream = new TestWritable();
12. writableStream.cork();
13. writableStream.write('data1', 'utf8');
14. writableStream.write('data2', 'utf8');
15. writableStream.uncork();
16. writableStream.end();
17. writableStream.on('finish', () => {
18. console.info("all Data is End"); // all Data is End
19. });
```

### on

PhonePC/2in1TabletTVWearable

on(event: string, callback: Callback<emitter.EventData>): void

注册事件处理函数来监听可写流上的不同事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' | 'drain' |'error' | 'finish' 。  - 'close'：完成[end()](js-apis-stream.md#end)调用，结束写入操作，触发该事件。  - 'drain'：在可写流缓冲区中数据清空时触发该事件。  - 'error'：在可写流发生异常时触发该事件。  - 'finish'：在数据缓冲区全部写入到目标后触发该事件。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，返回事件传输的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. callback(new Error());
8. }
9. }

11. let callbackCalled = false;
12. let writable = new TestWritable();
13. writable.on('error', () => {
14. console.info("Writable event test", callbackCalled.toString()); // Writable event test false
15. });
16. writable.write('hello', 'utf8', () => {
17. });
```

### off

PhonePC/2in1TabletTVWearable

off(event: string, callback?: Callback<emitter.EventData>): void

移除通过[on](js-apis-stream.md#on)注册的事件处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' | 'drain' |'error' | 'finish' 。  - 'close'：完成[end()](js-apis-stream.md#end)调用，结束写入操作，触发该事件。  - 'drain'：在可写流缓冲区中数据清空时触发该事件。  - 'error'：在可写流发生异常时触发该事件。  - 'finish'：在数据缓冲区全部写入到目标后触发该事件。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. callback();
8. }
9. }

11. let writableStream = new TestWritable();
12. let testListenerCalled = false;
13. let testListener = () => {
14. testListenerCalled = true;
15. };
16. writableStream.on('finish', testListener);
17. writableStream.off('finish');
18. writableStream.write('test');
19. writableStream.end();
20. setTimeout(() => {
21. console.info("Writable off test", testListenerCalled.toString()); // Writable off test false
22. }, 0);
```

### doInitialize

PhonePC/2in1TabletTVWearable

doInitialize(callback: Function): void

用户实现这个函数。该函数在可写流初始化阶段被调用，无需用户调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class MyWritable extends stream.Writable {
2. doInitialize(callback: Function) {
3. super.doInitialize(callback);
4. console.info("Writable doInitialize"); // Writable doInitialize
5. }

7. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
8. super.doWrite(chunk, encoding, callback);
9. }
10. }

12. new MyWritable();
```

### doWrite

PhonePC/2in1TabletTVWearable

doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void

提供一个数据写出接口供开发者实现，该接口函数会在数据被成功写出时自动调用，无需手动触发。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 是 | 要写出的数据。 |
| encoding | string | 是 | 字符编码类型。当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
7. console.info("Writable chunk is", chunk); // Writable chunk is data
8. callback();
9. }
10. }

12. let writableStream = new TestWritable();
13. writableStream.write('data', 'utf8');
```

### doWritev

PhonePC/2in1TabletTVWearable

doWritev(chunks: string[] | Uint8Array[], callback: Function): void

提供一个数据批量写出接口供使用者实现，该接口函数会在数据被成功写出时自动调用，无需用户手动触发。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunks | string[] | Uint8Array[] | 是 | 待批量写出的数据块数组。 |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestWritable extends stream.Writable {
2. constructor() {
3. super();
4. }

6. doWritev(chunks: string[] | Uint8Array[], callback: Function) {
7. console.info("Writable chunk", chunks);
8. callback();
9. }
10. // Writable chunk data1
11. // Writable chunk data2
12. }

14. let writableStream = new TestWritable();
15. writableStream.write('data1', 'utf8');
16. writableStream.write('data2', 'utf8');
17. writableStream.uncork();
18. writableStream.end();
```

## ReadableOptions

PhonePC/2in1TabletTVWearable

Readable构造函数的选项信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| encoding | string | 否 | 是 | 指定数据的编码格式，如果传入非法字符串，将会在Readable构造函数中抛出异常。  - 支持格式：utf-8、UTF-8、GBK、GB2312、gb2312、GB18030、gb18030、ibm866、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、gbk、big5、euc-jp、iso-2022-jp、shift\_jis、euc-kr、x-mac-cyrillic、utf-16be、utf-16le。  - 默认值是：'utf-8'。 |

## Readable

PhonePC/2in1TabletTVWearable

表示可读取数据的流。可读流用于从数据源（如文件、网络套接字等）读取数据。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| readableObjectMode | boolean | 是 | 否 | 用于指定可读流是否以对象模式工作。true表示流被配置为对象模式，false表示流处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。 |
| readable | boolean | 是 | 否 | 表示可读流是否处于可读状态。true表示流处于可读状态，false表示流中没有更多数据可供读取。 |
| readableHighWatermark | number | 是 | 否 | 定义缓冲区的最大数据量。默认值为16 \* 1024字节。 |
| readableFlowing | boolean | null | 是 | 否 | 表示当前可读流的状态。true表示流处于流动模式，false表示流处于非流动模式。默认值是true。 |
| readableLength | number | 是 | 否 | 表示缓冲区的当前字节数。 |
| readableEncoding | string | null | 是 | 否 | 被解码成字符串时所使用的字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| readableEnded | boolean | 是 | 否 | 表示当前可读流是否已经结束。true表示流已经没有更多数据可读且已结束，false表示流尚未结束，仍有数据可读或等待读取。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Readable的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let readableStream = new stream.Readable();
```

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: ReadableOptions)

Readable的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ReadableOptions](js-apis-stream.md#readableoptions) | 是 | Readable构造函数的选项信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let option : stream.ReadableOptions = {
2. encoding : 'utf-8'
3. };
4. let readableStream = new stream.Readable(option);
```

### read

PhonePC/2in1TabletTVWearable

read(size?: number): string | null

从可读流缓冲区读取数据，并返回读取到的数据，如果未读取到数据，则返回null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 否 | 读取数据的字节数。默认为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | null | 可读流读取出的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200038 | The doRead method has not been implemented. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readableStream = new TestReadable();
11. readableStream.push('test');
12. readableStream.pause();
13. let dataChunk = readableStream.read();
14. console.info('Readable data is', dataChunk); // Readable data is test
```

### resume

PhonePC/2in1TabletTVWearable

resume(): Readable

将流的读取模式从暂停切换到流动模式，可用接口isPaused判断是否已切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Readable](js-apis-stream.md#readable) | 当前可读流本身。 |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readableStream = new TestReadable();
11. readableStream.resume();
12. console.info("Readable test resume", !readableStream.isPaused()); // 切换流动模式成功时，此处日志将打印"Readable test resume true"
```

### pause

PhonePC/2in1TabletTVWearable

pause(): Readable

将流的读取模式从流动切换到暂停模式，可用接口isPaused判断是否已切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Readable](js-apis-stream.md#readable) | 当前可读流本身。 |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readableStream = new TestReadable();
11. readableStream.pause();
12. console.info("Readable test pause", readableStream.isPaused()); // Readable test pause true
```

### setEncoding

PhonePC/2in1TabletTVWearable

setEncoding(encoding?: string): boolean

设置可读流的字符编码。

当缓冲区有数据时，不允许设置字符编码，返回值为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 需要设置的字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否设置成功。true表示设置成功，false表示设置失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readableStream = new TestReadable();
11. let result = readableStream.setEncoding('utf8');
12. console.info("Readable result", result); // Readable result true
```

### isPaused

PhonePC/2in1TabletTVWearable

isPaused(): boolean

检查流是否处于暂停模式，调用[pause()](js-apis-stream.md#pause)后，返回值为true；调用[resume()](js-apis-stream.md#resume)后，返回值为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回流是否处于暂停模式。true表示流处于暂停模式，false表示流未处于暂停模式。 |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readableStream = new TestReadable();
11. console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused false
12. readableStream.pause();
13. console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused true
```

### pipe

PhonePC/2in1TabletTVWearable

pipe(destination: Writable, options?: Object): Writable

将一个可读流与一个可写流连接起来，实现数据的自动传输。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destination | [Writable](js-apis-stream.md#writable) | 是 | 接收数据的可写流。 |
| options | Object | 否 | 预留字段，暂不支持使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Writable](js-apis-stream.md#writable) | 返回当前可写流对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. this.push('test');
8. this.push(null);
9. }
10. }

12. class TestWritable extends stream.Writable {
13. constructor() {
14. super();
15. }

17. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
18. console.info("Readable test pipe", chunk); // Readable test pipe test
19. callback();
20. }
21. }

23. let readable = new TestReadable();
24. let writable = new TestWritable();
25. readable.pipe(writable);
```

### unpipe

PhonePC/2in1TabletTVWearable

unpipe(destination?: Writable): Readable

从可写流中移除所有或指定的已连接的可读流。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destination | [Writable](js-apis-stream.md#writable) | 否 | 从当前可写流中移除指定的这个可读流。默认为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Readable](js-apis-stream.md#readable) | 返回当前可读流对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. this.push('test');
8. this.push(null);
9. }
10. }

12. class TestWritable extends stream.Writable {
13. constructor() {
14. super();
15. }

17. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
18. callback();
19. }
20. }

22. let readable = new TestReadable();
23. let writable = new TestWritable();
24. readable.pipe(writable);
25. readable.unpipe(writable);
26. readable.on('data', () => {
27. console.info("Readable test unpipe data event triggered");
28. });
29. // unpipe成功断开连接之后，data事件将不会触发，不会打印"Readable test unpipe data event triggered"
```

### on

PhonePC/2in1TabletTVWearable

on(event: string, callback: Callback<emitter.EventData>): void

注册事件处理函数来监听可读流上的不同事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' | 'data' |'end' | 'error'|'readable'|'pause'|'resume' 。  - 'close'：完成[push()](js-apis-stream.md#push)调用，传入null值，触发该事件。  - 'data'：当流传递给消费者一个数据块时触发该事件。  - 'end'：完成[push()](js-apis-stream.md#push)调用，传入null值，触发该事件。  - 'error'：流发生异常时触发。  - 'readable'：当有可从流中读取的数据时触发该事件。  - 'pause'：完成[pause()](js-apis-stream.md#pause)调用，触发该事件。  - 'resume'：完成[resume()](js-apis-stream.md#resume)调用，触发该事件。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，返回事件数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. throw new Error('Simulated error');
8. }
9. }

11. let readable = new TestReadable();
12. readable.push('test');
13. readable.on('error', () => {
14. console.info("error event called"); // error event called
15. });
```

### off

PhonePC/2in1TabletTVWearable

off(event: string, callback?: Callback<emitter.EventData>): void

移除通过[on](js-apis-stream.md#on)注册的事件处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' | 'data' |'end' | 'error'|'readable'|'pause'|'resume' 。  - 'close'：完成[push()](js-apis-stream.md#push)调用，传入null值，触发该事件。  - 'data'：当流传递给消费者一个数据块时触发该事件。  - 'end'：完成[push()](js-apis-stream.md#push)调用，传入null值，触发该事件。  - 'error'：流发生异常时触发。  - 'readable'：当有可从流中读取的数据时触发该事件。  - 'pause'：完成[pause()](js-apis-stream.md#pause)调用，触发该事件。  - 'resume'：完成[resume()](js-apis-stream.md#resume)调用，触发该事件。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readable = new TestReadable();

12. function read() {
13. console.info("read() called");
14. }

16. readable.setEncoding('utf8');
17. readable.on('readable', read);
18. readable.off('readable');
19. readable.push('test');
20. // off注销对readable事件的监听后，read函数不会被调用，"read() called"也不会被打印
```

### doInitialize

PhonePC/2in1TabletTVWearable

doInitialize(callback: Function): void

使用者实现这个函数，这个函数在可读流第一次使用[on](js-apis-stream.md#on-1)监听时被调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class MyReadable extends stream.Readable {
2. doInitialize(callback: Function) {
3. super.doInitialize(callback);
4. console.info("Readable doInitialize"); // Readable doInitialize
5. }

7. doRead(size: number) {
8. }
9. }

11. let myReadable = new MyReadable();
12. myReadable.on('data', () => {
13. });
```

### doRead

PhonePC/2in1TabletTVWearable

doRead(size: number): void

数据读取接口，需要在子类中被实现。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 读取数据的字节数。 取值范围：0 <= size <= Number.MAX\_VALUE。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. console.info("doRead called"); // doRead called
8. }
9. }

11. let readable = new TestReadable();
12. readable.on('data', () => {
13. });
```

### push

PhonePC/2in1TabletTVWearable

push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean

将数据推送到可读流缓冲区中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | Uint8Array | string | undefined | null | 是 | 读取的数据。  API version22开始发生兼容性变更，在API version21及之前的版本其类型为：Uint8Array | string | null。 |
| encoding | string | 否 | 数据的编码格式。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可读流的缓冲区中是否还有空间。true表示缓冲区还有空间，false表示流的内部缓冲区已满。输入null时，固定返回false表示推送结束，没有数据块可推送。 |

**示例：**

```
1. class TestReadable extends stream.Readable {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }
8. }

10. let readable = new TestReadable();
11. let testData = 'Hello world';
12. readable.push(testData);
13. console.info("Readable push test", readable.readableLength); // Readable push test 11
```

## Duplex

PhonePC/2in1TabletTVWearable

双工流是一个同时支持可读和可写能力的流。双工流允许数据在两个方向上进行传输，既可以读取数据，又可以写入数据。

Duplex类继承[Readable](js-apis-stream.md#readable)，支持Readable中所有的方法。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| writableObjectMode | boolean | 是 | 否 | 用于指定双工流的写模式是否以对象模式工作。true表示流的写模式被配置为对象模式，false表示流的写模式处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。 |
| writableHighWatermark | number | 是 | 否 | 定义双工流的写模式下缓冲区数据量的水位线大小。当前版本不支持开发者自定义修改设置水位线大小。调用[write()](js-apis-stream.md#write-1)写入后，若缓冲区数据量达到该值，[write()](js-apis-stream.md#write-1)会返回false。默认值为16 \* 1024字节。 |
| writable | boolean | 是 | 否 | 表示双工流是否处于可写状态。true表示当前流是可写的，false表示流当前不再接受写入操作。 |
| writableLength | number | 是 | 否 | 表示双工流缓冲区中待写入的字节数。 |
| writableCorked | number | 是 | 否 | 表示双工流cork状态计数。值大于0时，双工流处于强制写入缓冲区状态，值为0时，该状态解除。使用[cork()](js-apis-stream.md#cork-1)方法时计数加一，使用[uncork()](js-apis-stream.md#uncork-1)方法时计数减一，使用[end()](js-apis-stream.md#end-1)方法时计数清零。 |
| writableEnded | boolean | 是 | 否 | 表示当前双工流的[end()](js-apis-stream.md#end-1)是否被调用，该状态不代表数据已经全部写入。true表示[end()](js-apis-stream.md#end-1)已被调用，false表示[end()](js-apis-stream.md#end-1)未被调用。 |
| writableFinished | boolean | 是 | 否 | 表示当前双工流是否处于写入完成状态。true表示当前流已处于写入完成状态，false表示当前流的写入操作可能还在进行中。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Duplex的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let duplex = new stream.Duplex();
```

### write

PhonePC/2in1TabletTVWearable

write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean

将数据写入流的缓冲区中。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 否 | 需要写入的数据。默认值为undefined。当前版本不支持null、undefined和空字符串。 |
| encoding | string | 否 | 字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 否 | 回调函数。默认不调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可写流的缓冲区中是否还有空间。true表示缓冲区还有空间，false表示流的内部缓冲区数据量已达到设定水位线，不建议继续写入，如果连续调用写入函数，数据仍会被添加到缓冲区中，直到内存溢出为止。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200036 | The stream has been ended. |
| 10200037 | The callback is invoked multiple times consecutively. |
| 10200039 | The doTransform method has not been implemented for a class that inherits from Transform. |

**示例：**

```
1. class TestDuplex extends stream.Duplex {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }

9. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
10. console.info("duplexStream chunk is", chunk); // duplexStream chunk is test
11. callback();
12. }
13. }

15. let duplexStream = new TestDuplex();
16. let result = duplexStream.write('test', 'utf8');
17. console.info("duplexStream result", result); // duplexStream result true
```

### end

PhonePC/2in1TabletTVWearable

end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable

结束双工流的写入操作。如果属性writableCorked的值大于0，会置零该值并输出缓冲区剩余数据。如果传入chunk参数，则根据实际运行情况，通过write或者doWrite将其作为最后一块数据写入。其中通过doWrite写入时，encoding参数的合法性检查依赖doWrite。end单独使用（不使用write）并传入chunk参数的情况下，必然通过doWrite写入。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 否 | 需要写入的数据。默认为undefined。 |
| encoding | string | 否 | 字符编码类型。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 否 | 回调函数。默认不调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Writable](js-apis-stream.md#writable) | 返回可写流对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200039 | The doTransform method has not been implemented for a class that inherits from Transform. |

**示例：**

```
1. class TestDuplex extends stream.Duplex {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }

9. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
10. console.info("Duplex chunk is", chunk); // Duplex chunk is test
11. callback();
12. }
13. }

15. let duplexStream = new TestDuplex();
16. duplexStream.end('test', 'utf8', () => {
17. console.info("Duplex is end"); // Duplex is end
18. });
```

### setDefaultEncoding

PhonePC/2in1TabletTVWearable

setDefaultEncoding(encoding?: string): boolean

设置双工流的默认字符编码，确保在读取数据时正确解析字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 需要设置的默认字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否设置成功。true表示设置成功，false表示设置失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestDuplex extends stream.Duplex {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }

9. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
10. callback();
11. }
12. }

14. let duplexStream = new TestDuplex();
15. let result = duplexStream.setDefaultEncoding('utf8');
16. console.info("duplexStream is result", result); // duplexStream is result true
```

### cork

PhonePC/2in1TabletTVWearable

cork(): boolean

将写入的数据强制写入缓冲区暂存，用来优化连续写入操作的性能。使用后属性writableCorked的值会加一。建议和[uncork()](js-apis-stream.md#uncork-1)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置cork状态是否成功。true表示设置成功，false表示设置失败。 |

**示例：**

```
1. let duplexStream = new stream.Duplex();
2. let result = duplexStream.cork();
3. console.info("duplexStream cork result", result); // duplexStream cork result true
```

### uncork

PhonePC/2in1TabletTVWearable

uncork(): boolean

解除cork状态，解除后将缓冲区中的数据全部刷新，并将其写入目标位置。使用后属性writableCorked的值会减一，如果该值降为0，则解除cork状态，否则流依然处于cork状态。建议和[cork()](js-apis-stream.md#cork-1)成对使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回解除cork状态是否成功。true表示成功，false表示失败。 |

**示例：**

```
1. let dataWritten = '';
2. class TestDuplex extends stream.Duplex {
3. constructor() {
4. super();
5. }

7. doRead(size: number) {
8. }

10. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
11. dataWritten += chunk;
12. callback();
13. }
14. }

16. let duplexStream = new TestDuplex();
17. duplexStream.cork();
18. duplexStream.write('a');
19. duplexStream.write('b');
20. duplexStream.uncork();
21. console.info("Duplex test uncork", dataWritten); // Duplex test uncork ab
```

### doWrite

PhonePC/2in1TabletTVWearable

doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void

数据写出接口是一个由使用者实现的函数，在数据被写出时自动调用，而不需要用户手动调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 是 | 要写出的数据。 |
| encoding | string | 是 | 字符编码类型。当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestDuplex extends stream.Duplex {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }

9. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
10. console.info("duplexStream chunk is", chunk); // duplexStream chunk is data
11. callback();
12. }
13. }

15. let duplexStream = new TestDuplex();
16. duplexStream.write('data', 'utf8');
```

### doWritev

PhonePC/2in1TabletTVWearable

doWritev(chunks: string[] | Uint8Array[], callback: Function): void

数据分批写出接口是一个由使用者实现的函数，在数据被写出时自动调用，而不需要用户手动调用。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunks | string[] | Uint8Array[] | 是 | 待批量写出的数据块数组。 |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestDuplex extends stream.Duplex {
2. constructor() {
3. super();
4. }

6. doRead(size: number) {
7. }

9. doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
10. callback();
11. }

13. doWritev(chunks: string[] | Uint8Array[], callback: Function) {
14. console.info("duplexStream chunk", chunks[0]); // duplexStream chunk data1
15. callback();
16. }
17. }

19. let duplexStream = new TestDuplex();
20. duplexStream.cork();
21. duplexStream.write('data1', 'utf8');
22. duplexStream.write('data2', 'utf8');
23. duplexStream.uncork();
24. duplexStream.end();
```

## Transform

PhonePC/2in1TabletTVWearable

转换流是一个特殊的双工流，支持可读和可写能力的流，可以对数据进行转换并输出结果。Transform类继承[Duplex](js-apis-stream.md#duplex)，支持Duplex中所有的方法。

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Transform的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let transform = new stream.Transform();
```

### doTransform

PhonePC/2in1TabletTVWearable

doTransform(chunk: string, encoding: string, callback: Function): void

对输入的数据块进行转换或处理，并通过回调函数通知操作完成。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | 是 | 需要写入的数据。 |
| encoding | string | 是 | 字符编码类型。当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。 |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestTransform extends stream.Transform {
2. constructor() {
3. super();
4. }

6. doTransform(chunk: string, encoding: string, callback: Function) {
7. let stringChunk = chunk.toString().toUpperCase();
8. console.info("Transform test doTransform", stringChunk); // Transform test doTransform HELLO
9. this.push(stringChunk);
10. callback();
11. }
12. }

14. let tr = new TestTransform();
15. tr.write("hello");
```

### doFlush

PhonePC/2in1TabletTVWearable

doFlush(callback: Function): void

该函数会在流结束时被调用，用于处理剩余的数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. class TestTransform extends stream.Transform {
2. constructor() {
3. super();
4. }

6. doTransform(chunk: string, encoding: string, callback: Function) {
7. callback();
8. }

10. doFlush(callback: Function) {
11. callback(null, 'test');
12. }
13. }

15. let transform = new TestTransform();
16. transform.end('my test');
17. transform.on('data', (data) => {
18. console.info("data is", data.data); // data is test
19. });
```
