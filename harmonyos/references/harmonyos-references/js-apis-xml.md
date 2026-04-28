---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-xml
title: @ohos.xml (XML解析与生成)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.xml (XML解析与生成)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c76b75782d1addba175f82c8cd5b4bc7ebeb8bf04ce8ad35b9d7455092ca42ce
---

本模块提供XML生成和解析的接口。

本模块提供了两种生成XML文件的方式:

* [XmlSerializer](js-apis-xml.md#xmlserializer)：适用于已知XML文本大小的情况
* [XmlDynamicSerializer20+](js-apis-xml.md#xmldynamicserializer20)：适用于未知XML文本大小的情况。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { xml } from '@kit.ArkTS';
```

## XmlSerializer

PhonePC/2in1TabletTVWearable

XmlSerializer接口用于生成XML文件。

### constructor

PhonePC/2in1TabletTVWearable

constructor(buffer: ArrayBuffer | DataView, encoding?: string)

XmlSerializer的构造函数。

说明

buffer是开发者根据需要自定义大小的缓存区域，用于临时存储生成的XML文本。在使用过程中必须确保缓存区域足以容纳生成的文本内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | DataView | 是 | 用于接收写入XML信息的ArrayBuffer或DataView内存。 |
| encoding | string | 否 | 编码格式，默认'utf-8'（目前仅支持'utf-8'）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let arrayBuffer = new ArrayBuffer(2048);
2. let thatSer = new xml.XmlSerializer(arrayBuffer, "utf-8");
```

### setAttributes

PhonePC/2in1TabletTVWearable

setAttributes(name: string, value: string): void

添加元素的属性和属性值。

说明

该接口对所添加数据不做标准XML校验处理，确保所添加的数据符合标准XML规范。例如不允许添加数字开头的属性名称以及添加多个同名的属性名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 属性。 |
| value | string | 是 | 属性值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.startElement("note");
6. thatSer.setAttributes("importance", "high");
7. thatSer.endElement();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result); // <note importance="high"/>
```

### addEmptyElement

PhonePC/2in1TabletTVWearable

addEmptyElement(name: string): void

添加一个空元素。

说明

该接口对所添加数据不做标准XML校验处理，确保所添加的数据符合标准XML规范。例如不允许添加数字开头的元素名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 元素的名称。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.addEmptyElement("d");
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <d/>
```

### setDeclaration

PhonePC/2in1TabletTVWearable

setDeclaration(): void

设置带有编码信息的文件声明。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.setDeclaration();
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result);
9. // <?xml version="1.0" encoding="utf-8"?>
```

### startElement

PhonePC/2in1TabletTVWearable

startElement(name: string): void

根据给定名称添加元素开始标记。

说明

* 调用该接口后须调用[endElement](js-apis-xml.md#endelement)写入元素结束标记，以确保节点正确闭合。
* 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 当前元素的元素名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.startElement("note");
6. thatSer.setText("Happy");
7. thatSer.endElement();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result);
11. // <note>Happy</note>
```

### endElement

PhonePC/2in1TabletTVWearable

endElement(): void

添加元素结束标记。

说明

调用该接口前必须先调用[startElement](js-apis-xml.md#startelement)接口写入元素开始标记。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.startElement("note");
6. thatSer.setText("Happy");
7. thatSer.endElement();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result);
11. // <note>Happy</note>
```

### setNamespace

PhonePC/2in1TabletTVWearable

setNamespace(prefix: string, namespace: string): void

添加当前元素标记的命名空间。

说明

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。例如禁止添加数字开头的前缀以及为同一个元素设置多个命名空间。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 当前元素及其子元素的前缀。 |
| namespace | string | 是 | 当前元素及其子元素的命名空间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.setNamespace("h", "http://www.w3.org/TR/html4/");
6. thatSer.startElement("note");
7. thatSer.endElement();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result);
11. // <h:note xmlns:h="http://www.w3.org/TR/html4/"/>
```

### setComment

PhonePC/2in1TabletTVWearable

setComment(text: string): void

