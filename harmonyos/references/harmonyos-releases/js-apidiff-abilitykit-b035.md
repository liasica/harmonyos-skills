---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-b035
title: Ability Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d7c170d5d25ab76f4c84c09fff9b5e90ebb841b628fad5643ba5963cfa6e4e9c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：UIAbilityContext；  API声明：openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>;  差异内容：16000001,16000002,16000004,16000005,16000006,16000008,16000009,16000010,16000011,16000012,16000013,16000019,16200001,201,401 | 类名：UIAbilityContext；  API声明：openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>;  差异内容：16000001,16000002,16000004,16000005,16000006,16000008,16000009,16000010,16000011,16000012,16000013,16000019,16000053,16200001,201,401 | api/application/UIAbilityContext.d.ts |
| 错误码变更 | 类名：UIExtensionContext；  API声明：openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>;  差异内容：16000001,16000002,16000004,16000005,16000006,16000008,16000009,16000010,16000011,16000012,16000013,16000019,16000069,16200001,201,401 | 类名：UIExtensionContext；  API声明：openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>;  差异内容：16000001,16000002,16000004,16000005,16000006,16000008,16000009,16000010,16000011,16000012,16000013,16000019,16000053,16000069,16200001,201,401 | api/application/UIExtensionContext.d.ts |
| 函数变更 | 类名：ChildProcess；  API声明：onStart(): void;  差异内容：NA | 类名：ChildProcess；  API声明：onStart(args?: ChildProcessArgs): void;  差异内容：args?: ChildProcessArgs | api/@ohos.app.ability.ChildProcess.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface ChildProcessArgs  差异内容： export interface ChildProcessArgs | api/@ohos.app.ability.ChildProcessArgs.d.ts |
| 新增API | NA | 类名：ChildProcessArgs；  API声明：entryParams?: string;  差异内容：entryParams?: string; | api/@ohos.app.ability.ChildProcessArgs.d.ts |
| 新增API | NA | 类名：ChildProcessArgs；  API声明：fds?: Record<string, number>;  差异内容：fds?: Record<string, number>; | api/@ohos.app.ability.ChildProcessArgs.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface ChildProcessOptions  差异内容： export interface ChildProcessOptions | api/@ohos.app.ability.ChildProcessOptions.d.ts |
| 新增API | NA | 类名：ChildProcessOptions；  API声明：isolationMode?: boolean;  差异内容：isolationMode?: boolean; | api/@ohos.app.ability.ChildProcessOptions.d.ts |
| 新增API | NA | 类名：global；  API声明： export default class PhotoEditorExtensionAbility  差异内容： export default class PhotoEditorExtensionAbility | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionAbility；  API声明：context: PhotoEditorExtensionContext;  差异内容：context: PhotoEditorExtensionContext; | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionAbility；  API声明：onCreate(): void;  差异内容：onCreate(): void; | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionAbility；  API声明：onForeground(): void;  差异内容：onForeground(): void; | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionAbility；  API声明：onBackground(): void;  差异内容：onBackground(): void; | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionAbility；  API声明：onDestroy(): void | Promise<void>;  差异内容：onDestroy(): void | Promise<void>; | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionAbility；  API声明：onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void;  差异内容：onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void; | api/@ohos.app.ability.PhotoEditorExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace sendableContextManager  差异内容： declare namespace sendableContextManager | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：sendableContextManager；  API声明：export type SendableContext = \_SendableContext;  差异内容：export type SendableContext = \_SendableContext; | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：sendableContextManager；  API声明：function convertFromContext(context: common.Context): SendableContext;  差异内容：function convertFromContext(context: common.Context): SendableContext; | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：sendableContextManager；  API声明：function convertToContext(sendableContext: SendableContext): common.Context;  差异内容：function convertToContext(sendableContext: SendableContext): common.Context; | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：sendableContextManager；  API声明：function convertToApplicationContext(sendableContext: SendableContext): common.ApplicationContext;  差异内容：function convertToApplicationContext(sendableContext: SendableContext): common.ApplicationContext; | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：sendableContextManager；  API声明：function convertToAbilityStageContext(sendableContext: SendableContext): common.AbilityStageContext;  差异内容：function convertToAbilityStageContext(sendableContext: SendableContext): common.AbilityStageContext; | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：sendableContextManager；  API声明：function convertToUIAbilityContext(sendableContext: SendableContext): common.UIAbilityContext;  差异内容：function convertToUIAbilityContext(sendableContext: SendableContext): common.UIAbilityContext; | api/@ohos.app.ability.sendableContextManager.d.ets |
| 新增API | NA | 类名：global；  API声明： export default class PhotoEditorExtensionContext  差异内容： export default class PhotoEditorExtensionContext | api/application/PhotoEditorExtensionContext.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionContext；  API声明：saveEditedContentWithUri(uri: string): Promise<AbilityResult>;  差异内容：saveEditedContentWithUri(uri: string): Promise<AbilityResult>; | api/application/PhotoEditorExtensionContext.d.ts |
| 新增API | NA | 类名：PhotoEditorExtensionContext；  API声明：saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>;  差异内容：saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>; | api/application/PhotoEditorExtensionContext.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SendableContext  差异内容： interface SendableContext | api/application/SendableContext.d.ets |
| 新增API | NA | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionNameList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：requestPermissionOnSetting(context: Context, permissionNameList: Array<Permissions>): Promise<Array<GrantStatus>>; | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：AtManager；  API声明：requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>;  差异内容：requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>; | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：abilityAccessCtrl；  API声明： export enum SwitchType  差异内容： export enum SwitchType | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：SwitchType；  API声明：CAMERA = 0  差异内容：CAMERA = 0 | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：SwitchType；  API声明：MICROPHONE = 1  差异内容：MICROPHONE = 1 | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：SwitchType；  API声明：LOCATION = 2  差异内容：LOCATION = 2 | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：LaunchReason；  API声明：PREPARE\_CONTINUATION = 10  差异内容：PREPARE\_CONTINUATION = 10 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：childProcessManager；  API声明：function startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>;  差异内容：function startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>; | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：common；  API声明：export type PhotoEditorExtensionContext = \_PhotoEditorExtensionContext.default;  差异内容：export type PhotoEditorExtensionContext = \_PhotoEditorExtensionContext.default; | api/@ohos.app.ability.common.d.ts |
| 新增API | NA | 类名：Params；  API声明：PAGE\_PATH = 'ohos.param.atomicservice.pagePath'  差异内容：PAGE\_PATH = 'ohos.param.atomicservice.pagePath' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：ROUTER\_NAME = 'ohos.param.atomicservice.routerName'  差异内容：ROUTER\_NAME = 'ohos.param.atomicservice.routerName' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：PAGE\_SOURCE\_FILE = 'ohos.param.atomicservice.pageSourceFile'  差异内容：PAGE\_SOURCE\_FILE = 'ohos.param.atomicservice.pageSourceFile' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：BUILD\_FUNCTION = 'ohos.param.atomicservice.buildFunction'  差异内容：BUILD\_FUNCTION = 'ohos.param.atomicservice.buildFunction' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：SUB\_PACKAGE\_NAME = 'ohos.param.atomicservice.subpackageName'  差异内容：SUB\_PACKAGE\_NAME = 'ohos.param.atomicservice.subpackageName' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：setSupportedProcessCache(isSupported: boolean): void;  差异内容：setSupportedProcessCache(isSupported: boolean): void; | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly installSource: string;  差异内容：readonly installSource: string; | api/bundleManager/ApplicationInfo.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly releaseType: string;  差异内容：readonly releaseType: string; | api/bundleManager/ApplicationInfo.d.ts |
| 函数变更 | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionNameList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：context: Context, permissionNameList: Array<Permissions> | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：context: Context, permissionList: Array<Permissions> | api/@ohos.abilityAccessCtrl.d.ts |
