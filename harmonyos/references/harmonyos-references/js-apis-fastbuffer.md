---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fastbuffer
title: @ohos.fastbuffer (FastBuffer)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.fastbuffer (FastBuffer)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5184a23de6412933956abc64ec485bf7bfbb693a8cff0deec0e5480e74a35ee8
---

FastBuffer对象是更高效的Buffer容器，用于表示固定长度的字节序列，是专门存放二进制数据的缓存区。

FastBuffer通过from构造时，仅支持FastBuffer、Uint8Array、string、Array、ArrayBuffer类型的参数。

需要高性能处理大型二进制数据（如图片、文件传输、网络通信等）时，推荐使用FastBuffer。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { fastbuffer } from '@kit.ArkTS';
```

## BufferEncoding

PhonePC/2in1TabletTVWearable

type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex'

表示支持的编码格式类型。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| 'ascii' | 表示ascii格式。 |
| 'utf8' | 表示utf8格式。 |
| 'utf-8' | 表示utf8格式。 |
| 'utf16le' | 表示utf16小端序格式。 |
| 'ucs2' | utf16le格式的别名。 |
| 'ucs-2' | utf16le格式的别名。 |
| 'base64' | 表示base64格式。 |
| 'base64url' | 表示base64url格式。 |
| 'latin1' | iso-8859-1的别名，向下兼容ascii格式。 |
| 'binary' | 表示二进制格式。 |
| 'hex' | 表示十六进制格式。 |

## fastbuffer.alloc

PhonePC/2in1TabletTVWearable

alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer

创建指定字节长度的FastBuffer对象并初始化。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32\_MAX。 |
| fill | string | FastBuffer | number | 否 | 填充至新缓存区的值，默认值：0。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 编码格式（当fill为string时，才有意义）。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 返回一个FastBuffer对象。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.alloc(5);
4. let buf2 = fastbuffer.alloc(5, 'a');
5. let buf3 = fastbuffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');
6. console.info(buf2.toString());
7. // 输出结果：aaaaa
8. console.info(buf3.toString());
9. // 输出结果：hello world
```

## fastbuffer.allocUninitializedFromPool

PhonePC/2in1TabletTVWearable

allocUninitializedFromPool(size: number): FastBuffer

