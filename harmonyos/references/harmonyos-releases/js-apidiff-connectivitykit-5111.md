---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-5111
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1f0a7b75d74798c7e5754859c0d3fe977ea3eff946e15b9f1f65b8bcfc453be2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：socket；  API声明：function sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>;  差异内容：401 | 类名：socket；  API声明：function sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>;  差异内容：NA | api/@ohos.bluetooth.socket.d.ts |
| 删除错误码 | 类名：socket；  API声明：function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>;  差异内容：401 | 类名：socket；  API声明：function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>;  差异内容：NA | api/@ohos.bluetooth.socket.d.ts |
| 删除错误码 | 类名：HceService；  API声明：off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void;  差异内容：401 | 类名：HceService；  API声明：off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void;  差异内容：NA | api/@ohos.nfc.cardEmulation.d.ts |
| 删除错误码 | 类名：omapi；  API声明：function on(type: 'stateChanged', callback: Callback<ServiceState>): void;  差异内容：401 | 类名：omapi；  API声明：function on(type: 'stateChanged', callback: Callback<ServiceState>): void;  差异内容：NA | api/@ohos.secureElement.d.ts |
| 删除错误码 | 类名：omapi；  API声明：function off(type: 'stateChanged', callback?: Callback<ServiceState>): void;  差异内容：401 | 类名：omapi；  API声明：function off(type: 'stateChanged', callback?: Callback<ServiceState>): void;  差异内容：NA | api/@ohos.secureElement.d.ts |
| 删除错误码 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(): Promise<boolean>;  差异内容：3100205 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(): Promise<boolean>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：NdefTag；  API声明：readNdef(): Promise<NdefMessage>;  差异内容：3100205 | 类名：NdefTag；  API声明：readNdef(): Promise<NdefMessage>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage): Promise<void>;  差异内容：3100205 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：NdefTag；  API声明：setReadOnly(): Promise<void>;  差异内容：3100205 | 类名：NdefTag；  API声明：setReadOnly(): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number): Promise<number[]>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number): Promise<number[]>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[]): Promise<void>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[]): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number): Promise<void>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number): Promise<void>;  差异内容：3100205 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number): Promise<number[]>;  差异内容：3100205 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number): Promise<number[]>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[]): Promise<void>;  差异内容：3100205 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[]): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage): Promise<void>;  差异内容：3100205 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage): Promise<void>;  差异内容：3100205 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage): Promise<void>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：BarcodeTag；  API声明：getBarcode(): Promise<ArrayBuffer>;  差异内容：3100205 | 类名：BarcodeTag；  API声明：getBarcode(): Promise<ArrayBuffer>;  差异内容：NA | api/tag/nfctech.d.ts |
| 删除错误码 | 类名：TagSession；  API声明：transmit(data: number[]): Promise<number[]>;  差异内容：3100205 | 类名：TagSession；  API声明：transmit(data: number[]): Promise<number[]>;  差异内容：NA | api/tag/tagSession.d.ts |
| 新增API | NA | 类名：a2dp；  API声明：interface CodecInfoList  差异内容：interface CodecInfoList | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfoList；  API声明：codecType: CodecType;  差异内容：codecType: CodecType; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfoList；  API声明：codecBitsPerSampleArray: CodecBitsPerSample[];  差异内容：codecBitsPerSampleArray: CodecBitsPerSample[]; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfoList；  API声明：codecChannelModeArray: CodecChannelMode[];  差异内容：codecChannelModeArray: CodecChannelMode[]; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfoList；  API声明：codecSampleRateArray: CodecSampleRate[];  差异内容：codecSampleRateArray: CodecSampleRate[]; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfoList；  API声明：codecBitRateArray: CodecBitRate[];  差异内容：codecBitRateArray: CodecBitRate[]; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfoList；  API声明：codecFrameLengthArray: CodecFrameLength[];  差异内容：codecFrameLengthArray: CodecFrameLength[]; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明：enum CodecBitRate  差异内容：enum CodecBitRate | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_96000 = 0  差异内容：CODEC\_BIT\_RATE\_96000 = 0 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_128000 = 1  差异内容：CODEC\_BIT\_RATE\_128000 = 1 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_192000 = 2  差异内容：CODEC\_BIT\_RATE\_192000 = 2 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_256000 = 3  差异内容：CODEC\_BIT\_RATE\_256000 = 3 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_320000 = 4  差异内容：CODEC\_BIT\_RATE\_320000 = 4 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_480000 = 5  差异内容：CODEC\_BIT\_RATE\_480000 = 5 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_640000 = 6  差异内容：CODEC\_BIT\_RATE\_640000 = 6 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_960000 = 7  差异内容：CODEC\_BIT\_RATE\_960000 = 7 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitRate；  API声明：CODEC\_BIT\_RATE\_ABR = 8  差异内容：CODEC\_BIT\_RATE\_ABR = 8 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明：enum CodecFrameLength  差异内容：enum CodecFrameLength | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecFrameLength；  API声明：CODEC\_FRAME\_LENGTH\_5MS = 0  差异内容：CODEC\_FRAME\_LENGTH\_5MS = 0 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecFrameLength；  API声明：CODEC\_FRAME\_LENGTH\_10MS = 1  差异内容：CODEC\_FRAME\_LENGTH\_10MS = 1 | api/@ohos.bluetooth.a2dp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CodecInfo；  API声明：codecBitRate?: CodecBitRate;  差异内容：codecBitRate?: CodecBitRate; | api/@ohos.bluetooth.a2dp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CodecInfo；  API声明：codecFrameLength?: CodecFrameLength;  差异内容：codecFrameLength?: CodecFrameLength; | api/@ohos.bluetooth.a2dp.d.ts |
