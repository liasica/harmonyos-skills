---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform
title: animateTransform
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > animateTransform
category: harmonyos-references
scraped_at: 2026-04-29T13:53:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:255aa2ffe8a36c7cddf3df0f78e4f8fef045f7265ccb6ae126231c517771f730
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

transform动效，支持的组件范围：

<circle>, <ellipse>, <line>, <path>, <polygon>, <polyline>, <rect>, <text>

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

支持animate属性和以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | [translate | scale | rotate | skewX | skewY] | - | 是 | 设置transform动画的类型 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="back_container">
4. <svg>
5. <polygon points="60,30 90,90 30,90" fill="red">
6. <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0 120 140" to="360 360 420" dur="3s" repeatCount="indefinite"></animateTransform>
7. </polygon>
8. <polygon points="60,30 90,90 30,90" fill="red">
9. <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animateTransform>
10. </polygon>
11. <polygon points="60,30 90,90 30,90" fill="green">
12. <animateTransform attributeName="transform" attributeType="XML" type="scale" from="1" to="2" dur="3s" repeatCount="indefinite"></animateTransform>
13. </polygon>
14. <polygon points="60,30 90,90 30,90" fill="green">
15. <animateTransform attributeName="transform" attributeType="XML" type="scale" from="1 1" to="2 4" dur="3s" repeatCount="indefinite"></animateTransform>
16. </polygon>
17. <polygon points="60,30 90,90 30,90" fill="#D2691E">
18. <animateTransform attributeName="transform" attributeType="XML" type="skewX" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
19. </polygon>
20. <polygon points="60,30 90,90 30,90" fill="#D2691E">
21. <animateTransform attributeName="transform" attributeType="XML" type="skewY" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
22. </polygon>
23. <polygon points="60,30 90,90 30,90" fill="#D2691E">
24. <animateTransform attributeName="transform" attributeType="XML" type="skewX" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
25. <animateTransform attributeName="transform" attributeType="XML" type="skewY" from="10" to="100" dur="3s" repeatCount="indefinite"></animateTransform>
26. </polygon>
27. <polygon points="60,30 90,90 30,90" fill="blue">
28. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300" dur="3s" repeatCount="indefinite"></animateTransform>
29. </polygon>
30. <polygon points="60,30 90,90 30,90" fill="blue">
31. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0 0" to="0 300" dur="3s" repeatCount="indefinite"></animateTransform>
32. </polygon>
33. <polygon points="60,30 90,90 30,90" fill="blue">
34. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0 0" to="300 300" dur="3s" repeatCount="indefinite"></animateTransform>
35. </polygon>
36. </svg>
37. </div>
38. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: flex-start;
5. align-items: flex-start;
6. background-color: #f8f8ff;
7. }

9. .back_container {
10. flex-direction: row;
11. justify-content: flex-start;
12. align-items: flex-start;
13. height: 1000px;
14. width: 1080px;
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/LhcIyv9NS4WuUMn_FaMCOg/zh-cn_image_0000002589326647.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055338Z&HW-CC-Expire=86400&HW-CC-Sign=EFAE3E8E71DA969927859CE0529BBDA66978A47986242CEFD49F9F8351CC2204)