从缓冲池中创建指定大小未初始化的FastBuffer对象，需要使用[fill](js-apis-fastbuffer.md#fill)函数来初始化FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32\_MAX。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 未初始化的Buffer实例。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(10);
4. buf.fill(0);
5. // "buf":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## fastbuffer.allocUninitialized

PhonePC/2in1TabletTVWearable

allocUninitialized(size: number): FastBuffer

创建指定大小未初始化的FastBuffer对象，需要使用[fill](js-apis-fastbuffer.md#fill)函数来初始化FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32\_MAX。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 未初始化的FastBuffer实例。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitialized(10);
4. buf.fill(0);
5. // "buf":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## fastbuffer.byteLength

PhonePC/2in1TabletTVWearable

byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number

根据不同的编码格式，返回指定字符串的字节数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer | 是 | 指定字符串。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定字符串的字节数。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let str = 'hello world';
4. console.info(`${str}: ${str.length} characters, ${fastbuffer.byteLength(str, 'utf-8')} bytes`);
5. // 输出结果：hello world: 11 characters, 11 bytes

7. str = '\u00bd + \u00bc = \u00be';
8. console.info(`${str}: ${str.length} characters, ${fastbuffer.byteLength(str, 'utf-8')} bytes`);
9. // 输出结果：½ + ¼ = ¾: 9 characters, 12 bytes
```

## fastbuffer.compare

PhonePC/2in1TabletTVWearable

compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1

返回两个FastBuffer对象的比较结果，通常用于对FastBuffer对象数组进行排序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf1 | [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | Uint8Array | 是 | 待比较的第一个对象。 |
| buf2 | [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | Uint8Array | 是 | 待比较的第二个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| -1 | 0 | 1 | 如果buf1与buf2相同，则返回0。  如果排序时buf1位于buf2之后，则返回1。  如果排序时buf1位于buf2之前，则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from('1234');
4. let buf2 = fastbuffer.from('0123');
5. let res = fastbuffer.compare(buf1, buf2);

7. console.info(Number(res).toString());
8. // 输出结果：1
```

## fastbuffer.concat

PhonePC/2in1TabletTVWearable

concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer

将数组中指定字节长度的内容复制到新的FastBuffer对象中并返回拼接后的FastBuffer对象。

当数组中所有对象的长度总和大于totalLength时，返回结果的长度将被截断为totalLength。

当数组中所有对象的长度总和小于totalLength时，返回结果的多余部分将会被填充为0。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | [FastBuffer](js-apis-fastbuffer.md#fastbuffer)[] | Uint8Array[] | 是 | 实例数组。 |
| totalLength | number | 否 | 需要复制的总字节长度，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 返回新的FastBuffer对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from("1234");
4. let buf2 = fastbuffer.from("abcd");
5. let buf = fastbuffer.concat([buf1, buf2]);
6. console.info(buf.toString('hex'));
7. // 输出结果：3132333461626364
```

## fastbuffer.from

PhonePC/2in1TabletTVWearable

from(array: number[]): FastBuffer

根据指定数组创建新的FastBuffer对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | number[] | 是 | 指定数组，数组内各元素的取值范围为[0, 255]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 新的FastBuffer对象。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
4. console.info(buf.toString('hex'));
5. // 输出结果：627566666572
```

## fastbuffer.from

PhonePC/2in1TabletTVWearable

from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer

创建与arrayBuffer共享内存的指定长度的FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayBuffer | ArrayBuffer | SharedArrayBuffer | 是 | 实例对象。 |
| byteOffset | number | 否 | 字节偏移量，默认值：0。 |
| length | number | 否 | 字节长度， 默认值:（arrayBuffer.byteLength - byteOffset）。取值范围：0 <= length <= arrayBuffer.byteLength - byteOffset。传入null时返回空FastBuffer。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 返回一个FastBuffer对象，该对象与入参对象arrayBuffer共享相同的内存区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let ab = new ArrayBuffer(10);
4. let buf = fastbuffer.from(ab, 0, 2);
5. console.info(buf.length.toString());
6. // 输出结果：2
```

## fastbuffer.from

PhonePC/2in1TabletTVWearable

from(buffer: FastBuffer | Uint8Array): FastBuffer

当入参为FastBuffer对象时，创建新的FastBuffer对象并复制入参FastBuffer对象的数据，然后返回新对象。

当入参为Uint8Array对象时，基于Uint8Array对象的内存创建新的FastBuffer对象并返回，保持数据的内存关联。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | Uint8Array | 是 | 对象数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 返回新的FastBuffer对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. // 以FastBuffer对象类型进行创建新的FastBuffer对象
4. let buf1 = fastbuffer.from('buffer');
5. let buf2 = fastbuffer.from(buf1);
6. console.info(buf2.toString());
7. // 输出结果：buffer

9. // 以Uint8Array对象类型进行创建FastBuffer对象，保持对象间内存共享
10. let uint8Array = new Uint8Array(10);
11. let buf3 = fastbuffer.from(uint8Array);
12. buf3.fill(1)
13. console.info("uint8Array:", uint8Array)
14. // 输出结果：1,1,1,1,1,1,1,1,1,1
```

## fastbuffer.from

PhonePC/2in1TabletTVWearable

from(value: string, encoding?: BufferEncoding): FastBuffer

根据指定编码格式的字符串，创建新的FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 字符串。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 返回新的FastBuffer对象。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from('this is a test');
4. let buf2 = fastbuffer.from('7468697320697320612074c3a97374', 'hex');

6. console.info(buf1.toString());
7. // 输出结果：this is a test
8. console.info(buf2.toString());
9. // 输出结果：this is a tést
```

## fastbuffer.isBuffer

PhonePC/2in1TabletTVWearable

isBuffer(obj: Object): boolean

判断obj是否为FastBuffer。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object | 是 | 判断对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果obj是FastBuffer，则返回true，否则返回false。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let result = fastbuffer.isBuffer(fastbuffer.alloc(10)); // 10: fastbuffer size
4. console.info("result = " + result);
5. // 输出结果：result = true
6. let result1 = fastbuffer.isBuffer(fastbuffer.from('foo'));
7. console.info("result1 = " + result1);
8. // 输出结果：result1 = true
9. let result2 = fastbuffer.isBuffer('a string');
10. console.info("result2 = " + result2);
11. // 输出结果：result2 = false
12. let result3 = fastbuffer.isBuffer([]);
13. console.info("result3 = " + result3);
14. // 输出结果：result3 = false
15. let result4 = fastbuffer.isBuffer(new Uint8Array(1024));
16. console.info("result4 = " + result4);
17. // 输出结果：result4 = false
```

## fastbuffer.isEncoding

PhonePC/2in1TabletTVWearable

isEncoding(encoding: string): boolean

判断encoding是否为支持的编码格式。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 是 | 编码格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是支持的编码格式返回true，反之则返回false。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. console.info(fastbuffer.isEncoding('utf-8').toString());
4. // 输出结果：true
5. console.info(fastbuffer.isEncoding('hex').toString());
6. // 输出结果：true
7. console.info(fastbuffer.isEncoding('utf/8').toString());
8. // 输出结果：false
9. console.info(fastbuffer.isEncoding('').toString());
10. // 输出结果：false
```

## fastbuffer.transcode

PhonePC/2in1TabletTVWearable

transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer

将FastBuffer或Uint8Array对象从fromEnc编码转换为toEnc编码。

fastbuffer.transcode支持的编码：'ascii' | 'utf8' | 'utf16le'| 'ucs2' | 'latin1'| 'binary'。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | Uint8Array | 是 | 实例对象。 |
| fromEnc | string | 是 | 当前编码格式。支持的格式范围为BufferEncoding。传入空字符串时，表示使用编码格式'utf8'。 |
| toEnc | string | 是 | 目标编码。 支持的格式范围为[BufferEncoding](js-apis-fastbuffer.md#bufferencoding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 将当前编码转换成目标编码，并返回一个新的FastBuffer对象。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let newBuf = fastbuffer.transcode(fastbuffer.from('buffer'), 'utf-8', 'ascii');
4. console.info("newBuf = " + newBuf.toString('ascii'));
5. // 输出结果：newBuf = buffer
```

## FastBuffer

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | FastBuffer对象的字节长度。 |
| buffer | ArrayBuffer | 是 | 否 | ArrayBuffer对象。 |
| byteOffset | number | 是 | 否 | 当前Buffer所在内存池的偏移量。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from("1236");
4. console.info(JSON.stringify(buf.length));
5. // 输出结果：4
6. let arrayBuffer = buf.buffer;
7. console.info(JSON.stringify(new Uint8Array(arrayBuffer)));
8. // 输出结果：{"0":49,"1":50,"2":51,"3":54}
9. console.info(JSON.stringify(buf.byteOffset));
10. // 输出结果：0
```

### compare

PhonePC/2in1TabletTVWearable

compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1

比较当前对象this与目标对象target，并返回比较结果。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | Uint8Array | 是 | 要比较的实例对象。 |
| targetStart | number | 否 | target实例中开始的偏移量。默认值：0。 0 <= targetStart <= target.length。 |
| targetEnd | number | 否 | target实例中结束的偏移量（不包含结束位置）。默认值：目标对象的字节长度。取值范围：0 <= targetEnd <= target.length。 |
| sourceStart | number | 否 | this实例中开始的偏移量。默认值：0。取值范围：0 <= sourceStart <= this.length。 |
| sourceEnd | number | 否 | this实例中结束的偏移量（不包含结束位置）。默认值：当前对象的字节长度。取值范围：0 <= sourceEnd <= this.length。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| -1 | 0 | 1 | 返回比较结果。  -1：当前排列在目标前；  0：当前与目标相同；  1：当前排列在目标后。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
4. let buf2 = fastbuffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

6. console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
7. // 输出结果：0
8. console.info(buf1.compare(buf2, 0, 6, 4).toString());
9. // 输出结果：-1
10. console.info(buf1.compare(buf2, 5, 6, 5).toString());
11. // 输出结果：1
```

### copy

PhonePC/2in1TabletTVWearable

copy(target: FastBuffer| Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number

将this实例中指定位置的数据复制到target的指定位置上，并返回复制的字节总长度。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | Uint8Array | 是 | 要复制到的Buffer或Uint8Array实例。 |
| targetStart | number | 否 | target实例中开始写入的偏移量。默认值：0。取值范围：0 <= targetStart <= UINT32\_MAX。 |
| sourceStart | number | 否 | this实例中开始复制的偏移量。默认值: 0。取值范围：0 <= sourceStart <= UINT32\_MAX。 |
| sourceEnd | number | 否 | this实例中结束复制的偏移量（不包含结束位置）。默认值：当前对象的字节长度。取值范围：0 <= sourceEnd <= this.length。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 复制的字节总长度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.allocUninitializedFromPool(26);
4. let buf2 = fastbuffer.allocUninitializedFromPool(26).fill('!');

6. for (let i = 0; i < 26; i++) {
7. buf1.writeInt8(i + 97, i);
8. }

10. buf1.copy(buf2, 8, 16, 20);
11. console.info(buf2.toString('ascii', 0, 25));
12. // 输出结果：!!!!!!!!qrst!!!!!!!!!!!!!
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[number, number]>

返回一个包含key值和value值的迭代器。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[number, number]> | 包含key和value的迭代器，同时两者皆为number类型。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from('buffer');
4. let pair = buf.entries();
5. let next: IteratorResult<Object[]> = pair.next();
6. while (!next.done) {
7. console.info("fastbuffer: " + next.value);
8. /*
9. 输出结果：buffer: 0,98
10. fastbuffer: 1,117
11. fastbuffer: 2,102
12. fastbuffer: 3,102
13. fastbuffer: 4,101
14. fastbuffer: 5,114
15. */
16. next = pair.next();
17. }
```

### equals

PhonePC/2in1TabletTVWearable

equals(otherBuffer: Uint8Array | FastBuffer): boolean

逐字节比较this和otherBuffer是否相等。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| otherBuffer | Uint8Array | FastBuffer | 是 | 比较的目标对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 若this和otherBuffer逐字节相等则返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from('ABC');
4. let buf2 = fastbuffer.from('414243', 'hex');
5. let buf3 = fastbuffer.from('ABCD');

7. console.info(buf1.equals(buf2).toString());
8. // 输出结果：true
9. console.info(buf1.equals(buf3).toString());
10. // 输出结果：false
```

### fill

PhonePC/2in1TabletTVWearable

fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer

使用value填充当前对象指定位置的数据，默认为循环填充，并返回填充后的FastBuffer对象。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | FastBuffer | Uint8Array | number | 是 | 用于填充的值。 |
| offset | number | 否 | 起始偏移量。默认值：0。取值范围：0 <= offset <= this.length。 |
| end | number | 否 | 结束偏移量（不包含结束位置）。 默认值：当前对象的字节长度。取值范围：0 <= end <= this.length。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 字符编码格式（value为string才有意义）。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FastBuffer](js-apis-fastbuffer.md#fastbuffer) | 返回填充后的FastBuffer对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let b = fastbuffer.allocUninitializedFromPool(50).fill('h');
4. console.info(b.toString());
5. // 输出结果：hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
```

### includes

PhonePC/2in1TabletTVWearable

includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean

检查FastBuffer对象是否包含value值。

若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。

当byteOffset大于等于this.length时，返回false。当byteOffset小于等于-this.length，查找整个FastBuffer中是否存在value。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | FastBuffer | Uint8Array | 是 | 要搜索的内容。 |
| byteOffset | number | 否 | 字节偏移量。若为正数，则从0开始计算偏移量；若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。默认值：0。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 字符编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 若FastBuffer对象包含value值时返回true，否则为false。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from('this is a buffer');
4. console.info(buf.includes('this').toString());
5. // 输出结果：true
6. console.info(buf.includes('be').toString());
7. // 输出结果：false
```

### indexOf

PhonePC/2in1TabletTVWearable

indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number

返回当前对象中首次出现value的索引，如果不包含value，则返回-1。

若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。

当byteOffset大于等于this.length时，返回-1。当byteOffset小于等于-this.length，返回整个FastBuffer中首次出现value的索引。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | FastBuffer | Uint8Array | 是 | 要查找的内容。 |
| byteOffset | number | 否 | 字节偏移量。若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。默认值：0。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 字符编码格式。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回第一次出现的位置。 |

**示例**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from('this is a buffer');
4. console.info(buf.indexOf('this').toString());
5. // 输出结果：0
6. console.info(buf.indexOf('is').toString());
7. // 输出结果：2
```

### keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<number>

返回一个包含key值的迭代器。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<number> | 返回一个包含key值的迭代器。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from('buffer');
4. let keys = buf.keys();
5. for (const key of keys) {
6. console.info(key.toString());
7. }
8. /*
9. 输出结果：0
10. 1
11. 2
12. 3
13. 4
14. 5
15. */
```

### values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<number>

返回一个包含value的迭代器。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<number> | 迭代器。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from('buffer');
4. let pair = buf1.values()
5. let next:IteratorResult<number> = pair.next()
6. while (!next.done) {
7. console.info(next.value.toString());
8. /*
9. 输出结果：98
10. 117
11. 102
12. 102
13. 101
14. 114
15. */
16. next = pair.next();
17. }
```

### lastIndexOf

PhonePC/2in1TabletTVWearable

lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number

返回当前对象中最后一次出现value的索引，如果对象不包含value，则返回-1。

若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。

当byteOffset大于等于this.length时，返回整个FastBuffer中最后一次出现value的索引。当byteOffset小于等于-this.length时，返回-1。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | FastBuffer | Uint8Array | 是 | 要搜索的内容。 |
| byteOffset | number | 否 | 字节偏移量。若byteOffset为正数，则从0开始计算偏移量；如果为负数，则从末尾开始计算偏移量。默认值：this.length - 1。 |
| encoding | [BufferEncoding](js-apis-fastbuffer.md#bufferencoding) | 否 | 字符编码格式。默认值：'utf8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 最后一次出现value值的索引。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from('this buffer is a buffer');
4. console.info(buf.lastIndexOf('this').toString());
5. // 输出结果：0
6. console.info(buf.lastIndexOf('buffer').toString());
7. // 输出结果：17
```

### readBigInt64BE

PhonePC/2in1TabletTVWearable

readBigInt64BE(offset?: number): bigint

从指定的offset处读取有符号的大端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
4. 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
5. console.info(buf.readBigInt64BE(0).toString());
6. // 输出结果：7161960797921896816
```

### readBigInt64LE

PhonePC/2in1TabletTVWearable

readBigInt64LE(offset?: number): bigint

从指定的offset处读取有符号的小端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
4. 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
5. console.info(buf.readBigInt64LE(0).toString());
6. // 输出结果：8100120198111388771
```

### readBigUInt64BE

PhonePC/2in1TabletTVWearable

readBigUInt64BE(offset?: number): bigint

从指定的offset处读取无符号的大端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
4. 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
5. console.info(buf.readBigUInt64BE(0).toString());
6. // 输出结果：7161960797921896816
```

### readBigUInt64LE

PhonePC/2in1TabletTVWearable

readBigUInt64LE(offset?: number): bigint

从指定的offset处读取无符号的小端序64位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
4. 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
5. console.info(buf.readBigUInt64LE(0).toString());
6. // 输出结果：8100120198111388771
```

### readDoubleBE

PhonePC/2in1TabletTVWearable

readDoubleBE(offset?: number): number

从指定的offset处读取64位大端序双精度值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
4. console.info(buf.readDoubleBE(0).toString());
5. // 输出结果：8.20788039913184e-304
```

### readDoubleLE

PhonePC/2in1TabletTVWearable

readDoubleLE(offset?: number): number

从指定的offset处读取64位小端序双精度值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 8，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
4. console.info(buf.readDoubleLE(0).toString());
5. // 输出结果：5.447603722011605e-270
```

### readFloatBE

PhonePC/2in1TabletTVWearable

readFloatBE(offset?: number): number

从指定的offset处读取32位大端序浮点数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
4. console.info(buf.readFloatBE(0).toString());
5. // 输出结果：2.387939260590663e-38
```

### readFloatLE

PhonePC/2in1TabletTVWearable

readFloatLE(offset?: number): number

从指定的offset处读取32位小端序浮点数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
4. console.info(buf.readFloatLE(0).toString());
5. // 输出结果：1.539989614439558e-36
```

### readInt8

PhonePC/2in1TabletTVWearable

readInt8(offset?: number): number

从指定的offset处读取有符号的8位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 1，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([-1, 5]);
4. console.info(buf.readInt8(0).toString());
5. // 输出结果：-1
6. console.info(buf.readInt8(1).toString());
7. // 输出结果：5
```

### readInt16BE

PhonePC/2in1TabletTVWearable

readInt16BE(offset?: number): number

从指定的offset处读取有符号的大端序16位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0, 5]);
4. console.info(buf.readInt16BE(0).toString());
5. // 输出结果：5
```

### readInt16LE

PhonePC/2in1TabletTVWearable

readInt16LE(offset?: number): number

从指定的offset处读取有符号的小端序16位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0, 5]);
4. console.info(buf.readInt16LE(0).toString());
5. // 输出结果：1280
```

### readInt32BE

PhonePC/2in1TabletTVWearable

readInt32BE(offset?: number): number

从指定的offset处读取有符号的大端序32位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0, 0, 0, 5]);
4. console.info(buf.readInt32BE(0).toString());
5. // 输出结果：5
```

### readInt32LE

PhonePC/2in1TabletTVWearable

readInt32LE(offset?: number): number

从指定的offset处读取有符号的小端序32位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0, 0, 0, 5]);
4. console.info(buf.readInt32LE(0).toString());
5. // 输出结果：83886080
```

### readIntBE

PhonePC/2in1TabletTVWearable

readIntBE(offset: number, byteLength: number): number

从指定的offset处读取byteLength个字节，并将结果解释为支持最高48位精度的大端序、二进制补码有符号值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。 |
| byteLength | number | 是 | 读取的字节数。取值范围：1 <= byteLength <= 6。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from("ab");
4. let num = buf.readIntBE(0, 1);
5. console.info(num.toString());
6. // 输出结果：97
```

