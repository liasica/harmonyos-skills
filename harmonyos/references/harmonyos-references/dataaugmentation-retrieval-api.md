---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-retrieval-api
title: retrieval（智慧化数据平台）
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > ArkTS API > retrieval（智慧化数据平台）
category: harmonyos-references
scraped_at: 2026-04-29T13:56:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:55cb478770f0265c5e26a63e5b71b1711f9a1d0118dac61a8f8bb313834a36ec
---

智慧数据平台（ArkData Intelligence Platform，AIP）提供端侧的数据智慧化能力，实现数据和AI智能在端侧闭环。作为端侧智慧化能力底座，将支持以下能力：

* 多模态嵌入模型：使用嵌入模型（Embedding Model）对多模态数据生成向量表征，将文本、图片等数据映射到同一向量空间，支撑基于语义的多模态知识检索。
* 多模态数据存储：支持端侧向量、倒排索引等多模态数据存储，避免将原始数据发送到服务器进行处理，减少了数据泄露的风险。
* 知识检索：逐步构建语义索引、知识图谱、召回、重排等功能，支持用户知识的语义化检索。
* 知识生成与整理：基于用户文档、消息、电子邮件、照片、视频、日历事件、屏幕上下文等数据，支持高效数据整理与知识生成，实现数据到知识的转换。

  **起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { retrieval } from '@kit.DataAugmentationKit';
