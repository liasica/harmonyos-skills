---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-structure
title: 标准化数据结构 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 标准化数据结构 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe0766355a15c269a127b746e56e79eae6c948a6fbc8187b55a812f6b6e2929b
---

## 场景介绍

针对[UTD标准化数据类型](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformdatatype)中的部分常见类型，为了方便业务使用，我们按照不同的数据类型提供了标准化数据结构，例如系统定义的桌面图标类型（对应的标准化数据类型标识为'openharmony.app-item'），我们明确定义了该数据结构对应的相关描述信息。

某些业务场景下应用可以直接使用我们具体定义的UTD标准化数据结构，例如跨应用拖拽场景。拖出方应用可以按照标准化数据结构将拖拽数据写入[拖拽事件](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)，拖入方应用从拖拽事件中读取拖拽数据并按照标准化数据结构进行数据的解析。这使得不同应用间的数据交互遵从相同的标准定义，有效减少了跨应用数据交互的开发工作量。

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

   ```
   1. // 1. 导入unifiedDataChannel和uniformTypeDescriptor模块。
   2. import { uniformDataStruct, uniformTypeDescriptor, unifiedDataChannel } from '@kit.ArkData';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataStructure/entry/src/main/ets/pages/UdmfInterface.ets#L16-L20)
2. 创建超链接数据记录。
3. 创建数据记录并添加到统一数据对象中。
4. 创建统一数据对象实例。
5. 添加plainText数据记录。
6. 添加并获取当前UnifiedData对象内的所有数据记录。
7. 遍历每条记录，判断该记录的数据类型，转换为子类对象并得到原数据记录。

   ```
   1. // 2. 创建超链接数据记录。
   2. let hyperlinkDetails: Record<string, string> = {
   3. 'attr1': 'value1',
   4. 'attr2': 'value2'
   5. }
   6. let hyperlink: uniformDataStruct.Hyperlink = {
   7. uniformDataType: 'general.hyperlink',
   8. url: 'www.XXX.com',
   9. description: 'This is the description of this hyperlink',
   10. details: hyperlinkDetails
   11. }

   13. // 修改hyperlink属性description
   14. hyperlink.description = '...';

   16. // 访问对象属性。
   17. hilog.info(0xFF00, '[Sample_Udmf]', `hyperlink.url = ${hyperlink.url}`);

   19. // 3. 创建纯文本数据类型记录，将其添加到刚才创建的UnifiedData对象。
   20. let plainTextDetails: Record<string, string> = {
   21. 'attr1': 'value1',
   22. 'attr2': 'value2'
   23. }
   24. let plainText: uniformDataStruct.PlainText = {
   25. uniformDataType: 'general.plain-text',
   26. textContent: 'This is plainText textContent example',
   27. abstract: 'this is abstract',
   28. details: plainTextDetails
   29. }
   30. // 4. 创建一个统一数据对象实例。
   31. let unifiedData = new unifiedDataChannel.UnifiedData();
   32. let hyperlinkRecord =
   33. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
   34. let plainTextRecord =
   35. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);

   37. // 5. 添加plainText数据记录。
   38. unifiedData.addRecord(hyperlinkRecord);
   39. unifiedData.addRecord(plainTextRecord);

   41. // 6. 记录添加完成后，可获取当前UnifiedData对象内的所有数据记录。
   42. let records = unifiedData.getRecords();

   44. // 7. 遍历每条记录，判断该记录的数据类型，转换为子类对象，得到原数据记录。
   45. for (let i = 0; i < records.length; i++) {
   46. let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
   47. let record = unifiedDataRecord.getValue() as object;
   48. if (record != undefined) {
   49. // 读取该数据记录的类型
   50. let type: string = record['uniformDataType'];
   51. switch (type) {
   52. case uniformTypeDescriptor.UniformDataType.HYPERLINK:
   53. Object.keys(record).forEach(key => {
   54. hilog.info(0xFF00, '[Sample_Udmf]', `show records: ${key} + , value: ${record[key]}`);
   55. });
   56. break;
   57. case uniformTypeDescriptor.UniformDataType.PLAIN_TEXT:
   58. Object.keys(record).forEach(key => {
   59. hilog.info(0xFF00, '[Sample_Udmf]', `show records: ${key} + , value: ${record[key]}`);
   60. });
   61. break;
   62. default:
   63. break;
   64. }
   65. }
   66. }
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataStructure/entry/src/main/ets/pages/UdmfInterface.ets#L23-L90)
