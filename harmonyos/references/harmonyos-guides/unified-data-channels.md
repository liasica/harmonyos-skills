---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unified-data-channels
title: 通过标准化数据通路实现数据共享 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 跨应用数据共享 > 多对多跨应用数据共享 > 通过标准化数据通路实现数据共享 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:163708a3a49ac1aba4b7529a5a252db012f811cce80e21c51e7bcfb904801005
---

## 场景介绍

在多对多跨应用数据共享的场景下，需要提供一条数据通路能够写入多个不同应用的数据并共享给其他应用进行读取。

UDMF针对多对多跨应用数据共享的不同业务场景提供了标准化的数据通路，提供了标准化的数据写入与读取接口。

## 标准化数据通路的定义和实现

标准化数据通路是为各种业务场景提供的跨应用的数据写入与读取通路，它可以暂存应用需要共享的符合标准化数据定义的统一数据对象，并提供给其他应用进行访问，同时按照一定的策略对暂存数据的修改、删除权限和生命周期进行管理。

标准化数据通路通过UDMF提供的系统服务实现，应用（数据提供方）需要共享公共数据时可以通过UDMF提供的插入接口将数据写入到UDMF的数据通路中，并且可以通过UDMF提供的更新和删除接口对本应用已经存入数据进行更新和删除操作。目标应用（数据访问方）可以通过UDMF提供的读取接口进行数据的访问。

标准化数据通路相关接口不推荐多线程调用。

统一数据对象UnifiedData在UDMF数据通路中具有全局唯一URI标识，其定义为udmf://intention/bundleName/groupId，其中各组成部分的含义分别为：

* **udmf:** 协议名，表示使用UDMF提供的数据通路。
* **intention:** UDMF已经支持的数据通路类型枚举值，对应不同的业务场景。
* **bundleName:** 数据来源应用的包名称。
* **groupId:** 分组名称，支持批量数据分组管理。

当前UDMF中的跨应用数据共享通路有：**公共数据通路**

**公共数据通路**：应用共享的公用数据共享通路，所有应用均可向通路中写入数据，写入方可以根据写入数据时生成的数据唯一标识符进行数据的更新、删除、指定数据标识符进行查询、全量查询；数据读取方能通过唯一标识符读取指定的数据，也可以设置Intention枚举类型为DATA\_HUB来读取当前数据通路中的全量数据。公共数据通路通常仅用于传输应用间的过程数据，无法用于传输沙箱目录下文件等有权限管控的数据。UDMF会统一对数据的生命周期进行管理，每小时定期清理存入时长超过一小时的数据。

## 接口说明

以下是UDMF标准化数据通路的相关接口，更多接口及使用方式请见[标准化数据通路](../harmonyos-references/js-apis-data-unifieddatachannel.md)和[标准化数据定义与描述](../harmonyos-references/js-apis-data-uniformtypedescriptor.md)。

| 接口名称 | 描述 |
| --- | --- |
| insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void | 将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用callback异步回调。 |
| updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void | 更新已写入UDMF的公共数据通路的数据，使用callback异步回调。 |
| queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void | 查询UDMF公共数据通路的数据，使用callback异步回调。 |
| deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void | 删除UDMF公共数据通路的数据，返回删除的数据集，使用callback异步回调。 |

## 开发步骤

