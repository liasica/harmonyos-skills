---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-convertxml
title: @ohos.convertxml (xml转换JavaScript)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.convertxml (xml转换JavaScript)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ff1ec0f55138041006df093958c2856f2bdf1d8ef4acebeff5a026b18427a35
---

本模块提供将XML文本转换为JavaScript对象的解析能力。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { convertxml } from '@kit.ArkTS';
```

## ConvertXML

PhonePC/2in1TabletTVWearable

### fastConvertToJSObject14+

PhonePC/2in1TabletTVWearable

fastConvertToJSObject(xml: string, options?: ConvertOptions) : Object

转换XML文本为Object类型对象。

说明

该接口无法满足解析大数据量的XML文件，当单元素文本内容超过10M时，会打印异常信息并返回一个仅包含XML标签头的基础Object对象。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。fastConvertToJSObject接口转换后的对象以换行符（LF）表示换行。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200002 | Invalid xml string. |

**示例：**

```
1. try {
2. let xml =
3. '<?xml version="1.0" encoding="utf-8"?>' +
4. '<note importance="high" logged="true">' +
5. '   <title>Hello\r\nWorld</title>' +
6. '   <todo><![CDATA[Work\r\n]]></todo>' +
7. '</note>';
8. let conv = new convertxml.ConvertXML();
9. let options: convertxml.ConvertOptions = {
10. trim: false,
11. declarationKey: "_declaration",
12. instructionKey: "_instruction",
13. attributesKey: "_attributes",
14. textKey: "_text",
15. cdataKey: "_cdata",
16. doctypeKey: "_doctype",
17. commentKey: "_comment",
18. parentKey: "_parent",
19. typeKey: "_type",
20. nameKey: "_name",
21. elementsKey: "_elements"
22. };
23. let result = JSON.stringify(conv.fastConvertToJSObject(xml, options));
24. console.info(result);
25. } catch (e) {
26. console.error((e as Object).toString());
27. }
28. // 输出(宽泛型)
29. // {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Hello\nWorld"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"cdata","_cdata":"Work\n"}]}]}]}
```

### largeConvertToJSObject23+

PhonePC/2in1TabletTVWearable

largeConvertToJSObject(xml: string, options?: ConvertOptions): Object

将XML文本转换为Object类型对象，此方法支持解析单个节点大小超过10M的大型XML文本。

说明

当传入的XML文本无法正确解析为Object类型对象时，打印异常信息并返回一个仅包含XML标签头的基础Object对象。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200002 | Invalid xml string. |

**示例：**

```
1. try {
2. let xmlstr =
3. '<?xml version="1.0" encoding="utf-8"?>' +
4. '<?custom-pi processing="example"?>' +
5. '<catalog id="books">' +
6. '<!-- Bestseller Example -->' +
7. '<book category="fiction" ref="B101">' +
8. '<title>Echoes &amp; Whispers</title>' +
9. '<price unit="USD">19.99</price>' +
10. '<descr>' +
11. '<![CDATA[<b>suspense</b>novel & Legendary Stories]]>' +
12. '</descr>' +
13. '<popular/>' +
14. '</book>' +
15. '</catalog>';
16. let conv = new convertxml.ConvertXML();
17. let options: convertxml.ConvertOptions = {
18. trim: false,
19. declarationKey: "_declaration",
20. instructionKey: "_instruction",
21. attributesKey: "_attributes",
22. textKey: "_text",
23. cdataKey: "_cdata",
24. doctypeKey: "_doctype",
25. commentKey: "_comment",
26. parentKey: "_parent",
27. typeKey: "_type",
28. nameKey: "_name",
29. elementsKey: "_elements"
30. };
31. let result = JSON.stringify(conv.largeConvertToJSObject(xmlstr, options));
32. console.info(result);
33. } catch (e) {
34. console.error((e as Object).toString());
35. }
36. // 输出(宽泛型)
37. // {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"instruction","_name":"custom-pi","_instruction":"processing=\"example\""},{"_type":"element","_name":"catalog","_attributes":{"id":"books"},"_elements":[{"_type":"comment","_comment":" Bestseller Example "},{"_type":"element","_name":"book","_parent":"catalog","_attributes":{"category":"fiction","ref":"B101"},"_elements":[{"_type":"element","_name":"title","_parent":"book","_elements":[{"_type":"text","_text":"Echoes & Whispers"}]},{"_type":"element","_name":"price","_parent":"book","_attributes":{"unit":"USD"},"_elements":[{"_type":"text","_text":"19.99"}]},{"_type":"element","_name":"descr","_parent":"book","_elements":[{"_type":"cdata","_cdata":"<b>suspense</b>novel & Legendary Stories"}]},{"_type":"element","_name":"popular","_parent":"book"}]}]}]}
```

### convertToJSObject(deprecated)

PhonePC/2in1TabletTVWearable

convertToJSObject(xml: string, options?: ConvertOptions) : Object

转换XML文本为Object类型对象。

说明

从API version 9开始支持，从API version 14开始废弃，建议使用[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | 传入的XML文本，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 处理后返回的JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200002 | Invalid xml string. |

**示例：**

```
1. try {
2. let xml =
3. '<?xml version="1.0" encoding="utf-8"?>' +
4. '<note importance="high" logged="true">' +
5. '    <title>Happy</title>' +
6. '    <todo>Work</todo>' +
7. '    <todo>Play</todo>' +
8. '</note>';
9. let conv = new convertxml.ConvertXML();
10. let options: convertxml.ConvertOptions = {
11. trim: false,
12. declarationKey: "_declaration",
13. instructionKey: "_instruction",
14. attributesKey: "_attributes",
15. textKey: "_text",
16. cdataKey: "_cdata",
17. doctypeKey: "_doctype",
18. commentKey: "_comment",
19. parentKey: "_parent",
20. typeKey: "_type",
21. nameKey: "_name",
22. elementsKey: "_elements"
23. };
24. let result = JSON.stringify(conv.convertToJSObject(xml, options));
25. console.info(result);
26. } catch (e) {
27. console.error((e as Object).toString());
28. }
29. // 输出(宽泛型)
30. // {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