```

## getRetriever

PhonePC/2in1Tablet

getRetriever(config: RetrievalConfig): Promise<Retriever>

获取检索器，进行多路检索召回。使用promise异步回调。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [RetrievalConfig](dataaugmentation-retrieval-api.md#retrievalconfig) | 是 | 检索器的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Retriever](dataaugmentation-retrieval-api.md#retriever)> | Promise对象，返回检索器对象。 |

**示例：**

```
1. import { retrieval } from '@kit.DataAugmentationKit';
2. import { relationalStore } from '@kit.ArkData';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Page {
8. async retrieve() {
9. let vectorDBConfig:retrieval.DbConfig = {
10. name:"vector_store_test.db",
11. securityLevel:relationalStore.SecurityLevel.S3
12. }

14. let invidxDBConfig:retrieval.DbConfig = {
15. name:"invidx_store_test.db",
16. securityLevel:relationalStore.SecurityLevel.S3
17. }
18. let context: Context | undefined = this.getUIContext().getHostContext();
19. if (context == undefined) {
20. console.info("getHostContext failed.");
21. return;
22. }
23. let channelConfigVector:retrieval.ChannelConfig = {
24. channelType:retrieval.ChannelType.VECTOR_DATABASE,
25. context:context,
26. dbConfig:vectorDBConfig
27. }

29. let channelConfigInvIdx:retrieval.ChannelConfig = {
30. channelType:retrieval.ChannelType.INVERTED_INDEX_DATABASE,
31. context:context,
32. dbConfig:invidxDBConfig
33. }

35. let retrievalConfig:retrieval.RetrievalConfig = {
36. channelConfigs:[channelConfigInvIdx, channelConfigVector]
37. }

39. let globalRetriever:retrieval.Retriever | undefined;
40. // 获取检索器
41. await retrieval.getRetriever(retrievalConfig)
42. .then((retriever:retrieval.Retriever) => {
43. globalRetriever = retriever;
44. console.info("globalRetriever is success");
45. })
46. .catch((err:BusinessError) => {
47. globalRetriever = undefined;
48. console.error("Failed to get Retriever and code is " + err.code);
49. })
50. }

52. build() {
53. Column() {
54. Text('test')
55. }
56. }
57. }
```

## RetrievalConfig

PhonePC/2in1Tablet

管理召回的配置

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelConfigs | Array<[ChannelConfig](dataaugmentation-retrieval-api.md#channelconfig)> | 是 | 不同检索回路的配置信息数组。 |

## ChannelConfig

PhonePC/2in1Tablet

管理每个检索回路的配置信息。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| channelType | [ChannelType](dataaugmentation-retrieval-api.md#channeltype) | 否 | 否 | 当前检索回路的数据库类型。 |
| context | [common.BaseContext](js-apis-inner-application-basecontext.md) | 否 | 否 | 应用的上下文。  FA模型的应用Context定义。  Stage模型的应用Context定义。 |
| dbConfig | [DbConfig](dataaugmentation-retrieval-api.md#dbconfig) | 否 | 否 | 当前检索回路的数据库配置。 |

## ChannelType

PhonePC/2in1Tablet

数据库类型枚举。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VECTOR\_DATABASE | 0 | 向量数据库。 |
| INVERTED\_INDEX\_DATABASE | 1 | 倒排数据库。 |

## DbConfig

PhonePC/2in1Tablet

type DbConfig = relationalStore.StoreConfig

数据库配置。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| [relationalStore.StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig) | 数据库配置。 |

## Retriever

PhonePC/2in1Tablet

检索器，用于多路检索召回。

下列接口都需先使用[retrieval.getRetriever](dataaugmentation-retrieval-api.md#getretriever)获取到检索器实例，再通过此实例调用对应接口。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

### retrieveRdb

PhonePC/2in1Tablet

retrieveRdb(query: string, condition: RetrievalCondition): Promise<RdbRecords>

给定检索条件（包含查询词分词、召回条件），从一个关系型数据库检索召回满足条件的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 当前检索的查询词,长度上限为1000字节。 |
| condition | [RetrievalCondition](dataaugmentation-retrieval-api.md#retrievalcondition) | 是 | 检索条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RdbRecords](dataaugmentation-retrieval-api.md#rdbrecords)> | Promise对象，返回检索召回数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021200001](dataaugmentation-error-code.md#section1021200001-数据库文件损坏) | The database is corrupted. |
| [1021200002](dataaugmentation-error-code.md#section1021200002-数据库或事务关闭) | The database is closed. |
| [1021200003](dataaugmentation-error-code.md#section1021200003-数据库busy) | The database is busy. |
| [1021200004](dataaugmentation-error-code.md#section1021200004-数据库内存不足) | The database is out of memory. |
| [1021200100](dataaugmentation-error-code.md#section1021200100-sqlite-通用错误) | SQLite: Generic error. |
| [1021200101](dataaugmentation-error-code.md#section1021200101-sqlite访问权限被拒绝) | SQLite: Access permission denied. |
| [1021200102](dataaugmentation-error-code.md#section1021200102-sqlite数据库文件已锁定) | SQLite: The database file is locked. |
| [1021200103](dataaugmentation-error-code.md#section1021200103-sqlite发生了某种磁盘io错误) | SQLite: Some kind of disk I/O error occurred. |
| [1021200104](dataaugmentation-error-code.md#section1021200104-wal文件大小超过默认上限) | SQLite: The WAL file size exceeds the default limit. |
| [1021200105](dataaugmentation-error-code.md#section1021200105-无法打开数据库文件) | SQLite: Unable to open the database file. |
| [1021201000](dataaugmentation-error-code.md#section1021201000-retrieval-recall-error) | Retrieval: An error occurred during the reacall phase. |
| [1021201001](dataaugmentation-error-code.md#section1021201001-retrieval-re-ranking-error) | Retrieval: An error occurred during the re-ranking phase. |
| [1021201002](dataaugmentation-error-code.md#section1021201002-retrieval-numerical-parameter-out-of-range) | Retrieval: The value of the numerical parameter is outside the constrained range. |
| [1021201003](dataaugmentation-error-code.md#section1021201003-retrieval-invalid-primary-keys) | Retrieval: There are invalid primary keys. |
| [1021201004](dataaugmentation-error-code.md#section1021201004-retrieval-unsupport-composite-primary-key-in-re-ranking) | Retrieval: A re-ranking algorithm that does not support composite primary keys was used. |
| [1021201005](dataaugmentation-error-code.md#section1021201005-retrieval-empty-string-field) | Retrieval: There are fields with empty strings. |
| [1021201006](dataaugmentation-error-code.md#section1021201006-retrieval-illegal-filter-input) | Retrieval: The filter input is invalid. |
| [1021201007](dataaugmentation-error-code.md#section1021201007-retrieval-invalid-recall-field-name) | Retrieval: There are invalid recall names in RecallCondition. |
| [1021201008](dataaugmentation-error-code.md#section1021201008-retrieval-vector-similarity-threshold-too-high) | Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter. |
| [1021201009](dataaugmentation-error-code.md#section1021201009-retrieval-rerankmethod-parameters-do-not-match-the-channel-type) | Retrieval: RerankMethod parameters do not match the channel type. |
| [1021201010](dataaugmentation-error-code.md#section1021201010-retrieval-empty-parameter-value) | Retrieval: There exists a parameter value that should not be empty but is actually empty |
| [1021200012](dataaugmentation-error-code.md#section1021200012-unable-to-generate-embeddings) | Unable to generate embeddings. |

**示例：**

```
1. import { retrieval } from '@kit.DataAugmentationKit';
2. import { relationalStore } from '@kit.ArkData';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Page {

9. async retrieve() {
10. let vectorDBConfig:retrieval.DbConfig = {
11. name:"vector_test.db",
12. securityLevel:relationalStore.SecurityLevel.S3
13. }

15. let invidxDBConfig:retrieval.DbConfig = {
16. name:"files_test.db",
17. securityLevel:relationalStore.SecurityLevel.S3
18. }
19. let context: Context | undefined = this.getUIContext().getHostContext();
20. if (context == undefined) {
21. console.info("getHostContext failed.");
22. return;
23. }
24. let channelConfigVector:retrieval.ChannelConfig = {
25. channelType:retrieval.ChannelType.VECTOR_DATABASE,
26. context:context,
27. dbConfig:vectorDBConfig
28. }

30. let channelConfigInvIdx:retrieval.ChannelConfig = {
31. channelType:retrieval.ChannelType.INVERTED_INDEX_DATABASE,
32. context:context,
33. dbConfig:invidxDBConfig
34. }

36. let retrievalConfig:retrieval.RetrievalConfig = {
37. channelConfigs:[channelConfigInvIdx, channelConfigVector]
38. }

40. let globalRetriever:retrieval.Retriever | undefined;
41. await retrieval.getRetriever(retrievalConfig)
42. .then((retriever:retrieval.Retriever) => {
43. globalRetriever = retriever;
44. console.info("globalRetriever is success");
45. })
46. .catch((err:BusinessError) => {
47. globalRetriever = undefined;
48. console.error("Failed to get Retriever and code is " + err.code);
49. })

51. let fieldWeight:Record<string, number> = {
52. "filename":4.0
53. }

55. let fieldSlops:Record<string, number> = {
56. "filename":5
57. }

59. let bm25Strategy:retrieval.Bm25Strategy = {
60. bm25Weight:1.5,
61. columnWeight:fieldWeight
62. }

64. let exactStrategy:retrieval.ExactMatchingStrategy = {
65. exactMatchingWeight:1.2,
66. columnWeight:fieldWeight
67. }

69. let outOfOrderStrategy:retrieval.ProximityStrategy = {
70. proximityWeight:1.0,
71. columnWeight:fieldWeight,
72. columnSlops:fieldSlops
73. }

75. let invertedIndexStrategies:Array<retrieval.InvertedIndexStrategy> = [bm25Strategy, exactStrategy, outOfOrderStrategy]

77. let recallConditionInvIdx:retrieval.InvertedIndexRecallCondition ={
78. ftsTableName:"files",
79. primaryKey:["fileid"],
80. fromClause:"files",
81. responseColumns:["fileid", "filename", "keywords"],
82. deepSize:2,
83. invertedIndexStrategies:invertedIndexStrategies,
84. recallName:"invIdxRecall"
85. }

87. // 这里 floatArray 时输入的 query 的表征向量，根据实际情况需要修改
88. let floatArray = new Float32Array([0.006954, -0.079041, 0.046173, 0.157959, -0.017212, 0.037018, -0.072083, -0.028488, -0.099854, 0.044037, -0.008911, -0.063049, 0.035950, -0.105835, 0.057739, 0.060364, -0.062042, 0.044159, 0.143188, 0.123901, -0.069641, -0.061920, -0.086731, -0.092468, 0.092957, -0.027649, -0.005497, -0.039276, 0.017502, -0.046570, -0.115906, 0.081177, -0.153931, -0.040588, 0.123474, -0.099060, 0.062042, 0.026352, -0.041382, -0.099548, 0.071167, -0.120850, 0.082642, 0.026398, -0.035614, -0.008545, -0.076660, -0.031067, 0.192017, -0.052582, 0.005310, 0.052734, 0.199463, 0.075195, -0.070740, -0.035950, 0.073120, 0.089172, 0.075989, 0.003582, 0.050201, -0.012787, 0.016647, -0.053619, 0.001906, -0.060181, -0.068359, -0.114502, -0.045013, 0.004547, -0.004673, -0.148071, 0.126343, 0.019394, -0.063110, -0.055908, 0.071228, 0.002369, 0.041412, 0.126709, -0.053467, 0.127808, 0.055420, 0.206177, 0.002169, -0.001452, 0.095520, -0.042511, 0.099243, -0.164185, 0.093384, -0.014618, -0.129150, -0.238770, -0.085327, 0.051300, -0.020004, 0.010063, -0.084351, -0.003567, 0.064941, -0.205322, -0.158936, -0.074768, 0.104370, 0.197021, -0.080688, -0.066772, -0.036346, 0.034912, -0.019760, 0.110474, 0.128662, 0.094727, 0.024948, -0.033356, -0.081848, 0.054474, -0.065857, -0.156494, 0.002527, 0.097595, -0.027420, 0.039185, 0.063965, 0.220093, 0.029556, -0.115417]);

90. let vectorQuery:retrieval.VectorQuery = {
91. column:"keywords",
92. value:floatArray,
93. similarityThreshold:0.35
94. }

96. let recallConditionVector:retrieval.VectorRecallCondition = {
97. vectorQuery:vectorQuery,
98. fromClause:"vector",
99. primaryKey:["fileid"],
100. responseColumns:["filename_text", "filename", "int64_value", "double_value", "bool_value", "blob_value"],
101. recallName:"vectorRecall",
102. deepSize:2
103. }

105. let vectorWeights:Record<string, number> = {
106. "vectorRecall":0.5
107. }

109. let invidxWeights:Record<string, number> = {
110. "vectorRecall":0.5
111. }

113. let vectorRerankParameter:retrieval.VectorRerankParameter = {
114. vectorWeights:vectorWeights,
115. thresholds:[0.55, 0.45]
116. }

118. let invidxRerankParameter:retrieval.InvertedIndexRerankParameter = {
119. invertedIndexWeights:invidxWeights,
120. }

122. let parameters:Record<retrieval.ChannelType, retrieval.RerankParameter> = {
123. 0:vectorRerankParameter,
124. 1:invidxRerankParameter
125. }

127. let rerankMethod:retrieval.RerankMethod = {
128. rerankType:retrieval.RerankType.RRF,
129. parameters:parameters,
130. isSoftmaxNormalized:true
131. }

133. let groundTruthIds: Array<string> = ['1','2', '3'];
134. let explain : retrieval.ExplanationConfig ={
135. groundTruths: groundTruthIds
136. }

138. let retrievalCondition:retrieval.RetrievalCondition = {
139. rerankMethod:rerankMethod,
140. recallConditions:[recallConditionInvIdx, recallConditionVector],
141. resultCount:2,
142. explanation:explain
143. }

146. if (globalRetriever != undefined) {
147. let query:string = "运动直播场景";
148. // 执行检索
149. globalRetriever.retrieveRdb(query, retrievalCondition)
150. .then((rdbdata:retrieval.RdbRecords) => {

152. console.info(`#########  retrieval result ############`);
153. for (let i = 0; i < rdbdata.records.length; i++) {
154. console.info(` primaryKey is ${rdbdata.records[i].primaryKey}`);
155. Object.keys(rdbdata.records[i].columns).forEach((key) => {
156. if (rdbdata.records && rdbdata.records[i]) {
157. let value = rdbdata.records[i].columns[key];
158. console.info(`recall Scores Key: ${key}, Value: ${value}`);
159. }
160. });
161. console.info(`score is ${rdbdata.records[i].score}`);

163. Object.keys(rdbdata.records[i].recallScores).forEach((channelType) => {
164. if (rdbdata.records) {
165. let scores:Record<string, retrieval.RecallScore>  = rdbdata.records[i].recallScores[channelType];
166. Object.keys(scores).forEach((key)=>{
167. let value = scores[key];
168. console.info(`recall Scores channelType is ${channelType}, Key: ${key}, score: ${value.score}`);
169. });
170. }
171. });
172. console.info("recall Scores", rdbdata.records[i].recallScores.toString());
173. Object.keys(rdbdata.records[i].features).forEach((key) => {
174. if (rdbdata.records && rdbdata.records[i]) {
175. let value = rdbdata.records[i].features[key];
176. console.info(`features Key: ${key}, Value: ${value}`);
177. }
178. });
179. console.info(`similarityLevel is ${rdbdata.records[i].similarityLevel}`);

181. }

183. console.info(`#########  missdGroundTruthsPrimaryKey ############`);
184. if(rdbdata.missedGroundTruths != undefined && rdbdata.missedGroundTruths.length != 0){
185. for (let i = 0; i < rdbdata.missedGroundTruths.length; i++) {
186. console.info(`missdGroundTruthsPrimaryKey is ${rdbdata.missedGroundTruths[i].primaryKey}`);
187. Object.keys(rdbdata.missedGroundTruths[i].columns).forEach((key) => {
188. if (rdbdata.missedGroundTruths && rdbdata.missedGroundTruths[i]) {
189. let value = rdbdata.missedGroundTruths[i].columns[key];
190. console.info(`missdGroundTruths recall Scores Key: ${key}, Value: ${value}`);
191. }
192. });
193. console.info(` missdGroundTruths score is ${rdbdata.missedGroundTruths[i].score}`);

195. Object.keys(rdbdata.missedGroundTruths[i].recallScores).forEach((channelType) => {
196. if (rdbdata.missedGroundTruths) {
197. let scores:Record<string, retrieval.RecallScore>  = rdbdata.missedGroundTruths[i].recallScores[channelType];
198. Object.keys(scores).forEach((key)=>{
199. let value = scores[key];
200. console.info(`missdGroundTruths recall Scores channelType is ${channelType}, Key: ${key}, score: ${value.score}`);
201. });
202. }
203. });
204. console.info("missdGroundTruths recall Scores", rdbdata.missedGroundTruths[i].recallScores.toString());
205. Object.keys(rdbdata.missedGroundTruths[i].features).forEach((key) => {
206. if (rdbdata.missedGroundTruths && rdbdata.missedGroundTruths[i]) {
207. let value = rdbdata.missedGroundTruths[i].features[key];
208. console.info(`missdGroundTruths features Key: ${key}, Value: ${value}`);
209. }
210. });
211. console.info(`missdGroundTruths similarityLevel is ${rdbdata.missedGroundTruths[i].similarityLevel}`);
212. }
213. }
214. console.info("retrieval success.");
215. })
216. .catch((err:BusinessError) => {
217. console.error("Failure in retrieveRdb and code is " + err.code);
218. })
219. }
220. }

222. build() {
223. Column() {
224. Text('test')
225. }
226. }
227. }
```

## RetrievalCondition

PhonePC/2in1Tablet

检索条件。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| recallConditions | Array<[RecallCondition](dataaugmentation-retrieval-api.md#recallcondition)> | 否 | 否 | 召回的条件，数组中的每个元素对应一个召回操作。 |
| rerankMethod | [RerankMethod](dataaugmentation-retrieval-api.md#rerankmethod) | 否 | 是 | 重排方法。其参数rerankType默认值为RRF算法，参数parameters默认值遵循[RecallCondition](dataaugmentation-retrieval-api.md#recallcondition)中相应检索回路的参数。 |
| resultCount | number | 否 | 是 | 重排后允许返回结果的最大数量。默认值为500。必须为正整数。 |
| explanation | [ExplanationConfig](dataaugmentation-retrieval-api.md#explanationconfig) | 否 | 是 | 检索解释 |

## ExplanationConfig

PhonePC/2in1Tablet

检索解释配置

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| groundTruths | Array<string> | 否 | 否 | 待解释的文档id，为字符串类型可取任意值。 |

## Recallcondition

PhonePC/2in1Tablet

type RecallCondition = InvertedIndexRecallCondition | VectorRecallCondition

召回操作的条件。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| [InvertedIndexRecallCondition](dataaugmentation-retrieval-api.md#invertedindexrecallcondition) | 倒排召回条件。 |
| [VectorRecallCondition](dataaugmentation-retrieval-api.md#vectorrecallcondition) | 向量召回条件。 |

## InvertedIndexRecallCondition

PhonePC/2in1Tablet

倒排检索的召回条件。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ftsTableName | string | 否 | 否 | 倒排检索所用的fts（Full-Text Search）数据表的名称，用于执行bm25函数输入。必须为存在的表名且不能为空字符串。 |
| fromClause | string | 否 | 否 | 查询目标索引名。不能为空字符串。  fromClause指定的表中包含filters中涉及的所有字段，允许两种输入：  1. 和ftsTableName填一样的值，则倒排检索将仅局限在倒排表内进行检索。  2. 提供完整select...join语句的方式，来连接fts表之外的元素表，作为检索表（注意，使用此模式时，该select语句中必须有rowid字段且必须是fts表的rowid。例如当ftsTableName为“files”时，存在一个元素表metadata需要参与filters过滤，则应如下定义fromClause："SELECT files.rowid as rowid, \* FROM metadata JOIN files ON metadata.fileid = files.fileid"。） |
| primaryKey | Array<[ColumnName](dataaugmentation-retrieval-api.md#columnname)> | 否 | 否 | 召回结果主键字段，会作为召回字段之一，作为多路召回文档聚合依据。一次查询中所有召回操作的主键字段数量之和必须和相等且不能为空。 |
| responseColumns | Array<[ColumnName](dataaugmentation-retrieval-api.md#columnname)> | 否 | 否 | 需要额外召回的字段集合。Array<[ColumnName](dataaugmentation-retrieval-api.md#columnname)>中[ColumnName](dataaugmentation-retrieval-api.md#columnname)不得为空。 |
| invertedIndexStrategies | Array<[InvertedIndexStrategy](dataaugmentation-retrieval-api.md#invertedindexstrategy)> | 否 | 是 | 召回策略列表，决定了倒排表应当如何打分。如果为空，则默认执行全表匹配。 |
| recallName | [RecallName](dataaugmentation-retrieval-api.md#recallname) | 否 | 是 | 当前检索回路的名称，作为重排阶段识别依据。默认值为随机字符串。构造方法中可以不构建该参数，如果有这个参数则值不能为空字符串。 |
| filters | Array<[FilterInfo](dataaugmentation-retrieval-api.md#filterinfo)> | 否 | 是 | 附加的过滤条件。 |
| deepSize | number | 否 | 是 | 重排阶段包含当前召回过程的最大结果数。默认值500，必须为正整数。 |

## ColumnName

PhonePC/2in1Tablet

type ColumnName = string

数据表的列名，类型为字符串。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| string | 数据表列名对应的类型，为字符串类型可取任意值。 |

## RecallName

PhonePC/2in1Tablet

type RecallName = string

召回回路名称，类型为字符串，用于给倒排和向量两路召回取名。例如出现两路向量召回时，给两路向量取名做区分。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| string | 召回路径名称对应的类型，类型为字符串，可取任意值。 |

## FilterInfo

PhonePC/2in1Tablet

过滤器信息。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| columns | Array<[ColumnName](dataaugmentation-retrieval-api.md#columnname)> | 否 | 否 | 被过滤的列名称。 |
| operator | [Operator](dataaugmentation-retrieval-api.md#operator) | 否 | 是 | 过滤条件中的操作算子。operator和filterValue、operator和filterRange至少有一组同时设置，过滤功能才能生效。 |
| filterValue | [FilterValue](dataaugmentation-retrieval-api.md#filtervalue) | 否 | 是 | 过滤条件中的过滤值。 |
| filterRange | [FilterRange](dataaugmentation-retrieval-api.md#filterrange) | 否 | 是 | 过滤条件中的过滤范围。 |

## FilterValue

PhonePC/2in1Tablet

type FilterValue = number | string | bigint

过滤条件中的过滤值。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| number | FilterValue 收到的类型为number则过滤条件为数字类型 |
| string | FilterValue 收到的类型为string则过滤条件为字符串类型 |
| bigint | FilterValue 收到的类型为bigint则过滤条件为int64类型 |

## FilterRange

PhonePC/2in1Tablet

过滤条件中的过滤值范围。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| max | number | 是 | 最大过滤值。 |
| min | number | 是 | 最小过滤值，取值需小于最大过滤值。 |

## Operator

PhonePC/2in1Tablet

过滤条件中的操作算子。column为数据库表中的字段名，filterValue为该字段的取值。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 操作 | 说明 |
| --- | --- |
| OP\_EQ = '=' | <column>等于<filterValue>。 |
| OP\_NE = '!=' | <column>不等于<filterValue>。 |
| OP\_LT = '<' | <column>小于<filterValue>，其中<filterValue>为数值。 |
| OP\_LE = '<=' | <column>小于等于<filterValue>，其中<filterValue>为数值。 |
| OP\_GT = '>' | <column>大于<filterValue>，其中<filterValue>为数值。 |
| OP\_GE = '>=' | <column>大于等于<filterValue>，其中<filterValue>为数值。 |
| OP\_IN = 'IN' | <column> IN <filterValue>，其中<filterValue>为string且通过','组合。 |
| OP\_NOT\_IN = 'NOT\_IN' | <column> NOT IN <filterValue>，其中<filterValue>为string且通过','拼接。 |
| OP\_BETWEEN = 'BETWEEN' | <column>的值在 <filterRange.min> 和 <filterRange.max>之间。 |
| OP\_LIKE = 'LIKE' | 通过LIKE匹配含有<filterValue>的<column> ,其中<filterValue>为string。 |
| OP\_NOT\_LIKE = 'NOT\_LIKE' | <column> NOT LIKE <filterValue>，其中<filterValue>为string。 |

## InvertedIndexStrategy

PhonePC/2in1Tablet

type InvertedIndexStrategy = Bm25Strategy | ExactMatchingStrategy | ProximityStrategy

倒排召回策略。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| [Bm25Strategy](dataaugmentation-retrieval-api.md#bm25strategy) | 部分命中策略，检索目标只要命中查询词中的80%核心词就可以被召回，召回结果基于bm25算法进行评分，适用于对检索目标匹配要求较宽松的场景。 |
| [ExactMatchingStrategy](dataaugmentation-retrieval-api.md#exactmatchingstrategy) | 精确命中策略，要求检索目标和查询词完全匹配才能被召回，适用于对检索目标匹配要求较严格的场景。 |
| [ProximityStrategy](dataaugmentation-retrieval-api.md#proximitystrategy) | 乱序命中策略，查询词的分词结果在检索目标中不必严格按照原本顺序出现，各个分词结果在指定间隔内都出现即可召回，适用于对检索目标匹配要求中等的场景。 |

## Bm25Strategy

PhonePC/2in1Tablet

倒排检索所用的bm25策略。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bm25Weight | number | 否 | 否 | bm25策略的打分权重，在多种倒排策略并存的情况下，控制该策略对最终召回结果的评分影响程度。 |
| columnWeight | Record<[ColumnName](dataaugmentation-retrieval-api.md#columnname), number> | 否 | 是 | 指定该策略运用于倒排表的哪些字段，以及这些字段对应的权重（用于控制字段匹配情况对最终结果的影响程度）  如果字段为空，则默认该策略运用于倒排表的全部字段，会默认增加1个配置，字段名为倒排表名，权重值为1.0。  如果不为空，则字段名不为空字符串，权重值为非负数。 |

## ExactMatchingStrategy

PhonePC/2in1Tablet

倒排检索所用的精确场景匹配策略。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exactMatchingWeight | number | 否 | 否 | 精确场景匹配策略的打分权重，在多种倒排策略并存的情况下，控制该策略对最终召回结果的评分影响程度。 |
| columnWeight | Record<[ColumnName](dataaugmentation-retrieval-api.md#columnname), number> | 否 | 是 | 指定该策略运用于倒排表的哪些字段，以及这些字段对应的权重（用于控制字段匹配情况对最终结果的影响程度）  如果字段为空，则默认该策略运用于倒排表的全部字段，会默认增加1个配置，字段名为倒排表名，权重值为1.0。  如果不为空，则字段名不为空字符串，权重值为非负数。 |

## ProximityStrategy

PhonePC/2in1Tablet

倒排检索所用的近似与乱序匹配策略。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| proximityWeight | number | 否 | 否 | 近似与乱序匹配策略的打分权重，在多种倒排策略并存的情况下，控制该策略对最终召回结果的评分影响程度。 |
| columnWeight | Record<[ColumnName](dataaugmentation-retrieval-api.md#columnname), number> | 否 | 是 | 指定该策略运用于倒排表的哪些字段，以及这些字段对应的权重（用于控制字段匹配情况对最终结果的影响程度）  如果字段为空，则默认该策略运用于倒排表的全部字段，会默认增加1个配置，字段名为倒排表名，权重值为1.0。  如果不为空，则字段名不为空字符串，权重值为非负数。 |
| columnSlops | Record<[ColumnName](dataaugmentation-retrieval-api.md#columnname), number> | 否 | 是 | 每个字段使用的偏移量配置。默认值和columnWeight相同的字段，值为10。字段不能为空，对应值必须为非负数。 |

## VectorRecallCondition

PhonePC/2in1Tablet

向量检索的召回条件。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vectorQuery | [VectorQuery](dataaugmentation-retrieval-api.md#vectorquery) | 否 | 否 | 用于向量检索的查询词向量。 |
| fromClause | string | 否 | 否 | 查询目标索引名。不能为空字符串。  fromClause指定的表中包含filters中涉及的所有字段，接受两种输入：  1. 和ftsTableName填一样的值，则倒排检索将仅局限在倒排表内进行检索；  2. 提供完整select...join语句的方式，来连接fts表之外的元素表，作为倒排这一路的被检索表。（使用此模式时，该select语句中必须有rowid字段且必须定义为fts表的rowid。例如：当ftsTableName为“files”时，存在一个元素表metadata需要参与filters过滤，则应如下定义fromClause："SELECT files.rowid as rowid, \* FROM metadata JOIN files ON metadata.fileid = files.fileid"。）。 |
| primaryKey | Array<[ColumnName](dataaugmentation-retrieval-api.md#columnname)> | 否 | 否 | 召回结果主键字段，会作为召回字段之一，作为多路召回文档聚合依据。一次查询中所有RecallCondition的主键字段数量必须相等且不能为空。 |
| responseColumns | Array<[ColumnName](dataaugmentation-retrieval-api.md#columnname)> | 否 | 否 | 需要额外召回的字段集合。ColumnName不得为空。 |
| recallName | [RecallName](dataaugmentation-retrieval-api.md#recallname) | 否 | 是 | 当前检索回路的名称，作为重排阶段识别依据。默认值为随机字符串，不能为空字符串 |
| filters | Array<[FilterInfo](dataaugmentation-retrieval-api.md#filterinfo)> | 否 | 是 | 额外的过滤条件。 |
| deepSize | number | 否 | 是 | 当前召回过程给重排阶段返回的最大结果数。默认值500，必须为正整数。 |

## VectorQuery

PhonePC/2in1Tablet

根据查询词生成的向量。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| column | [ColumnName](dataaugmentation-retrieval-api.md#columnname) | 否 | 否 | 待匹配向量字段名。必须为指定的向量数据库中存在的向量类型字段。 |
| value | Float32Array | 否 | 是 | 向量列的向量值。  如果未定义value字段，系统将尝试将原始query生成向量。目前在PC上支持自动生成。  从HarmonyOS 6.0.0 Beta2版本开始，此参数由“必填”变更为“可选”。 |
| similarityThreshold | number | 否 | 是 | 向量阈值，用于过滤不相似向量的阈值。默认值为1，取值范围最小值为0，最大值为[VectorRerankParameter](dataaugmentation-retrieval-api.md#vectorrerankparameter)中有效thresholds的最小值。 |

## RerankMethod

PhonePC/2in1Tablet

重排策略的参数。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rerankType | [RerankType](dataaugmentation-retrieval-api.md#reranktype) | 否 | 否 | 重排算法，取值类型为枚举类[RerankType](dataaugmentation-retrieval-api.md#reranktype)，可选项为RRF、FUSED\_SCORE，分别指向rrf排序算法以及分数融合排序算法。默认值为RRF。 |
| parameters | Record<[ChannelType](dataaugmentation-retrieval-api.md#channeltype), [RerankParameter](dataaugmentation-retrieval-api.md#rerankparameter)> | 否 | 是 | 每个召回回路对应的重排参数。如果上述检索参数RetrievalCondition中的存在的channelType未在parameters中配置重排参数，则会自动填充该channelType对应的重排参数默认值。倒排的重排参数默认值参考[InvertedIndexRerankParameter](dataaugmentation-retrieval-api.md#invertedindexrerankparameter)，向量的重排参数默认值参考[VectorRerankParameter](dataaugmentation-retrieval-api.md#vectorrerankparameter)。 |
| isSoftmaxNormalized | boolean | 否 | 是 | FUSED\_SCORE模式下，是否使用softmax函数归一化计算重排最终得分。默认为false。true表示使用softmax函数归一化计算重排最终得分，false表示不使用。 |

## RerankType

PhonePC/2in1Tablet

重排算法的类型。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 值 | 说明 |
| --- | --- | --- |
| RRF | 0 | Reciprocal Rank Fusion(RRF)方法。根据各路召回位置信息进行分档排序。  适用场景：对结果多样性要求较高的场景，希望每路结果平等输出。 |
| FUSION\_SCORE | 1 | 基于得分的召回融合方法。根据各路相关性分数进行分档排序。适用场景：对相关性准确性要求高、召回分数可靠且注重结果的排序稳定性的场景。 |

## RerankParameter

PhonePC/2in1Tablet

type RerankParameter = InvertedIndexRerankParameter| VectorRerankParameter

重排算法的参数配置。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| [InvertedIndexRerankParameter](dataaugmentation-retrieval-api.md#invertedindexrerankparameter) | 重排参数为InvertedIndexRerankParameter。 |
| [VectorRerankParameter](dataaugmentation-retrieval-api.md#vectorrerankparameter) | 重排参数为VectorRerankParameter。 |

## InvertedIndexRerankParameter

PhonePC/2in1Tablet

用于倒排索引的重排算法的参数。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| invertedIndexWeights | Record<[RecallName](dataaugmentation-retrieval-api.md#recallname), number> | 否 | 否 | 每路召回的重排权重，体现各路召回在重排过程中的重要性。key为各路召回RecallCondition的[RecallName](dataaugmentation-retrieval-api.md#recallname)，value为对应那一路召回的权重。  权重值必须为非负数。如果未定义某一路召回的权重，则默认值为1。 |

## VectorRerankParameter

PhonePC/2in1Tablet

用于向量数据的重排算法的参数。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vectorWeights | Record<[RecallName](dataaugmentation-retrieval-api.md#recallname), number> | 否 | 否 | 每路召回的重排权重，体现各路召回在重排过程中的重要性。key为各路召回RecallCondition的[RecallName](dataaugmentation-retrieval-api.md#recallname)，value为对应那一路召回的权重。权重值必须为非负数。如果未定义某一路召回的权重，则默认值为1。 |
| thresholds | Array<number> | 否 | 是 | 向量召回的分档阈值，用户应当从[0, 1]范围内给3个值，高、中、低档最低分，赋值对应cosine()相似度得分，越高越相关；  如果是2个值，则分出高、中两档，剩下结果都是低档；  如果是1个值，则除了高档剩下结果都是低档。  当给出多于3个值，则使用从大到小排序后前3个数值，后面忽略。如果未定义，默认值为[0.6, 0.45, 0.4]。 |
| numberInspector | Record<[RecallName](dataaugmentation-retrieval-api.md#recallname), [ColumnName](dataaugmentation-retrieval-api.md#columnname)> | 否 | 是 | 向量召回数字匹配降档策略配置，如果查询中存在数字，但是对应目标字段中的数字和查询数字不匹配，则将该检索结果的相关性降低。key为对应向量召回条件中的[RecallName](dataaugmentation-retrieval-api.md#recallname)，value为对应模式匹配字段名。默认值为空。 |

## RdbRecords

PhonePC/2in1Tablet

检索结果。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| records | Array<[ItemInfo](dataaugmentation-retrieval-api.md#iteminfo)> | 否 | 否 | 检索结果 |
| missedGroundTruths | Array<[ItemInfo](dataaugmentation-retrieval-api.md#iteminfo)> | 否 | 是 | 未检索到指定文档的信息 |

## ItemInfo

PhonePC/2in1Tablet

检索结果中每条数据的特定内容。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryKey | string | 否 | 否 | 检索结果的主键。 |
| columns | Record<string, [relationalStore.ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | 否 | 召回列及其内容。 |
| score | number | 否 | 否 | 检索重排后的最终得分，其反映了重排记录与查询词之间的相似度。score取值大于等于0。 |
| recallScores | Record<[ChannelType](dataaugmentation-retrieval-api.md#channeltype), Record<string, [RecallScore](dataaugmentation-retrieval-api.md#recallscore)>> | 否 | 否 | 每路召回的得分，其反映了每路召回对该结果的相关性评估。key为该路RecallCondition的scoreKey；  - 如果这里没有体现RetrievalCondition中的某一路RecallCondition的scoreKey，则代表该路召回认为该结果相关性过低不予召回。 |
| features | Record<string, number> | 否 | 否 | 不同倒排策略的得分。目前支持的倒排策略及得分为：  - "exact\_phase"：文档字段精确命中查询语句的得分。  - "out\_of\_order\_phase"：文档字段命中近似乱序匹配策略的得分。  - "token\_bm25"：文档字段bm25策略得分。  - "core\_count"：文档单个匹配字段内核心词总数。 |
| similarityLevel | [SimilarityLevel](dataaugmentation-retrieval-api.md#similaritylevel) | 否 | 否 | 根据语义向量距离以及文本匹配程度，对检索结果按照相关性分档，方便对结果进行进一步筛选并且过滤。 |

## RecallScore

PhonePC/2in1Tablet

召回过程的得分。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| score | number | 否 | 否 | 召回得分。 |
| isReverseQuery | boolean | 否 | 否 | 表示得分是否来自反查过程。true表示来自反查过程，flase表示来自原始召回过程。 |

## SimilarityLevel

PhonePC/2in1Tablet

根据语义向量距离以及文本匹配程度，对检索结果按照相关性的高中低分档，方便对结果进行进一步筛选并且过滤。

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 保留值，暂无特定含义。 |
| LOW | 1 | 结果和Query的语义向量距离小，表示语义更相似。 |
| MEDIUM | 2 | 结果和Query的语义向量距离中等，表示语义相似性中等。 |
| HIGH | 3 | 结果和Query的语义向量距离大，表示语义差异较大，相关性低。 |