### readIntLE

PhonePC/2in1TabletTVWearable

readIntLE(offset: number, byteLength: number): number

从指定的offset处读取byteLength个字节，并将结果解释为支持最高48位精度的小端序、二进制补码有符号值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。 |
| byteLength | number | 是 | 读取的字节数。取值范围：1 <= byteLength <= 6。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
4. console.info(buf.readIntLE(0, 6).toString(16));
5. // 输出结果：-546f87a9cbee
```

### readUInt8

PhonePC/2in1TabletTVWearable

readUInt8(offset?: number): number

从offset处读取8位无符号整型数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 1，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([1, -2]);
4. console.info(buf.readUInt8(0).toString());
5. // 输出结果：1
6. console.info(buf.readUInt8(1).toString());
7. // 输出结果：254
```

### readUInt16BE

PhonePC/2in1TabletTVWearable

readUInt16BE(offset?: number): number

从指定的offset处读取无符号的大端序16位整数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56]);
4. console.info(buf.readUInt16BE(0).toString(16));
5. // 输出结果：1234
6. console.info(buf.readUInt16BE(1).toString(16));
7. // 输出结果：3456
```

### readUInt16LE

PhonePC/2in1TabletTVWearable

readUInt16LE(offset?: number): number

从指定的offset处的buf读取无符号的小端序16位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 2，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56]);
4. console.info(buf.readUInt16LE(0).toString(16));
5. // 输出结果：3412
6. console.info(buf.readUInt16LE(1).toString(16));
7. // 输出结果：5634
```

