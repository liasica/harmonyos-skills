---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics3d-510
title: ArkGraphics 3D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > ArkGraphics 3D
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:363e4ee0850e04c9bec7be7828eb99976731938476c45816cd5a92ce8eb5264d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface BloomSettings  差异内容：export interface BloomSettings | api/graphics3d/ScenePostProcessSettings.d.ts |
| 新增API | NA | 类名：BloomSettings；  API声明：thresholdHard?: number;  差异内容：thresholdHard?: number; | api/graphics3d/ScenePostProcessSettings.d.ts |
| 新增API | NA | 类名：BloomSettings；  API声明：thresholdSoft?: number;  差异内容：thresholdSoft?: number; | api/graphics3d/ScenePostProcessSettings.d.ts |
| 新增API | NA | 类名：BloomSettings；  API声明：scaleFactor?: number;  差异内容：scaleFactor?: number; | api/graphics3d/ScenePostProcessSettings.d.ts |
| 新增API | NA | 类名：BloomSettings；  API声明：scatter?: number;  差异内容：scatter?: number; | api/graphics3d/ScenePostProcessSettings.d.ts |
| 新增API | NA | 类名：SceneResourceType；  API声明：MESH\_RESOURCE = 8  差异内容：MESH\_RESOURCE = 8 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface MeshResource  差异内容：export interface MeshResource | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum GeometryType  差异内容：export enum GeometryType | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：GeometryType；  API声明：CUSTOM = 0  差异内容：CUSTOM = 0 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：GeometryType；  API声明：CUBE = 1  差异内容：CUBE = 1 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：GeometryType；  API声明：PLANE = 2  差异内容：PLANE = 2 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：GeometryType；  API声明：SPHERE = 3  差异内容：SPHERE = 3 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export abstract class GeometryDefinition  差异内容：export abstract class GeometryDefinition | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：GeometryDefinition；  API声明：readonly geometryType: GeometryType;  差异内容：readonly geometryType: GeometryType; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum PrimitiveTopology  差异内容：export enum PrimitiveTopology | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：PrimitiveTopology；  API声明：TRIANGLE\_LIST = 0  差异内容：TRIANGLE\_LIST = 0 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：PrimitiveTopology；  API声明：TRIANGLE\_STRIP = 1  差异内容：TRIANGLE\_STRIP = 1 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export class CustomGeometry  差异内容：export class CustomGeometry | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：topology?: PrimitiveTopology;  差异内容：topology?: PrimitiveTopology; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：vertices: Vec3[];  差异内容：vertices: Vec3[]; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：indices?: number[];  差异内容：indices?: number[]; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：normals?: Vec3[];  差异内容：normals?: Vec3[]; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：uvs?: Vec2[];  差异内容：uvs?: Vec2[]; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CustomGeometry；  API声明：colors?: Color[];  差异内容：colors?: Color[]; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export class CubeGeometry  差异内容：export class CubeGeometry | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：CubeGeometry；  API声明：size: Vec3;  差异内容：size: Vec3; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export class PlaneGeometry  差异内容：export class PlaneGeometry | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：PlaneGeometry；  API声明：size: Vec2;  差异内容：size: Vec2; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：global；  API声明：export class SphereGeometry  差异内容：export class SphereGeometry | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：SphereGeometry；  API声明：radius: number;  差异内容：radius: number; | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：SphereGeometry；  API声明：segmentCount: number;  差异内容：segmentCount: number; | api/graphics3d/SceneTypes.d.ts |
| 起始版本有变化 | 类名：global；  API声明：export interface RenderParameters  差异内容：15 | 类名：global；  API声明：export interface RenderParameters  差异内容：18 | api/graphics3d/Scene.d.ts |
| 起始版本有变化 | 类名：RenderParameters；  API声明：alwaysRender?: boolean;  差异内容：15 | 类名：RenderParameters；  API声明：alwaysRender?: boolean;  差异内容：18 | api/graphics3d/Scene.d.ts |
| 起始版本有变化 | 类名：Scene；  API声明：renderFrame(params?: RenderParameters): boolean;  差异内容：15 | 类名：Scene；  API声明：renderFrame(params?: RenderParameters): boolean;  差异内容：18 | api/graphics3d/Scene.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Scene；  API声明：importNode(name: string, node: Node, parent: Node | null): Node;  差异内容：importNode(name: string, node: Node, parent: Node | null): Node; | api/graphics3d/Scene.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Scene；  API声明：importScene(name: string, scene: Scene, parent: Node | null): Node;  差异内容：importScene(name: string, scene: Scene, parent: Node | null): Node; | api/graphics3d/Scene.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SceneResourceFactory；  API声明：createGeometry(params: SceneNodeParameters, mesh: MeshResource): Promise<Geometry>;  差异内容：createGeometry(params: SceneNodeParameters, mesh: MeshResource): Promise<Geometry>; | api/graphics3d/Scene.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SceneResourceFactory；  API声明：createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>;  差异内容：createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>; | api/graphics3d/Scene.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SceneResourceFactory；  API声明：createScene(uri?: ResourceStr): Promise<Scene>;  差异内容：createScene(uri?: ResourceStr): Promise<Scene>; | api/graphics3d/Scene.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PostProcessSettings；  API声明：bloom?: BloomSettings;  差异内容：bloom?: BloomSettings; | api/graphics3d/ScenePostProcessSettings.d.ts |
