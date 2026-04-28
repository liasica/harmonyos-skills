---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing
title: 知识加工
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > 知识加工
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:574d832b0c3e1558a62a89c311179ec825c49b53a7e22306fb84a60d1023981c
---

知识加工是指根据实际业务数据生成知识库的能力，主要包含以下两个方面：

* 通过配置schema生成知识加工的产物（如倒排表、向量库、向量表），这些产物最终用于知识问答过程中的检索。schema的配置应基于实际业务使用的数据库及数据表结构。知识加工和检索对中文处理进行了优化，因此中文问答的效果优于英文。
* 通过调用获取知识加工状态的接口，查询当前的加工状态。

知识加工支持处理如下文件类型。

* 文本和网页类型：txt、html。
* 办公文件类型：doc、docx、ppt、pptx、xls、xlsx、pdf，仅支持纯文本的基本处理，复杂或特定内容可由应用侧自行解析处理后转成txt格式进行后续加工。
* 图片类型：jpeg、jpg、png。

从6.1.0(23)版本开始，新增支持关键字表和时间特征表。当前知识加工生成的产物结构如下：

**表1** 倒排表结构

| 列名 | 类型 | 含义 |
| --- | --- | --- |
| reference\_id | UNINDEXED | 关联id，与业务表主键id对应。 |
| chunk\_id | UNINDEXED | 用于标识每一个切分后的Chunk。一个Chunk代表需要进行知识加工的文本的一个切片。 |
| chunk\_source | UNINDEXED | 每个Chunk在业务表中的字段归属。 |
| chunk\_text | TEXT | 倒排索引字段，每个Chunk的文本内容。 |

**表2** 向量表结构

| 列名 | 类型 | 含义 |
| --- | --- | --- |
| id | INTEGER | 自增主键。 |
| reference\_id | INTEGER | 关联id，与业务表主键id对应。 |
| chunk\_id | TEXT | 用于标识每一个切分后的Chunk。一个Chunk代表需要进行知识加工的文本的一个切片。 |
| chunk\_source | TEXT | 每个Chunk在业务表中的字段归属。 |
| repr | FLOATVECTOR(128) | chunk\_id对应的文本的向量表征。 |
| Scalar | TEXT | Schema中定义的所有标量字段，类型均为TEXT。 |

**表3** 关键字表结构

| 列名 | 类型 | 含义 |
| --- | --- | --- |
| id | INTEGER | 自增主键。 |
| reference\_id | INTEGER | 关联id，与业务表主键id对应。 |
| chunk\_id | TEXT | 用于标识每一个切分后的Chunk。一个Chunk代表需要进行知识加工的文本的一个切片。 |
| word | TEXT | 匹配到的关键字。 |
| extendFields | TEXT | Schema中customKeyword字段下extendFields定义的所有列，每个字段一列，类型均为TEXT。 |

**表4** 时间特征表结构

| 列名 | 类型 | 含义 |
| --- | --- | --- |
| id | INTEGER | 自增主键。 |
| reference\_id | INTEGER | 关联id，与业务表主键id对应。 |
| chunk\_id | TEXT | 用于标识每一个切分后的Chunk。一个Chunk代表需要进行知识加工的文本的一个切片。 |
| start\_time | TEXT | 匹配到的时间段的开始时间。 |
| end\_time | TEXT | 匹配到的时间段的结束时间。 |
| extendFields | TEXT | Schema中time字段下extendFields定义的所有列，每个字段一列，类型均为TEXT。 |

## 触发知识加工的时机

触发知识加工包含下列两种情况。