添加注释内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 当前元素的注释内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.setComment("Hello, World!");
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <!--Hello, World!-->
```

### setCDATA

PhonePC/2in1TabletTVWearable

setCDATA(text: string): void

提供在CDATA标签中添加数据的能力，所生成的CDATA标签结构为："<![CDATA[" + 所添加的数据 + "]]>"。

说明

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许在CDATA标签中添加包含"]]>"字符串的数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | CDATA属性的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.setCDATA('root SYSTEM')
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <![CDATA[root SYSTEM]]>
```

### setText

PhonePC/2in1TabletTVWearable

setText(text: string): void

添加标签值。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | text属性的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.startElement("note");
6. thatSer.setAttributes("importance", "high");
7. thatSer.setText("Happy");
8. thatSer.endElement();
9. let uint8 = new Uint8Array(arrayBuffer);
10. let result = util.TextDecoder.create().decodeToString(uint8);
11. console.info(result); // <note importance="high">Happy</note>
```

### setDocType

PhonePC/2in1TabletTVWearable

setDocType(text: string): void

添加文档类型。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | DocType属性的内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let arrayBuffer = new ArrayBuffer(2048);
4. let thatSer = new xml.XmlSerializer(arrayBuffer);
5. thatSer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">
```

## XmlDynamicSerializer20+

PhonePC/2in1TabletTVWearable

XmlDynamicSerializer类用于动态生成XML字符串。当无法确定XML内容长度时，推荐使用该类。

说明

使用该类构造的对象无需自行创建ArrayBuffer，程序动态扩容，可以不断添加XML元素，最终序列化结果字符串长度上限为100000。

### constructor20+

PhonePC/2in1TabletTVWearable

constructor(encoding?: string)

XmlDynamicSerializer的构造函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 编码格式，默认'utf-8'(目前仅支持'utf-8')。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200066 | Incorrect encoding format, only support utf-8. |

**示例：**

```
1. let serializer = new xml.XmlDynamicSerializer('utf-8');
```

### getOutput20+

PhonePC/2in1TabletTVWearable

getOutput(): ArrayBuffer

返回XML字符串的ArrayBuffer。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 用于接收写入XML信息的ArrayBuffer内存。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.startElement("note");
5. serializer.setText("Happy");
6. serializer.endElement();
7. let arr = serializer.getOutput();
8. let uint8 = new Uint8Array(arr);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result); // <note>Happy</note>
```

### setAttributes20+

PhonePC/2in1TabletTVWearable

setAttributes(name: string, value: string): void

写入元素的属性和属性值。

说明

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的属性名称以及添加多个同名的属性名称。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 属性。所组成的XML长度不能超过100000，不可为空字符。 |
| value | string | 是 | 属性值。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200063 | Illegal position for xml. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.startElement("note");
5. serializer.setAttributes("importance", "high");
6. serializer.endElement();
7. let arrayBuffer = serializer.getOutput();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result); // <note importance="high"/>
```

### addEmptyElement20+

PhonePC/2in1TabletTVWearable

addEmptyElement(name: string): void

写入一个空元素。

说明

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 该空元素的元素名。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.addEmptyElement("d");
5. let arrayBuffer = serializer.getOutput();
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <d/>
```

### setDeclaration20+

PhonePC/2in1TabletTVWearable

setDeclaration(): void

编写带有编码的文件声明。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200063 | Illegal position for xml. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.setDeclaration();
5. let arrayBuffer = serializer.getOutput();
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <?xml version="1.0" encoding="utf-8"?>
```

### startElement20+

PhonePC/2in1TabletTVWearable

startElement(name: string): void

写入元素开始标记。

说明

* 调用该接口后须调用[endElement](js-apis-xml.md#endelement)写入元素结束标记，以确保节点正确闭合。
* 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 当前元素的元素名。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.startElement("note");
5. serializer.setText("Happy");
6. serializer.endElement();
7. let arrayBuffer = serializer.getOutput();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result); // <note>Happy</note>
```

### endElement20+

PhonePC/2in1TabletTVWearable

endElement(): void

写入元素结束标记。

说明

调用该接口前必须先调用[startElement](js-apis-xml.md#startelement)接口写入元素开始标记。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200065 | There is no match between the startElement and the endElement. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.startElement("note");
5. serializer.setText("Happy");
6. serializer.endElement();
7. let arrayBuffer = serializer.getOutput();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result); // <note>Happy</note>
```

