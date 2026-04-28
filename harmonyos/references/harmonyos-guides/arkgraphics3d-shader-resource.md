---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-shader-resource
title: .shader资源文件格式要求
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D资源创建以及使用 > .shader资源文件格式要求
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2200fc666cc65b19f99acaed6d7d4b3341f503f6a9353bbf92d5060cdc219540
---

ArkGraphics 3D中支持的.shader文件基于JSON格式，书写.shader文件时需符合JSON语法要求。文件包含以下部分：

## compatibility\_info

* 类型：object
* 说明：用于向引擎声明shader版本兼容性信息。统一使用如下字段：

  ```
  1. "compatibility_info": { "version": "22.00", "type": "shader" }
  ```

  表示这是引擎22.00版本下的shader描述文件。

## vert

* 类型：string
* 说明：指定使用该shader的DrawCall中使用的vertex shader文件。
* 默认值：

  ```
  1. "vert": "3dshaders://shader/core3d_dm_fw.vert.spv"
  ```
* 自定义路径：

  ```
  1. "vert": "appshaders://yourDir/yourShader.vert.spv"
  ```

  其中yourDir/yourShader.vert.spv是用户使用的shader文件在文件沙箱中的路径。

## frag

* 类型：string
* 说明：指定使用该shader的DrawCall中使用的fragment shader文件。
* 默认值：

  ```
  1. "frag": "3dshaders://shader/core3d_dm_fw.frag.spv"
  ```
* 自定义路径：

  ```
  1. "frag": "appshaders://yourDir/yourShader.frag.spv"
  ```

  其中yourDir/yourShader.frag.spv是用户使用的shader文件在文件沙箱中的路径。

## vertexInputDeclaration

* 类型：string
* 说明：指定输入vertex数据中的attributes排布方式。
* 当前限制：渲染引擎暂不支持自定义attributes排布，保持默认值即可。
* 默认值：

  ```
  1. "vertexInputDeclaration": "3dvertexinputdeclarations://core3d_dm_fw.shadervid"
  ```

## state

* 类型：object
* 说明：指定本次渲染管线中的pipeline state，包括rasterizationState、depthStencilState、colorBlendState三部分：

### rasterizationState

用于表示光栅化过程中的属性配置，具体包括：

* enableDepthClamp：用于控制渲染过程中的depth写入时是否进行clamp，true表示进行clamp，false表示不进行clamp。当前此属性应设置为false。
* enableDepthBias：用于控制渲染过程中的depth写入时是否进行Bias计算，true表示进行Bias计算，false表示不进行Bias计算。当前此属性应设置为false。
* enableRasterizerDiscard：用于控制本次drawCall的fragment阶段是否跳过，true表示跳过，false表示不跳过。
* polygonMode：用于指定光栅化渲染中的三角形填充方式，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "fill" | 全填充模式，将三角形内部所有像素填充颜色。 |
  | "line" | 线填充模式，只绘制三角形的边线。 |
  | "point" | 点填充模式，只绘制三角形的顶点。 |
* cullModeFlags：用于指定光栅化渲染中的culling方式，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "back" | 背面剔除，不渲染三角形的背面。 |
  | "front" | 正面剔除，不渲染三角形的正面。 |
  | "none" | 不进行剔除，正面和背面都渲染。 |
  | "front\_and\_back" | 全部剔除，正面和背面都不渲染。 |
* frontFace：用于指定三角面的正面如何定义，可取值及含义见下表。

  | 可取值 | 顶点排序方式 | 说明 |
  | --- | --- | --- |
  | "counter\_clockwise" | 逆时针 | 按逆时针顺序排列的三角形被认为是正面。 |
  | "clockwise" | 顺时针 | 按顺时针顺序排列的三角形被认为是正面。 |

### depthStencilState

用于表示深度测试和模板测试的状态属性，具体包括：