### readUInt32BE

PhonePC/2in1TabletTVWearable

readUInt32BE(offset?: number): number

从指定的offset处的buf读取无符号的大端序32位整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78]);
4. console.info(buf.readUInt32BE(0).toString(16));
5. // 输出结果：12345678
```

### readUInt32LE

PhonePC/2in1TabletTVWearable

readUInt32LE(offset?: number): number

从指定的offset处的buf读取无符号的小端序32位整数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 偏移量。取值范围：0 <= offset <= this.length - 4，默认值：0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78]);
4. console.info(buf.readUInt32LE(0).toString(16));
5. // 输出结果：78563412
```

### readUIntBE

PhonePC/2in1TabletTVWearable

readUIntBE(offset: number, byteLength: number): number

从指定的offset处的buf读取byteLength个字节，并将结果解释为支持最高48位精度的无符号大端序整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。 |
| byteLength | number | 是 | 要读取的字节数。读取的字节数。取值范围：1 <= byteLength <= 6。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。当offset为小数时，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
4. console.info(buf.readUIntBE(0, 6).toString(16));
5. // 输出结果：1234567890ab
```

### readUIntLE

PhonePC/2in1TabletTVWearable

readUIntLE(offset: number, byteLength: number): number

从指定的offset处的buf读取byteLength个字节，并将结果解释为支持最高48位精度的无符号小端序整数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 偏移量。取值范围：0 <= offset <= this.length - byteLength，默认值：0。 |
| byteLength | number | 是 | 读取的字节数。取值范围：1 <= byteLength <= 6。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 读取出的内容。当offset为小数时，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
4. console.info(buf.readUIntLE(0, 6).toString(16));
5. // 输出结果：ab9078563412
```

