---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataaugmentation-retrieval
title: 智慧化数据检索-ArkTS
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > 智慧化数据检索-ArkTS
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8276b36e0f94bf5fda97cbd3ee800babbe10e1c98a3a48bd89035c81c7deb85e
---

## 场景介绍

智慧化数据检索可用于文件整理，文件搜索等场景，例如：关键词检索、语义检索（文搜文）和跨模态检索（文搜图）。智慧化数据检索通过多路召回和重排两个阶段实现：

* 多路召回是指通过多种不同的策略或算法从海量数据中快速筛选出候选结果集。这些策略可针对不同的特征、模型或者数据来源，旨在尽可能覆盖各种潜在场景。ArkData提供了倒排和向量两路召回的能力，并支持灵活的条件过滤。
* 重排是针对多路召回得到的候选结果集进行二次筛选，通过简单规则或者更复杂的模型（如机器学习或深度学习模型）计算各个结果的相关性分数，并重新排列顺序。

## 倒排检索召回

倒排检索召回包含核心词选取和倒排召回子策略。

### 核心词选取

在接收到用户查询时，于构造倒排查询SQL语句之前，应先根据词权重、词性及词的相对位置筛选出查询中的核心词集合。重排过程中，核心词是否命中是评判结果相关性的重要指标。当前核心词选取逻辑如下：

1. 对分词结果从前到后遍历，累加词的权重，直到累加的词权重值超过总和词权重\*核心词系数，这部分累加的词为核心词。
2. 所有词性为“eng”（英文单词或字母）和“m”（数字）的分词全部视为核心词。

查询中的词权重和词性信息来源于高斯分词器的分词结果。

### 倒排召回子策略

为了保障召回结果的准确性，倒排召回使用SQLite FTS5倒排引擎能力，提供了3个倒排算子来进行相关结果匹配、打分。倒排算子如下：

* bm25算子：根据查询词在各字段中的命中情况，以bm25评分的加权和作为最终得分。
* 精确命中算子：如果文档字段中精确命中该查询语句，则给出其打分。
* 乱序窗口命中算子：如果文档字段中，在一定窗口范围内，出现所有用户查询词，则给出其打分。

此外，每个倒排算子还提供了匹配特征。最终的倒排召回得分是这三个策略加权后的结果。

## 向量检索召回

向量召回是通过将用户查询转化为向量（需使用嵌入模型进行向量化处理）来检索相似向量，从而实现语义相近内容的召回。向量近似的阈值在召回配置中设定。

## 反查

在多路召回完成后，部分结果仅由向量召回而未被倒排召回（或仅由倒排召回而未被向量召回）。这些差集在聚合多路召回结果时，缺乏其他路径提供的召回信息。由于重排模块要求每个召回结果包含所有路径的召回信息，因此需要对这些差集进行反查操作。

## 排序模块

排序模块包括对结果进行分档以及档内排序，使用的算法有RRF和分数融合排序。

### 对结果进行分档

以多路召回结果作为输入，基于各路召回的特征值或者召回分数，实现召回结果的相关性分档。档位共三个，分为高、中、低档位，供业务对最终检索结果相关性进行判断。

对于倒排召回，基于查询结果中被匹配字段对用户的查询词命中情况进行分档。

1. 高档位：存在匹配字段精确命中用户查询语句。
2. 中档位：命中大多数核心词。
3. 低档位：命中部分查询词。

“命中大多数核心词”是指当核心词数量小于等于3时，核心词全命中；当核心词数量大于3时，核心词命中N-1个，其中N为查询中被识别为核心词的总数。

对于向量召回，基于配置的一个或多个向量分数阈值对档位进行划分，当文档的向量分数大于等于某档位的阈值时，则划分至该档位。向量分数阈值是由1个或2个范围在[0,1]的数字组成。向量分数阈值有两个值时，分别表示高档位和中档位的阈值，向量分数小于中档位阈值则均为低档位；阈值有一个值时，该值表示高档位阈值，向量分数小于该值则均为低档位，无中档位。

对于同一个检索结果，倒排召回和向量召回的分档结果不一致时，以高档位结果优先。

### 档内排序算法：RRF算法

