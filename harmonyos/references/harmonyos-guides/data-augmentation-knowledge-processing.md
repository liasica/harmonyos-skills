---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing
title: 知识加工
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > 知识加工
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7ecb8526436291968cf7bf1a841bb3bcc3ce296ecd9a43ae639494509229a140
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

从26.0.0版本开始，知识加工新增支持邮件智能分析能力。

1. 导入模块。

   ```typescript
   import { knowledgeProcessor } from '@kit.DataAugmentationKit';
   import { relationalStore } from '@kit.ArkData';
   import { UIContext } from '@kit.ArkUI';
   ```
2. 配置知识加工schema文件knowledge\_schema.json，下文是配置示例，实际文件内容请根据业务需要进行配置。知识加工产物命名规则如下：

   * 倒排库与数据源库是同一个数据库。
   * 倒排表名相较于数据源表名增加了"\_inverted"后缀（email->email\_inverted）。
   * 向量库名相较于数据源库名增加了"\_vector"后缀（testmail\_store.db->testmail\_store\_vector.db）。
   * 向量表名相较于数据源表名增加了"\_vector"后缀（email->email\_vector）。

   ```typescript
      // 文件路径：src/main/resources/rawfile/arkdata/knowledge/knowledge_schema.json
      // 项目中没有该目录请递归创建
      // 实际使用时请去除注释，示例中增加注释仅作字段说明用
      {
        "knowledgeSource": [{
          "version": 1,
          "dbName": "testmail_store.db",  // 存储原始数据的数据库文件名
          "tables": [{
            "tableName": "email",  // 用于知识加工的表名
            "referenceFields": ["id"],  // 知识数据源引用字段，用于关联知识库中的数据
            "processSequence": {  // 定义加工顺序为id倒序
              "columnName": "id",
              "sortType": "DESC"
            },
            "customKeyword": {
                "wordTablePath": "/data/storage/el2/base/haps/entry/files/keywords.txt", // 此处仅作示例，实际文件路径根据业务实际情况配置
                "sourceFields": ["subject", "content"],  // 关键字提取生效的列
                "extendFields": []  // 创建关键字表时额外增加的列，数据与源表一致
            },
            "commonAttribute": {
                "time": {
                    "baseTimeField": "received_date",
                    "sourceFields": ["subject", "content"],
                    "extendFields": ["sender"]
                }
            },
            "knowledgeFields": [{  // 关注的知识字段
              "columnName": "subject",  // 关注的字段名称
              "type": ["Text"]  // 关注的字段类型，Text则表示要做向量和倒排
            },
            {
              "columnName": "content",
              "type": ["Text"]
            },
            {
              "columnName": "image_text",
              "type": ["Text"]
            },
            {
              "columnName": "attachment_names",
              "type": ["Text"]
            },
            {
              "columnName": "inline_files",
              "type": ["Json"],
              "parser": [
                {
                  "type": "File",
                  "path": "$[*].uri"  // path字段的值为Json路径表达式
                }
              ]
            },
            {
              "columnName": "sender",
              "type": ["Scalar"],  // Scalar表示标量字段，不做加工，直接写到向量数据表中对应的列，用于标量检索过滤
              "description": "sender"
            },
            {
              "columnName": "receivers",
              "type": ["Scalar"],
              "description": "receivers"
            },
            {
              "columnName": "received_date",
              "type": ["Scalar"],
              "description": "received_date"
            }],
            "pipelineHandlers": {
              "FileParserHandler": ["SplitTextHandler"],  // 表示文件解析完成后交由文本切分处理器SplitTextHandler进行处理
              "SplitTextHandler": ["TextEmbeddingHandler"],
              "TextEmbeddingHandler": ["ImageEmbeddingHandler"],
              "ImageEmbeddingHandler": []
            }
          }],
          "knowledgeProcess": {
            "embeddingModelCfg":
            {
              "modelVersion": "default"  // 向量表征模型，"default" 表示默认版本
            },
            "chunkSplitter":
            {
              "chunkSize": 3072,
              "segmentSize": 300,
              "overlapRatio": 0.1
            },
            "perRecordLimit":
            {
              "parseFileMaxCnt": 10,
              "textEmbeddingMaxCnt": 50,
              "imageEmbeddingMaxCnt": 10
            }
          }
        }]
      }
   ```

   | 字段 | 是否可选 | 说明 |
   | --- | --- | --- |
   | version | 否 | schema的版本号，正整数，最大值为2147483647。 |
   | dbName | 否 | 数据库名称，最小长度为1，最大长度为120，支持数字、大小写字母、下划线和字符“.”。 |
   | tableName | 否 | 知识表名称，最小长度为1，最大长度为120，支持数字、大小写字母和下划线。 |
   | columnName | 否 | 知识字段列名，最小长度为1，最大长度为255。 |
   | referenceFields | 否 | 关联知识表主键，仅支持一个字段，字段本身最小长度为1，最大长度为255，关联的知识表主键是整数类型。 |
   | type | 否 | 知识字段类型，支持的知识字段类型，包括：  - Text：纯文本知识加工字段。  - Scalar：标量字段。  必须包含description字段，字段取值范围：[1，255]。  Scalar字段不会进行知识加工，内容与业务表对应字段保持一致。  Scalar字段的columnName允许长度范围：[1, 128]。  - Json：Json格式的知识加工字段。  必须包含parser字段，用于指定文件路径的解析器。  每个Json字段允许定义的parser数量范围是[1, 5]，最多支持提取5个不同的本地文件路径。  每个parser对象必填type和path，其中type为File，path的长度范围是[1，255]。  path必须是合法的Json路径表达式，用于表示知识加工需要解析的文件路径。  - Markdown: Markdown格式的知识加工字段。当前仅支持一个Markdown类型的知识字段，且Markdown字段不能同时设置为其它类型。**起始版本：** 6.1.0(23) |
   | processSequence | 是 | 加工顺序，用于定义数据的加工顺序，包含columnName和sortType两个字段。  - columnName对应一个数据源表的列名。  columnName值的长度范围是[1，255]，支持数字、大小写字母和下划线。  columnName对应的列必须是整数类型，且必须在数据源表里存在。  - sortType用于指定升序或降序排列。  sortType仅能配置为"ASC"（升序）或"DESC"（降序）。 |
   | customKeyword | 是 | 自定义关键字，用于配置关键字提取功能。配置该字段后知识加工会额外生成关键字表，表名相比数据源表增加"\_knowledge\_keyword"后缀，包含三个字段。  - wordTablePath对应关键词列表文件的路径，长度范围是[1, 255]，文件必须是.txt类型且实际存在。  - sourceFields用于指定关键词提取功能生效的列，长度范围[1, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  - extendFields用于指定关键字提取产物额外需要创建的列，长度范围[0, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  **起始版本：** 6.1.0(23) |
   | commonAttribute | 是 | 公共特征，当前仅支持配置时间特征，对应字段为"time"。配置该字段后知识加工会额外生成时间表，表名相比数据源表增加"\_knowledge\_time"后缀， 包含三个字段。  - baseTimeField对应基准时间列，长度范围是[1, 255]且该列实际存在。该列在数据源表中需要是合法的Unix毫秒级时间戳。  - sourceFields用于指定时间特征提取功能生效的列，长度范围[1, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  - extendFields用于指定时间特征提取产物额外需要创建的列，长度范围[0, 10]。其中每个列的长度范围是[1, 255]，且只能包含数字、大小写字母和下划线。  **起始版本：** 6.1.0(23) |
   | pipelineHandlers | 否 | 执行顺序，用于定义知识加工时各处理模块（Handler）的执行顺序，可以控制原始数据如何被解析、切分、表征，最终写入倒排表与向量表。  可修改Handler流程，配置为一个映射（unordered\_map<string, vector<string>>），每个键为当前Handler，值为其后续执行的Handler列表，参考示例：  "pipelineHandlers":  {  "FileParserHandler": ["SplitTextHandler"],  "SplitTextHandler": ["TextEmbeddingHandler"],  "TextEmbeddingHandler": ["ImageEmbeddingHandler"],  "ImageEmbeddingHandler": []  }  当前Handler支持的名称包括：FileParserHandler、SplitTextHandler、TextEmbeddingHandler、ImageEmbeddingHandler、MailSummaryHandler、MailTodoHandler、MailClassificationHandler。  Handler之间不能出现循环依赖，否则系统会在加载schema时报错。  每个Handler的下游可以为空数组，表示加工流程在此结束。  推荐的标准知识加工流程为：  FileParserHandler → SplitTextHandler → TextEmbeddingHandler → ImageEmbeddingHandler。  邮件智慧分析推荐的标准执行流程为：MailSummaryHandler->MailTodoHandler->MailClassificationHandler，可根据需要增删handler。  如果配置顺序错误（如跳过某些处理器、顺序不通或形成闭环），可能导致文件未处理、加工流程中断或初始化失败。  可根据实际场景适当简化，例如：仅加工倒排索引时只配置SplitTextHandler。  各Handler功能与依赖说明如下：  - FileParserHandler：提取Json字段中指向本地文件的文本内容，支持格式：doc、docx、ppt、pptx、xls、xlsx、html、txt、pdf、png、jpg、jpeg。文本类文件会提取正文内容，图片文件会通过OCR提取可识别文本。不依赖其他Handler。  推荐组合：建议放在SplitTextHandler之前，使提取出的文件内容能被切分、表征。  未配置影响：Json字段内文件不会被解析，倒排和向量中均无这些内容（不影响图片向量表征）。  - SplitTextHandler：对文本字段进行两级切分。  - 第一级chunk：用于倒排索引  - 第二级segment：用于向量表征（Embedding）    推荐组合：必须在TextEmbeddingHandler之前；否则向量表征阶段缺少segment，后续表征失败。  未配置影响：倒排表和向量表都无文本内容，检索无法返回文本相关内容。  - TextEmbeddingHandler：对SplitTextHandler产生的segment进行文本向量表征，生成供向量检索使用的数据。依赖SplitTextHandler的结果。  推荐组合：放在SplitTextHandler之后、ImageEmbeddingHandler 之前。  未配置影响：文本表征结果不会进入向量表，影响语义搜索。  - ImageEmbeddingHandler：根据Json字段解析后的图像路径加载图片，并对图像特征进行向量表征。图片处理不依赖SplitTextHandler和TextEmbeddingHandler，也不会参与文本倒排表，独立于文本处理流程。  推荐组合：放在TextEmbeddingHandler之后，避免图片路径字段被误当作文本参与表征，产生噪声。  未配置影响：图像表征结果不会进入向量表，影响图片相关搜索。  - MailSummaryHandler：通过大模型对邮件内容进行语义分析，生成邮件内容的摘要。  未配置影响：不执行邮件摘要功能。  - MailTodoHandler：通过大模型对邮件内容进行语义分析，识别邮件是否包含待办，并自动提取关键要素，将其转化为结构化的待办事项。  未配置影响：不执行邮件待办功能。  - MailClassificationHandler：通过大模型对邮件内容进行语义分析，对邮件进行多分类，分类的类别为以下类别之一：投诉、决策、审批、求助、待办、进展报告、其他，类别数量和种类均不支持自定义，但接口调用方可以自行选择在界面展示哪些类别。  推荐组合：MailClassificationHandler放在MailTodoHandler之后，利用待办提取信息辅助分类。  未配置影响：不执行邮件分类功能。 |
   | knowledgeProcess | 是 | 加工参数，用于设置知识加工参数配置，开发者可根据实际情况选择一个或多个字段进行配置。配置对应字段后，对应的子字段内部的内容均为必填，不允许部分配置。包括以下三个字段。  - embeddingModelCfg：表征模型设置。  若knowledgeProcess中配置了embeddingModelCfg字段，则必须包含modelVersion字段，类型为字符串，表示所使用的向量表征模型版本。  字段值最大长度为100，若为空字符串会使用默认版本。  该字段值需与实际部署或支持的模型版本匹配，且知识加工的表征模型版本需要和推理的版本一致，当前默认值为"default"。  - chunkSplitter：文本切分设置。  若knowledgeProcess字段中配置了chunkSplitter字段，则需同时配置以下三个子字段，均为必填项。  - chunkSize：每个Chunk的最大长度，整数类型，取值范围为[100, 5000]，默认值为3072。    - segmentSize：Chunk内部分段的最大长度，是向量表征的单位，整数类型，取值范围为[128, 512]，默认值为300。    - overlapRatio：相邻Chunk之间的重叠比例，浮点数类型，取值范围为(0.0, 0.3]，默认值为0.1。  这些参数用于控制文本切分策略，影响切分粒度、上下文连续性，如果未配置，则系统将使用上述默认值。  - perRecordLimit：文件预处理限制。  若knowledgeProcess中配置了perRecordLimit字段，则需同时配置以下三个字段，均为必填项。  - parseFileMaxCnt：每条记录最多允许解析的文件数，整数类型，取值范围为[0, 200]，默认值为10。    - textEmbeddingMaxCnt：每条记录最多进行向量表征的文本段数量，整数类型，取值范围为[0, 200]，默认值为50，超出限制的文本段不会被表征。    - imageEmbeddingMaxCnt：每条记录最多进行处理的图片数量，整数类型，取值范围为[0, 200]，默认值为10。  这些参数用于限制单条记录在知识加工过程中的最大处理规模，如果未配置，则系统将采用默认值。 |
   | mailAnalysisProcess | 是 | 邮件分析参数，用于设置邮件分析参数配置，配置对应字段后，对应的子字段内部的内容均为必填，不允许部分配置。  典型示例形如："mailAnalysisProcess": { "outputTableName": "mail\_ai\_insights", "inputFields": { "subject": "subject", "content": "content", "received\_date": "received\_date" }, "outputFields": { "summary": "summary", "todo": "todo", "classification": "classification" } }  **字段说明**  - outputTableName：邮件分析输出表的表名，字符串长度范围[1, 120]。  - inputFields：邮件分析输入表的被处理列名，应和knowledgeFields字段中的列名对应，当前包含：subject（邮件标题在邮件分析输入表中的列名）、content（邮件内容在邮件分析输入表中的列名）、received\_date（邮件接收时间在邮件分析输入表中的列名），字符串长度范围[1, 255]。  - outputFields：邮件分析输出表的列名，当前包含：summary（邮件分析生成的摘要在邮件分析输出表中的列名）、todo（邮件分析生成的待办在邮件分析输出表中的列名）、classification（邮件分析生成的分类在邮件分析输出表中的列名），字符串长度范围[1, 255]。  **邮件分析功能约束**  - 邮件分析不管邮件是否已读都会进行处理，已读邮件的分析结果是否展示由接口调用方来决定。  - 邮件分析只会基于单封邮件的标题、正文内容和邮件接收时间，不包含附件、图片、表格等内容。  - 如果正文小于45字节，邮件摘要会直接返回原文。  - 已取消邮件（已取消或者Cancel开头）跳过邮件待办提取，邮件分类直接设为"其他"类别。  - 对于存在回复/转发内容的邮件，只处理最新回复/转发的非空内容块，历史内容不处理。  **邮件分析结果示例**  - 邮件摘要：摘要文本，例如：本周三下午3点召开项目进度同步会议，汇报各模块开发进度，明确问题与方向，了解模块推进情况，组织风险讨论，明确责任人及时限，安排下周工作计划，优化资源配置，确保资金合理使用。  - 邮件待办：json字符串，例如{"todo\_list":[{"content":"参加本周三下午3点的项目进度同步会议","end\_time":"","start\_time":"2026-04-19 15:00:00"}]}，时间格式YYYY-MM-DD HH:MM:SS(24小时制)，无时间时start\_time或end\_time为空字符串。如未提取到待办，则分析结果为空字符串。可能会提取出不止一个待办，即todo\_list的元素数量超过1个。  - 邮件分类：分类结果必须是预定义类别的字符串之一：投诉、决策、审批、求助、待办、进展报告、其他。类别数量和种类均不支持自定义，但接口调用方可以自行选择在界面展示哪些类别。 |
3. 配置数据源库[开库参数](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)，根据业务需要预置数据。下文是示例代码片段，仅供参考，具体实现方式请根据业务需要调整。

   schema示例中inline\_files列配置的type为Json，且其path字段为指向uri的路径表达式，那么知识加工会去数据库中的inline\_files字段解析uri对应的值作为文件路径。插入数据的SQL语句inline\_files列的值应配置为示例代码中所示的文件路径的对象数组形式。加工时会根据获取的文件路径进行知识构建。

   **注意** 

   * relationalStore开库参数配置中的name字段需要与schema文件中"dbName"字段保持一致，并且enableSemanticIndex字段需要设置为true才会触发知识加工。
   * 建表语句中的表名需要与schema文件中"tableName"字段保持一致，列名与"columnName"字段保持一致。

   ```typescript
   let context = UIContext.getCallingScopeUIContext()?.getHostContext();

   // relationalStore开库参数配置
   let knowledgeConfig: relationalStore.StoreConfig = {
     name: 'test.db',// 已触发知识加工的数据库名
     securityLevel: relationalStore.SecurityLevel.S1,
     vector: false,
     tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
     enableSemanticIndex: true,
   };

   let sourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
     rdbSource: knowledgeConfig
   };

   let config: knowledgeProcessor.KnowledgeProcessorConfig = {
     sourceConfig: sourceConfig,
   };
   ```

   ```typescript
   let sourceDbStore: relationalStore.RdbStore;
   ```

   ```typescript
   async initDBData() {
     try {
       await relationalStore.getRdbStore(context, knowledgeConfig)
         .then((retriever:relationalStore.RdbStore) => {
           sourceDbStore = retriever;
         });
       let createSourceTable = 'CREATE TABLE IF NOT EXISTS mail (' +
         'id INTEGER PRIMARY KEY,' +
         'subject TEXT,' +
         'content TEXT' +
         ');';
       await sourceDbStore.executeSql(createSourceTable);
       let sqlInsert =
         'INSERT INTO mail (subject, content) VALUES ("运动直播场景", "content");';
       await sourceDbStore.execute(sqlInsert);
       console.info('InitModel success');
     } catch (err) {
       console.error('InitModel failed msg: ' + err.message + ' code: ' + err.code);
     }
   }
   ```
4. 可根据业务需要，调用[getStatus()](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#getstatus)接口，查询当前的知识加工状态。

   ```typescript
   async getStatus() {
     try {
       // 获取知识加工对象
       let processor = await knowledgeProcessor.getKnowledgeProcessor(context, config);
       console.info('GetStatus getKnowledgeProcessor success');
       if (processor) {
         await processor.getStatus();
         console.info('GetStatus success');
       }
     } catch (err) {
       console.error('GetStatus failed msg: ' + err.message + ' code: ' + err.code);
     }
   }
   ```
5. 可根据业务需要，调用[startProcess](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#startprocess)(option: [KnowledgeProcessConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessconfig))接口，启动知识加工。

   ```typescript
   async startProcess() {
     try {
       // 获取知识加工对象
       let processor = await knowledgeProcessor.getKnowledgeProcessor(context, config);
       console.info('StartProcess getKnowledgeProcessor success');
       // 启动知识加工
       let processMode: knowledgeProcessor.KnowledgeProcessMode = knowledgeProcessor.KnowledgeProcessMode.INVERTED_INDEX;
       let processconfig: knowledgeProcessor.KnowledgeProcessConfig = {
         mode: processMode,
       };
       if (processor) {
         await processor.startProcess(processconfig);
         console.info('StartProcess success');
       }
     } catch (err) {
       console.error('StartProcess failed msg: ' + err.message + ' code: ' + err.code);
     }
   }
   ```
6. 可根据业务需要，调用[stopProcess](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#stopprocess)()接口，停止知识加工。

   ```typescript
   async stopProcess() {
     try {
       // 获取知识加工对象
       let processor = await knowledgeProcessor.getKnowledgeProcessor(context, config);
       console.info('StopProcess getKnowledgeProcessor success');
       if (processor) {
         await processor.stopProcess();
         console.info('StopProcess success');
       }
     } catch (err) {
       console.error('StopProcess failed msg: ' + err.message + ' code: ' + err.code);
     }
   }
   ```
7. 可根据业务需要，调用[cleanKnowledgeData](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#cleanknowledgedata)(context: [common.BaseContext](../harmonyos-references/js-apis-inner-application-basecontext.md), config: [KnowledgeProcessorConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig))接口，将知识库进行清理。注意：看约束和限制说明使用。

   ```typescript
   async cleanKnowledgeData() {
     try {
       // 清理知识库
       await knowledgeProcessor.cleanKnowledgeData(context, config);
       console.info('CleanKnowledgeData success');
     } catch (err) {
       console.error('CleanKnowledgeData failed msg: ' + err.message + ' code: ' + err.code);
     }
   }
   ```
8. 邮件智慧分析handler支持通过调用[getStatus()](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#getstatus)接口查询当前知识加工状态。使用前需在[KnowledgeProcessorConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig)中完成以下配置：

   * llm配置：需提供具备chat函数的大语言模型实例，该函数的具体实现由调用方自定义（如使用[localChatModel](../harmonyos-references/dataaugmentation-localchatmodel-api.md)中的函数），可能需要先初始化大模型（加载大模型、初始化大模型状态等），并自行管理大模型的生命周期。
   * properties配置：根据业务需求设置相关参数，详见[KnowledgeProcessorConfig](../harmonyos-references/dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig)。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { relationalStore } from '@kit.ArkData';
   import { knowledgeProcessor } from '@kit.DataAugmentationKit';
   import { localChatModel } from '@kit.DataAugmentationKit'

   class MockLLMEngine implements knowledgeProcessor.ChatLLM {
     async chat(query: string): Promise<string> {
       console.info(`[LLM] Chat query: ${query}`);

       const questionInfo: localChatModel.QuestionInfo = {
         questionId: 1,
         content: query
       };
       const localConfig: localChatModel.Config = {
         isStream: false
       };

       return new Promise<string>((resolve) => {
         localChatModel.chat(questionInfo, localConfig, (err: BusinessError, ans: localChatModel.Answer) => {
           if (err) {
             console.error('[LLM] Chat failed:', err.message);
             resolve(""); // 即使失败也 resolve，避免调用者永远挂起
           } else {
             console.info(`[LLM] Chat done: ${ans.content}`);
             resolve(ans.content); // 把大模型返回的结果传出去
           }
         });
       });
     }
   }

   // 获取知识加工状态的异步函数，业务自行按需调用
   async function getStatus() {
     let context = getContext();
     // relationalStore开库参数配置
     const storeConfig: relationalStore.StoreConfig = {
       name: 'testmail_store.db',  // 注意与步骤1中"dbName"字段保持一致
       securityLevel: relationalStore.SecurityLevel.S1,
       enableSemanticIndex: true,
       tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
     };

     let knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
       rdbSource: storeConfig,
     };

     let myLLM = new MockLLMEngine();
     let knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
       sourceConfig: knowledgeSourceConfig,
       llm: myLLM,
       properties: "{\"userName\": \"John\", \"maxCtxLen\": 30000}",
     }
     try {
       // 获取知识加工对象
       const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
       // 获取知识加工状态
       const status: knowledgeProcessor.ProcessorStatus = await processor.getStatus();
       return status;
     } catch (err) {
       console.error("Error: " + err.message + " code: " + err.code);
       return undefined;
     }
   }
   ```
