---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-aipp-configuration-file
title: 模型转换AIPP配置文件说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > AIPP > 模型转换AIPP配置文件说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7130d949b7050563ebdc14c544289bf406ab662ef2096b07ccc5fc5bc83d5585
---

## 模型转换AIPP配置文件说明

一份功能完整的AIPP配置文件示例如下：

```
1. # AIPP的配置以aipp_op开始，标识这是一个AIPP算子的配置，aipp_op支持配置多个
2. aipp_op {
3. # input_name参数为可选，标识对模型的哪个输入做AIPP处理
4. # 类型：string
5. input_name: "data"

7. # related_input_rank参数为可选，与input_name对应，推荐使用input_name，当模型输入名称未知时，可使用related_input_rank标识对模型的第几个输入做AIPP处理
8. # 类型：uint32
9. related_input_rank: 0

11. # node_after_aipp参数为可选，用于当一个输入之后有多个分支，需要对分支进行不同的AIPP处理的场景，且需满足均配置或者均不配置，不能只配置一部分分支
12. # 类型：string
13. node_after_aipp: "op_name"

15. # input_edge_idx参数为可选，与node_after_aipp对应，当输入Data算子之后的若干算子名称重复时，可以使用input_edge_idx标识对第几个分支进行AIPP处理
16. # 类型：uint32
17. input_edge_idx: 0

19. input_para {
20. # 输入图片的类型
21. # 类型: enum
22. # 取值范围：[YUV420SP_U8, XRGB8888_U8, ARGB8888_U8, YUYV_U8, YUV422SP_U8, AYUV444_U8, YUV400_U8, RGB888_U8]
23. format: AYUV444_U8

25. shape {
26. # 输入图片的宽度、高度
27. # 类型：uint32
28. # 取值范围 & 约束：[0,4096]、对于除了YUV400之外的YUV类型的图片，要求取值是偶数
29. src_image_size_w: 800
30. src_image_size_h: 600
31. }

33. # max_src_image_size用于动态AIPP的场景，当图片的长宽或者输入类型不确定时，设置输入图片最大的size
34. # 类型: uint32
35. max_src_image_size: 102400
36. }

38. # == Crop参数设置 == #
39. crop_func {
40. switch: true
41. dynamic: true
42. load_start_pos_w: 50
43. load_start_pos_h: 50
44. crop_size_w: 400
45. crop_size_h: 400
46. }

48. # == Channel Swap参数设置 == #
49. swap_func {
50. dynamic: true
51. rbuv_swap_switch: true
52. ax_swap_switch: true
53. }

55. # == Resize参数设置 == #
56. resize_func {
57. switch: true
58. dynamic: true
59. resize_output_w: 200
60. resize_output_h: 200
61. }

63. # == Color Space Conversion参数设置 == #
64. csc_func {
65. switch: true
66. dynamic: true
67. matrix_r0c0: 256
68. matrix_r0c1: 0
69. matrix_r0c2: 259
70. matrix_r1c0: 256
71. matrix_r1c1: -88
72. matrix_r1c2: -183
73. matrix_r2c0: 256
74. matrix_r2c1: 454
75. matrix_r2c2: 0
76. output_bias_0: 0
77. output_bias_1: 0
78. output_bias_2: 0
79. input_bias_0: 16
80. input_bias_1: 128
81. input_bias_2: 128
82. }

84. # == Data Type Conversion参数设置 == #
85. dtc_func {
86. switch: true
87. dynamic: true
88. mean_chn_0: 0
89. mean_chn_1: 0
90. mean_chn_2: 0
91. mean_chn_3: 0
92. min_chn_0: 0
93. min_chn_1: 0
94. min_chn_2: 0
95. min_chn_3: 0
96. var_reci_chn_0: 1.0
97. var_reci_chn_1: 1.0
98. var_reci_chn_2: 1.0
99. var_reci_chn_3: 1.0
100. }

102. # == Rotation参数设置 == #
103. rotation_func {
104. switch: true
105. dynamic: true
106. rotation_angle: 0.0
107. }

109. # == Padding参数设置 == #
110. padding_func {
111. switch: true
112. dynamic: true
113. left_padding_size: 12
114. right_padding_size: 12
115. top_padding_size: 12
116. bottom_padding_size: 12
117. padding_value_chn_0: 20.0
118. padding_value_chn_1: 20.0
119. padding_value_chn_2: 20.0
120. padding_value_chn_3: 20.0
121. }
122. }
```