动画叠加

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="back_container">
4. <svg>
5. <polygon points="60,30 90,90 30,90" fill="black">
6. <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
7. 600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
8. </polygon>
9. <polygon points="60,30 90,90 30,90" fill="green">
10. <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
11. 600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
12. <animateTransform attributeName="transform" attributeType="XML" type="rotate" values="0; 5; 0; 10" keyTimes="0;
13. 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
14. </polygon>
15. <polygon points="60,30 90,90 30,90" fill="blue">
16. <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
17. 600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
18. <animateTransform attributeName="transform" attributeType="XML" type="scale" values="1; 1.2; 1; 1.2"
19. keyTimes="0; 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
20. </polygon>
21. <polygon points="60,30 90,90 30,90" fill="red">
22. <animateTransform attributeName="transform" attributeType="XML" type="translate" values="0 0; 200 200; 400 0;
23. 600 200" keyTimes="0; 0.4; 0.8;1.0" dur="3s" repeatCount="indefinite"></animateTransform>
24. <animateTransform attributeName="transform" attributeType="XML" type="scale" values="1; 1.2; 1; 1.2"
25. keyTimes="0; 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
26. <animateTransform attributeName="transform" attributeType="XML" type="skewX" values="0; 10; 0; 10"
27. keyTimes="0; 0.4; 0.8; 1.0" dur="3s" repeatCount="indefinite"></animateTransform>
28. </polygon>
29. </svg>
30. </div>
31. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: flex-start;
5. align-items: flex-start;
6. background-color: #f8f8ff;
7. }
8. .back_container {
9. flex-direction: row;
10. justify-content: flex-start;
11. align-items: flex-start;
12. height: 1000px;
13. width: 1080px;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/AVy3EL6VSBiJiok7TvNydg/zh-cn_image_0000002589246589.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055338Z&HW-CC-Expire=86400&HW-CC-Sign=AC4CA5C0C00B1E9F4158B7B4FD497FE6D7D57E451042FA30E992777DD12C561C)

涉及组件示例

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="back_container">
4. <svg>
5. <svg fill="white" width="600" height="600" viewBox="0 0 50 50">
6. <path stroke="black" fill="none" stroke-linejoin="miter" stroke-miterlimit="1" id="p2"
7. d="M1,19 l7,-3 l7,3 m2,0 l3.5,-3 l3.5 ,3 m2,0 l2 ,-3 l2 ,3 m2,0 l0.75,-3 l0.75,3 m2,0 l0.5 ,-3 l0.5,3">
8. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="25"
9. dur="3s" repeatCount="indefinite"></animateTransform>
10. </path>
11. </svg>
12. <polygon points="60,20 90,80 30,80" fill="black">
13. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
14. dur="3s" repeatCount="indefinite"></animateTransform>
15. </polygon>
16. <circle cx="60" cy="130" r="40" stroke-width="4" fill="white" stroke="blue">
17. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
18. dur="3s" repeatCount="indefinite"></animateTransform>
19. </circle>
20. <line x1="10" x2="300" y1="280" y2="280" stroke-width="10" stroke="black" stroke-linecap="square">
21. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
22. dur="3s" repeatCount="indefinite"></animateTransform>
23. </line>
24. <polyline points="10,380 50,335 50,385 100,310" fill="white" stroke="black">
25. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
26. dur="3s" repeatCount="indefinite"></animateTransform>
27. </polyline>
28. <ellipse cx="100" cy="450" rx="70" ry="50" fill="blue">
29. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
30. dur="3s" repeatCount="indefinite"></animateTransform>
31. </ellipse>
32. <rect width="100" height="100" x="50" y="540" stroke-width="10" stroke="red" rx="10" ry="10"
33. stroke-dasharray="5 3" stroke-dashoffset="3">
34. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
35. dur="3s" repeatCount="indefinite"></animateTransform>
36. </rect>
37. <text x="20" y="700" fill="#D2691E" font-size="40">
38. animate-transform
39. <animateTransform attributeName="transform" attributeType="XML" type="translate" from="0" to="300"
40. dur="3s" repeatCount="indefinite"></animateTransform>
41. </text>
42. </svg>
43. </div>
44. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: flex-start;
5. align-items: flex-start;
6. background-color: #f8f8ff;
7. }
8. .back_container {
9. flex-direction: row;
10. justify-content: flex-start;
11. align-items: flex-start;
12. height: 1000px;
13. width: 1080px;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Rzcd4VO2QdOUeur-qF6O0g/zh-cn_image_0000002558766782.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055338Z&HW-CC-Expire=86400&HW-CC-Sign=3D9BA988C58BAD93FBBCE615ACE2400147B7767D876157DF82C2B675A2590D91)
