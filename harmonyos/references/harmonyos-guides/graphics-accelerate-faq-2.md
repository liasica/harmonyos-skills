---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-2
title: 开启超帧外插模式后运动物体边缘出现严重拖影现象，可能的原因是什么
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏渲染加速服务 > 开启超帧外插模式后运动物体边缘出现严重拖影现象，可能的原因是什么
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:08+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:2fb64aa0cf4f06a0096eafbc9025b2dfc01a484764eb54b0655152c128a84357
---

由于外插模式需要标记模板缓冲（Stencil Buffer）的第8位用于区分静态物体和动态物体，即静态物体模板值第8位标记成0，动态物体模板值第8位标记成1，模板缓冲的低7位模板值开发者可自行设置。如果标记错误或漏标记，可能会在动态物体边缘产生严重的拖影现象。

**现象描述**

Demo中运动角色出现头身分离等严重拖影现象，角色头部向右偏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ga0dlGeYQAC7UORLQ9B_SA/zh-cn_image_0000002788467792.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=F61635ADB15DA8EA091DF8CF4328E602ECEBD5FBF420D38383BE565610BFD5DD)

**原因分析**

通过抓帧查看模板缓冲中的模板值，发现头发区域模板值为0，身体区域模板值为0x80。由于角色头、身均属于运动目标区域，应该将所有运动物体区域的模板值第8位标记为1。错误的头部区域模板值导致超帧效果出现头身分离的严重拖影现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/azdikLicRzKJPu98VweaWA/zh-cn_image_0000002817507281.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C847E5D0CDA6977DE6E88087D87611A98DB0BDE29185291C5864E4C1006566F)

**处理步骤**

基于分析结论，造成头身分离拖影现象的主要原因是运动区域模板值未统一标记为1xxx xxxx。因此将运动角色头发和面部区域的模板值统一改为0x80，保持和身体模板值一致，头身分离的拖影现象消失，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/AGH6uOq_Sxeo4FbSeln9Ow/zh-cn_image_0000002788307850.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=59FB2175E785479BC0F3AC627415BB1D4FB9F5E833AAFC47159A49959121A296)

**代码示例**

检查动态物体材质Shader中的模板值是否设置正确，即静态物体模板值标记为0xxx xxxx，动态物体模板值标记为1xxx xxxx。

```cs
Shader "Standard_with_stencil"
{
    Properties
    {
        /* ... */
        _LightingStencilRef("Lighting Stencil Reference", Float) = 128 // 将动态物体材质模板值改为1xxx xxxx，消除头身分离现象
        [Enum(UnityEngine.Rendering.CompareFunction)] _LightingStencilComp("Lighting Stencil Comparison", Float) = 8
        _StencilReadMask("Stencil Read Mask", Float) = 255
        _StencilWriteMask("Stencil Write Mask", Float) = 255
    }
    SubShader
    {
        /* ... */
        Pass
        {
            /* ... */
            Stencil
            {
                Ref[_LightingStencilRef]
                Comp[_LightingStencilComp]
                ReadMask[_StencilReadMask]
                WriteMask[_StencilWriteMask]
                Pass Replace
            }
        }
    }
}
```

**说明** 

不同管线的Shader中需要配置模板值的Pass不同，如下：

* 团结引擎URP管线

  在每个有DepthOnly或DepthNormals的Pass中，即出现Tags {"LightMode" = "DepthOnly" }或Tags {"LightMode" = "DepthNormals" }的Pass，配置模板值。
* 团结引擎Build-in管线

  在每个有ForwardBase或ForwardAdd的Pass中，即出现Tags {"LightMode" = "ForwardBase" }或Tags {"LightMode" = "ForwardAdd" }的Pass，配置模板值。
