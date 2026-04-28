---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-510
title: Device Security Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:39e347e1f27babf977b0925446fe36f005bfd67b48ff033357d35b034663e821
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：safetyDetect；  API声明：function checkUrlThreat(req: UrlCheckRequest): Promise<UrlCheckResponse>;  差异内容：NA | 类名：safetyDetect；  API声明：function checkUrlThreat(req: UrlCheckRequest): Promise<UrlCheckResponse>;  差异内容：1010800005,1010800006,1010800007,1010800008,801 | api/@hms.security.safetyDetect.d.ts |
| 新增错误码 | 类名：safetyDetect；  API声明：function checkSysIntegrity(req: SysIntegrityRequest): Promise<SysIntegrityResponse>;  差异内容：NA | 类名：safetyDetect；  API声明：function checkSysIntegrity(req: SysIntegrityRequest): Promise<SysIntegrityResponse>;  差异内容：1010800005,1010800006,1010800007,1010800008,801 | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：function checkSysIntegrityOnLocal(): Promise<string>;  差异内容：function checkSysIntegrityOnLocal(): Promise<string>; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：AttestType；  API声明：ATTEST\_TYPE\_SECIMAGE\_PROCESS = 3  差异内容：ATTEST\_TYPE\_SECIMAGE\_PROCESS = 3 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：AttestExceptionErrCode；  API声明：ATTEST\_ERROR\_SIGNATURE\_VERIFICATION\_FAILED = 1011500017  差异内容：ATTEST\_ERROR\_SIGNATURE\_VERIFICATION\_FAILED = 1011500017 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：AttestExceptionErrCode；  API声明：ATTEST\_ERROR\_SECIMAGE\_PROCESS\_FAILED = 1011500018  差异内容：ATTEST\_ERROR\_SECIMAGE\_PROCESS\_FAILED = 1011500018 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export enum SecImageProcFormat  差异内容：export enum SecImageProcFormat | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcFormat；  API声明：SECIMAGE\_FORMAT\_INVALID = 0  差异内容：SECIMAGE\_FORMAT\_INVALID = 0 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcFormat；  API声明：SECIMAGE\_FORMAT\_YUV\_NV21 = 1  差异内容：SECIMAGE\_FORMAT\_YUV\_NV21 = 1 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcFormat；  API声明：SECIMAGE\_FORMAT\_JPEG = 2  差异内容：SECIMAGE\_FORMAT\_JPEG = 2 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export enum SecImageProcOperation  差异内容：export enum SecImageProcOperation | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcOperation；  API声明：SECIMAGE\_COMPRESSION = 0  差异内容：SECIMAGE\_COMPRESSION = 0 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcOperation；  API声明：SECIMAGE\_CROPPING = 1  差异内容：SECIMAGE\_CROPPING = 1 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcOperation；  API声明：SECIMAGE\_COMPRESSION\_AND\_CROPPING = 2  差异内容：SECIMAGE\_COMPRESSION\_AND\_CROPPING = 2 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export interface SecImageBuffer  差异内容：export interface SecImageBuffer | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageBuffer；  API声明：secImage: ArrayBuffer;  差异内容：secImage: ArrayBuffer; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export interface CropRegion  差异内容：export interface CropRegion | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion；  API声明：x: number;  差异内容：x: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion；  API声明：y: number;  差异内容：y: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion；  API声明：width: number;  差异内容：width: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion；  API声明：height: number;  差异内容：height: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export enum SecImageProcTag  差异内容：export enum SecImageProcTag | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag；  API声明：SECIMAGE\_TAG\_INVALID = AttestTagType.ATTEST\_TAG\_TYPE\_INVALID | 0  差异内容：SECIMAGE\_TAG\_INVALID = AttestTagType.ATTEST\_TAG\_TYPE\_INVALID | 0 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag；  API声明：SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 1  差异内容：SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 1 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag；  API声明：SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 2  差异内容：SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 2 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag；  API声明：SECIMAGE\_TAG\_PROC\_OPERATION = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 3  差异内容：SECIMAGE\_TAG\_PROC\_OPERATION = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 3 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag；  API声明：SECIMAGE\_TAG\_COMPRESSION\_QUALITY = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 4  差异内容：SECIMAGE\_TAG\_COMPRESSION\_QUALITY = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 4 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag；  API声明：SECIMAGE\_TAG\_CROP\_REGION = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 5  差异内容：SECIMAGE\_TAG\_CROP\_REGION = AttestTagType.ATTEST\_TAG\_TYPE\_UINT | 5 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export interface SecImageProcParams  差异内容：export interface SecImageProcParams | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcParams；  API声明：tag: SecImageProcTag;  差异内容：tag: SecImageProcTag; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcParams；  API声明：value: number | CropRegion;  差异内容：value: number | CropRegion; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：export interface SecImageProcParamsArray  差异内容：export interface SecImageProcParamsArray | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcParamsArray；  API声明：properties: Array<SecImageProcParams>;  差异内容：properties: Array<SecImageProcParams>; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService；  API声明：function procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>;  差异内容：function procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>; | api/@hms.security.trustedAppService.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：FraudDetectionRequest；  API声明：version?: number;  差异内容：version?: number; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
