---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-spatialreconkit-7002
title: Spatial Recon Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Spatial Recon Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e00d705a58111723ca2cced2a4525bbad0317159c7e6f9a303b64b3a5420edf1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace spatialEdit  差异内容：declare namespace spatialEdit | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：spatialEdit；  API声明：export enum PaintMode  差异内容：export enum PaintMode | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：PaintMode；  API声明：REPLACE = 0  差异内容：REPLACE = 0 | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：PaintMode；  API声明：MULTIPLY = 1  差异内容：MULTIPLY = 1 | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：PaintMode；  API声明：ADD = 2  差异内容：ADD = 2 | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：spatialEdit；  API声明：export class GSEdit  差异内容：export class GSEdit | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：static editGSNode(node: spatialRender.GSNode): GSEdit | undefined;  差异内容：static editGSNode(node: spatialRender.GSNode): GSEdit | undefined; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：selectBy2DBox(rect: Rect): void;  差异内容：selectBy2DBox(rect: Rect): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：selectBy3DBox(aabb: Aabb): void;  差异内容：selectBy3DBox(aabb: Aabb): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：selectByIndex(indices: number[]): void;  差异内容：selectByIndex(indices: number[]): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：selectBy2DMask(mask: image.PixelMap): void;  差异内容：selectBy2DMask(mask: image.PixelMap): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：invertSelection(): void;  差异内容：invertSelection(): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：clearSelection(): void;  差异内容：clearSelection(): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：transform(matrix: Mat4x4): void;  差异内容：transform(matrix: Mat4x4): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：paint(color: Color, mode: PaintMode): void;  差异内容：paint(color: Color, mode: PaintMode): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：remove(): void;  差异内容：remove(): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：undo(): void;  差异内容：undo(): void; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：getRecommended3DBox(ori: Vec3, dir: Vec3): Aabb;  差异内容：getRecommended3DBox(ori: Vec3, dir: Vec3): Aabb; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：saveToPLY(uri: string): Promise<boolean>;  差异内容：saveToPLY(uri: string): Promise<boolean>; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：GSEdit；  API声明：extract3DMainBody(pressPoint: Vec2): Promise<boolean>;  差异内容：extract3DMainBody(pressPoint: Vec2): Promise<boolean>; | api/@hms.graphics.spatialEdit.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface TiledGSImportSettings  差异内容：export interface TiledGSImportSettings | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSImportSettings；  API声明：uri: string;  差异内容：uri: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface TiledGSNode  差异内容：export interface TiledGSNode | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSNode；  API声明：setCamera(camera: Camera): void;  差异内容：setCamera(camera: Camera): void; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSNode；  API声明：setTileRequestCallback(callback: GSTileRequestCallback | null): void;  差异内容：setTileRequestCallback(callback: GSTileRequestCallback | null): void; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：TiledGSNode；  API声明：notifyTileReady(tile: GSTile): void;  差异内容：notifyTileReady(tile: GSTile): void; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSPlugin；  API声明：static loadTiledGSNode(scene: Scene, params: TiledGSImportSettings, parent?: Node): Promise<TiledGSNode>;  差异内容：static loadTiledGSNode(scene: Scene, params: TiledGSImportSettings, parent?: Node): Promise<TiledGSNode>; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export interface GSTile  差异内容：export interface GSTile | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：GSTile；  API声明：uri: string;  差异内容：uri: string; | api/@hms.graphics.spatialRender.d.ts |
| 新增API | NA | 类名：spatialRender；  API声明：export type GSTileRequestCallback = (tiles: GSTile[]) => void;  差异内容：export type GSTileRequestCallback = (tiles: GSTile[]) => void; | api/@hms.graphics.spatialRender.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.graphics.spatialEdit.d.ts  差异内容：SpatialReconKit | api/@hms.graphics.spatialEdit.d.ts |
