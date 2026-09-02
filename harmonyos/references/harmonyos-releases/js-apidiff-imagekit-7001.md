---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-7001
title: Image Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:cf1f5730a78b2ff46f449b5796fa89f4e9c429a38d52da37bbe0da8fe9e2fda8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PixelMapFormat；  API声明：ALPHA\_U8 = 15  差异内容：ALPHA\_U8 = 15 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOption；  API声明：maxEmbedThumbnailDimension?: number;  差异内容：maxEmbedThumbnailDimension?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapFromPixels(pixels: ArrayBuffer, param: InitializationOptions): Promise<PixelMap>;  差异内容：function createPixelMapFromPixels(pixels: ArrayBuffer, param: InitializationOptions): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap;  差异内容：function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createEmptyPixelMap(param: InitializationOptions): PixelMap;  差异内容：function createEmptyPixelMap(param: InitializationOptions): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>;  差异内容：readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：readAllPixelsToBufferSync(dst: ArrayBuffer): void;  差异内容：readAllPixelsToBufferSync(dst: ArrayBuffer): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：readPixelsToArea(area: PositionArea): Promise<void>;  差异内容：readPixelsToArea(area: PositionArea): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：readPixelsToAreaSync(area: PositionArea): void;  差异内容：readPixelsToAreaSync(area: PositionArea): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：writePixelsFromArea(area: PositionArea): Promise<void>;  差异内容：writePixelsFromArea(area: PositionArea): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：writePixelsFromAreaSync(area: PositionArea): void;  差异内容：writePixelsFromAreaSync(area: PositionArea): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>;  差异内容：writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：writeAllPixelsFromBufferSync(src: ArrayBuffer): void;  差异内容：writeAllPixelsFromBufferSync(src: ArrayBuffer): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：setOpacity(value: number): Promise<void>;  差异内容：setOpacity(value: number): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：setOpacitySync(value: number): void;  差异内容：setOpacitySync(value: number): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：extractAlphaPixelMap(): Promise<PixelMap>;  差异内容：extractAlphaPixelMap(): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：extractAlphaPixelMapSync(): PixelMap;  差异内容：extractAlphaPixelMapSync(): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyScale(x: number, y: number, level?: AntiAliasingLevel): Promise<void>;  差异内容：applyScale(x: number, y: number, level?: AntiAliasingLevel): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyScaleSync(x: number, y: number, level?: AntiAliasingLevel): void;  差异内容：applyScaleSync(x: number, y: number, level?: AntiAliasingLevel): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyTranslate(x: number, y: number): Promise<void>;  差异内容：applyTranslate(x: number, y: number): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyTranslateSync(x: number, y: number): void;  差异内容：applyTranslateSync(x: number, y: number): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyRotate(angle: number): Promise<void>;  差异内容：applyRotate(angle: number): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyRotateSync(angle: number): void;  差异内容：applyRotateSync(angle: number): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyFlip(horizontal: boolean, vertical: boolean): Promise<void>;  差异内容：applyFlip(horizontal: boolean, vertical: boolean): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyFlipSync(horizontal: boolean, vertical: boolean): void;  差异内容：applyFlipSync(horizontal: boolean, vertical: boolean): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyCrop(region: Region): Promise<void>;  差异内容：applyCrop(region: Region): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：applyCropSync(region: Region): void;  差异内容：applyCropSync(region: Region): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：PNG\_METADATA = 19  差异内容：PNG\_METADATA = 19 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：JFIF\_METADATA = 20  差异内容：JFIF\_METADATA = 20 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：TIFF\_METADATA = 21  差异内容：TIFF\_METADATA = 21 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：XMP\_METADATA = 22  差异内容：XMP\_METADATA = 22 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：AVIS\_METADATA = 23  差异内容：AVIS\_METADATA = 23 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey；  API声明：GIF\_HAS\_GLOBAL\_COLOR\_MAP = 'GifHasGlobalColorMap'  差异内容：GIF\_HAS\_GLOBAL\_COLOR\_MAP = 'GifHasGlobalColorMap' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey；  API声明：GIF\_CANVAS\_WIDTH = 'GifCanvasWidth'  差异内容：GIF\_CANVAS\_WIDTH = 'GifCanvasWidth' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey；  API声明：GIF\_CANVAS\_HEIGHT = 'GifCanvasHeight'  差异内容：GIF\_CANVAS\_HEIGHT = 'GifCanvasHeight' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey；  API声明：GIF\_LOOP\_COUNT = 'GifLoopCount'  差异内容：GIF\_LOOP\_COUNT = 'GifLoopCount' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey；  API声明：GIF\_UNCLAMPED\_DELAY\_TIME = 'GifUnclampedDelayTime'  差异内容：GIF\_UNCLAMPED\_DELAY\_TIME = 'GifUnclampedDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsPropertyKey；  API声明：HEIFS\_UNCLAMPED\_DELAY\_TIME = 'HeifsUnclampedDelayTime'  差异内容：HEIFS\_UNCLAMPED\_DELAY\_TIME = 'HeifsUnclampedDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsPropertyKey；  API声明：HEIFS\_CANVAS\_HEIGHT = 'HeifsCanvasHeight'  差异内容：HEIFS\_CANVAS\_HEIGHT = 'HeifsCanvasHeight' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsPropertyKey；  API声明：HEIFS\_CANVAS\_WIDTH = 'HeifsCanvasWidth'  差异内容：HEIFS\_CANVAS\_WIDTH = 'HeifsCanvasWidth' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum TiffPropertyKey  差异内容：enum TiffPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：DOCUMENT\_NAME = 'TiffDocumentName'  差异内容：DOCUMENT\_NAME = 'TiffDocumentName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：PHOTOMETRIC\_INTERPRETATION = 'TiffPhotometricInterpretation'  差异内容：PHOTOMETRIC\_INTERPRETATION = 'TiffPhotometricInterpretation' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：ORIENTATION = 'TiffOrientation'  差异内容：ORIENTATION = 'TiffOrientation' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：RESOLUTION\_UNIT = 'TiffResolutionUnit'  差异内容：RESOLUTION\_UNIT = 'TiffResolutionUnit' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：COPYRIGHT = 'TiffCopyright'  差异内容：COPYRIGHT = 'TiffCopyright' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：DATE\_TIME = 'TiffDateTime'  差异内容：DATE\_TIME = 'TiffDateTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：IMAGE\_DESCRIPTION = 'TiffImageDescription'  差异内容：IMAGE\_DESCRIPTION = 'TiffImageDescription' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：Y\_RESOLUTION = 'TiffYResolution'  差异内容：Y\_RESOLUTION = 'TiffYResolution' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：X\_RESOLUTION = 'TiffXResolution'  差异内容：X\_RESOLUTION = 'TiffXResolution' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：WHITE\_POINT = 'TiffWhitePoint'  差异内容：WHITE\_POINT = 'TiffWhitePoint' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：TILE\_LENGTH = 'TiffTileLength'  差异内容：TILE\_LENGTH = 'TiffTileLength' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：TRANSFER\_FUNCTION = 'TiffTransferFunction'  差异内容：TRANSFER\_FUNCTION = 'TiffTransferFunction' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：TILE\_WIDTH = 'TiffTileWidth'  差异内容：TILE\_WIDTH = 'TiffTileWidth' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：MAKE = 'TiffMake'  差异内容：MAKE = 'TiffMake' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：MODEL = 'TiffModel'  差异内容：MODEL = 'TiffModel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：HOST\_COMPUTER = 'TiffHostComputer'  差异内容：HOST\_COMPUTER = 'TiffHostComputer' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：COMPRESSION = 'TiffCompression'  差异内容：COMPRESSION = 'TiffCompression' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：SOFTWARE = 'TiffSoftware'  差异内容：SOFTWARE = 'TiffSoftware' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：PRIMARY\_CHROMATICITIES = 'TiffPrimaryChromaticities'  差异内容：PRIMARY\_CHROMATICITIES = 'TiffPrimaryChromaticities' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffPropertyKey；  API声明：ARTIST = 'TiffArtist'  差异内容：ARTIST = 'TiffArtist' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum JfifPropertyKey  差异内容：enum JfifPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifPropertyKey；  API声明：DENSITY\_UNIT = 'JfifDensityUnit'  差异内容：DENSITY\_UNIT = 'JfifDensityUnit' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifPropertyKey；  API声明：X\_DENSITY = 'JfifXDensity'  差异内容：X\_DENSITY = 'JfifXDensity' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifPropertyKey；  API声明：Y\_DENSITY = 'JfifYDensity'  差异内容：Y\_DENSITY = 'JfifYDensity' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifPropertyKey；  API声明：VERSION = 'JfifVersion'  差异内容：VERSION = 'JfifVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifPropertyKey；  API声明：IS\_PROGRESSIVE = 'JfifIsProgressive'  差异内容：IS\_PROGRESSIVE = 'JfifIsProgressive' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum PngPropertyKey  差异内容：enum PngPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：X\_PIXELS\_PER\_METER = 'PngXPixelsPerMeter'  差异内容：X\_PIXELS\_PER\_METER = 'PngXPixelsPerMeter' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：MODIFICATION\_TIME = 'PngModificationTime'  差异内容：MODIFICATION\_TIME = 'PngModificationTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：SOFTWARE = 'PngSoftware'  差异内容：SOFTWARE = 'PngSoftware' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：COPYRIGHT = 'PngCopyright'  差异内容：COPYRIGHT = 'PngCopyright' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：CREATION\_TIME = 'PngCreationTime'  差异内容：CREATION\_TIME = 'PngCreationTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：SRGB\_INTENT = 'PngSRGBIntent'  差异内容：SRGB\_INTENT = 'PngSRGBIntent' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：AUTHOR = 'PngAuthor'  差异内容：AUTHOR = 'PngAuthor' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：INTERLACE\_TYPE = 'PngInterlaceType'  差异内容：INTERLACE\_TYPE = 'PngInterlaceType' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：WARNING = 'PngWarning'  差异内容：WARNING = 'PngWarning' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：Y\_PIXELS\_PER\_METER = 'PngYPixelsPerMeter'  差异内容：Y\_PIXELS\_PER\_METER = 'PngYPixelsPerMeter' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：GAMMA = 'PngGamma'  差异内容：GAMMA = 'PngGamma' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：CHROMATICITIES = 'PngChromaticities'  差异内容：CHROMATICITIES = 'PngChromaticities' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：DESCRIPTION = 'PngDescription'  差异内容：DESCRIPTION = 'PngDescription' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：TITLE = 'PngTitle'  差异内容：TITLE = 'PngTitle' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：COMMENT = 'PngComment'  差异内容：COMMENT = 'PngComment' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngPropertyKey；  API声明：DISCLAIMER = 'PngDisclaimer'  差异内容：DISCLAIMER = 'PngDisclaimer' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：readonly heifsCanvasHeight?: number;  差异内容：readonly heifsCanvasHeight?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：readonly heifsCanvasWidth?: number;  差异内容：readonly heifsCanvasWidth?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HeifsMetadata；  API声明：readonly heifsUnclampedDelayTime?: number;  差异内容：readonly heifsUnclampedDelayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class JfifMetadata  差异内容：class JfifMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifMetadata；  API声明：readonly densityUnit?: number;  差异内容：readonly densityUnit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifMetadata；  API声明：readonly xDensity?: number;  差异内容：readonly xDensity?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifMetadata；  API声明：readonly yDensity?: number;  差异内容：readonly yDensity?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifMetadata；  API声明：readonly isProgressive?: boolean;  差异内容：readonly isProgressive?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：JfifMetadata；  API声明：readonly version?: number[];  差异内容：readonly version?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class GifMetadata  差异内容：class GifMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly delayTime?: number;  差异内容：readonly delayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly unclampedDelayTime?: number;  差异内容：readonly unclampedDelayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly hasGlobalColorMap?: boolean;  差异内容：readonly hasGlobalColorMap?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly loopCount?: number;  差异内容：readonly loopCount?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly disposalType?: number;  差异内容：readonly disposalType?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly canvasHeight?: number;  差异内容：readonly canvasHeight?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifMetadata；  API声明：readonly canvasWidth?: number;  差异内容：readonly canvasWidth?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class TiffMetadata  差异内容：class TiffMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly primaryChromaticities?: number[];  差异内容：readonly primaryChromaticities?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly tileWidth?: number;  差异内容：readonly tileWidth?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly tileLength?: number;  差异内容：readonly tileLength?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly dateTime?: string;  差异内容：readonly dateTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly make?: string;  差异内容：readonly make?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly photometricInterpretation?: number;  差异内容：readonly photometricInterpretation?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly whitePoint?: number[];  差异内容：readonly whitePoint?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly documentName?: string;  差异内容：readonly documentName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly imageDescription?: string;  差异内容：readonly imageDescription?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly software?: string;  差异内容：readonly software?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly xResolution?: number;  差异内容：readonly xResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly yResolution?: number;  差异内容：readonly yResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly hostComputer?: string;  差异内容：readonly hostComputer?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly transferFunction?: string;  差异内容：readonly transferFunction?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly artist?: string;  差异内容：readonly artist?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly orientation?: Orientation;  差异内容：readonly orientation?: Orientation; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly model?: string;  差异内容：readonly model?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly resolutionUnit?: number;  差异内容：readonly resolutionUnit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly compression?: number;  差异内容：readonly compression?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：TiffMetadata；  API声明：readonly copyright?: string;  差异内容：readonly copyright?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class PngMetadata  差异内容：class PngMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly xPixelsPerMeter?: number;  差异内容：readonly xPixelsPerMeter?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly software?: string;  差异内容：readonly software?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly disclaimer?: string;  差异内容：readonly disclaimer?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly description?: string;  差异内容：readonly description?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly copyright?: string;  差异内容：readonly copyright?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly interlaceType?: number;  差异内容：readonly interlaceType?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly comment?: string;  差异内容：readonly comment?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly author?: string;  差异内容：readonly author?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly chromaticities?: number[];  差异内容：readonly chromaticities?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly creationTime?: string;  差异内容：readonly creationTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly modificationTime?: string;  差异内容：readonly modificationTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly gamma?: number;  差异内容：readonly gamma?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly yPixelsPerMeter?: number;  差异内容：readonly yPixelsPerMeter?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly sRGBIntent?: number;  差异内容：readonly sRGBIntent?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly title?: string;  差异内容：readonly title?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PngMetadata；  API声明：readonly warning?: string;  差异内容：readonly warning?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum XMPTagType  差异内容：enum XMPTagType | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：STRING = 1  差异内容：STRING = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：UNORDERED\_ARRAY = 2  差异内容：UNORDERED\_ARRAY = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：ORDERED\_ARRAY = 3  差异内容：ORDERED\_ARRAY = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：ALTERNATE\_ARRAY = 4  差异内容：ALTERNATE\_ARRAY = 4 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：ALTERNATE\_TEXT = 5  差异内容：ALTERNATE\_TEXT = 5 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTagType；  API声明：STRUCTURE = 6  差异内容：STRUCTURE = 6 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface XMPNamespace  差异内容：interface XMPNamespace | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPNamespace；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPNamespace；  API声明：prefix: string;  差异内容：prefix: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const XMP\_BASIC: XMPNamespace;  差异内容：const XMP\_BASIC: XMPNamespace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const XMP\_RIGHTS: XMPNamespace;  差异内容：const XMP\_RIGHTS: XMPNamespace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const EXIF: XMPNamespace;  差异内容：const EXIF: XMPNamespace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const DUBLIN\_CORE: XMPNamespace;  差异内容：const DUBLIN\_CORE: XMPNamespace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const TIFF: XMPNamespace;  差异内容：const TIFF: XMPNamespace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface XMPTag  差异内容：interface XMPTag | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTag；  API声明：xmpNamespace: XMPNamespace;  差异内容：xmpNamespace: XMPNamespace; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTag；  API声明：name: string;  差异内容：name: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTag；  API声明：type: XMPTagType;  差异内容：type: XMPTagType; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPTag；  API声明：value?: string;  差异内容：value?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface XMPEnumerateOptions  差异内容：interface XMPEnumerateOptions | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPEnumerateOptions；  API声明：isRecursive?: boolean;  差异内容：isRecursive?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPEnumerateOptions；  API声明：onlyQualifier?: boolean;  差异内容：onlyQualifier?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class XMPMetadata  差异内容：class XMPMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>;  差异内容：public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public setValue(path: string, type: XMPTagType, value?: string): Promise<void>;  差异内容：public setValue(path: string, type: XMPTagType, value?: string): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public getTag(path: string): Promise<XMPTag | null>;  差异内容：public getTag(path: string): Promise<XMPTag | null>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public removeTag(path: string): Promise<void>;  差异内容：public removeTag(path: string): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public enumerateTags(callback: (path: string, tag: XMPTag) => boolean, rootPath?: string, options?: XMPEnumerateOptions): void;  差异内容：public enumerateTags(callback: (path: string, tag: XMPTag) => boolean, rootPath?: string, options?: XMPEnumerateOptions): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>;  差异内容：public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public setBlob(buffer: ArrayBuffer): Promise<void>;  差异内容：public setBlob(buffer: ArrayBuffer): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：XMPMetadata；  API声明：public getBlob(): Promise<ArrayBuffer>;  差异内容：public getBlob(): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum AvisPropertyKey  差异内容：enum AvisPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AvisPropertyKey；  API声明：DELAY\_TIME = 'AvisDelayTime'  差异内容：DELAY\_TIME = 'AvisDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class AvisMetadata  差异内容：class AvisMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AvisMetadata；  API声明：readonly delayTime?: number;  差异内容：readonly delayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：gifMetadata?: GifMetadata;  差异内容：gifMetadata?: GifMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：tiffMetadata?: TiffMetadata;  差异内容：tiffMetadata?: TiffMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：jfifMetadata?: JfifMetadata;  差异内容：jfifMetadata?: JfifMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：pngMetadata?: PngMetadata;  差异内容：pngMetadata?: PngMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：xmpMetadata?: XMPMetadata;  差异内容：xmpMetadata?: XMPMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：avisMetadata?: AvisMetadata;  差异内容：avisMetadata?: AvisMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface DecodingOptionsForThumbnail  差异内容：interface DecodingOptionsForThumbnail | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForThumbnail；  API声明：generateThumbnailIfAbsent?: boolean;  差异内容：generateThumbnailIfAbsent?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForThumbnail；  API声明：maxGeneratedPixelDimension?: number;  差异内容：maxGeneratedPixelDimension?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>;  差异内容：createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined;  差异内容：createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined; | api/@ohos.multimedia.image.d.ts |