* enableDepthTest：用于控制是否开启深度测试，true表示开启，false表示关闭。若开启深度测试则非透明物体将按照深度呈现遮挡关系，若关闭深度测试则物体按照绘制顺序排序。
* enableDepthWrite：用于物体绘制时深度附件是否写入该物体的深度值，true表示写入，false表示不写入。
* enableDepthBoundsTest：在深度测试的基础上再规定了通过深度测试的最小值和最大值范围，在此范围之外的值不通过深度测试，true表示开启，false表示关闭。当前此属性应设置为false。
* enableStencilTest：用于控制是否开启模板测试，true表示开启，false表示关闭。若开启模板测试则通过模板测试的物体会被绘制，没有通过模板测试的物体不被绘制，若关闭则不进行模板测试。
* depthCompareOp：用于控制深度测试的比较方式，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "never" | 永不通过深度测试，像素不会被绘制。 |
  | "less" | 当前像素深度小于已有深度值时通过测试，像素被绘制。 |
  | "equal" | 当前像素深度等于已有深度值时通过测试，像素被绘制。 |
  | "less\_or\_equal" | 当前像素深度小于或等于已有深度值时通过测试，像素被绘制。 |
  | "greater" | 当前像素深度大于已有深度值时通过测试，像素被绘制。 |
  | "not\_equal" | 当前像素深度不等于已有深度值时通过测试，像素被绘制。 |
  | "greater\_or\_equal" | 当前像素深度大于或等于已有深度值时通过测试，像素被绘制。 |
  | "always" | 总是通过深度测试，像素总是被绘制。 |

### colorBlendState

用于指定本次渲染中渲染源与渲染目标的混合状态属性。包括colorAttachments，用于指定本次渲染中颜色附件的混合状态属性。colorAttachments具体包括如下几项：

* enableBlend：渲染源与渲染目标的混合是否开启，true表示开启混合，false表示关闭混合。若开启则渲染源与渲染目标以指定方式混合，若不开启则不进行混合。
* colorWriteMask：指定渲染颜色附件中通道掩码，若指定了通道掩码则该通道将被计算混合，若不指定则不计算混合，可取值有r\_bit、g\_bit、b\_bit、a\_bit，各个通道可以用|符号取并集，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "r\_bit" | 红色通道允许写入或参与混合。 |
  | "g\_bit" | 绿色通道允许写入或参与混合。 |
  | "b\_bit" | 蓝色通道允许写入或参与混合。 |
  | "a\_bit" | 透明通道允许写入或参与混合。 |
