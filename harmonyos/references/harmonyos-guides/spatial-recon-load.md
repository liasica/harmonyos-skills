---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-load
title: 加载3DGS模型
breadcrumb: 指南 > 图形 > Spatial Recon Kit（空间建模服务） > 加载3DGS模型
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:00+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6f0b5055cdd3dd122d3d8b85c5de94103ded42dd6b643371cd44c989f8c9ff1e
---

## 适用场景

支持的3DGS模块格式包括：MP4、PLY、GLB三种格式。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/uzM4TcfBRZOycFM7jQnn7Q/zh-cn_image_0000002712404946.png)

## 接口说明

以下仅列出本指南示例代码中调用的部分主要接口：

| 接口名 | 描述 |
| --- | --- |
| static loadGSNode(scene: [Scene](../harmonyos-references/js-apis-inner-scene.md), params: [GSImportSettings](../harmonyos-references/spatial-recon-spatialrender.md#gsimportsettings), parent?: [Node](../harmonyos-references/js-apis-inner-scene-nodes.md#node)): Promise<[GSNode](../harmonyos-references/spatial-recon-spatialrender.md#gsnode)> | 加载3DGS模型。 |

## 开发步骤

1. 从entry目录进入/src/main/ets/entryability/EntryAbility.ets文件，导入空间建模模块。

   ```typescript
   import { spatialRender } from '@kit.SpatialReconKit';
   import { Scene, RenderContext } from '@kit.ArkGraphics3D'
   ```
2. 加载当前场景的上下文。

   ```typescript
   let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
   ```
3. 调用加载3DGS模型接口。

   ```typescript
   if (renderContext != null) {
     renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
     let scene = Scene.load().then(async (scene: Scene) => {
       let uri = "OhosRawFile://assets/gltf/model.glb"; // 3DGS模型的uri，根据实际情况修改
       let offset = 0;
       let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
     });
   }
   ```
