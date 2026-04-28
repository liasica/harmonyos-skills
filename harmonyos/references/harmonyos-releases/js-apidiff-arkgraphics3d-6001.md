---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics3d-6001
title: ArkGraphics 3D
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > ArkGraphics 3D
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0dc7ccc0629c34b1f62c605b35c1fe8153776b586137a011500fd2a6a63376bf
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface RaycastResult  差异内容：export interface RaycastResult | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RaycastResult；  API声明：node: Node;  差异内容：node: Node; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RaycastResult；  API声明：centerDistance: number;  差异内容：centerDistance: number; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RaycastResult；  API声明：hitPosition: Position3;  差异内容：hitPosition: Position3; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface RaycastParameters  差异内容：export interface RaycastParameters | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RaycastParameters；  API声明：rootNode?: Node;  差异内容：rootNode?: Node; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface RenderResourceFactory  差异内容：export interface RenderResourceFactory | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RenderResourceFactory；  API声明：createSampler(params: SceneResourceParameters): Promise<Sampler>;  差异内容：createSampler(params: SceneResourceParameters): Promise<Sampler>; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SceneComponent  差异内容：export interface SceneComponent | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：SceneComponent；  API声明：name: string;  差异内容：name: string; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：SceneComponent；  API声明：readonly property: Record<string, string | number | Vec2 | Vec3 | Vec4 | SceneResource | boolean | number[] | string[] | SceneResource[] | Vec2[] | Vec3[] | Vec4[] | null | undefined>;  差异内容：readonly property: Record<string, string | number | Vec2 | Vec3 | Vec4 | SceneResource | boolean | number[] | string[] | SceneResource[] | Vec2[] | Vec3[] | Vec4[] | null | undefined>; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface RenderContext  差异内容：export interface RenderContext | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RenderContext；  API声明：getRenderResourceFactory(): RenderResourceFactory;  差异内容：getRenderResourceFactory(): RenderResourceFactory; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RenderContext；  API声明：loadPlugin(name: string): Promise<boolean>;  差异内容：loadPlugin(name: string): Promise<boolean>; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：MaterialType；  API声明：METALLIC\_ROUGHNESS = 2  差异内容：METALLIC\_ROUGHNESS = 2 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum CullMode  差异内容：export enum CullMode | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：CullMode；  API声明：NONE = 0  差异内容：NONE = 0 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：CullMode；  API声明：FRONT = 1  差异内容：FRONT = 1 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：CullMode；  API声明：BACK = 2  差异内容：BACK = 2 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Blend  差异内容：export interface Blend | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Blend；  API声明：enabled: boolean;  差异内容：enabled: boolean; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface RenderSort  差异内容：export interface RenderSort | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：RenderSort；  API声明：renderSortLayer?: number;  差异内容：renderSortLayer?: number; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：RenderSort；  API声明：renderSortLayerOrder?: number;  差异内容：renderSortLayerOrder?: number; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface MaterialProperty  差异内容：export interface MaterialProperty | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MaterialProperty；  API声明：image: Image | null;  差异内容：image: Image | null; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MaterialProperty；  API声明：factor: Vec4;  差异内容：factor: Vec4; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MaterialProperty；  API声明：sampler?: Sampler;  差异内容：sampler?: Sampler; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface MetallicRoughnessMaterial  差异内容：export interface MetallicRoughnessMaterial | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：baseColor: MaterialProperty;  差异内容：baseColor: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：normal: MaterialProperty;  差异内容：normal: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：material: MaterialProperty;  差异内容：material: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：ambientOcclusion: MaterialProperty;  差异内容：ambientOcclusion: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：emissive: MaterialProperty;  差异内容：emissive: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：clearCoat: MaterialProperty;  差异内容：clearCoat: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：clearCoatRoughness: MaterialProperty;  差异内容：clearCoatRoughness: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：clearCoatNormal: MaterialProperty;  差异内容：clearCoatNormal: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：sheen: MaterialProperty;  差异内容：sheen: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：MetallicRoughnessMaterial；  API声明：specular: MaterialProperty;  差异内容：specular: MaterialProperty; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum SamplerFilter  差异内容：export enum SamplerFilter | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：SamplerFilter；  API声明：NEAREST = 0  差异内容：NEAREST = 0 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：SamplerFilter；  API声明：LINEAR = 1  差异内容：LINEAR = 1 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum SamplerAddressMode  差异内容：export enum SamplerAddressMode | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：SamplerAddressMode；  API声明：REPEAT = 0  差异内容：REPEAT = 0 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：SamplerAddressMode；  API声明：MIRRORED\_REPEAT = 1  差异内容：MIRRORED\_REPEAT = 1 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：SamplerAddressMode；  API声明：CLAMP\_TO\_EDGE = 2  差异内容：CLAMP\_TO\_EDGE = 2 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Sampler  差异内容：export interface Sampler | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Sampler；  API声明：magFilter?: SamplerFilter;  差异内容：magFilter?: SamplerFilter; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Sampler；  API声明：minFilter?: SamplerFilter;  差异内容：minFilter?: SamplerFilter; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Sampler；  API声明：mipMapMode?: SamplerFilter;  差异内容：mipMapMode?: SamplerFilter; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Sampler；  API声明：addressModeU?: SamplerAddressMode;  差异内容：addressModeU?: SamplerAddressMode; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Sampler；  API声明：addressModeV?: SamplerAddressMode;  差异内容：addressModeV?: SamplerAddressMode; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Morpher  差异内容：export interface Morpher | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Morpher；  API声明：readonly targets: Record<string, number>;  差异内容：readonly targets: Record<string, number>; | api/graphics3d/SceneResources.d.ts |
| 成员由子类迁移至父类 | 类名：SceneResourceFactory；  API声明：createShader(params: SceneResourceParameters): Promise<Shader>;  差异内容：createShader(params: SceneResourceParameters): Promise<Shader>; | 类名：RenderResourceFactory；  API声明：createShader(params: SceneResourceParameters): Promise<Shader>;  差异内容：createShader(params: SceneResourceParameters): Promise<Shader>; | api/graphics3d/Scene.d.ts |
| 成员由子类迁移至父类 | 类名：SceneResourceFactory；  API声明：createImage(params: SceneResourceParameters): Promise<Image>;  差异内容：createImage(params: SceneResourceParameters): Promise<Image>; | 类名：RenderResourceFactory；  API声明：createImage(params: SceneResourceParameters): Promise<Image>;  差异内容：createImage(params: SceneResourceParameters): Promise<Image>; | api/graphics3d/Scene.d.ts |
| 成员由子类迁移至父类 | 类名：SceneResourceFactory；  API声明：createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>;  差异内容：createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>; | 类名：RenderResourceFactory；  API声明：createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>;  差异内容：createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>; | api/graphics3d/Scene.d.ts |
| 成员由子类迁移至父类 | 类名：SceneResourceFactory；  API声明：createScene(uri?: ResourceStr): Promise<Scene>;  差异内容：createScene(uri?: ResourceStr): Promise<Scene>; | 类名：RenderResourceFactory；  API声明：createScene(uri?: ResourceStr): Promise<Scene>;  差异内容：createScene(uri?: ResourceStr): Promise<Scene>; | api/graphics3d/Scene.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Scene；  API声明：static getDefaultRenderContext(): RenderContext | null;  差异内容：static getDefaultRenderContext(): RenderContext | null; | api/graphics3d/Scene.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Scene；  API声明：createComponent(node: Node, name: string): Promise<SceneComponent>;  差异内容：createComponent(node: Node, name: string): Promise<SceneComponent>; | api/graphics3d/Scene.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Scene；  API声明：getComponent(node: Node, name: string): SceneComponent | null;  差异内容：getComponent(node: Node, name: string): SceneComponent | null; | api/graphics3d/Scene.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Camera；  API声明：raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>;  差异内容：raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>; | api/graphics3d/SceneNodes.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Geometry；  API声明：readonly morpher?: Morpher;  差异内容：readonly morpher?: Morpher; | api/graphics3d/SceneNodes.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Material；  API声明：shadowReceiver?: boolean;  差异内容：shadowReceiver?: boolean; | api/graphics3d/SceneResources.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Material；  API声明：cullMode?: CullMode;  差异内容：cullMode?: CullMode; | api/graphics3d/SceneResources.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Material；  API声明：blend?: Blend;  差异内容：blend?: Blend; | api/graphics3d/SceneResources.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Material；  API声明：alphaCutoff?: number;  差异内容：alphaCutoff?: number; | api/graphics3d/SceneResources.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Material；  API声明：renderSort?: RenderSort;  差异内容：renderSort?: RenderSort; | api/graphics3d/SceneResources.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Animation；  API声明：speed?: number;  差异内容：speed?: number; | api/graphics3d/SceneResources.d.ts |