### convert(deprecated)

PhonePC/2in1TabletTVWearable

convert(xml: string, options?: ConvertOptions) : Object

转换XML文本为JavaScript对象。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | 传入的XML文本。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，默认值是ConvertOptions对象，由其中各个属性的默认值组成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 处理后返回的JavaScript对象。 |

**示例：**

```
1. let xml =
2. '<?xml version="1.0" encoding="utf-8"?>' +
3. '<note importance="high" logged="true">' +
4. '    <title>Happy</title>' +
5. '    <todo>Work</todo>' +
6. '    <todo>Play</todo>' +
7. '</note>';
8. let conv = new convertxml.ConvertXML();
9. let options: convertxml.ConvertOptions = {
10. trim: false,
11. declarationKey: "_declaration",
12. instructionKey: "_instruction",
13. attributesKey: "_attributes",
14. textKey: "_text",
15. cdataKey: "_cdata",
16. doctypeKey: "_doctype",
17. commentKey: "_comment",
18. parentKey: "_parent",
19. typeKey: "_type",
20. nameKey: "_name",
21. elementsKey: "_elements"
22. };
23. let result = JSON.stringify(conv.convert(xml, options));
24. console.info(result);
25. // 输出(宽泛型)
26. // {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

## ConvertOptions

PhonePC/2in1TabletTVWearable

转换选项。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trim | boolean | 否 | 否 | 是否修剪位于文本前后的空白字符，true表示xml文本前后的空白字符将会被修剪，false则表示空白字符会被保留。 |
| ignoreDeclaration | boolean | 否 | 是 | 是否忽略xml写入声明指示，true表示忽略xml写入声明指示，false则相反，默认false。 |
| ignoreInstruction | boolean | 否 | 是 | 是否忽略xml的写入处理指令，true表示忽略xml的写入处理指令，false则相反，默认false。 |
| ignoreAttributes | boolean | 否 | 是 | 是否忽略元素的属性信息，true表示忽略元素的属性信息，false则相反，默认false。 |
| ignoreComment | boolean | 否 | 是 | 是否忽略元素的注释信息，true表示忽略元素的注释信息，false则相反，默认false。 |
| ignoreCDATA | boolean | 否 | 是 | 是否忽略元素的CDATA信息，true表示忽略元素的CDATA信息，false则相反，默认false。 |
| ignoreDoctype | boolean | 否 | 是 | 是否忽略元素的Doctype信息，true表示忽略元素的Doctype信息，false则相反，默认false。 |
| ignoreText | boolean | 否 | 是 | 是否忽略元素的文本信息，true表示忽略元素的文本信息，false则相反，默认false。 |
| declarationKey | string | 否 | 否 | 用于输出对象中declaration的属性键的名称。 |
| instructionKey | string | 否 | 否 | 用于输出对象中instruction的属性键的名称。 |
| attributesKey | string | 否 | 否 | 用于输出对象中attributes的属性键的名称。 |
| textKey | string | 否 | 否 | 用于输出对象中text的属性键的名称。 |
| cdataKey | string | 否 | 否 | 用于输出对象中cdata的属性键的名称 |
| doctypeKey | string | 否 | 否 | 用于输出对象中doctype的属性键的名称。 |
| commentKey | string | 否 | 否 | 用于输出对象中comment的属性键的名称。 |
| parentKey | string | 否 | 否 | 用于输出对象中parent的属性键的名称。 |
| typeKey | string | 否 | 否 | 用于输出对象中type的属性键的名称。 |
| nameKey | string | 否 | 否 | 用于输出对象中name的属性键的名称。 |
| elementsKey | string | 否 | 否 | 用于输出对象中elements的属性键的名称。 |