* srcColorBlendFactor: 指定渲染源颜色通道的混合因子，可取值及含义见下表。

  | 可取值 | 因子 | 结果 | 应用场景 |
  | --- | --- | --- | --- |
  | "zero" | 0 | 源颜色×0=0 | 不显示新颜色，只保留背景。 |
  | "one" | 1 | 源颜色×1=源颜色 | 新颜色完全显示，覆盖背景。 |
  | "src\_color" | 源颜色 | 源颜色×源颜色 | 新颜色按自身颜色比例混合显示。 |
  | "one\_minus\_src\_color" | 1-源颜色 | 源颜色×(1-源颜色) | 新颜色按自身剩余颜色比例混合显示。 |
  | "dst\_color" | 目标颜色 | 源颜色×目标颜色 | 新颜色按背景颜色比例混合显示。 |
  | "one\_minus\_dst\_color" | 1-目标颜色 | 源颜色×(1-目标颜色) | 新颜色按背景剩余颜色比例混合显示。 |
  | "src\_alpha" | 源Alpha | 源颜色×源Alpha | 新颜色按自身Alpha比例混合显示。 |
  | "one\_minus\_src\_alpha" | 1-源Alpha | 源颜色×(1-源Alpha) | 新颜色按自身Alpha剩余比例混合显示。 |
  | "dst\_alpha" | 目标Alpha | 源颜色×目标Alpha | 新颜色按背景Alpha比例混合显示。 |
  | "one\_minus\_dst\_alpha" | 1-目标Alpha | 源颜色×(1-目标Alpha) | 新颜色按背景Alpha剩余比例混合显示。 |
  | "constant\_color" | 固定颜色常量 | 源颜色×固定颜色常量 | 新颜色按固定颜色比例混合显示。 |
  | "one\_minus\_constant\_color" | 1-固定颜色常量 | 源颜色×(1-固定颜色常量) | 新颜色按固定颜色剩余比例混合显示。 |
  | "constant\_alpha" | 固定Alpha常量 | 源颜色×固定Alpha常量 | 新颜色按固定Alpha比例混合显示。 |
  | "one\_minus\_constant\_alpha" | 1-固定Alpha常量 | 源颜色×(1-固定Alpha常量) | 新颜色按固定Alpha剩余比例混合显示。 |
  | "src\_alpha\_saturate" | min(源Alpha, 1-目标Alpha) | 源颜色×min(源Alpha, 1-目标Alpha) | 新颜色按源Alpha与背景剩余Alpha最小值比例混合显示，避免叠加过强。 |
  | "src1\_color" | 第二源颜色 | 源颜色×第二源颜色 | 新颜色按第二源颜色比例混合显示。 |
  | "one\_minus\_src1\_color" | 1-第二源颜色 | 源颜色×(1-第二源颜色) | 新颜色按第二源颜色剩余比例混合显示。 |
  | "src1\_alpha" | 第二源Alpha | 源颜色×第二源Alpha | 新颜色按第二源Alpha比例混合显示。 |
  | "one\_minus\_src1\_alpha" | 1-第二源Alpha | 源颜色×(1-第二源Alpha) | 新颜色按第二源Alpha剩余比例混合显示。 |
* dstColorBlendFactor：指定渲染目标颜色通道的混合因子，可取值及含义见下表。

  | 可取值 | 因子 | 结果 | 应用场景 |
  | --- | --- | --- | --- |
  | "zero" | 0 | 目标颜色×0=0 | 不显示背景颜色，相当于背景清零。 |
  | "one" | 1 | 目标颜色×1=目标颜色 | 保留背景颜色原样，不受影响。 |
  | "src\_color" | 源颜色 | 目标颜色×源颜色 | 背景按新颜色比例混合显示。 |
  | "one\_minus\_src\_color" | 1-源颜色 | 目标颜色×(1-源颜色) | 背景按新颜色剩余比例混合显示。 |
  | "dst\_color" | 目标颜色 | 目标颜色×目标颜色 | 背景按自身比例混合显示。 |
  | "one\_minus\_dst\_color" | 1-目标颜色 | 目标颜色×(1-目标颜色) | 背景按自身剩余比例混合显示。 |
  | "src\_alpha" | 源Alpha | 目标颜色×源Alpha | 背景按源Alpha比例混合显示。 |
  | "one\_minus\_src\_alpha" | 1-源Alpha | 目标颜色×(1-源Alpha) | 背景按源Alpha剩余比例混合显示。 |
  | "dst\_alpha" | 目标Alpha | 目标颜色×目标Alpha | 背景按自身Alpha比例混合显示。 |
  | "one\_minus\_dst\_alpha" | 1-目标Alpha | 目标颜色×(1-目标Alpha) | 背景按自身Alpha剩余比例混合显示。 |
  | "constant\_color" | 固定颜色常量 | 目标颜色×固定颜色常量 | 背景按固定颜色比例混合显示。 |
  | "one\_minus\_constant\_color" | 1-固定颜色常量 | 目标颜色×(1-固定颜色常量) | 背景按固定颜色剩余比例混合显示。 |
  | "constant\_alpha" | 固定Alpha常量 | 目标颜色×固定Alpha常量 | 背景按固定Alpha比例混合显示。 |
  | "one\_minus\_constant\_alpha" | 1-固定Alpha常量 | 目标颜色×(1-固定Alpha常量) | 背景按固定Alpha剩余比例混合显示。 |
  | "src\_alpha\_saturate" | min(源Alpha, 1-目标Alpha) | 目标颜色×min(源Alpha, 1-目标Alpha) | 背景按源Alpha与背景剩余Alpha最小值比例混合显示，避免叠加过强。 |
  | "src1\_color" | 第二源颜色 | 目标颜色×第二源颜色 | 背景按第二源颜色比例混合显示。 |
  | "one\_minus\_src1\_color" | 1-第二源颜色 | 目标颜色×(1-第二源颜色) | 背景按第二源颜色剩余比例混合显示。 |
  | "src1\_alpha" | 第二源Alpha | 目标颜色×第二源Alpha | 背景按第二源Alpha比例混合显示。 |
  | "one\_minus\_src1\_alpha" | 1-第二源Alpha | 目标颜色×(1-第二源Alpha) | 背景按第二源Alpha剩余比例混合显示。 |