### subarray

PhonePC/2in1TabletTVWearable

subarray(start?: number, end?: number): FastBuffer

截取当前对象指定位置的数据并返回。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 否 | 截取开始位置。默认值：0。 |
| end | number | 否 | 截取结束位置（不包含结束位置）。默认值：当前对象的字节长度。取值范围：start <= end <= this.length。传入null时返回空FastBuffer。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FastBuffer | 返回新的FastBuffer对象。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.allocUninitializedFromPool(26);

5. for (let i = 0; i < 26; i++) {
6. buf1.writeInt8(i + 97, i);
7. }
8. const buf2 = buf1.subarray(0, 3);
9. console.info(buf2.toString('ascii', 0, buf2.length));
10. // 输出结果: abc
```

### swap16

PhonePC/2in1TabletTVWearable

swap16(): FastBuffer

将当前对象转换为无符号的16位整数数组，并交换字节顺序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FastBuffer | 交换之后的FastBuffer对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200009 | The fastbuffer size must be a multiple of 16-bits. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
4. console.info(buf1.toString('hex'));
5. // 输出结果：0102030405060708
6. buf1.swap16();
7. console.info(buf1.toString('hex'));
8. // 输出结果：0201040306050807
```

### swap32

PhonePC/2in1TabletTVWearable