以[PlainText](../harmonyos-references/js-apis-data-uniformdatastruct.md#plaintext)、[HTML](../harmonyos-references/js-apis-data-uniformdatastruct.md#html)、[PixelMap](../harmonyos-references/js-apis-data-uniformdatastruct.md#pixelmap15)三种数据进行多对多数据共享的过程为例说明开发步骤，数据提供方可以通过UDMF提供的insertData接口将数据写入公共数据通路，获取到的返回值（生成的数据的唯一标识符），可用于对其插入的数据进行更新和删除操作。数据访问方则可以通过UDMF提供的查询接口获取当前公共数据通路的全量数据。

### 数据提供方

1. 导入unifiedDataChannel、uniformTypeDescriptor和uniformDataStruct模块。

   ```
   1. import { unifiedDataChannel, uniformTypeDescriptor, uniformDataStruct } from '@kit.ArkData';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L16-L19)
2. 创建一个统一数据对象并插入到UDMF的公共数据通路中。

   1. 导入对应数据对象模块。

      ```
      1. import { BusinessError } from '@kit.BasicServicesKit';
      2. import { image } from '@kit.ImageKit';
      ```

      [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L21-L24)
   2. 创建并插入数据。

      ```
      1. // 准备PlainText文本数据内容
      2. let plainTextObj: uniformDataStruct.PlainText = {
      3. uniformDataType: 'general.plain-text',
      4. textContent: 'Hello world',
      5. abstract: 'This is abstract'
      6. }
      7. let record =
      8. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextObj);
      9. // 准备HTML数据内容
      10. let htmlObj: uniformDataStruct.HTML = {
      11. uniformDataType: 'general.html',
      12. htmlContent: '<div><p>Hello world</p></div>',
      13. plainContent: 'Hello world'
      14. }
      15. // 为该记录增加一种样式，两种样式存储的是同一个数据，为不同表达形式
      16. record.addEntry(uniformTypeDescriptor.UniformDataType.HTML, htmlObj);
      17. let unifiedData = new unifiedDataChannel.UnifiedData(record);

      19. // 准备pixelMap数据内容
      20. let arrayBuffer = new ArrayBuffer(4 * 3 * 3);
      21. let opt: image.InitializationOptions = {
      22. editable: true,
      23. pixelFormat: 3,
      24. size: { height: 3, width: 3 },
      25. alphaType: 3
      26. };
      27. let pixelMap: uniformDataStruct.PixelMap = {
      28. uniformDataType: 'openharmony.pixel-map',
      29. pixelMap: image.createPixelMapSync(arrayBuffer, opt)
      30. }
      31. unifiedData.addRecord(new unifiedDataChannel.UnifiedRecord(
      32. uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap));
      33. // 指定要插入数据的数据通路枚举类型
      34. let options: unifiedDataChannel.Options = {
      35. intention: unifiedDataChannel.Intention.DATA_HUB
      36. }
      37. try {
      38. unifiedDataChannel.insertData(options, unifiedData, (err, key) => {
      39. if (err === undefined) {
      40. hilog.info(0xFF00, '[Sample_Udmf]', `Succeeded in inserting data. key = ${key}`);
      41. } else {
      42. hilog.error(0xFF00, '[Sample_Udmf]', `Succeeded in inserting data. key = ${key})`);
      43. }
      44. });
      45. } catch (e) {
      46. let error: BusinessError = e as BusinessError;
      47. hilog.error(0xFF00, '[Sample_Udmf]',
      48. `Insert data throws an exception. code is ${error.code},message is ${error.message}`);
      49. }
      ```

      [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L27-L77)
3. 更新上一步插入的统一数据对象。

   ```
   1. let plainTextUpdate: uniformDataStruct.PlainText = {
   2. uniformDataType: 'general.plain-text',
   3. textContent: 'How are you',
   4. abstract: 'This is abstract'
   5. }
   6. let recordUpdate =
   7. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextUpdate);
   8. let htmlUpdate: uniformDataStruct.HTML = {
   9. uniformDataType: 'general.html',
   10. htmlContent: '<div><p>How are you</p></div>',
   11. plainContent: 'How are you'
   12. }
   13. recordUpdate.addEntry(uniformTypeDescriptor.UniformDataType.HTML, htmlUpdate);
   14. let unifiedDataUpdate = new unifiedDataChannel.UnifiedData(recordUpdate);

   16. // 指定要更新的统一数据对象的URI
   17. let optionsUpdate: unifiedDataChannel.Options = {
   18. // 此处的key值仅为示例，不可直接使用，其值与insertData接口回调函数中key保持一致
   19. key: 'udmf://DataHub/com.ohos.test/0123456789'
   20. };

   22. try {
   23. unifiedDataChannel.updateData(optionsUpdate, unifiedDataUpdate, (err) => {
   24. if (err === undefined) {
   25. hilog.info(0xFF00, '[Sample_Udmf]', `Succeeded in updating data.`);
   26. } else {
   27. hilog.error(0xFF00, '[Sample_Udmf]', `Failed to update data. code is ${err.code},message is ${err.message}`);
   28. }
   29. });
   30. } catch (e) {
   31. let error: BusinessError = e as BusinessError;
   32. hilog.error(0xFF00, '[Sample_Udmf]',
   33. `Update data throws an exception. code is ${error.code},message is ${error.message}`);
   34. }
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L81-L116)
4. 删除存储在UDMF公共数据通路中的统一数据对象。

   ```
   1. // 指定要删除数据的数据通路枚举类型
   2. let optionsDelete: unifiedDataChannel.Options = {
   3. intention: unifiedDataChannel.Intention.DATA_HUB
   4. };

   6. try {
   7. unifiedDataChannel.deleteData(optionsDelete, (err, data) => {
   8. if (err === undefined) {
   9. hilog.info(0xFF00, '[Sample_Udmf]', `Succeeded in deleting data. size = ${data.length}`);
   10. for (let i = 0; i < data.length; i++) {
   11. let records = data[i].getRecords();
   12. for (let j = 0; j < records.length; j++) {
   13. let types = records[j].getTypes();
   14. // 根据业务需要从记录中获取样式数据
   15. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
   16. let text =
   17. records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
   18. hilog.info(0xFF00, '[Sample_Udmf]', `${i + 1}.${text.textContent}`);
   19. }
   20. if (types.includes(uniformTypeDescriptor.UniformDataType.HTML)) {
   21. let html =
   22. records[j].getEntry(uniformTypeDescriptor.UniformDataType.HTML) as uniformDataStruct.HTML;
   23. hilog.info(0xFF00, '[Sample_Udmf]', `${i + 1}.${html.htmlContent}`);
   24. }
   25. }
   26. }
   27. } else {
   28. hilog.error(0xFF00, '[Sample_Udmf]', `Failed to delete data. code is ${err.code},message is ${err.message}`);
   29. }
   30. });
   31. } catch (e) {
   32. let error: BusinessError = e as BusinessError;
   33. hilog.error(0xFF00, '[Sample_Udmf]',
   34. `Delete data throws an exception. code is ${error.code},message is ${error.message}`);
   35. }
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L120-L156)

### 数据访问方

1. 导入unifiedDataChannel、uniformTypeDescriptor和uniformDataStruct模块。

   ```
   1. import { unifiedDataChannel, uniformTypeDescriptor, uniformDataStruct } from '@kit.ArkData';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L16-L19)
