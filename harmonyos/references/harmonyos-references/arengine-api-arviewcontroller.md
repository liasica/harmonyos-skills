---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller
title: arViewController（AR场景管理能力）
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > ArkTS API > arViewController（AR场景管理能力）
category: harmonyos-references
scraped_at: 2026-04-29T14:05:04+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3b0b2ace092b311df95c711980835287ee4f6173d4590b2c72ace757f6ed42c3
---

本模块提供AR Engine（AR引擎服务）的arViewController（AR场景管理能力）相关接口。

基础核心能力包括AR会话管理、空间对象管理与场景化管理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

## 导入模块

PhoneTabletTV

```
1. import { arEngine, arViewController } from '@kit.AREngine';
```

## LandmarkType

PhoneTabletTV

人脸关键点类别。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| LEFT\_EYE | 0 | 左眼。 |
| LEFT\_SIDE\_OF\_MOUTH | 1 | 嘴巴左侧。 |
| RIGHT\_EYE | 2 | 右眼。 |
| RIGHT\_SIDE\_OF\_MOUTH | 3 | 嘴巴右侧。 |
| TIP\_OF\_NOSE | 4 | 鼻尖。 |
| CENTER\_OF\_FACE | 5 | 人脸中心。 |

## ARViewContext

PhoneTabletTV

ARView上下文，用于AR场景管理，包括初始化、暂停、恢复及销毁。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

### ARViewContext.init

PhoneTabletTV

init(): Promise<void>