swap32(): FastBuffer

将当前对象转换为无符号的32位整数数组，并交换字节顺序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FastBuffer | 交换之后的FastBuffer对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200009 | The fastbuffer size must be a multiple of 32-bits. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
4. console.info(buf1.toString('hex'));
5. // 输出结果：0102030405060708
6. buf1.swap32();
7. console.info(buf1.toString('hex'));
8. // 输出结果：0403020108070605
```

### swap64

PhonePC/2in1TabletTVWearable

swap64(): FastBuffer

将当前对象转换为无符号的64位整数数组，并交换字节顺序。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FastBuffer | 交换之后的FastBuffer对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200009 | The fastbuffer size must be a multiple of 64-bits. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
4. console.info(buf1.toString('hex'));
5. // 输出结果：0102030405060708
6. buf1.swap64();
7. console.info(buf1.toString('hex'));
8. // 输出结果：0807060504030201
```

### toJSON

PhonePC/2in1TabletTVWearable

toJSON(): Object

将Buffer转为JSON并返回。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | JSON对象。 |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
4. let obj = buf1.toJSON();
5. console.info(JSON.stringify(obj));
6. // 输出结果: {"type":"FastBuffer","data":[1,2,3,4,5]}
```

### toString

PhonePC/2in1TabletTVWearable

toString(encoding?: string, start?: number, end?: number): string

将当前对象中指定位置的数据转成指定编码格式的字符串并返回。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 字符编码格式。默认值：'utf8'。 |
| start | number | 否 | 开始位置。默认值：0。 |
| end | number | 否 | 结束位置。默认值：Buffer.length。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串。当start >= this.length或start > end时返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf1 = fastbuffer.allocUninitializedFromPool(26);
4. for (let i = 0; i < 26; i++) {
5. buf1.writeInt8(i + 97, i);
6. }
7. console.info(buf1.toString('utf-8'));
8. // 输出结果: abcdefghijklmnopqrstuvwxyz
```

