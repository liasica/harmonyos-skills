---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics3d-6101
title: ArkGraphics 3D
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > ArkGraphics 3D
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e307ec58469b7c7eaac894cd7e9cbdb94f4d13b0144375222be426422e80dff2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface RenderConfiguration  差异内容：export interface RenderConfiguration | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RenderConfiguration；  API声明：shadowResolution?: Vec2;  差异内容：shadowResolution?: Vec2; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：Scene；  API声明：get environment(): Environment;  差异内容：get environment(): Environment; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：Scene；  API声明：get animations(): Animation[];  差异内容：get animations(): Animation[]; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：Scene；  API声明：get root(): Node | null;  差异内容：get root(): Node | null; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：Scene；  API声明：get renderConfiguration(): RenderConfiguration;  差异内容：get renderConfiguration(): RenderConfiguration; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：Scene；  API声明：cloneNode(node: Node, parent: Node, name: string): Node | null;  差异内容：cloneNode(node: Node, parent: Node, name: string): Node | null; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：GeometryType；  API声明：CYLINDER = 4  差异内容：CYLINDER = 4 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：GeometryDefinition；  API声明：get geometryType(): GeometryType;  差异内容：get geometryType(): GeometryType; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Mat4x4  差异内容：export interface Mat4x4 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：Mat4x4；  API声明：x: Vec4;  差异内容：x: Vec4; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：Mat4x4；  API声明：y: Vec4;  差异内容：y: Vec4; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：Mat4x4；  API声明：z: Vec4;  差异内容：z: Vec4; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：Mat4x4；  API声明：w: Vec4;  差异内容：w: Vec4; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：get vertices(): Vec3[];  差异内容：get vertices(): Vec3[]; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CubeGeometry；  API声明：get size(): Vec3;  差异内容：get size(): Vec3; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：PlaneGeometry；  API声明：get size(): Vec2;  差异内容：get size(): Vec2; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：SphereGeometry；  API声明：get radius(): number;  差异内容：get radius(): number; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：SphereGeometry；  API声明：get segmentCount(): number;  差异内容：get segmentCount(): number; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class CylinderGeometry  差异内容：export declare class CylinderGeometry | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CylinderGeometry；  API声明：get radius(): number;  差异内容：get radius(): number; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CylinderGeometry；  API声明：get height(): number;  差异内容：get height(): number; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CylinderGeometry；  API声明：get segmentCount(): number;  差异内容：get segmentCount(): number; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：SpotLight；  API声明：innerAngle?: number;  差异内容：innerAngle?: number; | api/graphics3d/SceneNodes.d.ts |
| 新增API | NA | 类名：SpotLight；  API声明：outerAngle?: number;  差异内容：outerAngle?: number; | api/graphics3d/SceneNodes.d.ts |
| 新增API | NA | 类名：Camera；  API声明：getViewMatrix(): Mat4x4;  差异内容：getViewMatrix(): Mat4x4; | api/graphics3d/SceneNodes.d.ts |
| 新增API | NA | 类名：Camera；  API声明：getProjectionMatrix(): Mat4x4;  差异内容：getProjectionMatrix(): Mat4x4; | api/graphics3d/SceneNodes.d.ts |
| 新增API | NA | 类名：Shader；  API声明：setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void;  差异内容：setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MaterialType；  API声明：UNLIT = 3  差异内容：UNLIT = 3 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MaterialType；  API声明：OCCLUSION = 4  差异内容：OCCLUSION = 4 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum PolygonMode  差异内容：export enum PolygonMode | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：PolygonMode；  API声明：FILL = 0  差异内容：FILL = 0 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：PolygonMode；  API声明：LINE = 1  差异内容：LINE = 1 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：PolygonMode；  API声明：POINT = 2  差异内容：POINT = 2 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Material；  API声明：polygonMode?: PolygonMode;  差异内容：polygonMode?: PolygonMode; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface UnlitMaterial  差异内容：export interface UnlitMaterial | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：UnlitMaterial；  API声明：baseColor: MaterialProperty;  差异内容：baseColor: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface OcclusionMaterial  差异内容：export interface OcclusionMaterial | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Environment；  API声明：environmentRotation?: Quaternion;  差异内容：environmentRotation?: Quaternion; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Effect；  API声明：getPropertyValue(propertyName: string): Object | null | undefined;  差异内容：getPropertyValue(propertyName: string): Object | null | undefined; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Effect；  API声明：setPropertyValue(propertyName: string, value: Object | undefined): boolean;  差异内容：setPropertyValue(propertyName: string, value: Object | undefined): boolean; | api/graphics3d/SceneResources.d.ts |
| 删除API | 类名：Scene；  API声明：environment: Environment;  差异内容：environment: Environment; | NA | api/graphics3d/Scene.d.ts |
| 删除API | 类名：Scene；  API声明：readonly animations: Animation[];  差异内容：readonly animations: Animation[]; | NA | api/graphics3d/Scene.d.ts |
| 删除API | 类名：Scene；  API声明：readonly root: Node | null;  差异内容：readonly root: Node | null; | NA | api/graphics3d/Scene.d.ts |
| 删除API | 类名：GeometryDefinition；  API声明：readonly geometryType: GeometryType;  差异内容：readonly geometryType: GeometryType; | NA | api/graphics3d/SceneTypes.d.ts |
| 删除API | 类名：CustomGeometry；  API声明：vertices: Vec3[];  差异内容：vertices: Vec3[]; | NA | api/graphics3d/SceneTypes.d.ts |
| 删除API | 类名：CubeGeometry；  API声明：size: Vec3;  差异内容：size: Vec3; | NA | api/graphics3d/SceneTypes.d.ts |
| 删除API | 类名：PlaneGeometry；  API声明：size: Vec2;  差异内容：size: Vec2; | NA | api/graphics3d/SceneTypes.d.ts |
| 删除API | 类名：SphereGeometry；  API声明：radius: number;  差异内容：radius: number; | NA | api/graphics3d/SceneTypes.d.ts |
| 删除API | 类名：SphereGeometry；  API声明：segmentCount: number;  差异内容：segmentCount: number; | NA | api/graphics3d/SceneTypes.d.ts |