### AIPP配置多输入支持

AIPP支持对一个多输入模型的多个输入分别配置AIPP，也支持在一个输入Data算子有多个输出分支的情况下，对不同的输出分支分别配置AIPP。

AIPP配置的多输入支持由2组共4个配置参数控制：input\_name和related\_input\_rank用于指定对哪一个输入进行AIPP处理，node\_after\_aipp和input\_edge\_idx用于指定对Data算子的多个输出中的哪一个输出进行AIPP处理。

input\_name和related\_input\_rank两个参数推荐使用input\_name，related\_input\_rank参数用于模型输入名称不确定的场景，如果同时配置这两个参数，则两个参数互为校验；如果两个参数都没有被配置，默认对模型的第一个输入进行AIPP处理。

node\_after\_aipp和input\_edge\_idx两个参数推荐使用node\_after\_aipp，input\_edge\_idx用于Data算子的多个输出分支衔接的算子名称重复或不确定的场景，如果同时配置这两个参数，则两个参数互为校验；如果两个参数都没有被配置，则该Data算子的所有输出分支使用同一个AIPP处理。

### AIPP配置区分动态AIPP与静态AIPP

只要有一个AIPP子功能的dynamic开关配置为true，或者没有打开任何一个子功能的开关，则生成的DaVinci模型为动态AIPP模型，需要在模型推理阶段传入AIPP配置参数；相反没有任何子功能的dynamic开关配置为true，并且至少有一个子功能的开关是打开的，则生成的DaVinci模型为静态AIPP模型，模型推理阶段使用配置文件中定义的AIPP配置参数。

对于动态AIPP的场景，AIPP可以允许输入图片的长宽，以及图片类型不确定，对应即src\_image\_size\_w、src\_image\_size\_h和input\_format三个参数不配置，此时开发者需要指定动态AIPP处理时的最大图片尺寸，配置max\_src\_image\_size。

## 图片裁剪(Crop)

图片裁剪功能是指在原始图片中从指定的起点裁剪出指定大小的子图。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

* 静态配置时，crop\_size\_w和crop\_size\_h以设定的值作为输出shape。
* 动态配置时，crop\_size\_w和crop\_size\_h为预分配的最大输出shape，实际运行时设置的参数值不超过预分配的最大值。

### 静态配置

```
1. crop_func {
2. switch: true
3. load_start_pos_w: 50
4. load_start_pos_h: 50
5. crop_size_w: 150
6. crop_size_h: 150
7. }
```

### 动态配置

```
1. crop_func {
2. switch: true
3. dynamic: true
4. load_start_pos_w: 0
5. load_start_pos_h: 0
6. crop_size_w: 150
7. crop_size_h: 150
8. }
```

## 通道交换功能(axSwap/uvSwap/rbSwap)

交换图片的通道支持AX通道交换、UV通道交换、RB通道交换。

* AX通道交换：仅支持ARGB8888、XRGB8888、AYUV444格式，其他格式不支持。
* UV通道交换：仅支持YUV420SP、YUV422SP\_U8、YUYV、AYUV444格式，其他格式不支持。
* RB通道交换：仅支持ARGB8888、XRGB8888、RGB888\_U8格式，其他格式不支持。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```
1. swap_func {
2. ax_swap_switch: true
3. rbuv_swap_switch: false
4. }
```

### 动态配置

可以不写具体的参数，在动态创建input tensor时指定。

```
1. swap_func {
2. dynamic: true
3. ax_swap_switch: true
4. rbuv_swap_switch: false
5. }
```

## 色域转换功能(CSC)

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

支持的转换格式如下：

* 支持从YUV420SP、YUYV、YUV422SP、AYUV444转到RGB888、BGR888。
* 支持从XRGB8888、ARGB8888、RGB888转到YVU444SP、YUV444SP、YUV400。

