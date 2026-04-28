---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-conversion
title: XML转换
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS基础类库 > XML生成、解析与转换 > XML转换
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:640118ce5f35283ba907fb3bf04d824b5af7550c7f5d96b6e293721a4ef65057
---

将XML文本转换为JavaScript对象，便于处理和操作数据，适用于JavaScript应用程序。

语言基础类库提供ConvertXML类，将XML文本转换为JavaScript对象，输入为待转换的XML字符串及转换选项，输出为转换后的JavaScript对象。具体转换选项可见[API参考@ohos.convertxml](../harmonyos-references/js-apis-convertxml.md)。

## 注意事项

XML解析及转换需要确保传入的XML数据符合XML标准格式。

## 开发步骤

以XML转换为JavaScript对象为例，说明如何获取标签值。

1. 引入所需的模块。

   ```
   1. import { convertxml } from '@kit.ArkTS';
   ```
2. 输入待转换的XML，设置转换选项。支持的转换选项及含义，请参见[ConvertOptions](../harmonyos-references/js-apis-convertxml.md#convertoptions)。

   说明

   请确保传入的XML文本符合标准格式，若包含“&”字符，请使用实体引用“&amp;”替换。

   ```
   1. let xml: string =
   2. '<?xml version="1.0" encoding="utf-8"?>' +
   3. '<note importance="high" logged="true">' +
   4. '    <title>Happy</title>' +
   5. '    <todo>Work</todo>' +
   6. '    <todo>Play</todo>' +
   7. '</note>';
   8. let options: convertxml.ConvertOptions = {
   9. // trim: false 转换后是否删除文本前后的空格，否
   10. // declarationKey: "_declaration" 转换后文件声明使用_declaration来标识
   11. // instructionKey: "_instruction" 转换后指令使用_instruction标识
   12. // attributesKey: "_attributes" 转换后属性使用_attributes标识
   13. // textKey: "_text" 转换后标签值使用_text标识
   14. // cdataKey: "_cdata" 转换后未解析数据使用_cdata标识
   15. // docTypeKey: "_doctype" 转换后文档类型使用_doctype标识
   16. // commentKey: "_comment" 转换后注释使用_comment标识
   17. // parentKey: "_parent" 转换后父类使用_parent标识
   18. // typeKey: "_type" 转换后元素类型使用_type标识
   19. // nameKey: "_name" 转换后标签名称使用_name标识
   20. // elementsKey: "_elements" 转换后元素使用_elements标识
   21. trim: false,
   22. declarationKey: '_declaration',
   23. instructionKey: '_instruction',
   24. attributesKey: '_attributes',
   25. textKey: '_text',
   26. cdataKey: '_cdata',
   27. doctypeKey: '_doctype',
   28. commentKey: '_comment',
   29. parentKey: '_parent',
   30. typeKey: '_type',
   31. nameKey: '_name',
   32. elementsKey: '_elements'
   33. }
   ```
3. 调用fastConvertToJSObject函数并打印结果。

   ```
   1. let conv: convertxml.ConvertXML = new convertxml.ConvertXML();
   2. let result: object = conv.fastConvertToJSObject(xml, options);
   3. let strRes: string = JSON.stringify(result); // 将js对象转换为json字符串，用于显式输出
   4. console.info(strRes);
   ```

   输出结果如下所示：

   ```
   1. strRes:
   2. {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note",
   3. "_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_parent":"note",
   4. "_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_parent":"note","_elements":
   5. [{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_parent":"note","_elements":[{"_type":"text",
   6. "_text":"Play"}]}]}]}
   ```
