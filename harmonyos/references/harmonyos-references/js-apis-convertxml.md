---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-convertxml
title: "@ohos.convertxml (XML转换JavaScript)"
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.convertxml (XML转换JavaScript)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5793349df652fa4c021abbc55afc497d987d3bd73fce93c46e781868e4d06a79
---

本模块提供将XML文本转换为JavaScript对象的解析能力，适用于XML配置文件解析、XML格式网络数据处理、数据迁移与格式转换等场景。转换过程中，XML的各类组件（声明、指令、元素、属性、文本、CDATA、注释和Doctype等）会按照ConvertOptions中配置的键名映射为JavaScript对象的属性，形成层级嵌套的对象结构，简化了XML数据的处理流程，支持通过ConvertOptions自定义键名映射实现灵活的输出结构。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { convertxml } from '@kit.ArkTS';
```

## ConvertXML

ConvertXML类提供将XML文本转换为JavaScript对象的能力，推荐使用[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)进行常规XML文本解析，当单元素文本内容超过10M时推荐使用[largeConvertToJSObject23+](js-apis-convertxml.md#largeconverttojsobject23)。已废弃的[convertToJSObject](js-apis-convertxml.md#converttojsobjectdeprecated)和[convert](js-apis-convertxml.md#convertdeprecated)方法不再维护，建议使用[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)替代。

### fastConvertToJSObject14+

fastConvertToJSObject(xml: string, options?: ConvertOptions) : Object

将XML文本转换为Object类型对象，适用于XML配置文件解析、数据报文处理等场景。该方法将XML文本解析为层级嵌套结构，各XML组件按ConvertOptions中配置的键名映射为对象的属性。当单元素文本内容超过10M时，建议使用[largeConvertToJSObject23+](js-apis-convertxml.md#largeconverttojsobject23)替代。

**说明** 

该接口无法满足解析单元素文本内容超过10M的XML文件，当单元素文本内容超过10M时，会输出异常日志信息并返回一个仅包含XML声明的基础Object对象。如需解析单元素文本内容超过10M的XML文本，建议使用[largeConvertToJSObject23+](js-apis-convertxml.md#largeconverttojsobject23)替代。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。fastConvertToJSObject接口转换后的对象以换行符（LF）表示换行。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，需符合XML语法规范，若包含“&”字符，请使用实体引用“&amp;”替换。单元素文本内容超过10M时，输出异常日志并返回仅包含XML声明的基础Object，建议使用largeConvertToJSObject替代。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象，用于提供解析后的XML结构信息，具体属性键名由ConvertOptions定义，可通过配置键名访问XML各组件的映射数据。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200002 | Invalid xml string. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '   <title>Hello\r\nWorld</title>' +
    '   <todo><![CDATA[Work\r\n]]></todo>' +
    '</note>';
  // 创建ConvertXML转换实例
  let converter = new convertxml.ConvertXML();
  // 配置转换选项
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  // 调用fastConvertToJSObject接口转换XML文本
  let result = JSON.stringify(converter.fastConvertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  let err: BusinessError = e as BusinessError;
  console.error(`Failed to convert XML text to JS object using fastConvertToJSObject. Code: ${err.code}, message: ${err.message}`);
}
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Hello\nWorld"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"cdata","_cdata":"Work\n"}]}]}]}
```

### largeConvertToJSObject23+

largeConvertToJSObject(xml: string, options?: ConvertOptions): Object

将XML文本转换为Object类型对象，适用于XML日志文件、数据报文等大型XML解析场景。此方法支持解析单元素大小超过10M的大型XML文本，针对大文本场景进行了优化，可有效避免单元素文本过大导致的解析异常。当[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)因单元素文本内容超过10M无法正常解析时，可使用本方法作为替代方案。

**说明** 