* 通过[开发步骤](data-augmentation-knowledge-processing.md#开发步骤)配置knowledge\_schema.json和开库参数后，每次开库都会启动一次知识加工任务。
* 当已经成功开库并且存在一个活跃的数据库连接时，数据源表发生数据变更（插入、更新、删除）时会自动触发加工任务。

## 约束限制

1. 知识加工使用的表不支持同时进行端端同步、端云同步以及搜索。
2. 知识加工schema配置文件为src/main/resources/rawfile/arkdata/knowledge/knowledge\_schema.json，文件内容必须是合法的Json字符串。
3. 知识加工清理接口：在schema升级场景下，首次开库或调用getKnowledgeProcessor接口前调用cleanKnowledgeData接口。

## 接口说明

知识加工关键接口[common.BaseContext](../harmonyos-references/js-apis-inner-application-basecontext.md)如下表所示，具体API说明详见[API参考](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getKnowledgeProcessor](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#getknowledgeprocessor)(context: [common.BaseContext](../harmonyos-references/js-apis-inner-application-basecontext.md), config: [KnowledgeProcessorConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig)): Promise<[KnowledgeProcessor](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessor)> | 获取知识加工对象，进行获取知识加工状态等操作。 |
| [getStatus](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#getstatus)(): Promise<[ProcessorStatus](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#processorstatus)> | 获取知识加工状态。 |
| [startProcess](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#startprocess)(option: [KnowledgeProcessConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessconfig)): Promise<void> | 根据入参的配置，启动知识加工。 |
| [stopProcess](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#stopprocess)(): Promise<void> | 停止当前知识加工。 |
| [cleanKnowledgeData](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#cleanknowledgedata)(context: [common.BaseContext](../harmonyos-references/js-apis-inner-application-basecontext.md), config: [KnowledgeProcessorConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig)): Promise<void> | 清理知识库，根据入参中的知识加工配置获取对应知识库信息，将知识库进行清理。 |
| [getRdbStore](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstore-1)(context: [Context](../harmonyos-references/js-apis-inner-application-context.md), config: [StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)): Promise<[RdbStore](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md)> | 创建或打开已有的关系型数据库，按照步骤2配置开库参数后，调用该接口可触发知识加工。 |

## 开发步骤

从6.1.0(23)版本开始，知识加工schema配置文件knowledge\_schema.json新增支持commonAttribute和customKeyword参数；knowledgeField的type字段新增支持Markdown类型。

1. 配置知识加工schema文件knowledge\_schema.json，下文是配置示例，实际文件内容请根据业务需要进行配置。知识加工产物命名规则如下：

   * 倒排库与数据源库是同一个数据库。
   * 倒排表名相较于数据源表名增加了"\_inverted"后缀（email->email\_inverted）。
   * 向量库名相较于数据源库名增加了"\_vector"后缀（testmail\_store.db->testmail\_store\_vector.db）。
   * 向量表名相较于数据源表名增加了"\_vector"后缀（email->email\_vector）。

   ```
   1. // 文件路径：src/main/resources/rawfile/arkdata/knowledge/knowledge_schema.json
   2. // 项目中没有该目录请递归创建
   3. // 实际使用时请去除注释，示例中增加注释仅作字段说明用
   4. {
   5. "knowledgeSource": [{
   6. "version": 1,
   7. "dbName": "testmail_store.db",  // 存储原始数据的数据库文件名
   8. "tables": [{
   9. "tableName": "email",  // 用于知识加工的表名
   10. "referenceFields": ["id"],  // 知识数据源引用字段，用于关联知识库中的数据
   11. "processSequence": {  // 定义加工顺序为id倒序
   12. "columnName": "id",
   13. "sortType": "DESC"
   14. },
   15. "customKeyword": {
   16. "wordTablePath": "/data/storage/el2/base/haps/entry/files/keywords.txt", // 此处仅作示例，实际文件路径根据业务实际情况配置
   17. "sourceFields": ["subject", "content"],  // 关键字提取生效的列
   18. "extendFields": []  // 创建关键字表时额外增加的列，数据与源表一致
   19. },
   20. "commonAttribute": {
   21. "time": {
   22. "baseTimeField": "received_date",
   23. "sourceFields": ["subject", "content"],
   24. "extendFields": ["sender"]
   25. }
   26. },
   27. "knowledgeFields": [{  // 关注的知识字段
   28. "columnName": "subject",  // 关注的字段名称
   29. "type": ["Text"]  // 关注的字段类型，Text则表示要做向量和倒排
   30. },
   31. {
   32. "columnName": "content",
   33. "type": ["Text"]
   34. },
   35. {
   36. "columnName": "image_text",
   37. "type": ["Text"]
   38. },
   39. {
   40. "columnName": "attachment_names",
   41. "type": ["Text"]
   42. },
   43. {
   44. "columnName": "inline_files",
   45. "type": ["Json"],
   46. "parser": [
   47. {
   48. "type": "File",
   49. "path": "$[*].uri"  // path字段的值为Json路径表达式
   50. }
   51. ]
   52. },
   53. {
   54. "columnName": "sender",
   55. "type": ["Scalar"],  // Scalar表示标量字段，不做加工，直接写到向量数据表中对应的列，用于标量检索过滤
   56. "description": "sender"
   57. },
   58. {
   59. "columnName": "receivers",
   60. "type": ["Scalar"],
   61. "description": "receivers"
   62. },
   63. {
   64. "columnName": "received_date",
   65. "type": ["Scalar"],
   66. "description": "received_date"
   67. }],
   68. "pipelineHandlers": {
   69. "FileParserHandler": ["SplitTextHandler"],  // 表示文件解析完成后交由文本切分处理器SplitTextHandler进行处理
   70. "SplitTextHandler": ["TextEmbeddingHandler"],
   71. "TextEmbeddingHandler": ["ImageEmbeddingHandler"],
   72. "ImageEmbeddingHandler": []
   73. }
   74. }],
   75. "knowledgeProcess": {
   76. "embeddingModelCfg":
   77. {
   78. "modelVersion": "default"  // 向量表征模型，"default" 表示默认版本
   79. },
   80. "chunkSplitter":
   81. {
   82. "chunkSize": 3072,
   83. "segmentSize": 300,
   84. "overlapRatio": 0.1
   85. },
   86. "perRecordLimit":
   87. {
   88. "parseFileMaxCnt": 10,
   89. "textEmbeddingMaxCnt": 50,
   90. "imageEmbeddingMaxCnt": 10
   91. }
   92. }
   93. }]
   94. }
   ```

   | 字段 | 是否可选 | 说明 |
   | --- | --- | --- |
   | version | 否 | schema的版本号，正整数，最大值为2147483647。 |
   | dbName | 否 | 数据库名称，最小长度为1，最大长度为120，支持数字、大小写字母、下划线和字符“.”。 |
   | tableName | 否 | 知识表名称，最小长度为1，最大长度为120，支持数字、大小写字母和下划线。 |
   | columnName | 否 | 知识字段列名，最小长度为1，最大长度为255。 |
   | referenceFields | 否 | 知识表主键，仅支持一个字段，且字段为整数类型，字段值最小长度为1，最大长度为255。 |
   | type | 否 | 知识字段类型，支持的知识字段类型，包括：  - Text：纯文本知识加工字段。  - Scalar：标量字段。  必须包含description字段，字段取值范围：[1，255]。  Scalar字段不会进行知识加工，内容与业务表对应字段保持一致。  Scalar字段的columnName允许长度范围：[1, 128]。  - Json：Json格式的知识加工字段。  必须包含parser字段，用于指定文件路径的解析器。  每个Json字段允许定义的parser数量范围是[1, 5]，最多支持提取5个不同的本地文件路径。  每个parser对象必填type和path，其中type为File，path的长度范围是[1，255]。  path必须是合法的Json路径表达式，用于表示知识加工需要解析的文件路径。  - Markdown: Markdown格式的知识加工字段。当前仅支持一个Markdown类型的知识字段，且Markdown字段不能同时设置为其它类型。**起始版本：** 6.1.0(23) |
   | processSequence | 是 | 加工顺序，用于定义数据的加工顺序，包含columnName和sortType两个字段。  - columnName对应一个数据源表的列名。  columnName值的长度范围是[1，255]，支持数字、大小写字母和下划线。  columnName对应的列必须是整数类型，且必须在数据源表里存在。  - sortType用于指定升序或降序排列。  sortType仅能配置为"ASC"（升序）或"DESC"（降序）。 |
   | customKeyword | 是 | 自定义关键字，用于配置关键字提取功能。配置该字段后知识加工会额外生成关键字表，表名相比数据源表增加"\_knowledge\_keyword"后缀，包含三个字段。  - wordTablePath对应关键词列表文件的路径，长度范围是[1, 255]，文件必须是.txt类型且实际存在。  - sourceFields用于指定关键词提取功能生效的列，长度范围[1, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  - extendFields用于指定关键字提取产物额外需要创建的列，长度范围[0, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  **起始版本：** 6.1.0(23) |
   | commonAttribute | 是 | 公共特征，当前仅支持配置时间特征，对应字段为"time"。配置该字段后知识加工会额外生成时间表，表名相比数据源表增加"\_knowledge\_time"后缀， 包含三个字段。  - baseTimeField对应基准时间列，长度范围是[1, 255]且该列实际存在。该列在数据源表中需要是合法的Unix毫秒级时间戳。  - sourceFields用于指定时间特征提取功能生效的列，长度范围[1, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  - extendFields用于指定时间特征提取产物额外需要创建的列，长度范围[0, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  **起始版本：** 6.1.0(23) |
   | pipelineHandlers | 否 | 执行顺序，用于定义知识加工时各处理模块（Handler）的执行顺序，可以控制原始数据如何被解析、切分、表征，最终写入倒排表与向量表。  可修改Handler流程，配置为一个映射（unordered\_map<string, vector<string>>），每个键为当前Handler，值为其后续执行的Handler列表，参考示例：  "pipelineHandlers":  {  "FileParserHandler": ["SplitTextHandler"],  "SplitTextHandler": ["TextEmbeddingHandler"],  "TextEmbeddingHandler": ["ImageEmbeddingHandler"],  "ImageEmbeddingHandler": []  }  当前Handler支持的名称包括：FileParserHandler、SplitTextHandler、TextEmbeddingHandler、ImageEmbeddingHandler。  Handler之间不能出现循环依赖，否则系统会在加载schema时报错。  每个Handler的下游可以为空数组，表示加工流程在此结束。  推荐的标准知识加工流程为：  FileParserHandler → SplitTextHandler → TextEmbeddingHandler → ImageEmbeddingHandler。  如果配置顺序错误（如跳过某些处理器、顺序不通或形成闭环），可能导致文件未处理、加工流程中断或初始化失败。  可根据实际场景适当简化，例如：仅加工倒排索引时只配置SplitTextHandler。  各Handler功能与依赖说明如下：  - FileParserHandler：提取Json字段中指向本地文件的文本内容，支持格式：doc、docx、ppt、pptx、xls、xlsx、html、txt、pdf、png、jpg、jpeg。文本类文件会提取正文内容，图片文件会通过OCR提取可识别文本。不依赖其他Handler。  推荐组合：建议放在SplitTextHandler之前，使提取出的文件内容能被切分、表征。  未配置影响：Json字段内文件不会被解析，倒排和向量中均无这些内容（不影响图片向量表征）。  - SplitTextHandler：对文本字段进行两级切分。  - 第一级chunk：用于倒排索引  - 第二级segment：用于向量表征（Embedding）    推荐组合：必须在TextEmbeddingHandler之前；否则向量表征阶段缺少segment，后续表征失败。  未配置影响：倒排表和向量表都无文本内容，检索无法返回文本相关内容。  - TextEmbeddingHandler：对SplitTextHandler产生的segment进行文本向量表征，生成供向量检索使用的数据。依赖SplitTextHandler的结果。  推荐组合：放在SplitTextHandler之后、ImageEmbeddingHandler 之前。  未配置影响：文本表征结果不会进入向量表，影响语义搜索。  - ImageEmbeddingHandler：根据Json字段解析后的图像路径加载图片，并对图像特征进行向量表征。图片处理不依赖SplitTextHandler和TextEmbeddingHandler，也不会参与文本倒排表，独立于文本处理流程。  推荐组合：放在TextEmbeddingHandler之后，避免图片路径字段被误当作文本参与表征，产生噪声。  未配置影响：图像表征结果不会进入向量表，影响图片相关搜索。 |
   | knowledgeProcess | 是 | 加工参数，用于设置知识加工参数配置，开发者可根据实际情况选择一个或多个字段进行配置。配置对应字段后，对应的子字段内部的内容均为必填，不允许部分配置。包括以下三个字段。  - embeddingModelCfg：表征模型设置。  若knowledgeProcess中配置了embeddingModelCfg字段，则必须包含modelVersion字段，类型为字符串，表示所使用的向量表征模型版本。  字段值最大长度为100，若为空字符串会使用默认版本。  该字段值需与实际部署或支持的模型版本匹配，且知识加工的表征模型版本需要和推理的版本一致，当前默认值为"default"。  - chunkSplitter：文本切分设置。  若knowledgeProcess字段中配置了chunkSplitter字段，则需同时配置以下三个子字段，均为必填项。  - chunkSize：每个Chunk的最大长度，整数类型，取值范围为[100, 5000]，默认值为3072。    - segmentSize：Chunk内部分段的最大长度，是向量表征的单位，整数类型，取值范围为[128, 512]，默认值为300。    - overlapRatio：相邻Chunk之间的重叠比例，浮点数类型，取值范围为(0.0, 0.3]，默认值为0.1。  这些参数用于控制文本切分策略，影响切分粒度、上下文连续性，如果未配置，则系统将使用上述默认值。  - perRecordLimit：文件预处理限制。  若knowledgeProcess中配置了perRecordLimit字段，则需同时配置以下三个字段，均为必填项。  - parseFileMaxCnt：每条记录最多允许解析的文件数，整数类型，取值范围为[0, 200]，默认值为10。    - textEmbeddingMaxCnt：每条记录最多进行向量表征的文本段数量，整数类型，取值范围为[0, 200]，默认值为50，超出限制的文本段不会被表征。    - imageEmbeddingMaxCnt：每条记录最多进行处理的图片数量，整数类型，取值范围为[0, 200]，默认值为10。  这些参数用于限制单条记录在知识加工过程中的最大处理规模，如果未配置，则系统将采用默认值。 |
2. 配置数据源库[开库参数](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)，根据业务需要预置数据。下文是示例代码片段，仅供参考，具体实现方式请根据业务需要调整。

   schema示例中inline\_files列配置的type为Json，且其path字段为指向uri的路径表达式，那么知识加工会去数据库中的inline\_files字段解析uri对应的值作为文件路径。插入数据的SQL语句inline\_files列的值应配置为示例代码中所示的文件路径的对象数组形式。加工时会根据获取的文件路径进行知识构建。

   注意

   * relationalStore开库参数配置中的name字段需要与中"dbName"字段保持一致，并且enableSemanticIndex字段需要设置为true才会触发知识加工。
   * 建表语句中的表名需要与中"tableName"字段保持一致，列名与"columnName"字段保持一致。

   ```
   1. import { relationalStore } from '@kit.ArkData';

   3. // relationalStore开库参数配置
   4. const storeConfig: relationalStore.StoreConfig = {
   5. name: 'testmail_store.db',  // 注意与步骤1中"dbName"字段保持一致
   6. securityLevel: relationalStore.SecurityLevel.S3,
   7. enableSemanticIndex: true,  // 注意该项设为true才会触发知识加工
   8. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
   9. };

   11. // 建表语句，注意表名应与步骤1中"tableName"字段保持一致，列名与"columnName"字段保持一致
   12. const createTableSql = "CREATE TABLE IF NOT EXISTS email(id integer primary key, subject text, " +
   13. "content text, image_text text, attachment_names text, inline_files text, sender text, " +
   14. "receivers text, received_date text);";

   16. // 插入数据语句，请按实际业务需要实现，下文仅作参考
   17. const sql = `insert or replace into email VALUES(0, 'Subject of an email', 'Content of an email', 'Convert image to text through OCR',
   18. 'attachment_name_1.txt, attachment_name_2.txt', '[{"uri":"/data/storage/el2/base/haps/entry/files/capture_1.png"},{"uri":"/data/storage/el2/base/haps/entry/files/capture_2.jpeg"}]',
   19. 'test1(test1@example.com)', 'test2(test2@example.com), test3(test3@example.com)', 'Convert time to timestamp');`;
   ```
3. 可根据业务需要，调用[getStatus()](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#getstatus)接口，查询当前的知识加工状态。

   ```
   1. import { relationalStore } from '@kit.ArkData';
   2. import { knowledgeProcessor } from '@kit.DataAugmentationKit';
   3. import { UIAbility, common } from '@kit.AbilityKit';

   5. // relationalStore开库参数配置
   6. const storeConfig: relationalStore.StoreConfig = {
   7. name: 'testmail_store.db',  // 注意与步骤1中"dbName"字段保持一致
   8. securityLevel: relationalStore.SecurityLevel.S3,
   9. enableSemanticIndex: true,
   10. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
   11. };

   13. let knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
   14. rdbSource: storeConfig,
   15. }
   16. let knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
   17. sourceConfig: knowledgeSourceConfig,
   18. }

   20. // 获取知识加工状态的异步函数，业务自行按需调用
   21. async function getStatus() {
   22. const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
   23. try {
   24. // 获取知识加工对象
   25. const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
   26. // 获取知识加工状态
   27. const status: knowledgeProcessor.ProcessorStatus = await processor.getStatus();
   28. return status;
   29. } catch (err) {
   30. console.error("Error: " + err.message + " code: " + err.code);
   31. return undefined;
   32. }
   33. }
   ```
4. 可根据业务需要，调用[startProcess](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#startprocess)(option: [KnowledgeProcessConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessconfig))接口，启动知识加工。

   ```
   1. import { relationalStore } from '@kit.ArkData';
   2. import { knowledgeProcessor } from '@kit.DataAugmentationKit';
   3. import { UIAbility, common } from '@kit.AbilityKit';

   5. // relationalStore开库参数配置
   6. const storeConfig: relationalStore.StoreConfig = {
   7. name: 'testmail_store.db',  // 注意与步骤1中"dbName"字段保持一致
   8. securityLevel: relationalStore.SecurityLevel.S3,
   9. enableSemanticIndex: true,
   10. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
   11. };

   13. let knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
   14. rdbSource: storeConfig,
   15. }
   16. let knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
   17. sourceConfig: knowledgeSourceConfig,
   18. }

   20. // 启动知识加工的异步函数，业务自行按需调用
   21. async function startProcess() {
   22. const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
   23. try {
   24. // 获取知识加工对象
   25. const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
   26. // 启动知识加工
   27. let processMode: knowledgeProcessor.KnowledgeProcessMode = knowledgeProcessor.KnowledgeProcessMode.INVERTED_INDEX;
   28. let config: knowledgeProcessor.KnowledgeProcessConfig = {
   29. mode: processMode,
   30. }
   31. await processor.startProcess(config);
   32. } catch (err) {
   33. console.error("Error: " + err.message + " code: " + err.code);
   34. }
   35. }
   ```
5. 可根据业务需要，调用[stopProcess](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#stopprocess)()接口，停止知识加工。

   ```
   1. import { relationalStore } from '@kit.ArkData';
   2. import { knowledgeProcessor } from '@kit.DataAugmentationKit';
   3. import { UIAbility, common } from '@kit.AbilityKit';

   5. // relationalStore开库参数配置
   6. const storeConfig: relationalStore.StoreConfig = {
   7. name: 'testmail_store.db',  // 注意与步骤1中"dbName"字段保持一致
   8. securityLevel: relationalStore.SecurityLevel.S3,
   9. enableSemanticIndex: true,
   10. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
   11. };

   13. let knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
   14. rdbSource: storeConfig,
   15. }
   16. let knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
   17. sourceConfig: knowledgeSourceConfig,
   18. }

   20. // 停止知识加工的异步函数，业务自行按需调用
   21. async function stopProcess() {
   22. const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
   23. try {
   24. // 获取知识加工对象
   25. const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
   26. // 停止知识加工
   27. await processor.stopProcess();
   28. } catch (err) {
   29. console.error("Error: " + err.message + " code: " + err.code);
   30. }
   31. }
   ```
6. 可根据业务需要，调用[cleanKnowledgeData](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#cleanknowledgedata)(context: [common.BaseContext](../harmonyos-references/js-apis-inner-application-basecontext.md), config: [KnowledgeProcessorConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig))接口，将知识库进行清理。注意：看约束和限制说明使用。

   ```
   1. import { relationalStore } from '@kit.ArkData';
   2. import { knowledgeProcessor } from '@kit.DataAugmentationKit';
   3. import { UIAbility, common } from '@kit.AbilityKit';

   5. // relationalStore开库参数配置
   6. const storeConfig: relationalStore.StoreConfig = {
   7. name: 'testmail_store.db',  // 注意与步骤1中"dbName"字段保持一致
   8. securityLevel: relationalStore.SecurityLevel.S3,
   9. enableSemanticIndex: true,
   10. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
   11. };

   13. let knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
   14. rdbSource: storeConfig,
   15. }
   16. let knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
   17. sourceConfig: knowledgeSourceConfig,
   18. }

   20. // 清理知识库的异步函数，业务自行按需调用
   21. async function cleanKnowledgeData() {
   22. const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
   23. try {
   24. // 清理知识库
   25. await knowledgeProcessor.cleanKnowledgeData(context, knowledgeProcessorConfig);
   26. } catch (err) {
   27. console.error("Error: " + err.message + " code: " + err.code);
   28. }
   29. }
   ```