### setNamespace20+

PhonePC/2in1TabletTVWearable

setNamespace(prefix: string, namespace: string): void

写入当前元素标记的命名空间。

说明

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的前缀以及对同一个元素设置多个命名空间。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 当前元素及其子元素的前缀。所组成的XML长度不能超过100000，不可为空字符。 |
| namespace | string | 是 | 当前元素及其子元素的命名空间。所组成的XML长度不能超过100000，不可为空字符。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.setNamespace("h", "http://www.w3.org/TR/html4/");
5. serializer.startElement("note");
6. serializer.endElement();
7. let arrayBuffer = serializer.getOutput();
8. let uint8 = new Uint8Array(arrayBuffer);
9. let result = util.TextDecoder.create().decodeToString(uint8);
10. console.info(result); // <h:note xmlns:h="http://www.w3.org/TR/html4/"/>
```

### setComment20+

PhonePC/2in1TabletTVWearable

setComment(text: string): void

写入注释内容。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 当前元素的注释内容。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.setComment("Hello, World!");
5. let arrayBuffer = serializer.getOutput();
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <!--Hello, World!-->
```

### setCdata20+

PhonePC/2in1TabletTVWearable

setCdata(text: string): void

提供在CDATA标签中添加数据的能力，所生成的CDATA标签结构为："<![CDATA[" + 所添加的数据 + "]]>"。

说明

该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许在CDATA标签中添加包含"]]>"字符串的数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | CDATA属性的内容。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.setCdata('root SYSTEM')
5. let arrayBuffer = serializer.getOutput();
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <![CDATA[root SYSTEM]]>
```

### setText20+

PhonePC/2in1TabletTVWearable

setText(text: string): void

写入标签值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 标签值。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.startElement("note");
5. serializer.setAttributes("importance", "high");
6. serializer.setText("Happy");
7. serializer.endElement();
8. let arrayBuffer = serializer.getOutput();
9. let uint8 = new Uint8Array(arrayBuffer);
10. let result = util.TextDecoder.create().decodeToString(uint8);
11. console.info(result); // <note importance="high">Happy</note>
```

### setDocType20+

PhonePC/2in1TabletTVWearable

setDocType(text: string): void

写入文档类型。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | DocType属性的内容。所组成的XML长度不能超过100000。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let serializer = new xml.XmlDynamicSerializer('utf-8');
4. serializer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
5. let arrayBuffer = serializer.getOutput();
6. let uint8 = new Uint8Array(arrayBuffer);
7. let result = util.TextDecoder.create().decodeToString(uint8);
8. console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">
```

## XmlPullParser

PhonePC/2in1TabletTVWearable

XmlPullParser接口用于解析现有的XML文件。

### constructor

PhonePC/2in1TabletTVWearable

constructor(buffer: ArrayBuffer | DataView, encoding?: string)

构造并返回一个XmlPullParser对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | DataView | 是 | 用于解析的XML文本信息。 |
| encoding | string | 否 | 编码格式，默认'utf-8'（目前仅支持'utf-8'）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml = '<title>Happy</title>'
4. let textEncoder = new util.TextEncoder();
5. let uint8Array = textEncoder.encodeInto(strXml);
6. let that = new xml.XmlPullParser(uint8Array.buffer as object as ArrayBuffer, 'UTF-8');
```

### parseXml14+

PhonePC/2in1TabletTVWearable

parseXml(option: ParseOptions): void

解析XML。

