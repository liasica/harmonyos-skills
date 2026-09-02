---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6111
title: Basic Services Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:28fa02584b5be67a98df4f26f98ffd488dafa072a48ba9a892c4c68c689e56bd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare class SelectionExtensionAbility  差异内容：declare class SelectionExtensionAbility | api/@ohos.selectionInput.SelectionExtensionAbility.d.ts |
| 新增API | NA | 类名：SelectionExtensionAbility；  API声明：context: SelectionExtensionContext;  差异内容：context: SelectionExtensionContext; | api/@ohos.selectionInput.SelectionExtensionAbility.d.ts |
| 新增API | NA | 类名：SelectionExtensionAbility；  API声明：onConnect(want: Want): rpc.RemoteObject;  差异内容：onConnect(want: Want): rpc.RemoteObject; | api/@ohos.selectionInput.SelectionExtensionAbility.d.ts |
| 新增API | NA | 类名：SelectionExtensionAbility；  API声明：onDisconnect(): void;  差异内容：onDisconnect(): void; | api/@ohos.selectionInput.SelectionExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class SelectionExtensionContext  差异内容：declare class SelectionExtensionContext | api/@ohos.selectionInput.SelectionExtensionContext.d.ts |
| 新增API | NA | 类名：SelectionExtensionContext；  API声明：startAbility(want: Want): Promise<void>;  差异内容：startAbility(want: Want): Promise<void>; | api/@ohos.selectionInput.SelectionExtensionContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace selectionManager  差异内容：declare namespace selectionManager | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void;  差异内容：function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void;  差异内容：function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：function getSelectionContent(): Promise<string>;  差异内容：function getSelectionContent(): Promise<string>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>;  差异内容：function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：function destroyPanel(panel: Panel): Promise<void>;  差异内容：function destroyPanel(panel: Panel): Promise<void>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：interface SelectionInfo  差异内容：interface SelectionInfo | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：selectionType: SelectionType;  差异内容：selectionType: SelectionType; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：startDisplayX: number;  差异内容：startDisplayX: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：startDisplayY: number;  差异内容：startDisplayY: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：endDisplayX: number;  差异内容：endDisplayX: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：endDisplayY: number;  差异内容：endDisplayY: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：startWindowX: number;  差异内容：startWindowX: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：startWindowY: number;  差异内容：startWindowY: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：endWindowX: number;  差异内容：endWindowX: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：endWindowY: number;  差异内容：endWindowY: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：displayID: number;  差异内容：displayID: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：windowID: number;  差异内容：windowID: number; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：interface Panel  差异内容：interface Panel | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setUiContent(path: string): Promise<void>;  差异内容：setUiContent(path: string): Promise<void>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：show(): Promise<void>;  差异内容：show(): Promise<void>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：hide(): Promise<void>;  差异内容：hide(): Promise<void>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：startMoving(): Promise<void>;  差异内容：startMoving(): Promise<void>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：moveToGlobalDisplay(x: number, y: number): Promise<void>;  差异内容：moveToGlobalDisplay(x: number, y: number): Promise<void>; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：on(type: 'destroyed', callback: Callback<void>): void;  差异内容：on(type: 'destroyed', callback: Callback<void>): void; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：off(type: 'destroyed', callback?: Callback<void>): void;  差异内容：off(type: 'destroyed', callback?: Callback<void>): void; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：on(type: 'hidden', callback: Callback<void>): void;  差异内容：on(type: 'hidden', callback: Callback<void>): void; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：Panel；  API声明：off(type: 'hidden', callback?: Callback<void>): void;  差异内容：off(type: 'hidden', callback?: Callback<void>): void; | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：selectionManager；  API声明：enum SelectionType  差异内容：enum SelectionType | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionType；  API声明：MOUSE\_MOVE = 1  差异内容：MOUSE\_MOVE = 1 | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionType；  API声明：DOUBLE\_CLICK = 2  差异内容：DOUBLE\_CLICK = 2 | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：SelectionType；  API声明：TRIPLE\_CLICK = 3  差异内容：TRIPLE\_CLICK = 3 | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface PanelInfo  差异内容：export interface PanelInfo | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：panelType: PanelType;  差异内容：panelType: PanelType; | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：x: number;  差异内容：x: number; | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：y: number;  差异内容：y: number; | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：width: number;  差异内容：width: number; | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：height: number;  差异内容：height: number; | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum PanelType  差异内容：export enum PanelType | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：MENU\_PANEL = 1  差异内容：MENU\_PANEL = 1 | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：MAIN\_PANEL = 2  差异内容：MAIN\_PANEL = 2 | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace settingsLite  差异内容：declare namespace settingsLite | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：settingsLite；  API声明：function openPinSettingPage(): void;  差异内容：function openPinSettingPage(): void; | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：settingsLite；  API声明：function openNfcSettingsPage(): void;  差异内容：function openNfcSettingsPage(): void; | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：settingsLite；  API声明：function openDoubleClickSettingsPage(): void;  差异内容：function openDoubleClickSettingsPage(): void; | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：settingsLite；  API声明：interface ClickCallback  差异内容：interface ClickCallback | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：ClickCallback；  API声明：onResult(result: boolean): void;  差异内容：onResult(result: boolean): void; | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：settingsLite；  API声明：function isDoubleClickAppForSelf(callback: ClickCallback): void;  差异内容：function isDoubleClickAppForSelf(callback: ClickCallback): void; | api/@ohos.settingsLite.d.ts |
| 新增API | NA | 类名：Pattern；  API声明：HTTP\_URL = 3  差异内容：HTTP\_URL = 3 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern；  API声明：FLIGHT\_NUMBER = 4  差异内容：FLIGHT\_NUMBER = 4 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard；  API声明：hasRemoteData(): boolean;  差异内容：hasRemoteData(): boolean; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：public onStartPrintJob(jobInfo: print.PrintJob): void;  差异内容：public onStartPrintJob(jobInfo: print.PrintJob): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：public onCancelPrintJob(jobInfo: print.PrintJob): void;  差异内容：public onCancelPrintJob(jobInfo: print.PrintJob): void; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：PrintExtensionAbility；  API声明：public onRequestPrinterCapability(printerId: number): print.PrinterCapability;  差异内容：public onRequestPrinterCapability(printerId: number): print.PrinterCapability; | api/@ohos.app.ability.PrintExtensionAbility.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAY\_STATE\_CHANGE = 'usual.event.bluetooth.a2dpsource.PLAY\_STATE\_CHANGE'  差异内容：COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAY\_STATE\_CHANGE = 'usual.event.bluetooth.a2dpsource.PLAY\_STATE\_CHANGE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_BLUETOOTH\_SCO\_CONNECT\_STATE\_CHANGE = 'usual.event.bluetooth.SCO\_CONNECT\_STATE\_CHANGE'  差异内容：COMMON\_EVENT\_BLUETOOTH\_SCO\_CONNECT\_STATE\_CHANGE = 'usual.event.bluetooth.SCO\_CONNECT\_STATE\_CHANGE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrintMargin  差异内容：interface PrintMargin | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintMargin；  API声明：top?: number;  差异内容：top?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintMargin；  API声明：bottom?: number;  差异内容：bottom?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintMargin；  API声明：left?: number;  差异内容：left?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintMargin；  API声明：right?: number;  差异内容：right?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrinterRange  差异内容：interface PrinterRange | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterRange；  API声明：startPage?: number;  差异内容：startPage?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterRange；  API声明：endPage?: number;  差异内容：endPage?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterRange；  API声明：pages?: Array<number>;  差异内容：pages?: Array<number>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PreviewAttribute  差异内容：interface PreviewAttribute | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PreviewAttribute；  API声明：previewRange: PrinterRange;  差异内容：previewRange: PrinterRange; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PreviewAttribute；  API声明：result?: number;  差异内容：result?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrintResolution  差异内容：interface PrintResolution | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintResolution；  API声明：id: string;  差异内容：id: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintResolution；  API声明：horizontalDpi: number;  差异内容：horizontalDpi: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintResolution；  API声明：verticalDpi: number;  差异内容：verticalDpi: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrinterCapability  差异内容：interface PrinterCapability | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapability；  API声明：colorMode: number;  差异内容：colorMode: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapability；  API声明：duplexMode: number;  差异内容：duplexMode: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapability；  API声明：pageSize: Array<PrintPageSize>;  差异内容：pageSize: Array<PrintPageSize>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapability；  API声明：resolution?: Array<PrintResolution>;  差异内容：resolution?: Array<PrintResolution>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapability；  API声明：minMargin?: PrintMargin;  差异内容：minMargin?: PrintMargin; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterCapability；  API声明：options?: Object;  差异内容：options?: Object; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrinterInfo  差异内容：interface PrinterInfo | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：printerId: string;  差异内容：printerId: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：printerName: string;  差异内容：printerName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：printerState: PrinterState;  差异内容：printerState: PrinterState; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：printerIcon?: number;  差异内容：printerIcon?: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：capability?: PrinterCapability;  差异内容：capability?: PrinterCapability; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInfo；  API声明：options?: Object;  差异内容：options?: Object; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrintJob  差异内容：interface PrintJob | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：fdList: Array<number>;  差异内容：fdList: Array<number>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：jobId: string;  差异内容：jobId: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：printerId: string;  差异内容：printerId: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：jobState: PrintJobState;  差异内容：jobState: PrintJobState; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：jobSubstate: PrintJobSubState;  差异内容：jobSubstate: PrintJobSubState; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：copyNumber: number;  差异内容：copyNumber: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：pageRange: PrinterRange;  差异内容：pageRange: PrinterRange; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：isSequential: boolean;  差异内容：isSequential: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：pageSize: PrintPageSize;  差异内容：pageSize: PrintPageSize; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：isLandscape: boolean;  差异内容：isLandscape: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：colorMode: number;  差异内容：colorMode: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：duplexMode: number;  差异内容：duplexMode: number; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：margin?: PrintMargin;  差异内容：margin?: PrintMargin; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：preview?: PreviewAttribute;  差异内容：preview?: PreviewAttribute; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJob；  API声明：options?: Object;  差异内容：options?: Object; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_SMB\_LOGIN\_LOCKOUT = 13100012  差异内容：E\_PRINT\_SMB\_LOGIN\_LOCKOUT = 13100012 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_SMB\_CONNECTION\_FAILURE = 13100013  差异内容：E\_PRINT\_SMB\_CONNECTION\_FAILURE = 13100013 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_SMB\_INVALID\_CREDENTIALS = 13100014  差异内容：E\_PRINT\_SMB\_INVALID\_CREDENTIALS = 13100014 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState, callback: AsyncCallback<void>): void;  差异内容：function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState, callback: AsyncCallback<void>): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>;  差异内容：function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：selectedDriver?: PpdInfo;  差异内容：selectedDriver?: PpdInfo; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterInformation；  API声明：selectedProtocol?: string;  差异内容：selectedProtocol?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultColorMode?: PrintColorMode;  差异内容：defaultColorMode?: PrintColorMode; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultCollate?: boolean;  差异内容：defaultCollate?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultReverse?: boolean;  差异内容：defaultReverse?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>;  差异内容：function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface SharedHost  差异内容：interface SharedHost | api/@ohos.print.d.ts |
| 新增API | NA | 类名：SharedHost；  API声明：ip: string;  差异内容：ip: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：SharedHost；  API声明：shareName: string;  差异内容：shareName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：SharedHost；  API声明：workgroupName: string;  差异内容：workgroupName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PpdInfo  差异内容：interface PpdInfo | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PpdInfo；  API声明：manufacturer: string;  差异内容：manufacturer: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PpdInfo；  API声明：nickName: string;  差异内容：nickName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PpdInfo；  API声明：ppdName: string;  差异内容：ppdName: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>;  差异内容：function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：enum WatermarkHandleResult  差异内容：enum WatermarkHandleResult | api/@ohos.print.d.ts |
| 新增API | NA | 类名：WatermarkHandleResult；  API声明：WATERMARK\_HANDLE\_SUCCESS = 0  差异内容：WATERMARK\_HANDLE\_SUCCESS = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：WatermarkHandleResult；  API声明：WATERMARK\_HANDLE\_FAILURE = 1  差异内容：WATERMARK\_HANDLE\_FAILURE = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：type WatermarkCallback = (jobId: string, fd: number) => void;  差异内容：type WatermarkCallback = (jobId: string, fd: number) => void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function registerWatermarkCallback(callback: WatermarkCallback): void;  差异内容：function registerWatermarkCallback(callback: WatermarkCallback): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function unregisterWatermarkCallback(callback?: WatermarkCallback): void;  差异内容：function unregisterWatermarkCallback(callback?: WatermarkCallback): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void;  差异内容：function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：settings；  API声明：function openBiometricsSettingsPage(context: Context): void;  差异内容：function openBiometricsSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings；  API声明：function openNfcSettingsPage(context: Context): void;  差异内容：function openNfcSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings；  API声明：function openDoubleClickSettingsPage(context: Context): void;  差异内容：function openDoubleClickSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings；  API声明：function isDoubleClickAppForSelf(): Promise<boolean>;  差异内容：function isDoubleClickAppForSelf(): Promise<boolean>; | api/@ohos.settings.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.selectionInput.SelectionExtensionAbility.d.ts  差异内容：BasicServicesKit | api/@ohos.selectionInput.SelectionExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.selectionInput.SelectionExtensionContext.d.ts  差异内容：BasicServicesKit | api/@ohos.selectionInput.SelectionExtensionContext.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.selectionInput.selectionManager.d.ts  差异内容：BasicServicesKit | api/@ohos.selectionInput.selectionManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.selectionInput.SelectionPanel.d.ts  差异内容：BasicServicesKit | api/@ohos.selectionInput.SelectionPanel.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.settingsLite.d.ts  差异内容：BasicServicesKit | api/@ohos.settingsLite.d.ts |
