---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-agentframeworkkit-6003
title: Agent Framework Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Agent Framework Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:938eec0cc013dc5d74ab691114937c517455b0c6da84600cc7d61d281714b1fb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export declare class AgentController  差异内容：export declare class AgentController | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：AgentController；  API声明：isAgentSupport(context: common.UIAbilityContext, agentId: string): Promise<boolean>;  差异内容：isAgentSupport(context: common.UIAbilityContext, agentId: string): Promise<boolean>; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：AgentController；  API声明：on(type: 'agentDialogOpened', callback: Callback<void>): void;  差异内容：on(type: 'agentDialogOpened', callback: Callback<void>): void; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：AgentController；  API声明：off(type: 'agentDialogOpened', callback?: Callback<void>): void;  差异内容：off(type: 'agentDialogOpened', callback?: Callback<void>): void; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：AgentController；  API声明：on(type: 'agentDialogClosed', callback: Callback<void>): void;  差异内容：on(type: 'agentDialogClosed', callback: Callback<void>): void; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：AgentController；  API声明：off(type: 'agentDialogClosed', callback?: Callback<void>): void;  差异内容：off(type: 'agentDialogClosed', callback?: Callback<void>): void; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class FunctionController  差异内容：export declare class FunctionController | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface BaseOptions  差异内容：export declare interface BaseOptions | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：BaseOptions；  API声明：title?: string;  差异内容：title?: string; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：BaseOptions；  API声明：titleFontSize?: number;  差异内容：titleFontSize?: number; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：BaseOptions；  API声明：iconSize?: number;  差异内容：iconSize?: number; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：BaseOptions；  API声明：iconColors?: ResourceColor[];  差异内容：iconColors?: ResourceColor[]; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface FunctionOptions  差异内容：export declare interface FunctionOptions | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionOptions；  API声明：queryText?: string;  差异内容：queryText?: string; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionOptions；  API声明：controlSize?: ControlSize;  差异内容：controlSize?: ControlSize; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionOptions；  API声明：buttonType?: ButtonType;  差异内容：buttonType?: ButtonType; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionOptions；  API声明：isShowShadow?: boolean;  差异内容：isShowShadow?: boolean; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionOptions；  API声明：titleColors?: ResourceColor[];  差异内容：titleColors?: ResourceColor[]; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：global；  API声明：export enum ButtonType  差异内容：export enum ButtonType | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：ButtonType；  API声明：CIRCLE = 0  差异内容：CIRCLE = 0 | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：ButtonType；  API声明：CAPSULE = 1  差异内容：CAPSULE = 1 | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct FunctionComponent  差异内容：export declare struct FunctionComponent | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionComponent；  API声明：agentId: string;  差异内容：agentId: string; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionComponent；  API声明：onError: ErrorCallback;  差异内容：onError: ErrorCallback; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionComponent；  API声明：options?: FunctionOptions;  差异内容：options?: FunctionOptions; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionComponent；  API声明：controller?: FunctionController;  差异内容：controller?: FunctionController; | api/@hms.ai.AgentFramework.d.ets |
| 新增API | NA | 类名：FunctionComponent；  API声明：build(): void;  差异内容：build(): void; | api/@hms.ai.AgentFramework.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.ai.AgentFramework.d.ets  差异内容：AgentFrameworkKit | api/@hms.ai.AgentFramework.d.ets |