* colorBlendOp：指定渲染源和渲染目标颜色通道的混合方式，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "add" | 源颜色+目标颜色。 |
  | "subtract" | 源颜色-目标颜色。 |
  | "reverse\_subtract" | 目标颜色-源颜色。 |
  | "min" | 取源颜色与目标颜色的最小值。 |
  | "max" | 取源颜色与目标颜色的最大值。 |
* srcAlphaBlendFactor：指定渲染源透明通道的混合因子，可取值及含义见下表。

  | 可取值 | 因子 | 结果 | 应用场景 |
  | --- | --- | --- | --- |
  | "zero" | 0 | 源Alpha×0=0 | 不显示新颜色透明度，相当于透明度清零。 |
  | "one" | 1 | 源Alpha×1=源Alpha | 保留新颜色透明度原样，不受影响。 |
  | "src\_color" | 源颜色 | 源Alpha×源颜色 | 新颜色透明度按自身颜色比例混合显示。 |
  | "one\_minus\_src\_color" | 1-源颜色 | 源Alpha×(1-源颜色) | 新颜色透明度按自身剩余颜色比例混合显示。 |
  | "dst\_color" | 目标颜色 | 源Alpha×目标颜色 | 新颜色透明度按背景颜色比例混合显示。 |
  | "one\_minus\_dst\_color" | 1-目标颜色 | 源Alpha×(1-目标颜色) | 新颜色透明度按背景剩余颜色比例混合显示。 |
  | "src\_alpha" | 源Alpha | 源Alpha×源Alpha | 新颜色透明度按自身Alpha比例混合显示。 |
  | "one\_minus\_src\_alpha" | 1-源Alpha | 源Alpha×(1-源Alpha) | 新颜色透明度按自身剩余Alpha比例混合显示。 |
  | "dst\_alpha" | 目标Alpha | 源Alpha×目标Alpha | 新颜色透明度按背景Alpha比例混合显示。 |
  | "one\_minus\_dst\_alpha" | 1-目标Alpha | 源Alpha×(1-目标Alpha) | 新颜色透明度按背景剩余Alpha比例混合显示。 |
  | "constant\_color" | 固定颜色常量 | 源Alpha×固定颜色常量 | 新颜色透明度按固定颜色比例混合显示。 |
  | "one\_minus\_constant\_color" | 1-固定颜色常量 | 源Alpha×(1-固定颜色常量) | 新颜色透明度按固定颜色剩余比例混合显示。 |
  | "constant\_alpha" | 固定Alpha常量 | 源Alpha×固定Alpha常量 | 新颜色透明度按固定Alpha比例混合显示。 |
  | "one\_minus\_constant\_alpha" | 1-固定Alpha常量 | 源Alpha×(1-固定Alpha常量) | 新颜色透明度按固定Alpha剩余比例混合显示。 |
  | "src\_alpha\_saturate" | min(源Alpha, 1-目标Alpha) | 源Alpha×min(源Alpha, 1-目标Alpha) | 新颜色透明度按源Alpha与背景剩余Alpha最小值比例混合显示，避免叠加过强。 |
  | "src1\_color" | 第二源颜色 | 源Alpha×第二源颜色 | 新颜色透明度按第二源颜色比例混合显示。 |
  | "one\_minus\_src1\_color" | 1-第二源颜色 | 源Alpha×(1-第二源颜色) | 新颜色透明度按第二源颜色剩余比例混合显示。 |
  | "src1\_alpha" | 第二源Alpha | 源Alpha×第二源Alpha | 新颜色透明度按第二源Alpha比例混合显示。 |
  | "one\_minus\_src1\_alpha" | 1-第二源Alpha | 源Alpha×(1-第二源Alpha) | 新颜色透明度按第二源Alpha剩余比例混合显示。 |
