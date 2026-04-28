---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-65
title: 如何定制构建多目标产物
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何定制构建多目标产物
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6162e09a6a0f9b4ef255758bc2ba7fca6bf5fcdaa1a1d1d6de82f8038a17ee7b
---

**问题场景：**

根据不同的部署环境、目标人群和运行环境，定制构建多目标产物，将同一应用定制为不同版本。

**参考代码：**

1、项目build-profile.json5配置示例如下：

```
1. {
2. "app": {
3. "products": [
4. {
5. "name": "default",
6. "signingConfig": "default",
7. "compileSdkVersion": "4.1.0(11)",
8. "compatibleSdkVersion": "4.1.0(11)",
9. "runtimeOS": "HarmonyOS",
10. },
11. {
12. "name": "release",
13. "signingConfig": "release",
14. "compileSdkVersion": "4.1.0(11)",
15. "compatibleSdkVersion": "4.1.0(11)",
16. "runtimeOS": "HarmonyOS",
17. },
18. {
19. "name": "beta1",
20. "compileSdkVersion": "4.1.0(11)",
21. "compatibleSdkVersion": "4.1.0(11)",
22. "runtimeOS": "HarmonyOS",
23. },
24. {
25. "name": "zhaohangzhuanyong",
26. "compileSdkVersion": "4.1.0(11)",
27. "compatibleSdkVersion": "4.1.0(11)",
28. "runtimeOS": "HarmonyOS",
29. }
30. ],
31. "buildModeSet": [
32. {
33. "name": "debug",
34. },
35. {
36. "name": "beta1"
37. }
38. ],
39. "signingConfigs": [
40. {
41. "name": "release",
42. "material": {
43. "storePassword": "",
44. "certpath": "",
45. "keyAlias": "",
46. "keyPassword": "",
47. "profile": "",
48. "signAlg": "SHA256withECDSA",
49. "storeFile": ""
50. },
51. "type": "HarmonyOS"
52. },
53. {
54. "name": "default",
55. "material": {
56. "storePassword": "",
57. "certpath": "",
58. "keyAlias": "",
59. "keyPassword": "",
60. "profile": "",
61. "signAlg": "SHA256withECDSA",
62. "storeFile": ""
63. },
64. "type": "HarmonyOS"
65. }
66. ]
67. },
68. "modules": [
69. {
70. "name": "entry",
71. "srcPath": "./entry",
72. "targets": [
73. {
74. "name": "default",
75. "applyToProducts": [
76. "release"
77. ]
78. }
79. ]
80. },
81. {
82. "name": "library1",
83. "srcPath": "./library1"
84. },
85. {
86. "name": "library2",
87. "srcPath": "./library2"
88. },
89. {
90. "name": "library",
91. "srcPath": "./library",
92. "targets": [
93. {
94. "name": "default",
95. "applyToProducts": [
96. "release"
97. ]
98. }
99. ]
100. },
101. ]
102. }
```

[build-profile\_demo.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/build-profile_demo.json5#L3-L104)

2、target的配置在modules下的build-profile.json5中，配置示例如下：

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. "arkOptions": {
5. // "apPath": "./modules.ap" /* Profile used for profile-guided optimization (PGO), a compiler optimization technique to improve app runtime performance. */
6. }
7. },
8. "buildOptionSet": [
9. {
10. "name": "release",
11. "arkOptions": {
12. "obfuscation": {
13. "ruleOptions": {
14. "enable": true,
15. "files": [
16. "./obfuscation-rules.txt"
17. ]
18. }
19. }
20. }
21. },
22. ],
23. "targets": [
24. {
25. "name": "default",
26. "runtimeOS": "HarmonyOS"
27. },
28. {
29. "name": "ohosTest",
30. }
31. ]
32. }
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library3/build-profile.json5#L3-L34)
