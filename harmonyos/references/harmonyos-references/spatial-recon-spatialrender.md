---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialrender
title: spatialRender
breadcrumb: API参考 > 图形 > Spatial Recon Kit（空间建模服务） > ArkTS API > spatialRender
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e736d4f09c312ef26e360da1be1d611295e3febb0296c5d7083b483c2f79f753
---

spatialRender模块主要用于渲染3DGS数据，展示3DGS渲染场景。

**起始版本：** 6.0.1(21)

## 导入模块

```typescript
import { spatialRender } from '@kit.SpatialReconKit';
```

## GSNode

表示一个3DGS（3D Gaussian Splatting）渲染对象，帮助开发者操作3DGS模型。GSNode类继承自[Node](js-apis-inner-scene-nodes.md#node)，使用方法请参考Node。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

**示例：**

```typescript
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/model.glb";
    let offset = 0;
    
    // 通过GSPlugin.loadGSNode获取GSNode实例
    let gsNode: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, { uri, offset }, scene.root);
    
    // 设置节点位置
    gsNode.position = { x: 3, y: 0, z: 0 };
    // 设置节点缩放
    gsNode.scale = { x: 1.5, y: 1.5, z: 1.5 };
    // 设置节点可见性
    gsNode.visible = true;
  });
}
```

## TiledGSNode

表示一个分块3DGS（Tiled 3D Gaussian Splatting）渲染对象，专门用于加载和渲染大规模的3DGS场景。TiledGSNode类继承自[Node](js-apis-inner-scene-nodes.md#node)，使用方法请参考Node。

### setCamera

setCamera(camera: Camera): void

设置驱动分块选择的相机。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | [Camera](js-apis-inner-scene-nodes.md#camera) | 是 | 驱动分块选择的相机。默认使用渲染当前场景的相机，可以设置其他的相机。 |

**示例：**

```typescript
import { Scene, RenderContext, Camera, Node } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    if (!scene.root) {
      return;
    }
    let root: Node = scene.root as Node;

    // 创建相机
    let srf = scene.getResourceFactory();
    let camera: Camera = await srf.createCamera({ name: "Camera1", path: root.path });
    camera.clearColor = { r: 202/255.0, g: 233/255.0, b: 246/255.0, a: 1.0 };
    camera.nearPlane = 0.5;
    camera.farPlane = 10000.0;
    let PI = 3.141592653;
    let DEG2RAD = PI * 2.0 / 360.0;
    camera.fov = 60.0 * DEG2RAD;
    camera.enabled = true;

    // 配置分块3DGS导入参数
    let params: spatialRender.TiledGSImportSettings = {
      uri: "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json"
    };

    // 加载分块3DGS模型
    let promise = spatialRender.GSPlugin.loadTiledGSNode(scene, params, root);
    promise.then((tiledGSNode: spatialRender.TiledGSNode) => {
      if (!camera) {
        return;
      }
      // 设置驱动分块选择的相机
      tiledGSNode.setCamera(camera);
      // 设置节点属性
      tiledGSNode.position = { x: 0, y: 0, z: 0 };
      tiledGSNode.scale = { x: 1, y: 1, z: 1 };
      tiledGSNode.visible = true;
    });
  });
}
```

### setTileRequestCallback

setTileRequestCallback(callback: GSTileRequestCallback | null): void

设置瓦片请求回调函数，当渲染器需要应用程序提供瓦片数据时，会调用该回调。该回调接收应用程序应加载的瓦片（文件）列表。使用callback异步回调。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GSTileRequestCallback](spatial-recon-spatialrender.md#gstilerequestcallback) | 是 | 回调函数。当渲染器请求瓦片时触发成功，返回渲染器向应用请求的[GSTile](spatial-recon-spatialrender.md#gstile)瓦片列表；否则为错误对象。 |

**示例：**

```typescript
import { Scene, RenderContext, Camera, Node } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    if (!scene.root) {
      return;
    }
    let root: Node = scene.root as Node;

    // 创建相机
    let srf = scene.getResourceFactory();
    let camera: Camera = await srf.createCamera({ name: "Camera1", path: root.path });
    camera.clearColor = { r: 202/255.0, g: 233/255.0, b: 246/255.0, a: 1.0 };
    camera.nearPlane = 0.5;
    camera.farPlane = 10000.0;
    let PI = 3.141592653;
    let DEG2RAD = PI * 2.0 / 360.0;
    camera.fov = 60.0 * DEG2RAD;
    camera.enabled = true;

    // 配置分块3DGS导入参数
    let params: spatialRender.TiledGSImportSettings = {
      uri: "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json"
    };

    // 加载分块3DGS模型
    let promise = spatialRender.GSPlugin.loadTiledGSNode(scene, params, root);
    promise.then((tiledGSNode: spatialRender.TiledGSNode) => {
      if (!camera) {
        return;
      }
      // 设置驱动分块选择的相机
      tiledGSNode.setCamera(camera);
      // 设置节点属性
      tiledGSNode.position = { x: 0, y: 0, z: 0 };
      tiledGSNode.scale = { x: 1, y: 1, z: 1 };
      tiledGSNode.visible = true;
      // 向渲染器注册瓦片请求回调
      tiledGSNode.setTileRequestCallback((tiles: spatialRender.GSTile[]) => {
        // 获取并保存远端瓦片数据，然后通知渲染器瓦片准备就绪
        if (!tiles || tiles.length <= 0) {
          return;
        }
      });
    });
  });
}
```

### notifyTileReady

notifyTileReady(tile: GSTile): void

通知渲染器指定的瓦片现在可以加载。[tile.uri](spatial-recon-spatialrender.md#gstile)相对路径指向的文件已可访问，并可被渲染器读取。如果渲染器不再需要该瓦片（例如在获取完成前相机已移开），该调用将不执行任何操作。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tile | [GSTile](spatial-recon-spatialrender.md#gstile) | 是 | 数据可用的瓦片。 |

**示例：**

```typescript
import { Scene, RenderContext, Camera, Node } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    if (!scene.root) {
      return;
    }
    let root: Node = scene.root as Node;

    // 创建相机
    let srf = scene.getResourceFactory();
    let camera: Camera = await srf.createCamera({ name: "Camera1", path: root.path });
    camera.clearColor = { r: 202/255.0, g: 233/255.0, b: 246/255.0, a: 1.0 };
    camera.nearPlane = 0.5;
    camera.farPlane = 10000.0;
    let PI = 3.141592653;
    let DEG2RAD = PI * 2.0 / 360.0;
    camera.fov = 60.0 * DEG2RAD;
    camera.enabled = true;

    // 配置分块3DGS导入参数
    let params: spatialRender.TiledGSImportSettings = {
      uri: "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json"
    };

    // 加载分块3DGS模型
    let promise = spatialRender.GSPlugin.loadTiledGSNode(scene, params, root);
    promise.then((tiledGSNode: spatialRender.TiledGSNode) => {
      if (!camera) {
        return;
      }
      // 设置驱动分块选择的相机
      tiledGSNode.setCamera(camera);
      // 设置节点属性
      tiledGSNode.position = { x: 0, y: 0, z: 0 };
      tiledGSNode.scale = { x: 1, y: 1, z: 1 };
      tiledGSNode.visible = true;
      // 向渲染器注册瓦片请求回调
      tiledGSNode.setTileRequestCallback((tiles: spatialRender.GSTile[]) => {
        if (!tiles || tiles.length <= 0) {
          return;
        }
        for (const tile of tiles) {
          // 向远端请求获取瓦片数据，并持久化保存至uri指定相对路径
          // ......
          // 通知渲染器某个瓦片数据准备就绪
          tiledGSNode..notifyTileReady(tile);
        }
      });
    });
  });
}
```

## GSPlugin

GSPlugin类封装了与3DGS相关的内容，包括3DGS插件ID和3DGS模型加载接口，帮助开发者实现对3DGS的自定义功能。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

**注意** 

调用GSPlugin接口前，必须先加载对应的插件ID，否则会出现未定义的行为。

**示例：**

```typescript
import { spatialRender } from '@kit.SpatialReconKit';
import { Scene } from '@kit.ArkGraphics3D';

// 获取默认渲染上下文
let renderContext = Scene.getDefaultRenderContext();
if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
}
```

### 常量

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| PLUGIN\_ID | string | 表示3DGS插件ID。使用前需调用[renderContext.loadPlugin](js-apis-inner-scene.md#loadplugin20)(GSPlugin.PLUGIN\_ID)加载插件。 |
| RETRO\_EFFECT\_ID | string | 表示复古效果ID。需先加载PLUGIN\_ID，然后作为[EffectParameters](js-apis-inner-scene.md#effectparameters21).effectId传入[createEffect](js-apis-inner-scene.md#createeffect21)创建效果实例。 |
| COMIC\_EFFECT\_ID | string | 表示漫画效果ID。需先加载PLUGIN\_ID，然后作为EffectParameters.effectId传入createEffect创建效果实例。 |
| OBRA\_DINN\_EFFECT\_ID | string | 表示黑白bit效果ID。需先加载PLUGIN\_ID，然后作为EffectParameters.effectId传入createEffect创建效果实例。 |
| COLOR\_EDITING\_EFFECT\_ID | string | 表示颜色编辑效果ID。需先加载PLUGIN\_ID，然后作为EffectParameters.effectId传入createEffect创建效果实例。 |

开发者不需要感知各ID的具体值，推荐直接使用字符串变量。

### loadGSNode

static loadGSNode(scene: Scene, params: GSImportSettings, parent?: Node): Promise<GSNode>

加载3DGS模型，使用Promise异步回调。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | [Scene](js-apis-inner-scene.md) | 是 | 指定在应用界面想要显示的场景，是ArkGraphics 3D基础模块。建议通过调用[Scene.load](js-apis-inner-scene.md#load)来获取。 |
| params | [GSImportSettings](spatial-recon-spatialrender.md#gsimportsettings) | 是 | 加载3DGS模型的设置。 |
| parent | [Node](js-apis-inner-scene-nodes.md#node) | 否 | 预期挂载3DGS模型的节点。如果不传，加载的3DGS模型会被挂载到Scene的根节点上。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GSNode](spatial-recon-spatialrender.md#gsnode)> | Promise对象，返回3DGS模型对应的GSNode。 |

**示例：**

```typescript
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  let scene = Scene.load().then(async (scene: Scene) => {
    // 设置3DGS模型文件的URI路径，根据实际情况修改
    let uri = "OhosRawFile://assets/gltf/model.glb";
    // 偏移量参数（用于模型的位移调整，可根据需求设置）
    let offset = 0;
    // 通过GSPlugin加载指定的3DGS节点，并将其添加到场景根节点下
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
  });
}
```

### loadTiledGSNode

static loadTiledGSNode(scene: Scene, params: TiledGSImportSettings, parent?: Node): Promise<TiledGSNode>

加载分块3DGS模型，使用Promise异步回调。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | [Scene](js-apis-inner-scene.md) | 是 | 指定在应用界面想要显示的场景，是ArkGraphics 3D基础模块。建议通过调用[Scene.load](js-apis-inner-scene.md#load)来获取。 |
| params | [TiledGSImportSettings](spatial-recon-spatialrender.md#tiledgsimportsettings) | 是 | 加载分块3DGS模型的设置。 |
| parent | [Node](js-apis-inner-scene-nodes.md#node) | 否 | 预期挂载分块3DGS模型的节点。如果不传，加载的分块3DGS模型会被挂载到Scene的根节点上。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TiledGSNode](spatial-recon-spatialrender.md#tiledgsnode)> | Promise对象，返回分块3DGS模型对应的TiledGSNode。 |

**示例：**

```typescript
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  let scene = Scene.load().then(async (scene: Scene) => {
    // 设置分块3DGS模型清单文件的URI路径，根据实际情况修改
    let uri = "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json";
    // 通过GSPlugin加载指定的分块3DGS节点，并将其添加到场景根节点下
    let tiledGSNode: spatialRender.TiledGSNode = await spatialRender.GSPlugin.loadTiledGSNode(scene, { uri }, scene.root);
  });
}
```

## GSImportSettings

GSImportSettings类封装了加载3DGS模型的设置，包括模型路径和数据在文件中的偏移量。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 3DGS模型的文件路径。传入空字符串将导致加载失败。 |
| offset | number | 否 | 是 | 待加载数据在3DGS模型文件中的偏移量。默认值0。 |

**示例：**

```typescript
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  let scene = Scene.load().then(async (scene: Scene) => {
    // 设置3DGS模型文件的URI路径，根据实际情况修改
    let uri = "OhosRawFile://assets/gltf/doll.glb";
    // 偏移量参数（用于模型的位移调整）
    let offset = 0;
    // 配置导入参数
    let setting: spatialRender.GSImportSettings = { uri: uri, offset : offset};
    // 通过GSPlugin加载指定的3DGS节点，并添加到场景根节点下
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, setting, scene.root);
  });
}
```

## TiledGSImportSettings

TiledGSImportSettings类封装了加载分块3DGS模型的设置，包含清单文件路径。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 分块3DGS模型清单文件（JSON）的路径，用于描述瓦片层级结构。传入空字符串将导致加载失败。 |

**示例：**

```typescript
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  let scene = Scene.load().then(async (scene: Scene) => {
    // 设置分块3DGS模型清单文件的URI路径，根据实际情况修改
    let uri = "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json";
    // 配置导入参数
    let setting: spatialRender.TiledGSImportSettings = { uri: uri };
    // 通过GSPlugin加载指定的分块3DGS节点，并添加到场景根节点下
    let tiledGSNode: spatialRender.TiledGSNode = await spatialRender.GSPlugin.loadTiledGSNode(scene, setting, scene.root);
  });
}
```

## RetroEffectParams

RetroEffect参数，该类型为字符串枚举，该枚举值可在[Effect](js-apis-inner-scene-resources.md#effect21)的[getPropertyValue](js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.SpatialRender

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR\_NUM | 'colorNum' | RetroEffect中colorNum属性的名称。  属性对应取值类型为number。该属性表示使用多少种颜色来作为颜色抖动。通常属性值越大图像质量越高、值越小复古风格越重。属性取值范围大于0，默认值8。 |
| PIXEL\_SIZE | 'pixelSize' | RetroEffect中pixelSize属性的名称。  属性对应取值类型为number。该属性表示下采样的程度。越大越重。若该属性取值为1，则不会进行下采样。属性取值范围大于等于1，默认值4。 |
| BLEND\_ENABLED | 'blendEnabled' | RetroEffect中blendEnabled属性的名称。  属性对应取值类型为boolean。该属性表示是否把处理后的图片与原始图片融合，属性值设置为true会把处理后的图片与原始图片融合，设置为false不会做融合。由于复古风格会造成图像的亮度下降、色彩偏移，将该属性值设为true用以维持图像的亮度与色彩。属性取值默认为true。 |
| CURVE | 'curve' | RetroEffect中curve属性的名称。  属性对应取值类型为number。该属性表示显像管电视屏幕带有的曲率。复古风格会模拟显像管电视的显示特征。该属性代表显像管电视屏幕带有的曲率，属性取值越大曲率越大。属性取值范围[0, 1]，默认值0.25。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建复古效果实例（使用GSPlugin预定义的效果ID）
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO_EFFECT_ID });
    // 获取复古效果参数（颜色数量）的当前值
    let colNum = effect.getPropertyValue(spatialRender.RetroEffectParams.COLOR_NUM);
    // 设置复古效果参数（颜色数量）为4
    let res = effect.setPropertyValue(spatialRender.RetroEffectParams.COLOR_NUM, 4);
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## RetroEffect

RetroEffect接口封装了复古风格的效果参数，可实现自定义的复古风格。该类继承自[Effect](js-apis-inner-scene-resources.md#effect21)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorNum | number | 否 | 否 | 使用多少种颜色来作为颜色抖动。通常值越大图像质量越高、值越小复古风格越重。取值范围大于0。默认值8。 |
| pixelSize | number | 否 | 否 | 下采样的程度。越大越重。若为1，则不会进行下采样。取值范围大于等于1。默认值4。 |
| blendEnabled | boolean | 否 | 否 | 是否把处理后的图片与原始图片融合，设置为true会把处理后的图片与原始图片融合，设置为false不会做融合。复古风格会造成图像的亮度下降、色彩偏移。设为true用以维持图像的亮度与色彩。默认值true。 |
| curve | number | 否 | 否 | 显像管电视屏幕带有的曲率。复古风格会模拟显像管电视的显示特征，  curve代表显像管电视屏幕带有的曲率，值越大曲率越大。取值范围[0, 1]。默认值0.25。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建复古效果实例（类型为RetroEffect）
    let effect : spatialRender.RetroEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO_EFFECT_ID }) as spatialRender.RetroEffect;
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## ComicEffectParams

ComicEffect参数，该类型为字符串枚举，该枚举值可在[Effect](js-apis-inner-scene-resources.md#effect21)的[getPropertyValue](js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.SpatialRender

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINE\_THRESHOLD | 'lineThreshold' | ComicEffect中lineThreshold属性的名称。  属性对应取值类型为number。该属性表示用来判定像素为轮廓线的阈值，图像梯度大于该阈值的像素会被判定为轮廓线。该属性取值范围[0, 1]，默认值为0.2。 |
| LINE\_COLOR | 'lineColor' | ComicEffect中lineThreshold属性的名称。  属性对应取值类型为[Color](js-apis-inner-scene-types.md#color)。该属性表示轮廓线的颜色。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建漫画效果实例（使用GSPlugin预定义的漫画效果ID）
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COMIC_EFFECT_ID });
    // 获取漫画效果参数（线条阈值）的当前值
    let threshold = effect.getPropertyValue(spatialRender.ComicEffectParams.LINE_THRESHOLD);
    // 设置漫画效果参数（线条阈值）为0.5
    let res = effect.setPropertyValue(spatialRender.ComicEffectParams.LINE_THRESHOLD, 0.5);
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将漫画效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## ComicEffect

ComicEffect接口封装了漫画风格的效果的参数，可实现自定义的漫画风格。该类继承自[Effect](js-apis-inner-scene-resources.md#effect21)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lineThreshold | number | 否 | 否 | 判定像素为轮廓线的阈值。图像梯度（像素与相邻像素的明暗差异。差异越大，梯度值越大，该像素越可能是轮廓线）大于该阈值的像素会被判定为轮廓线。取值范围[0, 1] ，默认值0.2。 |
| lineColor | [Color](js-apis-inner-scene-types.md#color) | 否 | 否 | 轮廓线的颜色。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建漫画效果实例（类型为ComicEffect）
    let effect : spatialRender.ComicEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COMIC_EFFECT_ID }) as spatialRender.ComicEffect;
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将漫画效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## ObraDinnEffectParams

ObraDinnEffect参数，该类型为字符串枚举，该枚举值可在[Effect](js-apis-inner-scene-resources.md#effect21)的[getPropertyValue](js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.SpatialRender

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOISE\_STRENGTH | 'noiseStrength' | ObraDinnEffect中的noiseStrength属性的名称。  属性对应取值类型为number。该属性表示选择哪些像素用来颜色抖动。该属性可以起到平滑边缘的效果，加大噪声强度会导致边缘更模糊。属性取值范围[0, 1]，默认值0.3。 |
| THRESHOLD | 'threshold' | ObraDinnEffect中的threshold属性的名称。  属性对应取值类型为number。该属性表示将像素分为前景颜色或后景颜色的阈值。该属性取值越高，图像整体的颜色会越接近后景颜色。属性值取值范围[0, 1]，默认值0.4。 |
| FOREGROUND\_COLOR | 'foregroundColor' | ObraDinnEffect中的foregroundColor属性的名称。  属性对应取值类型为[Color](js-apis-inner-scene-types.md#color)。该属性表示前景颜色。 |
| BACKGROUND\_COLOR | 'backgroundColor' | ObraDinnEffect中的backgroundColor属性的名称。  属性对应取值类型为[Color](js-apis-inner-scene-types.md#color)。该属性表示背景颜色。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建黑白bit效果实例（使用GSPlugin预定义的效果ID）
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.OBRA_DINN_EFFECT_ID });
    // 获取黑白bit效果参数（噪声强度）的当前值
    let noiseStrength = effect.getPropertyValue(spatialRender.ObraDinnEffectParams.NOISE_STRENGTH);
    // 设置黑白bit效果参数（噪声强度）为0.5
    let res = effect.setPropertyValue(spatialRender.ObraDinnEffectParams.NOISE_STRENGTH, 0.5);
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将黑白bit效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## ObraDinnEffect

ObraDinnEffect接口封装了bit（黑白点阵）风格的效果参数，可实现自定义的bit风格。该类继承自[Effect](js-apis-inner-scene-resources.md#effect21)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| noiseStrength | number | 否 | 否 | 选择哪些像素用来颜色抖动。可以起到平滑边缘的效果。加大噪声强度会导致边缘更模糊。取值范围[0, 1]，默认值0.3。 |
| threshold | number | 否 | 否 | 把像素分为前景颜色或后景颜色的阈值。高于该阈值的像素会被处理为前景颜色。threshold越低，图像整体的颜色会越接近前景颜色。threshold越高，图像整体的颜色会越接近后景颜色。取值范围[0, 1]，默认值0.4。 |
| foregroundColor | [Color](js-apis-inner-scene-types.md#color) | 否 | 否 | 前景颜色。 |
| backgroundColor | [Color](js-apis-inner-scene-types.md#color) | 否 | 否 | 背景颜色。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建黑白bit效果实例（类型为ObraDinnEffect）
    let effect : spatialRender.ObraDinnEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.OBRA_DINN_EFFECT_ID }) as spatialRender.ObraDinnEffect;
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将黑白bit效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## ColorEditingEffectParams

ColorEditingEffect参数，该类型为字符串枚举，该枚举值可在[Effect](js-apis-inner-scene-resources.md#effect21)的[getPropertyValue](js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.SpatialRender

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXPOSURE | 'exposure' | ColorEditingEffect中的exposure属性的名称。  属性对应取值类型为number。该属性表示图像的曝光度。属性推荐取值范围[-5, 5]，默认值0.0。 |
| CONTRAST | 'contrast' | ColorEditingEffect中的contrast属性的名称。  属性对应取值类型为number。该属性表示图像的对比度。属性推荐取值范围[0, 2]，默认值1.0。 |
| TEMPERATURE | 'temperature' | ColorEditingEffect中的temperature属性的名称。  属性对应取值类型为number。该属性表示图像的色温。属性推荐取值范围[-2, 2]，默认值0.0。 |
| TINT | 'tint' | ColorEditingEffect中的tint属性的名称。  属性对应取值类型为number。该属性表示图像的色调。属性推荐取值范围[-1, 1]，默认值0.0。 |
| SATURATION | 'saturation' | ColorEditingEffect中的saturation属性的名称。  属性对应取值类型为number。该属性表示图像的饱和度。属性推荐取值范围[0, 2]，默认值1.0。 |
| VIBRANCE | 'vibrance' | ColorEditingEffect中的vibrance属性的名称。  属性对应取值类型为number。该属性表示图像的自然饱和度。属性推荐取值范围[-1, 1]，默认值0.0。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建颜色编辑效果实例（使用GSPlugin预定义的效果ID）
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COLOR_EDITING_EFFECT_ID });
    // 获取颜色编辑效果参数（曝光度）的当前值
    let exposure = effect.getPropertyValue(spatialRender.ColorEditingEffectParams.EXPOSURE);
    // 设置颜色编辑效果参数（曝光度）为0.5
    let res = effect.setPropertyValue(spatialRender.ColorEditingEffectParams.EXPOSURE, 0.5);
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将颜色编辑效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## ColorEditingEffect

ColorEditingEffect接口封装了颜色编辑风格的参数，可帮助开发者实现自定义的图像风格。该类继承自[Effect](js-apis-inner-scene-resources.md#effect21)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exposure | number | 否 | 否 | 图像的曝光度，推荐取值范围[-5，5]，默认值0.0。 |
| contrast | number | 否 | 否 | 图像的对比度，推荐取值范围[0, 2]，默认值1.0。 |
| temperature | number | 否 | 否 | 图像的色温，推荐取值范围[-2, 2]，默认值0.0。 |
| tint | number | 否 | 否 | 图像的色调，推荐取值范围[-1，1]，默认值0.0。 |
| saturation | number | 否 | 否 | 图像的饱和度，推荐取值范围[0, 2]，默认值1.0。 |
| vibrance | number | 否 | 否 | 图像的自然饱和度，推荐取值范围[-1, 1]，默认值0.0。 |

**示例：**

```typescript
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  // 加载空间重建插件GSPlugin
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    // 获取场景的资源工厂
    let rf = scene.getResourceFactory();
    // 创建颜色编辑效果实例（类型为ColorEditingEffect）
    let effect : spatialRender.ColorEditingEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COLOR_EDITING_EFFECT_ID }) as spatialRender.ColorEditingEffect;
    // 创建摄像机
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    // 将颜色编辑效果添加到摄像机的效果链中
    camera.effects.append(effect)
  });
}
```

## GSTile

3D高斯瓦片的描述符。一个GSTile对应清单文件中的一个.sog文件。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 包含3D高斯瓦片数据的.sog文件的Uri。 |

**示例：**

```typescript
import { Scene, RenderContext, Camera, Node } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    if (!scene.root) {
      return;
    }
    let root: Node = scene.root as Node;

    // 创建相机
    let srf = scene.getResourceFactory();
    let camera: Camera = await srf.createCamera({ name: "Camer1", path: root.path });
    camera.enabled = true;

    // 配置分块3DGS导入参数
    let params: spatialRender.TiledGSImportSettings = {
      uri: "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json"
    };

    // 加载分块3DGS模型
    let promise = spatialRender.GSPlugin.loadTiledGSNode(scene, params, root);
    promise.then((tiledGSNode: spatialRender.TiledGSNode) => {
      if (!camera) {
        return;
      }
      // 设置驱动分块选择的相机
      tiledGSNode.setCamera(camera);
      // 向渲染器注册瓦片请求回调
      tiledGSNode.setTileRequestCallback((tiles: spatialRender.GSTile[]) => {
        if (!tiles || tiles.length <= 0) {
          return;
        }
        // 遍历请求的瓦片列表，获取对应uri
        for (const tile of tiles) {
          console.debug('tile uri=', tile.uri);
        }
      });
    });
  });
}
```

## GSTileRequestCallback

type GSTileRequestCallback = (tiles: GSTile[]) => void

回调函数，用于传递来自渲染器的瓦片数据请求。当驱动相机移动且渲染器需要加载更多瓦片时触发。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tiles | [GSTile](spatial-recon-spatialrender.md#gstile)[] | 是 | 渲染器向应用请求的瓦片列表。 |

**示例：**

```typescript
import { Scene, RenderContext, Camera, Node } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

// 获取默认的渲染上下文
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  // 加载场景
  Scene.load().then(async (scene: Scene) => {
    if (!scene.root) {
      return;
    }
    let root: Node = scene.root as Node;

    // 创建相机
    let srf = scene.getResourceFactory();
    let camera: Camera = await srf.createCamera({ name: "Camer1", path: root.path });
    camera.enabled = true;

    // 配置分块3DGS导入参数
    let params: spatialRender.TiledGSImportSettings = {
      uri: "file:///data/storage/el2/base/files/uav-lod/sanyapo.scene.json"
    };

    // 加载分块3DGS模型
    let promise = spatialRender.GSPlugin.loadTiledGSNode(scene, params, root);
    promise.then((tiledGSNode: spatialRender.TiledGSNode) => {
      if (!camera) {
        return;
      }
      // 设置驱动分块选择的相机
      tiledGSNode.setCamera(camera);
      // 向渲染器注册瓦片请求回调
      tiledGSNode.setTileRequestCallback((tiles: spatialRender.GSTile[]) => {
        if (!tiles || tiles.length <= 0) {
          return;
        }
        // 遍历请求的瓦片列表
        for (const tile of tiles) {
          // 向远端发送请求，获取对应瓦片数据并持久化保存
        }
      });
    });
  });
}
```