初始化[ARViewContext](arengine-api-arviewcontroller.md#arviewcontext)，初始化AR会话和设置AR渲染场景等。使用Promise异步回调。

**需要权限：** ohos.permission.CAMERA 和 ohos.permission.GYROSCOPE 和 ohos.permission.ACCELEROMETER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中返回801错误码，可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permissions not granted, such as the camera permission. |
| 801 | Device not compatible. |
| 1009200001 | Failure. |
| 1009200007 | Configuration not supported. |
| 1009200008 | Resource exhausted. |
| 1009200009 | Service unavailable. |
| 1009200010 | Camera unavailable. |
| 1009200201 | ARView invalid operation. |
| 1009200202 | Graphics3D AR scene required. |
| 1009200203 | AREngine config required. |
| 1009200204 | AR session setup failed. |
| 1009200205 | AR scene camera setup failed. |

**示例：**

```
1. import { arViewController } from '@kit.AREngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
5. await context.init();
```

### ARViewContext.pause

PhoneTabletTV

pause(): void

暂停相机跟踪与AR场景渲染。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200201 | ARView invalid operation. |
| 1009200204 | AR session setup failed. |

**示例：**

```
1. import { arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.pause();
```

### ARViewContext.destroy

PhoneTabletTV

destroy(): Promise<void>

销毁[ARViewContext](arengine-api-arviewcontroller.md#arviewcontext)，释放ARView使用资源，包括AR会话与呈现场景销毁，在退出ARView时使用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200201 | ARView invalid operation. |
| 1009200204 | AR session setup failed. |

**示例：**

```
1. import { arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.destroy();
```

### ARViewContext.resume

PhoneTabletTV

resume(): void

用于恢复暂停的相机跟踪与AR场景渲染。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200010 | Camera unavailable. |
| 1009200201 | ARView invalid operation. |
| 1009200204 | AR session setup failed. |

**示例：**

```
1. import { arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.resume();
```

### ARViewContext.scene

PhoneTabletTV

set scene(scene: Scene)

设置ARView的AR场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | [Scene](js-apis-inner-scene.md#scene-1) | 是 | AR呈现场景，用于管理空间节点。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';
2. import { arViewController } from '@kit.AREngine';

4. Scene.load().then((scene: Scene) => {
5. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
6. context.scene = scene;
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to load scene. Code is ${err.code}, message is ${err.message}.`);
9. });
```

### ARViewContext.scene

PhoneTabletTV

get scene(): Scene

获得的AR呈现场景，用于管理空间节点。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scene](js-apis-inner-scene.md#scene-1) | AR呈现场景，用于管理空间节点。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';
2. import { arViewController } from '@kit.AREngine';

4. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
5. context.scene;
```

### ARViewContext.session

PhoneTabletTV

get session(): arEngine.ARSession | undefined

获取AR会话，用于获取相关AR环境跟踪、相机跟踪、命中检测等能力，如相机位姿、平面信息、创建锚点等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [arEngine.ARSession](arengine-api-arengine.md#arsession) | undefined | 获得的AR会话内容，AR会话正常设置之后返回为arEngine.ARSession，异常设置或异常操作导致ARViewContext未初始化成功，返回undefined。 |

**示例：**

```
1. import { arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.session;
```

### ARViewContext.config

PhoneTabletTV

set config(conf: arEngine.ARConfig)

设置AR会话的配置文件，如北向坐标、性能模式等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| conf | [arEngine.ARConfig](arengine-api-arengine.md#arconfig) | 是 | [ARSession](arengine-api-arengine.md#arsession)的功能配置参数。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.config = {
5. type: arEngine.ARType.WORLD,
6. poseMode: arEngine.ARPoseMode.GRAVITY_AND_HEADING,
7. powerMode: arEngine.ARPowerMode.POWER_SAVING,
8. depthMode: arEngine.ARDepthMode.AUTOMATIC
9. };
```

### ARViewContext.loadAsset

PhoneTabletTV

loadAsset(resourcePath: ResourceStr, landmark: LandmarkType): Promise<void>

在指定的关键点处放置模型。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourcePath | [ResourceStr](ts-types.md#resourcestr) | 是 | 存储模型的路径。 |
| landmark | [LandmarkType](arengine-api-arviewcontroller.md#landmarktype) | 是 | 指定想要放置模型的关键点。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. // 此处为用户本地存放模型路径
5. let resourcePath:ResourceStr = $rawfile('xxxx/xxxx');
6. context.loadAsset(resourcePath, arViewController.LandmarkType.LEFT_EYE);
```

### ARViewContext.removeAsset

PhoneTabletTV

removeAsset(landmark: LandmarkType):Promise<void>

在指定的关键点移除已放置的模型。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| landmark | [LandmarkType](arengine-api-arviewcontroller.md#landmarktype) | 是 | 指定想要移除模型的关键点。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.removeAsset(arViewController.LandmarkType.LEFT_EYE);
```

### ARViewContext.clearResource

PhoneTabletTV

clearResource():Promise<void>

清除所有放置的模型。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { arViewController } from '@kit.AREngine';

3. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
4. context.clearResource();
```

### ARViewContext.setBlendShapeWeight

PhoneTabletTV

setBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType, weight: number): boolean

设置指定Node里特定微表情的权重，用于渲染表情。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 新建锚点对应的AR场景节点。  **说明：** Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |
| type | [arEngine.ARBlendShapeType](arengine-api-arengine.md#arblendshapetype) | 是 | 微表情类型。 |
| weight | number | 是 | 微表情权重，范围是0到1。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 微表情权重设置结果。true代表成功，false代表失败 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
5. ctx.setBlendShapeWeight(node, arEngine.ARBlendShapeType.EYE_BLINK_LEFT, 0.1);
6. }
```

### ARViewContext.getBlendShapeWeight

PhoneTabletTV

getBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType): number | null

获取指定Node里特定微表情的权重。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 新建锚点对应的AR场景节点。  **说明：** Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |
| type | [arEngine.ARBlendShapeType](arengine-api-arengine.md#arblendshapetype) | 是 | 微表情类型。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | null | 当前微表情的权重，若传入的node或type有误，则返回null。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
5. ctx.getBlendShapeWeight(node, arEngine.ARBlendShapeType.EYE_BLINK_LEFT);
6. }
```

### ARViewContext.transformPose

PhoneTabletTV

transformPose(position: Vec3, rotation: Quaternion): arEngine.ARPose | null

将位姿信息从AR坐标系转换为AGP渲染引擎坐标系。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Vec3](js-apis-inner-scene-types.md#vec3) | 是 | 位姿坐标信息 |
| rotation | [Quaternion](js-apis-inner-scene-types.md#quaternion) | 是 | 位姿朝向信息。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [arEngine.ARPose](arengine-api-arengine.md#arpose) | null | 转换后的位姿信息，若传入参数无效或创建[ARPose](arengine-api-arengine.md#arpose)对象失败则返回null。 |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Vec3, Quaternion } from '@kit.ArkGraphics3D';

4. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
5. let pose: Vec3 = { x: 1.0, y: -1.0, z: -0.5 };
6. let rot: Quaternion = {
7. x: -0.1,
8. y: 0.2,
9. z: -0.3,
10. w: 0.5
11. };
12. context.transformPose(pose, rot);
```

### ARViewContext.callback

PhoneTabletTV

set callback(callback: ARViewCallback)

回调函数，可根据回调功能实现对应业务逻辑。使用callback方式异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ARViewCallback](arengine-api-arviewcontroller.md#arviewcallback) | 是 | ARViewCallback抽象类，声明ARView的回调接口。使用callback方式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. class ARViewCallbackImpl extends arViewController.ARViewCallback {

6. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
7. console.info('onAnchorAdd');
8. console.info(`add anchor id = ${String(anchor.id)}`);
9. console.info(`add anchor translation = ${anchor.getPose().translation}`);
10. console.info(`add node pose = ${node.position}`);
11. }

13. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
14. console.info('onAnchorUpdate');
15. console.info(`update anchor id = ${String(anchor.id)}`);
16. console.info(`update anchor translation = ${anchor.getPose().translation}`);
17. console.info(`update node pose = ${node.position}`);
18. }

20. async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
21. let arSession: arEngine.ARSession | undefined = ctx.session;
22. if (arSession) {
23. let frame: arEngine.ARFrame = arSession.getFrame();
24. if (!frame) {
25. console.error('Failed to get arSession.frame, it is undefined or null');
26. } else {
27. console.info(`Succeeded in getting arSession.frame = ${frame.timestamp}`);
28. await frame.release();
29. }
30. } else {
31. console.error('Failed to get arSession, arSession is undefined');
32. }
33. }
34. }

36. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
37. context.callback = new ARViewCallbackImpl();
```

## ARViewCallback

PhoneTabletTV

ARViewCallback抽象类，声明ARView的回调接口。使用callback方式异步返回结果。

开发者需继承此类并且根据业务逻辑实现回调子类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

### ARViewCallback.onAnchorAdd

PhoneTabletTV

abstract onAnchorAdd(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

当AR会话检测到新平面时，平面自动创建锚点以及对应的场景节点，并在帧刷新逻辑中自动触发此回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [ARViewContext](arengine-api-arviewcontroller.md#arviewcontext) | 是 | 当前ARView的上下文信息（ARViewContext）。 |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 新建锚点对应的AR场景节点。  **说明：** Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |
| anchor | [arEngine.ARAnchor](arengine-api-arengine.md#aranchor) | 是 | 新平面对应的新创建的锚点。  **说明：** [ARAnchor](arengine-api-arengine.md#aranchor)的位姿使用了AR Engine重力对齐世界坐标系。具体参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. // 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
5. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
6. // 其他操作
7. }
```

### ARViewCallback.onAnchorUpdate

PhoneTabletTV

abstract onAnchorUpdate(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

更新AR会话中的锚点时，ARView自动检测该锚点对应的场景节点，并调用该回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [ARViewContext](arengine-api-arviewcontroller.md#arviewcontext) | 是 | 当前ARView的上下文信息（ARViewContext）。 |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 新建锚点对应的AR场景节点。  **说明：** Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |
| anchor | [arEngine.ARAnchor](arengine-api-arengine.md#aranchor) | 是 | 更新锚点。  **说明：** [ARAnchor](arengine-api-arengine.md#aranchor)的位姿使用了AR Engine重力对齐世界坐标系。具体参见[坐标系说明](../harmonyos-guides/arengine-overview.md#坐标系说明)。 |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';
2. import { Node } from '@kit.ArkGraphics3D';

4. // 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
5. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
6. // 其他操作
7. }
```

### ARViewCallback.onFrameUpdate

PhoneTabletTV

abstract onFrameUpdate(ctx: ARViewContext, sysBootTs: number): void

AR场景每帧刷新前会自动触发该回调，开发者可以基于此回调进行AR实体摆放位姿调整、动画调整以及相机位姿调整等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [ARViewContext](arengine-api-arviewcontroller.md#arviewcontext) | 是 | 当前ARView的上下文信息。 |
| sysBootTs | number | 是 | 时间戳，单位为us。 |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';

3. // 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
4. onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
5. let arSession: arEngine.ARSession | undefined = ctx.session;
6. if (arSession) {
7. let frame: arEngine.ARFrame = arSession.getFrame();
8. if (!frame){
9. console.error('Failed to get arSession.frame, it is undefined or null');
10. } else {
11. console.info(`Succeeded in getting arSession.frame = ${frame.timestamp}`);
12. await frame.release();
13. }
14. } else {
15. console.error('Failed to get arSession, arSession is undefined');
16. }
17. }
```

## arViewController.isARTypeSupported

PhoneTabletTV

isARTypeSupported(type: arEngine.ARFeatureType): boolean

在ARViewController中调用此接口来判断AR特性是否支持在当前设备上运行。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [arEngine.ARFeatureType](arengine-api-arengine.md#arfeaturetype) | 是 | 表示想要检查能否正常运行的AR特性。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | AR特性检查结果。true表示该设备支持，false则表示该设备不支持。 |

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](arengine-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

**示例：**

```
1. import { arEngine, arViewController } from '@kit.AREngine';

3. arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
```
