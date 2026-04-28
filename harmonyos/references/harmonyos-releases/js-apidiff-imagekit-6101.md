---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-6101
title: Image Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f34c1807dc9a56a07fc24d5318dcdcd0e7911be49f4b19895ec97c0262aeb856
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：image；  API声明：function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined;  差异内容：function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface ImageReceiverOptions  差异内容：interface ImageReceiverOptions | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageReceiverOptions；  API声明：size?: Size;  差异内容：size?: Size; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageReceiverOptions；  API声明：capacity?: number;  差异内容：capacity?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface ImageBufferData  差异内容：interface ImageBufferData | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageBufferData；  API声明：readonly rowStride: number[];  差异内容：readonly rowStride: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageBufferData；  API声明：readonly pixelStride: number[];  差异内容：readonly pixelStride: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageBufferData；  API声明：readonly byteBuffer: ArrayBuffer;  差异内容：readonly byteBuffer: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>;  差异内容：function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapFromSurfaceWithTransformationSync(surfaceId: string, transformEnabled: boolean): PixelMap;  差异内容：function createPixelMapFromSurfaceWithTransformationSync(surfaceId: string, transformEnabled: boolean): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface HdrComposeOptions  差异内容：interface HdrComposeOptions | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrComposeOptions；  API声明：desiredPixelFormat?: PixelMapFormat;  差异内容：desiredPixelFormat?: PixelMapFormat; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>;  差异内容：getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：HEIFS\_METADATA = 15  差异内容：HEIFS\_METADATA = 15 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Metadata；  API声明：getBlob(): Promise<ArrayBuffer>;  差异内容：getBlob(): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Metadata；  API声明：setBlob(blob: ArrayBuffer): Promise<void>;  差异内容：setBlob(blob: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum HeifsPropertyKey  差异内容：enum HeifsPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsPropertyKey；  API声明：HEIFS\_DELAY\_TIME = 'HeifsDelayTime'  差异内容：HEIFS\_DELAY\_TIME = 'HeifsDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class HeifsMetadata  差异内容：class HeifsMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：readonly heifsDelayTime?: number;  差异内容：readonly heifsDelayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：static createInstance(): HeifsMetadata;  差异内容：static createInstance(): HeifsMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：getProperties(key: Array<string>): Promise<Record<string, string | null>>;  差异内容：getProperties(key: Array<string>): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：setProperties(records: Record<string, string | null>): Promise<void>;  差异内容：setProperties(records: Record<string, string | null>): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：getAllProperties(): Promise<Record<string, string | null>>;  差异内容：getAllProperties(): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：clone(): Promise<HeifsMetadata>;  差异内容：clone(): Promise<HeifsMetadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：getBlob(): Promise<ArrayBuffer>;  差异内容：getBlob(): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：setBlob(blob: ArrayBuffer): Promise<void>;  差异内容：setBlob(blob: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum Orientation  差异内容：enum Orientation | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：TOP\_LEFT = 1  差异内容：TOP\_LEFT = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：TOP\_RIGHT = 2  差异内容：TOP\_RIGHT = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：BOTTOM\_RIGHT = 3  差异内容：BOTTOM\_RIGHT = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：BOTTOM\_LEFT = 4  差异内容：BOTTOM\_LEFT = 4 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：LEFT\_TOP = 5  差异内容：LEFT\_TOP = 5 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：RIGHT\_TOP = 6  差异内容：RIGHT\_TOP = 6 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：RIGHT\_BOTTOM = 7  差异内容：RIGHT\_BOTTOM = 7 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：LEFT\_BOTTOM = 8  差异内容：LEFT\_BOTTOM = 8 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class ExifMetadata  差异内容：class ExifMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：newSubfileType?: number;  差异内容：newSubfileType?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subfileType?: number;  差异内容：subfileType?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：imageWidth?: number;  差异内容：imageWidth?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：imageLength?: number;  差异内容：imageLength?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：bitsPerSample?: number[];  差异内容：bitsPerSample?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：compression?: number;  差异内容：compression?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：photometricInterpretation?: number;  差异内容：photometricInterpretation?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：imageDescription?: string;  差异内容：imageDescription?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：make?: string;  差异内容：make?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：model?: string;  差异内容：model?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：stripOffsets?: number[];  差异内容：stripOffsets?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：orientation?: Orientation;  差异内容：orientation?: Orientation; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：samplesPerPixel?: number;  差异内容：samplesPerPixel?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：rowsPerStrip?: number;  差异内容：rowsPerStrip?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：stripByteCounts?: number[];  差异内容：stripByteCounts?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：xResolution?: number;  差异内容：xResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：yResolution?: number;  差异内容：yResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：planarConfiguration?: number;  差异内容：planarConfiguration?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：resolutionUnit?: number;  差异内容：resolutionUnit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：transferFunction?: string;  差异内容：transferFunction?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：software?: string;  差异内容：software?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：dateTime?: string;  差异内容：dateTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：artist?: string;  差异内容：artist?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：whitePoint?: number[];  差异内容：whitePoint?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：primaryChromaticities?: number[];  差异内容：primaryChromaticities?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：photoMode?: number;  差异内容：photoMode?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：jpegInterchangeFormat?: number;  差异内容：jpegInterchangeFormat?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：jpegInterchangeFormatLength?: number;  差异内容：jpegInterchangeFormatLength?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：yCbCrCoefficients?: number[];  差异内容：yCbCrCoefficients?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：yCbCrSubSampling?: number[];  差异内容：yCbCrSubSampling?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：yCbCrPositioning?: number;  差异内容：yCbCrPositioning?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：referenceBlackWhite?: number[];  差异内容：referenceBlackWhite?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：copyright?: string;  差异内容：copyright?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：exposureTime?: number;  差异内容：exposureTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：fNumber?: number;  差异内容：fNumber?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：exposureProgram?: number;  差异内容：exposureProgram?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：spectralSensitivity?: string;  差异内容：spectralSensitivity?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsVersionID?: number[];  差异内容：gpsVersionID?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsLatitudeRef?: string;  差异内容：gpsLatitudeRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsLatitude?: number[];  差异内容：gpsLatitude?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsLongitudeRef?: string;  差异内容：gpsLongitudeRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsLongitude?: number[];  差异内容：gpsLongitude?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsAltitudeRef?: number;  差异内容：gpsAltitudeRef?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsAltitude?: number;  差异内容：gpsAltitude?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsTimestamp?: number[];  差异内容：gpsTimestamp?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsSatellites?: string;  差异内容：gpsSatellites?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsStatus?: string;  差异内容：gpsStatus?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsMeasureMode?: string;  差异内容：gpsMeasureMode?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDop?: number;  差异内容：gpsDop?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsSpeedRef?: string;  差异内容：gpsSpeedRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsSpeed?: number;  差异内容：gpsSpeed?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsTrackRef?: string;  差异内容：gpsTrackRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsTrack?: number;  差异内容：gpsTrack?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsImgDirectionRef?: string;  差异内容：gpsImgDirectionRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsImgDirection?: number;  差异内容：gpsImgDirection?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsMapDatum?: string;  差异内容：gpsMapDatum?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestLatitudeRef?: string;  差异内容：gpsDestLatitudeRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestLatitude?: number[];  差异内容：gpsDestLatitude?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestLongitudeRef?: string;  差异内容：gpsDestLongitudeRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestLongitude?: number[];  差异内容：gpsDestLongitude?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestBearingRef?: string;  差异内容：gpsDestBearingRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestBearing?: number;  差异内容：gpsDestBearing?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestDistanceRef?: string;  差异内容：gpsDestDistanceRef?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDestDistance?: number;  差异内容：gpsDestDistance?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsProcessingMethod?: string;  差异内容：gpsProcessingMethod?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsAreaInformation?: string;  差异内容：gpsAreaInformation?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDateStamp?: string;  差异内容：gpsDateStamp?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsDifferential?: number;  差异内容：gpsDifferential?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gpsHPositioningError?: number;  差异内容：gpsHPositioningError?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：isoSpeedRatings?: number;  差异内容：isoSpeedRatings?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：photographicSensitivity?: number[];  差异内容：photographicSensitivity?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：oecf?: ArrayBuffer;  差异内容：oecf?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sensitivityType?: number;  差异内容：sensitivityType?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：standardOutputSensitivity?: number;  差异内容：standardOutputSensitivity?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：recommendedExposureIndex?: number;  差异内容：recommendedExposureIndex?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：isoSpeedLatitudeyyy?: number;  差异内容：isoSpeedLatitudeyyy?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：isoSpeedLatitudezzz?: number;  差异内容：isoSpeedLatitudezzz?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：exifVersion?: string;  差异内容：exifVersion?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：dateTimeOriginal?: string;  差异内容：dateTimeOriginal?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：dateTimeDigitized?: string;  差异内容：dateTimeDigitized?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：offsetTime?: string;  差异内容：offsetTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：offsetTimeOriginal?: string;  差异内容：offsetTimeOriginal?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：offsetTimeDigitized?: string;  差异内容：offsetTimeDigitized?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：componentsConfiguration?: string;  差异内容：componentsConfiguration?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：compressedBitsPerPixel?: number;  差异内容：compressedBitsPerPixel?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：shutterSpeedValue?: number;  差异内容：shutterSpeedValue?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：apertureValue?: number;  差异内容：apertureValue?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：brightnessValue?: number;  差异内容：brightnessValue?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：exposureBiasValue?: number;  差异内容：exposureBiasValue?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：maxApertureValue?: number;  差异内容：maxApertureValue?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subjectDistance?: number;  差异内容：subjectDistance?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：meteringMode?: number;  差异内容：meteringMode?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：lightSource?: number;  差异内容：lightSource?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：flash?: number;  差异内容：flash?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：focalLength?: number;  差异内容：focalLength?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subjectArea?: number[];  差异内容：subjectArea?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：makerNote?: ArrayBuffer;  差异内容：makerNote?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：userComment?: string;  差异内容：userComment?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subsecTime?: string;  差异内容：subsecTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subsecTimeOriginal?: string;  差异内容：subsecTimeOriginal?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subsecTimeDigitized?: string;  差异内容：subsecTimeDigitized?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：flashpixVersion?: string;  差异内容：flashpixVersion?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：colorSpace?: number;  差异内容：colorSpace?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：pixelXDimension?: number;  差异内容：pixelXDimension?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：pixelYDimension?: number;  差异内容：pixelYDimension?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：relatedSoundFile?: string;  差异内容：relatedSoundFile?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：flashEnergy?: number;  差异内容：flashEnergy?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：spatialFrequencyResponse?: ArrayBuffer;  差异内容：spatialFrequencyResponse?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：focalPlaneXResolution?: number;  差异内容：focalPlaneXResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：focalPlaneYResolution?: number;  差异内容：focalPlaneYResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：focalPlaneResolutionUnit?: number;  差异内容：focalPlaneResolutionUnit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subjectLocation?: number[];  差异内容：subjectLocation?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：exposureIndex?: number;  差异内容：exposureIndex?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sensingMethod?: number;  差异内容：sensingMethod?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：fileSource?: ArrayBuffer;  差异内容：fileSource?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sceneType?: ArrayBuffer;  差异内容：sceneType?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：cfaPattern?: ArrayBuffer;  差异内容：cfaPattern?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：customRendered?: number;  差异内容：customRendered?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：exposureMode?: number;  差异内容：exposureMode?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：whiteBalance?: number;  差异内容：whiteBalance?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：digitalZoomRatio?: number;  差异内容：digitalZoomRatio?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：focalLengthIn35mmFilm?: number;  差异内容：focalLengthIn35mmFilm?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sceneCaptureType?: number;  差异内容：sceneCaptureType?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gainControl?: number;  差异内容：gainControl?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：contrast?: number;  差异内容：contrast?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：saturation?: number;  差异内容：saturation?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sharpness?: number;  差异内容：sharpness?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：deviceSettingDescription?: ArrayBuffer;  差异内容：deviceSettingDescription?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：subjectDistanceRange?: number;  差异内容：subjectDistanceRange?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：imageUniqueId?: string;  差异内容：imageUniqueId?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：cameraOwnerName?: string;  差异内容：cameraOwnerName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：bodySerialNumber?: string;  差异内容：bodySerialNumber?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：lensSpecification?: number[];  差异内容：lensSpecification?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：lensMake?: string;  差异内容：lensMake?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：lensModel?: string;  差异内容：lensModel?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：lensSerialNumber?: string;  差异内容：lensSerialNumber?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：compositeImage?: number;  差异内容：compositeImage?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sourceImageNumberOfCompositeImage?: number[];  差异内容：sourceImageNumberOfCompositeImage?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：sourceExposureTimesOfCompositeImage?: ArrayBuffer;  差异内容：sourceExposureTimesOfCompositeImage?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：gamma?: number;  差异内容：gamma?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：static createInstance(): ExifMetadata;  差异内容：static createInstance(): ExifMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：getProperties(key: Array<string>): Promise<Record<string, string | null>>;  差异内容：getProperties(key: Array<string>): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：setProperties(records: Record<string, string | null>): Promise<void>;  差异内容：setProperties(records: Record<string, string | null>): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：getAllProperties(): Promise<Record<string, string | null>>;  差异内容：getAllProperties(): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：clone(): Promise<ExifMetadata>;  差异内容：clone(): Promise<ExifMetadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：getBlob(): Promise<ArrayBuffer>;  差异内容：getBlob(): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ExifMetadata；  API声明：setBlob(blob: ArrayBuffer): Promise<void>;  差异内容：setBlob(blob: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM: number = 9;  差异内容：const XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM: number = 9; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const XMAGE\_WATERMARK\_MODE\_BORDER: number = 10;  差异内容：const XMAGE\_WATERMARK\_MODE\_BORDER: number = 10; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_PROFESSIONAL: number = 2;  差异内容：const CAPTURE\_MODE\_PROFESSIONAL: number = 2; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW: number = 7;  差异内容：const CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW: number = 7; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_PANORAMA: number = 8;  差异内容：const CAPTURE\_MODE\_PANORAMA: number = 8; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_TAIL\_LIGHT: number = 9;  差异内容：const CAPTURE\_MODE\_TAIL\_LIGHT: number = 9; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_LIGHT\_GRAFFITI: number = 10;  差异内容：const CAPTURE\_MODE\_LIGHT\_GRAFFITI: number = 10; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_SILKY\_WATER: number = 11;  差异内容：const CAPTURE\_MODE\_SILKY\_WATER: number = 11; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_STAR\_TRACK: number = 12;  差异内容：const CAPTURE\_MODE\_STAR\_TRACK: number = 12; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_WIDEAPERTURE: number = 19;  差异内容：const CAPTURE\_MODE\_WIDEAPERTURE: number = 19; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_MOVING\_PHOTO: number = 20;  差异内容：const CAPTURE\_MODE\_MOVING\_PHOTO: number = 20; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_PORTRAIT: number = 23;  差异内容：const CAPTURE\_MODE\_PORTRAIT: number = 23; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW: number = 42;  差异内容：const CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW: number = 42; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_SUPER\_MACRO: number = 47;  差异内容：const CAPTURE\_MODE\_SUPER\_MACRO: number = 47; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_SNAP\_SHOT: number = 62;  差异内容：const CAPTURE\_MODE\_SNAP\_SHOT: number = 62; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum FocusMode  差异内容：enum FocusMode | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FocusMode；  API声明：AF\_A = 0  差异内容：AF\_A = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FocusMode；  API声明：AF\_S = 1  差异内容：AF\_S = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FocusMode；  API声明：AF\_C = 2  差异内容：AF\_C = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：FocusMode；  API声明：MF = 3  差异内容：MF = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum XmageColorMode  差异内容：enum XmageColorMode | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XmageColorMode；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XmageColorMode；  API声明：BRIGHT = 1  差异内容：BRIGHT = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XmageColorMode；  API声明：SOFT = 2  差异内容：SOFT = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XmageColorMode；  API声明：MONO = 3  差异内容：MONO = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class MakerNoteHuaweiMetadata  差异内容：class MakerNoteHuaweiMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：isXmageSupported?: boolean;  差异内容：isXmageSupported?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：xmageWatermarkMode?: number;  差异内容：xmageWatermarkMode?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：xmageLeft?: number;  差异内容：xmageLeft?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：xmageTop?: number;  差异内容：xmageTop?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：xmageRight?: number;  差异内容：xmageRight?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：xmageBottom?: number;  差异内容：xmageBottom?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：xmageColorMode?: XmageColorMode;  差异内容：xmageColorMode?: XmageColorMode; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：isCloudEnhanced?: boolean;  差异内容：isCloudEnhanced?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：cloudLabel?: string;  差异内容：cloudLabel?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：isWindSnapshot?: boolean;  差异内容：isWindSnapshot?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneVersion?: number;  差异内容：sceneVersion?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneFoodConfidence?: number;  差异内容：sceneFoodConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneStageConfidence?: number;  差异内容：sceneStageConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneBlueSkyConfidence?: number;  差异内容：sceneBlueSkyConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneGreenPlantConfidence?: number;  差异内容：sceneGreenPlantConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneBeachConfidence?: number;  差异内容：sceneBeachConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneSnowConfidence?: number;  差异内容：sceneSnowConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneSunsetConfidence?: number;  差异内容：sceneSunsetConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneFlowersConfidence?: number;  差异内容：sceneFlowersConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneNightConfidence?: number;  差异内容：sceneNightConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：sceneTextConfidence?: number;  差异内容：sceneTextConfidence?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：faceCount?: number;  差异内容：faceCount?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：faceConfidences?: number[];  差异内容：faceConfidences?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：faceSmileScores?: number[];  差异内容：faceSmileScores?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：captureMode?: number;  差异内容：captureMode?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：burstNumber?: number;  差异内容：burstNumber?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：isFrontCamera?: boolean;  差异内容：isFrontCamera?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：rollAngle?: number;  差异内容：rollAngle?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：pitchAngle?: number;  差异内容：pitchAngle?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：physicalAperture?: number;  差异内容：physicalAperture?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：focusMode?: FocusMode;  差异内容：focusMode?: FocusMode; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：static createInstance(): MakerNoteHuaweiMetadata;  差异内容：static createInstance(): MakerNoteHuaweiMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：getProperties(key: Array<string>): Promise<Record<string, string | null>>;  差异内容：getProperties(key: Array<string>): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：setProperties(records: Record<string, string | null>): Promise<void>;  差异内容：setProperties(records: Record<string, string | null>): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：getAllProperties(): Promise<Record<string, string | null>>;  差异内容：getAllProperties(): Promise<Record<string, string | null>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：clone(): Promise<MakerNoteHuaweiMetadata>;  差异内容：clone(): Promise<MakerNoteHuaweiMetadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：getBlob(): Promise<ArrayBuffer>;  差异内容：getBlob(): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MakerNoteHuaweiMetadata；  API声明：setBlob(blob: ArrayBuffer): Promise<void>;  差异内容：setBlob(blob: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface ImageMetadata  差异内容：interface ImageMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：exifMetadata?: ExifMetadata;  差异内容：exifMetadata?: ExifMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：makerNoteHuaweiMetadata?: MakerNoteHuaweiMetadata;  差异内容：makerNoteHuaweiMetadata?: MakerNoteHuaweiMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：heifsMetadata?: HeifsMetadata;  差异内容：heifsMetadata?: HeifsMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>;  差异内容：readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>;  差异内容：writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Image；  API声明：readonly colorSpace: colorSpaceManager.ColorSpace;  差异内容：readonly colorSpace: colorSpaceManager.ColorSpace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Image；  API声明：getBufferData(): ImageBufferData | null;  差异内容：getBufferData(): ImageBufferData | null; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Image；  API声明：getMetadata(key: HdrMetadataKey): HdrMetadataValue | null;  差异内容：getMetadata(key: HdrMetadataKey): HdrMetadataValue | null; | api/@ohos.multimedia.image.d.ts |
