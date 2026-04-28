---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-b105
title: Image Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:04+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5f4ec606b866ef76539cb7fdaddf8524f276a283330b51ba19aba9ae6933da3f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ImagePacker；  API声明：packing(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>;  差异内容：packing(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>;  差异内容：packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packToFile(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>;  差异内容：packToFile(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>;  差异内容：packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface PackingOptionsForSequence  差异内容： interface PackingOptionsForSequence | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：frameCount: number;  差异内容：frameCount: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：delayTimeList: Array<number>;  差异内容：delayTimeList: Array<number>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：disposalTypes?: Array<number>;  差异内容：disposalTypes?: Array<number>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：loopCount?: number;  差异内容：loopCount?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：setMemoryNameSync(name: string): void;  差异内容：setMemoryNameSync(name: string): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface Picture  差异内容： interface Picture | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：getMainPixelmap(): PixelMap;  差异内容：getMainPixelmap(): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：getHdrComposedPixelmap(): Promise<PixelMap>;  差异内容：getHdrComposedPixelmap(): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：getGainmapPixelmap(): PixelMap | null;  差异内容：getGainmapPixelmap(): PixelMap | null; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void;  差异内容：setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null;  差异内容：getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>;  差异内容：setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：getMetadata(metadataType: MetadataType): Promise<Metadata>;  差异内容：getMetadata(metadataType: MetadataType): Promise<Metadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：marshalling(sequence: rpc.MessageSequence): void;  差异内容：marshalling(sequence: rpc.MessageSequence): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：release(): void;  差异内容：release(): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPicture(mainPixelmap: PixelMap): Picture;  差异内容：function createPicture(mainPixelmap: PixelMap): Picture; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPictureFromParcel(sequence: rpc.MessageSequence): Picture;  差异内容：function createPictureFromParcel(sequence: rpc.MessageSequence): Picture; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture;  差异内容：function createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface AuxiliaryPicture  差异内容： interface AuxiliaryPicture | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：writePixelsFromBuffer(data: ArrayBuffer): Promise<void>;  差异内容：writePixelsFromBuffer(data: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：readPixelsToBuffer(): Promise<ArrayBuffer>;  差异内容：readPixelsToBuffer(): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：getType(): AuxiliaryPictureType;  差异内容：getType(): AuxiliaryPictureType; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>;  差异内容：setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：getMetadata(metadataType: MetadataType): Promise<Metadata>;  差异内容：getMetadata(metadataType: MetadataType): Promise<Metadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：getAuxiliaryPictureInfo(): AuxiliaryPictureInfo;  差异内容：getAuxiliaryPictureInfo(): AuxiliaryPictureInfo; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void;  差异内容：setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：release(): void;  差异内容：release(): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： enum AuxiliaryPictureType  差异内容： enum AuxiliaryPictureType | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：GAINMAP = 1  差异内容：GAINMAP = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：DEPTH\_MAP = 2  差异内容：DEPTH\_MAP = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：UNREFOCUS\_MAP = 3  差异内容：UNREFOCUS\_MAP = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：LINEAR\_MAP = 4  差异内容：LINEAR\_MAP = 4 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：FRAGMENT\_MAP = 5  差异内容：FRAGMENT\_MAP = 5 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： enum MetadataType  差异内容： enum MetadataType | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：EXIF\_METADATA = 1  差异内容：EXIF\_METADATA = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：FRAGMENT\_METADATA = 2  差异内容：FRAGMENT\_METADATA = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface Metadata  差异内容： interface Metadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Metadata；  API声明：getProperties(key: Array<string>): Promise<Record<string, string | null>>;  差异内容：getProperties(key: Array<string>): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Metadata；  API声明：setProperties(records: Record<string, string | null>): Promise<void>;  差异内容：setProperties(records: Record<string, string | null>): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Metadata；  API声明：getAllProperties(): Promise<Record<string, string | null>>;  差异内容：getAllProperties(): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Metadata；  API声明：clone(): Promise<Metadata>;  差异内容：clone(): Promise<Metadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： enum FragmentMapPropertyKey  差异内容： enum FragmentMapPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FragmentMapPropertyKey；  API声明：X\_IN\_ORIGINAL = 'XInOriginal'  差异内容：X\_IN\_ORIGINAL = 'XInOriginal' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FragmentMapPropertyKey；  API声明：Y\_IN\_ORIGINAL = 'YInOriginal'  差异内容：Y\_IN\_ORIGINAL = 'YInOriginal' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FragmentMapPropertyKey；  API声明：WIDTH = 'FragmentImageWidth'  差异内容：WIDTH = 'FragmentImageWidth' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FragmentMapPropertyKey；  API声明：HEIGHT = 'FragmentImageHeight'  差异内容：HEIGHT = 'FragmentImageHeight' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface DecodingOptionsForPicture  差异内容： interface DecodingOptionsForPicture | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForPicture；  API声明：desiredAuxiliaryPictures: Array<AuxiliaryPictureType>;  差异内容：desiredAuxiliaryPictures: Array<AuxiliaryPictureType>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface AuxiliaryPictureInfo  差异内容： interface AuxiliaryPictureInfo | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureInfo；  API声明：auxiliaryPictureType: AuxiliaryPictureType;  差异内容：auxiliaryPictureType: AuxiliaryPictureType; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureInfo；  API声明：size: Size;  差异内容：size: Size; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureInfo；  API声明：rowStride: number;  差异内容：rowStride: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureInfo；  API声明：pixelFormat: PixelMapFormat;  差异内容：pixelFormat: PixelMapFormat; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureInfo；  API声明：colorSpace: colorSpaceManager.ColorSpaceManager;  差异内容：colorSpace: colorSpaceManager.ColorSpaceManager; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：createPicture(options?: DecodingOptionsForPicture): Promise<Picture>;  差异内容：createPicture(options?: DecodingOptionsForPicture): Promise<Picture>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageReceiver；  API声明：off(type: 'imageArrival', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'imageArrival', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageCreator；  API声明：off(type: 'imageRelease', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'imageRelease', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.image.d.ts |