### 静态配置

静态AIPP配置色域转化矩阵示例如下。

```
1. csc_func {
2. switch: true
3. matrix_r0c0: 256
4. matrix_r0c1: 454
5. matrix_r0c2: 0
6. matrix_r1c0: 256
7. matrix_r1c1: -88
8. matrix_r1c2: -183
9. matrix_r2c0: 256
10. matrix_r2c1: 0
11. matrix_r2c2: 359
12. output_bias_0: 0
13. output_bias_1: 0
14. output_bias_2: 0
15. input_bias_0: 0
16. input_bias_1: 128
17. input_bias_2: 128
18. }
```

### 动态配置

指定输出的色域格式，动态场景下，inputFormat可以改变，但是output\_format不可变，否则会报错，因为输出的格式一般是固定的。

```
1. csc_func {
2. switch: true
3. dynamic: true
4. output_format: RGB888_U8
5. color_space: JPEG
6. }
```

## 图片缩放(Resize)

图片缩放功能支持图片放大缩小，采用双线性插值方式进行缩放。缩放输出图片最小为16x16，缩放输出最大为448x448。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```
1. resize_func {
2. switch: true
3. resize_output_w: 182
4. resize_output_h: 182
5. }
```

### 动态配置

resize\_output\_w、resize\_output\_h为预分配最大size。

```
1. resize_func {
2. switch: true
3. dynamic: true
4. resize_output_w: 250
5. resize_output_h: 200
6. }
```

## 数据类型转换(DTC)

数据类型转化功能是指将输入的图片数据类型通过转化公式转换为FP16类型送给后续模块计算，实际为依次执行减均值、减最小值和乘方差操作。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```
1. dtc_func {
2. switch: true
3. mean_chn_0: 4
4. mean_chn_1: 4
5. mean_chn_2: 4
6. min_chn_0: 2.0
7. min_chn_1: 2.0
8. min_chn_2: 2.0
9. var_reci_chn_0: 2.0
10. var_reci_chn_1: 2.0
11. var_reci_chn_2: 2.0
12. }
```

### 动态配置

可以不写具体的参数，在动态创建input tensor时指定。

```
1. dtc_func {
2. switch: true
3. dynamic: true
4. }
```

## 图片旋转(Rotation)

旋转功能支持图片旋转90°、180°和270°，以适配手机在不同方向时的图像数据。当前旋转功能只支持静态单算子场景，动态场景以及卷积融合场景不支持。静态配置如下。

```
1. rotate_para {
2. switch: true
3. dynamic: true
4. rotation_angle: 0.0
5. }
```

## 图片补边

图片补边功能支持在图片上下左右padding指定大小的数据。 padding的数据可以按通道来设置不同的值，最多补四个通道，如果有的通道没有设置的话，就默认补0，上下左右Padding的大小最大为32，即最多上下各补32行，左右各补32列。

* 当crop或resize作为最后一个AIPP算子时，它的输出shape固定，即输出shape不可动态调整。后面如果接卷积，卷积的输入shape就是crop或resize的输出shape。
* 当crop或者resize后接padding算子时

  + 如果padding算子是静态的，那么padding算子前面的crop或resize也相当于是静态的，输出shape固定不变，crop或resize的输出shape加上padding的值就是后面卷积的shape。
  + 如果padding算子是动态的，那么padding算子的四个padding值就写0。此时，padding算子前的crop或resize的输出就是后面卷积的shape。动态时可以调整参数值，但是要保证最终的输出等于卷积的输入。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```
1. padding_func {
2. switch: true
3. left_padding_size: 21
4. right_padding_size: 21
5. top_padding_size: 21
6. bottom_padding_size: 21
7. padding_value_chn_0: 20.0
8. padding_value_chn_1: 20.0
9. padding_value_chn_2: 20.0
10. padding_value_chn_3: 20.0
11. }
```

### 动态配置

padding算子是动态的，padding算子的四个padding值就写0，padding value的值在动态创建input tensor时指定。

