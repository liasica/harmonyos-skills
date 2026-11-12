---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-filter
title: 添加滤镜效果
breadcrumb: 指南 > 图形 > Spatial Recon Kit（空间建模服务） > 添加滤镜效果
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:15+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f2bd65fac7b5fc8c8662cac16ae9ded94e61cfab384f9b7dabb0fa190195cfaf
---

为3DGS模型渲染画面添加风格化滤镜，包括：复古滤镜、漫画风格、黑白bit效果、颜色编辑。

## 接口说明

以下仅列出本指南示例代码中调用的部分主要接口：

| 接口名 | 描述 |
| --- | --- |
| RETRO\_EFFECT\_ID | 表示复古效果对应的ID。 |
| COMIC\_EFFECT\_ID | 表示漫画效果对应的ID。 |
| OBRA\_DINN\_EFFECT\_ID | 表示黑白bit效果对应的ID。 |
| COLOR\_EDITING\_EFFECT\_ID | 表示颜色编辑效果对应的ID。 |

## 开发步骤

1. 首先从项目根目录进入/src/main/ets/entryability/EntryAbility.ets文件，导入空间建模模块。

   ```typescript
   import { Scene, RenderContext } from '@kit.ArkGraphics3D';
   import { spatialRender } from '@kit.SpatialReconKit';
   import { RenderingPipelineType } from '@ohos.graphics.scene'
   ```
2. 加载当前场景的上下文。

   ```typescript
   let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
   ```
3. 调用滤镜接口。

   ```typescript
   if (renderContext != null) {
     renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
     Scene.load().then(async (scene: Scene) => {
       let rf = scene.getResourceFactory();
       let effect : spatialRender.RetroEffect =
         await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO_EFFECT_ID }) as spatialRender.RetroEffect;
       let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
       camera.effects.append(effect)
     }).catch((reason: string) => { console.error("Error: " + reason) }));
   }
   ```