**元服务API**：从API version 14 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [ParseOptions](js-apis-xml.md#parseoptions) | 是 | XML解析选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

具体使用场景可参照[解析XML标签和标签值](../harmonyos-guides/xml-parsing.md#解析xml标签和标签值)和[解析XML属性和属性值](../harmonyos-guides/xml-parsing.md#解析xml属性和属性值)

```
1. import { xml, util } from '@kit.ArkTS';

3. let strxml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note importance="high" logged="true">' +
6. '    <title><![CDATA[测试\n测试]]></title>' +
7. '</note>';
8. let textEncoder = new util.TextEncoder();
9. let uint8 = textEncoder.encodeInto(strxml);

11. function func(key: xml.EventType, value: xml.ParseInfo) {
12. if (key == xml.EventType.CDSECT) {
13. console.info(JSON.stringify(value.getText()));
14. }
15. return true;
16. }
17. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
18. let pullParser = new xml.XmlPullParser(uint8.buffer as object as ArrayBuffer);
19. pullParser.parseXml(options);
20. // "测试\n测试"
```

### parse(deprecated)

PhonePC/2in1TabletTVWearable

parse(option: ParseOptions): void

该接口用于解析XML。

说明

从API version 8开始支持，从API version 14开始废弃，建议使用[parseXml14+](js-apis-xml.md#parsexml14)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [ParseOptions](js-apis-xml.md#parseoptions) | 是 | XML解析选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note importance="high" logged="true">' +
6. '<company>John &amp; Hans</company>' +
7. '<title>Happy</title>' +
8. '</note>';
9. let textEncoder = new util.TextEncoder();
10. let arrBuffer = textEncoder.encodeInto(strXml);
11. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
12. let str = '';
13. function func(name: string, value: string) {
14. str = name + value;
15. console.info(str);
16. return true;
17. }
18. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func}
19. that.parse(options);
20. // note
21. // company
22. // John & Hans
23. // company
24. // title
25. // Happy
26. // title
27. // note
```

## AttributeWithTagCb20+

PhonePC/2in1TabletTVWearable

type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagName | string | 是 | 标签名称。 |
| key | string | 是 | 属性名称。 |
| value | string | 是 | 属性的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否继续解析标签名称、属性名称及属性的值。true表示继续解析，false表示停止解析。 |

## ParseOptions

PhonePC/2in1TabletTVWearable

XML解析选项。

**系统能力：** SystemCapability.Utils.Lang。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportDoctype | boolean | 否 | 是 | 是否解析文档类型，false表示不解析文档类型，true表示解析文档类型，默认值false。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| ignoreNameSpace | boolean | 否 | 是 | 是否忽略命名空间，忽略命名空间后，将不会对其进行解析。true表示忽略命名空间，false表示不忽略命名空间，默认值false。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| tagValueCallbackFunction | (name: string, value: string) => boolean | 否 | 是 | 解析开始标签、标签值和结束标签，默认值undefined，表示不解析。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| attributeValueCallbackFunction | (name: string, value: string) => boolean | 否 | 是 | 解析属性和属性值，默认值undefined，表示不解析。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| tokenValueCallbackFunction | (eventType: [EventType](js-apis-xml.md#eventtype), value: [ParseInfo](js-apis-xml.md#parseinfo)) => boolean | 否 | 是 | 解析元素事件类型([EventType](js-apis-xml.md#eventtype))和[ParseInfo](js-apis-xml.md#parseinfo)属性，默认值undefined，表示不解析。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| attributeWithTagCallbackFunction20+ | [AttributeWithTagCb](js-apis-xml.md#attributewithtagcb20) | 否 | 是 | 解析标签名称、属性名称及属性的值，默认值为undefined，表示不执行解析。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## ParseInfo

PhonePC/2in1TabletTVWearable

当前XML解析信息。

### getColumnNumber

PhonePC/2in1TabletTVWearable

getColumnNumber(): number

获取当前列号，从1开始计数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前列号。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
4. let textEncoder = new util.TextEncoder();
5. let arrBuffer = textEncoder.encodeInto(strXml);
6. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
7. let str = "";
8. function func(key: xml.EventType, value: xml.ParseInfo) {
9. str += 'key:' + key + ' value:' + value.getColumnNumber() + ' ';
10. return true; // 决定是否继续解析，用于继续或终止解析。
11. }
12. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
13. that.parseXml(options);
14. console.info(str);
15. // key:0 value:1 key:2 value:45 key:4 value:50 key:3 value:57 key:1 value:57
```

### getDepth

PhonePC/2in1TabletTVWearable

getDepth(): number

获取元素的当前深度。

说明

标签内的空白事件深度与标签的深度保持一致。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回元素的当前深度。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note importance="high">' +
6. '<title>Happy</title>' +
7. '</note>';
8. let textEncoder = new util.TextEncoder();
9. let arrBuffer = textEncoder.encodeInto(strXml);
10. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
11. let str = "";
12. function func(key: xml.EventType, value: xml.ParseInfo) {
13. str += 'key:' + key + ' value:' + value.getDepth() + ' ';
14. return true; // 决定是否继续解析，用于继续或终止解析。
15. }
16. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
17. that.parseXml(options);
18. console.info(str);
19. // key:0 value:0 key:2 value:1 key:2 value:2 key:4 value:2 key:3 value:2 key:3 value:1 key:1 value:0
```

### getLineNumber

PhonePC/2in1TabletTVWearable

getLineNumber(): number

获取当前行号，从1开始。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前行号。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Work</note>';
4. let textEncoder = new util.TextEncoder();
5. let arrBuffer = textEncoder.encodeInto(strXml);
6. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
7. let str = "";
8. function func(key: xml.EventType, value: xml.ParseInfo) {
9. str += 'key:' + key + ' value:' + value.getLineNumber() + ' ';
10. return true; // 决定是否继续解析，用于继续或终止解析。
11. }
12. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
13. that.parseXml(options);
14. console.info(str);
15. // key:0 value:1 key:2 value:1 key:4 value:1 key:3 value:1 key:1 value:1
```

### getName

PhonePC/2in1TabletTVWearable

getName(): string

获取当前元素名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前元素名称。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
4. let textEncoder = new util.TextEncoder();
5. let arrBuffer = textEncoder.encodeInto(strXml);
6. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
7. let str = "";
8. function func(key: xml.EventType, value: xml.ParseInfo) {
9. str += 'key:' + key + ' value:' + value.getName() + ' ';
10. return true; // 决定是否继续解析，用于继续或终止解析。
11. }
12. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
13. that.parseXml(options);
14. console.info(str);
15. // key:0 value: key:2 value:note key:4 value: key:3 value:note key:1 value:
```

### getNamespace

PhonePC/2in1TabletTVWearable

getNamespace(): string

获取当前元素的命名空间。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前元素的命名空间。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note xmlns:h="http://www.w3.org">' +
6. '<h:title>Happy</h:title>' +
7. '</note>';
8. let textEncoder = new util.TextEncoder();
9. let arrBuffer = textEncoder.encodeInto(strXml);
10. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
11. let str = "";
12. function func(key: xml.EventType, value: xml.ParseInfo) {
13. str += 'key:' + key + ' value:' + value.getNamespace() + ' ';
14. return true; // 决定是否继续解析，用于继续或终止解析。
15. }
16. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:false, tokenValueCallbackFunction:func}
17. that.parseXml(options);
18. console.info(str);
19. // key:0 value: key:2 value: key:2 value:http://www.w3.org key:4 value: key:3 value:http://www.w3.org key:3 value: key:1 value:
```

### getPrefix

PhonePC/2in1TabletTVWearable

getPrefix(): string

获取当前元素前缀。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前元素前缀。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note xmlns:h="http://www.w3.org/TR/html4">' +
6. '<h:title>Happy</h:title>' +
7. '</note>';
8. let textEncoder = new util.TextEncoder();
9. let arrBuffer = textEncoder.encodeInto(strXml);
10. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
11. let str = "";
12. function func(key: xml.EventType, value: xml.ParseInfo) {
13. str += 'key:' + key + ' value:' + value.getPrefix() + ' ';
14. return true; // 决定是否继续解析，用于继续或终止解析。
15. }
16. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:false, tokenValueCallbackFunction:func}
17. that.parseXml(options);
18. console.info(str);
19. // key:0 value: key:2 value: key:2 value:h key:4 value: key:3 value:h key:3 value: key:1 value:
```

### getText

PhonePC/2in1TabletTVWearable

getText(): string

获取当前事件的文本内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前事件的文本内容。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
4. let textEncoder = new util.TextEncoder();
5. let arrBuffer = textEncoder.encodeInto(strXml);
6. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
7. let str = "";
8. function func(key: xml.EventType, value: xml.ParseInfo) {
9. str += 'key:' + key + ' value:' + value.getText() + ' ';
10. return true; // 决定是否继续解析，用于继续或终止解析。
11. }
12. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
13. that.parseXml(options);
14. console.info(str);
15. // key:0 value: key:2 value: key:4 value:Happy key:3 value: key:1 value:
```

### isEmptyElementTag

PhonePC/2in1TabletTVWearable

isEmptyElementTag(): boolean

判断当前元素是否为空元素。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true，表示当前元素为空元素。返回false，表示当前元素为非空元素。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note importance="high" logged="true">' +
6. '<title/>' +
7. '</note>';
8. let textEncoder = new util.TextEncoder();
9. let arrBuffer = textEncoder.encodeInto(strXml);
10. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
11. let str = "";
12. function func(key: xml.EventType, value: xml.ParseInfo) {
13. str += 'key:' + key + ' value:' + value.isEmptyElementTag() + ' ';
14. return true; // 决定是否继续解析，用于继续或终止解析。
15. }
16. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
17. that.parseXml(options);
18. console.info(str);
19. // key:0 value:false key:2 value:false key:2 value:true key:3 value:false key:3 value:false key:1 value:false
```

### isWhitespace

PhonePC/2in1TabletTVWearable

isWhitespace(): boolean

判断当前事件是否仅包含空格字符。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true，表示当前文本事件仅包含空格字符。返回false，表示当前文本事件包含非空格字符。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml =
4. '<?xml version="1.0" encoding="utf-8"?>' +
5. '<note importance="high" logged="true">' +
6. '<title> </title>' +
7. '</note>';
8. let textEncoder = new util.TextEncoder();
9. let arrBuffer = textEncoder.encodeInto(strXml);
10. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
11. let str = "";
12. function func(key: xml.EventType, value: xml.ParseInfo) {
13. str += 'key:' + key + ' value:' + value.isWhitespace() + ' ';
14. return true; // 决定是否继续解析，用于继续或终止解析。
15. }
16. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
17. that.parseXml(options);
18. console.info(str);
19. // key:0 value:true key:2 value:false key:2 value:true key:10 value:true key:3 value:true key:3 value:true key:1 value:true
```

### getAttributeCount

PhonePC/2in1TabletTVWearable

getAttributeCount(): number

获取当前开始标记的属性数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前开始标记的属性数。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. let strXml = '<?xml version="1.0" encoding="utf-8"?><note importance="high" logged="true"/>';
4. let textEncoder = new util.TextEncoder();
5. let arrBuffer = textEncoder.encodeInto(strXml);
6. let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
7. let str = "";
8. function func(key: xml.EventType, value: xml.ParseInfo) {
9. str += 'key:' + key + ' value:' + value.getAttributeCount() + ' ';
10. return true; // 决定是否继续解析，用于继续或终止解析。
11. }
12. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
13. that.parseXml(options);
14. console.info(str);
15. // key:0 value:0 key:2 value:2 key:3 value:2 key:1 value:0
```

## EventType

PhonePC/2in1TabletTVWearable

事件类型枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START\_DOCUMENT | 0 | 启动文件事件。 |
| END\_DOCUMENT | 1 | 结束文件事件。 |
| START\_TAG | 2 | 启动标签事件。 |
| END\_TAG | 3 | 结束标签事件。 |
| TEXT | 4 | 文本事件。 |
| CDSECT | 5 | CDATA事件。 |
| COMMENT | 6 | XML注释事件。 |
| DOCDECL | 7 | XML文档类型声明事件。 |
| INSTRUCTION | 8 | XML处理指令声明事件。 |
| ENTITY\_REFERENCE | 9 | 实体引用事件。 |
| WHITESPACE | 10 | 空白事件。 |
