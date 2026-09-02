---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-agentframeworkkit-7002
title: Agent Framework Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Agent Framework Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d0eef279861c21222d2f2874e69d69c53ccd5445144405e35fdf6c5277583a1c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export enum Role  差异内容：export enum Role | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Role；  API声明：AGENT = 0  差异内容：AGENT = 0 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Role；  API声明：USER = 1  差异内容：USER = 1 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Role；  API声明：UNSPECIFIED = 2  差异内容：UNSPECIFIED = 2 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum TaskState  差异内容：export enum TaskState | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：SUBMITTED = 0  差异内容：SUBMITTED = 0 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：WORKING = 1  差异内容：WORKING = 1 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：INPUT\_REQUIRED = 2  差异内容：INPUT\_REQUIRED = 2 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：COMPLETED = 3  差异内容：COMPLETED = 3 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：CANCELED = 4  差异内容：CANCELED = 4 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：FAILED = 5  差异内容：FAILED = 5 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：REJECTED = 6  差异内容：REJECTED = 6 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：AUTH\_REQUIRED = 7  差异内容：AUTH\_REQUIRED = 7 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskState；  API声明：UNSPECIFIED = 8  差异内容：UNSPECIFIED = 8 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Part  差异内容：export interface Part | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：text?: string;  差异内容：text?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：raw?: string;  差异内容：raw?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：url?: string;  差异内容：url?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：data?: object | string | number | boolean;  差异内容：data?: object | string | number | boolean; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：mediaType?: string;  差异内容：mediaType?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：filename?: string;  差异内容：filename?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Part；  API声明：metadata?: object;  差异内容：metadata?: object; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Message  差异内容：export interface Message | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：messageId: string;  差异内容：messageId: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：role: Role;  差异内容：role: Role; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：parts: Part[];  差异内容：parts: Part[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：contextId?: string;  差异内容：contextId?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：extensions?: string[];  差异内容：extensions?: string[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：metadata?: object;  差异内容：metadata?: object; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：referenceTaskIds?: string[];  差异内容：referenceTaskIds?: string[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Message；  API声明：taskId?: string;  差异内容：taskId?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Artifact  差异内容：export interface Artifact | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Artifact；  API声明：artifactId: string;  差异内容：artifactId: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Artifact；  API声明：parts: Part[];  差异内容：parts: Part[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Artifact；  API声明：description?: string;  差异内容：description?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Artifact；  API声明：extensions?: string[];  差异内容：extensions?: string[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Artifact；  API声明：metadata?: object;  差异内容：metadata?: object; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Artifact；  API声明：name?: string;  差异内容：name?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface TaskStatus  差异内容：export interface TaskStatus | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskStatus；  API声明：state: TaskState;  差异内容：state: TaskState; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskStatus；  API声明：timestamp?: string;  差异内容：timestamp?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskStatus；  API声明：message?: Message;  差异内容：message?: Message; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Task  差异内容：export interface Task | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Task；  API声明：id: string;  差异内容：id: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Task；  API声明：contextId: string;  差异内容：contextId: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Task；  API声明：status: TaskStatus;  差异内容：status: TaskStatus; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Task；  API声明：artifacts?: Artifact[];  差异内容：artifacts?: Artifact[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Task；  API声明：history?: Message[];  差异内容：history?: Message[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Task；  API声明：metadata?: object;  差异内容：metadata?: object; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export type OnDataCallback = (method: AgentOperation, context: RequestContext) => void;  差异内容：export type OnDataCallback = (method: AgentOperation, context: RequestContext) => void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export function createA2AServer(agentCard: common.AgentCard, onData: OnDataCallback, want?: Want): Server;  差异内容：export function createA2AServer(agentCard: common.AgentCard, onData: OnDataCallback, want?: Want): Server; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export type ProxySender = (data: string) => void;  差异内容：export type ProxySender = (data: string) => void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Server  差异内容：export interface Server | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Server；  API声明：start(): void;  差异内容：start(): void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Server；  API声明：stop(): void;  差异内容：stop(): void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Server；  API声明：onMessage(data: string, sender: ProxySender): void;  差异内容：onMessage(data: string, sender: ProxySender): void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Server；  API声明：onAuth(data: string): string;  差异内容：onAuth(data: string): string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Server；  API声明：updateStatus(taskId: string, status: TaskStatus): void;  差异内容：updateStatus(taskId: string, status: TaskStatus): void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：Server；  API声明：addArtifact(taskId: string, taskArtifactParam: TaskArtifactParam): void;  差异内容：addArtifact(taskId: string, taskArtifactParam: TaskArtifactParam): void; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum AgentOperation  差异内容：export enum AgentOperation | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：AgentOperation；  API声明：EXECUTE = 0  差异内容：EXECUTE = 0 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：AgentOperation；  API声明：CANCEL = 1  差异内容：CANCEL = 1 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：AgentOperation；  API声明：CLEAR\_CONTEXT = 2  差异内容：CLEAR\_CONTEXT = 2 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：AgentOperation；  API声明：PERCEPTION\_SUGGEST = 3  差异内容：PERCEPTION\_SUGGEST = 3 | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface RequestContext  差异内容：export interface RequestContext | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getAgentId(): string | undefined;  差异内容：getAgentId(): string | undefined; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getClientSessionId(): string | undefined;  差异内容：getClientSessionId(): string | undefined; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getUserInput(delimiter?: string): string;  差异内容：getUserInput(delimiter?: string): string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getMessage(): Message | undefined;  差异内容：getMessage(): Message | undefined; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getRelatedTasks(): Task[];  差异内容：getRelatedTasks(): Task[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getCurrentTask(): Task | undefined;  差异内容：getCurrentTask(): Task | undefined; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getTaskId(): string | undefined;  差异内容：getTaskId(): string | undefined; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getContextId(): string | undefined;  差异内容：getContextId(): string | undefined; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：RequestContext；  API声明：getMetadata(): object;  差异内容：getMetadata(): object; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface TaskArtifactParam  差异内容：export interface TaskArtifactParam | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：parts: Part[];  差异内容：parts: Part[]; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：artifactId?: string;  差异内容：artifactId?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：name?: string;  差异内容：name?: string; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：metadata?: object;  差异内容：metadata?: object; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：append?: boolean;  差异内容：append?: boolean; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：lastChunk?: boolean;  差异内容：lastChunk?: boolean; | api/@hms.ai.A2A.d.ts |
| 新增API | NA | 类名：TaskArtifactParam；  API声明：extensions?: string[];  差异内容：extensions?: string[]; | api/@hms.ai.A2A.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.ai.A2A.d.ts  差异内容：AgentFrameworkKit | api/@hms.ai.A2A.d.ts |
