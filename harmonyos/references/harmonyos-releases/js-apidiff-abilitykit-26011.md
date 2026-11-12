---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-26011
title: Ability Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Ability Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7ae0ebfd2d332b03ab368d2ac81fcd50b1a5dc05ef0f164c8b7a0864751997de
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace cliManager  差异内容：declare namespace cliManager | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：interface ExecCmdOptions  差异内容：interface ExecCmdOptions | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：workDir?: string;  差异内容：workDir?: string; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：env?: Record<string, string>;  差异内容：env?: Record<string, string>; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：background?: boolean;  差异内容：background?: boolean; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：yieldMs?: number;  差异内容：yieldMs?: number; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：timeout?: number;  差异内容：timeout?: number; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：policy?: string;  差异内容：policy?: string; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecCmdOptions；  API声明：callback?: ToolEventCallback;  差异内容：callback?: ToolEventCallback; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：interface ExecResult  差异内容：interface ExecResult | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecResult；  API声明：exitCode?: number;  差异内容：exitCode?: number; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecResult；  API声明：outputText?: string;  差异内容：outputText?: string; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecResult；  API声明：errorText?: string;  差异内容：errorText?: string; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecResult；  API声明：signalNumber?: number;  差异内容：signalNumber?: number; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecResult；  API声明：timeOut: boolean;  差异内容：timeOut: boolean; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：ExecResult；  API声明：executionTime: number;  差异内容：executionTime: number; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：enum SessionStatus  差异内容：enum SessionStatus | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：SessionStatus；  API声明：RUNNING = 'running'  差异内容：RUNNING = 'running' | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：SessionStatus；  API声明：COMPLETED = 'completed'  差异内容：COMPLETED = 'completed' | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：SessionStatus；  API声明：FAILED = 'failed'  差异内容：FAILED = 'failed' | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：interface CliSessionInfo  差异内容：interface CliSessionInfo | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：CliSessionInfo；  API声明：sessionId: string;  差异内容：sessionId: string; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：CliSessionInfo；  API声明：toolName: string;  差异内容：toolName: string; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：CliSessionInfo；  API声明：status: SessionStatus;  差异内容：status: SessionStatus; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：CliSessionInfo；  API声明：result?: ExecResult;  差异内容：result?: ExecResult; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：function execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>;  差异内容：function execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：function subscribeSession(sessionId: string, callback: ToolEventCallback): Promise<void>;  差异内容：function subscribeSession(sessionId: string, callback: ToolEventCallback): Promise<void>; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：function clearSession(sessionId: string): Promise<void>;  差异内容：function clearSession(sessionId: string): Promise<void>; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：function querySession(sessionId: string): Promise<CliSessionInfo>;  差异内容：function querySession(sessionId: string): Promise<CliSessionInfo>; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：cliManager；  API声明：function sendMessage(sessionId: string, message: string): Promise<void>;  差异内容：function sendMessage(sessionId: string, message: string): Promise<void>; | api/@ohos.app.cli.cliManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ChildProcessInformation  差异内容：export interface ChildProcessInformation | api/application/ChildProcessInformation.d.ts |
| 新增API | NA | 类名：ChildProcessInformation；  API声明：pid: number;  差异内容：pid: number; | api/application/ChildProcessInformation.d.ts |
| 新增API | NA | 类名：ChildProcessInformation；  API声明：parentPid: number;  差异内容：parentPid: number; | api/application/ChildProcessInformation.d.ts |
| 新增API | NA | 类名：ChildProcessInformation；  API声明：processName: string;  差异内容：processName: string; | api/application/ChildProcessInformation.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface CliToolEvent  差异内容：export interface CliToolEvent | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：CliToolEvent；  API声明：toolEventType: ToolEventType;  差异内容：toolEventType: ToolEventType; | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：CliToolEvent；  API声明：data: string;  差异内容：data: string; | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum ToolEventType  差异内容：export enum ToolEventType | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：ToolEventType；  API声明：STDOUT = 'stdout'  差异内容：STDOUT = 'stdout' | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：ToolEventType；  API声明：STDERR = 'stderr'  差异内容：STDERR = 'stderr' | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：ToolEventType；  API声明：EXIT = 'exit'  差异内容：EXIT = 'exit' | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：ToolEventType；  API声明：ERROR = 'error'  差异内容：ERROR = 'error' | api/application/CliToolEvent.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnEventFn = (event: CliToolEvent) => void;  差异内容：type OnEventFn = (event: CliToolEvent) => void; | api/application/ToolEventCallback.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ToolEventCallback  差异内容：export interface ToolEventCallback | api/application/ToolEventCallback.d.ts |
| 新增API | NA | 类名：ToolEventCallback；  API声明：onEvent: OnEventFn;  差异内容：onEvent: OnEventFn; | api/application/ToolEventCallback.d.ts |
| 新增API | NA | 类名：application；  API声明：export function createModuleContextSync(context: Context, moduleName: string): Context;  差异内容：export function createModuleContextSync(context: Context, moduleName: string): Context; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：childProcessManager；  API声明：export type ChildProcessInformation = \_ChildProcessInformation;  差异内容：export type ChildProcessInformation = \_ChildProcessInformation; | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：childProcessManager；  API声明：function getChildProcessInfos(): Promise<Array<ChildProcessInformation>>;  差异内容：function getChildProcessInfos(): Promise<Array<ChildProcessInformation>>; | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager；  API声明：export enum HyperSnapErrorType  差异内容：export enum HyperSnapErrorType | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorType；  API声明：CREATE\_SNAPSHOT = 0  差异内容：CREATE\_SNAPSHOT = 0 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorType；  API声明：FORK\_FROM\_SNAPSHOT = 1  差异内容：FORK\_FROM\_SNAPSHOT = 1 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager；  API声明：export enum HyperSnapErrorCode  差异内容：export enum HyperSnapErrorCode | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_OK = 0  差异内容：ERR\_OK = 0 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_SYSTEM\_INNER = 1  差异内容：ERR\_SYSTEM\_INNER = 1 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_SNAPSHOT\_EXIST = 2  差异内容：ERR\_SNAPSHOT\_EXIST = 2 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_PROCESS\_IS\_RUNNING = 3  差异内容：ERR\_PROCESS\_IS\_RUNNING = 3 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_SNAPSHOT\_PROCESS\_IS\_DIED = 4  差异内容：ERR\_SNAPSHOT\_PROCESS\_IS\_DIED = 4 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_SNAPSHOT\_IS\_INTERRUPTED = 5  差异内容：ERR\_SNAPSHOT\_IS\_INTERRUPTED = 5 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_EXISTS\_ILLEGAL\_BINDER = 6  差异内容：ERR\_EXISTS\_ILLEGAL\_BINDER = 6 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorCode；  API声明：ERR\_LAST\_PROCESS\_NOT\_FULLY\_EXITED = 7  差异内容：ERR\_LAST\_PROCESS\_NOT\_FULLY\_EXITED = 7 | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager；  API声明：export interface HyperSnapErrorInfo  差异内容：export interface HyperSnapErrorInfo | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorInfo；  API声明：code: HyperSnapErrorCode;  差异内容：code: HyperSnapErrorCode; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorInfo；  API声明：msg: string;  差异内容：msg: string; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：HyperSnapErrorInfo；  API声明：occurTimeStamp: number;  差异内容：occurTimeStamp: number; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager；  API声明：function getLastError(errType: HyperSnapErrorType): Promise<HyperSnapErrorInfo>;  差异内容：function getLastError(errType: HyperSnapErrorType): Promise<HyperSnapErrorInfo>; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：StartOptions；  API声明：preferDefaultBrowser?: boolean;  差异内容：preferDefaultBrowser?: boolean; | api/@ohos.app.ability.StartOptions.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：UKEY\_AUTH = 40  差异内容：UKEY\_AUTH = 40 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：export enum BundleInstallStatus  差异内容：export enum BundleInstallStatus | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInstallStatus；  API声明：BUNDLE\_NOT\_EXIST = 1  差异内容：BUNDLE\_NOT\_EXIST = 1 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInstallStatus；  API声明：BUNDLE\_INSTALLING = 2  差异内容：BUNDLE\_INSTALLING = 2 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInstallStatus；  API声明：BUNDLE\_INSTALLED = 3  差异内容：BUNDLE\_INSTALLED = 3 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getBundleInstallStatus(bundleName: string): BundleInstallStatus;  差异内容：function getBundleInstallStatus(bundleName: string): BundleInstallStatus; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：getUIAbilityChildProcessInfos(): Promise<Array<ChildProcessInformation>>;  差异内容：getUIAbilityChildProcessInfos(): Promise<Array<ChildProcessInformation>>; | api/application/ApplicationContext.d.ts |
| 新增kit | 类名：global；  API声明：api@ohos.ability.dataUriUtils.d.ts  差异内容：NA | 类名：global；  API声明：api@ohos.ability.dataUriUtils.d.ts  差异内容：AbilityKit | api/@ohos.ability.dataUriUtils.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.cli.cliManager.d.ts  差异内容：AbilityKit | api/@ohos.app.cli.cliManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.function.functionManager.d.ts  差异内容：AbilityKit | api/@ohos.app.function.functionManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\ChildProcessInformation.d.ts  差异内容：AbilityKit | api/application/ChildProcessInformation.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\CliToolEvent.d.ts  差异内容：AbilityKit | api/application/CliToolEvent.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\ToolEventCallback.d.ts  差异内容：AbilityKit | api/application/ToolEventCallback.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：UIAbilityContext；  API声明：setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>;  差异内容：setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>; | 类名：UIAbilityContext；  API声明：setAbilityInstanceInfo(label: string, icon: image.PixelMap, groupId: string): Promise<void>;  差异内容：setAbilityInstanceInfo(label: string, icon: image.PixelMap, groupId: string): Promise<void>; | api/application/UIAbilityContext.d.ts |