当传入的XML文本无法正确解析为Object类型对象时，输出异常日志信息并返回一个仅包含XML声明的基础Object对象。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，需符合XML语法规范，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象，包含解析后的XML结构信息，具体属性键名由ConvertOptions定义。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200002 | Invalid xml string. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let xmlString =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<?custom-pi processing="example"?>' +
    '<catalog id="books">' +
      '<!-- Bestseller Example -->' +
      '<book category="fiction" ref="B101">' +
        '<title>Echoes &amp; Whispers</title>' +
        '<price unit="USD">19.99</price>' +
        '<descr>' +
          '<![CDATA[<b>suspense</b>novel & Legendary Stories]]>' +
        '</descr>' +
        '<popular/>' +
      '</book>' +
    '</catalog>';
  // 创建ConvertXML转换实例
  let converter = new convertxml.ConvertXML();
  // 配置转换选项
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  // 调用largeConvertToJSObject接口转换大型XML文本
  let result = JSON.stringify(converter.largeConvertToJSObject(xmlString, options));
  console.info(result);
} catch (e) {
  let err: BusinessError = e as BusinessError;
  console.error(`Failed to convert XML text to JS object using largeConvertToJSObject. Code: ${err.code}, message: ${err.message}`);
}
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"instruction","_name":"custom-pi","_instruction":"processing=\"example\""},{"_type":"element","_name":"catalog","_attributes":{"id":"books"},"_elements":[{"_type":"comment","_comment":" Bestseller Example "},{"_type":"element","_name":"book","_parent":"catalog","_attributes":{"category":"fiction","ref":"B101"},"_elements":[{"_type":"element","_name":"title","_parent":"book","_elements":[{"_type":"text","_text":"Echoes & Whispers"}]},{"_type":"element","_name":"price","_parent":"book","_attributes":{"unit":"USD"},"_elements":[{"_type":"text","_text":"19.99"}]},{"_type":"element","_name":"descr","_parent":"book","_elements":[{"_type":"cdata","_cdata":"<b>suspense</b>novel & Legendary Stories"}]},{"_type":"element","_name":"popular","_parent":"book"}]}]}]}
```

### convertToJSObject(deprecated)

convertToJSObject(xml: string, options?: ConvertOptions) : Object

将XML文本转换为Object类型对象，适用于XML配置文件解析、数据格式转换等场景。该方法将XML文本解析为层级嵌套结构，各XML组件按ConvertOptions中配置的键名映射为对象的属性。

**说明** 

从API version 9开始支持，从API version 14开始废弃。建议使用[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)替代。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，需符合XML语法规范，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象，包含解析后的XML结构信息，具体属性键名由ConvertOptions定义。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200002 | Invalid xml string. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
      '<note importance="high" logged="true">' +
      '    <title>Happy</title>' +
      '    <todo>Work</todo>' +
      '    <todo>Play</todo>' +
      '</note>';
  // 创建ConvertXML转换实例
  let converter = new convertxml.ConvertXML();
  // 配置转换选项
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  // 调用convertToJSObject接口转换XML文本（已废弃，建议使用fastConvertToJSObject）
  let result = JSON.stringify(converter.convertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  let err: BusinessError = e as BusinessError;
  console.error(`Failed to convert XML text to JS object using convertToJSObject. Code: ${err.code}, message: ${err.message}`);
}
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

### convert(deprecated)

convert(xml: string, options?: ConvertOptions) : Object

将XML文本转换为Object类型对象。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[fastConvertToJSObject14+](js-apis-convertxml.md#fastconverttojsobject14)替代。

在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xml | string | 是 | XML文本，需符合XML语法规范，若包含“&”字符，请使用实体引用“&amp;”替换。 |
| options | [ConvertOptions](js-apis-convertxml.md#convertoptions) | 否 | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 转换后的JavaScript对象，包含解析后的XML结构信息，具体属性键名由ConvertOptions定义。 |

**示例：**

```ts
let xml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title>Happy</title>' +
    '    <todo>Work</todo>' +
    '    <todo>Play</todo>' +
    '</note>';
