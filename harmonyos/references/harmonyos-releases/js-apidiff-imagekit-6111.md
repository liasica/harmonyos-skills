---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-6111
title: Image Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:5fd79d555fb50aab646fc6b6ee4fd33d46d11ce43a3ed0c0eb9a01a2829eea27
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：ImageSource；  API声明：createPicture(options?: DecodingOptionsForPicture): Promise<Picture>;  差异内容：NA | 类名：ImageSource；  API声明：createPicture(options?: DecodingOptionsForPicture): Promise<Picture>;  差异内容：7700203 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo, allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture;  差异内容：function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo, allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：DNG\_METADATA = 16  差异内容：DNG\_METADATA = 16 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType；  API声明：WEBP\_METADATA = 17  差异内容：WEBP\_METADATA = 17 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum DngPropertyKey  差异内容：enum DngPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DNG\_VERSION = 'DNGVersion'  差异内容：DNG\_VERSION = 'DNGVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DNG\_BACKWARD\_VERSION = 'DNGBackwardVersion'  差异内容：DNG\_BACKWARD\_VERSION = 'DNGBackwardVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：UNIQUE\_CAMERA\_MODEL = 'UniqueCameraModel'  差异内容：UNIQUE\_CAMERA\_MODEL = 'UniqueCameraModel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：LOCALIZED\_CAMERA\_MODEL = 'LocalizedCameraModel'  差异内容：LOCALIZED\_CAMERA\_MODEL = 'LocalizedCameraModel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CFA\_PLANE\_COLOR = 'CFAPlaneColor'  差异内容：CFA\_PLANE\_COLOR = 'CFAPlaneColor' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CFA\_LAYOUT = 'CFALayout'  差异内容：CFA\_LAYOUT = 'CFALayout' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：LINEARIZATION\_TABLE = 'LinearizationTable'  差异内容：LINEARIZATION\_TABLE = 'LinearizationTable' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BLACK\_LEVEL\_REPEAT\_DIM = 'BlackLevelRepeatDim'  差异内容：BLACK\_LEVEL\_REPEAT\_DIM = 'BlackLevelRepeatDim' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BLACK\_LEVEL = 'BlackLevel'  差异内容：BLACK\_LEVEL = 'BlackLevel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BLACK\_LEVEL\_DELTA\_H = 'BlackLevelDeltaH'  差异内容：BLACK\_LEVEL\_DELTA\_H = 'BlackLevelDeltaH' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BLACK\_LEVEL\_DELTA\_V = 'BlackLevelDeltaV'  差异内容：BLACK\_LEVEL\_DELTA\_V = 'BlackLevelDeltaV' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：WHITE\_LEVEL = 'WhiteLevel'  差异内容：WHITE\_LEVEL = 'WhiteLevel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DEFAULT\_SCALE = 'DefaultScale'  差异内容：DEFAULT\_SCALE = 'DefaultScale' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DEFAULT\_CROP\_ORIGIN = 'DefaultCropOrigin'  差异内容：DEFAULT\_CROP\_ORIGIN = 'DefaultCropOrigin' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DEFAULT\_CROP\_SIZE = 'DefaultCropSize'  差异内容：DEFAULT\_CROP\_SIZE = 'DefaultCropSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：COLOR\_MATRIX1 = 'ColorMatrix1'  差异内容：COLOR\_MATRIX1 = 'ColorMatrix1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：COLOR\_MATRIX2 = 'ColorMatrix2'  差异内容：COLOR\_MATRIX2 = 'ColorMatrix2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CAMERA\_CALIBRATION1 = 'CameraCalibration1'  差异内容：CAMERA\_CALIBRATION1 = 'CameraCalibration1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CAMERA\_CALIBRATION2 = 'CameraCalibration2'  差异内容：CAMERA\_CALIBRATION2 = 'CameraCalibration2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：REDUCTION\_MATRIX1 = 'ReductionMatrix1'  差异内容：REDUCTION\_MATRIX1 = 'ReductionMatrix1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：REDUCTION\_MATRIX2 = 'ReductionMatrix2'  差异内容：REDUCTION\_MATRIX2 = 'ReductionMatrix2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ANALOG\_BALANCE = 'AnalogBalance'  差异内容：ANALOG\_BALANCE = 'AnalogBalance' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：AS\_SHOT\_NEUTRAL = 'AsShotNeutral'  差异内容：AS\_SHOT\_NEUTRAL = 'AsShotNeutral' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：AS\_SHOT\_WHITEXY = 'AsShotWhiteXY'  差异内容：AS\_SHOT\_WHITEXY = 'AsShotWhiteXY' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BASELINE\_EXPOSURE = 'BaselineExposure'  差异内容：BASELINE\_EXPOSURE = 'BaselineExposure' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BASELINE\_NOISE = 'BaselineNoise'  差异内容：BASELINE\_NOISE = 'BaselineNoise' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BASELINE\_SHARPNESS = 'BaselineSharpness'  差异内容：BASELINE\_SHARPNESS = 'BaselineSharpness' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BAYER\_GREEN\_SPLIT = 'BayerGreenSplit'  差异内容：BAYER\_GREEN\_SPLIT = 'BayerGreenSplit' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：LINEAR\_RESPONSE\_LIMIT = 'LinearResponseLimit'  差异内容：LINEAR\_RESPONSE\_LIMIT = 'LinearResponseLimit' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CAMERA\_SERIAL\_NUMBER = 'CameraSerialNumber'  差异内容：CAMERA\_SERIAL\_NUMBER = 'CameraSerialNumber' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：LENS\_INFO = 'LensInfo'  差异内容：LENS\_INFO = 'LensInfo' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CHROMA\_BLUR\_RADIUS = 'ChromaBlurRadius'  差异内容：CHROMA\_BLUR\_RADIUS = 'ChromaBlurRadius' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ANTI\_ALIAS\_STRENGTH = 'AntiAliasStrength'  差异内容：ANTI\_ALIAS\_STRENGTH = 'AntiAliasStrength' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：SHADOW\_SCALE = 'ShadowScale'  差异内容：SHADOW\_SCALE = 'ShadowScale' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DNG\_PRIVATE\_DATA = 'DNGPrivateData'  差异内容：DNG\_PRIVATE\_DATA = 'DNGPrivateData' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：MAKER\_NOTE\_SAFETY = 'MakerNoteSafety'  差异内容：MAKER\_NOTE\_SAFETY = 'MakerNoteSafety' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CALIBRATION\_ILLUMINANT1 = 'CalibrationIlluminant1'  差异内容：CALIBRATION\_ILLUMINANT1 = 'CalibrationIlluminant1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CALIBRATION\_ILLUMINANT2 = 'CalibrationIlluminant2'  差异内容：CALIBRATION\_ILLUMINANT2 = 'CalibrationIlluminant2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BEST\_QUALITY\_SCALE = 'BestQualityScale'  差异内容：BEST\_QUALITY\_SCALE = 'BestQualityScale' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：RAW\_DATA\_UNIQUE\_ID = 'RawDataUniqueID'  差异内容：RAW\_DATA\_UNIQUE\_ID = 'RawDataUniqueID' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ORIGINAL\_RAW\_FILE\_NAME = 'OriginalRawFileName'  差异内容：ORIGINAL\_RAW\_FILE\_NAME = 'OriginalRawFileName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ORIGINAL\_RAW\_FILE\_DATA = 'OriginalRawFileData'  差异内容：ORIGINAL\_RAW\_FILE\_DATA = 'OriginalRawFileData' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ACTIVE\_AREA = 'ActiveArea'  差异内容：ACTIVE\_AREA = 'ActiveArea' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：MASKED\_AREAS = 'MaskedAreas'  差异内容：MASKED\_AREAS = 'MaskedAreas' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：AS\_SHOT\_ICC\_PROFILE = 'AsShotICCProfile'  差异内容：AS\_SHOT\_ICC\_PROFILE = 'AsShotICCProfile' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：AS\_SHOT\_PRE\_PROFILE\_MATRIX = 'AsShotPreProfileMatrix'  差异内容：AS\_SHOT\_PRE\_PROFILE\_MATRIX = 'AsShotPreProfileMatrix' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CURRENT\_ICC\_PROFILE = 'CurrentICCProfile'  差异内容：CURRENT\_ICC\_PROFILE = 'CurrentICCProfile' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CURRENT\_PRE\_PROFILE\_MATRIX = 'CurrentPreProfileMatrix'  差异内容：CURRENT\_PRE\_PROFILE\_MATRIX = 'CurrentPreProfileMatrix' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：COLORIMETRIC\_REFERENCE = 'ColorimetricReference'  差异内容：COLORIMETRIC\_REFERENCE = 'ColorimetricReference' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：CAMERA\_CALIBRATION\_SIGNATURE = 'CameraCalibrationSignature'  差异内容：CAMERA\_CALIBRATION\_SIGNATURE = 'CameraCalibrationSignature' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_CALIBRATION\_SIGNATURE = 'ProfileCalibrationSignature'  差异内容：PROFILE\_CALIBRATION\_SIGNATURE = 'ProfileCalibrationSignature' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：EXTRA\_CAMERA\_PROFILES = 'ExtraCameraProfiles'  差异内容：EXTRA\_CAMERA\_PROFILES = 'ExtraCameraProfiles' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：AS\_SHOT\_PROFILE\_NAME = 'AsShotProfileName'  差异内容：AS\_SHOT\_PROFILE\_NAME = 'AsShotProfileName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：NOISE\_REDUCTION\_APPLIED = 'NoiseReductionApplied'  差异内容：NOISE\_REDUCTION\_APPLIED = 'NoiseReductionApplied' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_NAME = 'ProfileName'  差异内容：PROFILE\_NAME = 'ProfileName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_HUE\_SAT\_MAP\_DIMS = 'ProfileHueSatMapDims'  差异内容：PROFILE\_HUE\_SAT\_MAP\_DIMS = 'ProfileHueSatMapDims' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_HUE\_SAT\_MAP\_DATA1 = 'ProfileHueSatMapData1'  差异内容：PROFILE\_HUE\_SAT\_MAP\_DATA1 = 'ProfileHueSatMapData1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_HUE\_SAT\_MAP\_DATA2 = 'ProfileHueSatMapData2'  差异内容：PROFILE\_HUE\_SAT\_MAP\_DATA2 = 'ProfileHueSatMapData2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_TONE\_CURVE = 'ProfileToneCurve'  差异内容：PROFILE\_TONE\_CURVE = 'ProfileToneCurve' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_EMBED\_POLICY = 'ProfileEmbedPolicy'  差异内容：PROFILE\_EMBED\_POLICY = 'ProfileEmbedPolicy' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_COPYRIGHT = 'ProfileCopyright'  差异内容：PROFILE\_COPYRIGHT = 'ProfileCopyright' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：FORWARD\_MATRIX1 = 'ForwardMatrix1'  差异内容：FORWARD\_MATRIX1 = 'ForwardMatrix1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：FORWARD\_MATRIX2 = 'ForwardMatrix2'  差异内容：FORWARD\_MATRIX2 = 'ForwardMatrix2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PREVIEW\_APPLICATION\_NAME = 'PreviewApplicationName'  差异内容：PREVIEW\_APPLICATION\_NAME = 'PreviewApplicationName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PREVIEW\_APPLICATION\_VERSION = 'PreviewApplicationVersion'  差异内容：PREVIEW\_APPLICATION\_VERSION = 'PreviewApplicationVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PREVIEW\_SETTINGS\_NAME = 'PreviewSettingsName'  差异内容：PREVIEW\_SETTINGS\_NAME = 'PreviewSettingsName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PREVIEW\_SETTINGS\_DIGEST = 'PreviewSettingsDigest'  差异内容：PREVIEW\_SETTINGS\_DIGEST = 'PreviewSettingsDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PREVIEW\_COLOR\_SPACE = 'PreviewColorSpace'  差异内容：PREVIEW\_COLOR\_SPACE = 'PreviewColorSpace' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PREVIEW\_DATE\_TIME = 'PreviewDateTime'  差异内容：PREVIEW\_DATE\_TIME = 'PreviewDateTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：RAW\_IMAGE\_DIGEST = 'RawImageDigest'  差异内容：RAW\_IMAGE\_DIGEST = 'RawImageDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ORIGINAL\_RAW\_FILE\_DIGEST = 'OriginalRawFileDigest'  差异内容：ORIGINAL\_RAW\_FILE\_DIGEST = 'OriginalRawFileDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：SUB\_TILE\_BLOCK\_SIZE = 'SubTileBlockSize'  差异内容：SUB\_TILE\_BLOCK\_SIZE = 'SubTileBlockSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ROW\_INTERLEAVE\_FACTOR = 'RowInterleaveFactor'  差异内容：ROW\_INTERLEAVE\_FACTOR = 'RowInterleaveFactor' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_LOOK\_TABLE\_DIMS = 'ProfileLookTableDims'  差异内容：PROFILE\_LOOK\_TABLE\_DIMS = 'ProfileLookTableDims' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_LOOK\_TABLE\_DATA = 'ProfileLookTableData'  差异内容：PROFILE\_LOOK\_TABLE\_DATA = 'ProfileLookTableData' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：OPCODE\_LIST1 = 'OpcodeList1'  差异内容：OPCODE\_LIST1 = 'OpcodeList1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：OPCODE\_LIST2 = 'OpcodeList2'  差异内容：OPCODE\_LIST2 = 'OpcodeList2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：OPCODE\_LIST3 = 'OpcodeList3'  差异内容：OPCODE\_LIST3 = 'OpcodeList3' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：NOISE\_PROFILE = 'NoiseProfile'  差异内容：NOISE\_PROFILE = 'NoiseProfile' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ORIGINAL\_DEFAULT\_FINAL\_SIZE = 'OriginalDefaultFinalSize'  差异内容：ORIGINAL\_DEFAULT\_FINAL\_SIZE = 'OriginalDefaultFinalSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ORIGINAL\_BEST\_QUALITY\_FINAL\_SIZE = 'OriginalBestQualityFinalSize'  差异内容：ORIGINAL\_BEST\_QUALITY\_FINAL\_SIZE = 'OriginalBestQualityFinalSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：ORIGINAL\_DEFAULT\_CROP\_SIZE = 'OriginalDefaultCropSize'  差异内容：ORIGINAL\_DEFAULT\_CROP\_SIZE = 'OriginalDefaultCropSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_HUE\_SAT\_MAP\_ENCODING = 'ProfileHueSatMapEncoding'  差异内容：PROFILE\_HUE\_SAT\_MAP\_ENCODING = 'ProfileHueSatMapEncoding' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：PROFILE\_LOOK\_TABLE\_ENCODING = 'ProfileLookTableEncoding'  差异内容：PROFILE\_LOOK\_TABLE\_ENCODING = 'ProfileLookTableEncoding' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：BASELINE\_EXPOSURE\_OFFSET = 'BaselineExposureOffset'  差异内容：BASELINE\_EXPOSURE\_OFFSET = 'BaselineExposureOffset' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DEFAULT\_BLACK\_RENDER = 'DefaultBlackRender'  差异内容：DEFAULT\_BLACK\_RENDER = 'DefaultBlackRender' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：NEW\_RAW\_IMAGE\_DIGEST = 'NewRawImageDigest'  差异内容：NEW\_RAW\_IMAGE\_DIGEST = 'NewRawImageDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：RAW\_TO\_PREVIEW\_GAIN = 'RawToPreviewGain'  差异内容：RAW\_TO\_PREVIEW\_GAIN = 'RawToPreviewGain' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey；  API声明：DEFAULT\_USER\_CROP = 'DefaultUserCrop'  差异内容：DEFAULT\_USER\_CROP = 'DefaultUserCrop' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class DngMetadata  差异内容：class DngMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly dngVersion?: number[];  差异内容：readonly dngVersion?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly dngBackwardVersion?: number[];  差异内容：readonly dngBackwardVersion?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly uniqueCameraModel?: string;  差异内容：readonly uniqueCameraModel?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly localizedCameraModel?: string;  差异内容：readonly localizedCameraModel?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly cfaPlaneColor?: number[];  差异内容：readonly cfaPlaneColor?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly cfaLayout?: number;  差异内容：readonly cfaLayout?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly linearizationTable?: number[];  差异内容：readonly linearizationTable?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly blackLevelRepeatDim?: number[];  差异内容：readonly blackLevelRepeatDim?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly blackLevel?: number[];  差异内容：readonly blackLevel?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly blackLevelDeltaH?: number[];  差异内容：readonly blackLevelDeltaH?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly blackLevelDeltaV?: number[];  差异内容：readonly blackLevelDeltaV?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly whiteLevel?: number[];  差异内容：readonly whiteLevel?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly defaultScale?: number[];  差异内容：readonly defaultScale?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly defaultCropOrigin?: number[];  差异内容：readonly defaultCropOrigin?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly defaultCropSize?: number[];  差异内容：readonly defaultCropSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly colorMatrix1?: number[];  差异内容：readonly colorMatrix1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly colorMatrix2?: number[];  差异内容：readonly colorMatrix2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly cameraCalibration1?: number[];  差异内容：readonly cameraCalibration1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly cameraCalibration2?: number[];  差异内容：readonly cameraCalibration2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly reductionMatrix1?: number[];  差异内容：readonly reductionMatrix1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly reductionMatrix2?: number[];  差异内容：readonly reductionMatrix2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly analogBalance?: number[];  差异内容：readonly analogBalance?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly asShotNeutral?: number[];  差异内容：readonly asShotNeutral?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly asShotWhiteXY?: number[];  差异内容：readonly asShotWhiteXY?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly baselineExposure?: number;  差异内容：readonly baselineExposure?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly baselineNoise?: number;  差异内容：readonly baselineNoise?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly baselineSharpness?: number;  差异内容：readonly baselineSharpness?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly bayerGreenSplit?: number;  差异内容：readonly bayerGreenSplit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly linearResponseLimit?: number;  差异内容：readonly linearResponseLimit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly cameraSerialNumber?: string;  差异内容：readonly cameraSerialNumber?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly lensInfo?: number[];  差异内容：readonly lensInfo?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly chromaBlurRadius?: number;  差异内容：readonly chromaBlurRadius?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly antiAliasStrength?: number;  差异内容：readonly antiAliasStrength?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly shadowScale?: number;  差异内容：readonly shadowScale?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly dngPrivateData?: ArrayBuffer;  差异内容：readonly dngPrivateData?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly makerNoteSafety?: boolean;  差异内容：readonly makerNoteSafety?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly calibrationIlluminant1?: number;  差异内容：readonly calibrationIlluminant1?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly calibrationIlluminant2?: number;  差异内容：readonly calibrationIlluminant2?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly bestQualityScale?: number;  差异内容：readonly bestQualityScale?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly rawDataUniqueID?: string;  差异内容：readonly rawDataUniqueID?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly originalRawFileName?: string;  差异内容：readonly originalRawFileName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly originalRawFileData?: ArrayBuffer;  差异内容：readonly originalRawFileData?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly activeArea?: number[];  差异内容：readonly activeArea?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly maskedAreas?: number[];  差异内容：readonly maskedAreas?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly asShotICCProfile?: ArrayBuffer;  差异内容：readonly asShotICCProfile?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly asShotPreProfileMatrix?: number[];  差异内容：readonly asShotPreProfileMatrix?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly currentICCProfile?: ArrayBuffer;  差异内容：readonly currentICCProfile?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly currentPreProfileMatrix?: number[];  差异内容：readonly currentPreProfileMatrix?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly colorimetricReference?: number;  差异内容：readonly colorimetricReference?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly cameraCalibrationSignature?: string;  差异内容：readonly cameraCalibrationSignature?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileCalibrationSignature?: string;  差异内容：readonly profileCalibrationSignature?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly extraCameraProfiles?: number[];  差异内容：readonly extraCameraProfiles?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly asShotProfileName?: string;  差异内容：readonly asShotProfileName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly noiseReductionApplied?: number;  差异内容：readonly noiseReductionApplied?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileName?: string;  差异内容：readonly profileName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileHueSatMapDims?: number[];  差异内容：readonly profileHueSatMapDims?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileHueSatMapData1?: number[];  差异内容：readonly profileHueSatMapData1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileHueSatMapData2?: number[];  差异内容：readonly profileHueSatMapData2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileToneCurve?: number[];  差异内容：readonly profileToneCurve?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileEmbedPolicy?: number;  差异内容：readonly profileEmbedPolicy?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileCopyright?: string;  差异内容：readonly profileCopyright?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly forwardMatrix1?: number[];  差异内容：readonly forwardMatrix1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly forwardMatrix2?: number[];  差异内容：readonly forwardMatrix2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly previewApplicationName?: string;  差异内容：readonly previewApplicationName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly previewApplicationVersion?: string;  差异内容：readonly previewApplicationVersion?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly previewSettingsName?: string;  差异内容：readonly previewSettingsName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly previewSettingsDigest?: string;  差异内容：readonly previewSettingsDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly previewColorSpace?: number;  差异内容：readonly previewColorSpace?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly previewDateTime?: string;  差异内容：readonly previewDateTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly rawImageDigest?: string;  差异内容：readonly rawImageDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly originalRawFileDigest?: string;  差异内容：readonly originalRawFileDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly subTileBlockSize?: number[];  差异内容：readonly subTileBlockSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly rowInterleaveFactor?: number;  差异内容：readonly rowInterleaveFactor?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileLookTableDims?: number[];  差异内容：readonly profileLookTableDims?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileLookTableData?: number[];  差异内容：readonly profileLookTableData?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly opcodeList1?: ArrayBuffer;  差异内容：readonly opcodeList1?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly opcodeList2?: ArrayBuffer;  差异内容：readonly opcodeList2?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly opcodeList3?: ArrayBuffer;  差异内容：readonly opcodeList3?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly noiseProfile?: number[];  差异内容：readonly noiseProfile?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly originalDefaultFinalSize?: number[];  差异内容：readonly originalDefaultFinalSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly originalBestQualityFinalSize?: number[];  差异内容：readonly originalBestQualityFinalSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly originalDefaultCropSize?: number[];  差异内容：readonly originalDefaultCropSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileHueSatMapEncoding?: number;  差异内容：readonly profileHueSatMapEncoding?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly profileLookTableEncoding?: number;  差异内容：readonly profileLookTableEncoding?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly baselineExposureOffset?: number;  差异内容：readonly baselineExposureOffset?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly defaultBlackRender?: number;  差异内容：readonly defaultBlackRender?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly newRawImageDigest?: string;  差异内容：readonly newRawImageDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly rawToPreviewGain?: number;  差异内容：readonly rawToPreviewGain?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata；  API声明：readonly defaultUserCrop?: number[];  差异内容：readonly defaultUserCrop?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum WebPPropertyKey  差异内容：enum WebPPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey；  API声明：CANVAS\_WIDTH = 'WebPCanvasWidth'  差异内容：CANVAS\_WIDTH = 'WebPCanvasWidth' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey；  API声明：CANVAS\_HEIGHT = 'WebPCanvasHeight'  差异内容：CANVAS\_HEIGHT = 'WebPCanvasHeight' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey；  API声明：DELAY\_TIME = 'WebPDelayTime'  差异内容：DELAY\_TIME = 'WebPDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey；  API声明：UNCLAMPED\_DELAY\_TIME = 'WebPUnclampedDelayTime'  差异内容：UNCLAMPED\_DELAY\_TIME = 'WebPUnclampedDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey；  API声明：LOOP\_COUNT = 'WebPLoopCount'  差异内容：LOOP\_COUNT = 'WebPLoopCount' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：class WebPMetadata  差异内容：class WebPMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata；  API声明：readonly canvasWidth?: number;  差异内容：readonly canvasWidth?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata；  API声明：readonly canvasHeight?: number;  差异内容：readonly canvasHeight?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata；  API声明：readonly delayTime?: number;  差异内容：readonly delayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata；  API声明：readonly unclampedDelayTime?: number;  差异内容：readonly unclampedDelayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata；  API声明：readonly loopCount?: number;  差异内容：readonly loopCount?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：dngMetadata?: DngMetadata;  差异内容：dngMetadata?: DngMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata；  API声明：webPMetadata?: WebPMetadata;  差异内容：webPMetadata?: WebPMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForPicture；  API声明：desiredSizeForMainPixelMap?: Size;  差异内容：desiredSizeForMainPixelMap?: Size; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForPicture；  API声明：desiredPixelFormat?: PixelMapFormat;  差异内容：desiredPixelFormat?: PixelMapFormat; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface ImageRawData  差异内容：interface ImageRawData | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageRawData；  API声明：buffer: ArrayBuffer;  差异内容：buffer: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageRawData；  API声明：bitsPerPixel: number;  差异内容：bitsPerPixel: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>;  差异内容：readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：createImageRawData(): Promise<ImageRawData>;  差异内容：createImageRawData(): Promise<ImageRawData>; | api/@ohos.multimedia.image.d.ts |