2. 查询存储在UDMF公共数据通路中的全量统一数据对象。

   ```
   1. // 指定要查询数据的数据通路枚举类型
   2. let options: unifiedDataChannel.Options = {
   3. intention: unifiedDataChannel.Intention.DATA_HUB
   4. };

   6. try {
   7. unifiedDataChannel.queryData(options, (err, data) => {
   8. if (err === undefined) {
   9. hilog.info(0xFF00, '[Sample_Udmf]', `Succeeded in querying data. size = ${data.length}`);
   10. for (let i = 0; i < data.length; i++) {
   11. let records = data[i].getRecords();
   12. for (let j = 0; j < records.length; j++) {
   13. let types = records[j].getTypes();
   14. // 根据业务需要从记录中获取样式数据
   15. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
   16. let text =
   17. records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
   18. hilog.info(0xFF00, '[Sample_Udmf]', `${i + 1}.${text.textContent}`);
   19. }
   20. if (types.includes(uniformTypeDescriptor.UniformDataType.HTML)) {
   21. let html =
   22. records[j].getEntry(uniformTypeDescriptor.UniformDataType.HTML) as uniformDataStruct.HTML;
   23. hilog.info(0xFF00, '[Sample_Udmf]', `${i + 1}.${html.htmlContent}`);
   24. }
   25. }
   26. }
   27. } else {
   28. hilog.error(0xFF00, '[Sample_Udmf]', `Failed to query data. code is ${err.code},message is ${err.message}`);
   29. }
   30. });
   31. } catch (e) {
   32. let error: BusinessError = e as BusinessError;
   33. hilog.error(0xFF00, '[Sample_Udmf]',
   34. `Query data throws an exception. code is ${error.code},message is ${error.message}`);
   35. }
   ```

   [UdmfInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels/entry/src/main/ets/pages/UdmfInterface.ets#L160-L196)