### write

PhonePC/2in1TabletTVWearable

write(str: string, offset?: number, length?: number, encoding?: string): number

在FastBuffer对象的offset偏移处写入指定编码的字符串，写入的字节长度为length。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 要写入Buffer的字符串。 |
| offset | number | 否 | 偏移量。默认值：0。 |
| length | number | 否 | 最大字节长度。默认值：(this.length - offset)。 |
| encoding | string | 否 | 字符编码。默认值：'utf8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |
| 10200068 | The underlying ArrayBuffer is null or detach. |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.alloc(256);
4. let len = buf.write('\u00bd + \u00bc = \u00be', 0);
5. console.info(`${len} bytes: ${buf.toString('utf-8', 0, len)}`);
6. // 输出结果: 12 bytes: ½ + ¼ = ¾

8. let buffer1 = fastbuffer.alloc(10);
9. let length = buffer1.write('abcd', 8);
10. console.info("length = " + length);
11. // 输出结果：length = 2
```

### writeBigInt64BE

PhonePC/2in1TabletTVWearable

writeBigInt64BE(value: bigint, offset?: number): number

在FastBuffer对象的offset偏移处写入有符号的大端序64位BigInt型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 写入Buffer的数据。取值范围：-INT64\_MAX <= value <= INT64\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeBigInt64BE(BigInt(0x0102030405060708), 0);
5. console.info("result = " + result);
6. // 输出结果：result = 8
```

### writeBigInt64LE

PhonePC/2in1TabletTVWearable

writeBigInt64LE(value: bigint, offset?: number): number

在FastBuffer对象的offset偏移处写入有符号的小端序64位BigInt型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 写入Buffer的数据。取值范围：-INT64\_MAX <= value <= INT64\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeBigInt64LE(BigInt(0x0102030405060708), 0);
5. console.info("result = " + result);
6. // 输出结果：result = 8
```

### writeBigUInt64BE

PhonePC/2in1TabletTVWearable

writeBigUInt64BE(value: bigint, offset?: number): number

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

在FastBuffer对象的offset偏移处写入无符号的大端序64位BigUInt型数据。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 写入Buffer的数据。取值范围：0 <= value <= UINT64\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
5. console.info("result = " + result);
6. // 输出结果：result = 8
```

### writeBigUInt64LE

PhonePC/2in1TabletTVWearable

writeBigUInt64LE(value: bigint, offset?: number): number

在FastBuffer对象的offset偏移处写入无符号的小端序64位BigUInt型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 写入Buffer的数据。取值范围：0 <= value <= UINT64\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeBigUInt64LE(BigInt(0xdecafafecacefade), 0);
5. console.info("result = " + result);
6. // 输出结果：result = 8
```

### writeDoubleBE

PhonePC/2in1TabletTVWearable

writeDoubleBE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的64位双浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-DOUBLE\_MAX <= value <= DOUBLE\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeDoubleBE(123.456, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 8
```

### writeDoubleLE

PhonePC/2in1TabletTVWearable

