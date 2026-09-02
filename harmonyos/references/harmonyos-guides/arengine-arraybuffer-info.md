---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info
title: 数据类型转换说明
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 数据类型转换说明
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:20+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8e79f7428ac50a249ac054808c25c90a4c6ec14a21cf1cd6e3690e77e0649126
---

在开发AR应用时，部分数据类型需要转换才能使用，以下进行汇总及示例。

## ArrayBuffer

在一些不支持接收ArrayBuffer数据类型的方法中，需要将其反序列化为int32或者float32类型，涉及转换的接口列表如下：

| 接口名 | 描述 |
| --- | --- |
| [ImageComponent](../harmonyos-references/arengine-api-arengine.md#imagecomponent) | 参数buffer为ArrayBuffer类型，可转换为int32。 |
| [ARPlane.getPolygonXZ](../harmonyos-references/arengine-api-arengine.md#arplanegetpolygonxz) | 返回值为ArrayBuffer类型，可转换为float32。 |
| [ARSceneMesh.getVertices](../harmonyos-references/arengine-api-arengine.md#arscenemeshgetvertices) | 返回值为ArrayBuffer类型，可转换为float32。 |
| [ARSceneMesh.getVertexNormals](../harmonyos-references/arengine-api-arengine.md#arscenemeshgetvertexnormals) | 返回值为ArrayBuffer类型，可转换为float32。 |
| [ARSceneMesh.getTriangleIndices](../harmonyos-references/arengine-api-arengine.md#arscenemeshgettriangleindices) | 返回值为ArrayBuffer类型，可转换为int32。 |
| [ARSemanticDensePointData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensepointdata) | 参数id为ArrayBuffer类型，可转换为int32。 |
| [ARSemanticDensePointData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensepointdata) | 参数position为ArrayBuffer类型，可转换为float32。 |
| [ARSemanticDensePointData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensepointdata) | 参数color为ArrayBuffer类型，可转换为int32。 |

转换的示例如下：

```typescript
export function arrayBufferFloat32ToNumber(buffer: ArrayBuffer): number[] {
  let view: Float32Array = new Float32Array(buffer);
  let numberArray: number[] = Array.from(view);
  return numberArray;
}

export function arrayBufferInt32ToNumber(buffer: ArrayBuffer): number[] {
  let view: Int32Array = new Int32Array(buffer);
  let numberArray: number[] = Array.from(view);
  return numberArray;
}
```
