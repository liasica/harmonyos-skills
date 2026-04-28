---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataaugmentationkit-6001
title: Data Augmentation Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Data Augmentation Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7c8db1000932eb7093d8584fa83a5de5665d8391dc9837b0699a2b63d16bdd0a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace rag  差异内容：declare namespace rag | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface LLMStreamAnswer  差异内容：interface LLMStreamAnswer | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMStreamAnswer；  API声明：isFinished: boolean;  差异内容：isFinished: boolean; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMStreamAnswer；  API声明：chunk: string;  差异内容：chunk: string; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMStreamAnswer；  API声明：err?: BusinessError<string>;  差异内容：err?: BusinessError<string>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：enum LLMRequestStatus  差异内容：enum LLMRequestStatus | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestStatus；  API声明：LLM\_SUCCESS = 0  差异内容：LLM\_SUCCESS = 0 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestStatus；  API声明：LLM\_REQUEST\_ERROR = 1  差异内容：LLM\_REQUEST\_ERROR = 1 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestStatus；  API声明：LLM\_LOAD\_FAILED = 2  差异内容：LLM\_LOAD\_FAILED = 2 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestStatus；  API声明：LLM\_TIMEOUT = 3  差异内容：LLM\_TIMEOUT = 3 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestStatus；  API声明：LLM\_BUSY = 4  差异内容：LLM\_BUSY = 4 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface LLMRequestInfo  差异内容：interface LLMRequestInfo | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestInfo；  API声明：chatId: number;  差异内容：chatId: number; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：LLMRequestInfo；  API声明：status: LLMRequestStatus;  差异内容：status: LLMRequestStatus; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：abstract class ChatLLM  差异内容：abstract class ChatLLM | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：ChatLLM；  API声明：abstract streamChat(query: string, callback: Callback<LLMStreamAnswer>): Promise<LLMRequestInfo>;  差异内容：abstract streamChat(query: string, callback: Callback<LLMStreamAnswer>): Promise<LLMRequestInfo>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface Config  差异内容：interface Config | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Config；  API声明：llm: ChatLLM;  差异内容：llm: ChatLLM; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Config；  API声明：retrievalConfig: retrieval.RetrievalConfig;  差异内容：retrievalConfig: retrieval.RetrievalConfig; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Config；  API声明：retrievalCondition: retrieval.RetrievalCondition;  差异内容：retrievalCondition: retrieval.RetrievalCondition; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface Answer  差异内容：interface Answer | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Answer；  API声明：chunk: string;  差异内容：chunk: string; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Answer；  API声明：data?: Array<retrieval.ItemInfo>;  差异内容：data?: Array<retrieval.ItemInfo>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：enum StreamType  差异内容：enum StreamType | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：StreamType；  API声明：THOUGHT = 0  差异内容：THOUGHT = 0 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：StreamType；  API声明：REFERENCE = 1  差异内容：REFERENCE = 1 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：StreamType；  API声明：ANSWER = 2  差异内容：ANSWER = 2 | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface Stream  差异内容：interface Stream | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Stream；  API声明：type: StreamType;  差异内容：type: StreamType; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Stream；  API声明：answer: Answer;  差异内容：answer: Answer; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：Stream；  API声明：isFinished: boolean;  差异内容：isFinished: boolean; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface RunConfig  差异内容：interface RunConfig | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：RunConfig；  API声明：answerTypes: Array<StreamType>;  差异内容：answerTypes: Array<StreamType>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface FeedbackInfo  差异内容：interface FeedbackInfo | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：FeedbackInfo；  API声明：runId: number;  差异内容：runId: number; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：FeedbackInfo；  API声明：score: number;  差异内容：score: number; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：FeedbackInfo；  API声明：source?: Record<StreamType, Answer>;  差异内容：source?: Record<StreamType, Answer>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：FeedbackInfo；  API声明：comment?: string;  差异内容：comment?: string; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：interface RagSession  差异内容：interface RagSession | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：RagSession；  API声明：streamRun(question: string, config: RunConfig, callback: AsyncCallback<Stream>): Promise<number>;  差异内容：streamRun(question: string, config: RunConfig, callback: AsyncCallback<Stream>): Promise<number>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：RagSession；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：function createRagSession(context: common.Context, config: Config): Promise<RagSession>;  差异内容：function createRagSession(context: common.Context, config: Config): Promise<RagSession>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：rag；  API声明：function feedback(context: common.Context, feedbackInfo: FeedbackInfo): Promise<void>;  差异内容：function feedback(context: common.Context, feedbackInfo: FeedbackInfo): Promise<void>; | api/@hms.data.rag.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace retrieval  差异内容：declare namespace retrieval | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：function getRetriever(config: RetrievalConfig): Promise<Retriever>;  差异内容：function getRetriever(config: RetrievalConfig): Promise<Retriever>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface RetrievalConfig  差异内容：interface RetrievalConfig | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RetrievalConfig；  API声明：channelConfigs: Array<ChannelConfig>;  差异内容：channelConfigs: Array<ChannelConfig>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface ChannelConfig  差异内容：interface ChannelConfig | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ChannelConfig；  API声明：channelType: ChannelType;  差异内容：channelType: ChannelType; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ChannelConfig；  API声明：context: common.BaseContext;  差异内容：context: common.BaseContext; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ChannelConfig；  API声明：dbConfig: DbConfig;  差异内容：dbConfig: DbConfig; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：enum ChannelType  差异内容：enum ChannelType | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ChannelType；  API声明：VECTOR\_DATABASE = 0  差异内容：VECTOR\_DATABASE = 0 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ChannelType；  API声明：INVERTED\_INDEX\_DATABASE = 1  差异内容：INVERTED\_INDEX\_DATABASE = 1 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type DbConfig = relationalStore.StoreConfig;  差异内容：type DbConfig = relationalStore.StoreConfig; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface Retriever  差异内容：interface Retriever | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Retriever；  API声明：retrieveRdb(query: string, condition: RetrievalCondition): Promise<RdbRecords>;  差异内容：retrieveRdb(query: string, condition: RetrievalCondition): Promise<RdbRecords>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface RetrievalCondition  差异内容：interface RetrievalCondition | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RetrievalCondition；  API声明：recallConditions: Array<RecallCondition>;  差异内容：recallConditions: Array<RecallCondition>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RetrievalCondition；  API声明：rerankMethod?: RerankMethod;  差异内容：rerankMethod?: RerankMethod; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RetrievalCondition；  API声明：resultCount?: number;  差异内容：resultCount?: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type RecallCondition = InvertedIndexRecallCondition | VectorRecallCondition;  差异内容：type RecallCondition = InvertedIndexRecallCondition | VectorRecallCondition; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface InvertedIndexRecallCondition  差异内容：interface InvertedIndexRecallCondition | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：ftsTableName: string;  差异内容：ftsTableName: string; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：fromClause: string;  差异内容：fromClause: string; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：primaryKey: Array<ColumnName>;  差异内容：primaryKey: Array<ColumnName>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：responseColumns: Array<ColumnName>;  差异内容：responseColumns: Array<ColumnName>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：invertedIndexStrategies?: Array<InvertedIndexStrategy>;  差异内容：invertedIndexStrategies?: Array<InvertedIndexStrategy>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：recallName?: RecallName;  差异内容：recallName?: RecallName; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：filters?: Array<FilterInfo>;  差异内容：filters?: Array<FilterInfo>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRecallCondition；  API声明：deepSize?: number;  差异内容：deepSize?: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type ColumnName = string;  差异内容：type ColumnName = string; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type RecallName = string;  差异内容：type RecallName = string; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface FilterInfo  差异内容：interface FilterInfo | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：FilterInfo；  API声明：columns: Array<ColumnName>;  差异内容：columns: Array<ColumnName>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：FilterInfo；  API声明：operator?: Operator;  差异内容：operator?: Operator; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：FilterInfo；  API声明：filterValue?: FilterValue;  差异内容：filterValue?: FilterValue; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：FilterInfo；  API声明：filterRange?: FilterRange;  差异内容：filterRange?: FilterRange; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type FilterValue = string | number | bigint;  差异内容：type FilterValue = string | number | bigint; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface FilterRange  差异内容：interface FilterRange | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：FilterRange；  API声明：max: number;  差异内容：max: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：FilterRange；  API声明：min: number;  差异内容：min: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：enum Operator  差异内容：enum Operator | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_EQ = '='  差异内容：OP\_EQ = '=' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_NE = '!='  差异内容：OP\_NE = '!=' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_LT = '<'  差异内容：OP\_LT = '<' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_LE = '<='  差异内容：OP\_LE = '<=' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_GT = '>'  差异内容：OP\_GT = '>' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_GE = '>='  差异内容：OP\_GE = '>=' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_IN = 'IN'  差异内容：OP\_IN = 'IN' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_NOT\_IN = 'NOT\_IN'  差异内容：OP\_NOT\_IN = 'NOT\_IN' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_BETWEEN = 'BETWEEN'  差异内容：OP\_BETWEEN = 'BETWEEN' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_LIKE = 'LIKE'  差异内容：OP\_LIKE = 'LIKE' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Operator；  API声明：OP\_NOT\_LIKE = 'NOT\_LIKE'  差异内容：OP\_NOT\_LIKE = 'NOT\_LIKE' | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type InvertedIndexStrategy = Bm25Strategy | ExactMatchingStrategy | ProximityStrategy;  差异内容：type InvertedIndexStrategy = Bm25Strategy | ExactMatchingStrategy | ProximityStrategy; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface Bm25Strategy  差异内容：interface Bm25Strategy | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Bm25Strategy；  API声明：bm25Weight: number;  差异内容：bm25Weight: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：Bm25Strategy；  API声明：columnWeight?: Record<ColumnName, number>;  差异内容：columnWeight?: Record<ColumnName, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface ExactMatchingStrategy  差异内容：interface ExactMatchingStrategy | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ExactMatchingStrategy；  API声明：exactMatchingWeight: number;  差异内容：exactMatchingWeight: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ExactMatchingStrategy；  API声明：columnWeight?: Record<ColumnName, number>;  差异内容：columnWeight?: Record<ColumnName, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface ProximityStrategy  差异内容：interface ProximityStrategy | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ProximityStrategy；  API声明：proximityWeight: number;  差异内容：proximityWeight: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ProximityStrategy；  API声明：columnWeight?: Record<ColumnName, number>;  差异内容：columnWeight?: Record<ColumnName, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ProximityStrategy；  API声明：columnSlops?: Record<ColumnName, number>;  差异内容：columnSlops?: Record<ColumnName, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface VectorRecallCondition  差异内容：interface VectorRecallCondition | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：vectorQuery: VectorQuery;  差异内容：vectorQuery: VectorQuery; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：fromClause: string;  差异内容：fromClause: string; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：primaryKey: Array<ColumnName>;  差异内容：primaryKey: Array<ColumnName>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：responseColumns: Array<ColumnName>;  差异内容：responseColumns: Array<ColumnName>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：recallName?: RecallName;  差异内容：recallName?: RecallName; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：filters?: Array<FilterInfo>;  差异内容：filters?: Array<FilterInfo>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRecallCondition；  API声明：deepSize?: number;  差异内容：deepSize?: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface VectorQuery  差异内容：interface VectorQuery | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorQuery；  API声明：column: ColumnName;  差异内容：column: ColumnName; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorQuery；  API声明：value: Float32Array;  差异内容：value: Float32Array; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorQuery；  API声明：similarityThreshold?: number;  差异内容：similarityThreshold?: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface RerankMethod  差异内容：interface RerankMethod | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RerankMethod；  API声明：rerankType: RerankType;  差异内容：rerankType: RerankType; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RerankMethod；  API声明：parameters?: Record<ChannelType, RerankParameter>;  差异内容：parameters?: Record<ChannelType, RerankParameter>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RerankMethod；  API声明：isSoftmaxNormalized?: boolean;  差异内容：isSoftmaxNormalized?: boolean; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：enum RerankType  差异内容：enum RerankType | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RerankType；  API声明：RRF = 0  差异内容：RRF = 0 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RerankType；  API声明：FUSION\_SCORE = 1  差异内容：FUSION\_SCORE = 1 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：type RerankParameter = InvertedIndexRerankParameter | VectorRerankParameter;  差异内容：type RerankParameter = InvertedIndexRerankParameter | VectorRerankParameter; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface InvertedIndexRerankParameter  差异内容：interface InvertedIndexRerankParameter | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：InvertedIndexRerankParameter；  API声明：invertedIndexWeights: Record<RecallName, number>;  差异内容：invertedIndexWeights: Record<RecallName, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface VectorRerankParameter  差异内容：interface VectorRerankParameter | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRerankParameter；  API声明：vectorWeights: Record<RecallName, number>;  差异内容：vectorWeights: Record<RecallName, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRerankParameter；  API声明：thresholds?: Array<number>;  差异内容：thresholds?: Array<number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：VectorRerankParameter；  API声明：numberInspector?: Record<RecallName, ColumnName>;  差异内容：numberInspector?: Record<RecallName, ColumnName>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface RdbRecords  差异内容：interface RdbRecords | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RdbRecords；  API声明：records: Array<ItemInfo>;  差异内容：records: Array<ItemInfo>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface ItemInfo  差异内容：interface ItemInfo | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ItemInfo；  API声明：primaryKey: string;  差异内容：primaryKey: string; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ItemInfo；  API声明：columns: Record<string, relationalStore.ValueType>;  差异内容：columns: Record<string, relationalStore.ValueType>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ItemInfo；  API声明：score: number;  差异内容：score: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ItemInfo；  API声明：recallScores: Record<ChannelType, Record<string, RecallScore>>;  差异内容：recallScores: Record<ChannelType, Record<string, RecallScore>>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ItemInfo；  API声明：features: Record<string, number>;  差异内容：features: Record<string, number>; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ItemInfo；  API声明：similarityLevel: SimilarityLevel;  差异内容：similarityLevel: SimilarityLevel; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface RecallScore  差异内容：interface RecallScore | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RecallScore；  API声明：score: number;  差异内容：score: number; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：RecallScore；  API声明：isReverseQuery: boolean;  差异内容：isReverseQuery: boolean; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：enum SimilarityLevel  差异内容：enum SimilarityLevel | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：SimilarityLevel；  API声明：NONE = 0  差异内容：NONE = 0 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：SimilarityLevel；  API声明：LOW = 1  差异内容：LOW = 1 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：SimilarityLevel；  API声明：MEDIUM = 2  差异内容：MEDIUM = 2 | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：SimilarityLevel；  API声明：HIGH = 3  差异内容：HIGH = 3 | api/@hms.data.retrieval.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.data.rag.d.ts  差异内容：DataAugmentationKit | api/@hms.data.rag.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.data.retrieval.d.ts  差异内容：DataAugmentationKit | api/@hms.data.retrieval.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.DataAugmentationKit.d.ts  差异内容：DataAugmentationKit | kits/@kit.DataAugmentationKit.d.ts |
