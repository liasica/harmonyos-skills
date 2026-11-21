---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-load
title: 加载3DGS模型
breadcrumb: 指南 > 图形 > Spatial Recon Kit（空间建模服务） > 加载3DGS模型
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:67ffa023fd957126d099399ad436b269091234a0292ba11e87ba8ba3b791b127
---

## 适用场景

支持的3DGS模块格式包括：MP4、PLY、GLB三种格式。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/EWPdv1puTye90k1QmNeFGg/zh-cn_image_0000002821757743.png?HW-CC-KV=V1&HW-CC-Date=20261121T011047Z&HW-CC-Expire=31536000000&HW-CC-Sign=9299CCD3710D085B617B0D52B915FDC1D9EA8A7599FD0389F3A3FF501B526882)

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
     }.catch((reason: string) => { console.error("Error: " + reason) }));
   }
   ```
