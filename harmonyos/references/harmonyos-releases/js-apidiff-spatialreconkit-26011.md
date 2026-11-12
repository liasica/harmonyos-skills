---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-spatialreconkit-26011
title: Spatial Recon Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Spatial Recon Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:86b40f4ee3bba86d31ccad82fc673704ce182bebb7a0b8a4e36ebbe1263b7075
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：spatialEdit；  API声明：export enum FloaterRemovalMode  差异内容：export enum FloaterRemovalMode | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：FloaterRemovalMode；  API声明：GS\_EDIT\_SINGLE\_VIEW = 'SingleView'  差异内容：GS\_EDIT\_SINGLE\_VIEW = 'SingleView' | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：spatialEdit；  API声明：interface FloaterRemovalParameters  差异内容：interface FloaterRemovalParameters | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：FloaterRemovalParameters；  API声明：mode: FloaterRemovalMode;  差异内容：mode: FloaterRemovalMode; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：spatialEdit；  API声明：export class FloaterRemovalTask  差异内容：export class FloaterRemovalTask | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：FloaterRemovalTask；  API声明：readonly isSuccess: Promise<boolean>;  差异内容：readonly isSuccess: Promise<boolean>; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：FloaterRemovalTask；  API声明：getProgress(): number;  差异内容：getProgress(): number; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：removeFloaters(option: FloaterRemovalParameters): FloaterRemovalTask;  差异内容：removeFloaters(option: FloaterRemovalParameters): FloaterRemovalTask; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：destroy(): void;  差异内容：destroy(): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export enum TiledGSRenderPreference  差异内容：export enum TiledGSRenderPreference | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSRenderPreference；  API声明：SMOOTH = 'smooth'  差异内容：SMOOTH = 'smooth' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSRenderPreference；  API声明：BALANCED = 'balanced'  差异内容：BALANCED = 'balanced' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSRenderPreference；  API声明：DETAILED = 'detailed'  差异内容：DETAILED = 'detailed' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSImportSettings；  API声明：renderPreference?: TiledGSRenderPreference;  差异内容：renderPreference?: TiledGSRenderPreference; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export enum CameraCollisionStatus  差异内容：export enum CameraCollisionStatus | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionStatus；  API声明：COLLISION = 'collision'  差异内容：COLLISION = 'collision' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionStatus；  API声明：NO\_COLLISION = 'noCollision'  差异内容：NO\_COLLISION = 'noCollision' | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface CameraCollisionRequest  差异内容：export interface CameraCollisionRequest | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionRequest；  API声明：startPosition: Vec3;  差异内容：startPosition: Vec3; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionRequest；  API声明：endPosition: Vec3;  差异内容：endPosition: Vec3; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface CameraCollisionResult  差异内容：export interface CameraCollisionResult | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionResult；  API声明：status: CameraCollisionStatus;  差异内容：status: CameraCollisionStatus; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export class CameraCollisionDetector  差异内容：export class CameraCollisionDetector | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionDetector；  API声明：static load(uri: string): Promise<CameraCollisionDetector | null>;  差异内容：static load(uri: string): Promise<CameraCollisionDetector | null>; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：CameraCollisionDetector；  API声明：detect(request: CameraCollisionRequest): Promise<CameraCollisionResult>;  差异内容：detect(request: CameraCollisionRequest): Promise<CameraCollisionResult>; | api/@hms.graphics.spatialRender.d.ts |
