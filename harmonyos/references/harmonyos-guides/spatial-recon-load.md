---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-load
title: 加载3DGS模型
breadcrumb: 指南 > 图形 > Spatial Recon Kit（空间建模服务） > 加载3DGS模型
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a4e00c43afb7947c06453426cca0876220e33e81b8da1443c9daef079fead680
---

## 适用场景

支持的3DGS模块格式包括：MP4、PLY、GLB三种格式。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eezLPGpUQ7mOxn3jPtMdVw/zh-cn_image_0000002583478735.png?HW-CC-KV=V1&HW-CC-Date=20260427T234750Z&HW-CC-Expire=86400&HW-CC-Sign=9D49B551B9B888F33E5A8DFFD0EE9B5D069CD516D2816AE99982297D3BB7C452)

## 接口说明

以下仅列出本指南示例代码中调用的部分主要接口：

| 接口名 | 描述 |
| --- | --- |
| static loadGSNode(scene: [Scene](../harmonyos-references/js-apis-inner-scene.md), params: [GSImportSettings](../harmonyos-references/spatial-recon-spatialrender.md#gsimportsettings), parent?: [Node](../harmonyos-references/js-apis-inner-scene-nodes.md#node)): Promise<[GSNode](../harmonyos-references/spatial-recon-spatialrender.md#gsnode3dgs渲染对象)> | 加载3DGS模型。 |

## 开发步骤

1. 从entry目录进入/src/main/ets/entryability/EntryAbility.ets文件，导入空间建模模块。

   ```
   1. import { spatialRender } from '@kit.SpatialReconKit';
   2. import { Scene, RenderContext } from '@kit.ArkGraphics3D'
   ```
2. 加载当前场景的上下文。

   ```
   1. let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
   ```
3. 调用加载3DGS模型接口。

   ```
   1. if (renderContext != null) {
   2. renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
   3. let scene = Scene.load().then(async (scene: Scene) => {
   4. let uri = "OhosRawFile://assets/gltf/model.glb"; //3DGS模型的uri，根据实际情况修改
   5. let offset = 0;
   6. let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
   7. });
   8. }
   ```
