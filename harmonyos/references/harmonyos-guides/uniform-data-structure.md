---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-structure
title: 标准化数据结构 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 标准化数据结构 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2be3bbdef38b81fb3668472677811920a45002d0a9d28ffe8243ee2072f3ee16
---

## 场景介绍

针对UTD标准化数据类型[uniformdatatype](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformdatatype)中的部分常见类型，为了方便业务使用，我们按照不同的数据类型提供了标准化数据结构，例如系统定义的桌面图标类型（对应的标准化数据类型标识为'openharmony.app-item'），我们明确定义了该数据结构对应的相关描述信息。

某些业务场景下应用可以直接使用我们具体定义的UTD标准化数据结构，例如跨应用拖拽场景。拖出方应用可以按照标准化数据结构将拖拽数据写入拖拽事件[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)，拖入方应用从拖拽事件中读取拖拽数据并按照标准化数据结构进行数据的解析。这使得不同应用间的数据交互遵从相同的标准定义，有效减少了跨应用数据交互的开发工作量。

## 接口说明

UDMF针对部分标准化数据类型定义的标准化数据结构如下所示：

| 数据结构 | 数据类型 | 说明 |
| --- | --- | --- |
| [PlainText](../harmonyos-references/js-apis-data-uniformdatastruct.md#plaintext) | 'general.plain-text' | 纯文本。 |
| [Hyperlink](../harmonyos-references/js-apis-data-uniformdatastruct.md#hyperlink) | 'general.hyperlink' | 超链接。 |
| [HTML](../harmonyos-references/js-apis-data-uniformdatastruct.md#html) | 'general.html' | 富文本。 |
| [OpenHarmonyAppItem](../harmonyos-references/js-apis-data-uniformdatastruct.md#openharmonyappitem) | 'openharmony.app-item' | 图标。 |
| [ContentForm](../harmonyos-references/js-apis-data-uniformdatastruct.md#contentform14) | 'general.content-form' | 内容卡片。 |

## 开发步骤

以使用标准化数据结构定义数据内容（包含超链接、纯文本两条数据记录）为例，提供基本的开发步骤。

数据提供方可通过UDMF提供的addRecord()接口，使用getRecords()接口获取当前数据对象内的所有数据记录。

1. 导入对应模块。

   ```typescript
   // 1. 导入uniformDataStruct、unifiedDataChannel和uniformTypeDescriptor模块。
   import { uniformDataStruct, uniformTypeDescriptor, unifiedDataChannel } from '@kit.ArkData';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建超链接数据记录。
3. 创建纯文本数据类型记录。
4. 创建统一数据对象及记录。
5. 添加数据记录。
6. 获取当前UnifiedData对象内的所有数据记录。
7. 遍历每条记录，判断该记录的数据类型，转换为子类对象并得到原数据记录。

   ```typescript
   // 2. 创建超链接数据记录。
   let hyperlinkDetails: Record<string, string> = {
     'attr1': 'value1',
     'attr2': 'value2'
   }
   let hyperlink: uniformDataStruct.Hyperlink = {
     uniformDataType: 'general.hyperlink',
     url: 'www.XXX.com',
     description: 'This is the description of this hyperlink',
     details: hyperlinkDetails
   }

   // 修改hyperlink属性description
   hyperlink.description = '...';

   // 访问对象属性。
   hilog.info(0xFF00, '[Sample_Udmf]', `hyperlink.url = ${hyperlink.url}`);

   // 3. 创建纯文本数据类型记录。
   let plainTextDetails: Record<string, string> = {
     'attr1': 'value1',
     'attr2': 'value2'
   }
   let plainText: uniformDataStruct.PlainText = {
     uniformDataType: 'general.plain-text',
     textContent: 'This is plainText textContent example',
     abstract: 'this is abstract',
     details: plainTextDetails
   }
   // 4. 创建统一数据对象及记录。
   let unifiedData = new unifiedDataChannel.UnifiedData();
   let hyperlinkRecord =
     new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
   let plainTextRecord =
     new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);

   // 5. 添加数据记录。
   unifiedData.addRecord(hyperlinkRecord);
   unifiedData.addRecord(plainTextRecord);

   // 6. 记录添加完成后，可获取当前UnifiedData对象内的所有数据记录。
   let records = unifiedData.getRecords();

   // 7. 遍历每条记录，判断该记录的数据类型，转换为子类对象，得到原数据记录。
   for (let i = 0; i < records.length; i++) {
     let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
     let record = unifiedDataRecord.getValue() as object;
     if (record != undefined) {
       // 读取该数据记录的类型
       let type: string = record['uniformDataType'];
       switch (type) {
         case uniformTypeDescriptor.UniformDataType.HYPERLINK:
           Object.keys(record).forEach(key => {
             hilog.info(0xFF00, '[Sample_Udmf]', `show records: ${key}, value: ${record[key]}`);
           });
           break;
         case uniformTypeDescriptor.UniformDataType.PLAIN_TEXT:
           Object.keys(record).forEach(key => {
             hilog.info(0xFF00, '[Sample_Udmf]', `show records: ${key}, value: ${record[key]}`);
           });
           break;
         default:
           break;
       }
     }
   }
   ```