以多路召回结果作为输入，基于RRF算法实现多路召回结果的重排，并支持多路召回的每路进行权重配置。RRF算法通常会根据元素在各个召回策略中的排名来计算RRF得分。例如，对于一个元素在不同召回策略中的排名分别为 \_r\_1,\_r\_2,⋯,r\*\*n，其 RRF得分可以通过以下公式来计算。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/StbD9zy2Toe5TswmS3ax-w/zh-cn_image_0000002706834140.png)

其中\_k\_是一个常数，用于调整排名的影响程度。通过计算每个元素的RRF得分，将元素根据得分进行排序，得到结果列表。

### 档内排序算法：分数融合排序

以多路召回结果作为输入，并基于多路召回结果的召回分数计算排序分数来实现重排，同时支持对多路召回的每路进行权重配置。分数融合排序算法会根据配置的每路权重对每个元素在每路的得分进行加权平均，计算出一个最终得分，最后将元素根据得分进行排序，得到结果列表。

## 约束限制

* 当前只支持基于向量数据库、倒排数据库的召回。
* 查询词长度不超过512字符。

## 接口说明

以下是智慧数据多路召回和重排的相关接口。

| 接口名称 | 描述 |
| --- | --- |
| [retrieval.getRetriever](../harmonyos-references/dataaugmentation-retrieval-api.md#getretriever)(config: [RetrievalConfig](../harmonyos-references/dataaugmentation-retrieval-api.md#retrievalconfig)): Promise<[Retriever](../harmonyos-references/dataaugmentation-retrieval-api.md#retriever)> | 创建并获取检索器。 |
| [retrieveRdb](../harmonyos-references/dataaugmentation-retrieval-api.md#retrieverdb)(query: string, condition: [RetrievalCondition](../harmonyos-references/dataaugmentation-retrieval-api.md#retrievalcondition)): Promise<[RdbRecords](../harmonyos-references/dataaugmentation-retrieval-api.md#rdbrecords)> | 给定检索条件（包含query分词、召回条件、重排策略），检索召回满足条件的数据。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { retrieval } from '@kit.DataAugmentationKit';
   import { relationalStore } from '@kit.ArkData';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化倒排数据和向量数据。

   ```typescript
   let rdbStoreInvIdx: relationalStore.RdbStore;

   let rdbStoreVector: relationalStore.RdbStore;

   let storeConfigVector: relationalStore.StoreConfig = {
     name: 'vector_test.db',
     securityLevel: relationalStore.SecurityLevel.S3,
     vector: true,
   };

   let storeConfigInvIdx: relationalStore.StoreConfig = {
     name: 'files_test.db',
     securityLevel: relationalStore.SecurityLevel.S3,
     tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
   };
   ```

   ```typescript
   async initDBData() {
     let context: Context | undefined = this.getUIContext().getHostContext();
     if (context == undefined) {
       console.error('getHostContext failed.');
       return;
     }
     rdbStoreVector = await relationalStore.getRdbStore(context, storeConfigVector);
     if (rdbStoreVector != undefined) {
       let createSql = 'CREATE TABLE IF NOT EXISTS vector (fileid TEXT PRIMARY KEY, filename_text TEXT, filename FLOATVECTOR(128), keywords_text TEXT, keywords FLOATVECTOR(128), chapter FLOATVECTOR(128), abstract FLOATVECTOR(128), int64_value BIGINT, double_value DOUBLE, bool_value BOOLEAN, blob_value BLOB)';
       await rdbStoreVector.execute(createSql);
       this.insertVectorDB();

       let createSql2 = 'CREATE TABLE IF NOT EXISTS keyword_vector (KEYWORD TEXT PRIMARY KEY, EMBEDDING FLOATVECTOR(128))';
       await rdbStoreVector.execute(createSql2);
       this.insertVectorDB2();
     }
     rdbStoreInvIdx = await relationalStore.getRdbStore(context, storeConfigInvIdx);
     if (rdbStoreInvIdx != undefined) {
       let createSql = 'CREATE VIRTUAL TABLE IF NOT EXISTS files USING fts5(fileid, filename, keywords, chapter, abstract, content, tokenize = "customtokenizer")';
       await rdbStoreInvIdx.execute(createSql);
       this.insertInvIdxDB();
     }
     console.info('InitDBData success.');
   }
   ```

   ```typescript
   async insertVectorDB2() {
     let sqlInsertKeywordVector1:string =
       'INSERT INTO keyword_vector (keyword, embedding) VALUES ("运动直播场景", "[0.006954,-0.079041,0.046173,0.157959,-0.017212,0.037018,-0.072083,-0.028488,-0.099854,0.044037,-0.008911,-0.063049,0.035950,-0.105835,0.057739,0.060364,-0.062042,0.044159,0.143188,0.123901,-0.069641,-0.061920,-0.086731,-0.092468,0.092957,-0.027649,-0.005497,-0.039276,0.017502,-0.046570,-0.115906,0.081177,-0.153931,-0.040588,0.123474,-0.099060,0.062042,0.026352,-0.041382,-0.099548,0.071167,-0.120850,0.082642,0.026398,-0.035614,-0.008545,-0.076660,-0.031067,0.192017,-0.052582,0.005310,0.052734,0.199463,0.075195,-0.070740,-0.035950,0.073120,0.089172,0.075989,0.003582,0.050201,-0.012787,0.016647,-0.053619,0.001906,-0.060181,-0.068359,-0.114502,-0.045013,0.004547,-0.004673,-0.148071,0.126343,0.019394,-0.063110,-0.055908,0.071228,0.002369,0.041412,0.126709,-0.053467,0.127808,0.055420,0.206177,0.002169,-0.001452,0.095520,-0.042511,0.099243,-0.164185,0.093384,-0.014618,-0.129150,-0.238770,-0.085327,0.051300,-0.020004,0.010063,-0.084351,-0.003567,0.064941,-0.205322,-0.158936,-0.074768,0.104370,0.197021,-0.080688,-0.066772,-0.036346,0.034912,-0.019760,0.110474,0.128662,0.094727,0.024948,-0.033356,-0.081848,0.054474,-0.065857,-0.156494,0.002527,0.097595,-0.027420,0.039185,0.063965,0.220093,0.029556,-0.115417]");';
     await rdbStoreVector.execute(sqlInsertKeywordVector1);
     // ...
   }
   ```

   ```typescript
   async insertVectorDB() {
     let sqlInsertVector1:string =
       'INSERT INTO vector (fileid, filename_text, filename, keywords_text, keywords, chapter, abstract, int64_value, double_value, bool_value, blob_value) VALUES ("0", "运动直播场景", "[0.006954,-0.079041,0.046173,0.157959,-0.017212,0.037018,-0.072083,-0.028488,-0.099854,0.044037,-0.008911,-0.063049,0.035950,-0.105835,0.057739,0.060364,-0.062042,0.044159,0.143188,0.123901,-0.069641,-0.061920,-0.086731,-0.092468,0.092957,-0.027649,-0.005497,-0.039276,0.017502,-0.046570,-0.115906,0.081177,-0.153931,-0.040588,0.123474,-0.099060,0.062042,0.026352,-0.041382,-0.099548,0.071167,-0.120850,0.082642,0.026398,-0.035614,-0.008545,-0.076660,-0.031067,0.192017,-0.052582,0.005310,0.052734,0.199463,0.075195,-0.070740,-0.035950,0.073120,0.089172,0.075989,0.003582,0.050201,-0.012787,0.016647,-0.053619,0.001906,-0.060181,-0.068359,-0.114502,-0.045013,0.004547,-0.004673,-0.148071,0.126343,0.019394,-0.063110,-0.055908,0.071228,0.002369,0.041412,0.126709,-0.053467,0.127808,0.055420,0.206177,0.002169,-0.001452,0.095520,-0.042511,0.099243,-0.164185,0.093384,-0.014618,-0.129150,-0.238770,-0.085327,0.051300,-0.020004,0.010063,-0.084351,-0.003567,0.064941,-0.205322,-0.158936,-0.074768,0.104370,0.197021,-0.080688,-0.066772,-0.036346,0.034912,-0.019760,0.110474,0.128662,0.094727,0.024948,-0.033356,-0.081848,0.054474,-0.065857,-0.156494,0.002527,0.097595,-0.027420,0.039185,0.063965,0.220093,0.029556,-0.115417]", "运动,相机,直播,华为,外设", "[0.017029,0.008209,-0.037292,0.218262,0.066895,0.142944,-0.032501,-0.015961,-0.097229,-0.095398,-0.065186,-0.048401,0.000182,-0.118896,-0.036743,0.041534,-0.122742,0.118591,0.140869,0.009567,-0.059875,0.007156,-0.098999,-0.044861,0.000140,0.096985,-0.149658,0.002346,0.018112,0.052338,-0.046265,0.119690,-0.048737,0.001713,0.072937,-0.079346,-0.012535,0.032623,0.026627,0.034973,0.053528,-0.022110,0.026733,0.060089,-0.116516,-0.043518,-0.043488,-0.044159,0.157715,-0.030762,-0.019791,-0.052338,0.197876,-0.002966,-0.009422,-0.065125,0.061096,-0.001552,0.113220,-0.085083,0.112976,-0.037415,-0.020096,-0.104492,-0.078430,0.051971,-0.040314,0.006413,0.120361,-0.072876,-0.048584,-0.091797,0.079041,0.094971,0.072144,0.093323,-0.007469,-0.046417,0.023453,0.113220,-0.029449,0.015457,0.018341,0.076111,-0.041443,-0.023071,0.064941,-0.119324,0.003418,-0.183472,0.017746,0.037506,-0.092468,-0.247925,0.035217,0.042206,-0.043060,0.049866,-0.071533,0.055115,0.087463,-0.107849,-0.105774,-0.088013,0.138794,0.133667,-0.105591,0.080017,-0.291260,0.065918,-0.010307,0.137695,0.077942,0.031372,-0.031494,-0.066772,-0.184082,0.121826,0.027359,-0.025604,-0.125244,0.035828,0.082153,0.065979,0.053650,0.204834,0.141479,-0.093140]", "[0.038727,0.080627,0.012520,-0.097778,-0.079651,-0.080627,0.072510,0.233887,0.063354,0.089355,-0.100342,0.022797,0.071655,-0.029770,0.036591,0.004120,-0.107788,0.074402,0.158081,-0.136841,0.073792,0.012650,-0.062500,-0.005177,-0.011795,0.089233,0.091309,-0.053497,0.007099,-0.111084,-0.009789,0.107178,0.033752,-0.034943,-0.006947,-0.010880,-0.069763,-0.074768,0.031769,-0.041870,0.011497,-0.126343,0.004051,-0.104675,0.011032,-0.054047,0.055023,0.161987,-0.164551,0.123413,-0.059692,0.093262,-0.070251,-0.083435,0.007645,0.035187,0.016373,-0.101807,-0.049683,0.023773,-0.117249,0.076172,0.039886,0.032227,0.119385,-0.098328,-0.024857,0.098328,-0.148804,0.002064,-0.116150,-0.015526,0.060181,-0.213379,0.043121,-0.017761,-0.075012,-0.008507,-0.011986,0.002188,0.042938,0.152100,0.112793,0.095215,-0.020905,-0.202515,0.006176,-0.072998,0.022263,-0.116516,-0.092773,0.024002,0.086182,-0.016418,-0.125366,0.116821,-0.047943,0.076355,-0.056732,-0.284424,-0.076416,-0.120667,-0.178833,-0.066956,0.080627,0.037872,0.024857,0.038666,0.021423,-0.125854,-0.032867,0.062256,0.017380,0.040985,-0.127441,0.170898,-0.062408,-0.010910,-0.122925,0.041534,-0.036530,-0.108398,0.146973,0.110962,-0.067322,0.070740,0.013237,0.000191]", "[0.012939,-0.063782,0.031616,0.127441,-0.055023,0.004395,-0.048828,0.045105,-0.079712,-0.024704,0.035126,-0.028763,0.033447,-0.102478,0.095581,0.066284,-0.001293,0.021500,0.074463,0.107361,-0.078918,-0.048767,-0.079773,-0.009651,0.115417,-0.087463,-0.055420,-0.059265,-0.019897,-0.050842,-0.187256,0.060608,-0.195801,-0.069092,0.148193,-0.093994,0.113037,0.062378,-0.014488,-0.116638,0.049225,-0.089050,0.122498,-0.005947,0.012444,-0.003235,-0.075439,0.046814,0.160522,-0.087769,0.039917,-0.022247,0.178955,0.099670,-0.016327,-0.021088,0.061279,0.109436,0.073547,0.035980,0.016708,0.017685,-0.053894,-0.045624,-0.031647,-0.041107,-0.079407,-0.067383,-0.015472,-0.054199,-0.014114,-0.164185,0.099182,-0.027191,-0.021957,-0.014603,0.093750,-0.001885,0.074951,0.094238,-0.001523,0.099731,0.045288,0.104187,-0.105957,0.030701,0.108154,-0.116394,0.090820,-0.153809,0.016983,0.059662,-0.109070,-0.269043,-0.109253,0.053131,-0.002453,0.025360,-0.108093,-0.054871,0.079834,-0.245972,-0.136841,-0.063293,0.174927,0.122498,-0.104980,-0.130249,-0.051605,0.057556,-0.071106,0.078369,0.081848,0.039459,0.021927,-0.000520,-0.001396,0.064575,-0.087463,-0.095398,-0.015175,0.164062,-0.089600,-0.004246,0.054199,0.225464,0.050018,-0.049957]", 1234567890123456781, 3.1411, true, "12345678");';
     await rdbStoreVector.execute(sqlInsertVector1);
     // ...
   }
   ```

   ```typescript
   async insertInvIdxDB() {
     let sqlInsert1 : string =
       'INSERT INTO files (fileid, filename, keywords, chapter, abstract, content) VALUES ("0", "运动直播场景", "运动,相机,直播,华为,外设", "", "运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景运动直播场景", "dummy");';
     await rdbStoreInvIdx.execute(sqlInsert1);
     // ...
   }
   ```
3. 配置倒排、向量数据库相关的信息和上下文对象，并且生成检索器对象，用于后面的检索。

   ```typescript
   let globalRetriever:retrieval.Retriever | undefined;
   ```

   ```typescript
   async getRetriever() {
     let vectorDBConfig:retrieval.DbConfig = {
       name:'vector_test.db',
       securityLevel:relationalStore.SecurityLevel.S3
     }

     let invidxDBConfig:retrieval.DbConfig = {
       name:'files_test.db',
       securityLevel:relationalStore.SecurityLevel.S3
     }
     let context: Context | undefined = this.getUIContext().getHostContext();
     if (context == undefined) {
       console.info('getHostContext failed.');
       return;
     }
     let channelConfigVector:retrieval.ChannelConfig = {
       channelType:retrieval.ChannelType.VECTOR_DATABASE,
       context:context,
       dbConfig:vectorDBConfig
     }

     let channelConfigInvIdx:retrieval.ChannelConfig = {
       channelType:retrieval.ChannelType.INVERTED_INDEX_DATABASE,
       context:context,
       dbConfig:invidxDBConfig
     }

     let retrievalConfig:retrieval.RetrievalConfig = {
       channelConfigs:[channelConfigInvIdx, channelConfigVector]
     }

     await retrieval.getRetriever(retrievalConfig)
       .then((retriever:retrieval.Retriever) => {
         globalRetriever = retriever;
         console.info('GetRetriever success');
       })
       .catch((err:BusinessError) => {
         globalRetriever = undefined;
         console.error('Failure in getRetriever and code is ' + err.code);
       })
   }
   ```
4. 执行检索：使用前一步获取到的检索器，配合检索条件进行检索。

   ```typescript
   let fieldWeight:Record<string, number> = {
     'filename':4.0
   }

   let fieldSlops:Record<string, number> = {
     'filename':5
   }

   let bm25Strategy:retrieval.Bm25Strategy = {
     bm25Weight:1.5,
     columnWeight:fieldWeight
   }

   let exactStrategy:retrieval.ExactMatchingStrategy = {
     exactMatchingWeight:1.2,
     columnWeight:fieldWeight
   }

   let outOfOrderStrategy:retrieval.ProximityStrategy = {
     proximityWeight:1.0,
     columnWeight:fieldWeight,
     columnSlops:fieldSlops
   }

   let invertedIndexStrategies:Array<retrieval.InvertedIndexStrategy> = [bm25Strategy, exactStrategy, outOfOrderStrategy]

   let recallConditionInvIdx:retrieval.InvertedIndexRecallCondition ={
     ftsTableName:'files',
     primaryKey:['fileid'],
     fromClause:'files',
     responseColumns:['fileid', 'filename', 'keywords'],
     deepSize:2,
     invertedIndexStrategies:invertedIndexStrategies,
     recallName:'invIdxRecall'
   }

   // 这里 floatArray 时输入的 query 的表征向量，根据实际情况需要修改
   let floatArray = new Float32Array([0.006954, -0.079041, 0.046173, 0.157959, -0.017212, 0.037018, -0.072083, -0.028488, -0.099854, 0.044037, -0.008911, -0.063049, 0.035950, -0.105835, 0.057739, 0.060364, -0.062042, 0.044159, 0.143188, 0.123901, -0.069641, -0.061920, -0.086731, -0.092468, 0.092957, -0.027649, -0.005497, -0.039276, 0.017502, -0.046570, -0.115906, 0.081177, -0.153931, -0.040588, 0.123474, -0.099060, 0.062042, 0.026352, -0.041382, -0.099548, 0.071167, -0.120850, 0.082642, 0.026398, -0.035614, -0.008545, -0.076660, -0.031067, 0.192017, -0.052582, 0.005310, 0.052734, 0.199463, 0.075195, -0.070740, -0.035950, 0.073120, 0.089172, 0.075989, 0.003582, 0.050201, -0.012787, 0.016647, -0.053619, 0.001906, -0.060181, -0.068359, -0.114502, -0.045013, 0.004547, -0.004673, -0.148071, 0.126343, 0.019394, -0.063110, -0.055908, 0.071228, 0.002369, 0.041412, 0.126709, -0.053467, 0.127808, 0.055420, 0.206177, 0.002169, -0.001452, 0.095520, -0.042511, 0.099243, -0.164185, 0.093384, -0.014618, -0.129150, -0.238770, -0.085327, 0.051300, -0.020004, 0.010063, -0.084351, -0.003567, 0.064941, -0.205322, -0.158936, -0.074768, 0.104370, 0.197021, -0.080688, -0.066772, -0.036346, 0.034912, -0.019760, 0.110474, 0.128662, 0.094727, 0.024948, -0.033356, -0.081848, 0.054474, -0.065857, -0.156494, 0.002527, 0.097595, -0.027420, 0.039185, 0.063965, 0.220093, 0.029556, -0.115417]);

   let vectorQuery:retrieval.VectorQuery = {
     column:'keywords',
     value:floatArray,
     similarityThreshold:0.35
   }

   let recallConditionVector:retrieval.VectorRecallCondition = {
     vectorQuery:vectorQuery,
     fromClause:'vector',
     primaryKey:['fileid'],
     responseColumns:['filename_text', 'filename', 'int64_value', 'double_value', 'bool_value', 'blob_value'],
     recallName:'vectorRecall',
     deepSize:2
   }

   let vectorWeights:Record<string, number> = {
     'vectorRecall':0.5
   }

   let invidxWeights:Record<string, number> = {
     'vectorRecall':0.5
   }

   let vectorRerankParameter:retrieval.VectorRerankParameter = {
     vectorWeights:vectorWeights,
     thresholds:[0.55, 0.45]
   }
   let invidxRerankParameter:retrieval.InvertedIndexRerankParameter = {
     invertedIndexWeights:invidxWeights,
   }

   let parameters:Record<retrieval.ChannelType, retrieval.RerankParameter> = {
     0:vectorRerankParameter,
     1:invidxRerankParameter
   }

   let rerankMethod:retrieval.RerankMethod = {
     rerankType:retrieval.RerankType.RRF,
     parameters:parameters,
     isSoftmaxNormalized:true
   }

   let groundTruthIds: Array<string> = ['1','2', '3'];
   let explain : retrieval.ExplanationConfig ={
     groundTruths: groundTruthIds
   }

   let retrievalCondition:retrieval.RetrievalCondition = {
     rerankMethod:rerankMethod,
     recallConditions:[recallConditionInvIdx, recallConditionVector],
     resultCount:2,
     explanation:explain
   }
   ```

   ```typescript
   async retrieveRdb() {
     if (globalRetriever != undefined) {
       let query:string = '运动直播场景';
       // 执行检索
       globalRetriever.retrieveRdb(query, retrievalCondition)
         .then((rdbdata:retrieval.RdbRecords) => {

           // ...
           console.info('RetrieveRdb success.');
         })
         .catch((err:BusinessError) => {
           console.error('Failure in retrieveRdb and code is ' + err.code);
         })
     }
   }
   ```
