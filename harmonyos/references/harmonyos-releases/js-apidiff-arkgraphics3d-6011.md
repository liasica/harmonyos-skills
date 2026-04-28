---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics3d-6011
title: ArkGraphics 3D
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > ArkGraphics 3D
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:099549b5f765b56882f08431216280de39341dc3fb918e2d41252c24fe290525
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface CameraParameters  差异内容：export interface CameraParameters | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：CameraParameters；  API声明：renderingPipeline?: RenderingPipelineType;  差异内容：renderingPipeline?: RenderingPipelineType; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface EffectParameters  差异内容：export interface EffectParameters | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：EffectParameters；  API声明：effectId: string;  差异内容：effectId: string; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：NodeType；  API声明：CUSTOM = 255  差异内容：CUSTOM = 255 | api/graphics3d/SceneNodes.d.ts |
| 新增API | NA | 类名：SceneResourceType；  API声明：EFFECT = 9  差异内容：EFFECT = 9 | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface Effect  差异内容：export interface Effect | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Effect；  API声明：enabled: boolean;  差异内容：enabled: boolean; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：Effect；  API声明：readonly effectId: string;  差异内容：readonly effectId: string; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum RenderingPipelineType  差异内容：export enum RenderingPipelineType | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：RenderingPipelineType；  API声明：FORWARD\_LIGHTWEIGHT = 0  差异内容：FORWARD\_LIGHTWEIGHT = 0 | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：RenderingPipelineType；  API声明：FORWARD = 1  差异内容：FORWARD = 1 | api/graphics3d/SceneTypes.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SceneResourceFactory；  API声明：createEffect(params: EffectParameters): Promise<Effect>;  差异内容：createEffect(params: EffectParameters): Promise<Effect>; | api/graphics3d/Scene.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Camera；  API声明：renderingPipeline?: RenderingPipelineType;  差异内容：renderingPipeline?: RenderingPipelineType; | api/graphics3d/SceneNodes.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Camera；  API声明：readonly effects: Container<Effect>;  差异内容：readonly effects: Container<Effect>; | api/graphics3d/SceneNodes.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SceneResourceFactory；  API声明：createCamera(params: SceneNodeParameters): Promise<Camera>;  差异内容：createCamera(params: SceneNodeParameters): Promise<Camera>; | 类名：SceneResourceFactory；  API声明：createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>;  差异内容：createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>; | api/graphics3d/Scene.d.ts |