```
1. padding_func {
2. switch: true
3. dynamic: true
4. left_padding_size: 0
5. right_padding_size: 0
6. top_padding_size: 0
7. bottom_padding_size: 0
8. }
```

## 完整AIPP动态配置示例

```
1. aipp_op {
2. input_para {
3. shape {
4. src_image_size_w: 480
5. src_image_size_h: 384
6. }
7. }
8. crop_func {
9. switch: true
10. dynamic: true
11. load_start_pos_w: 50
12. load_start_pos_h: 50
13. crop_size_w: 150
14. crop_size_h: 150
15. }
16. resize_func {
17. switch: true
18. dynamic: true
19. resize_output_w: 250
20. resize_output_h: 200
21. }
22. padding_func {
23. switch: true
24. dynamic: true
25. left_padding_size: 0
26. right_padding_size: 0
27. top_padding_size: 0
28. bottom_padding_size: 0
29. }
30. swap_func {
31. dynamic: true
32. ax_swap_switch: true
33. }
34. csc_func {
35. switch: true
36. dynamic: true
37. output_format: RGB888_U8
38. color_space: JPEG
39. }
40. dtc_func {
41. switch: true
42. dynamic: true
43. }
44. }
```

## 完整AIPP静态配置

```
1. aipp_op {
2. input_para {
3. shape {
4. src_image_size_w: 480
5. src_image_size_h: 384
6. }
7. format: AYUV444_U8
8. }
9. crop_func {
10. switch: true
11. load_start_pos_w: 50
12. load_start_pos_h: 50
13. crop_size_w: 150
14. crop_size_h: 150
15. }
16. resize_func {
17. switch: true
18. resize_output_w: 182
19. resize_output_h: 182
20. }
21. padding_func {
22. switch: true
23. left_padding_size: 21
24. right_padding_size: 21
25. top_padding_size: 21
26. bottom_padding_size: 21
27. }
28. swap_func {
29. ax_swap_switch: true
30. }
31. csc_func {
32. switch: true
33. matrix_r0c0: 256
34. matrix_r0c1: 454
35. matrix_r0c2: 0
36. matrix_r1c0: 256
37. matrix_r1c1: -88
38. matrix_r1c2: -183
39. matrix_r2c0: 256
40. matrix_r2c1: 0
41. matrix_r2c2: 359
42. output_bias_0: 0
43. output_bias_1: 0
44. output_bias_2: 0
45. input_bias_0: 0
46. input_bias_1: 128
47. input_bias_2: 128
48. }
49. dtc_func {
50. switch: true
51. mean_chn_0: 4
52. mean_chn_1: 4
53. mean_chn_2: 4
54. min_chn_0: 2.0
55. min_chn_1: 2.0
56. min_chn_2: 2.0
57. var_reci_chn_0: 2.0
58. var_reci_chn_1: 2.0
59. var_reci_chn_2: 2.0
60. }
61. rotate_func {
62. switch: true
63. rotate_angle: 180.0
64. }
65. }
```

## 动静态混合配置示例

动静混合场景不支持配置rotate旋转参数，因为此时模型是动态的，动态场景暂不支持rotate旋转参数的配置。

```
1. aipp_op {
2. input_para {
3. shape {
4. src_image_size_w: 200
5. src_image_size_h: 200
6. }
7. format: ARGB8888_U8
8. }
9. crop_func {
10. switch: true
11. dynamic: true
12. crop_size_w: 100
13. crop_size_h: 100
14. }
15. resize_func {
16. switch: true
17. resize_output_w: 200
18. resize_output_h: 200
19. }
20. padding_func {
21. switch: true
22. right_padding_size: 24
23. bottom_padding_size: 24
24. }
25. swap_func {
26. rbuv_swap_switch: true
27. ax_swap_switch: true
28. }
29. dtc_func {
30. switch: true
31. mean_chn_0: 4
32. mean_chn_1: 4
33. mean_chn_2: 4
34. min_chn_0: 2.0
35. min_chn_1: 2.0
36. min_chn_2: 2.0
37. var_reci_chn_0: 2.0
38. var_reci_chn_1: 2.0
39. var_reci_chn_2: 2.0
40. }
41. }
```