writeDoubleLE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的64位双浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-DOUBLE\_MAX <= value <= DOUBLE\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeDoubleLE(123.456, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 8
```

### writeFloatBE

PhonePC/2in1TabletTVWearable

writeFloatBE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的32位浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-FLOAT\_MAX <= value <= FLOAT\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeFloatBE(3.1415, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 4
```

### writeFloatLE

PhonePC/2in1TabletTVWearable

writeFloatLE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的32位浮点型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-FLOAT\_MAX <= value <= FLOAT\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(8);
4. let result = buf.writeFloatLE(3.1415, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 4
```

### writeInt8

PhonePC/2in1TabletTVWearable

writeInt8(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入8位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-INT8\_MAX <= value <= INT8\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(2);
4. let result = buf.writeInt8(2, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 1
7. let result1 = buf.writeInt8(-2, 1);
8. console.info("result1 = " + result1);
9. // 输出结果：result1 = 2
```

### writeInt16BE

PhonePC/2in1TabletTVWearable

writeInt16BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的16位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-INT16\_MAX <= value <= INT16\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(2);
4. let result = buf.writeInt16BE(0x0102, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 2
```

### writeInt16LE

PhonePC/2in1TabletTVWearable

writeInt16LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的16位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-INT16\_MAX <= value <= INT16\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(2);
4. let result = buf.writeInt16LE(0x0304, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 2
```

### writeInt32BE

PhonePC/2in1TabletTVWearable

writeInt32BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的32位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-INT32\_MAX <= value <= INT32\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeInt32BE(0x01020304, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 4
```

### writeInt32LE

PhonePC/2in1TabletTVWearable

writeInt32LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的32位有符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：-INT32\_MAX <= value <= INT32\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeInt32LE(0x05060708, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 4
```

### writeIntBE

PhonePC/2in1TabletTVWearable

writeIntBE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入大端序的有符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围取决于byteLength。 |
| offset | number | 是 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。传入null或undefined时偏移量为0。 |
| byteLength | number | 是 | 要写入的字节数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(6);
4. let result = buf.writeIntBE(0x1234567890ab, 0, 6);
5. console.info("result = " + result);
6. // 输出结果：result = 6
```

### writeIntLE

PhonePC/2in1TabletTVWearable

writeIntLE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入小端序的有符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围取决于byteLength。 |
| offset | number | 是 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。传入null或undefined时偏移量为0。 |
| byteLength | number | 是 | 要写入的字节数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(6);
4. let result = buf.writeIntLE(0x1234567890ab, 0, 6);
5. console.info("result = " + result);
6. // 输出结果：result = 6
```

### writeUInt8

PhonePC/2in1TabletTVWearable

writeUInt8(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入8位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：0 <= value <= UINT8\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeUInt8(0x3, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 1
7. let result1 = buf.writeUInt8(0x4, 1);
8. console.info("result1 = " + result1);
9. // 输出结果：result1 = 2
10. let result2 = buf.writeUInt8(0x23, 2);
11. console.info("result2 = " + result2);
12. // 输出结果：result2 = 3
13. let result3 = buf.writeUInt8(0x42, 3);
14. console.info("result3 = " + result3);
15. // 输出结果：result3 = 4
```

### writeUInt16BE

PhonePC/2in1TabletTVWearable

writeUInt16BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的16位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：0 <= value <= UINT16\_MAX。 |
| offset | number | 否 | 偏移量。默认值为0。取值范围：0 <= offset <= this.length - 2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeUInt16BE(0xdead, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 2
7. let result1 = buf.writeUInt16BE(0xbeef, 2);
8. console.info("result1 = " + result1);
9. // 输出结果：result1 = 4
```

### writeUInt16LE

PhonePC/2in1TabletTVWearable

writeUInt16LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的16位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：0 <= value <= UINT16\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeUInt16LE(0xdead, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 2
7. let result1 = buf.writeUInt16LE(0xbeef, 2);
8. console.info("result1 = " + result1);
9. // 输出结果：result1 = 4
```

### writeUInt32BE

PhonePC/2in1TabletTVWearable

writeUInt32BE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入大端序的32位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围：0 <= value <= UINT32\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeUInt32BE(0xfeedface, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 4
```

### writeUInt32LE

PhonePC/2in1TabletTVWearable

writeUInt32LE(value: number, offset?: number): number

在FastBuffer对象的offset偏移处写入小端序的32位无符号整型数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入FastBuffer对象的数据。取值范围：0 <= value <= UINT32\_MAX。 |
| offset | number | 否 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - 4。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(4);
4. let result = buf.writeUInt32LE(0xfeedface, 0);
5. console.info("result = " + result);
6. // 输出结果：result = 4
```

### writeUIntBE

PhonePC/2in1TabletTVWearable

writeUIntBE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入大端序的无符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围取决于byteLength。 |
| offset | number | 是 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。传入null或undefined时偏移量为0。 |
| byteLength | number | 是 | 要写入的字节数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(6);
4. let result = buf.writeUIntBE(0x1234567890ab, 0, 6);
5. console.info("result = " + result);
6. // 输出结果：result = 6
```

### writeUIntLE

PhonePC/2in1TabletTVWearable

writeUIntLE(value: number, offset: number, byteLength: number): number

在FastBuffer对象的offset偏移处写入小端序的无符号数据，字节长度为byteLength。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 写入Buffer的数据。取值范围取决于byteLength。 |
| offset | number | 是 | 偏移量。默认值：0。取值范围：0 <= offset <= this.length - byteLength。传入null或undefined时偏移量为0。 |
| byteLength | number | 是 | 要写入的字节数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 偏移量offset加上写入的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

**示例：**

```
1. import { fastbuffer } from '@kit.ArkTS';

3. let buf = fastbuffer.allocUninitializedFromPool(6);
4. let result = buf.writeUIntLE(0x1234567890ab, 0, 6);
5. console.info("result = " + result);
6. // 输出结果：result = 6
```
