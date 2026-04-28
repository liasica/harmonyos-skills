---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-parsing
title: XML解析
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS基础类库 > XML生成、解析与转换 > XML解析
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8536ec77ddbbfff6f9405eb8e5f6dfb511892110cdba2a1558238d5a39b3944
---

对于以XML作为载体传递的数据，实际使用中需要对相关的元素进行解析，一般包括[解析XML标签和标签值](xml-parsing.md#解析xml标签和标签值)、[解析XML属性和属性值](xml-parsing.md#解析xml属性和属性值)、[解析XML事件类型和元素信息](xml-parsing.md#解析xml事件类型和元素信息)三类操作。如在Web服务中，XML是SOAP（Simple Object Access Protocol）协议的基础，SOAP消息通常以XML格式封装，包含请求和响应参数，通过解析这些XML消息，Web服务可以处理来自客户端的请求并生成相应的响应。

XML模块提供XmlPullParser类用于解析XML文本，输入为包含XML数据的ArrayBuffer或DataView，输出为结构化的解析结果。

**表1** XML解析选项，其详细介绍请参见[ParseOptions](../harmonyos-references/js-apis-xml.md#parseoptions)。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supportDoctype | boolean | 否 | 是否解析文档类型，false表示不解析文档类型，true表示解析文档类型，默认false。 |
| ignoreNameSpace | boolean | 否 | 是否忽略命名空间，忽略命名空间后，将不会对其进行解析。true表示忽略命名空间，false表示不忽略命名空间，默认false。 |
| tagValueCallbackFunction | (name: string, value: string) => boolean | 否 | 获取tagValue回调函数，打印XML标签及标签值。默认为undefined，表示不解析XML标签和标签值。 |
| attributeValueCallbackFunction | (name: string, value: string) => boolean | 否 | 获取attributeValue回调函数，打印XML属性及属性值。默认为undefined，表示不解析XML属性和属性值。 |
| tokenValueCallbackFunction | (eventType: EventType, value: ParseInfo) => boolean | 否 | 获取tokenValue回调函数，打印XML事件类型及parseInfo对应属性。默认为undefined，表示不解析XML事件类型。 |

## 注意事项

* 确保传入的XML数据符合标准格式。
* 目前不支持解析指定节点的值。

## 解析XML标签和标签值

1. 引入模块。

   ```
   1. import { xml, util } from '@kit.ArkTS'; // 需要使用util模块函数对文本编码
   ```
2. 对XML文本编码后调用XmlPullParser。

   可以基于ArrayBuffer创建XmlPullParser对象，也可以基于DataView创建XmlPullParser对象（两种创建方式返回结果无区别）。

   ```
   1. let strXml: string =
   2. '<?xml version="1.0" encoding="utf-8"?>' +
   3. '<note importance="high" logged="true">' +
   4. '<title>Play</title>' +
   5. '<lens>Work</lens>' +
   6. '</note>';
   7. let textEncoder: util.TextEncoder = new util.TextEncoder();
   8. let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml); // 对数据进行编码，防止中文字符乱码
   9. // 方式1：基于ArrayBuffer构造XmlPullParser对象
   10. let xmlParser: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
   ```

   ```
   1. // 方式2：基于DataView构造XmlPullParser对象
   2. let dataView: DataView = new DataView(arrBuffer.buffer as object as ArrayBuffer);
   3. let xmlParser: xml.XmlPullParser = new xml.XmlPullParser(dataView, 'UTF-8');
   ```
3. 自定义回调函数，本例直接打印出标签及标签值。

   ```
   1. function func(name: string, value: string): boolean {
   2. if (name == 'note') {
   3. console.info(name);
   4. }
   5. if (value == 'Play' || value == 'Work') {
   6. console.info('    ' + value);
   7. // ...
   8. }
   9. if (name == 'title' || name == 'lens') {
   10. console.info('  ' + name);
   11. }
   12. return true; //true:继续解析 false:停止解析
   13. }
   ```
4. 设置解析选项，调用parseXml函数。

   ```
   1. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func};
   2. xmlParser.parseXml(options);
   ```

   输出结果如下所示：

   ```
   1. note
   2. title
   3. Play
   4. title
   5. lens
   6. Work
   7. lens
   8. note
   ```

## 解析XML属性和属性值

1. 引入模块。

   ```
   1. import { xml, util } from '@kit.ArkTS'; // 使用util模块对文本编码
   ```
2. 对XML文本编码后调用XmlPullParser。

   ```
   1. let strXml: string =
   2. '<?xml version="1.0" encoding="utf-8"?>' +
   3. '<note importance="high" logged="true">' +
   4. '    <title>Play</title>' +
   5. '    <title>Happy</title>' +
   6. '    <lens>Work</lens>' +
   7. '</note>';
   8. let textEncoder: util.TextEncoder = new util.TextEncoder();
   9. let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml); // 对数据进行编码，防止中文字符乱码
   10. let xmlParser: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
   ```
3. 自定义回调函数，示例直接打印出属性及属性值。

   ```
   1. let str: string = '';
   2. function func(name: string, value: string): boolean {
   3. str += name + ' ' + value + ' ';
   4. return true; // true:继续解析 false:停止解析
   5. }
   ```
4. 设置解析选项，调用parseXml函数。

   ```
   1. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, attributeValueCallbackFunction:func};
   2. xmlParser.parseXml(options);
   3. console.info(str); // 打印所有属性及其值
   ```

   输出结果如下所示：

   ```
   1. importance high logged true // note节点的属性及属性值
   ```

## 解析XML事件类型和元素信息

1. 引入模块。

   ```
   1. import { xml, util } from '@kit.ArkTS'; // 使用util模块函数对文本编码
   ```
2. 对XML文本编码后调用XmlPullParser。

   ```
   1. let strXml: string =
   2. '<?xml version="1.0" encoding="utf-8"?>' +
   3. '<note importance="high" logged="true">' +
   4. '<title>Play</title>' +
   5. '</note>';
   6. let textEncoder: util.TextEncoder = new util.TextEncoder();
   7. let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml); // 对数据进行编码，防止中文字符乱码
   8. let xmlParser: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
   ```
3. 自定义回调函数，示例直接打印元素事件类型及元素深度。

   ```
   1. let str: string = '';
   2. function func(name: xml.EventType, value: xml.ParseInfo): boolean {
   3. str = name + ' ' + value.getDepth(); // getDepth 获取元素在XML文档中的当前深度
   4. console.info(str);
   5. // ...
   6. return true; // true:继续解析 false:停止解析
   7. }
   ```
4. 设置解析选项，调用parseXml函数。

   ```
   1. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func};
   2. xmlParser.parseXml(options);
   ```

   输出结果如下所示：

   ```
   1. 0 0 // 0：<?xml version="1.0" encoding="utf-8"?> 对应事件类型START_DOCUMENT值为0  0：起始深度为0
   2. 2 1 // 2：<note importance="high" logged="true"> 对应事件类型START_TAG值为2  1：深度为1
   3. 2 2 // 2：<title>对应事件类型START_TAG值为2  2：深度为2
   4. 4 2 // 4：Play对应事件类型TEXT值为4  2：深度为2
   5. 3 2 // 3：</title>对应事件类型END_TAG值为3  2：深度为2
   6. 3 1 // 3：</note>对应事件类型END_TAG值为3  1：深度为1（与<note对应>）
   7. 1 0 // 1：对应事件类型END_DOCUMENT值为1  0：深度为0
   ```

## 场景示例

此处以调用所有解析选项为例，提供解析XML标签、属性和事件类型的开发示例。

```
1. import { xml, util } from '@kit.ArkTS';
2. // ...
3. let strXml: string =
4. '<?xml version="1.0" encoding="UTF-8"?>' +
5. '<book category="COOKING">' +
6. '<title lang="en">Everyday</title>' +
7. '<author>Giana</author>' +
8. '</book>';
9. let textEncoder: util.TextEncoder = new util.TextEncoder();
10. let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml);
11. let xmlParser: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
12. let str: string = '';

14. function tagFunc(name: string, value: string): boolean {
15. str = name + value;
16. console.info('tag-' + str);
17. return true;
18. }

20. function attFunc(name: string, value: string): boolean {
21. str = name + ' ' + value;
22. console.info('attri-' + str);
23. return true;
24. }

26. function tokenFunc(name: xml.EventType, value: xml.ParseInfo): boolean {
27. str = name + ' ' + value.getDepth();
28. console.info('token-' + str);
29. // ...
30. return true;
31. }
32. // ...
33. let options: xml.ParseOptions = {
34. supportDoctype: true,
35. ignoreNameSpace: true,
36. tagValueCallbackFunction: tagFunc,
37. attributeValueCallbackFunction: attFunc,
38. tokenValueCallbackFunction: tokenFunc
39. };
40. xmlParser.parseXml(options);
```

输出结果如下所示：

```
1. tag-
2. token-0 0
3. tag-book
4. token-2 1
5. attri-category COOKING
6. tag-title
7. token-2 2
8. attri-lang en
9. tag-Everyday
10. token-4 2
11. tag-title
12. token-3 2
13. tag-author
14. token-2 2
15. tag-Giana
16. token-4 2
17. tag-author
18. token-3 2
19. tag-book
20. token-3 1
21. tag-
22. token-1 0
```