* dstAlphaBlendFactor：指定渲染目标透明通道的混合因子，可取值及含义见下表。

  | 可取值 | 因子 | 结果 | 应用场景 |
  | --- | --- | --- | --- |
  | "zero" | 0 | 目标Alpha×0=0 | 不显示背景透明度，相当于透明度清零。 |
  | "one" | 1 | 目标Alpha×1=目标Alpha | 保留背景透明度原样，不受影响。 |
  | "src\_color" | 源颜色 | 目标Alpha×源颜色 | 背景透明度按新颜色比例混合显示。 |
  | "one\_minus\_src\_color" | 1-源颜色 | 目标Alpha×(1-源颜色) | 背景透明度按新颜色剩余比例混合显示。 |
  | "dst\_color" | 目标颜色 | 目标Alpha×目标颜色 | 背景透明度按自身比例混合显示。 |
  | "one\_minus\_dst\_color" | 1-目标颜色 | 目标Alpha×(1-目标颜色) | 背景透明度按自身剩余比例混合显示。 |
  | "src\_alpha" | 源Alpha | 目标Alpha×源Alpha | 背景透明度按源Alpha比例混合显示。 |
  | "one\_minus\_src\_alpha" | 1-源Alpha | 目标Alpha×(1-源Alpha) | 背景透明度按源Alpha剩余比例混合显示。 |
  | "dst\_alpha" | 目标Alpha | 目标Alpha×目标Alpha | 背景透明度按自身Alpha比例混合显示。 |
  | "one\_minus\_dst\_alpha" | 1-目标Alpha | 目标Alpha×(1-目标Alpha) | 背景透明度按自身剩余Alpha比例混合显示。 |
  | "constant\_color" | 固定颜色常量 | 目标Alpha×固定颜色常量 | 背景透明度按固定颜色比例混合显示。 |
  | "one\_minus\_constant\_color" | 1-固定颜色常量 | 目标Alpha×(1-固定颜色常量) | 背景透明度按固定颜色剩余比例混合显示。 |
  | "constant\_alpha" | 固定Alpha常量 | 目标Alpha×固定Alpha常量 | 背景透明度按固定Alpha比例混合显示。 |
  | "one\_minus\_constant\_alpha" | 1-固定Alpha常量 | 目标Alpha×(1-固定Alpha常量) | 背景透明度按固定Alpha剩余比例混合显示。 |
  | "src\_alpha\_saturate" | min(源Alpha, 1-目标Alpha) | 目标Alpha×min(源Alpha, 1-目标Alpha) | 背景透明度按源Alpha与背景剩余Alpha最小值比例混合显示，避免叠加过强。 |
  | "src1\_color" | 第二源颜色 | 目标Alpha×第二源颜色 | 背景透明度按第二源颜色比例混合显示。 |
  | "one\_minus\_src1\_color" | 1-第二源颜色 | 目标Alpha×(1-第二源颜色) | 背景透明度按第二源颜色剩余比例混合显示。 |
  | "src1\_alpha" | 第二源Alpha | 目标Alpha×第二源Alpha | 背景透明度按第二源Alpha比例混合显示。 |
  | "one\_minus\_src1\_alpha" | 1-第二源Alpha | 目标Alpha×(1-第二源Alpha) | 背景透明度按第二源Alpha剩余比例混合显示。 |
