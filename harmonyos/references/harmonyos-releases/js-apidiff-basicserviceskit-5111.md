---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-5111
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4e776005dbc0873db5b2e893529c788b907d73e475e3e38f6285252013542f18
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：CommonEventPublishData；  API声明：isSticky?: boolean;  差异内容：NA | 类名：CommonEventPublishData；  API声明：isSticky?: boolean;  差异内容：ohos.permission.COMMONEVENT\_STICKY | api/commonEvent/commonEventPublishData.d.ts |
| 权限变更 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS or ohos.permission.MANAGE\_SETTINGS | api/@ohos.settings.d.ts |
| 权限变更 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.MANAGE\_SETTINGS | api/@ohos.settings.d.ts |
| 权限变更 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string): Promise<boolean>;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string): Promise<boolean>;  差异内容：ohos.permission.MANAGE\_SETTINGS | api/@ohos.settings.d.ts |
| 权限变更 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：DEVICE\_SHARED, USER\_PROPERTY ohos.permission.MANAGE\_SETTINGS. or [USER\_SECURE] ohos.permission.MANAGE\_SECURE\_SETTINGS. | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS or ohos.permission.MANAGE\_SETTINGS | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace serialManager  差异内容：declare namespace serialManager | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function getPortList(): Readonly<SerialPort>[];  差异内容：function getPortList(): Readonly<SerialPort>[]; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function hasSerialRight(portId: number): boolean;  差异内容：function hasSerialRight(portId: number): boolean; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function requestSerialRight(portId: number): Promise<boolean>;  差异内容：function requestSerialRight(portId: number): Promise<boolean>; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function cancelSerialRight(portId: number): void;  差异内容：function cancelSerialRight(portId: number): void; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function open(portId: number): void;  差异内容：function open(portId: number): void; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function close(portId: number): void;  差异内容：function close(portId: number): void; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function getAttribute(portId: number): Readonly<SerialAttribute>;  差异内容：function getAttribute(portId: number): Readonly<SerialAttribute>; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function setAttribute(portId: number, attribute: SerialAttribute): void;  差异内容：function setAttribute(portId: number, attribute: SerialAttribute): void; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>;  差异内容：function read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function readSync(portId: number, buffer: Uint8Array, timeout?: number): number;  差异内容：function readSync(portId: number, buffer: Uint8Array, timeout?: number): number; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>;  差异内容：function write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：function writeSync(portId: number, buffer: Uint8Array, timeout?: number): number;  差异内容：function writeSync(portId: number, buffer: Uint8Array, timeout?: number): number; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：interface SerialPort  差异内容：interface SerialPort | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：portId: number;  差异内容：portId: number; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：SerialPort；  API声明：deviceName: string;  差异内容：deviceName: string; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：interface SerialAttribute  差异内容：interface SerialAttribute | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：SerialAttribute；  API声明：baudRate: BaudRates;  差异内容：baudRate: BaudRates; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：SerialAttribute；  API声明：dataBits?: DataBits;  差异内容：dataBits?: DataBits; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：SerialAttribute；  API声明：parity?: Parity;  差异内容：parity?: Parity; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：SerialAttribute；  API声明：stopBits?: StopBits;  差异内容：stopBits?: StopBits; | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：enum BaudRates  差异内容：enum BaudRates | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_50 = 50  差异内容：BAUDRATE\_50 = 50 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_75 = 75  差异内容：BAUDRATE\_75 = 75 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_110 = 110  差异内容：BAUDRATE\_110 = 110 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_134 = 134  差异内容：BAUDRATE\_134 = 134 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_150 = 150  差异内容：BAUDRATE\_150 = 150 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_200 = 200  差异内容：BAUDRATE\_200 = 200 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_300 = 300  差异内容：BAUDRATE\_300 = 300 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_600 = 600  差异内容：BAUDRATE\_600 = 600 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_1200 = 1200  差异内容：BAUDRATE\_1200 = 1200 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_1800 = 1800  差异内容：BAUDRATE\_1800 = 1800 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_2400 = 2400  差异内容：BAUDRATE\_2400 = 2400 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_4800 = 4800  差异内容：BAUDRATE\_4800 = 4800 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_9600 = 9600  差异内容：BAUDRATE\_9600 = 9600 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_19200 = 19200  差异内容：BAUDRATE\_19200 = 19200 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_38400 = 38400  差异内容：BAUDRATE\_38400 = 38400 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_57600 = 57600  差异内容：BAUDRATE\_57600 = 57600 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_115200 = 115200  差异内容：BAUDRATE\_115200 = 115200 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_230400 = 230400  差异内容：BAUDRATE\_230400 = 230400 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_460800 = 460800  差异内容：BAUDRATE\_460800 = 460800 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_500000 = 500000  差异内容：BAUDRATE\_500000 = 500000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_576000 = 576000  差异内容：BAUDRATE\_576000 = 576000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_921600 = 921600  差异内容：BAUDRATE\_921600 = 921600 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_1000000 = 1000000  差异内容：BAUDRATE\_1000000 = 1000000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_1152000 = 1152000  差异内容：BAUDRATE\_1152000 = 1152000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_1500000 = 1500000  差异内容：BAUDRATE\_1500000 = 1500000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_2000000 = 2000000  差异内容：BAUDRATE\_2000000 = 2000000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_2500000 = 2500000  差异内容：BAUDRATE\_2500000 = 2500000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_3000000 = 3000000  差异内容：BAUDRATE\_3000000 = 3000000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_3500000 = 3500000  差异内容：BAUDRATE\_3500000 = 3500000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：BaudRates；  API声明：BAUDRATE\_4000000 = 4000000  差异内容：BAUDRATE\_4000000 = 4000000 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：enum DataBits  差异内容：enum DataBits | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：DATABIT\_8 = 8  差异内容：DATABIT\_8 = 8 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：DATABIT\_7 = 7  差异内容：DATABIT\_7 = 7 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：DATABIT\_6 = 6  差异内容：DATABIT\_6 = 6 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：DataBits；  API声明：DATABIT\_5 = 5  差异内容：DATABIT\_5 = 5 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：enum Parity  差异内容：enum Parity | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：PARITY\_NONE = 0  差异内容：PARITY\_NONE = 0 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：PARITY\_ODD = 1  差异内容：PARITY\_ODD = 1 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：PARITY\_EVEN = 2  差异内容：PARITY\_EVEN = 2 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：PARITY\_MARK = 3  差异内容：PARITY\_MARK = 3 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：Parity；  API声明：PARITY\_SPACE = 4  差异内容：PARITY\_SPACE = 4 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：serialManager；  API声明：enum StopBits  差异内容：enum StopBits | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：StopBits；  API声明：STOPBIT\_1 = 0  差异内容：STOPBIT\_1 = 0 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：StopBits；  API声明：STOPBIT\_2 = 1  差异内容：STOPBIT\_2 = 1 | api/@ohos.usbManager.serial.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：export enum PerformanceClassLevel  差异内容：export enum PerformanceClassLevel | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：PerformanceClassLevel；  API声明：CLASS\_LEVEL\_HIGH  差异内容：CLASS\_LEVEL\_HIGH | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：PerformanceClassLevel；  API声明：CLASS\_LEVEL\_MEDIUM  差异内容：CLASS\_LEVEL\_MEDIUM | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：PerformanceClassLevel；  API声明：CLASS\_LEVEL\_LOW  差异内容：CLASS\_LEVEL\_LOW | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const performanceClass: PerformanceClassLevel;  差异内容：const performanceClass: PerformanceClassLevel; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：PrintJobSubState；  API声明：PRINT\_JOB\_BLOCK\_FILE\_UPLOADING\_ERROR = 30  差异内容：PRINT\_JOB\_BLOCK\_FILE\_UPLOADING\_ERROR = 30 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintErrorCode；  API声明：E\_PRINT\_TOO\_MANY\_FILES = 13100010  差异内容：E\_PRINT\_TOO\_MANY\_FILES = 13100010 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function getAddedPrinters(): Promise<Array<string>>;  差异内容：function getAddedPrinters(): Promise<Array<string>>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：interface PrinterPreferences  差异内容：interface PrinterPreferences | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultDuplexMode?: PrintDuplexMode;  差异内容：defaultDuplexMode?: PrintDuplexMode; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultPrintQuality?: PrintQuality;  差异内容：defaultPrintQuality?: PrintQuality; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultMediaType?: string;  差异内容：defaultMediaType?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultPageSizeId?: string;  差异内容：defaultPageSizeId?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：defaultOrientation?: PrintOrientationMode;  差异内容：defaultOrientation?: PrintOrientationMode; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：borderless?: boolean;  差异内容：borderless?: boolean; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterPreferences；  API声明：options?: string;  差异内容：options?: string; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：enum PrinterEvent  差异内容：enum PrinterEvent | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterEvent；  API声明：PRINTER\_EVENT\_ADDED = 0  差异内容：PRINTER\_EVENT\_ADDED = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterEvent；  API声明：PRINTER\_EVENT\_DELETED = 1  差异内容：PRINTER\_EVENT\_DELETED = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterEvent；  API声明：PRINTER\_EVENT\_STATE\_CHANGED = 2  差异内容：PRINTER\_EVENT\_STATE\_CHANGED = 2 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterEvent；  API声明：PRINTER\_EVENT\_INFO\_CHANGED = 3  差异内容：PRINTER\_EVENT\_INFO\_CHANGED = 3 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterEvent；  API声明：PRINTER\_EVENT\_PREFERENCE\_CHANGED = 4  差异内容：PRINTER\_EVENT\_PREFERENCE\_CHANGED = 4 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrinterEvent；  API声明：PRINTER\_EVENT\_LAST\_USED\_PRINTER\_CHANGED = 5  差异内容：PRINTER\_EVENT\_LAST\_USED\_PRINTER\_CHANGED = 5 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：enum DefaultPrinterType  差异内容：enum DefaultPrinterType | api/@ohos.print.d.ts |
| 新增API | NA | 类名：DefaultPrinterType；  API声明：DEFAULT\_PRINTER\_TYPE\_SET\_BY\_USER = 0  差异内容：DEFAULT\_PRINTER\_TYPE\_SET\_BY\_USER = 0 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：DefaultPrinterType；  API声明：DEFAULT\_PRINTER\_TYPE\_LAST\_USED\_PRINTER = 1  差异内容：DEFAULT\_PRINTER\_TYPE\_LAST\_USED\_PRINTER = 1 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void;  差异内容：type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function on(type: 'printerChange', callback: PrinterChangeCallback): void;  差异内容：function on(type: 'printerChange', callback: PrinterChangeCallback): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print；  API声明：function off(type: 'printerChange', callback?: PrinterChangeCallback): void;  差异内容：function off(type: 'printerChange', callback?: PrinterChangeCallback): void; | api/@ohos.print.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.usbManager.serial.d.ts  差异内容：BasicServicesKit | api/@ohos.usbManager.serial.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PrinterInformation；  API声明：preferences?: PrinterPreferences;  差异内容：preferences?: PrinterPreferences; | api/@ohos.print.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PrinterInformation；  API声明：alias?: string;  差异内容：alias?: string; | api/@ohos.print.d.ts |