// 创建ConvertXML转换实例
let converter = new convertxml.ConvertXML();
// 配置转换选项
let options: convertxml.ConvertOptions = {
  trim: false,
  declarationKey: "_declaration",
  instructionKey: "_instruction",
  attributesKey: "_attributes",
  textKey: "_text",
  cdataKey: "_cdata",
  doctypeKey: "_doctype",
  commentKey: "_comment",
  parentKey: "_parent",
  typeKey: "_type",
  nameKey: "_name",
  elementsKey: "_elements"
};
// 调用convert接口转换XML文本（已废弃，建议使用fastConvertToJSObject）
let result = JSON.stringify(converter.convert(xml, options));
console.info(result);
// 输出(宽泛型)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

## ConvertOptions

转换选项，用于自定义XML到JavaScript对象的转换行为，如控制是否修剪空白字符、是否忽略特定组件（声明、指令、属性、注释、CDATA、Doctype和文本等），以及指定输出对象中各类型组件的属性键名称。

**说明** 

各键属性（declarationKey、instructionKey等）的取值应唯一，不可与其他键属性值重复，否则输出对象可能出现键名冲突。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trim | boolean | 否 | 否 | 是否修剪位于文本内容前后的空白字符，true表示元素内文本内容前后的空白字符将会被修剪，false则表示空白字符会被保留，默认false。 |
| ignoreDeclaration | boolean | 否 | 是 | 是否忽略XML声明，true表示忽略XML声明，false表示保留XML声明，默认false。 |
| ignoreInstruction | boolean | 否 | 是 | 是否忽略XML处理指令，true表示忽略XML处理指令，false表示保留XML处理指令，默认false。 |
| ignoreAttributes | boolean | 否 | 是 | 是否忽略元素的属性信息，true表示忽略元素的属性信息，false表示保留元素的属性信息，默认false。 |
| ignoreComment | boolean | 否 | 是 | 是否忽略元素的注释信息，true表示忽略元素的注释信息，false表示保留元素的注释信息，默认false。 |
| ignoreCDATA | boolean | 否 | 是 | 是否忽略元素的CDATA（Character Data）信息，true表示忽略元素的CDATA信息，false表示保留元素的CDATA信息，默认false。 |
| ignoreDoctype | boolean | 否 | 是 | 是否忽略Doctype（Document Type Declaration）信息，true表示忽略元素的Doctype信息，false表示保留元素的Doctype信息，默认false。 |
| ignoreText | boolean | 否 | 是 | 是否忽略元素的文本信息，true表示忽略元素的文本信息，false表示保留元素的文本信息，默认false。 |
| declarationKey | string | 否 | 否 | 用于输出对象中declaration的属性键的名称，仅在ignoreDeclaration为false时生效。 |
| instructionKey | string | 否 | 否 | 用于输出对象中instruction的属性键的名称，仅在ignoreInstruction为false时生效。 |
| attributesKey | string | 否 | 否 | 用于输出对象中attributes的属性键的名称，仅在ignoreAttributes为false时生效。 |
| textKey | string | 否 | 否 | 用于输出对象中text的属性键的名称，仅在ignoreText为false时生效。 |
| cdataKey | string | 否 | 否 | 用于输出对象中cdata的属性键的名称，仅在ignoreCDATA为false时生效。 |
| doctypeKey | string | 否 | 否 | 用于输出对象中doctype的属性键的名称，仅在ignoreDoctype为false时生效。 |
| commentKey | string | 否 | 否 | 用于输出对象中comment的属性键的名称，仅在ignoreComment为false时生效。 |
| parentKey | string | 否 | 否 | 用于输出对象中parent的属性键的名称，parent表示当前元素所属的父元素名称。 |
| typeKey | string | 否 | 否 | 用于输出对象中type的属性键的名称，type标识XML组件的类型（如element、text、cdata、comment、instruction等）。 |
| nameKey | string | 否 | 否 | 用于输出对象中name的属性键的名称。 |
| elementsKey | string | 否 | 否 | 用于输出对象中elements的属性键的名称。 |
