---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsdrawable
title: hdsDrawable
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS API > hdsDrawable
category: harmonyos-references
scraped_at: 2026-04-29T13:57:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:31b2ad511f8b9b3ce0ffa49614953c4f26681e2dc202e752e206d5ef496d7dd2
---

本模块提供图标处理能力，包括对前后景合成、剪切、缩放、描边处理，支持分层图标和单层图标处理。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { hdsDrawable } from '@kit.UIDesignKit';
```

## hdsDrawable.getHdsLayeredIcon

PhonePC/2in1TabletTV

getHdsLayeredIcon(bundleName: string, layeredDrawableDescriptor: LayeredDrawableDescriptor, size: number, hasBorder?: boolean): image.PixelMap

获取处理后的分层图标接口，可通过该接口获取PixelMap格式的图标，适用于需插入单个图标的场景。分层图标对象以LayeredDrawableDescriptor格式定义，可以通过传入Symbol资源的id或name生成，其中hasBorder参数决定是否为输出的图标添加描边（在线主题场景时不支持设置描边），size参数指定输出图标的尺寸。

LayeredDrawableDescriptor对象：判断的方法是打开对应的Symbol json文件后观察其layered-image属性是否包含类似下面的结构：

```
1. "layered-image":
2. {
3. "background": "$background_path",
4. "foreground": "$foreground_path"
5. }
```

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bundleName | string | 是 | 与应用绑定，为应用Bundle名称。 |
| layeredDrawableDescriptor | [LayeredDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor) | 是 | 需要处理的分层图标数据对象。 |
| size | number | 是 | 接口处理完成后输出的图标对象为正方形，该值表示输出对象的正方形边长，包含描边区域，取值范围：大于0，单位：vp。 |
| hasBorder | boolean | 否 | 是否描边，true：描边，false：不描边，默认false，在线主题场景不支持设置描边。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 接口处理完成后返回的图标数据对象，格式为PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The value of bundleName is incorrect.  Parameter error. The value of layeredDrawableDescriptor is incorrect.  Parameter error. The value of size is incorrect.  Parameter error. The value of hasBorder is incorrect.  Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**示例：**

```
1. import { LayeredDrawableDescriptor } from '@kit.ArkUI';
2. import { hdsDrawable } from '@kit.UIDesignKit';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. let bundleName: string = 'com.example.uidesignkit';
9. try {
10. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
11. let resManager: resourceManager.ResourceManager =
12. (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
13. let layeredDrawableDescriptor: LayeredDrawableDescriptor =
14. (resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor; // 传入已创建的图片资源
15. let processedIcon: image.PixelMap =
16. hdsDrawable.getHdsLayeredIcon(bundleName, layeredDrawableDescriptor, 48, true);
17. } catch (err) {
18. let message = (err as BusinessError).message;
19. let code = (err as BusinessError).code;
20. console.error(`getHdsLayeredIcon failed, code: ${code}, message: ${message}`);
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/SAns584nRwm8bf_zbrTjcQ/zh-cn_image_0000002589246851.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=017DC1751F9ED1C584FA77013B0C19980A18F3F876F1D79B67295680E7DF8118)

## hdsDrawable.getHdsLayeredIconAsync

PhonePC/2in1TabletTV

getHdsLayeredIconAsync(bundleName: string, layeredDrawableDescriptor: LayeredDrawableDescriptor, size: number, hasBorder?: boolean): Promise<image.PixelMap>

获取处理后的分层图标接口，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bundleName | string | 是 | 与应用绑定，为应用Bundle名称。 |
| layeredDrawableDescriptor | [LayeredDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor) | 是 | 需要处理的分层图标数据对象。 |
| size | number | 是 | 接口处理完成后输出的图标对象为正方形，该值表示输出对象的正方形边长，包含描边区域，取值范围：大于0，单位：vp。 |
| hasBorder | boolean | 否 | 处理后的图标是否要描边，true：描边，false：不描边，默认false，在线主题场景不支持设置描边。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，接口处理完成后返回的图标数据对象，格式为PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The value of bundleName is incorrect.  Parameter error. The value of layeredDrawableDescriptor is incorrect.  Parameter error. The value of size is incorrect.  Parameter error. The value of hasBorder is incorrect.  Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**示例：**

```
1. import { LayeredDrawableDescriptor } from '@kit.ArkUI';
2. import { hdsDrawable } from '@kit.UIDesignKit';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. let bundleName: string = 'com.example.uidesignkit';
9. try {
10. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
11. let resManager: resourceManager.ResourceManager =
12. (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
13. let layeredDrawableDescriptor: LayeredDrawableDescriptor =
14. (resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor; // 传入已创建的图片资源

16. hdsDrawable.getHdsLayeredIconAsync(bundleName, layeredDrawableDescriptor, 48, true)
17. .then((data: image.PixelMap) => {
18. let processedIcon: image.PixelMap = data;
19. })
20. .catch((err: BusinessError) => {
21. console.error(`getHdsLayeredIconAsync return error, code: ${err.code}, msg: ${err.message}`);
22. });
23. } catch (err) {
24. let message = (err as BusinessError).message;
25. let code = (err as BusinessError).code;
26. console.error(`getHdsLayeredIconAsync failed, code: ${code}, message: ${message}`);
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/KMj_Y9q7RHyX58urdmctGQ/zh-cn_image_0000002589246851.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=4ECF8B0DE1C4A4ECBA09E3F6E5D472FB545F12E9AF388B1F25F351A716374220)

## hdsDrawable.getHdsIcon

PhonePC/2in1TabletTV

getHdsIcon(bundleName: string, pixelMap: image.PixelMap, size: number, mask: image.PixelMap, hasBorder?: boolean): image.PixelMap

获取处理后的单层图标接口，可通过该接口获取PixelMap格式的图标，适用于需插入单个图标的场景。其中hasBorder参数决定是否为输出的图标添加描边（在线主题场景时不支持设置描边），size参数指定输出图标的尺寸。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bundleName | string | 是 | 与应用绑定，为应用Bundle名称。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 单层图标数据对象。 |
| size | number | 是 | 接口处理完成后输出的图标对象为正方形，该值表示输出对象的正方形边长，包含描边区域，取值范围：大于0，单位：vp。 |
| mask | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图标蒙版信息，用于图标剪切处理。 |
| hasBorder | boolean | 否 | 是否描边，true：描边，false：不描边，默认false，在线主题场景不支持设置描边。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 接口处理完成后返回的图标数据对象，格式为PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The value of bundleName is incorrect.  Parameter error. The value of pixelMap is incorrect.  Parameter error. The value of size is incorrect.  Parameter error. The value of mask is incorrect.  Parameter error. The value of hasBorder is incorrect.  Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**示例：**

```
1. import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
2. import { hdsDrawable } from '@kit.UIDesignKit';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. let bundleName: string = 'com.example.uidesignkit';
9. try {
10. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
11. let resManager: resourceManager.ResourceManager =
12. (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
13. let layeredDrawableDescriptor: LayeredDrawableDescriptor =
14. (resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor; // 传入已创建的图片资源
15. let drawableDescriptor: DrawableDescriptor =
16. (resManager?.getDrawableDescriptor($r('app.media.normal_icon_512').id)) as DrawableDescriptor; // 传入已创建的图片资源
17. let processedIcon: image.PixelMap = hdsDrawable.getHdsIcon(bundleName, drawableDescriptor?.getPixelMap(), 48,
18. layeredDrawableDescriptor?.getMask().getPixelMap(), true);
19. } catch (err) {
20. let message = (err as BusinessError).message;
21. let code = (err as BusinessError).code;
22. console.error(`getHdsIcon failed, code: ${code}, message: ${message}`);
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/3CQpzB0uT0CGRCoS7UGT3A/zh-cn_image_0000002558767044.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=E94D50D53303CBD627B1E348249B208DC40D5B1581FA770A5F0EE3447AF0ADBD)

## hdsDrawable.getHdsIconAsync

PhonePC/2in1TabletTV

getHdsIconAsync(bundleName: string, pixelMap: image.PixelMap, size: number, mask: image.PixelMap, hasBorder?: boolean): Promise<image.PixelMap>

获取处理后的单层图标接口，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bundleName | string | 是 | 与应用绑定，为应用Bundle名称。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 单层图标数据对象。 |
| size | number | 是 | 接口处理完成后输出的图标对象为正方形，该值表示输出对象的正方形边长，包含描边区域，取值范围：大于0，单位：vp。 |
| mask | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图标蒙版信息，用于图标剪切处理。 |
| hasBorder | boolean | 否 | 处理后的图标是否要描边，true：描边，false：不描边，默认false，在线主题场景不支持设置描边。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，接口处理完成后返回的图标数据对象，格式为PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The value of bundleName is incorrect.  Parameter error. The value of pixelMap is incorrect.  Parameter error. The value of size is incorrect.  Parameter error. The value of mask is incorrect.  Parameter error. The value of hasBorder is incorrect.  Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**示例：**

```
1. import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
2. import { hdsDrawable } from '@kit.UIDesignKit';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. let bundleName: string = 'com.example.uidesignkit';
9. try {
10. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
11. let resManager: resourceManager.ResourceManager =
12. (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
13. let layeredDrawableDescriptor: LayeredDrawableDescriptor =
14. (resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor; // 传入已创建的图片资源
15. let drawableDescriptor: DrawableDescriptor =
16. (resManager?.getDrawableDescriptor($r('app.media.normal_icon_512').id)) as DrawableDescriptor; // 传入已创建的图片资源

18. hdsDrawable.getHdsIconAsync(bundleName, drawableDescriptor?.getPixelMap(), 48,
19. layeredDrawableDescriptor?.getMask().getPixelMap(), true)
20. .then((data: image.PixelMap) => {
21. let processedIcon: image.PixelMap = data;
22. })
23. .catch((err: BusinessError) => {
24. console.error(`getHdsIconAsync return error, code: ${err.code}, msg: ${err.message}`);
25. });
26. } catch (err) {
27. let message = (err as BusinessError).message;
28. let code = (err as BusinessError).code;
29. console.error(`getHdsIconAsync failed, code: ${code}, message: ${message}`);
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/tFCu4izRR4SoEdEBvLympA/zh-cn_image_0000002558767044.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=C3AC12C6ABA69DCC450D0C5478E30DA82A8CE5A1FE8673225B962FBD3C5F1E28)

## hdsDrawable.getHdsLayeredIcons

PhonePC/2in1TabletTV

getHdsLayeredIcons(icons: Array<LayeredIcon>, options: Options): Promise<Array<ProcessedIcon>>

批量获取处理后的分层图标接口，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| icons | Array<[LayeredIcon](ui-design-hdsdrawable.md#layeredicon)> | 是 | 待处理的分层图标数据集合。 |
| options | [Options](ui-design-hdsdrawable.md#options) | 是 | 处理分层图标的配置项信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProcessedIcon](ui-design-hdsdrawable.md#processedicon)>> | Promise对象，返回处理后的图像数据集合。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The value of icons is incorrect.  Parameter error. The value of size is incorrect.  Parameter error. The value of hasBorder is incorrect.  Parameter error. The value of parallelNumber is incorrect. |
| 1012600001 | Task is busy. |

**示例：**

```
1. import { LayeredDrawableDescriptor } from '@kit.ArkUI';
2. import { hdsDrawable } from '@kit.UIDesignKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { resourceManager } from '@kit.LocalizationKit';
5. import { common } from '@kit.AbilityKit';

7. let bundleName: string = 'com.example.uidesignkit';
8. let options: hdsDrawable.Options = {
9. size: 48,
10. hasBorder: true,
11. parallelNumber: 4
12. };

14. try {
15. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
16. let resManager: resourceManager.ResourceManager =
17. (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
18. let layeredDrawableDescriptor: LayeredDrawableDescriptor =
19. (resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor; // 传入已创建的图片资源
20. let layeredIcons: Array<hdsDrawable.LayeredIcon> = [];
21. for (let i = 0; i < 10; i++) {
22. layeredIcons.push({
23. bundleName: `${bundleName}-${i}`,
24. layeredDrawableDescriptor: layeredDrawableDescriptor
25. });
26. }

28. hdsDrawable.getHdsLayeredIcons(layeredIcons, options)
29. .then((data: Array<hdsDrawable.ProcessedIcon>) => {
30. console.info(`getHdsLayeredIcons data size: ${data.length}`);
31. let processedIconList: Array<hdsDrawable.ProcessedIcon> = data;
32. })
33. .catch((err: BusinessError) => {
34. console.error(`getHdsLayeredIcons error, code: ${err.code}, msg: ${err.message}`);
35. });
36. } catch (err) {
37. let message = (err as BusinessError).message;
38. let code = (err as BusinessError).code;
39. console.error(`getHdsLayeredIcons failed, code: ${code}, message: ${message}`);
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Vqp-ShCrSaOqdZjhurEFLQ/zh-cn_image_0000002589246851.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=CD5E40ADD6DC2A8E09E472636A98BF487F517DE32333BEEA6C7058EB5CC5096E)

## hdsDrawable.getHdsIcons

PhonePC/2in1TabletTV

getHdsIcons(icons: Array<Icon>, mask: image.PixelMap, options: Options): Promise<Array<ProcessedIcon>>

批量获取处理后的单层图标接口，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| icons | Array<[Icon](ui-design-hdsdrawable.md#icon)> | 是 | 待处理的单层图标数据集合。 |
| mask | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图标蒙版信息，用于图标剪切处理。 |
| options | [Options](ui-design-hdsdrawable.md#options) | 是 | 处理单层图标的配置项信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProcessedIcon](ui-design-hdsdrawable.md#processedicon)>> | Promise对象，返回处理后的图像数据集合。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The value of icons is incorrect.  Parameter error. The value of mask is incorrect.  Parameter error. The value of size is incorrect.  Parameter error. The value of hasBorder is incorrect.  Parameter error. The value of parallelNumber is incorrect. |
| 1012600001 | Task is busy. |

**示例：**

```
1. import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
2. import { hdsDrawable } from '@kit.UIDesignKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { resourceManager } from '@kit.LocalizationKit';
5. import { common } from '@kit.AbilityKit';

7. let bundleName: string = 'com.example.uidesignkit';
8. let options: hdsDrawable.Options = {
9. size: 48,
10. hasBorder: true,
11. parallelNumber: 4
12. };

14. try {
15. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
16. let resManager: resourceManager.ResourceManager =
17. (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
18. let layeredDrawableDescriptor: LayeredDrawableDescriptor =
19. (resManager.getDrawableDescriptor($r('app.media.drawable')
20. .id)) as LayeredDrawableDescriptor; // 传入已创建的图片资源
21. let drawableDescriptor: DrawableDescriptor =
22. (resManager?.getDrawableDescriptor($r('app.media.normal_icon_512').id)) as DrawableDescriptor; // 传入已创建的图片资源
23. let icons: Array<hdsDrawable.Icon> = [];
24. for (let i = 0; i < 10; i++) {
25. icons.push({
26. bundleName: `${bundleName}-${i}`,
27. pixelMap: drawableDescriptor.getPixelMap()
28. });
29. }

31. hdsDrawable.getHdsIcons(icons, layeredDrawableDescriptor.getMask().getPixelMap(), options)
32. .then((data: Array<hdsDrawable.ProcessedIcon>) => {
33. console.info(`getHdsIcons data size: ${data.length}`);
34. let processedIconList: Array<hdsDrawable.ProcessedIcon> = data;
35. })
36. .catch((err: BusinessError) => {
37. console.error(`getHdsIcons error, code: ${err.code}, msg: ${err.message}`);
38. });
39. } catch (err) {
40. let message = (err as BusinessError).message;
41. let code = (err as BusinessError).code;
42. console.error(`getHdsIcons failed, code: ${code}, message: ${message}`);
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/4pzaJyU0QBSGh9kGJ7-N0g/zh-cn_image_0000002558767044.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=DF9A7110CA5FF5FC6C7EAC244CC0E33E8A9D66B121E575676623783AB5D9E396)

## LayeredIcon

PhonePC/2in1TabletTV

分层图标数据对象。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用Bundle名称。 |
| layeredDrawableDescriptor | [LayeredDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor) | 否 | 否 | 需要处理的分层图标数据对象。 |

## Options

PhonePC/2in1TabletTV

图标数据处理接口对应的配置项信息。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| size | number | 否 | 否 | 接口处理完成后输出的图标对象为正方形，该值表示输出对象的正方形边长，包含描边区域，取值范围：大于0，单位：vp。 |
| hasBorder | boolean | 否 | 是 | 是否描边，true：描边，false：不描边，默认false，在线主题场景不支持设置描边。 |
| parallelNumber | number | 否 | 是 | 批量处理图标数据的并发数量，默认（推荐）：4，最大10。 |

## ProcessedIcon

PhonePC/2in1TabletTV

处理后的图标对象。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用Bundle名称。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 接口处理完成后返回的图标数据对象，格式为PixelMap。 |

## Icon

PhonePC/2in1TabletTV

单层图标数据对象。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用Bundle名称。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 单层图标数据对象。 |