* alphaBlendOp：指定渲染源和渲染目标透明通道的混合方式，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "add" | 源alpha+目标alpha。 |
  | "subtract" | 源alpha-目标alpha。 |
  | "reverse\_subtract" | 目标alpha-源alpha。 |
  | "min" | 取源alpha与目标alpha的最小值。 |
  | "max" | 取源alpha与目标alpha的最大值。 |

## materialMetadata

* 类型：array<MaterialMetadata>
* 说明：指定渲染材质的元数据。MaterialMetadata对象包含材质名称name及自定义属性customProperties。

### name

用于标识材质组件名称，当前有效值为"MaterialComponent"。

### customProperties

用于指定渲染中传入的自定义属性。包括data数组，用于指定渲染中传入的自定义数据。data数组中的对象包含以下属性：

* name：用于指定渲染中传入的自定义数据名称与自定义渲染中的数据名对应。
* displayName：用于指定3D编辑器中显示的名称。
* type：用于指定数据类型，可取值及含义见下表。

  | 可取值 | 说明 |
  | --- | --- |
  | "vec4" | 4维向量[x, y, z, w]。 |
  | "vec3" | 3维向量[x, y, z]。 |
  | "vec2" | 2维向量[x, y]。 |
  | "float" | 浮点数。 |
  | "int" | 整数。 |
* value：属性默认值。

## 示例

```
1. {
2. "compatibility_info" : { "version" : "22.00", "type" : "shader" },
3. "vert": "3dshaders://shader/core3d_dm_fw.vert.spv",
4. "frag": "appshaders://custom_shader/custom_material_sample.frag.spv",
5. "vertexInputDeclaration": "3dvertexinputdeclarations://core3d_dm_fw.shadervid",
6. "state": {
7. "rasterizationState": {
8. "enableDepthClamp": false,
9. "enableDepthBias": false,
10. "enableRasterizerDiscard": false,
11. "polygonMode": "fill",
12. "cullModeFlags": "back",
13. "frontFace": "counter_clockwise"
14. },
15. "depthStencilState": {
16. "enableDepthTest": true,
17. "enableDepthWrite": true,
18. "enableDepthBoundsTest": false,
19. "enableStencilTest": false,
20. "depthCompareOp": "less_or_equal"
21. },
22. "colorBlendState": {
23. "colorAttachments": [
24. {
25. "enableBlend": true,
26. "colorWriteMask": "r_bit|g_bit|b_bit|a_bit",
27. "srcColorBlendFactor": "one",
28. "dstColorBlendFactor": "one_minus_src_alpha",
29. "colorBlendOp": "add",
30. "srcAlphaBlendFactor": "one",
31. "dstAlphaBlendFactor": "one_minus_src_alpha",
32. "alphaBlendOp": "add"
33. }
34. ]
35. }
36. },
37. "materialMetadata": [
38. {
39. "name": "MaterialComponent",
40. "customProperties": [
41. {
42. "data": [
43. {
44. "name": "vec_1",
45. "displayName": "Color",
46. "type": "vec4",
47. "value" : [1.0,1.0,1.0,1.0]
48. },
49. {
50. "name": "time",
51. "displayName": "Time",
52. "type": "float",
53. "value": 0.0
54. },
55. {
56. "name": "dof",
57. "displayName": "Dof",
58. "type": "int",
59. "value": 1
60. },
61. {
62. "name": "motionblur",
63. "displayName": "MotionBlur",
64. "type": "int",
65. "value": 1
66. }
67. ]
68. }
69. ]
70. }
71. ]
72. }
```
