---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform
title: animateTransform
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > animateTransform
category: harmonyos-references
scraped_at: 2026-11-21T09:14:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b6cc2838e91970f8ea9c60d8a10a423ddba5bec6b52335334fc1c892a3a5f82c
---

**说明** 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

transform动效，支持的组件范围：

<circle>, <ellipse>, <line>, <path>, <polygon>, <polyline>, <rect>, <text>

## 权限列表

无

## 子组件

不支持。

## 属性

支持animate属性和以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | [translate | scale | rotate | skewX | skewY] | - | 是 | 设置transform动画的类型 |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <div class="back_container">
    <svg>
      <polygon points="60,30 90,90 30,90" fill="red">
        <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0 120 140" to="360 360 420" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="red">
        <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="green">
        <animateTransform attributeName="transform" attributeType="XML" type="scale" from="1" to="2" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="green">
        <animateTransform attributeName="transform" attributeType="XML" type="scale" from="1 1" to="2 4" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="#D2691E">
        <animateTransform attributeName="transform" attributeType="XML" type="skewX" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="#D2691E">
        <animateTransform attributeName="transform" attributeType="XML" type="skewY" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="#D2691E">
        <animateTransform attributeName="transform" attributeType="XML" type="skewX" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
        <animateTransform attributeName="transform" attributeType="XML" type="skewY" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="blue">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="blue">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0 0" to="0 300" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="blue">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0 0" to="300 300" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
    </svg>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #f8f8ff;
}

.back_container {
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
  height: 1000px;
  width: 1080px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/QU-3y60KQ-6fsOWLx942EQ/zh-cn_image_0000002821759463.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011322Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE9C910CE752187E802E7B66E52CD0766F3F296EC9C8BF2D27ADA301773FF135)

动画叠加

```html
<!-- xxx.hml -->
<div class="container">
  <div class="back_container">
    <svg>
      <polygon points="60,30 90,90 30,90" fill="black">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
          600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="green">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
          600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
        <animateTransform attributeName="transform" attributeType="XML" type="rotate" values="0; 5; 0; 10" keyTimes="0;
          0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="blue">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
          600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
        <animateTransform attributeName="transform" attributeType="XML" type="scale" values="1; 1.2; 1; 1.2"
          keyTimes="0; 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <polygon points="60,30 90,90 30,90" fill="red">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
          600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
        <animateTransform attributeName="transform" attributeType="XML" type="scale" values="1; 1.2; 1; 1.2"
          keyTimes="0; 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
        <animateTransform attributeName="transform" attributeType="XML" type="skewX" values="0; 10; 0; 10"
          keyTimes="0; 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
    </svg>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #f8f8ff;
}
.back_container {
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
  height: 1000px;
  width: 1080px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/UPF-r_H0T-iPiwQsiheOsQ/zh-cn_image_0000002793039534.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011322Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF925A4C6742AF3845918EA08AF12C6FB6387BBD55C9B2B996AE30803BF02F1D)

涉及组件示例

```html
<!-- xxx.hml -->
<div class="container">
  <div class="back_container">
    <svg>
      <svg fill="white" width="600" height="600" viewBox="0 0 50 50">
        <path stroke="black" fill="none" stroke-linejoin="miter" stroke-miterlimit="1" id="p2"
          d="M1,19 l7,-3 l7,3 m2,0 l3.5,-3 l3.5 ,3 m2,0 l2 ,-3 l2 ,3 m2,0 l0.75,-3 l0.75,3 m2,0 l0.5 ,-3 l0.5,3">
          <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="25"
            dur="3s" repeatCount="indefinite"></animateTransform>
        </path>
      </svg>
      <polygon points="60,20 90,80 30,80" fill="black">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </polygon>
      <circle cx="60" cy="130" r="40" stroke-width="4" fill="white" stroke="blue">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </circle>
      <line x1="10" x2="300" y1="280" y2="280" stroke-width="10" stroke="black" stroke-linecap="square">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </line>
      <polyline points="10,380 50,335 50,385 100,310" fill="white" stroke="black">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </polyline>
      <ellipse cx="100" cy="450" rx="70" ry="50" fill="blue">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </ellipse>
      <rect width="100" height="100" x="50" y="540" stroke-width="10" stroke="red" rx="10" ry="10"
        stroke-dasharray="5 3" stroke-dashoffset="3">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </rect>
      <text x="20" y="700" fill="#D2691E" font-size="40">
        animate-transform
        <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
          dur="3s" repeatCount="indefinite"></animateTransform>
      </text>
    </svg>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #f8f8ff;
}
.back_container {
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
  height: 1000px;
  width: 1080px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/WpSEIHQbRbSpPqcrvrZEnQ/zh-cn_image_0000002792879560.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011322Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1E05AF4E2D7ACC4ED239A1EE33E9D0D2EBA851EC98DD995801E026C57FE8565)
