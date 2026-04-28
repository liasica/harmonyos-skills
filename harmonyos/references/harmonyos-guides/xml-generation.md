---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-generation
title: XML生成
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS基础类库 > XML生成、解析与转换 > XML生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2cd29a9dfcf90db14e28d96f04e3933ecffd457e696669d9b7ca92da1137bd5
---

XML可以作为数据交换格式，被各种系统和应用程序支持。例如Web服务，可以将结构化数据以XML格式进行传递。

XML还可以作为消息传递格式，用于分布式系统中不同节点的通信。

## 注意事项

* XML标签必须成对出现，生成开始标签就要生成结束标签。
* XML标签对大小写敏感，开始标签与结束标签大小写要一致。

## 开发步骤

XML模块提供XmlSerializer及XmlDynamicSerializer类来生成XML数据，使用XmlSerializer需传入固定长度的ArrayBuffer或DataView对象作为输出缓冲区，用于存储序列化后的XML数据。

XmlDynamicSerializer类动态扩容，程序根据实际生成的数据大小自动创建ArrayBuffer。

调用不同的方法写入不同的内容，如startElement(name: string)写入元素开始标记，setText(text: string)写入标签值。

XML模块的API接口可以参考[@ohos.xml](../harmonyos-references/js-apis-xml.md)的详细描述，按需求调用相应的函数可以生成一份完整的XML数据。

使用XmlSerializer生成XML示例如下：

1. 引入模块。

   ```
   1. import { xml, util } from '@kit.ArkTS';
   ```
2. 创建缓冲区，构造XmlSerializer对象。可以基于ArrayBuffer构造XmlSerializer对象，也可以基于DataView构造XmlSerializer对象。

   方式1：基于ArrayBuffer构造XmlSerializer对象

   ```
   1. let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
   2. let serializer: xml.XmlSerializer = new xml.XmlSerializer(arrayBuffer); // 基于ArrayBuffer构造XmlSerializer对象
   ```

   方式2：基于DataView构造XmlSerializer对象

   ```
   1. let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
   2. let dataView: DataView = new DataView(arrayBuffer); // 创建一个DataView
   3. let serializer: xml.XmlSerializer = new xml.XmlSerializer(dataView); // 基于DataView构造XmlSerializer对象
   ```
3. 调用XML元素生成函数。

   ```
   1. serializer.setDeclaration(); // 写入XML的声明
   2. serializer.startElement('bookstore'); // 写入元素开始标记
   3. serializer.startElement('book'); // 嵌套元素开始标记
   4. serializer.setAttributes('category', 'COOKING'); // 写入属性及其属性值
   5. serializer.startElement('title');
   6. serializer.setAttributes('lang', 'en');
   7. serializer.setText('Everyday'); // 写入标签值
   8. serializer.endElement(); // 写入结束标记
   9. serializer.startElement('author');
   10. serializer.setText('Giana');
   11. serializer.endElement();
   12. serializer.startElement('year');
   13. serializer.setText('2005');
   14. serializer.endElement();
   15. serializer.endElement();
   16. serializer.endElement();
   ```
4. 使用Uint8Array操作ArrayBuffer，并调用TextDecoder对Uint8Array解码后输出。

   ```
   1. let uint8Array: Uint8Array = new Uint8Array(arrayBuffer); // 使用Uint8Array读取arrayBuffer的数据
   2. let textDecoder: util.TextDecoder = util.TextDecoder.create(); // 调用util模块的TextDecoder类
   3. let result: string = textDecoder.decodeToString(uint8Array); // 对uint8Array解码
   4. console.info(result);
   ```

   输出结果如下：

   ```
   1. <?xml version="1.0" encoding="utf-8"?><bookstore>
   2. <book category="COOKING">
   3. <title lang="en">Everyday</title>
   4. <author>Giana</author>
   5. <year>2005</year>
   6. </book>
   7. </bookstore>
   ```

使用XmlDynamicSerializer生成XML示例如下：

1. 引入模块。

   ```
   1. import { xml, util } from '@kit.ArkTS';
   ```
2. 调用XML元素生成函数。

   ```
   1. let dySerializer = new xml.XmlDynamicSerializer('utf-8');
   2. dySerializer.setDeclaration(); // 写入XML的声明
   3. dySerializer.startElement('bookstore'); // 写入元素开始标记
   4. dySerializer.startElement('book'); // 嵌套元素开始标记
   5. dySerializer.setAttributes('category', 'COOKING'); // 写入属性及其属性值
   6. dySerializer.startElement('title');
   7. dySerializer.setAttributes('lang', 'en');
   8. dySerializer.setText('Everyday'); // 写入标签值
   9. dySerializer.endElement(); // 写入结束标记
   10. dySerializer.startElement('author');
   11. dySerializer.setText('Giana');
   12. dySerializer.endElement();
   13. dySerializer.startElement('year');
   14. dySerializer.setText('2005');
   15. dySerializer.endElement();
   16. dySerializer.endElement();
   17. dySerializer.endElement();
   18. let arrayBuffer = dySerializer.getOutput();
   ```
3. 使用Uint8Array操作ArrayBuffer，并调用TextDecoder对Uint8Array解码后输出。

   ```
   1. let uint8Array: Uint8Array = new Uint8Array(arrayBuffer);
   2. let result: string = util.TextDecoder.create().decodeToString(uint8Array);
   3. console.info(result);
   ```

   输出结果如下：

   ```
   1. <?xml version="1.0" encoding="utf-8"?>
   2. <bookstore>
   3. <book category="COOKING">
   4. <title lang="en">Everyday</title>
   5. <author>Giana</author>
   6. <year>2005</year>
   7. </book>
   8. </bookstore>
   ```
